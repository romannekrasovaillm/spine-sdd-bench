# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (нестабильная; аддитивное расширение 0.1 — согласия и рекуррентные платежи; до A1 фиксируется v1.0-draft)
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

Для рекуррентного дебита: `paymentType=RECURRING` + `consentId` (см. §8). Разовый платёж (`paymentType=ONE_TIME`, по умолчанию) — поведение не меняется.

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `RECURRING_DISABLED` (403), `NOT_FOUND` (404), `CONSENT_NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `CONSENT_NOT_ACTIVE` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `CONSENT_LIMIT_EXCEEDED` (422), `CONSENT_EXPIRED` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `consent.signed` — согласие подписано плательщиком (`status: ACTIVE`)
- `consent.declined` — плательщик отказался подписывать
- `consent.revoked` — согласие отозвано
- `consent.expired` — согласие истекло (срок/лимит)
- `consent.suspended` — согласие приостановлено банком/AML

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
5. Точная форма/поля согласия и порядок подписания — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].

## 8. Согласия и рекуррентные платежи (v0.2, аддитивно)

Расширение v0.2 **обратно совместимо**: все новые поля — опциональные, новые пути — `/v1/consents*`; существующие `/v1/payments` и статусная модель разовых платежей не меняются.

### 8.1 Создание запроса согласия

`POST /v1/consents` (заголовок `Idempotency-Key` обязателен)

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "amountLimit": 49900,             // копейки, максимум за один дебит
  "currency": "RUB",
  "maxTotalAmount": 149700,         // опц., суммарный лимит
  "validityStart": "2026-09-28T00:00:00.000Z",
  "validityEnd": "2027-09-28T00:00:00.000Z",
  "merchantConsentId": "sub-12345", // опц., сквозной для ТСП
  "paymentPurpose": "Подписка на онлайн-кинотеатр"
}
```

Ответ `201`:
```json
{
  "consentId": "cns_7b2e9d1a",
  "status": "REQUESTED",           // REQUESTED | PENDING_SIGN | ACTIVE | REVOKED | EXPIRED | DECLINED | SUSPENDED
  "amountLimit": 49900,
  "remainingLimit": 149700,
  "merchantConsentId": "sub-12345",
  "createdAt": "2026-09-28T10:00:00.000Z"
}
```

Правила: `amountLimit` > 0; статус `REQUESTED → PENDING_SIGN` — после получения sign-ссылки/QR от ОПКЦ. Подписание выполняет плательщик в приложении своего банка (вне шлюза); факт подписания приходит событием ОПКЦ → `ACTIVE` → вебхук `consent.signed`.

### 8.2 Статус согласия

`GET /v1/consents/{consentId}` → `200 { consentId, status, amountLimit, remainingLimit, expiresAt, merchantConsentId, createdAt }`

### 8.3 Отзыв согласия

`POST /v1/consents/{consentId}/revoke` (заголовок `Idempotency-Key` обязателен)

Ответ `200`:
```json
{ "consentId": "cns_7b2e9d1a", "status": "REVOKED" }
```

Правила: отзыв переводит согласие в `REVOKED` (терминальное) после подтверждения ОПКЦ; новые дебиты отклоняются (`409 CONSENT_NOT_ACTIVE`). Повторный отзыв идемпотентен.

### 8.4 Рекуррентный дебит

`POST /v1/payments` с `paymentType=RECURRING` и `consentId`:

```json
{
  "tspId": "tsp_9f3c2a1b",
  "amount": 49900,
  "currency": "RUB",
  "paymentType": "RECURRING",
  "consentId": "cns_7b2e9d1a",
  "paymentPurpose": "Ежемесячное списание",
  "merchantOrderId": "sub-12345-2026-09"
}
```

Семантика: дебит инициируется без QR и без действия клиента. Статусы дебита — подмножество статусной машины платежа: `CREATED → PAID → CREDITED → COMPLETED`, терминальный `FAILED`; `QR_ISSUED`/`EXPIRED` неприменимы. Guard (AD-009): согласие должно быть `ACTIVE`, сумма ≤ `remainingLimit`, в пределах срока; иначе `409 CONSENT_NOT_ACTIVE` / `422 CONSENT_LIMIT_EXCEEDED` / `422 CONSENT_EXPIRED`.

### 8.5 Ошибки согласий

`CONSENT_NOT_FOUND` (404), `CONSENT_NOT_ACTIVE` (409), `CONSENT_LIMIT_EXCEEDED` (422), `CONSENT_EXPIRED` (422), `RECURRING_DISABLED` (403 — фича выключена фиче-флагом). Формат — RFC 9457 (см. §4).
