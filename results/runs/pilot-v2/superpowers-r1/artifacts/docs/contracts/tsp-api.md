# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1; дельта 0.2 — на гейте A3 по ADR-008)
- Версия контракта: 0.2 (нестабильная; до A1 фиксируется v1.0-draft). Дельта 0.1→0.2 аддитивна: существующие пути, поля, `required` и enum не изменены
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (мандаты и рекуррентные списания), AD-003, AD-009 (spine)

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

### 3.6 Создание мандата (подписка) — дельта 0.2

`POST /v1/mandates`

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "amount": 49900,                 // копейки, сумма регулярного списания (шаблон)
  "currency": "RUB",
  "maxAmountPerDebit": 49900,      // потолок одного списания
  "periodicity": "MONTHLY",        // справочник значений — по НСПК [ТРЕБУЕТ ПРОВЕРКИ]
  "maxTotalAmount": 598800,        // опц., общий потолок за весь срок согласия
  "validUntil": "2027-08-15",      // опц., срок согласия; лимит срока — по НСПК [ТРЕБУЕТ ПРОВЕРКИ]
  "paymentPurpose": "Подписка «Кино+», ежемесячно",
  "merchantOrderId": "sub-12345"   // опц., сквозной идентификатор ТСП
}
```

Ответ `201`:
```json
{
  "mandateId": "man_7c2b1a9f",
  "status": "PENDING_CONSENT",
  "consentQrId": "QR-…",           // QR/ссылка на согласие (id в ОПКЦ, сквозной для сверки)
  "consentQrUrl": "https://qr.nspk.ru/…",
  "amount": 49900,
  "maxAmountPerDebit": 49900,
  "periodicity": "MONTHLY",
  "validUntil": "2027-08-15",
  "createdAt": "2026-09-28T10:00:00.000Z"
}
```

Правила: `Idempotency-Key` обязателен; согласие оформляется **существующим QR-флоу** (§3.2) — отдельный `qrType` не вводится; до подтверждения плательщиком мандат в `PENDING_CONSENT`, списания невозможны; после активации условия мандата (`amount`, `maxAmountPerDebit`, `periodicity`, `validUntil`) **иммутабельны** — изменение только новым мандатом.

### 3.7 Списание по мандату (внеочередное) — дельта 0.2

`POST /v1/mandates/{mandateId}/debits`

Запрос:
```json
{
  "amount": 49900,             // опц.; по умолчанию — сумма мандата; ≤ maxAmountPerDebit
  "debitRef": "debit-2026-10", // опц., сквозной идентификатор ТСП для сверки
  "paymentPurpose": "Подписка «Кино+» за октябрь"
}
```

Ответ `201`:
```json
{
  "paymentId": "pay_1f4d8c22",
  "mandateId": "man_7c2b1a9f",
  "amount": 49900,
  "status": "CREATED",
  "debitRef": "debit-2026-10"
}
```

Правила: `Idempotency-Key` обязателен; идемпотентность — по `(mandateId, periodKey)`: повторная инициация за тот же период возвращает тот же `paymentId` без второго списания; мандат должен быть `ACTIVE`; сумма ≤ `maxAmountPerDebit`; периодичность и срок соблюдены. Нарушение — `422` (`MANDATE_NOT_ACTIVE`, `MANDATE_LIMIT_EXCEEDED`). Платёж использует **те же** статусы, что и разовый (§3.3), и виден через `GET /v1/payments/{paymentId}`; признак рекуррентности — поле `mandateId`.

### 3.8 Управление мандатом — дельта 0.2

- `POST /v1/mandates/{mandateId}/revoke` → `200 { mandateId, status: "REVOKED", revokedAt }` — отзыв согласия (терминальный переход).
- `POST /v1/mandates/{mandateId}/suspend` → `200 { mandateId, status: "SUSPENDED" }` — приостановка списаний.
- `POST /v1/mandates/{mandateId}/resume` → `200 { mandateId, status: "ACTIVE" }` — возобновление (если срок и общий лимит не исчерпаны).

Правила: отзыв терминален — возврат к `ACTIVE` невозможен, только новое согласие (новый мандат); после отзыва новые списания невозможны (цель — ≤ 5 мин, `docs/nfr.md` §7); повторный отзыв/приостановка идемпотентны.

### 3.9 Статус мандата — дельта 0.2

`GET /v1/mandates/{mandateId}` → `200`

```json
{
  "mandateId": "man_7c2b1a9f",
  "status": "ACTIVE",
  "amount": 49900,
  "maxAmountPerDebit": 49900,
  "periodicity": "MONTHLY",
  "validUntil": "2027-08-15",
  "activatedAt": "2026-09-28T10:05:00.000Z",
  "debitedTotal": 99800,
  "lastDebit": { "paymentId": "pay_1f4d8c22", "amount": 49900, "status": "COMPLETED", "at": "2026-09-28T10:10:00.000Z" }
}
```

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Дельта 0.2: `MANDATE_NOT_FOUND` (404), `MANDATE_NOT_ACTIVE` (422), `MANDATE_LIMIT_EXCEEDED` (422 — превышение `maxAmountPerDebit`, периодичности или общего лимита). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`

События дельты 0.2 (мандаты; рекуррентное списание публикует **те же** `payment.*`, что и разовый платёж):
- `mandate.activated` — согласие подтверждено плательщиком, мандат активен (`status: ACTIVE`)
- `mandate.suspended` — списания приостановлены
- `mandate.revoked` — согласие отозвано (`status: REVOKED`)

ТСП обязан игнорировать неизвестные типы событий (прямая совместимость при добавлении новых типов).

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
- Дельта 0.1→0.2 (мандаты и рекуррентные списания, ADR-008) — **аддитивная**: добавлены новые пути `/v1/mandates*`, новые схемы и опциональное поле `mandateId` в `Payment`. Существующие пути, поля, `required` и enum (`status`, `qrType`) не изменены; переход на `/v2` не требуется. Проверка — дифф контракта v0.1→v0.2 в критерии приёмки A-10.

## 7. Открытые вопросы (для A1/A3)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ]. Для мандатов: справочник `periodicity`, максимальный срок согласия и максимальные суммы — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Дельта 0.2: формат `periodKey` в API списания (передаёт ТСП или вычисляет шлюз по периодичности и времени) — решение A3; влияет на идемпотентность внеочередных списаний.
6. Дельта 0.2: нужна ли ТСП выгрузка истории списаний/отзывов и в каком виде — решение A3 (объём первой волны).
