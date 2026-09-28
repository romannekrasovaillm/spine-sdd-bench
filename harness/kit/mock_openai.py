#!/usr/bin/env python3
"""Mock OpenAI-совместимого эндпоинта — ТОЛЬКО для сквозной проверки конвейера run_live.py.

Решатель: если в запросе есть инструмент записи файла и ещё не было результата инструмента —
один tool-call, пишущий docs/adr/ADR-008-mock.md; иначе — финальный текст.
Судья: валидный JSON по критериям, извлечённым из промпта («### <id> — …»), балл MOCK_JUDGE_SCORE.
Поддерживает stream=true (SSE). Журнал запросов — MOCK_LOG.
"""
import json, os, re, sys, time
from http.server import BaseHTTPRequestHandler, HTTPServer

LOG = os.environ.get("MOCK_LOG", "/tmp/mock_openai.log")
ADR = ("# ADR-008 (mock)\n\n- Status: Proposed (A3)\n\n## Решение\nПодписка — отдельный агрегат; списание — обычный платёж, "
       "зачисление только из PAID (AD-005).\n\n## Альтернативы\n- расширить статусную машину — отвергнуто\n\n"
       "## Последствия\n- (−) новое хранилище согласий\n- Обратимость: высокая, откат флагом\n")


def solver_reply(body):
    tools = [t.get("function", {}).get("name") for t in body.get("tools", [])]
    had_tool = any(m.get("role") == "tool" for m in body.get("messages", []))
    writer = next((t for t in tools if t and re.search(r"write", t, re.I)), None)
    m = re.search(r"(/[^\s\"'`]+/cells/[^/\s]+/ws)", json.dumps(body.get("messages", []), ensure_ascii=False))
    ws = m.group(1) if m else os.environ.get("MOCK_CWD", os.getcwd())
    if writer and not had_tool:
        return {"role": "assistant", "content": None, "tool_calls": [{
            "id": "call_1", "type": "function",
            "function": {"name": writer, "arguments": json.dumps(
                {"file_path": os.path.join(ws, "docs/adr/ADR-008-mock.md"),
                 "content": ADR}, ensure_ascii=False)}}]}
    return {"role": "assistant", "content": "Готово (mock): docs/adr/ADR-008-mock.md"}


def judge_reply(prompt):
    ids = re.findall(r"^### ([a-z0-9_]+) — ", prompt, re.M)
    s = int(os.environ.get("MOCK_JUDGE_SCORE", "3"))
    return {"role": "assistant", "content": json.dumps({
        "scores": [{"criterion_id": i, "score": s, "rationale": "свидетельство отсутствует" if s == 1 else
                    "Цитата: \"зачисление только из PAID\". mock"} for i in ids],
        "verdict": "mock"}, ensure_ascii=False)}


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        text = json.dumps(body.get("messages", []), ensure_ascii=False)
        msg = judge_reply("\n".join(m.get("content") or "" for m in body["messages"] if isinstance(m.get("content"), str))) \
            if "архитектурный судья" in text else solver_reply(body)
        with open(LOG, "a") as f:
            f.write(json.dumps({"t": time.time(), "model": body.get("model"), "stream": body.get("stream"),
                                "tools": len(body.get("tools", [])), "kind": "judge" if "судья" in text else "solver",
                                "reply_tool": bool(msg.get("tool_calls"))}, ensure_ascii=False) + "\n")
        usage = {"prompt_tokens": 100, "completion_tokens": 20, "total_tokens": 120}
        finish = "tool_calls" if msg.get("tool_calls") else "stop"
        if body.get("stream"):
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.end_headers()
            delta = dict(msg)
            if delta.get("tool_calls"):
                delta["tool_calls"] = [{**tc, "index": 0} for tc in delta["tool_calls"]]
            chunks = [{"choices": [{"index": 0, "delta": delta, "finish_reason": None}]},
                      {"choices": [{"index": 0, "delta": {}, "finish_reason": finish}], "usage": usage}]
            for c in chunks:
                c.update(id="mock", object="chat.completion.chunk", created=int(time.time()), model=body.get("model"))
                self.wfile.write(f"data: {json.dumps(c, ensure_ascii=False)}\n\n".encode())
            self.wfile.write(b"data: [DONE]\n\n")
        else:
            data = {"id": "mock", "object": "chat.completion", "created": int(time.time()), "model": body.get("model"),
                    "choices": [{"index": 0, "message": msg, "finish_reason": finish}], "usage": usage}
            raw = json.dumps(data, ensure_ascii=False).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

    def do_GET(self):
        raw = json.dumps({"data": [{"id": "mock-model", "object": "model"}]}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(raw)


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", int(sys.argv[1]) if len(sys.argv) > 1 else 18080), H).serve_forever()
