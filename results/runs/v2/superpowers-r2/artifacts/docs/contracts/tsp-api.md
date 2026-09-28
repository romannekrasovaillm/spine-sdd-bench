# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (нестабильная; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008/ADR-009/ADR-010 (подписки), AD-003, AD-009, AD-010

**История версий.** v0.2 аддитивно расширяет v0.1 подписками СБП (рекуррентные списания по согласию плательщика): добавлены пути `/v1/subscriptions*`, опциональные поля `subscriptionId`/`periodKey` в платеже и новые события вебхуков. Ломающих изменений относительно v0.1 нет — потребители v0.1 продолжают работать без правок (проверено `arch contract-diff`: breaking = 0). Совместимость — см. §6.

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

Для **рекуррентного списания** ТСП передаёт `subscriptionId` (и, если поддерживается, `periodKey`) — тогда платёж является списанием по мандату (см. §8). Для списания QR не выпускается: путь статусов `CREATED → PAID → CREDITED → COMPLETED` (без `QR_ISSUED`); при неопределённом исходе списание остаётся в `CREATED` (техническое подсостояние `OPKC_UNKNOWN` наружу не выставляется, см. `docs/spec/subscriptions.md`).

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

Коды для списаний по подписке (§8): `SUBSCRIPTION_NOT_ACTIVE` (422 — мандат `PENDING_CONSENT`/`PAUSED`/`REVOKED`/`EXPIRED`), `SUBSCRIPTION_LIMIT_EXCEEDED` (422 — превышен лимит разового списания или периода), `CHARGE_PERIOD_CLOSED` (409 — списание за этот период уже было), `CONSENT_REVOKED` (422 — согласие отозвано; списание в СБП не отправляется). Эти коды — аддитивны и клиентам v0.1 не возвращаются.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`

События подписок (v0.2, §8):
- `subscription.activated` — согласие плательщика подтверждено, мандат действует
- `subscription.paused` / `subscription.resumed` — списания приостановлены/возобновлены
- `subscription.revoked` — согласие отозвано (списания прекращены)
- `subscription.expired` — истёк срок действия мандата
- `charge.completed` — рекуррентное списание зачислено (`paymentId`, `subscriptionId`, `periodKey`)
- `charge.failed` — списание отклонено (мандат/лимит/ОПКЦ)

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
- **v0.2 (подписки) — аддитивное расширение `/v1`**: новые пути, опциональные поля (`subscriptionId`, `periodKey`) и новые события. Существующие потребители v0.1 не обязаны меняться; новые коды ошибок и события возвращаются только при использовании подписок. Ломающих изменений нет (`arch contract-diff` — PASS, breaking = 0).

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.

Открытые вопросы по подпискам (v0.2):

5. Формат `periodKey` и правила повторных списаний за период — по сервису СБП [ТРЕБУЕТ ПРОВЕРКИ].
6. Состав параметров мандата, которые поддерживает сервис СБП (периодичность, лимиты за период) — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
7. Нужен ли метод «предпросмотр согласия» (что подписывает плательщик) — ждёт требований комплаенса.
8. Требуемый состав и канал уведомления плательщика о списании — финализируют ИБ/юристы [ТРЕБУЕТ ПРОВЕРКИ].

## 8. Подписки СБП (рекуррентные списания) — v0.2

Модель авторизации — ADR-008: **мандат** (согласие плательщика) хранится в ядре шлюза как единый источник истины; согласие подтверждает плательщик в приложении **своего** банка в рамках СБП-потока; каждое **списание инициирует ТСП** на период; без действующего мандата и в пределах лимитов списание недопустимо (AD-009), неопределённый исход — без повторной отправки (AD-010). Полная модель переходов — `docs/spec/subscriptions.md`.

### 8.1 Методы

| Метод | Назначение | Идемпотентность |
|---|---|---|
| `POST /v1/subscriptions` | создать подписку и запустить подтверждение согласия | `Idempotency-Key` → тот же `subscriptionId` |
| `GET /v1/subscriptions/{subscriptionId}` | состояние мандата | GET |
| `POST /v1/subscriptions/{subscriptionId}/pause` | приостановить списания (согласие не отзывается) | `Idempotency-Key` |
| `POST /v1/subscriptions/{subscriptionId}/resume` | возобновить списания | `Idempotency-Key` |
| `POST /v1/subscriptions/{subscriptionId}/cancel` | отменить подписку (отзыв/прекращение согласия) | `Idempotency-Key` |
| `GET /v1/subscriptions/{subscriptionId}/payments` | список списаний (наблюдаемость, разбор) | GET |
| `POST /v1/payments` с `subscriptionId` | **рекуррентное списание** по мандату | `Idempotency-Key` + `periodKey` (ADR-010) |

### 8.2 Создание подписки

```json
{
  "tspId": "tsp_9f3c2a1b",
  "merchantSubscriptionId": "sub-2026-0001",
  "maxAmountPerCharge": 59900,
  "maxAmountPerPeriod": 59900,
  "period": "MONTH",
  "paymentPurpose": "Подписка «Кино+», 1 месяц",
  "redirectUrl": "https://merchant.example.com/subscription/return"
}
```

Ответ `201`:
```json
{
  "subscriptionId": "sub_7c2a91",
  "merchantSubscriptionId": "sub-2026-0001",
  "status": "PENDING_CONSENT",
  "maxAmountPerCharge": 59900,
  "period": "MONTH",
  "expiresAt": "2027-09-28T00:00:00.000Z"
}
```

Статусы мандата: `PENDING_CONSENT | ACTIVE | PAUSED | REVOKED | EXPIRED`. Списание разрешено только в `ACTIVE`.

### 8.3 Списание по подписке

`POST /v1/payments` c `Idempotency-Key`:

```json
{
  "tspId": "tsp_9f3c2a1b",
  "subscriptionId": "sub_7c2a91",
  "amount": 59900,
  "currency": "RUB",
  "periodKey": "2026-09",
  "merchantOrderId": "sub-2026-0001-202609"
}
```

Ответ `201` — обычный платёж (`paymentId`, `status`). Далее платёж живёт в статусной машине: `CREATED → PAID → CREDITED → COMPLETED` (без `QR_ISSUED`); при неопределённом исходе остаётся `CREATED` (внутреннее `OPKC_UNKNOWN`) до разрешения через запрос статуса/сверку.

Отказы: `SUBSCRIPTION_NOT_ACTIVE` (422), `SUBSCRIPTION_LIMIT_EXCEEDED` (422), `CHARGE_PERIOD_CLOSED` (409), `CONSENT_REVOKED` (422). При любом из них обращение в ОПКЦ не выполняется.

### 8.4 Совместимость

Для потребителей v0.1 ничего не меняется: поля `subscriptionId`/`periodKey` опциональны, новые пути и события используются только при работе с подписками.
