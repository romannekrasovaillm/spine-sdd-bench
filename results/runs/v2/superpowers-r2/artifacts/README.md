# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).

## Изменение: подписки СБП (рекуррентные C2B-списания)

Запрос ТСП на рекуррентные списания по согласию плательщика оформлен поверх принятого решения (маршрут **Critical**, значимость 10/15) и **ожидает человеческого решения A3**:

- `docs/solutioning-sbp-subscriptions.md` — полный Solutioning изменения (значимость/маршрут, влияние на AD-001..008, компоненты, потоки, гейты, gaps, что остаётся человеку).
- `docs/adr/ADR-008..010` — Proposed: модель авторизации и оркестрация, согласие/ПДн/отзыв, идемпотентность и неопределённый исход.
- `changes/sbp-subscriptions/` — дельта изменения (`DELTA.md`), `RISK.md`, `ACCEPTANCE.md`, `ROLLBACK.md`, `ADR.md`, `DECISION.md` (A3-пакет), `HANDOFF.md` (epic-context для исполнителей).
- Контракты: `openapi/tsp-api.yaml` и `docs/contracts/tsp-api.md` §8 (v0.2, аддитивно, breaking = 0), `docs/contracts/opkc-adapter.md` (операции сервиса мандатов), `docs/spec/subscriptions.md` (автомат мандата), `docs/nfr.md` §7, `docs/rfp/vendor-rfp.md` (G8, POC P9–P11).
- Spine: AD-009..AD-011 (Proposed).

## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-011 (AD-001..008 приняты; AD-009..011 Proposed)
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps
  solutioning-sbp-subscriptions.md  Solutioning изменения (подписки СБП)
  nfr.md                     измеримые NFR (+ §7 подписки)
  contracts/tsp-api.md       контракт API ТСП v0.2 (мерчант-API; v0.2 — подписки, аддитивно)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.2 (ядро ↔ транспорт; основа RFP)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты
  spec/subscriptions.md      автомат мандата (согласия) и допуск списания
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  adr/ADR-001..010.md        архитектурные решения (ADR-008..010 — подписки, Proposed)
changes/sbp-subscriptions/   дельта изменения: DELTA.md, RISK.md, ACCEPTANCE.md, ROLLBACK.md, ADR.md, DECISION.md, HANDOFF.md
openapi/tsp-api.yaml         контракт API ТСП v0.2 (OpenAPI)
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton)
```
