# Контракт API ТСП (мерчант-API) — v0.1 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft); разделы подписок СБП (§3.6–3.10, §4, §5) — **0.2 draft** (ADR-008, аддитивно к v0.1)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки СБП), AD-003, AD-009 (spine)

Назначение: контракт между **ТСП/мерчантом** и **СБП-шлюзом банка** (ядро, собственная разработка). Контракт **не зависит** от протокола ОПКЦ СБП (AD-008): адаптер НСПК скрыт за внутренним интерфейсом шлюза.

## 1. Общие положения

- Транспорт: **HTTPS, REST/JSON**, версия пути `/v1`.
- Кодировка: UTF-8. Числа сумм — **целые, в копейках** (minor units), валюта — `RUB` (ISO 4217: 643).
- Временные метки — ISO 8601 (UTC), формат `YYYY-MM-DDTHH:MM:SS.sssZ`.
- Авторизация ТСП: **mTLS** (сертификат ТСП, выпущенный УЦ банка) + `X-API-Key`. Детали финализирует ИБ на A4; для v0.1 — mTLS обязателен.
- Rate limiting: по умолчанию 50 req/s на ТСП (конфигурируемо); превышение — `429` + заголовок `Retry-After`.
- Корреляция: каждый ответ содержит `X-Trace-Id` (генерируется шлюзом, прокидывается в логи/SIEM).

## 2. Идемпотентность

- Заголовок `Idempotency-Key` **обязателен** для всех `POST`.
- Ключ генерирует ТСП (UUID); шлюз хранит маппинг ключ → ресурс **24 часа**.
- Повторный `POST` с тем же ключом и тем же телом → возвращается **тот же ресурс** (тот же `paymentId`/`refundId`), статус 200/201 без повторного действия.
- Повторный `POST` с тем же ключом, но **другим телом** → `409 IDEMPOTENCY_CONFLICT`.
- GET-запросы идемпотентны по своей природе, ключ не требуется.

## 3. Методы

### 3.1 Регистрация ТСП (онбординг)

`POST /v1/tsp`

Запрос:
```json
{
  "inn": "7701234567",
  "ogrn": "1027700132195",
  "name": "ООО «Ромашка»",
  "merchantType": "LE",            // LE | IE | SELF_EMPLOYED
  "mcc": "5411",
  "settlementAccount": "40702810900000000001",
  "pointsOfSale": [
    { "name": "Магазин на Тверской", "address": "Москва, ул. Тверская, 1", "phone": "+74950000000" }
  ],
  "webhookUrl": "https://merchant.example.com/hooks/sbp",
  "webhookSecret": "…"             // секрет для HMAC-подписи вебхуков (см. §5)
}
```

Ответ `201`:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "status": "ACTIVE"
}
```

Примечания: регистрация ТСП в ОПКЦ выполняется асинхронно через адаптер; если ОПКЦ не подтвердил — ТСП получает статус `PENDING_OPKC`, приём платежей недоступен до подтверждения. Критерии отказа (ПОД/ФТ) — на этапе A4.

### 3.2 Создание платежа (динамический QR / ссылка)

`POST /v1/payments`

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "amount": 149990,                // копейки, int
  "currency": "RUB",
  "qrType": "dynamic",             // dynamic | static | link
  "paymentPurpose": "Заказ № 12345",
  "ttlSeconds": 900,               // опц.; лимит — по НСПК [ТРЕБУЕТ ПРОВЕРКИ]
  "redirectUrl": "https://merchant.example.com/order/12345/return",
  "merchantOrderId": "order-12345" // опц., сквозной для ТСП
}
```

Ответ `201`:
```json
{
  "paymentId": "pay_8d1e4f5a",
  "qrId": "QR-…",                  // id в ОПКЦ (сквозной для сверки)
  "qrUrl": "https://qr.nspk.ru/AS100001ORTF4GAF80KPJ53K186D9A3G?type=02&bank=…&crc=…",
  "qrImage": "data:image/png;base64,…", // опц., если ТСП не рендерит сам
  "status": "QR_ISSUED",
  "amount": 149990,
  "expiresAt": "2026-08-15T18:00:00.000Z"
}
```

Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (ADR-002). Максимальная сумма — по лимитам НСПК [ТРЕБУЕТ ПРОВЕРКИ].

### 3.3 Запрос статуса платежа

`GET /v1/payments/{paymentId}`

Ответ `200`:
```json
{
  "paymentId": "pay_8d1e4f5a",
  "status": "COMPLETED",           // CREATED | QR_ISSUED | PAID | CREDITED | COMPLETED | FAILED | EXPIRED | REFUNDED
  "amount": 149990,
  "paidAt": "2026-08-15T17:31:02.000Z",
  "creditingStatus": "CREDITED",   // технический статус зачисления (для ТСП)
  "refunds": [
    { "refundId": "ref_1a2b3c", "amount": 149990, "status": "COMPLETED" }
  ],
  "errorCode": null,               // код отклонения НСПК, если статус FAILED
  "merchantOrderId": "order-12345"
}
```

### 3.4 Возврат (полный/частичный)

`POST /v1/payments/{paymentId}/refunds`

Запрос:
```json
{
  "amount": 149990,                // <= оплаченная сумма; опц. (по умолчанию — полный)
  "reason": "Возврат по заявлению клиента"
}
```

Ответ `201`:
```json
{ "refundId": "ref_1a2b3c", "paymentId": "pay_8d1e4f5a", "amount": 149990, "status": "PENDING" }
```

Правила: возврат возможен только если платёж в состоянии `CREDITED`/`COMPLETED` (ADR-005, сага). Полный возврат переводит платёж в `REFUNDED`; частичные — платёж остаётся `COMPLETED`, возврат виден в `refunds[]`. Статус возврата: `PENDING → COMPLETED | FAILED`.

### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`

### 3.6 Подписки СБП: регистрация согласия плательщика (v0.2, ADR-008)

`POST /v1/mandates` — заголовок `Idempotency-Key` обязателен.

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "payerRef": "pm_…",              // токенизированная ссылка на плательщика (не открытые ПДн, AD-006)
  "maxAmountPerPeriod": 59900,     // копейки, лимит одного списания за период
  "period": "MONTHLY",             // период списаний [ТРЕБУЕТ ПРОВЕРКИ — по правилам НСПК]
  "maxTotalAmount": 718800,        // опц., общий лимит согласия
  "validUntil": "2027-09-28T00:00:00.000Z",
  "paymentPurpose": "Подписка «Кино+»",
  "redirectUrl": "https://merchant.example.com/subscription/return",
  "merchantOrderId": "sub-12345"
}
```

Ответ `201`:
```json
{
  "mandateId": "mnd_7a2b9c",
  "status": "PENDING_PAYER",        // CREATED | PENDING_PAYER | ACTIVE | SUSPENDED | REVOKED | REJECTED | EXPIRED
  "consentUrl": "https://…",       // ссылка/QR для подтверждения согласия плательщиком в своём банке
  "maxAmountPerPeriod": 59900,
  "period": "MONTHLY",
  "validUntil": "2027-09-28T00:00:00.000Z"
}
```

Правила: подтверждение согласия выполняет **плательщик в своём банке** (вне банка-эквайера); шлюз получает результат событием НСПК (`mandate.activated`/`mandate.rejected`). Списания возможны только при `status = ACTIVE`. Параметры согласия иммутабельны после `ACTIVE`; изменение = новое согласие.

### 3.7 Статус согласия

`GET /v1/mandates/{mandateId}` → `200 { mandateId, status, maxAmountPerPeriod, period, maxTotalAmount, validUntil, activatedAt, revokedAt, reasonCode }`

### 3.8 Инициирование рекуррентного списания

`POST /v1/mandates/{mandateId}/debits` — `Idempotency-Key` обязателен; ключ идемпотентности списания = `Idempotency-Key` + `(mandateId, period)` (AD-009).

Запрос:
```json
{
  "amount": 59900,                 // <= maxAmountPerPeriod и в остатке maxTotalAmount
  "period": "2026-10",             // идентификатор периода [ТРЕБУЕТ ПРОВЕРКИ — формат от НСПК]
  "merchantOrderId": "sub-12345-2026-10"
}
```

Ответ `201`:
```json
{
  "debitId": "dbt_4e5f6a",
  "paymentId": "pay_8d1e4f5a",     // агрегат платежа (origin=MANDATE)
  "mandateId": "mnd_7a2b9c",
  "amount": 59900,
  "status": "DEBIT_PENDING"        // DEBIT_PENDING | PAID | CREDITED | COMPLETED | FAILED | EXPIRED | REFUNDED
}
```

Правила: списание допустимо только при `mandate.status = ACTIVE`, `now < validUntil`, сумме в пределах лимитов и **при отсутствии успешного списания за этот период** (иначе `409 PERIOD_ALREADY_DEBITED`). Сумма и реквизиты иммутабельны после `DEBIT_PENDING`. Зачисление — только из подтверждённого статуса `PAID` (AD-005/AD-009). Возврат по списанию — существующей сагой (§3.4).

### 3.9 Статус списания

`GET /v1/debits/{debitId}` → `200 { debitId, paymentId, mandateId, amount, status, errorCode, paidAt }`

### 3.10 Приостановка/возобновление/отзыв согласия (v0.2)

- `POST /v1/mandates/{mandateId}/suspend` → `200 { mandateId, status: "SUSPENDED" }` (новые списания запрещены, согласие возобновляемо).
- `POST /v1/mandates/{mandateId}/resume` → `200 { mandateId, status: "ACTIVE" }` (по подтверждению банка плательщика).
- `POST /v1/mandates/{mandateId}/revoke` → `200 { mandateId, status: "REVOKED" }` (отзыв со стороны ТСП; отзыв плательщиком приходит событием `mandate.revoked`).

Статусы `SUSPENDED`/`RESUME`/`REVOKE` — опциональны и включаются по решению бизнеса (см. §7).

## 4. Ошибки (RFC 9457, Problem Details)

```json
{
  "type": "https://api.bank.ru/sbp/errors/amount-exceeds-paid",
  "title": "Сумма возврата превышает оплаченную",
  "status": 422,
  "detail": "Доступная к возврату сумма: 149990",
  "code": "AMOUNT_EXCEEDS_PAID",
  "traceId": "…",
  "idempotencyKey": "…"
}
```

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Коды подписок СБП (v0.2): `MANDATE_NOT_FOUND` (404), `MANDATE_NOT_ACTIVE` (422), `MANDATE_EXPIRED` (422), `AMOUNT_EXCEEDS_MANDATE_LIMIT` (422), `PERIOD_ALREADY_DEBITED` (409), `MANDATE_ALREADY_REVOKED` (409). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`

События подписок СБП (v0.2, ADR-008):
- `mandate.pending` — запрос согласия передан плательщику
- `mandate.activated` — согласие действует (`status: ACTIVE`)
- `mandate.rejected` — плательщик/банк отклонил согласие
- `mandate.suspended` / `mandate.revoked` / `mandate.expired` — изменение/прекращение действия согласия
- `debit.completed` — рекуррентное списание зачислено
- `debit.failed` — списание отклонено (`errorCode`: `INSUFFICIENT_FUNDS`, `MANDATE_REVOKED`, `LIMIT_EXCEEDED`, `DEBIT_TIMEOUT`, …)

Тело (`payment.completed`):
```json
{
  "eventId": "evt_…",
  "type": "payment.completed",
  "paymentId": "pay_8d1e4f5a",
  "status": "COMPLETED",
  "amount": 149990,
  "timestamp": "2026-08-15T17:32:00.000Z"
}
```

Доставка: ответ ТСП `2xx` = успех; иначе ретрай (экспоненциальная задержка + джиттер), после исчерпания — DLQ. ТСП обязан отвечать идемпотентно по `eventId`.

## 6. Версионирование и совместимость

- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.
- Добавление опциональных полей — обратно совместимо, не требует новой версии.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.
- **Подписки СБП (v0.2, ADR-008)** — аддитивны к v0.1: новые ресурсы `mandates`/`debits`, новые опциональные поля. Статусы списания отдаются в ресурсе `Debit`, чтобы **не расширять enum `Payment.status`** и не ломать строгих потребителей v0.1; в `Payment` добавляются только опциональные поля `origin` и `mandateId`. Существующие пути, обязательные поля и значения enum v0.1 не изменяются. Совместимость подтверждается diff-openapi (oasdiff) в CI: только additive.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Подписки СБП (ADR-008): формат идентификатора периода, значения и лимиты `maxAmountPerPeriod`/`maxTotalAmount`, правила `suspend`/`resume` — по документации НСПК и бизнес-требованиям [ТРЕБУЕТ ПРОВЕРКИ].
6. Версия контракта подписок: аддитивная 0.2 в `/v1` (рекомендуется) vs отдельный `/v2` — решение на гейте A1.
