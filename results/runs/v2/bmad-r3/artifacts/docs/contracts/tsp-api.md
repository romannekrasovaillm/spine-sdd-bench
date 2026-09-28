# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (нестабильная; до A1 фиксируется v1.0-draft). **Эволюция v0.1 → v0.2 строго аддитивная** (подписки СБП); существующие потребители v0.1 не ломаются.
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки/мандат), ADR-009 (жизненный цикл мандата), ADR-010 (инициатор), AD-003 (spine)
- Изменение: «Подписки СБП» — `docs/changes/2026-09-sbp-subscriptions/`

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
- Регулярные списания создаёт инициатор ядра, а не ТСП; их натуральный ключ идемпотентности — **`(mandateId, periodKey)`** (AD-011): повторная инициация за тот же период не создаёт второй платёж.

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

### 3.6 Мандаты и подписки (v0.2)

Подписка СБП = **мандат** (согласие плательщика, ADR-009) + **расписание** (владеет ядро шлюза, ADR-008). Каждое регулярное списание — обычный платёж с `paymentType=recurring` и `mandateId`; его зачисление идёт по общим правилам (только из `PAID`, AD-005).

#### Регистрация мандата

`POST /v1/mandates` (`Idempotency-Key` обязателен)

```json
{
  "tspId": "tsp_9f3c2a1b",
  "mandateType": "fixed",            // fixed | variable
  "amount": 99000,                   // опц.; обязательна и фиксирована при fixed
  "maxAmount": 500000,               // опц.; обязателен при variable (лимит одного списания)
  "period": "P1M",                   // ISO 8601 период
  "currency": "RUB",
  "paymentPurpose": "Подписка «Кино+», ежемесячно",
  "merchantOrderId": "sub-777"
}
```

Ответ `201`:
```json
{
  "mandateId": "mnd_2c7b1e90",
  "status": "PENDING_CONSENT",
  "mandateType": "fixed",
  "amount": 99000,
  "period": "P1M",
  "consentUrl": "https://…",         // ссылка/данные для подтверждения плательщиком (детали — по НСПК)
  "merchantOrderId": "sub-777"
}
```

Правила: мандат активируется (`ACTIVE`) только после подтверждения согласия плательщиком через ОПКЦ/банк плательщика; до этого списания невозможны. После `ACTIVE` реквизиты и лимит мандата не расширяются — изменение = новый мандат.

#### Статус мандата

`GET /v1/mandates/{mandateId}` → `200 { mandateId, status, mandateType, amount?, maxAmount?, period, activatedAt?, revokedAt?, merchantOrderId }`

Статусы: `PENDING_CONSENT | ACTIVE | SUSPENDED | REVOKED | EXPIRED` (наружу выставляются; технические подсостояния скрыты).

#### Отзыв мандата (инициатива ТСП)

`POST /v1/mandates/{mandateId}/revoke` (`Idempotency-Key` обязателен) → `200 { mandateId, status: "REVOKED", … }`

Правила: отзыв блокирует **новые** списания (приоритетно); уже подтверждённые НСПК списания доводятся по общим правилам. Отзыв плательщика приходит от ОПКЦ событием `mandate.revoked` — ТСП получает вебхук (см. §5) и не управляет им.

#### Список списаний по мандату

`GET /v1/mandates/{mandateId}/charges?periodKey={periodKey}` → `200 [ { paymentId, periodKey, status, amount, scheduledAt?, paidAt? } ]`

#### Задание суммы для `variable`-мандата

`POST /v1/mandates/{mandateId}/charges` (`Idempotency-Key` обязателен)

```json
{ "amount": 480050, "periodKey": "2026-10", "paymentPurpose": "ЖКУ, октябрь" }
```

Ответ `201`: `{ mandateId, periodKey, amount, status: "SCHEDULED", scheduledAt }`

Правила: сумма задаётся ТСП **заранее** для периода и не превышает `maxAmount` (иначе `422 MANDATE_LIMIT_EXCEEDED`); банк инициирует списание в срок периода. Для `fixed`-мандата метод не требуется — сумма берётся из мандата. Если к началу периода сумма по `variable`-мандату не задана, списание за период **не инициируется** (fail-closed; событие/алерт по политике).

Регулярные списания также видны через `GET /v1/payments/{paymentId}` как обычные платежи с полями `paymentType=recurring`, `mandateId`, `periodKey`. Инициатор списаний — ядро шлюза; ТСП не создаёт регулярный платёж вручную (charge-on-demand — вне scope, см. ADR-008 Deferred).

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

Коды контура подписок (v0.2): `MANDATE_NOT_FOUND` (404), `MANDATE_NOT_ACTIVE` (422), `MANDATE_REVOKED` (422), `MANDATE_LIMIT_EXCEEDED` (422). Попытка списания/изменения по недействующему мандату не создаёт финансового движения.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `mandate.activated` — согласие плательщика подтверждено, мандат `ACTIVE` (v0.2)
- `mandate.revoked` — мандат отозван плательщиком/НСПК (v0.2)
- `mandate.suspended` / `mandate.expired` — мандат приостановлен/истёк (v0.2)

Регулярные списания используют те же события `payment.*` (поле `paymentType=recurring`, `mandateId`, `periodKey`), что и разовые платежи; отдельного типа события на списание не вводится.

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
- **v0.1 → v0.2 (подписки) — аддитивная эволюция в `/v1`:** добавлены только новые пути (`/v1/mandates…`), новые схемы (`Mandate`, `MandateRequest`, `ChargeRef`) и опциональные поля (`Payment.paymentType`, `Payment.mandateId`, `Payment.periodKey`). Существующие пути, обязательные поля и значения enum (`Payment.status`) не изменены — потребитель v0.1 продолжает работать без изменений.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Подписочный контур (v0.2): порядок и содержимое подтверждения согласия плательщика, формат `consentUrl`, сроки и способ уведомления о списании, порядок отзыва — по протоколу НСПК [ТРЕБУЕТ ПРОВЕРКИ].
6. Поля периода `period`/`periodKey`: календарь и таймзона (календарный месяц/день месяца/UTC) — финализировать с НСПК и бизнесом; влияет на `(mandateId, periodKey)`.
7. Нужен ли отдельный `GET /v1/mandates` (список мандатов ТСП) — объём продукта, ждёт бизнес.
8. Политика дуннинга и её отражение в API (видимость неуспешных попыток списания ТСП) — см. `docs/changes/2026-09-sbp-subscriptions/07-human-decisions.md`.
