# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).
- Изменение (proposed): **`changes/sbp-subscriptions/`** — рекуррентные C2B-списания (СБП-подписки) по согласию плательщика; маршрут **Critical** (10/15), решение — `docs/adr/ADR-008`, ожидает A3, затем передаётся исполнителям (`changes/sbp-subscriptions/HANDOFF.md`).

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
  adr/ADR-001..008.md        архитектурные решения
openapi/
  tsp-api.yaml               контракт API ТСП (v0.2.0 — аддитивно)
changes/
  sbp-subscriptions/         Proposed: рекуррентные C2B-списания (дельта, ADR-008, impact, contracts, handoff)
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton)
```
