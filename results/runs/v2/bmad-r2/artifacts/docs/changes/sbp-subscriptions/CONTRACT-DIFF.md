# Дельта контрактов: СБП-подписки (без поломки существующих потребителей)

- Status: Proposed (входит в пакет изменения; публикуется после гейта A3′)
- Date: 2026-09-28
- Owner: solution-architect (платёжный контур)
- Решение: `docs/adr/ADR-008-...md`; оценка — `IMPACT.md`
- Затрагивает: `openapi/tsp-api.yaml` (0.1.0 → 0.2.0), `docs/contracts/tsp-api.md` (v0.1 → v0.2), `docs/contracts/opkc-adapter.md` (v0.1 → v0.2)

## 1. Правила совместимости (инвариант изменения)

1. Никаких удалений и переименований в существующих путях, полях, кодах и статусах.
2. **Ни одного нового обязательного поля/заголовка** в существующих запросах; все новые поля — опциональные.
3. Новые значения — только в **новых** перечислениях (`MandateStatus`). `Payment.status` не расширяется.
4. Новые пути, события и коды ошибок — аддитивны.
5. Действующий потребитель, не использующий подписки, получает **прежнее поведение**; `initiation` по умолчанию — `ONE_OFF`.
6. Мажорная версия `/v2` и deprecation `/v1` **не требуются**.

## 2. `openapi/tsp-api.yaml`: сводка дельты

| Элемент | Действие | Совместимость |
|---|---|---|
| `info.version` | `0.1.0 → 0.2.0` | минор, аддитивно |
| `paths./v1/payments.post` | без изменения структуры; в `PaymentRequest` добавлены опциональные `mandateId`, `initiation` | обратно совместимо |
| `paths./v1/payments/{paymentId}.get` | в `Payment` добавлены опциональные `mandateId`, `initiation` | обратно совместимо |
| `paths./v1/mandates.post` | **новый** | аддитивно |
| `paths./v1/mandates/{mandateId}.get` | **новый** | аддитивно |
| `paths./v1/mandates/{mandateId}/revoke.post` | **новый** | аддитивно |
| `components.schemas.MandateRequest` | **новый** | аддитивно |
| `components.schemas.Mandate` | **новый** | аддитивно |
| `components.schemas.MandateStatus` | **новый** enum `[CREATED, PENDING_PAYER, ACTIVE, SUSPENDED, REVOKED, EXPIRED, FAILED]` | аддитивно |
| `components.schemas.PaymentRequest.required` | без изменения (`[amount, merchantOrderId]`) | обратно совместимо |
| `components.schemas.Payment.required` | без изменения (`[paymentId, amount, status]`) | обратно совместимо |

## 3. `docs/contracts/tsp-api.md`: дельта v0.1 → v0.2

### 3.1. Новые методы (раздел 3.6 «Согласия на рекуррентные списания»)

| Метод | Назначение | Идемпотентность | Ответ |
|---|---|---|---|
| `POST /v1/mandates` | Регистрация согласия плательщика; возврат QR/ссылки для подтверждения | `Idempotency-Key` (обязателен) | `201 {mandateId, status: PENDING_PAYER, qrId, qrUrl, qrImage?, expiresAt}` |
| `GET /v1/mandates/{mandateId}` | Статус согласия | идемпотентен | `200 Mandate` |
| `POST /v1/mandates/{mandateId}/revoke` | Отзыв согласия по инициативе ТСП | `Idempotency-Key` (обязателен) | `200 Mandate` со `status: REVOKED` |

Пример тела `POST /v1/mandates` (аддитивно, точные поля лимитов — по протоколу НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`):

```json
{
  "tspId": "tsp_9f3c2a1b",
  "currency": "RUB",
  "maxAmountPerCharge": 99900,        // копейки, опц.
  "maxAmountPerPeriod": 999000,       // копейки, опц.
  "period": "MONTHLY",                // опц., справочник по протоколу
  "validUntil": "2027-09-28T00:00:00.000Z",
  "redirectUrl": "https://merchant.example.com/subscription/12345/return",
  "merchantMandateId": "sub-12345",
  "payerReference": "opaque-ref"      // опц., непрозрачная ссылка; ПДн минимизируются
}
```

Пример тела рекуррентного платежа:

```json
{
  "paymentId": "pay_8d1e4f5a",
  "mandateId": "mnd_7c2a9b1e",
  "amount": 59900,
  "currency": "RUB",
  "paymentPurpose": "Подписка «Кинопоиск», сентябрь"
}
```

Правила: рекуррентное списание допускается только при согласии `ACTIVE` того же ТСП/валюты и в пределах лимитов; QR не запрашивается; сумма и реквизиты платежа иммутабельны (ADR-002); повтор с тем же `Idempotency-Key` → тот же `paymentId`.

### 3.2. Расширение существующего `POST /v1/payments`

Добавлены **опциональные** поля:

- `mandateId` (string) — идентификатор согласия;
- `initiation` (`ONE_OFF | RECURRENT`, по умолчанию `ONE_OFF`).

Для `initiation=RECURRENT` поле `qrType` не требуется и QR не выдаётся. Для существующих потребителей без этих полей поведение прежнее.

### 3.3. Расширение ответа `GET /v1/payments/{paymentId}`

Добавлены **опциональные** `mandateId`, `initiation`. `refunds[]` работает как прежде.

### 3.4. Новые вебхук-события (раздел 5)

- `mandate.activated` — согласие подтверждено плательщиком (`PENDING_PAYER → ACTIVE`).
- `mandate.revoked` — согласие отозвано (плательщиком/его банком или ТСП).
- `mandate.expired` — истёк срок согласия.
- `mandate.failed` — регистрация/подтверждение согласия не удались.

Заголовки и подпись (HMAC, `X-SBP-Event-Id`) — как для существующих событий; ТСП дедуплицирует по `eventId`. События `payment.completed`/`payment.failed` применяются и к рекуррентным списаниям.

### 3.5. Новые коды ошибок (раздел 4)

Аддитивно к существующим:

| Код | HTTP | Когда |
|---|---|---|
| `MANDATE_NOT_FOUND` | 404 | Согласие не найдено |
| `MANDATE_NOT_ACTIVE` | 422 | Попытка списания по согласию не в `ACTIVE` |
| `MANDATE_REVOKED` | 422 | Согласие отозвано |
| `MANDATE_LIMIT_EXCEEDED` | 422 | Сумма превышает лимит согласия |
| `MANDATE_TSP_MISMATCH` | 403 | Согласие принадлежит другому ТСП |

Тело ошибок — прежний формат RFC 9457 (Problem Details). Существующие коды не меняются.

## 4. `docs/contracts/opkc-adapter.md`: дельта v0.1 → v0.2 (внутренний контракт)

Аддитивно к §3–4:

| Метод / событие | Смысл | Ключевые поля |
|---|---|---|
| `registerMandate` | Зарегистрировать согласие в ОПКЦ | `reference` (= `mandateId`), реквизиты лимитов/срока, `tspId` |
| `getMandateStatus` | Статус согласия (сверка/опрос) | `mandateRef` → `PENDING_PAYER`/`ACTIVE`/`REVOKED`/`EXPIRED`/`UNKNOWN` |
| `cancelMandate` | Отзыв/закрытие согласия | `mandateRef`, `reason` |
| `createSubscriptionCharge` | Инициация списания по согласию | `reference` (= `paymentId`), `mandateRef`, `amount`, `currency` |
| событие `mandate.activated` / `mandate.revoked` / `mandate.expired` | Изменение состояния согласия | `eventId`, `mandateRef`(= `reference`), `timestamp` |
| событие `charge.scheduled` (условно) | Предварительное уведомление о списании, если требует протокол | `eventId`, `mandateRef`, `chargeRef`, `notifyAt` |

Требования к вендору сохраняются и расширяются: **идемпотентность мутирующих методов по `reference`** (в т.ч. `registerMandate`, `createSubscriptionCharge`) — обязательное требование RFP (см. `docs/rfp/vendor-rfp.md` §2 G3); нормализация статусов согласия; тестовый контур со сценариями согласий и повторов.

## 5. Влияние на действующих потребителей

- Потребитель без подписок: **изменений не требуется**; все прежние запросы валидны, ответы содержат те же обязательные поля.
- Потребитель, внедряющий подписки: использует новые пути; для списаний передаёт `mandateId` + `initiation=RECURRENT`.
- Метрика совместимости: доля успешных прежних вызовов после релиза v0.2 — 100 %; контрактные тесты существующих схем — без изменений.

Открытые вопросы по контракту — в `docs/contracts/tsp-api.md` §7 и `docs/solutioning.md` §10.
