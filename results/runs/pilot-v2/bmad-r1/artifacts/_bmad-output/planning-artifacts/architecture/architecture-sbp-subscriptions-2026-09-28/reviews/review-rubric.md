# Rubric walk — ARCHITECTURE-SPINE change «СБП subscriptions (recurrent C2B debits by payer consent)»

- Reviewer: independent architecture reviewer (rubric walker), read-only
- Date: 2026-09-28
- Deliverable under review:
  - `ARCHITECTURE-SPINE.md` (AD-001…AD-008 inherited vs new AD-009…AD-011)
  - `docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelschika.md`
  - `docs/spec/mandate-lifecycle.md`, `docs/spec/state-machine.md`
  - `docs/contracts/tsp-api.md` (v0.2), `docs/contracts/opkc-adapter.md` (v0.2)
  - supporting: `openapi/tsp-api.yaml` v0.2.0-draft, `docs/nfr.md` §7, `docs/solutioning.md` §11, `_bmad-output/.../ARCHITECTURE-DECISION-SBP-SUBSCRIPTIONS.md`, `.arch-handoff/subscriptions/*`
- Method: walk the 6-point good-spine checklist against the artifacts above; report only defects that are real (a divergence point two units could implement incompatibly, an unenforceable/incomplete Rule, an internal contradiction, or a dimension left undecided without being deferred).

## Verdict

**pass-with-findings** — 0 critical, 2 high, 4 medium, 2 low.

No inherited invariant (AD-001…AD-008) is weakened or silently overridden; the one place where the new work extends an inherited decision (ADR-002's canonical FSM) is explicitly surfaced as an additive extension (ADR-008 decision package §8). The change is nevertheless not yet divergence-free at the altitude it claims: two contract-visible parameters/behaviours are not governed by any invariant, one Rule's consistency mechanism is unspecified, and one payment transition is referenced but not defined.

## Findings

### R-01 [HIGH] `maxTotalAmount` (cumulative limit) is contract-visible but governed by no AD and appears in no spec

- Files: `ARCHITECTURE-SPINE.md` AD-009…AD-011; `docs/spec/mandate-lifecycle.md`; compared with `docs/contracts/tsp-api.md` §3.6/§3.7/§4 and `openapi/tsp-api.yaml` (`MandateRequest.maxTotalAmount`, `Mandate.maxTotalAmount`), `docs/contracts/opkc-adapter.md` (`createMandate`).
- What: the public contract exposes `maxTotalAmount` as an optional cumulative cap and commits to enforcing it — `MANDATE_LIMIT_EXCEEDED (422, «amount > maxAmountPerCharge» или превышен `maxTotalAmount`)`. But:
  - ADR-008 Decision 1 lists the mandate parameters (`maxAmountPerCharge`, `validFrom/validTo`, …) and **omits `maxTotalAmount`** entirely;
  - AD-011's Rule states the charge guard as «`ACTIVE` ∧ `amount ≤ maxAmountPerCharge` ∧ текущее время в периоде действия ∧ `tspId` совпадает…» — no cumulative limit;
  - `mandate-lifecycle.md` §4 repeats the same four-term guard and never mentions `maxTotalAmount` anywhere in the document.
- Why it matters (divergence): the level below has two units — the charge API (per-charge check) and the mandate aggregate (running total). Nothing tells them how to accumulate, when to reject, or whether the check must be in the same transaction. One implementer reads the contract and enforces it; another reads the spine/lifecycle and does not. Result: charges that individually pass `maxAmountPerCharge` can exceed the total the payer consented to — the exact "списание … сверх лимита" class AD-011 claims to prevent.
- Fix: add `maxTotalAmount` to AD-011's Rule (including "накопленная сумма подтверждённых списаний мандата"), or explicitly defer/remove it from the contract. If kept, it needs the same transactional treatment as `maxAmountPerCharge` (and its own concurrency story).

### R-02 [HIGH] Charge-vs-revocation linearizability is asserted but the mechanism is unspecified; AD-011's wording is self-contradictory

- Files: `ARCHITECTURE-SPINE.md` AD-011; `docs/spec/mandate-lifecycle.md` §3, §4, М5/М7.
- What: AD-011 `Prevents`: «отзыв согласия, не остановивший новые списания». Rule: «…проверяется в одной транзакции с созданием платежа… Отзыв или приостановка мандата **в той же транзакции** запрещает новые списания.» The phrase «в той же транзакции» is ungrammatical/ambiguous: revocation runs in its own transaction (М5/М7), so "the same transaction" can only refer back to the charge transaction — but a revocation cannot be performed inside the charge transaction. An implementer cannot derive from the Rule what serialization is required.
- Why it matters (divergence/race): with ordinary READ COMMITTED, transaction T_charge can read mandate `ACTIVE`, then T_revoke commits `REVOKED`, then T_charge inserts the payment and commits — a charge is created after revocation. `mandate-lifecycle.md` §4 only says "в одной транзакции", and `docs/nfr.md` §7 demands «Списаний после отзыва мандата = 0 … p99 < 2 с», which such an interleaving violates. Two units (charge API and mandate lifecycle) can each be "compliant" under different locking/versioning choices.
- Fix: state the concurrency control in the Rule — e.g. the charge transaction must take a row lock / compare-and-set on the mandate aggregate (`SELECT … FOR UPDATE` or an optimistic `version`), so that charge-creation and revoke/suspend serialize; and reword AD-011's last sentence ("commit of a revocation/suspension must prevent any charge that has not already passed the guard").

### R-03 [MEDIUM] `CREATED → EXPIRED` is referenced for mandate charges but the transition is not defined; `state-machine.md` §2а claims T13 is the only addition

- Files: `docs/spec/mandate-lifecycle.md` §4 vs `docs/spec/state-machine.md` §2 (T-table), §2а.
- What: `mandate-lifecycle.md` §4 states «`CREATED → EXPIRED`/`FAILED` — как у обычного платежа (отказ/таймаут)». But the ordinary-payment FSM has no `CREATED → EXPIRED`: T3 is `CREATED → FAILED`, and T5 is `QR_ISSUED → EXPIRED`. `state-machine.md` §2а asserts «Добавлен только переход **T13** (`CREATED → PAID` без `QR_ISSUED`); все остальные состояния, переходы … без изменений.» The same §4 diagram also contradicts its own text (only `FAILED` is drawn from `CREATED`).
- Why it matters: a charge has no QR/TTL, so "expire while awaiting OPKC confirmation" is plausibly needed — but it is undefined. One unit will leave a stuck charge in `CREATED` forever; another will invent a transition. Either the FSM needs a defined `CREATED → EXPIRED` (or an explicit statement that a mandate charge can never expire from `CREATED`), or §4's text is wrong.
- Fix: reconcile the two files — add the transition to the T-table (and drop the "only T13" claim) or remove the claim from `mandate-lifecycle.md` §4.

### R-04 [MEDIUM] Mandate lifecycle transitions M6 (resume) and M9 (expire) have no corresponding webhook event; M4 maps consent-expiry to `mandate.rejected`

- Files: `docs/spec/mandate-lifecycle.md` §2 (M4/M6/M9), §7; `docs/contracts/tsp-api.md` §5.
- What: `tsp-api.md` §5 defines exactly four mandate events: `mandate.activated`, `mandate.rejected`, `mandate.revoked`, `mandate.suspended`. There is no `mandate.resumed` and no `mandate.expired`. Yet M6 (`SUSPENDED → ACTIVE`, resume) and M9 (`ACTIVE → EXPIRED`) both end with "…, outbox, аудит" without naming an event; M4 (`PENDING_CONSENT → EXPIRED`) tells the TSP `mandate.rejected` even though the consent merely timed out.
- Why it matters: the TSP side is a separate implementation unit whose whole subscription-billing loop depends on mandate state. Without a defined outward event, one TSP will poll, another will assume `mandate.activated` is reused for resume, a third will never learn the mandate expired — and the `mandate.rejected` hijack in M4 is a semantic mismatch that will surface as a support defect. The spine's own `mandate-lifecycle.md` §7 asserts the outward status set is complete.
- Fix: add `mandate.resumed` / `mandate.expired` (or explicitly state that resume reuses `mandate.activated` and expiry reuses `mandate.revoked`/`rejected`), and name the event in each M-row's action.

### R-05 [MEDIUM] The operational envelope is decided only in downstream documents, not at the spine altitude

- Files: `ARCHITECTURE-SPINE.md` (AD-009…AD-011, Deferred) vs `docs/adr/ADR-008` Reversibility, `ARCHITECTURE-DECISION-…` §6.2, `docs/nfr.md` §7.
- What: the rubric asks whether every dimension the altitude owns is decided, deferred, or an open question. For this change the following operational dimensions are decided **outside** the spine and are not even named in it (not under Deferred, not as an open question):
  - rollout/isolation: per-TSP feature flag / kill-switch («Выключение подписок для ТСП не влияет на QR-приём»);
  - rollback: managed revocation of active mandates, "no data rollback", RTO ≤ 1 h, decision owner;
  - reconciliation ownership/cadence for mandates (only `mandate-lifecycle.md` §6 gives an hourly target and stop-signal handling).
- Why it matters: the spine is the artifact the level below inherits; AD-001…AD-008 stayed silent on ops too, but this change adds a *customer-facing kill switch* and a *revocation-based rollback* that are materially different from "don't deploy". If they live only in the ADR/decision doc, the code handoff (`TASK.md` item 9) is the only place they are binding, and the ops unit is not bound by the spine.
- Fix: add one spine block (or a Deferred entry) covering: per-TSP enable/disable semantics, rollback = revocation + kill-switch with owner, mandate-reconciliation cadence and stop-signal runbook owner.

### R-06 [MEDIUM] Charge idempotency semantics disagree between `mandate-lifecycle.md` §5 and `tsp-api.md` §3.9 / ADR-008 §5

- Files: `docs/spec/mandate-lifecycle.md` §5; `docs/contracts/tsp-api.md` §2, §3.9, §4; `docs/adr/ADR-008…` Decision 5.
- What: `mandate-lifecycle.md` §5 lists the idempotency key for a charge as `Idempotency-Key` **plus** (`mandateId`, `merchantOrderId`/период) and says a repeat returns «тот же `paymentId`, второго списания … нет; конфликт периода — `409`». `tsp-api.md` §3.9 and ADR-008 §5 say a repeat `merchantOrderId`/период within a mandate is `409 MANDATE_CHARGE_CONFLICT` — regardless of `Idempotency-Key`. So for the same `(mandateId, merchantOrderId)` with a **different** `Idempotency-Key`, one doc implies "same `paymentId`", the other "409". A merchant retry after a client crash (new key) is exactly this case.
- Why it matters: charge API and persistence are separately built units; the retry-after-crash path is the highest-frequency real-world trigger. Divergent handling produces either duplicate-looking failures or missed idempotency, and it contradicts the `Prevents` of AD-010.
- Fix: state one precedence rule (recommended: `(mandateId, merchantOrderId)` is the primary uniqueness key → return the existing `paymentId` with 200 even under a new `Idempotency-Key`; `409` only when the same order id carries a *different* amount/purpose), and align all three documents.

### R-07 [MEDIUM] AD-009's Rule does not cover its own stated `Prevents` (gateway↔OPKC consent divergence)

- Files: `ARCHITECTURE-SPINE.md` AD-009.
- What: AD-009 `Prevents` includes «расхождение "шлюз считает согласие действующим — банк плательщика считает его отозванным"». The Rule, however, only covers storage ("отдельный агрегат"), atomic transitions, and `opkcMandateRef` — it says nothing about detecting or repairing that divergence. The reconciliation duty appears only in `Binds` («сверка с ОПКЦ»); the concrete stop-signal behaviour lives in `mandate-lifecycle.md` §6. At spine altitude the anti-divergence mechanism for AD-009's headline risk is therefore not in the Rule, unlike AD-002/AD-003/AD-005 which carry their fitness/mechanism inline.
- Why it matters: `Binds` is a scope statement, not a `Rule`; a unit reading the spine gains no obligation to reconcile the mandate aggregate. Given the pre-signed-consent model (payer revokes in their own bank), this is the risk most likely to produce an unauthorised debit.
- Fix: move the stop-signal into AD-009's Rule (mandatory periodic reconciliation of `ACTIVE`/`SUSPENDED`/`PENDING_CONSENT` mandates; "OPKC revoked & local ACTIVE" → immediate local `REVOKED` + alert), with a fitness check as in AD-002/AD-005.

### R-08 [LOW] Pre-existing: ADR-002's canonical states/substates differ from `state-machine.md` (not caused by this change)

- Files: `docs/adr/ADR-002…` Decision 1 vs `docs/spec/state-machine.md` §1.
- What: ADR-002 lists terminal `REVERSED` and substates `NOTIFY_SENT` / `ABS_IN_PROGRESS`; `state-machine.md` has no `REVERSED` and uses `NOTIFY_PENDING` / `ABS_PENDING`. The mandate change does not touch this, but it demonstrates that the "canonical state list kept in one place (spine)" that ADR-002 itself calls for is still not true.
- Why it matters: low for this change; flagged for completeness under checklist item 6 (state named in one place, absent in another). Pre-existing, out of scope for ADR-008.

## Checklist walk (per rubric item)

1. **Real divergence points fixed, none missed?** Mostly yes for the mandate aggregate, the charge path, revoke/suspend semantics, API and adapter surface. Missed: the cumulative limit `maxTotalAmount` (**R-01**), charge-vs-revoke linearizability (**R-02**), resume/expiry outward events (**R-04**), charge-idempotency precedence (**R-06**). Verdict: partial.

2. **Every Rule enforceable and does it prevent its divergence?** AD-002/AD-003/AD-005-style fitness is present for the inherited invariants. AD-010 is enforceable (T13 + explicit idempotency extension). AD-009's Rule does not carry the mechanism for its own headline `Prevents` (**R-07**). AD-011's Rule (i) omits `maxTotalAmount` (**R-01**) and (ii) does not state the serialization mechanism for "revocation stops new charges" (**R-02**). Verdict: partial.

3. **Deferred still safe?** Deferred correctly keeps the bank scheduler out with an explicit trigger to revisit, and the scope return (`solutioning.md` §1) is consistent. Residual divergence risks that are *not* in Deferred: `maxTotalAmount` (**R-01**) and the notification-before-charge enforcement point (below, item 5). Disputes/chargebacks remain inherited-Deferred; it would be worth noting whether a disputed *mandate* charge also suspends the mandate, but that is arguably parent-level scope. Verdict: pass, with the two caveats above.

4. **Any new AD weakening/contradicting AD-001…AD-008?** No. AD-009/AD-010/AD-011 are additive; AD-005 is explicitly preserved; AD-001/AD-004/AD-006/AD-007 are unaffected; AD-008 [ADOPTED] is inherited (transport still vendor-bound and blocked on НСПК docs). The extension of ADR-002's FSM (`QR_ISSUED` previously the canonical path) is surfaced, not silently overridden (ADR-008 decision package §8). Verdict: pass.

5. **Every altitude-owned dimension decided/deferred/open?** Domain model, idempotency, limits (except cumulative), contracts, reversibility: decided. Protocol semantics, legal model, limits/risk policy, PDn/КИИ, commission: correctly flagged open. Under-covered: the operational envelope — rollout/kill-switch, rollback ownership, mandate-reconciliation owner (**R-05**) — and the notification-before-charge *enforcement point*: AD-011 names the requirement but not who enforces it, `tsp-api.md` §3.9 makes `noticeRef` optional, and `docs/nfr.md` §7 demands 100% compliance, so the gateway unit and the TSP unit can each assume the other does it. Verdict: partial.

6. **Internal inconsistencies across spine / ADR-008 / mandate-lifecycle / contracts?**
   - `CREATED → EXPIRED` referenced by `mandate-lifecycle.md` §4 but undefined in `state-machine.md`, which claims T13 is the only change (**R-03**).
   - Charge-idempotency precedence: `mandate-lifecycle.md` §5 vs `tsp-api.md` §3.9 / ADR-008 §5 (**R-06**).
   - `maxTotalAmount`: present in `tsp-api.md`/`openapi`, absent from ADR-008 Decision, AD-009…011 and `mandate-lifecycle.md` (**R-01**).
   - Mandate events: M6/M9 define transitions whose outward event does not exist in `tsp-api.md` §5; M4 maps `EXPIRED` to `mandate.rejected` (**R-04**).
   - AD-011 Rule wording «в той же транзакции» is incoherent (**R-02**).
   - Naming: `docs/solutioning.md` §1 writes the change as "(AD-008, см. §11)", colliding with spine AD-008 (hybrid strategy); it should be ADR-008. LOW, cosmetic, but it is a real cross-reference error in a document the ADR lists as touched.
   - `opkc-adapter.md` `revokeMandate` is described as «отзыв/приостановка согласия» while the response is `REVOKED`, and `getMandateStatus` has no `SUSPENDED`; the gateway's resumable `SUSPENDED` therefore has no OPKC mirror, and `mandate-lifecycle.md` §6's reconciliation list does not cover "we SUSPENDED / OPKC ACTIVE". LOW — currently benign (local suspension is strictly more restrictive, and suspend does not call the adapter per M5), but it is an unstated assumption.
   - Pre-existing: ADR-002 `REVERSED`/substate names vs `state-machine.md` (**R-08**).
   Verdict: partial.

## What is sound (no finding)

- The central architectural move — mandate as a separate aggregate, charge as an ordinary payment of the existing FSM, credit still gated on `PAID` — is the correct anti-divergence choice and is carried consistently through spine, ADR, lifecycle, contracts and NFR.
- Additive-only contract evolution (`/v1` preserved, optional `Payment` fields, "ignore unknown events") is consistently stated in ADR-008, `tsp-api.md` §6 and `openapi`.
- `transport.unavailable` / fail-closed behaviour, vendor RFP obligations and the "no charge blindly" prohibition are coherently surfaced as open questions (A2) rather than decided silently.
- Scope return (subscriptions out of roadmap, bank scheduler kept Deferred with a return condition) is properly registered in `solutioning.md` §1/§11 and the spine Deferred.

## Bottom line

The change is architecturally coherent and does not weaken the accepted spine. It is not yet a divergence-free spine for the level below: `maxTotalAmount` and the charge/revoke serialization are the two places where two units can be simultaneously "compliant" and still violate a stated `Prevents`. Close R-01 and R-02 (and reconcile R-03/R-04) before handoff; R-05/R-06/R-07 should be resolved or explicitly deferred at spine altitude.
