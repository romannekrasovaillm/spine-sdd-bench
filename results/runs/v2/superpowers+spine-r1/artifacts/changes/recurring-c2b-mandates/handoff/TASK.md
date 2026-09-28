# Задача для кодового харнесса

Реализовать **СБП-подписки** (рекуррентные C2B-списания по согласию плательщика) поверх принятого платёжного шлюза СБП:

1. **API мандатов** для ТСП: `POST /v1/mandates` (Idempotency-Key), `GET /v1/mandates/{mandateId}`, `GET /v1/mandates/{mandateId}/charges`, `POST /v1/mandates/{mandateId}/revoke` — по `openapi/tsp-api.yaml` v0.2 и `docs/contracts/tsp-api.md` §7.
2. **Статусная машина мандата**: `PENDING_CONSENT → ACTIVE → REVOKED | EXPIRED | REJECTED` (опц. `SUSPENDED`), переходы — атомарно «статус + outbox + аудит» (AD-002), идемпотентность по `eventId`.
3. **Планировщик списаний**: расписание в БД (AD-011), выборка due-мандатов `ACTIVE`, создание `Charge` `(mandateId, billingPeriod)` в одной транзакции с outbox (AD-010), аренда лидера как защита в глубину.
4. **Списание как платёж**: `Payment` (`source=SUBSCRIPTION`) проходит существующую статусную машину; зачисление в АБС — только из `PAID` (AD-005); `UNKNOWN` не повторять, разрешать сверкой.
5. **События и вебхуки ТСП**: `mandate.activated|revoked|expired|rejected`; `payment.*` дополняются `mandateId`, `billingPeriod`.
6. **Мок-адаптер ОПКЦ**: операции согласия и списания по мандату с идемпотентностью по `reference` — реальный протокол НСПК **не реализуется** (внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`).

**Предусловие.** Человеческое решение A3 (ADR-008, ADR-009) принято, предлагаемые инварианты AD-009/AD-010/AD-011 ратифицированы.

**Не делать:** второй источник истины/хранилище подписок; вызовы ОПКЦ/АБС вне адаптеров; реализацию протокола НСПК в ядре; ломающие изменения контракта v0.1; правки `ARCHITECTURE-SPINE.md` и `CONSTRAINTS.yaml` вне дельты.

## План отката

Откат кода — единым коммитом исполнителя: `git reset --hard <baseline>` (baseline — последний коммит до работы). Продуктовый откат — фиче-флаги `subscriptions.enroll=off` и `subscriptions.charge=off` (начатые операции доводятся штатно). Сигналы отката: любой случай двойного списания за период или списания без `ACTIVE`-мандата; провал fitness-гейта; непустой `conflicts_with_prior_decisions`. Владелец решения — solution-архитектор; исполнитель откат не выполняет и не маскирует проблему обходным редизайном. Детали — `ACCEPTANCE.md` §4.

## Финализация (обязательно)

Результат забирается из git, поэтому перед финальным ответом зафиксируй работу коммитом:

```bash
git add -A -- . ':!changes/recurring-c2b-mandates/handoff'
git commit -m "<кратко: что реализовано>"
git status --short
```

- Коммитится код и тесты; служебный каталог пакета передачи в коммит не входит.

## Контракт результата

Финальный ответ обязан завершаться JSON-объектом (после него — ни символа):

```json
{"status": "complete|partial|blocked", "assumptions": [], "open_questions": [], "conflicts_with_prior_decisions": []}
```

- `status`: `complete` — выполнено полностью; `partial` — частично; `blocked` — заблокировано.
- `assumptions`: допущения, принятые при реализации.
- `open_questions`: вопросы к архитектору.
- `conflicts_with_prior_decisions`: расхождения с принятыми ранее решениями (ADR, spine) — обязаны остановить и эскалировать.

## Чеклист перед финальным ответом

- [ ] Реализация сверена с `SPEC.md` (контракты интерфейсов, структуры данных, границы ошибок, критерии верификации); расхождения — в `conflicts_with_prior_decisions`, а не молчаливым отступлением.
- [ ] Применены исполняемые правила: `arch-be rules template apply consent-before-auto-action --ad AD-9 --dir .`, `… idempotency-key --ad AD-10 …`, `… unknown-outcome-no-resend --ad AD-10 …`; проверены зубы (тест падает на нарушающей реализации).
- [ ] `arch-be control check .` — PASS; `openapi_lint` — PASS; `contract_diff` v0.1 → v0.2 (breaking = 0).
- [ ] Негативные сценарии `AC-6…AC-13` покрыты тестами.
