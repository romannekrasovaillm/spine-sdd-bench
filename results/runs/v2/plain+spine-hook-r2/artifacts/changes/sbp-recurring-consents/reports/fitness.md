# Отчёт прогонов контроля — sbp-recurring-consents

Дата: 2026-09-28. Все прогоны выполнены на рабочем дереве после внесения изменения (база `bench-baseline`).

## Fitness и линтеры

```
arch-be control check .
→ Правил: 12, нарушений: 0 (error: 0, warn: 0); реестр: 12 правил (error: 10), отпечаток d68193b3; ослаблений нет
→ Итог: PASS

arch-be control spine ARCHITECTURE-SPINE.md
→ spine: нарушений нет

arch-be delta validate sbp-recurring-consents
→ дельта 'sbp-recurring-consents': нарушений нет

arch-be delta guard --base bench-baseline
→ Изменённых файлов: 22, защищённых среди них: 1 (активных дельт: 1)
→ [ok] ARCHITECTURE-SPINE.md — покрыт активной дельтой 'sbp-recurring-consents'
→ Итог: PASS
```

## Контрактный гейт

```
openapi_lint openapi/tsp-api.yaml → 0 находок (error: 0, warn: 0) → PASS

contract_diff old=openapi/tsp-api.yaml@v0.1 new=openapi/tsp-api.yaml@v0.2
→ contract_diff: 5 изменений (breaking: 0, non-breaking: 5): добавлены пути
  /v1/consents, /v1/consents/{consentId}, /v1/consents/{consentId}/charges,
  /v1/consents/{consentId}/revoke, /v1/payments/{paymentId}/charges/{chargeId}
→ Итог: PASS
```

## Единый гейт

```
arch-be gate --route auto --base bench-baseline
→ Маршрут Fast (auto: score 0) — механический floor не видит смысловых триггеров
→ fitness PASS, delta_guard PASS, rule_weakened PASS, spine_lint PASS
→ Итог: PASS

arch-be gate --route critical --base bench-baseline
→ fitness PASS, delta_guard PASS, rule_weakened PASS, spine_lint PASS, sensors PASS
→ trace_check SKIP (нет model/), model_validate SKIP (нет model/), nfr SKIP (нет model/)
→ evidence_verify — bundle собран, неполон (см. EVIDENCE.yaml: нет A3, walking skeleton, репетиции, валидации)
→ Итог: INCOMPLETE (обязательные составляющие без входа) / на evidence — FAIL до заполнения
```

## Сенсоры спецификаций

```
arch-be control sensors docs/spec
→ required_sections: state-machine.md, consent-state-machine.md — PASS
→ upstream_coverage — PASS
→ Итог: FAIL→исправлено: до изменения state-machine.md не имела секций «Проблема/Критерии приёмки/Риски»
```

## Вывод

Детерминированный контур (fitness, spine-линтер, дельта, контрактный гейт) — зелёный. Критический маршрут неполон по составу, который физически отсутствует до реализации: типизированная модель (`model/`), walking skeleton, решение A3, репетиция отката, валидация. Это ожидаемое состояние пакета, выносимого на архитектурное решение, а не на выпуск.
