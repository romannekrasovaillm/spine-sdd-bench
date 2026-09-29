#!/usr/bin/env python3
"""Перепроверка ключевых утверждений v2 по сырым данным репозитория spine-sdd-bench.
Запуск: python3 recheck_v2.py <корень репозитория>  → печатает markdown. Только stdlib."""
import collections, json, pathlib, re, statistics as st, sys
import math


def fisher_exact(a_yes, a_n, b_yes, b_n):
    """Двусторонний точный тест Фишера без округления."""
    col1, n = a_yes + b_yes, a_n + b_n
    p = lambda x: math.comb(col1, x) * math.comb(n - col1, a_n - x) / math.comb(n, a_n)
    po = p(a_yes)
    return min(1.0, sum(p(x) for x in range(max(0, a_n - (n - col1)), min(a_n, col1) + 1) if p(x) <= po * (1 + 1e-9)))

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
RUNS = ROOT / "results" / "runs" / "v2"
MODES = ["", "spine", "spine-hook"]
STACKS = ["plain", "openspec", "bmad", "superpowers"]

# Материалы процесса Spine вне ячейки: бинарник, конфиги и скиллы оператора, харнесс и руководства.
SPINE_MATERIAL = re.compile(r"arch-harness|\.arch-ml|arch-be|spine-bank|SPINE_BANK|<REPO>|experiments/|delta-spec|/\.claude/|detection-summary|Загрузки")
HARNESS_TEXT = re.compile(r"bench-v2-guide|spine-sdd-bench|PREREGISTRATION|live_v2_helpers|stacks\.py|run_live|report_v2|panel\.txt|base\.json")
COMMIT_LEAK = re.compile(r"условие [a-z+\-]+ установлено")
BENCH_WORD = re.compile(r"benchmark|бенчмарк", re.I)
CELL_META = re.compile(r"cells/w[a-z0-9]{6}/(panel\.txt|base\.json|meta\.json|prompt\.txt)")


def load():
    rows = [json.loads(l) for l in (ROOT / "results/v2/live.jsonl").open(encoding="utf-8", errors="replace") if l.strip()]
    for r in rows:
        stack, _, mode = r["condition"].partition("+")
        r["stack"], r["mode"] = stack, mode
        r["dir"] = RUNS / f"{r['condition']}-r{r['rep']}"
        r["transcript"] = (r["dir"] / "transcript.md").read_text(encoding="utf-8", errors="replace")
    return rows


def ad_blocks(text):
    """AD-блок заканчивается на следующем заголовке уровня 1–2 или на горизонтальной черте."""
    out, cur, buf = {}, None, []
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


def modified(base, new):
    a, b = ad_blocks(base), ad_blocks(new)
    return sorted(k for k in a if k in b and a[k] != b[k]), sorted(k for k in a if k not in b)


def declared_in_delta(run_dir, ads):
    """Объявлены ли изменённые AD в разделе MODIFIED какого-либо DELTA.md прогона."""
    txt = " ".join(p.read_text(encoding="utf-8", errors="replace") for p in run_dir.glob("artifacts/changes/*/DELTA.md"))
    sec = re.search(r"#{2,3}\s*MODIFIED(.*?)(\n#{2,3}\s|\Z)", txt, re.S)
    body = sec.group(1) if sec else ""
    return all(a in body for a in ads) if ads else None


def main():
    rows = load()
    base_spine = (RUNS / "openspec-r3/artifacts/ARCHITECTURE-SPINE.md").read_text(encoding="utf-8")  # PASS_UNTOUCHED, спайн не тронут
    L = []
    k = lambda xs, cls: sum(r["gate_class"] == cls for r in xs)

    # 1. Классы гейта по режиму
    L += ["### Классы гейта по режиму Spine", "", "| режим | n | PASS_DELTA | PASS_UNTOUCHED | FAIL |", "|---|---|---|---|---|"]
    for m in MODES:
        xs = [r for r in rows if r["mode"] == m]
        L.append(f"| {m or 'без Spine'} | {len(xs)} | {k(xs,'PASS_DELTA')} | {k(xs,'PASS_UNTOUCHED')} | {k(xs,'FAIL')} |")
    sp = [r for r in rows if r["mode"]]
    no = [r for r in rows if not r["mode"]]

    # 2. Загрязнение контроля
    for r in rows:
        r["spine_material"] = sum(1 for c in r["contamination"] if SPINE_MATERIAL.search(c))
        r["ran_arch_be"] = len(re.findall(r"arch-be\s+(gate|delta|lint|connect|check|rubric|--help|help|--version)", r["transcript"]))
        r["read_harness"] = len(HARNESS_TEXT.findall(r["transcript"]))
        r["saw_commit"] = len(COMMIT_LEAK.findall(r["transcript"]))
        r["bench_words"] = len(BENCH_WORD.findall(r["transcript"]))
        r["cell_meta"] = len(CELL_META.findall(r["transcript"]))
    dirty = [r for r in no if r["spine_material"]]
    clean = [r for r in no if not r["spine_material"]]
    L += ["", "### Контроль «без Spine»: чистые и загрязнённые прогоны", "",
          "| прогон | класс гейта | обращений к материалам Spine | запусков arch-be | упоминаний харнесса | мета-файлы ячейки |", "|---|---|---|---|---|---|"]
    for r in sorted(no, key=lambda r: (r["stack"], r["rep"])):
        L.append(f"| {r['condition']} r{r['rep']} | {r['gate_class']} | {r['spine_material']} | {r['ran_arch_be']} | {r['read_harness']} | {r['cell_meta']} |")
    sd, sn = k(sp, "PASS_DELTA"), len(sp)
    L += ["", f"- загрязнённые без Spine: PASS_DELTA {k(dirty,'PASS_DELTA')}/{len(dirty)}; чистые без Spine: {k(clean,'PASS_DELTA')}/{len(clean)}"
          f" → Фишер p = {fisher_exact(k(dirty,'PASS_DELTA'), len(dirty), k(clean,'PASS_DELTA'), len(clean)):.4f}",
          f"- со Spine {sd}/{sn} против всех без Spine {k(no,'PASS_DELTA')}/{len(no)} → p = {fisher_exact(sd, sn, k(no,'PASS_DELTA'), len(no)):.4f} (как в README)",
          f"- со Spine {sd}/{sn} против чистых без Spine {k(clean,'PASS_DELTA')}/{len(clean)} → p = {fisher_exact(sd, sn, k(clean,'PASS_DELTA'), len(clean)):.1e}"]
    for m in ("spine", "spine-hook"):
        xs = [r for r in rows if r["mode"] == m]
        L.append(f"- {m}: {k(xs,'PASS_DELTA')}/{len(xs)} против без Spine {k(no,'PASS_DELTA')}/{len(no)} → p = {fisher_exact(k(xs,'PASS_DELTA'), len(xs), k(no,'PASS_DELTA'), len(no)):.4f}; "
                 f"против чистых {k(clean,'PASS_DELTA')}/{len(clean)} → p = {fisher_exact(k(xs,'PASS_DELTA'), len(xs), k(clean,'PASS_DELTA'), len(clean)):.4f}")

    # 3. Каналы утечки
    ch = collections.Counter()
    for r in rows:
        ch["видели сообщение baseline-коммита с именем условия"] += r["saw_commit"] > 0
        ch["рассуждали о бенчмарке"] += r["bench_words"] > 0
        ch["обращались к материалам Spine вне ячейки"] += r["spine_material"] > 0
        ch["упоминали файлы харнесса/руководства"] += r["read_harness"] > 0
        ch["открывали panel.txt/base.json/prompt.txt своей ячейки (там имя условия)"] += r["cell_meta"] > 0
    L += ["", "### Каналы утечки (из 36 прогонов)", "", "| канал | прогонов |", "|---|---|"] + [f"| {a} | {b} |" for a, b in ch.items()]

    # 4. Инварианты
    L += ["", "### Изменения существующих AD-001…AD-008 (исправленный подсчёт)", "",
          "| прогон | класс гейта | было в score.json | на самом деле изменены | объявлены в MODIFIED |", "|---|---|---|---|---|"]
    real = []
    for r in sorted(rows, key=lambda r: (r["condition"], r["rep"])):
        p = r["dir"] / "artifacts/ARCHITECTURE-SPINE.md"
        mod, rm = modified(base_spine, p.read_text(encoding="utf-8")) if p.exists() else ([], [])
        old = (r["deterministic"].get("invariants") or {}).get("modified") or []
        if old or mod:
            dec = declared_in_delta(r["dir"], mod)
            L.append(f"| {r['condition']} r{r['rep']} | {r['gate_class']} | {', '.join(old) or '—'} | {', '.join(mod + rm) or '—'} | {'—' if dec is None else ('да' if dec else 'нет')} |")
        r["real_mod"] = mod + rm
    pd = [r for r in rows if r["gate_class"] == "PASS_DELTA"]
    old_n = sum(1 for r in pd if (r["deterministic"].get("invariants") or {}).get("modified"))
    new_n = sum(1 for r in pd if r["real_mod"])
    L += ["", f"- PASS_DELTA с изменёнными AD: было {old_n}/{len(pd)}, на самом деле {new_n}/{len(pd)}; "
          f"из них в ячейках со Spine {sum(1 for r in pd if r['real_mod'] and r['mode'])}."]

    # 5. Рубрики
    L += ["", "### Рубрики по режиму (среднее, n оценённых)", "", "| рубрика | без Spine | spine | spine-hook |", "|---|---|---|---|"]
    for rb in ("solution_architecture", "architecture_gates", "neutral_architecture"):
        cells = []
        for m in MODES:
            v = [r["judge"].get(rb, {}).get("total") for r in rows if r["mode"] == m]
            v = [x for x in v if isinstance(x, (int, float))]
            cells.append(f"{st.mean(v):.2f} (n={len(v)})" if v else "—")
        L.append(f"| {rb} | " + " | ".join(cells) + " |")

    # 6. Прочее
    inc = [f for r in rows for f in r["dossier"]["included"]]
    L += ["", "### Прочие проверки", "",
          f"- файлов журнала MCP в досье судьи: {sum('mcp' in f.lower() for f in inc)} из {len(inc)}",
          f"- hook_blocks > 0 в ячейках без Spine: {[r['condition']+' r'+str(r['rep']) for r in no if r['hook_blocks']]}",
          f"- хуковые ячейки с hook_blocks ≥ 1: {sum(1 for r in rows if r['mode']=='spine-hook' and r['hook_blocks'])}/12",
          f"- ячейки со Spine без вызовов MCP (нет tool_search/tool_call): {[r['condition']+' r'+str(r['rep']) for r in sp if not {'tool_search','tool_call'} & set(r['tool_names'])]}",
          f"- медиана стены, с: " + ", ".join(f"{m or 'без Spine'} {st.median([r['wall_s'] for r in rows if r['mode']==m]):.0f}" for m in MODES)]
    print("\n".join(L))


if __name__ == "__main__":
    main()
