# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (аддитивное расширение рекуррентными согласиями, ADR-008..010; ресурсы и семантика v0.1 не меняются)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (согласие), ADR-009 (двойное списание), ADR-010 (эволюция контракта), AD-003, AD-009 (spine)

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

### 3.6 Создание согласия плательщика (рекуррентное списание)

`POST /v1/consents` (заголовок `Idempotency-Key` обязателен)

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "amountType": "FIXED",           // FIXED | VARIABLE
  "maxAmountPerCharge": 49900,     // копейки; обязателен при FIXED
  "currency": "RUB",
  "periodicity": "MONTHLY",        // WEEKLY | MONTHLY | QUARTERLY | ANNUAL
  "maxTotalAmount": 598800,        // опц., лимит за весь срок
  "validUntil": "2027-09-28T00:00:00.000Z", // опц.; лимит срока — по НСПК [ТРЕБУЕТ ПРОВЕРКИ]
  "purpose": "Подписка «Кино+», тариф Стандарт",
  "merchantOrderId": "sub-12345",
  "redirectUrl": "https://merchant.example.com/subscription/return"
}
```

Ответ `201`:
```json
{
  "consentId": "cons_7a1b2c3d",
  "tspId": "tsp_9f3c2a1b",
  "status": "PENDING_PAYER",
  "amountType": "FIXED",
  "maxAmountPerCharge": 49900,
  "currency": "RUB",
  "periodicity": "MONTHLY",
  "consentUrl": "https://qr.nspk.ru/…",
  "qrId": "QR-…",
  "validUntil": "2027-09-28T00:00:00.000Z"
}
```

Правила: согласие оформляет **плательщик в приложении своего банка**; до активации (`ACTIVE`) списания запрещены. Изменение лимитов/периодичности невозможно — только отзыв и новое согласие.

### 3.7 Статус согласия

`GET /v1/consents/{consentId}` → `200 Consent`, где `status`: `PENDING_PAYER | ACTIVE | SUSPENDED | REVOKED | EXPIRED | REJECTED`; `activatedAt`/`revokedAt` заполняются по факту.

### 3.8 Отзыв согласия (ТСП)

`POST /v1/consents/{consentId}/revoke` (заголовок `Idempotency-Key` обязателен) → `200 Consent` со статусом `REVOKED`. Повторный вызов идемпотентен. Отзыв плательщиком приходит нотификацией ОПКЦ и отражается тем же статусом.

### 3.9 Рекуррентное списание по согласию

`POST /v1/consents/{consentId}/charges` (заголовок `Idempotency-Key` обязателен)

Запрос:
```json
{
  "amount": 49900,                 // копейки, ≤ maxAmountPerCharge
  "currency": "RUB",
  "billingId": "2026-09",          // стабильный идентификатор периода ТСП (ADR-009)
  "merchantOrderId": "sub-12345-2026-09",
  "description": "Абонентская плата за сентябрь"
}
```

Ответ `201`:
```json
{
  "chargeId": "chg_5e6f7a8b",
  "paymentId": "pay_8d1e4f5a",
  "consentId": "cons_7a1b2c3d",
  "amount": 49900,
  "currency": "RUB",
  "billingId": "2026-09",
  "status": "CREATED",             // CREATED | PAID | CREDITED | COMPLETED | FAILED | CANCELLED
  "createdAt": "2026-09-28T10:00:00.000Z"
}
```

Правила: списание создаётся **только при согласии `ACTIVE`** (иначе `409 CONSENT_NOT_ACTIVE`), сумма ≤ `maxAmountPerCharge` (иначе `422 CHARGE_EXCEEDS_CONSENT_LIMIT`). Уникальность — пара `(consentId, billingId)`: повтор с тем же `billingId` возвращает существующий `chargeId`/`paymentId`; та же пара с другой суммой → `409 CHARGE_CONFLICT` (ADR-009). Результат списания — обычный платёж, виден через `GET /v1/payments/{paymentId}` (поле `status`, `consentId`, `initiation=CONSENT`).

### 3.10 Статус списания

`GET /v1/payments/{paymentId}/charges/{chargeId}` → `200 Charge` (статусы списания, см. §3.9).

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

Коды рекуррентных операций (v0.2): `CONSENT_NOT_ACTIVE` (409), `CONSENT_EXPIRED` (422), `CHARGE_EXCEEDS_CONSENT_LIMIT` (422), `CHARGE_CONFLICT` (409, та же пара `(consentId, billingId)` с другой суммой), `CONSENT_NOT_REVOCABLE` (409).

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `consent.activated` — согласие активировано плательщиком (`status: ACTIVE`)
- `consent.revoked` — согласие отозвано (плательщиком или ТСП)
- `consent.rejected` — в оформлении согласия отказано
- `consent.expired` — истёк срок действия согласия

Результат рекуррентного списания приходит существующими событиями `payment.*` (списание — обычный платёж); дополнительно в теле присутствует `consentId`.

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
- Версия 0.2 — **аддитивное** расширение v0.1: добавлены только новые пути (`/v1/consents…`, `/v1/payments/{paymentId}/charges/{chargeId}`), новые опциональные поля (`Payment.consentId`, `Payment.initiation`) и новые события (`consent.*`). Существующие операции `POST /v1/payments` и `GET /v1/payments/{paymentId}` не изменены; `contract_diff` v0.1→v0.2 даёт breaking: 0 (ADR-010). Перед релизом контракта — обязательный гейт `openapi_lint` + `contract_diff`.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Рекуррентные: точные поля/статусы мандата и тайминги уведомлений — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ]; формат `billingId` — согласовать с ТСП-пилотами.
6. Правило отзыва «списание в полёте» (ADR-011) — юридическое подтверждение до A3.
