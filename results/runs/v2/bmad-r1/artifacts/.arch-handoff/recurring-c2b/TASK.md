# Задача для кодового харнесса (инкремент): рекуррентные C2B-списания (мандаты)

Инкремент к walking skeleton платёжного шлюза СБП (C2B-приём) по `docs/adr/ADR-008-recurring-c2b-mandate.md`, `docs/change/recurring-c2b-change-package.md` и контрактам v0.2. Реализовать поверх уже принятой архитектуры, не меняя существующий QR-поток.

1. **Мандат плательщика** — новый агрегат в БД шлюза со своей статусной машиной `CREATED → PENDING_CONSENT → ACTIVE → SUSPENDED → ACTIVE → … → REVOKED`/`EXPIRED`, плюс `DECLINED`; лимиты (`maxAmountPerDebit`, `maxTotalAmount` за период, `maxDebitsPerPeriod`, `validUntil`), `payerRef` (токенизирован, без полных ПДн), `consentRef`. Каждый переход — атомарная транзакция «статус + outbox + аудит».
2. **API ТСП v0.2 (аддитивно)** — `POST /v1/mandates`, `GET /v1/mandates/{mandateId}`, `POST /v1/mandates/{mandateId}/revoke`, `POST /v1/mandates/{mandateId}/payments`, `GET /v1/mandates/{mandateId}/payments`; новые схемы `Mandate*`; в `Payment` — только новые **опциональные** поля `initiationType`, `mandateId`. Существующие пути и значения `Payment.status` не менять.
3. **Рекуррентное списание — платёж в существующей статусной машине** (`CREATED → PAID → CREDITED → COMPLETED`, терминальный `FAILED`); состояние `QR_ISSUED` не используется. Зачисление — только из `PAID` (AD-005, AD-010).
4. **Guard-проверки до вызова ОПКЦ** (в одной транзакции с учётом расхода лимита): мандат `ACTIVE`; `amount ≤ maxAmountPerDebit`; сумма за период ≤ `maxTotalAmount`; число списаний за период ≤ `maxDebitsPerPeriod`; `now ≤ validUntil`; валюта совпадает; ТСП активен. Нарушение → `422`, вызова ОПКЦ и финансового действия нет.
5. **Идемпотентность**: создание мандата и списание — по `Idempotency-Key` (повтор → тот же ресурс); расход лимита — по `paymentId` (повтор не двоит); отзыв — по `mandateId` (повтор возвращает состояние, не ошибку); нотификации/события НСПК — по `eventId`.
6. **Мок-адаптер ОПКЦ расширить** мандатными операциями `registerMandate`, `getMandateStatus`, `revokeMandate`, `createDebit`, `getDebitStatus` и событиями `mandate.activated`/`mandate.declined`/`mandate.revoked`/`mandate.expired`/`debit.confirmed`/`debit.rejected`. Реальный протокол НСПК **не реализуется** (внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`); ядро остаётся контрактно-независимым от транспорта (AD-008).
7. **Нотификатор ТСП** — мандатные вебхуки `mandate.activated|declined|revoked|expired`; дебетовые исходы — существующими `payment.completed`/`payment.failed`.
8. **Тесты обязательны**, включая негативные и гонки: списание без `ACTIVE`-мандата; списание сверх лимитов; повтор с тем же `Idempotency-Key`; повтор события (`eventId`); гонка «отзыв ∥ списание»; недостижимость зачисления из `CREATED`; contract-compat test v0.1→v0.2 (нет удалённых полей, изменений `required` и enum `Payment.status`).

Spine-инварианты `ARCHITECTURE-SPINE.md` (AD-001..AD-010) обязательны. AD-009/AD-010 приняты как `Proposed` (ADR-008); если ратификация не подтверждена — считать их связывающими и при конфликте с любым принятым AD останавливать работу и эскалировать. Критерии приёмки — `docs/change/recurring-c2b-change-package.md` §6 и NFR `docs/nfr.md` §7 (выполнимы на моках). Приоритет — доказать архитектуру сквозным сценарием мандата, а не полнотой продукта.

## Контракт результата

Финальный ответ обязан завершаться JSON-объектом (после него — ни символа):

```json
{"status": "complete|partial|blocked", "assumptions": [], "open_questions": [], "conflicts_with_prior_decisions": []}
```

- `status`: `complete` — выполнено полностью; `partial` — частично; `blocked` — заблокировано.
- `assumptions`: допущения, принятые при реализации.
- `open_questions`: вопросы к архитектору.
- `conflicts_with_prior_decisions`: расхождения с принятыми ранее решениями (ADR, spine) — при непустом списке работа останавливается и эскалируется.

Архитектурный контекст инкремента — `ARCHITECTURE.md`, ограничения — `CONSTRAINTS.yaml`, решение — `adr/ADR-008-recurring-c2b-mandate.md`. Базовый пакет (walking skeleton) — в родительском каталоге `.arch-handoff/`.
