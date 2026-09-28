"""Установка методических стеков в Qwen Code — v2 (факторная сетка «стек × режим Spine»).

Каждое условие получает: копию живого кейса, собственный git, собственный HOME
(изоляция user-scope расширений Qwen Code) и зафиксированный baseline-коммит с
тегом `bench-baseline` (якорь для Stop-хука, находка F2).
Версии пиннингуются — входы эксперимента не должны дрейфовать между прогонами.

v2: условия комбинируются — `<стек>+spine` (советующий режим) и
`<стек>+spine-hook` (блокирующий Stop-хук). Старые имена `spine` и `spine-hook`
остаются алиасами `plain+spine` и `plain+spine-hook`.
"""
import json, os, pathlib, shutil, subprocess

PINS = {
    "qwen": "@qwen-code/qwen-code@0.24.6",
    "openspec": "@fission-ai/openspec@1.13.2",
    "bmad": "bmad-method@6.12.0",
    "superpowers_ref": "v6.4.2",          # git-тег obra/superpowers; см. SUPERPOWERS_REF
    "arch_be": "0.3.11",
    "calm": "@finos/calm-cli@1.60.1",     # FINOS Common Architecture Language Model
}

STACKS = ["plain", "openspec", "bmad", "superpowers", "calm", "calm-explicit"]
SPINE_MODES = ["", "spine", "spine-hook"]          # "" — без Spine
ALIASES = {"spine": "plain+spine", "spine-hook": "plain+spine-hook"}   # совместимость с v1
FACTORIAL = [f"{s}+{m}" if m else s
             for s in ["plain", "openspec", "bmad", "superpowers"] for m in SPINE_MODES]
CONDITIONS = FACTORIAL + ["calm", "calm-explicit"]
BASE_TAG = "bench-baseline"   # якорь для Stop-хука (см. F2)

# Референсный Stop-хук из вывода `arch-be connect qwen` (сам connect его в Qwen не пишет).
SPINE_STOP_HOOK = (
    'BASE=""; for a in origin/main main origin/master master; do '
    'if git rev-parse --verify --quiet "$a" >/dev/null 2>&1; then BASE=$(git merge-base "$a" HEAD 2>/dev/null || true); break; fi; done; '
    'if [ -n "$BASE" ]; then out=$(arch-be gate --route auto --base "$BASE" 2>&1) || { printf "%s\\n\\nspine: гейт FAIL — исправьте находки error\\n" "$out" >&2; exit 2; }; '
    'else out=$(arch-be gate --route auto 2>&1) || { printf "%s\\n\\nspine: гейт FAIL\\n" "$out" >&2; exit 2; }; fi'
)

# Исправленный хук v2: база — тег baseline, а не merge-base (F2: merge-base = HEAD при
# незакоммиченной работе → score 0). `git add -A -N` делает новые файлы видимыми в диффе,
# не индексируя их содержимое. Отклонение от референса connect — объявлено в DEVIATIONS.
SPINE_STOP_HOOK_V2 = (
    'git add -A -N >/dev/null 2>&1; '
    f'out=$(arch-be gate --route auto --base {BASE_TAG} 2>&1) || '
    '{ printf "%s\\n\\nspine: гейт FAIL — исправьте находки error\\n" "$out" >&2; exit 2; }'
)


def parse_condition(condition):
    """'bmad+spine-hook' -> ('bmad', 'spine-hook'); 'spine' -> ('plain', 'spine')."""
    cond = ALIASES.get(condition, condition)
    stack, _, spine = cond.partition("+")
    if stack not in STACKS or spine not in SPINE_MODES:
        raise ValueError(f"неизвестное условие: {condition}")
    return stack, spine


def sh(cmd, cwd=None, env=None, check=True, timeout=600, input_text=None):
    p = subprocess.run(cmd, cwd=cwd, env=env, shell=True, capture_output=True, text=True,
                       timeout=timeout, input=input_text)
    if check and p.returncode != 0:
        raise RuntimeError(f"[{cmd}] exit={p.returncode}\n{p.stdout[-2000:]}\n{p.stderr[-2000:]}")
    return p


def git_commit(root, msg):
    sh("git add -A && git -c user.email=bench@local -c user.name=bench commit -q --allow-empty -m "
       + json.dumps(msg, ensure_ascii=False), cwd=root)


def base_env(home):
    env = dict(os.environ)
    env["HOME"] = home
    # ~/.local/bin добавлен явно: там лежит бинарник arch-be, а у фоновых процессов
    # PATH может быть урезан (отклонение, объявлено в DEVIATIONS пререгистрации v2).
    env["PATH"] = ":".join([os.path.expanduser("~/.local/bin"), os.path.expanduser("~/bin"),
                            os.path.expanduser("~/.npm-global/bin")]) + ":" + env["PATH"]
    env["NO_COLOR"] = "1"
    return env


def _install_stack(stack, ws, env, superpowers_src):
    if stack == "openspec":
        sh("openspec init --tools qwen --no-animation --language ru .", cwd=ws, env=env)
    elif stack == "bmad":
        sh(f"npx -y {PINS['bmad']} install --directory . --modules bmm --tools qwen --yes "
           "--communication-language Russian --document-output-language Russian", cwd=ws, env=env, timeout=900)
    elif stack == "superpowers":
        # Установщик спрашивает плагин из marketplace — подтверждаем Enter через псевдотерминал.
        sh(f"printf '\\n' | script -qc 'qwen extensions install {superpowers_src} --consent' /dev/null",
           cwd=ws, env=env, timeout=300)
        out = sh("qwen extensions list", cwd=ws, env=env).stdout
        if "superpowers" not in out:
            raise RuntimeError("superpowers не установился:\n" + out)
    elif stack in ("calm", "calm-explicit"):
        # CALM: CLI + его родной AI-набор. Провайдера `qwen` у `calm init-ai` нет
        # (только copilot | kiro | claude | codex), поэтому берём ближайший
        # supported-путь (claude) и переносим тот же скилл туда, где его видит
        # Qwen Code — в .qwen/skills/. Ничего не дописываем от себя.
        sh(f"npm i --no-save --no-package-lock {PINS['calm']}", cwd=ws, env=env, timeout=1800)
        sh("npx calm init-ai --provider claude --directory .", cwd=ws, env=env, timeout=900)
        src = pathlib.Path(ws, ".claude/skills/calm")
        if not src.is_dir():
            raise RuntimeError("calm init-ai не создал .claude/skills/calm")
        dst = pathlib.Path(ws, ".qwen/skills/calm")
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    elif stack != "plain":
        raise ValueError(stack)


def _merge_settings(ws, incoming):
    """Слить incoming в .qwen/settings.json, не затирая чужие ключи (MCP стека и пр.)."""
    s = pathlib.Path(ws, ".qwen/settings.json")
    s.parent.mkdir(parents=True, exist_ok=True)
    cfg = json.loads(s.read_text()) if s.exists() else {}
    for k, v in incoming.items():
        if k not in cfg:
            cfg[k] = v
        elif isinstance(v, dict) and isinstance(cfg[k], dict):
            for kk, vv in v.items():
                cfg[k].setdefault(kk, vv)
    s.write_text(json.dumps(cfg, ensure_ascii=False, indent=2))
    return cfg


def _add_stop_hook(ws, hook=SPINE_STOP_HOOK_V2):
    cfg = _merge_settings(ws, {})
    stops = cfg.setdefault("hooks", {}).setdefault("Stop", [])
    if not any(hook in json.dumps(x, ensure_ascii=False) for x in stops):
        stops.append({"hooks": [{"type": "command", "command": hook, "timeout": 150}]})
    pathlib.Path(ws, ".qwen/settings.json").write_text(
        json.dumps(cfg, ensure_ascii=False, indent=2))


def _install_spine(ws, env):
    """Spine до стека: `connect` НЕ раскладывает скиллы, если `.qwen/skills` уже есть (F9)."""
    sh("arch-be connect qwen", cwd=ws, env=env)
    s = pathlib.Path(ws, ".qwen/settings.json")
    return json.loads(s.read_text()) if s.exists() else {}


def install(condition, case_dir, dest, superpowers_src):
    """Создать рабочее пространство условия. Возвращает (workspace, home).

    Отклонение от руководства v2 (DEVIATIONS, находка F9): Spine ставится ПЕРВЫМ,
    потому что `arch-be connect qwen` отказывается раскладывать свои скиллы в уже
    существующий `.qwen/skills` («чужую библиотеку не перетираем»). При обратном
    порядке комбинированные ячейки с openspec и bmad теряли 66 скиллов Spine.
    """
    stack, spine = parse_condition(condition)
    ws, home = os.path.join(dest, "ws"), os.path.join(dest, "home")
    shutil.rmtree(dest, ignore_errors=True)
    shutil.copytree(case_dir, ws, ignore=shutil.ignore_patterns(".git"))
    os.makedirs(home)
    sh("git init -q && git checkout -q -b main", cwd=ws)
    git_commit(ws, "case: исходный кейс")
    env = base_env(home)
    spine_cfg = {}
    if spine:
        spine_cfg = _install_spine(ws, env)
    _install_stack(stack, ws, env, superpowers_src)
    if spine:
        # стек мог переписать settings.json — возвращаем MCP Spine и ставим хук
        keep = {k: v for k, v in spine_cfg.items() if k in ("mcpServers",)}
        _merge_settings(ws, keep)
        if spine == "spine-hook":
            _add_stop_hook(ws)
    git_commit(ws, f"baseline: условие {condition} установлено")
    sh(f"git tag -f {BASE_TAG}", cwd=ws)
    return ws, home


def skill_names(ws, home):
    q, ext = pathlib.Path(ws, ".qwen/skills"), pathlib.Path(home, ".qwen/extensions")
    names = [p.name for p in q.glob("*")] if q.exists() else []
    if ext.exists():
        names += [p.name for e in ext.glob("*") for p in (e / "skills").glob("*") if (e / "skills").exists()]
    return names


# Минимумы из одиночного прогона (отчёт v1, раздел 2.1). Сверять, а не угадывать.
EXPECTED = {"spine": {"project_skills": 66, "mcp": "spine"}, "openspec": {"project_skills": 6, "commands": 6},
            "bmad": {"project_skills": 29}, "superpowers": {"extension_skills": 15}}


def verify_install(condition, inv, names):
    """Комбинированное условие = сумма одиночных. Иначе установка сломала соседа."""
    stack, spine = parse_condition(condition)
    parts = [p for p in (stack, "spine" if spine else "") if p in EXPECTED]
    need = {"project_skills": 0, "extension_skills": 0, "commands": 0}
    for p in parts:
        for k, v in EXPECTED[p].items():
            if k in need:
                need[k] += v
    problems = [f"{k}: {inv.get(k, 0)} < {v}" for k, v in need.items() if inv.get(k, 0) < v]
    if spine and "spine" not in inv.get("mcp_servers", []):
        problems.append("нет MCP spine")
    if spine == "spine-hook" and "Stop" not in inv.get("hooks", []):
        problems.append("нет Stop-хука")
    dup = sorted({n for n in names if names.count(n) > 1})
    if dup:
        problems.append("коллизии имён скиллов: " + ", ".join(dup))
    return problems


def inventory(ws, home):
    """Что стек реально добавил в хост: скиллы, команды, MCP, хуки."""
    q = pathlib.Path(ws, ".qwen")
    ext = pathlib.Path(home, ".qwen/extensions")
    settings = {}
    if (q / "settings.json").exists():
        settings = json.loads((q / "settings.json").read_text())
    ext_skills = sum(len(list((e / "skills").glob("*"))) for e in ext.glob("*") if (e / "skills").exists()) if ext.exists() else 0
    return {
        "project_skills": len(list((q / "skills").glob("*"))) if (q / "skills").exists() else 0,
        "extension_skills": ext_skills,
        "commands": len(list((q / "commands").rglob("*.md"))) if (q / "commands").exists() else 0,
        "mcp_servers": sorted(settings.get("mcpServers", {}).keys()),
        "hooks": sorted(settings.get("hooks", {}).keys()),
    }
