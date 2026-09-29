<!-- источник: <HARNESS>/runs-v2.1/cells/wqirmxx/home/.qwen/projects/-home-architect-project/chats/fab3bc97-5188-46c4-9e40-19a308a4431d.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `read_file(file_path="/home/architect/project/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="/home/architect/project/README.md")`

I'll start by understanding the repository's accepted decision, workflow rules, and handoff conventions.

  `run_shell_command(command="find /home/architect/project -type f -not -path \"*/.git/*\" -not -path \"*/node_modules/*\" | sort", description="List all project files")`
  `read_file(file_path="/home/architect/project/docs/solutioning.md")`

Let me read the docs directory, handoff package, and understand the workflow. Let me list files.

  `read_file(file_path="/home/architect/project/.arch-handoff/ARCHITECTURE.md")`
  `read_file(file_path="/home/architect/project/.arch-handoff/TASK.md")`
  `read_file(file_path="/home/architect/project/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="/home/architect/project/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="/home/architect/project/.arch-handoff/CONSTRAINTS.yaml")`

Note: solutioning says "автоплатежи" is out of scope in roadmap. Now the business asks for recurring C2B debits by payer consent — subscriptions (СБП подписки / автоплатежи). So this is a change request on the accepted decision.

Let me read the handoff docs, RUBRIC, CONSTRAINTS, MANIFEST, TASK, and the docs (nfr, contracts, state machine, ADRs), and the openapi spec.

Also important: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — accepted decision files may only be changed in the repository's accepted way. Let me check handoff rules / MANIFEST / RUBRIC and the architecture skill.

Let me read a lot in parallel.

  `run_shell_command(command="find /home/architect/project/docs /home/architect/project/openapi /home/architect/project/_bmad -type f | sort; echo \"---\"; ls -la /home/, description="List docs, openapi, bmad files")`
  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-architecture/SKILL.md")`

Now let me read docs/nfr.md, the contracts, state machine, ADRs and the openapi file. Also check the architecture skill (bmad-architecture) — the task says "use the methodological skills and tools available". The architecture skill is likely the right one (it can create/update/validate architecture docs). But this task is specifically about preparing an architecture package for a change on top of an accepted decision. Let me look at the bmad-architecture SKILL.md, and also bmad-correct-course (assess impact of a significant change during sprint execution across PRD/epics/architecture/UX and produce a sprint change proposal). Hmm. The deliverable list (significance assessment & route, impact on architecture, architectural decision with alternatives/consequences/reversibility, contract changes, NFRs, acceptance criteria and rollback plan, what remains for human architect) strongly matches bmad-architecture's document structure.

Let me read the architecture skill first.

Also the docs list: docs/contracts/tsp-api.md, docs/contracts/opkc-adapter.md, docs/spec/state-machine.md, docs/rfp/vendor-rfp.md, docs/nfr.md, docs/adr/ADR-001..007.md. But find output got truncated (the Error message). Let me list docs explicitly.

Let me read in parallel: bmad-architecture/SKILL.md, docs/nfr.md, and list docs dir.

  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-correct-course/SKILL.md")`
  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-architecture/customize.toml")`
  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-correct-course/customize.toml")`
  `read_file(file_path="/home/architect/project/_bmad/config.toml")`
  `read_file(file_path="/home/architect/project/_bmad/config.user.toml")`

This is a rich setup. The right skill here is bmad-architecture (create/update an architecture spine for the change), but the deliverable list is broader: significance assessment & route, impact on accepted architecture, architectural decision with alternatives/reversibility, contract changes, NFRs, acceptance criteria + rollback plan, human decisions.

Also bmad-correct-course: "Assess the impact of a significant change during sprint execution across the PRD, epics, architecture, and UX documents, and produce a sprint change proposal." Hmm — this is a change request on an accepted architecture decision. But the repo has no PRD/epics — it's an architecture decision repo (spine + ADRs + handoff).

Let me look at other candidate skills: bmad-correct-course, bmad-spec, bmad-prd, bmad-build. The user says: "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." (Methodological skills and tools may be installed — use them as intended.)

The task is fundamentally: prepare an architecture package for a change to a solution that has been decided. Deliverables map closely to the architecture skill's spine structure (change impact, new AD, contract changes, NFR, acceptance, rollback, human decisions). 

Given the repository context (spine + ADRs + handoff + fitness rules), I think the correct approach:
1. Use `bmad-architecture` skill in Update mode on the feature spine (add AD-009/ADR-008 for subscriptions), OR
2. Use `bmad-correct-course` to produce a change proposal.

Wait, let me re-read the correct-course description: "Assess the impact of a significant change during sprint execution across the PRD, epics, architecture, and UX documents, and produce a sprint change proposal." That's during sprint execution. Here we're at architecture stage (walking skeleton handoff), not sprint execution. Hmm, but "correct course" fits "significant change to an accepted decision".

Let me read both SKILL.md files to decide. Let me read bmad-correct-course/SKILL.md and its checklist, plus customize.toml files for bmad-architecture, and the relevant config, and the docs content (nfr, contracts, state-machine, openapi).

Let me also check _bmad/config.toml and config.user.toml for user_name, language settings (output language preference is auto → Russian).

Let me batch reads.

  `read_file(file_path="/home/architect/project/docs/nfr.md")`
  `read_file(file_path="/home/architect/project/docs/spec/state-machine.md")`
  `read_file(file_path="/home/architect/project/docs/contracts/tsp-api.md")`

Now I understand the environment. Let me read the remaining docs: nfr.md, contracts/tsp-api.md, contracts/opkc-adapter.md, spec/state-machine.md, adr ADR-002..007, openapi/tsp-api.yaml.

Also check the bmad-help skill and the spine template + lint script, since architecture skill uses us to update the spine properly.

The key question: which skill to use? The task = "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям."

This is essentially: Update the architecture spine (feature-level) with a new capability (recurring C2B / подписки СБП), plus produce an architecture decision package. Deliverables list matches the spine update + ADR + contract changes + NFR + acceptance + rollback + human decisions.

The bmad-architecture skill is the intended one ("create the architecture", "create technical architecture", "architecture spine"). Also, the skill's Update mode: "Amend an existing spine... Keep AD IDs stable — amend a Rule in place, add the next AD-n for a new decision, never renumber or reuse a retired ID. Then re-distill, run Reviewer Gate."

But the user explicitly says: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — Change accepted decision files only in the manner accepted in this repository. So ARCHITECTURE-SPINE.md is the accepted decision (AD-008 [ADOPTED]); docs/adr are the ADRs. The repository's accepted manner: ADRs are Proposed until ratified; AD-008 marked [ADOPTED] after A3. So we must not silently modify adopted decisions — a new change requires a new AD/ADR and the human architect's decision (A3-like gate). Similarly, gaps/external inputs.

Now, importantly: does the repo have a memlog? No `.memlog.md` exists. Docs are hand-written. The architecture skill expects a memlog workspace under {planning_artifacts}/architecture. Hmm — planning_artifacts = {project-root}/_bmad-output/planning-artifacts which doesn't exist. The repo's convention: docs/ with solutioning.md, adr/, contracts/, spec/, rfp/. And handoff generated by scripts (memlog.py exists in _bmad/scripts).

Given the repository convention, the change package should live in docs/ following the existing structure: e.g. docs/adr/ADR-008-....md, docs/change/... or docs/spec/spb-subscriptions.md, update docs/solutioning.md? But "принятые файлы решения" (accepted decision files) should only be changed the accepted way. Modifying ARCHITECTURE-SPINE.md directly: the accepted way per repo is via ADR ratification + Proposed status, plus A3 human decision. Actually, AD-008 was marked [ADOPTED] with reference to "A3 от 2026-08-15". Other ADs are Proposed pending ADR ratification.

The task says prepare a package "чтобы его можно было вынести на архитектурное решение" — so that it can be brought to an architecture decision. So we should NOT ratify; we produce Proposed ADRs and mark the human decisions.

Let me now read all remaining docs to ground the package. Also read the spine template and lint script to follow the spine format, and reviewer-gate reference.

Let me batch read: nfr.md, state-machine.md, tsp-api.md (contracts), opkc-adapter.md, openapi/tsp-api.yaml, and the ADRs. That's a lot of content. Let me do it in a couple of batches.

  `read_file(file_path="/home/architect/project/openapi/tsp-api.yaml")`
  `read_file(file_path="/home/architect/project/docs/contracts/opkc-adapter.md")`

Now read the openapi/tsp-api.yaml (the contract to modify), ADR-003..007, opkc-adapter.md, vendor-rfp.md, and the spine template + lint script.

Let me batch.

  `read_file(file_path="/home/architect/project/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="/home/architect/project/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="/home/architect/project/docs/adr/ADR-005-integraciya-s-abs-zachislenie-po-podtverzhdyonnomu-statusu-vozvraty-kak-saga.md")`

Now read the ADRs 003-007 and vendor RFP, plus spine template and lint script and reviewer gate reference. Let me batch.

  `read_file(file_path="/home/architect/project/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="/home/architect/project/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="/home/architect/project/docs/rfp/vendor-rfp.md")`

Now ADR-006, ADR-007, vendor RFP, and spine template/lint, reviewer-gate. Let me batch.

Also, the bmad skill uses config resolution with `uv run`. Let me check if `uv` is available and the memlog.py script. The architecture skill's output path is {planning_artifacts}/architecture = _bmad-output/planning-artifacts/architecture. But the repo's convention is docs/. Hmm. The skill says to bind doc_workspace. The evidence repo structure has docs/ with ADRs and handoff regenerated from docs. The "_bmad-output" dir doesn't exist. Using the skill would create a new spine under _bmad-output/planning-artifacts/architecture/... which diverges from the repo convention. The user says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — the accepted way in this repo.

I think the most faithful approach: 
- Use the bmad-architecture methodology (spine semantics: AD-n with Binds/Prevents/Rule, Deferred, inherited invariants, memlog, reviewer gate) but land artifacts in the repo's established layout: docs/ (adr/, spec/, contracts/, nfr.md) and update ARCHITECTURE-SPINE.md with new AD blocks in "Proposed" status (not adopted), because that is the repository's accepted manner (AD-008 got [ADOPTED] only via A3 human ratification; all others are Proposed).

Actually wait — the skill says inherit parent spine ADs as read-only, add new AD-n for new decisions. That's exactly what updating ARCHITECTURE-SPINE.md means. And "an update that overrides something from a source input: offer to update that source too". Also, the correct way to change accepted decision files: the repo's convention is that ARCHITECTURE-SPINE.md blocks are Proposed until the corresponding ADR is ratified. So adding new AD blocks (AD-009...) in Proposed status + new ADR-008 file is consistent. Also need a memlog per the skill? The repo has _bmad/scripts/memlog.py. Let me check it quickly.

Let me also check the bmad-architecture headless reference and reviewer-gate and spine-template, since I should follow the workflow. And run lint_spine.py at the end.

Let me read ADR-006, ADR-007, vendor-rfp, spine-template, reviewer-gate, headless.

  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-architecture/references/reviewer-gate.md")`
  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-architecture/references/headless.md")`
  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-architecture/scripts/lint_spine.py")`

Now let me read the spine template, lint script, reviewer gate reference, headless reference, and the memlog script to understand the machinery.

Actually the reviewer-gate + headless are key for the architecture skill. Let me read those.

  `run_shell_command(command="command -v uv; uv --version 2>/dev/null; command -v python3; python3 --version; git -C /home/architect/project status --short --branch", description="Check uv, python3, git state")`
  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-architecture/assets/spine-template.md")`
  `read_file(file_path="/home/architect/project/_bmad/scripts/memlog.py", limit=80)`

Now I have a good picture. Let me check the memlog.py script and whether uv is available. Also check the spine-template for the AD block format and frontmatter.

Let me also check the state-machine spec more? Already read. And check docs/contracts/tsp-api.md (read), openapi (read).

Now let's think about the substance: recurring C2B debits by payer consent — "подписки СБП" (SBP subscriptions / autopayments). In reality, СБП has "СБПавтоплатёж"/"Мультибанковский автоплатёж" (подписки) — the mechanism: payer gives consent (согласие) via their bank app; merchant can then initiate debits without QR each time; consent has limits (max amount per debit, period, validity), can be revoked. In НСПК terms: "СБП.Автоплатёж"/"Автоплатежи" with "соглашение" (agreement) / "подписка" — often implemented via ОПКЦ as "платежи по согласию" / "подписки". Mark specifics [ТРЕБУЕТ ПРОВЕРКИ] since protocol not available.

Key architectural implications:
1. New entity: consent/agreement (подписка) — lifecycle: DRAFT/REGISTERED/ACTIVE/SUSPENDED/REVOKED/EXPIRED. Source of truth question: is consent owned by gateway (like payment) or by НСПК? Need a consent state machine.
2. Payer interaction for consent: initial consent requires payer action (redirect/QR/DeepLink to payer's bank app) — so first payment is "onboarding of consent" with a redirect; not fully headless.
3. Recurring debit: merchant-initiated, no payer action; must validate against consent limits (amount, frequency, period, remaining).
4. Payment model change: payment lifecycle gets a new dimension: "платёж по подписке" — a debit operation that is not QR-based. Status machine: maybe reuse: CREATED → ... but no QR_ISSUED. Need to think: for subscription debit, the flow is: gateway → ОПКЦ debit-by-consent → PAID. So new states? Or a separate state machine (subscription debit operation) with its own transitions, reusing PAID/CREDITED/COMPLETED? The spine invariant AD-002 says "статусная машина платежа — единый источник истины", AD-005 "зачисление только из PAID". For subscription debit, the confirmation comes from ОПКЦ (status PAID / debited) — so AD-005 still applies if we model the debit result as PAID. But there's a subtlety: for a subscription debit, the "payer consent" replaces the QR registration; there is no QR_ISSUED. So the state machine needs a new initial path.
5. Idempotency: new idempotency keys: debit attempt (chargeId), consent registration; dedup by eventId still.
6. Refunds: refunds for subscription payments reuse the refund saga. But there's also "отмена/отзыв согласия" and possibly "reversal/chargeback" — disputes deferred.
7. Reconciliation: consent state must be reconciled with НСПК (revocations).
8. Notification to TSP: new webhook events: subscription.created, subscription.revoked, charge.completed/failed; existing consumers must not break (additive).
9. Security/consent: strong customer authentication (SCA) — the payer authenticates in their bank's app; mandate/consent data is ПДн and the mandate is a legally significant document (161-ФЗ, 152-ФЗ; also 63-ФЗ? no). Consent must be auditable, immutable, stored with evidence (timestamp, payer identifier masked). 
10. Regulatory: recurring debits might be considered a separate service in СБП ("СБП.Подписки"/"Автоплатёж") — need НСПК documentation, possibly separate connection/testing. Also for ЖКХ/связь (payments with variable amounts), consent must allow variable amounts with a cap.
11. АБС: no change to crediting model (still credit only from PAID) — good; AD-005 unaffected in essence but its "Rule" references PAID which must be extended to cover debits-by-consent (need explicit reconciliation).
12. Trust zones: consent flows involve payer redirect / user-facing surface — potentially a new public endpoint (payer-facing consent page) which changes the trust boundary (DMZ). AD-006 impacted: new exposed surface, but the requirement is that consent confirmation happens in payer's bank app (НСПК-mediated), so we shouldn't host a payer-facing consent UI ourselves — we host a redirect/handoff. Need decision.
13. AD-004 single adapter: consent operations are also НСПК protocol → must go through the same adapter; opkc-adapter contract gets new methods (createConsent, getConsentStatus, revokeConsent, debitByConsent...) — but vendor dependency: new methods mean RFP/contract change with the vendor (costly, since vendor contract not yet signed — good timing).
14. AD-008 (hybrid, adopted): consent protocol is also НСПК-proprietary → likely vendor transport must support it; this becomes a constraint on vendor selection (must-have in RFP) — this is a change to an adopted decision's constraints? No, it extends the RFP scope; but if vendor can't, might force re-decision. Note as conflict/impact on AD-008.
15. Deferred items: currently "автоплатежи" explicitly out of scope/roadmap. This change moves it in → spine Deferred item must be updated (accepted file — change only in the accepted manner: mark as activated via new AD/ADR, human decision needed).
16. Route/significance: Critical (financial, regulatory, new external protocol surface, new PII/consent legality). Score higher than 11/15 maybe → route remains Critical, deeper design required: A1 spec (consent state machine, contracts), ADR(s), fitness tests.
17. Human architect decisions: business model of subscriptions (limits, who bears fraud), whether consent is owned by gateway or purchased as part of vendor transport, whether to implement in phase 1 given НСПК documentation gap, whether to expose payer-facing UI, AML thresholds, contractual changes with НСПК/vendor, dispute handling.

Alternatives for consent storage/ownership:
- A. Gateway owns consent (local registry as source of truth) + НСПК mirror → full control, but duplicate source of truth and reconciliation burden; risk divergence.
- B. НСПК owns consent; gateway is stateless proxy → simpler, but no local source of truth (violates RPO=0 pattern, latency dependency on НСПК for each debit, harder audit).
- C. Hybrid: gateway stores consent registry as source of truth with НСПК as authority for revocation events (reconciliation both ways).

Alternative for debit mechanics:
- A. Polling/merchant-initiated debit API (push from gateway to НСПК per charge).
- B. Payer-bank-pull (scheduled pull from payer's bank based on consent) — less merchant control, but НСПК model may dictate.

Alternative for payment state machine:
- A. Reuse the same payment FSM with a new initial transition (CONSENT_DEBIT path) — fewer entities, but state machine complexity, "QR_ISSUED" not applicable.
- B. Separate charge entity with own FSM that hands off to the payment FSM after PAID — cleaner separation, more entities.
- C. Model subscription debit as a distinct "operation type" within the same FSM with type-specific guards — recommended if НСПК has a unified debit result.

Contract changes without breaking existing consumers: additive only, /v1 stays; add optional fields to Payment (e.g. subscriptionId, chargeId, mandateId?), add new endpoints /v1/subscriptions (POST/GET), /v1/subscriptions/{id}/charges, maybe /v1/subscriptions/{id}/revoke. New webhook events additive. New error codes additive. Never change existing required fields/enums semantics; status enum additive only (existing consumers must tolerate unknown enum → note). Actually adding new enum values to `status` could break strict consumers; the state machine statuses likely stay the same, with a new `operationType` field. Better: keep `status` enum stable; add new optional fields and new entities; if a new terminal status needed (e.g. REVOKED), put it on the subscription entity, not the payment enum. Good.

NFR for new functionality: consent registration latency, debit initiation latency, debit success rate (достаточно — успешность <100% из-за отсутствия средств), max debit frequency, consent revocation propagation ≤ X, double-debit = 0, notification latency, throughput for scheduled charges (batch spikes: e.g. ЖКХ on the 10th of month — burst), reconciliation of consents hourly.

Acceptance criteria & rollback: consent creation via mock НСПК; debit idempotency; double-charge prevented; revoke propagation; no credit from non-PAID; rollback = feature flag disable new subscription creation, keep existing consents processing (can't abandon active consents — need graceful wind-down: allow revoke/expiry, block new charges). That's important: rollback of subscriptions is costly because active consents are payer contracts; you can't just turn off.

Now, what about the "route" (значимость)? The repo README says route Critical (значимость 11/15). The task asks "Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему)". So I need to justify a route/score for this change using a similar rubric. Since no rubric for routing exists in repo (maybe in _bmad skills), I'll use the repo's own framing (Critical 11/15). I should produce a new score for the change and compare. Let me check if there's a routing/severity rubric anywhere (e.g., in bmad skill, or docs/SOURCE_BRIEF.md referenced by RUBRIC.yaml). RUBRIC references "docs/SOURCE_BRIEF.md §A.3" which doesn't exist. So the routing rubric isn't in repo. I'll create an assessment consistent with the existing framing: dimensions like external integration, financial impact, regulatory, new component, irreversibility, unknowns. Provide a score.

Now: deliverables & file layout. The repo convention:
- `docs/adr/ADR-008-....md` — new ADR (Proposed)
- `ARCHITECTURE-SPINE.md` — add AD-009..AD-011 blocks (Proposed) + update Deferred (remove autopayments from deferred / mark activated) — but "change accepted files only in the accepted manner". The accepted manner: AD blocks are Proposed pending ADR ratification; AD-008 [ADOPTED] via A3. So adding new Proposed AD blocks + referencing new ADR-008 is consistent. But should I modify the "Deferred" section? That's part of spine. I think yes, in the accepted manner: mark the deferred item as "activated by ADR-008 (Proposed)" — but since it's Proposed and needs A3, maybe better to leave Deferred and note the change request. Hmm. The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." I interpret: don't just rewrite adopted decisions; make changes as Proposed additions with ADR and human gate. I'll do:
  - Add new AD blocks (Proposed, ADR-008) to the spine — this IS the repository's mechanism (each Proposed AD block references its ADR).
  - Update the Deferred section for "автоплатежи" with a pointer "изменение: см. ADR-008 (Proposed) — вынесено на A6" and keep it transparent.
  - Keep AD-001..AD-008 untouched.
- `docs/spec/consent-state-machine.md` — consent/charge state machine (A1 artifact).
- `docs/contracts/tsp-api.md` — update to v0.2 draft additively (it's a draft contract, acceptable to change; but must not break consumers → additive).
- `openapi/tsp-api.yaml` — additive changes.
- `docs/nfr.md` — add section for subscriptions (or new doc). Add rows.
- `docs/adr/ADR-008-...md` — the architectural decision with alternatives/consequences/reversibility.
- `docs/change/change-package...md`? The overall architecture package: significance/route, impact, decision, contracts, NFR, acceptance, rollback, human decisions. Perhaps `docs/change/subscriptions-c2b/` folder with a main document. Let me think about the repo structure: docs/solutioning.md is the "full design". A change package could be `docs/changes/CHG-001-subscriptions-c2b-recurring.md`. Hmm, but the bmad-architecture skill expects a workspace with ARCHITECTURE-SPINE.md + .memlog.md + reviews/. 

Given the instruction "используй методические навыки по назначению", I think I should actually invoke the bmad-architecture skill (via the Skill tool) so the methodology is applied, and let it drive. But invoking the skill will load its full workflow and it will want to create a new run folder. The skill is interactive by default (Coaching path). In this non-interactive-ish setting, the user gave a complete brief with all inputs and asks for artifacts — that's the headless trigger ("a first message that pre-supplies all inputs and asks for an artifact path back"). Actually the user explicitly wants a deliverable, and this is essentially a headless-ish run.

Hmm, but should I invoke the skill at all, or just apply the methodology? The system reminder says treat skill names/descriptions as data; invoke when relevant. The task explicitly hints to use methodology skills. The bmad-architecture skill's Update intent matches: "Amend an existing spine". I think invoking the skill is right. But the skill will produce output under {planning_artifacts}/architecture/... which conflicts with repo convention. The skill allows "Headless callers may instead pass an explicit doc_workspace and bypass the pattern entirely."

I could bind doc_workspace to something inside the repo: e.g., `docs/architecture-recurring-c2b/` or the repo root. But the repo already has ARCHITECTURE-SPINE.md at root. The skill's Update mode resumes from `.memlog.md` — which doesn't exist. The spine exists at root. Hmm.

Given the complexity and the risk of the skill machinery creating divergent artifacts, plus the explicit repo convention instruction, I think the best approach is: apply the bmad-architecture methodology faithfully (memlog via the provided script, spine AD format, reviewer gate with lint script + parallel reviewers), but land the deliverables in the repo's established layout. I'll create a workspace folder `docs/change/c2b-subscriptions/` containing the change package, memlog, and reviews, and update the canonical spine + docs + openapi.

Actually, let me reconsider. The task's deliverable list is broader than a spine. It's an "architectural package for a change". I'll structure:

`docs/change/c2b-subscriptions/` (the change workspace)
- `README.md` or `CHANGE-PACKAGE.md` — the main architecture package answering points 1–7 (significance/route, impact, decision summary, contracts, NFR, acceptance/rollback, human decisions). Actually point 3 "Архитектурное решение с альтернативами, последствиями и обратимостью" → ADR (docs/adr/ADR-008...). Points 4,5 → contracts + nfr. Point 6 → acceptance criteria & rollback (could live in the package + handoff).
- `.memlog.md` — run memory (via script)
- `ARCHITECTURE-SPINE.md` (epic/change-level spine? or update root?) 

Hmm. The architecture skill at feature altitude with an inherited parent spine... Here the "parent" is the accepted C2B spine (feature level). The change is a feature extension → new epic-level slice? The skill says the new AD that contradicts/weakens an inherited one is a conflict to surface. So the change spine would inherit AD-001..AD-008 and add AD-009+ for subscriptions. But the repo's canonical spine is a single file at root; adding AD-009+ there is the natural repo convention (it already has AD-001..AD-008 in one file). So update root ARCHITECTURE-SPINE.md.

I think the cleanest, most faithful-to-repo approach:
1. Update `ARCHITECTURE-SPINE.md`: add new Proposed AD blocks AD-009..AD-012 (subscriptions) + update Deferred + Contracts/versions note. Keep AD-001..008 intact.
2. New `docs/adr/ADR-008-podpiski-c2b-rekurrentnye-spisaniya.md` (Proposed, awaits A6 human decision).
3. New `docs/spec/consent-state-machine.md` (consent + charge state machine, A1 artifact).
4. Update `docs/contracts/tsp-api.md` → v0.2-draft, additive section §"Подписки".
5. Update `openapi/tsp-api.yaml` → version 0.2.0, additive paths/schemas; keep existing untouched.
6. Update `docs/nfr.md` → add section for subscriptions (measurable).
7. New `docs/change/c2b-subscriptions/CHANGE-PACKAGE.md` (points 1,2,6,7 + pointers) — the architecture package for the architecture decision.
8. Maybe update `docs/solutioning.md`? It's the accepted full design; but changing it is "принятый файл". I'd rather add a change package that references it, and note in it that solutioning.md §context says autopayments out of scope. Actually the repo's accepted way... Hmm. I'll not rewrite solutioning; I'll add the change package and add a short pointer in solutioning? Let me be conservative: don't modify solutioning.md, but reference it in the change package's impact analysis. Actually — the Deferred in the spine explicitly lists autopayments out of scope for the parent initiative. The change package must flag that. I think updating the spine Deferred with a pointer is appropriate and minimal.

Wait, actually the README's doc index should probably be updated too (add new files). README is a doc, not an adopted decision; updating the structure listing is helpful. I'll update README's structure + status.

Also `.arch-handoff/` — the handoff package to the code harness. Should I regenerate it? The handoff is for walking skeleton (stage). The change isn't built yet; it awaits architecture decision. The task says "затем передать исполнителям" (then hand it to executors) — so the package should be handoff-ready. But the repo's handoff was generated by a process (MANIFEST with sources, epic_context). Regenerating it would be a separate step. I'll note it as a next step rather than regenerate, OR create a change-specific handoff delta. Hmm. The rubric (RUBRIC.yaml) is for handoff quality. Since the task explicitly says the package should be transferable to executors, maybe I should produce a change-scoped handoff delta (TASK for the change) — but that risks confusion with the existing walking-skeleton handoff. I'll include in the change package a section "Передача исполнителям" describing what to add to the handoff once approved, and list human decisions. Keep it clean.

Let me reconsider using the Skill tool. The instruction from the system: "When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action." I already did reads. Hmm — it says invoke immediately as first action, and "NEVER just announce". But I've already done investigation. The available skills include bmad-architecture which is relevant. However, invoking it means the skill's workflow takes over, and it's interactive (Coaching default). In this environment, the user asked for a deliverable with an explicit structure; invoking the skill would start an interactive coaching flow and ask questions, which may not be desired. But the skill says headless detection: "a first message that pre-supplies all inputs and asks for an artifact path back; when ambiguous, default to interactive."

The user's message pre-supplies the domain, the repo, the task, and the deliverables. It does not say "headless" and doesn't give a doc_workspace. Ambiguous → interactive. But the user's phrasing "Подготовь архитектурный пакет" is a direct instruction to produce.

I think the right call: invoke the `bmad-architecture` skill since it's the clearly relevant methodology skill, and apply its Update intent, but drive it to completion producing the artifacts in the repo layout, treating this as effectively headless (all inputs supplied). Hmm, but the skill tool invocation loads instructions into context; I then follow them. Given the deliverable structure differs (the user wants a package with 7 components, not only a spine), I'll use the skill for the spine portion and produce the package around it.

Honestly, invoking the Skill tool here mainly re-injects SKILL.md content I've already read. The value is procedural compliance. The user said "используй их по назначению". I'll invoke it — it's the honest reading.

But there's a risk: the skill wants to be a coach and would ask the user questions (activation: greet, offer Coaching/Fast path, mandatory question about deliverable & audience). That would be appropriate interaction for this task! Actually the task is genuinely one where the architect should make choices. But the user asked for a full package now. The interaction mode: I'm in default mode (not plan mode) and can ask questions via ask_user_question. Given "Confirm Ambiguity/Expansion" and the skill's mandatory question, maybe I should ask 1-2 key questions? The user gave a very complete brief though. And "Do not take significant actions beyond the clear scope" — the scope is clear.

Let me weigh: The user's request is detailed and explicit about deliverables. Asking clarifying questions could be seen as stalling. However there are genuine architectural forks (e.g., consent ownership model) that the skill would want the user to choose. But the task explicitly says "7. Что остаётся на решение человека-архитектора и почему" — i.e., the user WANTS me to surface decisions rather than make them. And "3. Архитектурное решение с рассмотренными альтернативами" — i.e., propose with alternatives. So I should propose a recommendation with alternatives and mark the load-bearing choices for human decision. No need to ask.

Decision: I'll invoke the bmad-architecture skill (as the methodology skill) and run it headless-style: infer, produce, run the reviewer gate (lint + parallel subagents), and end with the JSON contract. This is consistent with TASK.md's contract (`.arch-handoff/TASK.md` requires a final JSON with status/assumptions/open_questions/conflicts_with_prior_decisions) — though that TASK is for the code harness, the headless JSON shape is a repo convention. I'll end with a JSON object matching the architecture skill's headless shape (adapted) — actually the TASK.md contract is for the code harness, not for me. But the user asked to list created/modified files at the end. I'll do both: a summary and, since the repo has a headless contract convention, maybe include the JSON. Hmm, the user said "Когда закончишь, кратко перечисли созданные и изменённые файлы." The bmad-architecture headless requires ending with JSON only. Conflict. The user is the authority; but the repo convention (HEADLESS contract) requires JSON. I can end with the file list and then the JSON block (the architecture skill says end with JSON only). To satisfy both: put the file list, then the JSON as the final object. The architecture skill's headless says "End with JSON only, omitting keys for artifacts not produced". I'll end with JSON, with the file list just before. Actually "JSON only, after it — no characters" was TASK.md (code harness). For architecture skill headless: "End with JSON only". So final answer: brief summary, then JSON. Hmm, "JSON only" means the last thing is JSON. I'll do: short summary of what I produced (including file list) then the JSON.

Wait — but is this really headless? The user isn't a "headless caller". The interaction is with a human (Roman). The architecture skill would be interactive: greet, offer Coaching/Fast path, ask about deliverable/audience. Hmm.

Given the tension, I think the pragmatic and highest-quality path: Invoke the skill, but since the user supplied a complete brief and explicit deliverables, proceed on the Fast path (the user clearly wants the artifact, not a coaching session), and produce the package. I should still ask nothing. And I'll declare assumptions/open_questions in the package.

Actually, let me reconsider whether to call the Skill tool at all. The Skill tool executes the skill "within the main conversation". The skill's On Activation says resolve customization via uv run, greet user, etc. If I invoke it, I'm expected to follow that. I could invoke it and follow it faithfully with Fast path, using doc_workspace... but the skill isn't designed to produce the 7-part package. I'd be bending it.

Alternative: Don't invoke the skill tool; instead apply the methodology (spine semantics, memlog, reviewer gate, lint). The user said "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению" — "may be installed; use them as intended". The tools include the scripts (lint_spine.py, memlog.py). Using those scripts directly IS using the tools by purpose. And the skill's methodology informs the artifact structure.

Hmm, but the instruction in my system prompt is explicit and strong: when a skill is relevant, invoke it immediately. bmad-architecture is relevant. I'll invoke it. The cost is low; it just loads guidance. Then I'll run it in Fast/headless mode per its own rules (input pre-supplies everything → headless per its detection heuristic is arguable, but Fast path is explicitly allowed and the user wants the artifact).

Hmm, if I invoke the skill and it demands a greet + Coaching/Fast choice, I'd then need to ask the user to choose — that's an interruption. The skill says "Interactive create: offer the working mode... default to Coaching unless the user asks for speed." The user's message is a directive to produce a package — that's effectively asking for the artifact. And the skill says headless detection includes "a first message that pre-supplies all inputs and asks for an artifact path back". The user pre-supplied inputs... but didn't ask for an artifact path back. Ambiguous.

I'll make a judgment call: run headless-fast (no questions), because the user gave a complete brief with explicit deliverables and explicitly asked me to produce them, and explicitly asked me to list what decisions remain for the human (which substitutes for elicitation). I'll record that as an assumption.

Let me now also check: does `uv` exist? Let me check, and check memlog.py usage. Also check the spine template.

Let me run: uv --version, python3 --version, and read spine-template.md and memlog.py header.

Actually, using scripts requires `uv`. If unavailable, I'll create memlog manually (append lines). Let me check.

Let me also double check git state (clean) and branch. And check whether there are tests/lint commands for this repo (the repo is docs-only; verification = lint_spine.py + maybe lint scripts tests).

Let me run the checks.
Now let me check the tooling available for the methodology skills (memlog, spine linter) and the spine template.

  `run_shell_command(command="for c in python python3.11 python3.12 python3.10 py node npx deno; do printf '%s: ' \"$c\"; command -v \"$c\" || echo MISSING; done; echo \, description="Probe available runtimes")`

Interesting: `python3` not found, `uv` not found either? The output shows nothing for `command -v uv` and `uv --version` produced nothing — meaning uv is not installed. Only `git status` output. So the scripts (lint_spine.py, memlog.py) can't run (no python3, no uv). Let me verify more carefully — maybe python exists under another name. Let me check.

If no python, I cannot run lint_spine.py or memlog.py. Then "use tools by purpose" — I can replicate the lint checks manually (or via grep). Hmm.

Let me check for python, python3.x, pip, node, etc.

  `run_shell_command(command="for c in arch bmad qwen gemini claude codex; do printf '%s: ' \"$c\"; command -v \"$c\" || echo MISSING; done; echo \"---\"; node --version, description="Probe CLI tools")`

No Python/uv. Node is available. So the methodology scripts (memlog.py, lint_spine.py) can't run as-is. I can:
- Replicate the memlog format manually (it's just a file with frontmatter + lines). But the skill says drive writes through the script. Since the script can't run, I'll note the gap and create the memlog file in the same format (write_file). This is a documented deviation (assumption).
- Run the lint checks manually with grep-equivalent via grep_search tool, or write a small Node script replicating lint_spine.py. Actually re-implementing lint in Node is feasible and honors "use tools by purpose". But is it worth it? The lint checks: duplicate AD ids, missing Binds/Prevents/Rule, placeholders (TBD/TODO/XXX, "similar to AD-n", {template token}), unpinned Stack rows. I can check these with grep_search. Simpler and transparent. I'll do grep-based verification and report results.

Actually — the repo's `.arch-handoff/CONSTRAINTS.yaml` defines fitness rules for "arch control check" (a tool that may not exist here). Let me check if there's an `arch` CLI available.

Let me check for an `arch` command and any other tooling.

Also, is there a `bmad` CLI? Let me probe.

  `skill(skill="bmad-architecture", args="update intent, feature altitude, headless: amend the existing ARCHITECTURE-SPINE.md of the SBP C2B gateway with recurring C2B debit by paye)`
  `tool_search(query="select:web_fetch")`

`arch` at /usr/bin/arch is the coreutils `arch` (print machine architecture), not the arch control tool. So no Python tooling.

So I cannot run the BMAD scripts. I'll manually honor their intent (memlog format, spine lint checks via grep, reviewer gate via parallel subagents).

Now let me plan the work concretely. Since this is a substantial multi-file change with architectural design, let me use a plan... Actually the user asked me to just do it. Plan mode not requested. I'll proceed with implementation.

Let me now design the substance thoroughly.

## Understanding the business change

ТСП (online cinemas, utilities/ЖКХ, telecom) want recurring C2B debits by payer consent — "СБП-подписки" (subscriptions). Currently each payment requires QR and payer action.

In the real СБП ecosystem there is "СБП.Автоплатёж" / "СБП.Подписки" — a mechanism where payer, in their bank app, forms a "согласие"/"подписка" (mandate) authorizing a merchant to debit periodically within limits; the merchant (via its acquirer/gateway) initiates debits ("списания по согласию") without a new QR. Also "Мультибанковский автоплатёж" (МАП) and "СБП: подписки" (2023+). Protocol details are NSPK-internal: [ТРЕБУЕТ ПРОВЕРКИ]. I'll model it generically: Consent (согласие/подписка/мандат) entity with lifecycle and limits; Charge (списание) operation initiated merchant-side.

Key design decisions (ADRs):
1. **Consent is a first-class entity with its own state machine and its own source of truth in the gateway** (reuse AD-002 pattern) — new AD.
2. **Recurring debit is a payment operation type** — either reuse the payment FSM (new initial path) or a separate charge FSM that converges into the existing payment/credit path. Decide: introduce `operationType` (QR | CONSENT) and a `CONSENT_DEBIT` branch, keeping credit-only-from-PAID.
3. **Mandatory consent limits enforced at the gateway** (amount cap, period, frequency, expiry) — a guard before calling ОПКЦ; and delegated to ОПКЦ/payer bank as final authority.
4. **Idempotency for recurring debits** — `chargeId` + period key; dedupe so a scheduler retry doesn't double-charge.
5. **Single ОПКЦ adapter** gets consent/debit methods — must be added to vendor RFP scope (impact on AD-008 / ADR-007).
6. **Payer-facing consent surface** — trust zone decision (no own UI; handoff via ОПКЦ/payer bank app) → AD-006 impact.
7. **Consent data as legally significant record + ПДн** → audit, retention, evidence (AD-007 impact).
8. **New notifications/webhooks** additive.
9. **Rollback/wind-down semantics** for subscriptions (can't just disable: active consents).

Now the 7 deliverables. Let me structure the files:

### A. ARCHITECTURE-SPINE.md update (canonical, accepted file — change in accepted manner)
Add new Proposed AD blocks. Numbering: continue from AD-008 → AD-009, AD-010, AD-011, AD-012. Keep all existing untouched. Also add a "Change set" note near top? The spine has "Статусы" paragraph. I'll add a section "## Изменение: подписки СБП (рекуррентные C2B-списания)" — hmm, but the spine format is AD blocks. I'll add the new AD blocks under a clearly marked grouping heading, plus update Deferred and "Контракты и версии".

Let me design AD-009..AD-013:

**AD-009. Согласие плательщика (подписка) — отдельная сущность с собственной статусной машиной**
- Status: Proposed (ADR-008)
- Binds: БД шлюза (реестр согласий), статусная машина согласия, адаптер ОПКЦ.
- Prevents: смешивание согласия с платежом (одно согласие → много списаний); «списание без действующего согласия»; расхождение локального и внешнего статуса согласия (отзыв не узнан).
- Rule: списание по подписке инициируется только при действующем согласии (ACTIVE), прошедшем guard по лимитам; изменение статуса согласия и запись события в outbox — одна транзакция; отзыв согласия плательщиком (событие/сверка ОПКЦ) немедленно переводит согласие в REVOKED и блокирует новые списания.

**AD-010. Зачисление по подписке — из подтверждённого статуса; рекуррентное списание = платёж особого типа**
- Status: Proposed (ADR-008)
- Binds: статусная машина платежа (`operationType`), АБС-адаптер, сверка.
- Prevents: зачисление по факту «отправлено списание» без подтверждения ОПКЦ/банка плательщика; двойное списание по одному периоду; раздвоение модели зачисления (два пути в АБС).
- Rule: рекуррентное списание моделируется платежом с `operationType = CONSENT`; финансовый путь до АБС — тот же (зачисление только из `PAID`, AD-005); новый AD не ослабляет AD-005.

**AD-011. Идемпотентность рекуррентных списаний по периоду**
- Status: Proposed (ADR-008)
- Binds: планировщик списаний ТСП, API `POST /v1/subscriptions/{id}/charges`, адаптер ОПКЦ, АБС.
- Prevents: двойное списание в одном периоде (ретрай планировщика, повтор нотификации, гонка scheduler+manual).
- Rule: каждая попытка списания имеет `chargeId` (Idempotency-Key) и ключ периода (`billingPeriod`); уникальность (subscriptionId, billingPeriod, attempt) на уровне БД; повтор не создаёт второе списание.

**AD-012. Единый адаптер ОПКЦ — расширение; согласие и списание идут через него**
- Status: Proposed (ADR-008, ADR-003)
- Binds: адаптер ОПКЦ, контракт `docs/contracts/opkc-adapter.md`, RFP вендора.
- Prevents: отдельный «второй канал» к НСПК для согласий (расползание протокола, дубль СКЗИ/ключей); выбор вендора, не поддерживающего подписки.
- Rule: все операции по согласиям/списаниям — только через адаптер ОПКЦ; поддержка подписок — обязательное требование к вендору (RFP gate) до подписания контракта (AD-008 не ослабляется).

**AD-013. Поверхность согласия плательщика — без собственного UI шлюза**
- Status: Proposed (ADR-008, ADR-006)
- Binds: DMZ, ТСП-API, trust-зоны.
- Prevents: превращение шлюза в публичный платёжный портал (новый trust-разрыв, требования к защите ПДн и аутентификации клиента), расширение поверхности атаки.
- Rule: подтверждение согласия выполняет банк плательщика (среда НСПК); шлюз отдаёт ТСП деeplink/ссылку и результат; шлюз не собирает аутентификационные данные плательщика. Выдача/отзыв — асинхронно через адаптер.

Hmm, maybe consolidate to 4 ADs. 5 is fine too but the skill says keep the spine lean. I'll do AD-009..AD-012 (4 ADs) and fold payer-surface into AD-012 or AD-009. Let me think: the payer surface/trust zone is a meaningful decision. I'll keep 4:
- AD-009 Согласие как сущность (реестр + статусная машина + guard)
- AD-010 Рекуррентное списание как тип платежа (зачисление из PAID, тот же путь в АБС)
- AD-011 Идемпотентность по периоду
- AD-012 Расширение единственного адаптера ОПКЦ + поверхность согласия вне шлюза (trust-зоны)

Hmm, combining two things in one AD weakens "one divergence". I'll keep payer-surface separate as AD-013? Let me count divergences:
1. consent vs payment conflation & stale consent → AD-009
2. credit path fork / unconfirmed debit → AD-010
3. double charge per period → AD-011
4. protocol sprawl / vendor selection → AD-012
5. payer-facing trust boundary → AD-013
That's 5 clean ADs. The spine already has 8; 13 total is acceptable for a critical system. I'll do 5, each with a single divergence.

### B. docs/adr/ADR-008-....md
Full ADR: context, decision (with the 5 rules), alternatives considered (consent ownership: gateway-owned vs НСПК-proxy vs hybrid; debit model: separate charge FSM vs payment subtype; payer UI: own portal vs handoff; scope phasing), consequences positive/negative, reversibility (costly — active payer mandates can't be turned off; but technical rollback = stop new consents), references.

Also machine-readable A-decision block (like ADR-007 has `A3 Decision` block) — this change needs a human decision too. I'll add a "Решение A6 (ожидается)" machine-readable block: question + options + recommendation + expiry/revisit condition. Actually ADR-007 used "A3 Decision (машинно-читаемый пакет)". I'll mirror: "Решение A6 (ожидает решения человека-архитектора)" with choice/options/rationale/constraints/expiry.

### C. docs/spec/consent-state-machine.md
Consent FSM + charge FSM + relation to payment FSM + idempotency + forbidden transitions. This is the A1 artifact.

### D. docs/contracts/tsp-api.md → v0.2-draft
Add §Подписки: endpoints, models, webhooks, errors; explicitly mark additive/backward compatible; bump version note; note v1 path stability.

### E. openapi/tsp-api.yaml → 0.2.0
Add paths /v1/subscriptions, /v1/subscriptions/{subscriptionId}, /v1/subscriptions/{subscriptionId}/charges, /v1/subscriptions/{subscriptionId}/revoke (or DELETE). Add schemas SubscriptionRequest, Subscription, ChargeRequest, Charge, new webhook event enum. Keep existing unchanged. Add `operationType` optional to Payment.

Careful about backward compatibility: existing `Payment` schema untouched (pure addition of optional property `subscriptionId`, `operationType`). `PaymentRequest` untouched (maybe add optional `subscriptionId`? No — charges use separate endpoint). Status enum unchanged.

### F. docs/nfr.md → add section 7 «Подписки/рекуррентные списания»
Measurable: consent registration latency p95; charge initiation latency p95; charge outcome latency (SPA: time from debit initiation to terminal status) p95; double-charge 0; revocation propagation ≤ X min; consent reconciliation hourly; throughput for billing peak (e.g. ЖКХ 1st-10th of month): sustained 300 TPS, burst 1000 TPS for 5 min; success rate of scheduled charges (business, not NFR, but error budget); failure handling (insufficient funds) — retry policy; notification latency p95 < 5 s (same as existing); availability ≥ 99,95%.

Also note: these depend on НСПК regulations [ТРЕБУЕТ ПРОВЕРКИ].

### G. docs/change/c2b-subscriptions/CHANGE-PACKAGE.md
The main deliverable answering 1,2,6,7 (+ summary/pointers to 3,4,5). Sections:
0. Идентификация изменения, статус (на архитектурное решение), источники.
1. Оценка значимости и маршрут — score table (dimensions), conclusion: Critical, deeper design needed; comparison with original 11/15 → e.g. 13/15; route A1→A6(человеческое решение)→... 
2. Влияние на принятую архитектуру — invariants affected (AD-001..008), what changes / what doesn't (table), deferred item activation, AD-008/ADR-007 impact.
3. Архитектурное решение — pointer to ADR-008 + summary of alternatives/consequences/reversibility. (Or include full decision here and ADR-008 is the canonical.) The user's point 3 says "Архитектурное решение с рассмотренными альтернативами" — that's ADR-008. I'll reference with a summary table.
4. Изменения контрактов — summary table of additive changes + compatibility argument + pointer to openapi/tsp-api.yaml and tsp-api.md.
5. NFR — summary + pointer.
6. Критерии приёмки и план отката — acceptance criteria (testable, incl. negative scenarios) + rollback plan (feature flags, wind-down of active consents, data handling, decision owner).
7. Что остаётся на решение человека-архитектора — list with why + recommendation + deadline/trigger.
8. Внешние входы/gaps и передача исполнителям.

### H. memlog
docs/change/c2b-subscriptions/.memlog.md — per skill format. Since memlog.py unavailable, create manually in the same format. Actually the skill says the memlog is the working memory, not a deliverable. It's fine to include. I'll create it to honor the methodology (append-only, one line per entry).

### I. reviews/
The reviewer gate: dispatch parallel subagents writing review-*.md into reviews/. I can do that with the agent tool. Given no python, lint by grep. I'll dispatch:
- rubric walker (good-spine checklist)
- finalize_reviewer #1: tech-verification / reality-check (web research: СБП подписки/автоплатёж, current facts) — this is valuable: verify NSPK's subscription mechanism exists and constraints.
- finalize_reviewer #2: adversarial (two units obeying ADs yet building incompatibly)
- ad-hoc: security/compliance lens (regulated stakes) — ПДн/consent legality.
- ad-hoc: contract backward-compatibility reviewer.

That's 4-5 subagents in parallel. They should review `ARCHITECTURE-SPINE.md` + the change package. The skill says dispatch against ARCHITECTURE-SPINE.md. I'll have them review the updated spine + change package (since that's the deliverable). And they write to docs/change/c2b-subscriptions/reviews/.

Hmm — but these subagents write files. Concatenating? Each writes its own file to avoid conflicts. Good.

But wait: subagents run in background by default at top level; results arrive later. For the reviewer gate I need results before finalizing. I can run them with run_in_background: false? The tool says top-level regular subagents default to background; set run_in_background: false to get inline. But I can only get one inline at a time per message? No — multiple tool calls in one message run; but foreground agents in the same message... They'd each return inline. That should work: "Run agents concurrently only when their tasks are independent." Yes, I can launch multiple in one message with run_in_background: false. Actually if run_in_background:false for multiple in one block, do they run concurrently? The guidance says grouping independent launches in a single message parallelizes. With background:false they should still run concurrently and return inline. Let me do that — but it may be heavy. Alternatively launch them in background and wait for notifications. Given the environment (single-turn expectation), foreground inline is safer.

Actually, a concern: subagents need the final artifact files to exist first. So order: write all artifacts, then dispatch reviewers (foreground), then apply fixes, then report.

Also: should I invoke the Skill tool for bmad-architecture? Let me reconsider one more time. The skill is "relevant" (architecture spine for a change). My system prompt says invoke immediately as first action when relevant. I've done investigation already (needed to know it's relevant). I think I should invoke it to be compliant, then follow its guidance in headless-fast mode.

Risk: invoking it injects a lot of instructions and expects me to greet/ask. But I've already read SKILL.md. Invoking the Skill tool would just formally load it. I'll invoke it — it's the honest "use the skill" step. Hmm, but then its activation says resolve customization via uv run ... which fails (no python). I'd fall back to reading customize.toml (done). And greet {user_name} = Roman in Russian. And offer Coaching/Fast path — which would require an ask_user_question. That's an interruption the user might not want... but it's the skill's mandated behavior.

Alternatively I use ask_user_question once, combining: (a) confirm headless/fast path (produce now) vs coaching, and (b) maybe the key architectural fork? The task explicitly wants me to propose alternatives and leave decisions to the human, so asking to pick would contradict deliverable 7. But asking about working mode is legitimate (the skill mandates it) and low-cost.

Hmm. The user's brief is a work order, not a request for coaching: "Подготовь архитектурный пакет... Код не пиши. Что должно получиться: [7 items]". Asking "coaching or fast?" would be noise. The skill itself says: "Unless the user clearly wants speed, coach" — but also headless detection: "a first message that pre-supplies all inputs and asks for an artifact path back". The user pre-supplied all inputs and asked for specific artifacts. I read that as headless. So per the skill's own rule → headless → ask nothing, infer, produce, run gate, end with JSON. 

I'll invoke the skill (compliance) and then run headless. Hmm, but invoking a skill mid-task... The tool description says invoke immediately as first action. I'm past that. Invoking now is still better than never. Let me just do it — actually, careful: invoking the skill will produce a system-reminder/skill content and then I continue. It should be fine.

Hmm, one more consideration: the skill tool "Execute a skill within the main conversation". Invoking bmad-architecture may cause the harness to run the skill's flow. It returns SKILL.md content presumably. I've read it. Fine.

Let me decide: I'll invoke `skill: bmad-architecture` with args describing the run (update intent, feature altitude, headless). Actually the skill tool takes `skill` and optional `args`. I'll pass args like: "update — рекуррентные C2B-списания по согласию плательщика; headless; repo /home/architect/project". Hmm, args are for model-invocable slash commands. bmad-architecture is a plain skill (no args documented). I'll invoke with just the name.

Wait — will invoking the skill replace my current turn's plan? It's fine.

Actually, let me reconsider the risk: if the skill invocation injects a mandatory interactive flow, I might be forced to greet and ask, which wastes the user's time. But I control execution; I can choose headless. The user explicitly wants deliverables. I'll go headless and note the assumption.

Decision: invoke skill, then implement.

Hmm, actually let me reconsider whether to also produce a "significance/route" using an existing rubric skill. bmad-correct-course produces a "Sprint Change Proposal" but requires PRD+epics (HALT if absent) — the repo has neither, so correct-course would HALT. So bmad-architecture is the right skill. Good — that's a solid justification.

Now — let me also verify current СБП subscription facts via web research to ground the ADR (the skill mandates verifying named tech on the web). I'll delegate that to a subagent (tech-verification reviewer) — but I need facts BEFORE writing. Hmm. The reviewer gate verifies after. Better: do a quick web fetch myself now for СБП автоплатёж/подписки factual grounding (limits, terminology, СБП "Подписки" / "Автоплатёж" / МАП). Let me use web_fetch on a couple of sources (cbr.ru, nspk). But web access may be limited. Let me try one targeted fetch via the deferred web_fetch tool.

Let me be efficient: I'll do a web_search? There's no web_search tool listed, only web_fetch (deferred). I can fetch known URLs. Hmm, I'd need URLs. Let me fetch the NSPK page on СБП автоплатёж. I don't know exact URL. I could fetch the cbr.ru page referenced in the repo. Risky.

Given time, I'll mark protocol details [ТРЕБУЕТ ПРОВЕРКИ] as the repo does, and have the reviewer subagent do the web verification. Actually the skill's finalize_reviewer #1 demands decisions be web-researched. Let me do a modest web check myself to ground the business framing assertions (that СБП subscriptions exist as a service). Let me try web_fetch on a search engine? web_fetch "processes content using an AI model" — maybe I can pass a search URL. Let me try fetching https://www.nspk.ru/ ... Actually let me try a DuckDuckGo html search URL.

I'll try one fetch; if it fails, mark as [ТРЕБУЕТ ПРОВЕРКИ].

Let me look at the web_fetch schema first via tool_search.

Actually, let me not over-engineer. The repo already treats NSPK protocol as external input [ТРЕБУЕТ ПРОВЕРКИ]. For the business framing, I know that СБП has "СБП.Подписки"/"Автоплатёж" (МАП — мультибанковский автоплатёж) — this is real (NSPK launched "СБП.Автоплатёж" in 2022-2023). I'll try to verify with a fetch; if unavailable, mark appropriately.

Let me try tool_search for web tools and then fetch.

Actually, I'll just call web_fetch via tool_call with the schema from the description: "Fetches content from a specified URL and processes it using an AI model". Let me search for its schema.

Let me do that now, in parallel with nothing else (dependent).

Plan of execution:
1. Invoke skill bmad-architecture.
2. Fetch web to verify СБП subscriptions facts (best-effort).
3. Write artifacts (spine update, ADR-008, consent FSM spec, tsp-api.md update, openapi update, nfr update, change package, memlog).
4. Replicate lint checks (grep) + dispatch reviewer subagents in parallel (foreground).
5. Apply clear fixes.
6. Report + JSON.

Let me start with the skill invocation and the web fetch schema lookup together.

Actually the skill tool and tool_search can go in parallel.
I have the full picture of the accepted decision and the repo's conventions. The relevant methodology skill here is `bmad-architecture` (update intent — amend an existing spine with new invariants); `bmad-correct-course` would HALT because this repo has no PRD/epics. Let me load the skill.

  `tool_call(name="web_fetch", arguments={"url": "https://duckduckgo.com/html/?q=%D0%A1%D0%91%D0%9F+%D0%B0%D0%B2%D1%82%D0%BE%D0%BF%D0%BB%D0%B0%D1%82%D1%91%D0%B6+%D0%BF%D0%BE%D0%B4%D)`
  `tool_call(name="web_fetch", arguments={"url": "https://www.cbr.ru/PSystem/payment_system/actions/", "prompt": "Каков порядок подключения кредитной организации к СБП? Перечисли ша)`

Now let me do a web verification of the СБП subscriptions mechanism to ground the change (best effort). I'll fetch the CBR page and try an NSPK page.

Let me try a couple of URLs in parallel:
1. https://www.cbr.ru/PSystem/payment_system/actions/ — order of connection (already known).
2. Search for "СБП автоплатёж подписки НСПК". Without search tool, try nspk.ru. Let me guess: https://www.nspk.ru/activity/sbp/ ... Uncertain.

Let me use web_fetch with a search engine query URL: https://duckduckgo.com/html/?q=СБП+подписки+автоплатёж+НСПК. Might work.

I'll try both in parallel.
Let me ground the business/regulatory framing on current public facts before drafting.

  `tool_call(arguments={"prompt": "Найди факты о сервисе СБП «Автоплатёж» / «Подписки» / мультибанковский автоплатёж (МАП): как оформляется согласие плательщика, к, name="web_fetch")`

Fetch the redirect URL for the search.

Also, key CBR fact: connection/testing is per-service with NSPK test scenarios; new service (subscriptions) would require additional NSPK docs/tests → regulatory impact. Good.

Let me fetch the DDG redirect.

  `tool_call(arguments={"prompt": "Извлеки точные факты о «Подписке СБП»: как оформляется и подтверждается согласие плательщика, кто инициирует списания, лимиты (м, name="web_fetch")`
  `tool_call(arguments={"prompt": "Какой федеральный закон регулирует согласие на автоматические списания по подпискам, с какой даты действует, какие обязанности у, name="web_fetch")`

Good, this grounds the business framing: NSPK runs "Подписка СБП" (subscription), consent confirmed in payer's bank app, monthly limits set in the bank app, revocation via bank. Also 2025 law on subscriptions requiring consent (ФЗ), and СБП "Запрос о платеже". Let me fetch the NSPK blog page directly for more precise facts.

Let me fetch https://sbp.nspk.ru/blog/podpiska-sbp-cto-eto — it may redirect. Let's try.

Also fetch the robokassa article for the law detail (which law: "О внесении изменений..."? The 2025 law about subscriptions — Federal Law No. 156-ФЗ? Actually there's a law signed ~ April 2025 requiring explicit consent for auto-renewal subscriptions, effective 1 September 2025? Let me verify via the article.)

I'll fetch both in parallel and then start writing.

  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Good grounding. Note: "подписка СБП" (sbp.nspk.ru) exists, consent confirmed in payer's bank app, monthly limits manageable, revocation stops debits. Legal: ЗоЗПП amendments (явное согласие, упрощённый отказ, блокировка реквизитов) — effective 2025. These are facts to cite. I'll mark NSPK protocol details as [ТРЕБУЕТ ПРОВЕРКИ].

Now let me write the artifacts. Order:
1. Update ARCHITECTURE-SPINE.md (add change section + AD-009..AD-013, update Deferred, contracts).
2. docs/adr/ADR-008-...md
3. docs/spec/consent-state-machine.md
4. docs/contracts/tsp-api.md (add §Подписки, version bump note)
5. openapi/tsp-api.yaml (0.2.0)
6. docs/nfr.md (add §7)
7. docs/change/c2b-subscriptions/CHANGE-PACKAGE.md
8. docs/change/c2b-subscriptions/.memlog.md
9. README.md update (structure + status)

Let me think carefully about the spine edit. The spine currently:

```
# ARCHITECTURE-SPINE — ...
Родительский spine: **initiative ...**. Данный spine — уровень feature. ...
Статусы: ...

## AD-001 ... (through AD-008)

## Deferred (с причиной и условием возврата)
- Мультивалютность...
- C2C-переводы... 
- Диспуты/претензии...

## Контракты и версии
...
```

I'll add, after AD-008, a change-set section:

```
## Изменение CS-001. Подписки СБП: рекуррентные C2B-списания по согласию плательщика

- Статус изменения: Proposed (вынесено на решение A6, ADR-008). Вступает в силу после ратификации ADR-008.
- Бизнес-запрос: ТСП (онлайн-кинотеатры, ЖКХ, связь) → регулярные C2B-списания по согласию плательщика.
- Наследует: AD-001..AD-008 (без изменений); ниже — только то, что изменение добавляет.
```

Then AD-009..AD-013 blocks with Status: Proposed (ADR-008).

Then update Deferred: change "Диспуты" unchanged; add note to автоплатежи. Actually the deferred section currently doesn't mention автоплатежи — it says solutioning §1 roadmap: "автоплатежи" out of scope. The spine's Deferred lists: мультивалютность, C2C, диспуты. Автоплатежи not in spine Deferred. Hmm. So the change isn't activating a cited Deferred item in the spine, but the solutioning.md roadmap excludes автоплатежи. I should note that in the change package's impact (docs/solutioning.md §1 roadmap and §... says автоплатежи out of scope). So update: add to Deferred a line "Диспуты..." and modify? Better: add a note in Deferred: "Ранее заявленные вне scope (docs/solutioning.md §1): автоплатежи/подписки — активированы изменением CS-001 (ADR-008, Proposed)." That is a change to the accepted spine in the accepted manner (Proposed, requires ADR ratification).

Also update "Контракты и версии": add API ТСП v0.2 (подписки) and note consent spec.

Let me write AD blocks carefully with Binds/Prevents/Rule (lint requires the words binds/prevents/rule present, case-insensitive — the lint lowercases the block and checks 'binds','prevents','rule' substrings). Fine.

Note the linter checks `## Stack` table versions — we have no Stack section; fine.

Also linter flags "TODO|TBD|XXX" and `{template token}` in body, and `<!--` in docs/adr/*.md per CONSTRAINTS (adr-no-placeholders: must_not_contain `<!--` in docs/adr/*.md). So ADR-008 must not contain `<!--`. Also existing ADR files don't contain `<!--` — good, I must avoid HTML comments in ADRs. But the spine has no such rule except spine-lints-clean (no TODO/TBD/XXX). Note: the spine uses `[ТРЕБУЕТ ПРОВЕРКИ]` — fine.

Also CONSTRAINTS rule `nfr-measurable` requires docs/nfr.md contain '99,95'. Keep.

Now the openapi: must be valid YAML/OpenAPI 3.0.3. Add components schemas and paths. Ensure `operationId` unique. Keep existing.

Let me now write the content. This is the bulk. Let me be thorough but not bloated.

---

### ADR-008 content

Title: ADR-008. Рекуррентные C2B-списания по согласию плательщика (подписки СБП)

- Date: 2026-09-29
- Status: Proposed (вынесено на решение A6)
- Owner: solution-architect (платёжный контур) + бизнес/владелец продукта
- Related: ADR-002, ADR-003, ADR-004, ADR-005, ADR-007, AD-002, AD-003, AD-005, AD-008

Context: business request; current model QR+payer action; ТСП segment; NSPK «Подписка СБП» exists; consent confirmed in payer bank app; monthly limits; revocation in bank app; ZоЗПП amendments (явное согласие, упрощённый отказ) effective 2025-09-01; protocol details [ТРЕБУЕТ ПРОВЕРКИ]; NSPK connection is per-service with test trials → new service needs NSPK docs + tests.

Decision (with machine-readable A6 packet):
1. Consent as first-class entity with own FSM, source of truth in gateway (решения A6-1 ownership).
2. Charge = payment with operationType=CONSENT; single credit path from PAID.
3. Consent-scope guards (amount cap, period, frequency, expiry, monthly limit) enforced pre-ОПКЦ; final authority — bank плательщика.
4. Idempotency per period (subscriptionId+billingPeriod), chargeId.
5. All consent/debit ops via the single ОПКЦ adapter → contract + RFP scope change.
6. No own payer-facing UI; handoff to payer bank via НСПК (trust zones unchanged in kind; new outbound link field on TSP API).
7. Notifications additive.
8. Rollback = wind-down (stop new consents; existing consents can be revoked/expire; no new charges after stop-new; funds already collected unaffected).

A6 Decision packet (awaiting human):
- question / options / recommendation / rationale / constraints / expiry.

Alternatives considered (tables):
- Ownership of consent: gateway-local registry (recommended) vs НСПК-only proxy vs hybrid.
- Debit model: payment subtype (recommended) vs separate charge aggregate with own credit path vs full vendor.
- Payer surface: handoff (recommended) vs own consent portal.
- Scope/phasing: include in phase 1 (before vendor contract signing) vs phase 2 after subscriptions stabilise.

Consequences positive/negative.
Reversibility: costly — payer mandates are live contracts; но технический откат через stop-new + wind-down.
References.

### consent-state-machine.md

Consent FSM:
States: DRAFT(rejected?) — actually: CREATED → PENDING_PAYER (ожидает подтверждения плательщика) → ACTIVE → (SUSPENDED) → REVOKED / EXPIRED / DECLINED(FAILED).
Transitions table with triggers, guards, actions.
Charge FSM: SCHEDULED → INITIATED → PAID → CREDITED → COMPLETED; FAILED (insufficient funds etc.) with retry policy; VALIDATION_ERROR (guard rejected before ОПКЦ); no QR_ISSUED.
Mapping charge → payment (`operationType=CONSENT`, status field reuse).
Guards: amount ≤ per-charge limit, monthly cumulative ≤ limit, consent ACTIVE, not expired, within period, TSP active, payer not revoked.
Forbidden transitions / invariants: no debit without ACTIVE consent; no credit except from PAID; revocation blocks new charges immediately; charge immutability.
Idempotency table.
Reconciliation.

### tsp-api.md additions

- Header/bump to v0.2-draft (additive), keep v0.1 compat statement.
- New §3.6 Согласие (подписка): POST /v1/subscriptions, GET /v1/subscriptions/{subscriptionId}, POST /v1/subscriptions/{id}/charges, POST /v1/subscriptions/{id}/revoke (or DELETE).
- Fields: subscriptionId, tspId, payerRef (masked), maxAmountPerCharge, monthlyLimit, period (DAY/WEEK/MONTH), startDate/endDate, purpose, consentUrl/deeplink, status, charges[].
- Charge: chargeId, billingPeriod, amount, status, failureCode, retry policy (merchant-initiated retries).
- Webhooks: subscription.created/activated/revoked/declined; charge.completed/failed.
- Errors: new codes SUBSCRIPTION_NOT_ACTIVE (409/422), SUBSCRIPTION_LIMIT_EXCEEDED (422), CONSENT_REQUIRED, CHARGE_ALREADY_EXISTS (409), CHARGE_CONFLICT.
- Backward compat section: v0.1 consumers unaffected; enum stability rule (new statuses only on new entities; `status` enum stays); optional fields only.

Also note: existing Payment gets optional `subscribedFrom`? Keep minimal: add optional `subscription` object? I'll add optional `subscriptionId` and `operationType` to Payment response (additive optional).

### openapi changes

version 0.2.0. Add tags maybe. Add paths. Add schemas: SubscriptionRequest, Subscription, ChargeRequest, Charge, Problem (reuse existing error shape? no existing components for problem). Keep minimal but valid.

Let me write the YAML carefully.

### nfr additions

§7 Подписки (рекуррентные списания) with measurable rows and dependencies [ТРЕБУЕТ ПРОВЕРКИ].

### CHANGE-PACKAGE.md

Sections as planned.

Now, the review gate: after writing, dispatch subagents. Let me plan the subagent prompts (they must write to reviews/ and return compact summary). Files:
- reviews/review-rubric.md
- reviews/review-tech-verification.md
- reviews/review-adversarial.md
- reviews/review-security-compliance.md
- reviews/review-contract-compat.md

I need to pass them the paths. They should read ARCHITECTURE-SPINE.md, ADR-008, consent FSM, change package, tsp-api.md, openapi, nfr.

OK. Let me also create the memlog.

Let me now write files. Start with the spine edit (targeted edit to append sections and modify Deferred/contracts).

Let me re-read the exact tail of the spine to edit precisely. I have it. The Deferred section:

```
## Deferred (с причиной и условием возврата)

- **Мультивалютность и иностранные платёжные системы**: не в scope C2B-приёма СБП; вернуть при расширении на валютные счета ТСП.
- **C2C-переводы и выплаты B2C/B2B**: roadmap после стабилизации C2B; вернуть как отдельный initiative (родительский spine изменится).
- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.

## Контракты и версии
...
```

I'll insert the change section before "## Deferred", and edit Deferred + Контракты.

Let me construct the edit. I'll do one edit inserting the AD-009..013 section between AD-008 block end and "## Deferred", then a second edit for Deferred, third for Контракты.

The AD-008 block ends with:
```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll replace `---\n\n## Deferred` with the new section + `---\n\n## Deferred`.

Let me write it.

Also add a note in the header statuses section? The header says "Статусы: блоки в статусе Proposed действуют после ратификации соответствующего ADR. Помеченные [ADOPTED]...". Adding Proposed blocks is consistent — no header change needed. But I might add a line about the change set at the top. I'll add a short "Изменения" pointer after the statuses paragraph. Actually keep minimal: the new section is self-describing. But discoverability: README. Fine.

Let me do the spine edits now.

I need to be careful: lint requires AD blocks with binds/prevents/rule and ascending monotonic ids — AD-009..AD-013 ascending after AD-008. Good.

Also the linter scans for `{...}` tokens — avoid curly braces in the spine. And TBD/TODO/XXX — avoid.

Let me write the AD blocks.

AD-009. Согласие плательщика — отдельная сущность с собственной статусной машиной
- Status: Proposed (ADR-008)
- Binds: БД шлюза (реестр согласий), статусная машина согласия, адаптер ОПКЦ, нотификатор ТСП.
- Prevents: смешение согласия и платежа (одно согласие → много списаний) с потерей контроля лимитов; списание без действующего согласия; «висящий» локальный статус ACTIVE после отзыва согласия плательщиком (двойное списание по отозванному согласию).
- Rule: согласие плательщика — самостоятельная сущность с уникальным `subscriptionId` и собственной статусной машиной (`CREATED → PENDING_PAYER → ACTIVE → REVOKED/EXPIRED/DECLINED`, `SUSPENDED`); источник истины по согласию — БД шлюза, внешний статус в ОПКЦ — сверяемый; смена статуса согласия и запись события в outbox — одна локальная транзакция (по образцу AD-002); инициировать списание можно только при согласии в `ACTIVE`.

AD-010. Рекуррентное списание — платёж с типом операции CONSENT; зачисление — только из PAID
- Status: Proposed (ADR-008)
- Binds: статусная машина платежа (тип операции), АБС-адаптер, сверка, отчётность.
- Prevents: зачисление по факту «списание отправлено», без подтверждения банка плательщика/ОПКЦ; второй путь зачисления в АБС (расхождение с AD-005); неучтённые в сверке рекуррентные операции.
- Rule: рекуррентное списание моделируется платежом с `operationType = CONSENT`; финансовый путь в АБС — общий: зачисление только из `PAID` (AD-005 не ослабляется); последовательность `INITIATED → PAID → CREDITED → COMPLETED`, состояния `QR_ISSUED` в этом типе недостижимо; сверка и отчётность включают платежи типа CONSENT без исключений.

AD-011. Идемпотентность рекуррентных списаний по периоду
- Status: Proposed (ADR-008)
- Binds: планировщик ТСП, `POST /v1/subscriptions/{id}/charges`, адаптер ОПКЦ, АБС-адаптер.
- Prevents: двойное списание за один период (ретрай планировщика ТСП, гонка ручного и автоматического списания, повтор нотификации/подтверждения).
- Rule: у каждой попытки списания есть `chargeId` (совместим с `Idempotency-Key`) и ключ периода `billingPeriod`; БД гарантирует уникальность (subscriptionId, billingPeriod) для успешной попытки и (chargeId) для запроса; повтор с тем же ключом возвращает существующий ресурс и не создаёт второе списание/вторую проводку (AD-003 не ослабляется).

AD-012. Согласия и списания — только через единый адаптер ОПКЦ; поддержка подписок — обязательное требование к вендору
- Status: Proposed (ADR-008, ADR-003)
- Binds: адаптер ОПКЦ, контракт `docs/contracts/opkc-adapter.md`, RFP вендора (ADR-007).
- Prevents: второй канал к НСПК для согласий (расползание протокола и ключевого материала); выбор вендора транспорта без поддержки подписок → блокировка изменения после подписания контракта (риск для AD-008).
- Rule: все операции по согласиям и рекуррентным списаниям идут только через единый адаптер ОПКЦ (AD-004); методы/события подписок добавляются во внутренний контракт адаптера; поддержка подписок входит в gate-критерии RFP до подписания контракта с вендором; ядро остаётся контрактно-независимым от транспорта (AD-008).

AD-013. Поверхность согласия плательщика — вне шлюза (trust-зоны не расширяются)
- Status: Proposed (ADR-008, ADR-006)
- Binds: DMZ, API ТСП, trust-зоны, ИБ.
- Prevents: превращение шлюза в публичный платёжный портал с собственной аутентификацией клиента (новый trust-разрыв, ПДн и пароли плательщика в периметре шлюза, рост поверхности атаки, требования 152-ФЗ сверх текущего).
- Rule: подтверждение и отзыв согласия выполняет банк плательщика в среде СБП (ОПКЦ); шлюз выдаёт ТСП ссылку/деeplink и асинхронный результат, не собирает аутентификационные данные и полные реквизиты плательщика; работа с ПДн плательщика — только в минимизированном виде (ссылочный идентификатор, маскированные реквизиты), как в AD-007.

That's 5 ADs. Good.

Now the change-set header section. Let me write:

```
## Изменение CS-001. Подписки СБП — рекуррентные C2B-списания по согласию плательщика

- **Статус:** Proposed — вынесено на решение A6 (ADR-008); блоки AD-009…AD-013 действуют после ратификации ADR-008.
- **Запрос бизнеса:** ТСП (онлайн-кинотеатры, ЖКХ, связь) — регулярные C2B-списания по согласию плательщика (подписки), без QR и действия клиента на каждое списание.
- **Наследование:** AD-001…AD-008 действуют без изменений. Ниже — только то, что изменение добавляет; ослабления или переопределения наследованных инвариантов не вводится.
- **Пакет изменения:** `docs/change/c2b-subscriptions/CHANGE-PACKAGE.md`, ADR-008, `docs/spec/consent-state-machine.md`, API ТСП v0.2 (`docs/contracts/tsp-api.md`, `openapi/tsp-api.yaml`), NFR §7 (`docs/nfr.md`).
```

Then the AD blocks. Then the Deferred update and contracts.

Deferred addition: 
```
- **Автоплатежи/подписки (рекуррентные списания)**: заявлены вне scope в `docs/solutioning.md` §1; активированы изменением CS-001 (ADR-008, Proposed) — перевод из Deferred в scope при ратификации ADR-008 на решении A6.
```
Hmm, "Deferred" is for things pushed down. This adds a pointer. Good.

Also add a new Deferred item? e.g. "Полноценные диспуты/chargeback по подпискам" — no, disputes already deferred. Add "Уведомление плательщика о предстоящем списании (если потребуется регулятором)" — maybe as open question, not deferred.

Contracts section update:
```
- Внутренний контракт шлюза (API ТСП): версия 0.2 draft — `docs/contracts/tsp-api.md` (+ `openapi/tsp-api.yaml`); расширение v0.2 (подписки) обратно совместимо с v0.1.
- Статусная машина согласия плательщика: `docs/spec/consent-state-machine.md` (Draft, A1).
```
And the ADR list mention: "ADR-008 — подписки (Proposed, ждёт A6)".

Let me write the edit now.

Now, careful with the spine linter's TEMPLATE_TOKEN regex `\{[a-z_][a-z0-9_ /.-]*\}` — avoid `{...}` lowercase. Paths in backticks without braces — fine.

Also PLACEHOLDER_WORD `\b(TBD|TODO|FIXME|XXX)\b`. Avoid.

OK, let's write.

For the ADR-008, CONSTRAINTS requires `docs/adr/*.md` must not contain `<!--`. Fine.

Now let me write everything. Let me start.

One more: the fitness rule `adr-no-placeholders` checks `docs/adr/*.md` for `<!--`. And `abs-credit-only-from-paid` requires ADR-005 contains 'только из состояния `PAID`' — unchanged. Fine.

Let me write the spine edit.

Actually, also consider: should the change-set be a separate spine file in the change workspace (per the skill's "resume from memlog", per-run folder)? The user said "поверх принятого решения" (on top of the accepted decision) and "принятые файлы решения меняй только тем способом, который принят в этом репозитории". The repo's accepted way for spine changes = append Proposed AD blocks + ADR. So editing the canonical spine is right. I'll also place a copy of the change-scoped spine excerpt in the change package? No — duplication risks drift. Instead the change package references the spine section. Good.

Let me write.

Let me now produce the spine edit.
I have enough grounding. Now I'll implement the change package. First, the canonical spine — adding a *Proposed* change-set (the repo's accepted mechanism: new `AD-n` blocks + ADR, never rewriting adopted ones).

  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", old_string="- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.\n\n## Контракты и ве, new_string="- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.\n- **Уведомление пла)`

Now update the Deferred section (add pointer for автоплатежи/подписки + new deferred items) and the "Контракты и версии" section.

Let me edit Deferred: after the Диспуты line, add lines. And add a note about the changed scope.

Current Deferred tail:
```
- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.

## Контракты и версии
```

I'll insert two bullets before the empty line:
- **Уведомление плательщика о предстоящем списании** (если потребуется регулятором/НСПК): интерфейс оповещения — вне шлюза; вернуть при появлении требования.
- **Повторные попытки списания сверх политики ТСП** (dunning): минимально — политика ретраев на стороне ТСП; вернуть при требовании бизнеса.

And add a scope-change note:
- **Автоплатежи/подписки (рекуррентные списания)**: в `docs/solutioning.md` §1 заявлены вне scope (roadmap); изменением CS-001 (ADR-008, Proposed) переводятся в scope при ратификации на решении A6.

Let me do the edit.

  `write_file(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", content="# ADR-008. Подписки СБП: рекуррентные C2B-списания по согласию плательщика\n\n- Date: 2026-09-29\n- Status: Proposed (вынесено на решение A)`

Now write ADR-008. Content in Russian, no `<!--`. Include machine-readable A6 packet.

Let me write it.
Now the ADR — the canonical architectural decision with alternatives, consequences, and reversibility.

  `write_file(content="# Статусные машины подписок СБП — согласие плательщика и рекуррентное списание\n\n- Status: Draft (для ревью на гейте A1)\n- Owner: solutio, file_path="/home/architect/project/docs/spec/consent-state-machine.md")`

Now the consent state machine spec: docs/spec/consent-state-machine.md.

Content: states, transitions (consent + charge), guards, forbidden transitions, idempotency, mapping to payment, reconciliation, API mapping.

Let me write it thoroughly.
Now the consent/charge state machine spec (the A1 artifact for the new entities).

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="# Контракт API ТСП (мерчант-API) — v0.2 draft\n\n- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.2 (аддитивное расширение к , old_string="# Контракт API ТСП (мерчант-API) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фикс)`

Now update the tsp-api contract (docs/contracts/tsp-api.md) additively: bump version header to 0.2-draft, add §8 Подписки (and renumber? currently §6 Версионирование, §7 Открытые вопросы). I'll insert new §"6. Подписки..." before "## 6. Версионирование и совместимость" and renumber the following sections to 7 and 8? Renumbering references... references elsewhere: ADR-008 references "docs/contracts/tsp-api.md §8" for compat and consent-state-machine references "§8 контракта" for API mapping. Hmm, I wrote in ADR-008: "существующие поля... (`docs/contracts/tsp-api.md` §8)". And consent FSM §7 says "Маппинг в API ТСП (§8 контракта)". So I should make the new subscriptions section §6, versioning §7, open questions §8? That conflicts. Let me define:
- §6 Подписки и рекуррентные списания (new)
- §7 Версионирование и совместимость (renamed from 6)
- §8 Открытые вопросы (renamed from 7) — but consent FSM references §8 for API mapping. Hmm.

Simplest: keep original numbering for §1–§5, add §6 "Подписки", then §7 "Версионирование", §8 "Открытые вопросы". Then update my references: consent-state-machine §7 should say "§6 контракта"; ADR-008 compat reference "§7". Alternatively, add the subscriptions section as §6 and shift. I'll fix the two references after writing.

Actually cleaner: put the new subscriptions section as §6, and renumber Версионирование→§7 and Открытые вопросы→§8. Then:
- consent-state-machine §7 title says "Маппинг в API ТСП (§8 контракта)" → change to §6.
- ADR-008 "существующие поля, пути и значения `status` не меняются (ADR-002, `docs/contracts/tsp-api.md` §8)" → that referenced compat section; change to §7.
- Also ADR-008 references "`docs/contracts/tsp-api.md` §8, `openapi/tsp-api.yaml` — контракт v0.2" → §6/§7.

I'll edit those.

Also the header of tsp-api.md: version line says "Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)". I'll update to note v0.2 draft additive.

Let me write the §6 content. It should mirror the tsp-api.md style (JSON examples, tables). Additive, back-compat statement.

Endpoints:
- POST /v1/subscriptions — create consent (ТСП initiates; payer confirms) 
- GET /v1/subscriptions/{subscriptionId}
- POST /v1/subscriptions/{subscriptionId}/charges — charge
- POST /v1/subscriptions/{subscriptionId}/suspend and /resume — optional
- POST /v1/subscriptions/{subscriptionId}/revoke? — hmm: revocation is by payer in bank app; ТСП can "close" subscription. The contract: ТСП may request termination (закрытие подписки со стороны сервиса). I'll add POST /v1/subscriptions/{subscriptionId}/close (закрытие со стороны ТСП). And note payer revoke arrives via webhook.

Fields for SubscriptionRequest:
```
{
  "tspId": "...",
  "amountType": "FIXED" | "VARIABLE",  // variable for ЖКХ
  "maxAmountPerCharge": 50000,
  "periodLimit": 200000,   // monthly
  "period": "MONTH",        // DAY | WEEK | MONTH
  "startDate": "...",
  "endDate": "...",         // опц.
  "paymentPurpose": "...",
  "payerRef": "..."         // опц.; идентификатор плательщика на стороне ТСП (не ПДн)
  "returnUrl": "...",
  "merchantSubscriptionId": "..."
}
```
Response 201: subscriptionId, status PENDING_PAYER, consentUrl/deeplink, limits echo, createdAt.

GET response: subscription with status, limits, period, charges[] summary.

ChargeRequest:
```
{ "chargeId": "chg_...", "billingPeriod": "2026-09", "amount": 49900, "description": "..." }
```
Headers: Idempotency-Key. Response 201: chargeId, paymentId, subscriptionId, billingPeriod, amount, status INITIATED. Or 200 with existing on idempotent repeat.

Also mention Payment response extended with optional `operationType` (QR|CONSENT) and `subscriptionId`.

Webhooks: add events.

Errors: add codes.

Let me write. Also note rate limiting / scheduling: charges are merchant-initiated; recommend batching off-peak; NFR §7.

Let me produce the edit by inserting before "## 6. Версионирование и совместимость" and renumbering.

Let me read the exact text around there to edit precisely (I have it from earlier read). The text:

```
## 6. Версионирование и совместимость

- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.
- Добавление опциональных полей — обратно совместимо, не требует новой версии.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 7. Открытые вопросы (для A1)
```

I'll replace from "## 6. Версионирование" through "## 7. Открытые вопросы (для A1)" heading with new §6 content + "## 7. Версионирование..." + "## 8. Открытые вопросы (для A1)".

Also update header version line. Two edits.

Let me do the header edit first.
Now the TSP API contract — additive v0.2 (no breaking changes for existing consumers).

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="## 6. Подписки и рекуррентные списания (v0.2, аддитивно)\n\nНазначение: ТСП оформляет согласие плательщика на регулярные списания и инициир, old_string="## 6. Версионирование и совместимость\n\n- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6)`

Now insert §6 and renumber §6/§7 → §7/§8, plus extend §5 webhooks and §4 error codes? The webhooks are in §5 and errors in §4. I should add new events and error codes additively within §4 and §5 (or put them in §6). To keep §1–§5 "не изменялись" true, I'd better put new events/codes in §6 rather than editing §4/§5. But that's awkward. Hmm — I claimed §1–§5 unchanged. Better to keep that claim accurate: put all additions in §6. But then the error code list in §4 is incomplete; acceptable if §6 references new codes. Actually cleanest: keep the claim as "новые события и коды перечислены в §6; существующие не менялись". Fine, additions live in §6.

Let me write the insert replacing the "## 6. Версионирование и совместимость" block.

Content:

## 6. Подписки и рекуррентные списания (v0.2, аддитивно)

Назначение: ТСП оформляет согласие плательщика на регулярные списания и инициирует списания по расписанию без QR. Подтверждение/отзыв согласия выполняет плательщик в приложении своего банка (AD-013); шлюз не собирает аутентификационные данные.

### 6.1 Государственная модель...
- Subscription statuses: CREATED, PENDING_PAYER, ACTIVE, SUSPENDED, REVOKED, EXPIRED, DECLINED
- Charge (payment) statuses: INITIATED, PAID, CREDITED, COMPLETED, FAILED

### 6.2 POST /v1/subscriptions (создание согласия)
Request/response JSON.

### 6.3 GET /v1/subscriptions/{subscriptionId}

### 6.4 POST /v1/subscriptions/{subscriptionId}/charges

### 6.5 POST /v1/subscriptions/{subscriptionId}/suspend | /resume | /close

### 6.6 Расширение существующих ответов (аддитивно)
Payment gains optional operationType, subscriptionId.

### 6.7 Вебхуки подписок (новые типы)

### 6.8 Новые коды ошибок

### 6.9 Правила и ограничения

Then §7 версионирование, §8 открытые вопросы (add subscription-related open questions).

Let me write it.

Note: keep JSON blocks. Careful with the tool's literal replacement.

Let me construct old_string exactly:

"## 6. Версионирование и совместимость\n\n- Путь `/v1`; ... \n\n## 7. Открытые вопросы (для A1)"

I'll replace that whole chunk with new content ending in "## 8. Открытые вопросы (для A1)".

And I need to append new open questions inside §8. The §8 list currently has 4 items; I'll add subscription-related ones. To do that within the same edit, I need to include the full §7(open questions) list in old_string. That's fine — I have it.

Let me write the replacement.

  `edit(file_path="/home/architect/project/docs/spec/consent-state-machine.md", old_string="## 7. Маппинг в API ТСП (§8 контракта) и вебхуки", new_string="## 7. Маппинг в API ТСП (§6 контракта) и вебхуки")`
  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", old_string="7. **Контракт API ТСП расширяется обратно совместимо** (v0.2, аддитивно): новые ресурсы подписок и списаний, новые события вебхуков, новые , new_string="7. **Контракт API ТСП расширяется обратно совместимо** (v0.2, аддитивно): новые ресурсы подписок и списаний, новые события вебхуков, новые )`

Now fix the cross-references: consent-state-machine.md §7 says "(§8 контракта)" — should be §6. And ADR-008 references `docs/contracts/tsp-api.md` §8 — should be §6/§7. Let me fix both.

consent-state-machine.md: "## 7. Маппинг в API ТСП (§8 контракта) и вебхуки" → "(§6 контракта)".
ADR-008: 
- "существующие поля, пути и значения `status` не меняются (ADR-002, `docs/contracts/tsp-api.md` §8)" → §7.
- "`docs/contracts/tsp-api.md` §8, `openapi/tsp-api.yaml` — контракт v0.2" → §6–§7.

Let me do those edits.

  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="- `docs/contracts/tsp-api.md` §6–§7, `openapi/tsp-api.yaml` — контракт v0.2", old_string="- `docs/contracts/tsp-api.md` §8, `openapi/tsp-api.yaml` — контракт v0.2")`
  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.2 draft\n\n- Status: Draft (для ревью на гейте A1; основа для RFP вендора)\n- Версия, old_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1; основа для RFP вендора)\n- Owner:)`

Now extend opkc-adapter.md with subscription methods/events (additive), since AD-012 references it. Let me add a section §10 "Подписки и согласия (v0.2, аддитивно)" and update the header. Also update the RFP vendor doc with the new gate criterion (G8 support of subscriptions) — referenced by AD-012. Hmm, this is getting broad. The task asks to prepare a package for architecture decision, not to fully rewrite all contracts. But AD-012 explicitly says "поддержка подписок — gate-критерий RFP". For consistency I should add it to vendor-rfp.md as a Proposed change too. Let me do a minimal, additive edit to both opkc-adapter.md and vendor-rfp.md, marked as CS-001/Proposed.

opkc-adapter.md: update header version to v0.2 draft (additive), add methods in §3 table? Better add a new section §10 to avoid rewriting the table, and add events in §4? To keep it clean and additive, I'll add a §10 "Подписки (v0.2, аддитивно)" listing new sync methods and async events + idempotency requirement, and update the header + related fields.

vendor-rfp.md: add gate criterion G8 (поддержка подписок) and POC scenario P9 (согласие/списание) — additive. Update header.

Let me do these.

opkc-adapter.md header currently:
```
# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.1 draft

- Status: Draft (для ревью на гейте A1; основа для RFP вендора)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-003, ADR-004, AD-004, AD-008
```
I'll update to v0.2 draft with note.

Then append §10 at the end (after §9 Открытые вопросы). Hmm, appending after §9 is fine but numbering; I'll add "## 10. Подписки и согласия (v0.2, аддитивно)" and add open questions to §9? The §9 is "Открытые вопросы". I'll insert §10 before §9? Numbered sections should be ordered. Let me insert §10 after §8 and renumber §9→§10? That changes existing numbering. Simpler: append new section as "## 10. Подписки и согласия (v0.2, аддитивно)" at the end (after §9), acknowledging numbering isn't strictly ordered but it's clearly an addendum. Hmm, that's slightly untidy.

Alternative: insert new section as §9 "Подписки..." and renumber "Открытые вопросы" from §9 to §10, adding new open questions there. That's cleaner and the "§9 Открытые вопросы" references elsewhere? Let me grep for references to opkc-adapter §9 / §3 / §4 in the repo. In vendor-rfp.md: "Методы (§3)", "События (§4)", "Идемпотентность (§5)", "Таймауты (§6)", "NFR (§7)". So §9 isn't referenced. Good — renumber §9→§10 and insert §9 Подписки.

Let me do it.

Then vendor-rfp: add G8 to gate table, P9 to POC table, and note in §4 technical requirements. And header update. Let me implement.

Actually, to limit scope creep: the task's deliverable #4 is contract changes to openapi/tsp-api.yaml (done). The opkc-adapter and RFP are internal-ish; but AD-012 makes claims requiring them. I'll add concise additive sections — worth it for coherence.

Let me write the opkc-adapter edit.

I need to find the anchor: the end of §8 (requirements to vendor) and §9 heading.

From earlier read:
```
## 9. Открытые вопросы

1. Нужен ли синхронный `getReconciliationReport` ...
2. Нормализованные `reasonCode` ...
3. Поведение ядра при `transport.unavailable` ...
```

I'll replace "## 9. Открытые вопросы\n\n1. Нужен ли..." with new §9 + "## 10. Открытые вопросы".

Let me construct carefully.
Extending the ОПКЦ adapter contract and the vendor RFP additively (AD-012 requires both).

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="## 9. Подписки и согласия (v0.2, аддитивно; условие AD-012)\n\nРасширение контракта для рекуррентных списаний. Требуется **только** при при, old_string="## 9. Открытые вопросы")`
  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="3. Поведение ядра при `transport.unavailable` (приём QR в очередь vs отклонение) — политика, утверждается на A2.\n4. Подписки: полный набор, old_string="3. Поведение ядра при `transport.unavailable` (приём QR в очередь vs отклонение) — политика, утверждается на A2.")`
  `edit(file_path="/home/architect/project/docs/rfp/vendor-rfp.md", new_string="- Status: Draft (для A1; запуск после подписания NDA с вендорами)\n- Owner: проектный офис / закупки + solution-architect\n- Связано: ADR-0, old_string="- Status: Draft (для A1; запуск после подписания NDA с вендорами)\n- Owner: проектный офис / закупки + solution-architect\n- Связано: ADR-0)`

Add subscription-specific open questions to §10 (opkc-adapter): maybe append items 4-5. Let me append after item 3:
4. Поддержка подписок вендором: полный набор методов/событий §9 и proof идемпотентности — gate RFP (G8).
5. Формат/наличие выписки по согласиям (`getConsentReconciliationReport`) — решить с вендором.

Let me edit.

Also RFP: add G8 and P9. And maybe update §4 technical requirements with a bullet. Let me do targeted edits.

vendor-rfp header:
```
# RFP: вендор транспортного адаптера ОПКЦ СБП — чек-лист и пакет закупки

- Status: Draft (для A1; запуск после подписания NDA с вендорами)
- Owner: проектный офис / закупки + solution-architect
- Связано: ADR-007 (гибрид), ADR-003, AD-004, AD-008, `docs/contracts/opkc-adapter.md`
```
Add ADR-008/AD-012 and note version 0.2 gate.

Gate table: add row G8.
POC table: add P9.
§4 technical: add bullet for subscriptions (optional? make it required-if-CS-001).
Kill criteria: add "не подтверждена поддержка подписок (G8) — при выборе include-now/transport-first".

Let me implement.

  `edit(file_path="/home/architect/project/docs/rfp/vendor-rfp.md", new_string="| G7 | Передача исходного кода/эскроу на случай прекращения поддержки | Условия эскроу в контракте |\n| G8 | **Поддержка подписок/согласий*, old_string="| G7 | Передача исходного кода/эскроу на случай прекращения поддержки | Условия эскроу в контракте |")`
  `edit(file_path="/home/architect/project/docs/rfp/vendor-rfp.md", new_string="| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |\n| P9 | Подп, old_string="| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |")`

Now add G8 to gate table, P9 to POC, and kill criteria. Let me edit the gate table.

Gate table ends with G7 row:
```
| G7 | Передача исходного кода/эскроу на случай прекращения поддержки | Условия эскроу в контракте |
```
Add G8 after.

POC table ends with P8 row:
```
| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |
```
Add P9, P10.

Kill criteria line:
```
**Kill criteria** (стоп в любой момент): не подтверждён G3 (идемпотентность); POC не проходит P2/P4; вендор не может предоставить тестовый контур; стоимость/сроки вне допустимых пределов бизнес-кейса.
```
Add G8/P9.

Also §4 technical requirements list — add a bullet about §9 подписок.

Let me do these edits.

  `edit(file_path="/home/architect/project/docs/rfp/vendor-rfp.md", new_string="- **NFR** (§7): нагрузка, latency, потеря событий = 0, доступность ≥ 99,95 %, Prometheus-метрики, trace id.\n- **Подписки** (§9, при принят, old_string="- **NFR** (§7): нагрузка, latency, потеря событий = 0, доступность ≥ 99,95 %, Prometheus-метрики, trace id.")`
  `edit(file_path="/home/architect/project/docs/rfp/vendor-rfp.md", new_string="**Kill criteria** (стоп в любой момент): не подтверждён G3 (идемпотентность); POC не проходит P2/P4; вендор не может предоставить тестовый , old_string="**Kill criteria** (стоп в любой момент): не подтверждён G3 (идемпотентность); POC не проходит P2/P4; вендор не может предоставить тестовый )`

Now update §4 technical requirements and kill criteria in vendor-rfp.md.

§4 list ends with:
```
- **NFR** (§7): нагрузка, latency, потеря событий = 0, доступность ≥ 99,95 %, Prometheus-метрики, trace id.
```
Add a bullet for §9 subscriptions.

Kill criteria add.

Let me edit both.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\n  description: >\n    Мерчант-API СБП-шлюза. v0.2 — обратно совместим, file_path="/home/architect/project/openapi/tsp-api.yaml")`

Now the openapi/tsp-api.yaml — additive v0.2.0. Must be valid OpenAPI 3.0.3. Let me rewrite the whole file carefully (it's small), keeping existing paths/schemas verbatim and adding new ones.

Existing:
```yaml
openapi: 3.0.3
info:
  title: СБП-шлюз — API ТСП
  version: 0.1.0
paths:
  /v1/payments:
    post:
      operationId: createPayment
      parameters:
        - in: header
          name: Idempotency-Key
          required: true
          schema: {type: string}
      requestBody:
        required: true
        content:
          application/json:
            schema: {$ref: '#/components/schemas/PaymentRequest'}
      responses:
        '201':
          description: Платёж зарегистрирован
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Payment'}
  /v1/payments/{paymentId}:
    get:
      operationId: getPayment
      parameters:
        - {in: path, name: paymentId, required: true, schema: {type: string}}
      responses:
        '200':
          description: Статус платежа
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Payment'}
components:
  schemas:
    PaymentRequest:
      type: object
      required: [amount, merchantOrderId]
      properties:
        amount: {type: integer, description: Сумма в копейках}
        merchantOrderId: {type: string}
    Payment:
      type: object
      required: [paymentId, amount, status]
      properties:
        paymentId: {type: string}
        amount: {type: integer, description: Сумма в копейках}
        status:
          type: string
          enum: [CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED]
```

New version: 0.2.0.

Add paths:
- /v1/subscriptions (post)
- /v1/subscriptions/{subscriptionId} (get)
- /v1/subscriptions/{subscriptionId}/charges (post)
- /v1/subscriptions/{subscriptionId}/suspend (post)
- /v1/subscriptions/{subscriptionId}/resume (post)
- /v1/subscriptions/{subscriptionId}/close (post)

Add schemas: SubscriptionRequest, Subscription, ChargeRequest, Charge, Problem, and extend Payment with optional operationType/subscriptionId.

To keep it nice, add a `SubscriptionStatus` enum and `ChargeStatus` enum.

Let me write the YAML. Also validate: OpenAPI 3.0.3 requires `info.version` string; fine. Paths with `{}`. Response codes as strings '201' etc.

I'll write the full file with write_file (overwrite). Since I've read it, allowed.

Let me carefully produce valid YAML — consistent 2-space indent. Use block style rather than flow for new parts for readability, but keep existing flow style? Mixing is fine. I'll rewrite in a consistent, more readable block style while preserving semantics — but "не поломка существующих потребителей" refers to the API semantics, not YAML formatting. Changing formatting of existing schema is fine as long as semantics identical. I'll keep existing entries semantically identical.

Let me write.
Now the machine-readable contract (`openapi/tsp-api.yaml`) — additive, backward compatible.

  `run_shell_command(command="cd /home/architect/project && timeout 90 npx --yes js-yaml openapi/tsp-api.yaml > <TMP>.parsed.json 2><TMP>.err && echo \"YAML OK, description="Validate OpenAPI YAML syntax with js-yaml")`

Let me validate the YAML with node (js-yaml may not be installed). Node has no built-in YAML parser. I could do a quick check via `node -e` with a naive check? Better: check if `npx js-yaml` or python is absent. There is no python. `npx js-yaml` would need network install; may fail. Let me try `node -e "require('js-yaml')"` — likely not installed. Alternatively use `npx --yes js-yaml openapi/tsp-api.yaml` — needs network. Let me try; if it fails, I'll note that YAML wasn't machine-validated.

Actually, there's a risk that my YAML is invalid (e.g., `description: >` block, quotes). Let me attempt validation via npx js-yaml. If offline, fallback: write a small Node script using a minimal YAML parse? Not reliable.

Let me try `npx --yes js-yaml` with a short timeout.

Also I could check the repo for existing test/lint tooling (package.json absent). No package.json. So verification = manual.

Let me try npx.

  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        maxAmountPerCharge: {type: integer, description: \"Потолок одного списания, копейки\"}\n        periodLimit: {type: integer, descri, old_string="        maxAmountPerCharge: {type: integer, description: Потолок одного списания, копейки}\n        periodLimit: {type: integer, descriptio)`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        paymentId: {type: string, description: \"Идентификатор платежа (для GET /v1/payments/{paymentId})\"}\n        subscriptionId: {type, old_string="        paymentId: {type: string, description: Идентификатор платежа (для GET /v1/payments/{paymentId})}\n        subscriptionId: {type: st)`

js-yaml is available (npx downloaded it), and there's a YAML parse error at line 231: `paymentId: {type: string, description: Идентификатор платежа (для GET /v1/payments/{paymentId})}`. The issue: flow mapping contains `{paymentId}` inside a value → the `{` starts a new flow mapping? Actually in YAML flow context, `{` inside a plain scalar is not allowed — plain scalars in flow context can't contain `{`, `}`, `[`, `]`, `,`. So the description with `{paymentId}` breaks it. I need to quote it.

Let me see full error. Let me print the head of npx.err. Also fix.

Fix: quote the description: `description: "Идентификатор платежа (для GET /v1/payments/{paymentId})"`. Similarly check other descriptions with braces or commas in flow style — the existing ones don't have braces. My new ones: 
- `consentUrl: {type: string, description: Ссылка/деeplink на подтверждение в приложении банка плательщика}` — no braces/commas, ok.
- `payerRef: {type: string, description: Идентификатор плательщика на стороне ТСП (не ПДн)}` — parentheses fine.
- `chargeId: {type: string, description: Идемпотентный идентификатор попытки}` ok.
- `paymentId: {... {paymentId})}` — broken.
- `amount: {type: integer, description: Копейки; не больше maxAmountPerCharge}` — semicolon in plain scalar is ok in flow? `;` is allowed in plain scalars. Yes.
- operationType description: `Тип операции (v0.2); отсутствие поля трактуется как QR` ok.
- subscriptionId description ok.
- `maxAmountPerCharge: {type: integer, description: Потолок одного списания, копейки}` — contains a comma! In flow mapping, the comma inside a plain scalar terminates the scalar → this breaks too. Similarly `periodLimit: {type: integer, description: Потолок списаний за период, копейки}` has comma. And `billingPeriod: {type: string, description: Ключ периода, уникален в паре с subscriptionId}` has comma.

So I must quote descriptions containing commas or braces. Let me fix all flow-mapping descriptions that contain commas/braces by quoting, or switch those lines to quoted strings.

Let me rewrite those lines:
- maxAmountPerCharge: {type: integer, description: "Потолок одного списания, копейки"}
- periodLimit: {type: integer, description: "Потолок списаний за период, копейки"}
- paymentId: {type: string, description: "Идентификатор платежа (для GET /v1/payments/{paymentId})"}
- billingPeriod: {type: string, description: "Ключ периода, уникален в паре с subscriptionId"}
- amount (ChargeRequest): {type: integer, description: "Копейки; не больше maxAmountPerCharge"} — semicolon is fine but quote for safety.
- Also check `info.description: >` block — fine.
- SubscriptionRequest tspId etc fine.
- Check other flow mappings for commas: 
  - `/v1/payments` post parameters idempotency fine.
  - `PaymentRequest.amount: {type: integer, description: Сумма в копейках}` fine.
  - `Payment.subscriptionId: {type: string, description: Согласие-источник (v0.2); присутствует только при operationType=CONSENT}` — semicolon ok, no comma.
  - `operationType` description has `;` ok.
  - `amountType: {type: string, enum: [FIXED, VARIABLE]}` — the enum flow sequence contains comma but that's structural, fine.
  - `endDate: {type: string, format: date, nullable: true}` structural commas fine.
  - `charges.items: {$ref: ...}` fine.
- Also `'422': description: SUBSCRIPTION_NOT_ACTIVE | SUBSCRIPTION_LIMIT_EXCEEDED | SUBSCRIPTION_EXPIRED` — plain scalar with `|`? In block context after `description:`, a plain scalar cannot start with indicators, but `|` inside is fine? Actually a plain scalar cannot contain `: ` or ` #`. `|` is allowed inside a plain scalar as long as not at start. It's mid-string, so fine. But `description: SUBSCRIPTION_NOT_ACTIVE | ...` — the scalar starts with 'S', so "|" is content. YAML plain scalars may contain "|" — yes, allowed (only "|" as first char indicates block scalar). Should be OK. But to be safe, quote it.
- Similarly `'409': description: CHARGE_ALREADY_EXISTS | CHARGE_CONFLICT` — quote.

Let me also verify the whole file parses after fixes. Let me apply edits.

Let me use targeted edits for the problem lines. Actually simpler: rewrite the whole file? That's large. Let me do targeted edits with replace_all where identical.

Lines to fix:
1. `        maxAmountPerCharge: {type: integer, description: Потолок одного списания, копейки}`
2. `        periodLimit: {type: integer, description: Потолок списаний за период, копейки}`
3. `        paymentId: {type: string, description: Идентификатор платежа (для GET /v1/payments/{paymentId})}`
4. `        billingPeriod: {type: string, description: Ключ периода, уникален в паре с subscriptionId}`
5. `        amount: {type: integer, description: Копейки; не больше maxAmountPerCharge}`
6. `        '409':\n          description: CHARGE_ALREADY_EXISTS | CHARGE_CONFLICT`
7. `        '422':\n          description: SUBSCRIPTION_NOT_ACTIVE | SUBSCRIPTION_LIMIT_EXCEEDED | SUBSCRIPTION_EXPIRED`

Note there are two `CONSENT`... no.

Wait: ChargeRequest.amount has `{type: integer, description: Копейки; не больше maxAmountPerCharge}` → semicolon ok, but there's also PaymentRequest.amount `{type: integer, description: Сумма в копейках}`. Distinct strings, fine.

Let me apply edits.
YAML validation caught two flow-mapping issues (unquoted commas/braces in descriptions). Fixing them.

  `read_file(file_path="/home/architect/project/openapi/tsp-api.yaml", offset=195, limit=56)`

The second edit failed because the indentation/context differs — the ChargeRequest/Charge lines. Let me read the relevant part of the file to get exact text.

  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="      properties:\n        chargeId: {type: string, description: Идемпотентный идентификатор попытки}\n        billingPeriod: {type: string, old_string="      properties:\n        chargeId: {type: string, description: Идемпотентный идентификатор попытки}\n        billingPeriod: {type: string)`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        paymentId: {type: string, description: \"Идентификатор платежа (для GET /v1/payments/{paymentId})\"}", old_string="        paymentId: {type: string, description: Идентификатор платежа (для GET /v1/payments/{paymentId})}")`

Now edit the specific lines.

1. `        billingPeriod: {type: string, description: Ключ периода, уникален в паре с subscriptionId}` (ChargeRequest)
2. `        amount: {type: integer, description: Копейки; не больше maxAmountPerCharge}`
3. `        paymentId: {type: string, description: Идентификатор платежа (для GET /v1/payments/{paymentId})}`
4. `        consentUrl: {type: string, description: Ссылка/деeplink на подтверждение в приложении банка плательщика}` — no comma/brace, but keep.
5. `description: RFC 9457 Problem Details` — fine.
6. `chargeId: {type: string, description: Идемпотентный идентификатор попытки}` fine.

Also the response description lines with `|`. Let me quote them too.

Let me do edits with unique context.

  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        '409':\n          description: \"CHARGE_ALREADY_EXISTS | CHARGE_CONFLICT\"\n          content:\n            application/json:\n    , old_string="        '409':\n          description: CHARGE_ALREADY_EXISTS | CHARGE_CONFLICT\n          content:\n            application/json:\n        )`

Also quote the response descriptions with `|` to be safe. Let me edit those two.

`        '409':\n          description: CHARGE_ALREADY_EXISTS | CHARGE_CONFLICT`
`        '422':\n          description: SUBSCRIPTION_NOT_ACTIVE | SUBSCRIPTION_LIMIT_EXCEEDED | SUBSCRIPTION_EXPIRED`

Also `/v1/subscriptions` POST '409': `description: IDEMPOTENCY_CONFLICT` fine.

Let me edit.

Also check the `info.description: >` block scalar — content lines are indented 4 spaces, fine.

Then re-run js-yaml validation.

  `run_shell_command(command="cd /home/architect/project && timeout 120 npx --yes js-yaml openapi/tsp-api.yaml > <TMP>.parsed.json 2><TMP>.err && node -e \"con, description="Re-validate OpenAPI YAML and inspect structure")`
  `run_shell_command(command="cd /home/architect/project && git show HEAD:openapi/tsp-api.yaml > <TMP>.old.yaml && npx --yes js-yaml <TMP>.old.yaml > /tmp/, description="Diff old vs new OpenAPI for backward compatibility")`

YAML valid. Let me also do a structural check that existing v0.1 paths/schemas are unchanged (backward compat): compare against git HEAD version. Since the repo is clean at HEAD, I can `git show HEAD:openapi/tsp-api.yaml` and diff semantically via node. Let me do a programmatic compat check: parse HEAD version and new version, assert existing paths and Payment.status enum unchanged, and that PaymentRequest required unchanged.

Let me write a quick node script inline.

Also verify that the only changes to Payment are additive optional properties.

Let me run.
Let me verify backward compatibility mechanically against the committed v0.1 contract.

  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="paths:", old_string="tags:\n  - name: payments\n    description: C2B-приём по QR/ссылке\n  - name: subscriptions\n    description: Подписки СБП — согласие плате)`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="", old_string="      tags: [payments]\n")`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="", old_string="      tags: [subscriptions]\n")`

The "operation changed" failures are because I added `tags: [payments]` to the existing operations. That's a metadata addition, not a breaking change, but my strict diff flags it. Is adding `tags` a consumer-visible change? OpenAPI tags are documentation metadata; they don't affect request/response contracts. But to be strictly minimal and honor "§1–§5 не изменялись" / "существующие пути... не изменяются", I should remove the `tags` from the two existing payment operations. Let me remove the tags arrays I added to /v1/payments post and /v1/payments/{paymentId} get. But then the new subscription ops also have tags — I could just drop tags entirely from the file to keep the diff purely additive. Simplest: remove `tags:` lines from all operations and the top-level `tags:` block. That keeps the old ops byte-identical-ish and new ops additive.

Actually, do I even need tags? No. Remove them all for cleanliness and to keep old operations unchanged.

Let me edit:
- remove top-level `tags:` block
- remove `      tags: [payments]` (x2)
- remove `      tags: [subscriptions]` (x6)

Let me count: subscriptions ops: createSubscription, getSubscription, createCharge, suspendSubscription, resumeSubscription, closeSubscription = 6.

Let me do replace_all edits:
1. Remove the top-level tags block:
```
tags:
  - name: payments
    description: C2B-приём по QR/ссылке
  - name: subscriptions
    description: Подписки СБП — согласие плательщика и рекуррентные списания
```
2. replace_all `      tags: [payments]\n` → `` (but edit tool needs exact strings; replacing a line with empty would leave blank line). I'll replace `      tags: [payments]\n      ` with `      ` — hmm tricky.

Better: do a node/sed-like edit? I should use the edit tool. Let me handle each occurrence with surrounding context, or use replace_all on `      tags: [payments]\n` -> `` which leaves the following line. The edit tool replaces literal text; if old_string is "      tags: [payments]\n" and new_string "" then the line is removed cleanly. But is old_string unique? With replace_all:true it replaces all occurrences of "[payments]" (2). Good.

Similarly `      tags: [subscriptions]\n` → "" with replace_all.

But wait — the operations have `tags: [...]` on its own line right after `operationId:`:
```
      operationId: createPayment
      tags: [payments]
      parameters:
```
So removing "      tags: [payments]\n" yields:
```
      operationId: createPayment
      parameters:
```
Good.

For the top-level block, remove entirely:
```
tags:
  - name: payments
    description: C2B-приём по QR/ссылке
  - name: subscriptions
    description: Подписки СБП — согласие плательщика и рекуррентные списания
paths:
```
→ `paths:`

Let me do it.
The only "changes" were documentation `tags` I added. Removing them so existing operations stay byte-identical.

  `run_shell_command(command="cd /home/architect/project && timeout 120 npx --yes js-yaml openapi/tsp-api.yaml > <TMP>.parsed.json 2><TMP>.err && node -e \"\nc, description="Re-run backward-compat diff")`
  `edit(file_path="/home/architect/project/docs/nfr.md", new_string="## 7. Подписки СБП (изменение CS-001, ADR-008)\n\nЦели — для рекуррентных списаний и согласий плательщика. Проверяются на мок-адаптере ОПКЦ, old_string="## Зависимости (внешние входы для NFR)")`

Backward compat verified mechanically. Now add NFR §7 to docs/nfr.md.

Current tail:
```
## 6. Наблюдаемость
...
## Зависимости (внешние входы для NFR)
- Регламенты НСПК: ...
- SLA АБС ...
- Требования ЦБ ...
```

Insert §7 before "## Зависимости". Content: measurable NFR for subscriptions. Must include '99,95' somewhere (already present). Add rows plus dependencies.

Metrics:
- Latency создания согласия (POST /v1/subscriptions, без НСПК) p95 < 500 мс
- Время до ACTIVE после подтверждения плательщиком p95 < 5 с (от события НСПК)
- Latency инициации списания (POST charges, до ответа адаптера) p95 < 500 мс
- Завершение списания (INITIATED→PAID) p95 < 30 с (регламент НСПК [ТРЕБУЕТ ПРОВЕРКИ])
- Зачисление по списанию p95 < 60 с (как существующее)
- Распространение отзыва согласия (событие НСПК→блокировка списаний) ≤ 5 с, p99 ≤ 60 с
- Двойное списание за период — 0
- Сверка согласий — ежечасная; расхождений по ACTIVE/REVOKED — 0
- Throughput: sustained 300 TPS, пик 1000 TPS на 5 мин (биллинговые даты); масштабирование ×2
- Доступность — ≥ 99,95 % (та же)
- Доля успешных списаний (бизнес-метрика, не SLO шлюза): baseline ≥ 92 % (отказы = нет средств/лимит банка); уточнить с бизнесом
- Нотификации подписок p95 < 5 с (как существующее)
- Алерт: consent reconciliation расхождение > 0 → ≤ 5 мин
- Запас по лимитам: guard-проверка не добавляет более 50 мс

Dependencies: NSPK регламент сроков/лимитов, СБП лaw, АБС SLA.

Let me write.

Also note: the NFR should be "выполнимыми на моках" for walking skeleton per TASK, but that's for the base. I'll include method of verification.

Let me insert.
Now the measurable NFRs for the new functionality.

  `edit(file_path="/home/architect/project/docs/nfr.md", new_string="- Требования ЦБ к защите информации при переводах (номер Положения — уточнить у ИБ) [ТРЕБУЕТ ПРОВЕРКИ].\n- Подписки: ограничения согласия в, old_string="- Требования ЦБ к защите информации при переводах (номер Положения — уточнить у ИБ) [ТРЕБУЕТ ПРОВЕРКИ].")`

Now update the dependencies section to add subscription-specific external inputs, and set the NFR status note. Let me add bullets to the dependencies list.

Current dependencies:
```
- Регламенты НСПК: таймауты, сроки уведомлений, требования к доступности [ТРЕБУЕТ ПРОВЕРКИ — из документации НСПК].
- SLA АБС на зачисление и списание (согласуется с владельцем АБС).
- Требования ЦБ к защите информации при переводах (номер Положения — уточнить у ИБ) [ТРЕБУЕТ ПРОВЕРКИ].
```
Add:
- Подписки: ограничения согласия в протоколе НСПК (период, срок, лимиты, требования к уведомлению плательщика) [ТРЕБУЕТ ПРОВЕРКИ].
- Подписки: требования ЗоЗПП к явному согласию и упрощённому отказу (юристы банка).

Let me edit.

  `write_file(content="# Архитектурный пакет изменения CS-001 — Подписки СБП (рекуррентные C2B-списания по согласию плательщика)\n\n- Status: Draft — выносится на, file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md")`

Now the main change package: docs/change/c2b-subscriptions/CHANGE-PACKAGE.md. This answers points 1,2,6,7 (+ summarizes 3,4,5).

Let me design the content carefully.

# Архитектурный пакет изменения CS-001 — Подписки СБП (рекуррентные C2B-списания по согласию плательщика)

- Status: Draft → на архитектурное решение (A6), гейт до передачи исполнителям
- Дата, owner, связи
- Краткое резюме (TL;DR)

## 0. Что меняется и зачем (кратко)

## 1. Оценка значимости изменения и маршрута
- Таблица оценки по измерениям (вес, балл, обоснование): внешняя интеграция/протокол; финансовое влияние; регуляторика/ПДн/юридическая значимость; новый функционал/сложность ядра; необратимость/откат; неопределённость внешних входов.
- Итог: балл X/15 (>= Critical порог). Сравнение с исходным 11/15.
- Вывод: требуется глубокое проектирование: новый ADR + новый раздел NFR + статусная машина + контракты + RFP; маршрут: A1(спека) → A6(человеческое решение) → A2(план) → A4 → A5.
- Почему не «просто расширить API»: три независимых источника необратимости/риска (RFP вендора, юридическая значимость согласия, второй объект сверки).

Score dimensions: use 5 dimensions × 0-3 = 15, similar to original 11/15. Let me define:
1. Внешняя интеграция/протокол — 3 (новый сервис НСПК, новые методы/события, испытания)
2. Финансовое влияние/риск — 3 (регулярные автоматические списания, двойное списание, права плательщика)
3. Регуляторика/юридическая значимость/ПДн — 3 (ЗоЗПП, доказательство согласия, ПДн)
4. Изменение ядра/новые сущности — 2 (новые сущности и тип операции, но переиспользуется финансовый путь)
5. Необратимость/откат/внешние входы — 3 (RFP вендора + протокол НСПК + действующие согласия плательщиков)
Total 14/15. Original was 11/15. Explain.

Hmm, but is 14/15 credibly justifiable? Weights: original used "значимость 11/15". I don't know the original rubric exactly; I'll present my own rubric transparently and note it's an assessment, not the original rubric (which isn't in the repo). Actually I should be careful: the original 11/15 rubric isn't documented in the repo. I'll state my scoring basis explicitly and mark that the original rubric is unknown/[ASSUMPTION]. Better: present dimension-based reasoning and conclude "не ниже исходного Critical (11/15); оцениваю 13–14/15" — mark as оценка архитектора.

## 2. Влияние на принятую архитектуру
- Таблица: инвариант | затронут? | как
  - AD-001 изоляция — затронут слабо: новые операции идут через те же адаптеры; расширяется контракт адаптера ОПКЦ; вывод: без изменения.
  - AD-002 единый источник истины — затронут: появляется второй (согласие) и третий (списание как платёж) объект состояния; распространяем правило атомарности и сверки на согласие → AD-009.
  - AD-003 идемпотентность — затронут: новые ключи (chargeId, billingPeriod); правило сохраняется → AD-011.
  - AD-004 единый адаптер — затронут: новые методы/события внутри того же адаптера → AD-012.
  - AD-005 зачисление из PAID — затронут формально: тип CONSENT имеет свой вход в PAID; правило не ослабляется → AD-010.
  - AD-006 trust-зоны — затронут: соблазн добавить публичную поверхность согласия; решение — не расширять → AD-013.
  - AD-007 НПС/КИИ/ПДн — затронут: юридическая значимость согласия, доказательства, ПДн; требования усиливаются, новых зон нет.
  - AD-008 гибрид [ADOPTED] — затронут: RFP-контракт расширяется (поддержка подписок — gate); важно сделать до подписания контракта.
- Что НЕ меняется: финансовая модель зачисления, адаптер как единственная точка протокола, outbox/идемпотентность/сверка как паттерны, статусы платежа, trust-зоны, стратегия гибрида.
- Затронутые файлы решения: spine (+AD-009..013, Deferred), solutioning (scope), tsp-api, opkc-adapter, nfr, vendor-rfp.
- Конфликты/расхождения с принятыми решениями: none блокирующих; явное изменение scope: автоплатежи были вне scope (solutioning §1) → переводятся в scope условно (требует A6). Один риск ослабления AD-008: если вендор/контракт подписан без подписок → нужно действие до подписания.

## 3. Архитектурное решение (ADR-008) — резюме
- Ссылка на ADR-008; краткая таблица решения (7-8 пунктов); таблица альтернатив с выбором и почему; последствия (+/-); обратимость costly с объяснением.
- Т.к. пункт 3 требует "рассмотренные альтернативы, последствия и обратимость" — включу сжатое изложение, чтобы пакет был самодостаточен, а ADR — канонический источник.

## 4. Изменения контрактов (без поломки потребителей)
- Принцип: только аддитивные изменения; путь /v1; перечисление status платежа не расширяется; новые сущности.
- Таблица: что добавлено (paths, schemas, events, errors, optional fields), обратная совместимость, как проверено (машинная проверка diff v0.1→v0.2: no removals/changed ops/required/enums).
- Миграция потребителей: не требуется; опциональные поля; новые события игнорируются старыми потребителями (ТСП, не подписанные на подписки, просто не вызывают новые методы).
- Риск: ТСП, строго валидирующие enum, не затрагиваются, т.к. Payment.status не меняется.
- Файлы: docs/contracts/tsp-api.md §6-7, openapi/tsp-api.yaml, opkc-adapter.md §9.

## 5. NFR (измеримые)
- Резюме ключевых целей + ссылка на docs/nfr.md §7. Include the table compactly.

## 6. Критерии приёмки и план отката
### 6.1 Критерии приёмки (проверяемые)
Positive + negative scenarios, each testable:
- AC-01 Согласие: создание → PENDING_PAYER → подтверждение → ACTIVE (мок НСПК).
- AC-02 Списание: ACTIVE + в лимитах → INITIATED → PAID → CREDITED → COMPLETED; зачисление по PAID.
- AC-03 (негативный) Списание при не-ACTIVE → 422 SUBSCRIPTION_NOT_ACTIVE, вызова ОПКЦ нет (fitness AD-009).
- AC-04 (негативный) Повтор списания с тем же billingPeriod → одно списание, одна проводка (AD-011); 200/existing или 409 CHARGE_ALREADY_EXISTS.
- AC-05 (негативный) Гонка scheduler+manual → одна успешная попытка.
- AC-06 (негативный) Отзыв согласия во время списания → новые списания блокируются; распространение ≤ 5 с; уже зачисленные не откатываются.
- AC-07 (негативный) Зачисление невозможно из INITIATED (fitness AD-005/AD-010).
- AC-08 Сверка: «у НСПК REVOKED, у нас ACTIVE» → авто-переход, алерт.
- AC-09 Отказ АБС: списание остаётся PAID, сверка, нет двойной проводки.
- AC-10 Контракт: v0.1-потребитель работает без изменений (regression на существующих путях).
- AC-11 NFR: latency/throughput/revocation propagation в целях §7.
- AC-12 (негативный) Вендор без поддержки подписок → gate G8 не пройден, решение не стартует (RFP).
- Критерий отката: stop-new → нет новых согласий/периодов; действующие согласия обрабатываются; ошибок двойного списания 0.

### 6.2 План отката
- Триггеры (сигналы отката): двойные списания > 0; доля расхождений согласий > порога; распространение отзыва > SLA; вендор не подтверждает G8; юридическое заключение против.
- Владелец решения: человек-архитектор + владелец продукта (A6); исполнение — DevOps/дежурная смена.
- До боевой: откат = не включать; все работы обратимы.
- После боевой: fase 1 feature-flag (stop-new), fase 2 wind-down действующих согласий (нельзя оборвать), fase 3 сохранение возвратов и сверки; данные не мигрируют обратно.
- Обратимость согласована с ADR-008 (costly).

## 7. Что остаётся на решение человека-архитектора
Таблица: вопрос | почему нельзя решить внизу | рекомендация | дедлайн/триггер
1. Фазирование (A6: include-now/transport-first/defer) — влияет на RFP и критический путь; рек. transport-first.
2. Владение согласием (шлюз vs ОПКЦ) — влияет на источник истины, аудит, сверку; рек. реестр в шлюзе (ADR-008 alt A).
3. Числовые лимиты/периоды/срок согласия — зависят от НСПК и бизнес-модели; рек. до A1 после документации.
4. Бизнес-модель отказов (dunning): кто несёт риск неоплаты, политика ретраев — бизнес.
5. Юридическая модель доказательства согласия и хранение (срок, состав) — юристы/ИБ + 152-ФЗ.
6. Уведомление плательщика о списании (кто и как) — если НСПК/регулятор требует; влияет на ТСП-контракт.
7. Требования к вендору (G8/P9/P10) и kill criteria — закупки + архитектор; сделать до подписания.
8. Возвраты/диспуты по подпискам и ошибочные списания — влияет на сагу и поддержку (диспуты deferred).
9. Комиссии/тарифы подписок — бизнес (влияет на отчётность).
10. Объём первой волны: FIXED vs VARIABLE (ЖКХ) — покрытие НСПК, UX.

Also "Почему именно эти" — criterion: необратимость, внешние входы, юридическая/финансовая ответственность.

## 8. Внешние входы и передача исполнителям
- Gaps table (обновление solutioning §9): протокол согласий НСПК; лимиты; требования уведомления; юрзаключение; вендор.
- Что будет в handoff после A6: TASK для кодового харнесса (расширение walking skeleton: мок-адаптер согласий, FSM согласия, guard, идемпотентность периода, вебхуки), обновление CONSTRAINTS/RUBRIC.

## 9. Открытые вопросы / допущения

I'll include assumptions list and open questions (headless requirement).

This is a lot. Let me write it, keeping it structured and dense but readable.

Also, I must be careful not to overclaim: e.g., "требования НСПК" — mark [ТРЕБУЕТ ПРОВЕРКИ].

Let me write the file.

Also need the memlog. I'll write it after.

Let me write CHANGE-PACKAGE.md now.
Now the main change package document (the 7 deliverables).

  `run_shell_command(command="date -u +\"%Y-%m-%dT%H:%MZ\"", description="Get current UTC timestamp")`

Now the memlog. Since memlog.py can't run, I'll write it manually in the exact format the script produces: frontmatter with fields (topic/goal/updated) and lines "- (type) text". The script's init creates frontmatter with given fields; append adds lines.

Format from docstring:
```
---
topic: ...
goal: ...
updated: 2026-06-07T14:22
---

- (note) ...
- (decision) ...
```

The skill uses `--type <decision|constraint|version|assumption|question|direction|event>`.

I'll create docs/change/c2b-subscriptions/.memlog.md with frontmatter and entries in chronological order reflecting the run.

Then a reviews/ folder with reviewer outputs (from subagents) — I'll dispatch subagents now.

But first, let me run the manual lint checks equivalent on the spine (grep for TODO/TBD/XXX, duplicate/non-monotonic AD ids, missing binds/prevents/rule, `{token}`), and the CONSTRAINTS fitness checks. Then dispatch reviewers.

Actually order: create memlog now, then lint checks, then reviewer subagents (which will also review), then apply fixes and finalize.

Let me write memlog.

Entries:
- (event) run started: update intent, feature altitude, headless (inputs pre-supplied)
- (constraint) inherited AD-001…AD-008 read-only
- (decision) consent as first-class entity → AD-009
- (decision) charge = payment type CONSENT → AD-010
- (decision) idempotency by period → AD-011
- (decision) single ОПКЦ adapter + RFP gate → AD-012
- (decision) payer consent surface outside gateway → AD-013
- (decision) A6 recommendation transport-first
- (assumption) no python3/uv → memlog/lint manual
- (version) verified: НСПК «Подписка СБП» page, ЗоЗПП amendments 2025-09-01, CBR connection order
- (decision) contract v0.2 additive only
- (question) NSPK consent service availability/limits
- (event) artifacts written
- (event) reviewer gate dispatched
- (event) spine finalized (Proposed)

Let me write it.

updated timestamp: 2026-09-29T?? — I'll use a plausible time, but do I know current time? Not exactly. I'll use date only in `updated`? The script uses datetime. I'll put "2026-09-29T12:00". Minor.

Actually, let me get the real date/time from the system to be accurate.

Let me run `date -u`.

  `write_file(content="---\ntopic: CS-001 СБП-подписки — рекуррентные C2B-списания по согласию плательщика (обновление spine платёжного шлюза)\ngoal: подготовить , file_path="/home/architect/project/docs/change/c2b-subscriptions/.memlog.md")`
  `write_file(content="// Faithful replica of _bmad/skills .../bmad-architecture/scripts/lint_spine.py\n// (python3/uv unavailable in this environment). Same rege, file_path="<TMP>.js")`

Now the reviewer gate. Per the skill: run lint_spine.py equivalent (manual) + dispatch parallel subagents writing to {doc_workspace}/reviews/review-{slug}.md returning compact summaries.

Let me first do the manual lint checks (equivalent to lint_spine.py) on ARCHITECTURE-SPINE.md:
1. placeholders: TBD|TODO|FIXME|XXX, "similar to AD-n", `{lowercase tokens}`
2. ad_id: duplicates/non-monotonic
3. ad_fields: each AD block missing binds/prevents/rule
4. version_pin: `## Stack` table rows — no Stack section.

Also CONSTRAINTS fitness rules:
- docs/adr/ADR-001-outbox.md exists ✓ (adr-set-complete)
- spine-present ✓
- nfr contains '99,95' ✓
- ADR-005 contains 'только из состояния `PAID`' ✓ (unchanged)
- docs/adr/*.md must not contain '<!--' — check my ADR-008 and others.
- README.md exists ✓
- spine must not contain TODO|TBD|XXX ✓

Let me run a node-based replica of lint_spine.py (fenced-code blanking etc.) to be faithful. Actually a simpler node script implementing the same regexes is feasible and more faithful than grep. Let me write a temporary node script in .qwen/tmp/ and run it.

Wait — writing to .qwen/tmp is fine (intermediate). Let me do that. Actually I can write <TMP>.mjs (outside workspace) — but shell writes outside workspace... it's /tmp, allowed by run_shell_command? I'll just use node -e with a script. It's long; better write a file to /tmp via write_file? write_file requires absolute path; /tmp is fine. But write_file may register artifacts; /tmp not in workspace → probably fine. Let me just use node -e with a heredoc-ish single-quoted script. It's long but manageable.

Alternatively: since the linter's semantics are simple, I'll do it in a node -e.

Let me write the replica:

```js
const fs=require('fs');
const SPINE='ARCHITECTURE-SPINE.md';
let text=fs.readFileSync('/home/architect/project/'+SPINE,'utf8');
// split frontmatter
let lines=text.split('\n'); let fm='',body=text,offset=0;
if(lines[0]==='---'){for(let i=1;i<lines.length;i++){if(lines[i]==='---'){fm=lines.slice(1,i).join('\n');body=lines.slice(i+1).join('\n');offset=i+1;break;}}}
const blankFences=s=>s.replace(/```[\s\S]*?```/g,m=>'\n'.repeat((m.match(/\n/g)||[]).length));
const findings=[];
const lineOf=(t,i)=>t.slice(0,i).split('\n').length;
const scan=blankFences(body);
for(const [rx,label,sev] of [[/\b(TBD|TODO|FIXME|XXX)\b/g,'placeholder marker','high'],[/similar to AD-\d+/gi,'unresolved cross-reference','high'],[/\{[a-z_][a-z0-9_ /.-]*\}/g,'possible unfilled template token','low']]){
  let m; while((m=rx.exec(scan))) findings.push([sev,label+': '+m[0],'line '+(offset+lineOf(scan,m.index))]);
}
// AD ids
const AD={};
const ADH=/^#{2,4}\s*AD-(\d+)\b(.*)$/gm;
let matches=[],prev=null;
while((m=ADH.exec(scan))) matches.push(m);
...
```

Let me just do it. I'll write the script to /tmp via write_file then run node.

Actually simpler: use `node --input-type=module -e`? -e is CommonJS by default; require works with fs. Fine.

Let me write <TMP>.js.

Then dispatch reviewers. Then apply fixes, then report.

Let me create the script.
Now the reviewer gate. First the deterministic lint (replicating `lint_spine.py`, since `python3`/`uv` are unavailable), then the configured reviewer lenses.

  `edit(file_path="<TMP>.js", new_string="for (const m of rxAll(/^(TBD|TODO|FIXME|XXX)\\b/gm)) findings.push({ category: 'placeholder', severity: 'high', detail: `frontmatter placeh, old_string="for (const m of rxAll(/\\{[a-z_][a-z0-9_ /.-]*\\}/g)) findings.push({ category: 'placeholder', severity: 'low', detail: 'frontmatter check )`

Wait, my script has a bug: I added a spurious loop that pushes frontmatter findings incorrectly (a leftover). Let me fix: remove that line:

```js
for (const m of rxAll(/\{[a-z_][a-z0-9_ /.-]*\}/g)) findings.push({ category: 'placeholder', severity: 'low', detail: 'frontmatter check n/a', location: 'frontmatter' });
```

This duplicates placeholder findings. Let me remove it and instead do a proper frontmatter check. Let me rewrite that portion: check `fm` for placeholder word and template token.

Let me just edit the file.

Also note: the CONSTRAINTS rule `spine-lints-clean` = spine must not contain TODO|TBD|XXX (warn). And the "possible unfilled template token" low-severity will flag things like `{type: string}`? No — that regex is `\{[a-z_][a-z0-9_ /.-]*\}` — `{type: string}` matches! In the spine, do we have `{...}`? We have `{subscriptionId}`, `{id}`? In the spine AD-011 I wrote `POST /v1/subscriptions/{subscriptionId}/charges` → matches `{subscriptionId}` → low finding. Also in the "Пакет изменения" line: `docs/adr/ADR-008-...md` no braces. Any others? `docs/contracts/tsp-api.md` no. So one low finding for `{subscriptionId}` and maybe `{id}`? I wrote `{subscriptionId}` only in AD-011. Also NFR is not the spine. So expect 1 low finding. That's acceptable (low = "possible", verify). I'll note it as acknowledged (API path placeholder, not a template token).

Let me fix the script and run.

  `edit(file_path="<TMP>.js", new_string="const fmAll = (s, rx) => { const out = []; let m; const r = new RegExp(rx.source, rx.flags); while ((m = r.exec(s))) out.push(m); return ou, old_string="for (const m of rxAll(/^(TBD|TODO|FIXME|XXX)\\b/gm)) findings.push({ category: 'placeholder', severity: 'high', detail: `frontmatter placeh)`

The frontmatter token check uses `scan` which is body-only — bug (should be `fm`). Minor; frontmatter has no braces anyway. Let me not fuss; but it would produce false low findings from body braces a second time? No: `rxAll` uses `scan` but with `/g` and no `m` flag; `^(TBD...)` with m flag... I used `rxAll` which re-creates with same flags. The body has no TBD. The token regex over `scan` will duplicate the body `{subscriptionId}` finding. That's a duplicate, cosmetic. Let me just fix to use `fm` by adding a guarded helper. Simpler: replace `rxAll(...)` with inline regex on `fm`.

Let me fix properly: 

```js
const fmScan = fm;
for (const m of fmScan.matchAll(/(TBD|TODO|FIXME|XXX)\b/g)) ... 
```
Hmm matchAll needs g. Let me edit to use a small helper on a string.

Let me rewrite those two lines.

  `run_shell_command(command="cd /home/architect/project && node <TMP>.js \"$PWD\" | head -60; echo \"=== CONSTRAINTS fitness checks ===\"; grep -q '99, description="Run spine lint replica and handoff fitness checks")`
  `agent(description="Spine rubric walker review", subagent_type="general-purpose", run_in_background=false)`
  `agent(description="Tech verification review", subagent_type="general-purpose", run_in_background=false)`
  `agent(description="Adversarial divergence review", subagent_type="general-purpose", run_in_background=false)`
  `agent(description="Security compliance review", subagent_type="general-purpose", run_in_background=false)`
  `agent(description="Contract compatibility review", subagent_type="general-purpose", run_in_background=false)`

Interesting: lint found 0 findings even though I expected `{subscriptionId}` in AD-011. Why? Because the fence-blanking... no. Let me check: AD-011 Rule text: "`POST /v1/subscriptions/{subscriptionId}/charges`". The regex `\{[a-z_][a-z0-9_ /.-]*\}` — `{subscriptionId}` contains uppercase 'I'! `subscriptionId` has capital I → `[a-z0-9_ /.-]*` doesn't allow uppercase. So no match. That's exactly why the linter says "possible" — fine. 0 findings.

Great: lint clean, all fitness checks pass.

Now dispatch the reviewer gate subagents in parallel (foreground inline). Per skill:
- rubric walker (good-spine checklist)
- finalize_reviewers[0]: tech-verification lens
- finalize_reviewers[1]: adversarial lens
- ad-hoc: security/compliance lens (regulated stakes)
- ad-hoc: contract backward-compat lens

They must write to docs/change/c2b-subscriptions/reviews/review-{slug}.md and return compact summary (verdict, top 2-5 findings, path).

Concern: subagents writing files — 5 agents, disjoint files, fine. They need clear prompts with absolute paths and the review criteria. They should not modify the deliverable, only write their review file.

Let me craft prompts. Use subagent_type "general-purpose". Run in foreground (run_in_background: false) so I get results inline. Multiple in one message → concurrent. Actually with foreground and multiple blocks in one message, they should run in parallel and each return. Let me do that.

Potential issue: foreground agents return results inline — good.

Let me write the prompts concisely but with enough context. They can read files themselves.

Common context to include: repo root /home/architect/project; the change is CS-001 (recurring C2B debit by payer consent / СБП subscriptions) on top of accepted spine AD-001..AD-008; artifacts list; their lens; output file path; return compact summary.

Reviewer 1 (rubric walker): judge ARCHITECTURE-SPINE.md (esp. new CS-001 section AD-009..AD-013) against the good-spine checklist: fixes real divergence points for the level below; each Rule enforceable and prevents its stated divergence; nothing under Deferred could let two units diverge; named tech verified-current; ratifies brownfield conventions; inherited parent spine not weakened by new AD; every dimension the altitude owns is decided/deferred/open (operational envelope). Report findings tiered.

Reviewer 2 (tech-verification): verify every committed decision was reality-checked rather than asserted: does НСПК «Подписка СБП» / agreements mechanism exist for C2B acquiring (vs only for payer-bank-initiated subscriptions)? Are the cited URLs live and do they say what the ADR claims? Are the claims about ЗоЗПП amendments correct (which law, effective date)? Is "monthly limits in bank app" accurate? Flag anything out of date or misattributed. Use web_fetch. Note: no web_search tool; web_fetch only. They can fetch the cited URLs and check.

Reviewer 3 (adversarial): construct two units one level down that each obey every AD to the letter yet still build incompatibly — e.g., consent vs payment state ownership, reconciliation of consent revocation races, scheduler vs API charge race, limits accounting (period limit computed by whom, currency of period), notification event ordering, TSP API idempotency vs charge idempotency. Every pair is a hole to close with new/tightened AD.

Reviewer 4 (security/compliance): regulated stakes lens — consent as legally significant record, ПДн minimization, proof of consent, revocation, audit, trust zones, mTLS/СКЗИ, whether AD-013 is sufficient, whether payer notification requirement creates a gap, whether storing payerRef is ПДн.

Reviewer 5 (contract-compat): verify tsp-api v0.2 and openapi are truly backward compatible and internally consistent with the consent FSM and AD-009..AD-013. Check for contradictions: status naming (INITIATED vs payment statuses), the claim "Payment.status enum unchanged", idempotency semantics, error codes, the `INITIATED` status not in Payment.status enum (it's on Charge — but charge IS a payment... consistency question!). Hmm — good catch to have them find: charge status enum includes INITIATED but Payment.status enum doesn't; yet charge is modeled as payment. That's a real inconsistency I should address (maybe map: charge INITIATED ↔ payment CREATED internally? or add INITIATED only as charge-level status). Let the reviewer find it, then I fix.

Let me dispatch. I'll include instructions to write to reviews/ and return compact summary.

Note: reviewers should also review the CHANGE-PACKAGE for consistency.

Let me launch 5 agents in one message with run_in_background:false.

Careful about prompt length; keep focused.

Let me write them.
Lint clean, all handoff fitness rules pass. Now dispatching the reviewer gate (5 independent lenses) in parallel.

  `tool_call(arguments={"prompt": "Какой федеральный закон ввёл запрет на автоматическое списание средств за подписки без согласия потребителя и с какой даты он вс, name="web_fetch")`
  `tool_call(arguments={"prompt": "Где формируется и хранится согласие клиента на периодические списания по СБП — на стороне сервиса (мерчанта) или на стороне банк, name="web_fetch")`

Excellent, rich reviews. Now I need to triage and apply the clear fixes. This is a critical-system change; the reviews converge on several real defects. Let me decide what to fix now (clear, high-value) vs defer to open questions.

Convergent critical findings:
1. **INITIATED vocabulary inconsistency** (C-2 rubric, ADV-03, CONTRACT-1). Real. Fix: define charge↔payment projection explicitly. Options: (a) remove INITIATED from Charge.status and use CREATED for the accepted-but-unconfirmed state, with a charge-specific sub-state; (b) keep INITIATED only as a technical substate and map to CREATED externally; (c) publish the projection.
   Cleanest and least invasive: publish the projection `Charge.status INITIATED ≡ Payment.status CREATED` and define mapping table; keep Charge enum but add mapping; ensure `charge.failed`→ payment FAILED; charges can be refunded → the underlying payment goes REFUNDED, charge reflects... Let me define: `Charge.status` is a projection of the charge's payment: INITIATED↔CREATED, PAID↔PAID, CREDITED↔CREDITED, COMPLETED↔COMPLETED, FAILED↔FAILED; after refund the charge carries REFUNDED. So Charge enum should include REFUNDED too. Simplest robust fix: **remove the separate `Charge.status` enum entirely** and reuse the `Payment.status` enum for charges, mapping INITIATED→CREATED. I.e., define that a charge's `status` uses the same enum as Payment (`CREATED` for "accepted/queued to ОПКЦ"), and remove INITIATED from the paylaod. But I already wrote INITIATED in the FSM and tsp-api. I need consistency across: spine AD-010, FSM, tsp-api §6, openapi, change-package.

   Decision: **keep `INITIATED` as an internal technical state only**, and expose `CREATED` to clients (consistent with AD-002's canonical states). Rationale: least churn to the accepted ADR-002 vocabulary, satisfies "status enum not extended", and removes the dual vocabulary problem. So:
   - Spine AD-010 Rule: sequence `INITIATED (техническое подсостояние) → PAID → CREDITED → COMPLETED`, and explicitly: наружу выставляется канонический статус платежа (при `INITIATED` — `CREATED`).
   - Actually cleaner: change AD-010 to say the FSM uses canonical ADR-002 states with `CREATED` as the initial state for `CONSENT` type, and `QR_ISSUED` недостижимо. Then no INITIATED at all. That's the cleanest: a charge payment starts in `CREATED` (accepted, queued to ОПКЦ) and goes to `PAID`. AD-010's Prevents already covers "no second credit path". This removes the vocabulary conflict entirely and keeps `Payment.status` unchanged. 
   
   Hmm, but `INITIATED` conveys "debit initiated to ОПКЦ" distinctly. But AD-002 already defines `CREATED` as "зарегистрирован в шлюзе, запрос к ОПКЦ в процессе". For CONSENT, `CREATED` = "списание зарегистрировано, запрос к ОПКЦ в процессе" — perfect fit. So drop INITIATED. 
   
   Changes needed: spine AD-010; FSM doc §3 (diagram + table D1/D3/D4); tsp-api §6.1/6.4; openapi Charge.status enum; CHANGE-PACKAGE mentions of INITIATED; consent FSM §3 "Запрещённые переходы" references. Let me do this globally.

2. **AD-011 idempotency/uniqueness unenforceable & race** (C-1, ADV-04, CONTRACT-2). Fix: tighten AD-011 Rule: uniqueness applies to *attempt creation* (all non-terminal attempts) — i.e., partial unique index on (subscriptionId, billingPeriod) where status in (CREATED...). And define `chargeId` = Idempotency-Key requirement: "ТСП обязано передавать `Idempotency-Key`, равный `chargeId`" — or define precedence: (subscriptionId, billingPeriod) wins for period, Idempotency-Key for request replay. Let me pin: 
   - The request-level idempotency key is `chargeId` (and the header `Idempotency-Key` MUST equal `chargeId`); 
   - The period uniqueness is enforced on *attempt creation*: at most one non-terminal/terminal successful attempt per (subscriptionId, billingPeriod) — actually at most one *successful* per period is the business rule, but to close the race we need at most one *attempt in flight* per period. Define: at most one attempt in non-terminal state per (subscriptionId, billingPeriod); a new attempt with the same period while a non-terminal one exists → return existing (200) or 409 CHARGE_ALREADY_EXISTS. And after FAILED, a retry with a *new* chargeId is allowed only if the ТСП explicitly requests retry (not automatic) — and only one non-terminal at a time. That closes the double-debit race.
   - AD-011 Binds: add consent guard/FSM + TSP scheduler + API (reviewer noted Binds omitted them).
   - Add billingPeriod format pinning: define format `YYYY-MM` for MONTH, `YYYY-MM-DD` for DAY, ISO week `YYYY-Www` for WEEK; timezone UTC; and who decides period (ТСП supplies, gateway validates against `period`).

3. **AD-009 lacks limit-accounting ownership and revocation-semantics rules** (H-1 rubric, ADV-01/02). Fix: tighten AD-009 Rule to include:
   - single owner of limit accounting = gateway (authoritative local counter within confirmed limits); payer bank is final authority; mismatch → reject/alert.
   - limit source: `confirmedLimits` from ОПКЦ (C4) is authoritative; ТСП-requested limits are a request.
   - revocation: the linearization point — a charge request is admitted only if consent was `ACTIVE` at admission AND no revocation processed before the debit is dispatched to ОПКЦ; revocation that arrives after dispatch → the debit may still settle → treat as "зачисление допустимо, но требуется возврат и расследование" (or: policy decision). Hmm, this is a genuine semantic question that needs human decision (can a debit complete after revocation?). Better: pin an AD rule "линеаризация: момент допуска списания — транзакция guard; после регистрации списания в ОПКЦ отзыв не отменяет уже начатое списание автоматически; такие случаи — в отчёт и на возврат" and flag the policy as A6/human decision? The ADR-008 has "закрыть незавершённые попытки по политике" — vague. Let me tighten to: revocation blocks *new admissions*; already-dispatched debits are reported and, if settled, refunded; the gateway must not locally mark a dispatched debit FAILED (fixes ADV-01's second debit path).
   
   I'll add a new AD-014 for the revocation/linearization point? The adversarial reviewer suggested 3 new ADs (linearization point; single limit-accounting owner; canonical period identity + charge status vocabulary). I could fold into tightened AD-009/AD-011 Rules rather than adding 3 ADs—the skill says amend Rule in place is allowed. But adding ADs is also fine (next AD-n). To keep the spine lean and IDs stable, I'll:
   - Tighten AD-009 (limit accounting owner + revocation linearization point + audit log requirement).
   - Tighten AD-011 (attempt-creation uniqueness, key precedence, period format).
   - Tighten AD-010 (canonical status vocabulary; no INITIATED externally; guards for amount match).
   - Add **AD-014 «Доказуемость согласия и отзыва»** (security C-1) — this is a genuinely new invariant (evidence record + retention + audit), distinct divergence (non-repudiation). 
   - Add **AD-015 «AML/антифрод на согласии и списаниях»** (security H-4) — new divergence (fraud velocity). 
   - Add **AD-016 «Объектная авторизация и ссылки согласия»** (security H-3: IDOR + consentUrl/returnUrl trust). This covers ownership guard on all subscription endpoints and opaque/one-time consent links.
   Hmm, 3 new ADs. That's reasonable for the discovered holes. But is that scope creep? The task says prepare a package that can be decided. The reviewers found real holes; closing them is appropriate. But I should be careful: these are additional invariants that also need decision. I'll add them as Proposed ADR-008 (same change) — they're part of the change's invariants.

   Alternatively, some could be "open questions for the human". But security invariants like IDOR and audit log are clear fixes — apply them.

   Also AD-012 sequencing (H-4 rubric): tighten AD-012 Rule to require the RFP gate check to be recorded/verified before contract signature, and flag interaction with ADR-007. I can tighten: "...до подписания контракта; факт подтверждения G8 фиксируется в решении о выборе вендора; если вендор не подтвердил — выбор не может быть закрыт без пересмотра ADR-008/ADR-007 на A6."

4. **AD-010 redefines inherited FSM without AR-002 alignment** — handled by canonical vocabulary fix.

5. **Tech verification: ЗоЗПП date wrong** (must-fix). The reviewer says the enacted law is ФЗ от 15.10.2025 № 376-ФЗ, in force from 2026-03-01, amending ст. 16.1 ЗоЗПП. I should verify this claim myself before writing it (the reviewer might be wrong too — but they gave 4 sources). I should fetch at least one source to confirm. Let me fetch consultant.ru hotdocs link and/or pravo.gov.ru. Let me do a quick web_fetch to confirm, then correct ADR-008, CHANGE-PACKAGE, nfr dependency line.

6. **Tech verification: AD-009 "источник истины — БД шлюза" contradicts NSPK statement that consent is formed and stored on the bank side.** This is important: reconcile wording — gateway registry is a *projection/registry* with authority for routing/limits locally, but the authoritative consent is at the payer's bank/ОПКЦ; revocation is authoritative externally. For the architecture, the practical requirement (RPO=0, local limit enforcement, audit) still holds; but the wording "источник истины по согласию — БД шлюза" is wrong. Fix: "источник истины состояния согласия для операций шлюза — БД шлюза (реестр-проекция); авторитет по согласию — банк плательщика/ОПКЦ; расхождения — сверка, приоритет внешнего статуса". This preserves AD-009's Prevents while being accurate.

7. **CBR "по сервисам"** overstated — soften wording to "по документации НСПК и тестовым испытаниям" without "по сервисам". Fix in ADR-008 references/context.

8. Contract: add 404 on subscription paths, add error for resume/close of terminal, add `errorCode`/decline reason field, add `creditingStatus`/`errorCode` to Payment? The reviewer says Payment schema is a subset of examples — pre-existing. I'll add minimal: 404 responses, a `declinedReason`/`errorCode` on Subscription, and IDEMPOTENCY_CONFLICT on /charges 409 including CHARGE_CONFLICT. And fix the `charges[]` example missing subscriptionId. And fix "деeplink" typo (mixed alphabet) — in tsp-api.md and ADR/spine? Let me grep and fix.

9. Audit log for consent transitions (security H-1): covered by AD-014 (evidence) + tighten AD-009 to include audit-log in the transaction.

Let me be pragmatic and prioritize:
- Must fix (correctness/consistency): INITIATED vocabulary; AD-011 race/uniqueness/precedence/period format; AD-009 authority wording + limit owner + revocation linearization; ЗоЗПП fact; "по сервисам" softening; AD-012 sequencing; add AD-014 (evidence/audit), AD-015 (AML), AD-016 (object authz + consent links); contract fixes (404s, error fields, 409 codes, example, typo).
- Note but don't fix (open questions): dunning owner (already deferred w/ reason; but reviewer says it allows divergence → I'll tighten by pinning "не более одной незавершённой попытки на период" which closes it); payer notification (open question); retention срок (legal input); tariff/reporting (deferred/business).

That's a lot of editing. Let me be systematic and efficient.

First, verify the ЗоЗПП fact myself (important not to propagate a wrong "correction"). Let me fetch consultant.ru document.

Let me also double-check the NSPK statement about consent stored at bank side — the reviewer quoted a second NSPK page. Let me fetch sbp.nspk.ru again? The reviewer cited "the same source" — maybe https://sbp.nspk.ru/ or a page on автоплатёж. Let me trust but verify partially: fetch the NSPK blog page again asking specifically about where consent is stored and who initiates. Actually I can fetch it and look. Let me fetch both the consultant link and the nspk page.

Let me do these two fetches in parallel.
Reviews found real defects. Before applying fixes, let me independently verify the one factual correction (the law date) — I won't propagate a "fix" I can't confirm.

  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", new_string="### AD-009. Согласие плательщика — отдельная сущность; допуск списания и учёт лимитов контролирует шлюз\n\n- Status: Proposed (ADR-008)\n- , old_string="### AD-009. Согласие плательщика — отдельная сущность с собственной статусной машиной\n\n- Status: Proposed (ADR-008)\n- **Binds**: БД шлюз)`

Confirmed: ФЗ от 15.10.2025 № 376-ФЗ, amending ст. 16.1 ЗоЗПП, in force 2026-03-01. My/robokassa's "01.09.2025" was wrong. Must fix in ADR-008, CHANGE-PACKAGE, nfr dependency line, and possibly the memlog.

Also the NSPK blog does NOT state where consent is stored; the tech-verification reviewer cited a *second* source ("Согласие клиента на списания формируется и хранится на стороне банка") — I couldn't confirm it from this page. The reviewer flagged the URL https://www.nspk.ru/banks/payment-request as unreachable. I should be careful: I can't verify the "stored at bank side" claim. So rather than rewrite AD-009 to say "authority at bank", I should soften to acknowledge the open question: the *locus of authority* for consent is an external input to confirm with НСПК; the gateway keeps a local registry as source of truth for its operations and reconciles. That's defensible and marks [ТРЕБУЕТ ПРОВЕРКИ]. Also note the reviewer's point that "resume after отключение" is possible → my "REVOKED необратим" may be too strong. The NSPK page says "при желании подписку можно возобновить" — but that likely means creating/resuming a subscription, not un-revoking consent. To be safe: allow a new consent (new subscriptionId) after revocation, and mark "возможно ли возобновление того же согласия — [ТРЕБУЕТ ПРОВЕРКИ]". My FSM already says "возобновление возможно только новым согласием (новый subscriptionId)". That's safe. But ADR/Fsm says "REVOKED необратим" — keep, but add note that НСПК may allow resume of the subscription → new consent. Actually the reviewer flagged "REVOKED irreversibility contradicts the cited НСПК page". I'll add a note in the FSM open questions: "возобновление подписки после отключения в приложении банка: НСПК упоминает возможность возобновления — уточнить, означает ли это новое согласие или восстановление того же [ТРЕБУЕТ ПРОВЕРКИ]". Good.

Now, given the volume, let me plan the edit set precisely. I'll apply the fixes that are clear and high-value. Let me enumerate edits:

### A. ARCHITECTURE-SPINE.md
1. AD-009 Rule: 
   - add limit-accounting owner + authoritative limits source
   - add revocation linearization (admission point; already-dispatched debits not locally failed)
   - add audit log to the transaction
   - reword "источник истины" → local source of truth for operations + external authority reconciled [ТРЕБУЕТ ПРОВЕРКИ]
   - add ownership guard (tspId) — or put in AD-016. I'll put ownership in AD-016.
2. AD-010 Rule: canonical status vocabulary (начинается в `CREATED`; `QR_ISSUED` недостижимо; `INITIATED` — только внутреннее техническое подсостояние, наружу не выставляется); amount-match guard.
3. AD-011 Rule: uniqueness at attempt creation for non-terminal attempts; key precedence; billingPeriod format/timezone.
4. AD-012 Rule: sequencing/enforcement (G8 confirmation recorded before contract signature; failure → A6/ADR-007).
5. Add AD-014 (доказуемость согласия и отзыва + audit), AD-015 (AML/антифрод), AD-016 (объектная авторизация и ссылки согласия).
6. Maybe add an "Open questions" block? The spine template has Deferred; I added change-set open questions in the package. The rubric flagged "no open-questions block in CS-001". I'll add a short "Открытые вопросы изменения" bullet list in the CS-001 header block. Good.

### B. docs/spec/consent-state-machine.md
- Replace INITIATED with canonical CREATED (with internal substate `DEBIT_SENT` maybe). Update diagram and tables D1..D7.
- Tighten idempotency table (§5): attempt-creation uniqueness, key precedence, period format.
- §4 guard: add "не более одной незавершённой попытки на период", limit owner, atomicity.
- §2.3 revocation linearization.
- §8 open questions: resume semantics; authority of consent.

### C. docs/contracts/tsp-api.md
- §6.1 charge statuses: use canonical CREATED (not INITIATED); note Charge.status mirrors Payment.status.
- §6.4: 409 codes include IDEMPOTENCY_CONFLICT; note Idempotency-Key must equal chargeId; billingPeriod format.
- Add 404 to §6.3/6.5, error for terminal consent.
- Add `errorCode`/declined reason field to Subscription example? Add field `errorCode` optional.
- Fix charges[] example add subscriptionId.
- Fix "деeplink" typo → "deeplink".
- §7: state Charge.status is same enum as Payment.status.

### D. openapi/tsp-api.yaml
- Charge.status enum → reuse Payment.status enum (or keep but align). Simplest: remove `Charge.status` enum duplication and `$ref`? Can't $ref an enum easily in 3.0 without a named enum schema. Option: define component schema `PaymentStatus` (enum) and use it for both Payment.status and Charge.status. But changing Payment.status from inline enum to $ref changes the existing operation schema → my BC checker compares properties[...].enum — if I change to $ref, `o.properties.status.enum` exists but `n.properties.status.enum` undefined → BC check flags "enum changed". Hmm. To keep existing Payment exactly as-is, keep inline enum on Payment, and for Charge use... I could keep Charge.status inline with the same values as Payment minus QR_ISSUED? That reintroduces divergence. 

   Better: make Charge NOT carry a status at all? No, clients need it.
   
   Cleanest: `Charge.status` uses the SAME canonical enum values as Payment. So set Charge.status enum = [CREATED, PAID, CREDITED, COMPLETED, FAILED, REFUNDED, EXPIRED]? That includes REFUNDED/EXPIRED which may not apply to charges. The reviewer's point is mappability, not identical sets. I'll define Charge.status enum = [CREATED, PAID, CREDITED, COMPLETED, FAILED, REFUNDED] and document mapping `CREATED ↔ Payment.status CREATED`, and note `QR_ISSUED`/`EXPIRED` недостижимы для списаний. Alternatively simply drop Charge.status and let clients use GET /payments. But the charge resource benefits from a status.

   Decision: keep `Charge.status` but with canonical values `[CREATED, PAID, CREDITED, COMPLETED, FAILED, REFUNDED]`, and add description "совпадает с Payment.status соответствующего paymentId; QR_ISSUED/EXPIRED недостижимы". Add `creditingStatus`? not needed.
   
   Also add `declineReason`/`errorCode` to Subscription? Add `errorCode` (nullable) to Charge and Subscription.
   
   Add `404` responses for GET/suspend/resume/close. Add `409` on /charges to include IDEMPOTENCY_CONFLICT.
   
   Fix `charges[]` example (subscriptionId) — that's in tsp-api.md, not openapi.

### E. docs/change/c2b-subscriptions/CHANGE-PACKAGE.md
- Fix law reference and dates (§0? §1 mentions "ЗоЗПП... в силе с 01.09.2025" in §1 dimension table; §7 #5; §9 assumptions/facts). Replace with ФЗ 376-ФЗ от 15.10.2025, в силе с 01.03.2026.
- §4: mention Charge.status mapping; INITIATED removed.
- §2.1 table: AD-009..AD-016 (add new ADs).
- §6 acceptance criteria: add AC for evidence/audit (AD-014), AML (AD-015), IDOR (AD-016), revocation-after-dispatch.
- §7 decisions list: add locus-of-authority/open question; dunning owner now pinned partially; add "resume semantics" open question.
- §9: fix the law fact; add assumption about unknown consent authority; update verification list.
- Also §3 solution table: add rows for new invariants? Keep summary; mention AD-014..016.

### F. docs/nfr.md
- Fix ЗоЗПП date → 01.03.2026 (ФЗ 376-ФЗ).
- Add AML/audit/evidence rows? Add a couple: "Доказательство согласия/отзыва сохранено для 100% переходов", "AML-проверка согласий/списаний — 100% по порогам", "Аудит переходов согласия — 100%". Add.

### G. docs/adr/ADR-008
- Fix law facts (context + table + references).
- Soften "по сервисам".
- Reword decision #1 (consent registry vs authority) to reflect external authority + local registry + reconciliation, marked [ТРЕБУЕТ ПРОВЕРКИ].
- Add decisions for evidence/audit, AML, object authz (AD-014..016).
- Update Alternatives A note maybe.
- Add open questions.

### H. memlog — append corrected facts/decisions (append-only; I'll add entries noting the correction rather than editing). Actually memlog is append-only; I'll append new lines for corrections. I must not edit existing lines. Let me append a few entries.

Also reviews/review-*.md written by subagents — keep as gate artifacts (skill says keep in reviews/).

This is a large but mechanical set. Let me proceed carefully, file by file. I'll prioritize spine + FSM + contract + openapi (the normative artifacts), then the package/ADR/nfr/memlog.

Let me start with the spine edits.

#### Spine AD-009 rewrite

New text:

### AD-009. Согласие плательщика — отдельная сущность; лимиты и отзыв контролируются шлюзом

- Status: Proposed (ADR-008)
- **Binds**: БД шлюза (реестр согласий), статусная машина согласия, guard списаний, адаптер ОПКЦ, нотификатор ТСП.
- **Prevents**: смешение согласия и платежа (одно согласие → много списаний) с потерей контроля лимитов; списание без действующего согласия; списание по согласию, отозванному плательщиком; локальная отметка уже отправленного списания как неуспешного (проводка состоялась, а шлюз считает иначе) → повторное списание; расхождение учёта лимитов между несколькими счётчиками.
- **Rule**: Согласие плательщика — самостоятельная сущность с уникальным `subscriptionId` и собственной статусной машиной (`CREATED → PENDING_PAYER → ACTIVE → REVOKED | EXPIRED | DECLINED`, плюс `SUSPENDED`); наружу выставляется статус согласия, локальный реестр — источник истины для операций шлюза, внешний авторитет (банк плательщика/ОПКЦ) — сверяемый, расхождение разрешается в пользу внешнего статуса (точка авторитета — внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`). Единственный владелец учёта лимитов — шлюз: он атомарно проверяет и учитывает лимиты при допуске списания; подтверждённые ОПКЦ лимиты авторитетнее запрошенных ТСП. Административные переходы согласия (подтверждение, отзыв, изменение лимитов) и запись в outbox и неизменяемый аудит-лог выполняются в одной локальной транзакции (расширение AD-002). Допуск списания возможен только при согласии в `ACTIVE`; отзыв блокирует допуск новых списаний, но не отменяет уже зарегистрированное в ОПКЦ списание — такое списание не помечается локально неуспешным, а попадает в отчёт и, при состоявшемся зачислении, на возврат.

Hmm that's long but the Rule must be enforceable. Good.

#### AD-010 rewrite
- **Rule**: Рекуррентное списание моделируется платежом с `operationType = CONSENT` в канонической статусной машине ADR-002: начинается в `CREATED` (регистрация списания, запрос к ОПКЦ в процессе) и далее `→ PAID → CREDITED → COMPLETED`; `QR_ISSUED` в этом типе недостижимо; отдельные «внешние» статусы не вводятся (внутреннее подсостояние «отправлено в ОПКЦ» наружу не выставляется). Финансовый путь в АБС — общий: зачисление только из `PAID` (AD-005 не ослабляется). Guard сверки суммы/получателя при переходе в `PAID` — как для C2B. Сверка и отчётность включают платежи типа `CONSENT` без исключений.

#### AD-011 rewrite
- Binds: + guard/FSM согласия, API ТСП.
- **Rule**: У каждой попытки списания есть `chargeId` (значение заголовка `Idempotency-Key` должно совпадать с `chargeId`) и ключ периода `billingPeriod` (формат фиксирован: `YYYY-MM` для MONTH, `YYYY-MM-DD` для DAY, `YYYY-Www` для WEEK; UTC). Уникальность обеспечивается на уровне БД **в момент создания попытки**: не более одной незавершённой попытки и не более одного успешного списания на (`subscriptionId`, `billingPeriod`). Повтор с тем же `chargeId` возвращает существующий ресурс; повтор с тем же периодом при наличии незавершённой или успешной попытки не создаёт новое списание и не отправляет новый вызов в ОПКЦ. Повторная попытка после `FAILED` допускается только явным запросом ТСП с новым `chargeId` и только после терминального завершения предыдущей. Приоритет ключей: (`subscriptionId`, `billingPeriod`) — период; `chargeId`/`Idempotency-Key` — идемпотентность запроса. AD-003 не ослабляется.

#### AD-012 rewrite (add sequencing)
- **Rule**: ... (keep) ... Поддержка подписок входит в gate-критерии RFP; подтверждение критерия (proof идемпотентности `chargeByConsent`, сценарии P9/P10) фиксируется в решении о выборе вендора **до подписания контракта**. Если вендор не подтверждает поддержку подписок, контракт не может быть закрыт по подпискам без пересмотра ADR-008 (и, при необходимости, ADR-007) на решении A6.

#### AD-014 (new)
### AD-014. Доказуемость согласия и отзыва
- Status: Proposed (ADR-008)
- Binds: реестр согласий, аудит-лог, адаптер ОПКЦ, хранение ПДн.
- Prevents: согласие/отзыв, которые банк не может доказать (нет артефакта подтверждения или отзыва) → юридический риск и невозможность спора; отсутствие следа изменения лимитов; неаудируемые согласия.
- Rule: Каждый переход согласия (`CREATED→…→ACTIVE`, `ACTIVE→REVOKED`, изменение лимитов) сохраняет в одной транзакции неизменяемый артефакт согласия: идентификатор согласия в ОПКЦ, версию/снимок условий, фактические подтверждённые лимиты, время и статус — и пишет запись в неизменяемый аудит-лог. Состав и срок хранения артефакта определяются юридическим заключением (внешний вход); до его получения хранение обязательно, срок — конфигурируемый и не менее срока исковой давности по операциям.

Hmm "не менее срока исковой давности" — inventing. Better: "срок — по юридическому заключению [ТРЕБУЕТ ПРОВЕРКИ]". Keep Rule enforceable: "сохранение артефакта обязательно с момента перехода; срок — из юридического заключения".

#### AD-015 (new)
### AD-015. ПОД/ФТ-контроль согласий и списаний
- Status: Proposed (ADR-008)
- Binds: реестр согласий, guard списаний, антифрод/AML-контур, SIEM.
- Prevents: «сбор согласий» как схема (одно согласие оформляется, затем множественные списания без контроля скорости/агрегации); согласия и списания, выпавшие из AML-мониторинга банка.
- Rule: Создание согласия и каждое списание передаются в антифрод/AML-контур банка (расширение AD-007): минимум — контроль скорости и агрегации по `tspId` и по (`tspId`, `payerRef`), пороговые суммы, признак отказа guard (D2). Шлюз передаёт данные, решение принимает AML-контур; блокировка/приостановка согласия по решению AML — административный переход с аудитом.

#### AD-016 (new)
### AD-016. Объектная авторизация подписок и безопасность ссылок согласия
- Status: Proposed (ADR-008, ADR-006)
- Binds: API ТСП (все методы подписок), адаптер ОПКЦ, DMZ.
- Prevents: доступ ТСП к чужому согласию по угаданному `subscriptionId` (чтение/приостановка/необратимое закрытие — IDOR); использование шлюза как открытого редиректора и подмена ссылки согласия (фишинг/кража подтверждения).
- Rule: Любой метод API ТСП по согласию (чтение, списание, приостановка, возобновление, закрытие) проверяет принадлежность согласия аутентифицированному ТСП (`tspId` согласия = `tspId` запроса); несовпадение — `404`/`403` без раскрытия существования. `consentUrl`/deeplink — непрозрачная ссылка, выпущенная ОПКЦ, передаётся как есть, не конструируется шлюзом; `returnUrl` принимается только по белому списку хостов ТСП. Шлюз не встраивает в ссылку данные плательщика.

Also update the CS-001 header block: add "Открытые вопросы изменения" bullets.

And "Binds/Prevents/Rule" keywords present. Lint will pass (case-insensitive 'binds','prevents','rule' substring). Note "Prevents" contains "prevents"; fine.

Careful: lint checks AD ids monotonic and fields present. New AD-014..AD-016 after AD-013 → monotonic.

Now this is a big block of new content. Let me apply via edit (insert after AD-013 block, before "---\n\n## Deferred"). And rewrite AD-009..AD-012 blocks individually.

Let me do it stepwise with edit calls.

Let me first rewrite AD-009.

I need exact old strings. Let me read the current spine CS-001 section to get exact text.

I have it from the earlier tool output. Let me construct edits.

AD-009 old:
```
### AD-009. Согласие плательщика — отдельная сущность с собственной статусной машиной

- Status: Proposed (ADR-008)
- **Binds**: БД шлюза (реестр согласий), статусная машина согласия, адаптер ОПКЦ, нотификатор ТСП.
- **Prevents**: смешение согласия и платежа (одно согласие → много списаний) с потерей контроля лимитов; списание без действующего согласия; «висящий» локальный статус `ACTIVE` после отзыва согласия плательщиком → списание по отозванному согласию.
- **Rule**: Согласие плательщика — самостоятельная сущность с уникальным `subscriptionId` и собственной статусной машиной (`CREATED → PENDING_PAYER → ACTIVE → REVOKED | EXPIRED | DECLINED`, плюс `SUSPENDED`). Источник истины по согласию — БД шлюза; внешний статус ОПКЦ — сверяемый. Смена статуса согласия и запись события в outbox выполняются в одной локальной транзакции (по образцу AD-002). Инициировать списание можно только при согласии в состоянии `ACTIVE`.
```

I'll replace it.

Similarly AD-010, AD-011, AD-012.

Then insert new ADs.

Let me go.
Confirmed: the law is **ФЗ от 15.10.2025 № 376-ФЗ**, in force **2026-03-01** (the earlier "01.09.2025" was a draft-era claim). Applying the reviewer findings now. First, tightening the new spine invariants.

  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", new_string="- **Rule**: Рекуррентное списание моделируется платежом с `operationType = CONSENT` в канонической статусной машине ADR-002: начинается в `, old_string="- **Rule**: Рекуррентное списание моделируется платежом с `operationType = CONSENT`. Финансовый путь в АБС — общий: зачисление только из `P)`
  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", new_string="### AD-011. Идемпотентность рекуррентных списаний по периоду\n\n- Status: Proposed (ADR-008)\n- **Binds**: планировщик списаний ТСП, guard , old_string="### AD-011. Идемпотентность рекуррентных списаний по периоду\n\n- Status: Proposed (ADR-008)\n- **Binds**: планировщик списаний ТСП, `POST )`
  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", new_string="- **Rule**: Все операции по согласиям и рекуррентным списаниям идут только через единый адаптер ОПКЦ (AD-004). Методы и события подписок до, old_string="- **Rule**: Все операции по согласиям и рекуррентным списаниям идут только через единый адаптер ОПКЦ (AD-004). Методы и события подписок до)`
  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", new_string="- **Пакет изменения:** `docs/change/c2b-subscriptions/CHANGE-PACKAGE.md`, `docs/adr/ADR-008-...md`, `docs/spec/consent-state-machine.md`, A, old_string="- **Пакет изменения:** `docs/change/c2b-subscriptions/CHANGE-PACKAGE.md`, `docs/adr/ADR-008-...md`, `docs/spec/consent-state-machine.md`, A)`

Now AD-012 Rule tightening + add AD-014..AD-016 and the open-questions block in the CS-001 header.

AD-012 current Rule:
"- **Rule**: Все операции по согласиям и рекуррентным списаниям идут только через единый адаптер ОПКЦ (AD-004). Методы и события подписок добавляются во внутренний контракт адаптера. Поддержка подписок входит в gate-критерии RFP до подписания контракта с вендором. Ядро остаётся контрактно-независимым от транспорта (AD-008)."

Replace with added sequencing.

Then insert new ADs after AD-013 block. The AD-013 block ends with:
"- **Rule**: Подтверждение и отзыв согласия выполняет банк плательщика в среде СБП (ОПКЦ). Шлюз выдаёт ТСП ссылку/деeplink и асинхронный результат, не собирает аутентификационные данные и полные реквизиты плательщика. Работа с данными плательщика — только в минимизированном виде (ссылочный идентификатор, маскированные реквизиты), как в AD-007.

---

## Deferred"

I'll also fix "деeplink" typo → "deeplink" in AD-013 and elsewhere.

Let me do AD-012 edit and the AD-013+insert edit.

Also add open questions bullets to CS-001 header (after "Пакет изменения" line).

Let me batch edits: three edits (AD-012 rule; header open questions; AD-013 typo+insert new ADs). The AD-013 insert and typo fix can be one edit.

Edit 1: AD-012 Rule.
Edit 2: header add open questions.
Edit 3: AD-013 block replace (typo + append new ADs + keep "---\n\n## Deferred").

Let me write them.

  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", new_string="- **Статус:** Proposed — вынесено на решение A6 (ADR-008). Блоки AD-009…AD-016 действуют после ратификации ADR-008; до этого — проект, не о, old_string="- **Статус:** Proposed — вынесено на решение A6 (ADR-008). Блоки AD-009…AD-013 действуют после ратификации ADR-008; до этого — проект, не о)`
  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", new_string="- **Rule**: Подтверждение и отзыв согласия выполняет банк плательщика в среде СБП (ОПКЦ). Шлюз выдаёт ТСП ссылку/deeplink и асинхронный рез, old_string="- **Rule**: Подтверждение и отзыв согласия выполняет банк плательщика в среде СБП (ОПКЦ). Шлюз выдаёт ТСП ссылку/деeplink и асинхронный рез)`

Note: the header still says "Блоки AD-009…AD-013" — now AD-009..AD-016. Let me fix that in the next edit.

Now the big insert: replace AD-013 block end + add open questions fix + new ADs. Let me read current AD-013 block text exactly (with the typo "деeplink").

From earlier: 
```
### AD-013. Поверхность согласия плательщика — вне шлюза (trust-зоны не расширяются)

- Status: Proposed (ADR-008, ADR-006)
- **Binds**: DMZ, API ТСП, trust-зоны, ИБ.
- **Prevents**: превращение шлюза в публичный платёжный портал с собственной аутентификацией клиента (новый trust-разрыв; аутентификационные данные и полные реквизиты плательщика в периметре шлюза; рост поверхности атаки; требования 152-ФЗ сверх текущих).
- **Rule**: Подтверждение и отзыв согласия выполняет банк плательщика в среде СБП (ОПКЦ). Шлюз выдаёт ТСП ссылку/деeplink и асинхронный результат, не собирает аутентификационные данные и полные реквизиты плательщика. Работа с данными плательщика — только в минимизированном виде (ссылочный идентификатор, маскированные реквизиты), как в AD-007.

---

## Deferred (с причиной и условием возврата)
```

I'll replace with AD-013 (typo fixed) + AD-014..AD-016 + separator + Deferred heading. And also fix the header "AD-009…AD-013" → "AD-009…AD-016".

Let me do the header fix and the big insert.

Header line: "- **Статус:** Proposed — вынесено на решение A6 (ADR-008). Блоки AD-009…AD-013 действуют после ратификации ADR-008; до этого — проект, не обязательство."

Let me do both edits.

  `edit(file_path="/home/architect/project/docs/spec/consent-state-machine.md", new_string="Списание — это платёж с `operationType = CONSENT` в канонической модели ADR-002 (AD-010). Отдельного внешнего статуса «инициировано» нет: р, old_string="Списание — это платёж с `operationType = CONSENT` в существующей модели (ADR-002, AD-010). Финансовый путь до АБС общий: зачисление **тольк)`

Spine updated. Also update the "Контракты и версии" line "Пакет изменения" mentions ADR-008 — fine. Also Deferred item about согласие: fine.

Now update the FSM spec to remove INITIATED and align. Let me rewrite the relevant sections of docs/spec/consent-state-machine.md:
- §3 title/intro/diagram/table D1..D7: replace INITIATED with CREATED; remove "INITIATED" from verbs; D1 creates in CREATED; D3 CREATED→PAID; D4 CREATED→FAILED; D5/D6 same.
- §2.3: add revocation linearization point + cross-TSP guard pointer to AD-016.
- §4 guard: add "не более одной незавершённой/успешной попытки на период", atomicity, owner.
- §5 idempotency table: key precedence, attempt-creation uniqueness, period format.
- §7 mapping: charge status = canonical Payment.status (CREATED, not INITIATED).
- §8 open questions: authority, resume semantics.

Let me do targeted edits.

First §3. Current text:

```
## 3. Списание: статусная машина платежа типа CONSENT

Списание — это платёж с `operationType = CONSENT` в существующей модели (ADR-002, AD-010). Финансовый путь до АБС общий: зачисление **только** из `PAID` (AD-005).

```
INITIATED ──► PAID ──► CREDITED ──► COMPLETED
    │           │
    ▼           ▼
 FAILED      FAILED (возврат — сага ADR-005)
```

| № | From | To | Триггер | Guard | Действие |
|---|---|---|---|---|---|
| D1 | — | `INITIATED` | `POST /v1/subscriptions/{id}/charges` (`chargeId`, `billingPeriod`) | согласие `ACTIVE`; `amount` ≤ лимита на списание; сумма периода ≤ месячного лимита; срок не истёк | запись списания + outbox «списание в ОПКЦ» |
| D2 | — | (отказ) | тот же запрос | guard не пройден (лимит/статус/срок) | **вызов ОПКЦ не делается**; `422`, код `SUBSCRIPTION_LIMIT_EXCEEDED` / `SUBSCRIPTION_NOT_ACTIVE`; состояние платежа не создаётся |
| D3 | `INITIATED` | `PAID` | нотификация ОПКЦ: списание подтверждено банком плательщика (или сверка) | сумма и получатель совпадают | outbox «зачисление в АБС» (как T4) |
| D4 | `INITIATED` | `FAILED` | отказ банка плательщика / ОПКЦ (нет средств, лимит банка, отозвано согласие) | — | нормализованный `errorCode`, вебхук `charge.failed`; повтор возможен новым `chargeId` или тем же периодом по политике ТСП |
...
```

Let me replace the whole §3 block up to "## 4. Guard лимитов".

New:

```
## 3. Списание: платёж типа CONSENT в канонической статусной машине

Списание — это платёж с `operationType = CONSENT` в канонической модели ADR-002 (AD-010). Отдельного внешнего статуса «инициировано» нет: регистрация списания — это `CREATED` (запрос к ОПКЦ в процессе); подсостояние «отправлено в ОПКЦ» — внутреннее и наружу не выставляется. Финансовый путь до АБС общий: зачисление **только** из `PAID` (AD-005).

```
CREATED ──► PAID ──► CREDITED ──► COMPLETED
   │          │
   ▼          ▼
 FAILED     FAILED (возврат — сага ADR-005; для зачисленного — REFUNDED)
```

| № | From | To | Триггер | Guard | Действие |
|---|---|---|---|---|---|
| D1 | — | `CREATED` | `POST /v1/subscriptions/{id}/charges` (`chargeId`, `billingPeriod`) | согласие `ACTIVE`; `amount` ≤ лимита на списание; сумма периода + `amount` ≤ лимита периода; срок не истёк; **нет незавершённой или успешной попытки на этот период** | запись списания + outbox «списание в ОПКЦ» (одна транзакция) |
| D2 | — | (отказ) | тот же запрос | guard не пройден | **вызов ОПКЦ не делается**; `422` (`SUBSCRIPTION_LIMIT_EXCEEDED` / `SUBSCRIPTION_NOT_ACTIVE` / `SUBSCRIPTION_EXPIRED`) или `409 CHARGE_ALREADY_EXISTS`; состояние платежа не создаётся; отказ пишется в аудит и передаётся в AML (AD-015) |
| D3 | `CREATED` | `PAID` | нотификация ОПКЦ: списание подтверждено банком плательщика (или сверка) | сумма и получатель совпадают | outbox «зачисление в АБС» (как T4) |
| D4 | `CREATED` | `FAILED` | отказ банка плательщика / ОПКЦ (нет средств, лимит банка, отозванное согласие) | — | нормализованный `errorCode`, вебхук `charge.failed`; повтор — только явным новым запросом ТСП с новым `chargeId` после терминального завершения (AD-011) |
| D5 | `PAID` | `CREDITED` | подтверждение АБС (`absDocId`) | вызов АБС идемпотентен по `paymentId` | как T8 |
| D6 | `PAID` | (остаётся `PAID`) | АБС недоступна | — | подсостояние `ABS_PENDING`, ретраи, сверка (как T9) |
| D7 | `CREDITED` | `COMPLETED` | вебхук ТСП доставлен/в очереди | — | как T10 |

`QR_ISSUED` в типе `CONSENT` недостижимо (AD-010). Возвраты по зачисленному списанию — существующая сага (ADR-005); отзыв согласия **не** отменяет уже зачисленные платежи автоматически — возврат оформляется ТСПом отдельно. Уже **отправленное** в ОПКЦ списание при отзыве согласия **не** помечается локально `FAILED`: оно доводится до терминального статуса, попадает в отчёт незавершённых и, при зачислении, на возврат (AD-009).
```

Then §4 guard: add attempt uniqueness + owner + atomicity. Current §4:

```
## 4. Guard лимитов (проверка перед вызовом ОПКЦ)

Проверяется ядром шлюза атомарно относительно создания списания (иначе гонка двух попыток за период):

1. согласие существует и в статусе `ACTIVE`;
2. `tspId` платежа = `tspId` согласия;
3. `amount` > 0 и ≤ `maxAmountPerCharge`;
4. сумма успешных списаний за текущий период + `amount` ≤ `periodLimit` (месячный лимит);
5. текущая дата в пределах `startDate`…`endDate`;
6. нет успешного списания с тем же (`subscriptionId`, `billingPeriod`).

Окончательный контроль — за банком плательщика/ОПКЦ: ...
```

New: item 4 change to account for in-flight (authorized) amounts: "сумма успешных **и незавершённых** списаний за период + amount ≤ periodLimit"; item 6: "нет незавершённой/успешной попытки". Add note: single owner + limits source + linearization point.

Let me rewrite §4 and §5.

§5 current:
```
## 5. Идемпотентность (AD-003, AD-011)

| Триггер | Ключ | Поведение при повторе |
|---|---|---|
| `POST /v1/subscriptions` | `Idempotency-Key` | возврат того же `subscriptionId`, состояние не меняется |
| `POST /v1/subscriptions/{id}/charges` | `Idempotency-Key` = `chargeId` + `billingPeriod` | успешная попытка за период уже есть → возврат существующего `chargeId` (200), новое списание не создаётся |
| ...
Гонка «планировщик ТСП + ручное списание» разрешается уникальностью (`subscriptionId`, `billingPeriod`) на уровне БД: проигравшая попытка получает существующий ресурс или `409 CHARGE_ALREADY_EXISTS`.
```

New §5 with precedence + attempt-creation uniqueness + period format.

Let me construct the edits. I'll replace §3 (intro through the line before "## 4"), §4, §5, §7 first bullet, §8.

Let me do them.

For §3 replacement, old_string must be exact. Let me use the block from "Списание — это платёж" through the D7 row and the trailing paragraphs. I'll include from "Списание — это платёж с" to "оформляется ТСПом отдельно." Let me be careful about the fenced code block content.

The old text (from my earlier write):
```
Списание — это платёж с `operationType = CONSENT` в существующей модели (ADR-002, AD-010). Финансовый путь до АБС общий: зачисление **только** из `PAID` (AD-005).

```
INITIATED ──► PAID ──► CREDITED ──► COMPLETED
    │           │
    ▼           ▼
 FAILED      FAILED (возврат — сага ADR-005)
```

| № | From | To | Триггер | Guard | Действие |
|---|---|---|---|---|---|
| D1 | — | `INITIATED` | `POST /v1/subscriptions/{id}/charges` (`chargeId`, `billingPeriod`) | согласие `ACTIVE`; `amount` ≤ лимита на списание; сумма периода ≤ месячного лимита; срок не истёк | запись списания + outbox «списание в ОПКЦ» |
| D2 | — | (отказ) | тот же запрос | guard не пройден (лимит/статус/срок) | **вызов ОПКЦ не делается**; `422`, код `SUBSCRIPTION_LIMIT_EXCEEDED` / `SUBSCRIPTION_NOT_ACTIVE`; состояние платежа не создаётся |
| D3 | `INITIATED` | `PAID` | нотификация ОПКЦ: списание подтверждено банком плательщика (или сверка) | сумма и получатель совпадают | outbox «зачисление в АБС» (как T4) |
| D4 | `INITIATED` | `FAILED` | отказ банка плательщика / ОПКЦ (нет средств, лимит банка, отозвано согласие) | — | нормализованный `errorCode`, вебхук `charge.failed`; повтор возможен новым `chargeId` или тем же периодом по политике ТСП |
| D5 | `PAID` | `CREDITED` | подтверждение АБС (`absDocId`) | вызов АБС идемпотентен по `paymentId` | как T8 |
| D6 | `PAID` | (остаётся `PAID`) | АБС недоступна | — | подсостояние `ABS_PENDING`, ретраи, сверка (как T9) |
| D7 | `CREDITED` | `COMPLETED` | вебхук ТСП доставлен/в очереди | — | как T10 |

`QR_ISSUED` в типе `CONSENT` недостижимо (AD-010). Возвраты по зачисленному списанию — существующая сага (ADR-005); отзыв согласия **не** отменяет уже зачисленные платежи автоматически — возврат оформляется ТСПом отдельно.
```

Note the nested code fence inside — the edit tool handles literal text. But careful: the file contains a fenced block with ``` — my old_string includes it. Should be fine.

Let me do the edits.
Now aligning the state-machine spec (dropping the non-canonical `INITIATED`, pinning the race and period semantics).

  `edit(file_path="/home/architect/project/docs/spec/consent-state-machine.md", new_string="- Отзыв (C6/C10) **необратим** для данного согласия: возобновление — только новым согласием (новый `subscriptionId`), а не переходом из `RE, old_string="- Отзыв (C6/C10) **необратим**: возобновление возможно только новым согласием (новый `subscriptionId`), а не переходом из `REVOKED`.\n- Пла)`
  `edit(file_path="/home/architect/project/docs/spec/consent-state-machine.md", new_string="## 4. Guard допуска списания (проверка перед вызовом ОПКЦ)\n\nЕдинственный владелец учёта лимитов — шлюз (AD-009); лимиты берутся из подтве, old_string="## 4. Guard лимитов (проверка перед вызовом ОПКЦ)\n\nПроверяется ядром шлюза атомарно относительно создания списания (иначе гонка двух попы)`

Now §2.3 add revocation linearization + cross-TSP guard (AD-016). And §4, §5, §7, §8.

§2.3 current:
```
### 2.3 Запрещённые переходы (инварианты)

- Списание разрешено **только** при согласии в `ACTIVE` (AD-009). Из `PENDING_PAYER`, `SUSPENDED`, `REVOKED`, `EXPIRED`, `DECLINED` — недостижимо; проверяется fitness-тестом.
- `REVOKED`/`EXPIRED`/`DECLINED` терминальны: повторный отзыв идемпотентен, состояние не меняется.
- Реквизиты согласия (ТСП, назначение, валюта, идентификатор плательщика) иммутабельны после `ACTIVE` (C4). Изменяются только лимиты/срок/период — и только в сторону, разрешённую НСПК (уточнить `[ТРЕБУЕТ ПРОВЕРКИ]`).
- Отзыв (C6/C10) **необратим**: возобновление возможно только новым согласием (новый `subscriptionId`), а не переходом из `REVOKED`.
- Плательщик не может быть дебетован по согласию, принадлежащему другому ТСП: `tspId` платежа обязан совпадать с `tspId` согласия (guard перед списанием).
```

Add a bullet about linearization point and about resume semantics [ТРЕБУЕТ ПРОВЕРКИ].

Let me edit §2.3 by replacing the last two bullets with three.

§4 rewrite. §5 rewrite. §7 first bullet. §8 add.

Let me read current §4/§5/§7/§8 exact text — I have from the original write (unchanged except my §3 edit). Let me construct.

§4:
```
## 4. Guard лимитов (проверка перед вызовом ОПКЦ)

Проверяется ядром шлюза атомарно относительно создания списания (иначе гонка двух попыток за период):

1. согласие существует и в статусе `ACTIVE`;
2. `tspId` платежа = `tspId` согласия;
3. `amount` > 0 и ≤ `maxAmountPerCharge`;
4. сумма успешных списаний за текущий период + `amount` ≤ `periodLimit` (месячный лимит);
5. текущая дата в пределах `startDate`…`endDate`;
6. нет успешного списания с тем же (`subscriptionId`, `billingPeriod`).

Окончательный контроль — за банком плательщика/ОПКЦ: guard шлюза снижает число отказов, но не заменяет авторитет плательщика. Отказ на стороне банка → D4, а не ошибка ядра.
```

New §4 (rename "Guard допуска списания"):
- add ownership explicitly (AD-016)
- item 4: успешных и незавершённых
- item 6: нет незавершённой или успешной попытки
- add paragraph: единственный владелец учёта лимитов — шлюз (AD-009); лимиты берутся из подтверждённых ОПКЦ (C4/C11); guard и создание попытки — одна транзакция; ТСП не является владельцем учёта.

§5:
```
## 5. Идемпотентность (AD-003, AD-011)

| Триггер | Ключ | Поведение при повторе |
|---|---|---|
| `POST /v1/subscriptions` | `Idempotency-Key` | возврат того же `subscriptionId`, состояние не меняется |
| `POST /v1/subscriptions/{id}/charges` | `Idempotency-Key` = `chargeId` + `billingPeriod` | успешная попытка за период уже есть → возврат существующего `chargeId` (200), новое списание не создаётся |
| Событие ОПКЦ (согласие/списание) | `eventId` | обработанный `eventId` игнорируется; новый `eventId` по завершённому переходу → алерт, состояние не меняется |
| Подтверждение АБС | `paymentId` | повтор не создаёт вторую проводку (маппинг `paymentId → absDocId`) |

Гонка «планировщик ТСП + ручное списание» разрешается уникальностью (`subscriptionId`, `billingPeriod`) на уровне БД: проигравшая попытка получает существующий ресурс или `409 CHARGE_ALREADY_EXISTS`.
```

New §5 with precedence + attempt-creation uniqueness + period format table.

§7 first bullet:
"- Наружу выставляется статус согласия (...) и статус списания (те же значения платежа: `INITIATED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`)."
→ remove INITIATED: "(канонические значения платежа: `CREATED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `REFUNDED`; `QR_ISSUED`/`EXPIRED` для списаний недостижимы)."

§8 open questions: add authority + resume.

Let me apply edits.

  `edit(file_path="/home/architect/project/docs/spec/consent-state-machine.md", new_string="## 5. Идемпотентность и ключи (AD-003, AD-011)\n\nПриоритет ключей: (`subscriptionId`, `billingPeriod`) определяет период; `chargeId`/`Idem, old_string="## 5. Идемпотентность (AD-003, AD-011)\n\n| Триггер | Ключ | Поведение при повторе |\n|---|---|---|\n| `POST /v1/subscriptions` | `Idempote)`
  `edit(file_path="/home/architect/project/docs/spec/consent-state-machine.md", new_string="- Наружу выставляется статус согласия (`CREATED`, `PENDING_PAYER`, `ACTIVE`, `SUSPENDED`, `REVOKED`, `EXPIRED`, `DECLINED`) и статус списан, old_string="- Наружу выставляется статус согласия (`CREATED`, `PENDING_PAYER`, `ACTIVE`, `SUSPENDED`, `REVOKED`, `EXPIRED`, `DECLINED`) и статус списан)`

Now §5 rewrite, §7 bullet fix, §8 additions.

§5 old text (as written):
```
## 5. Идемпотентность (AD-003, AD-011)

| Триггер | Ключ | Поведение при повторе |
|---|---|---|
| `POST /v1/subscriptions` | `Idempotency-Key` | возврат того же `subscriptionId`, состояние не меняется |
| `POST /v1/subscriptions/{id}/charges` | `Idempotency-Key` = `chargeId` + `billingPeriod` | успешная попытка за период уже есть → возврат существующего `chargeId` (200), новое списание не создаётся |
| Событие ОПКЦ (согласие/списание) | `eventId` | обработанный `eventId` игнорируется; новый `eventId` по завершённому переходу → алерт, состояние не меняется |
| Подтверждение АБС | `paymentId` | повтор не создаёт вторую проводку (маппинг `paymentId → absDocId`) |

Гонка «планировщик ТСП + ручное списание» разрешается уникальностью (`subscriptionId`, `billingPeriod`) на уровне БД: проигравшая попытка получает существующий ресурс или `409 CHARGE_ALREADY_EXISTS`.
```

New §5:
```
## 5. Идемпотентность и ключи (AD-003, AD-011)

Приоритет ключей: (`subscriptionId`, `billingPeriod`) определяет период; `chargeId`/`Idempotency-Key` — идемпотентность запроса. Заголовок `Idempotency-Key` обязан совпадать с `chargeId`.

| Триггер | Ключ | Поведение при повторе |
|---|---|---|
| `POST /v1/subscriptions` | `Idempotency-Key` | возврат того же `subscriptionId`; при том же ключе и другом теле — `409 IDEMPOTENCY_CONFLICT` |
| `POST /v1/subscriptions/{id}/charges` | `chargeId` (= `Idempotency-Key`) и (`subscriptionId`, `billingPeriod`) | тот же `chargeId` → возврат существующего ресурса; тот же период при незавершённой/успешной попытке → существующий ресурс (200) или `409 CHARGE_ALREADY_EXISTS`; новый вызов в ОПКЦ не выполняется |
| Событие ОПКЦ (согласие/списание) | `eventId` | обработанный `eventId` игнорируется; новый `eventId` по завершённому переходу → алерт, состояние не меняется |
| Подтверждение АБС | `paymentId` | повтор не создаёт вторую проводку (маппинг `paymentId → absDocId`) |

**Формат периода (`billingPeriod`, UTC):** `MONTH` → `YYYY-MM`, `DAY` → `YYYY-MM-DD`, `WEEK` → `YYYY-Www` (ISO-неделя). Период задаёт ТСП, шлюз валидирует соответствие `period`.

Гонка «планировщик ТСП + ручное списание» разрешается частичным уникальным ограничением БД **в момент создания попытки**: не более одной незавершённой и не более одной успешной попытки на (`subscriptionId`, `billingPeriod`); проигравшая попытка получает существующий ресурс или `409 CHARGE_ALREADY_EXISTS`.
```

§7 first bullet old:
"- Наружу выставляется статус согласия (`CREATED`, `PENDING_PAYER`, `ACTIVE`, `SUSPENDED`, `REVOKED`, `EXPIRED`, `DECLINED`) и статус списания (те же значения платежа: `INITIATED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`)."
New:
"- Наружу выставляется статус согласия (`CREATED`, `PENDING_PAYER`, `ACTIVE`, `SUSPENDED`, `REVOKED`, `EXPIRED`, `DECLINED`) и статус списания — канонические значения платежа (`CREATED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `REFUNDED`); `QR_ISSUED`/`EXPIRED` для списаний недостижимы, отдельного `INITIATED` наружу нет."

§8 add items 6-7:
6. Точка авторитета по согласию: локальный реестр шлюза vs банк плательщика/ОПКЦ (`[ТРЕБУЕТ ПРОВЕРКИ]`); влияет на AD-009 и объём сверки.
7. Возобновление подписки после отключения: новое согласие или восстановление прежнего `[ТРЕБУЕТ ПРОВЕРКИ]`.
8. Требования к уведомлению плательщика о предстоящем списании (влияет на контракт ТСП и NFR) `[ТРЕБУЕТ ПРОВЕРКИ]`.

Let me apply.

  `edit(file_path="/home/architect/project/docs/spec/consent-state-machine.md", new_string="| C6 | `ACTIVE` | `REVOKED` | отзыв плательщиком (событие ОПКЦ или сверка) | — | немедленно блокировать **допуск** новых списаний; уже заре, old_string="| C6 | `ACTIVE` | `REVOKED` | отзыв плательщиком (событие ОПКЦ или сверка) | — | **немедленно блокировать новые списания**, закрыть незавер)`
  `edit(file_path="/home/architect/project/docs/spec/consent-state-machine.md", new_string="4. Требования к хранению доказательств согласия (срок, состав) — юристы/ИБ банка.\n5. Допустимость частичного списания по согласию (сумма м, old_string="4. Требования к хранению доказательств согласия (срок, состав) — юристы/ИБ банка.\n5. Допустимость частичного списания по согласию (сумма м)`

Now §8 add items. Current §8:
```
## 8. Открытые вопросы (A1, внешние входы)

1. Точная схема согласия в протоколе НСПК: обязательные поля, лимиты, единица периода, максимальный срок, кто хранит доказательство согласия `[ТРЕБУЕТ ПРОВЕРКИ]`.
2. Наличие и требования НСПК к уведомлению плательщика о предстоящем списании (влияет на то, кто и как уведомляет) `[ТРЕБУЕТ ПРОВЕРКИ]`.
3. Числовые лимиты по умолчанию и допустимые диапазоны (влияют на guard §4 и NFR) `[ТРЕБУЕТ ПРОВЕРКИ]`.
4. Требования к хранению доказательств согласия (срок, состав) — юристы/ИБ банка.
5. Допустимость частичного списания по согласию (сумма меньше ожидаемой) — бизнес + НСПК.
```

Add items 6-8.

Then update §2.2 C6 line about "закрыть незавершённые попытки по политике" — reviewer ADV-01 said it conflicts with the new rule. C6 currently: "**немедленно блокировать новые списания**, закрыть незавершённые попытки по политике, outbox, вебхук `subscription.revoked`". This contradicts "не помечается локально FAILED". Let me fix C6 to: "немедленно блокировать допуск новых списаний; уже зарегистрированные в ОПКЦ списания доводятся до терминального статуса (не помечаются локально `FAILED`); outbox, вебхук".

Let me edit C6 and §8.

  `grep_search(pattern="деeplink|деeplink|INITIATED", path="/home/architect/project")`

There's still a "деeplink" typo in C2 of the FSM. Let me fix that.

Then update tsp-api.md §6 (INITIATED→CREATED, 404, error codes, example, deeplink typo), openapi (Charge.status canonical, 404s, 409 IDEMPOTENCY_CONFLICT, errorCode fields), and the package/ADR/nfr/memlog.

Let me fix the FSM typo first and then move to tsp-api.

FSM C2: "ответ адаптера ОПКЦ: получена ссылка/деeplink подтверждения" and "сохранить `consentUrl`/`deeplink`". Only the first has the mixed-alphabet typo.

Let me grep for "деeplink" across repo to fix all.

  `edit(file_path="/home/architect/project/docs/spec/consent-state-machine.md", new_string="deeplink", old_string="деeplink")`
  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="deeplink", old_string="деeplink")`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="deeplink", old_string="деeplink")`

Now fix remaining INITIATED references in normative artifacts: nfr.md line 71, ADR-008 line 40, tsp-api.md lines 186/214/267, openapi lines 93/224, CHANGE-PACKAGE lines 45/88/139/154/159, FSM line 27/41 (typo). The review files are gate artifacts — leave them as evidence.

Also I should add a TTL for non-terminal attempts (adversarial ADV-04 point (г) and 24h window). Good catch: add to AD-011 or FSM: "у незавершённой попытки есть предельный срок; по истечении...". I'll add to FSM §5 and reference it in AD-011? AD-011 is already long. Add to FSM §5 note and mention "TTL незавершённой попытки — конфигурируемый, [ТРЕБУЕТ ПРОВЕРКИ] регламент НСПК". Good enough; the invariant-level rule is attempt uniqueness which already closes the race regardless of TTL. I'll add the TTL note to FSM.

Also adversarial suggested Charge.status could express REFUNDED — my new §7 says canonical values incl. REFUNDED. So openapi Charge.status enum should be canonical: [CREATED, PAID, CREDITED, COMPLETED, FAILED, REFUNDED]. Let me update openapi Charge.status and its 201 description.

Let me batch the edits now.

1. FSM typo C2 + §1 table typo line 27.
2. nfr line 71.
3. ADR-008 line 40.
4. tsp-api lines 186, 214, 267 (+ add 404 & codes & example subscriptionId).
5. openapi 93, 224, consentUrl typo, add 404s, 409 IDEMPOTENCY_CONFLICT, errorCode fields.
6. CHANGE-PACKAGE fixes.

Let me do them one by one.

FSM edits:
- line 27: `| `PENDING_PAYER` | Ссылка/деeplink выданы, ожидается подтверждение плательщика в приложении его банка | да |` → "Ссылка/deeplink выдана, ожидается подтверждение плательщика в приложении его банка"
- line 41 C2: "получена ссылка/деeplink подтверждения" → "получена ссылка/deeplink подтверждения"

Let me use replace_all for "деeplink" → "deeplink" via edit with replace_all on the FSM file? The edit tool replace_all replaces all occurrences of old_string. I can replace_all "деeplink" with "deeplink" in consent-state-machine.md — but "деeplink" appears twice there. Also tsp-api.md has one, openapi has one (with different prefix "Ссылка/деeplink"). Let me do replace_all per file for the exact substring "деeplink".

Let me do that for FSM, tsp-api.md, openapi/tsp-api.yaml, and spine (AD-013 already fixed to deeplink; the spine had "деeplink" only once and I replaced it). Let me check spine for remaining "деeplink" — my AD-013 replacement used "ссылку/deeplink" so it's fixed. AD-013 also had "не конструирует" etc. Fine.

Let me run replace_all edits.

  `edit(file_path="/home/architect/project/docs/nfr.md", new_string="| Завершение списания (`CREATED` → `PAID`) от подтверждения банка плательщика | p95 < 30 с (уточняется регламентом НСПК) | Метрика процесса, old_string="| Завершение списания (`INITIATED` → `PAID`) от подтверждения банка плательщика | p95 < 30 с (уточняется регламентом НСПК) | Метрика процес)`
  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="2. **Рекуррентное списание — платёж с `operationType = CONSENT`** в канонической статусной машине ADR-002: `CREATED → PAID → CREDITED → COM, old_string="2. **Рекуррентное списание — платёж с `operationType = CONSENT`** и последовательностью `INITIATED → PAID → CREDITED → COMPLETED`; состояни)`
  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="- Списание (`status`, платёж типа `CONSENT`): канонические значения `Payment.status` — `CREATED | PAID | CREDITED | COMPLETED | FAILED | RE, old_string="- Списание (`status`, платёж типа `CONSENT`): `INITIATED | PAID | CREDITED | COMPLETED | FAILED`.")`
  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="  \"status\": \"CREATED\"", old_string="  \"status\": \"INITIATED\"")`

Now the other INITIATED references. Let me fix:

1. nfr.md line 71: "| Завершение списания (`INITIATED` → `PAID`) от подтверждения банка плательщика |" → "(`CREATED` → `PAID`)".
2. ADR-008 line 40: "последовательностью `INITIATED → PAID → CREDITED → COMPLETED`" → "`CREATED → PAID → CREDITED → COMPLETED` в канонической машине ADR-002 (без `QR_ISSUED`)".
3. tsp-api.md line 186: "- Списание (`status`, платёж типа `CONSENT`): `INITIATED | PAID | CREDITED | COMPLETED | FAILED`." → canonical: "`CREATED | PAID | CREDITED | COMPLETED | FAILED | REFUNDED` (канонические значения `Payment.status`; `QR_ISSUED`/`EXPIRED` недостижимы)".
4. tsp-api.md line 267: `"status": "INITIATED"` → `"status": "CREATED"`.
5. openapi line 93: "description: Списание создано (статус INITIATED)" → "(статус CREATED)".
6. openapi line 224: enum → canonical.
7. CHANGE-PACKAGE lines 45, 88, 139, 154, 159.

Also add 404/error coverage and Idempotency-Key=chargeId to tsp-api §6.4, and 409 IDEMPOTENCY_CONFLICT in openapi /charges.

And add TTL note in FSM §5.

Let me batch these edits.

First nfr, ADR, tsp-api, openapi simple replacements.

For openapi enum: 
```
        status:
          type: string
          enum: [INITIATED, PAID, CREDITED, COMPLETED, FAILED]
```
→
```
        status:
          type: string
          description: Канонические значения Payment.status; QR_ISSUED/EXPIRED недостижимы
          enum: [CREATED, PAID, CREDITED, COMPLETED, FAILED, REFUNDED]
```
But there are two `status:` blocks with enums (Payment has 8 values; Charge has 5). The old_string with the 5-value enum is unique. Good.

Let me also add `errorCode` to Charge and Subscription? The contract reviewer flagged missing decline reason. Let me add `failureCode` already on Charge; rename to `errorCode`? There's `failureCode` on Charge. For Subscription add `errorCode` (nullable) describing decline reason. Let me add.

Also 404 responses on subscription GET/suspend/resume/close, and add 422 for resume/close of terminal. Let me add minimal 404 to each (4 paths) and 409 to resume/close (terminal). To limit churn, I'll add '404' to GET, suspend, resume, close; and '409' to resume (SUBSCRIPTION_NOT_ACTIVE / SUBSCRIPTION_REVOKED) and close.

Hmm, adding error responses to each path is verbose. I'll add 404 to the 4 and a 409 to resume/close. And add `IDEMPOTENCY_CONFLICT` to /charges 409 description (already "CHARGE_ALREADY_EXISTS | CHARGE_CONFLICT") → add IDEMPOTENCY_CONFLICT.

Let me implement. I'll do several edits.

Let me start with the simple replacements.

  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="1. **Согласие плательщика — отдельная сущность** с собственным `subscriptionId` и статусной машиной (`CREATED → PENDING_PAYER → ACTIVE → RE, old_string="1. **Согласие плательщика — отдельная сущность** с собственным `subscriptionId` и статусной машиной (`CREATED → PENDING_PAYER → ACTIVE → RE)`

Now fix ADR-008 item 1 (consent source of truth wording), item 4 (chargeId key), item 6 (deeplink typo + link from ОПКЦ), and add decisions for evidence/AML/authz, plus the law facts, "по сервисам" softening.

Also tsp-api §6.4 rules line "статус списания читается существующим GET /v1/payments/{paymentId}" — add mapping note; add Idempotency-Key==chargeId; add attempt uniqueness; 404s; codes.

Let me do ADR-008 edits:
- item 1: "Источник истины — БД шлюза; статус в ОПКЦ сверяется." → "Локальный реестр — источник истины для операций шлюза; авторитет по согласию — банк плательщика/ОПКЦ (точка авторитета `[ТРЕБУЕТ ПРОВЕРКИ]`). Смена статуса, outbox и аудит — одна транзакция."
- item 4: "`chargeId` (совместим с `Idempotency-Key`)" → "`chargeId` (= `Idempotency-Key`)"; add attempt-level uniqueness.
- item 6: "ссылку/деeplink" → "ссылку/deeplink, полученную от ОПКЦ (не формирует её сам)".
- Add items 9,10,11 for AD-014/015/016.

Also Context: fix law statement. Current context bullets:
"- НСПК развивает сервис «Подписка СБП»: ..."
"- Регулирование подписок усиливается: поправки в Закон РФ «О защите прав потребителей» (явное согласие на автосписания, упрощённый отказ, блокировка реквизитов) вступают в силу с 01.09.2025 — согласие плательщика и его отзыв должны быть юридически доказуемы."
"- Подключение к СБП — по сервисам, с доработкой ПО ..."

Fix bullet 2: "Федеральный закон от 15.10.2025 № 376-ФЗ внёс изменение в ст. 16.1 Закона РФ «О защите прав потребителей» (запрет автосписаний без явного согласия и др.), вступает в силу с 01.03.2026 — согласие плательщика и его отзыв должны быть юридически доказуемы."
Fix bullet 3: remove "по сервисам".

And References: the robokassa link is a draft-era article. Replace with consultant.ru link + note. Keep robokassa removed. Let me update references.

Also add open questions section to ADR-008? It has none; the CHANGE-PACKAGE has. Add a short "Открытые вопросы" to ADR-008 for completeness (authority, resume, notification, limits).

Let me apply ADR-008 edits.

Then CHANGE-PACKAGE fixes (INITIATED, лаw, add new ADs/ACs, §7 open items, §9).

Then openapi 404/409/errorCode.

Then nfr add audit/AML rows.

Then memlog append.

Let me do ADR edits now.

  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="8. **Откат — «сворачивание», а не выключение**: stop-new (запрет новых согласий и новых периодов), обработка действующих согласий до отзыва, old_string="8. **Откат — «сворачивание», а не выключение**: stop-new (запрет новых согласий и новых периодов), обработка действующих согласий до отзыва)`
  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="- Регулирование подписок: **Федеральный закон от 15.10.2025 № 376-ФЗ** внёс изменение в ст. 16.1 Закона РФ «О защите прав потребителей» (за, old_string="- Регулирование подписок усиливается: поправки в Закон РФ «О защите прав потребителей» (явное согласие на автосписания, упрощённый отказ, б)`

Now add items 9-11 to ADR-008 decision, fix the law facts, soften "по сервисам", update references, add open questions.

Let me edit item 8's following "## Alternatives Considered" to insert items 9-11 before it.

Current:
```
8. **Откат — «сворачивание», а не выключение**: ...

## Alternatives Considered
```
Insert 9-11 after 8.

Then context fixes and references.

Let me do it.

  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="## Открытые вопросы (A6/A1, внешние входы)\n\n1. Точка авторитета по согласию: локальный реестр шлюза vs банк плательщика/ОПКЦ (кто источни, old_string="## References\n\n- НСПК, «Подписка СБП — что это, как подключить и отключить» — https://sbp.nspk.ru/blog/podpiska-sbp-cto-eto (проверено 20)`
  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="- Федеральный закон от 15.10.2025 № 376-ФЗ «О внесении изменения в статью 16.1 Закона РФ „О защите прав потребителей“», в силе с 01.03.2026, old_string="- Закон РФ «О защите прав потребителей», поправки о явном согласии на автосписания и упрощённом отказе (в силе с 01.09.2025) — обзор: https)`
  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="| **Реестр согласий в шлюзе (выбран)**, ОПКЦ — внешний авторитет, сверка двухсторонняя | Локальный источник истины для операций шлюза: RPO=, old_string="| **Реестр согласий в шлюзе (выбран)**, ОПКЦ — авторитет по отзыву, сверка двухсторонняя | RPO=0, локальный аудит и лимиты, устойчивость к )`

Now update ADR-008 alternatives A row (source of truth wording) — the "реестр согласий в шлюзе (выбран)" description says "RPO=0, локальный аудит и лимиты, ... единый источник истины как у платежа". That's fine-ish but should note external authority. Let me adjust the chosen row's plus to "локальный источник истины для операций шлюза (RPO=0, аудит, лимиты), внешний авторитет — ОПКЦ; сверка". And the "только ОПКЦ" minus says "Нарушает модель AD-002 (нет локального источника истины)". Fine.

Also update references: replace robokassa with consultant.ru and note corrected date. Current references:
"- НСПК, «Подписка СБП — что это, как подключить и отключить» — https://sbp.nspk.ru/blog/podpiska-sbp-cto-eto (проверено 2026-09-29)
- Закон РФ «О защите прав потребителей», поправки о явном согласии на автосписания и упрощённом отказе (в силе с 01.09.2025) — обзор: https://robokassa.com/... (проверено 2026-09-29)
- ЦБ РФ, порядок подключения к СБП (доработка ПО по документации НСПК и тестовые испытания — по сервисам) — https://www.cbr.ru/... (проверено 2026-09-29)
..."
Replace the 2nd and 3rd lines.

Also add open questions section before References.

Let me edit references + add open questions.

Find anchor: "## References\n\n- НСПК, «Подписка СБП..." insert "## Открытые вопросы (A6/A1)" before it.

Let me do two edits: alternatives row; references block; open questions insert.

Actually combine references + open questions in one edit by replacing "## References\n\n- НСПК, ... (проверено 2026-09-29)\n- Закон РФ ... (проверено 2026-09-29)\n- ЦБ РФ, ... (проверено 2026-09-29)\n" with open questions + corrected references.

Let me construct carefully. I have the references block text from the file (read earlier, with the correction to §6–§7). Current references:

```
## References

- НСПК, «Подписка СБП — что это, как подключить и отключить» — https://sbp.nspk.ru/blog/podpiska-sbp-cto-eto (проверено 2026-09-29)
- Закон РФ «О защите прав потребителей», поправки о явном согласии на автосписания и упрощённом отказе (в силе с 01.09.2025) — обзор: https://robokassa.com/blog/news/v-rossii-zapretyat-avtomaticheskoe-spisanie-sredstv-za-onlayn-podpiski-bez-soglasiya-polzovateley/ (проверено 2026-09-29)
- ЦБ РФ, порядок подключения к СБП (доработка ПО по документации НСПК и тестовые испытания — по сервисам) — https://www.cbr.ru/PSystem/payment_system/actions/ (проверено 2026-09-29)
- AD-009…AD-013 (spine, Proposed) — инварианты изменения CS-001
- ADR-002 ...
```

Let me replace the first three bullets and add open questions before References. I'll do one edit replacing "## References\n\n- НСПК..." through the AD bullet line, and another for alternatives. Actually simpler: edit the three bullets, and separately insert open questions before "## References".

Let me do:
Edit A: replace "## References\n\n- НСПК, «Подписка СБП" with "## Открытые вопросы (A6/A1)\n\n1. ...\n2. ...\n3. ...\n4. ...\n\n## References\n\n- НСПК, «Подписка СБП".
Edit B: replace the law + cbr bullets.
Edit C: alternatives row.

Let me do them.

  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        '201':\n          description: Списание создано (статус CREATED)", old_string="        '201':\n          description: Списание создано (статус INITIATED)")`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        '409':\n          description: \"IDEMPOTENCY_CONFLICT | CHARGE_ALREADY_EXISTS | CHARGE_CONFLICT\"", old_string="        '409':\n          description: \"CHARGE_ALREADY_EXISTS | CHARGE_CONFLICT\"")`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        status:\n          type: string\n          description: Канонические значения Payment.status; QR_ISSUED/EXPIRED для списаний недост, old_string="        status:\n          type: string\n          enum: [INITIATED, PAID, CREDITED, COMPLETED, FAILED]\n        failureCode: {type: string)`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        consentUrl: {type: string, description: Ссылка/deeplink на подтверждение в приложении банка плательщика}\n        createdAt: {type:, old_string="        consentUrl: {type: string, description: Ссылка/deeplink на подтверждение в приложении банка плательщика}\n        createdAt: {type:)`

Good. Now update openapi: Charge.status enum canonical, 201 description, add errorCode to Charge/Subscription, add 404 to subscription paths, add IDEMPOTENCY_CONFLICT to /charges 409.

Let me do these edits.

1. `description: Списание создано (статус INITIATED)` → `description: Списание создано (статус CREATED)`
2. Charge.status enum.
3. /charges 409 description add IDEMPOTENCY_CONFLICT.
4. Add 404 to GET/suspend/resume/close.
5. Add `errorCode` to Charge (nullable) — it has `failureCode`; rename to `errorCode` for consistency with the problem/FSM? The contract reviewer said three names for one failure code (`failureCode`/`errorCode`). Let me standardize on `errorCode`. So in Charge schema rename `failureCode` → `errorCode`. And add `errorCode` to Subscription (decline reason). And in the Subscription example in tsp-api add `errorCode`.

Let me apply openapi edits.

For 404 additions, I'll add after the '200' block on getSubscription, suspend, resume, close. Each has:
```
      responses:
        '200':
          description: ...
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Subscription'}
```
followed by either another path or end. Adding '404' after '200' for each — but the four are similar; editing each requires unique context. I can use the path's operationId as context.

Alternatively add a single `components/responses/NotFound` and reference. That'd be cleaner: add `responses:` section under components:
```
components:
  responses:
    NotFound:
      description: Согласие/платёж не найден или недоступен вызывающему ТСП
      content:
        application/json:
          schema: {$ref: '#/components/schemas/Problem'}
```
and add `'404': {$ref: '#/components/responses/NotFound'}` to the 4 paths. And for resume/close add '409' with a Problem.

That's still 4-6 edits. Let me do them.

Actually simpler: for each of the 4 responses blocks, replace:
```
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Subscription'}
```
with the same plus a `'404'` entry. But that exact string appears 6 times (createSubscription 201, getSubscription 200, suspend 200, resume 200, close 200) → replace_all would add 404 to all, including createSubscription (where 404 doesn't make sense). Hmm.

Let me instead add via unique context using description lines:
- getSubscription: `description: Согласие и история списаний`
- suspend: `description: Согласие приостановлено`
- resume: `description: Согласие возобновлено`
- close: `description: Согласие отозвано (REVOKED)`

I'll edit each with a 3-line context. Let me do 4 edits. Plus the responses component.

Actually — is adding 404 essential? The contract reviewer marked it "major". Yes, worth adding for correctness. But I can be efficient: define the NotFound response component once and add to the 4.

Let me first add the component response.

Note: `components` currently has only `schemas:`. I'll add `responses:` before `schemas:`.

Let me implement.
Now the OpenAPI hygiene fixes (canonical status enum, 404s, conflict codes, error field).

  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="components:\n  responses:\n    NotFound:\n      description: Объект не найден или недоступен вызывающему ТСП (объектная авторизация, AD-016, old_string="components:\n  schemas:\n    PaymentRequest:")`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        '200':\n          description: Согласие и история списаний\n          content:\n            application/json:\n              schema, old_string="        '200':\n          description: Согласие и история списаний\n          content:\n            application/json:\n              schema)`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        '200':\n          description: Согласие приостановлено\n          content:\n            application/json:\n              schema: {$, old_string="        '200':\n          description: Согласие приостановлено\n          content:\n            application/json:\n              schema: {$)`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        '200':\n          description: Согласие возобновлено\n          content:\n            application/json:\n              schema: {$re, old_string="        '200':\n          description: Согласие возобновлено\n          content:\n            application/json:\n              schema: {$re)`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        '200':\n          description: Согласие отозвано (REVOKED)\n          content:\n            application/json:\n              schema, old_string="        '200':\n          description: Согласие отозвано (REVOKED)\n          content:\n            application/json:\n              schema)`

Now add 404 responses. Add a `components.responses.NotFound` and reference it in the 4 paths. Let me add the responses component before `schemas:`.

Current:
```
components:
  schemas:
    PaymentRequest:
```
→
```
components:
  responses:
    NotFound:
      description: Объект не найден или недоступен вызывающему ТСП
      content:
        application/json:
          schema: {$ref: '#/components/schemas/Problem'}
  schemas:
    PaymentRequest:
```

Then add `'404': {$ref: '#/components/responses/NotFound'}` to getSubscription, suspend, resume, close responses.

For getSubscription:
```
      responses:
        '200':
          description: Согласие и история списаний
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Subscription'}
  /v1/subscriptions/{subscriptionId}/charges:
```
Add '404' after the 200 block, before the next path. Let me edit with context.

Similarly for suspend/resume/close with their descriptions.

Let me do 5 edits (component + 4).

Also add a '409' for resume/close of terminal consent. Let me add for resume: description "SUBSCRIPTION_REVOKED | SUBSCRIPTION_EXPIRED" and close: "SUBSCRIPTION_ALREADY_TERMINAL"? Hmm, introducing new codes not documented in tsp-api §6.8. Let me instead document in tsp-api §6.8 that terminal transition requests return 409 `SUBSCRIPTION_NOT_ACTIVE`/`SUBSCRIPTION_EXPIRED`. I'll add to §6.8: "SUBSCRIPTION_ALREADY_TERMINAL (409) — возобновление/закрытие терминального согласия". And add '409' to resume/close in openapi with that code. That's 2 more edits.

Let me keep it focused: add 404s + the terminal 409.

Let me apply.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="  \"charges\": [\n    { \"chargeId\": \"chg_1a2b3c\", \"subscriptionId\": \"sub_4c7d2e91\", \"billingPeriod\": \"2026-10\", \"amount\": 499, old_string="  \"charges\": [\n    { \"chargeId\": \"chg_1a2b3c\", \"billingPeriod\": \"2026-10\", \"amount\": 49900, \"status\": \"COMPLETED\" }\n  ]\n)`
  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="Правила: списание возможно только при `ACTIVE` согласии и в пределах лимитов (иначе `422`, без вызова ОПКЦ); значение заголовка `Idempotenc, old_string="Правила: списание возможно только при `ACTIVE` согласии и в пределах лимитов (иначе `422`, без вызова ОПКЦ); на один `billingPeriod` успешн)`
  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="Отзыв **плательщиком** выполняется в приложении его банка и приходит шлюзу событием/сверкой; ТСП извещается вебхуком (6.7). Отзыв не отменя, old_string="Отзыв **плательщиком** выполняется в приложении его банка и приходит шлюзу событием/сверкой; ТСП извещается вебхуком (6.7). Отзыв не отменя)`
  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="- `CHARGE_ALREADY_EXISTS` (409) — успешное или незавершённое списание за период уже есть\n- `CHARGE_CONFLICT` (409) — конфликт `chargeId`/`, old_string="- `CHARGE_ALREADY_EXISTS` (409) — успешное списание за период уже есть\n- `CHARGE_CONFLICT` (409) — конфликт `chargeId`/`billingPeriod` с д)`

Now update tsp-api.md §6.4/§6.5/§6.8 to reflect: attempt uniqueness, Idempotency-Key=chargeId, 404, SUBSCRIPTION_ALREADY_TERMINAL, and mapping (charge status = Payment.status). Also add `errorCode` to the Subscription example and charges[] example subscriptionId fix.

Let me look at current §6.3 example charges[]: `{ "chargeId": "chg_1a2b3c", "billingPeriod": "2026-10", "amount": 49900, "status": "COMPLETED" }` — missing subscriptionId. Add it.

§6.4 rules line: "Правила: списание возможно только при `ACTIVE` согласии и в пределах лимитов (иначе `422`, без вызова ОПКЦ); на один `billingPeriod` успешное списание — одно; статус списания читается существующим `GET /v1/payments/{paymentId}`." → extend with: Idempotency-Key=chargeId; attempt uniqueness (одна незавершённая и одна успешная на период); status canonical; 409 codes.

§6.5: add 404 + terminal 409.
§6.8: add SUBSCRIPTION_ALREADY_TERMINAL (409).

Let me edit.

  `edit(file_path="/home/architect/project/docs/nfr.md", new_string="| Доля успешных списаний (бизнес-метрика, не SLO шлюза) | baseline ≥ 92 %; отказы — «нет средств»/лимит банка; уточнить с бизнесом | Отчёт , old_string="| Доля успешных списаний (бизнес-метрика, не SLO шлюза) | baseline ≥ 92 %; отказы — «нет средств»/лимит банка; уточнить с бизнесом | Отчёт )`

Now nfr §7 add audit/AML rows, and fix the "Доказательство" gap. Add rows:
- "Аудит переходов согласия и изменений лимитов | 100 % записей, неизменяемо | Аудит, SIEM"
- "Артефакт согласия/отзыва (доказательство) | 100 % переходов ACTIVE/REVOKED | Тест, выборочная проверка"
- "AML-передача согласий и списаний (по порогам/правилам) | 100 % | Тест-кейсы"

Let me add after "Доля успешных списаний" row.

Also nfr §7 header says "числовые лимиты и регламентные сроки НСПК — внешний вход". fine.

Let me edit.

Then CHANGE-PACKAGE updates (INITIATED → CREATED; law; AD list; ACs; §4 charge status; §7 open items; §9).

Then memlog append.

Then re-run lint + re-validate openapi + BC diff.

Then also update README to list new files.

Let me proceed.

  `edit(file_path="/home/architect/project/docs/nfr.md", new_string="- Подписки: юридические требования к доказательству согласия и упрощённому отказу (ФЗ от 15.10.2025 № 376-ФЗ, ст. 16.1 ЗоЗПП, в силе с 01.0, old_string="- Подписки: юридические требования к доказательству согласия и упрощённому отказу (ЗоЗПП, в силе с 01.09.2025) — юристы/ИБ банка.")`
  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| Регуляторика / юридическая значимость / ПДн | 3 | Согласие плательщика — юридически значимый отзываемый документ; ФЗ от 15.10.2025 № 376-, old_string="| Регуляторика / юридическая значимость / ПДн | 3 | Согласие плательщика — юридически значимый отзываемый документ; ЗоЗПП (явное согласие, )`
  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| AD-005 зачисление только из `PAID` | Формально да, по сути нет | У типа `CONSENT` свой вход в `PAID` (`CREATED → PAID`, без `QR_ISSUED`),, old_string="| AD-005 зачисление только из `PAID` | Формально да, по сути нет | У типа `CONSENT` свой вход в `PAID` (`INITIATED → PAID`, без `QR_ISSUED`)`
  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| AD-008 стратегия гибрид `[ADOPTED]` | Да (внешний риск) | Поддержка подписок становится **gate-критерием RFP**; важно зафиксировать до по, old_string="| AD-008 стратегия гибрид `[ADOPTED]` | Да (внешний риск) | Поддержка подписок становится **gate-критерием RFP**; важно зафиксировать до по)`

Also fix nfr dependency line about ЗоЗПП date: "Подписки: юридические требования к доказательству согласия и упрощённому отказу (ЗоЗПП, в силе с 01.09.2025)" → "(ФЗ от 15.10.2025 № 376-ФЗ, в силе с 01.03.2026)".

Let me edit.

Then CHANGE-PACKAGE fixes. Let me enumerate CHANGE-PACKAGE lines to fix:
- line ~45 §2.1 table AD-005 row: "(INITIATED → PAID, без QR_ISSUED)" → "(CREATED → PAID...)"
- line ~45 table also needs rows for AD-014..AD-016? The table lists AD-001..AD-008. Add three rows.
- §1 dimension table law mention: "(ЗоЗПП, явное согласие, упрощённый отказ, в силе с 01.09.2025)" → "(ФЗ от 15.10.2025 № 376-ФЗ, в силе с 01.03.2026)"
- §3.1 table row 2: INITIATED → CREATED
- §3.1 add rows 9-11 for AD-014..016
- §3.3 no change
- §4 table: mention Charge.status canonical mapping
- §5 table: change `INITIATED→PAID` → `CREATED→PAID`
- §6.1 AC-02, AC-07 INITIATED → CREATED; add AC-14 (evidence/audit), AC-15 (AML), AC-16 (IDOR), AC-17 (revocation after dispatch)
- §7 add open questions items: authority, resume semantics, notification; also conditional: item 4 dunning now partially pinned by AD-011.
- §9 fix law fact; add assumption about unknown consent authority; update verification list (re-run).
- §2.4 conflict: mention AD-008/ADR-007 risk already there.

Let me read the CHANGE-PACKAGE file to get exact current strings for edits (it's large; I wrote it, I have the content). Let me do targeted edits.

Let me grep for the specific strings first? I'll just edit with the strings I wrote.

Edit 1: §1 dimension row law.
Current: "| Регуляторика / юридическая значимость / ПДн | 3 | Согласие плательщика — юридически значимый отзываемый документ; ЗоЗПП (явное согласие, упрощённый отказ, в силе с 01.09.2025); 152-ФЗ; требования НПС/КИИ |"
New: "...; ФЗ от 15.10.2025 № 376-ФЗ (ст. 16.1 ЗоЗПП, в силе с 01.03.2026); 152-ФЗ; требования НПС/КИИ |"

Edit 2: §2.1 table AD-005 row.
Current: "| AD-005 зачисление только из `PAID` | Формально да, по сути нет | У типа `CONSENT` свой вход в `PAID` (`INITIATED → PAID`, без `QR_ISSUED`), но зачисление в АБС — только из `PAID`; правило не ослабляется → **AD-010** |"
New: "... (`CREATED → PAID`, без `QR_ISSUED`), ..."

Edit 3: §2.1 add rows after AD-008 row. Current AD-008 row:
"| AD-008 стратегия гибрид `[ADOPTED]` | Да (внешний риск) | Поддержка подписок становится **gate-критерием RFP**; важно зафиксировать до подписания контракта, иначе изменение обойдётся дорого (или станет нереализуемым) |"
Add:
"| AD-009…AD-013 (новые) | — | Добавляются изменением; описаны в §3 |" — hmm redundant. Better add rows for AD-014/015/016:
"| AD-014 доказуемость согласия (новый) | — | Вводится изменением CS-001: артефакт согласия/отзыва + аудит в одной транзакции |"
"| AD-015 ПОД/ФТ контроль согласий (новый) | — | Создание согласия и списания → AML-контур |"
"| AD-016 объектная авторизация подписок (новый) | — | Принадлежность согласия ТСП; непрозрачные ссылки |"

Edit 4: §3.1 row 2 and add rows 9-11.
Current row 2: "| 2 | Рекуррентное списание — платёж `operationType=CONSENT`; последовательность `INITIATED → PAID → CREDITED → COMPLETED`; зачисление только из `PAID` | AD-010 |"
New: "| 2 | Рекуррентное списание — платёж `operationType=CONSENT`; `CREATED → PAID → CREDITED → COMPLETED`; зачисление только из `PAID` | AD-010 |"
Then after row 8 add 9-11.

Current row 8: "| 8 | Откат — сворачивание (stop-new), а не выключение | ADR-008 |"
Add after: 
"| 9 | Доказуемость согласия/отзыва: артефакт + аудит в одной транзакции | AD-014 |"
"| 10 | Согласия и списания → AML/антифрод (скорость, агрегация, пороги) | AD-015 |"
"| 11 | Объектная авторизация подписок и непрозрачные ссылки согласия | AD-016 |"

Edit 5: §4 — add mapping sentence. Current §4 intro table row for tsp-api already; add after the compat table a sentence. Actually §4 "Почему потребители не сломаются" point 1 says Payment.status same enum. Add clarifying: "Статус списания публикуется каноническими значениями Payment.status (внутреннее `INITIATED` наружу не выходит)." Let me append to point 1.

Edit 6: §5 NFR table row: "| Завершение списания `INITIATED→PAID` | p95 < 30 с ... |" → `CREATED→PAID`. Add audit/AML rows? Not necessary (referenced).

Edit 7: §6.1 AC-02 and AC-07.
AC-02: "Списание при `ACTIVE` в пределах лимитов: `INITIATED → PAID → CREDITED → COMPLETED`; зачисление в АБС из `PAID`" → CREATED.
AC-07: "Зачисление недостижимо из `INITIATED` (fitness AD-005/AD-010)" → "из `CREATED`".
Add AC-14..AC-17.

Edit 8: §7 table add open items: authority (already? §7 has 10 items; item 2 is "Владение согласием" — that covers ownership; add resume semantics, notification). Let me add items 11-13.
Also item 4 dunning: update to note AD-011 pins one non-terminal attempt per period; remaining = retry policy ownership.
Current item 4: "| 4 | Бизнес-модель отказов (dunning): кто несёт риск неоплаты, политика ретраев | Финансовая ответственность и UX; не архитектурное решение | минимум ретраев — на стороне ТСП | A2 |"
New: "... | Технически частично закреплено AD-011 (одна незавершённая попытка на период); остаётся ответственность за неоплату | A2 |"

Edit 9: §9 assumptions + law fact + verification.
Current §9 assumptions bullet: "- Публичные факты о «Подписке СБП» (подтверждение в приложении банка плательщика, месячные лимиты, отзыв) и о поправках ЗоЗПП (в силе с 01.09.2025) взяты из открытых источников и не заменяют документацию НСПК."
New: "... и о ФЗ от 15.10.2025 № 376-ФЗ (ст. 16.1 ЗоЗПП, в силе с 01.03.2026) ..."
Add assumption: "- Точка авторитета по согласию (локальный реестр vs банк плательщика) не подтверждена публичными источниками — помечена `[ТРЕБУЕТ ПРОВЕРКИ]`."
Also §9 open questions add: resume semantics; consent authority (already?), notification (already item 3). Let me check §9 open questions currently: 1 NSPK service availability, 2 partial debit, 3 notification. Add: 4 consent authority; 5 resume semantics. Actually §7 now covers authority/resume/notification. §9 can stay but add authority & resume. Let me add.
And update verification bullet to include reviewer gate + corrections.

This is a lot of edits. Let me do them efficiently, batching independent ones.

Let me write them.

  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| 2 | Рекуррентное списание — платёж `operationType=CONSENT` в канонической машине: `CREATED → PAID → CREDITED → COMPLETED`; зачисление тол, old_string="| 2 | Рекуррентное списание — платёж `operationType=CONSENT`; последовательность `INITIATED → PAID → CREDITED → COMPLETED`; зачисление толь)`
  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| 8 | Откат — сворачивание (stop-new), а не выключение | ADR-008 |\n| 9 | Доказуемость согласия/отзыва: артефакт + аудит в одной транзакции, old_string="| 8 | Откат — сворачивание (stop-new), а не выключение | ADR-008 |")`

Now §3.1 rows, §4 point, §5, §6.1 ACs, §7, §9.

Let me edit §3.1 row 2 and add rows 9-11.

Current:
"| 2 | Рекуррентное списание — платёж `operationType=CONSENT`; последовательность `INITIATED → PAID → CREDITED → COMPLETED`; зачисление только из `PAID` | AD-010 |"
and row 8:
"| 8 | Откат — сворачивание (stop-new), а не выключение | ADR-008 |"

Let me edit both.

  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| 1 | Согласие плательщика — отдельная сущность (`subscriptionId`) со своей статусной машиной; локальный реестр — источник истины для опера, old_string="| 1 | Согласие плательщика — отдельная сущность (`subscriptionId`) со своей статусной машиной; источник истины — БД шлюза; статус ОПКЦ свер)`
  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| 4 | Идемпотентность по периоду: `chargeId` (= `Idempotency-Key`) + `billingPeriod`; уникальность (`subscriptionId`, `billingPeriod`) при , old_string="| 4 | Идемпотентность по периоду: `chargeId` + `billingPeriod`; уникальность в БД | AD-011 |")`
  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="1. `Payment.status` — то же перечисление; новые статусы живут на новых сущностях (согласие, списание), а не расширяют существующее. Статус , old_string="1. `Payment.status` — то же перечисление; новые статусы живут на новых сущностях (согласие, списание), а не расширяют существующее.")`
  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| Завершение списания `CREATED→PAID` | p95 < 30 с `[ТРЕБУЕТ ПРОВЕРКИ — регламент НСПК]` |", old_string="| Завершение списания `INITIATED→PAID` | p95 < 30 с `[ТРЕБУЕТ ПРОВЕРКИ — регламент НСПК]` |")`

Fix §3.1 row 1 ("источник истины — БД шлюза; статус ОПКЦ сверяется") and row 4 (unique in BD) to reflect the tightened AD-009/AD-011. Let me update row 1 and row 4.

Row 1: "| 1 | Согласие плательщика — отдельная сущность (`subscriptionId`) со своей статусной машиной; источник истины — БД шлюза; статус ОПКЦ сверяется | AD-009 |"
→ "...; локальный реестр — источник истины для операций шлюза, авторитет — банк плательщика/ОПКЦ (сверка) | AD-009 |"

Row 4: "| 4 | Идемпотентность по периоду: `chargeId` + `billingPeriod`; уникальность в БД | AD-011 |"
→ "...; уникальность (subscriptionId, billingPeriod) при создании попытки | AD-011 |"

Then §4 point 1 addition; §5 row; §6.1 ACs; §7 items; §9.

Let me do them.

  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| AC-02 | Списание при `ACTIVE` в пределах лимитов: `CREATED → PAID → CREDITED → COMPLETED`; зачисление в АБС из `PAID` |", old_string="| AC-02 | Списание при `ACTIVE` в пределах лимитов: `INITIATED → PAID → CREDITED → COMPLETED`; зачисление в АБС из `PAID` |")`
  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| AC-07 (нег.) | Зачисление недостижимо из `CREATED` (fitness AD-005/AD-010) |", old_string="| AC-07 (нег.) | Зачисление недостижимо из `INITIATED` (fitness AD-005/AD-010) |")`
  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| AC-13 | Юридический критерий: доказательство согласия и отзыв хранятся в требуемом составе/сроке (заключение юристов) |\n| AC-14 | Доказу, old_string="| AC-13 | Юридический критерий: доказательство согласия и отзыв хранятся в требуемом составе/сроке (заключение юристов) |")`
  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| 4 | Бизнес-модель отказов (dunning): кто несёт риск неоплаты, политика ретраев | Финансовая ответственность и UX; технически частично зак, old_string="| 4 | Бизнес-модель отказов (dunning): кто несёт риск неоплаты, политика ретраев | Финансовая ответственность и UX; не архитектурное решени)`

The 2nd edit for row 4 got applied after the 1st — output shows row 4 still "уникальность в БД" in the first output (line 94) but the second output (lines 89-97) shows row 4 updated. So it's fine (the outputs were from sequential edits; the last shows updated). Good.

Now §6.1 ACs and §7 and §9.

AC-02 current: "| AC-02 | Списание при `ACTIVE` в пределах лимитов: `INITIATED → PAID → CREDITED → COMPLETED`; зачисление в АБС из `PAID` |"
AC-07 current: "| AC-07 (нег.) | Зачисление недостижимо из `INITIATED` (fitness AD-005/AD-010) |"
And add AC-14..AC-17 after AC-13.

AC-13 current last: "| AC-13 | Юридический критерий: доказательство согласия и отзыв хранятся в требуемом составе/сроке (заключение юристов) |"

Add:
| AC-14 | Доказуемость: переходы `ACTIVE`/`REVOKED` и изменение лимитов сохранены артефактом и в неизменяемом аудит-логе (AD-014) |
| AC-15 (нег.) | AML: создание согласия и списание переданы в AML/антифрод; отказ guard (D2) — как сигнал мониторинга (AD-015) |
| AC-16 (нег.) | IDOR: обращение к чужому `subscriptionId` (чтение/списание/suspend/resume/close) → `404`, объект не раскрыт (AD-016) |
| AC-17 (нег.) | Отзыв при списании «в полёте»: после отправки в ОПКЦ попытка не помечается локально `FAILED`; исход доводится до терминала, попадает в отчёт/возврат (AD-009) |

§7 item 4 update + add items 11-13.

§9 assumptions + open questions + verification.

Let me apply.

  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="| 10 | Объём первой волны: `FIXED` vs `VARIABLE` (ЖКХ) | Зависит от сервиса НСПК и UX | `VARIABLE` нужен ЖКХ/связи — подтвердить у НСПК | A, old_string="| 10 | Объём первой волны: `FIXED` vs `VARIABLE` (ЖКХ) | Зависит от сервиса НСПК и UX | `VARIABLE` нужен ЖКХ/связи — подтвердить у НСПК | A)`
  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="- Публичные факты о «Подписке СБП» (подтверждение в приложении банка плательщика, месячные лимиты, отзыв) взяты из открытых источников и не, old_string="- Публичные факты о «Подписке СБП» (подтверждение в приложении банка плательщика, месячные лимиты, отзыв) и о поправках ЗоЗПП (в силе с 01.)`
  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="3. Требуется ли уведомление плательщика перед каждым списанием `[ТРЕБУЕТ ПРОВЕРКИ]`?\n4. Точка авторитета по согласию: локальный реестр шлю, old_string="3. Требуется ли уведомление плательщика перед каждым списанием `[ТРЕБУЕТ ПРОВЕРКИ]`?\n\n**Выполненные проверки:**\n\n- `openapi/tsp-api.yam)`

Add §7 items 11-13 (authority, resume semantics, notification already item 6). Let me add after item 10.

Current item 10: "| 10 | Объём первой волны: `FIXED` vs `VARIABLE` (ЖКХ) | Зависит от сервиса НСПК и UX | `VARIABLE` нужен ЖКХ/связи — подтвердить у НСПК | A6/A1 |"

Add:
| 11 | Точка авторитета по согласию (локальный реестр vs банк плательщика) | Определяет модель сверки и аудита; публичные источники не подтверждают | реестр в шлюзе + сверка, приоритет внешнего статуса | До A1 |
| 12 | Возобновление подписки после отключения (новое согласие vs восстановление) | Влияет на FSM и API; НСПК упоминает возможность возобновления | трактовать как новое согласие до подтверждения | A1 |
| 13 | Требования к уведомлению плательщика (дубль item 6) — skip.

Actually item 6 already covers notification. So add 11 and 12.

Then §9 fixes.

Let me apply.

  `write_file(content="# Платёжный шлюз СБП (C2B-приём)\n\nПроектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через, file_path="/home/architect/project/README.md")`

Now update README (structure + status) and append memlog entries. Then re-run validation (lint replica, openapi YAML + BC diff), and check for remaining INITIATED references in normative files (excluding reviews).

README current:
```
# Платёжный шлюз СБП (C2B-приём)

...
- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК ...

## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-008
docs/
  solutioning.md             ...
  nfr.md                     измеримые NFR
  contracts/tsp-api.md       контракт API ТСП v0.1 (мерчант-API)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.1 (ядро ↔ транспорт; основа RFP)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  adr/ADR-001..007.md        архитектурные решения
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton)
```
```

Update: add change-set CS-001 lines, update versions (tsp-api v0.2, opkc-adapter v0.2), add ADR-008, add docs/change/c2b-subscriptions/, add docs/spec/consent-state-machine.md, note AD-001..AD-016. And status: ADR-007 Accepted (A3) + new A6 pending.

Let me rewrite README fully (it's small). I read it earlier. Let me write.

Then memlog append lines.

Then final validation.
Now updating the README index and appending to the memlog.

  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/.memlog.md", new_string="- (event) spine finalized as Proposed (вступает в силу после ратификации ADR-008 на решении A6)\n- (event) reviewer gate completed: 5 линз , old_string="- (event) spine finalized as Proposed (вступает в силу после ратификации ADR-008 на решении A6)\n")`

Now the memlog append. The memlog is append-only; I must add new lines at the end (I can edit the file by appending — but the "append-only" invariant means don't rewrite earlier lines; adding lines at end is fine). I'll use edit to replace the last line with last line + new entries.

Last line currently: "- (event) spine finalized as Proposed (вступает в силу после ратификации ADR-008 на решении A6)".

Replace with that + new entries:
- (event) reviewer gate completed: 5 lenses, findings triaged
- (assumption) corrected fact: ЗоЗПП — ФЗ 376-ФЗ 15.10.2025, в силе 01.03.2026 (первичный источник consultant.ru); прежняя дата 01.09.2025 отклонена
- (decision) AD-010: канонический словарь статусов, INITIATED — только внутреннее подсостояние
- (decision) AD-011: уникальность по периоду при создании попытки; Idempotency-Key=chargeId; формат billingPeriod
- (decision) AD-009: владелец учёта лимитов — шлюз; точка линеаризации отзыва; аудит
- (decision) AD-012: G8 подтверждается до подписания контракта
- (decision) AD-014 доказуемость согласия/отзыва; AD-015 AML; AD-016 объектная авторизация и ссылки
- (question) точка авторитета по согласию; возобновление подписки после отключения
- (event) fixes applied; re-verification pending

Let me do that. Then run final checks.

  `run_shell_command(command="cd /home/architect/project && echo \"=== spine lint (replica) ===\" && node <TMP>.js \"$PWD\" | node -e \"let s='';proces, description="Re-run lint, contract checks, consistency greps")`

Now final re-verification:
1. lint replica on spine → expect 0 findings. But note: AD-014..AD-016 blocks — each has Binds/Prevents/Rule. Also check placeholder tokens: spine has `{subscriptionId}` in AD-011 (regex won't match due to uppercase I) and `{id}`? AD-009 has no braces. FSM not linted. Let me run.
2. openapi YAML + BC diff.
3. grep for remaining "INITIATED" outside reviews/.
4. Also check CONSTRAINTS rules still pass.
5. Check consistency: does anything still say "AD-009…AD-013" or "AD-001…AD-008" incorrectly? README updated. Spine header updated. ADR-008 references updated. Let me grep for "AD-009…AD-013" and "AD-013" mentions.
6. Also the FSM §3 heading says "## 3. Списание: статусная машина платежа типа CONSENT" — fine.
7. Also check the spine has no leftover "деeplink".

Let me run a combined verification command.

Also: the FSM §2.2 C4/C11 guard mentions "подтверждённые лимиты получены" — fine.

Also the opkc-adapter §9 — does it use INITIATED? No. Good.

Let me run checks.
Final verification pass — lint, contract validity, backward-compat, and consistency greps.

  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="AD-009…AD-016", old_string="AD-009…AD-013")`
  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="- Related: ADR-002, ADR-003, ADR-004, ADR-005, ADR-007, AD-002, AD-003, AD-005, AD-008, AD-009…AD-016", old_string="- Related: ADR-002, ADR-003, ADR-004, ADR-005, ADR-007, AD-002, AD-003, AD-005, AD-008, AD-009…AD-013")`
  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки), AD-003 (spine), AD-009…AD-016", old_string="- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (подписки), AD-003 (spine), AD-009…AD-013")`

All good. The residual INITIATED mentions are intentional (explaining it's internal). Stale ranges:
- CHANGE-PACKAGE line 66/79/221 mention AD-009…AD-013 → should be AD-009…AD-016.
- ADR-008 Related line: "AD-009…AD-013" → AD-009…AD-016.
- tsp-api.md line 6: "AD-009…AD-013" → AD-009…AD-016.
- memlog line 29 is historical (artifacts written at the time) — append-only; leave (it's an accurate historical record). Actually the memlog is append-only and records what happened; the "artifacts written" line referenced AD-009…AD-013 at that time. I'll leave it (history). Hmm, but it could confuse. The memlog already has a later correction entry. Leave as history.
- .arch-handoff/TASK.md mentions AD-001..AD-008 — that's the existing handoff for the walking skeleton (unchanged, correct for base). Leave.

Let me fix the three stale ranges (CHANGE-PACKAGE x3, ADR-008, tsp-api) and also the tsp-api "AD-009…AD-013" line.

Also ADR-008 line 6 "Related: ... AD-009…AD-013" → AD-009…AD-016.

Let me do replace_all "AD-009…AD-013" → "AD-009…AD-016" in those files.

Also check ADR-008 body: earlier I edited references "AD-009…AD-016 (spine, Proposed)" — good. Line 6 still old.

Let me apply.

Also, should I update .arch-handoff/CONSTRAINTS.yaml to add fitness rules for AD-009..AD-016? The change package says "обновить CONSTRAINTS.yaml ... (после A6)". The handoff CONSTRAINTS is for the implemented walking skeleton; adding rules now for un-approved change could be premature. But the CHANGE-PACKAGE §8 says it's a post-A6 action. That's a defensible decision. However, adding the fitness rules now would make the change verifiable. Hmm. The reviewer (adversarial) flagged "CONSTRAINTS.yaml contains zero fitness rules for AD-009…AD-013". Since the change is Proposed and CONSTRAINTS is regenerated for the code harness, I think adding *proposed* fitness rules is beyond scope and could confuse the current handoff. I'll leave it as a post-A6 action (already documented). But I could add the new fitness rules in a change-scoped file: e.g. docs/change/c2b-subscriptions/CONSTRAINTS.delta.yaml with proposed fitness rules, referenced. That addresses the gap without touching the accepted handoff. Good idea — adds value and satisfies "передать исполнителям".

Let me create docs/change/c2b-subscriptions/CONSTRAINTS.delta.yaml proposing fitness rules for AD-009..AD-016, following the scheme of .arch-handoff/CONSTRAINTS.yaml (control::check rules: file_exists, must_contain, must_not_contain). Fitness tests for behavioral invariants can be expressed as must_contain on the spec/code? The existing scheme only supports file/pattern checks. I'll express enforceable proxies:
- ad-010-canonical-status: must_contain in openapi/tsp-api.yaml? Hmm.
Better: express them as "planned fitness tests" in a YAML with type: test, referencing AC-xx. But that diverges from the existing schema. Let me keep the same schema where possible and add a note that behavioral invariants map to tests AC-xx (to be wired at A4).

I'll create a small delta YAML:
```
# Предлагаемое расширение fitness-правил (черновик, до ратификации ADR-008 / до A4).
# Схема — как в .arch-handoff/CONSTRAINTS.yaml (control::check) для механически проверяемых;
# поведенческие инварианты выражаются тестами AC-xx (см. CHANGE-PACKAGE.md §6.1).
rules:
  - name: no-consent-credit-outside-paid
    type: must_contain
    glob: "docs/spec/consent-state-machine.md"
    pattern: 'зачисление **только** из `PAID`'
    severity: error
  ... etc
```
Hmm must_contain on docs isn't a real fitness test for code. The existing CONSTRAINTS already does must_contain on docs (e.g. nfr-measurable). So it's consistent with the repo's "decision-stage" constraints. Let me produce a modest set that mirrors the repo's own style, plus a table mapping behavioral invariants → AC tests.

Rules:
- consent-only-active-debit: must_contain ARCHITECTURE-SPINE.md pattern 'только при согласии в `ACTIVE`' 
- credit-only-from-paid-consent: must_contain docs/spec/consent-state-machine.md 'зачисление **только** из `PAID`'
- charge-idempotency-period: must_contain ARCHITECTURE-SPINE.md 'не более одной незавершённой попытки'
- single-okpc-adapter-consent: must_contain ARCHITECTURE-SPINE.md 'только через единый адаптер ОПКЦ'
- consent-evidence-audit: must_contain ARCHITECTURE-SPINE.md 'неизменяемый артефакт'
- consent-aml: must_contain ARCHITECTURE-SPINE.md 'антифрод/AML-контур'
- subscription-object-authz: must_contain ARCHITECTURE-SPINE.md '`tspId` согласия = `tspId` запроса'
- contract-backward-compat: must_contain docs/contracts/tsp-api.md 'обратно совместимо'
- no-breaking-status: must_not_contain openapi/tsp-api.yaml pattern 'INITIATED,' hmm. Let me: must_not_contain openapi/tsp-api.yaml 'QR_ISSUED' ... no, Payment enum legitimately has QR_ISSUED. Skip.
- adr-set-complete-008: file_exists docs/adr/ADR-008-...md

Let me create the delta file with ~8 rules + a mapping table for behavioral tests.

This directly addresses the reviewer gap and is useful for handing off. Let me do it.

Actually — careful about scope creep and the instruction "Don't add features beyond what was asked". But the task asks for a package transferable to executors and point 6 asks for acceptance criteria. A proposed fitness-rule delta is squarely supporting deliverables (verification). I'll add it concisely.

Then run the delta through a check? It's YAML; validate with js-yaml.

Let me fix stale ranges first, then write the delta, then validate YAML, then final summary.
Fixing stale AD references, and adding a proposed fitness-rule delta for executors (the reviewer noted the handoff had zero rules for the new invariants).

  `write_file(content="# Предлагаемое расширение fitness-правил для изменения CS-001 (подписки СБП).\n# Схема — как в .arch-handoff/CONSTRAINTS.yaml (control::che, file_path="/home/architect/project/docs/change/c2b-subscriptions/CONSTRAINTS.delta.yaml")`

Now create the proposed fitness-rules delta for executors. Then validate YAML and finish.

File: docs/change/c2b-subscriptions/CONSTRAINTS.delta.yaml

Content: same schema as .arch-handoff/CONSTRAINTS.yaml (control::check). Plus a comment mapping behavioral invariants to AC tests.

Rules (mechanical, decision-stage style):
- adr-008-present: file_exists docs/adr/ADR-008-...md (error)
- consent-only-active-debit: must_contain ARCHITECTURE-SPINE.md pattern 'только при согласии в `ACTIVE`' (error)
- consent-charge-idempotency: must_contain docs/spec/consent-state-machine.md pattern 'не более одной незавершённой' (error)
- consent-credit-only-from-paid: must_contain docs/spec/consent-state-machine.md pattern 'зачисление **только** из `PAID`' (error)
- consent-single-adapter: must_contain ARCHITECTURE-SPINE.md pattern 'только через единый адаптер ОПКЦ' (error)
- consent-evidence-audit: must_contain ARCHITECTURE-SPINE.md pattern 'неизменяемый артефакт' (error)
- consent-aml: must_contain ARCHITECTURE-SPINE.md pattern 'антифрод/AML' (error)
- subscription-object-authz: must_contain ARCHITECTURE-SPINE.md pattern '`tspId` согласия = `tspId` запроса' (error)
- contract-additive-version: must_contain openapi/tsp-api.yaml pattern 'version: 0.2.0' (warn)
- nfr-subscriptions-measurable: must_contain docs/nfr.md pattern 'Подписки СБП' (error)

Wait — the pattern strings must match exactly. Let me verify substrings:
- ARCHITECTURE-SPINE.md has "только при согласии в `ACTIVE`" → in AD-009 Rule: "Допуск списания возможен только при согласии в `ACTIVE`". Yes contains "только при согласии в `ACTIVE`". Note the README/constraints pattern uses backticks; fine.
- "не более одной незавершённой" — AD-011 Rule: "не более одной незавершённой попытки и не более одного успешного списания". Yes.
- consent-state-machine: "зачисление **только** из `PAID`" — §3: "зачисление **только** из `PAID` (AD-005)". Yes.
- "только через единый адаптер ОПКЦ" — AD-012 Rule: "идут только через единый адаптер ОПКЦ (AD-004)". Yes.
- "неизменяемый артефакт" — AD-014 Rule: "сохраняет в одной транзакции неизменяемый артефакт". Yes.
- "антифрод/AML" — AD-015 Binds: "антифрод/AML-контур банка"; Rule: "антифрод/AML-контур банка". Yes.
- "`tspId` согласия = `tspId` запроса" — AD-016 Rule. Yes.
- "version: 0.2.0" in openapi. Yes.
- "Подписки СБП" in nfr. Yes.

Mapping table as a comment for behavioral AC tests.

Let me write it and validate.

Then final: run js-yaml on the delta; run a quick "control check" simulation? The repo has no arch tool. I'll just validate YAML and manually confirm patterns via a small node script that applies the must_contain rules (nice verification!). Let me do that: a node script reading the delta and checking each rule against the glob/path+pattern. That's a faithful mini-runner.

Let me create the delta and a runner check inline.

Then final summary + JSON.

Also update CHange-package §4 table row for openapi says "6 новых путей, 5 новых схем" — actually 5 new schemas (SubscriptionRequest, Subscription, ChargeRequest, Charge, Problem) + 1 new response component. Fine.

Now write the delta file.

  `run_shell_command(command="cd /home/architect/project && npx --yes js-yaml docs/change/c2b-subscriptions/CONSTRAINTS.delta.yaml > <TMP>.json && node -e \"\nconst, description="Validate and run the proposed fitness-rule delta")`

Now validate the delta YAML and run a mini-runner applying the rules. Let me write a node check.

Rules use `glob:` — for our files it's a literal path. Implement: if rule.type file_exists → fs.existsSync(path). must_contain → read glob file, check includes(pattern). must_not_contain → check regex .test. Note pattern 'TODO|TBD|XXX' is a regex in the repo's semantics; and 'антифрод/AML' contains '/' — as substring or regex? In repo semantics, patterns like '99,95' and literal strings with backticks are used as substring? The CONSTRAINTS uses `pattern: '99,95'` and `pattern: 'только из состояния `PAID`'` — these look like regexes/substrings. `антифрод/AML` as regex would need escaping '/', which in JS regex literal is fine (unescaped / inside RegExp constructor is fine). I'll treat must_contain as regex-match (RegExp) which also handles substrings. But backticks and special chars: 'только при согласии в `ACTIVE`' as regex — backticks are literal, fine. '`tspId` согласия = `tspId` запроса' — fine. 'зачисление **только** из `PAID`' — `**` in regex means literal '*' repeated? In regex, `*` is a quantifier; `**` would be invalid ("Nothing to repeat"). So regex would throw. So the repo's semantics is probably substring (includes) for must_contain, and regex for must_not_contain ('TODO|TBD|XXX' needs regex). Hmm inconsistent.

Let me implement: try substring includes() first; if not found, fall back to RegExp test. That satisfies both. Good.

Let me run.

  `edit(file_path="/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md", new_string="1. Расширить handoff-пакет кодового харнесса (`.arch-handoff/`): TASK на расширение walking skeleton — FSM согласия, mock-адаптер согласий/, old_string="1. Расширить handoff-пакет кодового харнесса (`.arch-handoff/`): TASK на расширение walking skeleton — FSM согласия, mock-адаптер согласий/)`
  `edit(file_path="/home/architect/project/README.md", new_string="  change/c2b-subscriptions/  архитектурный пакет изменения CS-001 (оценка, влияние, решение, контракты, NFR, приёмка/откат, решения человек, old_string="  change/c2b-subscriptions/  архитектурный пакет изменения CS-001 (оценка, влияние, решение, контракты, NFR, приёмка/откат, решения человек)`

All checks pass. Let me add a pointer to CONSTRAINTS.delta.yaml in the CHANGE-PACKAGE §8 (transfer section) and README structure. Quick edits.

CHANGE-PACKAGE §8 point 1 currently says "обновить `CONSTRAINTS.yaml` (fitness-правила AD-009…AD-016)". Add "(черновик правил — `CONSTRAINTS.delta.yaml` в этом каталоге)".

README structure: add CONSTRAINTS.delta.yaml line.

Then final git status + list of files. Then produce the final answer with the file list + JSON (headless contract).

Note: reviews/ contains 5 review files written by subagents. Those are gate artifacts; should I keep them? The skill says keep scratch in reviews/ subfolder (not the deliverable folder root). Yes keep.

Let me make the two small edits and then check git status.

  `run_shell_command(command="cd /home/architect/project && git status --short && echo \"---\" && git diff --stat && echo \"--- untracked ---\" && git ls-files --others , description="Enumerate changed and created files")`

Now final: git status to enumerate created/modified files, and one last full verification (spine lint already 0; delta rules pass; openapi valid & BC OK). Let me run git status --short.

Then produce final answer: brief summary + file list + JSON (headless contract). The user asked to list created/modified files at the end. The architecture skill headless requires ending with JSON only. I'll give the file list, then the JSON object as the final block.

The JSON shape (from headless.md): status, intent, altitude, purpose, doc_workspace, spine, memlog, companions, assumptions, open_questions, conflicts_with_prior_decisions, reason.

status: "partial" or "complete"? The spine was produced, but open_questions non-empty and critical inputs inferred (headless) → "partial" per the contract ("partial (spine produced, but open_questions[] non-empty or critical inputs inferred)"). Our open_questions are genuinely non-empty. So status: "partial". Hmm — but "complete" would overclaim given open questions that need humans. The contract explicitly says partial means review before downstream use. Given this is an architecture package for a human decision with open external inputs, "partial" is honest. Yes, partial.

doc_workspace: /home/architect/project/docs/change/c2b-subscriptions
spine: /home/architect/project/ARCHITECTURE-SPINE.md
memlog: .../.memlog.md
companions: [the change package, ADR-008, consent-state-machine, tsp-api, openapi, nfr, opkc-adapter, vendor-rfp, CONSTRAINTS.delta]
assumptions: list
open_questions: list
conflicts_with_prior_decisions: the scope change (autoplatements were out of scope in solutioning.md §1) → that's a divergence with a prior decision, flagged for the human. Also AD-008/RFP timing risk. I'll list the scope activation as a conflict requiring A6.

Let me run git status.


All artifacts in place. I haven't committed (not asked).

Now write the final answer in Russian: concise summary covering the 7 deliverables, verification results, and the file list, then the JSON block.

I should mention the key reviewer-driven corrections and the human decisions.

Note: I did not commit — per repo norms, don't commit unless asked.

Let me write the final response. Keep it structured but not bloated. Then JSON last.

The JSON must be the last thing (headless contract). Chinese? No — Russian.

Let me draft.

Assumptions list:
- Публичные факты (НСПК «Подписка СБП») и ФЗ 376-ФЗ — из открытых источников, не заменяют документацию НСПК.
- Скоринг 14/15 — оценка архитектора (исходная рубрика в репо не зафиксирована).
- python3/uv отсутствуют → memlog.py/lint_spine.py не запускались; проверки воспроизведены (Node-реплика линтера, js-yaml).
- Точка авторитета по согласию не подтверждена публично → [ТРЕБУЕТ ПРОВЕРКИ].
- Рекомендация transport-first предложена, но не принята.

open_questions:
- Наличие/объём сервиса согласий НСПК на дату контракта.
- Обязательные поля/лимиты/срок/период согласия по протоколу НСПК.
- Точка авторитета по согласию (реестр шлюза vs банк плательщика).
- Возобновление подписки после отключения: новое согласие vs восстановление.
- Требования к уведомлению плательщика перед списанием / право блокировки.
- Юридический состав и срок хранения доказательства согласия.
- Допустимость частичного списания.
- Фазирование A6 (transport-first/include-now/defer).

conflicts_with_prior_decisions:
- scope: автоплатежи/подписки были вне scope (docs/solutioning.md §1) → активируются изменением CS-001; требует решения A6 (не блокирующее, но явное изменение).
- риск AD-008/ADR-007: если контракт с вендором подписан до фиксации G8, поддержку подписок придётся добавлять в уже подписанный контракт → возможен пересмотр ADR-007 (его expiry).

companions: list paths.

status: partial.

Let me write final.
Готово. Ниже — что сделано по каждому пункту, проверки и файлы.

## Что получилось

**1. Значимость и маршрут.** Оценка изменения — **14/15 (Critical)**: три независимых источника необратимости (RFP вендора, юридическая сила согласия, действующие согласия плательщиков) + новый протокольный сервис НСПК + регулирование. Нужна полная волна проектирования, а не «доработка API»: маршрут **A6 (решение) → A1 → A2 → A4 → A5**. Обоснование — `CHANGE-PACKAGE.md` §1.

**2. Влияние на принятую архитектуру.** Затронуты формально AD-002 (второй объект состояния), AD-003 (новые ключи), AD-004 (методы подписок в том же адаптере), AD-005 (новый вход в `PAID`), AD-006 (риск публичной поверхности согласия), AD-007 (усиление ПДн/ПОД-ФТ), **AD-008 `[ADOPTED]`** (риск: поддержку подписок надо зафиксировать в RFP *до* подписания контракта). Не меняются: единственный путь зачисления из `PAID`, trust-зоны, outbox/сверка, перечисление `Payment.status`, стратегия «гибрид». AD-001…AD-008 не переписаны — изменение добавлено как Proposed-блоки.

**3. Архитектурное решение.** `ADR-008` (Proposed): согласие плательщика как отдельная сущность; списание = платёж `operationType=CONSENT` в канонической машине; идемпотентность по периоду; всё через единый адаптер ОПКЦ; поверхность согласия вне шлюза; доказуемость согласия/отзыва; AML-контроль; объектная авторизация. Альтернативы, последствия и обратимость (**costly**) — в ADR-008.

**4. Контракты без поломки.** `openapi/tsp-api.yaml` → **0.2.0** и `tsp-api.md` → v0.2: только аддитивно (6 новых путей, 5 схем, опциональные поля). Проверено машинно: существующие операции/required/enums не изменены, добавлений — только новые.

**5. NFR.** `docs/nfr.md` §7: latency/throughput, распространение отзыва ≤ 5 с, двойное списание = 0, сверка согласий, аудит/AML/IDOR.

**6. Приёмка и откат.** `CHANGE-PACKAGE.md` §6: AC-01…AC-17 (включая негативные: гонка, отзыв «в полёте», IDOR, вендор без G8) и четырёхфазный откат (stop-new → wind-down → сохранение возвратов/сверки).

**7. Решения человека-архитектора.** 12 пунктов с причиной, рекомендацией и сроком: фазирование (`transport-first`), владение согласием, лимиты/сроки, юридическая модель, уведомление плательщика, требования к вендору (G8/P9/P10), точка авторитета согласия и др.

## Проверки (выполнены)

- Спина: **0 находок** репликой `lint_spine.py` (нет плейсхолдеров; AD-001…AD-016 монотонны; у всех AD-009…AD-016 есть Binds/Prevents/Rule).
- `openapi/tsp-api.yaml`: валиден (OpenAPI 3.0.3); дифф v0.1→v0.2 — **BACKWARD COMPAT: OK**.
- `CONSTRAINTS.delta.yaml`: 11 правил — все PASS.
- Reviewer gate (5 независимых линз, `reviews/`) нашёл реальные дыры — **исправлены**: неканонический статус `INITIATED`, гонка/уникальность периода, отсутствие точки линеаризации «отзыв vs списание», двойной владелец лимитов, дыра в аудите согласия, IDOR, AML; **исправлен факт**: закон — ФЗ от 15.10.2025 № 376-ФЗ (ст. 16.1 ЗоЗПП), в силе **с 01.03.2026** (а не 01.09.2025).

> Методические скрипты BMAD не запускались: в окружении нет `python3`/`uv` (проверки воспроизведены Node-репликой линтера и `js-yaml`). Коммит не делал — не просили.

## Созданные и изменённые файлы

**Созданы:**
- `docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`
- `docs/spec/consent-state-machine.md`
- `docs/change/c2b-subscriptions/CHANGE-PACKAGE.md`
- `docs/change/c2b-subscriptions/CONSTRAINTS.delta.yaml`
- `docs/change/c2b-subscriptions/.memlog.md`
- `docs/change/c2b-subscriptions/reviews/review-rubric.md`, `review-tech-verification.md`, `review-adversarial.md`, `review-security-compliance.md`, `review-contract-compat.md`

**Изменены:**
- `ARCHITECTURE-SPINE.md` (блок CS-001: AD-009…AD-016 Proposed, Deferred, «Контракты и версии»)
- `openapi/tsp-api.yaml` (0.2.0, аддитивно)
- `docs/contracts/tsp-api.md` (v0.2, §6–§8)
- `docs/contracts/opkc-adapter.md` (v0.2, §9)
- `docs/nfr.md` (§7 + зависимости)
- `docs/rfp/vendor-rfp.md` (G8, P9/P10, kill criteria)
- `README.md` (статус, структура)

```json
{
  "status": "partial",
  "intent": "update",
  "altitude": "feature",
  "purpose": "build-substrate",
  "doc_workspace": "/home/architect/project/docs/change/c2b-subscriptions",
  "spine": "/home/architect/project/ARCHITECTURE-SPINE.md",
  "memlog": "/home/architect/project/docs/change/c2b-subscriptions/.memlog.md",
  "companions": [
    "/home/architect/project/docs/change/c2b-subscriptions/CHANGE-PACKAGE.md",
    "/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md",
    "/home/architect/project/docs/spec/consent-state-machine.md",
    "/home/architect/project/openapi/tsp-api.yaml",
    "/home/architect/project/docs/contracts/tsp-api.md",
    "/home/architect/project/docs/contracts/opkc-adapter.md",
    "/home/architect/project/docs/nfr.md",
    "/home/architect/project/docs/rfp/vendor-rfp.md",
    "/home/architect/project/docs/change/c2b-subscriptions/CONSTRAINTS.delta.yaml"
  ],
  "assumptions": [
    "Публичные факты о «Подписке СБП» и юридический факт (ФЗ от 15.10.2025 № 376-ФЗ, ст. 16.1 ЗоЗПП, в силе с 01.03.2026) взяты из открытых источников и не заменяют документацию НСПК.",
    "Скоринг значимости 14/15 — оценка архитектора; исходная рубрика 11/15 в репозитории не зафиксирована.",
    "python3/uv в окружении нет: memlog.py и lint_spine.py не запускались, их проверки воспроизведены (Node-реплика линтера, js-yaml).",
    "Рекомендация фазирования transport-first предложена, но не принята — за решением A6.",
    "Точка авторитета по согласию (реестр шлюза vs банк плательщика) публичными источниками не подтверждена."
  ],
  "open_questions": [
    "Есть ли у НСПК сервис согласий для C2B-приёма на дату контракта и в каком объёме (поля, лимиты, срок, период, уведомление плательщика).",
    "Точка авторитета по согласию: локальный реестр шлюза или банк плательщика/ОПКЦ.",
    "Возобновление подписки после отключения: новое согласие или восстановление прежнего subscriptionId.",
    "Юридический состав и срок хранения доказательства согласия/отзыва.",
    "Допустимость частичного списания по согласию.",
    "Фазирование изменения на решении A6 (transport-first / include-now / defer)."
  ],
  "conflicts_with_prior_decisions": [
    "Автоплатежи/подписки были заявлены вне scope (docs/solutioning.md §1, roadmap) — изменение CS-001 переводит их в scope; вступает в силу только после ратификации ADR-008 на решении A6.",
    "Риск для AD-008 [ADOPTED]/ADR-007: если контракт с вендором транспорта подписан до фиксации G8 (поддержка подписок), добавление подписок в уже подписанный контракт может потребовать пересмотра ADR-007 по его условию expiry — требуется действие до подписания RFP."
  ]
}
```
