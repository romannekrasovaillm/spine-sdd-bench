# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..008`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, стратегия реализации принята (ADR-007 Accepted, A3 от 2026-08-15); ожидается получение документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).
- Изменение **CHG-001 (подписки СБП, рекуррентные списания)**: `docs/changes/CHG-001-sbp-subscriptions.md`, `docs/adr/ADR-008-sbp-podpiski-mandaty-rekurrentnye-spisaniya.md`, `docs/spec/mandate-state-machine.md`; схема — AD-009/AD-010, контракт API ТСП v0.2. Выносится на архитектурное решение (гейт A3′, см. CHG-001 §7).

## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-010
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps
  nfr.md                     измеримые NFR (в т.ч. §7 — подписки)
  changes/CHG-001-…md        пакет изменения: подписки СБП (рекуррентные списания)
  contracts/tsp-api.md       контракт API ТСП v0.2 (мерчант-API; v0.1 → v0.2 аддитивно)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.1 (ядро ↔ транспорт; основа RFP)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты
  spec/mandate-state-machine.md  статусная машина мандата и дебета (CHG-001)
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  adr/ADR-001..008.md        архитектурные решения
openapi/tsp-api.yaml         OpenAPI контракта API ТСП v0.2.0
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton)
  changes/CHG-001-subscriptions/  дельта handoff по подпискам (после ратификации ADR-008)
```
