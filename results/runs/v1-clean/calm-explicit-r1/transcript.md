<!-- источник: <HARNESS>/runs-clean/cells/wre6d78/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-clean-cells-wre6d78-ws/chats/d266d026-f250-46a7-a16d-5104ccd4b518.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы. Дополнительно к этому: смоделируй архитектуру изменения на языке CALM (архитектура как код) — узлы, интерфейсы, связи, потоки и контроли — и провалидируй модель родным валидатором CALM. Модель должна лежать в репозитории рядом с остальными артефактами решения.

  `skill(skill="calm")`

Let me start by understanding the task. The user is asking me to act as a solution architect for a bank, and prepare an architectural package for a change on top of an accepted solution — "Payment Gateway SBP (C2B acceptance)". The change: recurring C2B debits by payer consent — SBP subscriptions.

The user explicitly mentions there may be methodological skills and tools installed in the project. I see a `calm` skill (project) available — "An AI Assistant for FINOS CALM development." I need to use it. Also, the task explicitly asks to model the architecture change in CALM and validate with native CALM validator.

Let me first explore the repository to understand the structure, the accepted solution, the invariants, ADRs, contracts, etc. And I should load the `calm` skill since it's relevant.

Let me start by loading the calm skill (it's clearly relevant and the user explicitly asks to use installed methodological skills), and simultaneously explore the repo.

Actually, the skill instruction says: "When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action". The `calm` skill is clearly relevant. Let me invoke it first.

But I also want to read the repo. Let me do the skill first, then read files.

Let me invoke the calm skill.
Начну с загрузки проектного навыка `calm` (он явно относится к задаче — моделирование архитектуры как код), параллельно изучу репозиторий.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.claude/skills/calm/calm-prompts/archit)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.claude/skills/calm/calm-prompts/calm-c)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.claude/skills/calm/calm-prompts/node-c)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.claude/skills/calm/calm-prompts/relati)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.claude/skills/calm/calm-prompts/interf)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.claude/skills/calm/calm-prompts/contro)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.claude/skills/calm/calm-prompts/flow-c)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.claude/skills/calm/calm-prompts/metada)`

The skill instructs me to display "Loading FINOS CALM instructions..." and read the tool prompt files. Let me do that. Let me read the key prompt files.
Loading FINOS CALM instructions...

  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wre6d78/ws && find . -type f -not -path './node, description="List all repo files excluding node_modules and .git")`

I've read the CALM prompt files. I also need to read the remaining ones: pattern-creation, documentation-creation, standards-creation, moment-creation, timeline-creation, decorator-creation. But maybe not all are needed. The key ones for my task: architecture-creation, node-creation, relationship-creation, interface-creation, control-creation, flow-creation, metadata-creation. I have those.

Now let me explore the repository to understand the accepted solution. Let me read the key files:
- ARCHITECTURE-SPINE.md (invariants AD-001..AD-008)
- docs/solutioning.md
- docs/nfr.md
- docs/adr/ (ADR-001..007)
- docs/ status machine
- openapi/tsp-api.yaml
- .arch-handoff/ (TASK.md, RUBRIC.yaml, CONSTRAINTS.yaml, MANIFEST.json, ARCHITECTURE.md, adr/)
- README.md

Let me first get a full listing of the repo structure, then read files. Let me use glob and read key files in parallel.

Let me list the directory tree first.
CALM-инструкции загружены. Теперь изучу репозиторий — структуру и ключевые артефакты принятого решения.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/openapi/tsp-api.yaml")`

Now let me read the key files. Let me read them in parallel:
- ARCHITECTURE-SPINE.md
- README.md
- docs/solutioning.md
- docs/nfr.md
- docs/spec/state-machine.md
- openapi/tsp-api.yaml
- .arch-handoff/TASK.md
- .arch-handoff/ARCHITECTURE.md
- .arch-handoff/CONSTRAINTS.yaml
- .arch-handoff/RUBRIC.yaml
- .arch-handoff/MANIFEST.json
- docs/contracts/tsp-api.md
- docs/contracts/opkc-adapter.md

And the ADRs. Let me read the spine and README first, plus solutioning and nfr, state machine, and the openapi.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/adr/ADR-001-outbox.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/adr/ADR-002-model-konsistentnosti-)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/adr/ADR-005-integraciya-s-abs-zach)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/adr/ADR-007-proposed-a3.md")`

Now let me read the ADRs and the handoff package, plus the contracts. Let me read them in parallel.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/rfp/vendor-rfp.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.arch-handoff/ARCHITECTURE.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.arch-handoff/MANIFEST.json")`

Now let me read the remaining files: contracts (tsp-api.md, opkc-adapter.md), the handoff package (TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json), and rfp/vendor-rfp.md. Also check for any CALM existing artifacts.

  `run_shell_command(command="which calm 2>/dev/null; echo \"---npx---\"; npx --no-install @finos/calm-cli --version 2>/dev/null || echo \"no npx calm-cli\"; echo \"---n, description="Check calm CLI availability")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.qwen/skills/calm/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.claude/skills/calm/calm-prompts/decora)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/.claude/skills/calm/calm-prompts/patter)`

I now have a comprehensive understanding of the repository. Let me summarize the key facts:

**Accepted solution**: Payment gateway SBP (C2B acceptance). Critical route (significance 11/15).

**Spine invariants** (ARCHITECTURE-SPINE.md): AD-001..AD-008:
- AD-001: Isolation of payment contour
- AD-002: Single source of truth — payment state machine
- AD-003: Idempotency of financial operations
- AD-004: Single OPKC SBP adapter
- AD-005: Crediting only from confirmed status (PAID)
- AD-006: Trust zones and segmentation
- AD-007: Compliance with NPS, CII, PDn
- AD-008: Implementation strategy — hybrid [ADOPTED]

**Current state machine**: CREATED → QR_ISSUED → PAID → CREDITED → COMPLETED, plus terminal FAILED/EXPIRED/REFUNDED. Each payment requires QR + client action (scan QR / pay).

**Business task**: TSP (online cinemas, housing & utilities, telecom) ask for recurring C2B debits by payer consent — SBP subscriptions. Currently each payment requires QR and client action.

This is the "recurring payments / autopayments" (автоплатежи / рекуррентные списания по согласию) feature. In SBP terms, this corresponds to the "подписка" / "согласие плательщика" / "рекуррентный платёж" (recurring payment with payer consent). This is a well-known SBP C2B capability: consent-based pull payments (signed consent). The C2B "subscription" flow in SBP uses a "согласие" (consent) that the payer signs once, authorizing the merchant (TSP) to initiate debits up to a limit/period.

Now the task asks me to prepare an architectural package for this change, with 7 specific deliverables:

1. Assessment of change significance and route (how deep the design needs to be and why).
2. Impact on accepted architecture: which invariants are affected, what changes, what doesn't.
3. Architectural decision with alternatives, consequences, reversibility.
4. Contract changes (openapi/tsp-api.yaml) without breaking existing consumers.
5. Measurable NFR for the new functionality.
6. Acceptance criteria and rollback plan.
7. What remains for the human architect to decide and why.

Plus: model the architecture change in CALM (nodes, interfaces, relationships, flows, controls), validate with native CALM validator, and place the model in the repo next to other artifacts.

Constraints:
- "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — Change accepted decision files only in the way accepted in this repo. This means I should NOT rewrite ARCHITECTURE-SPINE.md, ADRs, solutioning.md, nfr.md directly in a way that contradicts the accepted way. The accepted way is: ADRs are added as new ADR-NNN files under docs/adr/, and the spine is the invariant file. New changes should be added as new artifacts (a new ADR for the change, a new change package), not by modifying the accepted ADRs in place. Also, the openapi/tsp-api.yaml can be extended in a backward-compatible way (add new paths/schemas, optional fields) — this is "the way accepted" for contract changes (versioning §6 of tsp-api contract).

Actually, let me re-read the constraint carefully: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — "Change accepted decision files only in the way accepted in this repository."

The repo's accepted way of evolving decisions:
- ADRs are individual files numbered ADR-001..007, with Status field.
- The spine (ARCHITECTURE-SPINE.md) holds invariants, marked Proposed/[ADOPTED]. New invariants would be added as AD-009 etc., marked Proposed until ratified.
- Contracts have versioning discipline (§6): new paths in /v1 with optional fields are backward compatible; breaking changes in /v2.
- docs/contracts/tsp-api.md and openapi/tsp-api.yaml are the source-of-truth contract.

So my approach for deliverables:
- Create a new ADR (ADR-008) for recurring C2B payments (consent-based), in docs/adr/ — following the ADR template used.
- Possibly add AD-009 to ARCHITECTURE-SPINE.md (new invariant) — but wait, "Принятые файлы решения меняй только тем способом, который принят" — the spine is the invariant file; adding a new invariant AD-009 is the accepted way (existing invariants are marked Proposed, and AD-008 is [ADOPTED]). Actually, I need to be careful. The spine has "Deferred" section listing "автоплатежи" (autopayments) as out of scope, to return later. So the change is actually RETURNING a deferred item ("Диспуты... автоплатежи"). Let me check: solutioning.md roadmap says "вне scope: C2C, выплаты B2C/B2B, диспуты, автоплатежи." And ARCHITECTURE-SPINE.md Deferred section says: "C2C-переводы и выплаты B2C/B2B... Диспуты/претензии..." — actually it doesn't explicitly list автоплатежи in the Deferred section of the spine. Let me re-read.

The spine Deferred section lists:
- Мультивалютность...
- C2C-переводы и выплаты B2C/B2B...
- Диспуты/претензии...

It doesn't list автоплатежи (autopayments) explicitly in the spine's Deferred. But solutioning.md §1 says roadmap (вне scope): "C2C, выплаты B2C/B2B, диспуты, автоплатежи." And solutioning.md §10 open questions #1: "Объём первой волны: только C2B-приём или сразу C2C/выплаты?" 

So автоплатежи (recurring) was deferred as roadmap. Now business brings it back.

The accepted way to evolve: I should create the change package as NEW artifacts:
1. A new ADR (ADR-008) — architectural decision for recurring C2B (consent-based subscriptions).
2. Modify openapi/tsp-api.yaml — this IS an accepted-decision file (the contract). The instruction says "меняй только тем способом, который принят" — the accepted way for contract is backward-compatible addition of new paths/schemas/optional fields. I need to update the contract WITHOUT breaking existing consumers. This is explicitly deliverable #4.
3. Possibly update ARCHITECTURE-SPINE.md to add AD-009 (a new invariant) and update the Deferred list to remove/annotate автоплатежи. This is the accepted way for the spine (add new AD, mark Proposed).

Actually, let me be careful about scope. The user asks to "подготовь архитектурный пакет этого изменения поверх принятого решения". The package should contain:
1-7 deliverables as documents.
Plus CALM model.

The deliverables are essentially a new architectural document (a change proposal / design doc) plus a new ADR plus contract changes plus CALM model.

Let me think about what files to create/modify:

**New files (create):**
1. `docs/adr/ADR-008-rekurrentnye-spisaniya-c2b-po-soglasiyu-platelshchika.md` — the architectural decision (deliverable #3).
2. `docs/changes/recurring-c2b/solutioning.md` or a single change package doc — the overall change package (deliverables #1, #2, #5, #6, #7). Actually, maybe put it as `docs/recurring-c2b/CHANGE-PACKAGE.md` or similar.

Hmm, let me think about the repository's convention. The repo has:
- docs/solutioning.md (main solutioning)
- docs/nfr.md (NFR)
- docs/adr/ADR-NNN.md
- docs/contracts/*.md
- docs/spec/state-machine.md
- docs/rfp/vendor-rfp.md

There's no "changes/" folder yet. I think the cleanest approach, consistent with the repo, is:

1. `docs/adr/ADR-008-recurring-c2b-consent.md` — new ADR (deliverable #3).
2. `docs/recurring-c2b/solutioning.md` — the change solutioning (significance/route, impact, NFR, acceptance criteria, rollback, human decisions) — deliverables #1, #2, #5, #6, #7.

Actually, maybe simpler: a single change package doc plus a new ADR. Let me keep it clean:

- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu.md` — ADR with alternatives/consequences/reversibility (deliverable #3).
- `docs/recurring-c2b/CHANGE-PACKAGE.md` — full change package (deliverables #1, #2, #5, #6, #7).
- `docs/recurring-c2b/spec/consent-state-machine.md` — consent state machine spec (analogous to docs/spec/state-machine.md).
- Modify `docs/contracts/tsp-api.md` — add consent/recurring payment endpoints (backward compatible).
- Modify `openapi/tsp-api.yaml` — add new paths/schemas (deliverable #4).
- Modify `ARCHITECTURE-SPINE.md` — add AD-009 (recurring consent invariant), update Deferred (deliverable #2 reflection in spine).
- CALM model: `calm/recurring-c2b.architecture.json` (deliverable — CALM model) + validate.

Wait, but "Принятые файлы решения меняй только тем способом, который принят" — I need to think about whether modifying ARCHITECTURE-SPINE.md is appropriate. The spine is the invariant file. Adding a NEW invariant (AD-009) is the accepted way (it's how the spine evolves — each AD maps to an ADR). But I should NOT change the meaning of existing invariants AD-001..AD-008. Adding AD-009 "рекуррентные списания только по подтверждённому согласию" as Proposed is consistent.

Actually, let me reconsider. The user said: "Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет." This is deliverable #2 — an ANALYSIS of impact. It doesn't necessarily mean I must edit the spine. But to be a complete package, I could propose the new invariant. The spine's accepted evolution: new AD entries are "Proposed" until the corresponding ADR is ratified. So I'll add AD-009 as Proposed, and update the Deferred section to reflect that автоплатежи is now being pulled back.

Hmm, but I want to be careful not to over-modify. Let me think about what "принятый способ" means precisely:

The repo is a solution design repo using:
- Spine (invariants) — evolved by adding AD entries with status.
- ADRs — evolved by adding new ADR files (never editing old ones, since they're dated decisions).
- Contracts — evolved by versioning discipline (backward-compatible additions in /v1, breaking in /v2).
- Specs — new files under docs/spec/.

So my plan:
1. **Add ADR-008** (new file) — never modify ADR-001..007.
2. **Add AD-009 to spine** (new invariant, Proposed) — never modify existing AD text; update Deferred list to note автоплатежи returned.
3. **Extend openapi/tsp-api.yaml and docs/contracts/tsp-api.md** — backward-compatible (add new endpoints, new optional fields; keep existing).
4. **Add new spec files** (consent state machine).
5. **Add change package doc** (significance/impact/NFR/acceptance/rollback/human decisions).
6. **Add CALM model** + validate.

Now, let me also check: is the `calm` CLI installed? The CALM skill says to check `which calm`. Let me check that. Also I need to understand what CALM native validator is available. The skill mentions `calm validate`. Let me check if `calm` is installed, and if not, whether it's available via npx @finos/calm-cli.

Let me also check the `.qwen/skills/calm/SKILL.md` and `.claude/skills/calm/SKILL.md` to see if there are additional instructions specific to this project.

Let me read the remaining CALM prompt files that might be relevant: pattern-creation, documentation-creation, standards-creation, decorator-creation, timeline-creation, moment-creation. Actually, for my task I need: nodes, relationships, interfaces, flows, controls, metadata. I have those. But let me check the SKILL.md for any project-specific validation instructions, and check calm CLI availability.

Let me also read the remaining prompt files quickly to be safe, and check calm availability.

Let me plan the work:

First, check `which calm` and read SKILL.md files and remaining prompt files. Then check node_modules for @finos/calm-cli.

Let me do these in parallel.
Изучил ядро решения. Теперь проверю наличие CALM-валидатора и дочитаю оставшиеся инструкции навыка.

  `write_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisa, content="# ADR-008. Рекуррентные C2B-списания по согласию плательщика (подписки СБП)\n\n- Date: 2026-09-28\n- Status: Proposed (требует ратификации )`

I now have enough understanding of CALM. The `calm` CLI is available via `npx @finos/calm-cli` (version 1.60.1). Good. I can use `npx --no-install @finos/calm-cli validate -a ...`.

Now let me plan my work carefully. This is a substantial architecture package. Let me think about the actual technical content.

## The Business Change: Recurring C2B debits by payer consent (SBP subscriptions)

In SBP (НСПК) terminology, this is the **"подписка" / рекуррентный платёж / согласие (consent)** feature. The SBP C2B standard has a mechanism where the payer signs a consent (согласие) authorizing the merchant (ТСП/получатель) to initiate debits (pull payments) from the payer's account up to a certain limit/period/frequency. This is the "СБП подписка" / "автоплатёж" / "рекуррентные платежи".

Key concepts:
- **Согласие (consent)**: a signed authorization by the payer, registered with the bank/ОПКЦ, specifying: merchant, max amount per debit, max frequency, validity period. The payer signs it once via their bank app (using a QR/link/redirect to the payer's bank).
- **Рекуррентный платёж (recurring payment)**: the merchant initiates a debit referencing the consent; no payer action needed at debit time.
- The consent has its own lifecycle (state machine): requested → awaiting payer sign → active → cancelled/expired/revoked → terminated.

Now, how does this affect the architecture?

### Current state
- Each payment: TSP → POST /payments → QR issued → payer scans QR and pays (payer action) → PAID → credit.

### New: recurring
- Add a **consent** concept: TSP registers a consent request → payer signs consent (via their bank / СБП) → consent ACTIVE.
- Then TSP initiates **recurring debits** referencing consent → these are processed like payments but WITHOUT QR/scan, directly → the ОПКЦ debits the payer's account (pull), → PAID → credit → COMPLETED.

This requires:
1. New API endpoints for consent management (create consent request, get consent status, revoke consent).
2. New API endpoint(s) for recurring payment initiation (POST /v1/recurring/payments referencing consentId), or extend POST /v1/payments with a `consentId` + `paymentType=recurring`.
3. New state machine for consent (separate from payment state machine).
4. The recurring payment flow: no QR_ISSUED step (or a different "PENDING" state while ОПКЦ debits).
5. New invariants: consent must be ACTIVE and within limits/validity to allow debit; debits idempotent; consent revocation stops future debits but not already-approved ones.

### Impact on invariants (spine AD-001..AD-008):
- AD-001 (isolation): unaffected — recurring logic lives in the same SBP gateway contour.
- AD-002 (single source of truth = payment state machine): EXTENDED — now there are TWO state machines (payment + consent), both in gateway DB, same atomic transition discipline. The consent is a new "single source of truth" entity.
- AD-003 (idempotency): EXTENDED — consent creation, consent revocation, and recurring debit initiation all need idempotency keys; ОПКЦ events for consent (signed/revoked) dedup by eventId.
- AD-004 (single ОПКЦ adapter): EXTENDED — the adapter contract must add consent operations (registerConsent, revokeConsent, initiateRecurringDebit, consent events). Still single adapter.
- AD-005 (crediting only from confirmed status): EXTENDED — recurring debit credits only from a confirmed "paid" state (no QR, but still PAID confirmation from ОПКЦ). The rule "зачисление только из подтверждённого статуса" holds; the source of confirmation for recurring is the consent-based debit notification, not a QR scan. Still PAID.
- AD-006 (trust zones): unaffected (same zones; payer consent signing goes through payer's bank, outside gateway).
- AD-007 (compliance NPS/CII/PDn): EXTENDED — consent is a new type of ПДн/финансово-значимый объект; consent data minimization; audit trail for consent lifecycle. 161-ФЗ now explicitly covers согласие (consent) as a legally significant object.
- AD-008 (hybrid strategy): unaffected — consent is core logic (own development), the transport adapter just adds consent operations. Vendor contract extended.

So the change is **significant but bounded**: it extends the core (new entity, new state machine, new adapter operations, new API), but does not change the topology, trust zones, or the hybrid strategy. Route: this is a **major feature** on a Critical-route system. Significance assessment: high (financial, new legal object — consent, NPS compliance, new external interaction with payer's bank via ОПКЦ). But it's additive, not a rewrite.

### Route assessment (deliverable #1)
- The system is Critical (11/15). A new financial object (consent) + new external flow (pull debit) touches AD-002, AD-003, AD-005, AD-007. This warrants a full solutioning + ADR, not a lightweight change.
- Deep design needed for: consent state machine + its invariants, consent→debit relationship, idempotency of debit initiation, adapter contract extension, and NPS/PDn implications of storing consent.
- But NOT deep re-design of: topology, transport (adapter remains), trust zones, hybrid strategy.

### Architectural decision (deliverable #3)
The main decision: how to model consent + recurring debits. Alternatives:
1. **Consent as a first-class entity with its own state machine + recurring debit as a payment variant** (reuse payment state machine, add a `paymentType=recurring` and skip QR_ISSUED). — recommended.
2. Consent stored only in ОПКЦ, gateway stateless proxy — rejected (no local source of truth, violates AD-002 spirit).
3. Recurring debit as a completely separate pipeline — rejected (duplicates payment machinery).
4. Model consent as a "template" and generate payments — similar to 1 but naming.

Decision: Introduce Consent entity (own state machine) + extend Payment with `paymentType` (ONE_TIME | RECURRING) and a `consentId` link. Recurring payment skips QR_ISSUED: CREATED → (OPKC debit accepted) → PAID → CREDITED → COMPLETED, with a new terminal/abort handling. Consent state machine: REQUESTED → PENDING_SIGN → ACTIVE → REVOKED/EXPIRED/SUSPENDED.

### Contract changes (deliverable #4) — backward compatible
OpenAPI tsp-api.yaml additions:
- New paths:
  - `POST /v1/consents` (create consent request) — with Idempotency-Key.
  - `GET /v1/consents/{consentId}` (consent status).
  - `POST /v1/consents/{consentId}/revoke` (revoke).
  - `POST /v1/recurring/payments` OR extend `POST /v1/payments` with optional `consentId` + `paymentType`. To be backward compatible, add optional `paymentType` (default ONE_TIME) and optional `consentId` to PaymentRequest; add `consentId` and `paymentType` to Payment response (optional). Add new consent schemas.
  - Webhooks: `consent.signed`, `consent.revoked`, `consent.expired` events; `payment.completed` already exists (recurring debit just reuses it).
- All additions are new paths or optional fields → backward compatible, no breaking change.

I'll keep the OpenAPI at version 0.1.0 but add `0.1.1`? Actually the contract version is `0.1.0` and status "Draft". The repo's versioning discipline: `/v1` path, additions backward compatible. I'll bump info.version to `0.2.0` (minor, backward-compatible additive) and note in the change package. Actually the tsp-api.md says "Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)". Since we're adding features, I'll bump to `0.2.0` and note the additive nature. This is acceptable.

### NFR (deliverable #5)
New measurable NFRs:
- Consent registration: p95 < 500ms (like QR registration).
- Consent signing notification delivery (from ОПКЦ): p95 < 5s.
- Recurring debit initiation: p95 < 1s (no QR issuance; ОПКЦ pull).
- Consent-debit limit enforcement: 100% (a debit exceeding consent limit/max-amount is rejected before reaching ОПКЦ — 0 violations).
- Idempotency: 0 double debits from retries.
- Consent revocation propagation: p95 < 5s; a debit initiated after revocation → 0 (rejected).
- Availability: same as gateway (≥99.95%).
- Reconciliation: consent lifecycle reconciled with ОПКЦ daily; 0 discrepancies on completed consents.
- Throughput: recurring debits add load; sustained 200 TPS must still hold; burst for "subscription day" (billing runs) — this is a key new NFR: batch of recurring debits (e.g. first-of-month billing) — peak 500 TPS, maybe a "mass debit" wave.

### Acceptance criteria & rollback (deliverable #6)
Acceptance criteria (positive + negative), rollback plan (feature flag, stop-new-consents, stop-new-debits, no data migration back).

### Human decisions (deliverable #7)
What remains for human architect:
- Whether recurring requires explicit sign at debit vs consent-based pull (regulatory reading of 161-ФЗ / НСПК rules) — the exact consent model (mandate vs standing order) depends on НСПК documentation [ТРЕБУЕТ ПРОВЕРКИ].
- Consent limits semantics (per-debit max, cumulative max, frequency) — business product decision.
- Payer consent UX/flow (redirect to payer bank vs QR) — product + НСПК.
- Whether revoke should refund in-flight debits.
- AML/fraud thresholds for recurring.
- Whether to support mandate amendments (change limit without re-sign).
- Payer-initiated cancellation channel (via payer's bank) vs TSP-initiated revoke — who can revoke.
- Data retention of consent under 152-ФЗ.

Now, let me also think about what to write to memory (auto memory). The task is a substantial piece of work but it's within this conversation. I might save a project memory about the repo's conventions (how ADRs/spine evolve) — but wait, the memory instructions say NOT to save code patterns, architecture conventions, file paths, project structure. The repo's decision-evolution convention is arguably a project convention but it's more of a "how to work here" feedback. Actually the "Do not save" list includes "Code patterns, conventions, architecture, file paths, or project structure (read the project instead)". So I should NOT save repo conventions to memory. I'll skip memory unless something surprising/durable emerges. Actually, I could save a `feedback` memory about "CALM CLI available via npx @finos/calm-cli, validate with calm validate -a". But that's a tool/workaround thing, and the "Do not save" says "MCP tool names, schemas... save only confirmed durable workarounds". The CALM CLI is a project tool, and I discovered it. Hmm. Actually this is borderline. I'll hold off on memory — the task doesn't really produce durable cross-conversation knowledge beyond what's in the repo. I'll focus on the deliverable.

Actually, wait — let me reconsider. The memory system says "When you learn something worth remembering across conversations, save it." One genuinely useful durable fact: the repo uses FINOS CALM and the CLI is available via `npx --no-install @finos/calm-cli` (no global `calm` binary). That's a "confirmed durable workaround" for this project. But it's also discoverable. I'll consider saving a small project reference memory at the end if appropriate. Let me not over-index on memory; the primary task is the architecture package.

Let me now also read the remaining CALM prompt files I haven't read: documentation-creation, standards-creation, moment-creation, timeline-creation. These may matter for how I should document. Actually, I've read enough. The key ones for building an architecture model are read. I'll skip the rest to avoid bloat, but actually I should be thorough about validation. Let me just proceed.

Now, one important thing: I should decide on the CALM model scope. The task says "смоделируй архитектуру изменения на языке CALM — узлы, интерфейсы, связи, потоки и контроли". So model the CHANGE architecture: the recurring C2B consent + debit flows. I'll create a CALM architecture JSON that models:
- Nodes: TSP (actor), Payer (actor) [signs consent via payer bank], SBP gateway (system), Consent service / State machine (service), Payment state machine (service), Consent DB + Payment DB (database), ОПКЦ adapter (service), ОПКЦ/НСПК (ecosystem/actor external), АБС adapter (service), АБС (system external), Notifier (service), Anti-fraud/AML (service).
- Interfaces: TSP API endpoints (consents, recurring payments), ОПКЦ adapter contract endpoints (registerConsent, initiateDebit, consent events), АБС credit.
- Relationships: connects/interacts.
- Flows: (1) consent creation & signing flow, (2) recurring debit flow.
- Controls: consent limit enforcement, idempotency, audit, NPS compliance, PDn minimization.

I'll name it `calm/recurring-c2b-consent.architecture.json`.

Where to place it? The repo has no `calm/` dir yet. I'll create `calm/` at repo root, or put under `docs/calm/`. The task says "Модель должна лежать в репозитории рядом с остальными артефактами решения." "рядом с остальными артефактами решения" = alongside the other solution artifacts. The solution artifacts are under `docs/`. But CALM is typically a top-level `calm/` or `architectures/`. Hmm. I think creating a top-level `calm/` directory is cleanest, or `docs/calm/`. Given the repo root already has `ARCHITECTURE-SPINE.md` and `openapi/`, I'll place the CALM model at `calm/recurring-c2b.architecture.json`. Actually, "рядом с остальными артефактами решения" — the decision artifacts are in docs/. I'll put it under `docs/calm/` to be literally "рядом". Hmm, but CALM architecture-as-code is more of a machine artifact. Either is defensible. I'll use `calm/` at root for clarity and mention it. Actually, let me reconsider — to keep it "рядом с остальными артефактами решения", and since `docs/` holds the solution artifacts (ADR, contracts, spec, nfr, solutioning), I'll place the CALM model at `docs/calm/recurring-c2b.architecture.json`. This keeps all solution artifacts together under docs/. But `openapi/` is at root too. Hmm.

I think the cleanest is to mirror the existing structure: root has `ARCHITECTURE-SPINE.md`, `openapi/`, `docs/`. A CALM model is architecture-as-code, similar in nature to `openapi/`. So I could place it at root `calm/`. But "рядом с остальными артефактами решения" strongly suggests docs/. 

I'll go with `docs/calm/recurring-c2b-consent.architecture.json` — placing it inside docs/ (next to adr/, contracts/, spec/) so it's clearly part of the solution artifacts, and I'll reference it from the change package and README-style notes.

Actually, let me reconsider once more. A cleaner and more conventional choice given the FINOS CALM convention: a top-level `calm/` directory containing architecture + optionally patterns/standards/controls. But since the task emphasizes "рядом с остальными артефактами решения" and the repo's decision artifacts live in `docs/`, I'll use `docs/calm/`. Final: `docs/calm/recurring-c2b-consent.architecture.json`.

Now let me also think about whether to modify ARCHITECTURE-SPINE.md. The task deliverable #2 is "Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет." This is analysis, which I'll put in the change package doc. But should I also add AD-009 to the spine? The spine is the invariant file; the accepted way to evolve it is adding a new AD. I think it's appropriate and expected to add AD-009 (Proposed) for the recurring consent invariant, and update the Deferred section. This is a real change to the accepted decision file, done "the accepted way" (add new Proposed AD, don't alter existing ADs).

However, I should be careful: adding to the spine is a modification of an accepted decision file. The user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The accepted way to change the spine is to add a new AD (Proposed) and reference its ADR. That's exactly what I'll do. And I'll update the "Deferred" section to note that автоплатежи/recurring is now pulled back (since it was deferred in solutioning, though not explicitly in the spine's Deferred list — the spine's Deferred list has C2C/выплаты/диспуты, not автоплатежи). Actually the spine Deferred list doesn't mention автоплатежи. solutioning.md §1 roadmap mentions "автоплатежи" as out of scope. So I'll:
- Add AD-009 (Proposed) to spine.
- Add a note in Deferred or just leave it (автоплатежи wasn't in the spine's Deferred list explicitly). I'll add the new invariant and update the "Контракты и версии" section to reference the new contract.

Actually, let me reconsider scope creep. The spine has "Deferred (с причиной и условием возврата)" section. The business is now returning автоплатежи (recurring). I'll add AD-009 and reference it. I'll also add a note that the deferred "автоплатежи" roadmap item (from solutioning §1) is now pulled back. This is faithful.

Let me now think about how much to modify. I want to:
1. Create `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu.md`
2. Create `docs/recurring-c2b/CHANGE-PACKAGE.md` (or maybe `docs/recurring-c2b/solutioning.md`). Let me name it `docs/recurring-c2b/solutioning.md` to mirror `docs/solutioning.md`. But then NFR, acceptance criteria, rollback, human decisions are all inside. Actually the change package needs to cover all 7 deliverables. I'll make one comprehensive doc: `docs/recurring-c2b/solutioning.md` covering significance/route (#1), impact (#2), NFR (#5), acceptance/rollback (#6), human decisions (#7). And the ADR (#3) is separate. And contract changes (#4) are in the openapi + tsp-api.md files themselves (plus a section in the change package summarizing them). And CALM model is separate.

Actually, let me structure more cleanly. The repo convention is fairly granular: solutioning.md, nfr.md, spec/state-machine.md, contracts/*.md, adr/*.md. For the recurring change, I'll mirror this:

- `docs/recurring-c2b/solutioning.md` — change solutioning: significance & route (#1), impact on invariants (#2), decision summary (points to ADR), contract change summary (#4 summary), NFR (#5), acceptance criteria & rollback (#6), human decisions (#7). This is the "архитектурный пакет" main doc.
- `docs/recurring-c2b/spec/consent-state-machine.md` — consent state machine spec (new entity).
- `docs/recurring-c2b/nfr.md` — NFR for the feature (or embed in solutioning). I'll embed NFR in solutioning to keep it as one package, but actually a separate nfr.md mirrors repo convention better. Hmm.

Let me not over-engineer. I'll create:
1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md` — ADR (#3).
2. `docs/recurring-c2b/solutioning.md` — full change package (#1, #2, #4-summary, #5, #6, #7). This will be the master doc.
3. `docs/recurring-c2b/spec/consent-state-machine.md` — consent state machine (supporting spec).
4. Modify `docs/contracts/tsp-api.md` — add consent + recurring endpoints (contract detail, backward compatible).
5. Modify `openapi/tsp-api.yaml` — add new paths/schemas (backward compatible) (#4).
6. Modify `ARCHITECTURE-SPINE.md` — add AD-009 (Proposed) + update Deferred note.
7. Create `docs/calm/recurring-c2b-consent.architecture.json` — CALM model, validate.

That's a lot but it's what the task requires. Let me also update README.md to reference the new artifacts? The README lists key docs. Adding a line for the recurring change package would be helpful and low-risk. I'll add a brief mention. Actually, to minimize touching accepted files, I'll keep README changes minimal — maybe add one bullet. The README is not a "decision file" per se, but it's a navigation doc. I'll add a short line under "Структура" or "Ключевые документы". Actually, I'll leave README mostly as-is but add a note in the change package that points to everything. Hmm, but updating README's "Структура" tree to include the new dirs would be good for discoverability. I'll add a concise line.

Let me be judicious. The instruction "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" is specifically about DECISION files (ADR, spine, contracts). README is navigation, not a decision. I'll update README minimally to add the change package reference (it's helpful and conventional).

Now, let me think carefully about the actual SBP recurring/consent semantics to make this technically credible.

**СБП C2B recurring payments (автоплатежи/подписки):** In the СБП C2B model, there's a "согласие на списание" (consent/mandate). The flow:
1. Merchant (ТСП) requests a consent from the payer.
2. Payer reviews and signs the consent in their bank's app (the consent is presented via a QR/link that routes to the payer's bank, similar to a payment but for a standing authorization).
3. Once signed, the consent is registered with ОПКЦ and becomes ACTIVE. It has parameters: max amount per debit, total/frequency limits, validity period.
4. Merchant then initiates recurring debits (pull) referencing the consent. ОПКЦ debits the payer's account without payer action, subject to the consent's limits.
5. Consent can be revoked by payer (via their bank) or merchant (stop), expires by time/limit.

For the gateway architecture, this maps cleanly:
- **Consent** is a new first-class entity in the gateway DB (source of truth), mirroring the payment state machine discipline.
- Consent states: `REQUESTED` (created, awaiting sign) → `SIGNING`/`PENDING_SIGN` → `ACTIVE` → terminal `REVOKED`, `EXPIRED`, `DECLINED` (payer declined), `SUSPENDED`.
- Recurring debit: a Payment with `paymentType=RECURRING` referencing `consentId`. Its flow skips QR_ISSUED: `CREATED` → (ОПКЦ accepts debit, returns a debit/payment id) → `PAID` (ОПКЦ confirms) → `CREDITED` → `COMPLETED`. Failure/decline → `FAILED`.
- Guard: debit allowed only if consent is ACTIVE and debit amount ≤ consent remaining limit and within validity window (this guard is checked by gateway BEFORE calling ОПКЦ, but the ultimate enforcement is at ОПКЦ/payer's bank — gateway check is a first line of defense + the ОПКЦ is the authoritative enforcer).
- The adapter contract (opkc-adapter.md) gains consent operations: `registerConsent`, `getConsentStatus`, `revokeConsent`, `initiateRecurringPayment` (or `createPayment` with a `consentReference` + mode), and consent events: `consent.signed`, `consent.declined`, `consent.revoked`, `consent.expired`.

This is a sound, credible design consistent with real СБП capabilities.

Now, key invariant additions (AD-009):
**AD-009. Рекуррентное списание только по активному согласию в пределах лимитов**
- Binds: сущность согласия (consent) в БД шлюза, адаптер ОПКЦ, статусная машина платежа.
- Prevents: списание без согласия, списание сверх лимитов согласия, списание по отозванному/истёкшему согласию, двойное списание при ретрае.
- Rule: рекуррентный дебит инициируется только если согласие в состоянии ACTIVE и сумма дебита ≤ остаточного лимита согласия в пределах срока действия; согласие и его отзыв — отдельный конечный автомат с атомарными переходами (AD-002) и идемпотентностью (AD-003). Fitness: недостижимость дебита из REVOKED/EXPIRED/DECLINED; 0 превышений лимита.

This is consistent with the existing spine style.

Now, let me also think about the impact on AD-005 specifically. AD-005 says "зачисление только из состояния PAID". For recurring, the debit is confirmed by ОПКЦ (not by QR scan), but still results in a "PAID" status (подтверждённый НСПК статус). So AD-005 holds unchanged: credit only from PAID. What changes is the *path* to PAID (no QR_ISSUED for recurring). So AD-005 is "extended in meaning" but not "changed" — the rule stays. I'll note this precisely.

Similarly AD-002: "Единый источник истины — статусная машина платежа". We now add a SECOND status machine (consent). AD-002's *rule* (atomic transitions) applies to the consent machine too. So AD-002 is extended to cover a second entity, not broken. I'll note this as "extended scope, same rule".

Now let me draft everything. I'll write the files.

Let me first decide on the exact OpenAPI changes (backward-compatible additions):

Add to `components.schemas`:
- `ConsentRequest` (create consent): required `tspId, amountLimit` (max per debit), optional `currency, maxTotalAmount, maxDebits, validityStart, validityEnd, merchantConsentId, purpose, paymentPurpose`.
- `Consent`: `consentId, status (REQUESTED|PENDING_SIGN|ACTIVE|REVOKED|EXPIRED|DECLINED|SUSPENDED), amountLimit, maxTotalAmount?, remainingLimit, expiresAt?, merchantConsentId?, createdAt`.
- Extend `PaymentRequest` with optional `paymentType` (ONE_TIME|RECURRING, default ONE_TIME) and optional `consentId`.
- Extend `Payment` with optional `paymentType` and `consentId`.
- `RecurringDebitRequest` — actually I'll just reuse PaymentRequest with paymentType=RECURRING + consentId. Simpler and backward compatible. But I might also add a dedicated `POST /v1/consents/{consentId}/payments` convenience? To keep it clean, I'll extend `POST /v1/payments` with optional `paymentType` + `consentId` (backward compatible), AND also provide `POST /v1/consents` for consent management. That's the minimal, clean design.

New paths:
- `POST /v1/consents` (Idempotency-Key header) → 201 Consent.
- `GET /v1/consents/{consentId}` → 200 Consent.
- `POST /v1/consents/{consentId}/revoke` (Idempotency-Key) → 200 Consent (status REVOKED/REVOKING).

Webhooks (in tsp-api.md, but OpenAPI doesn't model webhooks in 3.0 easily; I'll note them in the contract md and change package; optionally add them in a `callbacks` or just document). Since OpenAPI 3.0.3 supports `callbacks`, but to keep it simple and backward-compatible I'll add new webhook event types documented in the tsp-api.md and change package, and add them as `callbacks` in the OpenAPI only if clean. I'll keep OpenAPI focused on request/response paths and document webhooks in tsp-api.md (consistent with existing — the existing tsp-api.yaml doesn't model webhooks, it models request/response only; webhooks are in tsp-api.md §5). So I'll mirror that: add consent webhook events in tsp-api.md §5, not in the yaml.

Now let me write everything. This is going to be a lot of writing. Let me be efficient but thorough.

Let me start writing files. I'll do them one by one, with read_file already done for the files I'm editing (tsp-api.md, openapi/tsp-api.yaml, ARCHITECTURE-SPINE.md — all read).

Let me begin with the ADR-008.

Actually, let me think about the file naming for ADR-008 to match existing style. Existing: `ADR-001-outbox.md`, `ADR-002-model-konsistentnosti-...md`, etc. I'll name: `ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`.

Let me now also decide the directory for the change package. I'll use `docs/recurring-c2b/`:
- `docs/recurring-c2b/solutioning.md`
- `docs/recurring-c2b/spec/consent-state-machine.md`
- `docs/recurring-c2b/nfr.md` (maybe fold into solutioning; I'll keep NFR inside solutioning.md to avoid fragmentation — actually I'll make a separate nfr.md to mirror repo convention, but that's more files. Let me keep it consolidated in solutioning.md to reduce file count while staying complete. Hmm, the repo clearly separates nfr.md. But for a change package, consolidation is fine. I'll consolidate: solutioning.md contains everything (significance/route, impact, decision summary, contract summary, NFR, acceptance, rollback, human decisions). The consent state machine gets its own spec file (mirroring docs/spec/state-machine.md). That's clean.

So final file plan:
1. CREATE `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`
2. CREATE `docs/recurring-c2b/solutioning.md`
3. CREATE `docs/recurring-c2b/spec/consent-state-machine.md`
4. EDIT `docs/contracts/tsp-api.md` (add consent + recurring sections)
5. EDIT `openapi/tsp-api.yaml` (add paths/schemas)
6. EDIT `ARCHITECTURE-SPINE.md` (add AD-009, update Deferred/contracts)
7. CREATE `docs/calm/recurring-c2b-consent.architecture.json`
8. EDIT `README.md` (add references — minimal)
9. Validate CALM model.

Let me write the CALM model content carefully to pass validation. I need to recall the exact schema requirements.

CALM architecture JSON top-level:
```json
{
  "$schema": "https://calm.finos.org/release/1.2/meta/calm.json",
  "unique-id": "...",
  "name": "...",
  "description": "...",
  "metadata": [...],
  "nodes": [...],
  "relationships": [...],
  "flows": [...],
  "controls": {...}
}
```

Node required: unique-id, node-type, name, description.

Relationship required: unique-id, relationship-type (oneOf: connects/interacts/deployed-in/composed-of/options).

For `connects`, source/destination are `node-interface` objects with `node` (string, required) and optional `interfaces` (array of strings). The relationship-creation guide's example shows `connects` source/destination as `{node: "...", interfaces: [...]}`. But there's ambiguity: in the relationship schema shown, `connects-type` has source/destination as `$ref interface.json#/defs/node-interface`, which is `{node: string, interfaces?: array}`. So I can use `{"connects": {"source": {"node": "x"}, "destination": {"node": "y"}}}` without interfaces, or with interfaces.

Wait, actually I need to double check. Looking at the relationship-creation guide, the "connects" example uses source with `"node"` and `"interfaces"`. And the `connects-type` schema: `{source: {$ref node-interface}, destination: {$ref node-interface}}`. node-interface: `{node: string, interfaces?: array}`. Good.

For `interacts`: `{actor: string, nodes: [string]}` (minItems 1).

For `composed-of`: `{container: string, nodes: [string]}`.
For `deployed-in`: `{container: string, nodes: [string]}`.

Flow required: unique-id, name, description, transitions (array, minItems 1). Each transition: relationship-unique-id (string), sequence-number (int), description (string), optional direction.

Controls: object with patternProperties `^[a-zA-Z0-9-]+$` → {description, requirements:[{requirement-url, config|config-url}]}. requirement-url required; oneOf config-url|config.

Metadata: array of objects OR object. I'll use array of objects for top-level.

Now, a subtlety: the `$schema` URL and the actual validator. The `calm` CLI validate with `-a` will validate against the embedded `$schema`. The `$schema` is `https://calm.finos.org/release/1.2/meta/calm.json`. The CLI (v1.60.1) should resolve this (either bundled or via network). Since we're offline possibly, it might use a local schema directory. The `--schema-directory` option exists. But let me first try plain `npx @finos/calm-cli validate -a <file>` and see. If network resolution fails, I'll handle it. Actually, `calm validate -a` without `-p` does "Spectral rules on the architecture structure" plus JSON schema validation if `$schema` points to a pattern... Actually re-reading: "If the architecture contains a `$schema` property pointing to a pattern, it will automatically load and validate against that pattern. Otherwise, runs Spectral rules on the architecture structure only."

Hmm, the `$schema` here points to the CALM meta schema (`calm.json`), not a pattern. So `validate -a` alone would run Spectral rules + JSON schema validation against the meta schema? The docs are a bit ambiguous. The architecture-creation guide says: "Run CALM validation: `calm validate -a <filename>.architecture.json` ... Review output for errors: jsonSchemaValidationOutputs, spectralSchemaValidationOutputs". So `-a` does both JSON schema validation (against the meta schema) and Spectral. Good.

Let me just create a valid model and run `npx @finos/calm-cli validate -a docs/calm/recurring-c2b-consent.architecture.json -f pretty`.

I need to be careful about a few CALM schema details I might get wrong. Let me be conservative:
- Node `node-type` values: use the enum values (actor, ecosystem, system, service, database, network, ldap, webclient, data-asset). For external systems (НСПК, АБС, payer's bank), use `actor` or `ecosystem` or `system`. I'll use `actor` for humans (payer) and external orgs? Actually `actor` is "External systems or users". `ecosystem` is "High-level system boundaries". `system` is "Business systems". 

Let me map:
- TSP (merchant) — `actor` (external system/user of the gateway). Actually merchant is an external system that calls the API. `actor` fits ("External systems or users").
- Payer (физлицо) — `actor`.
- Payer's bank (банк плательщика) — `actor` or `ecosystem` (external). I'll use `ecosystem` for the external СБП ecosystem.
- ОПКЦ СБП (НСПК) — `ecosystem` (external operator) or `system`. I'll use `ecosystem`.
- АБС — `system` (internal bank system) or `ecosystem`. Since it's the bank's own core banking, `system` is fine but it's a separate trust zone; I'll use `system`.
- SBP gateway — `system` (business system) with composed-of relationships to its internal services.
- Consent service / state machine — `service`.
- Payment state machine — `service`.
- Consent DB, Payment DB — `database` (or one DB). I'll model a single "Gateway DB" as `database`, or split into two. To reflect the change cleanly, I'll model "Consent store" and "Payment store" but actually they're the same DB (БД шлюза). I'll model one `database` node "Gateway DB (payments + consents + outbox + audit)". Simpler and accurate. But to show the change, maybe two service nodes (payment state machine, consent state machine) both connecting to one DB. That's accurate.
- ОПКЦ adapter — `service`.
- АБС adapter — `service`.
- Notifier (webhook) — `service`.
- Anti-fraud/AML — `service` (or `system`).

For the change-specific model, I'll focus on the recurring/consent flows but include the existing payment machinery where the recurring debit reuses it.

Nodes list (concise but complete):
1. `tsp` (actor) — ТСП/мерчант.
2. `payer` (actor) — Плательщик.
3. `payer-bank` (ecosystem) — Банк плательщика (подписывает согласие, списывает при дебите).
4. `opkc-nspk` (ecosystem) — ОПКЦ СБП (НСПК).
5. `abs` (system) — АБС (счета ТСП).
6. `sbp-gateway` (system) — СБП-шлюз (контур).
7. `tsp-api` (service) — API ТСП (вход).
8. `payment-state-machine` (service) — статусная машина платежа.
9. `consent-state-machine` (service) — статусная машина согласия.
10. `opkc-adapter` (service) — адаптер ОПКЦ.
11. `abs-adapter` (service) — адаптер АБС.
12. `notifier` (service) — нотификатор ТСП.
13. `gateway-db` (database) — БД шлюза (платежи + согласия + outbox + аудит).
14. `antifraud-aml` (service) — антифрод/AML.

Relationships:
- tsp → tsp-api (interacts, actor=tsp, nodes=[tsp-api]) — or connects. I'll use `interacts` for actor→system and `connects` for system↔system. For TSP calling the API, `interacts` (actor tsp, nodes [tsp-api]) is fine. But then flows reference these relationships. Hmm, flows' transitions reference relationship-unique-id and direction. `interacts` has no source/destination direction (it's actor + nodes), so direction is ambiguous. For flow clarity, I'll use `connects` for most system-to-system, and `interacts` for human payer → payer-bank (payer scans/signs in their bank). 

Let me define relationships with `connects` for directional flows:
- `tsp-to-gateway-api`: connects tsp → tsp-api (source node tsp, dest tsp-api). Protocol HTTPS.
- `payer-signs-consent`: interacts actor=payer nodes=[payer-bank]. (payer signs consent in their bank app — this is an interaction not a gateway connection.)
- `payer-bank-to-opkc`: connects payer-bank → opkc-nspk (debit execution). Actually the debit goes: gateway → ОПКЦ → payer's bank. And consent signing: payer → payer-bank → (bank registers consent with ОПКЦ) → ОПКЦ → gateway (notified). Hmm. The consent sign flow: gateway creates consent request in ОПКЦ → ОПКЦ returns a sign link/QR → payer signs in their bank → payer-bank confirms to ОПКЦ → ОПКЦ notifies gateway. So the payer interacts with payer-bank; payer-bank talks to ОПКЦ; ОПКЦ talks to gateway adapter.

Let me define the core connections:
- `tsp-api-to-payment-sm`: connects tsp-api → payment-state-machine.
- `tsp-api-to-consent-sm`: connects tsp-api → consent-state-machine.
- `payment-sm-to-db`: connects payment-state-machine → gateway-db (protocol JDBC or generic). I'll use "JDBC"? DB access protocol. Actually gateway DB might be accessed via JDBC. I'll use protocol "JDBC" for DB connections, or leave protocol off. To be safe with the enum, JDBC is in the enum. I'll use JDBC for DB, HTTPS for REST, mTLS for ОПКЦ, AMQP for queue.
- `consent-sm-to-db`: connects consent-state-machine → gateway-db.
- `payment-sm-to-opkc-adapter`: connects payment-state-machine → opkc-adapter (internal REST, protocol HTTPS).
- `consent-sm-to-opkc-adapter`: connects consent-state-machine → opkc-adapter.
- `opkc-adapter-to-nspk`: connects opkc-adapter → opkc-nspk (protocol mTLS).
- `nspk-to-opkc-adapter` (events): connects opkc-nspk → opkc-adapter (protocol mTLS) — for events back. Actually bidirectional. I can use a single relationship and flows with direction. But for clarity, I'll add one relationship `opkc-adapter-nspk-link` connects opkc-adapter → opkc-nspk (mTLS), and flows use direction to describe return events? No — flows reference a relationship and a direction. To describe an event coming back, I'd need a separate relationship or use `destination-to-source` direction on the same relationship. The flow transition `direction` supports "destination-to-source". So one relationship `opkc-adapter-to-nspk` (source=opkc-adapter, dest=opkc-nspk) can describe both outbound (source-to-destination) and inbound events (destination-to-source). 

That's elegant. I'll use that.

- `payment-sm-to-abs-adapter`: connects payment-state-machine → abs-adapter (protocol AMQP, via queue) — actually the queue. I'll use AMQP.
- `abs-adapter-to-abs`: connects abs-adapter → abs (protocol HTTPS or a bank-internal protocol; I'll use HTTPS).
- `payment-sm-to-notifier`: connects payment-state-machine → notifier.
- `notifier-to-tsp`: connects notifier → tsp (webhooks, HTTPS).
- `consent-sm-to-notifier`: connects consent-state-machine → notifier (consent webhook events).
- `payment-sm-to-antifraud`: connects payment-state-machine → antifraud-aml (protocol HTTPS).
- `consent-sm-to-antifraud`: connects consent-state-machine → antifraud-aml.
- `gateway-composed`: composed-of container=sbp-gateway nodes=[tsp-api, payment-state-machine, consent-state-machine, opkc-adapter, abs-adapter, notifier]. (composition).

That's a comprehensive model. I should be careful not to overdo it, but the task explicitly asks for "узлы, интерфейсы, связи, потоки и контроли" — nodes, interfaces, relationships, flows, controls. So I should include interfaces on nodes too.

Interfaces: I'll add a few `interface-type` (flexible) interfaces to key nodes:
- tsp-api: `tsp-api-consent-endpoint` {url: "/v1/consents"}, `tsp-api-recurring-endpoint` {url: "/v1/payments?paymentType=RECURRING"}. Actually simpler: give tsp-api an interface `merchant-api` with `url`. But interface-type allows arbitrary properties. I'll add meaningful interfaces:
  - tsp-api: interfaces: [{unique-id: "tsp-api-https", url: "https://api.bank.ru/sbp/v1"}]
  - opkc-adapter: [{unique-id: "opkc-adapter-consent", ...}] — I'll keep interfaces minimal but present, since the task explicitly lists "интерфейсы".

Actually, to keep the model valid and not overly complex, I'll add interfaces to a few key nodes (tsp-api, opkc-adapter, abs-adapter) using interface-type (flexible), and reference them in `connects` source/destination interfaces where natural. But referencing interfaces in connects is optional. I'll add interfaces to nodes for richness but keep connects referencing nodes only (interfaces optional). Actually, to demonstrate interfaces properly, I'll reference them in at least the tsp-api and opkc-adapter connections.

Hmm, but referencing interfaces requires the interface unique-ids to exist on those nodes. Let me be careful: if I put `interfaces: ["x"]` in a connects source, the validator (Spectral) may check that the interface exists on the node. The relationship-creation guide says "Interface References: Must exist on the referenced node (for connects type)". So I need consistency. To reduce risk, I'll mostly NOT reference interfaces in connects (leave interfaces array out), and just define interfaces on nodes as descriptive. That's valid — node-interface only requires `node`.

Wait, but then "interfaces" on nodes serve no connect purpose. They're still valid descriptive metadata. The task asks to model interfaces, so having them on nodes is enough. I'll define interfaces on nodes (interface-type, flexible, with `unique-id` + a descriptive property like `url` or `host`), and connect relationships will reference just nodes (source/destination node ids). Good — lower risk.

Flows (2):
1. `consent-creation-and-signing-flow`: TSP creates consent request → gateway (tsp-api → consent-sm → opkc-adapter → ОПКЦ) → payer signs in payer bank → ОПКЦ notifies → consent ACTIVE → notifier → TSP.
2. `recurring-debit-flow`: TSP initiates recurring debit (tsp-api → payment-sm) → guard check consent ACTIVE → opkc-adapter → ОПКЦ → payer-bank debit → ОПКЦ confirms PAID → payment-sm → abs-adapter → АБС credit → CREDITED/COMPLETED → notifier → TSP.

I'll map transitions to relationships with sequence numbers and directions.

Controls (top-level and/or node-level):
- `consent-limit-enforcement` — requirement-url (fictional canonical URL) + config {max-amount, remaining-limit check, validity}.
- `idempotency` — config.
- `audit-trail` — config (unchanging log).
- `nps-compliance` (161-ФЗ) — config.
- `pdn-minimization` (152-ФЗ) — config.
- `consent-revocation-propagation`.

Control requirement-url: must be a string URL. I'll use canonical-looking URLs under `https://schemas.bank.ru/controls/...`. These don't need to be real; the validator only checks it's a string (and maybe that it's a valid URI format). I'll use valid URI strings.

Actually, wait — will Spectral complain about the requirement-url not being accessible? The docs say "Requirement URLs should be accessible schema definitions" but the validator typically doesn't fetch them. The validate command might try to load referenced URLs though. Hmm. Let me check: `calm validate -a` with `$schema` pointing to the meta schema. The controls' requirement-url are just strings in the data; the JSON schema validation checks they're strings; Spectral might have a rule about them. To be safe, I'll use `config` (inline) rather than `config-url`, and requirement-url as a simple URI string. I don't think the validator fetches requirement-url. But there's a risk Spectral has a rule like "requirement-url must be resolvable". Given the examples use `https://schemas.company.com/...`, and the validator is offline, I think these are treated as opaque strings. I'll proceed and validate; if there's an error, I'll adjust.

Actually, to minimize risk, maybe I should use `config` for all controls (inline config), and use a clearly-synthetic but valid `requirement-url`. If validation complains, I'll switch to a local relative path or a data URI. Let me just try.

Let me also decide metadata: top-level metadata array with a couple of objects (calm-version, architecture-version, owner, business-domain, etc.).

Now, let me also consider: should the CALM model be a full architecture (with `$schema` = calm.json) or reference a pattern? I'll make a plain architecture (not a pattern), which is what "смоделируй архитектуру изменения" asks. `$schema` = `https://calm.finos.org/release/1.2/meta/calm.json`.

Alright, I have a solid plan. Let me now also quickly verify the calm CLI can run offline (it may try to download schemas). Let me just write the model and validate, iterating as needed.

Let me also reconsider: do I need `-s` schema-directory? The calm-cli v1.60.1 likely bundles the release schemas. Let me test validate on the existing... there's no existing CALM model. Let me just create and validate.

Let me start writing. I'll write the ADR first, then the solutioning package, then spec, then edit contracts/spine/README, then CALM, then validate.

Given the volume, I'll write efficiently but with high quality. Let me begin.

Let me write ADR-008.

Actually, before writing, let me finalize the exact naming and identifiers used across files for consistency:

Consent states (canonical): 
`REQUESTED → PENDING_SIGN → ACTIVE → REVOKED | EXPIRED | DECLINED | SUSPENDED`
- REQUESTED: consent created in gateway, registration request to ОПКЦ in progress.
- PENDING_SIGN: ОПКЦ accepted, awaiting payer signature (sign link issued).
- ACTIVE: payer signed, consent effective.
- REVOKED: revoked (by payer or ТСП) — terminal.
- EXPIRED: validity period/limits exhausted — terminal.
- DECLINED: payer declined to sign — terminal.
- SUSPENDED: temporarily suspended (e.g., by bank/AML) — non-terminal, can return to ACTIVE.

Recurring payment: Payment with `paymentType=RECURRING`, `consentId`. States: reuse payment state machine but skip QR_ISSUED:
`CREATED → PAID → CREDITED → COMPLETED`, terminal `FAILED` (debit rejected by ОПКЦ/payer bank). No `QR_ISSUED`, no `EXPIRED` (no QR TTL). Actually there could be a `DEBIT_PENDING` technical sub-state while ОПКЦ processes the pull; I'll keep canonical financial states same (CREATED, PAID, CREDITED, COMPLETED, FAILED) and add technical sub-state `DEBIT_PENDING` (like ABS_PENDING) not exposed externally.

Idempotency keys:
- Consent creation: `Idempotency-Key`.
- Consent revoke: `Idempotency-Key`.
- Recurring debit initiation: `Idempotency-Key` (already required for POST /payments).
- ОПКЦ consent events: `eventId`.
- Debit confirmation: `eventId` (existing payment.paid event, now also triggered by recurring debit).

New adapter contract operations (opkc-adapter.md extension):
- `registerConsent` (core → adapter): reference=consentId, amountLimit, maxTotalAmount?, validity, purpose. Returns consentRef (ОПКЦ id) + signUrl/signQr.
- `getConsentStatus` (core → adapter): consentRef → ACTIVE/PENDING_SIGN/REVOKED/EXPIRED/DECLINED/SUSPENDED.
- `revokeConsent` (core → adapter): consentRef, reason → REVOKING/REVOKED.
- `initiateRecurringPayment` (core → adapter): reference=paymentId, consentRef, amount. Returns debit id + status.
  - Actually, could reuse `createPaymentLink` with a mode flag? No — recurring is a different operation (pull, no QR). I'll add `initiateRecurringPayment`.
- `getRecurringPaymentStatus` (reuse `getPaymentStatus`).
- Events (adapter → core): `consent.signed`, `consent.declined`, `consent.revoked`, `consent.expired`; `payment.paid`/`payment.rejected` reused for recurring debits.

Now, human decisions (#7):
1. Точная модель согласия по документации НСПК (форма согласия, порядок подписания, где хранится оригинал согласия — в ОПКЦ/банке плательщика; формат sign-ссылки/QR) — внешний вход [ТРЕБУЕТ ПРОВЕРКИ].
2. Семантика лимитов согласия (per-debit max, cumulative, frequency) и кто их считает (шлюз vs ОПКЦ) — продуктовое решение.
3. Каналы отзыва: только плательщик через свой банк, или также ТСП; нужно ли согласие на отзыв ТСП.
4. Поведение in-flight дебитов при отзыве/истечении согласия (дозачислить начатый vs остановить) — регуляторный вопрос.
5. Юридическая форма согласия и хранение ПДн (152-ФЗ, сроки) — юристы + ИБ.
6. AML/антифрод-пороги для рекуррентных списаний.
7. UX подписания согласия плательщиком (QR vs deep-link в приложение банка) — продукт.
8. Поддержка изменения лимита согласия без повторного подписания.

NFR (new):
- Consent registration p95 < 500ms.
- Consent sign notification → ACTIVE p95 < 5s.
- Recurring debit initiation p95 < 1s.
- Limit violation = 0 (100% enforced before ОПКЦ).
- Double debit = 0 (idempotency).
- Revoked consent → new debit = 0.
- Billing-day batch: sustained 200 TPS, burst 500 TPS (same as baseline), plus "массовый дебит" wave handled by queue backpressure.
- Consent reconciliation with ОПКЦ daily, 0 discrepancies.
- Availability ≥99.95%.

Acceptance criteria (positive + negative + rollback):
Positive:
- Create consent → sign → ACTIVE → recurring debit → PAID → CREDITED → COMPLETED, webhook.
- Limits enforced.
- Idempotent retries.
Negative:
- Debit on non-ACTIVE consent → rejected.
- Debit exceeding limit → rejected (before ОПКЦ).
- Duplicate eventId → ignored.
- ОПКЦ down → debit queued, no loss, reconciled.
- Revoke while debit in-flight → defined behavior (human decision).
Rollback:
- Feature flag `recurring.enabled`; stop-new (block new consent + new debit) without stopping one-time QR payments.
- No data migration back; consent records retained for audit; disable means reject new consent/debit requests.
- Signal: limit-violation rate > 0, or ОПКЦ consent protocol mismatch, or reconciliation discrepancy rate > threshold.

Now let me write everything. I'll start.

One more consideration: The user said "Код не пиши." (Don't write code.) The OpenAPI YAML and CALM JSON are not "code" in the programming sense — they are the required artifacts (deliverable #4 explicitly requires openapi changes, and CALM model is required). So writing YAML/JSON/Markdown is fine and expected. I will not write any application code (no walking skeleton, no mocks).

Let me write the files now.

I'll write ADR-008 first.
Я изучил всё ядро решения. Ключевые факты: принятое решение — «СБП-шлюз C2B», маршрут Critical (11/15), spine AD-001…AD-008 (AD-008 [ADOPTED]), статусная машина платежа (CREATED→QR_ISSUED→PAID→CREDITED→COMPLETED), где каждый платёж требует QR и действия клиента. Бизнес-запрос — рекуррентные C2B-списания по согласию (подписки СБП), что в репозитории ранее было помечено как roadmap «автоплатежи».

Составлю архитектурный пакет. Начну с ADR-008 и пакета изменений.

  `write_file(content="# Solutioning — Рекуррентные C2B-списания по согласию (подписки СБП)\n\n- Status: Proposed (архитектурный пакет изменения поверх принятого , file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/recurring-c2b/solutioning.md")`

Now let me write the change package (solutioning.md for recurring-c2b), which covers deliverables #1, #2, #4-summary, #5, #6, #7.

  `write_file(content="# Статусная машина согласия (consent) — спецификация переходов\n\n- Status: Draft (для ревью на гейте A1 пакета изменения)\n- Owner: soluti, file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/recurring-c2b/spec/consent-state-m)`

Now write the consent state machine spec.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\npaths:\n  /v1/payments:\n    post:\n      operationId: createPayment\, file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/openapi/tsp-api.yaml")`

Now edit the OpenAPI yaml (backward compatible). Let me carefully write the new yaml. I'll keep the existing content and add new paths and schemas.

Current yaml:
```yaml
openapi: 3.0.3
info:
  title: СБП-шлюз — API ТСП
  version: 0.1.0
paths:
  /v1/payments:
    post: ...
  /v1/payments/{paymentId}:
    get: ...
components:
  schemas:
    PaymentRequest:
      ...
    Payment:
      ...
```

I'll:
1. Bump version to 0.2.0.
2. Add optional `paymentType` and `consentId` to PaymentRequest and Payment.
3. Add new paths: /v1/consents, /v1/consents/{consentId}, /v1/consents/{consentId}/revoke.
4. Add ConsentRequest and Consent schemas.

Let me rewrite the full file to be safe and clean. Actually I'll use edit for targeted changes, but since there are several changes, rewriting the whole file via write_file is cleaner and I already read it. But write_file requires the file to exist and I've read it. It's fine.

Actually, I should use edit to make surgical changes to preserve the exact existing content and minimize diff. But multiple edits. Given the file is small, I'll rewrite it entirely with write_file, keeping existing content identical plus additions. Wait — the instruction says "write_file ... Unless the target's absence or current text contents have already been established in this session, you MUST use read_file first". I've read it. So write_file is allowed. But I must preserve existing exactly. Let me rewrite carefully.

Actually, to be safe and clear, let me use edit for the version bump + PaymentRequest/Payment, and edit to add new paths/schemas. Multiple edits on the same file. Let me do it with a few edit calls.

Let me do the edits:

Edit 1: version 0.1.0 → 0.2.0.
Edit 2: PaymentRequest add paymentType + consentId.
Edit 3: Payment add paymentType + consentId.
Edit 4: add new paths after /v1/payments/{paymentId} get.
Edit 5: add new schemas.

Actually, simpler to just rewrite the whole file. Let me write the complete new file.

Let me carefully compose the full YAML. I need to keep it valid OpenAPI 3.0.3.

Let me write it.
Теперь внесу обратно совместимые изменения в контракт API ТСП.

  `edit(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/contracts/tsp-api.md", old_string="- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)", new_string="- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.2 (нестабильная; аддитивное расширение 0.1 — согласия и рекуррентные платежи)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/contracts/tsp-api.md", old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `RECURRING_DISABLED` (403), `NOT_FOUND` (404), `C)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/contracts/tsp-api.md", old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`

Now I need to update `docs/contracts/tsp-api.md` — add §8 for consents and recurring, and update the version note. Also add new error codes and webhooks.

Let me edit tsp-api.md. I need to add:
1. Update the version header (0.1 → 0.2? The doc says "Версия контракта: 0.1"). Actually I'll add a note about 0.2 addition. Let me add a §8 section and update the status/version line, plus error codes and webhook events.

Let me make targeted edits.

First, update the header version line:
"Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)" → I'll change to reflect 0.2 draft with additive consent/recurring. Actually, let me keep it clean: change to "0.2 (нестабильная; аддитивное расширение 0.1 согласиями и рекуррентными платежами; до A1 фиксируется v1.0-draft)".

Second, add new error codes to §4 list.

Third, add new webhook events to §5.

Fourth, add §8 (Consents and recurring payments).

Let me do these edits.

Actually, let me be careful with the error codes line. Current:
"Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500)."

I'll add: `CONSENT_NOT_ACTIVE` (409), `CONSENT_LIMIT_EXCEEDED` (422), `CONSENT_EXPIRED` (422), `CONSENT_NOT_FOUND` (404), `RECURRING_DISABLED` (403).

Let me add these to the canonical codes list.

Let me make the edits now.

For the webhook events, current §5 lists:
- payment.completed, payment.failed, payment.expired, refund.completed/refund.failed.

I'll add consent events.

Let me do the edits via edit tool.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/contracts/tsp-api.md", offset=170, limit=30)`

I notice the header still says "# Контракт API ТСП (мерчант-API) — v0.1 draft" — I should update that too. Let me fix the title. Also I need to add §8 section for consents/recurring. Let me update the title and add §8.

Let me read the end of the file to see the current §7 and where to add §8.

  `edit(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/contracts/tsp-api.md", old_string="# Контракт API ТСП (мерчант-API) — v0.1 draft", new_string="# Контракт API ТСП (мерчант-API) — v0.2 draft")`
  `edit(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/contracts/tsp-api.md", old_string="Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (AD, new_string="Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (AD)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/contracts/tsp-api.md", old_string="## 7. Открытые вопросы (для A1)\n\n1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — road, new_string="## 7. Открытые вопросы (для A1)\n\n1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — road)`

Now let me add §8 section for consents and recurring payments before §7 (or after §6, before §7). Actually, the natural place is to add §8 after §7 (open questions), or insert new sections. But the existing §3 is "Методы" with 3.1-3.5. I should add consent methods as new subsections in §3 (3.6-3.8), and add a note in §3.2 about paymentType. And add §8 describing the consent/recurring contract.

Let me be careful about where to insert. The §3 methods currently are 3.1..3.5. I'll add 3.6 (создание согласия), 3.7 (статус согласия), 3.8 (отзыв согласия), and update §3.2 (создание платежа) to mention paymentType=RECURRING.

Actually, a cleaner approach: add a new top-level section §8 "Согласия и рекуррентные платежи (v0.2)" at the end, describing the new endpoints fully, and reference it from §3.2. This avoids deep edits into §3 and keeps the addition clearly marked as additive.

Let me add §8 at the end. Also fix the title "v0.1 draft" → "v0.2 draft".

Let me do the title fix and add §8.

For §8, I'll document:
- 8.1 Создание запроса согласия POST /v1/consents (request/response).
- 8.2 Статус согласия GET /v1/consents/{consentId}.
- 8.3 Отзыв согласия POST /v1/consents/{consentId}/revoke.
- 8.4 Рекуррентный дебит: POST /v1/payments с paymentType=RECURRING + consentId; семантика состояний (CREATED→PAID→CREDITED→COMPLETED, FAILED, без QR_ISSUED/EXPIRED).
- 8.5 Ошибки согласий.
- Note about backward compatibility.

Let me also update §3.2 to mention the optional paymentType/consentId fields (add to request example and rules). Actually I'll keep it minimal and put the detail in §8. I'll add a one-line note in §3.2.

Let me do the edits.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/contracts/opkc-adapter.md", offset=95)`

Now update the opkc-adapter.md contract — add §10 for consent operations and events. Let me add a new section at the end. The opkc-adapter.md currently has §1-9. Let me read its end to append §10.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/contracts/opkc-adapter.md", offset=80)`

The file seems to have fewer lines than expected (91 lines). Let me read the tail properly.

  `edit(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/contracts/opkc-adapter.md", old_string="## 9. Открытые вопросы\n\n1. Нужен ли синхронный `getReconciliationReport` или сверку делать событиями/файлами — решить с вендором на RFP (, new_string="## 9. Открытые вопросы\n\n1. Нужен ли синхронный `getReconciliationReport` или сверку делать событиями/файлами — решить с вендором на RFP ()`

Now append §10 to opkc-adapter.md for the consent/recurring operations and events. Let me add it.

  `edit(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/ARCHITECTURE-SPINE.md", old_string="- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec).", new_string="- Внутренний контракт шлюза (API ТСП): версия 0.2 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec; v0.2 — аддитивное расширени)`

Now update ARCHITECTURE-SPINE.md to add AD-009 and update Deferred section. Let me add AD-009 after AD-008, and update the Deferred section to note that автоплатежи (recurring) is now pulled back.

Let me look at the exact text to edit. The spine ends with AD-008, then "## Deferred", then "## Контракты и версии".

I'll:
1. Add AD-009 after AD-008 (before the "---" separator and "## Deferred").
2. Update the Deferred section to add a note about автоплатежи being returned.

Let me craft AD-009 in the spine's style.

AD-009:
```
## AD-009. Рекуррентное списание только по активному согласию в пределах лимитов

- Status: Proposed (ADR-008)
- **Binds**: сущность согласия (consent) в БД шлюза, статусная машина платежа, адаптер ОПКЦ.
- **Prevents**: списание без согласия, списание сверх лимитов согласия, списание по отозванному/истёкшему согласию, двойное списание при ретрае.
- **Rule**: Рекуррентный дебит инициируется только если согласие в состоянии `ACTIVE`, сумма дебита ≤ остаточного лимита согласия, в пределах срока действия. Согласие — отдельный конечный автомат с атомарными переходами (AD-002) и идемпотентностью (AD-003). Fitness: недостижимость дебита из `REVOKED`/`EXPIRED`/`DECLINED`; 0 превышений лимита.
```

For Deferred section, I'll add a note. The current Deferred section has three bullets. I'll add a note line about автоплатежи being returned. Actually, the Deferred section lists deferred items. Since автоплатежи is now returned (not deferred), I should add a "Returned" note. Let me add a bullet or a note.

Actually, the cleanest: add a note under Deferred heading like:
"- **Автоплатежи/рекуррентные списания (подписки СБП)**: возвращены из roadmap в scope (2026-09-28); см. ADR-008 и AD-009."

But автоплатежи wasn't in the spine's Deferred list (it was in solutioning.md roadmap). Let me check: the spine Deferred list has:
- Мультивалютность...
- C2C-переводы и выплаты B2C/B2B...
- Диспуты/претензии...

No автоплатежи. So I don't need to remove anything from Deferred. But I could add a note in the "Контракты и версии" section about the new ADR-008/AD-009. Actually, adding a note that the change exists is helpful. Let me add a small note in "Контракты и версии" referencing the new ADR and contract version.

Actually, the spine's "Контракты и версии" section says:
- Контракт НСПК: ...
- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — docs/contracts/tsp-api.md...
- Пиннинг версий...

I should update the "Внутренний контракт шлюза (API ТСП): версия 0.1 draft" to "0.2 draft" and note the consent/recurring extension. This is a faithful, accepted-way update (the contract version advanced).

Let me do these edits.

Edit 1: Add AD-009 after AD-008.
Edit 2: Update the "Внутренний контракт шлюза" version note.

Let me look at the exact AD-008 ending and Deferred start.

From my earlier read, the spine structure:
```
## AD-008. Стратегия реализации — гибрид [ADOPTED]
...
- **Rule**: ...

---

## Deferred (с причиной и условием возврата)
```

So I'll insert AD-009 between the AD-008 Rule line and the `---` before Deferred. Let me use the exact text.

The AD-008 section ends with:
"- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)"

I'll edit to insert AD-009 before the `---` and `## Deferred`.

Let me craft the edit with sufficient context.
Теперь обновлю spine — добавлю инвариант AD-009 и актуализирую версию контракта.

  `edit(file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/README.md", old_string="```\nARCHITECTURE-SPINE.md        инварианты AD-001..AD-008\ndocs/\n  solutioning.md             полный дизайн: компоненты, потоки, гейты, , new_string="```\nARCHITECTURE-SPINE.md        инварианты AD-001..AD-009\ndocs/\n  solutioning.md             полный дизайн: компоненты, потоки, гейты, )`

Now update README.md to reference the new artifacts. Let me add a line to the "Ключевые документы" or "Структура" section.

The README structure section lists:
```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-008
docs/
  solutioning.md             ...
  nfr.md                     ...
  contracts/tsp-api.md       ...
  contracts/opkc-adapter.md  ...
  spec/state-machine.md      ...
  rfp/vendor-rfp.md          ...
  adr/ADR-001..007.md        ...
.arch-handoff/               ...
```

I'll update:
- "инварианты AD-001..AD-008" → "AD-001..AD-009"
- add a line for recurring-c2b package and calm model.

Let me edit the README structure block.

  `write_file(content="{\n  \"$schema\": \"https://calm.finos.org/release/1.2/meta/calm.json\",\n  \"unique-id\": \"recurring-c2b-consent\",\n  \"name\": \"Рекурр, file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/calm/recurring-c2b-consent.archite)`

Now I need to create the CALM model. This is the last major artifact. Let me write a valid CALM architecture JSON.

Let me carefully construct it following the CALM v1.2 schema.

Top-level:
```json
{
  "$schema": "https://calm.finos.org/release/1.2/meta/calm.json",
  "unique-id": "recurring-c2b-consent",
  "name": "Recurring C2B payments by payer consent (SBP subscriptions)",
  "description": "...",
  "metadata": [...],
  "nodes": [...],
  "relationships": [...],
  "flows": [...],
  "controls": {...}
}
```

Nodes (14):
1. tsp — actor
2. payer — actor
3. payer-bank — ecosystem
4. opkc-nspk — ecosystem
5. abs — system
6. sbp-gateway — system (container, composed-of)
7. tsp-api — service
8. payment-state-machine — service
9. consent-state-machine — service
10. opkc-adapter — service
11. abs-adapter — service
12. notifier — service
13. gateway-db — database
14. antifraud-aml — service

Interfaces (on key nodes, interface-type flexible):
- tsp-api: [{unique-id: "tsp-api-https", url: "https://api.bank.ru/sbp/v1"}]
- opkc-adapter: [{unique-id: "opkc-adapter-mtls", url: "https://opkc-adapter.internal:8443"}]
- abs-adapter: [{unique-id: "abs-adapter-api", url: "https://abs-adapter.internal:9443"}]
- notifier: [{unique-id: "notifier-webhook-out", url: "https://notifier.internal"}]

Actually to keep it simpler and valid, I'll add interfaces to the key external-facing nodes. Let me add interfaces where it adds clarity.

Relationships (connects for system-system, interacts for payer→payer-bank, composed-of for sbp-gateway):

1. `tsp-to-tsp-api` connects tsp→tsp-api (HTTPS)
2. `payer-signs-in-bank` interacts actor=payer nodes=[payer-bank] (payer signs consent in payer bank)
3. `payer-bank-to-opkc` connects payer-bank→opkc-nspk (mTLS) — consent signing + debit execution between payer bank and ОПКЦ
4. `tsp-api-to-payment-sm` connects tsp-api→payment-state-machine (HTTPS)
5. `tsp-api-to-consent-sm` connects tsp-api→consent-state-machine (HTTPS)
6. `payment-sm-to-db` connects payment-state-machine→gateway-db (JDBC)
7. `consent-sm-to-db` connects consent-state-machine→gateway-db (JDBC)
8. `payment-sm-to-opkc-adapter` connects payment-state-machine→opkc-adapter (HTTPS)
9. `consent-sm-to-opkc-adapter` connects consent-state-machine→opkc-adapter (HTTPS)
10. `opkc-adapter-to-opkc` connects opkc-adapter→opkc-nspk (mTLS)
11. `payment-sm-to-abs-adapter` connects payment-state-machine→abs-adapter (AMQP)
12. `abs-adapter-to-abs` connects abs-adapter→abs (HTTPS)
13. `payment-sm-to-notifier` connects payment-state-machine→notifier (AMQP)
14. `consent-sm-to-notifier` connects consent-state-machine→notifier (AMQP)
15. `notifier-to-tsp` connects notifier→tsp (HTTPS)
16. `payment-sm-to-antifraud` connects payment-state-machine→antifraud-aml (HTTPS)
17. `consent-sm-to-antifraud` connects consent-state-machine→antifraud-aml (HTTPS)
18. `sbp-gateway-composed` composed-of container=sbp-gateway nodes=[tsp-api, payment-state-machine, consent-state-machine, opkc-adapter, abs-adapter, notifier]

That's a solid model.

Flows (2):

Flow 1: consent-creation-and-signing
transitions:
1. tsp-to-tsp-api (source-to-destination): ТСП создаёт запрос согласия
2. tsp-api-to-consent-sm (source-to-destination): запрос согласия в статусную машину согласия
3. consent-sm-to-opkc-adapter (source-to-destination): регистрация согласия в адаптере ОПКЦ
4. opkc-adapter-to-opkc (source-to-destination): регистрация согласия в ОПКЦ
5. opkc-adapter-to-opkc (destination-to-source): ОПКЦ возвращает sign-ссылку/QR
6. consent-sm-to-db (source-to-destination): сохранение PENDING_SIGN
7. tsp-api-to-consent-sm ... hmm, actually the sign link goes back to TSP via tsp-api. Let me simplify transitions to the essential path.

Actually, let me keep flows concise but meaningful. A flow's transitions reference relationships. I need each transition to reference a relationship and a direction.

Flow 1 "consent-creation-and-signing-flow":
- seq 1: tsp-to-tsp-api, source-to-destination: "ТСП создаёт запрос согласия (POST /v1/consents)"
- seq 2: tsp-api-to-consent-sm, source-to-destination: "API передаёт запрос в статусную машину согласия"
- seq 3: consent-sm-to-opkc-adapter, source-to-destination: "Регистрация согласия в адаптере ОПКЦ"
- seq 4: opkc-adapter-to-opkc, source-to-destination: "Запрос регистрации согласия в ОПКЦ"
- seq 5: opkc-adapter-to-opkc, destination-to-source: "ОПКЦ возвращает sign-ссылку/QR плательщику"
- seq 6: payer-signs-in-bank, source-to-destination: "Плательщик подписывает согласие в приложении своего банка" (interacts has no direction semantics; I'll set direction source-to-destination default)

Wait — for `interacts` relationships, there's no source/destination. The transition direction enum is "source-to-destination"/"destination-to-source". For interacts, "source-to-destination" would mean "actor → nodes" presumably. It's ambiguous but the schema just requires a direction value (default source-to-destination). I'll set direction for interacts to "source-to-destination" (meaning actor initiates toward nodes). Actually the flow-creation doc says direction is about the relationship's from/to nodes; for interacts there's no from/to. To avoid confusion, I'll just include the payer signing via a `connects` relationship between payer-bank and opkc-nspk instead of interacts, OR keep interacts and not over-think. 

Hmm, let me reconsider. The `interacts` relationship type connects an actor to nodes (e.g., a human interacts with a system). For flows, using interacts is a bit awkward. To keep flows clean and unambiguous, I'll model the payer signing as:
- relationship `payer-signs-consent`: connects payer → payer-bank (source=payer, dest=payer-bank). Actually payer is an actor, and "connects" is described as "systematic node-to-node connections (service-to-database, API-to-service)". But connects just requires source/destination node-interface with node ids; node-type doesn't restrict. I think connects is fine for actor→system too, though the guide says interacts is for actor→system. 

The guide says: "interacts: Use for actor-to-system interactions (user interacts with application, external system interacts with API)". And "connects: Use for systematic node-to-node connections (service-to-database, API-to-service, etc.)".

To be safe and semantically correct, I'll use `interacts` for the payer (actor) interacting with payer-bank, and just not include that in a flow (or include with direction and accept the default). Actually, I can include it in the flow with direction "source-to-destination" — the interacts type has `actor` and `nodes`; there's no explicit "from/to", but the flow tool's transition just references a relationship-unique-id and a direction. The validator likely doesn't cross-check direction vs relationship type deeply. But Spectral might. Let me minimize risk: keep interacts for payer, but DON'T reference it in flows. Instead, in the consent flow, represent the payer signing step via the `payer-bank-to-opkc` connection (payer bank notifies ОПКЦ of signature) and `opkc-adapter-to-opkc` (ОПКЦ notifies gateway). That keeps flows using only `connects` relationships with clear direction.

So for Flow 1, transitions (all connects):
- seq1: tsp-to-tsp-api (s2d): "ТСП создаёт запрос согласия"
- seq2: tsp-api-to-consent-sm (s2d): "Передача в статусную машину согласия"
- seq3: consent-sm-to-opkc-adapter (s2d): "Регистрация согласия в адаптере ОПКЦ"
- seq4: opkc-adapter-to-opkc (s2d): "Запрос регистрации согласия в ОПКЦ"
- seq5: opkc-adapter-to-opkc (d2s): "ОПКЦ возвращает sign-ссылку/QR; статус PENDING_SIGN"
- seq6: consent-sm-to-db (s2d): "Сохранение PENDING_SIGN + outbox"
- seq7: opkc-adapter-to-opkc (d2s): "Событие consent.signed от ОПКЦ после подписания плательщиком"  — hmm, this is again the same relationship. Using the same relationship twice with different descriptions is fine.

Actually, let me simplify: 
- seq7: consent-sm-to-db... no.

Let me write a clean flow:

Flow 1 transitions:
1. tsp-to-tsp-api (s2d): "ТСП инициирует создание согласия"
2. tsp-api-to-consent-sm (s2d): "Запрос в статусную машину согласия"
3. consent-sm-to-opkc-adapter (s2d): "Регистрация запроса согласия в адаптере ОПКЦ"
4. opkc-adapter-to-opkc (s2d): "Отправка запроса согласия в ОПКЦ"
5. opkc-adapter-to-opkc (d2s): "ОПКЦ возвращает sign-ссылку/QR (PENDING_SIGN)"
6. consent-sm-to-db (s2d): "Сохранение согласия и outbox-события"
7. opkc-adapter-to-opkc (d2s): "ОПКЦ доставляет событие consent.signed после подписания плательщиком"
8. consent-sm-to-notifier (s2d): "Нотификация ТСП (consent.signed)"

Flow 2 "recurring-debit-flow":
1. tsp-to-tsp-api (s2d): "ТСП инициирует рекуррентный дебит (paymentType=RECURRING)"
2. tsp-api-to-payment-sm (s2d): "Запрос в статусную машину платежа"
3. payment-sm-to-db (s2d): "Guard: проверка согласия ACTIVE и лимита (consent store)"
4. payment-sm-to-opkc-adapter (s2d): "Инициация дебита в адаптере ОПКЦ"
5. opkc-adapter-to-opkc (s2d): "Инициация рекуррентного дебита в ОПКЦ"
6. opkc-adapter-to-opkc (d2s): "ОПКЦ подтверждает списание (payment.paid)"
7. payment-sm-to-abs-adapter (s2d): "Зачисление на счёт ТСП через адаптер АБС"
8. abs-adapter-to-abs (s2d): "Зачисление в АБС"
9. payment-sm-to-notifier (s2d): "Нотификация ТСП (payment.completed)"

Wait, flow 2 seq 3 references payment-sm-to-db which connects payment-state-machine → gateway-db. But guard check of consent is really reading the consent state from DB. It's fine to model as "payment state machine reads consent + payment from gateway DB". But semantically the guard is a check by the payment state machine against the consent store (same DB). I'll describe it as "Guard AD-009: проверка согласия ACTIVE и лимита в БД шлюза". Good.

Actually there's a subtlety: the guard is checked by the payment-state-machine or by a coordinator. For the model, describing it as the payment state machine checking the DB is fine.

Now controls. I'll add top-level controls:
- consent-limit-enforcement
- idempotency
- audit-trail
- nps-compliance
- pdn-minimization
- consent-revocation-propagation

Each control: {description, requirements: [{requirement-url, config}]}.

requirement-url: use valid URIs. I'll use `https://schemas.bank.ru/controls/<name>.json`. config: inline object.

Let me write controls carefully following the schema:
```json
"controls": {
  "consent-limit-enforcement": {
    "description": "Рекуррентный дебит только по ACTIVE-согласию в пределах лимита и срока (AD-009)",
    "requirements": [
      {
        "requirement-url": "https://schemas.bank.ru/controls/consent-limit-enforcement.json",
        "config": {
          "guard": "status==ACTIVE AND amount<=remainingLimit AND now<=expiresAt",
          "enforcement-point": "before-initiateRecurringPayment",
          "authoritative-check": "OPKC"
        }
      }
    ]
  },
  ...
}
```

This should validate. The requirement-url is a string, config is an object. Good.

Now metadata. Top-level metadata: I'll use an array of objects.

Let me also double check: node `details` property allows only `detailed-architecture` and `required-pattern`. I won't use details.

For node interfaces, I'll use `interface-type` (flexible): `{unique-id: "...", url: "..."}`. This is valid (additionalProperties true).

Let me also consider whether the `calm validate -a` will try to resolve the `$schema` URL `https://calm.finos.org/release/1.2/meta/calm.json` over network. If offline, it might fail. The CLI v1.60.1 likely bundles schemas. Let me check if there's a bundled schema in node_modules. Actually, the calm-cli is available via npx (it's installed somewhere). Let me just try to validate and see the output. If it fails due to network, I'll use `--schema-directory` pointing to bundled schemas if they exist, or a local schema.

Let me write the CALM file now, then validate.

Let me write it carefully as valid JSON.

One concern: the `node-type` values. The enum includes: actor, ecosystem, system, service, database, network, ldap, webclient, data-asset. I'll use only these. For "payer-bank" and "opkc-nspk", I'll use `ecosystem` (external). For "abs" I'll use `system`. For "tsp" and "payer" — `actor`.

Let me also make sure `interacts` relationship is valid: `{actor: string, nodes: [string]}`. I'll use it for payer→payer-bank. But I decided not to reference it in flows. It can still exist as a relationship (the model includes it as a relationship, just not in flows). That's fine.

Actually, wait — should I include the payer-signs-in-bank interacts relationship at all if it's not in a flow? Yes, it's part of the architecture (payer interacts with their bank to sign the consent). It's good to include for completeness.

Let me finalize the relationship list. I'll also include the `payer-bank-to-opkc` connects for the debit execution between payer bank and ОПКЦ? Actually the debit execution: gateway → ОПКЦ → payer's bank debits payer account. The payer-bank is involved. But for the gateway's view, the debit goes gateway → ОПКЦ (adapter). ОПКЦ coordinates with payer bank. So payer-bank-to-opkc is a relationship outside the gateway's direct view but relevant to the flow. I'll include `opkc-nspk-to-payer-bank` connects (ОПКЦ → payer bank executes debit) to show the full path. Let me add it as connects `payer-bank-executes-debit`: source=opkc-nspk, dest=payer-bank (mTLS). And reference in flow 2 between step 5 and 6.

Hmm, but that complicates. Let me include it for completeness since the task asks for "потоки" (flows) that traverse the architecture, and the debit does traverse payer's bank. I'll add:

- `opkc-to-payer-bank`: connects opkc-nspk → payer-bank (mTLS), description "инициирует списание со счёта плательщика".

And in flow 2, insert between step 5 (gateway→ОПКЦ) and step 6 (ОПКЦ→gateway confirmation):
- seq: opkc-to-payer-bank (s2d): "ОПКЦ списывает со счёта плательщика в банке плательщика"

That's nice and complete.

Let me also reconsider the consent signing flow with payer bank: payer signs in payer-bank app → payer-bank notifies ОПКЦ → ОПКЦ notifies gateway (consent.signed). The payer-bank-to-opkc relationship covers "payer bank → ОПКЦ". I'll add `payer-bank-to-opkc` connects payer-bank → opkc-nspk. And reference in flow 1 after step 5.

So additional relationships:
- `payer-bank-to-opkc`: connects payer-bank → opkc-nspk (mTLS): "банк плательщика регистрирует подпись согласия в ОПКЦ"
- `opkc-to-payer-bank`: connects opkc-nspk → payer-bank (mTLS): "ОПКЦ инициирует списание в банке плательщика"

Flow 1 updated transitions:
1. tsp-to-tsp-api (s2d)
2. tsp-api-to-consent-sm (s2d)
3. consent-sm-to-opkc-adapter (s2d)
4. opkc-adapter-to-opkc (s2d)
5. opkc-adapter-to-opkc (d2s): "sign-ссылка/QR (PENDING_SIGN)"
6. consent-sm-to-db (s2d): "сохранение PENDING_SIGN + outbox"
7. payer-bank-to-opkc (s2d): "банк плательщика подтверждает подпись в ОПКЦ" — actually this is the payer signing. The interacts payer→payer-bank covers the payer's action; payer-bank-to-opkc covers the bank→ОПКЦ. Let me use:
7. payer-bank-to-opkc (s2d): "банк плательщика передаёт подпись согласия в ОПКЦ"
8. opkc-adapter-to-opkc (d2s): "ОПКЦ доставляет consent.signed в шлюз"
9. consent-sm-to-db (s2d): "переход в ACTIVE + outbox"
10. consent-sm-to-notifier (s2d): "вебхук consent.signed ТСП"

That's a clean flow. But maybe I'm over-detailing. Let me keep it reasonable — around 8-10 transitions is fine.

Let me finalize and write.

Actually, let me reduce risk of validation issues by keeping the model well-formed and not too exotic. Let me write it now.

For protocol values, use only from enum: HTTP, HTTPS, FTP, SFTP, JDBC, WebSocket, SocketIO, LDAP, AMQP, TLS, mTLS, TCP.

Let me write the JSON file.
Теперь создам CALM-модель изменения и провалидирую её.

  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wre6d78/ws && npx --no-install @finos/calm-cli , description="Validate CALM architecture model")`

Now validate the CALM model. Let me run the validate command. First, let me verify the JSON is valid, and then run `npx @finos/calm-cli validate -a ...`.

Let me run the validation.

  `write_file(content="{\n  \"$schema\": \"https://json-schema.org/draft/2020-12/schema\",\n  \"$id\": \"https://schemas.bank.ru/controls/consent-limit-enforcemen, file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/calm/controls/consent-limit-enforc)`
  `write_file(content="{\n  \"$schema\": \"https://json-schema.org/draft/2020-12/schema\",\n  \"$id\": \"https://schemas.bank.ru/controls/idempotency.json\",\n  \, file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/calm/controls/idempotency.requirem)`
  `write_file(content="{\n  \"$schema\": \"https://json-schema.org/draft/2020-12/schema\",\n  \"$id\": \"https://schemas.bank.ru/controls/consent-revocation.json\, file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/calm/controls/consent-revocation.r)`
  `write_file(content="{\n  \"$schema\": \"https://json-schema.org/draft/2020-12/schema\",\n  \"$id\": \"https://schemas.bank.ru/controls/nps-compliance.json\",\n, file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/calm/controls/nps-compliance.requi)`
  `write_file(content="{\n  \"$schema\": \"https://json-schema.org/draft/2020-12/schema\",\n  \"$id\": \"https://schemas.bank.ru/controls/pdn-minimization.json\",, file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/calm/controls/pdn-minimization.req)`
  `write_file(content="{\n  \"$schema\": \"https://json-schema.org/draft/2020-12/schema\",\n  \"$id\": \"https://schemas.bank.ru/controls/audit-trail.json\",\n  \, file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/calm/controls/audit-trail.requirem)`
  `write_file(content="{\n  \"$schema\": \"https://json-schema.org/draft/2020-12/schema\",\n  \"$id\": \"https://schemas.bank.ru/controls/credit-only-from-paid.js, file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/calm/controls/credit-only-from-pai)`
  `write_file(content="{\n  \"https://schemas.bank.ru/controls/consent-limit-enforcement.json\": \"controls/consent-limit-enforcement.requirement.json\",\n  \"htt, file_path="<HARNESS>/runs-clean/cells/wre6d78/ws/docs/calm/url-mapping.json")`

The validator is trying to load the `requirement-url` schemas from `https://schemas.bank.ru/...`, which is not allowlisted and doesn't exist. The control schema's `requirement-url` is actually resolved by the validator as a schema to validate against. I need to make the requirement-url resolvable locally, or use a `config-url` / local file.

The error says "Could not load requirement schema from 'https://schemas.bank.ru/controls/...': Direct URL loading is restricted to approved hosts."

Options:
1. Use a local file path for requirement-url. But requirement-url is supposed to be a URL. However, the CLI supports `--url-to-local-file-mapping`. But that requires a mapping file.
2. Use `config-url` instead of `config`? No, that's for config, not requirement.
3. Use a `calm.finos.org` URL that's allowlisted? The allowed hosts likely include `calm.finos.org` and `json-schema.org`. But the requirement-url needs to point to an actual resolvable requirement schema.

Actually, let me reconsider. The controls in CALM use `requirement-url` which must be resolvable. The cleanest fix: provide local requirement schema files in the repo (e.g., under `docs/calm/controls/`) and reference them via relative paths or via a URL mapping.

Actually, the simplest robust approach: 
- Create local requirement JSON files under `docs/calm/controls/*.json`.
- Reference them with `requirement-url` as relative paths? The schema requires `requirement-url` to be a string (a URI). The CLI's DirectUrlDocumentLoader resolves URLs. For local files, maybe use `file://` or relative path with url mapping.

Looking at the CLI instructions, there's `--url-to-local-file-mapping` which maps URLs to local paths. So I can:
- Keep the `requirement-url` as a canonical URL (e.g., `https://calm.finos.org/...` or a bank URL), and provide a mapping file mapping those URLs to local files.

But actually, a simpler approach that many CALM examples use: point `requirement-url` to a local relative path. Let me check how the validator resolves relative paths. The control-creation guide says requirement-url is "The requirement schema that specifies how a control should be defined" — an accessible URL. 

Actually, let me reconsider the whole controls approach. The `calm validate` is trying to load the requirement-url as a JSON schema and validate the `config` against it. This is the "control-requirement-validation" rule. To pass validation, the requirement-url must resolve to a loadable document.

The simplest fix: create local requirement schema files and use `--url-to-local-file-mapping` OR make requirement-url a local file path that the loader can resolve.

Let me check what the CLI accepts. The error mentions `DirectUrlDocumentLoader` and "approved hosts". There's a config with `--allowed-remote-hosts`. But adding schemas.bank.ru as allowed host won't help since the URL doesn't actually exist (it's synthetic).

Better: use local files. Let me create the requirement schema files under `docs/calm/controls/` and reference them via a mapping.

Actually, let me reconsider: maybe I should simplify and make the requirement-url point to a well-known, actually-resolvable CALM standard, OR use `config-url` pointing to a local file, OR — the cleanest — provide local requirement files and map them.

Let me think about what's cleanest and actually passes:

Approach A: Create local requirement JSON files and reference them with relative paths directly in `requirement-url`. The loader might resolve relative paths relative to the architecture file location. The CLI doc says "For patterns without an `$id` field, the CLI automatically resolves relative `$ref` paths against the pattern file's directory." That's for `$ref` in patterns. For requirement-url in controls, it uses DirectUrlDocumentLoader which expects URLs.

Approach B: Use `--url-to-local-file-mapping` with a JSON mapping file that maps my synthetic URLs to local files. This is explicitly supported.

Approach C: Use a requirement-url that is a real, allowlisted, resolvable URL. The allowlisted hosts probably include `calm.finos.org` (for the meta schemas). If I point requirement-url to something under `https://calm.finos.org/...`, would it resolve? Only if that file actually exists at that URL. It probably doesn't.

Approach D: Reconsider whether I even need `requirement-url` to be a URL. The schema `control-detail` requires `requirement-url` (string) and oneOf config-url/config. But the validator's `control-requirement-validation` Spectral rule loads the requirement-url as a schema. If I can't provide a resolvable requirement-url, validation fails.

Hmm. Let me look more carefully. Is `control-requirement-validation` a Spectral rule that's part of the default ruleset? It seems so. The rule loads requirement-url and validates config against it.

The robust solution: create local requirement schema files and use the url-to-local-file-mapping.

Let me do Approach B:
1. Create requirement JSON schema files under `docs/calm/controls/` (e.g., `consent-limit-enforcement.requirement.json`, etc.). These are JSON schemas describing the config.
2. Create a mapping file `docs/calm/url-mapping.json` mapping each synthetic URL to the local relative path.
3. Run validate with `-u docs/calm/url-mapping.json`.

Actually, simpler: since the mapping maps URL → local path (relative to the mapping file's location), I can keep my synthetic URLs and map them.

But wait — do I even need the requirement files to be JSON schemas? The `control-requirement-validation` rule validates the control's `config` against the requirement-url (as a schema). If the requirement-url points to a JSON schema, it validates config against it. If the requirement file is not a valid schema, it might error differently.

Let me create minimal valid JSON schema requirement files. Each requirement file is a JSON schema that `config` must conform to. I'll make them permissive (e.g., `{ "$schema": "https://json-schema.org/draft/2020-12/schema", "type": "object", "additionalProperties": true }`). That way config always validates.

Actually, even simpler and more meaningful: make each requirement a JSON schema with `type: object`. My config objects will validate.

But there's subtlety: what's the exact expected structure of a "requirement" file? The control-creation guide says requirement-url points to a "requirement.json file that defines what the control expects", and "Requirements may optionally use Standards as their base JSON schema". So a requirement file is essentially a JSON schema.

Let me create:
- `docs/calm/controls/consent-limit-enforcement.requirement.json`
- `docs/calm/controls/idempotency.requirement.json`
- `docs/calm/controls/consent-revocation.requirement.json`
- `docs/calm/controls/nps-compliance.requirement.json`
- `docs/calm/controls/pdn-minimization.requirement.json`
- `docs/calm/controls/audit-trail.requirement.json`
- `docs/calm/controls/credit-only-from-paid.requirement.json`

Each a minimal JSON schema.

Then a mapping file `docs/calm/url-mapping.json`:
```json
{
  "https://schemas.bank.ru/controls/consent-limit-enforcement.json": "controls/consent-limit-enforcement.requirement.json",
  ...
}
```

And run: `npx --no-install @finos/calm-cli validate -a docs/calm/recurring-c2b-consent.architecture.json -u docs/calm/url-mapping.json -f pretty`

Wait, but the mapping paths are "resolved relative to the mapping file's location". So mapping file at `docs/calm/url-mapping.json`, relative path `controls/consent-limit-enforcement.requirement.json` → `docs/calm/controls/consent-limit-enforcement.requirement.json`. Good.

But actually, there might be an even simpler approach: make `requirement-url` a `file://` URL pointing to the local file. But the DirectUrlDocumentLoader might reject file://. The url-to-local-file-mapping is the documented way.

Alternatively, I recall the `--url-to-local-file-mapping` flag description: "Path to JSON file mapping URLs to local paths". And "Paths are resolved relative to the mapping file's location." Good.

Let me also double check: do the flow-level controls also need requirement files? Yes — they use `requirement-url` too (`audit-trail` and `credit-only-from-paid`). My mapping covers `audit-trail` and `credit-only-from-paid`.

Now, also the flow-level controls use the same requirement-url for audit-trail (top-level `audit-trail` and flow-level `consent-lifecycle-audit` both reference `https://schemas.bank.ru/controls/audit-trail.json`). Both map to the same local file. Good.

Let me create the requirement files. I need to make them valid JSON schemas. Minimal:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.bank.ru/controls/consent-limit-enforcement.json",
  "title": "Consent limit enforcement control requirement",
  "type": "object",
  "properties": {
    "guard": { "type": "string" },
    "enforcement-point": { "type": "string" },
    "authoritative-check": { "type": "string" }
  },
  "additionalProperties": true
}
```

Wait, but should I include `$id` matching the URL? If I include `$id`, and the loader maps the URL to the local file, the `$id` might be used for resolution. Probably fine either way. To be safe, I'll include `$id` matching the URL so the loaded document's identity matches. Actually, when using url-to-local-file-mapping, the loader loads the local file in place of the URL; the `$id` inside doesn't strictly need to match, but it's cleaner. I'll include it.

Actually, let me keep it simpler and avoid potential issues: minimal schema with `type: object` and `additionalProperties: true`, plus title/description. I'll include `$schema` and `$id`.

Let me define each requirement file's properties to loosely match my config. But since `additionalProperties: true`, the config will validate regardless. So I can keep them minimal and uniform.

Let me write a generic requirement template and create 7 files. Actually, to reduce file count, could I use ONE requirement file for all controls? The mapping maps URLs → local paths; multiple URLs can map to the same file. But each requirement-url is different (different file names). I could map all 7 URLs to a single generic requirement file. That's clean: one generic requirement schema file, and the mapping maps all synthetic URLs to it.

Let me do that:
- `docs/calm/controls/control-requirement.json` (generic, `type: object`, `additionalProperties: true`).
- Mapping maps each of the 7 URLs to `controls/control-requirement.json`.

But wait — is it weird to map different URLs to the same file? It's fine for validation. But semantically, having distinct requirement files is more meaningful. However, for a change package, one generic requirement + specific config inline is acceptable and keeps the repo clean. Actually, let me create distinct requirement files to be more faithful (each control has its own requirement definition), but keep them minimal. Hmm, 7 files is a lot of noise.

Compromise: Create distinct requirement files but make them tiny. Actually, I'll go with distinct files because it's more correct and the task emphasizes "контроли" (controls) as a real deliverable. But 7 files + mapping is heavy. 

Let me reconsider: do I actually need the mapping approach, or can I just point requirement-url directly to relative local paths?

Let me test whether relative paths work directly. The DirectUrlDocumentLoader is URL-based. A relative path like "controls/foo.json" is not a valid URL. But maybe the CLI resolves relative paths. The CLI doc says relative `$ref` resolution is for patterns. For requirement-url, unclear.

The cleanest documented approach is url-to-local-file-mapping. Let me use it.

Actually, wait — there might be an even simpler approach. Let me check the `calm` CLI config: the error said "Direct URL loading is restricted to approved hosts. Host 'schemas.bank.ru' is not allowlisted." and suggested `calm init-config --allowed-remote-hosts schemas.bank.ru`. This means the CLI has an allowlist and a DirectUrlDocumentLoader that fetches URLs. The `--url-to-local-file-mapping` intercepts before fetching.

Let me go with url-to-local-file-mapping. I'll create:
1. `docs/calm/controls/` with 7 requirement files (or fewer).
2. `docs/calm/url-mapping.json`.

Actually, let me reduce to a cleaner set. I'll create distinct requirement files for the 7 distinct URLs (6 top-level + credit-only-from-paid + audit-trail shared). The distinct URLs are:
1. consent-limit-enforcement.json
2. idempotency.json
3. consent-revocation.json
4. nps-compliance.json
5. pdn-minimization.json
6. audit-trail.json (used twice: top-level + flow)
7. credit-only-from-paid.json (flow)

So 7 requirement files. Let me create them all under docs/calm/controls/.

To keep it manageable, I'll make each requirement file a small JSON schema with a title, description, type object, and relevant properties (loosely matching config), plus additionalProperties true.

Let me write them efficiently. Actually, I can write them as compact single-purpose schemas. Let me generate them.

Hmm, this is getting heavy. Let me reconsider whether there's a simpler validation path.

Alternative: Does `calm validate` have a `--strict` or a mode that skips control-requirement-validation? No.

Alternative: Use `config-url` pointing to a local file instead of inline `config`, and still need requirement-url resolvable. No, requirement-url is always required.

Alternative: Remove `controls` entirely from the model. But the task explicitly requires "контроли" (controls) in the model. So I must keep controls and make them validate.

OK, let me just create the requirement files + mapping. It's the correct, faithful approach.

Let me write a single generic requirement schema and map all URLs to it, to minimize noise. Actually, I'll do a middle ground: create the requirement files with meaningful (but loose) schemas. I'll write them compactly.

Let me create them. I'll write each file with the `write_file` tool. 7 files + 1 mapping = 8 files. That's fine.

Actually, let me reduce: I can map multiple URLs to ONE requirement file, since the mapping is URL→file and I control both. But semantically distinct controls referencing the same requirement schema is actually fine and even realistic (a shared "control requirement" standard). But then the requirement file would be generic.

Let me go with distinct requirement files (7), each minimal. This is the most faithful and avoids any weirdness.

Let me write them. I'll make each a valid JSON schema (2020-12).

Let me write a helper mentally and just produce 7 files.

Actually, to save effort and tokens, I'll create the requirement files with minimal but valid content. Each:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.bank.ru/controls/<name>.json",
  "title": "<Title>",
  "type": "object",
  "additionalProperties": true
}
```

That's enough to validate my inline configs (which are objects). I'll add a `description` field too for documentation.

Let me write all 7 files and the mapping file in parallel (multiple write_file calls in one message).

Then re-run validate with `-u`.

Let me write them.
Валидатор требует, чтобы `requirement-url` контролей резолвился в локальную схему. Создам локальные requirement-схемы и файл маппинга URL→файл.

  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wre6d78/ws && npx --no-install @finos/calm-cli , description="Validate CALM model with url mapping")`
  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wre6d78/ws && python3 -c \"import yaml,sys; d=y, description="Check OpenAPI YAML syntax")`

The CALM model validates cleanly: "Errors: no (0), Warnings: no (0), No issues found."

Now let me verify the other changed files don't have obvious issues. Let me run a quick check:
1. The OpenAPI YAML — validate it's well-formed. I can check with a quick YAML parse or an openapi linter. There's no openapi linter installed necessarily. Let me at least verify YAML is valid via a quick node/python check.

Actually, the repo's node_modules has @apidevtools (swagger-parser?) and @braintree. Let me check if there's a way to validate the OpenAPI. Actually, simpler: check YAML syntax with python yaml or node.

Let me verify:
- YAML validity of openapi/tsp-api.yaml (using python3 -c with yaml, or node).
- JSON validity of the CALM file (already validated by calm CLI, so it's valid JSON).
- The requirement files are valid JSON (validated indirectly by the mapping load — they loaded fine).

Let me also run the repo's own fitness checks if there's a command. The .arch-handoff/CONSTRAINTS.yaml mentions `arch control check` but that's a different tool (not installed?). There's no clear test command. The RUBRIC.yaml references "arch control check" with `control::check` schema. This seems to be a BMAD/arch tool not available in this environment. I'll not run it.

Let me at least validate the OpenAPI YAML syntactically. Let me check if python3 with yaml is available, or use node with a yaml parser. node_modules has... let me check for js-yaml or yaml package.

Actually, I can use the `@apidevtools/swagger-parser` or `@redocly/openapi-cli` if installed. Let me just do a simple YAML syntax check.

Let me check node_modules for a yaml parser. Actually, simpler: use python3 yaml.
CALM-модель провалидирована чисто (0 ошибок, 0 предупреждений). Проверю синтаксис изменённого OpenAPI-файла.

  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wre6d78/ws && git status --short && echo \"--- , description="Show git status and diff stat")`

The OpenAPI YAML is valid. All checks pass.

Now let me do a final review of what I've created/changed, and make sure everything is consistent. Let me run `git status` and `git diff --stat` to summarize.

Also, I should double check the spine change didn't break the "spine-lints-clean" rule (no TODO/TBD/XXX in ARCHITECTURE-SPINE.md). My additions don't contain those. Good.

Let me also verify the RUBRIC / CONSTRAINTS fitness rules: 
- `adr-no-placeholders`: docs/adr/*.md must NOT contain `<!--`. My ADR-008 has no `<!--`. Good.
- `nfr-measurable`: docs/nfr.md must contain '99,95'. I didn't touch docs/nfr.md (the base NFR file still has it). Good. My new NFR is in docs/recurring-c2b/solutioning.md, not docs/nfr.md, so the base rule still passes.
- `abs-credit-only-from-paid`: ADR-005 must contain 'только из состояния `PAID`'. I didn't touch ADR-005. Good.

Let me run git status and diff to confirm the set of changes and that I haven't accidentally touched unrelated files.

Let me also verify there are no leftover issues: the README now references docs/recurring-c2b/ and docs/calm/ which exist. Good.

Let me run git status.

  `write_file(content="---\nname: CALM validation in this repo\ndescription: How to validate FINOS CALM models here — npx command and the url-mapping gotcha for c, file_path="<HARNESS>/runs-clean/cells/wre6d78/home/.qwen/projects/-home-roman----------Q)`
  `write_file(content="# Project memory index\n\n- [CALM validation](reference/calm-validation.md) — npx @finos/calm-cli + url-mapping gotcha for controls\n", file_path="<HARNESS>/runs-clean/cells/wre6d78/home/.qwen/projects/-home-roman----------Q)`

All changes are as intended. Let me do a final review of the new files to make sure the README references match and there are no inconsistencies. I've already validated everything.

Let me quickly verify the new files are all present in the correct locations:
- docs/adr/ADR-008-...md ✓
- docs/recurring-c2b/solutioning.md ✓
- docs/recurring-c2b/spec/consent-state-machine.md ✓
- docs/calm/recurring-c2b-consent.architecture.json ✓
- docs/calm/controls/*.requirement.json (7 files) ✓
- docs/calm/url-mapping.json ✓

All good.

Now, let me consider whether I should save anything to memory. The task is complete. The memory instructions suggest saving durable cross-conversation knowledge. One genuinely durable, non-derivable fact: the repo's decision files are evolved by adding new ADRs (never editing old) and adding new spine ADs as Proposed; and the CALM CLI is available via `npx --no-install @finos/calm-cli` with the URL-mapping pattern for controls. But the "Do not save" list explicitly excludes "Code patterns, conventions, architecture, file paths, or project structure (read the project instead)" and "Debugging solutions or fix recipes". The CALM CLI usage is borderline a "confirmed durable workaround" (the URL-mapping for controls is a non-obvious gotcha). 

Actually, the URL-mapping requirement for CALM controls is a genuinely non-obvious, durable gotcha that could save time in future CALM work in this repo. That's a "confirmed durable workaround". I could save a small project `reference` or `feedback` memory. But it's about tooling specifics. The instructions say "save only confirmed durable workarounds, warnings, owner, or escalation path" for tool-related. This qualifies as a durable workaround: "CALM controls require resolvable requirement-url; use --url-to-local-file-mapping with local requirement schema files." 

Hmm, but I should be careful not to over-save. This is genuinely useful for future CALM modeling in this project. Let me save a concise project reference memory about the CALM validation setup in this repo (npx command + url-mapping pattern). Actually, the memory instructions also say "Before recommending a memory that names a file... verify it still exists" — I just created it, so it exists.

I'll save one concise project reference memory. Actually, let me reconsider: is this "durable cross-conversation knowledge" or "ephemeral task state"? The CALM CLI availability + the url-mapping gotcha is durable and non-obvious. I'll save a short project memory.

Let me write it to the PROJECT memory directory (project-scoped, since it's about this repo's tooling). Type: reference (pointer to how to validate CALM in this repo).

Actually, the memory type "reference" is for "pointers to where information lives in external systems (default project)". The CALM validation workflow is more of a "feedback"/workaround. Hmm. The four types: user, feedback, project, reference. 

- This is project-scoped tooling knowledge. "project" type = "ongoing work, goals, initiatives, bugs, or incidents not derivable from code/git". The CALM validation workflow IS derivable from code (the files I created: url-mapping.json, the skill instructions). Actually the skill already documents `--url-to-local-file-mapping`. So it's somewhat derivable. But the specific gotcha (control requirement-url must resolve, else validation fails) is a non-obvious gotcha.

I think a concise project `reference` memory is defensible: it points to the CALM validation command + mapping file in this repo. But given the "do not save" guidance leans toward not saving derivable things, and this is a one-off task, I'll make a judgment call: save a small, genuinely-useful project reference about how CALM validation is wired in this repo (the npx command and url-mapping), because the exact incantation (npx @finos/calm-cli validate -a ... -u ...) is non-obvious and I verified it works.

Let me save it concisely. Two-step: write the memory file + add pointer to MEMORY.md.

Actually, let me weigh this more. The user didn't ask me to remember anything. The memory system says "When you learn something worth remembering across conversations, save it." The CALM validation incantation IS worth remembering if the user will do more CALM work here. This is a reasonable proactive save. I'll do a minimal one.

Let me write the project memory.

Project memory dir: `<HARNESS>/runs-clean/cells/wre6d78/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-clean-cells-wre6d78-ws/memory`

I'll write `reference/calm-validation.md` and update MEMORY.md.

Actually, let me keep it lean and just do it. Content:

```markdown
---
name: CALM validation in this repo
description: How to validate FINOS CALM models in this repo (npx command + url-mapping for controls)
type: reference
---

CALM CLI is available via `npx --no-install @finos/calm-cli` (no global `calm` binary).

To validate an architecture model: `npx --no-install @finos/calm-cli validate -a <file>.architecture.json -f pretty`.

Gotcha: CALM `controls[].requirements[].requirement-url` must resolve to a local schema, else validation fails with "Direct URL loading is restricted to approved hosts". In this repo, requirement schemas live in `docs/calm/controls/*.requirement.json` and are wired via `docs/calm/url-mapping.json`; pass `-u docs/calm/url-mapping.json`.
```

And MEMORY.md pointer: `- [CALM validation](reference/calm-validation.md) — npx @finos/calm-cli + url-mapping for controls`.

This is concise and useful. Let me do it.

Actually, wait — I should double-check the MEMORY.md location and whether there's an existing MEMORY.md (the system said it's empty). I'll write the memory file and the MEMORY.md index.

The memory directories: USER memory dir and PROJECT memory dir. For a project-scoped tooling reference, use PROJECT memory dir.

Let me write.

Actually, let me reconsider whether to spend time on this. The primary deliverable is done. The memory is a nice-to-have. I'll do it quickly and correctly since it's genuinely useful and low-cost.

Let me write both files.
Все проверки прошли. Сохраню полезный для будущей работы факт о способе валидации CALM в этом репозитории (неочевидная деталь: `requirement-url` контролей обязан резолвиться локально).


Everything is done. Let me write the final summary to the user, in Russian (matching the user's language), concise but covering the 7 deliverables and the CALM model, plus the list of created/changed files.

Let me summarize the deliverables and where each lives, plus verification results.

Final answer structure:
- Brief statement of what was done.
- Map the 7 deliverables to files.
- CALM model + validation result.
- List of created and changed files.

Keep it concise but complete. The user asked "Когда закончишь, кратко перечисли созданные и изменённые файлы."

Let me write the final response.
Готово. Архитектурный пакет изменения «рекуррентные C2B-списания по согласию плательщика (подписки СБП)» подготовлен поверх принятого решения и провалидирован.

## Соответствие семи пунктам

1. **Значимость и маршрут** → `docs/recurring-c2b/solutioning.md` §1. Значимость **High** (в рамках Critical-системы 11/15): новый юридически значимый объект (согласие), финансовые риски, новый внешний pull-поток, пиковый профиль «день списания». Глубокое проектирование ядра изменения, но **без** перепроектирования топологии/trust-зон/транспорта/гибрида.
2. **Влияние на принятую архитектуру** → §2 + `ARCHITECTURE-SPINE.md`. Потабличный разбор AD-001…AD-008: что расширяется (AD-002, AD-003, AD-004, AD-007), что уточняется без изменения (AD-005), что не меняется (AD-001, AD-006, AD-008). Добавлен инвариант **AD-009** (Proposed).
3. **Архитектурное решение** → `docs/adr/ADR-008-…md` (альтернативы, последствия, обратимость).
4. **Изменения контрактов без поломки** → `openapi/tsp-api.yaml` (v0.1.0→0.2.0, только новые пути `/v1/consents*` и опциональные поля `paymentType`/`consentId`), `docs/contracts/tsp-api.md` §8, `docs/contracts/opkc-adapter.md` §10.
5. **Измеримые NFR** → §5 (латентность, 0 превышений лимита, 0 двойных списаний, отзыв за p95<5 с, пик «день списания», сверка).
6. **Приёмка и откат** → §6 (позитивные/негативные критерии, фиче-флаг `recurring.enabled`, stop-new без остановки разовых QR).
7. **Решения человека** → §7 (8 пунктов: модель согласия по НСПК, семантика лимитов, каналы отзыва, in-flight при отзыве, юридическая форма/ПДн, AML-пороги, UX, изменение лимита).

## CALM-модель

`docs/calm/recurring-c2b-consent.architecture.json` — 14 узлов, 19 связей, 2 потока (создание/подписание согласия; рекуррентный дебит), 6 контролей + 2 flow-контроля. **Провалидирована родным валидатором чисто:**

```
Summary — Errors: no (0) · Warnings: no (0)
No issues found.
```

## Созданные файлы
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`
- `docs/recurring-c2b/solutioning.md`
- `docs/recurring-c2b/spec/consent-state-machine.md`
- `docs/calm/recurring-c2b-consent.architecture.json`
- `docs/calm/url-mapping.json`
- `docs/calm/controls/*.requirement.json` (7 схем)

## Изменённые файлы (принятым в репозитории способом — аддитивно, без правки старых ADR/инвариантов)
- `ARCHITECTURE-SPINE.md` — добавлен AD-009 (Proposed), версия контракта 0.2
- `openapi/tsp-api.yaml` — новые пути/схемы (обратно совместимо)
- `docs/contracts/tsp-api.md` — §8 + коды ошибок + вебхуки `consent.*`
- `docs/contracts/opkc-adapter.md` — §10 (операции/события согласия, требования к вендору)
- `README.md` — структура актуализирована

Проверки: CALM-валидация — 0 ошибок; OpenAPI YAML распарсен корректно (5 путей, 4 схемы).
