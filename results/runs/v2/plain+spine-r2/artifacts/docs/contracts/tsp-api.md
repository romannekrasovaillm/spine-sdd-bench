# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1; v0.2 — дельта подписок, для A2/A3)
- Версия контракта: 0.2 (аддитивное расширение v0.1; ломающих изменений нет — `contract_diff` v0.1→v0.2: 0 breaking)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (мандат/списание), ADR-010 (аддитивная эволюция), AD-003, AD-010 (spine)

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

### 3.6 Подписки: согласие плательщика (мандат) и рекуррентные списания — новое в v0.2

Назначение: ТСП создаёт согласие плательщика (мандат) один раз; далее инициирует списания по нему без нового действия клиента (ADR-008). Списание — **вид платежа**: читается существующим `GET /v1/payments/{paymentId}` и возвращается существующей сагой возвратов (ADR-005).

#### 3.6.1 Создание мандата

`POST /v1/mandates` (заголовок `Idempotency-Key` обязателен)

```json
{
  "tspId": "tsp_9f3c2a1b",
  "merchantSubscriptionId": "sub-movie-42",
  "payerPhone": "+79001234567",         // опц.; идентификация согласия, маскируется в хранении
  "maxAmountPerDebit": 39900,          // максимум за одно списание, копейки
  "limit": { "amount": 39900, "period": "MONTH" },  // DAY | MONTH | TOTAL
  "frequency": "MONTHLY",              // DAILY | WEEKLY | MONTHLY | ON_DEMAND
  "validUntil": "2027-09-28T00:00:00.000Z",
  "purpose": "Подписка «Кино+», ежемесячно",
  "redirectUrl": "https://merchant.example.com/sub/return"
}
```

Ответ `201`: `{ "mandateId": "man_…", "status": "PENDING_CONSENT", "consentUrl": "https://…", "maxAmountPerDebit": 39900, "limit": {...}, "validUntil": "…" }`

Семантика: вызов **асинхронный по природе**. Если ОПКЦ на момент запроса недоступен/таймаут, мандат создаётся в `CREATED`, `consentUrl` может отсутствовать до ответа ОПКЦ, а клиент получает `201` с `CREATED` и позже вебхук `mandate.pending`/`mandate.rejected` (не `5xx` и не потеря операции). `consentUrl` при доступном ОПКЦ — p95 ≤ 5 с (см. REQ-SUB-1).

Правила: условия мандата **иммутабельны после активации** (изменение — новый мандат); плательщик подтверждает согласие по `consentUrl` в своём банке; `ACTIVE` наступает по событию ОПКЦ, при этом заполняется `payerRef` (маскированная ссылка на плательщика). Лимиты/срок — по правилам НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`.

#### 3.6.2 Состояние мандата

`GET /v1/mandates/{mandateId}` → `200`
```json
{
  "mandateId": "man_…",
  "mandateRef": "OPKC-…",
  "payerRef": "payer_***6789",         // маскированная ссылка; заполняется при активации (AD-007)
  "tspId": "tsp_9f3c2a1b",
  "status": "ACTIVE",                  // CREATED | PENDING_CONSENT | ACTIVE | SUSPENDED | REJECTED | REVOKED | EXPIRED
  "maxAmountPerDebit": 39900,
  "limit": { "amount": 39900, "period": "MONTH" },
  "activatedAt": "2026-09-28T10:00:00.000Z",
  "revokedAt": null,
  "revocationSource": null             // PAYER | MERCHANT | TSP_REQUEST
}
```

#### 3.6.3 Отзыв и приостановка мандата

`POST /v1/mandates/{mandateId}/revoke` (заголовок `Idempotency-Key`) → `200` с мандатом в `REVOKED`.
Отзыв плательщиком приходит событием ОПКЦ; оба пути дают `REVOKED`. Отзыв **необратим**; с момента обработки новые **инициации** списаний запрещены (ADR-009, NFR §7). Повторный отзыв идемпотентен.

`POST /v1/mandates/{mandateId}/suspend` / `POST /v1/mandates/{mandateId}/resume` (заголовок `Idempotency-Key`) — приостановка и возобновление списаний **без отзыва согласия** (`ACTIVE ⇄ SUSPENDED`); приостановка также может быть следствием политики dunning (ADR-009). Возобновление невозможно из `REVOKED`/`EXPIRED` (`422`).

#### 3.6.4 Инициирование рекуррентного списания

`POST /v1/mandates/{mandateId}/debits` (заголовок `Idempotency-Key` обязателен)

```json
{ "amount": 39900, "billingPeriod": "2026-10", "description": "Подписка за октябрь" }
```

`billingPeriod` — канонический период: `MONTHLY` — `YYYY-MM`, `DAILY` — `YYYY-MM-DD` (шаблон `^[0-9]{4}-[0-9]{2}(-[0-9]{2})?$`); формат обязателен, т.к. период — ключ уникальности.

Ответ `201`: объект `Payment` (`paymentType: "recurring"`, `mandateId`, `billingPeriod`, `status`).

Правила: списание допустимо только при мандате `ACTIVE`, в пределах срока, `amount <= maxAmountPerDebit`, лимита периода и `frequency`; **период резервируется при инициации** — повтор с тем же периодом (в т.ч. с другим `Idempotency-Key`) → `409` (`DEBIT_PERIOD_EXISTS`); списание сверх лимита / неактивный мандат → `422`; при перегрузке — `429` (допуск, ADR-011). Guard **перепроверяется при отправке** из очереди (ADR-009/ADR-011). Инициация принимается и ставится в очередь; финальный статус — через `GET /v1/payments/{paymentId}` и вебхук.

`GET /v1/mandates/{mandateId}/debits` → `200 [ Payment, … ]` — история списаний по мандату.

#### 3.6.5 Возвраты по списаниям

Возврат по списанию — существующая сага (ADR-005): `POST /v1/payments/{paymentId}/refunds` работает и для `paymentType=recurring`. Транспортный возврат в ОПКЦ адресуется ссылкой списания (`debitRef`/`reference`), а не `qrId` (см. `docs/contracts/opkc-adapter.md` §3–4 v0.2).

#### 3.6.6 Расширение схемы `Payment` (опциональные поля)

К существующему объекту `Payment` добавлены **опциональные** поля: `paymentType` (`single`|`recurring`; отсутствие = `single`), `mandateId`, `billingPeriod`. Enum `Payment.status` **не изменён** (AD-010). Это требование Tolerant Reader к потребителям: новые опциональные поля должны игнорироваться, а не ломать разбор.

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
Коды подписок (v0.2): `DEBIT_PERIOD_EXISTS` (409 — списание за период уже существует/зарезервировано), `MANDATE_NOT_ACTIVE` (422 — мандат не `ACTIVE`/вне срока), `MANDATE_LIMIT_EXCEEDED` (422 — сверх лимита согласия), `MANDATE_NOT_REVOCABLE` (422 — отзыв из текущего состояния невозможен). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`); для рекуррентного списания — то же событие (`paymentType: recurring`, `mandateId`)
- `payment.failed` — платёж/списание отклонено (для списания — недостаточно средств и т.п.)
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `mandate.pending` — мандат создан, ждёт подтверждения плательщика (v0.2)
- `mandate.activated` — согласие подтверждено, списания разрешены (v0.2)
- `mandate.rejected` — согласие не получено/отклонено (v0.2)
- `mandate.suspended` / `mandate.resumed` — приостановка/возобновление по политике dunning (v0.2)
- `mandate.revoked` — согласие отозвано (плательщиком или ТСП); новые списания запрещены (v0.2)
- `mandate.expired` — истёк срок согласия (v0.2)

Новые типы событий добавлены аддитивно (ADR-010): существующие типы и их семантика не изменены.

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
- **v0.1 → v0.2 (подписки): ломающих изменений нет** — только новые пути, новые схемы и опциональные поля; enum `Payment.status` не изменён (AD-010, ADR-010). Проверка — `contract_diff` (0 breaking).
- Потребители обязаны следовать Tolerant Reader: игнорировать неизвестные опциональные поля и неизвестные типы событий, не падать на них.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. **Модель согласия в протоколе НСПК** (мандат: поля, лимиты, обязанность уведомления плательщика перед списанием, поведение при отзыве в момент списания) — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ]; может уточнить схему `Mandate` и коды ошибок.
6. **Политика dunning** (число попыток, интервалы, порог `SUSPENDED`) — бизнес/комплаенс (A3), влияет на вебхуки `mandate.suspended`.
7. **Поведение при списании, «осевшем» после отзыва** (возврат/зачисление/ручной разбор) — правовая политика (A3), влияет на статусы списания.
8. Нужен ли ТСП отдельный метод паузы подписки (`POST /v1/mandates/{id}/suspend`) — roadmap, ждёт бизнес.
