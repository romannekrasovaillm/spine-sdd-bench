# Validation Evidence — add-recurring-payments

Итог: PASS (все прогоны ниже пройдены; поведенческие проверки — на A4)

Прогоны контура контроля на момент упаковки бандла (2026-09-28).

## Структурная валидация спецификации

- `openspec validate add-recurring-payments --strict` → `valid: true`, issues `[]` (PASS).
- `openspec status --change add-recurring-payments` → артефакты proposal/specs/design/tasks созданы.

## Архитектурный контроль (arch-be)

- `arch-be control check .` → **PASS** — правил 13, нарушений 0 (error: 0, warn: 0); состав правил не ослаблен относительно baseline.
- `arch-be control spine ARCHITECTURE-SPINE.md` → нарушений нет (дубли AD-id, пустые Binds/Prevents/Rule, заглушки — нет).
- `arch-be delta validate add-recurring-payments` → нарушений нет (секции ADDED/MODIFIED/REMOVED, EARS, без заглушек).
- `arch-be delta guard --base bench-baseline` → PASS — защищённая правка `ARCHITECTURE-SPINE.md` покрыта дельтой `add-recurring-payments`.
- `arch-be gate --route auto --base bench-baseline` → **PASS** (аттестация вердикта sha256).
- `arch-be control sensors openspec/changes/add-recurring-payments/specs` → PASS.

## Контракт

- `openapi_lint openapi/tsp-api.yaml` → **PASS** (error: 0, warn: 0).
- `contract_diff` v0.1 → v0.2 (`openapi`) → **PASS**, изменений 6, **breaking: 0**, non-breaking: 6 (все — добавленные пути CD-005). Совместимость существующих потребителей подтверждена.

## Значимость и маршрут

- `arch-be control score` (заявленные триггеры) → **Score 9 → маршрут Critical**: api_contract_change, consistency_model_change, criticality_or_exception, cross_domain_integration, data_contract_change, financial_impact, new_component, security_boundary_change, significant_nfr.
- `arch-be control score --from-diff` (механический пол) → 1 (api_contract_change) → Fast. **Расхождение зафиксировано**: механический детектор диффа не видит новые инварианты/NFR/consent как триггеры; маршрут определяется заявленной оценкой архитектора (Critical).

## Ограничение

Проверки выполнены на уровне документа/контракта (решение до кода). Поведенческие fitness-тесты (идемпотентность, двойное списание, отзыв) относятся к A4 и выполняются на walking skeleton — см. `ACCEPTANCE.md`, `tasks.md`.
