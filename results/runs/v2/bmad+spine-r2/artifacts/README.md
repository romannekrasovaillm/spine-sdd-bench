# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..010`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).

## Расширение: Подписки СБП (рекуррентные C2B-списания)

Поверх принятого решения подготовлено изменение «Подписки СБП» — рекуррентные списания по согласию плательщика (ТСП: онлайн-кинотеатры, ЖКХ, связь).

- Значимость: **Critical (11/15)** — новая граница безопасности, финансовое влияние, КИИ.
- Пакет изменения: `changes/subscriptions-c2b/` (`DELTA.md` — дельта OpenSpec, `IMPACT.md`), `PROBLEM.md`, `RISK.md`, `ACCEPTANCE.md`, `ROLLBACK.md`, `DECISION.md` (A3, ожидает человека), `WALKING-SKELETON.md`, `VALIDATION.md`, `docs/SPEC.md`, `docs/REVIEW.md`, `EVIDENCE.yaml`.
- Новые решения: `docs/adr/ADR-008..010`; новые инварианты: `AD-009`, `AD-010`; спецификация: `docs/spec/subscription-state-machine.md`; NFR: `docs/nfr.md` §7.
- Контракты: `openapi/tsp-api.yaml` v0.2 (аддитивно, breaking: 0), `docs/contracts/opkc-adapter.md` v0.2 (основа RFP).

## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-010
PROBLEM.md, RISK.md          проблема/цель и оценка значимости изменения «Подписки СБП»
ACCEPTANCE.md, ROLLBACK.md   критерии приёмки и план отката
DECISION.md                  запись A3 (подписывает человек)
WALKING-SKELETON.md, VALIDATION.md   сквозной скелет и план валидации
EVIDENCE.yaml                evidence bundle маршрута Critical
changes/
  subscriptions-c2b/         дельта OpenSpec (propose) + оценка влияния
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты
  SPEC.md                    спецификация изменения «Подписки СБП» (EARS)
  nfr.md                     измеримые NFR (в т.ч. §7 — подписки)
  REVIEW.md                  состязательное ревью изменения
  contracts/tsp-api.md       контракт API ТСП v0.2 (мерчант-API)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.2 (ядро ↔ транспорт; основа RFP)
  spec/state-machine.md      статусная машина платежа
  spec/subscription-state-machine.md  статусная машина подписки/списания
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ
  adr/ADR-001..010.md        архитектурные решения
openapi/tsp-api.yaml         контракт API ТСП v0.2.0
.arch-handoff/               handoff-пакет кодовому харнессу (walking skeleton)
reports/fitness.md           отчёт архитектурного контроля
```
