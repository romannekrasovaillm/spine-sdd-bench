# Отчёт fitness-проверок — Подписки СБП

Прогон: `arch-be` 0.3.11, 2026-09-28.

**Итог: PASS (19 правил, 0 нарушений; ослаблений относительно HEAD нет).** Единый гейт маршрута Critical — «выпуск заблокирован» из-за 4 пост-A3 артефактов (см. ниже); это не дефект fitness.

Команды и результаты:

| Проверка | Команда | Результат |
|---|---|---|
| Fitness-правила | `arch-be control check .` | PASS — правил 19 (error 17, warn 2), нарушений 0; ослаблений относительно HEAD нет |
| Линтер спайна | `arch-be control spine ARCHITECTURE-SPINE.md` | нарушений нет |
| Сенсоры спек | `arch-be control sensors docs/spec` | PASS — 4 сенсора, провалов 0 |
| Delta guard | `arch-be delta guard --repo .` | PASS — правки `ARCHITECTURE-SPINE.md` покрыты активной дельтой `sbp-subscriptions` |
| Delta validate | `arch-be delta validate sbp-subscriptions` | нарушений нет |
| Контрактный дифф | `arch-be contract-diff openapi/tsp-api.v0.1.yaml openapi/tsp-api.yaml` | PASS — breaking 0, non-breaking 6 |
| Значимость | `arch-be control score …` | 11/15 → Critical |
| Единый гейт | `arch-be gate --repo . --route critical` | **FAIL (exit 1) — «выпуск заблокирован»**; содержательных находок 0, причина — 4 пост-A3 артефакта (см. ниже) |

Состав реестра правил: 19 (error 17, warn 2). **Проверяют поведение: 0 из 19** — до появления кода это ожидаемо; поведенческие правила (`command_succeeds`) добавляются при handoff (`--refresh-constraints`).

## Статус единого гейта (Critical) — «выпуск заблокирован» (FAIL, exit 1)

| Составляющая | Статус | Причина |
|---|---|---|
| fitness, delta_guard, rule_weakened, spine_lint, sensors | PASS | проверено этим изменением |
| evidence_verify | FAIL | bundle 9/13; содержательных находок 0 (ревью READY, fitness PASS); отсутствуют `decision_a3`, `walking_skeleton`, `rollback_rehearsal`, `validation` — пост-A3/пост-реализация (не фабрикуются) |
| trace_check, nfr, model_validate | SKIP | в репозитории нет каталога `model/` (отдельная инициатива, `docs/solutioning-subscriptions.md` §7 п.6) |

Гейт осознанно заблокирован до A3 — зелёный здесь был бы признаком approval theater.
