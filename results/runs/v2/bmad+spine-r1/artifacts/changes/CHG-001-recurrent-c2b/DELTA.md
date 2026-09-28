# DELTA — CHG-001: Рекуррентные C2B-списания (подписки СБП)

- Изменение: CHG-001-recurrent-c2b
- Дата: 2026-09-28
- Статус: **Proposed** (ожидает человеческого решения A3)
- Маршрут: **Critical** (значимость 11/15; см. `SIGNIFICANCE.md`)
- Основание: бизнес-запрос ТСП (онлайн-кинотеатры, ЖКХ, связь) на рекуррентные списания по согласию плательщика
- Владелец: solution-architect (платёжный контур)
- Связанные документы: `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp-mandat-platelshchika.md`, `SIGNIFICANCE.md`, `IMPACT.md`, `CONTRACT-DELTA.md`, `NFR-DELTA.md`, `ACCEPTANCE.md`, `OPEN-QUESTIONS.md`

## 1. Намерение (propose)

Добавить в принятое решение «Платёжный шлюз СБП (C2B-приём)» поддержку **рекуррентных C2B-списаний по мандату плательщика** (подписки СБП), не вводя второго платёжного контура и не ломая существующих потребителей контракта. Изменение описывается как дельта относительно текущей истины; после решения A3 — apply, затем archive (влитие в живые источники).

## 2. Дельта

### ADDED

- **Spine-инварианты** (Proposed): `AD-009` (мандат — единственное основание списания), `AD-010` (списание — идемпотентная платёжная операция), `AD-011` (отзыв немедленно запрещает списания), `AD-012` (расписание и исполнение — прослеживаемый источник истины).
- **ADR-008** (Proposed): решение о модели подписок/мандатов; альтернативы, последствия, обратимость, черновик A3.
- **Контракт API ТСП**: пути `/v1/subscriptions` (POST/GET), `/v1/subscriptions/{subscriptionId}` (GET), `/v1/subscriptions/{subscriptionId}/cancel` (POST), `/v1/subscriptions/{subscriptionId}/charges` (GET), `/v1/charges/{chargeId}` (GET); схемы `SubscriptionRequest`, `Subscription`, `Charge`, `Problem`.
- **Правила CONSTRAINTS.yaml**: `recurrence-mandate-basis`, `recurrence-idempotent-charge`, `recurrence-no-double-charge`, `recurrence-contract-subscriptions`, `recurrence-nfr-measurable`.

### MODIFIED

- **ARCHITECTURE-SPINE.md** (применено сейчас): `AD-001.Binds` += «сервис подписок (мандаты), планировщик списаний»; `AD-003.Binds` += «списания подписки (`subscriptionId` + `billingPeriod`)»; `AD-004.Binds` += «события подписок ОПКЦ»; раздел «Контракты и версии» — контракт API ТСП `0.1 → 0.2` (аддитивно).
- **openapi/tsp-api.yaml** (применено сейчас): `info.version 0.1.0 → 0.2.0`; добавлены пути и схемы. Существующие операции `/v1/payments*` и схемы `PaymentRequest`/`Payment` **не изменены**. Доказано `contract_diff`: breaking = 0.
- **.arch-handoff/CONSTRAINTS.yaml** (применено сейчас): добавлены 5 правил (только добавление, без ослабления существующих).
- **docs/solutioning.md** (отложено до archive): «автоплатежи» переносятся из вне-scope в scope; в C4 добавляется сервис подписок/мандатов и планировщик; добавляется поток периодического списания.
- **docs/spec/state-machine.md** (отложено до archive): добавляется автомат мандата/подписки и реестр `charges`; связь `charge → paymentId`.
- **docs/contracts/tsp-api.md** (отложено до archive): раздел подписок, новые коды ошибок (`MANDATE_NOT_ACTIVE`, `SUBSCRIPTION_REVOKED`, `SUBSCRIPTION_NOT_CANCELLABLE`), события `subscription.*`.
- **docs/contracts/opkc-adapter.md** (отложено до archive): рекуррентные операции/события к контракту адаптера (основа RFP).
- **docs/nfr.md** (отложено до archive): NFR подписок из `NFR-DELTA.md`.

### REMOVED

- Из перечня вне-scope / Deferred выводится пункт «автоплатежи» (первые рекуррентные списания) — переводится в scope настоящим изменением. Иные пункты (C2C, выплаты, диспуты, мультивалютность) остаются вне scope без изменений.

## 3. Защищённые пути (delta_guard)

Дельта покрывает прямые правки защищённых артефактов:

- `ARCHITECTURE-SPINE.md` — ADDED `AD-009`..`AD-012`; MODIFIED `Binds` блоков `AD-001`, `AD-003`, `AD-004`, раздел «Контракты и версии».
- `.arch-handoff/CONSTRAINTS.yaml` — ADDED 5 правил.

Иных правок защищённых путей настоящая дельта не предполагает.

## 4. Границы изменения (что НЕ входит)

- Реальный протокол НСПК не реализуется: рекуррентный протокол — внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`, интеграция только через адаптер ОПКЦ (AD-008).
- C2C/выплаты, диспуты, мультивалютность — без изменений.
- Смена модели зачисления (AD-005) и модели денежного автомата (ADR-002) — не входит.

## 5. Цикл

1. **propose** — этот файл, `ADR-008` (Proposed), черновики контракта/NFR/приёмки. Гейты: `spine_lint`, `fitness_check`, `openapi_lint`, `contract_diff`, `delta_guard`.
2. **apply** — после человеческого решения A3: реализация по `ACCEPTANCE.md`, handoff-пакет перегенерируется (этап реализации).
3. **archive** — MODIFIED-документы вливаются в живую истину; дельта получает статус `archived`.
