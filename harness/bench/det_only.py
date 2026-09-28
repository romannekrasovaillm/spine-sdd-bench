#!/usr/bin/env python3
"""det_only.py — досчитать ТОЛЬКО детерминированный слой для ячеек без score.json.

Нужно для полноты публичного репозитория: у пилота и у ранних прогонов CALM
судья не запускался, но исход гейта (gate_class) измерим и его надо показать.

Запуск:
  BENCH_RUNS=runs-v2-pilot BENCH_OPAQUE=1 python3 det_only.py <conditions>
"""
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "spine-qwen-bench-kit" / "kit"))

import bench  # noqa: E402
from live_v2_helpers import gate_class, hook_blocks, contamination  # noqa: E402


def main(conds: list[str], reps: int) -> None:
    mp = bench.RUNS / "cell-map.json"
    m = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else None
    for cond in conds:
        for r in range(1, reps + 1):
            key = f"{cond}-r{r}"
            if m is not None and key not in m:
                continue
            d = bench.cell_dir(cond, r)
            if not (d / "meta.json").exists():
                continue
            if (d / "score.json").exists():
                print(f"{key}: уже есть score.json")
                continue
            meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
            ws = str(d / "ws")
            files = bench.agent_files(ws, meta["base_sha"])
            det = bench.deterministic(ws, meta["base_sha"])
            sc = {
                "files": files,
                "sensors": bench.sensors(ws, files),
                "deterministic": det,
                "gate_class": gate_class(det),
                "hook_blocks": hook_blocks(str(d / "home")),
                "contamination": contamination(
                    str(d / "home"), ws,
                    forbidden_roots=[bench.SPINE_BANK, bench.CELLS, bench.CASE, bench.REAL_HOME],
                    allow=[bench.REAL_HOME / "bin", bench.REAL_HOME / ".npm-global",
                           bench.REAL_HOME / ".nvm"]),
                "judge": {},
                "note": "только детерминированный слой: судья для этой кампании не запускался",
            }
            (d / "score.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"{key}: gate_class={sc['gate_class']} (судья не запускался)")


if __name__ == "__main__":
    conds = sys.argv[1].split(",") if len(sys.argv) > 1 else []
    main(conds, int(os.environ.get("REPS", "3")))
