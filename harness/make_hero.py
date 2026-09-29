#!/usr/bin/env python3
"""make_hero.py — единственная визуализация для начала README (v2.1).

Картинка читается без контекста и без статистики. Сверху вниз:

    1. ГЛАВНЫЙ ВЫВОД: дисциплину изменения даёт доступ к процессу, а не стек,
       рядом — шкала «как читать p (критерий Фишера)» с качественной оценкой
       силы доказательства: ПЛОХО / ТЕРПИМО / ХОРОШО / ОТЛИЧНО.
    2. ЧТО ЗНАЧИТ «ИЗМЕНЕНИЕ ЧЕРЕЗ ДЕЛЬТУ»: заявка -> правка решения -> гейт.
    3. Три группы прогонов по доступу к процессу Spine:
           нет доступа (чистый контроль v2 + песочница v2.1)  -> 0/18
           доступ случайный (нашли arch-be сами в $HOME)      -> 6/6
           доступ штатный (MCP + скиллы / Stop-хук)           -> 23/24
    4. ЧТО ЭТО ДАЁТ АРХИТЕКТОРУ: четыре следствия и «что делать в понедельник».
    5. НА ПРИМЕРЕ: один агент, один кейс, один стек — FAIL без доступа к процессу
       против PASS_DELTA с ним (plain-r1 против plain+spine-r1).
    6. КАК SPINE ОЦЕНЁН В ЦЕЛОМ: смысловые рубрики судьи — Spine не оценён лучше
       контроля по содержанию (различия меньше разброса внутри групп).
    7. Доказательная база: матрица 36 прогонов, утечки в песочнице v2.1,
       изменения существующих инвариантов, все волны серии.

Вся вёрстка идёт в одной системе координат (дюймы холста 16 x 19.7), поэтому текст
не наезжает на панели и не обрезается по краям.
"""
from __future__ import annotations

import csv
import statistics
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "charts"
OUT.mkdir(parents=True, exist_ok=True)

BG = "#0b0e13"
PANEL = "#101720"
CARD = "#171d27"
CELL = "#10151d"
FG = "#eef2f7"
MUTED = "#8b95a6"
DIM = "#5d6675"
GRID = "#232a36"
GREEN = "#2ea043"
YELLOW = "#d29922"
RED = "#e5484d"
BLUE = "#4c8dff"
GREY = "#6e7681"
LIME = "#7cc45c"

W, H = 16.0, 19.7

STACKS = [("plain", "голый агент"), ("openspec", "OpenSpec"), ("bmad", "BMAD"),
          ("superpowers", "superpowers")]
MODES = [("", "без Spine"), ("spine", "+spine\nсоветующий"),
         ("spine-hook", "+spine-hook\nблокирующий")]
CLASS_COLOR = {"PASS_DELTA": GREEN, "PASS_UNTOUCHED": YELLOW, "FAIL": RED, "": GREY}
WAVES = [("v1", "v1"), ("v1-clean", "v1-clean"), ("pilot-v2", "пилот v2"),
         ("v2", "v2"), ("v2.1", "v2.1 песочница")]


def load() -> list[dict]:
    with open(ROOT / "results" / "manifest.csv", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main() -> None:
    rows = load()
    v2 = [r for r in rows if r["campaign"] == "v2"]
    v21 = [r for r in rows if r["campaign"] == "v2.1"]

    def pd_(xs):
        return sum(1 for r in xs if r["gate_class"] == "PASS_DELTA")

    no_spine = [r for r in v2 if r["spine_mode"] == ""]
    clean_v2 = [r for r in no_spine if not int(r["access_spine_material"] or 0)]
    found_v2 = [r for r in no_spine if int(r["access_spine_material"] or 0)]
    with_spine = [r for r in v2 if r["spine_mode"]]
    groups = [
        ("НЕТ ДОСТУПА\nк процессу", pd_(clean_v2) + pd_(v21), len(clean_v2) + len(v21),
         "чистый контроль v2 (0/6)\n+ песочница v2.1 (0/12)", RED),
        ("ДОСТУП НАШЁЛСЯ\nсам", pd_(found_v2), len(found_v2),
         "агент сам нашёл arch-be\nи материалы вне песочницы", YELLOW),
        ("ДОСТУП ШТАТНЫЙ\nSpine подключён", pd_(with_spine), len(with_spine),
         "MCP + скиллы (12/12)\nи Stop-хук (11/12)", GREEN),
    ]

    fig = plt.figure(figsize=(W, H), dpi=150)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_facecolor(BG)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    def t(x, y, s, size=10, color=FG, weight="normal", ha="left", va="center", lsp=1.4):
        ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va,
                linespacing=lsp)

    def card(x0, y0, x1, y1, face=CARD, edge=GRID, lw=1.3, rs=0.08):
        ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                                    boxstyle=f"round,pad=0,rounding_size={rs}",
                                    linewidth=lw, edgecolor=edge, facecolor=face))

    # ------------------------------------------------------------------ шапка
    t(0.35, 19.40, "Spine × SDD-стеки", size=27, weight="bold")
    t(0.37, 19.00, f"{len(rows)} живых прогонов Qwen Code в роли solution-архитектора банка "
                   f"(кейс: платёжный шлюз СБП, изменение «СБП-подписки»)",
      size=12, color=MUTED)
    t(15.65, 19.44, "github.com/romannekrasovaillm/spine-sdd-bench", size=10.5, color=BLUE,
      ha="right")
    t(15.65, 19.12, "гейт — arch-be 0.3.11 · решатель — deepseek-flash · судья — glm-5.3",
      size=9.5, color=DIM, ha="right")

    # --------------------------------------------------- главный вывод + шкала p
    card(0.35, 17.12, 9.05, 18.86, face=PANEL, edge="#1d2634")
    t(0.62, 18.60, "ГЛАВНЫЙ ВЫВОД", size=9.5, color=MUTED, weight="bold")
    t(0.62, 18.12, "Дисциплину изменения даёт доступ к процессу,\nа не название стека",
      size=18, weight="bold", lsp=1.35)
    t(0.62, 17.65, "Один и тот же агент, один и тот же кейс, одни и те же стеки.\n"
                   "Разница только в том, видит ли агент механику принятого решения.",
      size=10.5, color=MUTED, lsp=1.45)
    t(0.62, 17.28, "Случайностью не объяснить: p = 5,4·10⁻¹¹ — 1 шанс из 18,5 млрд, "
                   "оценка «отлично».",
      size=10, color=GREEN, weight="bold")

    card(9.30, 17.12, 15.65, 18.86, face=PANEL, edge="#1d2634")
    t(9.55, 18.60, "КАК ЧИТАТЬ p (критерий Фишера)", size=10.5, color=FG, weight="bold")
    t(9.55, 18.34, "p — вероятность увидеть такую разницу случайно, если связи нет вообще.",
      size=9.4, color=MUTED)
    t(9.55, 18.16, "Чем меньше p, тем сильнее доказательство (оценка справа):",
      size=9.4, color=MUTED)

    def chip(y, label, col):
        xc, wch = 14.90, 1.15
        ax.add_patch(FancyBboxPatch((xc - wch / 2, y - 0.105), wch, 0.21,
                                    boxstyle="round,pad=0,rounding_size=0.06",
                                    linewidth=1.1, edgecolor=col,
                                    facecolor=mcolors.to_rgba(col, 0.16)))
        t(xc, y, label, size=8.2, color=col, weight="bold", ha="center")

    scale = [("p > 0,05", "разницы на этих данных не видно", DIM, MUTED, "ПЛОХО"),
             ("p < 0,05", "совпадением объяснить трудно (1 из 20)", YELLOW, MUTED, "ТЕРПИМО"),
             ("p < 0,001", "почти исключено (1 из 1000)", LIME, MUTED, "ХОРОШО"),
             ("p = 5,4·10⁻¹¹", "1 из 18 500 000 000 — здесь", GREEN, FG, "ОТЛИЧНО")]
    for i, (val, txt, col, tcol, grade) in enumerate(scale):
        y = 17.96 - i * 0.22
        t(9.55, y, val, size=10.5, color=col, weight="bold")
        t(10.95, y, "— " + txt, size=9.4, color=tcol)
        chip(y, grade, col)

    # ------------------------------------------- что значит «через дельту»
    card(0.35, 15.02, 15.65, 16.92, face=CARD, edge="#243044")
    t(0.62, 16.74, "ЧТО ЗНАЧИТ «ИЗМЕНЕНИЕ ЧЕРЕЗ ДЕЛЬТУ»", size=14, weight="bold")
    t(0.62, 16.50, "Принятое решение защищено гейтом: правку нельзя сделать молча — "
                   "её объявляют заявкой, то есть дельтой.", size=10, color=MUTED)
    steps = [
        ("1. ЗАЯВКА — до правки", GREEN,
         "Агент пишет дельту: что в решении\nДОБАВЛЯЕТСЯ, МЕНЯЕТСЯ и СНИМАЕТСЯ\n"
         "(ADDED / MODIFIED / REMOVED) и почему."),
        ("2. ПРАВКА РЕШЕНИЯ", BLUE,
         "Только затем меняются защищённые файлы:\nARCHITECTURE-SPINE.md, CONSTRAINTS.yaml,\n"
         "ADR и контракты. Дельта лежит рядом."),
        ("3. ПРОВЕРКА ГЕЙТОМ", FG,
         "Гейт сверяет: защищённый файл тронут без\nдельты → КРАСНЫЙ. Дельта есть → "
         "PASS_DELTA:\nизменение внесено принятым способом."),
    ]
    for i, (head, col, body) in enumerate(steps):
        x0 = 0.62 + i * 5.05
        card(x0, 15.32, x0 + 4.75, 16.34, face=CELL, edge=col, lw=1.5, rs=0.06)
        t(x0 + 0.22, 16.17, head, size=11, color=col, weight="bold")
        t(x0 + 0.22, 15.96, body, size=10.5, color=MUTED, va="top", lsp=1.45)
    t(0.62, 15.14, "Без дельты: молча переписал решение → 5 из 6 провалов гейта; "
                   "не тронул решение вовсе → гейт зелёный, но изменение живёт мимо "
                   "архитектуры (PASS_UNTOUCHED).",
      size=9.6, color=DIM)

    # ------------------------------------------------------------------ три группы
    t(0.35, 12.67, "PASS_DELTA — доля прогонов, где принятое решение изменено принятым "
                   "способом (через дельту)", size=11, weight="bold")
    for i, (label, yes, n, sub, col) in enumerate(groups):
        x0 = 0.35 + i * 5.15
        x1 = x0 + 4.95
        card(x0, 12.85, x1, 14.80, face=CARD, edge=col, lw=1.8)
        cx = (x0 + x1) / 2
        t(cx, 14.50, label, size=13, color=col, weight="bold", ha="center", lsp=1.35)
        t(cx, 14.02, f"{yes} / {n}", size=34, weight="bold", ha="center")
        ax.add_patch(Rectangle((x0 + 0.45, 13.58), 4.05, 0.16, color="#222a36"))
        share = yes / n if n else 0
        if share > 0:
            ax.add_patch(Rectangle((x0 + 0.45, 13.58), 4.05 * share, 0.16, color=col))
        t(cx, 13.32, f"{share:.0%} изменений через дельту", size=11, color=MUTED, ha="center")
        t(cx, 13.06, sub, size=10, color=DIM, ha="center", lsp=1.4)

    # ------------------------------------------- что это даёт архитектору
    card(0.35, 9.90, 15.65, 12.45, face=CARD, edge="#243044")
    t(0.62, 12.25, "ЧТО ЭТО ДАЁТ АРХИТЕКТОРУ", size=13.5, weight="bold")
    lessons = [
        ("1. СТЕК МОЖНО НЕ МЕНЯТЬ", GREEN,
         "Эффект даёт контур контроля, а не\nпереезд. В советующем режиме через\n"
         "дельту прошли 3/3 в каждом стеке:\nOpenSpec, BMAD, superpowers\nи голый агент."),
        ("2. ХУК НЕ ОБЯЗАТЕЛЕН", BLUE,
         "MCP + скиллы — 12/12.\nБлокирующий Stop-хук — 11/12\n"
         "и почти вдвое дольше: медиана\n990 с против 536 с. Процедуру\n"
         "делают доступной, не карательной."),
        ("3. ГЕЙТ ≠ АРХИТЕКТУРНОЕ РЕВЬЮ", YELLOW,
         "8 из 29 зелёных дельт меняли\nсуществующие AD (7 объявлены).\n"
         "Гейт видит файл и наличие дельты;\nчто именно изменилось в теле\n"
         "решения — читает человек."),
        ("4. ДОКАЗАТЕЛЬСТВО БЕЗ LLM", LIME,
         "Класс гейта, дельта и дифф\nвоспроизводимы и не зависят\n"
         "от модели. «Правка защищённого\nфайла без дельты — красный»\n"
         "ставится обязательным чеком CI."),
    ]
    for i, (head, col, body) in enumerate(lessons):
        x0 = 0.62 + i * 3.83
        card(x0, 10.47, x0 + 3.63, 11.99, face=CELL, edge=col, lw=1.4, rs=0.06)
        t(x0 + 0.18, 11.82, head, size=10, color=col, weight="bold")
        t(x0 + 0.18, 11.60, body, size=9.8, color=MUTED, va="top", lsp=1.45)
    t(0.62, 10.22, "Что делать в понедельник: 1) объявить защищённые файлы решения "
                  "(ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml) и завести шаблон дельты — "
                  "ADDED / MODIFIED / REMOVED + влияние на инварианты;",
      size=9.6, color=FG)
    t(0.62, 10.06, "2) договориться о едином месте дельты (changes/<id>/DELTA.md) — иначе "
                  "гейт её не увидит; 3) сделать гейт обязательным чеком CI; 4) начать "
                  "с советующего режима MCP + скиллы, хук — точечно.",
      size=9.6, color=DIM)

    # ------------------------------------------------------------- на примере
    card(0.35, 7.85, 15.65, 9.70, face=CARD, edge="#243044")
    t(0.62, 9.52, "НА ПРИМЕРЕ: один и тот же агент, один и тот же кейс, один и тот же "
                  "стек — голый агент (plain)", size=12.5, weight="bold")
    ex_left = ("БЕЗ ДОСТУПА К ПРОЦЕССУ → FAIL", RED,
               "ADR-008 и папку изменения агент завёл, но AD-009 и AD-010 дописал прямо",
               "в ARCHITECTURE-SPINE.md — дельты в конвенции контура "
               "(changes/<id>/DELTA.md) нет.",
               "Гейт: FAIL — защищённый файл правлен без дельты.",
               "Ревью и аудит: изменение в решении есть, заявки в истории решений нет.")
    ex_right = ("С ДОСТУПОМ К ПРОЦЕССУ → PASS_DELTA", GREEN,
                "Тот же стек и кейс: сначала changes/sbp-subscriptions/DELTA.md — ADDED /",
                "MODIFIED / REMOVED и таблица влияния, затем те же защищённые файлы.",
                "Гейт: PASS_DELTA — дельта объявляет изменение, набор контура полный.",
                "Ревью и аудит: одна дельта вместо 25 файлов, всё воспроизводимо.")
    for i, (head, col, l1, l2, l3, l4) in enumerate((ex_left, ex_right)):
        x0 = 0.62 + i * 7.55
        card(x0, 8.07, x0 + 7.20, 9.33, face=CELL, edge=col, lw=1.5, rs=0.06)
        t(x0 + 0.22, 9.16, head, size=11, color=col, weight="bold")
        t(x0 + 0.22, 8.96, f"{l1}\n{l2}\n{l3}\n{l4}", size=9.8, color=MUTED, va="top",
          lsp=1.45)
    t(0.62, 7.95, "Урок архитектору: конвенция «где и в каком виде живёт дельта» — часть "
                  "контура. Тот же агент и стек: без неё заявка есть, но гейт её не видит "
                  "→ FAIL; с ней → PASS_DELTA.",
      size=9.6, color=FG)

    # ------------------------------------------- как оценён Spine в целом
    card(0.35, 5.25, 15.65, 7.65, face=CARD, edge="#243044")
    t(0.62, 7.42, "КАК ОЦЕНЁН SPINE В ЦЕЛОМ — СМЫСЛОВЫЕ РУБРИКИ (судья glm-5.3, шкала 1–5)",
      size=12.5, weight="bold")
    t(0.62, 7.18, "Нейтральная рубрика написана не автором Spine (ISO/IEC/IEEE 42010, "
                  "arc42, ADR по Nygard).", size=9.4, color=MUTED)

    gx0, gx1, gv0, gv1 = 6.60, 13.10, 2.8, 4.3

    def gx(v):
        return gx0 + (v - gv0) / (gv1 - gv0) * (gx1 - gx0)

    for gv in (3.0, 3.5, 4.0):
        ax.plot([gx(gv), gx(gv)], [5.82, 7.08], color=GRID, lw=0.9,
                ls="--" if gv == 3.5 else ":", zorder=1)
        t(gx(gv), 5.72, f"{gv:.1f}".replace(".", ","), size=8.4, color=DIM, ha="center")

    spine_v2 = [r for r in v2 if r["spine_mode"]]
    base_v2 = [r for r in v2 if r["spine_mode"] == ""]

    def ms(xs, key):
        v = [float(r[key]) for r in xs if r[key] not in ("", None)]
        return statistics.mean(v), statistics.pstdev(v), len(v)

    rubs = [("solution_architecture", "пакет решения", 6.95, 0.27, 0.25),
            ("architecture_gates", "архитектурные гейты", 6.52, 0.54, 0.52),
            ("neutral_architecture", "нейтральная рубрика (не Spine)", 6.09, 0.30, 0.22)]
    for key, label, y, sd_b, sd_s in rubs:
        t(0.62, y, label, size=10, color=FG)
        t(3.10, y, key, size=8.4, color=DIM)
        mb, _, nb = ms(base_v2, key)
        msr, _, ns = ms(spine_v2, key)
        for m, sd, col, dy, ldy in ((mb, sd_b, GREY, 0.075, 0.135),
                                    (msr, sd_s, GREEN, -0.075, -0.135)):
            ax.plot([gx(m - sd), gx(m + sd)], [y + dy, y + dy], color=col, lw=1.6, alpha=0.6,
                    solid_capstyle="round", zorder=2)
            ax.scatter(gx(m), y + dy, s=100, color=col, zorder=3, edgecolors=BG,
                       linewidths=0.8)
            t(gx(m), y + ldy, f"{m:.2f}".replace(".", ","), size=8.6, color=col,
              weight="bold", ha="center")
    ax.scatter(13.55, 7.00, s=100, color=GREY, zorder=3, edgecolors=BG, linewidths=0.8)
    t(13.74, 7.00, "без Spine  (n = 12)", size=9, color=MUTED)
    ax.scatter(13.55, 6.72, s=100, color=GREEN, zorder=3, edgecolors=BG, linewidths=0.8)
    t(13.74, 6.72, "Spine всего  (n = 23–24)", size=9, color=MUTED)
    t(13.55, 6.46, "усы — разброс ±σ внутри группы,\nпунктир — порог рубрики 3,5",
      size=8.6, color=DIM, va="top", lsp=1.4)

    d = [ms(spine_v2, k)[0] - ms(base_v2, k)[0] for k, _, _, _, _ in rubs]
    t(0.62, 5.40, "Разница Spine − без Spine: пакет решения "
                  f"{d[0]:+.2f}".replace(".", ",") + ", гейты "
                  f"{d[1]:+.2f}".replace(".", ",") + ", нейтральная "
                  f"{d[2]:+.2f}".replace(".", ",") +
      " — меньше разброса внутри групп (σ 0,22–0,54). По содержанию Spine не оценён "
      "лучше: доказан способ изменения решения.", size=9.6, color=FG)

    # ------------------------------------------------------------------ матрица
    card(0.35, 1.62, 9.55, 5.05, face=CARD, edge=GRID)
    t(0.62, 4.78, "Основной анализ v2: 36 прогонов", size=12.5, weight="bold")
    mx0, mx1 = 0.55, 9.35
    colw = (mx1 - mx0) / 3
    for i, (_, mlabel) in enumerate(MODES):
        t(mx0 + colw * (i + 0.5), 4.46, mlabel, size=10.5, ha="center", lsp=1.35, color=FG)
    row_top, rowh = 4.00, 0.64
    for j, (skey, slabel) in enumerate(STACKS):
        y = row_top - j * rowh
        t(mx0 + 0.02, y, slabel, size=11, color=FG)
        for i, (mkey, _) in enumerate(MODES):
            cell_x0 = mx0 + colw * i + 0.10
            cell_x1 = mx0 + colw * (i + 1) - 0.10
            if j % 2 == 0:
                card(cell_x0, y - 0.25, cell_x1, y + 0.25, face=CELL, edge=GRID, lw=0.9,
                     rs=0.05)
            xs = [r for r in v2 if r["stack"] == skey and r["spine_mode"] == mkey]
            ccx = (cell_x0 + cell_x1) / 2
            for k, r in enumerate(sorted(xs, key=lambda z: z["rep"])):
                col = CLASS_COLOR.get(r["gate_class"], GREY)
                leak = int(r.get("access_spine_material") or 0) > 0
                sx = ccx + (k - 1) * 0.34
                ax.scatter(sx, y + 0.08, s=180, color=col, zorder=3,
                           edgecolors="white" if leak else BG,
                           linewidths=1.7 if leak else 1.1,
                           linestyles="dashed" if leak else "solid")
                t(sx, y + 0.08, r["rep"], size=6.8, color="#0b0e13", ha="center",
                  weight="bold")
            kind = Counter(r["gate_class"] for r in xs).most_common(1)[0][0]
            t(ccx, y - 0.16, {"PASS_DELTA": "через дельту",
                              "PASS_UNTOUCHED": "спайн не тронут",
                              "FAIL": "провал гейта"}.get(kind, "—"),
              size=8.4, color=CLASS_COLOR.get(kind, MUTED), ha="center")
    t(0.62, 1.70, "Белая штриховая обводка — агент нашёл материалы Spine сам.",
      size=9, color=MUTED)

    # ------------------------------------------------------------------ песочница v2.1
    card(9.80, 3.55, 15.65, 5.05, face=CARD, edge=GRID)
    t(10.05, 4.78, "Песочница v2.1: утечек нет", size=12.5, weight="bold")
    t(10.05, 4.52, "12 контрольных прогонов в контейнере.", size=9.8, color=MUTED)
    t(10.05, 4.34, "Изменений через дельту — ноль. Проверенные каналы:",
      size=9.8, color=MUTED)
    for i, name in enumerate(("материалы Spine", "харнесс и руководство",
                              "мета-файлы ячейки", "$HOME оператора")):
        y = 4.14 - i * 0.17
        t(10.05, y, "— " + name, size=8.8, color=DIM)
        t(15.40, y, "0", size=10.5, color=GREEN, weight="bold", ha="right")

    # ------------------------------------------------------------------ AD
    pd_rows = [r for r in v2 if r["gate_class"] == "PASS_DELTA"]
    decl = sum(1 for r in pd_rows if r["invariants_modified"] and not r["invariants_undeclared"])
    undecl = sum(1 for r in pd_rows if r["invariants_undeclared"])
    total = len(pd_rows)
    card(9.80, 1.62, 15.65, 3.45, face=CARD, edge=GRID)
    t(10.05, 3.20, "Что менялось в принятых инвариантах", size=12.5, weight="bold")
    x0, x1, h = 10.05, 15.40, 0.26
    ybar = 2.62
    ax.add_patch(Rectangle((x0, ybar), (x1 - x0) * decl / total, h, color=YELLOW))
    ax.add_patch(Rectangle((x0 + (x1 - x0) * decl / total, ybar), (x1 - x0) * undecl / total,
                           h, color=RED))
    ax.add_patch(Rectangle((x0 + (x1 - x0) * (decl + undecl) / total, ybar),
                           (x1 - x0) * (total - decl - undecl) / total, h, color="#222a36"))
    t(x0 + (x1 - x0) * decl / total / 2, ybar + h / 2, str(decl), size=12, color="#0b0e13",
      weight="bold", ha="center")
    t(x0 + (x1 - x0) * decl / total + (x1 - x0) * undecl / total / 2, ybar + h / 2,
      str(undecl), size=11, color="white", ha="center")
    t(x0 + (x1 - x0) * (decl + undecl) / total + (x1 - x0) * (total - decl - undecl)
      / total / 2, ybar + h / 2, str(total - decl - undecl), size=11, color=MUTED,
      ha="center")
    for i, (col, label) in enumerate([(YELLOW, "объявлено в MODIFIED дельты"),
                                      (RED, "не объявлено"),
                                      ("#222a36", "существующие AD не тронуты")]):
        ly = 2.32 - i * 0.20
        ax.add_patch(Rectangle((10.05, ly - 0.05), 0.16, 0.11, color=col))
        t(10.30, ly, label, size=8.8, color=MUTED)
    t(10.05, 1.76, f"из {total} зелёных дельт существующие AD меняли {decl + undecl};\n"
                   f"все — в ячейках со Spine, ослаблений правил нет.",
      size=9, color=DIM, va="top", lsp=1.4)

    # ------------------------------------------------------------------ волны
    t(0.35, 1.42, "Все волны серии — доля PASS_DELTA:", size=9.5, color=MUTED)
    xs = np.linspace(1.55, 9.10, len(WAVES))
    for i, (camp, label) in enumerate(WAVES):
        rs = [r for r in rows if r["campaign"] == camp]
        share = pd_(rs) / len(rs) if rs else 0
        col = RED if share == 0 else (GREY if camp.startswith("v1") else
                                      (BLUE if camp == "pilot-v2" else GREEN))
        ax.add_patch(Rectangle((xs[i] - 0.30, 0.74), 0.60, 0.40, color="#1c2530"))
        if share > 0:
            ax.add_patch(Rectangle((xs[i] - 0.30, 0.74), 0.60, 0.40 * share, color=col))
        t(xs[i], 0.58, f"{label} · {share:.0%} · n={len(rs)}", size=8.4, color=MUTED,
          ha="center")
    t(9.80, 0.96, "v2.1 — контроль в песочнице даёт ноль:\nэто подтверждение гипотезы, "
                  "а не провал.", size=9.2, color=MUTED, lsp=1.4)

    # ------------------------------------------------------------------ оговорки
    t(0.35, 0.30, "Оговорки: n = 3 на ячейку, судья — 1 сэмпл, проверка слепоты судьи "
                  "неинформативна, adr_quality и macedo_dimensions не оценены; "
                  "по рубрикам вывода нет.", size=8.4, color=DIM)
    t(0.35, 0.10, "Первый отчёт называл «24 из 29» изменившихся инвариантов — это была ошибка "
                  "подсчёта границы AD-блока; верное число 8 из 29 (docs/06-corrections-to-v2.md).",
      size=8.4, color=DIM)

    fig.savefig(OUT / "hero.png", facecolor=BG)
    fig.savefig(OUT / "hero.svg", facecolor=BG)
    print("hero ->", OUT / "hero.png")


if __name__ == "__main__":
    main()
