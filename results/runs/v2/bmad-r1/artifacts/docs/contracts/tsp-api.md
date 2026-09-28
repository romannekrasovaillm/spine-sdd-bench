# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (аддитивное расширение v0.1 под мандаты и рекуррентные списания, ADR-008; нестабильная до A1)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (рекуррентные C2B), AD-003 (spine)

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

### 3.6 Регистрация мандата (согласие на рекуррентные списания)

`POST /v1/mandates`

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "payerRef": "payer_tok_…",        // токенизированный/маскированный идентификатор плательщика (ПДн не передаются)
  "purpose": "Подписка «Кинопоиск+», тариф Стандарт",
  "limits": {
    "maxAmountPerDebit": 49900,     // максимум за одно списание, копейки
    "maxTotalAmount": 49900,        // максимум за период, копейки (опц.)
    "maxDebitsPerPeriod": 1,        // максимум списаний за период (опц.)
    "period": "MONTH",              // DAY | WEEK | MONTH | YEAR | TOTAL
    "currency": "RUB"
  },
  "validUntil": "2027-09-28T00:00:00.000Z", // опц.
  "merchantOrderId": "sub-98765"    // сквозной идентификатор подписки у ТСП (опц.)
}
```

Ответ `201`:
```json
{
  "mandateId": "mnd_3c7a91e2",
  "tspId": "tsp_9f3c2a1b",
  "status": "PENDING_CONSENT",
  "limits": { "maxAmountPerDebit": 49900, "maxTotalAmount": 49900, "maxDebitsPerPeriod": 1, "period": "MONTH", "currency": "RUB" },
  "purpose": "Подписка «Кинопоиск+», тариф Стандарт",
  "payerRef": "payer_tok_…",
  "validUntil": "2027-09-28T00:00:00.000Z",
  "createdAt": "2026-09-28T10:00:00.000Z",
  "activatedAt": null,
  "consentRef": "consent_…"
}
```

Правила: `Idempotency-Key` обязателен; повтор с тем же ключом → тот же `mandateId`. Мандат **не создаёт платёж**. Согласие подтверждает плательщик в приложении своего банка по каналу ОПКЦ; до перехода в `ACTIVE` списания невозможны. Лимиты контролируются шлюзом (AD-009); НСПК может контролировать дополнительно. Границы лимитов/периода — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].

### 3.7 Состояние мандата

`GET /v1/mandates/{mandateId}` → `200 Mandate`

Статусы мандата: `CREATED | PENDING_CONSENT | ACTIVE | SUSPENDED | DECLINED | REVOKED | EXPIRED`. `REVOKED`/`EXPIRED`/`DECLINED` — терминальные; повторные триггеры идемпотентны.

### 3.8 Отзыв/приостановка мандата

`POST /v1/mandates/{mandateId}/revoke`

Запрос (тело опц.): `{ "reason": "Заявление клиента" }`

Ответ `200`: `Mandate` с `status: REVOKED`, `revokedAt`, `revokedBy` (`TSP | PAYER | BANK`).

Правила: идемпотентно по `mandateId` — повторный отзыв возвращает текущее состояние (не ошибку). После `REVOKED` новые списания отклоняются немедленно (AD-009); уже начатые списания доводятся по своей саге. Отзыв плательщиком приходит событием ОПКЦ и приоритетен.

### 3.9 Рекуррентное списание по мандату

`POST /v1/mandates/{mandateId}/payments`

Запрос:
```json
{
  "amount": 49900,                  // <= maxAmountPerDebit и в пределах периода
  "currency": "RUB",
  "merchantOrderId": "inv-2026-10", // период/счёт у ТСП (опц.)
  "paymentPurpose": "Абонентская плата за октябрь 2026"
}
```

Ответ `201`: ресурс `Payment` (`paymentId`, `status: CREATED`, `initiationType: MANDATE`, `mandateId`).

Правила: `Idempotency-Key` обязателен; повтор → тот же `paymentId`, второго списания нет. Guard-проверки **до** вызова ОПКЦ: мандат `ACTIVE`; `amount ≤ maxAmountPerDebit`; сумма за период ≤ `maxTotalAmount`; число списаний за период ≤ `maxDebitsPerPeriod`; `now ≤ validUntil`; валюта совпадает; ТСП активен. Нарушение → `422` без вызова ОПКЦ и без финансового действия. Дальнейший жизненный цикл — **та же статусная машина**, что и у QR-платежа, но без `QR_ISSUED`: `CREATED → PAID (дебет подтверждён банком плательщика/НСПК) → CREDITED → COMPLETED`; отказ → `FAILED` с `errorCode` (например, `DEBIT_DECLINED`). Зачисление — только из `PAID` (AD-005, AD-010).

### 3.10 История списаний по мандату

`GET /v1/mandates/{mandateId}/payments?limit=50` → `200 { "items": [ Payment, … ] }`

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

Коды v0.2 (мандаты, ADR-008): `MANDATE_NOT_FOUND` (404), `MANDATE_NOT_ACTIVE` (422), `MANDATE_REVOKED` (422), `MANDATE_EXPIRED` (422), `AMOUNT_EXCEEDS_MANDATE_LIMIT` (422), `MANDATE_LIMIT_EXCEEDED` (422). Отказ банка плательщика по конкретному списанию — не HTTP-ошибка: платёж переходит в `FAILED`, `errorCode: DEBIT_DECLINED` (виден в `GET /v1/payments/{paymentId}` и вебхуке `payment.failed`).

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка (в т.ч. отказ по рекуррентному списанию)
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `mandate.activated` — плательщик подтвердил согласие, мандат `ACTIVE` (ADR-008)
- `mandate.declined` — плательщик отказал, мандат `DECLINED`
- `mandate.revoked` — мандат отозван (ТСП/плательщиком/банком)
- `mandate.expired` — истёк срок действия мандата

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

Тело мандатного события (`mandate.activated`):
```json
{
  "eventId": "evt_…",
  "type": "mandate.activated",
  "mandateId": "mnd_3c7a91e2",
  "status": "ACTIVE",
  "timestamp": "2026-09-28T10:05:00.000Z"
}
```

Доставка: ответ ТСП `2xx` = успех; иначе ретрай (экспоненциальная задержка + джиттер), после исчерпания — DLQ. ТСП обязан отвечать идемпотентно по `eventId`.

## 6. Версионирование и совместимость

- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.
- Добавление опциональных полей — обратно совместимо, не требует новой версии.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.
- **Совместимость v0.2 (ADR-008):** расширение мандатов — аддитивное. Существующие пути `/v1/payments*` не изменены; `PaymentRequest` и перечень значений `Payment.status` не изменены и не удалены; новые поля `Payment` (`initiationType`, `mandateId`) — опциональные; мандатные схемы и пути добавлены. Проверка совместимости — в критериях приёмки пакета изменения (contract-compat test).

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. (v0.2) Модель мандата и канала подтверждения согласия — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
6. (v0.2) Полнота модели лимитов (`maxTotalAmount`, `maxDebitsPerPeriod`, `period`) — согласовать с бизнесом и НСПК.
7. (v0.2) Планировщик биллинга: остаётся на стороне ТСП (ADR-008); подтвердить, что банк не берёт на себя календарь подписок.
8. (v0.2) Канал отзыва мандата плательщиком (только через НСПК/приложение банка плательщика) — уточнить по документации НСПК.
