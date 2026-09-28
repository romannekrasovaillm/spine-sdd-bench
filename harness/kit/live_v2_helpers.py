"""Дополнения к run_live.py для v2: класс исхода гейта, SKIP-состав, счётчик срабатываний хука,
скан утечек, детерминированный выбор документа-решения. Только stdlib."""
import pathlib, re


def gate_class(det):
    """PASS без касания принятой архитектуры — не то же, что PASS через дельту."""
    if det.get("spine_gate_exit") != 0:
        return "FAIL"
    if det.get("delta_dirs"):
        return "PASS_DELTA"            # принятое решение изменено принятым способом
    if det.get("protected_touched"):
        return "PASS_UNEXPLAINED"      # не должно случаться; разобрать вручную
    return "PASS_UNTOUCHED"            # спайн не тронут: изменение живёт вне принятой архитектуры


def gate_skips(stdout):
    """Составляющие гейта, ушедшие в SKIP. Формат строки сверен на выводе arch-be 0.3.11."""
    return sorted(set(re.findall(r"\[SKIP\]\s+(\S+)", stdout)))


HOOK_MARK = "spine: гейт FAIL"


def hook_blocks(home):
    """Сколько раз Stop-хук вернул exit 2 (по журналам Qwen в HOME ячейки)."""
    n = 0
    for p in pathlib.Path(home).rglob("*"):
        if p.is_file() and p.suffix in (".jsonl", ".json", ".log", ".txt"):
            try:
                n += p.read_text(encoding="utf-8", errors="replace").count(HOOK_MARK)
            except OSError:
                pass
    return n


def contamination(home, ws, forbidden_roots, allow=()):
    """Обращения агента к путям вне своей ячейки: соседние кейсы, исходники spine-bank, другие ячейки.
    forbidden_roots — абсолютные пути; собственные ws/home и allow (например ~/bin) исключаются."""
    ws, home = str(pathlib.Path(ws).resolve()), str(pathlib.Path(home).resolve())
    roots = [str(pathlib.Path(r).resolve()) for r in forbidden_roots]
    allow = tuple(str(pathlib.Path(a).resolve()) for a in allow)
    hits = set()
    for p in pathlib.Path(home).rglob("*.jsonl"):
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"(/[^\s\"'`,)\]}]+)", text):
            path = m.group(1).rstrip(".:;")
            if path.startswith((ws, home) + allow):
                continue
            if any(path.startswith(r) for r in roots):
                hits.add(path)
    return sorted(hits)


# Документ-решение для adr_quality: правило фиксируется в пререгистрации v2 и одинаково для всех.
DECISION_RULES = [
    r"^docs/adr/ADR-(0(0[89]|[1-9]\d)|[1-9]\d{2})[^/]*\.md$",   # новый ADR (ADR-001..007 — принятые)
    r"(^|/)changes/[^/]+/(design|DECISION|ADR)[^/]*\.md$",
    r"(^|/)openspec/changes/[^/]+/design\.md$",
    r"(^|/)_bmad-output/.*architecture[^/]*\.md$",
    r"(^|/)docs/superpowers/specs/.*\.md$",
    r"(^|/)changes/[^/]+/DELTA\.md$",
    r"(^|/)docs/solutioning[^/]*\.md$",
]


def decision_doc(files):
    for rule in DECISION_RULES:
        cands = sorted(f for f in files if re.search(rule, f))
        if cands:
            return cands[0]
    return None


# Приоритет файлов досье (стек-агностичный); бюджет и потолок — как в v1, но зафиксированы заранее.
DOSSIER_PRIORITY = DECISION_RULES + [
    r"(^|/)changes/[^/]+/.*\.md$", r"(^|/)openspec/changes/.*\.md$", r"(^|/)_bmad-output/.*\.md$",
    r"(^|/)docs/nfr[^/]*\.md$", r"(^|/)docs/contracts/", r"^openapi/", r"(^|/)docs/spec/",
    r"^ARCHITECTURE-SPINE\.md$", r"^\.arch-handoff/CONSTRAINTS\.yaml$", r".*",
]


def dossier_order(files):
    seen, out = set(), []
    for rule in DOSSIER_PRIORITY:
        for f in sorted(files):
            if f not in seen and re.search(rule, f):
                seen.add(f); out.append(f)
    return out


def _ad_blocks(text):
    """{'AD-005': 'тело блока', ...} по заголовкам вида '## AD-005. …'."""
    parts = re.split(r"(?m)^##\s+(AD-\d{3})\b", text)
    return {parts[i]: re.sub(r"\s+", " ", parts[i + 1]).strip() for i in range(1, len(parts) - 1, 2)}


def modified_invariants(old_spine, new_spine):
    """F4: delta_guard файловый. Какие СУЩЕСТВУЮЩИЕ AD изменены/удалены, какие добавлены."""
    a, b = _ad_blocks(old_spine), _ad_blocks(new_spine)
    return {"modified": sorted(k for k in a if k in b and a[k] != b[k]),
            "removed": sorted(k for k in a if k not in b),
            "added": sorted(k for k in b if k not in a)}
