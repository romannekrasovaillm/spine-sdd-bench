#!/usr/bin/env python3
"""apply_corrections_v2.py — R16: пересчёт метрик v2 исправленными функциями.

Что делает (по ревью spine-sdd-bench-v2-corrections.md, раздел 3.2 R16):
  * пересчитывает `invariants` в score.json каждого прогона v2 правильными границами
    AD-блока (П1: блок кончается на следующем заголовке уровня 1–2 или на `---`, а не
    на следующем `## AD-…`; прежняя версия отдавала хвост файла последнему AD);
  * добавляет `invariants_declared` — объявлены ли изменённые AD в разделе MODIFIED дельты;
  * добавляет каналы утечки: `access_spine_material`, `saw_condition_commit`, `read_harness`,
    `cell_meta_reads`, `runtime_spine_ok`;
  * пересобирает `results/manifest.csv`, `results/manifest.json`, `results/stats.json`.

Запуск: python3 apply_corrections_v2.py <корень репозитория>
"""
from __future__ import annotations

import collections
import csv
import json
import re
import statistics as st
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
RUNS = ROOT / "results" / "runs" / "v2"

SPINE_MATERIAL = re.compile(r"arch-harness|\.arch-ml|arch-be|spine-bank|SPINE_BANK|<REPO>|"
                            r"experiments/|delta-spec|/\.claude/|detection-summary|Загрузки")
HARNESS_TEXT = re.compile(r"bench-v2-guide|spine-sdd-bench|PREREGISTRATION|live_v2_helpers|"
                          r"stacks\.py|run_live|report_v2|panel\.txt|base\.json")
COMMIT_LEAK = re.compile(r"условие [a-z+\-]+ установлено")
CELL_META = re.compile(r"cells/w[a-z0-9]{6}/(panel\.txt|base\.json|meta\.json|prompt\.txt)")
ARCH_BE_RUN = re.compile(r"arch-be\s+(gate|delta|lint|connect|check|rubric|--help|help|--version)")
MCP_TOOLS = re.compile(r"mcp__spine__|\"spine\"\s*:\s*\{|tool_search[^\n]{0,200}spine")


# ------------------------------------------------------------------ П1
def ad_blocks(text: str) -> dict[str, str]:
    """AD-блок кончается на следующем заголовке уровня 1–2 или на горизонтальной черте."""
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


def modified_invariants(base: str, new: str) -> dict[str, list[str]]:
    a, b = ad_blocks(base), ad_blocks(new)
    return {"modified": sorted(k for k in a if k in b and a[k] != b[k]),
            "removed": sorted(k for k in a if k not in b),
            "added": sorted(k for k in b if k not in a)}


def declared_in_delta(run_dir: Path, ads: list[str]) -> list[str]:
    """Подмножество изменённых AD, объявленных в разделе MODIFIED дельты."""
    txt = " ".join(p.read_text(encoding="utf-8", errors="replace")
                   for p in run_dir.glob("artifacts/changes/*/DELTA.md"))
    sec = re.search(r"#{2,3}\s*MODIFIED(.*?)(\n#{2,3}\s|\Z)", txt, re.S)
    body = sec.group(1) if sec else ""
    return [a for a in ads if a in body]


def main() -> None:
    runs = sorted(RUNS.iterdir())
    # База: спайн из прогона, который его не касался (PASS_UNTOUCHED). Проверяем единогласие.
    unt = [d for d in runs if json.loads((d / "score.json").read_text(encoding="utf-8"))
           .get("gate_class") == "PASS_UNTOUCHED"]
    cands = {}
    for d in unt:
        f = d / "artifacts" / "ARCHITECTURE-SPINE.md"
        if f.exists():
            cands[d.name] = f.read_text(encoding="utf-8")
    if not cands:
        sys.exit("не найден baseline спайна (нет PASS_UNTOUCHED с артефактом)")
    shas = {re.sub(r"\s+", "", t) for t in cands.values()}
    if len(shas) != 1:
        sys.exit(f"baseline спайна неоднозначен: {sorted(cands)}")
    base = next(iter(cands.values()))
    print(f"baseline спайна взят из: {', '.join(sorted(cands))}")

    changed = 0
    for d in runs:
        sf = d / "score.json"
        sc = json.loads(sf.read_text(encoding="utf-8"))
        det = sc.get("deterministic") or {}
        new_file = d / "artifacts" / "ARCHITECTURE-SPINE.md"
        new = new_file.read_text(encoding="utf-8") if new_file.exists() else base
        inv = modified_invariants(base, new)
        declared = declared_in_delta(d, inv["modified"])
        det["invariants"] = inv
        det["invariants_declared"] = declared
        det["invariants_undeclared"] = [a for a in inv["modified"] if a not in declared]
        sc["deterministic"] = det
        tr = (d / "transcript.md").read_text(encoding="utf-8", errors="replace") if (d / "transcript.md").exists() else ""
        cont = sc.get("contamination") or []
        sc["access_spine_material"] = sum(1 for c in cont if SPINE_MATERIAL.search(c))
        sc["saw_condition_commit"] = len(COMMIT_LEAK.findall(tr))
        sc["read_harness"] = len(HARNESS_TEXT.findall(tr))
        sc["cell_meta_reads"] = len(CELL_META.findall(tr))
        sc["arch_be_runs"] = len(ARCH_BE_RUN.findall(tr))
        sc["runtime_spine_ok"] = bool(MCP_TOOLS.search(tr))
        sf.write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
        changed += 1
    print(f"score.json обновлено: {changed}")

    # ---- манифест
    man = ROOT / "results" / "manifest.csv"
    rows = list(csv.DictReader(man.open(encoding="utf-8")))
    keep = [k for k in rows[0] if k not in ("invariants_modified",)]
    add = ["invariants_modified", "invariants_declared", "invariants_undeclared",
           "access_spine_material", "saw_condition_commit", "read_harness", "cell_meta_reads",
           "arch_be_runs", "runtime_spine_ok"]
    header = keep + add
    out_rows = []
    for r in rows:
        if r["campaign"] != "v2":
            out_rows.append({**{k: r.get(k, "") for k in header}})
            continue
        d = RUNS / f"{r['condition']}-r{r['rep']}"
        sc = json.loads((d / "score.json").read_text(encoding="utf-8"))
        det = sc["deterministic"]
        r = dict(r)
        r["invariants_modified"] = ",".join(det["invariants"]["modified"])
        r["invariants_declared"] = ",".join(det["invariants_declared"])
        r["invariants_undeclared"] = ",".join(det["invariants_undeclared"])
        for k in ("access_spine_material", "saw_condition_commit", "read_harness",
                  "cell_meta_reads", "arch_be_runs", "runtime_spine_ok"):
            r[k] = sc.get(k)
        out_rows.append({k: r.get(k, "") for k in header})
    with man.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=header)
        w.writeheader()
        w.writerows(out_rows)
    (ROOT / "results" / "manifest.json").write_text(
        json.dumps(out_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"манифест пересобран: {len(out_rows)} строк")

    # ---- статистика
    v2 = [r for r in out_rows if r["campaign"] == "v2"]
    stats: dict = {"total_runs": len(out_rows),
                   "by_campaign": dict(collections.Counter(r["campaign"] for r in out_rows))}
    M = {"": "no_spine", "spine": "spine", "spine-hook": "spine_hook"}
    for m, label in M.items():
        xs = [r for r in v2 if r["spine_mode"] == m]
        stats[f"gate_{label}"] = {c: sum(1 for r in xs if r["gate_class"] == c)
                                  for c in ("PASS_DELTA", "PASS_UNTOUCHED", "FAIL")}
        stats[f"gate_{label}"]["n"] = len(xs)
        for rb in ("solution_architecture", "architecture_gates", "neutral_architecture"):
            vals = [float(r[rb]) for r in xs if r[rb] not in ("", None)]
            stats[f"rubric_{label}_{rb}"] = round(st.mean(vals), 2) if vals else None
    pd = [r for r in v2 if r["gate_class"] == "PASS_DELTA"]
    stats["pass_delta_n"] = len(pd)
    stats["pass_delta_modified"] = sum(1 for r in pd if r["invariants_modified"])
    stats["pass_delta_declared"] = sum(1 for r in pd if r["invariants_modified"]
                                       and not r["invariants_undeclared"])
    no = [r for r in v2 if r["spine_mode"] == ""]
    clean = [r for r in no if not int(r["access_spine_material"] or 0)]
    dirty = [r for r in no if int(r["access_spine_material"] or 0)]
    stats["control_clean"] = {"n": len(clean),
                              "PASS_DELTA": sum(1 for r in clean if r["gate_class"] == "PASS_DELTA")}
    stats["control_dirty"] = {"n": len(dirty),
                              "PASS_DELTA": sum(1 for r in dirty if r["gate_class"] == "PASS_DELTA")}
    stats["leak_channels"] = {
        "saw_condition_commit": sum(1 for r in v2 if int(r["saw_condition_commit"] or 0)),
        "spine_material": sum(1 for r in v2 if int(r["access_spine_material"] or 0)),
        "harness_text": sum(1 for r in v2 if int(r["read_harness"] or 0)),
        "cell_meta": sum(1 for r in v2 if int(r["cell_meta_reads"] or 0)),
    }
    (ROOT / "results" / "stats.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in stats.items() if k.startswith(("control", "pass_delta", "leak"))},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
