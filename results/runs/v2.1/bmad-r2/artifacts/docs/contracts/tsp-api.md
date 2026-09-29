# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1; v0.2 — предложение изменения CHG-001)
- Версия контракта: 0.2 (нестабильная; до A1 фиксируется v1.0-draft). Изменение 0.1 → 0.2: **только обратно совместимые дополнения** (подписки: мандаты/дебеты; см. §7).
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки), AD-003, AD-009, AD-010 (spine)

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
- Для рекуррентного списания (`POST /v1/mandates/{mandateId}/debits`, §7.2) дополнительный ключ — пара `(mandateId, billingRef)`: повтор не создаёт второе списание; тот же `billingRef` с другой суммой → `409 DEBIT_CONFLICT` (AD-003, AD-010).
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

Дополнительные коды для подписок (§7): `MANDATE_NOT_FOUND` (404), `MANDATE_NOT_ACTIVE` (409), `MANDATE_LIMIT_EXCEEDED` (422), `DEBIT_CONFLICT` (409). Отдельный `MANDATE_EXPIRED` не вводится: все не-`ACTIVE` состояния (включая `EXPIRED`) дают `MANDATE_NOT_ACTIVE`.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `mandate.activated`, `mandate.suspended`, `mandate.revoked`, `mandate.expired`, `mandate.rejected` — события жизненного цикла мандата (§7); тело содержит `mandateId`, `status`, `timestamp`. Результат рекуррентного списания доставляется существующими `payment.*` с полями `mandateId`/`billingRef`.

Потребитель обязан **игнорировать неизвестные типы событий** (залог обратной совместимости при добавлении новых).

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

## 7. Подписки (рекуррентные C2B-списания) — v0.2

Назначение: рекуррентные списания по согласию плательщика (мандату). Изменение **обратно совместимо** с v0.1: добавлены новые пути и необязательные поля; значения `Payment.status` не расширяются. См. ADR-008 (CHG-001), `docs/spec/mandate-state-machine.md`, spine AD-009/AD-010.

### 7.1 Мандат (согласие)

`POST /v1/mandates` (обязателен `Idempotency-Key`)

```json
{
  "tspId": "tsp_9f3c2a1b",
  "payerRef": "opkc_payer_…",              // идентификатор плательщика из потока согласия ОПКЦ; без сырых ПДн [ТРЕБУЕТ ПРОВЕРКИ — формат по документации НСПК]
  "maxAmount": 500000,                     // лимит одного списания, копейки
  "maxAmountPerPeriod": 1500000,           // лимит за период, копейки
  "period": "MONTH",                       // DAY | MONTH
  "maxDebitsPerPeriod": 3,                 // максимум списаний за период
  "validUntil": "2027-09-29T00:00:00.000Z",
  "paymentPurpose": "Подписка «Кинозал»"
}
```

Ответ `201`: `Mandate` со `status: CONSENT_PENDING` (или `CREATED`, если адаптер ОПКЦ отвечает асинхронно), `consentQrUrl`/`consentQrImage` (плательщик подтверждает согласие в своём банке `[ТРЕБУЕТ ПРОВЕРКИ — по документации НСПК]`), `consentVersion`.

Статусы мандата: `CREATED | CONSENT_PENDING | ACTIVE | SUSPENDED | REVOKED | EXPIRED | REJECTED`. Списания разрешены **только** при `ACTIVE`. Первичное `ACTIVE` устанавливается по подтверждению ОПКЦ, а не по инициативе ядра (возобновление после `SUSPENDED` — восстановление ранее подтверждённого согласия). `REVOKED`/`EXPIRED`/`REJECTED` — терминальные; `REVOKED` необратим. Не более одного `ACTIVE`-мандата на пару `(tspId, payerRef)`. Изменение лимитов = новый мандат.

`GET /v1/mandates/{mandateId}` → `200` `Mandate`.

`POST /v1/mandates/{mandateId}/revoke` → `200` `Mandate` (`REVOKED`) — прекращение подписки со стороны ТСП; необратимо. Отзыв плательщиком приходит событием ОПКЦ и также переводит мандат в `REVOKED`.

### 7.2 Рекуррентное списание (дебет)

`POST /v1/mandates/{mandateId}/debits` (обязателен `Idempotency-Key`)

```json
{
  "amount": 49900,                         // в пределах лимитов мандата
  "billingRef": "2026-10-kinzal-001",      // счёт/период ТСП; ключ идемпотентности с mandateId
  "paymentPurpose": "Абонентская плата за октябрь",
  "merchantOrderId": "sub-12345-202610"
}
```

Ответ `201`: `Payment` (`paymentId`, `mandateId`, `billingRef`, `status: CREATED`, …). Дальнейший статус — через `GET /v1/payments/{paymentId}`.

Дебет проходит `CREATED → PAID → CREDITED → COMPLETED` (отклонение — `FAILED`); состояние `QR_ISSUED` для дебета недостижимо (разовое действие плательщика не требуется). Зачисление — только из `PAID` (AD-005); возврат — та же сага (§3.4).

Правила: мандат должен быть `ACTIVE`; сумма и периодичность — в пределах лимитов (иначе `422 MANDATE_LIMIT_EXCEEDED`); повтор `(mandateId, billingRef)` или `Idempotency-Key` возвращает тот же `paymentId` без второго списания (AD-003, AD-010). Ключ `(mandateId, billingRef)` уникален на всё время жизни мандата (не ограничен 24-часовым окном `Idempotency-Key`). Дебет без ответа ОПКЦ дольше TTL по политике `[ТРЕБУЕТ ПРОВЕРКИ]` → `EXPIRED` (лимит освобождается). Если ОПКЦ подтверждает оплату уже после отзыва мандата, дебет зачисляется и возвращается по саге (`docs/spec/mandate-state-machine.md` §6).

### 7.3 Совместимость

- Добавлены только новые пути и необязательные поля; `PaymentRequest.required` и `Payment.status` не изменялись.
- `MandateStatus` — отдельное перечисление (не значения `Payment.status`), чтобы потребители не ломались.
- Новые значения перечислений, если появятся, добавляются аддитивно; потребитель игнорирует неизвестные значения/события.
- Ломающие изменения — только в `/v2` (§6).

## 8. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Механика подписок НСПК (поля согласия, подтверждение, уведомление перед списанием, правила отзыва) — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ]; см. CHG-001 §7 (H2/H3).
6. Дефолтные лимиты мандата и их конфигурируемость по ТСП — решение продукта/риска (CHG-001 §7, H4).
7. Допустимость частичных/разовых сумм в рамках мандата и модель изменения лимитов — CHG-001 §7, H5.
