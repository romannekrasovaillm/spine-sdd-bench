#!/usr/bin/env python3
"""Судья для Spine Core (`[models.X] kind = "cli"`): промпт из stdin → OpenAI-совместимый
/chat/completions → текст ответа в stdout. Только stdlib.

Окружение: JUDGE_BASE_URL (…/v1), JUDGE_MODEL, JUDGE_API_KEY.
Ключ читается только из окружения и никуда не пишется.
Промпт Spine приходит как «[system]…[user]…» — разделяем на две роли.
"""
import json, os, sys, time, urllib.request, urllib.error

if len(sys.argv) > 1 and sys.argv[1] == "--version":
    print(f"judge_cli 1.0 model={os.environ.get('JUDGE_MODEL', '?')}")
    sys.exit(0)

prompt = sys.stdin.read()
system, user = "", prompt
if prompt.lstrip().startswith("[system]") and "\n[user]" in prompt:
    head, user = prompt.split("\n[user]", 1)
    system = head.replace("[system]", "", 1).strip()
    user = user.strip()

messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
body = {"model": os.environ["JUDGE_MODEL"], "messages": messages, "temperature": 0.2}
req = urllib.request.Request(
    os.environ["JUDGE_BASE_URL"].rstrip("/") + "/chat/completions",
    data=json.dumps(body).encode(), method="POST",
    headers={"Content-Type": "application/json", "Authorization": "Bearer " + os.environ.get("JUDGE_API_KEY", "")})

for attempt in range(4):
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            data = json.load(r)
        text = data["choices"][0]["message"]["content"] or ""
        # Некоторые модели оборачивают JSON в ```json — снимаем обёртку, Spine ждёт чистый объект.
        t = text.strip()
        if t.startswith("```"):
            t = t.split("\n", 1)[1] if "\n" in t else t
            t = t.rsplit("```", 1)[0]
        print(t.strip())
        sys.exit(0)
    except (urllib.error.URLError, TimeoutError, KeyError) as e:
        if attempt == 3:
            print(f"judge_cli: запрос не удался: {e}", file=sys.stderr)
            sys.exit(1)
        time.sleep(2 ** attempt * 3)
