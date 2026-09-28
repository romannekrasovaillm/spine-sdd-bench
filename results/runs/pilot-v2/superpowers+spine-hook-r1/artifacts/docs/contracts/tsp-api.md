# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (нестабильная; до A1 фиксируется v1.0-draft). 0.2 добавляет согласия плательщика и регулярное списание — **обратно совместимо** (ADR-008, ADR-009)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (рекуррентные списания), ADR-009 (согласие), AD-003, AD-009

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

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`

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

## 8. Согласия плательщика и регулярные списания (v0.2; ADR-008, ADR-009)

Машинное описание — `openapi/tsp-api.yaml` (версия 0.2.0). Раздел описывает смысл и правила, которых нет в схеме.

### 8.1 Регистрация согласия (подписки)

`POST /v1/mandates` (заголовок `Idempotency-Key` обязателен)

```json
{
  "tspId": "tsp_9f3c2a1b",
  "maxAmountPerDebit": 59900,          // лимит одного списания, копейки
  "currency": "RUB",
  "periodicity": "MONTHLY",            // MONTHLY | WEEKLY | ON_DEMAND
  "validUntil": "2027-09-28T00:00:00.000Z",
  "paymentPurpose": "Подписка «Кино+», ежемесячно",
  "merchantOrderId": "sub-12345"
}
```

Ответ `201`:
```json
{
  "mandateId": "mnd_7c1a…",
  "tspId": "tsp_9f3c2a1b",
  "status": "PENDING_PAYER",
  "maxAmountPerDebit": 59900,
  "currency": "RUB",
  "periodicity": "MONTHLY",
  "validUntil": "2027-09-28T00:00:00.000Z"
}
```

Правила:

- После создания согласие переходит в `PENDING_PAYER` и ждёт подтверждения плательщика в его банке (событие ОПКЦ). До `ACTIVE` списания по нему невозможны.
- **Условия согласия неизменяемы** (ADR-009): изменить лимит/период/срок = создать новое согласие с полем `supersedes`.
- Статусы согласия: `PENDING_PAYER → ACTIVE → SUSPENDED / REVOKED / EXPIRED`; `REJECTED` — отказ плательщика или ОПКЦ. `REVOKED` и `EXPIRED` терминальны.
- Отзыв: `POST /v1/mandates/{mandateId}/revoke` (ТСП) или событие ОПКЦ (плательщик). Отзыв **немедленно** запрещает новые списания; повторный отзыв идемпотентен.

### 8.2 Регулярное списание

`POST /v1/payments` с `mandateId` (тело — как в §3.2, плюс два поля):

```json
{
  "tspId": "tsp_9f3c2a1b",
  "mandateId": "mnd_7c1a…",
  "occurrenceKey": "2026-10",          // метка периода серии
  "amount": 59900,
  "currency": "RUB",
  "paymentPurpose": "Подписка «Кино+», октябрь 2026",
  "merchantOrderId": "order-12345"
}
```

Правила:

- Ответ и статусная модель — как у обычного платежа (`§3.3`); QR-поля (`qrId`, `qrUrl`, `qrImage`) в ответе отсутствуют, статус `QR_ISSUED` не наступает.
- **Guard до обращения в ОПКЦ**: согласие `ACTIVE`; `amount ≤ maxAmountPerDebit`; `now ∈ [validFrom, validUntil]`; валюта совпадает. Нарушение → `422` (`MANDATE_NOT_ACTIVE`, `AMOUNT_EXCEEDS_MANDATE_LIMIT`) — платёж не создаётся и ОПКЦ не вызывается.
- **Идемпотентность серии**: ключ (`mandateId`, `occurrenceKey`). Повтор запроса с тем же ключом возвращает тот же `paymentId` без второго обращения в ОПКЦ и без второго зачисления. Дополнительно действует общий `Idempotency-Key` (§2).
- Зачисление — только из подтверждённого статуса `PAID` (AD-005); наступление периода само по себе зачислением не является.
- Неопределённый исход обращения к ОПКЦ (таймаут): повторная отправка списания запрещена, выполняется только запрос статуса; операция остаётся открытой (`CREATED`) до терминального статуса или сверки (AD-011).

### 8.3 Новые коды ошибок

`MANDATE_NOT_ACTIVE` (422), `MANDATE_NOT_FOUND` (404), `AMOUNT_EXCEEDS_MANDATE_LIMIT` (422), `OCCURRENCE_ALREADY_DEBITED` (422 — период уже успешно списан по этому согласию), `OCCURRENCE_OUT_OF_PERIOD` (422 — `occurrenceKey` не соответствует ожидаемому периоду для `periodicity`), `MANDATE_EXPIRED` (422).

### 8.4 Новые вебхуки

К событиям §5 добавляются: `mandate.activated`, `mandate.rejected`, `mandate.suspended`, `mandate.revoked`, `mandate.expired`, `payment.debit_failed` (списание по согласию не выполнено). Требования к доставке и дедупликации — как в §5 (`X-SBP-Event-Id`, `X-SBP-Signature`).

### 8.5 Обратная совместимость

- Новые поля запроса/ответа — **опциональны**; отсутствие `mandateId` сохраняет прежнее поведение одноразового платежа.
- Значения `Payment.status` **не изменены** (ADR-008 §2): новых статусов платежа не добавлено.
- Новые методы (`/v1/mandates*`) не затрагивают существующих потребителей.
- Добавлен код ответа `422` для `POST /v1/payments` (ранее не описан) — расширение, не изменение.
- Машинная проверка обратимости: `contract_diff` old↔new — 4 изменения, **breaking: 0**.
