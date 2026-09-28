# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1; v0.2 — изменение ADR-008)
- Версия контракта: 0.2-draft (2026-09-28; аддитивно добавлены мандаты и списания — §3.6–§3.9, обратная совместимость v0.1 в `/v1` сохранена)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки/мандаты), AD-003, AD-009, AD-010, AD-011 (spine)

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
  "paymentOrigin": "qr",           // qr | mandate — источник платежа (v0.2; опционально, по умолчанию qr)
  "mandateId": null,               // man_… для списаний по мандату (v0.2; иначе null)
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

### 3.6 Регистрация мандата (согласия на рекуррентные списания)

`POST /v1/mandates` — инициирует получение согласия плательщика; `Idempotency-Key` обязателен.

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "maxAmountPerCharge": 500000,        // копейки; лимит разового списания (обязателен)
  "maxTotalAmount": 6000000,           // копейки; опц. лимит за весь срок
  "validFrom": "2026-10-01T00:00:00.000Z",
  "validTo": "2027-10-01T00:00:00.000Z",
  "paymentPurpose": "Подписка «Кино+», тариф Базовый",
  "payerRef": "subscriber-42",         // опц. идентификатор плательщика у ТСП
  "consentRedirectUrl": "https://merchant.example.com/subscribe/done"
}
```

Ответ `201`:
```json
{
  "mandateId": "man_7c2b9e1d",
  "status": "PENDING_CONSENT",         // PENDING_CONSENT | ACTIVE | SUSPENDED | REVOKED | EXPIRED | REJECTED
  "consentUrl": "https://…",           // ссылка/QR для подтверждения согласия плательщиком (по протоколу ОПКЦ)
  "maxAmountPerCharge": 500000,
  "validFrom": "2026-10-01T00:00:00.000Z",
  "validTo": "2027-10-01T00:00:00.000Z"
}
```

Правила: `maxAmountPerCharge` > 0; `validTo` > `validFrom`; лимиты не выше лимитов НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`. Параметры мандата **иммутабельны после активации**: изменение условий — только новый мандат. Активация приходит асинхронно (вебхук `mandate.activated`) после подтверждения согласия через ОПКЦ [ТРЕБУЕТ ПРОВЕРКИ: форма и срок подтверждения согласия в протоколе].

### 3.7 Статус мандата

`GET /v1/mandates/{mandateId}` → `200 { mandateId, status, maxAmountPerCharge, maxTotalAmount, validFrom, validTo, payerRef, suspendedReason }`

### 3.8 Управление мандатом: приостановка, возобновление, отзыв

- `POST /v1/mandates/{mandateId}/suspend` → `200 { mandateId, status: "SUSPENDED" }` (новые списания запрещены; возобновляемо)
- `POST /v1/mandates/{mandateId}/resume` → `200 { mandateId, status: "ACTIVE" }`
- `POST /v1/mandates/{mandateId}/revoke` → `200 { mandateId, status: "REVOKED" }` (необратимо; новые списания запрещаются немедленно)

Все три метода идемпотентны (повтор → текущий/целевой статус, без ошибки) и, как все `POST` (§2), требуют заголовок `Idempotency-Key`. Отзыв плательщиком выполняется в его банке и (по протоколу ОПКЦ) приходит нотификацией — шлюз переводит мандат в `REVOKED` и уведомляет ТСП [ТРЕБУЕТ ПРОВЕРКИ: канал и форма нотификации об отзыве].

### 3.9 Списание по мандату

`POST /v1/mandates/{mandateId}/charges` — рекуррентное списание без QR; `Idempotency-Key` обязателен.

Запрос:
```json
{
  "amount": 49900,                     // копейки; <= maxAmountPerCharge
  "merchantOrderId": "sub-2026-10",    // обязателен; период/инвойс, уникален в рамках мандата
  "paymentPurpose": "Абонентская плата за октябрь 2026",
  "noticeRef": "notice-2026-10-01"     // опц. по умолчанию; обязателен, если политика A2 требует уведомление до списания (AD-016)
}
```

Ответ `201` — ресурс **Payment** с признаком списания:
```json
{
  "paymentId": "pay_8d1e4f5a",
  "mandateId": "man_7c2b9e1d",
  "paymentOrigin": "mandate",
  "status": "CREATED",                 // далее CREATED → PAID → CREDITED → COMPLETED (без QR_ISSUED)
  "amount": 49900,
  "merchantOrderId": "sub-2026-10"
}
```

Правила: списание возможно только при `status=ACTIVE`, `amount ≤ maxAmountPerCharge`, остатке `maxTotalAmount`, времени в периоде действия и совпадении ТСП-владельца; иначе — ошибка без создания платежа (AD-011). Финансовый ключ дедупликации — (`mandateId`, `merchantOrderId`), им владеет агрегат мандата на срок его жизни; `Idempotency-Key` защищает от повтора запроса (24 ч). Повтор `merchantOrderId` при **завершённом подтверждённом** списании → `409 MANDATE_CHARGE_CONFLICT`; при терминальном `FAILED`/`EXPIRED` ключ освобождается для повторной попытки. Если политика A2 требует уведомление до списания, подтверждение уведомления (`noticeRef`/`noticeConfirmedAt`) обязательно, иначе списание отклоняется (AD-016). Результат списания отражается стандартными событиями `payment.completed`/`payment.failed`. Зачисление — только из `PAID` (AD-005).

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `MANDATE_CHARGE_CONFLICT` (409, повтор `merchantOrderId`/периода в рамках мандата), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `MANDATE_NOT_ACTIVE` (422, мандат не `ACTIVE`), `MANDATE_LIMIT_EXCEEDED` (422, `amount > maxAmountPerCharge` или превышен `maxTotalAmount`), `MANDATE_EXPIRED` (422, вне периода действия), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `mandate.activated` — согласие плательщика подтверждено, мандат `ACTIVE` (v0.2)
- `mandate.suspended` — мандат приостановлен (v0.2)
- `mandate.resumed` — мандат возобновлён (v0.2)
- `mandate.expired` — истёк период действия мандата (v0.2)
- `mandate.rejected` — согласие не получено/отклонено ОПКЦ (v0.2)
- `mandate.revoked` — мандат отозван (плательщиком или ТСП) (v0.2)

Исход рекуррентного списания доставляется стандартными событиями `payment.*` (отдельных событий списания нет). ТСП обязан **игнорировать неизвестные типы событий** и обрабатывать их идемпотентно по `eventId` — это условие обратной совместимости при добавлении новых событий.

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
- v0.2 (2026-09-28, ADR-008): мандаты и списания добавлены **аддитивно** — новые пути `/v1/mandates*`, опциональные поля `Payment` (`paymentOrigin`, `mandateId`), новые события вебхуков и коды ошибок. Существующие потребители v0.1 не затрагиваются.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Мандаты: способ подтверждения согласия (`consentUrl`/QR, срок жизни ссылки) и кто хранит согласие — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
6. Уведомление плательщика до списания: обязательность, срок, канал, кто инициирует (`noticeRef` у ТСП или шлюз) — по регламенту НСПК и юридической модели [ТРЕБУЕТ ПРОВЕРКИ].
7. Лимиты мандата (`maxAmountPerCharge`, `maxTotalAmount`, периодичность) — по требованиям НСПК и риск-политике [ТРЕБУЕТ ПРОВЕРКИ].
8. Идемпотентность списания на стороне ОПКЦ по (`mandateId`, период) — требование к вендору транспорта (см. `docs/contracts/opkc-adapter.md` §5).
