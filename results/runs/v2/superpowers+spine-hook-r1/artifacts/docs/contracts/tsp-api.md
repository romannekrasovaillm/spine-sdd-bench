# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1 эпика СБП-подписок)
- Версия контракта: 0.2 (аддитивное расширение 0.1: СБП-подписки; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки), AD-003 (spine)

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

### 3.6 Согласия на рекуррентные списания (СБП-подписки)

> Добавлено в v0.2 (аддитивно; ADR-008). Согласие (мандат) — основание для рекуррентных списаний. Рекуррентное списание — обычный платёж с полем `mandateId`.

**Запрос согласия** — `POST /v1/mandates` (`Idempotency-Key` обязателен):

```json
{
  "tspId": "tsp_9f3c2a1b",
  "purpose": "Подписка «Кино+», 1 месяц",
  "amountPerCharge": 39900,
  "amountLimitPerCharge": 39900,
  "period": "MONTHLY",
  "startDate": "2026-10-01",
  "untilDate": "2027-10-01",
  "redirectUrl": "https://merchant.example.com/subscription/return"
}
```

Ответ `201`:
```json
{
  "mandateId": "man_7c2f1e9a",
  "status": "PENDING",
  "consentUrl": "https://qr.nspk.ru/…",
  "amountPerCharge": 39900,
  "amountLimitPerCharge": 39900,
  "period": "MONTHLY",
  "createdAt": "2026-09-28T10:00:00.000Z"
}
```

Правила: `amountPerCharge` — плановая сумма одного списания (её использует автосписание планировщика), `amountLimitPerCharge` — жёсткий лимит и не меньше `amountPerCharge`; плательщик подтверждает согласие в своём банке; до подтверждения статус `PENDING`, списания запрещены. `consentUrl` может быть заполнена не сразу, если регистрация в ОПКЦ асинхронна (тогда — из `GET` или события `mandate.pending`). Параметры согласия после `ACTIVE` иммутабельны — изменение лимита/суммы/срока требует нового согласия.

**Статус согласия** — `GET /v1/mandates/{mandateId}`; **список** — `GET /v1/mandates?status=…` (`PENDING | ACTIVE | SUSPENDED | REVOKED | EXPIRED`).

**Отзыв согласия** — `POST /v1/mandates/{mandateId}/revoke` (`Idempotency-Key` обязателен) → `200 { mandateId, status: "REVOKED", revokedAt }`. Идемпотентно; после фиксации отзыва новые списания невозможны, завершённые не откатываются. Приостановка согласия (`SUSPENDED`) — операция банка/антифрода (4-eyes), не метод ТСП; приостановить списания ТСП может через отзыв.

**Рекуррентное списание** — `POST /v1/mandates/{mandateId}/charges` (`Idempotency-Key` обязателен):

```json
{
  "amount": 39900,                 // <= amountLimitPerCharge; автосписание планировщика = amountPerCharge
  "periodKey": "2026-10",          // детерминированный ключ периода согласия; ключ идемпотентности (mandateId, periodKey)
  "merchantOrderId": "sub-2026-10"
}
```

Ответ `201` — объект `Payment` (та же статусная модель, без `QR_ISSUED`), в ответе присутствуют `mandateId` и `periodKey`. **Один период списывается один раз независимо от инициатора** (планировщик или ТСП): повтор с тем же `(mandateId, periodKey)`/`Idempotency-Key` не создаёт второе списание; тот же период с другой суммой → `409 IDEMPOTENCY_CONFLICT`. Списание при не-`ACTIVE` согласии → `422 MANDATE_NOT_ACTIVE`; превышение лимита → `422 MANDATE_LIMIT_EXCEEDED`; устаревший/неподтверждённый статус согласия → `422 MANDATE_STATE_STALE`.

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `MANDATE_NOT_FOUND` (404), `MANDATE_NOT_ACTIVE` (422), `MANDATE_REVOKED` (422), `MANDATE_LIMIT_EXCEEDED` (422), `MANDATE_STATE_STALE` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `mandate.pending` — согласие зарегистрировано в ОПКЦ, получена ссылка/QR для плательщика
- `mandate.activated` — согласие подтверждено плательщиком (`status: ACTIVE`)
- `mandate.suspended` — согласие приостановлено
- `mandate.revoked` — согласие отозвано
- `mandate.expired` — истёк срок действия согласия
- `mandate.charge.scheduled` — предстоящее рекуррентное списание (информационное событие для ТСП; **не является** уведомлением плательщика — уведомление плательщика идёт через внешнее звено, AD-012)

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
- v0.2 — аддитивное расширение v0.1 (подписки): добавлены пути `/v1/mandates*`, схемы `Mandate`/`MandateRequest`/`ChargeRequest`/`Problem`, поле `Payment.mandateId`, события `mandate.*` и коды `MANDATE_*`. Существующие пути, обязательные поля и перечень статусов платежа не изменялись; мажорная версия не требуется.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Срок предварительного уведомления плательщика перед рекуррентным списанием, срок хранения согласий и лимиты подписок — по правилам НСПК [ТРЕБУЕТ ПРОВЕРКИ].
6. Канал уведомления плательщика о предстоящем списании (банк плательщика / НСПК) — уточняется с НСПК и вендором.
7. Может ли плательщик задавать собственные лимиты (сумма/период) в согласии — на усмотрение продукта и НСПК.
