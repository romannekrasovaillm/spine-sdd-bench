# Контракт API ТСП (мерчант-API) — v0.1 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (рекуррентные списания), AD-003, AD-009 (spine)

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

### 3.6 Создание согласия (подписки)

`POST /v1/consents`

Запрос (идемпотентный, `Idempotency-Key` обязателен):
```json
{
  "tspId": "tsp_9f3c2a1b",
  "purpose": "Подписка «Кино+» ежемесячно",
  "maxAmountPerDebit": 49900,        // копейки; макс. сумма одного списания
  "currency": "RUB",
  "expiresAt": "2027-09-28T00:00:00.000Z", // опц.; срок действия согласия
  "recurrenceRule": "MONTHLY"        // опц.; справочник частот [ТРЕБУЕТ ПРОВЕРКИ по НСПК]
}
```

Ответ `201`:
```json
{
  "consentId": "cns_7e5d4c3b",
  "status": "CONSENT_PENDING",
  "maxAmountPerDebit": 49900,
  "expiresAt": "2027-09-28T00:00:00.000Z"
}
```

Примечания: регистрация согласия в СБП выполняется асинхронно через адаптер ОПКЦ; плательщик подтверждает согласие в приложении своего банка (сценарий выдачи — см. ADR-008 §11). До перехода в `CONSENT_ACTIVE` списания запрещены (AD-009). Точный набор параметров согласия и способ выдачи — по документации НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`.

### 3.7 Статус согласия

`GET /v1/consents/{consentId}`

Ответ `200`:
```json
{
  "consentId": "cns_7e5d4c3b",
  "status": "CONSENT_ACTIVE",        // CONSENT_PENDING | CONSENT_ACTIVE | CONSENT_SUSPENDED | CONSENT_REVOKED | CONSENT_EXPIRED
  "maxAmountPerDebit": 49900,
  "createdAt": "2026-09-28T10:00:00.000Z",
  "activatedAt": "2026-09-28T10:05:12.000Z",
  "revokedAt": null,
  "expiresAt": "2027-09-28T00:00:00.000Z"
}
```

### 3.8 Отзыв согласия

`POST /v1/consents/{consentId}/revoke` (идемпотентный; `Idempotency-Key` обязателен)

Ответ `200`:
```json
{ "consentId": "cns_7e5d4c3b", "status": "CONSENT_REVOKED" }
```

Примечания: отзыв может также инициировать плательщик в приложении своего банка — тогда шлюз получает событие от НСПК и переводит согласие в `CONSENT_REVOKED` (вебхук ТСП `consent.revoked`). После отзыва новые списания отклоняются (AD-009).

### 3.9 Рекуррентное списание

`POST /v1/consents/{consentId}/debits` (идемпотентный; `Idempotency-Key` обязателен)

Запрос:
```json
{
  "amount": 49900,                   // копейки; <= maxAmountPerDebit согласия
  "paymentPurpose": "Подписка «Кино+» за сентябрь",
  "merchantOrderId": "subs-2026-09"  // опц., сквозной для ТСП
}
```

Ответ `201`:
```json
{
  "paymentId": "pay_1f2a3b4c",
  "status": "DEBIT_INITIATED",       // рекуррентное списание инициировано, ожидается подтверждение НСПК
  "amount": 49900,
  "consentId": "cns_7e5d4c3b"
}
```

Правила: списание инициируется только при `CONSENT_ACTIVE` (AD-009); иначе `403 CONSENT_NOT_ACTIVE`. Дальнейший жизненный цикл списания — **та же статусная машина платежа**: `DEBIT_INITIATED → PAID → CREDITED → COMPLETED`, возвраты — через `POST /v1/payments/{paymentId}/refunds`. Зачисление выполняется только из `PAID` (AD-005).

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `CONSENT_NOT_ACTIVE` (403), `NOT_FOUND` (404), `CONSENT_NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `DEBIT_AMOUNT_EXCEEDS_CONSENT` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `consent.activated` — согласие активировано (`CONSENT_ACTIVE`)
- `consent.revoked` — согласие отозвано (`CONSENT_REVOKED`)
- `consent.suspended` / `consent.expired` — приостановлено / истёк срок
- `debit.confirmed` — рекуррентное списание подтверждено (`status: PAID`)
- `debit.failed` — рекуррентное списание отклонено/ошибка

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
- Рекуррентные методы (`/v1/consents`, `/v1/consents/{consentId}/debits`) и новые значения статусов (`DEBIT_INITIATED`, `CONSENT_*`) — **аддитивны**: существующие методы и поля не меняются, существующие потребители не затрагиваются.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Точный набор параметров согласия (`maxAmountPerDebit`, `recurrenceRule`, срок) и способ выдачи согласия плательщику — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ] (см. ADR-008 §11).
6. Политика in-flight списаний при отзыве согласия — решение бизнеса (см. ADR-008 §11).
