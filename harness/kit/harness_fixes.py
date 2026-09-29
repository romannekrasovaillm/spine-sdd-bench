"""harness_fixes.py — исправления харнесса v2 → v2.1 по итогам перепроверки.

Каждая функция закрывает конкретную находку ревью (номер П…). Только stdlib.

Отличие от ревью: П2 (файловая песочница) реализована на Docker, а не на bubblewrap.
Причина: в этой среде `kernel.apparmor_restrict_unprivileged_userns = 1`, из-за чего
bwrap не может создать uid-map («setting up uid map: Permission denied»), а прав на
изменение sysctl нет. Docker даёт более сильную изоляцию: контейнер видит только
смонтированные каталоги, реальный `$HOME` оператора в него не попадает.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import shlex

# ---------- П1. Инварианты: правильные границы AD-блока ------------------------------------------


def ad_blocks(text: str) -> dict[str, str]:
    """AD-блок заканчивается на следующем заголовке уровня 1–2 или на горизонтальной черте.

    Прежняя версия резала только по `## AD-…`, и последний блок (AD-008) поглощал
    `## Deferred` и `## Контракты и версии` — любая правка хвоста считалась изменением AD-008.
    """
    out: dict[str, str] = {}
    cur, buf = None, []
    for line in text.splitlines():
        m = re.match(r"^##\s+(AD-\d{3})\b", line)
        if m or re.match(r"^#{1,2}\s", line) or re.match(r"^---\s*$", line):
            if cur:
                out[cur] = re.sub(r"\s+", " ", " ".join(buf)).strip()
            cur, buf = (m.group(1), [line]) if m else (None, [])
            continue
        if cur:
            buf.append(line)
    if cur:
        out[cur] = re.sub(r"\s+", " ", " ".join(buf)).strip()
    return out


def modified_invariants(old_spine: str, new_spine: str) -> dict[str, list[str]]:
    a, b = ad_blocks(old_spine), ad_blocks(new_spine)
    return {"modified": sorted(k for k in a if k in b and a[k] != b[k]),
            "removed": sorted(k for k in a if k not in b),
            "added": sorted(k for k in b if k not in a)}


def declared_modified(ws: str, ads: list[str]) -> tuple[list[str], list[str]]:
    """Какие из изменённых AD объявлены в разделе MODIFIED дельт (`changes/*/DELTA.md`)."""
    body = ""
    for p in pathlib.Path(ws).glob("changes/*/DELTA.md"):
        t = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"#{2,3}\s*MODIFIED(.*?)(\n#{2,3}\s|\Z)", t, re.S)
        body += m.group(1) if m else ""
    dec = [a for a in ads if a in body]
    return dec, [a for a in ads if a not in dec]


# ---------- П3. Нейтральные следы установки ------------------------------------------------------

BASE_TAG = "accepted"                     # было 'bench-baseline' — выглядит как метка репозитория
COMMIT_CASE = "Принятое решение: импорт"
COMMIT_BASELINE = "Рабочее окружение"     # было 'baseline: условие {condition} установлено'


def hook_command(base_ref: str = BASE_TAG, log_path: str = "/var/log/archgate/hook.log") -> str:
    """Stop-хук: база от нейтральной метки, счётчик срабатываний в файле вне ws и HOME (П7).

    Маркер в stderr агенту по-прежнему виден — считать срабатывания по тексту больше не нужно.
    """
    return ('git add -A -N >/dev/null 2>&1; '
            f'out=$(arch-be gate --route auto --base {base_ref} 2>&1) || '
            f'{{ mkdir -p $(dirname {log_path}) 2>/dev/null; '
            f'echo "$(date -u +%FT%TZ) block" >> {log_path} 2>/dev/null; '
            'printf "%s\\n\\nгейт FAIL — исправьте находки error\\n" "$out" >&2; exit 2; }')


# ---------- П2. Файловая песочница (Docker) ------------------------------------------------------

AGENT_HOME = "/home/architect"
AGENT_WS = "/home/architect/project"
NODE_PREFIX = "/home/roman/.nvm/versions/node/v22.23.1"
NODE_IMAGE = "bench-agent:1"
QWEN_CLI = "/node/lib/node_modules/@qwen-code/qwen-code/cli.js"


def docker_argv(ws: str, home: str, token: str, spine: bool = False, arch_be: str | None = None,
                hook_log_dir: str | None = None, env: dict | None = None,
                node_prefix: str = NODE_PREFIX, image: str = NODE_IMAGE,
                net: bool = True, tty: bool = True) -> list[str]:
    """Команда запуска агента в контейнере.

    Агент видит только свой проект (ws), свой HOME и образ с node; реальный `$HOME`
    оператора, харнесс, spine-bank и соседние ячейки в контейнер не монтируются.
    `arch-be` монтируется ТОЛЬКО в ячейках со Spine.
    """
    uid = os.getuid()
    gid = os.getgid()
    a = ["docker", "run", "--rm", "-i"] + (["-t"] if tty else []) + \
        ["--name", f"bench-{token}" + ("" if tty else "-probe")]
    if net:
        a += ["--network", "bridge"]
    a += ["--user", f"{uid}:{gid}",
          "-v", f"{node_prefix}:/node:ro",
          "-v", f"{ws}:{AGENT_WS}",
          "-v", f"{home}:{AGENT_HOME}",
          "-w", AGENT_WS,
          "-e", f"HOME={AGENT_HOME}",
          "-e", "PATH=/node/bin:/usr/local/bin:/usr/bin:/bin",
          "-e", "CI=1",
          "-e", "NO_COLOR=",
          "-e", "TERM=xterm-256color"]
    if spine:
        if not arch_be:
            raise ValueError("ячейка со Spine без бинарника arch-be")
        a += ["-v", f"{arch_be}:/usr/local/bin/arch-be:ro"]
    if hook_log_dir:
        a += ["-v", f"{hook_log_dir}:/var/log/archgate"]
    for k, v in (env or {}).items():
        a += ["-e", f"{k}={v}"]
    a += [image, "/node/bin/node", QWEN_CLI]
    return a


def docker_shell(argv: list[str]) -> str:
    return " ".join(shlex.quote(x) for x in argv)


def probe_argv(ws: str, home: str, token: str, spine: bool, command: str,
               arch_be: str | None = None, node_prefix: str = NODE_PREFIX,
               image: str = NODE_IMAGE) -> list[str]:
    """Та же песочница, но вместо агента — проверочная команда (П6)."""
    a = docker_argv(ws, home, token, spine=spine, arch_be=arch_be, node_prefix=node_prefix,
                    image=image, tty=False)
    # отбрасываем хвост с node и CLI, подставляем sh -c
    return a[:-2] + ["/bin/sh", "-c", command]


# ---------- П6. Проверка доступности инструментов в сессии ---------------------------------------

PROBE_CMD = ("echo PROBE_HOME=$HOME; echo PROBE_PWD=$(pwd); echo PROBE_LS_HOME=$(ls /home | tr '\\n' ','); "
             "if command -v arch-be >/dev/null 2>&1; then echo PROBE_ARCH_BE=YES; else echo PROBE_ARCH_BE=NO; fi; "
             "echo PROBE_GIT=$(git -C . log --oneline 2>/dev/null | tr '\\n' '|'); "
             "echo PROBE_TAGS=$(git tag 2>/dev/null | tr '\\n' ','); "
             "echo PROBE_ENV_LEAK=$(env | grep -cE 'BENCH_|LIVE_|JUDGE_|SPINE_BANK')")


def probe_verdict(spine: bool, out: str) -> list[str]:
    """Явные маркеры вместо «отсутствия строки»: иначе ошибка docker читается как успех."""
    problems = []
    if "PROBE_HOME=/home/architect" not in out:
        problems.append("HOME агента не тот, что ожидался")
    if "PROBE_PWD=/home/architect/project" not in out:
        problems.append("рабочий каталог агента не тот, что ожидался")
    if "PROBE_LS_HOME=architect," not in out:
        problems.append("в /home видно больше, чем architect")
    if "PROBE_ENV_LEAK=0" not in out:
        problems.append("в окружении агента есть служебные переменные")
    has_arch = "PROBE_ARCH_BE=YES" in out
    if spine and not has_arch:
        problems.append("arch-be недоступен агенту в ячейке со Spine")
    if not spine and has_arch:
        problems.append("arch-be доступен в контроле — утечка")
    return problems


def session_saw_spine_tools(journal_text: str) -> bool:
    """После прогона: были ли инструменты Spine в сессии (по журналу Qwen)."""
    return bool(re.search(r"mcp__spine__|tool_search[^\n]{0,200}spine|\"spine\"\s*:\s*\{", journal_text))


# ---------- П2/П5. Классификатор обращений вне ячейки -------------------------------------------

ACCESS = {
    # «delta-spec» без контекста пути — это название раздела OpenSpec, а не обращение
    # к материалам Spine; поэтому токен ищется только в форме пути (уточнение к ревью).
    "spine_material": r"arch-harness|\.arch-ml|arch-be|spine-bank|SPINE_BANK|/delta-spec/|"
                      r"experiments/[^\s]*arch",
    "harness": r"<REPO>|bench-v2-guide|spine-sdd-bench|PREREGISTRATION|live_v2_helpers|"
               r"stacks\.py|run_live|report_v2",
    "cell_meta": r"cells/w[a-z0-9]{6}/(panel\.txt|base\.json|meta\.json|prompt\.txt)",
    "operator_home": r"<HOME>/(?!\.\.\./cells/)[^\s]*",
}


def classify_access(contamination: list[str], transcript: str = "") -> dict[str, int]:
    """Категории вместо «любой абсолютный путь»: шум regex (site-packages и т. п.) не засчитывается."""
    text = "\n".join(contamination) + "\n" + transcript
    return {k: len(re.findall(v, text)) for k, v in ACCESS.items()}


# ---------- П4. Проверка слепоты ------------------------------------------------------------------

BLIND_PROMPT = ("Перед вами архитектурный пакет изменения. Был ли при его подготовке использован "
                "специализированный инструмент архитектурного контроля (реестр правил, дельты, "
                "гейт)? Ответьте одним словом: ДА или НЕТ.\n\n--- ДОСЬЕ ---\n")


def blindness_balanced(answers: list[tuple[bool, bool]]) -> tuple[float | None, str]:
    """answers: [(есть Spine, судья сказал ДА)].

    Сбалансированная точность: постоянный ответ даёт ровно 0.5 независимо от состава выборки.
    """
    pos = [s for t, s in answers if t]
    neg = [s for t, s in answers if not t]
    if not pos or not neg:
        return None, "в выборке нет одного из классов — проверка неинформативна"
    tpr = sum(pos) / len(pos)
    tnr = sum(1 for s in neg if not s) / len(neg)
    bacc = (tpr + tnr) / 2
    const = len({s for _, s in answers}) == 1
    note = "судья отвечает одно и то же — различения нет" if const else ""
    return round(bacc, 3), note


def load_settings(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
