# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..008`, `ARCHITECTURE-SPINE.md`.
- Статус: базовое решение подготовлено; стратегия реализации A3 (ADR-007, hybrid) **принята 2026-08-15**. Изменение «СБП-подписки» (рекуррентные C2B-списания, ADR-008) — в статусе **proposed**, ожидает решения A3: `changes/sbp-recurring-subscriptions/`. Документация НСПК (протокол участника) — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`.

## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-008
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps
  nfr.md                     измеримые NFR
  contracts/tsp-api.md       контракт API ТСП v0.1 (мерчант-API)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.1 (ядро ↔ транспорт; основа RFP)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  spec/mandate-lifecycle.md  жизненный цикл мандата/подписки (ADR-008)
  adr/ADR-001..008.md        архитектурные решения
changes/sbp-recurring-subscriptions/  пакет изменения «СБП-подписки» (proposed, ждёт A3)
  DELTA.md                   дельта-спека (ADDED/MODIFIED/REMOVED, откат, приёмка)
  SIGNIFICANCE.md            оценка значимости и маршрута
  IMPACT.md                  влияние на инварианты принятого решения
  HUMAN-DECISIONS.md         что остаётся решить человеку
  handoff/                   handoff-пакет исполнителям (после A3)
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton)
```
