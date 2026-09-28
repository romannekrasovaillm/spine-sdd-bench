# Задача для кодового харнесса: СБП-подписки (рекуррентные C2B-списания)

> Условие запуска: **только после человеческого решения A3** (ADR-008 переведён в `Accepted`) и влития дельты `changes/sbp-subscriptions/DELTA.md`. До этого задача не передаётся в реализацию.

Реализовать walking skeleton подписок СБП поверх принятого шлюза (ADR-001..007), по `docs/adr/ADR-008-...md` и `docs/spec/state-machine.md` §7–8:

1. **Домен согласия.** REST API ТСП: `POST /v1/consents`, `GET /v1/consents/{consentId}`, `POST /v1/consents/{consentId}/revoke`, `POST /v1/consents/{consentId}/debits` (опц. режим); машина согласия `PENDING_PAYER → ACTIVE → SUSPENDED → REVOKED | EXPIRED`, терминальные `REJECTED`/`REVOKED`/`EXPIRED`; переходы атомарны «статус + outbox + аудит».
2. **Планировщик списаний.** Инициация списаний по расписанию согласия, идемпотентная по `consentId + billingPeriod`; рестарт без пропусков и дублей; guard «только `ACTIVE`».
3. **Списание как платёж.** Списание создаёт платёж в существующей машине (`CREATED → DEBIT_PENDING → PAID → CREDITED → COMPLETED`, терминальные `FAILED`); зачисление АБС — **только из `PAID`** (AD-005).
4. **Мок-адаптер ОПКЦ** с подписочными операциями (`createMandate`, `getMandateStatus`, `revokeMandate`, `createDebit`, `getDebitStatus`) и событиями (`mandate.*`, `debit.*`) — реальный протокол НСПК НЕ реализуется (внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`).
5. **Мок-адаптер АБС**: идемпотентное зачисление по `paymentId` для списаний.
6. **Нотификатор вебхуков**: события `consent.*` и `payment.*` с ретраями и DLQ.

Связывающие инварианты (spine, обязательны): AD-002, AD-003, AD-005, AD-009 (см. `ARCHITECTURE.md`). Критерии приёмки — NFR из `docs/nfr.md` §7 (выполнимы на моках): дубликаты списаний = 0, списание без `ACTIVE` = 0, отзыв ≤ 60 с. Приоритет — доказать архитектуру сквозным сценарием, а не полнотой продукта.

## Контракт результата

Финальный ответ обязан завершаться JSON-объектом (после него — ни символа):

```json
{"status": "complete|partial|blocked", "assumptions": [], "open_questions": [], "conflicts_with_prior_decisions": []}
```

- `status`: `complete` — выполнено полностью; `partial` — частично; `blocked` — заблокировано.
- `assumptions`: допущения, принятые при реализации.
- `open_questions`: вопросы к архитектору.
- `conflicts_with_prior_decisions`: расхождения с принятыми ранее решениями (ADR/spine) — **обязаны останавливать работу и эскалироваться**, не решаться молча.

Инварианты и запреты — `ARCHITECTURE.md`; ограничения — `CONSTRAINTS.yaml`; рубрика приёмки — `RUBRIC.yaml`; откат — `ROLLBACK.yaml`.
