# Дельта: sbp-subscriptions

- Route: Critical (`control score`: new_component, api_contract_change, financial_impact) — полный Solutioning дельты; детальный пакет — `docs/changes/sbp-subscriptions.md`
- Created: 2026-09-28

## Проблема

ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента.

## ADDED

- Инвариант `AD-009` в `ARCHITECTURE-SPINE.md`: списание по подписке — обычный платёж; наследует AD-005.
- Решение `docs/adr/ADR-008-subscriptions.md`.
- Контракт `openapi/tsp-api.yaml` v0.2: `/v1/subscriptions`, `/v1/subscriptions/{id}`, `/v1/subscriptions/{id}/charges` (аддитивно).
- NFR в `docs/nfr.md`, раздел «Подписки» (§7).
- Правило `subscription-charge-needs-consent` в `.arch-handoff/CONSTRAINTS.yaml`.
- Детальный пакет `docs/changes/sbp-subscriptions.md` (значимость, влияние, приёмка, откат, решения человека).

## MODIFIED

- `ARCHITECTURE-SPINE.md`: добавлен AD-009; существующие AD-001..AD-008 не меняются.
- `.arch-handoff/CONSTRAINTS.yaml`: реестр расширен новым правилом, существующие правила не ослаблены.
- `docs/nfr.md`: добавлен раздел §7 «Подписки СБП».
- `openapi/tsp-api.yaml`: версия 0.2.0, аддитивные эндпоинты; существующие `/v1/payments` и схема `Payment` не меняются.

## REMOVED

- Ничего.

## План отката

Фиче-флаг `subscriptions.enabled=false`; новые эндпоинты возвращают 404; данные подписок остаются, списания не создаются.

## Критерии приёмки

- [ ] Списание без согласия ACTIVE отклоняется, платёж не создаётся (тест)
- [ ] Зачисление по списанию — только из `PAID` (fitness, наследует AD-005)
- [ ] Повторный `POST /charges` с тем же `Idempotency-Key` — тот же `paymentId`, дубля нет
- [ ] Отзыв согласия ≤ 1 с; после отзыва списания = 0 (нагрузочный тест)
