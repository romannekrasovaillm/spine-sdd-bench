#!/usr/bin/env python3
"""make_charts.py — графики для витрины публичного репозитория.

Читает results/manifest.csv и строит четыре графика: исход гейта по ячейкам,
рубрики по ячейкам, эффект Spine как фактора и слепую зону delta_guard.
"""
from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve() / "charts"
OUT.mkdir(parents=True, exist_ok=True)

BG = "#0f1115"
PANEL = "#141922"
FG = "#e8ecf1"
GRID = "#2a2f3a"
C_PASS = "#2ea043"
C_UNTOUCHED = "#bf8700"
C_FAIL = "#d1242f"
YELLOW = "#d29922"
RED = "#e5484d"
MUTED = "#8b95a6"
FG = "#e8ecf1"
GRID = "#2a2f3a"
C_SPINE = "#1f6feb"
C_NOSPINE = "#8b949e"


def style(ax, title, ylabel=None):
    ax.set_facecolor(BG)
    for s in ax.spines.values():
        s.set_color(GRID)
    ax.tick_params(colors=FG, labelsize=9)
    ax.set_title(title, color=FG, fontsize=12, pad=12)
    if ylabel:
        ax.set_ylabel(ylabel, color=FG, fontsize=10)
    ax.grid(axis="y", color=GRID, alpha=0.5, linewidth=0.7)
    ax.set_axisbelow(True)


def panel(ax, color=PANEL):
    ax.set_facecolor(color)
    for s in ax.spines.values():
        s.set_visible(False)


def load():
    with open(OUT.parent / "results" / "manifest.csv", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main():
    rows = load()
    v2 = [r for r in rows if r["campaign"] == "v2"]
    cells = []
    for s in ("plain", "openspec", "bmad", "superpowers"):
        for m in ("", "spine", "spine-hook"):
            cells.append(f"{s}+{m}" if m else s)
    SHORT = ["plain", "p+sp", "p+hk", "ospec", "o+sp", "o+hk", "bmad", "b+sp", "b+hk",
             "spw", "s+sp", "s+hk"]
    fig = plt.figure(figsize=(13, 10.5), dpi=170, facecolor=BG)

    # 1. исход гейта по ячейкам (v2)
    ax = fig.add_subplot(2, 2, 1)
    x = np.arange(len(cells))
    bottom = np.zeros(len(cells))
    for cls, col, label in (("PASS_DELTA", C_PASS, "PASS через дельту"),
                            ("PASS_UNTOUCHED", C_UNTOUCHED, "PASS без касания спайна"),
                            ("FAIL", C_FAIL, "FAIL")):
        vals = []
        for c in cells:
            xs = [r for r in v2 if r["condition"] == c]
            vals.append(sum(1 for r in xs if r["gate_class"] == cls))
        vals = np.array(vals, dtype=float)
        ax.bar(x, vals, bottom=bottom, color=col, label=label, width=0.72)
        bottom += vals
    ax.set_xticks(x)
    ax.set_xticklabels(SHORT, fontsize=8)
    style(ax, "v2: исход гейта по ячейкам (n = 3)", "прогонов")
    ax.legend(facecolor=BG, edgecolor=GRID, labelcolor=FG, fontsize=8)

    # 2. рубрики по ячейкам
    ax2 = fig.add_subplot(2, 2, 2)
    rubs = [("solution_architecture", "solution_architecture", "#1f6feb"),
            ("architecture_gates", "architecture_gates", "#2ea043"),
            ("neutral_architecture", "neutral_architecture", "#a371f7")]
    w = 0.26
    for i, (key, label, col) in enumerate(rubs):
        vals = []
        for c in cells:
            v = [float(r[key]) for r in v2 if r["condition"] == c and r[key] not in ("", None)]
            vals.append(float(np.mean(v)) if v else np.nan)
        ax2.bar(x + (i - 1) * w, vals, w, color=col, label=label)
    ax2.axhline(3.5, ls="--", lw=0.9, color=C_FAIL)
    ax2.text(len(cells) - 0.4, 3.55, "порог 3.5", color=C_FAIL, fontsize=7, ha="right")
    ax2.set_xticks(x)
    ax2.set_xticklabels(SHORT, fontsize=8)
    ax2.set_ylim(0, 5)
    style(ax2, "v2: баллы рубрик (судья glm-5.3, 1 сэмпл)", "балл 1–5")
    ax2.legend(facecolor=BG, edgecolor=GRID, labelcolor=FG, fontsize=7,
               loc="upper center", bbox_to_anchor=(0.5, 1.0), ncol=1,
               labelspacing=0.25, borderpad=0.35)

    # 3. эффект Spine как фактора (контроль разделён по загрязнению)
    ax3 = fig.add_subplot(2, 2, 3)
    panel(ax3)
    no = [r for r in v2 if r["spine_mode"] == ""]
    clean = [r for r in no if not int(r["access_spine_material"] or 0)]
    dirty = [r for r in no if int(r["access_spine_material"] or 0)]
    groups = [("чистый\nконтроль", clean, C_NOSPINE),
              ("нашёл Spine\nсам", dirty, "#b07d3a"),
              ("+spine", [r for r in v2 if r["spine_mode"] == "spine"], C_SPINE),
              ("+spine-hook", [r for r in v2 if r["spine_mode"] == "spine-hook"], "#a371f7")]
    share = [sum(1 for r in xs if r["gate_class"] == "PASS_DELTA") / len(xs) * 100 if xs else 0
             for _, xs, _ in groups]
    bars = ax3.bar([g[0] for g in groups], share, color=[g[2] for g in groups], width=0.6)
    for b, v, (_, xs, _) in zip(bars, share, groups):
        ax3.text(b.get_x() + b.get_width() / 2, v + 3, f"{v:.0f}%\n(n={len(xs)})", ha="center",
                 color=FG, fontsize=8.5)
    ax3.set_ylim(0, 118)
    ax3.tick_params(axis="x", labelsize=8)
    style(ax3, "Доля изменений через дельту", "% прогонов с PASS_DELTA")

    # 4. изменения существующих инвариантов
    ax4 = fig.add_subplot(2, 2, 4)
    panel(ax4)
    pd = [r for r in v2 if r["gate_class"] == "PASS_DELTA"]
    ads = sum(1 for r in pd if r["invariants_modified"])
    undecl = sum(1 for r in pd if r["invariants_undeclared"])
    decl = ads - undecl
    total = len(pd)
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.set_xticks([])
    ax4.set_yticks([])
    ax4.set_title("Изменения существующих инвариантов AD-001…AD-008 в «зелёных» дельтах",
                  color=FG, fontsize=11, pad=8)
    x0, x1, h = 0.03, 0.97, 0.34
    ax4.add_patch(Rectangle((x0, 0.44), (x1 - x0) * decl / total, h, color=YELLOW))
    ax4.add_patch(Rectangle((x0 + (x1 - x0) * decl / total, 0.44), (x1 - x0) * undecl / total, h,
                            color=RED))
    ax4.add_patch(Rectangle((x0 + (x1 - x0) * ads / total, 0.44),
                            (x1 - x0) * (total - ads) / total, h, color="#2a3341"))
    ax4.text(x0 + (x1 - x0) * decl / total / 2, 0.61, str(decl), color="#0b0e13", fontsize=13,
             fontweight="bold", ha="center", va="center")
    ax4.text(x0 + (x1 - x0) * decl / total + (x1 - x0) * undecl / total / 2, 0.61, str(undecl),
             color="white", fontsize=12, ha="center", va="center")
    ax4.text(x0 + (x1 - x0) * ads / total + (x1 - x0) * (total - ads) / total / 2, 0.61,
             str(total - ads), color=MUTED, fontsize=13, ha="center", va="center")
    ax4.text(x0, 0.30, f"жёлтый — объявлены в MODIFIED дельты ({decl}); красный — нет ({undecl}); "
                       f"серый — существующие AD не менялись ({total - ads})",
             color=MUTED, fontsize=9.5)
    ax4.text(x0, 0.16, "Гейт смотрит на файл, а не на тело AD: объявленность и характер правки "
                       "остаются работой ревью.", color=MUTED, fontsize=9.5)

    fig.text(0.5, 0.012,
             "«Через дельту» = правка принятого решения вместе с заявкой (ADDED / MODIFIED / "
             "REMOVED), которую принимает гейт; правка защищённого файла без дельты — FAIL.",
             color=MUTED, fontsize=9, ha="center")
    fig.suptitle("Spine × SDD-стеки: живые прогоны в TUI Qwen Code",
                 color=FG, fontsize=15, y=0.98)
    fig.tight_layout(rect=[0, 0.032, 1, 0.96])
    fig.savefig(OUT / "dashboard.png", facecolor=BG)
    fig.savefig(OUT / "dashboard.svg", facecolor=BG)
    print("charts ->", OUT / "dashboard.png")


if __name__ == "__main__":
    main()
