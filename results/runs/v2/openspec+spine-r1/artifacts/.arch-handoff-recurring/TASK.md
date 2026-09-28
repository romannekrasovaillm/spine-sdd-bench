# Задача для кодового харнесса

Реализовать **рекуррентные C2B-списания по согласию плательщика (подписки СБП)** поверх принятого решения (ADR-001..007, `ARCHITECTURE-SPINE.md`), в соответствии с `docs/adr/ADR-008-*`, `docs/adr/ADR-009-*` и планом `openspec/changes/add-sbp-recurring-payments/tasks.md`:

1. **Согласие (mandate)** — сущность и жизненный цикл `PENDING_PAYER → ACTIVE → SUSPENDED → REVOKED | EXPIRED | REJECTED`; зеркало реестра СБП; атомарные переходы «состояние + outbox + аудит»; аудит неизменяем.
2. **Списание** — платёж существующей статусной машины с атрибутом `consentId` (`CREATED → PAID → CREDITED → COMPLETED`); зачисление только из `PAID`; предусловие `ACTIVE` + лимиты проверяется в одной транзакции с созданием попытки (AD-009).
3. **Идемпотентность попытки** — детерминированный ключ `(consentId, billingPeriod, attemptSeq)` как `reference` адаптера и внешний ключ АБС (AD-011).
4. **Планировщик и повторы** — по outbox/очереди, ретраи с экспоненциальной задержкой и джиттером, окно/число попыток — из политики; сглаживание пиков и per-ТСП честность.
5. **Отзыв согласия** — приоритетен: блокирует неподтверждённые ОПКЦ попытки, подтверждённые компенсирует возвратом (AD-010).
6. **API ТСП** — строго по `openapi/tsp-api.yaml` 0.2.0: `/v1/consents*`, опциональное поле `consentId` у платежа, коды ошибок RFC 9457.
7. **Нотификации** — события `consent.activated/revoked/expired`, `charge.completed/failed`, at-least-once, дедуп по `eventId`.
8. **Мок-адаптер ОПКЦ подписок** — операции `registerConsent/getConsentStatus/cancelConsent/createDebit/getDebitStatus` и события `consent.*/debit.*`; реальный протокол НСПК **не реализуется** (внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`), ядро контрактно-независимо от транспорта.

Технологический стек — по выбору команды, но с обоснованием в ADR. Приоритет — доказать архитектуру сквозным сценарием (включая гонку «списание / отзыв» и негативную матрицу), а не полнотой продукта. Критерии приёмки — `openspec/changes/add-sbp-recurring-payments/design.md` § Acceptance criteria и `changes/add-sbp-recurring-payments/DELTA.md` § Критерии приёмки. Spine-инварианты AD-001..AD-011 обязательны.

## Контракт результата

Финальный ответ обязан завершаться JSON-объектом (после него — ни символа):

```json
{"status": "complete|partial|blocked", "assumptions": [], "open_questions": [], "conflicts_with_prior_decisions": []}
```

- `status`: `complete` — выполнено полностью; `partial` — частично; `blocked` — заблокировано (перечислить недостающие входы, например документацию НСПК).
- `assumptions`: допущения, принятые при реализации.
- `open_questions`: вопросы к архитектору (например, политика повторов, лимиты).
- `conflicts_with_prior_decisions`: расхождения с ADR/spine — обязан остановить и эскалировать.

Архитектурный контекст — `ARCHITECTURE.md`, ограничения — `CONSTRAINTS.yaml`, рубрика приёмки — `RUBRIC.yaml`.
