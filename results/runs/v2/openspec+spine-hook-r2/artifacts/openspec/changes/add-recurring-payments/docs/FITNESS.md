# Fitness Report — add-recurring-payments

Итог: PASS (гейт `arch-be gate --route auto --base bench-baseline`; нарушений 0, правил 13)

## Вердикт гейта

- `arch-be gate --route auto --base bench-baseline` → **PASS**
  - fitness — правил: 13, нарушений: 0 (error: 0, warn: 0), отпечаток реестра `09f88f98`;
  - delta_guard — защищённых правок: 1 (`ARCHITECTURE-SPINE.md`), покрытие дельтой `add-recurring-payments`;
  - rule_weakened — реестр правил не ослаблен относительно `bench-baseline`;
  - spine_lint — находок 0;
  - trace_check / model_validate — SKIP (типизированная модель `model/` в кейсе не заведена).

## Правила, закрывающие новые инварианты

| id | Правило | Тип | Закрывает |
|---|---|---|---|
| C-020 | `recurring-only-active-consent` | must_contain (`ARCHITECTURE-SPINE.md` = `AD-009`) | AD-009 (списание только по `ACTIVE`-согласию) |
| C-021 | `recurring-no-double-period` | must_contain (`periodKey`) | AD-010 (ключ периода) |
| C-022 | `spine-ad-010-present` | must_contain (`AD-010`) | AD-010 присутствует в спайне |
| C-023 | `adr-008-present` | file_exists | ADR-008 (мандат) |
| C-024 | `nfr-recurring-measurable` | must_contain (`docs/nfr.md` = «Рекуррентные списания») | NFR §7 |
| C-025 | `contract-consents-path` | must_contain (`openapi/tsp-api.yaml` = `/v1/consents`) | контракт согласий |

## Существующие правила (не ослаблены)

`adr-set-complete`, `spine-present`, `nfr-measurable` (99,95), `abs-credit-only-from-paid` (`только из состояния PAID`), `adr-no-placeholders`, `readme-exists`, `spine-lints-clean`.

## Что механика НЕ проверяет (граница доверия)

- Поведенческие свойства (идемпотентность, отсутствие двойного списания, блокировка после отзыва, гонка) — правила выше проверяют **наличие инварианта в спайне**, а не его исполнение в коде. Исполнимые проверки поведения заводятся на A4 (`rule_template_apply`) и на walking skeleton — см. `ACCEPTANCE.md` AC-04/AC-06/AC-13/AC-15/AC-16.
- Рекомендация на A4: применить шаблоны исполняемых правил (property-тест на фейке + нарушающая реализация + проверка «зубов») к AD-009/AD-010.
