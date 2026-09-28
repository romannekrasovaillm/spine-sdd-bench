# Доказательство: обратная совместимость контракта API ТСП (v0.1.0 → v0.2.0)

Инструмент: MCP `contract_diff` (формат openapi).
Старая версия: `changes/sbp-recurring-c2b/contracts/tsp-api.v0.1.0.yaml` (снята с `openapi/tsp-api.yaml` до правки).
Новая версия: `openapi/tsp-api.yaml`.

```
contract_diff: 3 изменений (breaking: 0, non-breaking: 3)
Формат: openapi
[warn] #/paths/~1v1~1consents CD-005 — добавлен путь «/v1/consents»
[warn] #/paths/~1v1~1consents~1{consentId} CD-005 — добавлен путь «/v1/consents/{consentId}»
[warn] #/paths/~1v1~1consents~1{consentId}~1revoke CD-005 — добавлен путь «/v1/consents/{consentId}/revoke»
Итог: PASS
```

- `breaking: 0` — ломающих изменений нет; существующие потребители v0.1 правок не требуют.
- `non-breaking: 3` — добавлены новые пути. Изменение `info.version` 0.1.0 → 0.2.0 и добавление необязательных полей в `Payment`/`PaymentRequest` — аддитивны (правило CD-007 не сработало: ломающего диффа без смены major нет).

Примечание: diff-инструмент сообщает только новые пути; необязательные поля в существующих схемах — аддитивны по определению OpenAPI (потребитель их игнорирует) и подтверждаются `openapi_lint` (0 находок).
