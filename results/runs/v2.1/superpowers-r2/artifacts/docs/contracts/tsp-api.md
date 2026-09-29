# Контракт API ТСП (мерчант-API) — v0.2 draft (аддитивно к v0.1)

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft); приращение 0.2-draft от 2026-09-29 — аддитивное расширение «СБП-подписки» (§8), обратно совместимо с 0.1
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008/ADR-009 (подписки), AD-003 (spine)

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
- Приращение 0.2 (СБП-подписки, §8): добавлены новые пути и схемы; enum `Payment.status` **не изменён** (списание — отдельный ресурс `Charge`) → обратно совместимо, новая версия пути не требуется.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.

## 8. СБП-подписки: мандаты и рекуррентные списания (v0.2-draft, аддитивно)

- Status: Draft (изменение 2026-09-29; ADR-008, ADR-009; для ревью на гейте A3/A1)
- Совместимость: **аддитивное** расширение к v0.1 — существующие методы, поля и значения `status` платежа не меняются; списание вынесено в отдельный ресурс `Charge`, чтобы не менять enum `Payment.status`.

### 8.1 Общие положения

- Те же транспорт, авторизация (mTLS + `X-API-Key`), кодировка и правила идемпотентности, что и в §1–§2; `Idempotency-Key` **обязателен** для всех `POST` §8.
- Мандат — согласие плательщика на рекуррентные списания (ADR-008). Списание возможно только при мандате `ACTIVE` и в пределах лимитов/срока.
- Суммы — целые, в копейках; валюта — `RUB` (643); временные метки — ISO 8601 (UTC).

### 8.2 Создание мандата

`POST /v1/mandates`

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "maxAmountPerCharge": 49900,        // копейки, лимит на одно списание
  "maxAmountPerPeriod": 49900,        // опц., лимит за период [ТРЕБУЕТ ПРОВЕРКИ: поля/периоды НСПК]
  "periodType": "MONTH",              // опц.; справочник — по протоколу НСПК [ТРЕБУЕТ ПРОВЕРКИ]
  "validUntil": "2027-09-29T00:00:00.000Z", // опц., срок согласия
  "purpose": "Подписка «Кино+»",
  "redirectUrl": "https://merchant.example.com/subscription/return",
  "merchantOrderId": "sub-order-42"   // опц.
}
```

Ответ `201`:
```json
{
  "mandateId": "mnd_1a2b3c",
  "status": "PENDING_CONSENT",
  "consentUrl": "https://…",           // ссылка/данные для согласия плательщика (по протоколу НСПК)
  "expiresAt": "2026-09-29T18:00:00.000Z",
  "merchantOrderId": "sub-order-42"
}
```

### 8.3 Статус мандата

`GET /v1/mandates/{mandateId}` → `200`

```json
{
  "mandateId": "mnd_1a2b3c",
  "status": "ACTIVE",                  // PENDING_CONSENT | ACTIVE | REVOKED | EXPIRED | REJECTED | SUSPENDED
  "tspId": "tsp_9f3c2a1b",
  "maxAmountPerCharge": 49900,
  "maxAmountPerPeriod": 49900,
  "periodType": "MONTH",
  "validUntil": "2027-09-29T00:00:00.000Z",
  "activatedAt": "2026-09-29T12:05:00.000Z",
  "revokedAt": null,
  "merchantOrderId": "sub-order-42"
}
```

### 8.4 Отзыв мандата

`POST /v1/mandates/{mandateId}/revoke` → `200 { "mandateId": "mnd_1a2b3c", "status": "REVOKED" }`

Правила: отзыв идемпотентен; после отзыва новые списания запрещены (AD-011); отзыв самого плательщика приходит нотификацией `mandate.revoked`.

### 8.5 Инициация списания

`POST /v1/mandates/{mandateId}/charges`

Запрос:
```json
{
  "amount": 49900,                     // копейки; <= maxAmountPerCharge
  "currency": "RUB",
  "periodKey": "2026-10",              // опц.; ключ периода для защиты от дублей (ADR-009)
  "purpose": "Подписка «Кино+», октябрь",
  "merchantOrderId": "charge-order-42"
}
```

Ответ `201`:
```json
{ "chargeId": "chg_7f8e9d", "mandateId": "mnd_1a2b3c", "amount": 49900, "status": "SENT" }
```

Правила: мандат `ACTIVE`; `amount ≤ maxAmountPerCharge`; сумма списаний за период ≤ `maxAmountPerPeriod`; иначе — ошибка (см. §8.8). Статус `SENT` — списание инициировано в ОПКЦ; зачисление возможно только после `PAID` (AD-005/AD-010).

### 8.6 Статус списания

`GET /v1/charges/{chargeId}` → `200`

```json
{
  "chargeId": "chg_7f8e9d",
  "mandateId": "mnd_1a2b3c",
  "amount": 49900,
  "status": "COMPLETED",               // CREATED | SENT | PAID | CREDITED | COMPLETED | FAILED | EXPIRED
  "paidAt": "2026-10-01T09:00:02.000Z",
  "creditingStatus": "CREDITED",
  "errorCode": null,
  "merchantOrderId": "charge-order-42"
}
```

### 8.7 Вебхуки (расширение §5)

Дополнительные события (те же заголовки `X-SBP-Event-Id`, `X-SBP-Signature`; at-least-once, дедуп по `eventId`):

- `mandate.activated` — согласие получено, мандат `ACTIVE`;
- `mandate.rejected` — плательщик/ОПКЦ отклонил оформление;
- `mandate.revoked` — согласие отозвано;
- `mandate.expired` — истёк срок действия;
- `charge.completed` — списание зачислено ТСП (`status: COMPLETED`);
- `charge.failed` — списание отклонено/не состоялось (`errorCode`, `reason`).

Тело (`charge.completed`):
```json
{
  "eventId": "evt_…",
  "type": "charge.completed",
  "mandateId": "mnd_1a2b3c",
  "chargeId": "chg_7f8e9d",
  "status": "COMPLETED",
  "amount": 49900,
  "timestamp": "2026-10-01T09:00:03.000Z"
}
```

### 8.8 Ошибки (расширение §4)

Дополнительные канонические коды: `MANDATE_NOT_ACTIVE` (422), `MANDATE_EXPIRED` (422), `LIMIT_EXCEEDED` (422), `CHARGE_ALREADY_EXISTS` (409, при конфликте `periodKey`), `CONSENT_PENDING` (409). Формат Problem Details — как в §4.

### 8.9 Открытые вопросы (для A1)

1. Точные поля мандата, периоды и лимиты — по протоколу НСПК [ТРЕБУЕТ ПРОВЕРКИ].
2. Формат `consentUrl`/сценарий согласия (redirect, QR, приложение банка плательщика) — по протоколу НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Нужен ли метод отмены/приостановки мандата со стороны ТСП (аналог `revoke` для `SUSPENDED`).
4. Политика повторных попыток (dunning) — бизнес-решение, выносится на A3 (см. ADR-009).
