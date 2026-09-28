# Доказательство: линт контракта API ТСП v0.2.0

Инструмент: MCP `openapi_lint` (путь `openapi/tsp-api.yaml`).

```
openapi: 0 находок (error: 0, warn: 0)
Итог: PASS
```

Проверено для обеих версий (v0.1.0-draft и v0.2.0): версионирование, идемпотентность mutating-endpoint'ов (наличие `Idempotency-Key` у `POST`), ошибки RFC 9457 (`application/problem+json`).
