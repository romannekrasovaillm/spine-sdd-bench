# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).

## Изменение «Подписки СБП» (рекуррентные C2B-списания)

Пакет изменения поверх принятого решения (Critical, 9/15; ADR-008 — **ожидает A3**):

- `changes/sbp-recurring-subscriptions/DELTA.md` — дельта (ADDED/MODIFIED/REMOVED, откат, приёмка);
- `changes/sbp-recurring-subscriptions/handoff/` — handoff-пакет исполнителям (TASK, epic-context, CONSTRAINTS, RUBRIC, ADR);
- `docs/adr/ADR-008-*.md` — решение (согласие плательщика как первоклассная сущность);
- `docs/solutioning-subscriptions.md` — влияние на архитектуру, потоки, NFR §7, приёмка, откат, вопросы A3;
- `docs/spec/subscriptions.md` — статусная машина согласия;
- `openapi/tsp-api.yaml` v0.2.0 — аддитивное расширение (0 breaking), `docs/contracts/tsp-api.md` §6;
- спайн: AD-009, AD-010; правила — `.arch-handoff/CONSTRAINTS.yaml`.

## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-010
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps
  solutioning-subscriptions.md  изменение «подписки СБП»: влияние, потоки, приёмка, откат
  nfr.md                     измеримые NFR (§7 — рекуррентные списания)
  contracts/tsp-api.md       контракт API ТСП v0.2 (мерчант-API; §6 — подписки)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.1 (ядро ↔ транспорт; consent-операции)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты
  spec/subscriptions.md      статусная машина согласия плательщика (подписки)
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  adr/ADR-001..008.md        архитектурные решения
openapi/tsp-api.yaml         машиночитаемый контракт API ТСП v0.2.0
changes/sbp-recurring-subscriptions/  дельта изменения + handoff-пакет исполнителям
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton)
```
