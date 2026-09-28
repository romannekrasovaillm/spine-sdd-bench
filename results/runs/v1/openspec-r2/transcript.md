<!-- источник: <HARNESS>/runs/cells/openspec-r2/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-cells-openspec-r2-ws/chats/86c4bba4-bbcf-431f-9534-49341cd23103.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `glob(pattern="**/*")`

Let me start by understanding the repository and the task. This is an OpenSpec project with methodological skills available (openspec-* skills). The user is a solution architect and wants me to prepare an architectural package for a new change (recurring C2B debits / SBП subscriptions) on top of the accepted solution.

Key instruction: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — Change accepted solution files only in the way accepted in this repository. And "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." — Use methodological skills/tools as intended.

So I need to explore the repository first, understand the OpenSpec structure, the accepted solution files, and then use the OpenSpec propose/explore workflow to prepare the architectural package.

Let me start by reading the key files and understanding the structure. This is clearly an OpenSpec project. The task is to propose a change. The openspec-propose skill is relevant.

Let me first explore the repository thoroughly. I should read:
- ARCHITECTURE-SPINE.md (invariants AD-001..AD-008)
- docs/ (solutioning, NFR, ADR-001..007, contracts, state machine)
- openapi/tsp-api.yaml
- .arch-handoff/
- openspec/ structure

Let me do a broad exploration first. I should be careful and thorough. Let me read files in parallel.

Let me start with glob and reading key files.
Начну с изучения структуры репозитория и принятого решения, чтобы понять методику и формат, принятые в этом проекте.

  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/openspec/config.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/.qwen/skills/openspec-propose/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/.qwen/commands/opsx-propose.md")`

Let me read the key files. I'll start with the ARCHITECTURE-SPINE.md, README.md, and the openspec skills/commands to understand methodology. Also the openspec config.yaml.

Let me read in parallel a bunch of files.

  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/openapi/tsp-api.yaml")`

This is an OpenSpec project. The task is to propose a change. The `openspec-propose` skill is the right methodological tool. However, I need to first understand the accepted solution deeply, then formulate the change.

Important nuance: The user asks for a full architectural package that:
1. Оценка значимости изменения и маршрута (significance assessment and route)
2. Влияние на принятую архитектуру (impact on accepted architecture)
3. Архитектурное решение с альтернативами (ADR with alternatives)
4. Изменения контрактов without breaking consumers
5. Измеримые NFR
6. Критерии приёмки и план отката
7. Что остаётся на решение человека-архитектора

The OpenSpec propose workflow creates: proposal.md, specs/<capability>/spec.md, design.md, tasks.md. But the user also wants things like NFR, acceptance criteria, rollback plan, ADR with alternatives. These could be embedded in the design.md and proposal.md, or I might also need to create additional docs.

Wait — "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — Change accepted solution files only in the way accepted in this repository. This means I should NOT directly edit ARCHITECTURE-SPINE.md, docs/adr/ADR-*.md, docs/nfr.md, openapi/tsp-api.yaml directly. Instead, I should use OpenSpec change workflow (delta specs), and perhaps add a new ADR in docs/adr/ following the existing ADR format.

Actually, let me think about this carefully. The OpenSpec methodology: changes live in openspec/changes/<name>/ with proposal.md, specs/<capability>/spec.md (delta), design.md, tasks.md. The accepted specs live in openspec/specs/ (currently just .gitkeep — empty). The accepted solution is documented in ARCHITECTURE-SPINE.md and docs/ — these are NOT OpenSpec specs, they're markdown docs.

So the repo has two parallel documentation systems:
1. The "accepted solution" docs: ARCHITECTURE-SPINE.md, docs/adr/ADR-*.md, docs/nfr.md, docs/contracts/*.md, openapi/tsp-api.yaml
2. The OpenSpec change management: openspec/ (specs, changes)

The user says "Подготовь архитектурный пакет этого изменения поверх принятого решения" — prepare an architectural package of this change on top of the accepted solution. And "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — change the accepted solution files only via the accepted method in this repo.

The accepted method in this repo for introducing changes is the OpenSpec change workflow (propose → apply → archive → sync). The openspec config has `schema: spec-driven`. So the right approach is:

1. Use OpenSpec to create a change (propose workflow) with proposal.md, specs/<capability>/spec.md (delta), design.md, tasks.md.

2. For the "architectural package" the user wants, the ADR and NFR and contract changes — these need to be reflected. The design.md in OpenSpec can hold the ADR with alternatives. The delta spec captures the requirement changes. The contract changes (openapi/tsp-api.yaml) — the spec delta should describe them; actually changing openapi/tsp-api.yaml is implementation, but the user explicitly wants "Изменения контрактов (openapi/tsp-api.yaml) без поломки существующих потребителей" as part of the package.

Wait, but this is "planning only" — no code. openapi/tsp-api.yaml is a contract, not code. The user explicitly asks for contract changes as a deliverable. But the OpenSpec propose workflow says "Do not edit project code." A contract YAML is not code per se, but it's a source-of-truth artifact of the accepted solution.

Hmm. Let me re-read the user's request carefully.

The user wants 7 deliverables. These map to an architectural proposal. The question is HOW to structure this in the repo. The repo has:
- ARCHITECTURE-SPINE.md (invariants)
- docs/ (solutioning, nfr, adr, contracts, spec/state-machine, rfp)
- openapi/tsp-api.yaml
- .arch-handoff/
- openspec/ (the change management system)

The "accepted method" for changes is OpenSpec. The `.arch-handoff/` is a handoff package to a code harness (walking skeleton stage). The docs/ holds the accepted solution docs.

Let me read the rest of the key docs to understand deeply. I need to read:
- docs/solutioning.md
- docs/nfr.md
- docs/contracts/tsp-api.md
- docs/contracts/opkc-adapter.md
- docs/spec/state-machine.md
- docs/rfp/vendor-rfp.md
- docs/adr/ADR-001..007 (at least key ones)
- openapi/tsp-api.yaml
- .arch-handoff/ (TASK.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, ARCHITECTURE.md)

Let me also read the remaining openspec skills/commands to understand apply/archive/sync.

Let me read these in parallel batches.

  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/adr/ADR-002-model-konsistentnosti-pl)`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/adr/ADR-005-integraciya-s-abs-zachis)`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/contracts/opkc-adapter.md")`

Now let me read the remaining ADRs, contracts, and the .arch-handoff package to fully understand the methodology and format. Also the opkc-adapter contract, vendor-rfp, and the remaining openspec skills (explore, apply, archive, sync, update) briefly. And the .arch-handoff files (TASK.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, ARCHITECTURE.md).

Let me batch-read these.

  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/.arch-handoff/ARCHITECTURE.md")`

I have a good understanding now. Let me read the remaining files: .arch-handoff (TASK.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, ARCHITECTURE.md), and the remaining ADRs (001, 003, 006) briefly, plus the vendor-rfp.md. Also the openspec skills for explore/apply/archive/sync/update to understand the workflow and how the ADR files relate.

Actually, I have enough understanding of the OpenSpec propose workflow. But I should also read the .arch-handoff files since they define how accepted solution files should be changed (the "правила и пакет передачи"). And the remaining skills to understand how to properly author the change (especially what artifacts to create and how specs deltas work).

Let me read .arch-handoff files and remaining skills and remaining ADRs.

  `run_shell_command(command="openspec --version 2>&1; echo \"---context---\"; openspec context --json 2>&1", description="Проверить наличие OpenSpec CLI и корень проекта")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/adr/ADR-001-outbox.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/docs/rfp/vendor-rfp.md")`

I now have a very solid understanding. Let me read the remaining ADRs (001, 003, 006) briefly and the openspec skills for explore/apply/archive/sync/update, and the vendor-rfp.md. Actually, I have enough for the architecture. But I need to understand how the openspec change workflow handles the delta specs and how ADRs in docs/ relate to OpenSpec specs.

Key observation: The repo uses OpenSpec as its change management methodology, but the "accepted solution" is documented in `docs/` and `ARCHITECTURE-SPINE.md`, NOT in `openspec/specs/` (which is empty except .gitkeep). So the "accepted method" for changing the accepted solution is the OpenSpec change workflow — propose a change, which produces `openspec/changes/<name>/` with proposal.md, specs/<capability>/spec.md (delta), design.md, tasks.md. Then apply → archive → sync to move deltas into main specs.

But wait — the accepted solution files (ARCHITECTURE-SPINE.md, docs/adr/ADR-*.md, docs/nfr.md, openapi/tsp-api.yaml) are NOT OpenSpec specs. They're markdown docs. So the OpenSpec workflow's "sync specs" writes to openspec/specs/, not to docs/.

The user says: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." This means I should not directly edit ARCHITECTURE-SPINE.md, docs/adr/*.md, docs/nfr.md, openapi/tsp-api.yaml as if they were freely editable. The accepted way to introduce changes is via the OpenSpec change proposal workflow.

So my plan:
1. Use the `openspec-propose` skill workflow to create a change (e.g., `recurring-c2b-debits` / `sbp-subscriptions`).
2. The change artifacts will be:
   - proposal.md (what & why) — includes significance assessment, impact on accepted architecture (which invariants affected), open decisions for human architect
   - specs/<capability>/spec.md (delta) — new requirement: recurring debits / subscriptions, with ADDED/MODIFIED requirements
   - design.md (how) — the architectural decision with alternatives, consequences, reversibility, contract changes, NFR, acceptance criteria, rollback plan
   - tasks.md (implementation steps)
3. Also potentially need to add a new ADR (ADR-008) in docs/adr/? But wait — the OpenSpec workflow is the accepted method. Adding a new ADR directly to docs/adr/ would be editing the accepted solution docs. Hmm.

Actually, let me reconsider. The user wants a "архитектурный пакет" (architectural package) that can be "вынести на архитектурное решение" (brought to architecture decision) and then "передать исполнителям" (hand off to implementers). This maps exactly to the OpenSpec change proposal: it's a planning package that is reviewed, then handed to apply.

The 7 deliverables map to:
1. Оценка значимости и маршрута → proposal.md + design.md (route: Critical/Major, how deep)
2. Влияние на принятую архитектуру → proposal.md / design.md (which AD invariants affected)
3. Архитектурное решение с альтернативами → design.md (ADR-style, or a new ADR file)
4. Изменения контрактов → design.md describes; the delta spec captures new endpoints/fields
5. NFR → design.md or a spec section
6. Критерии приёмки и план отката → design.md / tasks.md
7. Открытые вопросы для человека-архитектора → proposal.md / design.md "Open Questions" section

The cleanest approach: use the OpenSpec change workflow. The design.md holds the ADR (with alternatives/consequences/reversibility), contract changes, NFR, acceptance criteria, rollback plan, and open questions. The spec.md (delta) holds the formal requirements. proposal.md holds the significance + impact assessment.

Now, regarding the contract change (openapi/tsp-api.yaml): The user explicitly lists "Изменения контрактов (openapi/tsp-api.yaml) без поломки существующих потребителей" as deliverable #4. This is about showing HOW the contract would change. In the OpenSpec propose workflow, we're in planning-only mode — no code, no editing project artifacts. But openapi/tsp-api.yaml is a contract, not code. Should I actually edit it?

The instruction "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — change accepted files only via accepted method. The accepted method is OpenSpec change workflow (propose). The propose workflow produces delta specs that describe changes but do NOT modify the main files until apply/archive/sync. So I should NOT directly edit openapi/tsp-api.yaml. Instead, I describe the contract changes in the spec delta and design.md (e.g., as a proposed new version of the contract or additive fields).

Actually, let me reconsider once more. There's tension between:
- The user explicitly wants a full architectural package (7 deliverables), including actual contract change details.
- The OpenSpec propose workflow (planning boundary): "Do not edit project code." A contract YAML is not code, but it's a project artifact.

I think the right approach, faithful to the repo's methodology, is:
1. Run the OpenSpec propose workflow to create the change with proposal.md, specs/<capability>/spec.md, design.md, tasks.md.
2. In design.md, include a full ADR section (alternatives, consequences, reversibility), the contract delta (with actual proposed OpenAPI fragments as examples), NFR table, acceptance criteria, rollback plan, and open questions.
3. NOT directly edit openapi/tsp-api.yaml, docs/nfr.md, ARCHITECTURE-SPINE.md, or docs/adr/*.md — because those are "accepted solution files" that change only via the OpenSpec apply/archive/sync flow (or via a new ADR in a subsequent step, which is itself a decision for the human architect).

Wait, but actually — is there a risk I'm overcomplicating? Let me reconsider what "the accepted way to change accepted solution files in this repo" is. 

Looking at the repo: the accepted solution files are docs/ (ADR-001..007, nfr, contracts, spec/state-machine) and ARCHITECTURE-SPINE.md. There's a `.arch-handoff/` package which is the handoff to a code harness. And there's `openspec/` which is the change management.

The README says: "Статус: решение подготовлено, ожидает человеческого решения A3 по стратегии реализации (ADR-007) и получения документации НСПК."

The OpenSpec config says `schema: spec-driven`. The openspec/specs/ is empty (only .gitkeep). This suggests the OpenSpec system is set up but the accepted solution hasn't been "spec'd" into openspec/specs yet — it lives in docs/ as ADRs.

So the methodology for a NEW change (recurring debits) is: propose a change via OpenSpec. This is the "accepted method" for introducing changes. The change artifacts are the "architectural package" the user wants.

I'm now confident. Let me use the openspec-propose skill. The skill is invoked via the Skill tool with skill name "openspec-propose". But actually, the skill is also available as a command. The system reminder says to invoke the skill via the Skill tool. But the skill instructions describe running `openspec` CLI commands.

Wait, let me check: do I have the `openspec` CLI available? The skill says "compatibility: Requires openspec CLI." and allowed-tools: Bash(openspec:*). Let me check if openspec CLI is available and if the project has a root.

Actually, the important thing: I should invoke the openspec-propose skill to load its guidance (it's already shown in the command file). The skill tool will load the SKILL.md. But I already read the SKILL.md and the command file. 

Hmm, but the guidance says "When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action". Let me think about whether I should invoke the skill tool. The skill is clearly relevant — this is an OpenSpec propose task. But I've already read the SKILL.md content directly via read_file.

Actually, the proper flow per the skill: I should invoke the skill (openspec-propose) which would give me the workflow, then run openspec CLI commands. But I've read the skill content already. The skill tool invocation would just re-present the same content.

Let me reconsider. The key question is whether the `openspec` CLI is actually available on this machine. Let me check. The skill says it requires the CLI. Let me run `openspec --version` or `openspec list --json` / `openspec context --json`.

Actually, I realize I should follow the workflow properly. Let me:
1. First check openspec CLI availability and project root via `openspec context --json` or `openspec list --json`.

But wait — there's also a subtlety. The user's task is broader than just "propose a change". The user wants a full architectural package with 7 specific deliverables, some of which (NFR, acceptance criteria, rollback plan, ADR with alternatives, contract changes) are richer than a minimal OpenSpec proposal. 

I think the right move is:
1. Use the OpenSpec propose workflow to scaffold the change (proposal.md, spec.md, design.md, tasks.md).
2. Enrich design.md with the ADR (alternatives/consequences/reversibility), contract delta, NFR table, acceptance criteria, rollback plan, open questions. The design.md template supports this.
3. proposal.md gets significance assessment + impact on architecture.
4. spec.md (delta) gets the formal requirement changes (ADDED/MODIFIED requirements with SHALL/MUST).

Also, I should note that there's a question of whether to ALSO create a new ADR-008 in docs/adr/ as part of the package. Given "Принятые файлы решения меняй только тем способом, который принят в этом репозитории", and the accepted method is OpenSpec changes, I should NOT create docs/adr/ADR-008 directly. Instead, the ADR content lives in the design.md of the change, and when the change is later applied/archived, the ADR would be formalized. OR, I flag it as an open question for the human architect ("should this become ADR-008").

Actually, let me reconsider the whole thing more holistically. The user is a solution architect and wants to prepare an architectural package to bring to an architecture decision. The OpenSpec "propose" workflow is exactly the mechanism this repo uses for that. The change will be "recurring C2B debits / СБП subscriptions".

Let me now think about the actual architectural content, since that's the substance.

## Domain understanding: Recurring C2B debits (subscriptions) in СБП

Current state: C2B payments require QR + client action each time. The business wants recurring debits by payer consent (subscriptions) — e.g., online cinemas, ЖКХ (housing utilities), telecom.

In СБП (Russian FPS), the C2B model supports "подписки" via recurring debits. The payer gives consent (согласие) to the ТСП/bank to debit a fixed or variable amount on a schedule. This is like SEPA Direct Debit or card recurring payments. The key СБП concept here: "Платёж по подписке" / "рекуррентный платёж" / "Согласие на списание" (acceptance of standing order).

Actually, in СБП the relevant mechanism is: НСПК СБП introduced "регулярные переводы" / "подписки" (C2B pull) where the payer pre-authorizes recurring debits. The technical flow involves:
- Payer gives consent (via their bank's app, or via the merchant's subscription setup).
- The consent is registered, possibly with НСПК (a "согласие" / mandate).
- The ТСП (or bank) initiates a debit request without the payer's action each period, referencing the consent.
- The payer's bank debits the account and confirms.

This is the "C2B pull" or "подписочный платёж" model. Key НСПК terms: "Платеж по согласию" / "инициирование списания получателем" (creditor-initiated). There might be a specific СБП scenario "подписка" (subscription) that НСПК released.

For our architecture, the key architectural changes are:
1. New domain entity: **Согласие (consent/mandate)** — payer's recurring consent, stored and managed. This is a NEW source of truth beyond the payment state machine.
2. New status machine for consent: ACTIVE → (debits) → SUSPENDED/REVOKED/EXPIRED.
3. New contract endpoints: create consent, manage consent, initiate recurring debit (trigger), list debits. Plus webhooks for consent events and debit results.
4. The recurring debit becomes a new payment flow that reuses the existing payment state machine (CREATED→...→COMPLETED) but triggered by a scheduler rather than QR. Actually, does recurring debit use QR? In СБП, a subscription debit might NOT use QR — it's a direct debit initiated by the merchant. So the "qrType" dimension changes: recurring debit is a new "payment method" that bypasses QR.

This is a significant architectural impact. Let me map to the invariants AD-001..AD-008:

- AD-001 (изоляция платёжного контура): NOT changed — recurring debits still go through the gateway adapters. New consent store lives in the gateway. Binds extend to include consent storage.
- AD-002 (единый источник истины — статусная машина платежа): EXTENDED — need a new status machine for consent, and the payment status machine may need a new state or a new "debit" entity. The rule "изменение финансового статуса + outbox в одной транзакции" extends to consent transitions.
- AD-003 (идемпотентность): EXTENDED — consent operations need idempotency keys too (consentId, debitId, mandate reference).
- AD-004 (единственный адаптер ОПКЦ): NOT changed — adapter gets new operations (register consent, initiate recurring debit), but still the single adapter.
- AD-005 (зачисление только из PAID): EXTENDED/REVISED — for recurring debits, the "PAID" trigger is the confirmation of the recurring debit. Need to be careful: the consent itself is NOT a payment; the debit triggered is. Зачисление still from confirmed status.
- AD-006 (trust-зоны): NOT changed materially, but consent data is ПДн and financial — same trust zones apply. Consent is sensitive personal data.
- AD-007 (соответствие): EXTENDED — consent is a new auditable object; revocations must be audited; 115-ФЗ/152-ФЗ consent rules.
- AD-008 (стратегия гибрид): NOT changed — vendor adapter must support НСПК subscription/subscription-consent operations; new RFP requirement.

So the impact: the change is significant (Major, likely 8-9/15), requires new ADRs (consent model + recurring debit orchestration), touches AD-002/AD-003/AD-005 (extends invariants, doesn't break), adds new binds. No invariant is BROKEN, but several are EXTENDED and a new invariant may be needed (AD-009: consent as separate source of truth with its own lifecycle; debit-initiation authorization).

Key architectural decisions to consider (alternatives):
1. **Where does the consent live and who is the source of truth?** Options: (a) consent in gateway (own store), (b) consent in НСПК as source of truth with gateway as cache, (c) consent in АБС. → Likely: gateway is the source of truth for consent lifecycle (consistent with AD-002), НСПК holds the operational consent (like QR registration), АБС is only told about debits.
2. **Debit triggering model**: (a) gateway-local scheduler (cron) triggers debits by consent schedule, (b) НСПК triggers (recurring mandate at НСПК level), (c) ТСП triggers each debit via API. → Likely hybrid: ТСП can trigger ad-hoc, and/or gateway scheduler for schedules; НСПК subscription mandate where available. Need human decision on who owns schedule (ТСП vs bank vs НСПК).
3. **Payment model for recurring debit**: reuse existing payment state machine (QR-less "debit" type) vs new "debit" entity. → Reuse payment machine with new type, add debit-specific states or reuse.
4. **Consent capture UX**: payer consent must be captured. Options: via payer's bank app (НСПК flow), via merchant redirect to bank consent page, via gateway consent API + payer auth. → This is the critical regulatory/UX decision, likely external (НСПК protocol defines consent flow).
5. **Variable vs fixed amount**: ЖКХ often variable. Consent must support amount limits (max amount, frequency, expiry) and payer revoke rights (regulatory).

Contract changes (backward compatible, additive):
- New endpoints under /v1 (additive, no break):
  - `POST /v1/consents` — create consent (with Idempotency-Key)
  - `GET /v1/consents/{consentId}` — status
  - `POST /v1/consents/{consentId}/revoke` or `DELETE` — revoke (payer or ТСП initiated)
  - `GET /v1/consents/{consentId}/debits` — list debits
  - `POST /v1/consents/{consentId}/debits` — trigger a recurring debit (or separate `POST /v1/debits`)
- New webhook events: `consent.revoked`, `consent.expired`, `debit.completed`, `debit.failed` (or reuse payment.* events with a `paymentType`/`method` field).
- Extend `Payment` schema with `paymentType: enum [one_time, recurring]`, `consentId?`, `mandateRef?`.
- Extend `PaymentRequest` with `consentId?` and `paymentType?` — optional fields (backward compatible).

NFR for recurring:
- Consent registration p95 < 500ms
- Scheduled debit processing throughput, on-time debit trigger (e.g., 99.9% of scheduled debits initiated within ±5 min of schedule)
- No double debit (idempotency by consentId + period/scheduleKey)
- Consent revoke propagation ≤ X seconds to stop debits
- Availability same as gateway; RPO=0 for consents too.

Acceptance criteria + rollback plan:
- Feature flag to disable recurring (stop new consents + stop new debits) while existing one-time flows unaffected.
- Rollback: since additive, rollback = disable feature flag; no data migration backwards; consents remain but no new debits.

Open questions for human architect:
- Who owns the debit schedule (ТСП vs bank vs НСПК)? — regulatory & НСПК protocol dependent.
- Fixed vs variable amount support (ЖКХ variable) — needs НСПК subscription variant confirmation.
- Payer consent capture UX flow — depends on НСПК protocol (external input [ТРЕБУЕТ ПРОВЕРКИ]).
- Payer's right to revoke — must be surfaced in payer's bank and/or gateway; confirm regulatory minimums.
- Whether recurring is a new AD (AD-009) or fits existing ADs.
- Whether to add ADR-008 (or 009) for consent model.

OK. Now, the mechanics. Let me check if the openspec CLI is available and whether the project has a valid root.

Let me run the openspec context command. Actually, let me first check if openspec is even installed.

Let me also read the remaining skills (explore, apply, archive, sync, update) briefly to understand the artifact structure and any additional guidance. Actually, I mainly need propose. But let me also check the openspec skill for "explore" since the user's task includes "Оценка значимости изменения и маршрута" — which is exploration + significance.

Actually, let me be efficient. Let me:
1. Check openspec CLI availability and root.
2. Read remaining ADRs (001, 003, 006) and vendor-rfp.md and remaining skills quickly.

Let me run the CLI check first, and read remaining files in parallel.

Actually, I can't run openspec and read files in the same message cleanly if I need openspec results first. Let me do a first batch: check openspec CLI + read remaining ADRs + skills.

  `run_shell_command(command="openspec new change \"recurring-c2b-debits\" 2>&1; echo \"---status---\"; openspec status --change \"recurring-c2b-debits\" --json 2>&1", description="Создать change и получить порядок артефактов")`

I now have a comprehensive understanding. The OpenSpec CLI is available (v1.13.2), and the project root is at `<HOME>/.../ws`.

Now let me look at the remaining skills briefly to understand the artifact structure for the propose workflow. Actually, I already read the full propose SKILL.md. I need to understand:
- The spec-driven schema artifacts: proposal.md, specs/<capability>/spec.md, design.md, tasks.md.
- How `openspec instructions` works to get the templates.

Let me check the other skills (apply, archive, sync, explore, update) briefly — actually the propose workflow is what I need. But I want to understand how the change artifacts get structured and what `openspec new change` scaffolds.

Let me also read the remaining ADR files? I've read ADR-001, 002, 003, 004, 005, 006, 007. That's all 7. Good.

Now, let me think about the actual flow I'll follow. I need to invoke the `openspec-propose` skill via the Skill tool (since the instructions say "When a skill is relevant, you must invoke this tool IMMEDIATELY"). But I've already read the skill content. Actually, I think the right thing is to proceed with the workflow manually following the SKILL.md, since I've read it. But the system reminder strongly says to invoke the skill. However, invoking the skill just loads the same content I've already read.

Hmm. Let me reconsider. The instruction: "When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action". I already did substantial exploration. The skill is `openspec-propose`. But actually there's a subtlety: the user's request is NOT literally "openspec propose" — it's a broader architectural task. But the repo's methodology is OpenSpec, and the user said "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению."

I think the cleanest, most faithful approach is:
1. Invoke the `openspec-propose` skill (to formally load the workflow and demonstrate I'm using the methodology).
2. Follow it: run `openspec new change`, `openspec status`, `openspec instructions`, etc.

But wait — the propose skill creates a change with proposal.md, specs/<capability>/spec.md, design.md, tasks.md. This is the "architectural package". However, the user's 7 deliverables include things like NFR, acceptance criteria, rollback plan, contract changes, ADR with alternatives. These map to design.md (which is "how" — the design doc holds ADR/alternatives/NFR/rollback) and proposal.md (significance/impact).

Actually, let me reconsider whether the "change" name should be `recurring-c2b-debits` or `sbp-subscriptions` or `recurring-payments`. Let me use `recurring-c2b-debits` (kebab-case, clear).

Let me also consider: should I use the `openspec-explore` skill first? The user's deliverable #1 is "Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему)". This is exploration. But I've already explored. The explore skill is for thinking through ideas. Given I've done deep exploration, I can proceed to propose.

Actually, there's a decision to make about the route/significance. The existing repo uses a "Critical" route with significance 11/15. For recurring debits, I need to assess significance. Let me think about the BMAD/Superpowers methodology hints: "маршрут" (route), "значимость" (significance) 11/15 scale, gates A0-A5. This suggests a specific methodology (BMAD = maybe "Банковская методология архитектурных документов"? or "Business Model Architecture Design"?). The `.arch-handoff` references "BMAD epic-context + headless-контракт, docs/SOURCE_BRIEF.md §A.3". 

There's a methodology of "solutioning" with routes (Critical/Major/Minor), significance scores, gates A0-A5. The recurring debits change should be classified on this same scale.

Let me assess: recurring C2B debits is a NEW payment method with NEW consent domain, NEW states, NEW contract endpoints, NEW webhooks, touches multiple invariants, regulatory/ПДн impact, financial impact (double debit). It's significant but reuses the existing gateway. It's probably "Major" (значимость ~8/15), not full "Critical" (11/15) because the core gateway and transport are already being built. Actually it could be argued Critical because it's financial + ПДн + new consent lifecycle. But the platform is already in design. Let me classify as Major with deep design (it needs its own ADR(s) + contract + NFR), not full re-solutioning.

Actually, let me not overthink the exact numeric score. The methodology uses significance 11/15 for the parent initiative. For this feature, I'll estimate significance ~8/15, route Major, requiring: ADR(s) (consent model + recurring orchestration), delta spec, contract delta, NFR, but NOT re-opening AD-001..AD-007.

Now, let me plan the actual work:

**Step 1**: Invoke openspec-propose skill (formal).
Actually, since I've already read the SKILL.md and command, and the skill tool would just reload it, but the guidance is strong. Let me invoke it to be safe and faithful. Actually, re-reading: "Invoke with `/opsx-propose`". The skill tool invocation with `skill: "openspec-propose"` loads the SKILL.md. I've read it. 

I think there's genuine value in NOT double-loading. But the instructions are explicit about invoking skills immediately. However, I've already done the exploration (which is part of the workflow). The skill would tell me to run `openspec new change` etc.

Let me just proceed to run the openspec CLI workflow directly, since I've already internalized the SKILL.md. Actually, I'll invoke the skill tool to be compliant, then proceed. Hmm, but that's somewhat wasteful. 

Let me weigh: The "Core Mandates" and skill instructions say invoke the skill. But I already read its content via read_file. The skill tool invocation would add the SKILL.md content to context again. That's minor. 

I'll proceed with the workflow directly, because I've already read the authoritative SKILL.md content. I'll run `openspec new change` to scaffold.

Actually, wait — I should double check: is there a risk that `openspec new change` creates files I shouldn't create, or does something wrong? The SKILL says to run it. It creates `openspec/changes/<name>/` scaffold. This is the accepted method. Good.

Let me also decide: do I need to ask the user clarifying questions first? The SKILL says "If the request contains ambiguity that would materially affect scope... ask the user before creating the change."

Key ambiguities for recurring debits:
1. Who owns the debit schedule (ТСП vs bank vs НСПК)?
2. Fixed vs variable amount (ЖКХ)?
3. Consent capture UX (payer's bank app vs merchant)?

These are genuinely material and also tied to external НСПК protocol (which is [ТРЕБУЕТ ПРОВЕРКИ]). But the user explicitly asked me to prepare the package including "Что остаётся на решение человека-архитектора и почему" — meaning they WANT me to enumerate open questions, not necessarily resolve them all. So I can make reasonable assumptions (record them) and list the open questions as deliverable #7.

However, there's one thing that IS material and might benefit from a quick clarification: whether the user wants me to actually modify `openapi/tsp-api.yaml` or just describe the changes. But the instruction "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" strongly implies: don't directly edit accepted files; use the OpenSpec change method (delta). So I'll describe contract changes in the spec delta + design.md, and NOT edit openapi/tsp-api.yaml directly. I'll note this explicitly.

Actually, let me reconsider. There's nuance. The user says "4. Изменения контрактов (openapi/tsp-api.yaml) без поломки существующих потребителей." This is a deliverable — they want to SEE the contract changes. In OpenSpec spec-driven, the delta spec.md captures this as ADDED/MODIFIED requirements. But to be concrete and useful, I could also include in design.md an actual proposed OpenAPI fragment (new endpoints/schemas) as an illustrative delta, clearly marked as "proposal, to be applied to tsp-api.yaml at apply time."

I think the best approach:
- The OpenSpec change (proposal.md, specs/, design.md, tasks.md) is the architectural package.
- design.md contains: ADR (alternatives/consequences/reversibility), contract delta (with concrete OpenAPI fragments), NFR table, acceptance criteria, rollback plan.
- proposal.md contains: significance assessment, route, impact on AD-001..AD-008, open questions for human architect.

This satisfies all 7 deliverables within the accepted methodology.

Now, about whether I should ALSO create a docs/adr/ADR-008 file: The accepted method for a NEW ADR in this repo... Looking at the repo, ADRs live in docs/adr/. But the change workflow (OpenSpec) is separate. The user said change accepted files only via accepted method. The accepted method to introduce a new ADR would be... hmm. Actually, there's no explicit "accepted method" for adding ADRs beyond writing them in docs/adr/. But the OpenSpec change workflow IS the change management.

I think the cleanest is: the new ADR(s) content lives in the change's design.md (as the ADR decision with alternatives). When the change is applied and later archived, the ADR can be promoted to docs/adr/ADR-008. For now, I'll flag "create docs/adr/ADR-008-<consent-model>.md upon ratification" as a task in tasks.md, and note it as a decision point. I will NOT create docs/adr/ADR-008 directly because the change isn't ratified yet (it's "Proposed", awaiting human architecture decision — consistent with how ADR-001..006 are "Proposed" and ADR-007 became "Accepted" after A3).

Actually, this is a really important nuance about the repo's discipline: ADRs in docs/adr/ are the "accepted solution". ADR-001..006 are "Proposed", ADR-007 is "Accepted". A new change should first go through OpenSpec propose (planning), get human review (architecture decision), and THEN the ADR gets added/ratified. So the ADR content lives in design.md now.

Let me finalize my plan and proceed. I'll:

1. Run `openspec new change "recurring-c2b-debits"`.
2. Run `openspec status --change "recurring-c2b-debits" --json`.
3. For each artifact, run `openspec instructions <artifact-id> --change "recurring-c2b-debits" --json`, read template, write artifact.
4. Final `openspec status`.

Let me start. First invoke the skill? I'll proceed with the CLI workflow. Actually, let me be a good citizen and invoke the skill tool first since it's the project's methodological entry point and the system reminder is explicit. It's cheap.

Hmm, but actually the skill tool will return the SKILL.md content (same as what I read). It's redundant but harmless. Actually, I'll skip re-invoking since I've already read the exact SKILL.md and command file, and I understand the workflow. The important thing is to execute correctly. I'll proceed to `openspec new change`.

Wait, one more consideration. Let me verify there are no existing changes with a similar name. The openspec/changes/ only has archive/.gitkeep. So no existing changes. Good.

Let me create the change. Name: `recurring-c2b-debits`. Actually, thinking about naming for the domain: the business term is "рекуррентные C2B-списания по согласию плательщика — подписки СБП". A good kebab-case name: `recurring-c2b-debits` or `sbp-subscriptions`. I'll go with `recurring-c2b-debits` (describes the mechanism) — but "sbp-subscriptions" is more product-oriented. The existing naming uses Russian transliterated kebab-case for ADRs (e.g. "model-konsistentnosti-platezha..."). But the change name convention in OpenSpec is usually English kebab-case. I'll use `recurring-c2b-debits`.

Let me proceed.

Actually, let me reconsider the capability path for the spec. The spec-driven schema: `specs/<capability-path>/spec.md`. The openspec/specs/ is empty. So I need to create a new capability. Given the existing solution's capability naming, I'd create a capability like `recurring-debits` or `subscriptions`. The delta spec describes the new requirements.

Let me start executing.
У меня достаточно контекста. Проект использует OpenSpec (`schema: spec-driven`, CLI v1.13.2 установлен, корень определён), а принятое решение живёт в `docs/` + `ARCHITECTURE-SPINE.md`. Значит, принятый способ внести изменение поверх решения — **OpenSpec change-пакет** (propose → ревью → apply/archive), а не прямая правка принятых файлов. Я подготовлю архитектурный пакет как change «рекуррентные C2B-списания».

Сначала создам change и посмотрю порядок артефактов.

  `run_shell_command(command="openspec instructions proposal --change \"recurring-c2b-debits\" --json 2>&1", description="Получить шаблон и правила для proposal")`

The change is created. Now I need to get the instructions for each artifact. The dependency order is: proposal (ready) → specs + design (blocked by proposal) → tasks (blocked by specs + design).

Let me get the instructions for proposal first, then write it, then get specs/design/tasks.

Let me get instructions for all artifacts in parallel (I can get them now, though proposal must be written first). Actually, let me get proposal instructions first, write proposal, then get specs and design instructions, write them, then tasks.

Let me get proposal instructions.

  `run_shell_command(command="openspec list --specs 2>&1; echo \"---list---\"; openspec list 2>&1", description="Инвентарь существующих спецификаций")`

I have the proposal template and instruction. Let me check the existing specs inventory with `openspec list --specs` to understand the capability organization. The openspec/specs/ only has .gitkeep, so there are likely no existing specs. Let me confirm.

  `run_shell_command(command="openspec instructions specs --change \"recurring-c2b-debits\" --json 2>&1", description="Шаблон для specs")`
  `run_shell_command(command="openspec instructions design --change \"recurring-c2b-debits\" --json 2>&1", description="Шаблон для design")`
  `run_shell_command(command="openspec instructions tasks --change \"recurring-c2b-debits\" --json 2>&1", description="Шаблон для tasks")`

No existing specs. So the change will introduce new capabilities. The openspec/specs/ is empty, meaning the "accepted solution" hasn't been formalized into OpenSpec specs yet — it lives in docs/. This is a bit unusual: the repo has OpenSpec set up, but the accepted solution is in docs/ + ARCHITECTURE-SPINE.md, not in openspec/specs/.

So for this change, I'll introduce new capabilities that describe the recurring debits/subscriptions functionality. These are deltas against... nothing in openspec/specs/, but conceptually they extend the accepted solution (which is in docs/). 

The instruction says: "New Capabilities: List capabilities being introduced. Each becomes a new specs/<capability-path>/spec.md."

Since there are no existing specs, I'll create new capabilities. What capabilities should I define? Let me think about the domain decomposition for recurring C2B debits:

1. **Consent management (согласия плательщика)** — `recurring-debit-consents` or `consents`: create/manage/revoke payer consents, lifecycle.
2. **Recurring debit execution (исполнение рекуррентных списаний)** — `recurring-debits`: schedule/trigger debits, reuse payment state machine, debit idempotency.
3. Maybe combine into one capability `recurring-c2b` with sub-capabilities.

Actually, for a clean OpenSpec structure, I'll create one capability with a clear path. Given the project uses a flat docs structure, I'll use a single capability path. Options:
- `recurring-debits` (covers consents + debits)
- `consents` + `recurring-debits` (two)

I think two capabilities is cleaner because consent lifecycle and debit execution are distinct concerns with different states, different contract surfaces, different invariants. But they're tightly coupled. Let me go with a single capability `recurring-c2b-debits` with clearly separated requirement sections (consents, debits), OR two capabilities.

Hmm. Let me think about what's most useful and least likely to cause validation issues. The spec delta file uses ADDED/MODIFIED/REMOVED Requirements headers. With no existing specs, everything is ADDED.

I'll go with a single capability `recurring-c2b` — no wait, the path should be meaningful. Let me use two capabilities since they're genuinely distinct and the contract/state machine differ:

Actually, simpler is better for a first delta. Let me use ONE capability: `recurring-debits` that encompasses consent lifecycle + debit execution. Inside the spec, I'll have requirements for both. This keeps it to one spec file, which is cleaner for a change of this size.

Wait, but actually, the consent is a prerequisite entity. Let me reconsider the cleanest decomposition:

The domain entities:
1. **Согласие (consent/mandate)** — a payer-authorization record: who (payer), to whom (ТСП), max amount, frequency, expiry, status (ACTIVE/SUSPENDED/REVOKED/EXPIRED). This is a NEW source of truth, parallel to payment.
2. **Рекуррентное списание (recurring debit)** — an execution instance, which produces a payment (reusing the payment state machine) or is itself a payment-like entity with a reference to consent.

Both are needed. I'll model as a single capability `recurring-debits` with two requirement groups. Actually, let me keep the capability name singular and domain-clear: `recurring-c2b-debits` as capability path might be redundant with change name. Better capability name: `subscriptions` or `recurring-payments`.

Let me use capability path `recurring-payments` (covers consents + recurring debits). This is clean, and it's the product term ("подписки СБП").

Actually, I'll split into two capabilities because they have different lifecycles, different NFR, different contract endpoints, and this maps better to the eventual ADR split:
- `recurring-payments/consents` — hmm, nested.

Let me keep it simple and pragmatic: ONE capability `recurring-payments`. The spec.md will have sections:
- Requirements for consent lifecycle (CONSENT-001...)
- Requirements for recurring debit execution (DEBIT-001...)

This is fine and matches the "keep it concise" guidance.

Now let me write the proposal.md. It should be concise (1-2 pages), in Russian, with SHALL/MUST in English (for spec; proposal is prose).

Let me draft the proposal content.

Actually, I realize I should think carefully about the substantive architecture before writing, because proposal → specs → design → tasks all need to be coherent. Let me lay out the full architecture now (this is the "deep design" the user asked for).

## Significance assessment (route)

The parent initiative (C2B gateway) is Critical, significance 11/15. Recurring debits is a feature-level extension on top of the accepted solution. Assessment:
- Financial impact: HIGH (double debit = customer harm, reputation, refunds; but the gateway's idempotency machinery already exists).
- Regulatory/compliance: HIGH (consent = ПДн + НПС; payer revoke rights; 115-ФЗ).
- New domain entity (consent) with its own lifecycle → new status machine → extends AD-002.
- New contract surface (endpoints + webhooks) → touches AD-003/AD-004.
- Reuses transport (AD-004) and АБС integration (AD-005) — no new external system.
- НСПК protocol for subscriptions is an external input [ТРЕБУЕТ ПРОВЕРКИ].

Significance estimate: ~8/15 → route **Major** (not full Critical, because platform and transport already in design; but deep design needed: new ADR + delta spec + contract + NFR). Deep design required because: new financial entity, new status machine, regulatory consent lifecycle, backward-compatible contract changes, idempotency across a NEW key (consentId/scheduleKey/debitId).

## Impact on invariants (AD-001..AD-008)

Let me produce a precise table:

- AD-001 (изоляция платёжного контура): **не меняется** по сути. Расширяется Binds: к шлюзу добавляется хранилище согласий и планировщик списаний; правило (только через адаптеры) сохраняется. Status: не трогаем.
- AD-002 (единый источник истины — статусная машина платежа): **расширяется** — появляется второй конечный автомат (согласие) с тем же правилом атомарности (переход + outbox + аудит в одной транзакции). Сам платёжный автомат дополняется (рекуррентный платёж может иметь другой путь — без QR). Rule обновляется: «изменение финансового статуса платежа И согласия + outbox атомарно».
- AD-003 (идемпотентность): **расширяется** — добавляются ключи идемпотентности согласия (`consentId`, `mandateRef`) и списания (`debitId`, `scheduleKey`/`periodKey`). Правило то же, область применения шире.
- AD-004 (единственный адаптер ОПКЦ): **не меняется** — адаптер получает новые операции (регистрация согласия, инициирование рекуррентного списания) через внутренний контракт; протокол по-прежнему только в адаптере.
- AD-005 (зачисление только из PAID): **не меняется по смыслу, уточняется** — рекуррентное списание, как и разовый платёж, зачисляется только из подтверждённого статуса (`PAID`); согласие само по себе НЕ является основанием для зачисления. Новый guard: списание возможно только при `consent.status == ACTIVE` и в пределах лимитов согласия.
- AD-006 (trust-зоны): **не меняется** — согласия (ПДн) живут в платёжном контуре, те же зоны; никакой новой зоны не требуется.
- AD-007 (соответствие): **расширяется** — согласие как новый аудируемый объект; отзыв/истечение/приостановка — в неизменяемом аудит-логе; ПДн-минимизация (маска номера счёта/телефона плательщика); 115-ФЗ для серийных списаний.
- AD-008 (гибрид): **не меняется**, но расширяет требования к вендору — поддержка рекуррентных операций НСПК (согласие/списание) становится пунктом RFP.

New invariant needed: **AD-009** — «Согласие — отдельный источник истины с собственным жизненным циклом; списание инициируется только по активному согласию в пределах лимитов». (To be proposed, status Proposed.)

Nothing is BROKEN. Two invariants extended (AD-002, AD-003), one refined (AD-005), one new (AD-009 proposed). AD-001/AD-004/AD-006/AD-008 unchanged in substance.

## Architectural decision (ADR with alternatives)

Core decision: introduce a **consent domain entity** as a second source of truth in the gateway (parallel to payment), with its own state machine and idempotency, and model each recurring debit as a payment that references the consent. The gateway scheduler (or ТСП trigger) initiates debits; consent lifecycle governs authorization.

Alternatives:

**Alt 1 (chosen): Consent in gateway + debit-as-payment reuse.**
- Consent store + state machine in gateway (source of truth). Recurring debit creates a payment reusing existing state machine (new `paymentType=recurring` + `consentId`), no QR path.
- Pros: consistent with AD-002 (gateway is source of truth), reuses payment/outbox/reconciliation/idempotency machinery, consent lifecycle auditable in one place.
- Cons: new entity + state machine; scheduler is new infra; consent store must be highly available (RPO=0).

**Alt 2: НСПК as source of truth for consent/mandate (gateway as cache).**
- Consent registered and stored in НСПК (mandate), gateway mirrors.
- Pros: less duplication; НСПК enforces consent at debit time.
- Cons: gateway loses local source of truth (violates AD-002 spirit); dependence on НСПК for every consent check; НСПК mandate model is external [ТРЕБУЕТ ПРОВЕРКИ]; revoke latency depends on НСПК.

**Alt 3: Consent in АБС (bank's account system owns mandate).**
- Pros: АБС already owns accounts; consent near money.
- Cons: АБС has no СБП concept (ADR-005), would leak СБП semantics into АБС; violates AD-001 (isolation) / AD-004; slow evolution.

**Alt 4: ТСП-side scheduling, gateway only executes ad-hoc debits.**
- ТСП triggers each debit; gateway has no scheduler, no consent store (just validates a token).
- Pros: minimal gateway change.
- Cons: no bank-side control of schedule/limits; consent revocation not enforceable at bank; ТСП could over-debit; regulatory risk. Rejected as primary (may be a supported mode).

Decision: Alt 1 as primary, with Alt 4 as an optional supported mode (ТСП-triggered ad-hoc debit referencing a registered consent), and consent mirrored to НСПК if the НСПК subscription mandate requires it (hybrid mirroring — Alt 2 partially, but gateway remains source of truth for lifecycle). This is the "deep" decision.

Reversibility: **reversible** before go-live (feature flag; consent store additive). After go-live: consent data migration is one-way (like ADR-001), but the consent entity can be deprecated/rolled back with a feature flag; no irreversible money movement beyond debits already executed. So "reversible at start, costly to fully unwind after prod" — consistent with ADR-001/ADR-007.

Sub-decisions:
1. Schedule ownership: hybrid — bank gateway scheduler owns schedules (cron by consent.frequency), but ТСП may trigger ad-hoc debit via API. (Open question: НСПК subscription model may dictate.)
2. Fixed vs variable amount: consent supports `maxAmountPerPeriod` (ЖКХ variable) with optional `fixedAmount`; debit amount must be ≤ max.
3. Consent capture UX: depends on НСПК protocol — payer consent via payer's bank app / НСПК consent flow [ТРЕБУЕТ ПРОВЕРКИ]. Gateway stores the consent record once captured.
4. Revoke: payer or ТСП can revoke; revoke → consent SUSPENDED/REVOKED; scheduler stops debits immediately; already-scheduled debits not yet executed are cancelled.

## Contract changes (backward compatible)

New endpoints (additive, /v1, no breaking):
- `POST /v1/consents` (Idempotency-Key) — create consent. Returns consentId + status.
- `GET /v1/consents/{consentId}` — consent status + limits.
- `POST /v1/consents/{consentId}/revoke` (Idempotency-Key) — revoke (payer or ТСП).
- `GET /v1/consents/{consentId}/debits` — list debits under consent.
- `POST /v1/consents/{consentId}/debits` (Idempotency-Key) — trigger a debit (ТСП-triggered mode), or `POST /v1/debits`.
- (Optional) `GET /v1/debits/{debitId}` — debit status.

Extensions to existing schemas (additive optional fields):
- `PaymentRequest`: add optional `consentId`, `paymentType` (enum `one_time|recurring`). Default `one_time` — backward compatible.
- `Payment`: add optional `paymentType`, `consentId`, `mandateRef`.
- `Payment.status` enum: no change needed (debit reuses CREATED..COMPLETED), OR add `DEBIT_PENDING`? Better: reuse existing states; recurring debit follows same lifecycle, skipping QR_ISSUED (goes CREATED→PAID→CREDITED→COMPLETED, or a "pending debit" pre-state). Actually, need a state for "scheduled but not yet executed"? No — a scheduled debit that hasn't been initiated isn't a payment yet; it's a schedule entry in the consent. When the debit executes, a Payment is created (CREATED) and proceeds.

Webhook events (additive):
- `consent.created`, `consent.revoked`, `consent.expired`, `consent.suspended`
- `debit.completed`, `debit.failed`, `debit.insufficient_funds` — or reuse `payment.*` with a `paymentType=recurring` discriminator. To avoid breaking existing webhook consumers, add new event types and optionally extend existing `payment.completed` body with `paymentType`/`consentId` (additive).

Idempotency: new keys — `consentId` for consent creation; `scheduleKey`/`periodKey` for scheduled debits (to prevent double debit in the same period); `debitId` for ad-hoc debits.

Versioning: all changes are additive (optional fields, new endpoints, new webhook types) → stay on /v1, no /v2 needed. Document in §6 of tsp-api.md.

## NFR (measurable)

New/refined NFR for recurring:
- Consent registration: p95 < 500 ms (same as QR registration).
- Debit initiation: p95 < 500 ms (same).
- Schedule accuracy: ≥ 99.9% of scheduled debits initiated within ±5 min of scheduled time (ЖКХ needs predictable debiting).
- Double debit: 0 (idempotency by scheduleKey + period).
- Revoke propagation: debit stopped ≤ 1 min after revoke (no new debits after revoke).
- Consent availability/RPO: same as gateway — RPO=0, ≥ 99.95%.
- Consent→НСПК sync (if mirrored): eventual, ≤ 60 s.
- Audit: 100% consent lifecycle transitions in immutable audit log.
- AML: 100% recurring debits pass AML thresholds check.
- Throughput: sustained 200 TPS includes recurring debits (burst on billing day: ЖКХ/телеком списывают пачкой в определённые дни — burst 500→1000 TPS).

Actually, a key NFR is burst capacity on billing days (many subscriptions debit on the 1st). This is a scheduling/batch concern: need to schedule debits across a window to flatten the burst. Add NFR: "burst debit initiation up to 1000 TPS for 1 min, scheduler spreads batch over window."

## Acceptance criteria + rollback plan

Acceptance (A4/A5 analog):
- Feature flag `recurring.enabled` gates consent creation and debit initiation independently.
- End-to-end: consent created → scheduled debit → НСПК confirm → АБС credit → webhook, with idempotent replay (same scheduleKey → no second debit).
- Negative: revoke mid-period → no further debits; debit amount > maxAmount → rejected; duplicate НСПК notification → single credit; АБС down → debit stays PAID, reconciled.
- Contract: existing one-time flows and existing consumers unaffected (regression suite green).
- NFR verified by load tests.

Rollback plan:
- Pre-go-live: reversible — don't enable feature flag; no data to unwind.
- Post-go-live: turn OFF `recurring.enabled` → stops new consents + new debits; already-executed debits settle normally (refunds via existing saga). Rolling release rollback. Consent data retained (no reverse migration), disabled via flag. Signal to rollback: double-debit incident, breach of schedule accuracy SLO, НСПК protocol mismatch.

## Open questions for human architect

1. НСПК subscription/mandate protocol — external input [ТРЕБУЕТ ПРОВЕРКИ]: exact consent model, consent capture UX (payer's bank app vs merchant), whether НСПК stores mandate. Blocks full consent design.
2. Schedule ownership: who is authoritative for the debit calendar (bank gateway vs ТСП vs НСПК)? Business decision.
3. Fixed vs variable amount; per-period max and frequency rules for ЖКХ (variable billing). Business + НСПК limits.
4. Payer revoke surface: must payer revoke in payer's bank app (НСПК) AND/OR in gateway? Regulatory minimums (161-ФЗ, НСПК rules).
5. Should this be a new AD (AD-009) + ADR-008, or fold into existing AD-002/AD-005? Architectural decision (I recommend new AD-009 + ADR-008).
6. Burst scheduling policy for billing days (flatten vs immediate) — ops/business.
7. Whether to extend existing tsp-api v1 or introduce /v2 — I recommend additive v1 (no break), confirm with product.

Now, this is a LOT of content. I need to distribute it across proposal.md, specs/, design.md, tasks.md appropriately:

- **proposal.md**: Why, What Changes (bullet list), Capabilities (new capability `recurring-payments`), Impact. Concise. Include the significance/route assessment and invariant impact summary (the user's deliverables #1 and #2 fit naturally in proposal as "Why"/"Impact" and maybe a brief "Маршрут и влияние" note). Actually, the proposal template is specific: Why / What Changes / Capabilities / Impact. I can put significance+route in "Why" (or a brief note), invariant impact in "Impact". But the user wants a THOROUGH package. The proposal should stay concise per instruction. The deeper impact analysis, ADR, NFR, acceptance, rollback go in design.md.

Let me map deliverables to artifacts:
1. Оценка значимости и маршрута → proposal.md (Why + a short "Маршрут/значимость" note) — actually I'll add a compact "Значимость и маршрут" line in Why, and detail in design.md §1.
2. Влияние на архитектуру (инварианты) → design.md §2 (table) + proposal Impact (brief).
3. ADR с альтернативами → design.md §3 (full ADR).
4. Изменения контрактов → design.md §4 + spec.md (formal requirements).
5. NFR → design.md §5.
6. Критерии приёмки + план отката → design.md §6, §7.
7. Открытые вопросы → design.md §8 + proposal (brief).

So design.md is the heavy document. proposal.md is the concise "why/what". spec.md is the formal delta. tasks.md is the implementation breakdown.

This is consistent with the OpenSpec schema (design = "how", includes ADR/alternatives/NFR/rollback).

Now let me write the files. I'll write proposal.md first, then get specs and design instructions (they're already partly known, but let me get their templates), then write specs and design, then tasks.

Actually, I already have the proposal template. Let me also get specs and design instructions now (in parallel) so I know the exact templates, but specs/design are "blocked" by proposal in the status (I must write proposal first for the status to advance, but I can still read their instructions/templates now). The instruction says to get instructions for each artifact that is "ready". But I can fetch instructions for specs and design too to know templates. Let me fetch them now in parallel with writing proposal? No, write_file and run_shell are independent. Let me fetch specs+design+tasks instructions now in parallel, then write all files.

Actually, let me be careful: tasks requires specs+design. I'll write proposal, then specs+design, then tasks. Let me fetch the templates for specs, design, tasks now in one batch.

  `write_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/openspec/changes/recurring-c2b-debits/pro, content="# Proposal\n\n## Why\n\nТСП (онлайн-кинотеатры, ЖКХ, связь) требуют рекуррентные C2B-списания по согласию плательщика — «подписки СБП». Сег)`

I now have all the templates and instructions. Let me write the artifacts.

The context field is: "Language: ru / All artifacts must be written in ru. Keep OpenSpec structural headings and SHALL/MUST keywords in English."

So all prose in Russian, but structural headings (## Purpose, ## ADDED Requirements, ### Requirement, #### Scenario, WHEN/THEN, SHALL/MUST) in English.

Let me write proposal.md first. It should be concise (1-2 pages), Russian.

Let me plan the capability path. I'll use `recurring-payments` as a single new capability. Actually, let me reconsider — should I split into two capabilities (consents + debits)? 

Given the guidance "do not add a new domain level when the project uses a flat layout", and the project's docs/ is flat, I'll use a single flat capability path `recurring-payments`.

Hmm, but actually, thinking more about it — consent management and recurring debit execution are genuinely two separable capabilities with distinct contracts, states, and even separate ADR concerns. But they're tightly coupled (debit requires consent). For a single change proposal, one capability is cleaner and avoids over-fragmentation. I'll go with one capability `recurring-payments`, with clear requirement prefixes (CONSENT-*, DEBIT-*).

Actually, wait. Let me reconsider naming. The capability describes "рекуррентные C2B-списания по согласию плательщика". A good capability name: `recurring-debits`. That captures both consent (prerequisite) and debit (execution). Or `subscriptions`. I'll use `recurring-debits`.

Let me finalize: capability path = `recurring-debits`.

Now write proposal.md.

For the proposal, I'll keep it concise but cover:
- Why (problem, why now, + significance/route)
- What Changes (bullet list, mark nothing BREAKING since all additive)
- Capabilities (New: recurring-debits; Modified: none since no existing specs)
- Impact (systems, APIs, invariants briefly)

Let me write it.

Actually, I want to include the significance/route assessment (deliverable #1) and invariant impact (deliverable #2) somewhere prominent. The proposal's "Impact" section is the right place for invariant impact. The "Why" can carry a brief significance note. But the user wants a THOROUGH treatment. The design.md will carry the deep analysis. In proposal, I'll add a compact "Значимость и маршрут" note and reference design.md.

Let me write all four files now. I'll write proposal.md first.

Let me draft the proposal.md content carefully in Russian.

---

# Proposal (I'll keep the heading as per template "# Proposal")

Actually the template starts with "# Proposal". Let me follow template structure but with Russian content.

## Why

ТСП (онлайн-кинотеатры, ЖКХ, связь) требуют рекуррентные C2B-списания по согласию плательщика — «подписки СБП». Сейчас каждый платёж требует выпуска QR и действия клиента, что неприемлемо для регулярных начислений. Это новое финансовое измерение поверх принятого решения (шлюз C2B), а не отдельная инициатива.

Значимость: ~8/15 (финансовые последствия двойного списания, ПДн согласия, новая доменная сущность и статусная машина, регуляторные требования к отзыву). Маршрут: **Major** — глубокая проработка нужна, но платформа и транспорт уже в проектировании; повторного Solutioning уровня Critical не требуется, но нужен отдельный ADR, delta-spec, изменения контракта и NFR.

## What Changes

- Новая доменная сущность **Согласие плательщика** (consent/mandate) с собственным жизненным циклом и статусной машиной — второй источник истины в шлюзе наряду с платежом.
- **Рекуррентное списание** как платёж, инициируемый по активному согласию (без QR), повторно использующий существующую статусную машину платежа.
- Новые методы API ТСП: создание/просмотр/отзыв согласия, инициирование и просмотр списаний (аддитивно, `/v1`).
- Новые типы вебхуков: `consent.*` и `debit.*` (аддитивно; существующие `payment.*` сохраняются).
- Расширение схем `PaymentRequest`/`Payment` опциональными полями (`paymentType`, `consentId`, `mandateRef`) — без изменения обязательных полей.
- Расширение требований к вендору адаптера ОПКЦ (рекуррентные операции НСПК) и к сверке/аудиту.
- Новый инвариант **AD-009** (предлагаемый): согласие — отдельный источник истины; списание только по активному согласию в пределах лимитов.
- Никаких **BREAKING** изменений существующего контракта.

## Capabilities

### New Capabilities
- `recurring-debits`: жизненный цикл согласия плательщика (создание, лимиты, отзыв/истечение) и исполнение рекуррентных списаний с идемпотентностью по периоду.

### Modified Capabilities
(пусто — в openspec/specs нет ранее зафиксированных спецификаций; принятое решение описано в docs/ + ARCHITECTURE-SPINE.md, изменение фиксируется как новая capability-дельта.)

## Impact

- **Инварианты spine**: AD-002 и AD-003 расширяются (второй автомат, новые ключи идемпотентности); AD-005 уточняется (зачисление только из подтверждённого статуса, согласие — не основание); предлагается AD-009. AD-001/AD-004/AD-006/AD-008 не меняются по сути. Ни один инвариант не нарушается.
- **API ТСП**: новые эндпоинты и события, опциональные поля — обратно совместимо, `/v1` сохраняется.
- **Адаптер ОПКЦ**: новые операции внутреннего контракта + событие, расширение RFP вендора.
- **Данные**: новая таблица согласий + планировщик списаний в платёжном контуре; RPO=0 распространяется на согласия.
- **Сверка/аудит/AML**: согласия и списания включаются в сверку, неизменяемый аудит-лог и AML-контроль.

---

That's a solid proposal. Now the spec.md (delta).

Spec delta: new capability `recurring-debits`, first section `## Purpose`, then `## ADDED Requirements`.

I need to write requirements with SHALL/MUST and scenarios (#### Scenario with WHEN/THEN, exactly 4 hashtags).

Let me define requirements:

## Purpose
Capability for payer-consented recurring C2B debits (СБП подписки): lifecycle of payer consents and execution of recurring debits against the existing payment state machine, with period idempotency and consent-authorization checks.

Requirements:

1. ### Requirement: Создание согласия плательщика
   The system SHALL allow a ТСП to register a payer consent (согласие) with idempotency key, capturing payer reference, ТСП, max amount per period, frequency, and expiry. Returns consentId + status.
   Scenarios: successful create; idempotent retry (same key → same consentId); conflict (same key diff body → 409).

2. ### Requirement: Жизненный цикл согласия
   Consent SHALL be in one of ACTIVE, SUSPENDED, REVOKED, EXPIRED. Transitions atomic (status + outbox + audit). Payer or ТСП revoke → REVOKED; schedule expiry → EXPIRED; operational hold → SUSPENDED.
   Scenarios: revoke; expiry; suspend.

3. ### Requirement: Лимиты согласия обязательны для списания
   A recurring debit SHALL be initiated only when consent.status == ACTIVE, within expiry, and debit amount ≤ maxAmountPerPeriod. Exceeded limit → rejected.
   Scenarios: within limits → accepted; over limit → rejected.

4. ### Requirement: Рекуррентное списание создаёт платёж без QR
   Each initiated recurring debit SHALL create a payment (paymentType=recurring, consentId set) that follows the payment state machine (CREATED→PAID→CREDITED→COMPLETED), with зачисление only from PAID.
   Scenarios: debit creates payment in CREATED; credit only from PAID.

5. ### Requirement: Идемпотентность списания по периоду
   The system SHALL prevent more than one debit per consent per period using a period key (scheduleKey/periodKey); retry/duplicate → same debit, no second debit.
   Scenarios: duplicate trigger same period → one debit; retry returns existing debit.

6. ### Requirement: Отзыв согласия прекращает новые списания
   After consent is REVOKED/EXPIRED/SUSPENDED, the system SHALL NOT initiate new debits; already-initiated debits continue to settlement.
   Scenarios: revoke → no new debit; in-flight debit settles.

7. ### Requirement: Нотификация событий согласия и списания
   The system SHALL deliver webhook events consent.* and debit.* (at-least-once, idempotent by eventId), in addition to existing payment.* events.
   Scenarios: consent revoked webhook; debit completed webhook.

8. ### Requirement: Аудит и сверка согласий и списаний
   Every consent lifecycle transition and debit SHALL be recorded in the immutable audit log and included in reconciliation.
   Scenarios: audit record; reconciliation includes debits.

That's 8 requirements, each with scenarios. Good. Maybe I'll consolidate to keep it tight but complete. Let me write full scenarios.

Now design.md. This is the heavy document with all the deliverables:
- Context (current state, constraints)
- Goals / Non-Goals
- Decisions (ADR with alternatives — the core)
- Risks / Trade-offs
- Migration Plan (deploy + rollback)
- Open Questions

But I also need to embed NFR, acceptance criteria, contract changes, invariant impact. The design template has: Context, Goals/Non-Goals, Decisions, Risks/Trade-offs, (Migration Plan, Open Questions are mentioned in instruction but not in template). The instruction lists sections: Context, Goals/Non-Goals, Decisions, Risks/Trade-offs, Migration Plan, Open Questions. The template only shows Context/Goals/Decisions/Risks. I can add Migration Plan and Open Questions sections (they're in the instruction). Also I'll add sections for "Влияние на принятую архитектуру" (invariant impact), "Изменения контрактов", "NFR", "Критерии приёмки" — these are the user's deliverables. The design.md is the right place.

Let me structure design.md:

# Design

## Context
(кратко: что уже есть — шлюз C2B, AD-001..008, статусная машина, idempotency, outbox, transport adapter; ссылка на proposal)

## Goals / Non-Goals
Goals: consent lifecycle + recurring debit execution reusing payment machine; backward-compatible contract; period idempotency; consent authorization.
Non-Goals: C2C, B2C payouts, disputes; QR-based one-time changes; consent capture UX (external НСПК); actual НСПК protocol.

## Значимость и маршрут (deliverable 1)
(краткое резюме — Major, 8/15, почему глубокая проработка)

## Влияние на принятую архитектуру (deliverable 2)
Table AD-001..AD-008 + AD-009 proposed.

## Decisions (deliverable 3 — ADR)
- D1: Consent как вторая доменная сущность в шлюзе (source of truth), с альтернативами.
- D2: Debit = payment reuse (paymentType=recurring), без отдельной сущности списания.
- D3: Schedule ownership hybrid (gateway scheduler + ТСП-triggered).
- D4: Идемпотентность по periodKey.
- D5: Fixed vs variable amount (maxAmountPerPeriod).
- D6: Reversibility assessment.

Each with alternatives table + consequences.

## Изменения контрактов (deliverable 4)
Endpoints, schemas, webhooks, idempotency keys, versioning — with concrete OpenAPI fragments (illustrative).

## NFR (deliverable 5)
Table.

## Критерии приёмки и план отката (deliverable 6)
Acceptance criteria + rollback.

## Risks / Trade-offs
Risk → mitigation table.

## Migration Plan
Deploy steps + rollback.

## Open Questions (deliverable 7)
List with why-human-needed.

This is comprehensive. It's a lot of content but the user explicitly asked for a thorough package.

Now tasks.md — implementation checklist. Since this is planning-only and the walking skeleton is being implemented by a code harness, tasks should reflect the implementation steps for recurring debits (consent store, state machine, endpoints, scheduler, webhooks, tests, docs). Each task with verification.

Note: the tasks instruction says "Before writing tasks, check design.md for Open Questions. If any of them would change what gets built, resolve them with the user first". Some open questions (НСПК protocol, schedule ownership) DO affect what gets built. But the user explicitly asked me to produce the package INCLUDING "что остаётся на решение человека-архитектора". So these open questions are intentionally deferred to the human architect — they're part of the deliverable. The tasks should therefore be scoped to what CAN be built now (the gateway-side consent/debit machinery with a mock adapter), explicitly gating the НСПК-dependent parts behind the external input. This is consistent with how the existing solution handles it (mock adapter, [ТРЕБУЕТ ПРОВЕРКИ]).

I'll structure tasks to build the walking-skeleton extension with mock adapter, and mark the НСПК-protocol-dependent steps as "blocked on external input" tasks (or reference the open questions). Actually, tasks should be actionable. I'll write tasks that build consent + recurring debit on the existing walking skeleton, with mock НСПК adapter extension, and note the gate.

Let me now write all four files. I'll write them in sequence (proposal, then specs, then design, then tasks), but I can write proposal + specs + design in one batch since I've already decided all content, then tasks after. Actually the write_file calls are independent; I can do them all. But to be safe and follow the dependency (specs/design depend on proposal being written), I'll write proposal first, then specs+design, then tasks. Since there are no actual read dependencies for MY content (I've already planned everything), I can write them all now. But the status check after each matters. Let me write proposal first, verify, then the rest.

Actually, to be efficient and since I've fully planned the content, I'll write proposal.md, spec.md, and design.md in parallel (three write_file calls in one message), then tasks.md after (it depends on specs+design existing). Then run final status + validate.

Wait, but I need to be careful: the spec.md path is `openspec/changes/recurring-c2b-debits/specs/recurring-debits/spec.md` (capability path `recurring-debits`).

Let me write proposal.md, spec.md, design.md now.

Let me carefully compose each file's full content.

For the spec, I must ensure scenarios use exactly `#### Scenario:` and WHEN/THEN bullets. Requirements use `### Requirement:`.

Let me write everything in Russian prose, keeping structural keywords English.

Let me now write the proposal.
Контекст собран, шаблоны получены. Пишу артефакты change-пакета. Начну с `proposal.md`, затем `specs/` и `design.md`.

  `write_file(content="# Spec Delta\n\n## Purpose\n\nОбеспечивает рекуррентные C2B-списания по согласию плательщика: управление жизненным циклом согласия (mandate, file_path="<HARNESS>/runs/cells/openspec-r2/ws/openspec/changes/recurring-c2b-debits/spe)`

Now write the spec.md delta.

  `write_file(content="# Design\n\n## Context\n\nПринятое решение «Платёжный шлюз СБП (C2B-приём)» уже зафиксировало: выделенный компонент с транзакционным outbox, file_path="<HARNESS>/runs/cells/openspec-r2/ws/openspec/changes/recurring-c2b-debits/des)`

Now write design.md — the heavy document with all the deliverables.

Let me compose it carefully, in Russian, keeping structural headings. I'll include:

1. Context
2. Goals / Non-Goals
3. Значимость и маршрут (deliverable 1)
4. Влияние на принятую архитектуру (deliverable 2)
5. Decisions (ADR with alternatives — deliverable 3)
6. Изменения контрактов (deliverable 4)
7. NFR (deliverable 5)
8. Критерии приёмки и план отката (deliverable 6)
9. Risks / Trade-offs
10. Migration Plan
11. Open Questions (deliverable 7)

Let me write it comprehensively but not bloated. I'll keep each section focused.

Let me write it now.

  `write_file(content="# Tasks\n\n## 1. Модель данных согласия и статусная машина\n\n- [ ] 1.1 Добавить таблицу `consents` с уникальным индексом `(consent_id)` и , file_path="<HARNESS>/runs/cells/openspec-r2/ws/openspec/changes/recurring-c2b-debits/tas)`

Now write tasks.md. The tasks should be actionable implementation steps for the walking skeleton extension, each with verification, in checkbox format, grouped under ## numbered headings.

Let me think about the implementation tasks for recurring debits on top of the existing walking skeleton:

1. Data model / consent store
2. Consent state machine + outbox/audit
3. Consent API endpoints
4. Recurring debit execution (paymentType=recurring) + period idempotency
5. Scheduler
6. Mock adapter extension
7. Webhooks
8. Tests (idempotency, negative, NFR)
9. Docs (contract, NFR updates — but note these are accepted files, changed via apply/archive/sync)

Note: since this is planning-only, tasks describe what apply will do. The tasks instruction says each task must state how to verify. And each group must land its own tests/docs.

Let me also note the gate: НСПК protocol-dependent parts blocked on external input — I'll mark a task that's gated.

Let me write tasks.md with checkbox format. Keep it focused on what can be built with the mock adapter.

Task groups:
1. Модель данных согласия (consent store + state machine)
2. API согласия и списания (endpoints)
3. Исполнение списаний (paymentType=recurring + periodKey idempotency + guard)
4. Планировщик списаний
5. Мок-адаптер ОПКЦ (registerConsent/initiateRecurringDebit) + нотификатор/вебхуки
6. Тесты и документация (acceptance/NFR)
7. Гейт на внешний вход НСПК (blocked)

Let me write concise but complete tasks with verification embedded.

I'll write it now.

  `run_shell_command(command="openspec status --change \"recurring-c2b-debits\" 2>&1; echo \"---validate---\"; openspec validate \"recurring-c2b-debits\" 2>&1; echo \"--, description="Статус и валидация change")`

Now run final status and validate.
Все четыре артефакта созданы. Проверяю статус и валидность change.

  `run_shell_command(command="cd <HARNESS>/runs/cells/openspec-r2/ws && find openspec/changes/recurring-c2b, description="Список созданных файлов change и статус git")`

The change is valid (both normal and strict). All 4 artifacts complete.

Now let me verify my work is complete and consistent. Let me do a final review of what I've created:

1. proposal.md — significance/route, what changes, capabilities, impact (invariants).
2. specs/recurring-debits/spec.md — formal delta with 8 requirements + scenarios.
3. design.md — full package: significance, invariant impact table, ADR decisions with alternatives, contract changes, NFR, acceptance criteria, rollback, risks, migration, open questions.
4. tasks.md — implementation checklist.

All 7 deliverables are covered:
1. Оценка значимости и маршрута → proposal (Why) + design §Значимость и маршрут. ✓
2. Влияние на принятую архитектуру → design §Влияние (table AD-001..AD-009) + proposal Impact. ✓
3. Архитектурное решение с альтернативами/последствиями/обратимостью → design §Decisions (D1-D6 with alternatives tables, consequences, reversibility). ✓
4. Изменения контрактов без поломки → design §Изменения контрактов (additive, /v1). ✓
5. Измеримые NFR → design §NFR. ✓
6. Критерии приёмки и план отката → design §Критерии приёмки и план отката. ✓
7. Что остаётся на решение человека → design §Open Questions. ✓

Now, one thing to double-check: the user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." I did NOT modify any accepted files (ARCHITECTURE-SPINE.md, docs/, openapi/tsp-api.yaml). I only created files under openspec/changes/recurring-c2b-debits/. This is correct — the OpenSpec change is the accepted method.

I should also verify I haven't left anything incomplete. Let me also double-check: did `openspec new change` create any other scaffold files (like `.openspec.yaml`)? Let me verify the change directory contents to report accurately.

Actually, let me check the full list of what was created in the change directory.

  `read_file(file_path="<HARNESS>/runs/cells/openspec-r2/ws/openspec/changes/recurring-c2b-debits/.op)`

The change directory contains 5 files (4 artifacts + .openspec.yaml scaffold). The git status shows only the new untracked directory `openspec/changes/recurring-c2b-debits/` — no accepted files were modified. 

The `.openspec.yaml` was auto-generated by `openspec new change`. Let me quickly check its content to make sure it doesn't have `skip_specs: true` (which would be wrong) or anything odd.


Everything is clean. The `.openspec.yaml` just has schema and created date, no skip_specs.

The work is complete. Let me now provide a concise final summary in Russian (matching the user's language).

The user asked me to:
1. Prepare an architectural package for recurring C2B debits.
2. Not write code.
3. Change accepted solution files only via the accepted method.
4. When done, briefly list created/changed files.

I should summarize:
- What I did (used OpenSpec change workflow — the repo's accepted method).
- The 7 deliverables and where they live.
- Created files list.
- Confirmation that no accepted files were modified (this is important to state).
- Next step (review → apply/archive → sync, and human decision points).

Let me write a concise but complete final answer. I should mention the key architectural conclusions briefly (significance Major ~8/15, invariants extended AD-002/003, refined AD-005, new AD-009 proposed, additive /v1 contract, decision D1-D6).

I should NOT over-explain but give enough to understand and act.

Let me write the final response in Russian.

Key points to convey:
- Package prepared as OpenSpec change `recurring-c2b-debits` (accepted method in repo), planning-only, no code.
- Validated: `openspec validate --strict` = valid, 4/4 artifacts.
- No accepted files touched (ARCHITECTURE-SPINE.md, docs/, openapi/tsp-api.yaml) — changes recorded as delta, to be merged via apply/archive/sync.
- Deliverable mapping.
- Key conclusions (very brief).
- Human decision points (brief, they're in design.md).

Let me write it.
Готово. Архитектурный пакет подготовлен как OpenSpec-изменение `recurring-c2b-debits` — это и есть принятый в репозитории способ менять решение поверх принятого (планирование только, код не писал). Ни один принятый файл (`ARCHITECTURE-SPINE.md`, `docs/`, `openapi/tsp-api.yaml`) напрямую не менялся: изменение зафиксировано как delta-пакет, который вносится через принятую процедуру `apply → archive → sync`.

Проверка: `openspec validate --strict` → **valid**, артефакты **4/4 complete**.

## Где лежат запрошенные 7 результатов

| # | Результат | Файл |
|---|---|---|
| 1 | Оценка значимости (~8/15, маршрут **Major**) и обоснование глубины | `proposal.md` (Why) + `design.md` §«Значимость и маршрут» |
| 2 | Влияние на инварианты AD-001…AD-008 + предлагаемый AD-009 | `design.md` §«Влияние на принятую архитектуру» |
| 3 | ADR с альтернативами, последствиями, обратимостью (D1–D6) | `design.md` §«Decisions» |
| 4 | Изменения контракта без поломки потребителей (аддитивно, `/v1`, без `/v2`) | `design.md` §«Изменения контрактов» |
| 5 | Измеримые NFR | `design.md` §«NFR» |
| 6 | Критерии приёмки и план отката | `design.md` §«Критерии приёмки и план отката» |
| 7 | Что остаётся человеку-архитектору и почему | `design.md` §«Open Questions» |

Плюс формальный контракт поведения — `specs/recurring-debits/spec.md` (8 требований со сценариями), и чек-лист реализации — `tasks.md`.

## Ключевые выводы

- **Ни один инвариант не нарушается.** AD-002 и AD-003 **расширяются** (второй автомат «согласие», новые ключи идемпотентности `consentId`/`debitId`/`periodKey`), AD-005 **уточняется** (зачисление только из `PAID`, согласие — не основание), AD-007 **расширяется**; предлагается **AD-009**. AD-001/AD-004/AD-006/AD-008 не меняются.
- **Ядро решения**: согласие — второй источник истины в шлюзе со своим автоматом; списание — платёж `paymentType=recurring`, переиспользующий существующую статусную машину; «одно списание на период» через `periodKey`; планировщик шлюза + опциональный триггер ТСП.
- **Контракт** — только аддитивные изменения `/v1` (новые эндпоинты `/v1/consents*`, опциональные поля в `PaymentRequest`/`Payment`, новые вебхуки `consent.*`/`debit.*`).

## Созданные файлы

```
openspec/changes/recurring-c2b-debits/
├── proposal.md
├── design.md
├── tasks.md
├── .openspec.yaml          (scaffold от openspec new change)
└── specs/recurring-debits/spec.md
```

Изменённых файлов нет — только новая (untracked) директория `openspec/changes/recurring-c2b-debits/`.

## Следующий шаг

Пакет готов к ревью. Для вынесения на архитектурное решение просмотрите `design.md` (особенно §«Decisions» и §«Open Questions»); после утверждения — `/opsx-apply` для передачи исполнителям. Шесть вопросов в «Open Questions» (модель подписки НСПК и UX захвата согласия, владелец расписания, фикс/переменная сумма для ЖКХ, поверхность отзыва, формализация AD-009/ADR-008, политика пиковой нагрузки) требуют решения человека-архитектора, поскольку зависят от внешнего входа НСПК `[ТРЕБУЕТ ПРОВЕРКИ]` или бизнес-решений.
