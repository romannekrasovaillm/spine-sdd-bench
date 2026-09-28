# Отчёт архитектурного контроля — изменение «Подписки СБП»

Дата: 2026-09-28. Маршрут: **Critical**. Источник: инструменты Spine (`arch-be`) на репозитории `ws`.

## Итог единого гейта

```
arch-be gate --route critical
  [PASS] fitness        — 14 правил, 0 нарушений (error 0, warn 0); ослаблений нет
  [PASS] delta_guard    — защищённые правки покрыты дельтой 'subscriptions-c2b' (ARCHITECTURE-SPINE.md)
  [PASS] rule_weakened  — реестр правил не ослаблен относительно HEAD
  [PASS] spine_lint     — находок 0
  [SKIP] trace_check/model_validate/nfr — нет каталога model/ (базовый репозиторий его не заводил)
  [PASS] sensors        — сенсоров 4, провалов нет
  [SKIP] evidence_verify — см. ниже (бандл собирается)
Итог: INCOMPLETE (exit 3) — обязательные составляющие без входа: trace_check, nfr, model_validate, evidence_verify
```

`INCOMPLETE` ожидаемо и **не означает нарушение**: часть обязательных составляющих маршрута Critical требует входов, которых в базовом репозитории нет или которые появляются на A4 (модель, evidence-бандл с подписанным A3). Ни одна проверенная составляющая не красная.

## Проверки по отдельности (факты)

| Проверка | Команда / инструмент | Результат |
|---|---|---|
| Fitness-правила | `fitness_check` | 14 правил, 0 нарушений; ослаблений относительно HEAD нет |
| Линтер spine | `spine_lint` | PASS (дубли/пустые поля/заглушки — нет) |
| Правки защищённых путей | `delta_guard` | PASS: `ARCHITECTURE-SPINE.md` покрыт дельтой `subscriptions-c2b`; `CONSTRAINTS.yaml` — в дельте |
| Обязательные секции спецификаций | `control sensors docs/spec` | PASS (2 файла, 4 сенсора, 0 провалов) |
| OpenAPI-контракт | `openapi_lint openapi/tsp-api.yaml` | PASS (0 находок) |
| Совместимость контракта | `contract_diff` 0.1.0 → 0.2.0 | PASS: 5 добавлений, **breaking: 0** |
| Маршрут значимости | `significance_score` | Critical, score 11 |

## Новые fitness-правила (CONSTRAINTS.yaml)

`adr-subscriptions-present`, `spine-consent-source-of-truth`, `spine-debit-period-idempotency`, `tsp-api-subscriptions-present`, `tsp-api-version-bumped`, `subscription-spec-acceptance`, `nfr-subscriptions-measurable` — все PASS, ни одно существующее правило не ослаблено.

## Что гейт НЕ проверяет (границы зелёного)

- Смысловую корректность решения (за это — `docs/REVIEW.md` и рубрики).
- Наличие/подпись решения A3 (`DECISION.md`, `decided_by` пуст — ожидается `a3_not_signed`).
- Репетицию отката (`rollback_rehearsal`) — проводится на A4.
- Внешние входы (протокол НСПК, правовое основание согласия) — вне механики.

## Вывод

Изменение **проходит все доступные механические гейты**; единый гейт в состоянии `INCOMPLETE` из-за отсутствующих входов (модель/бандл/A3), а не из-за нарушений. Пакет готов к вынесению на A3.

## Строка итога

Итог: PASS (14 правил, 0 нарушений; spine_lint PASS; delta_guard PASS; sensors PASS; openapi_lint PASS; contract_diff breaking: 0). Единый гейт маршрута Critical — `INCOMPLETE` (обязательные составляющие без входа: trace_check, nfr, model_validate, evidence_verify), выпуск до A3/A4 заблокирован.
