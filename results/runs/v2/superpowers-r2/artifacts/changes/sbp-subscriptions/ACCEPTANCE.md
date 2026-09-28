# Критерии приёмки: sbp-subscriptions

Проверяемые критерии для гейтов A4/A5. Негативные сценарии обязательны.

## Позитивные

- [ ] Сквозной сценарий: создание подписки → подтверждение согласия → списание → `PAID` → `CREDITED` → `COMPLETED`; вебхуки `subscription.activated` и `charge.completed` доставлены идемпотентно по `eventId`.
- [ ] Возврат списания проходит сагу возврата; полный возврат переводит платёж в `REFUNDED`, мандат не меняется.
- [ ] `GET /v1/subscriptions/{id}` и `GET /v1/subscriptions/{id}/payments` возвращают состояние мандата и список списаний.
- [ ] Контракт v0.2 обратно совместим: `arch contract-diff` между v0.1 и v0.2 — PASS, breaking = 0; потребитель v0.1 работает без изменений.

## Негативные

- [ ] Списание при мандате `PENDING_CONSENT`/`PAUSED`/`REVOKED`/`EXPIRED` отклоняется (`SUBSCRIPTION_NOT_ACTIVE`/`CONSENT_REVOKED`); обращения в ОПКЦ нет (тест-шпион на адаптер).
- [ ] Списание сверх лимита разового или за период отклоняется (`SUBSCRIPTION_LIMIT_EXCEEDED`).
- [ ] Повтор списания с тем же `Idempotency-Key` → тот же `paymentId`, второй проводки нет; повтор за закрытый период → `CHARGE_PERIOD_CLOSED` (fitness `idempotency-key`).
- [ ] Таймаут ОПКЦ → `OPKC_UNKNOWN`, повторной отправки нет, исход разрешается `getChargeStatus`/сверкой (fitness `unknown-outcome-no-resend`).
- [ ] Отзыв мандата в момент списания: зачисление не выполняется; повторный отзыв идемпотентен.
- [ ] Повторная нотификация СБП по завершённому списанию состояние не меняет (дедуп по `eventId`).
- [ ] ПДн плательщика отсутствуют в логах и метках метрик (fitness `no-pii-in-logs`); запись доказательства согласия неизменяема (fitness `append-only-journal`).

## Гейт и evidence

- [ ] `arch gate --route critical`: fitness, spine_lint, delta_guard, sensors — зелёные; `arch delta validate sbp-subscriptions` — без ошибок; `arch control spine ARCHITECTURE-SPINE.md` — без нарушений.
- [ ] Репетиция отката A4 подтверждает `ROLLBACK.md`.
