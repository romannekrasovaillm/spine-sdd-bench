# Дельта: recurring-subscriptions

- Route: Critical (score 8/15: new_component, new_datastore, cross_domain_integration, api_contract_change, data_contract_change, consistency_model_change, significant_nfr, financial_impact)
- Created: 2026-09-28
- ADR: `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelschika-sbp-podpiski.md` (Proposed, выносится на A3)

## Проблема

ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — «подписки СБП». Сейчас каждый платёж требует QR и действия клиента. Нужно однократное согласие плательщика (мандат) с лимитами, после которого ТСП инициирует списания без участия плательщика в каждом платеже, в пределах согласия.

## ADDED

- **`ARCHITECTURE-SPINE.md`**: инвариант `AD-009` (рекуррентное списание — только под активным согласием, в пределах лимитов) и `AD-010` (жизненный цикл согласия — отдельная машина состояний; отзыв немедленно запрещает новые списания). Статус `Proposed` (ADR-008).
- **`docs/adr/ADR-008-*.md`**: архитектурное решение (оценка значимости, влияние на AD-001…AD-008, альтернативы, последствия, обратимость, критерии приёмки, план отката, открытые вопросы для человека).
- **`docs/spec/recurring-consent.md`**: машины состояний согласия (`CREATED → PENDING_CONFIRMATION → ACTIVE → REVOKED/EXPIRED/PAUSED`) и рекуррентного списания (`CREATED → PAID` без `QR_ISSUED`), переходы, идемпотентность, гонка отзыва, сверка.
- **`docs/nfr.md` §7**: измеримые NFR рекуррентных списаний (латентность, отказ после отзыва ≤ 1 с, отсутствие двойных списаний, сверка согласий).

## MODIFIED

- **`openapi/tsp-api.yaml`**: версия `0.1.0 → 0.2.0`; аддитивно добавлены `/v1/consents`, `/v1/consents/{id}`, `/v1/consents/{id}/payments`, `/v1/consents/{id}/revoke|pause|resume` и схемы `Consent`/`ConsentRequest`/`RecurringPaymentRequest`; в `Payment` добавлены опциональные `paymentType`/`consentId`. Существующие `/v1/payments` не изменены.
- **`docs/contracts/tsp-api.md`**: `v0.1 → v0.2 draft`; добавлены §3.6–3.9 (согласие и рекуррентное списание), коды ошибок `CONSENT_*`, вебхуки `consent.*`, открытые вопросы.
- **`docs/contracts/opkc-adapter.md`**: аддитивно добавлены операции `createConsent`/`getConsentStatus`/`initiateRecurringDebit`/`revokeConsent` и события `consent.*`.
- **`docs/rfp/vendor-rfp.md`**: критерий допуска `G8` (поддержка рекуррентных операций НСПК) и сценарий POC `P9`.
- **`docs/solutioning.md` §11**, **`README.md`**: указатели на пакет изменения.

## REMOVED

- Нет. Ни один существующий Rule (`AD-001…AD-008`) не изменён и не удалён; изменение — чисто аддитивное.

## План отката

- До боевой эксплуатации: откат = не включать фичу (аддитивно, обратимо).
- После включения: фиче-флаг приёма согласий; `stop-new` (запрет новых согласий/списаний) без остановки обработки уже открытых платежей; откат релиза — rolling.
- Сигналы отката: рост DLQ по событиям согласия; расхождение сверки согласий с НСПК > 0; двойное списание или списание после отзыва (даже 1 случай — стоп-сигнал).
- Владелец решения: платёжный контур (solution-architect + SRE), эскалация — A3-владелец.

## Критерии приёмки

- [ ] `arch control check` и `arch gate` зелёные (delta_guard видит эту дельту; spine_lint чист).
- [ ] `openapi/tsp-api.yaml` валиден; существующие `/v1/payments`, `GET /v1/payments/{id}`, refunds не изменились (регресс по v0.1).
- [ ] Списание не создаётся при `consent.status != ACTIVE`, сверх `perDebitLimit`/`maxTotal`/срока, при несовпадении ТСП (AD-009).
- [ ] После `REVOKED`/`EXPIRED` новые списания отклоняются; уже `PAID`-списания доводятся до `COMPLETED` (AD-010).
- [ ] Идемпотентность: повтор `POST /consents`/`POST /consents/{id}/payments` и повтор событий `eventId` — без дублей (AD-003).
- [ ] Рекуррентное списание зачисляется только из `PAID`; двойных зачислений — 0 (AD-005).
- [ ] NFR из `docs/nfr.md` §7 выполнены (латентность, точность, отсутствие дублей).
- [ ] Тест гонки «отзыв параллельно со списанием» даёт ровно один исход без зависшего `CREATED`.
