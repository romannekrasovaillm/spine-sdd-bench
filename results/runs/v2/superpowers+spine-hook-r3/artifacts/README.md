# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15; заявленный маршрут закрепляется в `.arch-handoff/ROUTE.lock` после A3 — см. `docs/solutioning-subscriptions.md` §1).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..009`, `ARCHITECTURE-SPINE.md`.
- Статус: базовое решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).
- Расширение: **подписки СБП** (рекуррентные C2B-списания по согласию плательщика) — `docs/solutioning-subscriptions.md`, ADR-008/ADR-009, дельта `changes/spb-subscriptions/DELTA.md`; значимость 8/15 (Critical), **ожидает решения A3**.

## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-011 (AD-009..011 — подписки, Proposed)
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps
  solutioning-subscriptions.md  расширение: подписки СБП (значимость, влияние, откат, A3)
  nfr.md                     измеримые NFR (+ §7 подписки)
  contracts/tsp-api.md       контракт API ТСП v0.2 (мерчант-API; + согласия)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.1 (ядро ↔ транспорт; основа RFP)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты
  spec/subscription-consent.md  согласие плательщика: состояния, лимиты, дебет, отзыв
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  adr/ADR-001..009.md        архитектурные решения
changes/spb-subscriptions/   дельта (OpenSpec-протокол): ADDED/MODIFIED/REMOVED, откат, приёмка
openapi/tsp-api.yaml         машиночитаемый контракт API ТСП 0.2.0
.arch-handoff/               handoff-пакет кодовому харнессу (перегенерируется после A3)
```
