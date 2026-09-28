# Отчёт fitness-контроля — sbp-recurring-c2b

Источник: `.arch-handoff/CONSTRAINTS.yaml` (13 правил), гейт `arch-be gate`, проверка зубов `arch-be rules template verify`.

## Итог гейта (авто-маршрут)

```
arch-be gate --route auto --base bench-baseline
  [PASS] fitness — Правил: 13, нарушений: 0 (error: 0, warn: 0)
  [PASS] delta_guard — защищённый ARCHITECTURE-SPINE.md покрыт дельтой 'sbp-recurring-c2b'
  [PASS] rule_weakened — реестр не ослаблен относительно bench-baseline
  [PASS] spine_lint — находок: 0
Итог: PASS
```

Полный вывод — `evidence/gate.txt`.

## Итог гейта (заявленный маршрут Critical)

Runnable-составляющие PASS (fitness, delta_guard, rule_weakened, spine_lint, sensors). Итог `INCOMPLETE` — обязательные для Critical составляющие без входа: `trace_check`, `nfr`, `model_validate` (нет каталога типизированной модели `model/`), `evidence_verify` (bundle неполон на стадии решения). Полный вывод — `evidence/gate-critical.txt`.

## Правила, проверяющие поведение

| id | правило | инвариант | результат |
|---|---|---|---|
| C-100 | `consent_before_auto_action` | AD-009/AD-010 | PASS; на нарушающей реализации — FAIL (зубы есть) |
| C-101 | `debit_period_idempotency` | AD-003/AD-011 | PASS (проверка зубов шаблона — в `evidence/rules-verify-all.txt`) |
| C-102…C-105 | трассируемость NFR/спеки/контракта | AD-009/AD-010 | PASS |

## Ограничения

- Проверка C-100/C-101 выполняется на эталонной реализации шаблона (`skeleton/rule_templates/`), а не на коде сервиса: кода ещё нет (стадия решения). При реализации — перенести команды правил на код шлюза (`fix_hint` в CONSTRAINTS.yaml).
- Типизированная модель `model/` отсутствует → трассировка REQ→NFR→AD→правило проверяется прозой (`docs/solutioning-subscriptions.md` §8), а не `trace_check`/`nfr_check`. Решение о бутстрапе модели — за архитектором.
- `arch-be rules template verify --dir .` для C-101 даёт «пропуск: адаптирован» (имя правила не совпадает с ожидаемым шаблоном): проверка зуба самого шаблона `idempotency-key` выполнена отдельно (`evidence/rules-verify-all.txt`).
