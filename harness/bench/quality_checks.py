#!/usr/bin/env python3
"""quality_checks.py — надёжность судьи и проверка слепоты (руководство v2, §4.5).

1. `reliability` — 10 случайных досье судятся повторно; считается средняя абсолютная
   разность итогов и ρ Спирмена между первым и повторным судейством.
2. `blind` — судье показывают досье и просят угадать, каким инструментом сделан пакет
   (четыре стека или «без инструмента»); доля угадываний сравнивается со случайной 25 %.

Запуск:
  python3 quality_checks.py reliability [n]
  python3 quality_checks.py blind [n]
"""
from __future__ import annotations

import json
import os
import pathlib
import random
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
KIT = ROOT.parent / "spine-qwen-bench-kit" / "kit"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(KIT))

import envutil  # noqa: E402
import bench  # noqa: E402
from stacks import base_env, sh  # noqa: E402

REAL_HOME = Path(os.path.expanduser("~"))


def judge_env():
    env = base_env(str(REAL_HOME))
    env.update(envutil.judge_key_env())
    return env


def rows():
    f = bench.RESULTS / "live.jsonl"
    return [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]


def spearman(a, b):
    def rank(x):
        order = sorted(range(len(x)), key=lambda i: x[i])
        r = [0.0] * len(x)
        for pos, i in enumerate(order):
            r[i] = pos + 1
        return r
    ra, rb = rank(a), rank(b)
    ma, mb = statistics.mean(ra), statistics.mean(rb)
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = (sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb)) ** 0.5
    return round(num / den, 3) if den else None


def reliability(n=10, rubric="solution_architecture"):
    cfg = bench.judge_config()
    env = judge_env()
    rs = [r for r in rows() if (r.get("judge", {}).get(rubric, {}) or {}).get("total") is not None]
    rnd = random.Random(20260928)
    pick = rnd.sample(rs, min(n, len(rs)))
    pairs = []
    for r in pick:
        cell = bench.cell_dir(r["condition"], r["rep"])
        token = r.get("judge_token")
        dos = bench.RUNS / "judging" / f"dossier-package-{token}.md"
        if not dos.exists():
            continue
        res = bench._run_rubric("solution_architecture_part_a", dos, cfg, env, attempts=2)
        if res.get("total") is None:
            continue
        first = (r["judge"][rubric].get("parts") or {}).get("solution_architecture_part_a", {}).get("total")
        if first is None:
            first = r["judge"][rubric]["total"]
        pairs.append((r["condition"], r["rep"], first, res["total"]))
    out = ["# Надёжность судьи (повторное судейство)",
           "",
           f"Повторно оценено досье: {len(pairs)}; рубрика: `{rubric}` (часть A, 8 критериев).", ""]
    if pairs:
        d = [abs(a - b) for _, _, a, b in pairs]
        rho = spearman([a for _, _, a, _ in pairs], [b for _, _, _, b in pairs])
        out += [f"Средняя абсолютная разность итогов: **{statistics.mean(d):.2f}** "
                f"(медиана {statistics.median(d):.2f}); ρ Спирмена: **{rho}**.", "",
                "| условие | повтор | первый итог | повторный итог | разность |", "|---|---|---|---|---|"]
        out += [f"| {c} | {r} | {a:.2f} | {b:.2f} | {b - a:+.2f} |" for c, r, a, b in pairs]
    else:
        out.append("Повторных оценок не получилось (судья не отдал валидный ответ).")
    (bench.RESULTS / "judge-reliability.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


BLIND_PROMPT = """Ты — архитектурный эксперт. Ниже — архитектурный пакет изменения банковской системы.
Пакет сделан одним из пяти способов:
  A — без методического инструмента (голый агент);
  B — со стеком требований/спецификаций (openspec);
  C — со стеком ролевого планирования (bmad);
  D — со стеком дисциплины разработки (superpowers);
  E — с доменным архитектурным харнессом (spine).

Ответь ТОЛЬКО JSON: {"guess": "A|B|C|D|E", "confidence": 0..1, "why": "до 200 символов"}.
Угадывай даже при низкой уверенности.

--- ДОСЬЕ ---
"""


def blind(n=10):
    cfg = Path(bench.RUNS / "judge.toml")
    env = judge_env()
    rs = rows()
    rnd = random.Random(7)
    pick = rnd.sample(rs, min(n, len(rs)))
    # Судья живёт на локальном шлюзе (см. runs-v2/judge.toml), а не на эндпоинте решателя.
    api = "http://localhost:8787/v1"
    key = env.get("ZHIPU_API_KEY") or ""
    out = ["# Проверка слепоты судьи", "",
           "Судье показывают досье и просят угадать инструмент (5 вариантов). "
           "Случайный уровень — 20 % (25 % при четырёх стеках без «голого»).", "",
           "| условие | досье | ответ судьи | верно |", "|---|---|---|---|"]
    hits = tot = 0
    import urllib.request
    mapping = {"plain": "A", "openspec": "B", "bmad": "C", "superpowers": "D",
               "spine": "E", "plain+spine": "E"}
    for r in pick:
        token = r.get("judge_token")
        dos = bench.RUNS / "judging" / f"dossier-package-{token}.md"
        if not dos.exists():
            continue
        text = (BLIND_PROMPT + dos.read_text(encoding="utf-8")[:20000])
        body = {"model": bench.JUDGE_MODEL,
                "messages": [{"role": "user", "content": text}], "temperature": 0}
        req = urllib.request.Request(api.rstrip("/") + "/chat/completions",
                                     data=json.dumps(body).encode(), method="POST",
                                     headers={"Content-Type": "application/json",
                                              "Authorization": "Bearer " + key})
        try:
            import urllib.error
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.load(resp)
            ans = (data["choices"][0]["message"]["content"] or "").strip()
            guess = json.loads(ans[ans.index("{"):ans.rindex("}") + 1]).get("guess", "?")
        except Exception as e:  # noqa: BLE001
            guess = f"ошибка: {e}"
        expect = mapping.get(r["condition"].split("+")[0], "?")
        ok = (guess == expect)
        hits += ok
        tot += 1
        out.append(f"| {r['condition']} r{r['rep']} | {token} | {guess} | {'да' if ok else 'нет'} |")
    out += ["", f"Угадано {hits} из {tot} = {hits / tot:.0%} при случайном уровне 20 %."
            if tot else "Нет данных.", ""]
    (bench.RESULTS / "blindness.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "reliability"
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    {"reliability": reliability, "blind": blind}[cmd](k)
