# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (нестабильная; до A1 фиксируется v1.0-draft). v0.2 добавляет подписки СБП (согласия и списания) — изменение `changes/sbp-subscriptions`, ADR-008 (Proposed).
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки), AD-003, AD-009 (spine)

Назначение: контракт между **ТСП/мерчантом** и **СБП-шлюзом банка** (ядро, собственная разработка). Контракт **не зависит** от протокола ОПКЦ СБП (AD-008): адаптер НСПК скрыт за внутренним интерфейсом шлюза.

**Обратная совместимость:** v0.2 — аддитивное расширение v0.1. Существующие пути, поля и значения enum не удаляются и не сужаются; добавлено опциональное поле `consentId` в платеже и новые пути `/v1/consents*`. Потребители v0.1 работают без изменений.

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

### 3.6 Регистрация согласия (СБП-подписка) — v0.2

`POST /v1/consents`

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "payerId": "+79001234567",        // идентификатор плательщика по каналу НСПК [ТРЕБУЕТ ПРОВЕРКИ]
  "amount": 49900,                  // копейки: сумма периодического списания (или лимит)
  "currency": "RUB",
  "frequency": "MONTHLY",           // MONTHLY | WEEKLY | DAILY | ON_DEMAND
  "startDate": "2026-10-01",
  "endDate": "2027-10-01",          // опц.; лимит срока — по НСПК [ТРЕБУЕТ ПРОВЕРКИ]
  "maxAmount": 99900,               // опц.: потолок списания, если amount — переменная
  "paymentPurpose": "Подписка «Кино+»",
  "redirectUrl": "https://merchant.example.com/subscription/return",
  "merchantOrderId": "sub-12345"    // опц., сквозной для ТСП
}
```

Ответ `201`:
```json
{
  "consentId": "cns_7a2b9c1d",
  "status": "PENDING_PAYER",
  "amount": 49900,
  "frequency": "MONTHLY",
  "authUrl": "https://qr.nspk.ru/…",   // [ТРЕБУЕТ ПРОВЕРКИ] ссылка/канал авторизации плательщика
  "validUntil": "2026-09-28T12:30:00.000Z"
}
```

Правила: `Idempotency-Key` обязателен; повтор с тем же ключом и телом → тот же `consentId`; другое тело → `409 IDEMPOTENCY_CONFLICT`. Согласие активируется **только** подтверждением плательщика по каналу НСПК (событие `consent.activated`). До `ACTIVE` списания невозможны.

### 3.7 Статус согласия — v0.2

`GET /v1/consents/{consentId}`

Ответ `200`:
```json
{
  "consentId": "cns_7a2b9c1d",
  "status": "ACTIVE",              // PENDING_PAYER | ACTIVE | SUSPENDED | REVOKED | EXPIRED | REJECTED
  "amount": 49900,
  "frequency": "MONTHLY",
  "maxAmount": 99900,
  "nextDebitDate": "2026-11-01",
  "debits": [
    { "paymentId": "pay_8d1e4f5a", "billingPeriod": "2026-10", "amount": 49900, "status": "COMPLETED" }
  ],
  "activatedAt": "2026-10-01T09:00:00.000Z",
  "revokedAt": null,
  "merchantOrderId": "sub-12345"
}
```

### 3.8 Отзыв согласия — v0.2

`POST /v1/consents/{consentId}/revoke` → `202 { "consentId": "cns_7a2b9c1d", "status": "REVOKED" }`

Правила: отзыв идемпотентен; необратим; прекращает новые списания (ядро ≤ 60 с). Уже подтверждённые списания доводятся; корректировка — возвратом (§3.4). Отзыв может также прийти со стороны плательщика/НСПК — ТСП уведомляется событием `consent.revoked`.

### 3.9 Ручной триггер списания (опциональный режим) — v0.2

`POST /v1/consents/{consentId}/debits`

Запрос:
```json
{
  "billingPeriod": "2026-11",       // период, к которому относится списание
  "amount": 49900,                  // опц.; по умолчанию — сумма согласия; не выше maxAmount
  "reason": "Ежемесячная подписка"
}
```

Ответ `201`:
```json
{ "paymentId": "pay_8d1e4f5a", "consentId": "cns_7a2b9c1d", "status": "CREATED", "billingPeriod": "2026-11", "amount": 49900 }
```

Правила: доступно, если у ТСП включён режим списания по запросу (иначе `403 CONSENT_DEBIT_MODE_DISABLED`). Идемпотентность по `Idempotency-Key` и по `consentId + billingPeriod` — повтор/тик планировщика не создаёт второе списание. Списание видно как обычный платёж: `GET /v1/payments/{paymentId}` (поле `consentId`).

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `CONSENT_DEBIT_MODE_DISABLED` (403, v0.2), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `CONSENT_NOT_ACTIVE` (422, v0.2), `CONSENT_LIMIT_EXCEEDED` (422, v0.2), `CONSENT_EXPIRED` (422, v0.2), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `consent.activated` — согласие подтверждено плательщиком (`status: ACTIVE`, v0.2)
- `consent.rejected` — регистрация согласия отклонена (v0.2)
- `consent.revoked` — согласие отозвано (необратимо, v0.2)
- `consent.expired` — истёк срок согласия (v0.2)
- `consent.suspended` — согласие приостановлено (v0.2)

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
- **v0.2 (подписки СБП, ADR-008, Proposed):** аддитивное расширение — новые пути `/v1/consents*`, новые схемы и события, опциональное `consentId` в платеже; ломающих изменений нет (проверка `arch contract-diff`, CD-001..CD-007). Статус версии — Proposed до A3.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
