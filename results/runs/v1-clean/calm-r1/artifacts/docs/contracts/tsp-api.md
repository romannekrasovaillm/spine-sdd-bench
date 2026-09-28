# Контракт API ТСП (мерчант-API) — v0.2 draft (аддитивное расширение рекуррентных списаний)

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (аддитивное расширение для рекуррентных списаний, ADR-008; существующие методы v0.1 не изменены)
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

### 3.6 Создание согласия (рекуррентные списания)

`POST /v1/consents`

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "payerRef": "subscriber-12345",      // сквозной id плательщика у ТСП
  "amountLimit": {
    "maxPerDebit": 50000,              // максимум за одно списание, копейки
    "maxTotal": 600000,                // опц.; максимум суммарно за период действия
    "currency": "RUB"
  },
  "period": "P1M",                     // периодичность (ISO 8601 duration)
  "validity": {
    "validFrom": "2026-10-01T00:00:00.000Z",
    "validUntil": "2027-10-01T00:00:00.000Z"
  },
  "purpose": "Подписка на онлайн-кинотеатр"
}
```

Ответ `201`:
```json
{
  "consentId": "cst_5e7a9b1c",
  "status": "CONSENT_CREATED",
  "consentUrl": "https://...",         // ссылка на подтверждение в банке плательщика
  "amountLimit": { "maxPerDebit": 50000, "maxTotal": 600000, "currency": "RUB" },
  "period": "P1M",
  "validFrom": "2026-10-01T00:00:00.000Z",
  "validUntil": "2027-10-01T00:00:00.000Z"
}
```

Правила: `Idempotency-Key` обязателен. Согласие создаётся в `CONSENT_CREATED`; активация (`CONSENT_ACTIVE`) — после подтверждения плательщиком (нотификация `consent.activated`). Лимиты и `validUntil` **иммутабельны** после `CONSENT_ACTIVE`; изменение условий — новое согласие.

### 3.7 Статус согласия

`GET /v1/consents/{consentId}` → `200 { consentId, status, amountLimit, period, validFrom, validUntil, revokeReason }`
Статусы: `CONSENT_CREATED | CONSENT_ACTIVE | CONSENT_SUSPENDED | CONSENT_REVOKED | CONSENT_EXPIRED | CONSENT_FAILED`.

### 3.8 Отзыв согласия (ТСП)

`POST /v1/consents/{consentId}/revoke` → `200 { consentId, status: CONSENT_REVOKED, revokeReason }`

Правила: идемпотентно; повторный отзыв уже отозванного согласия возвращает `CONSENT_REVOKED` без ошибки. Отзыв — стоп для всех открытых списаний (AD-009).

### 3.9 Инициация рекуррентного списания (дебет)

`POST /v1/consents/{consentId}/debits`

Запрос:
```json
{
  "amount": 49900,                     // копейки; ≤ maxPerDebit и ≤ остаток maxTotal
  "merchantOrderId": "order-12345",
  "purpose": "Ежемесячная подписка"
}
```

Ответ `201`:
```json
{
  "paymentId": "pay_8d1e4f5a",
  "status": "CREATED",
  "amount": 49900,
  "paymentType": "RECURRENT",
  "consentId": "cst_5e7a9b1c"
}
```

Правила: доступно только из `CONSENT_ACTIVE`; `amount > 0` и в пределах лимитов; `Idempotency-Key` обязателен — повтор возвращает тот же `paymentId` (второго списания нет). Дебет далее идёт по платёжной машине (`CREATED → PAID → CREDITED → COMPLETED`), зачисление — только из `PAID` (AD-005).

### 3.10 Список списаний по согласию

`GET /v1/consents/{consentId}/debits` → `200 { items: [ Payment, ... ] }`

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `CONSENT_NOT_ACTIVE` (422), `CONSENT_LIMIT_EXCEEDED` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `consent.activated` — согласие подтверждено плательщиком (`status: CONSENT_ACTIVE`)
- `consent.revoked` — согласие отозвано (`status: CONSENT_REVOKED`, `revokeReason`)
- `consent.expired` — истёк срок действия (`status: CONSENT_EXPIRED`)
- `consent.suspended` — приостановлено (`status: CONSENT_SUSPENDED`)
- `consent.failed` — регистрация отклонена (`status: CONSENT_FAILED`)

Тело (`consent.revoked`):
```json
{
  "eventId": "evt_…",
  "type": "consent.revoked",
  "consentId": "cst_5e7a9b1c",
  "status": "CONSENT_REVOKED",
  "revokeReason": "Отозвано плательщиком",
  "timestamp": "2026-10-15T12:00:00.000Z"
}
```

Тело `payment.completed` для рекуррентного списания дополнительно содержит `paymentType: "RECURRENT"` и `consentId` (аддитивные опциональные поля).

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
- Расширение v0.2 (рекуррентные списания) — аддитивное: новые пути `/v1/consents/*` и опциональные поля `paymentType`/`consentId` в платеже; существующие потребители v0.1 не затрагиваются.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
