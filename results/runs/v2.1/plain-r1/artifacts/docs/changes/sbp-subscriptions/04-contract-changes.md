# 04. Изменения контрактов (v0.1 → v0.2), без поломки потребителей

- Status: Draft (для рассмотрения на архитектурном решении)
- Owner: solution-architect (платёжный контур) + ИБ
- Связано: ADR-008, `openapi/tsp-api.yaml`, `docs/contracts/tsp-api.md`, `docs/contracts/opkc-adapter.md`

Цель — **аддитивное** расширение контрактов. Правило совместимости уже зафиксировано в `docs/contracts/tsp-api.md` §6: добавление опциональных полей и новых путей обратно совместимо; ломающие изменения — только в `/v2`. Ниже — что добавлено и что **сознательно не тронуто**.

## 1. API ТСП (`openapi/tsp-api.yaml`, `docs/contracts/tsp-api.md`)

### 1.1 Добавлено (не ломает существующих потребителей)

| Элемент | Тип | Совместимость |
|---|---|---|
| `info.version` 0.1.0 → 0.2.0 | метаданные | Minor, аддитивно |
| `POST /v1/subscriptions` (`createSubscription`) | новый путь | Не затрагивает существующие операции |
| `GET /v1/subscriptions/{subscriptionId}` (`getSubscription`) | новый путь | — |
| `POST /v1/subscriptions/{subscriptionId}/cancel` (`cancelSubscription`) | новый путь | — |
| `GET /v1/subscriptions/{subscriptionId}/cycles` (`listSubscriptionCycles`) | новый путь | — |
| `SubscriptionRequest`, `Subscription`, `DebitSchedule` | новые схемы | — |
| `status` подписки: `PENDING_OPKC, ACTIVE, SUSPENDED, CANCELLED, DECLINED, EXPIRED` | **отдельный** enum (не `Payment.status`) | Не расширяет общий enum платёжа |
| `Payment.subscriptionId` (optional), `Payment.debitType` (optional: `ONE_TIME`/`RECURRING`) | новые **опциональные** поля ответа | Старые клиенты игнорируют неизвестные поля |
| Вебхук-события `subscription.activated`, `subscription.declined`, `subscription.cancelled`, `subscription.debit.failed` | новые типы событий | ТСП обрабатывает известные типы; цикл успешного списания отражается существующим `payment.completed` (с `subscriptionId`) |
| Коды ошибок `SUBSCRIPTION_NOT_FOUND`, `SUBSCRIPTION_NOT_ACTIVE`, `MANDATE_REVOKED`, `CYCLE_ALREADY_EXISTS` | новые значения в справочнике ошибок (markdown §4) | Новые коды не меняют семантику существующих |

### 1.2 Сознательно НЕ изменено (гарантия совместимости)

- `PaymentRequest.required` — остаётся `[amount, merchantOrderId]`; тело разового платежа не меняется.
- `Payment.required` — остаётся `[paymentId, amount, status]`.
- **Enum `Payment.status` не расширяется** — этот enum общий с разовыми платежами, и добавление значений могло бы сломать строгих клиентов со `switch`/exhaustive match. Статусы подписки живут в своём поле/схеме.
- Ни один существующий путь/поле/enum не удалён и не переименован; семантика существующих ошибок не меняется.

### 1.3 Правило для ТСП-потребителей (зафиксировать в §6)

- Клиент обязан **игнорировать неизвестные поля** и **не падать на неизвестных типах событий** (forward-compatible).
- Новый функционал подписок — opt-in: ТСП, не вызывающий `/v1/subscriptions`, не наблюдает изменений поведения.
- Новые опциональные поля появляются в ответах `GET /v1/payments/{id}` только для платежей-циклов подписки; для разовых платежей поведение ответа не меняется.

## 2. Контракт адаптера ОПКЦ (`docs/contracts/opkc-adapter.md`)

Внутренний контракт ядро↔транспорт (AD-008 [ADOPTED]) расширяется — это **основа расширения RFP/договора с вендором**, а не самостоятельная реализация банка.

### 2.1 Новые синхронные операции (ядро → адаптер)

| Метод | Ключевые поля | Ответ |
|---|---|---|
| `registerMandate` | `reference` (= `subscriptionId`), реквизиты ТСП/плательщика, параметры согласия | `ACCEPTED` (результат — событием) |
| `debitMandate` | `reference` (= `paymentId` цикла), `mandateId`, `cycleNumber`, `amount` | `ACCEPTED` (результат — событием) |
| `getMandateStatus` | `mandateId` / `reference` | нормализованный статус мандата |
| `cancelMandate` | `mandateId`, `reason` | `CANCELLED` |

### 2.2 Новые события (адаптер → ядро), at-least-once, дедуп по `eventId`

`mandate.registered`, `mandate.declined`, `mandate.debit.succeeded`, `mandate.debit.failed`, `mandate.cancelled`.

### 2.3 Обязательные требования к вендору (добавить в RFP)

- Идемпотентность `registerMandate` по `reference` и `debitMandate` по `reference` (= `paymentId` цикла) — **обязательно** (иначе ретраи дают двойное списание).
- Нормализация статусов/кодов отказа мандатов (ядро не разбирает протокольные тексты НСПК).
- Тестовый контур с воспроизводимыми сценариями: успешное списание, отказ плательщика, истёкший/отозванный мандат, повтор `debitMandate`.
- Точная механика мандатов НСПК — `[ТРЕБУЕТ ПРОВЕРКИ]`; контракт финализируется после получения документации НСПК.

## 3. Процедура фиксации

1. Ревью аддитивных изменений на гейте A1 (контракт ТСП) и в рамках расширения RFP (контракт адаптера).
2. Контрактный тест совместимости: прогон v0.1-клиента против v0.2 API — неизменно; проверка отсутствия изменений в `required`/существующих enum.
3. `docs/contracts/tsp-api.md` и `openapi/tsp-api.yaml` версионируются синхронно; при последующих ломающих изменениях — `/v2` (период поддержки ≥ 6 мес, §6).
