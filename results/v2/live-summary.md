# Живой прогон в TUI Qwen Code: Qwen Code × методические стеки

Решатель: `deepseek-flash`; судья: `glm-5.3`; повторов на условие: 3.

| Условие | n | solution_architecture | architecture_gates | adr_quality | macedo_dimensions | neutral_architecture | гейт Spine PASS | ломающих | защищённых | стена, с | сенсоры /10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| plain | 3 | 3.76 | 3.47 | — | — | 3.63 | 2/3 | 0 | 1.67 | 670.03 | 9 |
| plain+spine | 3 | 3.32 | 2.93 | — | — | 3.6 | 3/3 | 0 | 2 | 1221.17 | 9 |
| plain+spine-hook | 3 | 3.54 | 3.47 | — | — | 3.85 | 3/3 | 0 | 2 | 931.2 | 9 |
| openspec | 3 | 3.84 | 3.4 | — | — | 3.52 | 2/3 | 0 | 0.33 | 457.27 | 9 |
| openspec+spine | 3 | 3.73 | 3.5 | — | — | 3.85 | 3/3 | 0 | 1 | 593.23 | 9 |
| openspec+spine-hook | 3 | 3.43 | 2.93 | — | — | 3.82 | 3/3 | 0 | 1.33 | 1251.0 | 9 |
| bmad | 3 | 3.62 | 2.93 | — | — | 3.63 | 1/3 | 0 | 1 | 972.5 | 9 |
| bmad+spine | 3 | 3.7 | 3.47 | — | — | 3.78 | 3/3 | 0 | 1.33 | 558.2 | 9 |
| bmad+spine-hook | 3 | 3.8 | 3.8 | — | — | 3.93 | 3/3 | 0 | 2 | 839.47 | 9 |
| superpowers | 3 | 3.57 | 3.27 | — | — | 3.52 | 2/3 | 0 | 2 | 713.07 | 9 |
| superpowers+spine | 3 | 3.51 | 3.23 | — | — | 3.55 | 3/3 | 0 | 0.67 | 582.13 | 9 |
| superpowers+spine-hook | 3 | 3.74 | 3.2 | — | — | 4.0 | 3/3 | 0 | 2 | 957.5 | 9 |

## Парные эффекты против голого Qwen Code (solution_architecture, bootstrap 95% CI)

- plain+spine − plain = -0.44 CI (-0.84, 0.13) (n=3)
- plain+spine-hook − plain = -0.22 CI (-0.59, 0.45) (n=3)
- openspec − plain = 0.08 CI (0.0, 0.15) (n=3)
- openspec+spine − plain = -0.03 CI (-0.21, 0.26) (n=3)
- openspec+spine-hook − plain = -0.33 CI (-0.66, -0.13) (n=3)
- bmad − plain = -0.14 CI (-0.55, 0.52) (n=3)
- bmad+spine − plain = -0.06 CI (-0.46, 0.51) (n=3)
- bmad+spine-hook − plain = 0.04 CI (-0.27, 0.51) (n=3)
- superpowers − plain = -0.19 CI (-0.74, 0.52) (n=3)
- superpowers+spine − plain = -0.15 CI (-0.72, 0.42) (n=2)
- superpowers+spine-hook − plain = -0.02 CI (-0.52, 0.54) (n=3)

Сенсоры — эвристики наличия объектного минимума артефактов; это сигналы, не оценка качества.
Итог рубрики с неоценёнными критериями отбрасывается (находка F7 комплекта).
