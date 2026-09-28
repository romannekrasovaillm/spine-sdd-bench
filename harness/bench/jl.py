#!/usr/bin/env python3
"""jl.py — чтение JSONL-журнала сессии Qwen Code при изолированном HOME.

Отличие от tools/qwen_log.py навыка: HOME передаётся аргументом, а не берётся
из Path.home(). Это позволяет вести несколько параллельных прогонов в одном
процессе, у каждого — свой HOME (изоляция расширений и памяти Qwen).
"""
from __future__ import annotations

import json
import time
from pathlib import Path


def _projects(home: str) -> Path:
    return Path(home) / ".qwen" / "projects"


def newest_chat(home: str, cwd: str, since_mtime: float | None = None) -> Path | None:
    """Самый свежий .jsonl проекта, соответствующего cwd.

    Slug каталога проекта у Qwen не всегда равен cwd с заменой «/» на «-»
    (кириллица, «_», «.» схлопываются), поэтому основной путь — поиск по полю
    work_dir в *.runtime.json.
    """
    projects = _projects(home)
    if not projects.is_dir():
        return None
    target = str(Path(cwd).resolve())
    best: Path | None = None
    for rt in projects.glob("*/chats/*.runtime.json"):
        try:
            d = json.loads(rt.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        wd = str(d.get("work_dir") or "")
        if wd and str(Path(wd).resolve()) != target:
            continue
        chat = rt.with_name(rt.name.replace(".runtime.json", ".jsonl"))
        if chat.is_file() and (best is None or chat.stat().st_mtime > best.stat().st_mtime):
            best = chat
    if best is not None:
        return best
    # запасной путь — прямой slug
    slug = target.replace("/", "-")
    d = projects / slug / "chats"
    if d.is_dir():
        files = sorted(d.glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
        if files:
            return files[-1]
    return None


def analyse(chat: Path | None) -> tuple[int, int, bool]:
    """(всего записей, висящих functionCall, последняя запись — текст ассистента)."""
    if chat is None or not chat.is_file():
        return 0, 0, False
    calls: set[str] = set()
    answered: set[str] = set()
    total = 0
    last_is_text = False
    for raw in chat.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            d = json.loads(raw)
        except Exception:  # noqa: BLE001
            continue
        t = d.get("type")
        if t not in ("user", "assistant", "tool_result"):
            continue
        total += 1
        parts = (d.get("message") or {}).get("parts") or []
        has_text = False
        for p in parts:
            if not isinstance(p, dict):
                continue
            if "text" in p and str(p.get("text") or "").strip():
                has_text = True
            fc = p.get("functionCall")
            if fc and fc.get("id"):
                calls.add(fc["id"])
            fr = p.get("functionResponse")
            if fr and fr.get("id"):
                answered.add(fr["id"])
        if t == "assistant":
            last_is_text = has_text
    return total, len(calls - answered), last_is_text


def wait_turn(home: str, cwd: str, timeout: float, quiet: float = 20.0,
              poll: float = 4.0, on_tick=None, busy_fn=None) -> dict:
    """Ждёт конца хода агента по журналу И по кадру TUI.

    Конец хода: ход начался (журнал вырос), висящих functionCall нет, последняя
    запись — текст ассистента, журнал молчит `quiet` секунд И кадр TUI `quiet`
    секунд не показывает признаков работы (см. shots.agent_busy). Одного журнала
    мало: пока модель долго думает, он не растёт, и ход обрывался бы на 49-й
    секунде (наблюдено 2026-09-28 на условии plain).
    """
    t0 = time.time()
    chat = newest_chat(home, cwd)
    base = analyse(chat)[0] if chat else 0
    path0 = str(chat) if chat else None
    started = False
    last = (base, 0, False)
    quiet_since = time.time()
    busy_since = time.time()
    prev = -1
    while time.time() - t0 < timeout:
        chat = newest_chat(home, cwd)
        total, pending, last_text = analyse(chat)
        last = (total, pending, last_text)
        if chat is not None:
            if path0 is None or str(chat) != path0:
                path0, base, prev = str(chat), 0, -1
            if total > base:
                started = True
        if total != prev:
            prev = total
            quiet_since = time.time()
        if busy_fn is not None:
            try:
                if busy_fn():
                    busy_since = time.time()
            except Exception:  # noqa: BLE001
                pass
        if on_tick:
            on_tick(total, pending, last_text, time.time() - t0, started)
        quiet_for = time.time() - quiet_since
        frame_for = time.time() - busy_since
        if started and pending == 0 and last_text and quiet_for >= quiet and frame_for >= quiet:
            return {"ok": True, "elapsed": time.time() - t0, "records": total,
                    "pending": pending, "chat": str(chat) if chat else None,
                    "quiet_for": round(quiet_for), "frame_for": round(frame_for)}
        time.sleep(poll)
    return {"ok": False, "elapsed": time.time() - t0, "records": last[0],
            "pending": last[1], "chat": path0, "timeout": True,
            "quiet_for": round(time.time() - quiet_since),
            "frame_for": round(time.time() - busy_since)}


def dump_markdown(home: str, cwd: str, out_path: str | None = None, since: int = 0) -> str:
    """Читаемый Markdown-транскрипт сессии из JSONL (без захвата экрана)."""
    chat = newest_chat(home, cwd)
    if not chat:
        return ""
    lines: list[str] = [f"<!-- источник: {chat} -->", ""]
    idx = 0
    for raw in chat.read_text(encoding="utf-8", errors="replace").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            d = json.loads(raw)
        except Exception:  # noqa: BLE001
            continue
        t = d.get("type")
        parts = (d.get("message") or {}).get("parts") or []
        texts = [p.get("text") for p in parts if isinstance(p, dict) and p.get("text")]
        if t == "user":
            txt = "\n".join(x for x in texts if x and x.strip())
            if txt:
                idx += 1
                if idx > since:
                    lines.append(f"\n### ▶ Запрос оператора {idx}\n\n{txt}\n")
            for p in parts:
                fr = p.get("functionResponse") if isinstance(p, dict) else None
                if fr:
                    s = json.dumps(fr.get("response") or {}, ensure_ascii=False)
                    lines.append(f"  ↳ результат инструмента: {s[:400]}{'…' if len(s) > 400 else ''}\n")
        elif t == "assistant":
            for p in parts:
                fc = p.get("functionCall") if isinstance(p, dict) else None
                if fc:
                    args = fc.get("args") or {}
                    a = ", ".join(f"{k}={json.dumps(v, ensure_ascii=False)[:140]}"
                                  for k, v in list(args.items())[:3])
                    lines.append(f"  `{fc.get('name')}({a})`")
            txt = "\n".join(x for x in texts if x and x.strip())
            if txt.strip():
                lines.append(f"\n{txt.strip()}\n")
    text = "\n".join(lines)
    if out_path:
        Path(out_path).write_text(text, encoding="utf-8")
    return text


def tool_calls(home: str, cwd: str) -> list[dict]:
    """Список вызовов инструментов агента — для инвентаря «чем пользовался стек»."""
    chat = newest_chat(home, cwd)
    out: list[dict] = []
    if not chat:
        return out
    for raw in chat.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            d = json.loads(raw)
        except Exception:  # noqa: BLE001
            continue
        for p in (d.get("message") or {}).get("parts") or []:
            fc = p.get("functionCall") if isinstance(p, dict) else None
            if fc:
                out.append({"name": fc.get("name"), "args": fc.get("args") or {}})
    return out
