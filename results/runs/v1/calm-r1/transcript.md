<!-- источник: <HARNESS>/runs/cells/calm-r1/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-cells-calm-r1-ws/chats/3f871c66-27b2-4343-8eae-ea0826388c2b.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `skill(skill="calm")`

Let me understand the task. The user is asking me to act as a solution architect for a bank. The repository is an accepted solution "СБП Payment Gateway (C2B acceptance)". I need to prepare an architectural package for a business change: recurring C2B debits (subscriptions) by payer consent.

I need to:
1. Assess significance of the change and route (how deep design needed and why)
2. Impact on accepted architecture: which invariants affected, what changes, what doesn't
3. Architectural decision with considered alternatives, consequences, reversibility
4. Contract changes (`openapi/tsp-api.yaml`) without breaking existing consumers
5. Measurable NFRs for new functionality
6. Acceptance criteria and rollback plan
7. What remains for human architect decision and why

I must only modify accepted decision files in the way accepted in this repo. There may be methodological skills and tools installed — use them as intended.

There's a project skill "calm" available: "An AI Assistant for FINOS CALM development." This is clearly relevant. The repository is about FINOS CALM. Also there's `.arch-handoff/` with rules.

Let me first invoke the "calm" skill since it's clearly relevant, and also explore the repository structure.

Let me start by invoking the calm skill and reading key files.

Actually, let me follow the guidance: "When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action". The "calm" skill is project skill for FINOS CALM development. This is highly relevant. Let me invoke it first.

Let me also plan to read the key files: ARCHITECTURE-SPINE.md, docs/, .arch-handoff/.

Let me start with the skill.

  `glob(pattern=".claude/skills/calm/calm-prompts/*.md")`
  `glob(pattern=".qwen/skills/calm/**/*.md")`
  `glob(pattern="**/*")`

Let me follow the first interaction instructions. I need to read the tool prompt files. But first, let me understand the repository structure more. Let me read the key files.

Let me read the calm-prompts and also the main architecture files in parallel.

Let me first list the .claude/skills/calm directory and read the prompt files.
Loading FINOS CALM instructions...

  `glob(pattern="docs/**/*")`
  `glob(pattern=".arch-handoff/**/*")`
  `glob(pattern="openapi/**/*")`
  `glob(pattern="*.md")`

The glob returned too much because of node_modules. Let me focus on the actual project files, excluding node_modules. Let me read the key files directly.

Let me read the ARCHITECTURE-SPINE.md, README.md, and the docs/ and .arch-handoff/ and openapi/ directories.

  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/.arch-handoff/ARCHITECTURE.md")`

Let me read the key files. First the ARCHITECTURE-SPINE.md, README.md, TASK.md, and the handoff rules (RUBRIC, CONSTRAINTS, MANIFEST, ARCHITECTURE). Then the docs. Let me read them in parallel.

  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/openapi/tsp-api.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/contracts/opkc-adapter.md")`

Now I have a good understanding of the repository structure and its conventions. Let me read the remaining key documents: docs/solutioning.md, docs/nfr.md, docs/contracts/tsp-api.md, docs/spec/state-machine.md, openapi/tsp-api.yaml, and the ADR files. Let me read these to understand the full picture, especially the state machine and the TSP API contract.

Let me read the key files.

  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/adr/ADR-005-integraciya-s-abs-zachisleni)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/adr/ADR-002-model-konsistentnosti-platez)`

Now I have a comprehensive understanding of the repository. Let me read the ADR files quickly to understand the format and details, especially ADR-002 (state machine), ADR-005 (refunds saga), ADR-007 (implementation strategy). Let me also read the remaining ADR files.

Actually, I have enough context from the ARCHITECTURE.md epic-context which contained ADR-001, ADR-002 (partial). Let me read ADR-002 fully, ADR-004, ADR-005, ADR-007, and ADR-006 and ADR-003 to understand the conventions. Also I should understand the CALM methodology context.

Wait — the key question is: the repository uses CALM as a skill/methodology, but the actual architecture documents are markdown ADRs (not CALM JSON). The "calm" skill is "FINOS CALM development" but the repo is actually using a "spine" methodology with ADRs and invariants. The calm skill's first interaction instructions say to read the calm-prompts files. But actually, looking more carefully, the repository's actual working method is "ARCHITECTURE-SPINE" with ADRs, solutioning, NFR, contracts, state machine. The CALM skill is present but the repo doesn't seem to actually use CALM JSON schemas — it uses markdown ADR format.

Actually, wait. Let me reconsider. The task is: "Подготовь архитектурный пакет этого изменения поверх принятого решения". The methodology here is the "spine" approach — ARCHITECTURE-SPINE.md with invariants AD-001..AD-008, ADRs in docs/adr/, solutioning.md, nfr.md, contracts, state-machine.

The CALM skill is one of the "методические навыки и инструменты" (methodological skills and tools) that "могут быть установлены". But actually, the repo clearly uses a spine+ADR methodology, not CALM JSON. The calm skill is available but the actual deliverables are markdown documents.

Wait, let me re-read the task: "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." (The project may have methodological skills and tools installed — use them as intended.)

So the "calm" skill is installed. But is CALM the actual methodology of this repo? Let me check. The repo has `.claude/skills/` and `.qwen/skills/` with `calm` skill. But the architecture is documented in markdown ADRs + spine, NOT CALM JSON.

Actually, I think the naming here is confusing. "calm-r1" appears in the path (runs/cells/calm-r1). This is likely a benchmark/test cell named "calm-r1" (CALM round 1), testing whether the agent follows the CALM methodology skill. But the actual repo content is about a СБП payment gateway using a "spine" + ADR methodology.

Let me focus on what matters: the task asks me to produce an architectural package for the change (recurring C2B debits / subscriptions). The "принятый способ" (accepted way) of changing decision files in this repo is:
- Add ADRs in `docs/adr/ADR-00X-...md`
- Update `ARCHITECTURE-SPINE.md` (invariants) — but carefully, this is a spine; changes to spine require escalation to parent spine for conflicts
- Update `docs/solutioning.md`
- Update `docs/nfr.md`
- Update contracts `docs/contracts/tsp-api.md` and `openapi/tsp-api.yaml`
- Update state machine `docs/spec/state-machine.md`
- Possibly new ADR for recurring payments

The task's key constraint: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — Change accepted decision files only in the way accepted in this repo.

The accepted way: 
1. ADRs are added as new files `docs/adr/ADR-00X-<slug>.md`, with Status: Proposed, Owner, Related, Context, Decision, Alternatives Considered, Consequences, Reversibility, References.
2. The spine (`ARCHITECTURE-SPINE.md`) has invariants AD-001..AD-008 with "Status: Proposed (ADR-00X)" or "[ADOPTED]". A new invariant (e.g., AD-009) would need to be added in the same format. But note: the spine says "Локальное переопределение родительских ограничений запрещено; конфликт эскалируется наверх." Also AD-008 says local override of parent constraints is forbidden.

Actually, wait. Let me carefully understand the "spine" methodology. The ARCHITECTURE-SPINE.md has "Родительский spine: initiative «Подключение банка к СБП (эквайринг C2B)». Данный spine — уровень feature. Локальное переопределение родительских ограничений запрещено; конфликт эскалируется наверх."

So this spine is at "feature" level under a parent initiative spine. AD-001..AD-008 are the invariants of this feature spine.

The recurring C2B debits (subscriptions) is a new capability. The question is whether this belongs to this feature spine (C2B acceptance) or to a new initiative. Looking at the deferred section:
- "C2C-переводы и выплаты B2C/B2B: roadmap после стабилизации C2B; вернуть как отдельный initiative (родительский spine изменится)."

Recurring payments (subscriptions) is NOT in the deferred list explicitly. But "автоплатежи" IS mentioned in solutioning.md §1: "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

Wait, "автоплатежи" (autopayments) is listed as roadmap/out of scope. So recurring C2B debits is essentially "автоплатежи" (autopayments/subscriptions). This is currently OUT of scope (roadmap).

Hmm, but the task says the business is asking for it now. So I need to prepare an architectural package to bring it into scope.

Actually, this is a critical insight: recurring C2B debits (subscriptions) with payer consent = "автоплатежи" which is currently in the roadmap/out-of-scope list. This is a significant scope expansion.

Let me think about what the C2B recurring payment actually is in the СБП context. СБП (SBP) has a mechanism for recurring payments: "СБП Подписки" / recurring payments where the merchant initiates a debit from the payer's account with prior consent. This is different from the current C2B QR flow where the payer must actively scan and confirm each payment.

Actually, in СБП, there is a "подписка" (subscription) mechanism: The payer gives consent (согласие) in their bank app, and then the merchant can initiate recurring debits without QR. This is the C2B "recurring" flow.

Key architectural implications:
1. New state machine entities: "согласие" (consent/mandate) lifecycle, plus "рекуррентный платёж" (recurring payment) that references a consent.
2. The payment state machine might extend with a new source: instead of `QR_ISSUED`, a recurring debit could go straight to `PAID` (or a new state) since there's no QR.
3. Consent management: create consent, activate consent (payer confirms in bank app), revoke consent, expiration, limits.
4. Idempotency keys extended to consent operations.
5. Webhooks: new events (consent.created, consent.activated, consent.revoked, payment.completed for recurring).
6. Contract changes: new endpoints under /v1 (backward compatible) — consent resource, recurring payment creation with consentId.
7. AD-005 "зачисление только из PAID" still holds — recurring payment still needs confirmed НСПК status.
8. NFR: consent activation latency, recurring debit throughput, no double debit (idempotency), consent limits enforcement.

Now, the methodology. I need to figure out what the "accepted way" of modifying files is. Looking at the repo:

- ADRs go in `docs/adr/ADR-00X-slug.md` (and also mirrored in `.arch-handoff/adr/`? Actually the .arch-handoff/adr/ are copies. Wait, let me check if .arch-handoff is a snapshot copy or the source. The MANIFEST.json lists sources from docs/. The .arch-handoff/ARCHITECTURE.md is the "epic-context" generated from docs. The .arch-handoff/adr/*.md are copies.)

Actually, looking more carefully: `.arch-handoff/` is the handoff package to the code harness. It contains copies: `adr/ADR-001..007.md`, `ARCHITECTURE.md` (epic context), `CONSTRAINTS.yaml`, `MANIFEST.json`, `RUBRIC.yaml`, `TASK.md`.

So the source of truth is `docs/` and `ARCHITECTURE-SPINE.md` and `openapi/`. The `.arch-handoff/` is a generated handoff snapshot.

The task says: "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям."

So I need to prepare:
1. The architectural package for this change (assessment, impact, ADR, contract changes, NFR, acceptance criteria, rollback, human decisions).

The deliverables should be files. Given the repo convention, I should:
- Add a new ADR: `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md` (the next number is 008, since ADR-001..007 exist). Note ADR-007 is "proposed-a3" (implementation strategy) which is Accepted. So the next ADR number is 008.
- Add a new invariant to `ARCHITECTURE-SPINE.md`? Or update it? Actually, a new invariant AD-009 would be added, OR the change may not require a new invariant but rather a new ADR that binds to existing invariants.

Wait, but the task is a change request (business asks for recurring debits). The architectural package needs to be "вынесено на архитектурное решение" (brought to architectural decision). This means the ADR is in "Proposed" status and needs a human decision.

Let me think about the route/значимость. The change is significant: it adds a new product capability (subscriptions), touches the state machine (new consent entity), extends the API contract (backward compatible), adds new flows, new NFRs. This is a Critical route too — it's a financial capability. But it's an extension, not a rewrite.

Let me also think about whether this needs a NEW initiative (parent spine) or can fit in this feature spine. The deferred section says автоплатежи is roadmap "после стабилизации C2B". Since the parent spine is "Подключение банка к СБП (эквайринг C2B)", recurring debits are still C2B (merchant receives payment from consumer), just without QR. So it fits within the C2B initiative scope (эквайринг C2B). It's not C2C or B2C/B2B. So it belongs to this feature spine, but it's a significant extension.

Actually, wait — I should reconsider. Recurring C2B debits in СБП: is the flow "merchant initiates debit from payer's account with consent" (merchant-initiated / MIT) or is it still "payer pushes"? In СБП subscriptions, the payer gives consent, and then the merchant's bank (via ОПКЦ) requests a debit. The payment still flows through СБП. This is C2B (merchant receives). So it's within C2B scope.

Now let me plan the concrete deliverables. Since the user wants a comprehensive architectural package, and I should not write code, I'll produce markdown files following the repo's conventions.

Let me decide the file set:

1. **`docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md`** — the main ADR for this change. It follows the ADR format (Date, Status: Proposed, Owner, Related, Context, Decision, Alternatives Considered, Consequences, Reversibility, References).

2. **Update `ARCHITECTURE-SPINE.md`** — add AD-009 invariant for recurring debits (consent as first-class entity, debit only from active consent, etc.)? OR should I NOT touch the spine and instead note it as a proposal? The task says "какие инварианты затронуты". The spine currently has AD-001..AD-008. Adding AD-009 would be the "accepted way" if the change introduces a new invariant. But modifying the spine is a big deal — it's the parent decision.

Actually, let me reconsider. The spine is "инварианты AD-001…AD-008". The change (recurring) may:
- NOT break existing invariants AD-001..AD-008 (they still hold).
- Add new invariants (e.g., AD-009: рекуррентные списания возможны только по активному согласию плательщика; AD-010: дебет по согласию без QR — отдельный путь, но зачисление всё равно из PAID).

So I should propose new invariants. But how to "change the spine in the accepted way"? The spine's format is clear: each AD has "Status", "Binds", "Prevents", "Rule". Adding new AD blocks in "Proposed" status is the accepted way. And I should be careful: the spine header says "Локальное переопределение родительских ограничений запрещено; конфликт эскалируется наверх." — Adding NEW invariants is not overriding; it's extending the feature spine. That's acceptable, but I should flag if any new invariant conflicts with the parent initiative spine (it doesn't, since recurring C2B is still C2B).

Hmm, but actually, I need to be careful about the scope of my changes. The user says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." This means: when I change the accepted decision files (ARCHITECTURE-SPINE.md, docs/*, openapi/*), follow the repo's conventions. It does NOT mean "don't change them". It means "change them in the proper way."

So my plan:
1. Add new ADR(s) — ADR-008 (and possibly more if needed).
2. Update ARCHITECTURE-SPINE.md — add AD-009 (and AD-010) invariants in Proposed status.
3. Update docs/solutioning.md — add the recurring C2B flow (new section or update roadmap). Actually, solutioning.md currently lists "автоплатежи" as out of scope. I need to move it in scope and describe the new components/flows.
4. Update docs/nfr.md — add measurable NFRs for recurring debits.
5. Update docs/contracts/tsp-api.md — add consent endpoints + recurring payment endpoints (backward compatible).
6. Update openapi/tsp-api.yaml — add new paths/schemas (backward compatible, additive only).
7. Update docs/spec/state-machine.md — add consent state machine + recurring payment states/transitions.
8. Possibly update docs/contracts/opkc-adapter.md — add consent operations to the ОПКЦ adapter contract (createConsent, debitWithoutQr, etc.) — but this depends on НСПК protocol which is [ТРЕБУЕТ ПРОВЕРКИ].

Also the task asks for a "package" that can be brought to architectural decision. So I should produce a summary document too. Maybe a new file like `docs/solutioning-recurring.md` or a new ADR + updated files. Actually, the task's 7 deliverables map to:
1. Assessment of significance and route — could be a section in the ADR or a separate brief.
2. Impact on accepted architecture — a section.
3. ADR with alternatives — the ADR.
4. Contract changes — tsp-api.md + openapi.
5. NFR — nfr.md.
6. Acceptance criteria + rollback — section (in ADR or a separate doc).
7. Human decisions — section.

The most natural mapping in this repo:
- ADR-008 covers #3 (decision + alternatives + consequences + reversibility) and parts of #2 (impact), #7 (open questions for human).
- A new "solutioning" doc or an extension covers #1 (assessment/route), #2 (impact), #6 (acceptance + rollback).

Let me think about how to organize this cleanly. I think the cleanest approach:

**Primary new file**: `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski.md` — the architectural decision.

**Secondary new file**: Maybe `docs/solutioning-recurring.md` — but actually the repo already has `docs/solutioning.md` as the single solutioning doc. I should extend it rather than create a parallel doc. But extending solutioning.md significantly could be a large edit. Alternatively, create a dedicated `docs/adr/ADR-008-...` plus a dedicated brief.

Actually, let me reconsider what's cleanest and matches repo conventions. The repo has:
- One solutioning.md (full design)
- ADRs (one per decision)
- nfr.md
- contracts (tsp-api.md, opkc-adapter.md)
- spec/state-machine.md

The recurring change is big enough that it needs:
- A new ADR (ADR-008) — the decision to support recurring C2B debits via consent, with alternatives.
- Updates to tsp-api.md contract (add consent + recurring payment endpoints).
- Updates to openapi/tsp-api.yaml.
- Updates to state-machine.md (consent lifecycle + recurring payment states).
- Updates to nfr.md (recurring NFRs).
- Updates to solutioning.md (move автоплатежи from out-of-scope to in-scope; describe flows).
- Update ARCHITECTURE-SPINE.md (new invariants AD-009/AD-010).
- Update README.md (document list).

Plus a "package" summary doc that ties together the 7 deliverables for the human architect review. Maybe I'll write this as the ADR's "Context/Decision" plus a separate `docs/adr/ADR-008` and put the assessment/route/acceptance/rollback into the ADR itself.

Actually, given the task's 7 explicit deliverables, and the repo convention that each ADR has a specific structure, I think the best approach is:

1. Write `docs/adr/ADR-008-...` following the ADR template but expanded to include the assessment (#1), impact (#2), decision (#3), and reversibility. The ADR template has Context/Decision/Alternatives/Consequences/Reversibility/References. I'll enrich it.

2. Create a dedicated "architectural package" document that addresses all 7 points explicitly and points to the files. This could be `docs/solutioning-recurring.md` or `docs/proposals/recurring-c2b.md`. Hmm.

Wait, let me re-read the task once more:

"Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: [7 items]."

"Принятые файлы решения меняй только тем способом, который принят в этом репозитории."

"Когда закончишь, кратко перечисли созданные и изменённые файлы."

So the deliverable is: (a) an architectural package (documented), (b) modifications to accepted decision files in the accepted way, (c) a final list of files.

I think the right structure is:
- A main "package" document that answers the 7 questions in prose (this is what gets presented to the architecture board). This could be a new ADR + a brief. 
- The actual accepted-file changes: ADR-008, spine, tsp-api.md, openapi, state-machine.md, nfr.md, solutioning.md, README.md.

But I want to avoid over-engineering. Let me think about what "передать исполнителям" (hand off to implementers) requires. The handoff package is `.arch-handoff/`. But the task says "вынести на архитектурное решение и затем передать исполнителям" — so first to architectural decision, THEN to implementers. The package should be ready for both, but I don't need to regenerate `.arch-handoff/` now (that happens after the decision and stack selection). Actually, the MANIFEST says handoff is regenerated "после выбора стека и начала реализации". So I should NOT regenerate .arch-handoff now. I should just prepare the decision-level documents in docs/ and openapi/.

OK here's my refined plan. Let me define the actual content.

## Domain analysis: Рекуррентные C2B-списания (подписки СБП)

Current C2B: payer scans QR → pays → notify. Each payment requires payer action.

Recurring C2B (subscriptions): payer gives a one-time consent (согласие) in their bank app; merchant then initiates debits without payer action per billing cycle. In СБП this is the "подписка" / recurring payment mechanism.

Key domain entities:
- **Согласие (Consent/Mandate)**: created by ТСП, activated by payer (in payer's bank app via СБП), has limits (max amount, max frequency, validity period), revocable.
- **Рекуррентный платёж (Recurring Payment)**: initiated by ТСП referencing an active consent, debits payer account, credits ТСП account. No QR. Still needs confirmed НСПК status before crediting (AD-005 holds).

The state machine:
- Payment: currently CREATED → QR_ISSUED → PAID → CREDITED → COMPLETED. For recurring, there's no QR_ISSUED; instead the flow could be: CREATED → (debit initiated at НСПК) → PAID (confirmed) → CREDITED → COMPLETED. So a new path that skips QR_ISSUED. This is a state machine change.
- Consent: new state machine: CREATED (pending payer confirmation) → ACTIVE → (REVOKED | EXPIRED | SUSPENDED). 

Actually, let me be precise about СБП subscription mechanics. The consent is created by the merchant's bank (агент ТСП) and the payer confirms it in their own bank's app. The НСПК СБП has a "согласие" / подписка mechanism. When a recurring debit happens, the merchant's bank sends a debit request referencing the consent, and НСПК routes to payer's bank which executes the debit per the consent.

I should mark protocol details as [ТРЕБУЕТ ПРОВЕРКИ] since НСПК documentation is an external input, consistent with the repo convention.

## Impact on invariants (AD-001..AD-008)

- AD-001 (изоляция платёжного контура): unchanged; consent/recurring logic stays inside the СБП-шлюз.
- AD-002 (статусная машина): extended — consent becomes a new first-class state machine; recurring payment path skips QR_ISSUED. The rule (atomic transition + outbox) still holds.
- AD-003 (идемпотентность): extended — consent operations need idempotency; recurring debit init needs idempotency key; НСПК recurring events need eventId dedup.
- AD-004 (единственный адаптер ОПКЦ): unchanged — consent/debit protocol goes through the same adapter.
- AD-005 (зачисление только из PAID): **unchanged and critical** — recurring debit also credits only from confirmed НСПК status. No "платежи из воздуха" from a consent alone.
- AD-006 (trust-зоны): unchanged — consent data is ПДн, stays in secure zones.
- AD-007 (НПС/КИИ/ПДн): extended — consent is ПДн (152-ФЗ), needs consent storage minimization, revocation, audit.
- AD-008 (стратегия реализации): unchanged — core stays contract-independent; vendor adapter handles the recurring protocol.

New invariants to propose:
- **AD-009** (рекуррентное списание только по активному согласию): Prevents — списание без согласия, списание после отзыва согласия, превышение лимитов согласия. Rule: debits only from ACTIVE consent, with limits (amount, frequency, validity) enforced at the gateway before init; revocation is effective immediately.
- **AD-010** (отзыв согласия — стоп-сигнал): any pending/recurring debit after revocation → blocked. Could fold into AD-009. Let me keep it to one or two new invariants.

Actually let me think: maybe one new invariant AD-009 is enough (recurring debit requires active consent with enforced limits + immediate revocation). I'll propose AD-009 and maybe AD-010 for "согласие — это ПДн, отдельный жизненный цикл и аудит".

Let me settle on:
- AD-009: «Рекуррентное списание — только по активному согласию плательщика» (consent is a first-class entity; debit only from ACTIVE consent within limits; revocation is immediate; consent lifecycle audited).
- AD-010: «Зачисление рекуррентного платежа — только из подтверждённого статуса НСПК» — actually this is already AD-005. So no need for a separate invariant; AD-005 covers it. But I should explicitly note AD-005 extends to the new path.

Hmm, maybe just AD-009. Let me also consider AD-010 for "идемпотентность рекуррентного списания" — already AD-003. So one new invariant AD-009 is cleaner.

Actually, I realize I should be careful about "consent" being a new financial instrument. Let me propose AD-009 for consent and AD-010 for the recurring debit path (skip QR but still PAID-gated). But AD-010's rule would largely duplicate AD-005. I think I'll do:

- AD-009: Рекуррентные списания и согласие плательщика (consent entity, active-only debit, limits, immediate revocation, ПДн).

That's a single coherent new invariant. Good.

## Alternatives (for the ADR)

1. **Ввести согласие как first-class сущность в шлюзе (рекуррентный путь внутри шлюза)** — recommended.
2. **Вынести подписки в отдельный сервис (отдельный компонент)** — more isolation but duplicates status machine, idempotency, outbox, trust; more cost.
3. **Реализовать как серию обычных C2B платежей, инициируемых ТСП по расписанию (без согласия в СБП)** — no real consent mechanism, violates НСПК rules / 161-ФЗ, risky (списание без согласия), rejected.
4. **Вендорская «коробка» подписок** — vendor lock-in, closed logic, rejected per AD-007/AD-008.
5. **Расширить только API, делегировав согласие внешней системе** — leaks consent out of payment contour, violates AD-001.

## Contract changes (backward compatible)

New endpoints (additive, no breaking changes):
- `POST /v1/consents` — create consent (ТСП → шлюз → ОПКЦ).
- `GET /v1/consents/{consentId}` — consent status.
- `POST /v1/consents/{consentId}/revoke` — revoke consent (ТСП-initiated) — or `DELETE`.
- `POST /v1/consents/{consentId}/payments` — initiate recurring debit referencing consent (instead of QR). Or extend `POST /v1/payments` with `consentId` + `paymentType: recurring`.
- Webhook events: `consent.activated`, `consent.revoked`, `consent.expired`, `payment.completed` (recurring).

Backward compat: existing `POST /v1/payments` (QR) unchanged; new fields optional. New enum value in `status`? No — the payment status enum stays the same; recurring payments also go through PAID→CREDITED→COMPLETED. The `qrType` field: recurring payments won't have QR. So I should add an optional field `paymentMethod` or `consentId` rather than changing existing required fields.

Let me think about the cleanest additive design:
- Extend `POST /v1/payments` request with optional `consentId` (string). If present, it's a recurring debit; if absent, existing QR flow. This is backward compatible (optional field).
- Add `POST /v1/consents`, `GET /v1/consents/{consentId}`, `POST /v1/consents/{consentId}/revoke`.
- Add new webhook event types.
- Add new error codes: `CONSENT_NOT_ACTIVE`, `CONSENT_LIMIT_EXCEEDED`, `CONSENT_REVOKED`.

Actually, there's a subtlety: consent creation requires the payer to confirm. So consent lifecycle: ТСП creates consent → status CREATED → payer confirms in bank app → НСПК notifies → status ACTIVE. So there's an async activation.

Let me also consider: is `consentId` on the payment request the right model, or should recurring debits be a separate resource `POST /v1/consents/{consentId}/payments`? I'll propose both in the contract but pick one as primary. Actually, to minimize API surface and be idiomatic, I'll extend `POST /v1/payments` with optional `consentId` (and keep QR as the default). This is the least breaking.

## NFR for recurring

- Consent activation (payer confirmation) — p95 latency from НСПК notification to ACTIVE state + webhook.
- Recurring debit initiation throughput — same 200 TPS base, but batch (billing cycle) peak: e.g., subscription renewals on 1st of month → peak 1000 TPS burst, sustained 500.
- Double debit = 0 (idempotency by consentId + billingPeriodId / debitKey).
- Consent limit enforcement: 100% debits within limits; limit breach blocked before init = 0 breaches.
- Revocation immediacy: debit blocked within ≤ 1 s of revocation; no debit after revocation = 0.
- Consent data retention: minimized, per 152-ФЗ.

## Acceptance criteria + rollback

Acceptance criteria (measurable):
- Сквозной сценарий: consent create → activate (mock НСПК) → recurring debit → PAID → CREDITED → webhook.
- Negative: debit after revocation → blocked (409/422), no НСПК call.
- Negative: debit exceeding consent limit → blocked.
- Negative: duplicate debit (same idempotency key) → no double debit.
- Negative: НСПК down during debit → payment stays CREATED/PAID per state machine, retried idempotently, reconciliation.
- Fitness: зачисление только из PAID (extended to recurring path).

Rollback:
- Feature flag on consent/recurring endpoints (disabled by default); existing QR flow untouched.
- Stop-new: disable `POST /v1/consents` and recurring debit initiation; already-active consents continue but no new debits.
- No data migration rollback; consents remain as audit data.
- Reversibility: the ADR should be reversible (feature flag + additive API). Consent entity is new; removing it is low-cost pre-production.

## Human architect decisions (open questions)

1. Is recurring C2B within THIS feature spine or a new initiative? (My assessment: same C2B spine, but confirm scope boundary — this changes the parent spine only if the business wants C2C-like "variable" debits.)
2. Exact СБП consent/debit protocol semantics (limits model: max amount per debit, max frequency, validity) — depends on НСПК documentation [ТРЕБУЕТ ПРОВЕРКИ].
3. Whether consent limits are validated at gateway, НСПК, or both (double enforcement / who is authoritative).
4. Payer consent UX (where payer confirms: in merchant's flow vs payer's bank app) — product decision.
5. Refund/dispute policy for recurring debits (chargeback-like flow) — business decision.
6. Rate-limiting and scheduling model for billing peaks — infrastructure decision.

Now let me figure out how much to write and in which files. I'll be thorough but follow repo conventions.

Let me now also read the remaining ADRs to match exact format. Let me read ADR-002 (full), ADR-003, ADR-004, ADR-005, ADR-006, ADR-007. And the rfp file and the ADR-001 to see exact template. I already have ADR-001 and partial ADR-002 from ARCHITECTURE.md. Let me read the actual ADR files to match format precisely (the .arch-handoff copies are identical to docs/adr presumably).

Actually I have enough of the format from ADR-001 (in ARCHITECTURE.md epic context) and the structure. But let me read ADR-007 (accepted) and ADR-005 to see the exact style, and confirm the ADR file format. Let me read a couple more files.

  `grep_search(pattern="\"nodes\"|\"flows\"|release/1.2|\"schema\"", glob="*.json")`
  `grep_search(pattern="calm|CALM", glob="*.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/rfp/vendor-rfp.md")`

Now I have a very thorough understanding. Let me also quickly check the rfp file and the ADR-003 and ADR-006 briefly to be complete, and check if there's a CALM JSON somewhere. Actually, let me check if there are any CALM JSON files in the repo (the calm skill might be used for actual modeling).

Let me do a quick grep for CALM JSON files and also check the .qwen/skills/calm/SKILL.md and the calm-prompts to see if there's a specific workflow I need to follow for "documentation-creation" etc. Actually, the calm skill's role is about CALM JSON modeling, but this repo uses markdown ADRs. 

Wait, let me reconsider. The calm skill's SKILL.md is in .qwen/skills/calm/SKILL.md. The .claude/skills/calm/ also exists. But there's no CALM JSON in the actual repo (docs are markdown). The calm skill is likely a red herring / or the "methodological skill" that the repo author intends to be used for the CALM modeling of the architecture. But the actual accepted artifacts are markdown ADRs + spine.

Actually, re-reading the task: "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." (The project may have methodological skills and tools installed — use them as intended.)

The relevant methodological approach in THIS repo is clearly the "spine + ADR + solutioning + NFR + contracts + state-machine" approach. The CALM skill is installed but I've loaded it and it's about CALM JSON (release/1.2). The repo does NOT contain CALM JSON models — it contains markdown. So the CALM skill is not the primary methodology here; the primary methodology is the spine/ADR approach visible in the files.

Actually, wait — let me reconsider. The path "calm-r1" suggests this is a benchmark cell where the CALM skill is being tested. But the actual content is СБП payment gateway. The CALM skill might be intended to help with the architecture modeling. However, the repo's own conventions (spine, ADR, solutioning) are what matter for "изменение принятых файлов решения тем способом, который принят в этом репозитории."

Let me verify there are no CALM JSON files to avoid missing a convention.

  `ask_user_question(questions=[{"question": "Рекуррентные C2B-списания (подписки СБП) — это расширение ТЕКУЩЕГО feature-spine «Платёжный шлюз СБП (C2B-приём)» или новая и)`

I now understand the full repository. The CALM CLI is installed in node_modules, but the actual accepted architecture artifacts are markdown ADRs + spine + solutioning + NFR + contracts + state machine. The CALM skill is a "methodological skill" but the repo uses the spine/ADR methodology for the actual decision artifacts.

The key insight: the repo's methodology is "spine + ADR + solutioning + NFR + contracts + state-machine". This is what I need to follow. The CALM skill/CLI is present but there are NO CALM JSON models in the repo — the architecture is documented in markdown. So I should NOT create CALM JSON; I should follow the repo's markdown conventions.

Actually wait, let me reconsider. The calm skill's first interaction says to read the calm-prompts. I've loaded the skill. But the actual repo artifacts are markdown. The task is a solution-architecture task, and the repo clearly has its own methodology (spine + ADR). I'll follow the repo's methodology, which is the "accepted way" of changing decision files.

I now have everything I need. Let me plan the concrete files and content.

## Deliverables (files)

I'll create/modify the following:

### New files:
1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md` — the main ADR.

### Modified files (accepted decision files, changed in the accepted way):
2. `ARCHITECTURE-SPINE.md` — add AD-009 invariant (Proposed status).
3. `docs/solutioning.md` — move "автоплатежи" from roadmap to scope; add recurring flow section; update component diagram and flows, ADR table, gates.
4. `docs/nfr.md` — add recurring NFR section.
5. `docs/contracts/tsp-api.md` — add consent endpoints + recurring payment fields + webhook events + error codes.
6. `openapi/tsp-api.yaml` — add consent paths + schemas (additive).
7. `docs/spec/state-machine.md` — add consent state machine + recurring payment path.
8. `docs/contracts/opkc-adapter.md` — add consent operations (createConsent, debitByConsent, etc.) marked [ТРЕБУЕТ ПРОВЕРКИ].
9. `README.md` — update document list.

That's a lot. Let me be judicious. The task's 7 deliverables need to be answered. The core artifact is the ADR-008. Then the contract changes (tsp-api + openapi), NFR, state machine, solutioning, spine.

I think I should also write a "package summary" document that directly answers the 7 questions in prose for the architecture board. But actually, the ADR + updated files together ARE the package. However, the task explicitly lists 7 things that "должно получиться" (should result). Some of these (like #1 assessment of significance, #2 impact, #7 human decisions) are best captured in a single "assessment + impact" section. 

I think the cleanest is to create a dedicated brief document `docs/proposals/recurring-c2b-debit.md` — but that introduces a new directory. Alternatively, I can put the full 7-point answer in the ADR-008 itself (which is natural: the ADR's "Context" section covers #1 and #2, "Decision" covers #3, "Alternatives/Consequences/Reversibility" cover #3, and I add explicit sections for #5/#6/#7). But the ADR template is fairly fixed.

Actually, I think the best approach, matching the repo's structure where `docs/solutioning.md` is the "full design" doc, is:

1. ADR-008 — the decision (with alternatives, consequences, reversibility, impact, human decisions as open questions).
2. A new solutioning extension OR fold recurring into solutioning.md.

Let me reconsider scope. The user wants a "пакет" (package) that can be "вынесено на архитектурное решение" (brought to architecture decision) AND "затем передано исполнителям" (then handed to implementers).

Given the repo conventions, the "package" naturally consists of:
- ADR-008 (the decision to be made by the architecture board).
- Updated contracts (tsp-api, openapi) — for the Spec gate A1.
- Updated state-machine — for A1.
- Updated NFR — for A4/A5.
- Updated solutioning — the full design.
- Updated spine (new invariant) — for the parent spine alignment.

I'll produce these. To directly answer all 7 questions in a way that's easy to consume, I'll write the ADR-008 to be the central "decision package" that contains the assessment (#1), impact (#2), decision+alternatives+consequences+reversibility (#3), and references to the contract/NFR/state-machine changes (#4, #5), plus acceptance/rollback (#6) and human decisions (#7).

Actually, acceptance criteria and rollback in this repo live in solutioning.md (§7 gates, §8 rollback). So I'll update solutioning.md for #6. And #7 (human decisions) = open questions in the ADR + solutioning §10.

Let me define the actual content carefully.

## Content design

### Route/значимость assessment (#1)

The change: "Рекуррентные C2B-списания по согласию плательщика (подписки СБП)".

Current state: each payment requires QR + payer action. This is a new product capability (recurring debit / merchant-initiated), touching:
- New domain entity: согласие (consent/mandate).
- New payment path (skip QR).
- Contract extension (additive).
- New NFRs (billing peaks).
- New regulatory dimension (consent = ПДн, 152-ФЗ; 161-ФЗ for recurring; НСПК subscription rules).

Значимость: I'd assess this as **Critical** (like the base initiative at 11/15), because:
- Financial impact (recurring debits = ongoing revenue, but also double-debit risk).
- Regulatory (consent handling, revocation rights, 161-ФЗ / 152-ФЗ).
- State machine and idempotency invariants are directly touched (extension, not break).
- New external dependency (НСПК subscription protocol — [ТРЕБУЕТ ПРОВЕРКИ]).

But actually, is it Critical or Major? It's an extension of an already-Critical system. The core invariants (isolation, state machine, idempotency, PAID-gating) are preserved. But consent introduces a new financial-meaning entity and a new debit path. I'd call it **Critical** (значимость ~10/15), requiring full solutioning + new ADR + contract changes, but NOT a rewrite of the base. The depth of design: a new ADR (ADR-008), extension of state machine, additive contract, new NFRs. The route is the same "Critical" route with gates A0-A5, but the change rides on the existing solution.

Actually, let me reconsider the route more carefully. The repo's README says "Маршрут: Critical (значимость 11/15)". The solutioning says "Маршрут: Critical". The route is a defined concept (Critical/Major/Moderate/Minor). 

For recurring debits, the significance is high but it's an incremental extension. I'll assess: **Critical** (значимость 10/15) — new financial capability, consent entity (ПДн), new debit path touching the core status machine, new external protocol dependency, double-debit risk. Design depth: deep — full ADR + state machine extension + contract + NFR, but scoped as an extension (not a new initiative). This maps to the same gate route A0→A5.

### Impact on invariants (#2)

Table: for each AD-001..AD-008, whether affected.

- AD-001 (изоляция) — **не меняется**: consent/recurring logic stays in the gateway.
- AD-002 (статусная машина) — **расширяется**: consent gets its own state machine; payment gains a recurring path (skip QR_ISSUED). The rule (atomic transition + outbox) unchanged.
- AD-003 (идемпотентность) — **расширяется**: consent create/revoke and debit init need idempotency; recurring НСПК events need eventId dedup. The rule unchanged.
- AD-004 (единственный адаптер ОПКЦ) — **не меняется**: consent/debit protocol through same adapter.
- AD-005 (зачисление только из PAID) — **не меняется и критично**: recurring debit credits only from confirmed НСПК status. No "платежи из воздуха" from consent alone.
- AD-006 (trust-зоны) — **не меняется**: consent is ПДн, stored in secure zones (already covered).
- AD-007 (НПС/КИИ/ПДн) — **расширяется**: consent adds 152-ФЗ (consent storage, revocation, minimization); recurring debit adds НПС rules.
- AD-008 (стратегия реализации) — **не меняется**: core contract-independent; vendor adapter handles subscription protocol.

New invariant proposed: **AD-009** — рекуррентное списание только по активному согласию.

### ADR-008 decision (#3)

Decision: introduce "согласие" as a first-class entity in the gateway, with its own state machine; add a recurring debit path that references an active consent; keep AD-005 (credit only from PAID).

Alternatives:
1. Согласие как first-class сущность в шлюзе + рекуррентный путь (выбрано).
2. Отдельный сервис подписок (новый компонент) — изоляция, но дублирование статусной машины/outbox/идемпотентности/trust; выше TCO.
3. Эмулировать подписки серией обычных QR-платежей по расписанию ТСП (без согласия в СБП) — нет юридического согласия, нарушение 161-ФЗ/правил НСПК, риск списания без согласия; rejected.
4. Вендорская «коробка» подписок — vendor lock-in, закрытая логика, против AD-007/AD-008.
5. Делегировать согласие внешней системе — утечка согласия за платёжный контур, нарушение AD-001.

Consequences:
Positive: новый продукт (подписки), единая статусная модель, переиспользование outbox/идемпотентности/сверки, AD-005 сохраняет защиту от «платежей из воздуха».
Negative: новое финансовое состояние (согласие) — увеличение сложности статусной модели; новые ПДн-обязательства (152-ФЗ); пиковые нагрузки подписок (billing cycle); зависимость от протокола НСПК подписок [ТРЕБУЕТ ПРОВЕРКИ].

Reversibility: **reversible** на этапе проектирования/до кода; после включения — отзыв согласий + feature flag; согласие как сущность — additive, откат = stop-new без потери QR-функций.

### Contract changes (#4)

tsp-api.md + openapi: additive only.

New endpoints:
- `POST /v1/consents` — create consent (async activation).
- `GET /v1/consents/{consentId}` — status.
- `POST /v1/consents/{consentId}/revoke` — revoke (ТСП или банк).
- Extend `POST /v1/payments` with optional `consentId` (and `paymentType: "recurring"`) — when present, debit by consent (no QR).

New webhook events: `consent.activated`, `consent.revoked`, `consent.expired`, plus existing `payment.completed`/`payment.failed` reused for recurring debits.

New error codes: `CONSENT_NOT_FOUND` (404), `CONSENT_NOT_ACTIVE` (422), `CONSENT_REVOKED` (422), `CONSENT_LIMIT_EXCEEDED` (422), `CONSENT_EXPIRED` (422).

Backward compat guarantees: no changes to existing paths/fields; new fields optional; no change to existing enum values (payment status enum unchanged — recurring debits use same PAID→CREDITED→COMPLETED). Idempotency-Key applies to consents too.

### NFR (#5)

Add a section to nfr.md:
- Consent activation: p95 ≤ 5 s from НСПК event to ACTIVE + webhook (mock).
- Recurring debit initiation: p95 < 500 ms (same as QR registration).
- Billing-cycle peak throughput: sustained 500 TPS, burst 1000 TPS (batch on 1st of month).
- Double debit = 0 (idempotency by consentId + billingPeriodKey/debitKey).
- Limit enforcement: 100% debits within consent limits; limit breach = 0 (blocked pre-init).
- Revocation immediacy: no debit after revocation; blocked ≤ 1 s; = 0 post-revocation debits.
- Consent ПДн: storage minimized, encryption at rest, masking; revocation propagates to all layers.

### Acceptance criteria + rollback (#6)

Acceptance criteria (measurable, testable):
- Happy: consent create → payer activates (mock) → recurring debit → PAID → CREDITED → webhook payment.completed.
- Negative: debit after revoke → 422 CONSENT_REVOKED, no НСПК call.
- Negative: debit over limit → 422 CONSENT_LIMIT_EXCEEDED.
- Negative: duplicate debit (same Idempotency-Key) → no double debit.
- Negative: НСПК down → payment stays CREATED (or a pending state), idempotent retry, reconciliation catches.
- Fitness: зачисление рекуррентного платежа только из PAID (extends AD-005).
- Fitness: переход согласия REVOKED терминален.

Rollback:
- Feature flag on consent + recurring endpoints (off by default); QR flow untouched.
- Stop-new: disable `POST /v1/consents` + recurring debit init; active consents and already-created debits drain.
- No reverse data migration; consents remain as audit records.
- Reversibility: additive API + flag ⇒ low-cost rollback pre-prod; post-prod rollback = stop-new + retain data.

### Human decisions (#7)

1. Scope boundary: recurring C2B stays in THIS feature spine vs new initiative (affects parent spine; my recommendation: stays, as it's still C2B).
2. Consent limits model (per-debit max, frequency, validity) — authoritative source (gateway vs НСПК vs both) — depends on НСПК docs [ТРЕБУЕТ ПРОВЕРКИ].
3. Payer consent UX: where payer confirms (merchant app vs payer's bank app) — product decision.
4. Refund/dispute policy for recurring debits — business decision.
5. Scheduling/batch model for billing peaks + capacity commitment — infra/business decision.

Now let me write all the files. I'll write them carefully to match repo conventions (Russian, markdown, table formats, status fields, [ТРЕБУЕТ ПРОВЕРКИ] markers).

Let me start with the ADR-008. I'll use a slug similar to existing: `ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md`. Actually existing slugs are descriptive latin transliteration. I'll use `ADR-008-rekurrentnye-c2b-spisaniya-podpiski-soglasie.md` or simpler `ADR-008-rekurrentnye-c2b-spisaniya-podpiski.md`.

Let me determine the exact next ADR number: ADR-001..007 exist, so ADR-008 is next. Good.

Now, let me think about whether I should also update the `.arch-handoff/` files. The task says "передать исполнителям" is AFTER the architecture decision. The `.arch-handoff/` is generated for the code harness at "walking skeleton" stage. Since this change is being brought to architecture decision FIRST (not yet approved), I should NOT regenerate `.arch-handoff/` — that happens after approval + stack selection. The CONSTRAINTS.yaml says "После выбора стека и начала реализации handoff перегенерирует констрейнты". So .arch-handoff is not part of my scope now.

So my files:
1. Create `docs/adr/ADR-008-...md`.
2. Edit `ARCHITECTURE-SPINE.md` (add AD-009).
3. Edit `docs/solutioning.md`.
4. Edit `docs/nfr.md`.
5. Edit `docs/contracts/tsp-api.md`.
6. Edit `openapi/tsp-api.yaml`.
7. Edit `docs/spec/state-machine.md`.
8. Edit `docs/contracts/opkc-adapter.md`.
9. Edit `README.md`.

That's comprehensive. Let me be efficient but thorough.

Let me write the ADR first. I need to write it following the ADR template exactly.

Actually, let me reconsider the amount of files. The task is large and asks for a complete package. I'll do all 9 files but keep each edit focused and additive. Let me be careful not to break the CONSTRAINTS.yaml fitness rules:
- `adr-no-placeholders`: `docs/adr/*.md` must NOT contain `<!--`. So my ADR must not use HTML comments. The existing ADRs (like ADR-007) don't use `<!--`. Good.
- `nfr-measurable`: `docs/nfr.md` must contain '99,95'. Keep that.
- `abs-credit-only-from-paid`: ADR-005 must contain 'только из состояния `PAID`'. I won't touch ADR-005.
- spine must not contain TODO/TBD/XXX (warn).

Let me also make sure my openapi changes are valid YAML and additive.

Let me now write the ADR-008 file.

For the ADR, I'll include the assessment (#1) and impact (#2) in the Context section (or as a dedicated section), decision + alternatives + consequences + reversibility (#3), references to contract/NFR/state-machine (#4/#5), acceptance + rollback (#6), open questions (#7).

Actually, to precisely answer all 7 points, I'll structure ADR-008 with sections:
- Context (includes route assessment)
- Decision
- Impact on accepted architecture (invariants)
- Alternatives Considered
- Consequences
- Reversibility
- Contract changes (summary + pointer)
- NFR (summary + pointer)
- Acceptance criteria & rollback
- Open questions (human decisions)
- References

This is richer than the base ADR template but consistent — ADR-007 also had extra sections (A3 Decision). So it's fine.

Let me write it now.

Actually, I want to be careful about length. This is a substantial document. I'll write it thoroughly but not bloated.

Let me draft the ADR-008 content.

---

# ADR-008. Рекуррентные C2B-списания: подписки СБП по согласию плательщика

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур) + владелец продукта (подписки)
- Related: ADR-002, ADR-004, ADR-005, AD-002, AD-003, AD-005, AD-009 (предлагаемый)

## Context

... route assessment, current state, business need ...

## Decision

... consent entity + recurring debit path ...

## Impact on accepted architecture

... AD-001..AD-008 table + new AD-009 ...

## Alternatives Considered

...

## Consequences

...

## Reversibility

...

## Changes to contracts and NFR (указатели)

...

## Acceptance criteria and rollback

...

## Open questions (human decisions)

...

## References

...

---

Now let me write everything. I'll produce the files.

Let me start writing files. I'll do the ADR first, then the edits.

Actually, I realize I should think carefully about whether "согласие" (consent) in СБП is created by the ТСП or by the payer. In СБП subscriptions:
- The ТСП (merchant) initiates subscription creation with a link/QR that the payer confirms in their bank app.
- The consent is a НСПК-level object linking payer account ↔ merchant ↔ limits.

So the flow: ТСП → шлюз → ОПКЦ → создание "подписки" → плательщик подтверждает в своём банке → ОПКЦ нотифицирует активацию.

The recurring debit: ТСП → шлюз (consentId + amount + idempotency) → ОПКЦ (списание по согласию) → банк плательщика списывает → ОПКЦ нотифицирует PAID → шлюз → АБС зачисление → COMPLETED.

This matches the model. Good.

I'll write it now. Let me create the ADR file.

Let me also carefully decide on the exact naming of consent states and recurring payment states.

Consent states:
- `CREATED` — создан, ожидает подтверждения плательщика.
- `ACTIVE` — подтверждён плательщиком, действует.
- `REVOKED` — отозван (плательщиком или ТСП), терминальный.
- `EXPIRED` — истёк срок действия, терминальный.
- (optional) `SUSPENDED` — приостановлен (например, по AML) — I'll mention as optional, keep minimal. Actually let me keep it minimal: CREATED → ACTIVE → REVOKED/EXPIRED, plus a technical `ACTIVATION_PENDING`? No, CREATED already covers "awaiting confirmation". Keep minimal: CREATED, ACTIVE, REVOKED, EXPIRED.

Recurring payment states: reuse existing payment states. Path: `CREATED` → `PAID` (skip QR_ISSUED) → `CREDITED` → `COMPLETED`; terminal `FAILED`. Note: no QR, no EXPIRED (no TTL QR), but could have a "debit pending" state. Actually let me define the recurring path clearly:

`CREATED` (debit requested to ОПКЦ) → `PAID` (confirmed) → `CREDITED` → `COMPLETED`. Terminal: `FAILED` (rejected). No `QR_ISSUED`, no `EXPIRED`.

This means the payment state machine gains a new transition: T1 → CREATED; then a new transition `CREATED → PAID` (recurring path, when debit confirmed without QR) vs existing `CREATED → QR_ISSUED` (QR path). And existing `QR_ISSUED → PAID`.

So I need to add transitions to state-machine.md:
- T13: `CREATED → PAID` (recurring debit confirmed by НСПК; no QR) — guard: payment has `consentId`, consent ACTIVE, amount within limits.
- T14: `CREATED → FAILED` (debit rejected).

And add consent state machine transitions:
- C1: `— → CREATED` (POST /consents).
- C2: `CREATED → ACTIVE` (НСПК event consent.activated; payer confirmed).
- C3: `CREATED → REVOKED` (revoke before activation / activation timeout).
- C4: `ACTIVE → REVOKED` (payer or ТСП revoke).
- C5: `ACTIVE → EXPIRED` (validity period ends).
- C6: `CREATED → EXPIRED` (activation timeout).

Good.

Now for the ОПКЦ adapter contract (opkc-adapter.md), add consent operations:
- `createConsent` (ядро → адаптер): `reference` (= consentId ядра), `tspId`, limits (maxAmount, maxFrequency, validUntil), payer identifier. Returns `ACCEPTED` + `consentOpcId`.
- `revokeConsent` (ядро → адаптер): `reference` (= consentId), `reason`.
- `debitByConsent` (ядро → адаптер): `reference` (= paymentId ядра), `consentOpcId`/`consentId`, `amount`, `billingPeriodKey`. Returns `ACCEPTED`.
- Events: `consent.activated`, `consent.revoked`, `consent.expired`, `consent.rejected`; `payment.debited` (or reuse `payment.paid` for recurring).

Actually, the existing `payment.paid` event already carries `qrId`. For recurring there's no qrId — instead a consent reference. I'll note that `payment.paid` for recurring carries `consentRef`/`reference` instead of `qrId`. Or add a new event. To keep minimal and consistent, I'll extend `payment.paid` to be usable for both (qrId optional; consentRef optional). Mark protocol details [ТРЕБУЕТ ПРОВЕРКИ].

Let me now write everything. I'll produce a comprehensive but clean set of edits.

One more consideration: the `openapi/tsp-api.yaml` is quite minimal currently (only /v1/payments post + get). The docs/contracts/tsp-api.md is richer. The task says "Изменения контрактов (`openapi/tsp-api.yaml`)". So I need to update the OpenAPI file. I'll add consent paths and extend the PaymentRequest schema with optional `consentId`, and add Consent schemas. I'll keep it additive.

Let me write the openapi file fully (rewrite it, since I need to add paths and schemas — but I should preserve existing content exactly and add). Actually, editing is safer with edit tool, but rewriting the whole file with write_file is cleaner given I'm adding a lot. But write_file requires the file's absence or current text established. I've read it, so I can rewrite it with write_file. Actually, the guidance says use edit for targeted changes; but for a substantial restructure, writing the whole file is acceptable. However, "blind overwrites are rejected" — I've read the file so it's fine. But to be safe and show minimal diffs, I'll use edit to append new paths and schemas, and modify PaymentRequest. Actually the file is small; I'll rewrite it fully to keep it coherent. Let me use write_file for openapi (I've read it, so it's established).

Hmm, but rewriting risks accidentally changing something. The file is small and I have its exact content. I'll rewrite carefully preserving everything and adding.

Actually, let me use `edit` for the openapi to be safe and minimal. I'll:
1. Edit PaymentRequest schema to add `consentId` and `paymentType` optional fields.
2. Add new paths for consents (insert before the final `components:` or after the existing paths).
3. Add new schemas.

Let me plan the edit operations precisely.

Current openapi content:
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

I'll rewrite it fully to add the consent paths and schemas. Since it's a small file and I want to add significant content, rewriting is cleaner. I'll use write_file (I've read it, so it's fine).

Actually, let me use write_file for openapi since I'm restructuring it. For the markdown docs, I'll use edit to append/modify targeted sections.

Let me now also decide: should I bump the openapi version? The info.version is 0.1.0. I'll keep it 0.1.0 or bump to 0.2.0. The contract is additive. I'll bump to 0.2.0 to signal the new capability, but keep paths backward compatible. Actually the tsp-api.md says "Версия контракта: 0.1". I'll note v0.2 draft (additive). Let me bump info.version to 0.2.0.

Now let me write all files. I'll begin.

Let me write the ADR-008 first.

I'll be thorough in the ADR since it's the centerpiece.

Let me carefully write the impact table mapping each invariant.

Now writing. I'll produce the ADR file content.

For the "route" assessment, I'll phrase it as: маршрут Critical (значимость 10/15) — подписной сценарий затрагивает финансовую модель, статусную машину и новый класс ПДн (согласие), но как расширение существующего решения, а не новая инициатива; глубина проектирования — полный ADR + расширение Spec (статусная машина, контракты, NFR) без изменения AD-001..AD-008.

Let me write it.

I need to be mindful of the "adr-no-placeholders" fitness rule: `docs/adr/*.md` must not contain `<!--`. So no HTML comments in ADR. Good, I won't use them.

Let me write everything now. I'll do multiple write/edit in sequence. Since edits are independent files, but I want to be careful. I'll do them in a logical order.

Let me write the ADR file first.
I've now read the full repository. I understand the accepted methodology: a **spine** (`ARCHITECTURE-SPINE.md`, инварианты AD-001…AD-008) + **ADR** (`docs/adr/ADR-00X-*.md`) + **solutioning** + **NFR** + **контракты** (`docs/contracts/*.md`, `openapi/tsp-api.yaml`) + **статусная машина** (`docs/spec/state-machine.md`). Всё с маркерами статусов (`Proposed`/`Accepted`/`[ADOPTED]`) и `[ТРЕБУЕТ ПРОВЕРКИ]` для внешних входов НСПК.

Перед началом зафиксирую план и подтверждение по одному ключевому допущению о границе scope — это влияет на весь пакет.

  `write_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-p, content="# ADR-008. Рекуррентные C2B-списания: подписки СБП по согласию плательщика\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: solution-arc)`

The user confirmed:
1. Scope: extension of current spine (recurring C2B stays in scope, add AD-009).
2. Consent UX: payer confirms in their bank app (standard СБП subscription scenario).

Now I'll proceed to write the architectural package. Let me create all files.

Let me write the ADR-008 first.
Принято. Граница — расширение текущего spine (AD-009 добавляется, AD-001…AD-008 сохраняются), согласие плательщик подтверждает в приложении своего банка. Начинаю готовить пакет.

Создаю ADR-008:

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now let me update the ARCHITECTURE-SPINE.md to add AD-009 and update the Deferred section (remove автоплатежи from roadmap? Actually автоплатежи is in solutioning.md §1 roadmap, and in the Deferred section of the spine it's not listed. Let me check the spine's Deferred section again:

Deferred:
- Мультивалютность...
- C2C-переводы и выплаты B2C/B2B...
- Диспуты/претензии...

So "автоплатежи" is NOT in the spine's Deferred list — it's in solutioning.md §1 as "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

So for the spine, I just need to add AD-009. Let me add it after AD-008.

Let me edit the spine to add AD-009 before the "## Deferred" section.
Добавляю инвариант AD-009 в spine:

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/spec/state-machine.md", old_string="| `NOTIFY_PENDING` | Вебхук ТСП поставлен в очередь (доставка — outbox/нотификатор) |\n\n## 2. Таблица переходов", new_string="| `NOTIFY_PENDING` | Вебхук ТСП поставлен в очередь (доставка — outbox/нотификатор) |\n\n### Согласие (consent) — финансово-значимая сущнос)`

Now let me update the state machine spec (`docs/spec/state-machine.md`). I need to add:
1. Consent states section.
2. Consent transitions table.
3. Recurring payment path transitions (T13: CREATED → PAID, T14: CREATED → FAILED).
4. Update forbidden transitions section.
5. Update idempotency table (billingPeriodKey).
6. Update reconciliation for consents.
7. Update TSP API mapping.

Let me edit the state-machine.md. I'll add the consent states after section 1 (or a new section), add transitions, etc.

Let me read the current state-machine.md again — I already have it. I'll make targeted edits.

First, add consent state machine as a new section. The doc has sections:
1. Состояния (financial + technical)
2. Таблица переходов
3. Запрещённые переходы
4. Обработка повторных триггеров
5. Сверка и восстановление
6. Согласованность с API ТСП

I'll add:
- Section 1.5 or a new "Состояния согласия" subsection.
- Add consent transitions as a new table (section 2.1 or extend section 2).
- Add recurring payment transitions T13/T14 to the transitions table.
- Update section 3 (forbidden) to add consent invariants.
- Update section 4 idempotency table.
- Update section 5 reconciliation.
- Update section 6 mapping.

Let me do targeted edits. I'll append new content in the right places.

Actually, to keep it clean and avoid too many fragile edits, I'll:
1. Add a new subsection under section 1 for consent states.
2. Add T13/T14 to the transitions table (append rows before section 3).
3. Add a new subsection "Согласие — таблица переходов" after the payment transitions table.
4. Update forbidden transitions.
5. Update idempotency table.
6. Update reconciliation.
7. Update API mapping.

Let me do these edits. First, add consent states after the "Технические" table (end of section 1).

The section 1 ends with the technical states table:
```
### Технические (внутренние, наружу не выставляются)

| Состояние | Смысл |
|---|---|
| `ABS_PENDING` | Зачисление в АБС инициировано, ждём подтверждения (ретраи) |
| `NOTIFY_PENDING` | Вебхук ТСП поставлен в очередь (доставка — outbox/нотификатор) |
```

I'll add a new section 1.x after this.

Let me craft the edits carefully using unique context.

Edit 1: Add consent states after technical states table and before "## 2. Таблица переходов".

Actually the text between technical states and section 2 is:
```
| `NOTIFY_PENDING` | Вебхук ТСП поставлен в очередь (доставка — outbox/нотификатор) |

## 2. Таблица переходов
```

I'll insert consent states section between.

Let me do the edits.
Расширяю спецификацию статусной машины (`docs/spec/state-machine.md`):

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/spec/state-machine.md", new_string="| T12 | `COMPLETED` | (остаётся `COMPLETED`) | **частичный** возврат завершён | сумма возврата < суммы платежа | запись в `refunds[]`, вебх, old_string="| T12 | `COMPLETED` | (остаётся `COMPLETED`) | **частичный** возврат завершён | сумма возврата < суммы платежа | запись в `refunds[]`, вебх)`

Now add T13/T14 to the payment transitions table and add the consent transitions table after the payment transitions table.

The payment transitions table ends with T12:
```
| T12 | `COMPLETED` | (остаётся `COMPLETED`) | **частичный** возврат завершён | сумма возврата < суммы платежа | запись в `refunds[]`, вебхук `refund.completed` |

## 3. Запрещённые переходы (инварианты)
```

I'll insert T13/T14 before section 3, and add a consent transitions table.

  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/spec/state-machine.md", offset=75, limit=40)`

Now update the forbidden transitions section (section 3) to add consent invariants, and update idempotency (section 4), reconciliation (section 5), and API mapping (section 6).

Let me read the current state of section 3-6 to get exact text.

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/spec/state-machine.md", old_string="- `REFUNDED` достижим **только** из `COMPLETED` (только после зачисления).\n- Сумма и реквизиты платежа иммутабельны после `QR_ISSUED` (T2), new_string="- `REFUNDED` достижим **только** из `COMPLETED` (только после зачисления).\n- Сумма и реквизиты платежа иммутабельны после `QR_ISSUED` (T2))`
  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/spec/state-machine.md", new_string="## 5. Сверка и восстановление\n\n- Открытые состояния (`QR_ISSUED`, `PAID`, `ABS_PENDING`) — кандидаты для сверки с НСПК и АБС (ADR-004, AD, old_string="## 5. Сверка и восстановление\n\n- Открытые состояния (`QR_ISSUED`, `PAID`, `ABS_PENDING`) — кандидаты для сверки с НСПК и АБС (ADR-004, AD)`

Now update sections 5 and 6 (reconciliation and API mapping).

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/contracts/tsp-api.md", new_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n, old_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n)`

Now update the TSP API contract (`docs/contracts/tsp-api.md`). I need to:
1. Add §3.6 (consent endpoints) and §3.7 (recurring payment) after §3.5.
2. Update the payment request in §3.2 to mention optional `consentId`/`paymentType` — actually I'll add a note in §3.2 or add a new subsection. Let me add new sections 3.6 and 3.7.
3. Update error codes (§4) to add consent error codes.
4. Update webhooks (§5) to add consent events.

Let me make targeted edits.

First, add new error codes in §4. The current §4 has canonical codes list. Let me find and update it.

Current §4 text:
```
Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.
```

I'll add consent codes: `CONSENT_NOT_FOUND` (404), `CONSENT_NOT_ACTIVE` (422), `CONSENT_REVOKED` (422), `CONSENT_EXPIRED` (422), `CONSENT_LIMIT_EXCEEDED` (422).

Let me update it.

Actually, I'll add the new sections (3.6, 3.7) after §3.5, then update §4 codes, then update §5 webhooks. Let me do them in order.

First, insert §3.6 and §3.7 after §3.5. §3.5 text:
```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`

## 4. Ошибки (RFC 9457, Problem Details)
```

I'll insert between §3.5 and §4.
Расширяю контракт ТСП (`docs/contracts/tsp-api.md`) — новые разделы согласий и рекуррентного списания:

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/contracts/tsp-api.md", new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`

Now update the error codes in §4, and the webhooks in §5. Let me find the exact text for §4 canonical codes and §5 events.

Current §4 canonical codes:
```
Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.
```

Update to add consent codes.

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/contracts/tsp-api.md", new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`

Now update §5 webhooks events to add consent events. Current §5 events list:
```
События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
```

Add consent events.

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/contracts/tsp-api.md", new_string="Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (AD, old_string="Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (AD)`

Now I should also add a note to §3.2 (create payment) about the optional `consentId`/`paymentType`. Actually, §3.7 already references it, and I described it as extension. But to be thorough, let me add a short note in §3.2. Actually, §3.7 is sufficient and I referenced it. But let me check §3.2 to add a pointer. The §3.2 rules say "amount > 0; ... после создания сумма и реквизиты иммутабельны (ADR-002)".

I think the contract is complete. Now let me also update §6 (versioning) or §7 open questions if needed. Actually §7 open questions of tsp-api.md — let me check if I should add consent-related open questions. There's already "Отмена QR до оплаты". I could add a note about consent limit source. But that's already captured in ADR-008 §8. I'll leave tsp-api §7 as is, or add one line. Let me not over-edit.

Actually, let me add a small note in §3.2 to point to §3.7 for recurring. Let me check the exact §3.2 content end.

§3.2 ends with:
```
Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (ADR-002). Максимальная сумма — по лимитам НСПК [ТРЕБУЕТ ПРОВЕРКИ].
```

I'll add a sentence: "Для рекуррентного списания вместо `qrType` передаётся `consentId` — см. §3.7."

Let me do that edit.

  `write_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/openapi/tsp-api.yaml", content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\npaths:\n  /v1/payments:\n    post:\n      operationId: createPayment\)`

Now update the OpenAPI YAML. I'll rewrite the whole file with the additive consent paths and extended schemas, keeping existing content intact.

Let me write the full openapi file.
Обновляю `openapi/tsp-api.yaml` (аддитивно, версия 0.2.0):

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/contracts/opkc-adapter.md", new_string="| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |\n| `getReconciliationReport` | вып, old_string="| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |\n| `getReconciliationReport` | вып)`

Now update the ОПКЦ adapter contract (`docs/contracts/opkc-adapter.md`) to add consent operations and events. Mark protocol details [ТРЕБУЕТ ПРОВЕРКИ].

The current §3 table has methods. I'll add consent operations to §3 and events to §4.

Let me add to §3 (sync operations table) new rows: `createConsent`, `revokeConsent`, `debitByConsent` (or `createDebitByConsent`).

And §4 events: `consent.activated`, `consent.revoked`, `consent.expired`, `consent.rejected`. And note `payment.paid` can be triggered by recurring debit (consentRef instead of qrId).

Let me edit §3 table. The table ends with:
```
| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |
```

Add rows after it.

Actually, let me read the current opkc-adapter.md §3 and §4 to get exact text (I already have it). Let me edit.

§3 table current (from my earlier read):
```
| Метод | Направление смысла | Ключевые поля запроса | Ответ | Таймаут (p99.9) |
|---|---|---|---|---|
| `registerTsp` | регистрация/активация ТСП в ОПКЦ | `tspId` (ядро), реквизиты ТСП, `reference` | `jobId`, статус `ACCEPTED` (результат — событием) | 5 c |
| `createPaymentLink` | создание QR/ссылки | `reference` (= `paymentId` ядра), `amount` (копейки), `currency`, `qrType`, `ttlSeconds?`, `purpose?`, `redirectUrl?` | `qrId`, `qrUrl`, `expiresAt` | 3 c |
| `getPaymentStatus` | запрос статуса по `qrId` (сверка/опрос) | `qrId` | статус ОПКЦ: `PAID` / `PENDING` / `REJECTED` / `EXPIRED` / `UNKNOWN`, `paidAmount?`, `paidAt?` | 3 c |
| `cancelPaymentLink` | закрытие/отмена ссылки (TTL, отмена ТСП) | `qrId`, `reason` | `CANCELLED` | 3 c |
| `createRefund` | регистрация возврата в ОПКЦ | `reference` (= `refundId` ядра), `qrId`, `amount` | `ACCEPTED` (результат — событием) | 5 c |
| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |
| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |
```

I'll add consent rows.
Расширяю контракт адаптера ОПКЦ (`docs/contracts/opkc-adapter.md`):

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/contracts/opkc-adapter.md", new_string="| Тип события | Смысл | Ключевые поля |\n|---|---|---|\n| `payment.paid` | платёж подтверждён ОПКЦ (QR или рекуррентное списание) | `refere, old_string="| Тип события | Смысл | Ключевые поля |\n|---|---|---|\n| `payment.paid` | платёж подтверждён ОПКЦ | `qrId`, `reference` (= `paymentId`), `)`

Now add consent events to §4. Current §4 events table:
```
| Тип события | Смысл | Ключевые поля |
|---|---|---|
| `payment.paid` | платёж подтверждён ОПКЦ | `qrId`, `reference` (= `paymentId`), `amount`, `paidAt` |
| `payment.rejected` | платёж отклонён | `qrId`, `reference`, `reasonCode` (нормализованный), `reasonText` |
| `payment.expired` | ссылка истекла по TTL | `qrId`, `reference` |
| `tsp.registered` | ТСП активирован в ОПКЦ | `reference` (= `tspId` ядра) |
| `tsp.rejected` | ТСП отклонён ОПКЦ | `reference`, `reasonCode`, `reasonText` |
| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |
| `refund.rejected` | возврат отклонён | `refundRef`, `reasonCode`, `reasonText` |
| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |
```

I'll add consent events and a note that `payment.paid` for recurring carries consentRef instead of qrId.

Let me edit to add new event types and modify `payment.paid` description.

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/nfr.md", new_string="| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |\n\n## 7. Рекуррентные списания и согласия (подписки СБП)\n\nИзмерим, old_string="| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |\n\n## Зависимости (внешние входы для NFR)")`

Now update the NFR document (`docs/nfr.md`) to add a new section §7 for recurring debits. I'll add it before the "Зависимости" section.

Current nfr.md ends with §6 (Наблюдаемость) then "## Зависимости (внешние входы для NFR)".

I'll insert §7 after §6 and before "## Зависимости". Let me find exact text.

§6 ends:
```
| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |

## Зависимости (внешние входы для NFR)
```

I'll insert §7 between them.
Добавляю NFR для рекуррентных списаний (`docs/nfr.md`):

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/solutioning.md", new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты, **рекуррентные сп, old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop)`

Now update `docs/solutioning.md`:
1. §1: move "автоплатежи" from roadmap to in-scope.
2. Add a new section for recurring C2B flow (consent + recurring debit).
3. Update the ADR table (§5) to include ADR-008.
4. Update §7 gates (acceptance criteria) and §8 rollback plan.
5. Update §10 open questions.

Let me make targeted edits.

First, §1: "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

Change to note that автоплатежи (подписки) теперь в scope (ADR-008), остальное остаётся вне.

Let me edit §1.
Обновляю `docs/solutioning.md`:

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/solutioning.md", new_string="    Note over G: сбой на шаге → компенсация (отмена АБС-списания / повтор регистрации в НСПК / DLQ + runbook)\n```\n\n### 4.3 Создание и ак, old_string="    Note over G: сбой на шаге → компенсация (отмена АБС-списания / повтор регистрации в НСПК / DLQ + runbook)\n```\n\n## 5. Разбиение на ре)`

Now add a new section for recurring flows after §4.2 (Возврат). Let me find the location. §4.2 ends with the note about сбой на шаге. Then §5 "Разбиение на решения (ADR)".

Let me add §4.3 (согласие) and §4.4 (рекуррентное списание) before §5.

Actually, let me look at the structure. §4 has 4.1 and 4.2. I'll add 4.3 (создание и активация согласия) and 4.4 (рекуррентное списание). Then update §5 ADR table, §7 gates, §8 rollback, §10 open questions.

Let me find the exact text around §4.2 end and §5.

From my earlier read:
```
    Note over G: сбой на шаге → компенсация (отмена АБС-списания / повтор регистрации в НСПК / DLQ + runbook)
```

## 5. Разбиение на решения (ADR)
```

I'll insert §4.3 and §4.4 before §5.

Let me write the mermaid sequence diagrams for consent and recurring debit.

Consent flow:
```
### 4.3 Создание и активация согласия (подписка)

sequenceDiagram
    participant T as ТСП
    participant G as СБП-шлюз
    participant N as ОПКЦ СБП (НСПК)
    participant P as Банк плательщика

    T->>G: POST /v1/consents (Idempotency-Key, лимиты, срок)
    G->>G: согласие CREATED, outbox
    G->>N: createConsent (reference=consentId)
    N-->>P: запрос на подтверждение плательщика
    P-->>N: плательщик подтверждает в приложении
    N-->>G: нотификация consent.activated (eventId)
    G->>G: согласие ACTIVE, outbox
    G-->>T: вебхук consent.activated
```

Recurring debit flow:
```
### 4.4 Рекуррентное списание (без QR)

sequenceDiagram
    participant T as ТСП
    participant G as СБП-шлюз
    participant N as ОПКЦ СБП (НСПК)
    participant A as АБС

    T->>G: POST /v1/payments (consentId, amount, billingPeriodKey)
    G->>G: guard: согласие ACTIVE, лимиты, billingPeriodKey не дублируется → CREATED, outbox
    G->>N: debitByConsent (reference=paymentId)
    N-->>G: нотификация payment.paid (eventId)
    G->>G: дедуп по eventId, статус PAID, outbox
    G->>A: зачисление (paymentId, сумма, счёт ТСП) — только из PAID (AD-005)
    A-->>G: absDocId
    G->>G: CREDITED → COMPLETED, outbox
    G-->>T: вебхук payment.completed
    Note over G: отзыв согласия (revoke) → согласие REVOKED, любые последующие списания блокируются до вызова НСПК
```

Let me do this edit.

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/solutioning.md", new_string="| НПС/КИИ/ПДн: trust-зоны, ГОСТ | ADR-006 | AD-006, AD-007 |\n| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accept, old_string="| НПС/КИИ/ПДн: trust-зоны, ГОСТ | ADR-006 | AD-006, AD-007 |\n| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accept)`

Now update §5 ADR table to add ADR-008 row, and update §7 gates, §8 rollback, §10 open questions.

Let me read the current §5 table and §7-§10.

§5 table:
```
| Решение | ADR | Spine |
|---|---|---|
| Топология: выделенный компонент + outbox | ADR-001 | AD-001, AD-002 |
| Статусная машина + идемпотентность | ADR-002 | AD-002, AD-003 |
| Транспорт к ОПКЦ: изолированный адаптер, mTLS/ГОСТ, СКЗИ | ADR-003 | AD-004 |
| Нотификации: at-least-once, дедуп, DLQ, сверка | ADR-004 | AD-003 |
| АБС: зачисление из PAID, возвраты-сага | ADR-005 | AD-005 |
| НПС/КИИ/ПДн: trust-зоны, ГОСТ | ADR-006 | AD-006, AD-007 |
| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accepted) | AD-008 [ADOPTED] |
```

Add row for ADR-008.

Then §7 gates, §8 rollback, §10 open questions.

Let me add the ADR-008 row first.

  `read_file(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/solutioning.md", offset=184, limit=33)`

Now update §7 gates (acceptance criteria) and §8 rollback. Let me read the current §7, §8, §10.

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/solutioning.md", new_string="- **A0 (readiness)**: ADR-001..008 заполнены, spine пролинтован, gaps зафиксированы. Критерий: PASS.\n- **A1 (Spec)**: контракт API ТСП (v0, old_string="- **A0 (readiness)**: ADR-001..007 заполнены, spine пролинтован, gaps зафиксированы. Критерий: PASS.\n- **A1 (Spec)**: контракт API ТСП (v0)`

Now I'll update §7 (A0 references ADR-001..007 → 008; A1 mentions v0.1 → v0.2; add recurring acceptance criteria), §8 (rollback for recurring), §9 (gaps — add НСПК subscription protocol), §10 (open questions — add consent-related).

Let me update §7 gates. I'll rewrite the A0/A1/A4 to include recurring. Actually, I'll add acceptance criteria as a new sub-bullet under A4 or a new list. Let me add a dedicated "Критерии приёмки рекуррентных списаний" block.

Let me do targeted edits:

Edit 1: Update A0 and A1 lines to reference ADR-008 and v0.2.

Edit 2: Add recurring acceptance criteria after A5 or within §7.

Edit 3: Update §8 rollback to add recurring-specific rollback.

Edit 4: Update §9 gaps to add НСПК subscription protocol gap.

Edit 5: Update §10 open questions to add consent items.

Let me do these.

For §7, I'll update A0 and A1 and add a subsection for recurring acceptance criteria.

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/README.md", new_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..008`, `ARCHITEC, old_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITEC)`

Now update the README.md to reflect the new ADR-008 and AD-009 in the structure/document list. Also update the "Статус" line mentioning ADR-001..007.

Let me read README again (I have it). Current README:
```
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).

## Структура
...
  adr/ADR-001..007.md        архитектурные решения
```

I'll update `ADR-001..007` → `ADR-001..008` and add a line about AD-009. Also update spine description.

Let me edit README.
Обновляю `README.md`:

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/README.md", new_string="ARCHITECTURE-SPINE.md        инварианты AD-001..AD-009\ndocs/\n  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps\, old_string="ARCHITECTURE-SPINE.md        инварианты AD-001..AD-008\ndocs/\n  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps\)`
  `grep_search(pattern="<!--", path="<HARNESS>/runs/cells/calm-r1/ws/docs/adr")`
  `grep_search(pattern="TODO|TBD|XXX", path="<HARNESS>/runs/cells/calm-r1/ws/ARCHITECTURE-SPINE.md")`
  `grep_search(pattern="только из состояния `PAID`", path="<HARNESS>/runs/cells/calm-r1/ws/docs/adr/ADR-005-integraciya-s-abs-zachisleni)`
  `grep_search(pattern="99,95", path="<HARNESS>/runs/cells/calm-r1/ws/docs/nfr.md")`
  `glob(pattern="**/package.json")`

Now I need to verify the changes are consistent and run the fitness checks. There's a CONSTRAINTS.yaml with fitness rules, but there may be an actual `arch control check` tool. Let me check if there's a way to run the fitness checks. The CONSTRAINTS.yaml mentions "Fitness-правила для `arch control check` (схема control::check)". This might be a tool. Let me check if there's an `arch` CLI or similar.

Actually, let me verify my changes against the fitness rules manually:
1. `adr-set-complete`: `docs/adr/ADR-001-outbox.md` exists — yes, unchanged.
2. `spine-present`: `ARCHITECTURE-SPINE.md` exists — yes.
3. `nfr-measurable`: `docs/nfr.md` must contain '99,95' — yes, still there (§1).
4. `abs-credit-only-from-paid`: `docs/adr/ADR-005-...md` must contain 'только из состояния `PAID`' — I didn't touch ADR-005, so still there.
5. `adr-no-placeholders`: `docs/adr/*.md` must NOT contain `<!--` — my new ADR-008 has no HTML comments. Let me verify. I wrote it without `<!--`. Good.
6. `readme-exists`: README.md exists.
7. `spine-lints-clean`: ARCHITECTURE-SPINE.md must not contain TODO|TBD|XXX — my AD-009 doesn't contain these. Good.

Let me verify the ADR-008 file doesn't contain `<!--`. I wrote it without HTML comments. Let me quickly grep for `<!--` in docs/adr and TODO/TBD/XXX in spine to be safe.

Also I should verify the OpenAPI YAML is valid. Let me run a quick check — is there a way to validate YAML? I could use node with js-yaml (which is in node_modules) or just visually verify. Actually, let me run a quick node script to parse the YAML to confirm validity.

Let me also check if there's an `arch` CLI available to run `arch control check`. Let me search for it.

Actually, let me run a few verification commands:
1. Grep for `<!--` in docs/adr/*.md (should be empty).
2. Grep for TODO|TBD|XXX in ARCHITECTURE-SPINE.md.
3. Validate openapi YAML with node js-yaml.

Let me do these.

Actually, let me check if there's a package.json with scripts or an `arch` tool.
Проверяю согласованность изменений и fitness-правила:

  `run_shell_command(command="cd <HARNESS>/runs/cells/calm-r1/ws && node -e \"const y=require('js-yaml');co, description="Validate openapi YAML parses and inspect keys")`

Fitness checks pass. Now let me validate the OpenAPI YAML using node/js-yaml to make sure it parses correctly. Let me run a quick node command.
Fitness-правила соблюдены. Проверяю валидность OpenAPI YAML:

  `run_shell_command(command="cd <HARNESS>/runs/cells/calm-r1/ws && git status --short && echo \"---STAT---, description="Show git status and diff stat")`

OpenAPI YAML is valid. The version is 0.2.0, paths and schemas are present.

Now let me verify the whole set of changes is coherent. Let me also do a final git status/diff to see what's changed and confirm nothing unintended.

Let me run git status and a diff summary.

  `edit(file_path="<HARNESS>/runs/cells/calm-r1/ws/docs/contracts/tsp-api.md", new_string="# Контракт API ТСП (мерчант-API) — v0.2 draft\n\n- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.2 (аддитивное расширение v0, old_string="# Контракт API ТСП (мерчант-API) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фикс)`

All changes are as expected. The `.arch-handoff/` files are NOT modified (correct — handoff is regenerated after the decision + stack selection).

Now let me do a final review of the key deliverables to ensure consistency. Let me verify the ADR-008 file is complete and coherent by reading it once more (or at least confirm it's there). I already wrote it. It's fine.

Let me now write a concise final summary for the user, mapping to the 7 requested deliverables and listing created/modified files.

Actually, let me double-check one thing: the `docs/contracts/tsp-api.md` header still says "v0.1 draft" in its title/status. I added §3.6/§3.7 but the header still says version 0.1. There may be an inconsistency: the header says "Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)" while solutioning A1 now says v0.2. Let me update the tsp-api.md header to v0.2 to be consistent. Let me check the header.

From my earlier read:
```
# Контракт API ТСП (мерчант-API) — v0.1 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
```

I should update this to v0.2. Let me edit.
Согласую заголовок контракта ТСП с версией 0.2:


There's also §6 "Версионирование и совместимость" in tsp-api.md which says "Путь `/v1`; изменения, ломающие контракт, — только в `/v2`..." That's fine and consistent with additive change.

Also the tsp-api.md §7 "Открытые вопросы (для A1)" — I could add a note about consent open questions, but that's already covered in ADR-008 and solutioning §10. It's fine.

Now everything is consistent. Let me do a final summary.

Let me verify there are no other references to "v0.1" in tsp-api.md that would be inconsistent. Actually, the §1 "Общие положения" says "Путь `/v1`". Fine.

Let me also double check: the openapi info.version was bumped to 0.2.0, and the tsp-api.md header is v0.2. Consistent.

Now I'm done with the implementation. Let me write the final summary.

Actually, let me reconsider whether I should also verify the whole thing one more time with a final read of the ADR-008 to make sure it's well-formed. I'm confident it is.

Let me also think: is there anything in the task I haven't addressed?

1. ✅ Оценка значимости и маршрута — ADR-008 §1.
2. ✅ Влияние на принятую архитектуру — ADR-008 §2 (таблица инвариантов + AD-009) + spine edit.
3. ✅ Архитектурное решение с альтернативами, последствиями, обратимостью — ADR-008 §3-§6.
4. ✅ Изменения контрактов без поломки — tsp-api.md §3.6/§3.7/§4/§5, openapi (аддитивно).
5. ✅ Измеримые NFR — nfr.md §7.
6. ✅ Критерии приёмки и план отката — solutioning §7/§8.
7. ✅ Что остаётся на решение человека — ADR-008 §8 + solutioning §10.

All 7 covered. Now write the final summary listing created/modified files.

Let me write a concise but complete final answer in Russian.

I should also note that I did NOT modify `.arch-handoff/` (correctly, since it's regenerated after decision + stack selection), and did NOT modify ADR-001..007 (existing invariants preserved). And I should mention the fitness checks passed and the OpenAPI validation passed.

Let me write the final response.
Готово. Архитектурный пакет подготовлен поверх принятого решения, инварианты AD-001…AD-008 не изменены (только расширены), родительский spine не затронут.

## Итог по 7 пунктам

**1. Значимость и маршрут** — `Critical`, значимость 10/15. Новая финансово-значимая сущность «согласие», новый путь платежа без QR, новый внешний вход (протокол подписок НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`). Полный пакет решения, но как **расширение текущего feature-spine**, а не новая инициатива (по подтверждённому решению). A3 по стратегии реализации не пересматривается.

**2. Влияние на инварианты** — таблица в ADR-008 §2: AD-001/004/006/008 не затронуты; AD-002/003/007 расширяются; **AD-005 незыблем** (зачисление рекуррентного списания — по-прежнему только из `PAID`). Добавлен новый инвариант **AD-009** в spine.

**3. Решение + альтернативы** — согласие как first-class сущность шлюза + рекуррентный путь `CREATED→PAID→CREDITED→COMPLETED`; отклонены: отдельный сервис, эмуляция через QR без согласия (161-ФЗ), вендорская «коробка», делегирование согласия наружу. Обратимость: `reversible` до прода, `stop-new` после.

**4. Контракты без поломки** — аддитивно: новые пути `/v1/consents*`, опциональное поле `consentId` в `POST /v1/payments` (взаимоисключает `qrType`), новые вебхуки и коды ошибок. Существующие поля/методы/enum не изменены; OpenAPI поднят до 0.2.0.

**5. NFR** — `docs/nfr.md` §7: лимиты/отзыв (0 списаний после отзыва), двойное списание=0, batch-пик 500 TPS sustained / 1000 burst, активация p95 < 5 c.

**6. Критерии приёмки и откат** — `docs/solutioning.md` §7/§8: позитивные + негативные тесты (отзыв, лимит, дубль, недоступность ОПКЦ), фиче-флаг, stop-new, дренаж, QR-поток не затрагивается.

**7. На решение человека** — ADR-008 §8: источник истины лимитов, семантика гонки «списание vs отзыв», возвраты/диспуты по подпискам, модель batch-пика, ретенция ПДн.

## Созданные файлы
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md` — решение (альтернативы, последствия, обратимость, критерии, открытые вопросы).

## Изменённые файлы
- `ARCHITECTURE-SPINE.md` — добавлен AD-009 (Proposed).
- `docs/solutioning.md` — подписки в scope, потоки 4.3/4.4, таблица ADR, гейты A0/A1/A3, критерии приёмки, план отката, gaps, открытые вопросы.
- `docs/nfr.md` — §7 «Рекуррентные списания и согласия».
- `docs/contracts/tsp-api.md` — v0.2, §3.6/3.7, ошибки, вебхуки.
- `docs/contracts/opkc-adapter.md` — операции/события согласия и списания.
- `docs/spec/state-machine.md` — состояния/переходы согласия, рекуррентный путь T13/T14, идемпотентность, сверка.
- `openapi/tsp-api.yaml` — v0.2.0, аддитивные пути и схемы.
- `README.md` — документы и статус.

Проверки: fitness-правила `CONSTRAINTS.yaml` соблюдены (нет `<!--` в ADR, нет TODO/TBD/XXX в spine, `99,95` в NFR, `только из состояния PAID` в ADR-005), OpenAPI YAML валиден (парсится, 5 путей, 4 схемы). `.arch-handoff/` и `docs/adr/ADR-001..007` намеренно не менялись.
