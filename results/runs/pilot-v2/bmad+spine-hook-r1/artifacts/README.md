# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).

## Изменение: рекуррентные C2B-списания (подписки СБП)

Пакет изменения поверх принятого решения (на архитектурное решение A3 → handoff исполнителям):

- `changes/sbp-recurrent-c2b/DELTA.md` — дельта изменения истины (ADDED/MODIFIED/REMOVED, план отката, критерии).
- `docs/adr/ADR-008-...md` — архитектурное решение (согласие как ресурс, истина у ОПКЦ, списание — обычный платёж).
- `docs/solutioning-subscriptions.md` — полный Solutioning addendum (модель, потоки, альтернативы, влияние на инварианты).
- Инварианты **AD-009, AD-010** (Proposed) в `ARCHITECTURE-SPINE.md`; контракт ТСП **v0.2** аддитивно (`openapi/tsp-api.yaml`, `docs/contracts/tsp-api.md`); NFR §7 в `docs/nfr.md`.
- Evidence-пакет гейта: `docs/PROBLEM.md`, `docs/SPEC.md`, `docs/RISK.md`, `docs/ACCEPTANCE.md`, `docs/ROLLBACK.md`, `docs/DECISION.md`, `docs/WALKING-SKELETON.md`, `docs/REVIEW.md`, `docs/VALIDATION.md`, `reports/fitness.md`, `EVIDENCE.yaml`.
- Handoff исполнителям: `.arch-handoff/TASK-subscriptions.md`.

## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-010 (AD-009/AD-010 — Proposed, ADR-008)
changes/sbp-recurrent-c2b/   дельта изменения (подписки СБП): DELTA.md, PROPOSAL.md
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps
  nfr.md                     измеримые NFR
  contracts/tsp-api.md       контракт API ТСП v0.2 (мерчант-API)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.2 (ядро ↔ транспорт; основа RFP)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  adr/ADR-001..008.md        архитектурные решения
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton)
```
