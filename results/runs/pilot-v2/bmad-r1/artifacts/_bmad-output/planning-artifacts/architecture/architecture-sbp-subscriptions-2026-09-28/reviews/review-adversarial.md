# Adversarial review — ARCHITECTURE-SPINE.md as amended by the SBP subscriptions change (AD-009…AD-011)

- Date: 2026-09-28
- Reviewer: adversarial architecture reviewer (read-only pass)
- Artifact under attack: `ARCHITECTURE-SPINE.md` (AD-001…AD-011), `docs/adr/ADR-008-*.md`, `docs/spec/mandate-lifecycle.md`, `docs/spec/state-machine.md`, `docs/contracts/tsp-api.md` (v0.2-draft), `docs/contracts/opkc-adapter.md` (v0.2-draft), `openapi/tsp-api.yaml` (v0.2.0-draft), `docs/nfr.md` §7
- Method: decompose the amended solution into units one level below the spine; for each pair of units, assume both implement **their own** ADs and contracts literally and correctly; look for a pair of compliant implementations that (a) attribute the same decision to two owners, (b) disagree on a shared data shape or a dedup scope, (c) mutate one entity from two paths, or (d) state an invariant no single unit is required to enforce. Every finding below is such a pair, with the AD change that closes it.
- Out of scope (deliberately not attacked here): the unaudited absence of the НСПК protocol (`[ТРЕБУЕТ ПРОВЕРКИ]`), procurement, legal model of consent, and the pre-existing QR-only decisions that the amendment does not touch.

## Verdict

**Does not pass as written.** The amendment is consistent at the level of *states* and at the level of *single-unit behaviour*, but not at the level of *ownership and time*. It bolts a second lifecycle (the mandate aggregate, AD-009) and a second trigger surface (charges, AD-010) onto an existing payment FSM without:

1. an AD that defines the interface between the two lifecycles — who decides "stop this charge", and at what instant a charge becomes bound to a mandate (F-02, F-03, F-12, F-13);
2. an extension of the transport contract's **observation and cancellation** primitives to match the new charge type (F-04, part of F-02);
3. a named owner for the new idempotency key and the new cumulative limit (F-06, F-07, F-13);
4. an acknowledgement that the consent authority is external, i.e. the gateway holds a *projection*, not "the truth" (F-01, F-09, F-10).

Result: **5 Critical, 7 High, 3 Medium.** Every Critical is reachable on the ordinary path of a payer revocation or a lost notification, and every Critical ends with money moving in the direction the AD was written to prevent. None of the Criticals requires a unit to break an AD — the ADs are under-specified exactly where they need to be binding.

## Findings

Severity scale: **Critical** = a wrong financial outcome is reachable while both units obey their ADs, or a stated invariant is unenforceable (fails-open onto money). **High** = a shared shape/owner is ambiguous so two compliant builds diverge, with material functional or financial damage. **Medium** = a contract/ownership inconsistency that is currently latent but will be resolved differently by two owned components.

---

### F-01 — The consent aggregate has two owners, and the spine mislabels which one is authoritative — **Critical**

- **Pair:** (A) gateway mandate aggregate — `AD-009` / `ADR-008` §4 ("Мандат — **единый источник истины** согласия в БД шлюза"); (B) ОПКЦ СБП / payer's bank, reachable only through the vendor transport adapter — `AD-004`, `AD-008 [ADOPTED]`, `ADR-008` context ("согласие фиксируется в банке плательщика через ОПКЦ").
- **Each obeys its own text:** A stores the mandate and treats its DB row as the truth; B is the system that actually holds the payer's consent and whose protocol decides revocation, limits and validity; the adapter hides all of that behind the opaque `opkcMandateRef`.
- **Divergence:** the legal consent is created, held and revoked **outside** the gateway, yet `AD-009` promotes the gateway's cached projection to "единый источник истины". `docs/contracts/tsp-api.md` §7.5 still openly lists "кто хранит согласие — по документации НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`" — so the spine asserts an authority the contract explicitly leaves undecided. `mandate-lifecycle.md` §6 then treats "ОПКЦ revoked / we `ACTIVE`" as a 0-tolerance stop-signal, i.e. as an anomaly, when it is the *normal propagation window*.
- **Failure scenario:** payer revokes at t0 in their bank. The gateway learns at t1 (notification or, worst case, up to the hourly reconciliation). Between t0 and t1 `AD-011`'s guard sees a perfectly `ACTIVE` mandate and authorises charges. `NFR §7` says "Списаний после отзыва мандата = **0**". The invariant is unenforceable *as written*, because "revoked" is evaluated in the wrong system.
- **Closes with:** new **AD-012 — Consent authority and freshness.** ОПКЦ / payer's bank is the authority for existence, limits, validity and revocation of consent; the gateway aggregate is a **projection with an explicit freshness bound**. Define max staleness; require a pre-charge freshness check (or fail-closed) when staleness exceeds it; restate `AD-009` as "the single source of truth **for local gateway decisions**, derived from ОПКЦ-authoritative consent"; reclassify the §6 "revoked at ОПКЦ / active locally" case from anomaly to expected synchronisation, with the money decision governed by the freshness rule.

---

### F-02 — Nothing binds a charge to a mandate; the in-flight window is owned by no unit — **Critical**

- **Pair:** (A) mandate aggregate — `AD-009`, `AD-011` ("Отзыв или приостановка мандата в **той же транзакции** запрещает **новые** списания"); (B) payment FSM — `AD-010` and transition `T13` in `state-machine.md` §2 (guard: "`paymentOrigin=mandate`, мандат `ACTIVE` **на момент создания платежа**; шаг QR пропущен").
- **Each obeys its own text:** A forbids charges once revoked; B admits any charge that was created while the mandate was `ACTIVE`. Both statements are satisfied simultaneously by the same sequence.
- **Divergence:** the **binding point** — the instant at which a charge stops being "new" and becomes "in flight" — is defined nowhere. Under B, a charge is permanently entitled to credit once created under an `ACTIVE` mandate. Under A, revocation is supposed to stop charges, including the one already dispatched to ОПКЦ. `mandate-lifecycle.md` §4 narrates the case ("отзыв при списании в `CREATED` → попытка отмены в ОПКЦ; если отмена невозможна и приходит `PAID` — зачисление исполняется, компенсация — возвратом"), but that narrative is in a spec, holds no AD binding force, names no owner, and is not expressible in §2's transition table.
- **Failure scenario:** t0 charge created (mandate `ACTIVE`); t1 `POST /revoke` → `REVOKED`; t2 `payment.paid` arrives → B applies `T13` with a guard that was true at t0 → `PAID` → ABS credit. The payer revoked at t1 and is debited at t2. `NFR §7` is violated by construction. The same race exists for `M5` (`SUSPENDED`) and `M9` (`EXPIRED → validTo`), neither of which has any in-flight rule at all.
- **Closes with:** tighten **AD-011** and add a mandate↔payment interface clause: the payment persists the binding tuple (`mandateId`, `mandateEpoch`/version, `mandateStateAtBinding`); `T13`'s guard is evaluated against the **current** mandate epoch, not the creation-time snapshot; a charge whose mandate left `ACTIVE` after binding enters a `CANCEL_PENDING` sub-state whose **cancel command is owned by the mandate aggregate** (single writer), and the notification of the cancellation outcome (`MANDATE_CHARGE_CANCELLED` / `paidAfterCancel`) is the only admissible route back into `T13`. Fitness: no payment with `paymentOrigin=mandate` reaches `PAID` while its mandate is not `ACTIVE` without an explicit, audited override record.

---

### F-03 — The promised compensation for a post-revocation charge is architecturally unreachable — **Critical**

- **Pair:** (A) refund saga / ABS adapter — `AD-005`, `ADR-005` §4 ("Возврат — сага: **ТСП инициирует возврат** → шлюз проверяет, что платёж был зачислен (`CREDITED`/`COMPLETED`) → ...") and `tsp-api.md` §3.4/§3.3 (`REFUNDED` reachable only from `COMPLETED`; refund endpoint is a merchant call); (B) mandate aggregate — `AD-009` / `mandate-lifecycle.md` §4 ("если отмена невозможна и приходит `PAID` — зачисление исполняется, **компенсация — возвратом (сага)**").
- **Each obeys its own text:** A permits a refund only after the money is credited, and only when the merchant asks. B promises compensation as a consequence of revocation.
- **Divergence:** the compensation B promises is only reachable through a path A does not authorise: the credit must complete (`PAID → CREDITED → COMPLETED`) and then **the TSP** — not the party that revoked — must voluntarily call `POST /v1/payments/{id}/refunds`. No AD gives the gateway the trigger, the authority or the API to refund on the payer's revocation. The refund of a `PAID`-but-not-yet-`CREDITED` charge is structurally impossible (`REFUNDED` only from `COMPLETED`).
- **Failure scenario:** payer revokes; the in-flight charge proceeds to `PAID`; the ABS credit executes (exactly as `AD-005` mandates); the TSP has no incentive and no obligation to refund; the payer's money is retained by the merchant after the consent was withdrawn — a chargeback/dispute and a probable `NFR §7`/regulatory finding. The architecture contains no unit that can fix this automatically.
- **Closes with:** new **AD-013 — Bank-initiated compensation for charges bound to a non-`ACTIVE` mandate.** The gateway MUST open a system-initiated refund saga for any mandate charge that reaches `PAID` while its mandate is not `ACTIVE`, or whose cancellation is confirmed impossible; the saga is idempotent by `paymentId`, audited, and exempt from the merchant-initiated-only constraint. Extend `ADR-005` and `tsp-api.md` §3.4 with a system-initiated refund origin (`refundOrigin=mandate_revocation`) and a corresponding webhook. Fitness: no charge remains credited after mandate termination without an open or closed compensation record.

---

### F-04 — A mandate charge has no payment-status confirmation channel; reconciliation must invent one or leave the charge uncreditable — **Critical**

- **Pair:** (A) reconciliation — `ADR-004` §5, `state-machine.md` §5, `mandate-lifecycle.md` §6 (must re-query statuses for open operations and reconcile with the operator); (B) transport adapter contract — `AD-004`, `AD-008 [ADOPTED]`, `opkc-adapter.md` §3–§4.
- **Each obeys its own text:** A must compensate for lost notifications ("Потеря нотификации НСПК — 0 (компенсируется сверкой и опросом статусов)", `nfr.md` §3). B exposes `getPaymentStatus` keyed by **`qrId`** only, `getReconciliationReport` entries keyed by **`qrId`**, and `payment.paid` with `qrId` as a key field; `AD-010` says a mandate charge skips the QR step, so no `qrId` exists; there is **no** `getMandateChargeStatus` and `getMandateStatus` is mandate-level, not charge-level.
- **Divergence:** the two units agree on the in-band `payment.paid` event but not on the out-of-band path, which `ADR-004` makes mandatory. For mandate charges that path does not exist in the contract.
- **Failure scenario (both branches are wrong):**
  - (a) the notification is lost, and reconciliation can only observe `getMandateStatus = ACTIVE` plus the requested amount; a unit that credits on that evidence has credited **without confirmation of this charge** — `AD-005`'s "подтверждённый НСПК статус" silently degrades to "we believe the mandate is active";
  - (b) a strict unit refuses to credit without charge-level confirmation → the payer is debited and the TSP is never credited; the payment is stuck in `CREATED` forever, and it may not even appear in `getReconciliationReport` (keyed by `qrId`).
- **Closes with:** extend the adapter contract: `getPaymentStatus` accepts `reference` (`paymentId`) as an alternative key, or a new `getChargeStatus(opkcMandateRef, merchantOrderId)`; declare `qrId` explicitly nullable/absent for mandate charges; require `payment.paid`/`payment.rejected` to correlate by `reference`; require `getReconciliationReport` to include mandate charges keyed by `reference`. Add to the spine: "every financially significant payment, including `paymentOrigin=mandate`, has exactly one designated confirmation source reachable by a stable gateway-owned key". Fitness: reconciliation accounts for 100 % of `paymentOrigin=mandate` `PAID` transitions.

---

### F-05 — Two compliant units each own "the" credit trigger; `AD-005` constrains the state, not the number of triggers — **Critical**

- **Pair:** (A) payment FSM + outbox relayer — `AD-002` (status change + outbox in one transaction) and `T13`/`T4` actions ("outbox-событие «зачисление в АБС»"); (B) reconciliation / unfinished-operations sweep — `state-machine.md` §5 ("Платёж в `PAID` с недоступной АБС — остаётся `PAID`, ... **зачисление гарантируется сверкой**") under `AD-005`, which explicitly binds reconciliation.
- **Each obeys its own text:** A emits a credit command as part of the `PAID` transition. B is required to guarantee that a `PAID` payment is eventually credited and therefore selects `PAID`-without-credit rows. `AD-005` says only "вызов АБС на зачисление **возможен только из состояния `PAID`**" — it says nothing about how many emitters may exist, or who wins a race.
- **Divergence:** two legal emitters and a guard (`ADR-005` §2: "шлюз хранит `absDocId` результата и повторно не вызывает") that is a read-then-write check with **no stated atomicity**. A sweep that runs between the first ABS call and the persistence of `absDocId` issues a second call.
- **Failure scenario:** `PAID` → credit command emitted → ABS is slow (or the `< 60 s` SLA is not met) → before `absDocId` is written, the reconciliation sweep selects the same `PAID` row and issues a second credit. For an ABS that does not natively deduplicate — precisely the case `ADR-005` anticipates — two postings are created; the gateway stores one `absDocId`, so the second posting is invisible to every subsequent reconciliation. This is the categorical double-credit failure the whole design exists to prevent, reached without violating a single AD.
- **Closes with:** tighten **AD-005**/**ADR-005**: "exactly one credit attempt per payment, owned by a single designated emitter (the `PAID` transition). Before the first call to the ABS adapter, atomically persist a unique `absCreditAttempt(paymentId)` guard (unique constraint or `SELECT … FOR UPDATE`). Reconciliation, DLQ replay and operator runbooks may only invoke the **same** idempotent command and must not be able to reach the ABS adapter by any other path." Fitness: for each `paymentId`, at most one outbound ABS credit call observed at the adapter; exactly one `PAID → CREDITED` attempt record.

---

### F-06 — The charge idempotency key has three scopes, three lifetimes and no named owner — **High**

- **Pair:** (A) TSP API layer / idempotency store — `tsp-api.md` §2 (`Idempotency-Key`, "обязателен для всех `POST`", key→resource mapping stored **24 часа**); (B) mandate aggregate / charge validator — `AD-010` ("Идемпотентность — расширение `AD-003`: `Idempotency-Key` плюс запрет повторного `merchantOrderId` **или периода** в рамках одного мандата"); (C) vendor transport adapter — `opkc-adapter.md` §5 ("идемпотентность по (`opkcMandateRef`, **период/`merchantOrderId`**)").
- **Each obeys its own text:** A dedups on the header with a 24 h TTL; B dedups on a period tuple within a mandate; C dedups at the ОПКЦ boundary on its own tuple. `AD-003`'s "Binds" row (`вход ТСП (Idempotency-Key), нотификации НСПК (eventId), вызовы АБС (paymentId/refundId)`) was **never amended** to name the mandate aggregate or the adapter as idempotency owners — so no unit is formally the authority, and each contract defines "the extension" its own way.
- **Divergence:** three keys, none dominant, and the middle one is half-undefined: "период" is never given a field or a canonical form — it is either the TSP-controlled free string `merchantOrderId` or an OПКЦ-normalised period, depending on the reader.
- **Failure scenarios:**
  - **(a) Both fire — double debit.** A merchant retries after the 24 h window (or a DLQ replay re-injects the trigger) with a fresh `Idempotency-Key` and the same period. Store A misses (TTL); store C's mapping exists only for a *successful* operation and the first attempt was rejected (`NSPK_REJECTED`); store B released the reservation on `FAILED` (or never held it). A second payment is created and a second `executeMandateCharge` is issued. The vendor's safeguard cannot help, because the gateway has just re-declared the *same* period under a *different* token.
  - **(b) Both suppress — lost revenue.** Unit B implements the ban over **all** history including `FAILED`. One transient ОПКЦ rejection permanently poisons the period: the merchant gets `409 MANDATE_CHARGE_CONFLICT` for a period that was never successfully charged, and can never collect it under that mandate.
  - **(c) Semantic defeat.** `merchantOrderId` is merchant-controlled (`sub-2026-10`, `2026-10`, `INV-…` for the same month). With no canonical "период", all three keys are defeated by a merchant that changes its own string between retries — the exact double charge the extension was written to prevent.
- **Closes with:** tighten **AD-003**/**AD-010**: introduce a first-class, canonical `billingPeriod` (e.g. `YYYY-MM` or an explicit date range) in `MandateChargeRequest`; the authoritative dedup key is `(mandateId, billingPeriod)`, persisted for the **lifetime of the mandate** (not 24 h) and enforced by a **DB unique constraint committed in the same transaction as the payment insert**; define reservation release semantics on `FAILED`/`EXPIRED`/`REFUNDED` (release but retain an immutable record; a re-charge is a new payment that must reference the released `paymentId`); demote `Idempotency-Key` to a 24 h retry cache and state that it is **not** a sufficient guard on its own; treat `merchantOrderId` as metadata, never as a dedup key; require the adapter's token to be the same tuple with TTL ≥ mandate lifetime. Fitness: a replay with an expired `Idempotency-Key` cannot create a second charge; a concurrent duplicate-period pair yields exactly one payment.

---

### F-07 — `maxTotalAmount` is an invariant with no owner and no counter — **High**

- **Pair:** (A) TSP API validator — `tsp-api.md` §3.6 (`maxTotalAmount` request field) and §4 (`MANDATE_LIMIT_EXCEEDED`: "`amount > maxAmountPerCharge` **или превышен `maxTotalAmount`**"); (B) mandate aggregate / charge-creation transaction — `AD-011` guard ("`ACTIVE` ∧ `amount ≤ maxAmountPerCharge` ∧ текущее время в периоде ∧ `tspId` совпадает").
- **Each obeys its own text:** A rejects on the cumulative limit; B's guard is complete per `AD-011` — the cumulative limit is simply **not in it**.
- **Divergence:** no document defines where "charged to date" lives, when it increments (at creation or at `PAID`?), or what releases it (`FAILED`, `EXPIRED`, refund). `Mandate` in `openapi/tsp-api.yaml` has no such field, so even the merchant cannot see the remaining headroom.
- **Failure scenarios:** (a) a unit implemented strictly from `AD-011` never enforces the total → the limit the payer consented to is decorative and unbounded cumulative debits are legitimate; (b) a unit that does enforce it, but before the transaction (because `AD-011` does not ask for it *in* the transaction), loses a concurrent pair — two charges each pass and both commit; (c) a unit that increments at creation and never releases on `FAILED` permanently consumes headroom → legitimate later charges are rejected (**both suppress**).
- **Closes with:** tighten **AD-011**: include `chargedToDate + amount ≤ maxTotalAmount`, computed on the mandate aggregate row under the same lock/transaction as the payment insert; define the counter's lifecycle bound to the payment state (reserve at creation; release on terminal non-credited states; retain on `PAID`; give one explicit rule for refunds); expose `chargedToDate` in `GET /v1/mandates/{id}`.

---

### F-08 — The `AD-011` owner check reads a `tspId` no unit is required to source authoritatively — **High**

- **Pair:** (A) API/auth layer — `tsp-api.md` §1 (mTLS certificate + `X-API-Key`) but §3.2 documents `tspId` **in the request body**, while `openapi/tsp-api.yaml` `PaymentRequest` omits it; (B) mandate aggregate — `AD-011` guard "`tspId` совпадает с владельцем мандата".
- **Each obeys its own text:** A may resolve the tenant from the body (as the QR contract documents) or from the certificate; B's guard is written against an abstract `tspId` and does not say which. `MandateChargeRequest` carries no `tspId` at all, so B must import it from somewhere.
- **Divergence:** two candidate identity sources (authenticated principal vs body field) and a guard that names neither. `AD-011` explicitly promises to prevent "списание по мандату **чужого** ТСП" — but a guard that compares the *body* value to the mandate owner never compares it to the caller.
- **Failure scenario:** a charge is attributed from the request body while the authenticated principal differs → either a legitimate charge is rejected (both suppress) or an owner mismatch goes undetected and a charge is executed against another merchant's mandate. The QR path already exhibits the same ambiguity (`tspId` in §3.2, absent from the OpenAPI schema), so the amendment has inherited it into a security-critical guard.
- **Closes with:** tighten **AD-011** and `tsp-api.md`: the guard MUST use the **authenticated principal** (mTLS identity / API key → `tspId`); remove `tspId` from request bodies (and make the QR path consistent); add a fitness test proving a charge cannot be executed for a mandate owned by another TSP.

---

### F-09 — `SUSPENDED` has no counterpart at ОПКЦ, and the only transport operation available for it is irreversible — **High**

- **Pair:** (A) mandate aggregate — `mandate-lifecycle.md` `M5`/`M6` (suspend/resume); (B) transport adapter contract — `opkc-adapter.md` §3, which exposes **no** `suspendMandate`, and describes `revokeMandate` as "отзыв/**приостановка** согласия" returning `REVOKED`.
- **Each obeys its own text:** A implements its transition table exactly; B implements its operation list exactly.
- **Divergence:** the contract's own wording invites mapping "suspend" onto `revokeMandate`, which is irreversible at ОПКЦ. The mandate aggregate's `SUSPENDED` is reversible (`M6`); the ОПКЦ's `REVOKED` is not.
- **Failure scenario:** a mandate implementation that propagates suspension the way its contract describes irreversibly revokes the consent; `M6` resume then either fails outright or resumes locally while ОПКЦ holds `REVOKED` — and the next reconciliation applies the §6 stop-signal ("у ОПКЦ отозван, у нас `ACTIVE`") → forced `REVOKED` + alert, silently undoing the resume. If instead suspension is not propagated (the functionally correct choice, since `executeMandateCharge` is gateway-initiated), the local `SUSPENDED` / ОПКЦ `ACTIVE` divergence is covered by **no** §6 rule, so no unit is required to detect it — harmless today, fragile the moment the protocol gives the payer's bank standing.
- **Closes with:** state explicitly in **AD-009**/**AD-011** and the adapter contract that `SUSPENDED` is a gateway-local deny-flag with **no** ОПКЦ representation, that suspension MUST NOT be transmitted via `revokeMandate`, that resume is therefore local-only, and add "ОПКЦ `ACTIVE` ∧ we `SUSPENDED`" to `mandate-lifecycle.md` §6 as an **expected** divergence (no alert), distinguishable from a real mismatch.

---

### F-10 — Mandate terms have two sources; no AD says which one the guards read — **High**

- **Pair:** (A) mandate aggregate — `AD-009` and `M2` ("сохранить `opkcMandateRef`, **параметры подтверждены**") evaluating `validTo` and limits locally; (B) transport adapter / ОПКЦ — `opkc-adapter.md` §3 `createMandate` (sends `maxAmountPerCharge`, `maxTotalAmount`, `validFrom`, `validTo`) and §4 `mandate.activated` (returns `opkcMandateRef`, `reference`, **`validTo`**), while `getMandateStatus` returns **only** status.
- **Each obeys its own text:** A stores terms and enforces them; B forwards the requested terms and reports back a `validTo` — a field that only carries information if it can differ from what was requested.
- **Divergence:** `M2` never says whether the ОПКЦ-confirmed value **replaces** the requested one. The activation event deliberately returns `validTo` but no limits, so even if A adopts the event value, divergence in the limits is undetectable (no reconciliation field).
- **Failure scenario:** the payer's bank / ОПКЦ confirms a shorter validity or a lower per-charge limit. If A keeps its requested `validTo`, charges run past the consented validity → unauthorised debit. If A adopts the event's `validTo` but reconciliation cannot see limits, the two systems drift indefinitely. A longer confirmed validity with an adopted shorter local one makes the mandate `EXPIRED` early (revenue loss, both suppress).
- **Closes with:** tighten **AD-009** `M2`: the ОПКЦ-confirmed parameter set is authoritative and MUST be persisted as such (requested set retained for audit); require the activation event to carry the full confirmed set (not just `validTo`); require `getMandateStatus` to return confirmed limits and validity; add a reconciliation comparison with explicit tolerances.

---

### F-11 — The pre-charge payer notification has an NFR, no owner and no component — **High**

- **Pair:** (A) TSP API validator / `noticeRef` — `tsp-api.md` §3.9 ("`noticeRef` — опц.: ссылка на предварительное уведомление плательщика, **если требуется регламентом**"); (B) mandate aggregate / notification service — `AD-011` ("Требование уведомления плательщика до списания и его срок — по регламенту НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`") while `ADR-001`'s notifier delivers **merchant webhooks only**.
- **Each obeys its own text:** A accepts an optional opaque string; B defers the rule to an external regulation. Neither is required to send anything to the payer or to verify that something was sent.
- **Divergence:** `nfr.md` §7 demands "**100 %** списаний с соблюдением регламентного срока". The gateway cannot measure an opaque optional string and has no channel to the payer; the rule that is supposed to make the NFR achievable is deferred to `[ТРЕБУЕТ ПРОВЕРКИ]`. If the duty is the acquirer's (bank's) — the regulatorily plausible reading for a bank-side product — then **no component in the architecture performs it at all**.
- **Failure scenario:** a charge is created and executed with no evidence of the legally required pre-charge notice; the NFR is unmeasurable by construction; the first audit (or the first payer complaint) exposes an unbudgeted capability gap.
- **Closes with:** a new AD (or a mandatory clause in `AD-011`/`AD-009`) naming the accountable party and the evidence required at charge time. If the bank's duty: add a payer-notification capability and make a compliant notice a **guard precondition** for charge creation, with the evidence persisted in the mandate/audit record. If the merchant's: make `noticeRef` mandatory-when-required and validated, and include notice status in the reconciliation/audit scope. Rewrite `NFR §7`'s target against that named artifact.

---

### F-12 — Reconciliation is required to write mandate state, but the transition table has no such row and no single writer is declared — **High**

- **Pair:** (A) reconciliation — `mandate-lifecycle.md` §6 ("«У ОПКЦ мандат отозван, у нас `ACTIVE`» → **немедленный** локальный перевод в `REVOKED` + алерт"); (B) mandate aggregate — `mandate-lifecycle.md` §2, the authoritative transition table, where `M7`'s trigger is "отзыв плательщика (нотификация ОПКЦ) **или** отзыв ТСП" and no row corresponds to a reconciliation-detected revoke.
- **Each obeys its own text:** A performs the write §6 demands; B admits only the transitions in §2, each of which must be atomic with status + outbox + audit (`AD-009`).
- **Divergence:** two mutation paths into one entity, with the second path not represented in the first path's state machine, and no declared single writer.
- **Failure scenario:** B, implemented strictly from §2 (the natural reading of "переходы ... каждый переход выполняется атомарно"), has no legal transition for A's signal → the stop-signal is **dropped** and charges continue after the payer's revocation; or A writes the status out of band, bypassing `AD-009`'s atomic status+outbox+audit rule → an unaudited financial decision plus a DB state that contradicts the outbox — the exact class of defect `AD-002`/`AD-009` exist to prevent.
- **Closes with:** add explicit reconciliation-driven transitions (`M11`: `ACTIVE|SUSPENDED → REVOKED`, `reason=recon`, on ОПКЦ-confirmed revoke; `M12`: `ACTIVE → EXPIRED` on ОПКЦ-confirmed expiry) and a new clause: **the mandate aggregate is the only writer of mandate status; reconciliation issues commands, never writes.**

---

### F-13 — `opkcMandateRef` is delivered on two channels with no authority rule — **Medium**

- **Pair:** (A) mandate creation handler — `opkc-adapter.md` §3: `createMandate` returns `opkcMandateRef` **synchronously**; (B) mandate event consumer — `opkc-adapter.md` §4 `mandate.activated` also carries `opkcMandateRef`; `mandate-lifecycle.md` `M2` persists it, and §5 dedups activation by "`eventId` **+ `opkcMandateRef`**".
- **Each obeys its own text:** both persist the reference; both treat their channel as the way the reference arrives.
- **Divergence:** nothing requires the two values to be identical, and the composite dedup key `eventId + opkcMandateRef` makes a *different* reference a *new* event rather than a contradiction.
- **Failure scenario:** the adapter allocates a provisional reference in the sync response and a final one in the activation event (or a re-registration occurs). The composite key treats the second value as a new event; `M2`'s guard ("`opkcMandateRef` непустой, параметры подтверждены") passes and the state is already `ACTIVE`. Depending on implementation the stored reference is overwritten → every subsequent `executeMandateCharge` fails `INVALID_REFERENCE`, or ignored → the stored reference is the wrong one. Either way the mandate is `ACTIVE` but unusable, with no AD or reconciliation rule defining recovery.
- **Closes with:** tighten **AD-009** and the adapter contract: `createMandate` and `mandate.activated` MUST carry the identical `opkcMandateRef`; a mismatch is a hard error (mandate **not** activated, alarm, DLQ), never an idempotent no-op; the reference is written once, idempotently by `reference = mandateId`; add a fitness check that a live mandate's reference cannot change without an explicit re-registration flow.

---

### F-14 — Webhook payloads cannot attribute a payment to a mandate — **Medium**

- **Pair:** (A) notification service — `ADR-004`, `tsp-api.md` §5 (event body `{eventId, type, paymentId, status, amount, timestamp}`); (B) TSP API resource contract — `tsp-api.md` §3.3 / `openapi` `Payment` (which *does* carry `paymentOrigin`, `mandateId`, `merchantOrderId`).
- **Each obeys its own text:** §5 defines the event payload without mandate attribution; §3.3 defines the resource with it.
- **Divergence:** the merchant's primary integration surface (`payment.*` webhooks) is a strict subset of the resource shape for exactly the fields the subscription feature depends on.
- **Failure scenario:** a merchant running both QR and mandate flows cannot tell from `payment.completed`/`payment.failed` which mandate a debit belongs to or which billing period it settles; it must call `GET /v1/payments/{id}` for each event. For the segment this feature targets, the merchant's own ledger reconciliation — the control that stops the merchant re-charging a period — is materially weakened. Compounding this, `ADR-004` guarantees no ordering, so `mandate.revoked` may arrive before the `payment.completed` of a charge created pre-revocation, and the payload carries nothing that lets the merchant correlate the two.
- **Closes with:** additively add `paymentOrigin`, `mandateId`, `merchantOrderId` (and the accepted `billingPeriod` from F-06) to the `payment.*` event bodies; state an explicit contract obligation for merchant-side ordering/attribution (e.g. "a `payment.completed` for a mandate charge may arrive after a `mandate.*` event; both must be processed idempotently and attributed via `mandateId`").

---

### F-15 — `Idempotency-Key` is mandatory for every `POST` in prose but absent from the new mandate-management operations — **Medium**

- **Pair:** (A) API gateway idempotency middleware — `tsp-api.md` §2 ("Заголовок `Idempotency-Key` **обязателен** для всех `POST`", key→resource mapping 24 h, "тот же ключ, **другое тело** → `409`"); (B) mandate-management endpoints — `tsp-api.md` §3.8 ("Все три метода **идемпотентны** (повтор → текущий/целевой статус, без ошибки)") and `openapi/tsp-api.yaml`, which declares **no** `Idempotency-Key` parameter on `/suspend`, `/resume`, `/revoke`.
- **Each obeys its own text:** A enforces the blanket rule; B is idempotent by resource identity and declares no key. Neither text defers to the other.
- **Failure scenario:** a merchant implementing from the OpenAPI/§3.8 omits the header on `/revoke`; a strict middleware rejects the call `400 INVALID_REQUEST` → **the payer's revocation cannot be executed** — the one operation in the feature whose failure is a regulatory event, blocked by a transport-level validation rule (and one that F-01 makes more likely to be attempted). If the middleware instead synthesises a key, the 24 h key→resource mapping plus "same key, different body → `409`" can produce spurious conflicts for retried revokes.
- **Closes with:** tighten `tsp-api.md` §2: explicitly exempt (or explicitly require the header for) the idempotent-by-resource `POST`s and state precedence — "for `POST /v1/mandates/{id}/{suspend|resume|revoke}` the resource identity **is** the idempotency key; the header is optional and ignored if present" — and align the OpenAPI. Revocation must never be blocked by header validation.

---

## Attack attempts that were defended (recorded so the same ground is not re-attacked)

- **Duplicate `payment.paid` for the same charge.** `ADR-004` §2 (`eventId` dedup) plus `AD-002`'s atomic transition means retries of the *same* event cannot double-credit. The residual risk in F-05 is a *different emitter*, not a duplicate event.
- **Correction of a confirmed payment.** `PAID` cannot roll back, corrections only via the refund saga (`state-machine.md` §3) — coherent.
- **Retroactive re-consent.** Mandate terms are immutable after `M2` and changes require a new mandate (`mandate-lifecycle.md` §3) — correctly blocks "the payer agreed to X, we charged under Y".
- **A second financial path.** `AD-010` genuinely holds: the adapter contract contains no mandate-specific credit operation, and mandate charges reuse the FSM and the ABS adapter. Verified against `opkc-adapter.md` §3.
- **Refund before credit.** `REFUNDED` is reachable only from `COMPLETED` (`state-machine.md` §3) — sound, and the reason F-03 is a *compensation* gap rather than a refund-abuse gap.
- **`AD-005` at the letter for mandate charges.** `T13` still credits only from `PAID`; no transition writes to ABS from `CREATED`. The surrounding holes (F-02, F-04, F-05) are about *when* `PAID` may be reached and *how many* triggers emit the credit — not about bypassing `AD-005`.
- **Atomic status+outbox+audit for every mandate transition** (`AD-009`) is a genuinely strong control and is the reason F-12 is scoped to a *missing transition row* rather than to general outbox weakness.
- **Reconciliation stop-signal for "we `REVOKED`, ОПКЦ `ACTIVE`"** (repeat revoke + escalation) is sound; only its mirror (F-01) is not.
- **Contract additivity.** Verified against `openapi/tsp-api.yaml`: every v0.2 addition is a new path or an optional field; no v0.1 consumer breaks. All proposed changes above (including F-14) can stay additive.

## Cross-cutting themes

1. **Two lifecycles, no interface.** The amendment attaches a mandate lifecycle to a payment FSM without an AD defining the seam. F-02, F-03, F-12 and F-13 are four faces of the same omission: *when does a mandate decision become a payment fact, and which unit owns the decision at that instant?*
2. **The adapter gained operations but not observability.** `createMandate`/`executeMandateCharge`/`revokeMandate` were added; a way to *observe and abort a single charge* was not (F-04, part of F-02). The result is a charge type that `ADR-004`'s mandatory reconciliation cannot see.
3. **Idempotency became three-layered with no authority.** `AD-003` was extended in three different documents with three different keys, TTLs and owners (F-06, F-07, F-13). The extension is the amendment's weakest structural point because it is the *only* control standing between a retry and a double debit.
4. **Authority vs projection.** The bank treats its own database as the truth for a fact that an external party owns (F-01, F-09, F-10). Every one of these becomes a payer-facing incident at the first protocol detail that differs from the assumption.
5. **The merchant contract is incomplete for the merchant.** Notice evidence and mandate attribution are missing from the surfaces the merchant actually consumes (F-11, F-14), while the NFRs assume the merchant can provide/consume them.

## Proposed AD set (consolidated)

| AD | Title | Closes |
|---|---|---|
| **AD-012** | Consent authority and freshness (ОПКЦ is authoritative; gateway holds a bounded projection) | F-01, F-09, F-10 |
| **AD-013** | Bank-initiated compensation for charges bound to a non-`ACTIVE` mandate | F-03 |
| **AD-014** | Mandate↔payment binding point and in-flight charge policy (single owner of the cancel command) | F-02, part of F-12 |
| **AD-015** | Mandate-charge observability: confirmation and cancellation primitives in the adapter contract | F-04 |
| **AD-016** | One credit emitter, one attempt per `paymentId` | F-05 |
| **AD-017** | Canonical charge idempotency key and cumulative-limit counter | F-06, F-07 |
| **AD-018** | Authenticated principal is the mandate owner | F-08 |
| **AD-019** | Pre-charge notice: accountable party, evidence, and a measurable NFR | F-11 |
| tighten **AD-003 / AD-009 / AD-011 / ADR-005 / AD-002 already covers F-12** | Reconciliation-driven mandate transitions + single writer; webhook attribution; `Idempotency-Key` precedence; `opkcMandateRef` single channel | F-12, F-13, F-14, F-15 |

## Unit inventory used for pairing (for traceability)

Core gateway: TSP API layer + idempotency store · payment FSM (status machine, `T1`–`T13`) · mandate aggregate (`M1`–`M10`) · outbox + relayer · audit log. Perimeter: vendor transport adapter ОПКЦ (AD-004/AD-008) · ABS adapter (AD-005) · notification service (ADR-004) · reconciliation with ОПКЦ and АБС · antifraud/limits. External counterparts treated as units: ОПКЦ/НСПК (authority for consent per protocol) and the ABS.
