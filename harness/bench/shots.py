#!/usr/bin/env python3
"""shots.py — снятие кадров живой TUI-сессии и X11-скриншоты.

Два независимых источника доказательств:

1. `pane_frame` — точный кадр панели tmux (`capture-pane -e`, с цветом),
   сохраняется как .txt и .ansi; `render_ansi` превращает его в PNG.
   Это ровно то, что терминал показывал в этот момент.
2. `x11_screenshot` — настоящий снимок экрана X11 (окно зрителя с tmux,
   подключённым к живой сессии) через ffmpeg x11grab.

Ничего не «доигрывается»: если кадр пуст, PNG будет пустым.
"""
from __future__ import annotations

import re
import subprocess
import time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

DISPLAY = ":1"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

# Основная палитра xterm-256 (16 базовых + куб 6×6×6 + серые)
BASE16 = [
    (0, 0, 0), (205, 0, 0), (0, 205, 0), (205, 205, 0),
    (0, 0, 238), (205, 0, 205), (0, 205, 205), (229, 229, 229),
    (127, 127, 127), (255, 0, 0), (0, 255, 0), (255, 255, 0),
    (92, 92, 255), (255, 0, 255), (0, 255, 255), (255, 255, 255),
]


def _xterm256(n: int) -> tuple[int, int, int]:
    if n < 16:
        return BASE16[n]
    if n < 232:
        n -= 16
        r, g, b = n // 36, (n % 36) // 6, n % 6
        conv = lambda v: 0 if v == 0 else 55 + 40 * v  # noqa: E731
        return conv(r), conv(g), conv(b)
    v = 8 + 10 * (n - 232)
    return v, v, v


def tmux(*args, check: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(["tmux", *args], capture_output=True, text=True, check=check)


def pane_text(session: str) -> str:
    return tmux("capture-pane", "-p", "-t", session).stdout


def pane_ansi(session: str) -> str:
    return tmux("capture-pane", "-p", "-e", "-t", session).stdout


def _trim(text: str) -> str:
    lines = text.split("\n")
    while lines and lines[-1].strip() == "":
        lines.pop()
    while lines and lines[0].strip() == "":
        lines.pop(0)
    return "\n".join(lines) + "\n"


def pane_frame(session: str, out_base: Path, title: str = "") -> None:
    out_base.parent.mkdir(parents=True, exist_ok=True)
    out_base.with_suffix(".txt").write_text(_trim(pane_text(session)), encoding="utf-8")
    out_base.with_suffix(".ansi").write_text(_trim(pane_ansi(session)), encoding="utf-8")
    if title:
        out_base.with_suffix(".title").write_text(title, encoding="utf-8")


BUSY_MARKERS = ("esc to cancel", "Enter to steer")


def agent_busy(session: str) -> bool:
    """Работает ли агент прямо сейчас — по кадру TUI.

    Пока ход идёт, Qwen держит в кадре индикатор с секундомером
    («… 1m 14s · ↑ 3.8k tokens · esc to cancel») и подсказку «Enter to steer».
    В покое их нет. Одной тишины журнала мало: модель подолгу думает, не трогая
    журнал, и ход обрывался бы преждевременно.
    """
    try:
        frame = pane_text(session)
    except Exception:  # noqa: BLE001
        return False
    return any(m in frame for m in BUSY_MARKERS)


SGR = re.compile(r"\x1b\[([0-9;:]*)m")
OTHER_CSI = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")


def _parse_ansi_line(line: str, default_fg, default_bg):
    """→ [(char, fg, bg, bold)] с учётом SGR-последовательностей."""
    cells: list[tuple[str, tuple, tuple, bool]] = []
    fg, bg, bold = default_fg, default_bg, False
    i = 0
    while i < len(line):
        m = SGR.match(line, i)
        if m:
            params = [p for p in m.group(1).split(";") if p != ""] or ["0"]
            j = 0
            while j < len(params):
                try:
                    p = int(params[j])
                except ValueError:
                    j += 1
                    continue
                if p == 0:
                    fg, bg, bold = default_fg, default_bg, False
                elif p == 1:
                    bold = True
                elif p == 22:
                    bold = False
                elif p == 39:
                    fg = default_fg
                elif p == 49:
                    bg = default_bg
                elif 30 <= p <= 37:
                    fg = BASE16[p - 30]
                elif 90 <= p <= 97:
                    fg = BASE16[p - 90 + 8]
                elif 40 <= p <= 47:
                    bg = BASE16[p - 40]
                elif 100 <= p <= 107:
                    bg = BASE16[p - 100 + 8]
                elif p in (38, 48):
                    tgt_fg = p == 38
                    if j + 1 < len(params) and params[j + 1] == "5" and j + 2 < len(params):
                        col = _xterm256(int(params[j + 2]))
                        j += 2
                    elif j + 1 < len(params) and params[j + 1] == "2" and j + 4 < len(params):
                        col = (int(params[j + 2]), int(params[j + 3]), int(params[j + 4]))
                        j += 4
                    else:
                        col = None
                    if col is not None:
                        if tgt_fg:
                            fg = col
                        else:
                            bg = col
                j += 1
            i = m.end()
            continue
        m2 = OTHER_CSI.match(line, i)
        if m2:
            i = m2.end()
            continue
        ch = line[i]
        if ch == "\x1b":
            i += 1
            continue
        cells.append((ch, fg, bg, bold))
        i += 1
    return cells


def render_ansi(ansi_text: str, out_png: Path, font_size: int = 15,
                bg: tuple[int, int, int] = (12, 12, 14),
                title: str | None = None, header: str | None = None) -> Path:
    """Рендер кадра TUI (ANSI) в PNG — «скриншот» панели tmux."""
    try:
        font = ImageFont.truetype(FONT_PATH, font_size)
        font_b = ImageFont.truetype(FONT_BOLD, font_size)
    except OSError:
        font = font_b = ImageFont.load_default()

    mono = font.getbbox("M")
    cw = mono[2] - mono[0]
    ch_h = int(font_size * 1.35)
    lines = [ln.rstrip("\n") for ln in ansi_text.split("\n")]
    if lines and lines[-1] == "":
        lines.pop()
    cols = max((len(OTHER_CSI.sub("", SGR.sub("", ln))) for ln in lines), default=80)
    cols = max(cols, 80)
    rows = len(lines)

    head_h = int(ch_h + 12) if header else 0
    W = cw * cols + 24
    H = ch_h * rows + 24 + head_h
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)

    if header:
        d.rectangle([0, 0, W, head_h], fill=(28, 30, 38))
        d.text((12, 6), header, font=font_b, fill=(230, 232, 240))

    for r, line in enumerate(lines):
        x = 12
        y = 12 + head_h + r * ch_h
        for ch, fg, bgr, bold in _parse_ansi_line(line, (200, 202, 210), bg):
            if bgr != bg:
                d.rectangle([x, y, x + cw, y + ch_h], fill=bgr)
            if ch.strip():
                d.text((x, y), ch, font=font_b if bold else font, fill=fg)
            x += cw
    out_png.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_png)
    return out_png


ENV_X = {"DISPLAY": DISPLAY, "PATH": "/usr/bin:/bin:/usr/local/bin"}


def viewer_windows(pattern: str = "SpineBench") -> list[str]:
    for flag in ("--class", "--classname", "--name"):
        r = subprocess.run(["xdotool", "search", flag, pattern],
                           capture_output=True, text=True, env=ENV_X)
        wins = [w for w in r.stdout.split() if w]
        if wins:
            return wins
    return []


def x11_screenshot(out_png: Path, display: str = DISPLAY) -> Path:
    """Настоящий снимок экрана X11 (1920×1080)."""
    out_png.parent.mkdir(parents=True, exist_ok=True)
    env = {"DISPLAY": display, "PATH": "/usr/bin:/bin:/usr/local/bin"}
    wins = viewer_windows()
    if wins:
        subprocess.run(["xdotool", "windowactivate", "--sync", wins[-1]], env=env,
                       capture_output=True, text=True)
        time.sleep(1.2)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                    "-f", "x11grab", "-video_size", "1920x1080", "-i", f"{display}.0",
                    "-frames:v", "1", str(out_png)], env=env, capture_output=True, text=True)
    return out_png
