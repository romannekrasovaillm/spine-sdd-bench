# Контракт API ТСП (мерчант-API) — v0.1 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
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
  "qrType": "dynamic",             // dynamic | static | link; не применяется при paymentType=recurring
  "paymentType": "one_time",       // опц.; one_time (default) | recurring
  "consentId": "cs_…",             // обязателен при paymentType=recurring (AD-009)
  "billingReference": "bill-2026-09", // опц.; ключ дедупликации списания за расчётный период (recurring)
  "paymentPurpose": "Заказ № 12345",
  "ttlSeconds": 900,               // опц.; лимит — по НСПК [ТРЕБУЕТ ПРОВЕРКИ]; для recurring не применяется
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

Рекуррентное списание (`paymentType=recurring`, ADR-008, AD-009):
- обязательны `consentId` и `billingReference`; `qrType`/`ttlSeconds` не применяются;
- согласие должно быть `ACTIVE`, сумма ≤ `maxAmount` согласия и в пределах лимита за период — проверка в той же транзакции, что и создание платежа;
- повторный вызов с тем же `billingReference` (по одному `consentId`) возвращает **тот же** `paymentId` (дедупликация списания за период);
- ответ `201` содержит `status: CREATED` (переход в `PAID` — по событию подтверждения списания НСПК), поле `qrId`/`qrUrl` отсутствует.

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

### 3.6 Согласие на рекуррентные списания (consent/мандат) — ADR-008

Эндпоинты аддитивные; для существующих ТСП (только одноразовые платежи) не требуются.

#### 3.6.1 Создание согласия

`POST /v1/consents`

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "maxAmount": 149990,             // максимальная сумма одного списания, копейки
  "maxAmountPerPeriod": 499990,    // опц.; лимит за период
  "period": "month",               // опц.; day | week | month (при maxAmountPerPeriod)
  "expiresAt": "2027-09-28T00:00:00.000Z", // опц.; срок действия согласия
  "payerRef": "…"                  // опц.; минимизированный идентификатор плательщика (для сверки; детали ПДн — ИБ, ADR-006)
}
```

Ответ `201`:
```json
{
  "consentId": "cs_9f3c2a1b",
  "status": "PENDING",             // PENDING | ACTIVE | SUSPENDED | EXPIRED | CANCELLED | REVOKED
  "maxAmount": 149990,
  "expiresAt": "2027-09-28T00:00:00.000Z"
}
```

Правила: `Idempotency-Key` обязателен; лимиты иммутабельны после активации (изменение = новое согласие, ADR-008). Регистрация мандата в ОПКЦ — асинхронно; до подтверждения (`ACTIVE`) списания недоступны.

#### 3.6.2 Запрос согласия

`GET /v1/consents/{consentId}` → `200 { consentId, status, maxAmount, maxAmountPerPeriod, period, expiresAt, createdAt, revokedAt }`

#### 3.6.3 Отмена согласия ТСП

`POST /v1/consents/{consentId}/cancel` → `200 { consentId, status: "CANCELLED" }`

Отмена ТСП (подписка завершена) ≠ отзыв плательщика: отзыв приходит событием `consent.revoked` (инициатор — плательщик/НСПК) и переводит согласие в `REVOKED`. Оба состояния блокируют новые списания (AD-009).

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `CONSENT_NOT_FOUND` (404), `CONSENT_NOT_ACTIVE` (422), `CONSENT_LIMIT_EXCEEDED` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `consent.activated` / `consent.expired` / `consent.cancelled` / `consent.revoked` — жизненный цикл согласия (ADR-008)

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
