# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 → **0.2** (аддитивное расширение дельтой `sbp-subscriptions`, см. §8)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), AD-003 (spine)

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`

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

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.

## 8. Рекуррентные списания (СБП-подписки) — v0.2, аддитивно

- Статус: **Proposed** (дельта `sbp-subscriptions`, ADR-008; действует после A3)
- Связано: ADR-008, AD-009, AD-010, AD-011

Назначение: серия списаний по расписанию на основании согласия плательщика, без QR и без действия клиента в момент каждого списания. Раздел полностью **аддитивен**: существующие методы §3 не изменяются, `Payment` получает только опциональные поля.

### 8.1 Согласие плательщика (`Consent`)

- `POST /v1/consents` (`Idempotency-Key` обязателен): регистрация согласия. Тело — `tspId`, `amountLimit` (лимит на одно списание, копейки), `totalLimit` (опц.), `validTo`, `purpose` (опц.). Ответ `201` — `Consent{consentId, status:"PENDING"}`. Подтверждение плательщика происходит в его банке; о переходе в `ACTIVE` шлюз уведомляет событием `consent.activated`.
- `GET /v1/consents/{consentId}` — статус (`PENDING | ACTIVE | REVOKED | EXPIRED | REJECTED`).
- `DELETE /v1/consents/{consentId}` — отзыв (идемпотентно); блокирует будущие списания (AD-011).

### 8.2 Подписка (`Subscription`)

- `POST /v1/subscriptions` (`Idempotency-Key` обязателен): `tspId`, `consentId`, `amount`, `period` (`DAY|WEEK|MONTH|YEAR`), `firstDebitAt`, `purpose` (опц.). Требуется действующее согласие (`ACTIVE`); иначе `409`/`422 CONSENT_NOT_ACTIVE`.
- `GET /v1/subscriptions/{subscriptionId}` — статус (`ACTIVE | PAUSED | CANCELLED | EXPIRED`), `nextDebitAt`.
- `DELETE /v1/subscriptions/{subscriptionId}` — отмена; `POST .../pause`, `POST .../resume` — пауза/возобновление (все с `Idempotency-Key`).
- `GET /v1/subscriptions/{subscriptionId}/debits` — список списаний (`Payment` id); `POST .../debits` — внеплановое списание в рамках согласия (`Idempotency-Key`, проверяются лимит/срок согласия; при превышении — `CONSENT_LIMIT_EXCEEDED`).

### 8.3 Списание как платёж

Каждое списание — это ресурс `Payment` (§3.3) с опциональными полями `subscriptionId` и `initiationType` (`SCHEDULED` — по расписанию, `MERCHANT` — внеплановое, `PAYER` — разовый платёж по QR). Статусная модель списания: `CREATED → PAID → CREDITED → COMPLETED` (состояние `QR_ISSUED` не применяется); зачисление — только из `PAID` (AD-005, AD-010). Публичный enum статуса платежа не изменяется.

### 8.4 Новые типы вебхук-событий

`consent.activated`, `consent.revoked`, `consent.expired`, `consent.rejected`, `subscription.debit.scheduled`, `subscription.debit.completed`, `subscription.debit.failed`, `subscription.paused`, `subscription.cancelled`.

Совместимость: новые типы доставляются на существующий `webhookUrl`. ТСП обязан **игнорировать неизвестные типы** событий и обрабатывать события идемпотентно по `X-SBP-Event-Id` (ADR-004). Выделенный webhook URL для подписок — опция, решение A3.

### 8.5 Новые коды ошибок (RFC 9457)

`CONSENT_NOT_FOUND` (404), `CONSENT_NOT_ACTIVE` (422), `CONSENT_REVOKED` (422), `CONSENT_LIMIT_EXCEEDED` (422), `SUBSCRIPTION_NOT_FOUND` (404), `SUBSCRIPTION_NOT_ACTIVE` (422).

### 8.6 Идемпотентность рекуррентных операций

| Операция | Ключ | Поведение при повторе |
|---|---|---|
| `POST /v1/consents` | `Idempotency-Key` | тот же `consentId`, состояние не меняется |
| `POST /v1/subscriptions` | `Idempotency-Key` | та же `subscriptionId` |
| Списание по расписанию | `occurrenceKey = subscriptionId + scheduledFor` | второй `Payment` за тот же occurrence не создаётся |
| Внеплановое списание | `Idempotency-Key` | тот же `paymentId` |
| Отзыв/отмена/пауза | `Idempotency-Key` + статус ресурса | состояние не меняется |
