# Spec / Delta — add-recurring-payments

Этот артефакт фиксирует спецификацию изменения (дельта к живой истине).

## Артефакты-источники

- Дельта OpenSpec: `openspec/changes/add-recurring-payments/specs/recurring-payments/spec.md` (ADDED Requirements, capability `recurring-payments`).
- Дельта арх-харнесса: `changes/add-recurring-payments/DELTA.md` (ADDED/MODIFIED живого спайна и контракта).
- Живая истина, расширяемая при archive: `ARCHITECTURE-SPINE.md` (AD-009, AD-010), `docs/spec/state-machine.md`, `docs/contracts/tsp-api.md`, `openapi/tsp-api.yaml`, `docs/nfr.md`.

## Требования (ADDED, сводка)

1. **Регистрация согласия плательщика** — `POST /v1/consents` создаёт `PENDING`-согласие; `ACTIVE` — только по подтверждению НСПК.
2. **Списание только по действующему согласию и в пределах лимитов** — не-`ACTIVE` согласие и превышение лимита → отказ, платёж не создаётся (AD-009).
3. **Инициация рекуррентного списания** — платёж `initiationType=debit`, `CREATED → DEBIT_PENDING → PAID → CREDITED → COMPLETED`; идемпотентен по `Idempotency-Key`.
4. **Однократность списания за расчётный период** — уникальность `(subscriptionId, billingPeriod)` (AD-010).
5. **Отзыв согласия** — немедленный запрет новых списаний; подтверждённые доводятся; неподтверждённые → `FAILED/CONSENT_REVOKED` (ADR-009).
6. **Идемпотентность событий и переходов согласия** — атомарность «статус + outbox + аудит» (AD-002), дедуп по `eventId` (AD-003).
7. **Нотификации ТСП** — `consent.activated`, `consent.revoked`, `consent.expired` (at-least-once, HMAC, `X-SBP-Event-Id`).
8. **Наблюдаемость и аудит** — 100 % переходов согласия и списаний в аудит-логе, `traceId`, отчёт незавершённых операций.
9. **Совместимость с QR-потоком** — требования и контракт существующего потока не меняются.

## Контракт

`openapi/tsp-api.yaml` v0.1.0 → v0.2.0 — аддитивно: 6 новых путей, опциональные поля `Payment`, новое состояние `DEBIT_PENDING`, новые события. Ломающих изменений нет (`contract_diff`: breaking 0, non-breaking 6).

Полные формулировки с EARS и сценариями — в `specs/recurring-payments/spec.md`.
