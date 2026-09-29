# Задача для кодового харнесса — инкремент «Подписки СБП»

Поверх walking skeleton (`.arch-handoff/TASK.md`) реализовать рекуррентные C2B-списания по согласию плательщика по решению `docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya.md` и спецификации `docs/spec/subscription-lifecycle.md`:

1. **API подписок** (аддитивно к v0.1, без ломающих изменений): `POST /v1/subscriptions`, `GET /v1/subscriptions`, `GET /v1/subscriptions/{id}`, `POST /v1/subscriptions/{id}/cancel`, `GET /v1/subscriptions/{id}/charges` — по `docs/contracts/tsp-api-subscriptions.md` и `openapi/tsp-api.yaml` (v0.2.0-draft).
2. **Агрегаты `Consent` / `Subscription` / `Charge`** со статусными моделями из `docs/spec/subscription-lifecycle.md`; атомарные переходы (статус + outbox + аудит в одной транзакции).
3. **Планировщик рекуррентных списаний**: идемпотентность по `occurrence = (subscriptionId, plannedAt)`; повторный запуск/реплей не создаёт второго `Payment`.
4. **Плановое списание = обычный `Payment`**: расширить статусную машину состоянием `DEBIT_REQUESTED` (`CREATED → DEBIT_REQUESTED → PAID`); денежный путь `PAID → CREDITED → COMPLETED` не менять; **зачисление только из `PAID`** (AD-005).
5. **Расширить мок-адаптер ОПКЦ**: операции автоплатежа (регистрация/статус согласия, инициирование списания, отмена) и события `consent.*`, `payment.paid/rejected` — нормализованные, с `eventId`.
6. **Вебхуки**: новые события (`subscription.*`, `charge.failed`, `consent.expired`) с ретраями/DLQ, как в walking skeleton.
7. **Планировщик/сверка**: ежечасная сверка согласий с моком ОПКЦ; обнаружение occurrence без исхода; fail-safe «локально `ACTIVE`, у ОПКЦ `REVOKED`» → стоп списаний.

**Что запрещено менять (связывающие решения, дословные Rule — в `ARCHITECTURE.md`):**

- Не менять денежный путь и запрет зачисления вне `PAID` (AD-005).
- Не выставлять внутренние состояния наружу: `DEBIT_REQUESTED` в `GET /v1/payments/{paymentId}` отдаётся как `CREATED`; enum `Payment.status` и обязательные поля v0.1 — без изменений (совместимость).
- Не добавлять в ядро знание протокола НСПК (AD-004); операции автоплатежа — только через контракт адаптера.
- Не выполнять списание без `Consent=ACTIVE` и `Subscription=ACTIVE` (AD-009).
- Не создавать два `Payment` по одной `occurrence` (AD-010).
- Конфликт с spine обязан **останавливать работу** и эскалироваться, а не разрешаться локально.

**Критерии приёмки** — позитивные П1–П3 и негативные Н1–Н8 из `docs/solutioning-subscriptions.md` §8 (дубль планировщика, отказ списания, отзыв согласия, превышение лимита, недоступность ОПКЦ, повтор нотификации, расхождение сверки, не-ломание потребителя v0.1). Измеримые пороги — `docs/nfr-subscriptions.md`.

**План отката** — `docs/solutioning-subscriptions.md` §9. Критерий успешного отката: 0 «осиротевших» occurrence, 0 списаний после отключения/отзыва, сверка сходится, обычный C2B-приём не деградирован.

**Технологический стек** — как в walking skeleton; обоснование изменений (если нужны новые компоненты, например планировщик) — ADR в рамках инкремента.

**Рубрика качества** — `.arch-handoff/RUBRIC.yaml`. Эпик-контекст — `ARCHITECTURE.md` этого инкремента; констрейнты — `CONSTRAINTS.yaml`.

## Контракт результата

Финальный ответ обязан завершаться JSON-объектом (после него — ни символа):

```json
{"status": "complete|partial|blocked", "assumptions": [], "open_questions": [], "conflicts_with_prior_decisions": []}
```

- `status`: `complete` — выполнено полностью; `partial` — частично; `blocked` — заблокировано (перечислить недостающие входы).
- `conflicts_with_prior_decisions` — любое расхождение с ADR/spine обязано быть перечислено и **эскалировано** (не разрешать локально).
