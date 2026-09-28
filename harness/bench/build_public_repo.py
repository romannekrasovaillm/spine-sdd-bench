#!/usr/bin/env python3
"""build_public_repo.py — собрать чистый публичный репозиторий из результатов всех прогонов.

Что делает:
  * собирает кампании (v1, v1-clean, calm, pilot-v2, v2) в единый каталог;
  * копирует по каждому прогону meta/score/артефакты агента/транскрипт;
  * рендерит кадры живого TUI в PNG (из capture-pane, без зависимости от X);
  * санитизирует абсолютные пути и имена окружения;
  * строит сводные CSV и графики;
  * НИЧЕГО не пишет в исходные каталоги прогонов.

Запуск: python3 build_public_repo.py [--out DIR]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
KIT = ROOT.parent / "spine-qwen-bench-kit" / "kit"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(KIT))

import shots  # noqa: E402
from stacks import parse_condition  # noqa: E402
from live_v2_helpers import gate_class  # noqa: E402

CAMPAIGNS = [
    # имя, каталог прогонов, каталог результатов, каталог кадров, заголовок
    ("v2", "runs-v2", "results-v2", "frames-v2",
     "v2 — факторная сетка «4 стека × 3 режима Spine», n = 3"),
    ("pilot-v2", "runs-v2-pilot", "results-v2-pilot", "frames-v2-pilot",
     "Пилот v2 — 12 ячеек × 1 повтор (в основной анализ не входит)"),
    ("v1", "runs", "results", "frames",
     "v1 — пять одиночных условий, n = 2"),
    ("v1-clean", "runs-clean", "results-clean", "frames-clean",
     "v1-clean — повторный прогон с обезличенными каталогами, n = 2"),
]

SANITIZE = [
    (r"<HARNESS>", "<HARNESS>"),
    (r"<REPO>", "<REPO>"),
    (r"<SPINE_BANK>\.off", "<SPINE_BANK>"),
    (r"<SPINE_BANK>", "<SPINE_BANK>"),
    (r"<OTHER_CASE>", "<OTHER_CASE>"),
    (r"<HOME>/\.arch-ml", "<HOME>/.arch-ml"),
    (r"<HOME>", "<HOME>"),
    (r"/tmp/[A-Za-z0-9_\-]+", "<TMP>"),
]

TEXT_EXT = {".md", ".json", ".jsonl", ".txt", ".yaml", ".yml", ".py", ".sh", ".toml", ".csv",
            ".js", ".cff"}
ARTIFACT_EXT = {".md", ".json", ".yaml", ".yml", ".jsonl", ".txt", ".puml"}
SKIP_PARTS = {"node_modules", ".git", ".qwen", ".claude", "home", "_bmad", "__pycache__",
              ".arch-handoff/connect-manifest.json"}


def sanitize(text: str) -> str:
    for pat, rep in SANITIZE:
        text = re.sub(pat, rep, text)
    return text


def write_text(dst: Path, text: str) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(sanitize(text), encoding="utf-8")


def copy_text(src: Path, dst: Path) -> int:
    if not src.exists():
        return 0
    try:
        write_text(dst, src.read_text(encoding="utf-8", errors="replace"))
    except OSError:
        return 0
    return dst.stat().st_size


def cell_map(run_dir: Path) -> dict[str, str]:
    m = run_dir / "cell-map.json"
    if m.exists():
        return json.loads(m.read_text(encoding="utf-8"))
    out = {}
    for d in sorted((run_dir / "cells").iterdir()):
        if d.is_dir():
            out[d.name] = d.name
    return out


def agent_files(ws: Path) -> list[Path]:
    out = []
    for p in ws.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in ARTIFACT_EXT:
            continue
        rel = p.relative_to(ws)
        if any(part in SKIP_PARTS for part in rel.parts):
            continue
        if rel.parts and rel.parts[0] in ("ARCHITECTURE-SPINE.md",) and p.stat().st_size > 400_000:
            continue
        out.append(p)
    return out


def render_frame_png(ansi: Path, png: Path, header: str, max_width: int = 1280) -> bool:
    try:
        shots.render_ansi(ansi.read_text(encoding="utf-8", errors="replace"), png,
                          header=header, font_size=13)
    except Exception:  # noqa: BLE001
        return False
    try:
        from PIL import Image
        im = Image.open(png)
        if im.width > max_width:
            h = int(im.height * max_width / im.width)
            im = im.resize((max_width, h), Image.LANCZOS)
        im.save(png, optimize=True)
    except Exception:  # noqa: BLE001
        pass
    return png.exists()


def build(out: Path, campaigns: list[str] | None = None) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    manifest = []
    for name, runs_dir, res_dir, frames_dir, title in CAMPAIGNS:
        if campaigns and name not in campaigns:
            continue
        rd = ROOT / runs_dir
        if not rd.exists():
            print(f"пропуск кампании {name}: нет {rd}")
            continue
        cmap = cell_map(rd)
        rres = ROOT / res_dir
        rframes = ROOT / frames_dir
        # сводки кампании
        for f in ("live.jsonl", "live-summary.md", "live-summary-v2.md", "live-summary-v2-clean.md",
                  "PREREGISTRATION-v2.md", "preflight.md", "pilot.md", "CORRECTIONS-v1.md",
                  "judge-reliability.md", "blindness.md"):
            copy_text(rres / f, out / "results" / name / ("preregistration.md" if f.startswith("PREREG") else f))
        for cond_key, cid in sorted(cmap.items()):
            cell = rd / "cells" / cid
            if not (cell / "meta.json").exists():
                continue
            try:
                cond, rep = cond_key.rsplit("-r", 1)
                rep = int(rep)
                stack, mode = parse_condition(cond)
            except Exception:  # noqa: BLE001
                cond, rep, stack, mode = cond_key, 0, cond_key, ""
            meta = json.loads((cell / "meta.json").read_text(encoding="utf-8"))
            score = {}
            if (cell / "score.json").exists():
                score = json.loads((cell / "score.json").read_text(encoding="utf-8"))
            rid = f"{cond}-r{rep}"
            base = out / "results" / "runs" / name / rid
            write_text(base / "meta.json", json.dumps(meta, ensure_ascii=False, indent=2))
            if score:
                write_text(base / "score.json", json.dumps(score, ensure_ascii=False, indent=2))
            copy_text(cell / "prompt.txt", base / "prompt.txt")
            copy_text(cell / "panel.txt", base / "panel.txt")
            copy_text(cell / "transcript.md", base / "transcript.md")
            ws = cell / "ws"
            n_art = 0
            if ws.exists():
                for p in agent_files(ws):
                    rel = p.relative_to(ws)
                    if copy_text(p, base / "artifacts" / rel):
                        n_art += 1
            # кадр живого TUI
            raw = sorted((rframes / "raw" / f"{cond}-r{rep}").glob("*.ansi")) if rframes.exists() else []
            picks = [p for p in raw if not p.stem.startswith("00-start")] or raw
            png_rel = None
            if picks:
                src = picks[len(picks) // 2]
                png = out / "evidence" / name / f"{rid}.png"
                title_txt = ""
                tf = src.with_suffix(".title")
                if tf.exists():
                    title_txt = tf.read_text(encoding="utf-8").strip()
                if render_frame_png(src, png, f"Живой TUI Qwen Code · {title_txt or src.stem}"):
                    png_rel = str(png.relative_to(out))
            det = score.get("deterministic") or {}
            rub = {rb: (score.get("judge", {}).get(rb) or {}).get("total")
                   for rb in ("solution_architecture", "architecture_gates", "adr_quality",
                              "macedo_dimensions", "neutral_architecture")}
            manifest.append({
                "campaign": name, "condition": cond, "stack": stack, "spine_mode": mode,
                "rep": rep, "wall_s": meta.get("wall_s"), "turn_ok": meta.get("turn_ok"),
                "files_changed": len(meta.get("changed") or []),
                "tool_calls": meta.get("tool_calls"), "dialogs_answered": meta.get("dialogs_answered"),
                "gate_class": score.get("gate_class") or gate_class(det) if det else "",
                "gate_exit": det.get("spine_gate_exit"), "gate_fails": ",".join(det.get("spine_gate_fails") or []),
                "delta_dirs": ",".join(det.get("delta_dirs") or []),
                "protected_touched": len(det.get("protected_touched") or []),
                "invariants_modified": ",".join((det.get("invariants") or {}).get("modified") or []),
                "contract_breaking": det.get("contract_breaking"),
                "hook_blocks": score.get("hook_blocks"),
                "contamination": len(score.get("contamination") or []),
                "solver": meta.get("solver"), "judge": meta.get("judge_model") or meta.get("judge"),
                "artifacts": n_art, "frame": png_rel or "", **rub,
            })
            print(f"  {name}/{rid}: артефактов {n_art}, кадр {'да' if png_rel else 'нет'}")
    # манифест
    import csv
    if manifest:
        cols = list(manifest[0].keys())
        with (out / "results" / "manifest.csv").open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols)
            w.writeheader()
            w.writerows(manifest)
        (out / "results" / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nвсего прогонов в манифесте: {len(manifest)}")
    return {"runs": len(manifest)}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT.parent / "spine-sdd-bench-public"))
    ap.add_argument("--campaigns", default="")
    a = ap.parse_args()
    cs = [c for c in a.campaigns.split(",") if c] or None
    build(Path(a.out).resolve(), cs)
