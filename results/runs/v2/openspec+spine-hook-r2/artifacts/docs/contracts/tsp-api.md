# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (аддитивно к 0.1: рекуррентные списания по согласию; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (согласие/рекуррент), ADR-009 (отзыв), AD-003, AD-005, AD-009, AD-010 (spine)

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
  "status": "COMPLETED",           // CREATED | QR_ISSUED | DEBIT_PENDING | PAID | CREDITED | COMPLETED | FAILED | EXPIRED | REFUNDED
  "initiationType": "qr",          // qr | debit; для существующих потребителей отсутствие поля означает qr
  "consentId": null,               // заполнено для initiationType=debit
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

## 3а. Рекуррентные списания (подписки СБП) — новое в 0.2

Мандат на рекуррентное списание — **согласие плательщика**, подтверждаемое в СБП (ADR-008). Рекуррентное списание — платёж с `initiationType = debit`; зачисление по нему возможно только из `PAID` (AD-005). Новые `POST` требуют `Idempotency-Key`.

### 3а.1 Регистрация согласия

`POST /v1/consents`

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "maxAmountPerDebit": 200000,     // лимит на одно списание, копейки
  "maxAmountPerPeriod": 500000,    // лимит суммы за период, копейки
  "periodicity": "MONTHLY",        // DAILY | WEEKLY | MONTHLY
  "maxDebitsPerPeriod": 1,
  "validUntil": "2027-08-15T00:00:00.000Z",
  "description": "Подписка «Кинозал»",
  "merchantOrderRef": "sub-12345"
}
```

Ответ `201`:
```json
{
  "consentId": "cons_1a2b3c",
  "tspId": "tsp_9f3c2a1b",
  "status": "PENDING",
  "confirmationUrl": "https://qr.nspk.ru/…",   // плательщик подтверждает в своём банке
  "maxAmountPerDebit": 200000,
  "maxAmountPerPeriod": 500000,
  "periodicity": "MONTHLY",
  "validUntil": "2027-08-15T00:00:00.000Z"
}
```

Правила: согласие становится `ACTIVE` **только по подтверждению НСПК** (AD-009); в состоянии `PENDING` списания запрещены. Лимиты обязательны.

### 3а.2 Статус согласия

`GET /v1/consents/{consentId}` → `200 { consentId, status, лимиты, activatedAt, revokedAt }`, где `status ∈ {PENDING, ACTIVE, SUSPENDED, REVOKED, EXPIRED}`.

### 3а.3 Отзыв согласия

`POST /v1/consents/{consentId}/revoke` (Idempotency-Key) → `200 { consentId, status: "REVOKED" }`.

Правила (ADR-009): отзыв немедленно запрещает новые списания; уже подтверждённые НСПК (`PAID`) списания доводятся до завершения; неподтверждённые переводятся в `FAILED` с причиной `CONSENT_REVOKED`.

### 3а.4 Подписка

`POST /v1/subscriptions` (Idempotency-Key):
```json
{ "tspId": "tsp_9f3c2a1b", "consentId": "cons_1a2b3c", "merchantOrderId": "order-12345", "description": "Подписка «Кинозал»" }
```
Ответ `201`: `{ "subscriptionId": "sub_77aa11", "tspId": "…", "consentId": "cons_1a2b3c", "status": "ACTIVE" }`.
`GET /v1/subscriptions/{subscriptionId}` → `200 { subscriptionId, status, consentId, merchantOrderId }`, `status ∈ {ACTIVE, SUSPENDED, CANCELLED}`.

### 3а.5 Инициация рекуррентного списания

`POST /v1/subscriptions/{subscriptionId}/debits` (Idempotency-Key):
```json
{ "amount": 19900, "billingPeriod": "2026-10", "paymentPurpose": "Подписка «Кинозал», октябрь" }
```
Ответ `201` — объект `Payment`: `{ "paymentId": "pay_…", "status": "DEBIT_PENDING", "initiationType": "debit", "consentId": "cons_1a2b3c", "subscriptionId": "sub_77aa11", "billingPeriod": "2026-10", "amount": 19900 }`.

Правила (AD-009, AD-010): списание разрешено только при согласии `ACTIVE` и в пределах лимитов; шлюз **нормализует** `billingPeriod` по `periodicity` согласия (значение ТСП не является доверенным) и допускает **не более одного успешного** списания за период; повторная инициация за тот же период возвращает существующее незавершённое/успешное списание, а повтор после терминального `FAILED` создаёт новую попытку. Далее платёж идёт по статусной машине: `DEBIT_PENDING → PAID → CREDITED → COMPLETED` (терминальные `FAILED`, `EXPIRED`, `REFUNDED`). Списание проходит те же антифрод/AML-контроли, что и обычный платёж. Возврат по завершённому списанию разрешён в том числе после отзыва согласия.

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `CONSENT_NOT_ACTIVE` (403/422), `SUBSCRIPTION_NOT_ACTIVE` (422), `CONSENT_REVOKED` (422), `LIMIT_EXCEEDED` (422), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `consent.activated` — согласие подтверждено и активно (новое в 0.2)
- `consent.revoked` — согласие отозвано (плательщиком, ТСП или банком) (новое в 0.2)
- `consent.expired` — истёк срок согласия (новое в 0.2)

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
- 0.1 → 0.2 — аддитивное расширение (новые пути согласий/подписок/списаний, новые значения enum, новые события вебхуков); ломающих изменений нет (проверено `contract_diff`).
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Владелец расписания периодов (шлюз-планировщик vs ТСП-инициатор) — design D5, решение бизнеса/продукта; контракт 0.2 предполагает инициатора ТСП.
6. Нужен ли `SUSPENDED` (приостановка) в первой волне или достаточно `ACTIVE/REVOKED/EXPIRED` — влияет на enum, не на инварианты.
7. Точные значения `periodicity`, лимитов и сроков согласия — по документации НСПК по подпискам [ТРЕБУЕТ ПРОВЕРКИ].
8. Пороговые сценарии антифрод/AML для рекуррентных списаний — владелец ИБ.
