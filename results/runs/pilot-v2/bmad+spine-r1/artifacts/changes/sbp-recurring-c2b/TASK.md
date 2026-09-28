# Задача для кодового харнесса (increment: рекуррентные C2B-списания)

> Запускать **после** A3 (ратификация `docs/adr/ADR-008-recurring-c2b-subscriptions.md`) и подтверждения документации НСПК / поддержки вендором. До этого — только проектирование.

Реализовать приращение к walking skeleton платёжного шлюза СБП (C2B-приём): рекуррентные списания по согласию плательщика (подписки СБП).

## Scope

1. **Реестр согласий** (`mandate`): статусы `PENDING → ACTIVE → SUSPENDED | REVOKED | EXPIRED`, атомарные переходы (статус + outbox + аудит), иммутабельные условия, доказательство согласия, `prevMandateId`.
2. **API ТСП (аддитивно, v0.2.0)**: `POST /v1/mandates` (Idempotency-Key), `GET /v1/mandates/{mandateId}`, `POST /v1/mandates/{mandateId}/revoke`; расширение `POST /v1/payments` полями `paymentMethod=recurring` + `mandateId`; вебхуки `mandate.activated/revoked/expired`; коды `MANDATE_NOT_ACTIVE`, `MANDATE_LIMIT_EXCEEDED`, `MANDATE_NOT_FOUND`.
3. **Guard согласия**: списание принимается только при `ACTIVE`-согласии и в пределах лимитов; иначе `422` без вызовов ОПКЦ/АБС.
4. **Статусная машина**: списание переиспользует `CREATED → PAID → CREDITED → COMPLETED`; зачисление только из подтверждённого НСПК `PAID` (AD-005). Отдельных денежных состояний не вводить.
5. **Мок-адаптер ОПКЦ** (приращение): `registerMandate`, `getMandateStatus`, `revokeMandate`, `createDebit`, `getDebitStatus`; события `mandate.activated/revoked`, `debit.paid/rejected`, `debit.returned`. Реальный протокол НСПК НЕ реализуется (внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`).
6. **Сверка** — расширить на согласия и рекуррентные списания.

## Инварианты (обязательны, AD-009/AD-010 — дословно из `ARCHITECTURE-SPINE.md`)

- Рекуррентное списание инициируется только при наличии согласия в статусе `ACTIVE`, покрывающего ТСП, сумму, периодичность и срок; проверка — до вызова ОПКЦ и до зачисления. Отзыв согласия немедленно и идемпотентно блокирует новые списания; зачисление — только из подтверждённого НСПК статуса.
- Условия согласия иммутабельны; изменение — новое согласие со ссылкой на предыдущее. Каждое изменение состояния согласия — в неизменяемом аудит-логе.

## Критерии приёмки

См. `changes/sbp-recurring-c2b/ACCEPTANCE.md` (AC-1..AC-5, AC-N1..AC-N7 — негативные обязательны) и `NFR.md`. Регресс одиночных C2B-платежей обязателен; `contract_diff` — 0 ломающих изменений.

## Контракт результата

Финальный ответ обязан завершаться JSON-объектом (после него — ни символа):

```json
{"status": "complete|partial|blocked", "assumptions": [], "open_questions": [], "conflicts_with_prior_decisions": []}
```

- `conflicts_with_prior_decisions` обязательно останавливает работу и эскалирует (любое расхождение с ADR/spine — стоп).
- При `blocked` перечислить недостающие входы (например, отсутствие документации НСПК или поддержки вендором).

Архитектурный контекст — `changes/sbp-recurring-c2b/SOLUTIONING.md` + `.arch-handoff/ARCHITECTURE.md`; ограничения — `.arch-handoff/CONSTRAINTS.yaml`; решение — `docs/adr/ADR-008-recurring-c2b-subscriptions.md`.
