# Контракт API ТСП (мерчант-API) — v0.1 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (аддитивное расширение: рекуррентные списания и согласия; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (согласия/рекуррентные), AD-003, AD-009 (spine)

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

### 3.2.1 Рекуррентное списание (подписка)

Тот же `POST /v1/payments`, но с расширенным телом (аддитивно, разовые вызовы не меняются):

```json
{
  "tspId": "tsp_9f3c2a1b",
  "amount": 64900,                 // копейки, int — сумма текущего списания
  "currency": "RUB",
  "paymentType": "recurring",      // one_time (по умолчанию) | recurring
  "consentId": "cst_7b2e9d",       // обязателен при recurring
  "periodKey": "2026-09",          // обязателен при recurring: ключ биллингового периода
  "paymentPurpose": "Подписка «Кино+» за сентябрь",
  "merchantOrderId": "sub-98765"
}
```

Правила (AD-009):
- `consentId` и `periodKey` обязательны при `paymentType=recurring`; при `one_time` игнорируются/запрещены.
- Шлюз проверяет согласие: `ACTIVE`, `amount ≤ maxAmountPerDebit`, не превышен `maxTotalPerPeriod`, `now < endDate`. Нарушение → `403 CONSENT_INACTIVE` / `422 CONSENT_LIMIT_EXCEEDED` (см. §4).
- Дедупликация периода: повторный `POST` с тем же `consentId + periodKey` возвращает **тот же `paymentId`** (идемпотентно), даже при новом `Idempotency-Key`. Разные суммы за тот же `periodKey` → `409 IDEMPOTENCY_CONFLICT`.
- Рекуррентный платёж не выпускает QR и не проходит `QR_ISSUED`: путь `CREATED → PAID → CREDITED → COMPLETED` (ADR-008).

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

### 3.6 Создание согласия (подписки)

`POST /v1/consents` (заголовок `Idempotency-Key` обязателен)

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "merchantOrderId": "sub-98765",
  "payerRef": "payer_…",             // непрозрачная ссылка; минимум ПДн, необходимый НСПК (ADR-006)
  "maxAmountPerDebit": 100000,       // копейки, int
  "maxTotalPerPeriod": 300000,       // копейки, int — лимит за период
  "period": "month",                 // day | week | month
  "startDate": "2026-09-28",
  "endDate": "2027-09-28",
  "webhookUrl": "https://merchant.example.com/hooks/sbp-consents" // опц.; переопределяет вебхук ТСП
}
```

Ответ `201`:
```json
{
  "consentId": "cst_7b2e9d",
  "tspId": "tsp_9f3c2a1b",
  "status": "PENDING",               // PENDING → ACTIVE → CANCELLED | EXPIRED | REVOKED | FAILED
  "maxAmountPerDebit": 100000,
  "maxTotalPerPeriod": 300000,
  "period": "month",
  "startDate": "2026-09-28",
  "endDate": "2027-09-28"
}
```

Примечания: после создания согласие находится в `PENDING` до подтверждения плательщиком в приложении своего банка (через НСПК). Рекуррентные списания разрешены только из `ACTIVE` (AD-009). Активация/отзыв приходят нотификацией НСПК и доставляются ТСП вебхуком (см. §5).

### 3.7 Статус согласия

`GET /v1/consents/{consentId}` → `200` с телом, как в §3.6 (текущий `status` + лимиты). Идемпотентен по своей природе.

### 3.8 Отзыв согласия

`POST /v1/consents/{consentId}/cancel` (заголовок `Idempotency-Key` обязателен)

Ответ `200`: согласие переходит в `CANCELLED`; **новые** рекуррентные списания отклоняются немедленно (`403 CONSENT_INACTIVE`), уже инициированные (`CREATED`/`PAID`/`ABS_PENDING`) завершаются или компенсируются штатным путём (ADR-008). Отзыв идемпотентен: повторный вызов возвращает `CANCELLED`.

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Дополнительно для согласий/рекуррентных: `CONSENT_INACTIVE` (403), `CONSENT_NOT_FOUND` (404), `CONSENT_LIMIT_EXCEEDED` (422), `PERIOD_KEY_CONFLICT` (409). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `consent.activated` — согласие подтверждено плательщиком (`ACTIVE`)
- `consent.revoked` — согласие отозвано (плательщиком/ТСП/AML, `CANCELLED`/`REVOKED`)
- `consent.expired` — истёк срок действия (`EXPIRED`)

Тело (`consent.activated`):
```json
{
  "eventId": "evt_…",
  "type": "consent.activated",
  "consentId": "cst_7b2e9d",
  "tspId": "tsp_9f3c2a1b",
  "status": "ACTIVE",
  "timestamp": "2026-09-28T10:00:00.000Z"
}
```

ТСП обязан идемпотентно обрабатывать по `eventId` (ADR-004); событие `consent.revoked` — сигнал немедленно прекратить новые списания.

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
- Настоящее расширение (0.1 → 0.2) — строго аддитивное: новые эндпоинты `/v1/consents*` и опциональные поля `paymentType`/`consentId`/`periodKey`. Существующие потребители разовых платежей не меняют ни запросы, ни ожидания ответов: `paymentType` по умолчанию `one_time`, а поле `status` в `Payment` не меняет свой enum. Ломающих изменений нет.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
