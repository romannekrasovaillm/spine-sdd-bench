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

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve() / "charts"
OUT.mkdir(parents=True, exist_ok=True)

BG = "#0f1115"
FG = "#e8ecf1"
GRID = "#2a2f3a"
C_PASS = "#2ea043"
C_UNTOUCHED = "#bf8700"
C_FAIL = "#d1242f"
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
    ax2.legend(facecolor=BG, edgecolor=GRID, labelcolor=FG, fontsize=7)

    # 3. эффект Spine как фактора
    ax3 = fig.add_subplot(2, 2, 3)
    modes = ["", "spine", "spine-hook"]
    share, tot = [], []
    for m in modes:
        xs = [r for r in v2 if r["spine_mode"] == m]
        share.append(sum(1 for r in xs if r["gate_class"] == "PASS_DELTA") / len(xs) * 100 if xs else 0)
        tot.append(len(xs))
    bars = ax3.bar(["без Spine", "+spine (советующий)", "+spine-hook (блокирующий)"], share,
                   color=[C_NOSPINE, C_SPINE, "#a371f7"], width=0.55)
    for b, v, n in zip(bars, share, tot):
        ax3.text(b.get_x() + b.get_width() / 2, v + 2, f"{v:.0f}%\n(n={n})", ha="center",
                 color=FG, fontsize=9)
    ax3.set_ylim(0, 115)
    style(ax3, "Доля изменений, внесённых принятым способом", "% прогонов с PASS_DELTA")

    # 4. слепая зона delta_guard
    ax4 = fig.add_subplot(2, 2, 4)
    pd_rows = [r for r in v2 if r["gate_class"] == "PASS_DELTA"]
    mod = sum(1 for r in pd_rows if r["invariants_modified"])
    clean = len(pd_rows) - mod
    bars = ax4.barh(["зелёные дельты"], [mod], color=C_FAIL, label="меняли существующие AD")
    ax4.barh(["зелёные дельты"], [clean], left=[mod], color=C_PASS, label="существующие AD не тронуты")
    ax4.text(mod / 2, 0, str(mod), ha="center", va="center", color="white", fontsize=12)
    ax4.text(mod + clean / 2, 0, str(clean), ha="center", va="center", color="white", fontsize=12)
    style(ax4, "F4: что скрывают «зелёные» дельты", "")
    ax4.legend(facecolor=BG, edgecolor=GRID, labelcolor=FG, fontsize=8, loc="lower right")

    fig.suptitle("Spine × SDD-стеки: живые прогоны в TUI Qwen Code",
                 color=FG, fontsize=15, y=0.98)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT / "dashboard.png", facecolor=BG)
    fig.savefig(OUT / "dashboard.svg", facecolor=BG)
    print("charts ->", OUT / "dashboard.png")


if __name__ == "__main__":
    main()
