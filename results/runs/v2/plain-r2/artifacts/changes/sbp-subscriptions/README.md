# Изменение `sbp-subscriptions` — архитектурный пакет (рекуррентные C2B-списания)

- Status: **Proposed** — выносится на архитектурное решение (A3). Реализация не начинается до A3 и документации НСПК.
- Route: **Critical** (значимость 7/15 триггеров) — обоснование ниже и в `docs/adr/ADR-008-...md` §Значимость.
- Способ изменения принятого решения: **дельта** `changes/sbp-subscriptions/DELTA.md` (propose → apply → archive), защищённые файлы объявлены в ней (delta guard).
- Решение: `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md`.
- Передача исполнителям (после A3): `changes/sbp-subscriptions/handoff/`.

## 1. Оценка значимости и маршрута

`arch control score` → **Score 7 → маршрут Critical**. Триггеры:

| Триггер | Почему |
|---|---|
| `new_component` | новый домен «согласие» + планировщик списаний |
| `api_contract_change` | расширение `openapi/tsp-api.yaml` до v0.2 |
| `data_contract_change` | новая сущность согласия, новые ПДн-данные, новые таблицы |
| `cross_domain_integration` | согласие ↔ платежи ↔ АБС ↔ транспорт ОПКЦ |
| `significant_nfr` | новые измеримые NFR (срок списания, дубликаты, отзыв) |
| `financial_impact` | новый класс движения денег; риск двойного списания/списания без согласия |
| `criticality_or_exception` | платёжный/КИИ-контур; форсирует Critical |

**Вывод о глубине проектирования.** Требуется полный Solutioning (spine + ADR + NFR) и обязательная человеческая точка A3 — не Fast/Standard, не одна дельта. Причины: финансовое влияние, новая долгоживущая доменная сущность, ПДн/152-ФЗ, внешний вход НСПК, изменение контракта и зависимость от контракта вендора (ADR-007/AD-008).

## 2. Влияние на принятую архитектуру

| Инвариант | Влияние | Суть |
|---|---|---|
| AD-001 изоляция контура | не меняется | согласие и планировщик — в платёжном контуре |
| AD-002 единый источник истины | **расширяется** | согласие — вторая статусная машина; атомарность «статус + outbox + аудит» сохраняется |
| AD-003 идемпотентность | **расширяется** | ключи `consentId`, `consentId + billingPeriod` |
| AD-004 единственный адаптер ОПКЦ | набор расширяется | подписочные операции внутри того же адаптера; Rule не меняется |
| AD-005 зачисление только из `PAID` | **подтверждается** | `ACTIVE`-согласие — основание инициации, не зачисления |
| AD-006 trust-зоны | не меняется | новой границы доверия нет |
| AD-007 НПС/КИИ/ПДн | **расширяется** | согласие — ПДн; отзыв и аудит обязательны |
| AD-008 стратегия (гибрид) [ADOPTED] | не меняется; **новая зависимость** | addendum к контракту вендора на подписочные операции — решение человека |

Новый инвариант: **AD-009 (Proposed)** в `ARCHITECTURE-SPINE.md`.

## 3. Состав пакета и соответствие требованиям задания

| # | Что требовалось | Где лежит |
|---|---|---|
| 1 | Оценка значимости и маршрута | §1 этого файла; ADR-008 §Значимость; `arch control score` |
| 2 | Влияние на принятые инварианты | §2 этого файла; ADR-008 §Влияние; `ARCHITECTURE-SPINE.md` (AD-009, Binds, версии) |
| 3 | Архитектурное решение: альтернативы, последствия, обратимость | `docs/adr/ADR-008-...md` (A3-пакет, Alternatives, Consequences, Reversibility) |
| 4 | Изменения контрактов без поломки потребителей | `openapi/tsp-api.yaml` (v0.2.0, аддитивно), `docs/contracts/tsp-api.md` §4; проверка `arch contract-diff` |
| 5 | Измеримые NFR | `docs/nfr.md` §«Подписки СБП»; ADR-008 §NFR |
| 6 | Критерии приёмки и план отката | ADR-008 §Критерии/§План отката; `DELTA.md` §Критерии/§План отката; `handoff/ROLLBACK.yaml` |
| 7 | Что остаётся человеку-архитектору | ADR-008 §На решение человека-архитектора |

## 4. Живая истина, которая меняется при `apply`

- `ARCHITECTURE-SPINE.md` — AD-009, Binds AD-002/AD-003, «Контракты и версии» (TSP API v0.2).
- `docs/adr/ADR-008-...md` — ADDED.
- `docs/spec/state-machine.md` — машина согласия + переходы списания.
- `docs/contracts/tsp-api.md`, `openapi/tsp-api.yaml` — API подписок (аддитивно).
- `docs/contracts/opkc-adapter.md`, `docs/rfp/vendor-rfp.md` — подписочные операции транспорта.
- `docs/nfr.md`, `docs/solutioning.md` — NFR, область scope/roadmap, обязательные секции сенсора.
- `.arch-handoff/CONSTRAINTS.yaml` — fitness-правила подписок.
- `README.md` — статус и ссылка на пакет.

## 5. Проверки пакета (гейты)

```bash
arch control score --trigger new_component=true --trigger api_contract_change=true \
  --trigger data_contract_change=true --trigger cross_domain_integration=true \
  --trigger significant_nfr=true --trigger financial_impact=true \
  --trigger criticality_or_exception=true          # → Critical
arch delta validate sbp-subscriptions              # структура дельты
arch delta guard                                   # защищённые файлы объявлены
arch control check .                               # fitness, включая новые правила подписок
arch contract-diff <old.yml> openapi/tsp-api.yaml  # нет ломающих изменений
arch control sensors docs                          # обязательные секции
```
