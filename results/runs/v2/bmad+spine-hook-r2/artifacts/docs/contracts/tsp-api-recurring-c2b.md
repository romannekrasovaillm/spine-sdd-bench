# Изменения контракта API ТСП для рекуррентных C2B-списаний — v0.1 → v0.2

- Status: Draft (для ревью на гейте A1 изменения `sbp-recurring-c2b`)
- Owner: solution-architect (платёжный контур)
- Related: ADR-008, ADR-009, AD-003, AD-009; дополняет `docs/contracts/tsp-api.md`
- Машинный контракт: `openapi/tsp-api.yaml` (было `0.1.0`, стало `0.2.0`)

## 1. Принцип изменения: только аддитивно

Изменение **не ломает существующих потребителей v0.1**:

- существующие методы и поля не удаляются, не переименовываются и не меняют тип;
- новые поля добавляются только как **опциональные**;
- новые методы добавляются новыми путями под тем же префиксом `/v1`;
- значения существующих `enum` (статусы платежа) не меняются и не удаляются;
- версия контракта повышается минорно (`0.2.0`) — семантика «обратно совместимое добавление» (см. `docs/contracts/tsp-api.md` §6).

Проверка неразрушаемости — машинный дифф версий (`contract_diff`): breaking changes должны отсутствовать.

## 2. Новые методы

| Метод | Назначение | Идемпотентность |
|---|---|---|
| `POST /v1/mandates` | ТСП инициирует заявку на согласие плательщика (подписку) | `Idempotency-Key` обязателен |
| `GET /v1/mandates/{mandateId}` | Статус и параметры мандата | GET |
| `GET /v1/mandates` | Список мандатов ТСП (фильтры `tspId`, `status`, пагинация) | GET |
| `POST /v1/mandates/{mandateId}/revoke` | ТСП отменяет подписку (не путать с отзывом плательщиком в его банке) | `Idempotency-Key` обязателен |
| `POST /v1/mandates/{mandateId}/charges` | Ручное (внеплановое/повторное) списание в рамках мандата | `Idempotency-Key` обязателен |
| `GET /v1/mandates/{mandateId}/charges` | Список списаний по мандату | GET |

Плановые списания выполняет планировщик шлюза; ТСП наблюдает их через `GET /v1/payments/{paymentId}` и события. Метод `/v1/mandates/{mandateId}/charges` нужен для внепланового списания (например, повтор при неуспехе), а не для регулярного расписания.

## 3. Новые схемы (в общих чертах)

**`MandateRequest`**
```json
{
  "tspId": "tsp_9f3c2a1b",
  "payerRef": "tok_7c1a…",              // токен плательщика, согласованный с ОПКЦ; без ПДн
  "currency": "RUB",
  "maxAmountPerCharge": 99900,          // копейки, int
  "maxAmountPerPeriod": 199800,
  "period": "MONTH",                    // MONTH | WEEK | CUSTOM
  "validTo": "2027-09-28T00:00:00.000Z",
  "description": "Подписка «Кинопоиск+»",
  "redirectUrl": "https://merchant.example.com/subscription/return",
  "merchantSubscriptionId": "sub-12345"
}
```

**`Mandate`** (ответ)
```json
{
  "mandateId": "man_5a6b7c",
  "tspId": "tsp_9f3c2a1b",
  "status": "PENDING_CONSENT",          // PENDING_CONSENT | PENDING_OPKC | ACTIVE | SUSPENDED | REVOKED | EXPIRED | REJECTED
  "currency": "RUB",
  "maxAmountPerCharge": 99900,
  "maxAmountPerPeriod": 199800,
  "period": "MONTH",
  "validFrom": null,
  "validTo": "2027-09-28T00:00:00.000Z",
  "consentRef": null,                   // подтверждение ОПКЦ после активации
  "consentUrl": "https://…",            // для подтверждения плательщиком (канал — по НСПК)
  "createdAt": "2026-09-28T10:00:00.000Z",
  "merchantSubscriptionId": "sub-12345"
}
```

**`ChargeRequest`**
```json
{
  "amount": 49900,
  "periodKey": "2026-10",               // обязателен: ключ идемпотентности и знаменатель лимита периода
  "description": "Внеплановое списание"
}
```

`periodKey` обязателен для любого списания (формат — `docs/spec/subscription-lifecycle.md` §1): он одновременно ключ идемпотентности и знаменатель лимита `maxAmountPerPeriod`. Без него ручные списания могли бы гонкой превысить лимит периода.

**`Charge`** (ответ)
```json
{
  "chargeId": "chg_1a2b3c",
  "mandateId": "man_5a6b7c",
  "paymentId": "pay_8d1e4f5a",
  "periodKey": "2026-10",
  "amount": 49900,
  "status": "QR_ISSUED",                // статус платежа (см. §5)
  "createdAt": "2026-09-28T10:05:00.000Z"
}
```

## 4. Расширения существующих схем

**`PaymentRequest`** — добавляются опциональные поля:
- `origin`: `qr | link | recurring` (по умолчанию `qr` — поведение v0.1 сохраняется);
- `mandateId`: обязателен при `origin=recurring`;
- `periodKey`: опционален; при `origin=recurring` задаёт идемпотентность планового списания.

**`Payment`** — добавляются опциональные поля `origin`, `mandateId`, `periodKey`, `chargeId`. Существующие поля и значения `status` не меняются.

## 5. Семантика состояний

Для `origin=recurring` состояние `QR_ISSUED` означает «списание предъявлено банку плательщика, ожидается подтверждение» (QR не создаётся, `qrId`/`qrUrl`/`qrImage` отсутствуют). Набор состояний платежа не меняется; зачисление — только из `PAID` (AD-005).

## 6. Новые события вебхуков

Добавляются события жизненного цикла мандата (доставляются по тем же правилам: at-least-once, дедуп по `X-SBP-Event-Id`, HMAC-подпись):

- `mandate.activated` — согласие подтверждено (`status: ACTIVE`);
- `mandate.rejected` — согласие отклонено;
- `mandate.suspended` / `mandate.resumed` — приостановлен/возобновлён;
- `mandate.revoked` — согласие отозвано (плательщиком или ТСП);
- `mandate.expired` — истёк срок.

Движение денег по списанию отражается существующими событиями `payment.completed` / `payment.failed` / `payment.expired`, дополненными полями `origin`, `mandateId`, `periodKey` (аддитивно). Отдельные события `charge.*` **не вводятся**, чтобы не дублировать поток платежей.

Тело события (`mandate.activated`):
```json
{
  "eventId": "evt_…",
  "type": "mandate.activated",
  "mandateId": "man_5a6b7c",
  "status": "ACTIVE",
  "actor": "PAYER",                     // PAYER | TSP | BANK — источник перехода (для аудита)
  "consentRef": "…",
  "timestamp": "2026-09-28T10:02:00.000Z"
}
```

Поле `actor` присутствует во всех событиях жизненного цикла мандата: источник перехода необходим для аудита. Авторство отзыва различается:

- **отзыв плательщиком** инициируется в банке плательщика → событие ОПКЦ `mandate.revoked` с `actor=PAYER`;
- **отмена ТСП** инициируется через `POST /v1/mandates/{mandateId}/revoke` → шлюз вызывает `cancelMandate` адаптера ОПКЦ → подтверждение приходит событием `mandate.revoked` с `actor=TSP`.

## 7. Идемпотентность и ошибки

- Все новые `POST` требуют `Idempotency-Key`; повтор с тем же ключом и телом возвращает тот же ресурс (200/201), повтор с тем же ключом и другим телом — `409 IDEMPOTENCY_CONFLICT`.
- Повтор `POST /v1/mandates/{mandateId}/charges` с тем же `(mandateId, periodKey)` возвращает существующее списание (тот же `chargeId`/`paymentId`).
- Новые коды ошибок (RFC 9457, аддитивно к `docs/contracts/tsp-api.md` §4): `MANDATE_NOT_FOUND` (404), `MANDATE_NOT_ACTIVE` (409), `MANDATE_REVOKED` (409), `MANDATE_LIMIT_EXCEEDED` (422), `MANDATE_EXPIRED` (409), `PAYER_REF_INVALID` (422).

Пример:
```json
{
  "type": "https://api.bank.ru/sbp/errors/mandate-not-active",
  "title": "Мандат не активен",
  "status": 409,
  "detail": "Списание по мандату man_5a6b7c невозможно: статус REVOKED",
  "code": "MANDATE_NOT_ACTIVE",
  "traceId": "…",
  "idempotencyKey": "…"
}
```

## 8. Анализ совместимости

| Изменение | Тип | Влияние на потребителя v0.1 |
|---|---|---|
| Новые пути `/v1/mandates*` | аддитивное | нет — не вызываются старым кодом |
| Новые опциональные поля в `PaymentRequest`/`Payment` | аддитивное | нет — неизвестные поля игнорируются, старые поля без изменений |
| Новые значения `origin` | аддитивное | нет — по умолчанию `qr`, поведение прежнее |
| Новые события `mandate.*` | аддитивное | нет — старые подписки не затрагиваются |
| Новые коды ошибок | аддитивное | нет — старые коды сохранены и не переиспользованы |
| Повышение `info.version` `0.1.0 → 0.2.0` | минорное | нет — обратно совместимо |

Ожидаемый результат `contract_diff` (v0.1 → v0.2): **breaking changes — 0**.

## 9. Открытые вопросы

1. Формат `payerRef` (токен) — определяется протоколом НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`.
2. `consentUrl`/канал подтверждения плательщика (deep-link, QR, редирект в банк) — по НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`.
3. Нужны ли `suspend`/`resume` для ТСП (dunning) в первой версии.
4. Пагинация списков — курсорная или offset (финализируется на A1).
