# Контракт API ТСП: подписки СБП — v0.2 draft

- Status: Draft (предложение к гейту A1; ждёт A3 и документации НСПК по подпискам)
- Версия контракта: 0.2 (аддитивное расширение `docs/contracts/tsp-api.md` v0.1 → `openapi/tsp-api.yaml`)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-008, ADR-009, AD-003, AD-009, AD-010, AD-011, `../spec/subscriptions.md`, `../nfr-subscriptions.md`

Назначение: описать ресурсы подписок СБП в API ТСП. Расширение **аддитивное**: существующие методы, поля, статусы и события `payment.*` не меняются (см. §6). Протокол ОПКЦ по подпискам скрыт за адаптером (AD-008), наружу не протекает.

## 1. Общие положения

Действуют общие положения `tsp-api.md` §1: HTTPS/REST/JSON, путь `/v1`, UTF-8, суммы целые в копейках (`RUB`), ISO 8601 UTC, mTLS + `X-API-Key`, rate limiting с `429`/`Retry-After`, `X-Trace-Id` в каждом ответе.

Дополнительно для подписок:

- Все `POST` требуют `Idempotency-Key` (правило `tsp-api.md` §2 сохраняется).
- Идентификаторы: `mandateId`, `subscriptionId`, `debitId` — строки, сквозные для сверки.

## 2. Методы: мандаты (согласие плательщика)

### 2.1 Регистрация мандата

`POST /v1/mandates`

```json
{
  "tspId": "tsp_9f3c2a1b",
  "maxAmount": 99900,              // лимит одного списания, копейки
  "period": "MONTHLY",             // MONTHLY | WEEKLY | DAILY | CUSTOM (по регламенту СБП)
  "maxDebitsPerPeriod": 1,
  "validUntil": "2027-09-28T00:00:00.000Z",
  "paymentPurpose": "Подписка «Кино+»",
  "merchantOrderId": "sub-plan-42" // опц., сквозной для ТСП
}
```

Ответ `201`:

```json
{
  "mandateId": "man_7k2p9d1c",
  "status": "PENDING",
  "confirmUrl": "https://…",       // ссылка/QR подтверждения плательщиком
  "expiresAt": "2026-09-28T12:30:00.000Z",
  "maxAmount": 99900,
  "period": "MONTHLY"
}
```

Правила: подтверждение выполняет плательщик в СБП; до подтверждения мандат `PENDING` и списания невозможны. Повтор с тем же `Idempotency-Key` и телом возвращает тот же `mandateId`.

### 2.2 Статус мандата

`GET /v1/mandates/{mandateId}` → `200`

```json
{
  "mandateId": "man_7k2p9d1c",
  "status": "ACTIVE",              // PENDING | ACTIVE | REVOKED | EXPIRED | DECLINED
  "maxAmount": 99900,
  "period": "MONTHLY",
  "activatedAt": "2026-09-28T11:02:00.000Z",
  "validUntil": "2027-09-28T00:00:00.000Z",
  "revokedAt": null,
  "subscriptions": ["sub_1a2b3c"]
}
```

## 3. Методы: подписки

### 3.1 Создание подписки

`POST /v1/subscriptions`

```json
{
  "tspId": "tsp_9f3c2a1b",
  "mandateId": "man_7k2p9d1c",
  "amount": 49900,                 // сумма списания за период, копейки; <= maxAmount мандата
  "period": "MONTHLY",
  "firstDebitAt": "2026-10-01T06:00:00.000Z",
  "paymentPurpose": "Подписка «Кино+», октябрь",
  "merchantOrderId": "sub-42"
}
```

Ответ `201`:

```json
{
  "subscriptionId": "sub_1a2b3c",
  "status": "ACTIVE",
  "mandateId": "man_7k2p9d1c",
  "amount": 49900,
  "period": "MONTHLY",
  "nextDebitAt": "2026-10-01T06:00:00.000Z"
}
```

Правила: подписка создаётся только по мандату `ACTIVE`; `amount` ≤ `maxAmount` мандата, иначе `MANDATE_LIMIT_EXCEEDED`. Повтор с тем же `Idempotency-Key` — тот же `subscriptionId`.

### 3.2 Статус подписки

`GET /v1/subscriptions/{subscriptionId}` → `200`

```json
{
  "subscriptionId": "sub_1a2b3c",
  "status": "ACTIVE",              // ACTIVE | PAUSED | SUSPENDED | CANCELLED
  "mandateId": "man_7k2p9d1c",
  "amount": 49900,
  "period": "MONTHLY",
  "nextDebitAt": "2026-11-01T06:00:00.000Z",
  "lastDebit": { "debitId": "pay_…", "billingPeriod": "2026-10", "status": "COMPLETED" }
}
```

### 3.3 Пауза / возобновление / отмена

- `POST /v1/subscriptions/{subscriptionId}/pause` → `200 { subscriptionId, status: "PAUSED" }`
- `POST /v1/subscriptions/{subscriptionId}/resume` → `200 { subscriptionId, status: "ACTIVE", nextDebitAt }`
- `POST /v1/subscriptions/{subscriptionId}/cancel` → `200 { subscriptionId, status: "CANCELLED" }`

Правила: отмена и пауза запрещают будущие списания и **не отменяют** завершённые списания и возвраты. Отзыв мандата переводит связанные подписки в `SUSPENDED` (событие `subscription.suspended`).

### 3.4 Списания по подписке

`GET /v1/subscriptions/{subscriptionId}/debits` → `200 { "debits": [ … ] }`

Элемент списания — платёж (`tsp-api.md` §3.3) с полями связи:

```json
{
  "paymentId": "pay_8d1e4f5a",
  "subscriptionId": "sub_1a2b3c",
  "mandateId": "man_7k2p9d1c",
  "billingPeriod": "2026-10",
  "amount": 49900,
  "status": "COMPLETED",
  "errorCode": null
}
```

Отказ списания отдаётся существующим `status: "FAILED"` и полем `errorCode`; **новых значений `Payment.status` не вводится**.

## 4. Вебхуки

Доставка — по `tsp-api.md` §5 (at-least-once, HMAC, `X-SBP-Event-Id`, ретраи, DLQ). Изменения **аддитивные**:

- Существующие события `payment.completed`/`payment.failed`/`payment.expired` для списаний дополнительно несут `subscriptionId`, `mandateId`, `billingPeriod`.
- Новые типы: `mandate.activated`, `mandate.declined`, `mandate.revoked`, `mandate.expired`, `subscription.suspended`, `subscription.paused`, `subscription.resumed`, `subscription.cancelled`.
- **Правило потребителя:** неизвестный тип события и неизвестное опциональное поле MUST игнорироваться; обработка известных событий не должна нарушаться. Это условие обратной совместимости (см. §6).

```json
{
  "eventId": "evt_…",
  "type": "mandate.revoked",
  "mandateId": "man_7k2p9d1c",
  "subscriptionIds": ["sub_1a2b3c"],
  "timestamp": "2026-10-15T09:00:00.000Z"
}
```

## 5. Ошибки

Формат — RFC 9457 (`tsp-api.md` §4). Новые канонические коды:

| Код | HTTP | Смысл |
|---|---|---|
| `MANDATE_NOT_ACTIVE` | 422 | Мандат не в состоянии `ACTIVE` (создание подписки/списание отклонено) |
| `MANDATE_EXPIRED` | 422 | Истёк срок действия мандата |
| `MANDATE_LIMIT_EXCEEDED` | 422 | Сумма списания превышает лимит мандата |
| `SUBSCRIPTION_NOT_ACTIVE` | 422 | Подписка не в состоянии, допускающем операцию |
| `DEBIT_INSUFFICIENT_FUNDS` | 422 | Списание отклонено из-за недостатка средств (в `errorCode` платежа) |
| `DEBIT_DECLINED` | 422 | Списание отклонено ОПКЦ (прочие причины, нормализованные) |

Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200/201, а не ошибку.

## 6. Версионирование и совместимость

Расширение в рамках `/v1` допустимо, потому что оно **только аддитивное**:

1. Новые пути и новые ресурсы — существующие потребители их не вызывают.
2. Новые поля — только опциональные (`subscriptionId`, `mandateId`, `billingPeriod` в `Payment`); обязательных полей в существующих ответах не добавляется.
3. `Payment.status` не расширяется: отказ списания — `FAILED` + `errorCode`.
4. Новые типы событий — потребитель обязан игнорировать неизвестные (правило §4); существующие типы и их семантика не меняются.
5. Новые коды ошибок — добавляются, существующие не переиспользуются под другой смысл.

Ломающие изменения (`Payment.status`, удаление/переименование полей, новые обязательные поля в запросах, смена семантики существующих событий) — только в `/v2` по правилам `tsp-api.md` §6 с периодом поддержки обеих версий ≥ 6 мес. Проверка диффа — `contract_diff` (CD-001…CD-010); для этого изменения ожидается 0 breaking.

## 7. Открытые вопросы (для A1/A3)

1. Значения `period` и правила ретраев/сроки подтверждения мандата — по документации НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`.
2. Изменение суммы/периода действующей подписки, частичные списания — вне первой волны (см. `ADR-008`, Open Questions).
3. Формат `confirmUrl`/QR подтверждения мандата — по протоколу НСПК/продукту.
4. Нужен ли `GET /v1/mandates?tspId=…` (список мандатов) — по запросу продукта.
