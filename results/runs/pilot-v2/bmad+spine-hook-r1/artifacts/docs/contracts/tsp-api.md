# Контракт API ТСП (мерчант-API) — v0.2 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (v0.2 добавляет рекуррентные ресурсы **аддитивно**; v0.1 остаётся совместимой базой)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (рекуррентные списания), AD-003, AD-009, AD-010 (spine)

Назначение: контракт между **ТСП/мерчантом** и **СБП-шлюзом банка** (ядро, собственная разработка). Контракт **не зависит** от протокола ОПКЦ СБП (AD-008): адаптер НСПК скрыт за внутренним интерфейсом шлюза.

## 1. Общие положения

- Транспорт: **HTTPS, REST/JSON**, версия пути `/v1`.
- Кодировка: UTF-8. Числа сумм — **целые, в копейках** (minor units), валюта — `RUB` (ISO 4217: 643).
- Временные метки — ISO 8601 (UTC), формат `YYYY-MM-DDTHH:MM:SS.sssZ`.
- Авторизация ТСП: **mTLS** (сертификат ТСП, выпущенный УЦ банка) + `X-API-Key`. Детали финализирует ИБ на A4; для v0.1 — mTLS обязателен. Идентичность вызывающего — из сертификата; `tspId` в теле должен совпадать с ней, иначе `403` (проверка ownership, см. §3.6).
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

### 3.6 Согласие на рекуррентные списания (v0.2)

`POST /v1/consents` — создать согласие плательщика.

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "payerRef": "pmt_…",              // опц.: минимизированный идентификатор плательщика (токен/маска), если известен ТСП
  "purpose": "Подписка «Кинопоиск», ежемесячно",
  "maxAmountPerCharge": 59900,      // предел одного списания, копейки
  "maxAmountPerPeriod": 59900,      // предел за период, копейки
  "period": "MONTH",                // DAY | WEEK | MONTH | YEAR
  "frequency": "MONTHLY",
  "validUntil": "2027-09-28T00:00:00.000Z",
  "redirectUrl": "https://merchant.example.com/subscribe/return" // опц.
}
```

Ответ `201`:
```json
{
  "consentId": "cns_5a6b7c",
  "tspId": "tsp_9f3c2a1b",
  "status": "PENDING_PAYER",
  "consentUrl": "https://…",        // ссылка/диплинк плательщику для подтверждения в банке-эмитенте
  "mandateTextVersion": "v1"
}
```

Правила: согласие активируется **только по подтверждению плательщика** в его банке/через ОПКЦ; истина о статусе — у ОПКЦ (AD-010). **Маршрутизация плательщика:** шлюз возвращает `consentUrl` (ссылку/диплинк), по которой плательщик попадает на экран подтверждения; если ТСП передал `payerRef`, шлюз направляет подтверждение через известный канал, иначе плательщик идентифицируется банком-эмитентом при активации. Точный канал/формат — по регламенту ОПКЦ `[ТРЕБУЕТ ПРОВЕРКИ]`. Каждый ресурс согласия/подписки/списания принадлежит одному ТСП: обращение к чужому идентификатору → `403 FORBIDDEN` (проверка ownership, см. `x-authorization`).

`GET /v1/consents/{consentId}` → `200 Consent` со статусом: `CREATED | PENDING_PAYER | ACTIVE | SUSPENDED | REVOKED | EXPIRED | REJECTED`.

`POST /v1/consents/{consentId}/revoke` — отзыв согласия по инициативе ТСП (чужой ресурс → `403`). Останавливает **будущие** списания; проведённые платежи не отменяет (корректировка — возвратом, ADR-005).

### 3.7 Подписка (v0.2)

`POST /v1/subscriptions` — привязать согласие к тарифу/расписанию ТСП.

```json
{ "tspId": "tsp_9f3c2a1b", "consentId": "cns_5a6b7c", "planRef": "cinema-monthly", "schedule": "MONTHLY-5", "amount": 59900 }
```
Ответ `201`: `{ "subscriptionId": "sub_1f2e3d", "consentId": "cns_5a6b7c", "status": "ACTIVE", "nextChargeAt": "…" }`.

`GET /v1/subscriptions/{subscriptionId}` · `PATCH /v1/subscriptions/{subscriptionId}` (тело — `SubscriptionUpdate`: только изменяемые поля `schedule`/`amount`/`status`; неизменяемые `tspId`/`consentId`/`planRef` не требуются) · `DELETE /v1/subscriptions/{subscriptionId}` (отмена подписки; согласие при этом **не** отзывается автоматически). Чужой ресурс → `403`.

### 3.8 Рекуррентное списание (v0.2)

`POST /v1/subscriptions/{subscriptionId}/charges` — инициировать списание (по расписанию или вручную).

```json
{ "amount": 59900, "scheduledAt": "2026-10-05T03:00:00.000Z", "reason": "Ежемесячное списание" }
```
Ответ `201`: `{ "chargeId": "chg_9a8b7c", "subscriptionId": "sub_1f2e3d", "consentId": "cns_5a6b7c", "amount": 59900, "status": "PLANNED" }`.

Правила (AD-009): `scheduledAt` **обязателен** и должен быть **не ранее now + срока предуведомления** (baseline 24 ч; финально — по регламенту ОПКЦ `[ТРЕБУЕТ ПРОВЕРКИ]`); иначе `422 CHARGE_WINDOW_NOT_MET`. Немедленное списание запрещено. Списание материализуется в платёж **только** при `Consent.status=ACTIVE`, сумме/периодичности в пределах согласия и выдержанном окне предуведомления. Иначе — `charge.skipped` (или `422 CONSENT_LIMIT_EXCEEDED` при явном запросе вне лимита) без движения денег. **Дедупликация списаний:** уникальность в слоте расписания — по `(subscriptionId, scheduledAt)`; повторная инициация в тот же слот возвращает существующий `Charge`, а не создаёт новый (в дополнение к `Idempotency-Key` и идемпотентности планировщика по `chargeId`). Повторный запуск планировщика дубль не создаёт. Чужой ресурс → `403`.

`GET /v1/subscriptions/{subscriptionId}/charges/{chargeId}` → `200 Charge` (`PLANNED | NOTIFIED | INITIATED | DONE | SKIPPED | FAILED`, поле `paymentId` при материализации).

### 3.9 Предуведомление плательщика (v0.2)

Перед списанием шлюз инициирует уведомление плательщика через ОПКЦ (срок и канал — по регламенту ОПКЦ `[ТРЕБУЕТ ПРОВЕРКИ]`). Возражение/отмена в окне → списание не выполняется (`charge.skipped`). ТСП получает событие `charge.failed`/`charge.skipped`.

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

Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `FORBIDDEN` (403, чужой ресурс — ownership check), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `CONSENT_NOT_ACTIVE` (422), `CONSENT_LIMIT_EXCEEDED` (422), `CHARGE_WINDOW_NOT_MET` (422), `RATE_LIMITED` (429), `FEATURE_DISABLED` (503), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.

## 5. Вебхуки (нотификации ТСП)

Шлюз доставляет события на `webhookUrl` ТСП (ADR-004: at-least-once, ретраи, DLQ).

Заголовки: `X-SBP-Event-Id` (uuid события — для дедупликации у ТСП), `X-SBP-Signature` (HMAC-SHA256 тела, ключ — `webhookSecret`), `Content-Type: application/json`.

События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
- `consent.activated` — согласие активировано плательщиком (`consentId`, `status: ACTIVE`)
- `consent.revoked` — согласие отозвано/просрочено (`consentId`, причина)
- `charge.completed` — рекуррентное списание завершено (`chargeId`, `paymentId`, `status: DONE`)
- `charge.failed` — списание не удалось
- `charge.skipped` — списание не выполнено по согласию/лимиту/предуведомлению (деньги не двигались)

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
- **v0.1 → v0.2:** только добавление (новые пути consent/subscription/charge, новые схемы, новые события вебхуков). Существующие пути `/v1/payments*`, схемы `PaymentRequest`/`Payment` и перечисление `Payment.status` не изменялись. Проверено `contract_diff` (breaking: 0). Машиночитаемый контракт `openapi/tsp-api.yaml` заявлен как **OpenAPI 3.1.0** (securityScheme `mutualTLS`); он покрывает §3.2–3.3 и §3.6–3.8 — операции §3.1 (`POST /v1/tsp`) и §3.4–3.5 (возвраты) пока только в MD-версии (см. §7).
- Добавление опциональных полей — обратно совместимо, не требует новой версии.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
5. Рекуррентный протокол (методы/события согласий, срок предуведомления, поведение при отзыве во время платежа) — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ], фиксируется в контракте адаптера ОПКЦ.
6. Сроки хранения/уничтожения ПДн плательщика в согласии и снимок версии текста мандата (`mandateTextVersion`) — с юристами/ИБ (152-ФЗ).
7. Формат расписания (`schedule`) — простой строковый реестр или RFC 5545 RRULE; влияет на модель данных подписки.
8. Покрытие машиночитаемого `openapi/tsp-api.yaml`: перенести §3.1 (онбординг ТСП) и §3.4–3.5 (возвраты) из MD-версии; выровнять состав операций двух артефактов контракта.
