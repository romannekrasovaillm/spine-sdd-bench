# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (v0.1 — для A1; v0.2 — дельта `sbp-recurring-subscriptions`, для A1/A3 изменения)
- Версия контракта: 0.2 (аддитивно к 0.1: согласия, подписки, рекуррентные списания; ломающих изменений нет)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки), ADR-009 (защита данных согласия), AD-003, AD-009, AD-010

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

### 3.6 Регистрация согласия плательщика (подписки СБП)

`POST /v1/consents` (v0.2; `Idempotency-Key` обязателен)

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "maxAmountPerDebit": 100000,      // копейки: максимум на одно списание
  "maxAmountPerPeriod": 1000000,    // копейки: максимум за период
  "period": "P1M",                  // ISO 8601 duration
  "paymentPurpose": "Подписка «Кино+»",
  "validUntil": "2027-08-15T00:00:00.000Z",
  "redirectUrl": "https://merchant.example.com/subscription/return"
}
```

Ответ `201`:
```json
{
  "consentId": "cns_7b2e1f0a",
  "status": "PENDING_PAYER",
  "confirmationUrl": "https://qr.nspk.ru/…",
  "validUntil": "2027-08-15T00:00:00.000Z"
}
```

Правила: согласие активируется только после подтверждения плательщиком в приложении его банка (переход в `ACTIVE`). Согласие — данные ограниченного состава (ADR-009): полные реквизиты плательщика шлюзом не хранятся. Статусы: `CREATED | PENDING_PAYER | ACTIVE | SUSPENDED | REVOKED | EXPIRED | REJECTED`.

### 3.7 Состояние и отзыв согласия

- `GET /v1/consents/{consentId}` → `200 { consentId, status, tspId, maxAmountPerDebit, maxAmountPerPeriod, period, validUntil, activatedAt, revokedAt }`.
- `POST /v1/consents/{consentId}/revoke` (v0.2; `Idempotency-Key`) → `200 { consentId, status: "REVOKED", revokedAt }`. Отзыв **необратим**; после него новые списания запрещены (AD-009). Плательщик также может отозвать согласие в своём банке — шлюз получит событие от НСПК.

### 3.8 Подписка

- `POST /v1/subscriptions` (v0.2; `Idempotency-Key`): `{ tspId, consentId, paymentPurpose, merchantOrderId? }` → `201 { subscriptionId, consentId, status: "ACTIVE", … }`. Требует согласие в состоянии `ACTIVE`; иначе `422 CONSENT_NOT_ACTIVE`.
- `GET /v1/subscriptions/{subscriptionId}` → `200 Subscription`.
- `PATCH /v1/subscriptions/{subscriptionId}` (v0.2; `Idempotency-Key`): `{ status?: ACTIVE|PAUSED|CANCELLED, amount?, paymentPurpose? }` → `200 Subscription`. Изменения — в пределах лимитов согласия.

### 3.9 Рекуррентное списание (pull ТСП)

`POST /v1/subscriptions/{subscriptionId}/debits` (v0.2; `Idempotency-Key` обязателен)

Запрос:
```json
{
  "billingKey": "2026-09",          // ключ периода/попытки; ТСП задаёт
  "amount": 99900,                  // опционально, если не задано в подписке
  "merchantOrderId": "sub-12345-2026-09"
}
```

Ответ `201` — объект `Payment` с `paymentType: "recurring"`, `consentId`, `subscriptionId`, `billingKey`.

Правила:
- Идемпотентность — по паре `(consentId, billingKey)` (AD-010) в дополнение к `Idempotency-Key`: повтор возвращает ранее созданный `paymentId`, новое списание не создаётся.
- Списание невозможно при согласии не в `ACTIVE` → `422 CONSENT_NOT_ACTIVE` (AD-009).
- Превышение лимитов согласия → `422 CONSENT_LIMIT_EXCEEDED`.
- **Зачисление — только по подтверждённому НСПК статусу `PAID`** (AD-005 не меняется). Рекуррентное списание проходит `CREATED → PAID → CREDITED → COMPLETED` без фазы `QR_ISSUED`.
- **Policy по in-flight списанию при отзыве согласия** — решение человека (A3), см. `changes/sbp-recurring-subscriptions/DELTA.md`.

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `CONSENT_NOT_ACTIVE` (422, v0.2), `CONSENT_LIMIT_EXCEEDED` (422, v0.2), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `consent.activated` (v0.2) — согласие подтверждено плательщиком (`status: ACTIVE`)
- `consent.revoked` (v0.2) — согласие отозвано (плательщиком или ТСП)
- `consent.expired` (v0.2) — истёк срок действия согласия
- `subscription.updated` (v0.2) — изменено состояние подписки (пауза/возобновление/отмена)

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
- **v0.2 подтверждена как аддитивная**: `arch contract-diff openapi/tsp-api.yaml@v0.1 openapi/tsp-api.yaml@v0.2` → breaking: 0. Новые пути и необязательные поля; существующие потребители не затрагиваются.

## 7. Открытые вопросы (для A1/A3)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. **(v0.2)** Точный протокол сервиса согласий/автоплатежей НСПК (поля, таймауты, события) — внешний вход [ТРЕБУЕТ ПРОВЕРКИ].
6. **(v0.2)** Policy по in-flight списанию при отзыве согласия (зачислить и вернуть vs отклонить) — решение человека (A3).
7. **(v0.2)** Владение расписанием списаний: pull ТСП (выбрано, ADR-008) vs банковский планировщик — подтверждение продукта.
8. **(v0.2)** Состав и срок хранения данных согласия (ПДн) — DPO/юристы (ADR-009).
