#!/usr/bin/env python3
"""bench.py — живой прогон Qwen Code × методические стеки на кейсе sbp-gateway.

Наработка Opus 5.5 (spine-qwen-bench-kit/kit) берётся как есть по содержанию:
то же задание (TASK.md), тот же кейс, те же условия установки стеков, тот же
детерминированный скоринг и та же слепая рубричная оценка. Отличие одно и
принципиальное: агент работает в ЖИВОМ TUI Qwen Code в tmux под ролью
solution-архитектора, а не в headless-режиме (`-o json`), и ход прогона
документируется скриншотами.

Команды:
  python3 bench.py setup                 — кейс + клон superpowers
  python3 bench.py install               — установить 5 условий в изолированные ws
  python3 bench.py run  [--parallel 2]   — живые TUI-прогоны (+ скриншоты)
  python3 bench.py score                 — детерминированный скоринг + слепой судья
  python3 bench.py report                — сводка results/live-summary.md
  python3 bench.py docx                  — финальный отчёт .docx
  python3 bench.py status                — состояние ячеек
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import random
import re
import shutil
import statistics
import subprocess
import sys
import threading
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
KIT = ROOT.parent / "spine-qwen-bench-kit" / "kit"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(KIT))

import envutil  # noqa: E402
import jl  # noqa: E402
import shots  # noqa: E402
from stacks import (PINS, BASE_TAG, FACTORIAL, base_env, git_commit, install,  # noqa: E402
                    inventory, parse_condition, sh, skill_names, verify_install)
from live_v2_helpers import (contamination, decision_doc as v2_decision_doc, dossier_order,  # noqa: E402
                             gate_class, gate_skips, hook_blocks, modified_invariants)
from common import BASE_OPENAPI  # noqa: E402

SPINE_BANK = Path(os.environ.get("SPINE_BANK", "~/spine-bank")).expanduser()
SUPERPOWERS_SRC = Path(os.environ.get("SUPERPOWERS_SRC", "~/superpowers-bench")).expanduser()

def _root(env: str, default: str) -> Path:
    v = os.environ.get(env)
    if not v:
        return ROOT / default
    p = Path(v)
    return p if p.is_absolute() else ROOT / p


RUNS = _root("BENCH_RUNS", "runs")
CASE = RUNS / "case"
CELLS = RUNS / "cells"
FRAMES = _root("BENCH_FRAMES", "frames")
RESULTS = _root("BENCH_RESULTS", "results")
LOGS = _root("BENCH_LOGS", "logs")
# Обезличенные имена рабочих каталогов: агент не должен видеть по пути, какой
# продукт в этом прогоне проверяется (иначе условие перестаёт быть слепым).
OPAQUE = os.environ.get("BENCH_OPAQUE", "0") == "1"
CELLMAP = RUNS / "cell-map.json"
REAL_HOME = pathlib.Path(os.path.expanduser("~"))   # до любых переопределений HOME

CONDS = os.environ.get("BENCH_CONDS", ",".join(FACTORIAL)).split(",")
REPS = int(os.environ.get("BENCH_REPS", "2"))
SOLVER_MODEL = os.environ.get("SOLVER_MODEL", "deepseek-flash")
JUDGE_MODEL = os.environ.get("JUDGE_MODEL", "glm-5.3")
JUDGE_ALIAS = "glm-judge"
RUBRICS = ["solution_architecture", "architecture_gates", "adr_quality", "macedo_dimensions",
           "neutral_architecture"]
# Рубрики скопированы из spine-bank в комплект: на время прогона клон spine-bank
# убирается из $HOME агента (руководство §4.7), чтобы исходники Spine были недоступны.
RUBRIC_PATHS = {rb: HERE.parent / "kit-rubrics" / f"{rb}.yaml" for rb in RUBRICS[:4]}
RUBRIC_PATHS["neutral_architecture"] = KIT / "rubrics" / "neutral_architecture.yaml"
VIEWER_SESSION = "viewer"
X11 = threading.Lock()
RUN_CONDS: list[str] = list(FACTORIAL)
RUN_REPS: int = 2

# Явная просьба архитектора к CALM (условие `calm-explicit`): измеряет потолок
# продукта, когда его действительно применяют по назначению.
PROMPT_EXTRA = {
    "calm-explicit": (
        "Дополнительно к этому: смоделируй архитектуру изменения на языке CALM "
        "(архитектура как код) — узлы, интерфейсы, связи, потоки и контроли — и "
        "провалидируй модель родным валидатором CALM. Модель должна лежать в "
        "репозитории рядом с остальными артефактами решения."
    ),
}

INSTALL_DIRS = (".qwen/", ".claude/", "_bmad/", "openspec/config.yaml",
                ".arch-handoff/connect-manifest.json", "node_modules/", ".bench/",
                "package.json", "package-lock.json", ".calm.json", "calm-prompts/")
PROTECTED = ["ARCHITECTURE-SPINE.md", ".arch-handoff/CONSTRAINTS.yaml"] + \
            [f"docs/adr/ADR-00{i}" for i in range(1, 8)]
NEUTRALIZE = [(r"(?i)open\s*spec", "SPEC-TOOL"), (r"(?i)\bbmad\w*", "METHOD"),
              (r"(?i)superpowers?", "SKILLS"), (r"(?i)\bspine\b(?!-)", "CORE"),
              (r"(?i)arch-be", "cli"), (r"_bmad-output", "output"),
              (r"(?i)\bopsx-\w+", "cmd"), (r"(?i)qwen", "agent"),
              # CALM — модель архитектуры как код (FINOS): судья не должен узнавать продукт
              (r"(?i)\bcalm\b", "MODEL-LANG"), (r"(?i)finos", "FOUNDATION"),
              (r"(?i)init-ai", "init"), (r"(?i)docify", "docs-gen"),
              (r"(?i)calm-cli", "cli-model"), (r"(?i)architecture-as-code", "modeling")]


def cell_dir(c: str, r: int) -> Path:
    if not OPAQUE:
        return CELLS / f"{c}-r{r}"
    CELLS.mkdir(parents=True, exist_ok=True)
    m = json.loads(CELLMAP.read_text(encoding="utf-8")) if CELLMAP.exists() else {}
    key = f"{c}-r{r}"
    if key not in m:
        m[key] = "w" + "".join(random.choice("abcdefghijkmnpqrstuvwxyz23456789") for _ in range(6))
        CELLMAP.write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8")
    return CELLS / m[key]


# ------------------------------------------------------------------ setup
def setup() -> None:
    for p in (RUNS, CELLS, FRAMES, RESULTS, LOGS):
        p.mkdir(parents=True, exist_ok=True)
    if not CASE.exists():
        shutil.copytree(SPINE_BANK / "кейсы" / "sbp-gateway", CASE, ignore=shutil.ignore_patterns(".git"))
        (CASE / "openapi").mkdir(exist_ok=True)
        (CASE / "openapi" / "tsp-api.yaml").write_text(BASE_OPENAPI, encoding="utf-8")
        print(f"кейс подготовлен: {CASE}")
    if not SUPERPOWERS_SRC.exists():
        subprocess.run(["git", "clone", "--depth", "1", "--branch", PINS["superpowers_ref"],
                        "https://github.com/obra/superpowers.git", str(SUPERPOWERS_SRC)], check=True)
    print(f"superpowers: {SUPERPOWERS_SRC}")


def do_install(conds: list[str] | None = None, reps: int | None = None) -> None:
    setup()
    for c in (conds or CONDS):
        for r in range(1, (reps or REPS) + 1):
            d = cell_dir(c, r)
            if (d / "base.json").exists():
                print(f"== {c} r{r}: уже установлено")
                continue
            print(f"== {c} r{r}: установка стека", flush=True)
            ws, home = install(c, str(CASE), str(d), str(SUPERPOWERS_SRC))
            inv = inventory(ws, home)
            problems = verify_install(c, inv, skill_names(ws, home))
            if problems:
                raise RuntimeError(f"{c}: установка некорректна: {problems}")
            base_sha = sh("git rev-parse HEAD", cwd=ws).stdout.strip()
            (d / "base.json").write_text(json.dumps({
                "condition": c, "rep": r, "base_sha": base_sha,
                "inventory": inventory(ws, home), "pins": PINS,
                "solver": SOLVER_MODEL, "judge": JUDGE_MODEL,
            }, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"   ок: {d}")


# ------------------------------------------------------------------ TUI-прогон
def write_panel(cell: Path, cond: str, rep: int, phase: str, detail: str, events: list[str]) -> None:
    total = len(RUN_CONDS) * RUN_REPS
    idx = (RUN_CONDS.index(cond) if cond in RUN_CONDS else 0) * RUN_REPS + rep
    body = [
        "┌─ SPINE-BENCH · живой TUI Qwen Code ─────────────┐",
        f"│ Условие : {cond:<12} повтор {rep}        │",
        f"│ Ячейка  : {idx}/{total}".ljust(51) + "│",
        f"│ Стадия  : {phase[:33]:<33}│",
        f"│ Решатель: {SOLVER_MODEL[:33]:<33}│",
        "├─────────────────────────────────────────────────┤",
        "│ РОЛЬ: solution-архитектор банка                 │",
        "│ КЕЙС: sbp-gateway · изменение «СБП-подписки»    │",
        "├─────────────────────────────────────────────────┤",
    ]
    for ln in (detail.split("\n") if detail else []):
        for k in range(0, max(len(ln), 1), 47):
            body.append("│ " + ln[k:k + 47].ljust(47) + "│")
    body.append("├─────────────────────────────────────────────────┤")
    body.append("│ ЛЕНТА СОБЫТИЙ                                   │")
    for e in events[-9:]:
        body.append("│ " + e[:47].ljust(47) + "│")
    body.append("└─────────────────────────────────────────────────┘")
    (cell / "panel.txt").write_text("\n".join(body) + "\n", encoding="utf-8")


def tmux(*args) -> subprocess.CompletedProcess:
    return subprocess.run(["tmux", *args], capture_output=True, text=True)


def start_tui(session: str, cell: Path) -> None:
    ws, home = str(cell / "ws"), str(cell / "home")
    env = envutil.solver_env()
    tmux("kill-session", "-t", session)
    args = ["new-session", "-d", "-s", session, "-x", "200", "-y", "50", "-c", ws,
            "-e", f"HOME={home}", "-e", f"OPENAI_API_KEY={env['OPENAI_API_KEY']}",
            "-e", f"OPENAI_BASE_URL={env['OPENAI_BASE_URL']}", "-e", "TERM=xterm-256color",
            "-e", f"PATH={ws}/node_modules/.bin:{base_env(home)['PATH']}",
            f"qwen --auth-type openai --openai-base-url {env['OPENAI_BASE_URL']} "
            f"-m {SOLVER_MODEL} --approval-mode yolo"]
    r = tmux(*args)
    if r.returncode != 0:
        raise RuntimeError(f"tmux new-session: {r.stderr}")
    tmux("set-option", "-t", session, "status", "off")
    tmux("set-option", "-t", session, "window-size", "latest")
    loop = (f"while :; do clear; cat {cell/'panel.txt'} 2>/dev/null; "
            f"echo; echo '--- tmux: Ctrl-b d — отключиться ---'; sleep 2; done")
    tmux("split-window", "-h", "-l", "52", "-t", f"{session}", loop)
    tmux("select-pane", "-t", f"{session}.0")


DIALOG = re.compile(r"(?i)довер|trust|одобр|approve|разреш|allow|mcp server|выбрать|select an option")


def wait_ready(session: str, timeout: float = 150.0, log=print) -> bool:
    """Ждёт готовности TUI, подтверждая стартовые диалоги (доверие, MCP, авторизация)."""
    t0 = time.time()
    prev, stable = None, 0
    answered = 0
    while time.time() - t0 < timeout:
        cur = shots.pane_text(session)
        if DIALOG.search(cur):
            answered += 1
            log(f"   TUI-диалог #{answered}: подтверждаю Enter")
            tmux("send-keys", "-t", f"{session}.0", "Enter")
            time.sleep(4)
            prev, stable = None, 0
            continue
        if cur.strip() and cur == prev:
            stable += 1
            if stable >= 2 and time.time() - t0 > 6:
                return True
        else:
            stable = 0
        prev = cur
        time.sleep(4)
    return False


def clear_input(session: str, presses: int = 200) -> None:
    for _ in range(presses):
        tmux("send-keys", "-t", f"{session}.0", "BSpace")
    time.sleep(0.3)


def send_prompt(session: str, prompt: str) -> None:
    tmux("send-keys", "-t", f"{session}.0", "-l", prompt)
    time.sleep(1.0)
    tmux("send-keys", "-t", f"{session}.0", "Enter")


# Признак ЖИВОГО гейта человека. Подсказки навигации («↑/↓: Navigate») остаются
# в истории кадра и после закрытия диалога, поэтому смотрим только низ кадра и
# только на строку ожидания: иначе повторные Enter уходили бы в пустой ввод и
# могли отправить подсказку автодополнения.
DIALOG_LIVE = "Ожидание подтверждения от пользователя"
DIALOG_TAIL = 14


def answer_dialog(session: str, state: dict, cooldown: float = 8.0) -> bool:
    """Ответить на интерактивный гейт Qwen (AskUserQuestion) вариантом по умолчанию."""
    if time.time() - state.get("last_dialog", 0.0) < cooldown:
        return False
    try:
        frame = shots.pane_text(session)
    except Exception:  # noqa: BLE001
        return False
    tail = "\n".join(frame.splitlines()[-DIALOG_TAIL:])
    if DIALOG_LIVE in tail:
        tmux("send-keys", "-t", f"{session}.0", "Enter")
        state["last_dialog"] = time.time()
        print(f"[bench] {session}: ответ на гейт человека (Recommended)", flush=True)
        return True
    return False


def viewer_switch(session: str) -> None:
    r = tmux("list-clients", "-F", "#{client_tty}")
    for tty in r.stdout.split():
        tmux("switch-client", "-c", tty, "-t", session)


def viewer_autostart(session: str) -> None:
    r = tmux("list-clients", "-F", "#{client_name}")
    if r.stdout.strip():
        return
    subprocess.Popen(["gnome-terminal", "--window", "--maximize", "--class=SpineBench",
                      "--", "tmux", "attach", "-t", session],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                     env={**os.environ, "DISPLAY": shots.DISPLAY})
    time.sleep(4)
    print(f"экран зрителя выведен: gnome-terminal → tmux attach -t {session}")


def run_cell(cond: str, rep: int, timeout: float, parallel_slot: int) -> dict:
    cell = cell_dir(cond, rep)
    if (cell / "meta.json").exists():
        return {"condition": cond, "rep": rep, "skipped": True}
    ws, home = str(cell / "ws"), str(cell / "home")
    session = f"b-{cond}-r{rep}"
    base = json.loads((cell / "base.json").read_text(encoding="utf-8"))
    base_sha = base["base_sha"]
    task = " ".join((KIT / "TASK.md").read_text(encoding="utf-8").split())
    # Условие `calm-explicit` — тот же стек и то же задание, но архитектор явно
    # просит смоделировать изменение в CALM: это измерение потолка продукта,
    # тогда как условие `calm` измеряет его добровольное принятие.
    extra = PROMPT_EXTRA.get(cond, "")
    if extra:
        task = task + " " + " ".join(extra.split())
    (cell / "prompt.txt").write_text(task, encoding="utf-8")
    events = ["TUI-сессия создаётся", f"решатель {SOLVER_MODEL}"]

    write_panel(cell, cond, rep, "запуск TUI", "Qwen Code стартует в изолированном HOME", events)
    start_tui(session, cell)
    if not wait_ready(session):
        events.append("TUI не подтвердил готовность — продолжаю")
    events.append("TUI готов, роль архитектора задана")
    write_panel(cell, cond, rep, "отправка задания", "TASK.md → архитектурный пакет", events)
    shots.pane_frame(session, FRAMES / "raw" / f"{cond}-r{rep}" / "00-start", "старт TUI")

    clear_input(session)
    send_prompt(session, task)
    t0 = time.time()
    events.append("задание отправлено, агент работает")

    state = {"last_frame": 0.0, "last_x11": 0.0, "phase": "работа агента",
             "last_dialog": 0.0, "dialogs": 0}

    def on_tick(total, pending, last_text, elapsed, started):
        now = time.time()
        events_local = events
        # Гейт человека: Qwen в режиме yolo всё равно останавливается на
        # `AskUserQuestion`. Роль архитектора отвечает вариантом «Recommended»,
        # и это фиксируется в ленте как видимое событие прогона.
        if answer_dialog(session, state):
            state["dialogs"] += 1
            events_local.append(f"гейт человека: ответ #{state['dialogs']} (Recommended)")
        if started and elapsed - state["last_frame"] > 90:
            state["last_frame"] = elapsed
            slug = f"{cond}-r{rep}-t{int(elapsed):05d}"
            shots.pane_frame(session, FRAMES / "raw" / f"{cond}-r{rep}" / slug,
                             f"{cond} r{rep} · {int(elapsed)}s · записей {total} · висящих {pending}")
            events_local.append(f"кадр t={int(elapsed)}s записей={total}")
        if started and elapsed - state["last_x11"] > 300:
            state["last_x11"] = elapsed
            with X11:
                viewer_switch(session)
                time.sleep(0.5)
                shots.x11_screenshot(FRAMES / "raw" / f"{cond}-r{rep}" / f"x11-t{int(elapsed):05d}.png")
            events_local.append(f"X11-скриншот t={int(elapsed)}s")
        write_panel(cell, cond, rep, state["phase"],
                    f"ход идёт {int(elapsed)}s\nзаписей журнала {total}\nвисящих вызовов {pending}",
                    events_local)

    viewer_autostart(session)
    # В хуковых ячейках после Stop-хука модель получает дополнительный ход. Детектор
    # конца хода обязан переждать таймаут хука (150 с) — иначе он остановится между
    # ходом и хуком (руководство v2, §4.2).
    quiet = 200.0 if parse_condition(cond)[1] == "spine-hook" else 45.0
    res = jl.wait_turn(home, ws, timeout=timeout, quiet=quiet, poll=5.0, on_tick=on_tick,
                       busy_fn=lambda: shots.agent_busy(session))
    wall = round(time.time() - t0, 1)
    dialogs = state.get("dialogs", 0)

    events.append(f"ход завершён за {int(wall)}s" if res["ok"] else f"таймаут {int(wall)}s")
    write_panel(cell, cond, rep, "ход завершён" if res["ok"] else "таймаут",
                "снимаю финальный кадр и коммичу работу", events)
    shots.pane_frame(session, FRAMES / "raw" / f"{cond}-r{rep}" / "99-end", "финальный кадр TUI")
    with X11:
        viewer_switch(session)
        time.sleep(0.5)
        shots.x11_screenshot(FRAMES / f"{cond}-r{rep}-final.png")

    jl.dump_markdown(home, ws, str(cell / "transcript.md"))
    calls = jl.tool_calls(home, ws)
    sh("git add -A", cwd=ws)
    changed = sh(f"git diff --cached --name-status {base_sha}", cwd=ws).stdout.splitlines()
    if changed:
        git_commit(ws, f"agent: {cond} r{rep}")
    (cell / "status.json").write_text(json.dumps(
        {"done": True, "wall_s": wall, "ok": res["ok"], "records": res["records"]},
        ensure_ascii=False, indent=2), encoding="utf-8")
    meta = {"condition": cond, "rep": rep, "mode": "tui", "session": session,
            "base_sha": base_sha, "wall_s": wall, "turn_ok": res["ok"],
            "records": res["records"], "solver": SOLVER_MODEL, "judge": JUDGE_MODEL,
            "inventory": base["inventory"], "pins": PINS,
            "tool_calls": len(calls),
            "tool_names": sorted({c["name"] for c in calls if c.get("name")}),
            "dialogs_answered": dialogs,
            "changed": changed}
    (cell / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    write_panel(cell, cond, rep, "готово", f"файлов изменено: {len(changed)}", events)
    print(f"== {cond} r{rep}: ход {'ок' if res['ok'] else 'ТАЙМАУТ'} за {wall}s, файлов {len(changed)}",
          flush=True)
    return meta


def do_run(parallel: int, timeout: float, conds: list[str], reps: int) -> None:
    setup()
    global RUN_CONDS, RUN_REPS
    RUN_CONDS, RUN_REPS = list(conds), reps
    slots = threading.Semaphore(parallel)
    lock = threading.Lock()
    errors: list[str] = []

    def worker(c: str, r: int, i: int) -> None:
        with slots:
            try:
                run_cell(c, r, timeout, i)
            except Exception as e:  # noqa: BLE001
                with lock:
                    errors.append(f"{c} r{r}: {e}")
                print(f"!! {c} r{r}: {e}", flush=True)

    threads = []
    for i, c in enumerate(conds):
        for r in range(1, reps + 1):
            t = threading.Thread(target=worker, args=(c, r, i), daemon=True)
            t.start()
            threads.append(t)
            time.sleep(2)
    for t in threads:
        t.join()
    if errors:
        print("ОШИБКИ:\n" + "\n".join(errors))


# ------------------------------------------------------------------ скоринг
def agent_files(ws: str, base_sha: str) -> list[str]:
    names = sh(f"git diff --name-only {base_sha} HEAD", cwd=ws).stdout.split()
    return [n for n in names if not n.startswith(INSTALL_DIRS)
            and n.endswith((".md", ".yaml", ".yml", ".json", ".txt"))]


def sensors(ws: str, files: list[str]) -> dict:
    text = "\n".join(Path(ws, f).read_text(encoding="utf-8", errors="replace")
                     for f in files if Path(ws, f).exists())
    has = lambda pat: bool(re.search(pat, text, re.I | re.M))  # noqa: E731
    return {
        "chars": len(text),
        "significance_route": has(r"значимост|significance|маршрут|\broute\b"),
        "invariant_AD005_ref": has(r"AD-005"),
        "alternatives": has(r"альтернатив|alternatives? considered|rejected option"),
        "negative_consequences": has(r"отрицательн|минус|издержк|\(−\)|trade-?off|negative consequence"),
        "reversibility": has(r"обратим|reversib"),
        "rollback": has(r"откат|rollback"),
        "acceptance": has(r"критери\w* приёмки|критери\w* приемки|acceptance criteria|####\s*Scenario|\bGiven\b.*\bWhen\b"),
        "nfr_numeric": has(r"p9[59]|\d+\s*(мс|ms|rps|tps|с\b)|\d+[,.]?\d*\s*%"),
        "human_decision": has(r"\bA3\b|решени\w* человека|human (architecture )?decision|на решение архитектор|требует решения"),
        "placeholders": len(re.findall(r"\bTBD\b|\bTODO\b|\?\?\?|<[^>\n]{3,40}>", text)),
        "adr_files": len([f for f in files if re.search(r"(?i)adr", f)]),
    }


def deterministic(ws: str, base_sha: str) -> dict:
    home = str(Path(ws).parent / "home")
    env = base_env(home)
    res: dict = {}
    base_ref = BASE_TAG if sh(f"git rev-parse --verify --quiet {BASE_TAG}", cwd=ws,
                              check=False).returncode == 0 else base_sha
    g = sh(f"arch-be gate --repo . --base {base_ref}", cwd=ws, env=env, check=False, timeout=900)
    res["spine_gate_exit"] = g.returncode
    res["spine_gate_route"] = (re.search(r"Маршрут: (\S+)", g.stdout) or [None, None])[1]
    res["spine_gate_fails"] = re.findall(r"\[FAIL\] (\S+)", g.stdout)
    res["spine_gate_tail"] = (g.stdout + g.stderr)[-1500:]
    res["spine_gate_base"] = base_ref
    res["spine_gate_skips"] = gate_skips(g.stdout + g.stderr)
    old_spine = sh(f"git show {base_sha}:ARCHITECTURE-SPINE.md", cwd=ws, check=False).stdout
    new_spine = Path(ws, "ARCHITECTURE-SPINE.md")
    if old_spine and new_spine.exists():
        res["invariants"] = modified_invariants(old_spine, new_spine.read_text(encoding="utf-8"))
    old = sh(f"git show {base_sha}:openapi/tsp-api.yaml", cwd=ws, check=False).stdout
    new = Path(ws, "openapi/tsp-api.yaml")
    if new.exists() and old and new.read_text(encoding="utf-8") != old:
        tmp = Path(ws).parent / "base_api.yaml"
        tmp.write_text(old, encoding="utf-8")
        cd = sh(f"arch-be contract-diff {tmp} openapi/tsp-api.yaml", cwd=ws, env=env, check=False)
        m = re.search(r"breaking: (\d+), non-breaking: (\d+)", cd.stdout)
        res["contract_changed"], res["contract_breaking"] = True, int(m[1]) if m else None
        res["contract_nonbreaking"] = int(m[2]) if m else None
        res["contract_tail"] = (cd.stdout + cd.stderr)[-1200:]
    else:
        res["contract_changed"] = False
    if Path(ws, "openspec").exists():
        ov = sh("openspec validate --all --strict --no-interactive", cwd=ws, env=env, check=False)
        res["openspec_validate_exit"] = ov.returncode
    touched = sh(f"git diff --name-only {base_sha} HEAD", cwd=ws).stdout.split()
    # Родной контроль CALM: схема + соответствие pattern, если агент их создал.
    # Если в репозитории есть карта «внешний URL → локальная схема» (`*mapping*.json`),
    # валидатор вызывается с ней — это штатный способ CALM работать с внешними
    # requirement-схемами, иначе он справедливо отказывается тянуть чужие хосты.
    calm_models = [t for t in touched if t.endswith(".json")
                   and re.search(r"(?i)architectur|pattern|calm", t)]
    if calm_models and Path(ws, "node_modules/.bin/calm").exists():
        arch = [t for t in calm_models if re.search(r"(?i)architectur", t)] or calm_models
        pat = [t for t in calm_models if re.search(r"(?i)pattern", t)]
        maps = [t for t in touched if t.endswith(".json") and re.search(r"(?i)mapping", t)]
        if not maps:
            maps = [str(p.relative_to(ws)) for p in sorted(Path(ws).rglob("*mapping*.json"))
                    if "node_modules" not in p.parts and ".git" not in p.parts]
        q = f"npx --no-install calm validate -a {arch[0]}"
        if pat:
            q += f" -p {pat[0]}"
        if maps:
            q += f" -u {maps[0]}"
        cv = sh(q, cwd=ws, env=env, check=False, timeout=600)
        res["calm_validate_exit"] = cv.returncode
        res["calm_validate_tail"] = (cv.stdout + cv.stderr)[-1500:]
        res["calm_arch"] = arch[0]
        res["calm_pattern"] = pat[0] if pat else None
        res["calm_mapping"] = maps[0] if maps else None
    res["protected_touched"] = [t for t in touched if any(t.startswith(p) for p in PROTECTED)]
    res["delta_dirs"] = sorted({t.split("/")[1] for t in touched
                                if t.startswith("changes/") and t.count("/") >= 2})
    return res


def judge_config() -> Path:
    cfg = RUNS / "judge.toml"
    cfg.write_text(
        f'default_model = "{JUDGE_ALIAS}"\n\n'
        f'[models."{JUDGE_ALIAS}"]\nbase_url = "http://localhost:8787/v1"\n'
        f'model = "{JUDGE_MODEL}"\napi_key_env = "ZHIPU_API_KEY"\n\n'
        f'[judge]\nsamples = {os.environ.get("JUDGE_SAMPLES", "3")}\nrecord_operator = false\n',
        encoding="utf-8")
    return cfg


DOSSIER_BUDGET = int(os.environ.get("DOSSIER_BUDGET", "23500"))
PER_FILE_CAP = int(os.environ.get("PER_FILE_CAP", "6200"))

# Приоритет файлов в досье: сначала решение, затем проект изменения, затем NFR,
# контракты, спеки, спайн. Внутри ранга — по пути. Правило одинаково для всех
# условий; всё, что не влезло в лимит, названо в шапке досье (тихое усечение
# запрещено механикой Spine, ADR-004).
PRIORITY = [
    r"(?i)adr[-_]?008|/adr/",
    r"(?i)design\.md|DELTA\.md|proposal\.md",
    r"(?i)solutioning",
    r"(?i)\bnfr\b|nfr\.",
    r"(?i)contracts?/|openapi/|architectures?/|\.arch\.json$|pattern|CALM",
    r"(?i)spec|state-machine|mandate",
    r"(?i)ARCHITECTURE-SPINE",
]


def _rank(f: str) -> int:
    for i, pat in enumerate(PRIORITY):
        if re.search(pat, f):
            return i
    return len(PRIORITY)


def _cap(text: str, limit: int) -> tuple[str, bool]:
    if len(text) <= limit:
        return text, False
    head = int(limit * 0.62)
    tail = int(limit * 0.34)
    skipped = len(text) - head - tail
    return (text[:head] + f"\n\n[... УСЕЧЕНО при подготовке досье: показаны начало и конец файла, "
            f"пропущено {skipped} символов ...]\n\n" + text[-tail:], True)


def build_dossier(ws: str, files: list[str], token: str, blind_dir: Path, kind: str,
                  budget: int = DOSSIER_BUDGET) -> tuple[Path, dict]:
    """Досье судьи: детерминированный бюджет символов, без тихого усечения.

    Механика Spine отказывается оценивать текст длиннее 24 000 символов и
    прямо советует оценивать документ по разделам. Здесь раздел один —
    «архитектурный пакет», и он собирается по фиксированному приоритету
    с явными пометками об усечении и об исключённых файлах.
    """
    ordered = dossier_order(files)
    # Бюджет содержимого меньше общего: шапка досье (списки включённых и исключённых
    # файлов) тоже считается лимитом рубрики — 24 000 символов. Без этого запаса
    # досье выходило 24 188 символов и механика его отклоняла.
    budget = budget - 700
    parts: list[str] = []
    used = 0
    included, omitted, truncated = [], [], []
    for f in ordered:
        p = Path(ws, f)
        if not p.exists():
            continue
        body = p.read_text(encoding="utf-8", errors="replace")
        name = f
        for pat, rep in NEUTRALIZE:
            body, name = re.sub(pat, rep, body), re.sub(pat, rep, name)
        left = budget - used
        if left < 800:
            omitted.append(name)
            continue
        body, was = _cap(body, min(PER_FILE_CAP, left))
        block = f"\n\n===== ФАЙЛ: {name} =====\n\n{body}"
        if len(block) > left:
            omitted.append(name)
            continue
        parts.append(block)
        used += len(block)
        included.append(name)
        if was:
            truncated.append(name)
    head = (f"# Архитектурный пакет изменения «Подписки СБП» (раздел досье: {kind})\n\n"
            f"Файлов в пакете: {len(ordered)}; включено в досье: {len(included)}; "
            f"объём досье: {used} символов (лимит рубрики 24000).\n"
            f"Исключены по бюджету (названы явно, не потеряны молча): "
            f"{', '.join(omitted) if omitted else '—'}.\n"
            f"Усечены по бюджету файла: {', '.join(truncated) if truncated else '—'}.\n")
    text = head + "".join(parts)
    SAFE = 23_900
    if len(text) > SAFE:                       # страховка: жёсткий предел рубрики 24 000
        text = text[:SAFE - 120] + f"\n\n[... ДОСЬЕ УСЕЧЕНО до {SAFE} символов ...]\n"
        truncated.append("(хвост досье)")
    d = blind_dir / f"dossier-{kind}-{token}.md"
    blind_dir.mkdir(parents=True, exist_ok=True)
    d.write_text(text, encoding="utf-8")
    return d, {"included": included, "omitted": omitted, "truncated": truncated,
               "chars": len(text)}


def decision_doc(ws: str, files: list[str]) -> list[str]:
    """Документ-решение для рубрики adr_quality: ADR, иначе проект изменения."""
    for rank in (0, 1, 2):
        cand = [f for f in files if _rank(f) == rank and Path(ws, f).exists()]
        if cand:
            return sorted(cand, key=lambda f: -Path(ws, f).stat().st_size)[:1]
    return []


def _parse_judge(p) -> dict:
    text = p.stdout + "\n" + p.stderr
    total = re.search(r"Взвешенный итог:\*\* ([\d.]+)/5", text)
    decision = re.search(r"Решение рубрики: \S+ \((\w+)\)", text)
    rep = re.search(r"Отчёт для гейта: (\S+\.json)", text)
    crit, flags, indep = {}, {}, None
    if rep and Path(rep.group(1)).exists():
        try:
            j = json.loads(Path(rep.group(1)).read_text())
            for s_ in j.get("scores", []):
                crit[s_.get("criterion_id")] = s_.get("score")
                if s_.get("flags"):
                    flags[s_.get("criterion_id")] = s_["flags"]
            indep = j.get("independence")
        except Exception:  # noqa: BLE001
            pass
    unjudged = text.count("судья не оценил")
    out = {"total": float(total.group(1)) if total else None,
           "decision": decision.group(1) if decision else None,
           "criteria": crit, "flags": flags, "independence": indep,
           "unjudged": unjudged, "exit": p.returncode, "raw": text[-4000:]}
    if unjudged:
        out["total"] = None
    return out


def _run_rubric(rb_key: str, dos: Path, cfg: Path, env: dict, attempts: int = 3) -> dict:
    path = RUBRIC_PATHS.get(rb_key) or (HERE / "rubrics" / f"{rb_key}.yaml")
    if not Path(path).exists():
        path = HERE / "rubrics" / f"{rb_key}.yaml"
    cmd = (f'arch-be --config {cfg} rubric run {path} {dos} --model {JUDGE_ALIAS} '
           f'--author-model {SOLVER_MODEL} --no-cache')
    res: dict = {"total": None}
    for i in range(attempts):
        p = sh(cmd, cwd=str(dos.parent), env=env, check=False, timeout=5400)
        res = _parse_judge(p)
        if res["total"] is not None:
            res["attempts"] = i + 1
            return res
        if i + 1 < attempts:
            print(f"   {rb_key}: судья не дал балла (попытка {i + 1}) — повтор", flush=True)
    res["attempts"] = attempts
    return res


def ensure_split_rubrics() -> dict[str, list[Path]]:
    """solution_architecture (15 критериев) не помещается в один ответ судьи.

    Рубрика на 15 критериев с якорями — 14.4 КБ промпта; вместе с досье 37 КБ
    судья (glm-5.2 и glm-5.3) не отдаёт валидный JSON даже после повтора.
    Решение: те же критерии и веса, но двумя вызовами (8 + 7), итог собирается
    взвешенным средним — это ровно тот же взвешенный итог полной рубрики.
    """
    import yaml  # noqa: PLC0415
    src = RUBRIC_PATHS["solution_architecture"]
    data = yaml.safe_load(src.read_text(encoding="utf-8"))
    crits = data["criteria"]
    out_dir = HERE / "rubrics"
    out_dir.mkdir(exist_ok=True)
    parts: dict[str, list[Path]] = {}
    halves = [("a", crits[:8]), ("b", crits[8:])]
    for suffix, sub in halves:
        d = dict(data)
        d["name"] = f"solution_architecture_part_{suffix}"
        d["description"] = (f"{data.get('description', '')} — раздел {suffix.upper()} "
                            f"(критерии {crits.index(sub[0]) + 1}–{crits.index(sub[-1]) + 1} из {len(crits)})")
        d["criteria"] = sub
        f = out_dir / f"solution_architecture_part_{suffix}.yaml"
        f.write_text(yaml.safe_dump(d, allow_unicode=True, sort_keys=False), encoding="utf-8")
        parts.setdefault("solution_architecture", []).append(f)
    return parts


SPLIT = ensure_split_rubrics()
WEIGHTS = {}


def _weights() -> dict[str, dict[str, float]]:
    import yaml  # noqa: PLC0415
    if not WEIGHTS:
        for rb in RUBRICS:
            f = RUBRIC_PATHS[rb]
            d = yaml.safe_load(Path(f).read_text(encoding="utf-8"))
            WEIGHTS[rb] = {c["id"]: float(c.get("weight", 1)) for c in d["criteria"]}
    return WEIGHTS


def judge_pack(dos: Path, cfg: Path, env: dict, rubrics: list[str] | None = None) -> dict:
    out: dict = {}
    w = _weights()
    for rb in (rubrics or RUBRICS):
        if rb in SPLIT:
            parts = {}
            crit, flags = {}, {}
            for f in SPLIT[rb]:
                key = f.stem
                res = _run_rubric(key, dos, cfg, env)
                parts[key] = {k: res[k] for k in ("total", "decision", "exit", "unjudged")}
                parts[key]["raw"] = res["raw"][-1200:]
                crit.update(res.get("criteria") or {})
                flags.update(res.get("flags") or {})
                print(f"   {rb}[{key}]: {res['total']} ({res['decision']})", flush=True)
            ws = w[rb]
            have = {k: v for k, v in crit.items() if isinstance(v, (int, float)) and k in ws}
            parts_ok = all(p.get("total") is not None for p in parts.values())
            total = (round(sum(ws[k] * v for k, v in have.items()) / max(sum(ws[k] for k in have), 1e-9), 2)
                     if have and parts_ok else None)
            decisions = {p["decision"] for p in parts.values() if p.get("decision")}
            out[rb] = {"total": total,
                       "decision": (decisions.pop() if len(decisions) == 1 else "mixed") if decisions else None,
                       "criteria": crit, "flags": flags, "independence": None,
                       "unjudged": sum(p["unjudged"] for p in parts.values()),
                       "exit": max(p["exit"] for p in parts.values()),
                       "parts": parts, "raw": json.dumps(parts, ensure_ascii=False)[-3000:]}
            print(f"   {rb}: {out[rb]['total']} (свод по частям)", flush=True)
            continue
        out[rb] = _run_rubric(rb, dos, cfg, env)
        if out[rb]["total"] is None:
            out[rb]["total"] = None
        print(f"   {rb}: {out[rb]['total']} ({out[rb]['decision']})", flush=True)
    return out


def do_score(conds: list[str], reps: int, parallel: int | None = None) -> None:
    parallel = parallel or int(os.environ.get("SCORE_PARALLEL", "10"))
    """Скоринг ячеек: детерминированный слой — один раз, судья — добирается до полноты.

    Ячейка считается готовой, только если ВСЕ рубрики получили балл: судья
    (LLM) периодически не отдаёт валидный JSON, и такие рубрики добираются
    повторами при следующих запусках.
    """
    cfg = judge_config()
    env = base_env(os.path.expanduser("~"))
    env.update(envutil.judge_key_env())
    blind_dir = RUNS / "judging"
    blind = blind_dir / "blind-map.json"
    bmap = json.loads(blind.read_text()) if blind.exists() else {}
    lock = threading.Lock()

    # Этапность судейства: ONLY_RUBRICS позволяет оценить сначала гипотезные рубрики,
    # затем добрать остальные тем же проходом (score идемпотентен).
    only = [r for r in os.environ.get("ONLY_RUBRICS", "").split(",") if r]
    rubrics_todo = only or RUBRICS

    def complete(sc: dict) -> bool:
        j = sc.get("judge") or {}
        return all((j.get(rb) or {}).get("total") is not None for rb in rubrics_todo)

    def one(c: str, r: int) -> None:
        d = cell_dir(c, r)
        if not (d / "meta.json").exists():
            return
        sf = d / "score.json"
        if sf.exists():
            sc = json.loads(sf.read_text(encoding="utf-8"))
            if complete(sc):
                return
            missing = [rb for rb in rubrics_todo if (sc.get("judge", {}).get(rb) or {}).get("total") is None]
        else:
            sc, missing = None, list(rubrics_todo)
        meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
        ws = str(d / "ws")
        files = agent_files(ws, meta["base_sha"])
        if sc is None:
            print(f"== {c} r{r}: файлов агента {len(files)}; скоринг", flush=True)
            sc = {"files": files, "sensors": sensors(ws, files),
                  "deterministic": deterministic(ws, meta["base_sha"])}
            # --- метрики v2 (руководство §5.2)
            sc["gate_class"] = gate_class(sc["deterministic"])
            sc["hook_blocks"] = hook_blocks(str(d / "home"))
            sc["contamination"] = contamination(
                str(d / "home"), ws,
                forbidden_roots=[SPINE_BANK, CELLS, CASE, REAL_HOME],
                allow=[REAL_HOME / "bin", REAL_HOME / ".npm-global", REAL_HOME / ".nvm"])
            sc["decision_doc"] = v2_decision_doc(files)
            sc["spine_visible"] = bool(sc["deterministic"]["delta_dirs"]) or any(
                f.startswith(("changes/", "docs/adr/")) for f in files)
        else:
            print(f"== {c} r{r}: досчёт {missing}", flush=True)
        if not files:
            sf.write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
            return
        if not sc.get("judge_token"):
            with lock:
                token = "%08x" % random.getrandbits(32)
                bmap[token] = f"{c}-r{r}"
                blind_dir.mkdir(parents=True, exist_ok=True)
                blind.write_text(json.dumps(bmap, indent=2))
            sc["judge_token"] = token
        token = sc["judge_token"]
        dos = blind_dir / f"dossier-package-{token}.md"
        if not dos.exists():
            dos, dmeta = build_dossier(ws, files, token, blind_dir, "package")
            sc["dossier"] = dmeta
        judge = sc.get("judge") or {}
        todo = [rb for rb in missing if rb != "adr_quality"]
        if todo:
            judge.update(judge_pack(dos, cfg, env, todo))
        if "adr_quality" in missing:
            dec = sc.get("decision_doc") or v2_decision_doc(files)
            ddec = blind_dir / f"dossier-decision-{token}.md"
            if not ddec.exists() and dec:
                ddec, ddmeta = build_dossier(ws, [dec] if isinstance(dec, str) else dec,
                                             token, blind_dir, "decision")
                sc["decision_doc"] = dec
                sc["dossier_decision"] = ddmeta
            if ddec.exists():
                judge.update(judge_pack(ddec, cfg, env, ["adr_quality"]))
        sc["judge"] = judge
        sc["judge_model"] = JUDGE_MODEL
        with lock:
            sf.write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"   {c} r{r}: сенсоры "
              f"{sum(1 for k, v in sc['sensors'].items() if isinstance(v, bool) and v)}/10; "
              f"гейт exit={sc['deterministic']['spine_gate_exit']}; "
              f"судья {({k: (v or {}).get('total') for k, v in judge.items()})}", flush=True)

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=parallel) as ex:
        list(ex.map(lambda cr: one(*cr), [(c, r) for c in conds for r in range(1, reps + 1)]))


# ------------------------------------------------------------------ сводка
def boot_ci(diffs, n=5000):
    if len(diffs) < 2:
        return None
    rnd = random.Random(7)
    means = sorted(statistics.mean(rnd.choice(diffs) for _ in diffs) for _ in range(n))
    return round(means[int(0.025 * n)], 2), round(means[int(0.975 * n)], 2)


def rows(conds: list[str], reps: int) -> list[dict]:
    out = []
    for c in conds:
        for r in range(1, reps + 1):
            d = cell_dir(c, r)
            if (d / "meta.json").exists() and (d / "score.json").exists():
                out.append({**json.loads((d / "meta.json").read_text(encoding="utf-8")),
                            **json.loads((d / "score.json").read_text(encoding="utf-8"))})
    return out


def mean(vals):
    v = [x for x in vals if isinstance(x, (int, float))]
    return round(statistics.mean(v), 2) if v else None


def do_report(conds: list[str], reps: int) -> None:
    rs = rows(conds, reps)
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "live.jsonl").write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in rs), encoding="utf-8")
    by: dict[str, list] = {}
    for x in rs:
        by.setdefault(x["condition"], []).append(x)
    lines = ["# Живой прогон в TUI Qwen Code: Qwen Code × методические стеки", "",
             f"Решатель: `{SOLVER_MODEL}`; судья: `{JUDGE_MODEL}`; повторов на условие: {reps}.", "",
             "| Условие | n | " + " | ".join(RUBRICS) + " | гейт Spine PASS | ломающих | защищённых | стена, с | сенсоры /10 |",
             "|---|---|" + "---|" * (len(RUBRICS) + 5)]
    for c in conds:
        xs = by.get(c, [])
        if not xs:
            continue
        j = [mean([x.get("judge", {}).get(rb, {}).get("total") for x in xs]) for rb in RUBRICS]
        gate = f"{sum(1 for x in xs if x['deterministic']['spine_gate_exit'] == 0)}/{len(xs)}"
        brk = mean([x["deterministic"].get("contract_breaking") for x in xs])
        prot = mean([len(x["deterministic"]["protected_touched"]) for x in xs])
        sens = mean([sum(1 for k, v in x["sensors"].items() if isinstance(v, bool) and v) for x in xs])
        lines.append(f"| {c} | {len(xs)} | " + " | ".join("—" if v is None else str(v) for v in j)
                     + f" | {gate} | {brk} | {prot} | {mean([x['wall_s'] for x in xs])} | {sens} |")
    if "plain" in by:
        lines += ["", "## Парные эффекты против голого Qwen Code (solution_architecture, bootstrap 95% CI)", ""]
        base = {x["rep"]: x.get("judge", {}).get("solution_architecture", {}).get("total")
                for x in by["plain"]}
        for c in conds:
            if c == "plain" or c not in by:
                continue
            diffs = [x.get("judge", {}).get("solution_architecture", {}).get("total") - base[x["rep"]]
                     for x in by[c] if isinstance(base.get(x["rep"]), float)
                     and isinstance(x.get("judge", {}).get("solution_architecture", {}).get("total"), float)]
            if diffs:
                lines.append(f"- {c} − plain = {round(statistics.mean(diffs), 2)} CI {boot_ci(diffs)} (n={len(diffs)})")
    lines += ["", "Сенсоры — эвристики наличия объектного минимума артефактов; это сигналы, не оценка качества.",
              "Итог рубрики с неоценёнными критериями отбрасывается (находка F7 комплекта)."]
    (RESULTS / "live-summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


def do_det(conds: list[str], reps: int) -> None:
    """Пересчитать только детерминированный слой (гейт, контракт, родной контроль CALM)."""
    for c in conds:
        for r in range(1, reps + 1):
            d = cell_dir(c, r)
            sf = d / "score.json"
            if not sf.exists():
                continue
            sc = json.loads(sf.read_text(encoding="utf-8"))
            meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
            sc["deterministic"] = deterministic(str(d / "ws"), meta["base_sha"])
            sf.write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"{c} r{r}: гейт={sc['deterministic']['spine_gate_exit']} "
                  f"calm_validate={sc['deterministic'].get('calm_validate_exit')}", flush=True)


def do_status(conds: list[str], reps: int) -> None:
    for c in conds:
        for r in range(1, reps + 1):
            d = cell_dir(c, r)
            st = "—"
            if (d / "meta.json").exists():
                m = json.loads((d / "meta.json").read_text(encoding="utf-8"))
                st = f"прогон ок={m['turn_ok']} {m['wall_s']}s файлов={len(m['changed'])}"
            if (d / "score.json").exists():
                s = json.loads((d / "score.json").read_text(encoding="utf-8"))
                j = {k: v["total"] for k, v in s.get("judge", {}).items()}
                st += f" | судья {j}"
            print(f"{c:<12} r{r}: {st}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["setup", "install", "run", "score", "det", "report", "docx", "status"])
    ap.add_argument("--parallel", type=int, default=2)
    ap.add_argument("--timeout", type=float, default=float(os.environ.get("BENCH_TIMEOUT", "5400")))
    ap.add_argument("--conditions", default=",".join(CONDS))
    ap.add_argument("--reps", type=int, default=REPS)
    a = ap.parse_args()
    conds = a.conditions.split(",")
    if a.cmd == "setup":
        setup()
    elif a.cmd == "install":
        do_install(conds, a.reps)
    elif a.cmd == "run":
        do_run(a.parallel, a.timeout, conds, a.reps)
    elif a.cmd == "score":
        do_score(conds, a.reps)
    elif a.cmd == "det":
        do_det(conds, a.reps)
    elif a.cmd == "report":
        do_report(conds, a.reps)
    elif a.cmd == "docx":
        import report_docx
        report_docx.build(conds, a.reps)
    elif a.cmd == "status":
        do_status(conds, a.reps)
    return 0


if __name__ == "__main__":
    sys.exit(main())
