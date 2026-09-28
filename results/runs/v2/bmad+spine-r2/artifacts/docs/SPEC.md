# SPEC — Подписки СБП (рекуррентные C2B-списания по согласию плательщика)

- Status: Draft (proposal; вход A3)
- Owner: solution-architect (платёжный контур)
- Связано: `docs/adr/ADR-008…010`, `ARCHITECTURE-SPINE.md` AD-009/AD-010, `changes/subscriptions-c2b/DELTA.md`
- Тип: аддитивное расширение (`spec_or_delta`) — изменение относительно принятого решения, не система целиком

## 1. Требования (EARS)

- **REQ-SUB-1.** When ТСП регистрирует подписку, the шлюз shall создать согласие через адаптер ОПКЦ и хранить согласие/подписку как источник истины в своём контуре.
- **REQ-SUB-2.** If согласие не `ACTIVE`, then the шлюз shall отклонить рекуррентное списание, не обращаясь к НСПК.
- **REQ-SUB-3.** When приходит повторная попытка за `(subscriptionId, billingPeriod)`, the шлюз shall вернуть существующую попытку и не создать второе списание/проводку.
- **REQ-SUB-4.** If сумма/период/срок/число списаний вне условий согласия, then the шлюз shall отклонить списание без обращения к НСПК.
- **REQ-SUB-5.** When приходит подтверждение НСПК, the шлюз shall зачислить только из состояния `PAID`.
- **REQ-SUB-6.** When согласие отозвано, the шлюз shall в одной транзакции запретить новые списания и записать событие/аудит; подтверждённые — не откатывать автоматически.
- **REQ-SUB-7.** The шлюз shall доставлять события `subscription.activated`, `subscription.revoked`, `debit.completed`, `debit.failed` с at-least-once и дедупликацией по `eventId`.
- **REQ-SUB-8.** The шлюз shall сверять план ↔ НСПК ↔ АБС и публиковать метрики планировщика.

## 2. Функциональная спецификация

- **Компоненты (в контуре шлюза):** реестр согласий/подписок; планировщик рекуррентных списаний (HA); переиспользуются статусная машина, outbox, нотификатор, сверка, АБС-адаптер, адаптер ОПКЦ (расширяется).
- **Жизненный цикл подписки/согласия:** `PENDING_CONSENT → ACTIVE → (SUSPENDED ↔ ACTIVE) → REVOKED | EXPIRED` (терминальные `REVOKED`, `EXPIRED`). Полная таблица переходов — `docs/spec/subscription-state-machine.md`.
- **Жизненный цикл списания:** `SCHEDULED → CREATED → PAID → CREDITED → COMPLETED`; терминальные `FAILED`, `SKIPPED`; зачисление — только из `PAID`.
- **Идемпотентность:** API `POST` — `Idempotency-Key`; списание — ключ `(subscriptionId, billingPeriod)`; события — `eventId`; АБС — `debitId`.
- **Отзыв/приостановка:** транзакционный запрет новых списаний; компенсация уже подтверждённых — возврат (сага ADR-005).
- **Сверка:** план ↔ подтверждение НСПК ↔ зачисление АБС; расхождения — в отчёт незавершённых операций.

## 3. Изменения контрактов (неразрушающие, ADR-010)

- **API ТСП** (`openapi/tsp-api.yaml`, v0.2.0): `POST /v1/subscriptions`, `GET /v1/subscriptions/{id}`, `POST /v1/subscriptions/{id}/cancel`, `POST /v1/subscriptions/{id}/debits`, `GET /v1/subscriptions/{id}/debits/{debitId}`; новые схемы `SubscriptionRequest/Subscription/DebitRequest/Debit/Problem`; новые коды ошибок и события вебхуков. Подтверждено: `contract_diff` 0.1.0→0.2.0 — breaking: 0; `openapi_lint` — PASS.
- **Контракт адаптера ОПКЦ** (`docs/contracts/opkc-adapter.md`, v0.2): +`registerSubscription`, `getSubscriptionStatus`, `cancelSubscription`, `createDebit`, `getDebitStatus`; +события `subscription.activated/revoked`, `debit.paid/rejected`; идемпотентность `createDebit` по (`consentId`, `billingPeriod`).
- **RFP вендора:** расширен (scope п.7, G3, §4 методы/события, POC P9–P11).

## 4. Нефункциональные требования

Измеримые NFR подписок — `docs/nfr.md` §7: своевременность (≥99,5 % в окне ±30 мин, p95 ≤ 5 мин), двойные списания за период = 0, списания после отзыва = 0, применение отзыва ≤ 5 мин, масштаб ≥ 1 млн согласий (baseline), массовые списания 200/500 TPS с управлением темпом, RPO=0, RTO ≤ 1 ч, лаг планировщика p99 ≤ 15 мин, аудит жизненного цикла согласия 100 %.

## 5. Критерии приёмки

См. `ACCEPTANCE.md` (AC-1…AC-20), включая негативные сценарии (нет согласия → нет списания; дубль периода; отзыв в процессе; отказ АБС; гонка) и критерий успешного отката.

## 6. Вне scope (Deferred)

Upgrade/downgrade условий подписки, списание по требованию без расписания, пулы/мультиподписки, C2C/выплаты, диспуты (см. spine `Deferred`).

## 7. Открытые внешние входы

Протокол НСПК по подпискам, правовая форма/основание согласия (152-ФЗ/161-ФЗ), поддержка подписок вендором транспорта — см. `DECISION.md` и `changes/subscriptions-c2b/DELTA.md`.
