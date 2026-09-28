# Rubric review — ARCHITECTURE-SPINE.md (change 2026-09 «Подписки СБП»)

**Verdict: PASS WITH REQUIRED FIXES (not yet fit for ratification/handoff).** AD-009..012 name the right divergence points (mandate lifecycle, schedule ownership, idempotency key, revocation/consent), do not weaken AD-001..008 / ADR-001..007, and use stable monotonic IDs. But one Critical contradiction (the recurring charge's path to `PAID` does not exist in the inherited state machine) and four High gaps must be closed before A3 and before AD-009..012 are handed to the implementation teams.

Deliverable under judgement: `ARCHITECTURE-SPINE.md`. Context read: change package `docs/changes/2026-09-sbp-subscriptions/01..07`, `docs/adr/ADR-008..010`, `docs/spec/state-machine.md`, `docs/contracts/tsp-api.md`, `docs/contracts/opkc-adapter.md`, `openapi/tsp-api.yaml`.

## Checklist coverage (rubric items 1–6)

| # | Item | Result |
|---|---|---|
| 1 | Fixes real divergence points for the level below, misses none | **Partial** — mandate/scheduler/key/revocation fixed; `periodKey` contract value, the recurring field name, and the `CREATED → PAID` path are not (C1, H2, H4) |
| 2 | Every AD Rule enforceable and prevents its divergence | **Partial** — AD-009/010/012 rules have precision/ownership gaps (C1, H1, H3); AD-001..008 OK |
| 3 | Deferred cannot let two units diverge | **Partial** — two Deferred items do (H3, M6) |
| 4 | No new AD contradicts/weakens an earlier or inherited decision | **Pass with one caveat** — no weakening found; C1 is a *gap*, not a weakening, but it makes AD-010 unrealizable against ADR-002's transition table |
| 5 | No structural dimension left silent | **Partial** — security/ПДн retention (M4), deploy/rollback obligations (M5), operations/observability (L3) are decided only outside the spine |
| 6 | AD IDs stable/monotonic/non-reused | **Pass** — AD-001..012 strictly increasing, AD-009..012 appended after AD-008, no reuse, no dangling `AD-0xx` references |

---

## Critical

### C1. AD-010 mandates a charge path to `PAID` that the inherited state machine does not contain

- **File/section:** `ARCHITECTURE-SPINE.md` §AD-010 (Rule), §«Контракты и версии»; evidence in `docs/spec/state-machine.md` §2 (T2, T4) and §3.
- **What is wrong:** AD-010 requires the initiator to create the payment in `CREATED` and then says «дальнейшие переходы и зачисление — по общим правилам (зачисление **только из `PAID`**, AD-005)». But in the inherited machine the only entry to `PAID` is `T4: QR_ISSUED → PAID`, and `CREATED → QR_ISSUED` (T2) requires a `qrId` returned by `createPaymentLink`. A recurring debit calls `createRecurringDebit`, which returns only `ACCEPTED` and completes via the `payment.paid` event — it never produces a `qrId`. So a recurring charge in `CREATED` has **no legal transition to `PAID`**, while the spine simultaneously claims the payment state machine is reused unchanged.
- **Failure scenario:** the adapter delivers `payment.paid` for a charge that is still `CREATED`; unit A (scheduler/state machine) refuses the transition → the charge never reaches `PAID`, никогда не зачисляется, subscription silently stalls; unit B invents an unbound `CREATED → PAID`; unit C routes the charge through `QR_ISSUED` and issues a QR for a charge no payer will scan. Three implementations, three behaviours — exactly the divergence the spine exists to prevent. The package's own sequence diagram (`02-impact…` §2.4) already assumes the non-existent direct `CREATED → PAID`, confirming the ambiguity is load-bearing.
- **Concrete fix:** in AD-010's Rule, fix the entry point and the missing transition explicitly, e.g. «регулярное списание входит в машину в `CREATED`; перевод в `PAID` выполняется нотификацией НСПК `payment.paid` — переход `CREATED → PAID` (расширение ADR-002, добавляется в `docs/spec/state-machine.md` §2 и в fitness-набор); путь через `QR_ISSUED` для `recurring` запрещён (QR не выпускается)». Add one sentence to §«Контракты и версии», acknowledging that the payment transition table gains exactly this one transition (an extension of ADR-002, not a silent reuse). Reconcile ADR-008's `qrType = recurring` in the same pass (see H2).

---

## High

### H1. AD-011's `(mandateId, periodKey)` key as written forbids the дуннинг retries that ADR-010 requires

- **File/section:** `ARCHITECTURE-SPINE.md` §AD-011 (title and Rule); conflicting source `docs/adr/ADR-010…` §6 («каждая попытка — отдельная операция … **не более одного успешного** списания за период»).
- **What is wrong:** the AD title promises «Ровно одно списание на период», and the Rule says the natural key `(mandateId, periodKey)` «проверяется в одной транзакции с созданием платежа». Read literally, the first (possibly failing) attempt for a period claims the key, so a retry in the same period cannot create a payment — the дуннинг path ADR-010 §6 mandates becomes unreachable, or the key silently means "one *successful* charge" and the Rule text is wrong.
- **Failure scenario:** a charge fails for insufficient funds; dunning must retry within the same `periodKey`; unit A enforces a unique index on `(mandateId, periodKey)` → retry rejected → period lost; unit B treats the key as success-scoped → two attempts create two payment rows → reconciliation sees a double charge against AD-011.
- **Concrete fix:** state the invariant precisely, e.g. «ровно одно **успешное** списание на `(mandateId, periodKey)`; попытки (в т.ч. дуннинг) различаются `attemptNo`, уникальность `(mandateId, periodKey)` применяется к успешному/терминальному-успешному списанию (partial unique index), а не к любой попытке». Keep the title aligned with the corrected wording.

### H2. AD-010 does not name the field carrying `recurring`, and the bound ADR-008 uses a value that would break the additive contract the spine mandates

- **File/section:** `ARCHITECTURE-SPINE.md` §AD-010 («с типом `recurring`»), §«Контракты и версии» (strict additivity); conflicting sources `docs/adr/ADR-008…` §3 (`qrType = recurring`) vs `openapi/tsp-api.yaml` (`paymentType: [oneoff, recurring]`) and `docs/contracts/tsp-api.md` §3.2 (`qrType: dynamic | static | link`).
- **What is wrong:** the spine leaves «тип `recurring`» field-less. An implementer following the bound ADR-008 adds `recurring` to the existing `qrType` enum — which extends a v0.1 enum, contradicts «существующие типы и значения enum не расширяются» and breaks v0.1 consumers, i.e. violates the spine's own additivity rule. The v0.2 OpenAPI instead uses `paymentType`.
- **Failure scenario:** the ТСП-API unit implements `paymentType` (additive), the payment core implements `qrType=recurring` per ADR-008; the enum-guard test (`04-contract-changes.md` §3) fails or, worse, is relaxed, and a v0.1 consumer receiving `qrType=recurring` breaks.
- **Concrete fix:** in AD-010's Rule, name the marker as `paymentType: oneoff | recurring` (optional, absent = `oneoff`) and add «расширение enum `qrType` запрещено»; correct ADR-008 §3 accordingly. This is a one-line change that removes a whole class of divergence.

### H3. AD-012's payer-notification Rule is half-unenforceable, and the Deferred entry it points to lets the mandate and notifier units diverge

- **File/section:** `ARCHITECTURE-SPINE.md` §AD-012 (Rule) + §Deferred («Уведомление плательщика силами шлюза … до этого — внешнее допущение»); `docs/adr/ADR-009…` §6.
- **What is wrong:** the Rule states «каждое списание сопровождается уведомлением плательщика … (`[ТРЕБУЕТ ПРОВЕРКИ]`)» and binds «нотификатор», while the Deferred entry says it is not yet decided whether the gateway, the payer's bank or НСПК sends it. A Rule whose subject/owner is deferred cannot be enforced, and it is circular with the Deferred item: the Deferred item's return condition is the same unknown that the Rule depends on.
- **Failure scenario:** the mandate/scheduler unit assumes the gateway notifier sends the notice (and may gate charges on it); the notifier unit assumes НСПК/банк плательщика does → either no notice is ever sent (регуляторное нарушение) or two notices are sent; the fitness test «100 % списаний уведомлены» has no owner to point at.
- **Concrete fix:** split AD-012 into an unconditionally enforceable core and a deferred branch: core = «согласие и его доказательство — в неизменяемом аудите; отзыв обрабатывается приоритетно, немедленно блокирует новые списания и не может быть отменён ТСП»; deferred = «кто отправляет уведомление плательщику — шлюз или НСПК/банк плательщика; до решения владелец [НСПК/комплаенс] и срок возврата; обязанность шлюза вступает в силу только при решении "шлюз"». Then remove «нотификатор» from AD-012's Binds until that decision is made, or mark it as conditionally bound.

### H4. `periodKey` — a cross-boundary value exposed to ТСП and to the adapter — is neither fixed nor listed under Deferred

- **File/section:** `ARCHITECTURE-SPINE.md` §AD-011 («детерминированный `periodKey`») and §Deferred (absent); open question in `docs/contracts/tsp-api.md` §7.6 / `07-human-decisions.md` §7.4.
- **What is wrong:** AD-011 makes `periodKey` load-bearing (the natural key and the «ровно одно списание» proof), and the value crosses three unit boundaries: it is passed to `createRecurringDebit`, returned by `GET /v1/mandates/{mandateId}/charges?periodKey=`, and appears as `Payment.periodKey`. Its format, calendar and timezone are explicitly open (calendar month vs day-of-month vs UTC), and the spine's Deferred section does not mention it. Two units (scheduler and ТСП-API) therefore have no shared definition of the thing they must agree on.
- **Failure scenario:** the scheduler computes month-boundary `periodKey` in local time; the ТСП-API unit exposes/validates UTC or day-of-month form; the same charge appears under two different `periodKey` values, defeating the uniqueness proof and the charges listing.
- **Concrete fix:** pin the representation in AD-011 (at minimum: opaque canonical string, UTC-based, format fixed at A1 and versioned with the ТСП contract) **or** add an explicit Deferred entry with owner (НСПК + бизнес) and return condition, and state that until then `periodKey` is opaque to ТСП and generated only by the gateway.

---

## Medium

### M1. Дуннинг → `SUSPENDED` trigger/ownership is deferred outside the spine's Deferred section

- **File/section:** `ARCHITECTURE-SPINE.md` §AD-009 (Rule mentions «дуннинг/техблок») and §AD-011 («в пределах утверждённой политики»); §Deferred does not list the policy; the policy is deferred to human decisions in `07-human-decisions.md` §4.
- **Risk:** the scheduler unit and the mandate-lifecycle unit can diverge on who flips the mandate to `SUSPENDED`, and after how many failures.
- **Fix:** add a Deferred entry («политика дуннинга: число попыток, интервалы, порог `SUSPENDED`; владелец — продукт/риск») and bind the ownership in AD-009's Rule: «перевод мандата в `SUSPENDED` выполняет контур мандата по событию инициатора; инициатор сам статус мандата не меняет».

### M2. AD-009's limit wording is ambiguous and drops the `fixed` equality rule

- **File/section:** `ARCHITECTURE-SPINE.md` §AD-009 (Rule: «в пределах объявленного лимита»).
- **Risk:** "limit" can be read as per-charge (`maxAmount` = «лимит одного списания» per `openapi/tsp-api.yaml`) or cumulative over a period; and nothing in the spine's Rule forbids charging a *different* amount on a `fixed` mandate (the equality rule lives only in ADR-009 §3 / state-machine §8).
- **Fix:** restate in AD-009's Rule: «для `fixed` — сумма и период равны объявленным; для `variable` — сумма одного списания ≤ `maxAmount`; совокупный лимит за период не вводится этим решением (или вводится явно — тогда здесь же)».

### M3. AD-009 blocks only "новые" charges — the in-flight boundary is undefined

- **File/section:** `ARCHITECTURE-SPINE.md` §AD-009 (Rule) vs `docs/spec/state-machine.md` §8 and `06-acceptance…` AC-09.
- **Risk:** a revoke that arrives after a charge was created but before `PAID` is undefined: scheduler may re-read status and cancel, payment core may complete it and кредитовать. The package resolves this in AC-09/ADR-009 §4 ("уже подтверждённые НСПК доводятся") but the spine, which binds, does not.
- **Fix:** add to AD-009's Rule: «отзыв блокирует создание новых списаний; списание с уже подтверждённым НСПК статусом доводится по общим правилам; неподтверждённое — не инициируется; спорное — через возврат (AD-005/сага)».

### M4. Security/compliance: payer PII and consent-proof retention/erasure are silent in the spine

- **File/section:** `ARCHITECTURE-SPINE.md` §AD-007 (unchanged) and §AD-012; content lives only in `docs/adr/ADR-009…` §5/§7 and `05-nfr.md` §4.
- **Risk:** the mandate domain stores plательщик identifiers and consent proofs; 152-ФЗ retention and the impossibility of deleting mandates on rollback are load-bearing, yet no spine Rule binds them, and AD-009's Binds/Rule does not mention ПДн. (This is a *new* dimension for this feature, not merely an inherited one.)
- **Fix:** either extend AD-007's Binds/Rule to the mandate domain (ПДн минимизация/шифрование, маскирование в логах, retention доказательств согласия, запрет удаления при откате) or add a Deferred entry with ИБ/DPO owner and return condition.

### M5. Deploy/rollback obligations are not bound anywhere in the spine

- **File/section:** `ARCHITECTURE-SPINE.md` — absent; content lives in `06-acceptance-and-rollback.md` §3.
- **Risk:** «откат = не включать» (фиче-флаг) and «stop-new сохраняет обязательства; мандаты и доказательства не удаляются» are financially/регуляторно load-bearing, and a unit may implement rollback as data deletion.
- **Fix:** add one Rule clause (in AD-012 or a new AD): «функция включается/выключается фиче-флагом; откат не удаляет мандаты и доказательства согласия и сохраняет обязательства по отзыву/уведомлению и доведению начатых списаний».

### M6. Deferred «Charge-on-demand» does not fix who owns `periodKey` in that mode

- **File/section:** `ARCHITECTURE-SPINE.md` §Deferred (charge-on-demand item).
- **Risk:** it declares «общий натуральный ключ `(mandateId, periodKey)`» but in a ТСП-initiated model the ТСП has no period concept; the scheduler unit and the ТСП-API unit can diverge on whether ТСП sends `periodKey` or the gateway derives it from `nextChargeAt`, and arbitrary ТСП-driven charges may collide with scheduled periods.
- **Fix:** add to that Deferred item: «владелец `periodKey` даже при charge-on-demand — шлюз (выводит из расписания/`nextChargeAt`); ТСП передаёт только `mandateId`; ключ остаётся `(mandateId, periodKey)`».

### M7. The mandate→ТСП notification path (`mandate.*`) is not bound

- **File/section:** `ARCHITECTURE-SPINE.md` §AD-009 (Binds lacks «нотификатор»); §AD-002's outbox Rule is scoped to «финансовый статус платежа».
- **Risk:** who emits and delivers `mandate.activated/revoked/suspended/expired` (ordering, at-least-once, дедуп по `eventId`) rests on inherited ADR-004 and is not bound to the mandate unit — mandate lifecycle and notifier units can diverge on emission timing (e.g. emit on transition vs. on outbox poll).
- **Fix:** add «нотификатор ТСП» to AD-009's Binds and one clause: «события `mandate.*` публикуются через тот же outbox/нотификатор, что и `payment.*` (AD-002/ADR-004); дедуп — по `eventId`».

---

## Low

- **L1. AD-009's Rule defers atomicity to AD-002, whose Binds/Rule is payment-scoped.** `ARCHITECTURE-SPINE.md` §AD-002 («Изменение финансового статуса **платежа**…»; Binds = «БД шлюза (состояние платежа)»). AD-009 cites `(AD-002, AD-003)`, which a literal reader can dismiss as not applying to a mandate. Fix: restate the requirement in AD-009 («смена статуса мандата, запись outbox и аудита — в одной локальной транзакции БД шлюза») or extend AD-002's Binds/Rule to cover any aggregate whose state gates money movement.
- **L2. AD-010's «тем же сервисным путём, что и API ТСП» is not precise enough to enforce the "no second path" claim.** Fix: «через тот же доменный сервис создания платежа (не через внешний HTTP API, не прямой записью в БД); fitness: единственная точка создания `CREATED`».
- **L3. Operations/observability of the scheduler is decided only outside the spine.** `ADR-010` §7 and `05-nfr.md` §4 define lag/catch-up/dunning/DLQ signals, but no AD Rule binds them, so the scheduler and ops/monitoring units can diverge on what is emitted. Fix: add a clause to AD-011 («инициатор обязан публиковать lag, число catch-up, дуннинг-ретраи, отказы и глубину DLQ — пороги по NFR §7») or explicitly note that ADR-010 §7/NFR §7 are binding for the scheduler.
- **L4. Dual `AD-0xx` / `ADR-0xx` namespaces read confusingly** (e.g. `AD-009` status «(ADR-008, ADR-009; ждёт A3)» looks self-referential). IDs themselves are correct, stable and non-reused (rubric item 6 = pass). Fix (optional): one legend line at the top of the spine — «`AD-0xx` — инварианты spine; `ADR-0xx` — отдельные записи решений».

---

## Notes on the other rubric items (no finding)

- **Item 3, remaining Deferred items** («Мультивалютность», «C2C/B2C/B2B», «Диспуты») are out of scope with stated return conditions and cannot let the mandate/scheduler/API/adapter units diverge. Only the payer-notification (H3) and charge-on-demand (M6) entries do.
- **Item 4, weakening:** no new AD weakens an old one — AD-009/010/011 explicitly preserve AD-002/003/005/008 and ADR-002/005/007/008; AD-012 strengthens AD-007. The only failure of this kind is C1, which is a *gap against ADR-002's transition table*, not a weakening.
- **Item 6, IDs:** AD-001..012 monotonic; AD-009..012 appended after AD-008; no AD ID reused and no dangling references to AD IDs ≥ 013 in the repo.
