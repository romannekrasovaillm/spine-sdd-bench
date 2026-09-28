# Задача для кодового харнесса: подписки СБП (рекуррентные C2B-списания, ADR-008)

Реализовать изменение поверх walking skeleton платёжного шлюза СБП по решению `docs/adr/ADR-008-*.md`, `docs/spec/mandate-lifecycle.md` и контрактам `docs/contracts/tsp-api.md` (v0.2) / `docs/contracts/opkc-adapter.md` (v0.2):

1. **Агрегат мандата** в БД шлюза: состояния `PENDING_CONSENT → ACTIVE → SUSPENDED/REVOKED/EXPIRED/REJECTED`; переходы атомарны (статус + outbox + аудит, AD-009); параметры (`maxAmountPerCharge`, `maxTotalAmount`, `validFrom`, `validTo`, `tspId`, `opkcMandateRef`) иммутабельны после активации.
2. **API ТСП** (аддитивно к v0.1, `/v1`): `POST /v1/mandates`, `GET /v1/mandates/{id}`, `POST /v1/mandates/{id}/suspend|resume|revoke`, `POST /v1/mandates/{id}/charges` — по `openapi/tsp-api.yaml` v0.2.0-draft.
3. **Списание как обычный платёж**: тот же FSM, `paymentOrigin=mandate`, переход `CREATED → PAID` без QR (AD-010); зачисление в АБС — **только из `PAID`** (AD-005).
4. **Валидация в одной транзакции с созданием платежа** (AD-011): `ACTIVE` ∧ `amount ≤ maxAmountPerCharge` ∧ время в периоде ∧ ТСП-владелец; иначе — отказ без создания платежа. Отзыв/приостановка немедленно запрещают новые списания.
5. **Идемпотентность** (расширение AD-003): `Idempotency-Key` + запрет повтора `merchantOrderId`/периода в рамках мандата (`409 MANDATE_CHARGE_CONFLICT`); повтор любой нотификации/триггера не создаёт второе списание/проводку.
6. **Мок-адаптер ОПКЦ** (расширение существующего мока): `createMandate`, `getMandateStatus`, `revokeMandate`, `executeMandateCharge` + события `mandate.activated`/`mandate.revoked`/`mandate.rejected`; списание без QR; протокол НСПК НЕ реализуется (внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`).
7. **Нотификатор ТСП**: новые события `mandate.*`; ТСП обязан игнорировать неизвестные события; исход списания — стандартные `payment.*`.
8. **Сверка мандатов** с мок-ОПКЦ: расхождение «у ОПКЦ отозван — у нас `ACTIVE`» → немедленный локальный `REVOKED` + алерт.
9. **Изоляция**: per-ТСП фиче-флаг подписок; выключение не влияет на QR-приём.

Spine-инварианты обязательны: AD-001…AD-011 (см. `ARCHITECTURE.md`). Зачисление только из `PAID`, атомарные переходы, идемпотентность повторных доставок. Критерии приёмки — `RUBRIC.yaml` и `docs/nfr.md` §7 (выполнимы на моках): списаний после отзыва = 0, двойных списаний = 0, регресс QR ≤ 5 %. Стек — по выбору команды с обоснованием в ADR; приоритет — доказать архитектуру сквозным сценарием, а не полнотой продукта.

## Контракт результата

Финальный ответ обязан завершаться JSON-объектом (после него — ни символа):

```json
{"status": "complete|partial|blocked", "assumptions": [], "open_questions": [], "conflicts_with_prior_decisions": []}
```

- `status`: `complete` — выполнено полностью; `partial` — частично; `blocked` — заблокировано.
- `assumptions`: допущения, принятые при реализации.
- `open_questions`: вопросы к архитектору.
- `conflicts_with_prior_decisions`: расхождения с принятыми ранее решениями (ADR, spine); при наличии — остановка и эскалация.

Ограничения — `CONSTRAINTS.yaml`, рубрика приёмки — `RUBRIC.yaml`, источники — `MANIFEST.json`.
