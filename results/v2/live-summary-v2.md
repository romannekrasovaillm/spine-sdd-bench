# Живой прогон v2: стек × режим Spine

Прогонов: 36; исключение загрязнённых: нет (ITT).

| стек | Spine | n | solution_architecture | architecture_gates | adr_quality | macedo_dimensions | neutral_architecture | PASS_DELTA | PASS_UNTOUCHED | FAIL |
|---|---|---|---|---|---|---|---|---|---|---|
| plain | — | 3 | 3.76 | 3.47 | — | — | 3.63 | 2/3 | 0/3 | 1/3 |
| plain | spine | 3 | 3.32 | 2.93 | — | — | 3.60 | 3/3 | 0/3 | 0/3 |
| plain | spine-hook | 3 | 3.54 | 3.47 | — | — | 3.85 | 3/3 | 0/3 | 0/3 |
| openspec | — | 3 | 3.84 | 3.40 | — | — | 3.52 | 1/3 | 1/3 | 1/3 |
| openspec | spine | 3 | 3.73 | 3.50 | — | — | 3.85 | 3/3 | 0/3 | 0/3 |
| openspec | spine-hook | 3 | 3.43 | 2.93 | — | — | 3.82 | 2/3 | 1/3 | 0/3 |
| bmad | — | 3 | 3.62 | 2.93 | — | — | 3.63 | 1/3 | 0/3 | 2/3 |
| bmad | spine | 3 | 3.70 | 3.47 | — | — | 3.78 | 3/3 | 0/3 | 0/3 |
| bmad | spine-hook | 3 | 3.80 | 3.80 | — | — | 3.93 | 3/3 | 0/3 | 0/3 |
| superpowers | — | 3 | 3.57 | 3.27 | — | — | 3.52 | 2/3 | 0/3 | 1/3 |
| superpowers | spine | 3 | 3.51 | 3.23 | — | — | 3.55 | 3/3 | 0/3 | 0/3 |
| superpowers | spine-hook | 3 | 3.74 | 3.20 | — | — | 4.00 | 3/3 | 0/3 | 0/3 |

## Эффект Spine внутри стека (непарно, bootstrap 95% CI, перестановочный p)

- solution_architecture: plain+spine − plain = -0.44 CI95 (-0.76, -0.06) p=0.2; не хуже (±0.25): None CI90 None
- solution_architecture: plain+spine-hook − plain = -0.22 CI95 (-0.57, 0.157) p=0.3; не хуже (±0.25): None CI90 None
- solution_architecture: openspec+spine − openspec = -0.11 CI95 (-0.337, 0.177) p=0.5; не хуже (±0.25): None CI90 None
- solution_architecture: openspec+spine-hook − openspec = -0.41 CI95 (-0.747, -0.08) p=0.2; не хуже (±0.25): None CI90 None
- solution_architecture: bmad+spine − bmad = +0.08 CI95 (-0.217, 0.383) p=0.8; не хуже (±0.25): None CI90 None
- solution_architecture: bmad+spine-hook − bmad = +0.18 CI95 (-0.1, 0.42) p=0.4; не хуже (±0.25): None CI90 None
- solution_architecture: superpowers+spine − superpowers = -0.06 CI95 (-0.573, 0.457) p=0.8; не хуже (±0.25): None CI90 None
- solution_architecture: superpowers+spine-hook − superpowers = +0.17 CI95 (-0.227, 0.56) p=0.6; не хуже (±0.25): None CI90 None
- architecture_gates: plain+spine − plain = -0.53 CI95 (-1.233, 0.167) p=0.3; не хуже (±0.25): None CI90 None
- architecture_gates: plain+spine-hook − plain = -0.00 CI95 (-0.433, 0.467) p=1.0; не хуже (±0.25): None CI90 None
- architecture_gates: openspec+spine − openspec = +0.10 CI95 (-0.467, 0.667) p=0.8; не хуже (±0.25): None CI90 None
- architecture_gates: openspec+spine-hook − openspec = -0.47 CI95 (-1.2, 0.2) p=0.5; не хуже (±0.25): None CI90 None
- architecture_gates: bmad+spine − bmad = +0.53 CI95 (-0.033, 1.233) p=0.3; не хуже (±0.25): None CI90 None
- architecture_gates: bmad+spine-hook − bmad = +0.87 CI95 (0.267, 1.567) p=0.1; не хуже (±0.25): None CI90 None
- architecture_gates: superpowers+spine − superpowers = -0.03 CI95 (-0.967, 0.867) p=1.0; не хуже (±0.25): None CI90 None
- architecture_gates: superpowers+spine-hook − superpowers = -0.07 CI95 (-1.133, 0.967) p=1.0; не хуже (±0.25): None CI90 None
- neutral_architecture: plain+spine − plain = -0.04 CI95 (-0.183, 0.073) p=1.0; не хуже (±0.25): None CI90 None
- neutral_architecture: plain+spine-hook − plain = +0.22 CI95 (-0.193, 0.513) p=0.4; не хуже (±0.25): None CI90 None
- neutral_architecture: openspec+spine − openspec = +0.33 CI95 (-0.11, 0.853) p=0.4; не хуже (±0.25): None CI90 None
- neutral_architecture: openspec+spine-hook − openspec = +0.30 CI95 (-0.183, 0.813) p=0.7; не хуже (±0.25): None CI90 None
- neutral_architecture: bmad+spine − bmad = +0.15 CI95 (-0.183, 0.56) p=0.8; не хуже (±0.25): None CI90 None
- neutral_architecture: bmad+spine-hook − bmad = +0.30 CI95 (0.037, 0.67) p=0.3; не хуже (±0.25): None CI90 None
- neutral_architecture: superpowers+spine − superpowers = +0.04 CI95 (-0.373, 0.447) p=1.0; не хуже (±0.25): None CI90 None
- neutral_architecture: superpowers+spine-hook − superpowers = +0.48 CI95 (0.11, 0.817) p=0.2; не хуже (±0.25): None CI90 None

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
