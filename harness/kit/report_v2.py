#!/usr/bin/env python3
"""Сводка v2 по results/live.jsonl: факторная таблица стек × режим Spine, непарные эффекты,
точный тест Фишера для гейта, взаимодействие, эквивалентность/не-хуже. Только stdlib."""
import json, pathlib, statistics, sys

from stats_v2 import boot_diff, boot_interaction, perm_test, fisher_exact, equivalence, non_inferior, holm
from stacks import parse_condition
from live_v2_helpers import gate_class

RUBRICS = ["solution_architecture", "architecture_gates", "adr_quality", "macedo_dimensions",
           "neutral_architecture"]
STACKS, MODES = ["plain", "openspec", "bmad", "superpowers"], ["", "spine", "spine-hook"]
MARGIN = 0.25   # зафиксировано в PREREGISTRATION-v2


def load(path):
    rows = [json.loads(l) for l in pathlib.Path(path).read_text(encoding="utf-8").splitlines() if l.strip()]
    for r in rows:
        r["stack"], r["mode"] = parse_condition(r["condition"])
        r["gate_class"] = gate_class(r["deterministic"])
    return rows


def vals(rows, stack, mode, rubric, drop_contaminated=False):
    out = []
    for r in rows:
        v = (r.get("judge", {}).get(rubric, {}) or {}).get("total")
        if r["stack"] == stack and r["mode"] == mode and isinstance(v, (int, float)) \
                and not (drop_contaminated and r.get("contamination")):
            out.append(v)
    return out


def cnt(rows, stack, mode, cls):
    xs = [r for r in rows if r["stack"] == stack and r["mode"] == mode]
    return sum(r["gate_class"] in cls for r in xs), len(xs)


def fmt(x):
    return "—" if x is None else (f"{x:.2f}" if isinstance(x, float) else str(x))


def main(path="results/live.jsonl", drop_contaminated=False, out_path=None):
    rows = load(path)
    L = ["# Живой прогон v2: стек × режим Spine", "",
         f"Прогонов: {len(rows)}; исключение загрязнённых: {'да' if drop_contaminated else 'нет (ITT)'}.", "",
         "| стек | Spine | n | " + " | ".join(RUBRICS) + " | PASS_DELTA | PASS_UNTOUCHED | FAIL |",
         "|---|---|---|" + "---|" * (len(RUBRICS) + 3)]
    for s in STACKS:
        for m in MODES:
            n = sum(1 for r in rows if r["stack"] == s and r["mode"] == m)
            if not n:
                continue
            means = []
            for rb in RUBRICS:
                v = vals(rows, s, m, rb, drop_contaminated)
                means.append(fmt(round(statistics.mean(v), 2)) if v else "—")
            g = [f"{cnt(rows, s, m, {c})[0]}/{n}" for c in ("PASS_DELTA", "PASS_UNTOUCHED", "FAIL")]
            L.append(f"| {s} | {m or '—'} | {n} | " + " | ".join(means) + " | " + " | ".join(g) + " |")

    L += ["", "## Эффект Spine внутри стека (непарно, bootstrap 95% CI, перестановочный p)", ""]
    for rb in ["solution_architecture", "architecture_gates", "neutral_architecture"]:
        for s in STACKS:
            for m in ("spine", "spine-hook"):
                a = vals(rows, s, m, rb, drop_contaminated)
                b = vals(rows, s, "", rb, drop_contaminated)
                if len(a) >= 2 and len(b) >= 2:
                    ni, ci90 = non_inferior(a, b, MARGIN)
                    L.append(f"- {rb}: {s}+{m} − {s} = {statistics.mean(a) - statistics.mean(b):+.2f} "
                             f"CI95 {boot_diff(a, b)} p={perm_test(a, b)}; "
                             f"не хуже (±{MARGIN}): {ni} CI90 {ci90}")
                else:
                    L.append(f"- {rb}: {s}+{m} − {s}: n<2 — не оценимо")

    L += ["", "## Гейт: доля PASS_DELTA, точный тест Фишера", ""]
    pvals, labels = [], []
    for s in STACKS:
        for m in ("spine", "spine-hook"):
            a, b = cnt(rows, s, m, {"PASS_DELTA"}), cnt(rows, s, "", {"PASS_DELTA"})
            if a[1] and b[1]:
                p = fisher_exact(a[0], a[1], b[0], b[1])
                L.append(f"- {s}+{m}: {a[0]}/{a[1]} vs {s}: {b[0]}/{b[1]} → p={p}")
                if s in ("bmad", "superpowers") and m == "spine-hook":
                    pvals.append(p)
                    labels.append(f"H1 {s}")
        a, b = cnt(rows, s, "spine-hook", {"PASS_DELTA"}), cnt(rows, s, "spine", {"PASS_DELTA"})
        if a[1] and b[1]:
            L.append(f"- {s}: хук vs советующий: {a[0]}/{a[1]} vs {b[0]}/{b[1]} → "
                     f"p={fisher_exact(a[0], a[1], b[0], b[1])}")
    if pvals:
        L += ["", "Поправка Холма на подтверждающие тесты H1 (порог α = 0.05):", ""]
        for i, p, thr, sig in holm(pvals):
            L.append(f"- {labels[i]}: p={p} ≤ {thr} → {'значимо' if sig else 'не значимо'}")

    L += ["", "## Взаимодействие: даёт ли Spine стеку больше, чем голому хосту (solution_architecture)", ""]
    for s in STACKS[1:]:
        for m in ("spine", "spine-hook"):
            g = [vals(rows, s, m, "solution_architecture"), vals(rows, s, "", "solution_architecture"),
                 vals(rows, "plain", m, "solution_architecture"), vals(rows, "plain", "", "solution_architecture")]
            if min(map(len, g)) >= 2:
                L.append(f"- ({s}+{m} − {s}) − (plain+{m} − plain): CI95 {boot_interaction(*g)}")

    L += ["", f"Правило «≈ 0»: 90% CI разности целиком внутри ±{MARGIN}; "
              f"при n < 4 решающие правила не применяются.",
          "PASS_UNTOUCHED — гейт зелёный, но принятая архитектура не изменена: это не дисциплина изменения."]
    out = pathlib.Path(out_path) if out_path else \
        pathlib.Path(path).with_name("live-summary-v2" + ("-clean" if drop_contaminated else "") + ".md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    main(args[0] if args else "results/live.jsonl",
         drop_contaminated="--drop-contaminated" in sys.argv)
