# Задача для кодового харнесса — инкремент «Подписки СБП (рекуррентные C2B-списания)»

Реализовать поверх walking skeleton платёжного шлюза СБП **рекуррентные C2B-списания по согласию
плательщика** по решению `docs/adr/ADR-008-*.md` и `docs/solutioning-subscriptions.md`:

1. **Сервис согласий** — новая сущность «согласие плательщика» со статусной машиной
   `INITIATED→PENDING_PAYER→ACTIVE/SUSPENDED/REVOKED/EXPIRED/REJECTED` (`docs/spec/subscriptions.md`),
   атомарные переходы «статус + outbox + аудит» (AD-002), идемпотентность (AD-003), аудит (AD-010).
2. **API ТСП** — новые методы `POST /v1/subscriptions`, `GET /v1/subscriptions/{id}`,
   `POST /v1/subscriptions/{id}/charges`, `POST /v1/subscriptions/{id}/revoke` по
   `openapi/tsp-api.yaml` v0.2.0 (аддитивно, без ломания v0.1-потребителей).
3. **Guard списания** — списание инициируется только при согласии в состоянии `ACTIVE` и в пределах
   параметров (получатель, лимит на списание, суммарный лимит, период); иначе — отказ без создания
   платежа (AD-009).
4. **Списание = платёж** — использование существующей статусной машины платежа; зачисление в АБС
   **только из `PAID`** (AD-005); повторные доставки идемпотентны.
5. **Отзыв согласия** — блокировка новых списаний; списание, подтверждённое НСПК как `PAID` до
   отзыва, доводится до зачисления; «неопределённое» состояние разрешается сверкой, не догадкой.
6. **Адаптер ОПКЦ (мок)** — consent-операции `registerConsent`/`getConsentStatus`/`revokeConsent` и
   события `consent.activated`/`consent.rejected`/`consent.revoked` (`docs/contracts/opkc-adapter.md`);
   реальный протокол НСПК НЕ реализуется (внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`).
7. **Нотификатор** — вебхуки `subscription.activated`, `subscription.revoked`, `charge.completed`
   с ретраями и DLQ (ADR-004).

Инварианты спайна обязательны: AD-001, AD-002, AD-003, AD-004, AD-005, AD-009, AD-010 (см.
`ARCHITECTURE.md`). Критерии приёмки — NFR §7 и EARS-критерии (`docs/nfr.md`,
`docs/solutioning-subscriptions.md` §6). Приоритет — доказать архитектуру сквозным сценарием
(согласие → списание → зачисление; отзыв; негативные сценарии), а не полнотой продукта.

## Контракт результата

Финальный ответ обязан завершаться JSON-объектом (после него — ни символа):

```json
{"status": "complete|partial|blocked", "assumptions": [], "open_questions": [], "conflicts_with_prior_decisions": []}
```

- `status`: `complete` — выполнено полностью; `partial` — частично; `blocked` — заблокировано.
- `assumptions`: допущения, принятые при реализации.
- `open_questions`: вопросы к архитектору.
- `conflicts_with_prior_decisions`: расхождения с принятыми решениями (ADR, spine) — **останавливают
  работу и эскалируются**, не отклоняются молча.

Ограничения — `CONSTRAINTS.yaml` (в этом пакете), рубрика приёмки — `RUBRIC.yaml`, эпик-контекст —
`ARCHITECTURE.md`. План отката — `DELTA.md` §«План отката».
