# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).
- **Предложенное изменение «СБП-подписки»** (рекуррентные списания по согласию плательщика, значимость 7/15, Critical): `changes/sbp-subscriptions/` (DELTA + Solutioning), `docs/adr/ADR-008-sbp-subscriptions-mandates-scheduler.md`, инвариант `AD-009`, `docs/spec/subscription-model.md`, API ТСП v0.2 (`openapi/tsp-api.yaml`). Ожидает человеческого решения A3′ — не проведено в жизнь до ответа архитектора.

## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-009
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps
  nfr.md                     измеримые NFR
  contracts/tsp-api.md       контракт API ТСП v0.2 (мерчант-API; 0.2 — подписки, ADR-008)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.2 (ядро ↔ транспорт; основа RFP; §10 — мандаты)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты
  spec/subscription-model.md модель мандата и рекуррентных списаний (ADR-008, AD-009)
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  adr/ADR-001..008.md        архитектурные решения (008 — предложенное изменение «СБП-подписки»)
changes/sbp-subscriptions/   дельта изменения: DELTA.md + design.md (Solutioning)
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton)
```
