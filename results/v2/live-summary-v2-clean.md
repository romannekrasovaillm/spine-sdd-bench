# Живой прогон v2: стек × режим Spine

Прогонов: 36; исключение загрязнённых: да.

| стек | Spine | n | solution_architecture | architecture_gates | adr_quality | macedo_dimensions | neutral_architecture | PASS_DELTA | PASS_UNTOUCHED | FAIL |
|---|---|---|---|---|---|---|---|---|---|---|
| plain | — | 3 | — | — | — | — | — | 2/3 | 0/3 | 1/3 |
| plain | spine | 3 | 3.35 | 2.30 | — | — | 3.67 | 3/3 | 0/3 | 0/3 |
| plain | spine-hook | 3 | — | — | — | — | — | 3/3 | 0/3 | 0/3 |
| openspec | — | 3 | 3.53 | 3.00 | — | — | 3.00 | 1/3 | 1/3 | 1/3 |
| openspec | spine | 3 | 3.74 | 3.40 | — | — | 3.89 | 3/3 | 0/3 | 0/3 |
| openspec | spine-hook | 3 | — | — | — | — | — | 2/3 | 1/3 | 0/3 |
| bmad | — | 3 | 3.55 | 3.10 | — | — | 3.78 | 1/3 | 0/3 | 2/3 |
| bmad | spine | 3 | — | — | — | — | — | 3/3 | 0/3 | 0/3 |
| bmad | spine-hook | 3 | — | — | — | — | — | 3/3 | 0/3 | 0/3 |
| superpowers | — | 3 | — | — | — | — | — | 2/3 | 0/3 | 1/3 |
| superpowers | spine | 3 | — | — | — | — | — | 3/3 | 0/3 | 0/3 |
| superpowers | spine-hook | 3 | — | — | — | — | — | 3/3 | 0/3 | 0/3 |

## Эффект Spine внутри стека (непарно, bootstrap 95% CI, перестановочный p)

- solution_architecture: plain+spine − plain: n<2 — не оценимо
- solution_architecture: plain+spine-hook − plain: n<2 — не оценимо
- solution_architecture: openspec+spine − openspec: n<2 — не оценимо
- solution_architecture: openspec+spine-hook − openspec: n<2 — не оценимо
- solution_architecture: bmad+spine − bmad: n<2 — не оценимо
- solution_architecture: bmad+spine-hook − bmad: n<2 — не оценимо
- solution_architecture: superpowers+spine − superpowers: n<2 — не оценимо
- solution_architecture: superpowers+spine-hook − superpowers: n<2 — не оценимо
- architecture_gates: plain+spine − plain: n<2 — не оценимо
- architecture_gates: plain+spine-hook − plain: n<2 — не оценимо
- architecture_gates: openspec+spine − openspec: n<2 — не оценимо
- architecture_gates: openspec+spine-hook − openspec: n<2 — не оценимо
- architecture_gates: bmad+spine − bmad: n<2 — не оценимо
- architecture_gates: bmad+spine-hook − bmad: n<2 — не оценимо
- architecture_gates: superpowers+spine − superpowers: n<2 — не оценимо
- architecture_gates: superpowers+spine-hook − superpowers: n<2 — не оценимо
- neutral_architecture: plain+spine − plain: n<2 — не оценимо
- neutral_architecture: plain+spine-hook − plain: n<2 — не оценимо
- neutral_architecture: openspec+spine − openspec: n<2 — не оценимо
- neutral_architecture: openspec+spine-hook − openspec: n<2 — не оценимо
- neutral_architecture: bmad+spine − bmad: n<2 — не оценимо
- neutral_architecture: bmad+spine-hook − bmad: n<2 — не оценимо
- neutral_architecture: superpowers+spine − superpowers: n<2 — не оценимо
- neutral_architecture: superpowers+spine-hook − superpowers: n<2 — не оценимо

## Гейт: доля PASS_DELTA, точный тест Фишера

- plain+spine: 3/3 vs plain: 2/3 → p=1.0
- plain+spine-hook: 3/3 vs plain: 2/3 → p=1.0
- plain: хук vs советующий: 3/3 vs 3/3 → p=1.0
- openspec+spine: 3/3 vs openspec: 1/3 → p=0.4
- openspec+spine-hook: 2/3 vs openspec: 1/3 → p=1.0
- openspec: хук vs советующий: 2/3 vs 3/3 → p=1.0
- bmad+spine: 3/3 vs bmad: 1/3 → p=0.4
- bmad+spine-hook: 3/3 vs bmad: 1/3 → p=0.4
- bmad: хук vs советующий: 3/3 vs 3/3 → p=1.0
- superpowers+spine: 3/3 vs superpowers: 2/3 → p=1.0
- superpowers+spine-hook: 3/3 vs superpowers: 2/3 → p=1.0
- superpowers: хук vs советующий: 3/3 vs 3/3 → p=1.0

Поправка Холма на подтверждающие тесты H1 (порог α = 0.05):

- H1 bmad: p=0.4 ≤ 0.025 → не значимо
- H1 superpowers: p=1.0 ≤ 0.05 → не значимо

## Взаимодействие: даёт ли Spine стеку больше, чем голому хосту (solution_architecture)

- (openspec+spine − openspec) − (plain+spine − plain): CI95 (-0.127, 0.76)
- (openspec+spine-hook − openspec) − (plain+spine-hook − plain): CI95 (-0.713, 0.32)
- (bmad+spine − bmad) − (plain+spine − plain): CI95 (0.027, 0.963)
- (bmad+spine-hook − bmad) − (plain+spine-hook − plain): CI95 (-0.077, 0.84)
- (superpowers+spine − superpowers) − (plain+spine − plain): CI95 (-0.232, 0.985)
- (superpowers+spine-hook − superpowers) − (plain+spine-hook − plain): CI95 (-0.183, 0.93)

Правило «≈ 0»: 90% CI разности целиком внутри ±0.25; при n < 4 решающие правила не применяются.
PASS_UNTOUCHED — гейт зелёный, но принятая архитектура не изменена: это не дисциплина изменения.
