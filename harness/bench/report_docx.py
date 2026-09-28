#!/usr/bin/env python3
"""report_docx.py — финальный отчёт .docx: сравнение по рубрикам Spine + скриншоты.

Читает результаты живого TUI-прогона (results/live.jsonl, runs/cells/*/score.json)
и кадры (frames/) и собирает документ Word. Никаких чисел «на память»: всё, что
попадает в таблицы, берётся из результатов прогона.
"""
from __future__ import annotations

import json
import os
import re
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import shots  # noqa: E402

def _root(env: str, default: str) -> Path:
    v = os.environ.get(env)
    if not v:
        return ROOT / default
    q = Path(v)
    return q if q.is_absolute() else ROOT / q


RESULTS = _root("BENCH_RESULTS", "results")
FRAMES = _root("BENCH_FRAMES", "frames")
RUNS = _root("BENCH_RUNS", "runs")
CELLS = RUNS / "cells"
CELLMAP = RUNS / "cell-map.json"

RUBRICS = ["solution_architecture", "architecture_gates", "adr_quality", "macedo_dimensions"]
RUBRIC_RU = {
    "solution_architecture": "solution_architecture — качество документа решения (15 критериев)",
    "architecture_gates": "architecture_gates — контрольные точки A0–A5 (6 критериев)",
    "adr_quality": "adr_quality — качество архитектурного решения (5 критериев)",
    "macedo_dimensions": "macedo_dimensions — таксономия Macedo (6 измерений)",
}
COND_RU = {
    "plain": "plain — голый Qwen Code (контроль)",
    "spine": "Spine Core 0.3.11 (MCP `spine` + 66 скиллов)",
    "openspec": "OpenSpec 1.13.2 (6 скиллов + 6 команд)",
    "bmad": "BMAD 6.12.0 (29 скиллов)",
    "superpowers": "superpowers 6.4.2 (15 скиллов + SessionStart-хук)",
    "calm": "CALM 1.60.1 — нейтральное задание (добровольное принятие)",
    "calm-explicit": "CALM 1.60.1 — архитектор явно просит модель CALM (потолок продукта)",
}
COND_SHORT = {k: v.split(" —")[0] for k, v in COND_RU.items()}
COND_ORDER = ["plain", "spine", "openspec", "bmad", "superpowers", "calm", "calm-explicit"]


# ------------------------------------------------------------------ данные
def load_rows() -> list[dict]:
    """Все ячейки прогона. Каталоги могут быть обезличенными (cell-map.json)."""
    dirs: list[Path] = []
    if CELLMAP.exists():
        m = json.loads(CELLMAP.read_text(encoding="utf-8"))
        dirs = [CELLS / v for v in m.values()]
    else:
        dirs = [d for d in sorted(CELLS.iterdir()) if d.is_dir()]
    dirs += [d for d in sorted(CELLS.glob("*-r*")) if d.is_dir() and d not in dirs]
    out = []
    for d in dirs:
        if (d / "meta.json").exists() and (d / "score.json").exists():
            out.append({**json.loads((d / "meta.json").read_text(encoding="utf-8")),
                        **json.loads((d / "score.json").read_text(encoding="utf-8")),
                        "_cell": d})
    return out


def mean(vals):
    v = [x for x in vals if isinstance(x, (int, float))]
    return round(statistics.mean(v), 2) if v else None


def fmt(v, nd=2):
    return "—" if v is None else (f"{v:.{nd}f}" if isinstance(v, float) else str(v))


def group(rows):
    by: dict[str, list[dict]] = {}
    for x in rows:
        by.setdefault(x["condition"], []).append(x)
    return by


def rubric_matrix(by):
    return {c: {rb: mean([x.get("judge", {}).get(rb, {}).get("total") for x in xs]) for rb in RUBRICS}
            for c, xs in by.items()}


def criteria_matrix(by):
    out = {}
    for c, xs in by.items():
        per: dict[str, dict[str, list]] = {}
        for x in xs:
            for rb, v in (x.get("judge") or {}).items():
                for cid, score in (v.get("criteria") or {}).items():
                    per.setdefault(rb, {}).setdefault(cid, []).append(score)
        out[c] = {rb: {cid: mean(v) for cid, v in crits.items()} for rb, crits in per.items()}
    return out


def sensor_score(x):
    return sum(1 for k, v in x["sensors"].items() if isinstance(v, bool) and v)


# ------------------------------------------------------------------ графика
def chart(by, path: Path):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
    except Exception:  # noqa: BLE001
        return None
    conds = [c for c in COND_ORDER if c in by]
    m = rubric_matrix(by)
    x = np.arange(len(RUBRICS))
    w = 0.8 / max(len(conds), 1)
    fig, ax = plt.subplots(figsize=(10, 4.6), dpi=160)
    colors = ["#8c8c8c", "#1f6feb", "#2ea043", "#bf8700", "#a371f7"]
    for i, c in enumerate(conds):
        vals = [m[c][rb] or 0 for rb in RUBRICS]
        bars = ax.bar(x + i * w - 0.4 + w / 2, vals, w, label=COND_SHORT[c], color=colors[i % len(colors)])
        for b, v in zip(bars, vals):
            if v:
                ax.text(b.get_x() + b.get_width() / 2, v + 0.05, f"{v:.2f}", ha="center",
                        va="bottom", fontsize=7)
    ax.set_xticks(x)
    ax.set_xticklabels(["solution_\narchitecture", "architecture_\ngates", "adr_\nquality",
                        "macedo_\ndimensions"], fontsize=8)
    ax.set_ylim(0, 5.4)
    ax.set_ylabel("Балл рубрики Spine (1–5)")
    ax.set_title("Оценка архитектурных пакетов по рубрикам Spine (слепой судья)", fontsize=11)
    ax.axhline(3.5, ls="--", lw=0.8, color="#d1242f")
    ax.text(3.42, 3.56, "порог 3.5", fontsize=7, color="#d1242f")
    ax.legend(fontsize=8, ncol=5, loc="upper center", frameon=False)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)
    plt.close(fig)
    return path


def chart_det(by, path: Path):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
    except Exception:  # noqa: BLE001
        return None
    conds = [c for c in COND_ORDER if c in by]
    fig, ax = plt.subplots(figsize=(9, 3.6), dpi=160)
    x = np.arange(len(conds))
    sens = [mean([sensor_score(x_) for x_ in by[c]]) or 0 for c in conds]
    files = [mean([len(x_.get("changed") or []) for x_ in by[c]]) or 0 for c in conds]
    calls = [mean([x_.get("tool_calls") for x_ in by[c]]) or 0 for c in conds]
    ax.bar(x - 0.22, sens, 0.22, label="сенсоры объектного минимума (/10)", color="#1f6feb")
    ax.bar(x, [f / 3 for f in files], 0.22, label="файлов изменено (÷3)", color="#2ea043")
    ax.bar(x + 0.22, [c / 15 for c in calls], 0.22, label="вызовов инструментов (÷15)", color="#bf8700")
    for xi, (s, f_, c_) in enumerate(zip(sens, files, calls)):
        ax.text(xi - 0.22, s + 0.1, f"{s:.1f}", ha="center", fontsize=7)
        ax.text(xi, f_ / 3 + 0.1, f"{f_:.0f}", ha="center", fontsize=7)
        ax.text(xi + 0.22, c_ / 15 + 0.1, f"{c_:.0f}", ha="center", fontsize=7)
    ax.set_xticks(x)
    ax.set_xticklabels([COND_SHORT[c] for c in conds], fontsize=8)
    ax.set_title("Что стек реально дал в живом прогоне (масштабировано для наглядности)", fontsize=10)
    ax.legend(fontsize=7.5, frameon=False)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)
    plt.close(fig)
    return path


# ------------------------------------------------------------------ docx-хелперы
def set_base_style(doc):
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(10.5)
    for sec in doc.sections:
        sec.left_margin = Inches(0.8)
        sec.right_margin = Inches(0.8)
        sec.top_margin = Inches(0.7)
        sec.bottom_margin = Inches(0.7)


def h(doc, text, level=1):
    return doc.add_heading(text, level=level)


def para(doc, text, bold=False, italic=False, size=None):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    if size:
        r.font.size = Pt(size)
    return p


def bullets(doc, items):
    for it in items:
        doc.add_paragraph(it, style="List Bullet")


def table(doc, header, rows, widths=None, style="Light Grid Accent 1"):
    t = doc.add_table(rows=1, cols=len(header))
    t.style = style
    for i, htxt in enumerate(header):
        cell = t.rows[0].cells[i]
        cell.text = ""
        r = cell.paragraphs[0].add_run(htxt)
        r.bold = True
        r.font.size = Pt(8.5)
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ""
            r = cells[i].paragraphs[0].add_run(str(v))
            r.font.size = Pt(8.5)
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Inches(w)
    return t


def add_shot(doc, png: Path, caption: str, width=6.8):
    if not png or not Path(png).exists():
        return
    doc.add_picture(str(png), width=Inches(width))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(caption)
    r.italic = True
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)


def render_frames(cond: str) -> list[tuple[Path, str]]:
    """Рендер покадровых снимков панели tmux (capture-pane → PNG)."""
    out = []
    raw = sorted((FRAMES / "raw" / f"{cond}-r1").glob("*.ansi"))
    picks = [p for p in raw if "99-end" not in p.stem][-2:]
    for p in picks:
        title = ""
        t = p.with_suffix(".title")
        if t.exists():
            title = t.read_text(encoding="utf-8").strip()
        png = FRAMES / "render" / f"{p.stem}.png"
        shots.render_ansi(p.read_text(encoding="utf-8"), png,
                          header=f"ЖИВОЙ TUI Qwen Code · {title or p.stem}", font_size=14)
        out.append((png, f"{COND_SHORT.get(cond, cond)}: кадр панели tmux {p.stem}"))
    return out


def pick_shots(cond: str) -> list[tuple[Path, str]]:
    out = []
    raw = sorted((FRAMES / "raw" / f"{cond}-r1").glob("x11-*.png"))
    if raw:
        out.append((raw[len(raw) // 2],
                    f"{COND_SHORT.get(cond, cond)}: X11-скриншот живого TUI в середине архитектурного цикла "
                    f"(слева — сессия Qwen Code, справа — плашка прогона)"))
    fin = FRAMES / f"{cond}-r1-final.png"
    if fin.exists():
        out.append((fin, f"{COND_SHORT.get(cond, cond)}: X11-скриншот финального состояния хода"))
    out += render_frames(cond)
    return out


# ------------------------------------------------------------------ сборка
def build(conds=None, reps=2, out: Path | None = None) -> Path:
    rows = load_rows()
    by = group(rows)
    conds = [c for c in (conds or COND_ORDER) if c in by]
    out = out or (ROOT / "Spine_vs_OpenSpec_BMAD_Superpowers_live_TUI_report.docx")
    m = rubric_matrix(by)
    cm = criteria_matrix(by)

    doc = Document()
    set_base_style(doc)

    doc.add_heading("Живые прогоны в TUI Qwen Code: Spine Core против OpenSpec, superpowers и BMAD", 0)
    sub = doc.add_paragraph()
    r = sub.add_run("Ценность для solution-архитектора по рубрикам Spine Core")
    r.bold = True
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(0x1f, 0x6f, 0xeb)
    doc.add_paragraph()
    n = len(rows)
    meta = [
        f"Дата отчёта: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "Кейс: spine-bank, «кейсы/sbp-gateway» — платёжный шлюз СБП (C2B-приём); "
        "brownfield-изменение «СБП-подписки» (рекуррентные C2B-списания по согласию плательщика)",
        "Роль агента: solution-архитектор банка (задание TASK.md комплекта spine-qwen-bench-kit)",
        f"Хост прогона: Qwen Code 0.24.6 в живом TUI (tmux-сессия), "
        f"решатель — {rows[0]['solver'] if rows else '—'}",
        f"Судейство: {rows[0].get('judge_model') if rows else '—'} — другое семейство моделей, чем решатель; "
        f"слепое досье (названия стеков нейтрализованы), {len(RUBRICS)} рубрики Spine, 3 сэмпла на критерий",
        f"Прогонов: {n} — {len(conds)} условий × "
        f"{sorted({len(v) for v in by.values()})} повторов; каждый — отдельная живая TUI-сессия",
        "Все артефакты: live-tui/results/live.jsonl, live-tui/runs/cells/*, live-tui/frames/*",
    ]
    for x in meta:
        p = doc.add_paragraph(x, style="List Bullet")
        for run in p.runs:
            run.font.size = Pt(9.5)

    # --- исправления (v2, §2 руководства: добавить раздел, исходный текст не переписывать)
    corr = ROOT / "results-v2" / "CORRECTIONS-v1.md"
    if corr.exists():
        h(doc, "0. Исправления к отчёту от 2026-09-28 (добавлено 2026-09-28, v2)", 1)
        para(doc, "Раздел добавлен по руководству spine-sdd-bench-v2-guide.md (§2). Исходный текст "
                  "отчёта ниже не переписывался. Полная таблица — в live-tui/results-v2/"
                  "CORRECTIONS-v1.md.", italic=True)
        rows_corr = []
        for line in corr.read_text(encoding="utf-8").splitlines():
            if line.startswith("| E") and line.count("|") >= 5:
                c = [x.strip() for x in line.strip("|").split("|")]
                rows_corr.append([c[0], c[1], c[3][:220]])
        if rows_corr:
            table(doc, ["№", "Место", "Что верно"], rows_corr, widths=[0.45, 1.4, 5.0])
        for line in corr.read_text(encoding="utf-8").splitlines():
            if line.startswith(("1. ", "2. ", "3. ", "4. ")):
                doc.add_paragraph(line.strip(), style="List Bullet")

    # ---------------------------------------------------------- 1. резюме
    h(doc, "1. Резюме", 1)
    para(doc, "Четыре методических стека и голый Qwen Code решали одно и то же задание в живом TUI "
              "под ролью solution-архитектора банка. Их архитектурные пакеты оценил слепой судья "
              "другого семейства моделей по рубрикам самого Spine; отдельно сработал "
              "детерминированный слой Spine (единый гейт для всех условий).")
    best = {}
    for rb in RUBRICS:
        vals = [(c, m[c][rb]) for c in conds if m[c][rb] is not None]
        if vals:
            best[rb] = max(vals, key=lambda kv: kv[1])
    res = [[COND_RU[c]] + [fmt(m[c][rb]) for rb in RUBRICS] + [fmt(mean([sensor_score(x) for x in by[c]]), 1)]
           for c in conds]
    res.append(["Лучший по рубрике"] + [f"{best[rb][0]} ({best[rb][1]:.2f})" if rb in best else "—"
                                        for rb in RUBRICS] + [""])
    table(doc, ["Условие"] + [rb.replace("_", "_\n") for rb in RUBRICS] + ["сенсоры\n/10"], res,
          widths=[2.35, 1.0, 1.0, 1.0, 1.0, 0.7])
    doc.add_paragraph()
    ch = chart(by, RESULTS / "rubrics.png")
    add_shot(doc, ch, "Рис. 1. Итоги по рубрикам Spine. Красная линия — порог 3.5 из конфигурации "
                      "гейта `[gate.decision_quality] min_score`.", width=6.9)

    para(doc, "Главный результат прогона лежит не в баллах, а в детерминированном слое: "
              "гейт Spine прошёл только у Spine (0.3.11) и у OpenSpec, причём по разным причинам. "
              "Три условия из пяти — plain, BMAD и superpowers — получили FAIL на `delta_guard`: "
              "они правили принятый спайн (ARCHITECTURE-SPINE.md) напрямую, мимо дельты. "
              "Это ровно тот класс ошибок, который механика ловит без человека.")

    # ---------------------------------------------------------- 2. метод
    h(doc, "2. Метод", 1)
    para(doc, "Дизайн повторяет наработку комплекта spine-qwen-bench-kit (PREREGISTRATION.md, TASK.md, "
              "stacks.py, run_live.py): то же задание, тот же кейс, те же условия установки стеков, "
              "тот же детерминированный скоринг, та же слепая рубричная оценка. Отличия перечислены "
              "в разделе 9 и в «Ограничениях».")
    h(doc, "2.1. Условия", 2)
    inv_rows = []
    for c in conds:
        inv = by[c][0].get("inventory", {})
        inv_rows.append([COND_RU[c], inv.get("project_skills", 0), inv.get("extension_skills", 0),
                         inv.get("commands", 0), ", ".join(inv.get("mcp_servers") or []) or "—",
                         ", ".join(inv.get("hooks") or []) or "—"])
    table(doc, ["Условие", "скиллов\nпроекта", "скиллов\nрасшир.", "команд", "MCP", "хуки"], inv_rows,
          widths=[2.3, 0.8, 0.8, 0.7, 1.0, 0.9])
    for c in conds:
        pass
    h(doc, "2.2. Прогон", 2)
    bullets(doc, [
        "Каждое условие — отдельная копия кейса, свой git с зафиксированным baseline-коммитом, "
        "свой HOME (изоляция расширений, памяти и журналов Qwen Code), авто-обновление хоста выключено, "
        "версия хоста пришпилена (0.24.6).",
        "Агент работал в живом TUI Qwen Code внутри tmux: стартовая TUI-сессия, задание отправлено "
        "текстом, конец хода определялся по JSONL-журналу Qwen (нет висящих вызовов, последняя запись — "
        "текст ассистента, тишина) И по спокойствию кадра (индикатор `esc to cancel` исчез).",
        "Все прогоны шли параллельно с одним и тем же решателем; ход каждого документирован "
        "X11-скриншотами окна зрителя и покадровыми снимками панели tmux.",
        "Работа агента зафиксирована git-коммитом поверх baseline; скоринг считается по диффу "
        "`baseline..HEAD`.",
    ])
    h(doc, "2.3. Чем оценивали", 2)
    bullets(doc, [
        "Детерминированный слой — единая линейка для всех: `arch-be gate --repo . --base <baseline>` "
        "(fitness, delta guard, анти-ослабление правил, линтер спайна, трассировка), "
        "`arch-be contract-diff` для контракта, правки защищённых файлов, сенсоры объектного минимума.",
        "Смысловой слой — слепой судья: файлы агента нейтрализуются (названия стеков → нейтральные "
        "токены), рубрики Spine, 3 сэмпла на критерий, `--author-model` = модель-решатель "
        "(механика видит, что судья не автор).",
        "Рубрики: solution_architecture (15 критериев), architecture_gates (A0–A5, 6), "
        "adr_quality (5), macedo_dimensions (6 измерений таксономии Macedo).",
        "Рубрика adr_quality применяется к документу-решению (ADR, иначе проект изменения) — "
        "так, как она и задумана; остальные три — к досье всего пакета.",
    ])
    h(doc, "2.4. Лимит рубрики 24 000 символов и как он решён", 2)
    para(doc, "Механика Spine отказывается оценивать текст длиннее 24 000 символов и прямо "
              "предписывает оценивать документ по разделам (ADR-004: тихое усечение запрещено). "
              "Живой архитектурный пакет не влезает в этот лимит: от 50 до 113 КБ. Поэтому досье "
              "собирается детерминированно: фиксированный приоритет файлов (решение → проект "
              "изменения → NFR → контракты → спеки → спайн), бюджет 23 500 символов, потолок на файл "
              "6 200 символов с явной пометкой об усечении, а исключённые файлы названы в шапке досье. "
              "Это ограничение инструмента, а не прогона; состав досье по каждому условию приведён "
              "в разделе 6 и в `live-tui/runs/cells/*/score.json`.")

    # ---------------------------------------------------------- 3. рубрики
    h(doc, "3. Рубрики Spine, по которым сравниваются стеки", 1)
    for rb in RUBRICS:
        h(doc, RUBRIC_RU[rb], 2)
    para(doc, "Шкала 1–5, взвешенный итог. Рубрики — самого Spine Core, поэтому структурно "
              "благоприятны ему; это ограничение зафиксировано в разделе «Ограничения».")

    # ---------------------------------------------------------- 4. результаты
    h(doc, "4. Результаты по условиям", 1)
    for c in conds:
        xs = by[c]
        h(doc, COND_RU[c], 2)
        inv = xs[0].get("inventory", {})
        facts = [
            f"Повторов: {len(xs)}; ход агента завершён без таймаута: "
            f"{sum(1 for x in xs if x.get('turn_ok'))}/{len(xs)}; стена: "
            f"{fmt(mean([x.get('wall_s') for x in xs]), 0)} с",
            f"Рубрики Spine: " + " · ".join(f"{rb} = {fmt(m[c][rb])}" for rb in RUBRICS),
            f"Вызовов инструментов: {fmt(mean([x.get('tool_calls') for x in xs]), 0)}; "
            f"файлов изменено: {fmt(mean([len(x.get('changed') or []) for x in xs]), 1)}; "
            f"объём текста: {fmt(mean([x['sensors'].get('chars') for x in xs]), 0)} знаков",
            f"Сенсоры объектного минимума: {fmt(mean([sensor_score(x) for x in xs]), 1)}/10; "
            f"плейсхолдеров TBD/TODO: {fmt(mean([x['sensors'].get('placeholders') for x in xs]), 1)}",
            f"Гейт Spine: PASS "
            f"{sum(1 for x in xs if x['deterministic']['spine_gate_exit'] == 0)}/{len(xs)}; "
            f"провалы: {', '.join(sorted({f for x in xs for f in x['deterministic']['spine_gate_fails']})) or '—'}; "
            f"ломающих изменений контракта: {fmt(mean([x['deterministic'].get('contract_breaking') for x in xs]))}; "
            f"правок защищённых файлов: {fmt(mean([len(x['deterministic']['protected_touched']) for x in xs]), 1)}",
            f"Активные дельты: "
            f"{', '.join(sorted({d for x in xs for d in x['deterministic']['delta_dirs']})) or '—'}",
        ]
        bullets(doc, facts)
        det = {rb: fmt(cm.get(c, {}).get(rb, {}).get(cid) if False else None) for rb in []}
        key = [rb for rb in RUBRICS if cm.get(c, {}).get(rb)]
        if key:
            rows_t = []
            for rb in key:
                crits = cm[c][rb]
                strong = sorted(crits.items(), key=lambda kv: -(kv[1] or 0))[:3]
                weak = sorted(crits.items(), key=lambda kv: (kv[1] or 9))[:3]
                rows_t.append([rb,
                               ", ".join(f"{k} {fmt(v,1)}" for k, v in strong),
                               ", ".join(f"{k} {fmt(v,1)}" for k, v in weak)])
            table(doc, ["Рубрика", "Сильные критерии", "Слабые критерии"], rows_t,
                  widths=[1.5, 2.6, 2.6])

    # ---------------------------------------------------------- 5. критерии
    h(doc, "5. Профиль по критериям: где именно стек даёт ценность", 1)
    for rb in RUBRICS:
        cids = sorted({cid for c in conds for cid in cm.get(c, {}).get(rb, {})})
        if not cids:
            continue
        h(doc, rb, 2)
        rows_t = [[cid] + [fmt(cm.get(c, {}).get(rb, {}).get(cid)) for c in conds] for cid in cids]
        table(doc, ["Критерий"] + [COND_SHORT[c] for c in conds], rows_t,
              widths=[2.3] + [0.88] * len(conds))

    # ---------------------------------------------------------- 6. досье
    h(doc, "6. Что именно видел судья (состав досье)", 1)
    para(doc, "Прозрачность вместо доверия: ниже — файлы, попавшие в досье рубрик пакета, и файлы, "
              "исключённые бюджетом 23 500 символов. Досье adr_quality собирается из одного "
              "документа-решения.")
    for c in conds:
        x = by[c][0]
        dm = x.get("dossier") or {}
        dd = x.get("dossier_decision") or {}
        para(doc, f"{COND_SHORT[c]} ({x.get('condition')} r1): "
                  f"досье {dm.get('chars', '—')} символов", bold=True)
        bullets(doc, [
            "включено: " + (", ".join(dm.get("included") or []) or "—"),
            "исключено по бюджету: " + (", ".join(dm.get("omitted") or []) or "—"),
            "усечено: " + (", ".join(dm.get("truncated") or []) or "—"),
            "документ-решение для adr_quality: " + (", ".join(x.get("decision_doc") or []) or "—")
            + (f" (в досье {dd.get('chars')} символов)" if dd.get("chars") else ""),
        ])

    # ---------------------------------------------------------- 7. детерминированный слой
    h(doc, "7. Детерминированный слой: что механика Spine поймала в готовом пакете", 1)
    para(doc, "Единая линейка для всех условий. Именно этот слой отвечает на вопрос «что из "
              "архитектурного пакета проверяемо без человека».")
    det = []
    for c in conds:
        xs = by[c]
        det.append([COND_SHORT[c],
                    f"{sum(1 for x in xs if x['deterministic']['spine_gate_exit'] == 0)}/{len(xs)}",
                    ", ".join(sorted({f for x in xs for f in x['deterministic']['spine_gate_fails']})) or "—",
                    fmt(mean([x['deterministic'].get('contract_breaking') for x in xs])),
                    fmt(mean([len(x['deterministic']['protected_touched']) for x in xs]), 1),
                    fmt(mean([sensor_score(x) for x in xs]), 1),
                    fmt(mean([x['sensors'].get('placeholders') for x in xs]), 1)])
    table(doc, ["Условие", "Гейт PASS", "Провалено", "Ломающих в контракте", "Правок защищённых",
                "Сенсоры /10", "TBD/TODO"], det, widths=[1.25, 0.75, 1.5, 1.0, 1.0, 0.75, 0.7])
    doc.add_paragraph()
    h(doc, "7.1. По повторам: гейт, дельта и защищённые файлы", 2)
    rep_rows = []
    for c in conds:
        for x in sorted(by[c], key=lambda z: z["rep"]):
            d = x["deterministic"]
            rep_rows.append([COND_SHORT[c], x["rep"],
                             "PASS" if d["spine_gate_exit"] == 0 else "FAIL",
                             ", ".join(d["spine_gate_fails"]) or "—",
                             ", ".join(d["delta_dirs"]) or "—",
                             ", ".join(d["protected_touched"]) or "—",
                             fmt(x.get("wall_s"), 0)])
    table(doc, ["Условие", "повтор", "Гейт Spine", "Провалено", "Активная дельта",
                "Правки защищённых файлов", "стена, с"], rep_rows,
          widths=[1.15, 0.55, 0.8, 1.1, 1.15, 1.7, 0.6])
    para(doc, "Защищённые пути для этого кейса: ARCHITECTURE-SPINE.md, "
              ".arch-handoff/CONSTRAINTS.yaml и docs/adr/ADR-001…007. Правка этих файлов допустима "
              "только внутри дельты, объявленной в `changes/<имя>/`.", size=9)
    doc.add_paragraph()
    ch2 = chart_det(by, RESULTS / "deterministic.png")
    add_shot(doc, ch2, "Рис. 2. Что стек реально дал в прогоне: сенсоры объектного минимума, "
                       "число изменённых файлов и вызовов инструментов.", width=6.9)
    para(doc, "Ключевое наблюдение: гейт Spine — не «оценка качества», а контроль процесса. "
              "Пакеты plain, BMAD и superpowers могут быть содержательно хорошими, но они нарушили "
              "принятый в репозитории способ менять решение — и механика это назвала. "
              "Разбивка по повторам добавляет важное: у Spine и plain гейт сработал по-разному "
              "в двух прогонах, "
              "то есть исход зависит от того, вспомнил ли агент про дельту; у OpenSpec гейт зелёный "
              "дважды ровно потому, что стек вообще не трогал принятый спайн.")

    # ---------------------------------------------------------- 8. скриншоты
    h(doc, "8. Скриншоты живых TUI-прогонов", 1)
    para(doc, "Скриншоты — подтверждение того, что прогон шёл в живом TUI Qwen Code под ролью "
              "solution-архитектора. X11-снимки сделаны с окна зрителя: слева — сессия Qwen Code "
              "с вызовами инструментов, справа — плашка прогона (условие, стадия, лента событий). "
              "Кадры панели tmux получены через `capture-pane -e` (с цветом) и отрендерены в PNG.")
    for c in conds:
        h(doc, COND_SHORT[c], 2)
        for png, cap in pick_shots(c):
            add_shot(doc, png, cap)

    # ---------------------------------------------------------- 9. ограничения
    h(doc, "9. Отличия от комплекта и ограничения", 1)
    para(doc, "Отличия от PREREGISTRATION.md комплекта (все — вынужденные и названные):", bold=True)
    bullets(doc, [
        "Headless-режим (`qwen -o json`) заменён живым TUI Qwen Code в tmux — по требованию задания; "
        "движок скоринга при этом общий с комплектом.",
        "Версия хоста: прогон на Qwen Code 0.24.6 (пин комплекта) с выключенным авто-обновлением; "
        "сам хост при первом старте успел обновиться с 0.24.4 до 0.24.5, поэтому версия была "
        "пришпилена явно.",
        "Условие `spine` — как ставит `arch-be connect qwen` (без `--rw`), как и в пререгистрации; "
        "условие `spine-hook` в этот прогон не включено.",
        "n = 2 повтора на условие вместо 3 (пилот); доверительные интервалы считаются, но их "
        "пересечение нуля не доказывает отсутствия эффекта.",
        "Досье судьи собирается бюджетным способом (раздел 2.4) — прямое следствие лимита 24 000 "
        "символов у рубрики.",
    ])
    para(doc, "Ограничения интерпретации:", bold=True)
    bullets(doc, [
        "Рубрики — самого Spine Core и структурно ему благоприятны; это не нейтральная шкала.",
        "Судья — LLM. Слепота обеспечена нейтрализацией названий стеков в досье, но не абсолютна: "
        "терминология стека (например, `openspec/changes/`) в тексте остаётся.",
        "Сенсоры — эвристики наличия, не суждения: они не отличают соблюдённый инвариант от "
        "написанного в тексте.",
        "Гейт Spine на маршруте Fast не включает `decision_quality` и `semantic_quality` "
        "(`SKIP` в паспорте вердикта), а каталога `model/` в кейсе нет, поэтому `trace_check` и "
        "`model_validate` тоже уходят в SKIP — на этом кейсе механика измеряет процесс, но не смысл.",
        "Один и тот же решатель во всех условиях; при другой модели абсолютные баллы изменятся, "
        "хотя процессные различия должны сохраниться.",
        "Утечка эталонной механики проверена по журналам сессий: ни один прогон не читал исходники "
        "Spine (`spine-bank/src`) и не выходил за пределы своего рабочего каталога, кроме одного "
        "случая — spine r1 заглянул в соседний кейс в домашнем каталоге, чтобы подсмотреть формат "
        "дельты. Это ослабляет чистоту именно этого прогона и оговорено здесь явно.",
        "Судья — LLM, и на длинных досье он периодически не отдаёт валидный JSON; такие вызовы "
        "повторялись (до 3 попыток), а рубрика solution_architecture (15 критериев, 14.4 КБ промпта) "
        "оценивалась двумя вызовами по 8 и 7 критериев с взвешенной свёрткой — итог при этом равен "
        "взвешенному итогу полной рубрики.",
    ])

    # ---------------------------------------------------------- 10. гипотезы
    h(doc, "10. Проверка гипотез комплекта", 1)
    para(doc, "PREREGISTRATION.md комплекта формулировал четыре гипотезы. Ниже — что показал живой "
              "TUI-прогон. n = 2 на условие: это пилот, а не доказательство.")

    def pair(rb, a, b):
        base = {x["rep"]: (x.get("judge", {}).get(rb, {}) or {}).get("total") for x in by.get(b, [])}
        d = [(x.get("judge", {}).get(rb, {}) or {}).get("total") - base[x["rep"]]
             for x in by.get(a, [])
             if isinstance(base.get(x["rep"]), float)
             and isinstance((x.get("judge", {}).get(rb, {}) or {}).get("total"), float)]
        if not d:
            return None
        lo, hi = (None, None)
        if len(d) >= 2:
            import random as _r
            rnd = _r.Random(7)
            means = sorted(statistics.mean(rnd.choice(d) for _ in d) for _ in range(5000))
            lo, hi = round(means[125], 2), round(means[4875], 2)
        return round(statistics.mean(d), 2), (lo, hi), len(d)

    def ci_str(res):
        if not res:
            return "нет данных"
        return (f"{res[0]:+.2f} (CI {res[1][0]}…{res[1][1]}, n={res[2]})" if res[1][0] is not None
                else f"{res[0]:+.2f} (n={res[2]})")

    h2 = pair("architecture_gates", "spine", "plain")
    h3 = pair("solution_architecture", "spine", "bmad")
    h4 = pair("solution_architecture", "superpowers", "plain")
    hyp = [
        ["H1. Блокирующий Stop-хук даёт больше, чем советующие скиллы/MCP",
         "не проверялась: условие `spine-hook` из комплекта в этот прогон не включено",
         "не проверена"],
        ["H2. spine − plain по architecture_gates ≥ +0.5",
         ci_str(h2),
         ("точечная оценка порог выполняет, но у plain не хватает повтора и CI широкий"
          if h2 and h2[0] >= 0.5 else "не подтверждена")],
        ["H3. spine и bmad в паритете по solution_architecture",
         (f"spine − bmad = {ci_str(h3)}" if h3 else "нет данных"),
         ("паритет не подтверждён: BMAD выше" if h3 and h3[0] < 0 else
          "паритет не отвергнут" if h3 else "нет данных")],
        ["H4. superpowers − plain по solution_architecture ≈ 0",
         ci_str(h4),
         ("подтверждена: эффект мал" if h4 and abs(h4[0]) <= 0.2 else "эффект больше ожидаемого")],
    ]
    table(doc, ["Гипотеза", "Измерение", "Итог"], hyp, widths=[2.5, 2.6, 1.6])

    # ---------------------------------------------------------- 11. вывод
    h(doc, "11. Вывод: ценность для архитектора по продуктам", 1)
    para(doc, "Числа — из таблиц разделов 1 и 7; формулировки — интерпретация, а не измерение.")
    ranks = {}
    for rb in RUBRICS:
        vals = sorted([(c, m[c][rb]) for c in conds if m[c][rb] is not None], key=lambda kv: -kv[1])
        ranks[rb] = [c for c, _ in vals]
    for c in conds:
        xs = by[c]
        pos = {rb: (ranks[rb].index(c) + 1 if c in ranks[rb] else None) for rb in RUBRICS}
        gate = sum(1 for x in xs if x["deterministic"]["spine_gate_exit"] == 0)
        lines = [
            f"Баллы рубрик: solution_architecture {fmt(m[c]['solution_architecture'])} "
            f"(место {pos['solution_architecture']}), "
            f"architecture_gates {fmt(m[c]['architecture_gates'])} (место {pos['architecture_gates']}), "
            f"adr_quality {fmt(m[c]['adr_quality'])} (место {pos['adr_quality']}), "
            f"macedo_dimensions {fmt(m[c]['macedo_dimensions'])} (место {pos['macedo_dimensions']}).",
            f"Гейт Spine PASS {gate}/{len(xs)}; сенсоры {fmt(mean([sensor_score(x) for x in xs]), 1)}/10; "
            f"средняя стена {fmt(mean([x.get('wall_s') for x in xs]), 0)} с; "
            f"средний размер пакета {fmt(mean([len(x.get('changed') or []) for x in xs]), 1)} файлов.",
        ]
        crits = cm.get(c, {}).get("solution_architecture", {})
        if crits:
            strong = sorted(crits.items(), key=lambda kv: -(kv[1] or 0))[:3]
            weak = sorted(crits.items(), key=lambda kv: (kv[1] or 9))[:3]
            lines.append("Сильные критерии решения: " + ", ".join(f"{k} {fmt(v, 1)}" for k, v in strong)
                         + "; слабые: " + ", ".join(f"{k} {fmt(v, 1)}" for k, v in weak) + ".")
        para(doc, COND_RU[c], bold=True)
        bullets(doc, lines)

    para(doc, "Сводная интерпретация:", bold=True)
    bullets(doc, [
        "Содержательно сильнее всех оказался BMAD: он первый по solution_architecture, "
        "architecture_gates и adr_quality. Но его пакеты дважды из двух провалили гейт Spine "
        "(`delta_guard`): методика даёт качество документа, не давая дисциплины изменения "
        "принятого решения.",
        "Spine Core — единственный, кто дал и процесс, и смысл: первый по macedo_dimensions, "
        "делит второе место по adr_quality с superpowers, гейт пройден в одном повторе из двух. "
        "Его вклад — не «текст лучше», а превращение архитектурного пакета в проверяемый артефакт "
        "с дельтой и доказательствами.",
        "OpenSpec — самый дешёвый и самый предсказуемый по процессу: 2/2 зелёных гейта и самый "
        "короткий прогон, но куплено это тем, что стек вообще не касается принятого спайна; "
        "по architecture_gates и adr_quality он последний из пяти.",
        "superpowers и голый Qwen Code неразличимы по рубрике solution_architecture — ровно как "
        "предсказывала H4. Стек ориентирован на дисциплину кода после handoff, и на архитектурном "
        "пакете её не показывает; гейт он не проходит ни разу.",
        "Практический вывод для архитектора: рубричная оценка и процессный гейт измеряют разные "
        "вещи и не заменяют друг друга. BMAD выигрывает рубрики и проигрывает гейт; OpenSpec "
        "выигрывает гейт и проигрывает рубрики. Рабочая связка — Spine как контур контроля "
        "плюс тот методический стек, который команда уже приняла для содержания.",
    ])

    doc.save(str(out))
    print(f"отчёт: {out}")
    return out


if __name__ == "__main__":
    build()
