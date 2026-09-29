# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (аддитивное расширение к 0.1; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки), AD-003 (spine), AD-009…AD-016
- Изменение: CS-001 — §6 «Подписки и рекуррентные списания» добавлен; §1–§5 не изменялись (обратная совместимость, см. §7).

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

## 6. Подписки и рекуррентные списания (v0.2, аддитивно)

Назначение: ТСП оформляет согласие плательщика на регулярные списания и инициирует списания по расписанию без QR. Подтверждение и отзыв согласия выполняет плательщик в приложении своего банка (AD-013); шлюз не собирает аутентификационные данные и полные реквизиты плательщика. Все операции подписок идут через единый адаптер ОПКЦ (AD-012).

### 6.1 Статусы

- Согласие (`subscriptionStatus`): `CREATED | PENDING_PAYER | ACTIVE | SUSPENDED | REVOKED | EXPIRED | DECLINED`.
- Списание (`status`, платёж типа `CONSENT`): канонические значения `Payment.status` — `CREATED | PAID | CREDITED | COMPLETED | FAILED | REFUNDED` (`QR_ISSUED`/`EXPIRED` для списаний недостижимы; отдельного внешнего `INITIATED` нет — это внутреннее подсостояние).

### 6.2 Создание согласия

`POST /v1/subscriptions` (заголовок `Idempotency-Key` обязателен)

```json
{
  "tspId": "tsp_9f3c2a1b",
  "amountType": "VARIABLE",          // FIXED | VARIABLE (VARIABLE — ЖКХ/связь, сумма меняется от периода к периоду)
  "maxAmountPerCharge": 50000,       // копейки, потолок одного списания
  "periodLimit": 200000,             // копейки, потолок за период (месячный лимит плательщика — приоритетнее)
  "period": "MONTH",                 // DAY | WEEK | MONTH
  "startDate": "2026-10-01",
  "endDate": "2027-10-01",           // опц.; лимит срока — по НСПК [ТРЕБУЕТ ПРОВЕРКИ]
  "paymentPurpose": "Подписка «Кинозал»",
  "payerRef": "client-8891",         // опц.; идентификатор плательщика на стороне ТСП (не ПДн)
  "returnUrl": "https://merchant.example.com/subscription/return",
  "merchantSubscriptionId": "sub-2026-8891" // опц., сквозной для ТСП
}
```

Ответ `201`:

```json
{
  "subscriptionId": "sub_4c7d2e91",
  "subscriptionStatus": "PENDING_PAYER",
  "consentUrl": "https://…",         // ссылка/deeplink на подтверждение в приложении банка плательщика
  "maxAmountPerCharge": 50000,
  "periodLimit": 200000,
  "period": "MONTH",
  "createdAt": "2026-09-29T10:00:00.000Z"
}
```

Согласие становится `ACTIVE` только после подтверждения плательщиком; до этого списания запрещены. Отсутствие подтверждения в срок → `DECLINED`.

### 6.3 Согласие

`GET /v1/subscriptions/{subscriptionId}` → `200`

```json
{
  "subscriptionId": "sub_4c7d2e91",
  "subscriptionStatus": "ACTIVE",
  "amountType": "VARIABLE",
  "maxAmountPerCharge": 50000,
  "periodLimit": 200000,
  "period": "MONTH",
  "startDate": "2026-10-01",
  "endDate": "2027-10-01",
  "merchantSubscriptionId": "sub-2026-8891",
  "charges": [
    { "chargeId": "chg_1a2b3c", "subscriptionId": "sub_4c7d2e91", "billingPeriod": "2026-10", "amount": 49900, "status": "COMPLETED" }
  ]
}
```

### 6.4 Рекуррентное списание

`POST /v1/subscriptions/{subscriptionId}/charges` (заголовок `Idempotency-Key` обязателен)

```json
{
  "chargeId": "chg_1a2b3c",
  "billingPeriod": "2026-11",        // ключ периода; уникален в паре с subscriptionId
  "amount": 49900,                   // копейки; <= maxAmountPerCharge
  "description": "Ноябрь 2026"
}
```

Ответ `201` (новое списание) / `200` (идемпотентный повтор, то же `chargeId`):

```json
{
  "chargeId": "chg_1a2b3c",
  "paymentId": "pay_8d1e4f5a",
  "subscriptionId": "sub_4c7d2e91",
  "billingPeriod": "2026-11",
  "amount": 49900,
  "status": "CREATED"
}
```

Правила: списание возможно только при `ACTIVE` согласии и в пределах лимитов (иначе `422`, без вызова ОПКЦ); значение заголовка `Idempotency-Key` совпадает с `chargeId`; на один `billingPeriod` — не более одной незавершённой и не более одной успешной попытки (иначе `200` с существующим ресурсом или `409 CHARGE_ALREADY_EXISTS`); статус списания читается существующим `GET /v1/payments/{paymentId}` и совпадает с `Charge.status` (канонические значения `Payment.status`; подсостояние «отправлено в ОПКЦ» — внутреннее).

### 6.5 Управление согласием со стороны ТСП

- `POST /v1/subscriptions/{subscriptionId}/suspend` → `200` (статус `SUSPENDED`)
- `POST /v1/subscriptions/{subscriptionId}/resume` → `200` (статус `ACTIVE`)
- `POST /v1/subscriptions/{subscriptionId}/close` → `200` (статус `REVOKED`; отзыв **необратим**)

Отзыв **плательщиком** выполняется в приложении его банка и приходит шлюзу событием/сверкой; ТСП извещается вебхуком (6.7). Отзыв не отменяет уже зачисленные платежи — возврат оформляется через существующий `POST /v1/payments/{paymentId}/refunds`.
Все методы подписок проверяют принадлежность согласия аутентифицированному ТСП: чужое/несуществующее согласие → `404` (AD-016). Возобновление/закрытие терминального согласия (`REVOKED`/`EXPIRED`/`DECLINED`) → `409 SUBSCRIPTION_ALREADY_TERMINAL`.

### 6.6 Расширение существующих ответов (аддитивно)

Платёж (ответы `POST /v1/payments`, `GET /v1/payments/{paymentId}`) получает **опциональные** поля:

```json
{
  "operationType": "QR",             // QR (по умолчанию) | CONSENT
  "subscriptionId": "sub_4c7d2e91"   // присутствует только для operationType=CONSENT
}
```

Существующие поля, пути и значения `status` не изменяются; потребители v0.1 продолжают работать без изменений.

### 6.7 Вебхуки подписок (новые типы, §5 без изменений)

Дополнительные типы событий (та же доставка: at-least-once, `X-SBP-Event-Id`, `X-SBP-Signature`):

- `subscription.pending` — согласие ожидает подтверждения плательщика
- `subscription.activated` — согласие активно (в т.ч. возобновлено)
- `subscription.suspended`
- `subscription.revoked` — отозвано плательщиком или закрыто ТСП
- `subscription.expired`
- `subscription.declined`
- `charge.completed` / `charge.failed`

Тело содержит `eventId`, `type`, `subscriptionId`, `chargeId?`, `status`, `timestamp`.

### 6.8 Новые коды ошибок (дополнение к §4)

- `SUBSCRIPTION_NOT_ACTIVE` (422) — списание при неактивном согласии
- `SUBSCRIPTION_LIMIT_EXCEEDED` (422) — нарушение лимита на списание/период
- `SUBSCRIPTION_EXPIRED` (422) — срок согласия истёк
- `CHARGE_ALREADY_EXISTS` (409) — успешное или незавершённое списание за период уже есть
- `CHARGE_CONFLICT` (409) — конфликт `chargeId`/`billingPeriod` с другим телом запроса
- `SUBSCRIPTION_ALREADY_TERMINAL` (409) — возобновление/закрытие терминального согласия

## 7. Версионирование и совместимость

- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.
- Добавление опциональных полей — обратно совместимо, не требует новой версии (именно так выполнено v0.2: §6).
- Значения существующего перечисления `status` платежа **не расширяются**: новые статусы живут на новых сущностях (согласие, списание).
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 8. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Подписки: обязательные поля и ограничения согласия в протоколе НСПК (период, срок, лимиты), требования к уведомлению плательщика о списании — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
6. Подписки: нужен ли метод досрочного «запроса списания вне периода» и политика повторных попыток при `charge.failed` — бизнес + НСПК [ТРЕБУЕТ ПРОВЕРКИ].
