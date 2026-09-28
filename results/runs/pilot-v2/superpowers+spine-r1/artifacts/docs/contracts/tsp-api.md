# Контракт API ТСП (мерчант-API) — v0.2 draft (дельта подписок)

- Status: Draft (для ревью на гейте A1 дельты `changes/sbp-subscriptions`)
- Версия контракта: 0.2 (аддитивное расширение v0.1; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки/мандат), ADR-009 (списания), AD-003, AD-009, AD-010, AD-011 (spine)
- Совместимость: v0.2 **не ломает** потребителей v0.1 — только новые пути и опциональные поля (подтверждено `contract_diff`: 0 breaking)

Назначение: контракт между **ТСП/мерчантом** и **СБП-шлюзом банка** (ядро, собственная разработка). Контракт **не зависит** от протокола ОПКЦ СБП (AD-008): адаптер НСПК скрыт за внутренним интерфейсом шлюза.

## 1. Общие положения

- Транспорт: **HTTPS, REST/JSON**, версия пути `/v1`.
- Кодировка: UTF-8. Числа сумм — **целые, в копейках** (minor units), валюта — `RUB` (ISO 4217: 643).
- Временные метки — ISO 8601 (UTC), формат `YYYY-MM-DDTHH:MM:SS.sssZ`.
- Авторизация ТСП: **mTLS** (сертификат ТСП, выпущенный УЦ банка) + `X-API-Key`. Детали финализирует ИБ на A4; для v0.1 — mTLS обязателен.
- **Привязка ресурсов к ТСП (v0.2):** каждый ресурс (`paymentId`, `subscriptionId`, `chargeId`, `refundId`) принадлежит аутентифицированному ТСП (сертификат mTLS ↔ `tspId`); доступ к чужому ресурсу → `403 FORBIDDEN_RESOURCE` без раскрытия факта его существования. Это закрывает IDOR-класс на интерфейсе, инициирующем списания. `403` возвращается **всеми** resource-scoped методами (платежи, подписки, списания, возвраты), а не только списаниями.
- Rate limiting: по умолчанию 50 req/s на ТСП (конфигурируемо); превышение — `429` + заголовок `Retry-After`.
- Корреляция: каждый ответ содержит `X-Trace-Id` (генерируется шлюзом, прокидывается в логи/SIEM).

## 2. Идемпотентность

- Заголовок `Idempotency-Key` **обязателен** для всех `POST`.
- Ключ генерирует ТСП (UUID); шлюз хранит маппинг ключ → ресурс **24 часа**.
- Повторный `POST` с тем же ключом и тем же телом → возвращается **тот же ресурс** (тот же `paymentId`/`refundId`/`subscriptionId`/`chargeId`), статус 200/201 без повторного действия.
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
  "merchantOrderId": "order-12345", // опц., сквозной для ТСП
  "subscriptionId": "sub_…"        // опц. (v0.2): привязать платёж к подписке
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

### 3.6 Создание подписки (инициирование согласия) — v0.2

`POST /v1/subscriptions` (обязателен `Idempotency-Key`)

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "amountMode": "FIXED",           // FIXED | VARIABLE
  "amount": 49900,                 // при FIXED; копейки
  "maxAmount": 150000,             // при VARIABLE — лимит одного списания
  "currency": "RUB",
  "period": "MONTHLY",             // периодичность плановых списаний
  "dayOfPeriod": 5,                // день периода для планового списания
  "expiresAt": "2027-08-15T00:00:00.000Z",
  "merchantOrderId": "sub-12345",
  "description": "Подписка «Кинопоиск+, 1 месяц»"
}
```

Ответ `201`:
```json
{
  "subscriptionId": "sub_5c7d9e",
  "status": "PENDING_CONSENT",
  "amountMode": "FIXED",
  "amount": 49900,
  "currency": "RUB",
  "consentUrl": "https://qr.nspk.ru/…", // подтверждение согласия плательщиком
  "nextChargeAt": null,
  "createdAt": "2026-09-28T10:00:00.000Z"
}
```

Правила: до подтверждения плательщиком (`ACTIVE`) ни одно `charge` не создаётся (AD-009). Условия мандата (лимит, режим суммы, период) иммутабельны после `ACTIVE`; изменение — новая подписка. Для `amountMode=VARIABLE` обязательны `maxAmount` **и** `maxAmountPerPeriod`; `period` — из перечня (`WEEKLY|MONTHLY|QUARTERLY|ANNUAL`), `dayOfPeriod` — 1–28. Несогласованные комбинации отвергаются (валидация на A4; тест AC).

### 3.7 Управление подпиской — v0.2

`GET /v1/subscriptions/{subscriptionId}` → `200 { subscriptionId, status, amountMode, amount|maxAmount, currency, mandateRef, nextChargeAt, activatedAt, revokedAt, merchantOrderId }`

`POST /v1/subscriptions/{subscriptionId}/suspend` → `200 { … status: "PAUSED" }` (будущие списания не создаются)
`POST /v1/subscriptions/{subscriptionId}/resume` → `200 { … status: "ACTIVE" }`
`POST /v1/subscriptions/{subscriptionId}/revoke` → `200 { … status: "REVOKED" }` (остановка будущих списаний, AD-011)

Статусы: `PENDING_CONSENT | ACTIVE | PAUSED | REVOKED | EXPIRED | FAILED_CONSENT` (см. `docs/spec/subscription-state-machine.md`).

### 3.8 Списания по подписке — v0.2

`POST /v1/subscriptions/{subscriptionId}/charges` (обязателен `Idempotency-Key`) — **только для `amountMode=VARIABLE`**; для `FIXED`-подписок списания инициирует исключительно движок шлюза.

Запрос:
```json
{
  "amount": 87300,                 // <= maxAmount и maxAmountPerPeriod мандата
  "billingReference": "2026-09",   // опц.: корреляционная ссылка ТСП (период определяет шлюз из расписания)
  "description": "ЖКУ, сентябрь 2026"
}
```

Ответ `201`:
```json
{ "chargeId": "chg_…", "subscriptionId": "sub_5c7d9e", "amount": 87300, "status": "SCHEDULED", "dunning": false }
```

Правила: `periodKey` **вычисляет шлюз** из расписания подписки и даты (MSK), а не ТСП; `billingReference` — необязательная корреляционная ссылка. **Один periodKey = один charge** (AD-010): повтор за тот же календарный период (даже с другим `Idempotency-Key`) возвращает существующий charge, а не создаёт второй дебет. Лимит `maxAmountPerPeriod` действует на тот же календарный период. Для `FIXED` → `422 CHARGE_NOT_ALLOWED_FOR_FIXED`; превышение `maxAmount`/`maxAmountPerPeriod` → `422 AMOUNT_EXCEEDS_MANDATE`/`422 AMOUNT_EXCEEDS_PERIOD`.

`GET /v1/subscriptions/{subscriptionId}/charges` → `200 [ { chargeId, subscriptionId, paymentId, amount, status, billingPeriod, dunning, createdAt, completedAt, errorCode } ]`

Статусы charge: `SCHEDULED | INITIATED | PAID | CREDITED | COMPLETED | FAILED`. Плановые списания по расписанию создаёт движок шлюза (ADR-009); ТСП их видит в списке, отдельный запрос не требуется.

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500).
Коды подписок (v0.2): `SUBSCRIPTION_NOT_ACTIVE` (422), `AMOUNT_EXCEEDS_MANDATE` (422), `AMOUNT_EXCEEDS_PERIOD` (422), `CHARGE_NOT_ALLOWED_FOR_FIXED` (422), `SUBSCRIPTION_TERMINAL` (422 — операция над `REVOKED`/`EXPIRED`), `FORBIDDEN_RESOURCE` (403).
Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События платежей:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`

События подписок (v0.2):
- `subscription.activated` — согласие подтверждено, подписка `ACTIVE`
- `subscription.failed` — согласие не получено (`FAILED_CONSENT`)
- `subscription.paused` / `subscription.resumed`
- `subscription.revoked` — согласие отозвано (ТСП или плательщиком)
- `subscription.expired` — истёк срок мандата
- `charge.completed` — списание зачислено (`COMPLETED`)
- `charge.failed` — списание не удалось после dunning-политики
- `charge.dunning` — идут повторные попытки списания (опц., конфигурируемо)

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

Тело (`charge.completed`) дополнительно содержит `subscriptionId`, `chargeId`, `billingPeriod`.

Доставка: ответ ТСП `2xx` = успех; иначе ретрай (экспоненциальная задержка + джиттер), после исчерпания — DLQ. ТСП обязан отвечать идемпотентно по `eventId`.

## 6. Версионирование и совместимость

- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.
- Добавление опциональных полей — обратно совместимо, не требует новой версии.
- **v0.2 — аддитивное расширение v0.1**: новые пути `/v1/subscriptions*`, новые опциональные поля (`subscriptionId`, `chargeId`, `origin`), новые события вебхуков. Ни один существующий путь/поле не изменился и не удалён; `contract_diff` v0.1→v0.2 — 0 breaking.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 7. Открытые вопросы (для A1 дельты)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ]. Лимиты мандата подписок (per-charge, per-period, общий) — `[ТРЕБУЕТ ПРОВЕРКИ]`.
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Подписки: обязательность предварительного уведомления плательщика перед списанием и его форма — по регламенту НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`.
6. Подписки: переменная сумма и расписание — набор поддерживаемых режимов подтверждает бизнес (A3).
