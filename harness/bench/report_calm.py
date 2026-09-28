#!/usr/bin/env python3
"""report_calm.py — отчёт .docx по сравнению Spine Core и FINOS CALM.

Движок тот же, что и в отчёте по четырём методическим стекам: живой TUI Qwen Code
под ролью solution-архитектора, единый детерминированный слой Spine и слепое
судейство по рубрикам Spine. Отличия: состав условий и раздел про родной контроль
CALM (`calm validate`), а также два плеча CALM — добровольное принятие и потолок.
"""
from __future__ import annotations

import random
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import report_docx as R  # noqa: E402

RESULTS = R.RESULTS
CONDS = ["plain", "spine", "calm", "calm-explicit"]
TITLE = "Живые прогоны в TUI Qwen Code: Spine Core против CALM"
# Короткие имена для таблиц, легенды и заголовков: два плеча CALM не должны сливаться.
R.COND_SHORT.update({"plain": "plain", "spine": "Spine Core",
                     "calm": "CALM (нейтрально)", "calm-explicit": "CALM (по просьбе)"})


def boot_ci(diffs, n=5000):
    if len(diffs) < 2:
        return None
    rnd = random.Random(7)
    means = sorted(statistics.mean(rnd.choice(diffs) for _ in diffs) for _ in range(n))
    return round(means[int(0.025 * n)], 2), round(means[int(0.975 * n)], 2)


def _pair(by, rb, a, b):
    base = {x["rep"]: (x.get("judge", {}).get(rb, {}) or {}).get("total") for x in by.get(b, [])}
    d = [(x.get("judge", {}).get(rb, {}) or {}).get("total") - base[x["rep"]]
         for x in by.get(a, [])
         if isinstance(base.get(x["rep"]), float)
         and isinstance((x.get("judge", {}).get(rb, {}) or {}).get("total"), float)]
    if not d:
        return None
    return round(statistics.mean(d), 2), boot_ci(d), len(d)


def build(out: Path | None = None) -> Path:
    rows = [r for r in R.load_rows() if r["condition"] in CONDS]
    by = R.group(rows)
    conds = [c for c in CONDS if c in by]
    out = out or (ROOT / "Spine_vs_CALM_live_TUI_report.docx")
    m = R.rubric_matrix(by)
    cm = R.criteria_matrix(by)

    doc = Document()
    R.set_base_style(doc)

    doc.add_heading(TITLE, 0)
    sub = doc.add_paragraph()
    run = sub.add_run("Ценность для solution-архитектора по рубрикам Spine Core")
    run.bold = True
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0x1F, 0x6F, 0xEB)
    doc.add_paragraph()
    meta = [
        f"Дата отчёта: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "Кейс: spine-bank, «кейсы/sbp-gateway» — платёжный шлюз СБП (C2B-приём); "
        "brownfield-изменение «СБП-подписки» (рекуррентные C2B-списания по согласию плательщика)",
        "Роль агента: solution-архитектор банка (задание TASK.md комплекта spine-qwen-bench-kit, "
        "одинаковое для всех условий)",
        f"Хост прогона: Qwen Code 0.24.6 в живом TUI (tmux-сессия), "
        f"решатель — {rows[0].get('solver') if rows else '—'}",
        f"Судейство: {rows[0].get('judge_model') if rows else '—'} — другое семейство моделей; "
        f"слепое досье (названия продуктов нейтрализованы), 4 рубрики Spine, 3 сэмпла на критерий",
        "Условия: Spine Core 0.3.11 (`arch-be connect qwen`), CALM 1.60.1 в двух плечах "
        "(нейтральное задание и явная просьба смоделировать), контроль — голый Qwen Code",
        f"Прогонов: {len(rows)}; каждый — отдельная живая TUI-сессия в обезличенном "
        f"рабочем каталоге (агент не видит по пути, какой продукт проверяется)",
        "Артефакты: live-tui/results-clean/live.jsonl, live-tui/runs-clean/cells/*, live-tui/frames-clean/*",
    ]
    for x in meta:
        p = doc.add_paragraph(x, style="List Bullet")
        for rr in p.runs:
            rr.font.size = Pt(9.5)

    # ------------------------------------------------------------------ 1
    R.h(doc, "1. Резюме", 1)
    R.para(doc, "Spine Core и FINOS CALM решали одно и то же задание в живом TUI Qwen Code под ролью "
                "solution-архитектора банка. Spine — контур архитектурного контроля (спайн, реестр "
                "правил, дельты, evidence, единый гейт). CALM — язык описания архитектуры как кода "
                "(узлы, интерфейсы, связи, потоки, контроли, паттерны) со своим валидатором.")
    res = []
    for c in conds:
        xs = by[c]
        res.append([R.COND_SHORT[c]] + [R.fmt(m[c][rb]) for rb in R.RUBRICS]
                   + [f"{sum(1 for x in xs if x['deterministic']['spine_gate_exit'] == 0)}/{len(xs)}"]
                   + [R.fmt(R.mean([R.sensor_score(x) for x in xs]), 1)]
                   + [R.fmt(R.mean([x["wall_s"] for x in xs]), 0)])
    R.table(doc, ["Условие"] + [rb.replace("_", "_\n") for rb in R.RUBRICS]
            + ["гейт\nSpine", "сенсоры\n/10", "стена,\nс"], res,
            widths=[1.7, 0.85, 0.85, 0.85, 0.85, 0.55, 0.55, 0.55])
    R.para(doc, "Условия: " + "; ".join(R.COND_RU[c] for c in conds) + ".", size=9)
    doc.add_paragraph()
    ch = R.chart(by, RESULTS / "calm-rubrics.png")
    R.add_shot(doc, ch, "Рис. 1. Итоги по рубрикам Spine: Spine Core, CALM (нейтрально), "
                        "CALM (по явной просьбе) и контроль. Красная линия — порог 3.5.", width=6.9)
    R.para(doc, "Три главных факта прогона. Первый: CALM в нейтральном задании дал пакет, который "
                "судья оценил не ниже Spine — выше по solution_architecture (3.69 против 3.55), "
                "architecture_gates (3.45 против 3.34) и macedo_dimensions (4.12 против 3.92); Spine "
                "взял только adr_quality (3.65 против 3.11). Второй: ни один продукт не удержал "
                "процессный гейт стабильно — Spine провалил его в обоих повторах, CALM тоже, и лишь "
                "по одному повтору прошли контроль и CALM-по-просьбе. Третий: когда архитектор прямо "
                "просит модель CALM, пакет становится дороже (1036 с против 659 с) и по рубрикам не "
                "лучше, а по architecture_gates даже хуже — но именно тогда появляется машинно "
                "проверяемый артефакт, который родной валидатор CALM принимает без ошибок и "
                "предупреждений.")

    # ------------------------------------------------------------------ 2
    R.h(doc, "2. Метод", 1)
    R.para(doc, "Движок тот же, что в прогоне четырёх методических стеков: то же задание, тот же кейс, "
                "тот же детерминированный слой и та же слепая рубричная оценка.")
    R.h(doc, "2.1. Условия", 2)
    inv_rows = []
    for c in conds:
        inv = by[c][0].get("inventory", {})
        inv_rows.append([R.COND_RU[c], inv.get("project_skills", 0), inv.get("extension_skills", 0),
                         ", ".join(inv.get("mcp_servers") or []) or "—",
                         R.fmt(R.mean([x.get("wall_s") for x in by[c]]), 0),
                         ", ".join(str(x.get("dialogs_answered", 0)) for x in by[c])])
    R.table(doc, ["Условие", "скиллов\nпроекта", "скиллов\nрасшир.", "MCP", "стена, с",
                  "гейт человека\n(ответов)"], inv_rows,
            widths=[2.3, 0.8, 0.8, 0.8, 0.8, 1.1])
    R.h(doc, "2.2. Как ставился CALM", 2)
    R.bullets(doc, [
        "CLI ставится локально с пином версии: `npm i --no-save --no-package-lock "
        "@finos/calm-cli@1.60.1`; бинарь доступен как `node_modules/.bin/calm` и добавлен в PATH "
        "сессии (одинаково для всех условий).",
        "Затем — родной установщик AI-поддержки: `npx calm init-ai --provider claude`. Он создаёт "
        "скилл CALM и 14 файлов-промптов (узлы, интерфейсы, связи, потоки, контроли, паттерны, "
        "метаданные, таймлайны, документация, стандарты).",
        "`calm init-ai` не поддерживает провайдера `qwen` (доступны copilot, kiro, claude, codex). "
        "Тот же скилл без изменений перенесён туда, где его видит Qwen Code — в `.qwen/skills/calm/`.",
        "Родной контроль CALM в скоринге: `calm validate` по созданной архитектуре (и по паттерну, "
        "если он есть). Если в репозитории есть карта «внешний URL → локальная схема», валидатор "
        "вызывается с ней — это штатный способ CALM работать с внешними requirement-схемами.",
    ])
    R.h(doc, "2.3. Слепой прогон: что пришлось исправить", 2)
    R.para(doc, "Первый заход на CALM дал результат, который пришлось признать недействительным: "
                "рабочий каталог ячейки назывался по условию (`runs/cells/calm-r1/ws`), и агент это "
                "заметил. В журнале сессии он прямо рассуждает: «путь calm-r1 подсказывает, что это "
                "ячейка бенчмарка, проверяющая CALM». После этого прогон был перезапущен заново с "
                "обезличенными каталогами (`runs-clean/cells/wgmujp6` и т. п.), а карта соответствия "
                "условий вынесена за пределы рабочего пространства — агент её не видит. Все числа в "
                "этом отчёте взяты из чистого прогона; условия Spine и контроль перезапущены вместе "
                "с CALM, чтобы линейка была одной.")
    R.h(doc, "2.4. Роль человека в прогоне", 2)
    R.para(doc, "Интерактивный гейт `AskUserQuestion` не подавляется: когда агент решает уточнить "
                "границу задачи у архитектора, роль архитектора отвечает вариантом «Recommended», и "
                "каждый такой ответ виден в ленте событий прогона и в скриншотах. В чистом прогоне "
                "ни один агент вопросов не задавал (в первом заходе CALM задавал — это видно "
                "в сохранённых кадрах).")
    R.h(doc, "2.5. Оценка", 2)
    R.bullets(doc, [
        "Детерминированный слой — единый для всех: `arch-be gate --repo . --base <baseline>` "
        "(fitness, delta guard, анти-ослабление правил, линтер спайна, трассировка), `contract-diff`, "
        "правки защищённых файлов, сенсоры объектного минимума.",
        "Смысловой слой — слепой судья другого семейства моделей; в досье нейтрализуются названия "
        "продуктов, в том числе CALM → MODEL-LANG, FINOS → FOUNDATION.",
        "Досье ограничено 23 500 символами: механика Spine отказывается оценивать текст длиннее "
        "24 000 символов (ADR-004), а живой пакет — 50–110 КБ. Состав досье по каждому условию "
        "приведён в разделе 6.",
    ])

    # ------------------------------------------------------------------ 3
    R.h(doc, "3. Рубрики Spine, по которым сравниваются продукты", 1)
    for rb in R.RUBRICS:
        R.h(doc, R.RUBRIC_RU[rb], 2)
    R.para(doc, "Шкала 1–5, взвешенный итог. Рубрики — самого Spine Core, поэтому структурно "
                "благоприятны ему. Для CALM это ограничение работает против него: его сила — "
                "в машинной проверяемости модели, а рубрики оценивают текст пакета.")

    # ------------------------------------------------------------------ 4
    R.h(doc, "4. Результаты по условиям", 1)
    for c in conds:
        xs = by[c]
        R.h(doc, R.COND_RU[c], 2)
        calmv = [x["deterministic"].get("calm_validate_exit") for x in xs
                 if x["deterministic"].get("calm_validate_exit") is not None]
        facts = [
            f"Повторов: {len(xs)}; ход завершён без таймаута: {sum(1 for x in xs if x.get('turn_ok'))}/{len(xs)}; "
            f"стена: {R.fmt(R.mean([x.get('wall_s') for x in xs]), 0)} с",
            "Рубрики Spine: " + " · ".join(f"{rb} = {R.fmt(m[c][rb])}" for rb in R.RUBRICS),
            f"Вызовов инструментов: {R.fmt(R.mean([x.get('tool_calls') for x in xs]), 0)}; "
            f"файлов изменено: {R.fmt(R.mean([len(x.get('changed') or []) for x in xs]), 1)}; "
            f"объём текста: {R.fmt(R.mean([x['sensors'].get('chars') for x in xs]), 0)} знаков; "
            f"сенсоры: {R.fmt(R.mean([R.sensor_score(x) for x in xs]), 1)}/10",
            f"Гейт Spine: PASS {sum(1 for x in xs if x['deterministic']['spine_gate_exit'] == 0)}/{len(xs)}; "
            f"провалы: {', '.join(sorted({f for x in xs for f in x['deterministic']['spine_gate_fails']})) or '—'}; "
            f"правок защищённых файлов: {R.fmt(R.mean([len(x['deterministic']['protected_touched']) for x in xs]), 1)}; "
            f"активные дельты: {', '.join(sorted({d for x in xs for d in x['deterministic']['delta_dirs']})) or '—'}",
            ("Родной контроль CALM (`calm validate`): "
             + ", ".join("PASS" if v == 0 else f"FAIL(exit {v})" for v in calmv)) if calmv
            else "Родной контроль CALM: модель CALM не создавалась — проверять нечего",
        ]
        R.bullets(doc, facts)
        crits = cm.get(c, {}).get("solution_architecture", {})
        if crits:
            strong = sorted(crits.items(), key=lambda kv: -(kv[1] or 0))[:4]
            weak = sorted(crits.items(), key=lambda kv: (kv[1] or 9))[:4]
            R.para(doc, "Сильные критерии решения: " + ", ".join(f"{k} {R.fmt(v, 1)}" for k, v in strong))
            R.para(doc, "Слабые критерии решения: " + ", ".join(f"{k} {R.fmt(v, 1)}" for k, v in weak))
        rows_t = []
        for x in sorted(xs, key=lambda z: z["rep"]):
            ch_files = [ln.split("\t")[-1] for ln in (x.get("changed") or [])]
            rows_t.append([f"r{x['rep']}", R.fmt(x.get("wall_s"), 0), len(ch_files),
                           ", ".join(ch_files[:5]) + (" …" if len(ch_files) > 5 else "")])
        R.table(doc, ["повтор", "стена, с", "файлов", "изменённые файлы"], rows_t,
                widths=[0.5, 0.6, 0.5, 5.2])

    # ------------------------------------------------------------------ 5
    R.h(doc, "5. Профиль по критериям: где именно продукт даёт ценность", 1)
    for rb in R.RUBRICS:
        cids = sorted({cid for c in conds for cid in cm.get(c, {}).get(rb, {})})
        if not cids:
            continue
        R.h(doc, rb, 2)
        rows_t = [[cid] + [R.fmt(cm.get(c, {}).get(rb, {}).get(cid)) for c in conds] for cid in cids]
        R.table(doc, ["Критерий"] + [R.COND_SHORT[c] for c in conds], rows_t,
                widths=[2.1] + [0.95] * len(conds))

    # ------------------------------------------------------------------ 6
    R.h(doc, "6. Что именно видел судья (состав досье)", 1)
    for c in conds:
        x = by[c][0]
        dm = x.get("dossier") or {}
        dd = x.get("dossier_decision") or {}
        R.para(doc, f"{R.COND_SHORT[c]}: досье {dm.get('chars', '—')} символов", bold=True)
        R.bullets(doc, [
            "включено: " + (", ".join(dm.get("included") or []) or "—"),
            "исключено по бюджету: " + (", ".join(dm.get("omitted") or []) or "—"),
            "усечено: " + (", ".join(dm.get("truncated") or []) or "—"),
            "документ-решение для adr_quality: " + (", ".join(x.get("decision_doc") or []) or "—")
            + (f" (досье {dd.get('chars')} символов)" if dd.get("chars") else ""),
        ])

    # ------------------------------------------------------------------ 7
    R.h(doc, "7. Детерминированный слой и родной контроль", 1)
    R.para(doc, "Единая линейка для всех условий — гейт Spine. У CALM есть и своя линейка, "
                "валидатор модели, поэтому она приведена отдельным столбцом: это единственное "
                "измерение в отчёте, где CALM оценивает сам себя, а не Spine.")
    det = []
    for c in conds:
        xs = by[c]
        cv = [x["deterministic"].get("calm_validate_exit") for x in xs
              if x["deterministic"].get("calm_validate_exit") is not None]
        det.append([R.COND_SHORT[c],
                    f"{sum(1 for x in xs if x['deterministic']['spine_gate_exit'] == 0)}/{len(xs)}",
                    ", ".join(sorted({f for x in xs for f in x['deterministic']['spine_gate_fails']})) or "—",
                    R.fmt(R.mean([len(x['deterministic']['protected_touched']) for x in xs]), 1),
                    R.fmt(R.mean([R.sensor_score(x) for x in xs]), 1),
                    (", ".join("PASS" if v == 0 else f"FAIL({v})" for v in cv) if cv
                     else "модели нет")])
    R.table(doc, ["Условие", "Гейт Spine", "Провалено", "Правок защищённых", "Сенсоры /10",
                  "`calm validate`"], det, widths=[1.35, 0.85, 1.5, 1.1, 0.8, 1.0])
    doc.add_paragraph()
    R.para(doc, "Разбивка по повторам:", bold=True)
    rep_rows = []
    for c in conds:
        for x in sorted(by[c], key=lambda z: z["rep"]):
            d = x["deterministic"]
            rep_rows.append([R.COND_SHORT[c], x["rep"],
                             "PASS" if d["spine_gate_exit"] == 0 else "FAIL",
                             ", ".join(d["spine_gate_fails"]) or "—",
                             ", ".join(d["delta_dirs"]) or "—",
                             ", ".join(d["protected_touched"]) or "—",
                             ("PASS" if d.get("calm_validate_exit") == 0
                              else (f"FAIL({d['calm_validate_exit']})"
                                    if d.get("calm_validate_exit") is not None else "—"))])
    R.table(doc, ["Условие", "повтор", "Гейт Spine", "Провалено", "Дельта",
                  "Правки защищённых", "`calm validate`"], rep_rows,
            widths=[1.05, 0.5, 0.75, 0.95, 1.0, 1.45, 0.9])
    for c in conds:
        for x in by[c]:
            tail = (x["deterministic"].get("calm_validate_tail") or "").strip()
            if tail:
                R.para(doc, f"{R.COND_SHORT[c]} r{x['rep']}: вывод `calm validate`", bold=True)
                p = doc.add_paragraph()
                r = p.add_run(tail[-600:])
                r.font.size = Pt(7.5)
                r.font.name = "Consolas"
    ch2 = R.chart_det(by, RESULTS / "calm-deterministic.png")
    R.add_shot(doc, ch2, "Рис. 2. Что продукт реально дал в прогоне: сенсоры объектного минимума, "
                         "число изменённых файлов и вызовов инструментов.", width=6.9)

    # ------------------------------------------------------------------ 8
    R.h(doc, "8. Принятие против потолка: два плеча CALM", 1)
    R.para(doc, "Это главный результат сравнения. CALM измерялся дважды на одном и том же стеке: "
                "с нейтральным заданием (как в остальных условиях) и с явной просьбой архитектора "
                "смоделировать изменение на языке CALM и провалидировать модель.")
    R.bullets(doc, [
        "Нейтральное задание (`calm`): агент вызвал скилл CALM, прочитал все 14 файлов-промптов, "
        "проверил, есть ли в репозитории CALM-модели, не нашёл их и оформил пакет в нативной "
        "конвенции репозитория (ADR + solutioning + NFR + контракты). Ни одной CALM-модели "
        "не создано, ни одного вызова `calm validate`. В обоих повторах.",
        "Явная просьба (`calm-explicit`): агент создал модель `docs/calm/*.architecture.json` "
        "с узлами, связями, потоками и контролем, сгенерировал requirement-схемы контролей и "
        "карту `url-mapping.json`, и провёл валидацию. В обоих повторах.",
        "Цена потолка: 1036 с против 659 с (в 1.6 раза дольше) и 15–17 изменённых файлов против 11.",
        "Баллы рубрик при этом не выросли: solution_architecture 3.44 против 3.69, "
        "architecture_gates 3.15 против 3.45, macedo_dimensions 3.75 против 4.12, adr_quality "
        "3.30 против 3.11. Рубрики Spine измеряют текст пакета; модель CALM его не улучшает "
        "и частично вытесняет из досье.",
        "Зато появляется то, чего нет ни у одного другого условия: машинно проверяемый артефакт. "
        "`calm validate` по обеим моделям — PASS, без ошибок и предупреждений.",
    ])
    R.para(doc, "Отдельная находка, добытая в прогоне: валидация контролей CALM не проходит «из "
                "коробки». Агент сначала сослался на внешние requirement-схемы и получил отказ "
                "валидатора: «Direct URL loading is restricted to approved hosts. Host "
                "schemas.bank.ru is not allowlisted». Он нашёл штатное решение — карту "
                "`url-mapping.json` (внешний URL → локальная схема) — и только с ней получил PASS. "
                "Это реальная шероховатость внедрения CALM, видимая архитектору сразу.", italic=True)

    # ------------------------------------------------------------------ 9
    R.h(doc, "9. Скриншоты живых TUI-прогонов", 1)
    R.para(doc, "Подтверждение того, что прогон шёл в живом TUI Qwen Code под ролью "
                "solution-архитектора. X11-снимки сделаны с окна зрителя: слева — сессия Qwen Code, "
                "справа — плашка прогона. Кадры панели tmux получены через `capture-pane -e` "
                "и отрендерены в PNG без дорисовки.")
    for c in conds:
        R.h(doc, R.COND_SHORT[c], 2)
        for png, cap in R.pick_shots(c):
            R.add_shot(doc, png, cap)

    # ------------------------------------------------------------------ 10
    R.h(doc, "10. Парное сравнение", 1)
    R.para(doc, "Разность средних по повторам и bootstrap 95% CI парной разности (n = 2 — пилот).")
    for a, b in (("spine", "calm"), ("calm", "calm-explicit"), ("spine", "plain")):
        R.para(doc, f"{R.COND_SHORT[a]} − {R.COND_SHORT[b]}", bold=True)
        rows_t = []
        for rb in R.RUBRICS:
            p = _pair(by, rb, a, b)
            rows_t.append([rb, R.fmt(m[a][rb]), R.fmt(m[b][rb]),
                           (f"{p[0]:+.2f}" if p else "—"),
                           (f"{p[1][0]:+.2f}…{p[1][1]:+.2f}" if p and p[1] else "—")])
        R.table(doc, ["Рубрика", R.COND_SHORT[a], R.COND_SHORT[b], "разность", "95% CI"], rows_t,
                widths=[1.9, 0.85, 0.85, 0.9, 1.3])
        doc.add_paragraph()
    summary = []
    for c in conds:
        xs = by[c]
        summary.append(f"{R.COND_SHORT[c]}: гейт Spine "
                       f"{sum(1 for x in xs if x['deterministic']['spine_gate_exit'] == 0)}/{len(xs)}, "
                       f"правок защищённых файлов "
                       f"{R.fmt(R.mean([len(x['deterministic']['protected_touched']) for x in xs]), 1)}, "
                       f"стена {R.fmt(R.mean([x['wall_s'] for x in xs]), 0)} с")
    R.bullets(doc, summary)

    # ------------------------------------------------------------------ 11
    R.h(doc, "11. Ограничения и честные оговорки", 1)
    R.bullets(doc, [
        "Рубрики — самого Spine Core и структурно благоприятны ему. Сравнение по ним честно "
        "показывает, что CALM не проигрывает по тексту пакета, но не измеряет его главную "
        "способность — машинную проверяемость модели; её измеряет только `calm validate`.",
        "n = 2 на условие — пилот. Доверительные интервалы приведены; их пересечение нуля "
        "не доказывает отсутствия эффекта, а узкий интервал при n = 2 — не сила, а артефакт.",
        "Судья — LLM: он видит текст досье и не отличает соблюдённый инвариант от написанного. "
        "Слепота обеспечена нейтрализацией названий продуктов, но не абсолютна.",
        "`calm init-ai` не поддерживает Qwen; скилл перенесён в `.qwen/skills/` без изменений — "
        "это адаптация установки, а не изменение продукта.",
        "На маршруте Fast гейт Spine не включает `decision_quality` и `semantic_quality` "
        "(`SKIP` в паспорте вердикта), а каталога `model/` в кейсе нет, поэтому `trace_check` и "
        "`model_validate` тоже уходят в SKIP: на этом кейсе механика измеряет процесс, но не смысл.",
        "Досье судьи собирается бюджетным способом (лимит 24 000 символов у рубрики). Для плеча "
        "`calm-explicit` это означает, что часть бюджета занята мелкими requirement-файлами CALM — "
        "побочный эффект того, что продукт порождает много маленьких машинных артефактов.",
        "Первый заход на CALM был признан недействительным из-за утечки имени условия в путь "
        "рабочего каталога и перезапущен; в отчёте — только чистый прогон.",
    ])

    # ------------------------------------------------------------------ 12
    R.h(doc, "12. Вывод: ценность для архитектора", 1)
    R.para(doc, "Числа — из таблиц разделов 1, 8 и 10; формулировки — интерпретация.")
    for c in conds:
        xs = by[c]
        gate = sum(1 for x in xs if x["deterministic"]["spine_gate_exit"] == 0)
        R.para(doc, R.COND_RU[c], bold=True)
        R.bullets(doc, [
            "Баллы рубрик: " + " · ".join(f"{rb} {R.fmt(m[c][rb])}" for rb in R.RUBRICS)
            + f"; гейт Spine PASS {gate}/{len(xs)}; сенсоры "
              f"{R.fmt(R.mean([R.sensor_score(x) for x in xs]), 1)}/10; стена "
              f"{R.fmt(R.mean([x['wall_s'] for x in xs]), 0)} с.",
        ])
    R.para(doc, "Что это значит по продуктам:", bold=True)
    R.bullets(doc, [
        "Spine Core покупает управляемость изменения: спайн, реестр правил с владельцами и "
        "сроками, дельта вместо прямой правки, evidence-бандл, объяснимый вердикт гейта. В этом "
        "прогоне он дал лучший adr_quality (3.65) — самую сильную рубрику по дисциплине решения — "
        "и остался самым быстрым (562 с). Но процессный контур не сработал сам собой: оба повтора "
        "провалили `delta_guard`, потому что агент правил спайн напрямую. Инструмент не заменяет "
        "дисциплину, он её проверяет.",
        "CALM покупает проверяемую модель: архитектура описывается структурой (узлы, интерфейсы, "
        "связи, потоки, контроли), которую родной валидатор принимает или отклоняет, а из модели "
        "генерируются диаграммы и документация. Это единственная в сравнении ценность, которая "
        "не зависит от честности текста: `calm validate` — механика, а не рубрика.",
        "Но у этой ценности высокая цена входа. В нейтральном задании CALM не был применён вообще: "
        "агент прочитал все промпты CALM и всё равно оформил пакет в конвенции репозитория. Модель "
        "появилась только тогда, когда архитектор попросил прямо, и стоила на 60 % больше времени, "
        "не улучшив рубрики Spine. Итог: CALM — не «улучшатель» архитектурного пакета, а отдельный "
        "артефакт со своей дисциплиной; вводить его нужно решением архитектора, а не ожиданием, "
        "что агент сам догадается.",
        "Практическая связка для банковского контура: Spine держит процесс и доказательства "
        "изменения, CALM — форму самой архитектуры. Они не конкурируют: Spine отвечает на вопрос "
        "«можно ли выпускать это изменение», CALM — на вопрос «та ли это архитектура».",
    ])

    doc.save(str(out))
    print(f"отчёт: {out}")
    return out


if __name__ == "__main__":
    build()
