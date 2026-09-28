#!/usr/bin/env python3
"""envutil.py — секреты читаются из интерактивного профиля оболочки и живут
только в памяти процесса: на диск не пишутся (требование kit/PREREGISTRATION.md).
"""
from __future__ import annotations

import subprocess

_cache: dict[str, str] = {}


def secret(name: str) -> str:
    if name not in _cache:
        r = subprocess.run(["bash", "-ic", f'printf %s "${{{name}}}"'],
                           capture_output=True, text=True)
        _cache[name] = r.stdout.strip()
    return _cache[name]


def solver_env() -> dict:
    """Env для Qwen Code (решатель): DeepSeek через OpenAI-совместимый вход."""
    return {
        "OPENAI_API_KEY": secret("DEEPSEEK_API_KEY"),
        "OPENAI_BASE_URL": secret("OPENAI_BASE_URL") or "https://api.deepseek.com/v1",
    }


def judge_key_env() -> dict:
    """Env для судьи: другое семейство моделей (GLM/Zhipu)."""
    return {"ZHIPU_API_KEY": secret("ZHIPU_API_KEY")}
