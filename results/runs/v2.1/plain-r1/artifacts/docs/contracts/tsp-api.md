# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (нестабильная; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки), AD-003, AD-009 (spine)

## 0. История версий

- **v0.1** — приём C2B: создание платежа/QR, статус, возврат.
- **v0.2** — аддитивное расширение: подписки СБП (рекуррентные списания). Новые пути и **опциональные** поля; существующие обязательные поля и значения enum не изменены (обратная совместимость, см. §6). Детали и обоснование — `docs/changes/sbp-subscriptions/04-contract-changes.md`.

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

### 3.6 Создание подписки (v0.2, рекуррентные списания)

`POST /v1/subscriptions` (заголовок `Idempotency-Key` обязателен)

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "amount": 39900,
  "currency": "RUB",
  "merchantOrderId": "sub-order-777",
  "paymentPurpose": "Подписка «Кино», месяц",
  "schedule": { "period": "MONTHLY", "dayOfMonth": 15, "startAt": "2026-10-15T00:00:00.000Z" }
}
```

Ответ `201`:
```json
{
  "subscriptionId": "sub_7a1b2c3d",
  "tspId": "tsp_9f3c2a1b",
  "amount": 39900,
  "status": "PENDING_OPKC",
  "schedule": { "period": "MONTHLY", "dayOfMonth": 15 },
  "nextDebitAt": "2026-10-15T00:00:00.000Z"
}
```

Правила: согласие плательщика регистрируется в ОПКЦ асинхронно (по аналогии с регистрацией ТСП, §3.1); до статуса `ACTIVE` списания не производятся. Согласие — неизменяемый аудируемый артефакт (AD-010). Сумма и расписание иммутабельны после активации; изменение — отмена и новая подписка.

### 3.7 Статус и отмена подписки (v0.2)

`GET /v1/subscriptions/{subscriptionId}` → `200 Subscription` (схема `Subscription`, статусы `PENDING_OPKC|ACTIVE|SUSPENDED|CANCELLED|DECLINED|EXPIRED`).

`POST /v1/subscriptions/{subscriptionId}/cancel` (`Idempotency-Key` обязателен) — отмена подписки / отзыв согласия → `200 { subscriptionId, status: "CANCELLED" }`. После отмены **новые циклы не создаются**, включая цикл, ещё не отправленный в ОПКЦ (AD-010).

### 3.8 Циклы списания (v0.2)

`GET /v1/subscriptions/{subscriptionId}/cycles` → `200 [Payment]` — список платежей-циклов. Каждый цикл — обычный платёж (§3.3), в его ответе присутствуют `subscriptionId` и `debitType: RECURRING`; зачисление и вебхуки — как у разового платежа (`payment.completed`).

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

Коды v0.2 (подписки): `SUBSCRIPTION_NOT_FOUND` (404), `SUBSCRIPTION_NOT_ACTIVE` (409), `MANDATE_REVOKED` (422 — попытка списания/изменения по отозванному согласию), `CYCLE_ALREADY_EXISTS` (409 — повторное создание цикла). Новые коды не изменяют семантику существующих.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`); для цикла подписки содержит `subscriptionId`
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `subscription.activated` (v0.2) — согласие подтверждено, подписка `ACTIVE`
- `subscription.declined` (v0.2) — согласие отклонено ОПКЦ
- `subscription.cancelled` (v0.2) — подписка отменена/согласие отозвано
- `subscription.debit.failed` (v0.2) — цикл списания не удался (отказ плательщика/ОПКЦ); успешное списание цикла отражается существующим `payment.completed`

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
- **v0.2 (подписки)** — аддитивное расширение: новые пути, новые опциональные поля (`Payment.subscriptionId`, `Payment.debitType`), новые схемы/события/коды. Обязательные поля и значения enum (`Payment.status`, `PaymentRequest.required`) **не изменены**. Статусы подписки — отдельный enum (не расширение `Payment.status`), чтобы не ломать строгих клиентов.
- Требование к ТСП-потребителю: игнорировать неизвестные поля и неизвестные типы вебхук-событий (forward-compatible). Потребитель v0.1, не использующий `/v1/subscriptions`, изменений поведения не наблюдает.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. (v0.2) Точная модель согласия и расписания списаний — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ]; форма согласия плательщика — юристы/ИБ.
6. (v0.2) Политика при отказе плательщика (число попыток, поведение подписки) — бизнес + регламент НСПК.
