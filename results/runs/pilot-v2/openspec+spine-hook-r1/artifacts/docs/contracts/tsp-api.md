# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (0.1 → 0.2 **аддитивно** для изменения `add-sbp-subscriptions`; версия пути остаётся `/v1`, ломающих изменений нет — проверено `contract_diff`)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки СБП), AD-003, AD-009, AD-010 (spine)

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
- Для списаний по мандату (§3.9) действует **дополнительный ключ однократности** `(mandateId, invoiceId)`: повторная заявка на списание за тот же период подписки возвращает существующее списание и не создаёт второго финансового действия (AD-010), даже если ТСП использовал другой `Idempotency-Key`.

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

### 3.6 Создание мандата (согласия плательщика на рекуррентные списания)

`POST /v1/mandates`

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "amountLimit": 99900,            // копейки, максимум одного списания
  "periodLimit": 99900,            // копейки, максимум списаний за период
  "maxChargesPerPeriod": 1,
  "period": "MONTH",               // DAY | WEEK | MONTH | YEAR
  "validUntil": "2027-08-15T00:00:00.000Z",   // опц.
  "paymentPurpose": "Подписка «КиноПлюс», ежемесячно",
  "payerHint": "+7…"               // опц., подсказка для оформления согласия; ПДн минимизируются
}
```

Ответ `201`:
```json
{
  "mandateId": "mnd_4b7c9e21",
  "tspId": "tsp_9f3c2a1b",
  "status": "PENDING",
  "consentUrl": "https://…",
  "amountLimit": 99900,
  "periodLimit": 99900,
  "maxChargesPerPeriod": 1,
  "validUntil": "2027-08-15T00:00:00.000Z"
}
```

Правила: мандат создаётся в состоянии `PENDING`; согласие оформляется плательщиком в его банке, шлюз узнаёт об активации из ОПКЦ (событие `mandate.activated`). Лимиты и период обязательны, `amountLimit` > 0. `Idempotency-Key` обязателен.

### 3.7 Запрос состояния мандата

`GET /v1/mandates/{mandateId}`

Ответ `200`:
```json
{
  "mandateId": "mnd_4b7c9e21",
  "tspId": "tsp_9f3c2a1b",
  "status": "ACTIVE",              // PENDING | ACTIVE | REVOKED | EXPIRED | REJECTED
  "amountLimit": 99900,
  "periodLimit": 99900,
  "maxChargesPerPeriod": 1,
  "activatedAt": "2026-09-28T09:12:00.000Z",
  "revokedAt": null,
  "validUntil": "2027-08-15T00:00:00.000Z"
}
```

Примечание: состояние мандата — **проекция** состояния, подтверждённого ОПКЦ СБП; шлюз не поднимает статус «оптимистично» до подтверждения (AD-009).

### 3.8 Прекращение мандата по инициативе ТСП

`POST /v1/mandates/{mandateId}/cancel` → `202` (тело — `Mandate`).

Правила: доступность и семантика операции определяются протоколом СБП `[ТРЕБУЕТ ПРОВЕРКИ]`. Отзыв согласия **плательщиком** происходит в банке плательщика и приходит событием `mandate.revoked` независимо от этого метода. `Idempotency-Key` обязателен.

### 3.9 Списание по мандату

`POST /v1/mandates/{mandateId}/charges`

Запрос:
```json
{
  "invoiceId": "sub-2026-10",      // период подписки; вместе с mandateId — ключ однократности
  "amount": 99900,                 // копейки, ≤ amountLimit и в пределах periodLimit
  "paymentPurpose": "Подписка «КиноПлюс», октябрь 2026"
}
```

Ответ `201`:
```json
{
  "chargeId": "chg_77a1f0",
  "paymentId": "pay_8d1e4f5a",
  "mandateId": "mnd_4b7c9e21",
  "invoiceId": "sub-2026-10",
  "amount": 99900,
  "status": "CREATED"
}
```

Правила: списание возможно только по мандату в состоянии `ACTIVE`; при неподтверждённом/неизвестном состоянии — `422 MANDATE_UNKNOWN_STATE`; превышение лимитов — `422 MANDATE_LIMIT_EXCEEDED`; повтор за период — `409 CHARGE_ALREADY_EXISTS`. Созданный платёж проходит существующий жизненный цикл (`CREATED → PAID → CREDITED → COMPLETED`) **без** состояния `QR_ISSUED`; статус запрашивается тем же `GET /v1/payments/{paymentId}` (поле `initiationType` = `MANDATE`). `Idempotency-Key` обязателен.

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

Коды, добавленные изменением `add-sbp-subscriptions` (аддитивно): `MANDATE_NOT_ACTIVE` (422) — мандат не в состоянии `ACTIVE`; `MANDATE_LIMIT_EXCEEDED` (422) — превышены лимиты мандата; `MANDATE_EXPIRED` (422) — истёк срок действия мандата; `MANDATE_UNKNOWN_STATE` (422) — состояние мандата не подтверждено ОПКЦ (fail-closed, AD-009); `CHARGE_ALREADY_EXISTS` (409) — списание за этот `invoiceId` уже существует (AD-010).

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `mandate.activated` — плательщик оформил согласие, мандат активен (ADR-008)
- `mandate.revoked` — согласие отозвано (плательщиком в его банке или прекращено)
- `mandate.rejected` — мандат отклонён
- `mandate.expired` — истёк срок действия мандата

В событиях платежа, созданного списанием по мандату, добавляются опциональные поля `mandateId` и `invoiceId` (обратно совместимо).

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
- Изменение `add-sbp-subscriptions` (0.1 → 0.2) — **аддитивное**: только новые пути, новые схемы, опциональные поля и новые коды ошибок; публичный enum `Payment.status` не расширяется. Проверка `contract_diff` (старая-новая версия): breaking-изменений 0.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Подписки СБП (ADR-008, изменение `add-sbp-subscriptions`): доступность и семантика `POST /v1/mandates/{mandateId}/cancel` — по протоколу СБП `[ТРЕБУЕТ ПРОВЕРКИ]`.
6. Обязательность и форма подтверждения «первого списания» плательщиком — по регламенту НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`.
7. Максимальные лимиты мандата (сумма, число списаний за период) и допустимые периоды — по регламенту НСПК и продуктовой политике.
8. Формат уведомления плательщика о списании и ответственная сторона (банк-эквайер или банк плательщика) — ИБ/юристы.
