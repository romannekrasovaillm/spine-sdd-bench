# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..009`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).
- **Изменение в работе — «Подписки СБП» (рекуррентные C2B по согласию плательщика)**: пакет на архитектурное решение в `openspec/changes/sbp-subscriptions/` + `changes/sbp-subscriptions/DELTA.md`, решения ADR-008/ADR-009 (Proposed), инварианты AD-009…AD-011 (Proposed). Ждёт A3.

## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-011
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps
  nfr.md                     измеримые NFR
  nfr-subscriptions.md       NFR подписок (предложение, ждёт вливания)
  contracts/tsp-api.md       контракт API ТСП v0.2 (мерчант-API)
  contracts/subscriptions-api.md  контракт подписок СБП (мандаты, подписки, списания)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.2 (ядро ↔ транспорт; основа RFP)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты
  spec/subscriptions.md      машины мандата/подписки/списания, приёмка, риски
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  adr/ADR-001..007.md        архитектурные решения (принятое решение)
  adr/ADR-008, ADR-009.md    решения изменения «подписки» (Proposed, ждут A3)
openapi/tsp-api.yaml         машинный контракт API ТСП (v0.2, аддитивное расширение)
openspec/changes/sbp-subscriptions/  change: proposal + specs + design + tasks
changes/sbp-subscriptions/DELTA.md   дельта изменения (ADDED/MODIFIED/REMOVED, откат, приёмка)
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton)
```
