# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..008`, `ARCHITECTURE-SPINE.md`.
- Статус: базовое решение принято (A3 от 2026-08-15 по стратегии реализации, ADR-007 Accepted, AD-008 [ADOPTED]).
- Изменение поверх решения: **подписки СБП** (рекуррентные C2B-списания по согласию плательщика) — `openspec/changes/add-sbp-subscriptions/` (proposal, design, spec, tasks), `docs/adr/ADR-008-…` (Proposed), дельта спайна `changes/add-sbp-subscriptions/DELTA.md`, инварианты AD-009/AD-010 (Proposed). Маршрут изменения — **Critical**, **ожидает человеческого решения A3** по ADR-008 и получения документации НСПК по сервису подписок (внешний вход, `[ТРЕБУЕТ ПРОВЕРКИ]`).

## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-010 (AD-009/AD-010 — Proposed по ADR-008)
changes/
  add-sbp-subscriptions/     дельта спайна к изменению «подписки СБП» (правки защищённых файлов)
openspec/
  changes/add-sbp-subscriptions/  пакет изменения: proposal, design, specs/sbp-subscriptions, tasks
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps; §11 — изменение «подписки СБП»
  nfr.md                     измеримые NFR (цели; §7 — подписки СБП)
  contracts/tsp-api.md       контракт API ТСП v0.2 (мерчант-API)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.2 (ядро ↔ транспорт; основа RFP)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты (§7 — мандат и списания)
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  adr/ADR-001..008.md        архитектурные решения (ADR-008 — Proposed, подписки СБП)
openapi/tsp-api.yaml         контракт API ТСП (OpenAPI 3.0.3, 0.2.0 draft)
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton, базовый scope)
```
