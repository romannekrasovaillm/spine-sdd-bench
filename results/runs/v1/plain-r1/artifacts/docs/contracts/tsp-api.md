# Контракт API ТСП (мерчант-API) — v0.1 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), AD-003 (spine)

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

### 3.6 Согласие плательщика (подписка, рекуррентная авторизация)

Согласие — сущность первого класса (ADR-008, AD-009). Подтверждение согласия плательщиком выполняется в приложении банка плательщика через контур СБП; шлюз регистрирует согласие в ОПКЦ, получает события его жизненного цикла и инициирует дебиты. Согласие само по себе не даёт права на списание: финансовое списание допустимо только при `status == ACTIVE` **и** подтверждении дебита НСПК (`PAID`).

`POST /v1/consents` (заголовок `Idempotency-Key` обязателен)

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "currency": "RUB",
  "maxAmount": 100000,              // копейки, int; лимит одного списания
  "maxFrequency": "MONTHLY",        // DAILY | WEEKLY | MONTHLY | UNLIMITED
  "validFrom": "2026-09-28T00:00:00.000Z",
  "validTo": "2027-09-28T00:00:00.000Z",
  "purpose": "Подписка «Кино+»",
  "payerReference": "subscriber-12345", // сквозной идентификатор плательщика у ТСП
  "redirectUrl": "https://merchant.example.com/subscribe/return"
}
```

Ответ `201`:
```json
{
  "consentId": "con_1a2b3c4d",
  "tspId": "tsp_9f3c2a1b",
  "status": "PENDING",              // PENDING | ACTIVE | SUSPENDED | REVOKED | EXPIRED
  "maxAmount": 100000,
  "maxFrequency": "MONTHLY",
  "validTo": "2027-09-28T00:00:00.000Z"
}
```

`GET /v1/consents/{consentId}` → `200 { consentId, tspId, status, maxAmount, maxFrequency, validFrom, validTo, activatedAt?, revokedAt? }`

`POST /v1/consents/{consentId}/cancel` (заголовок `Idempotency-Key` обязателен) → `200 { consentId, status: "REVOKED" }`

Правила: `ACTIVE` наступает только после подтверждения плательщиком (событие `consent.activated`). Ревок возможен плательщиком (через его банк), ТСП (`cancel`) и по истечении `validTo`. Ревок необратим (AD-009).

### 3.7 Рекуррентное списание (дебит)

`POST /v1/consents/{consentId}/debits` (заголовок `Idempotency-Key` обязателен)

Запрос:
```json
{
  "amount": 79000,                  // копейки, int; ≤ consent.maxAmount
  "currency": "RUB",
  "purpose": "Списание за сентябрь",
  "merchantOrderId": "order-12345"
}
```

Ответ `201`:
```json
{
  "debitId": "dbt_7e8f9a0b",
  "paymentId": "pay_8d1e4f5a",     // дебит — платёж той же статусной машины (ADR-008)
  "consentId": "con_1a2b3c4d",
  "amount": 79000,
  "status": "CREATED"               // CREATED | PAID | CREDITED | COMPLETED | FAILED
}
```

Правила: дебит создаётся только при согласии `ACTIVE` и `amount ≤ maxAmount` (иначе `422 CONSENT_NOT_ACTIVE` / `422 CONSENT_LIMIT_EXCEEDED`, без вызова НСПК и без зачисления). Дебит проходит `CREATED → PAID → CREDITED → COMPLETED`, **минуя `QR_ISSUED`** (авторизация — согласие). Зачисление в АБС — только из `PAID` (AD-005, AD-010). Статус отслеживается через `GET /v1/payments/{paymentId}`; возврат дебита — обычная сага `POST /v1/payments/{paymentId}/refunds`.

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `CONSENT_NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `CONSENT_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `CONSENT_NOT_ACTIVE` (422), `CONSENT_LIMIT_EXCEEDED` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `consent.activated` — согласие подтверждено плательщиком (`status: ACTIVE`)
- `consent.suspended` — согласие приостановлено (`status: SUSPENDED`)
- `consent.revoked` — согласие отозвано (`status: REVOKED`)
- `consent.expired` — истёк срок действия (`status: EXPIRED`)
- `consent.failed` — согласие отклонено/не создано

Результат рекуррентного дебита доставляется событиями `payment.completed` / `payment.failed`; тело дополнительно содержит `consentId` и `paymentType: "RECURRING"` (для разовых — `paymentType: "ONE_SHOT"` или поле отсутствует).

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
- Согласия и дебиты (ADR-008) — **аддитивное** расширение: новые пути `/v1/consents*` и опциональные поля `consentId`/`paymentType` в `Payment`; существующие потребители `/v1/payments*` не затронуты.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Поля/события согласий и дебитов в протоколе НСПК (форматы, тайминги, отказные коды, retry при нехватке средств) — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
6. Частотные лимиты `maxFrequency` и ревок по инициативе ТСП — бизнес-правила, на решение продуктового владельца.
7. Дополнительное информирование плательщика перед списанием (push-уведомление/окно подтверждения) — решает комплаенс/продукт по 161-ФЗ/152-ФЗ [ТРЕБУЕТ ПРОВЕРКИ].
