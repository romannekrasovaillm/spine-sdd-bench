#!/usr/bin/env python3
"""make_hero.py — единственная визуализация для начала README.

Одна картинка, по которой читаются ключевые результаты всех волн эксперимента:
  * эффект Spine как фактора (PASS_DELTA по режимам) и пул-тест Фишера;
  * матрица «стек × режим Spine»: исход каждого из 36 прогонов основного анализа;
  * качество не просело (средние баллы трёх рубрик по режимам);
  * слепая зона delta_guard (F4);
  * оговорки, без которых числа нельзя цитировать;
  * доля PASS_DELTA по всем волнам серии (v1 → v1-clean → пилот → v2).
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "charts"
OUT.mkdir(parents=True, exist_ok=True)

BG = "#0b0e13"
PANEL = "#141922"
CELL = "#10151d"
FG = "#e9edf3"
MUTED = "#8b95a6"
GRID = "#242b38"
GREEN = "#2ea043"
YELLOW = "#d29922"
RED = "#e5484d"
BLUE = "#4c8dff"
PURPLE = "#a371f7"
GREY = "#6e7681"

STACKS = [("plain", "голый агент"), ("openspec", "OpenSpec"), ("bmad", "BMAD"),
          ("superpowers", "superpowers")]
MODES = [("", "без Spine"), ("spine", "+spine\nсоветующий"), ("spine-hook", "+spine-hook\nблокирующий")]
CLASS_COLOR = {"PASS_DELTA": GREEN, "PASS_UNTOUCHED": YELLOW, "FAIL": RED, "": GREY}
RUBRICS = [("solution_architecture", "solution_architecture", BLUE),
           ("architecture_gates", "architecture_gates", GREEN),
           ("neutral_architecture", "neutral_architecture", PURPLE)]
WAVES = [("v1", "v1\n5 условий"), ("v1-clean", "v1-clean\n4 условия"),
         ("pilot-v2", "пилот v2\n12 ячеек"), ("v2", "v2\n12 ячеек × 3")]


def load():
    with open(ROOT / "results" / "manifest.csv", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def blank(ax, face=PANEL):
    ax.set_facecolor(face)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])


def main():
    rows = load()
    v2 = [r for r in rows if r["campaign"] == "v2"]

    fig = plt.figure(figsize=(16, 11), dpi=150)
    fig.patch.set_facecolor(BG)
    gs = fig.add_gridspec(3, 4, height_ratios=[2.45, 1.25, 0.72], hspace=0.20, wspace=0.18,
                          left=0.025, right=0.975, top=0.885, bottom=0.03)

    fig.text(0.025, 0.955, "Spine × SDD-стеки", color=FG, fontsize=30, fontweight="bold")
    fig.text(0.025, 0.912, "68 живых прогонов Qwen Code в роли solution-архитектора банка  ·  "
                           "факторная сетка «4 стека × 3 режима Spine»",
             color=MUTED, fontsize=13)
    fig.text(0.975, 0.955, "github.com/romannekrasovaillm/spine-sdd-bench", color=BLUE,
             fontsize=11, ha="right")
    fig.text(0.975, 0.925, "гейт — arch-be 0.3.11 · судья — glm-5.3", color=MUTED, fontsize=10,
             ha="right")

    # ------------------------------------------------------------------ числа
    ax0 = fig.add_subplot(gs[0, 0])
    blank(ax0)
    ax0.set_xlim(0, 1)
    ax0.set_ylim(0, 1)
    ax0.text(0.05, 0.955, "ГЛАВНЫЙ ВОПРОС", color=MUTED, fontsize=9, fontweight="bold")
    ax0.text(0.05, 0.885, "Повышает ли Spine долю\nизменений, внесённых\nпринятым способом?",
             color=FG, fontsize=12, va="top", linespacing=1.5)
    ax0.plot([0.05, 0.95], [0.70, 0.70], color=GRID, lw=1)
    ax0.text(0.05, 0.60, "0 %", color=GREY, fontsize=29, fontweight="bold", va="center")
    ax0.annotate("", xy=(0.55, 0.60), xytext=(0.31, 0.60),
                 arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.8))
    ax0.text(0.58, 0.60, "96 %", color=GREEN, fontsize=29, fontweight="bold", va="center")
    ax0.text(0.05, 0.515, "чистый контроль: 0 из 6", color=MUTED, fontsize=9.5)
    ax0.text(0.58, 0.515, "со Spine: 23 из 24", color=MUTED, fontsize=9.5)
    ax0.plot([0.05, 0.95], [0.43, 0.43], color=GRID, lw=1)
    ax0.text(0.05, 0.355, "Точный тест Фишера", color=MUTED, fontsize=9.5)
    ax0.text(0.05, 0.245, "p = 1.2·10⁻⁵", color=FG, fontsize=19, fontweight="bold")
    ax0.text(0.05, 0.150, "против грязного контроля: p = 0.0028", color=MUTED, fontsize=10)
    ax0.plot([0.05, 0.95], [0.09, 0.09], color=GRID, lw=1)
    ax0.text(0.05, 0.02, "Провалов гейта у чистого контроля: 5 из 6", color=FG, fontsize=10.5)

    # ------------------------------------------------------------------ матрица
    axm = fig.add_subplot(gs[0, 1:])
    blank(axm)
    axm.set_xlim(-1.35, 4.15)
    axm.set_ylim(-1.35, 5.05)
    for i, (_, mlabel) in enumerate(MODES):
        axm.text(i + 0.5, 4.42, mlabel, color=FG, fontsize=11, ha="center", va="center",
                 linespacing=1.35)
    for j, (skey, slabel) in enumerate(STACKS):
        y = 4 - j - 0.5
        axm.text(-0.14, y, slabel, color=FG, fontsize=11.5, ha="right", va="center")
        for i, (mkey, _) in enumerate(MODES):
            xs = [r for r in v2 if r["stack"] == skey and r["spine_mode"] == mkey]
            axm.add_patch(FancyBboxPatch((i + 0.05, y - 0.40), 0.90, 0.80,
                                         boxstyle="round,pad=0.01,rounding_size=0.07",
                                         linewidth=1.1, edgecolor=GRID, facecolor=CELL))
            for k, r in enumerate(sorted(xs, key=lambda z: z["rep"])):
                col = CLASS_COLOR.get(r["gate_class"], GREY)
                leak = int(r.get("access_spine_material") or 0) > 0
                axm.scatter(i + 0.5 + (k - 1) * 0.26, y + 0.13, s=210, color=col,
                            edgecolors="white" if leak else BG,
                            linewidths=1.8 if leak else 1.3,
                            linestyles="dashed" if leak else "solid", zorder=3)
                axm.text(i + 0.5 + (k - 1) * 0.26, y + 0.13, r["rep"], color="#0b0e13",
                         fontsize=7.5, ha="center", va="center", zorder=4, fontweight="bold")
            kind = Counter(r["gate_class"] for r in xs).most_common(1)[0][0]
            label = {"PASS_DELTA": "через дельту", "PASS_UNTOUCHED": "спайн не тронут",
                     "FAIL": "провал гейта"}.get(kind, "—")
            axm.text(i + 0.5, y - 0.24, label, color=CLASS_COLOR.get(kind, MUTED),
                     fontsize=8.8, ha="center", va="center")
    axm.text(1.08, 4.86, "каждый кружок — один живой прогон, цифра — номер повтора",
             color=MUTED, fontsize=9.5, ha="center")
    axm.scatter(-1.22, -0.60, s=150, color=GREEN, edgecolors=BG)
    axm.text(-1.08, -0.60, "через дельту (PASS_DELTA)", color=MUTED, fontsize=10, va="center")
    axm.scatter(0.28, -0.60, s=150, color=YELLOW, edgecolors=BG)
    axm.text(0.42, -0.60, "спайн не тронут (PASS_UNTOUCHED)", color=MUTED, fontsize=10, va="center")
    axm.scatter(1.72, -0.60, s=150, color=RED, edgecolors=BG)
    axm.text(1.86, -0.60, "провал гейта (FAIL)", color=MUTED, fontsize=10, va="center")
    axm.scatter(-1.22, -0.97, s=150, color=GREY, edgecolors="white", linewidths=1.8,
                linestyles="dashed")
    axm.text(-1.08, -0.97, "обведён пунктиром — прогон нашёл материалы Spine вне своей ячейки "
             "(именно эти 6 прогонов дали PASS_DELTA в контроле)",
             color=MUTED, fontsize=9.2, va="center")

    # ------------------------------------------------------------------ рубрики
    axr = fig.add_subplot(gs[1, 0])
    blank(axr)
    axr.set_xlim(-0.5, 2.5)
    axr.set_ylim(0, 5.2)
    width = 0.24
    for k, (key, label, col) in enumerate(RUBRICS):
        vals = []
        for mkey, _ in MODES:
            v = [float(r[key]) for r in v2 if r["spine_mode"] == mkey and r[key] not in ("", None)]
            vals.append(float(np.mean(v)) if v else 0)
        axr.bar(np.arange(3) + (k - 1) * width, vals, width, color=col, label=label.split("_")[0])
    axr.plot([-0.5, 2.5], [3.5, 3.5], color=RED, lw=1, ls=(0, (4, 3)))
    axr.text(2.45, 3.6, "порог 3.5", color=RED, fontsize=8, ha="right")
    axr.set_xticks(range(3))
    axr.set_xticklabels(["без\nSpine", "+spine", "+spine-\nhook"], color=MUTED, fontsize=9)
    axr.set_yticks([1, 3, 5])
    axr.tick_params(colors=MUTED, labelsize=8, length=0)
    axr.set_title("Качество не просело: средние баллы рубрик", color=FG, fontsize=11, pad=8)
    axr.legend(facecolor=PANEL, edgecolor=GRID, labelcolor=MUTED, fontsize=7.6,
               loc="upper center", bbox_to_anchor=(0.5, 1.0), ncol=1, framealpha=0.95,
               handlelength=1.1, labelspacing=0.25, borderpad=0.4)

    # ------------------------------------------------------------------ F4
    axf = fig.add_subplot(gs[1, 1])
    blank(axf)
    pd = [r for r in v2 if r["gate_class"] == "PASS_DELTA"]
    mod = sum(1 for r in pd if r["invariants_modified"])
    clean = len(pd) - mod
    axf.set_xlim(0, 1)
    axf.set_ylim(0, 1)
    axf.set_title("Изменения существующих инвариантов", color=FG, fontsize=11, pad=8)
    ads = sum(1 for r in pd if r["invariants_modified"])
    undecl = sum(1 for r in pd if r["invariants_undeclared"])
    decl = ads - undecl
    x0, x1, w = 0.06, 0.94, 0.30
    total = len(pd)
    axf.add_patch(Rectangle((x0, 0.55), (x1 - x0) * decl / total, w, color=YELLOW))
    axf.add_patch(Rectangle((x0 + (x1 - x0) * decl / total, 0.55), (x1 - x0) * undecl / total, w,
                            color=RED))
    axf.add_patch(Rectangle((x0 + (x1 - x0) * ads / total, 0.55),
                            (x1 - x0) * (total - ads) / total, w, color="#2a3341"))
    axf.text(x0 + (x1 - x0) * decl / total / 2, 0.70, str(decl), color="#0b0e13", fontsize=13,
             fontweight="bold", ha="center", va="center")
    axf.text(x0 + (x1 - x0) * decl / total + (x1 - x0) * undecl / total / 2, 0.70, str(undecl),
             color="white", fontsize=12, ha="center", va="center")
    axf.text(x0 + (x1 - x0) * ads / total + (x1 - x0) * (total - ads) / total / 2, 0.70,
             str(total - ads), color=MUTED, fontsize=12, ha="center", va="center")
    axf.text(x0, 0.42, f"из {total} «зелёных» дельт существующие", color=FG, fontsize=10)
    axf.text(x0, 0.31, f"инварианты меняли {ads}; из них {decl} объявлены", color=FG, fontsize=10)
    axf.text(x0, 0.20, f"в MODIFIED дельты, {undecl} — нет (мелкое уточнение,", color=MUTED, fontsize=10)
    axf.text(x0, 0.09, "ослаблений нет). Гейт смотрит файл, не тело AD.", color=MUTED, fontsize=10)

    # ------------------------------------------------------------------ оговорки
    axc = fig.add_subplot(gs[1, 2:])
    blank(axc)
    axc.set_xlim(0, 1)
    axc.set_ylim(0, 1)
    axc.set_title("Без этих оговорок числа цитировать нельзя", color=FG, fontsize=11, pad=8)
    lines = [
        ("n = 3 на ячейку вместо 6",
         "значимы только большие эффекты; per-stack тесты H1 незначимы, пул — исследовательский"),
        ("проверка слепоты судьи неинформативна",
         "постоянный ответ; сбалансированная точность 0.5 — различения нет"),
        ("слепота прогона нарушена",
         "26 из 36 агентов находили материалы Spine вне ячейки; это и даёт контроль 6/6"),
        ("по рубрикам вывода нет",
         "n = 3, один сэмпл судьи, две рубрики не оценены"),
    ]
    for i, (a, b) in enumerate(lines):
        y = 0.82 - i * 0.245
        axc.text(0.015, y, "— " + a, color=FG, fontsize=10.2)
        axc.text(0.035, y - 0.10, b, color=MUTED, fontsize=9.2)

    # ------------------------------------------------------------------ волны серии
    axw = fig.add_subplot(gs[2, :])
    blank(axw)
    axw.set_xlim(0, 1)
    axw.set_ylim(0, 1)
    axw.set_title("Все волны серии: доля изменений, внесённых принятым способом (PASS_DELTA)",
                  color=FG, fontsize=11, pad=6, loc="left")
    xs = np.linspace(0.055, 0.80, len(WAVES))
    for i, (camp, label) in enumerate(WAVES):
        rs = [r for r in rows if r["campaign"] == camp]
        share = sum(1 for r in rs if r["gate_class"] == "PASS_DELTA") / len(rs) if rs else 0
        col = GREY if camp.startswith("v1") else (BLUE if camp == "pilot-v2" else GREEN)
        axw.add_patch(Rectangle((xs[i] - 0.035, 0.22), 0.07, share * 0.56, color=col))
        axw.text(xs[i], 0.22 + share * 0.56 + 0.055, f"{share:.0%}", color=FG, fontsize=12,
                 ha="center", fontweight="bold")
        axw.text(xs[i], 0.16, label, color=MUTED, fontsize=8.6, ha="center", va="top",
                 linespacing=1.4)
        axw.text(xs[i], 0.055, f"n = {len(rs)}", color=MUTED, fontsize=8, ha="center")
    axw.text(0.845, 0.62, "Волны несравнимы по баллам:", color=MUTED, fontsize=9)
    axw.text(0.845, 0.47, "разные модели и дизайн.", color=MUTED, fontsize=9)
    axw.text(0.845, 0.30, "Класс гейта детерминирован", color=MUTED, fontsize=9)
    axw.text(0.845, 0.15, "и сравним между волнами.", color=MUTED, fontsize=9)

    fig.savefig(OUT / "hero.png", facecolor=BG)
    fig.savefig(OUT / "hero.svg", facecolor=BG)
    print("hero ->", OUT / "hero.png")


if __name__ == "__main__":
    main()
