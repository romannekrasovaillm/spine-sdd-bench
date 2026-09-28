# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1 изменения «подписки СБП»)
- Версия контракта: 0.2 — расширяет 0.1 мандатами и рекуррентными списаниями **обратно совместимо**
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки), AD-003, AD-009, AD-010 (spine)
- Машиночитаемая версия: `openapi/tsp-api.yaml` (v0.2.0)

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

### 3.6 Мандаты (согласие плательщика на рекуррентные списания)

Новое в v0.2 (ADR-008). Мандат — согласие плательщика; подтверждается плательщиком в приложении своего банка через ОПКЦ. Шлюз ведёт состояние мандата (`docs/spec/mandate-state-machine.md`).

#### 3.6.1 Регистрация мандата

`POST /v1/mandates`

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "amountLimitPerCharge": 99900,   // разовый лимит, копейки
  "amountLimitTotal": 1198800,     // суммарный лимит, копейки
  "periodicity": "monthly",        // формат — по НСПК [ТРЕБУЕТ ПРОВЕРКИ]
  "paymentPurpose": "Подписка «Кино+»",
  "validUntil": "2027-08-15T00:00:00.000Z",
  "merchantOrderId": "sub-12345"
}
```

Ответ `201`:
```json
{
  "mandateId": "mnd_7a1c9e",
  "tspId": "tsp_9f3c2a1b",
  "status": "PENDING_CONSENT",
  "amountLimitPerCharge": 99900,
  "amountLimitTotal": 1198800,
  "amountChargedTotal": 0,
  "consentUrl": "https://qr.nspk.ru/…"
}
```

Правила: `Idempotency-Key` обязателен; мандат переходит в `ACTIVE` только по событию ОПКЦ `mandate.activated`; списания по мандату не в состоянии `ACTIVE` запрещены (AD-009).

#### 3.6.2 Статус мандата

`GET /v1/mandates/{mandateId}` → `200` с полями `Mandate` (см. `openapi/tsp-api.yaml`). Статусы: `PENDING_CONSENT | ACTIVE | SUSPENDED | REVOKED | EXPIRED | REJECTED`.

#### 3.6.3 Отзыв мандата (инициатива ТСП)

`POST /v1/mandates/{mandateId}/revoke` — тело опционально `{ "reason": "…" }`; ответ `200` со статусом `REVOKED`. Идемпотентно. Отзыв плательщиком приходит событием ОПКЦ, а не через этот метод.

### 3.7 Рекуррентное списание

Списание — это **платёж** (`POST /v1/payments`) с `paymentType = recurring` и обязательным `mandateId`:
```json
{
  "amount": 99900,
  "merchantOrderId": "sub-12345-2026-10",
  "paymentType": "recurring",
  "mandateId": "mnd_7a1c9e"
}
```
Правила: списание допускается только при `mandate.status = ACTIVE` и в пределах лимитов мандата (разовый/суммарный/периодичность) — иначе `422`; зачисление в АБС — только из подтверждённого `PAID` (AD-005, AD-010); повтор с тем же `Idempotency-Key` не создаёт второго дебета. Запрос без `paymentType`/`mandateId` — разовый платёж v0.1 (поведение не изменилось).

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `MANDATE_NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `MANDATE_NOT_ACTIVE` (422), `MANDATE_LIMIT_EXCEEDED` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку. При отклонении списания по мандату (`MANDATE_NOT_ACTIVE`/`MANDATE_LIMIT_EXCEEDED`) вызов АБС не производится (AD-009).

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`); используется и для рекуррентных списаний
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `mandate.activated` — согласие плательщика подтверждено, мандат активен
- `mandate.rejected` — в согласии отказано
- `mandate.revoked` — согласие отозвано (плательщиком или ТСП)
- `mandate.suspended` / `mandate.reactivated` — согласие приостановлено/возобновлено
- `mandate.expired` — истёк срок или исчерпан суммарный лимит

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
- **v0.1 → v0.2 (ADR-008)** — только аддитивно: новые пути `/v1/mandates*`, опциональные поля `mandateId`/`paymentType`, новые события и коды ошибок. Ломающих изменений нет (подтверждено `arch-be contract-diff`); потребители v0.1 продолжают работать без изменений.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. **Форма контракта списания** — переиспользование `POST /v1/payments` с `mandateId` (выбрано в ADR-008) против отдельного ресурса `charges` — подтверждается человеком-архитектором на A3.
6. **Состав и формат полей согласия и периодичности** — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
7. **Условная обязательность** `mandateId` при `paymentType=recurring` — формализовать в схеме (`oneOf`/discriminator) или оставить валидацией шлюза (`422`) — решение на A3.
8. **Планировщик списаний** (если бизнес вернётся к gateway-scheduled) — Deferred, отдельный ADR.
