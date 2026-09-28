# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..011`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).
- Изменение «Рекуррентные C2B-списания (подписки СБП)»: пакет — `changes/sbp-recurring-consents/` (дельта + дизайн + ADR-008..011 + критерии/откат/ревью); маршрут **Critical**, ожидает A3 по ADR-011 (правило отзыва согласия) и документации НСПК.

## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-009
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps
  nfr.md                     измеримые NFR
  contracts/tsp-api.md       контракт API ТСП v0.2 (мерчант-API; рекуррентные согласия)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.1 (ядро ↔ транспорт; основа RFP)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты
  spec/consent-state-machine.md  статусная машина согласия (рекуррентные списания)
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  adr/ADR-001..011.md        архитектурные решения
openapi/tsp-api.yaml         контракт OpenAPI API ТСП v0.2
changes/sbp-recurring-consents/  пакет изменения: DELTA, SOLUTION, RISK, ACCEPTANCE, ROLLBACK, REVIEW, HANDOFF, TASK, EVIDENCE
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton)
```

