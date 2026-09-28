<!-- источник: <HARNESS>/runs-clean/cells/wwd3ti3/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-clean-cells-wwd3ti3-ws/chats/c5daf733-dd6d-4d95-b67a-c1317b89df2a.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `run_shell_command(command="git status && echo \"---LOG---\" && git log --oneline -10", description="Git status and recent log")`
  `glob(pattern="**/*")`

The user wants me to prepare an architectural package for adding recurring C2B debits (subscriptions) to an existing SBP payment gateway decision. This is a substantial architecture task. Let me first understand the repository thoroughly.

This is clearly a task where I should:
1. Understand the existing architecture (spine, ADRs, contracts, NFRs, docs)
2. Use the project skills/tools appropriately (spine tools, adr-authoring, significance routing, nfr-design, delta-spec, etc.)

Let me start by exploring the repository. I need to read the key files:
- ARCHITECTURE-SPINE.md
- docs/solutioning.md, docs/nfr.md
- docs/adr/*.md
- docs/contracts/*
- openapi/tsp-api.yaml
- .arch-handoff/* (CONSTRAINTS.yaml, TASK.md, ARCHITECTURE.md, MANIFEST.json, RUBRIC.yaml)
- README.md

Let me first get the git status and explore the structure. This is a read-heavy investigation task, then I'll produce documents.

Let me be careful about the instruction: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." (Change accepted decision files only the way accepted in this repo). So I need to figure out whether changes go through delta-spec / ADR / etc.

Let me start exploring. I should use parallel tool calls to read files efficiently.

First, let me check git status and get the file tree.
Начну с изучения репозитория: спайн, принятые ADR, контракты, NFR и правила handoff-пакета.

  `glob(pattern="**/*.md")`
  `glob(pattern="docs/**/*")`
  `glob(pattern="openapi/**/*")`
  `glob(pattern=".arch-handoff/**/*")`

Let me read the key files. Let me get the full file list first, then read the core files in parallel.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/nfr.md")`

Now let me read the core files. I'll read them in parallel.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/adr/ADR-001-outbox.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/adr/ADR-002-model-konsistentnosti-)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/adr/ADR-004-at-least-once-dlq.md")`

Now let me read the ADRs, contracts, state machine, and the handoff package files.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/adr/ADR-005-integraciya-s-abs-zach)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/spec/state-machine.md")`

Let me continue reading ADR-005, 006, 007, contracts, state machine, and handoff files.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/openapi/tsp-api.yaml")`

Now let me read the contracts and the handoff package files.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.arch-handoff/ARCHITECTURE.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.arch-handoff/connect-manifest.json")`

Now let me read the handoff package files (CONSTRAINTS.yaml, TASK.md, ARCHITECTURE.md, MANIFEST.json, RUBRIC.yaml, connect-manifest.json).

  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.qwen/skills/significance-routing/SKILL)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.qwen/skills/adr-authoring/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.qwen/skills/adr-authoring/references/a)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.qwen/skills/delta-spec/SKILL.md")`

I now have a comprehensive understanding of the repository. Let me also check the RFP vendor file and the skills that are most relevant. The key skills I need to use:
- `significance-routing` (for significance/marшрут assessment)
- `adr-authoring` (for the ADR)
- `delta-spec` (how to change the accepted decision)
- `nfr-design` (for NFR)
- `spine-invariants` (for the spine)
- `spine-contracts-gate` (for contract changes without breaking)
- `readiness-gate` (criteria)

But first, I should determine how changes are made in this repo. The instruction says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." (Change accepted decision files only the way accepted in this repo).

Key insight from the repo structure:
- `ARCHITECTURE-SPINE.md` has AD-001..AD-008 with statuses Proposed/Adopted. ADs are "Proposed" until ratified by ADR, and "Adopted" after ratification.
- The spine has a "Deferred" section for features out of scope. Recurring C2B debits (subscriptions/автоплатежи) are currently listed in `docs/solutioning.md` section 1: "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." And the spine Deferred section says "C2C-переводы и выплаты B2C/B2B" are deferred, but автоплатежи (recurring) aren't explicitly in the Deferred list. Actually solutioning.md says "автоплатежи" is roadmap/вне scope.

So the change is about "автоплатежи" (recurring payments / autopayments), which are currently explicitly out of scope. This is a NEW feature that needs to be brought back into scope.

The proper way to change the repo:
1. New ADR(s) (ADR-008+) with Status Proposed, recording the decision with alternatives and consequences.
2. New spine block(s) AD-009 (or extend AD-008), with status Proposed.
3. Possibly update solutioning.md, nfr.md, state-machine.md, tsp-api.md contract, openapi/tsp-api.yaml.
4. New delta-spec? Let me check the delta-spec skill to understand how changes should be made.

Actually, there's a `delta_guard` MCP tool that gates direct edits to spine under protected paths (model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml) via delta protocol. But the repo currently doesn't have a model/ directory (it uses prose ADRs in docs/adr/). The spine is prose in ARCHITECTURE-SPINE.md.

Let me look at the delta-spec skill and the significance-routing skill and adr-authoring skill to follow the repo's conventions. Also I should understand the OpenSpec structure — there's a mention of OpenSpec but no openspec/ directory in the repo. So this repo uses ADR + spine prose, not OpenSpec deltas.

Let me read the key skills to understand the proper methodology. The most relevant skills to load:
1. `significance-routing` — to compute significance score and route
2. `adr-authoring` — to write the ADR properly (with template)
3. `delta-spec` — to understand how brownfield changes are described
4. `nfr-design` — for NFR
5. `spine-contracts-gate` — for contract changes (openapi)
6. `readiness-gate` — criteria

Let me also read the RFP vendor file briefly, and check the adr template.

Actually, I already have enough context. Let me read the key skill files to follow methodology precisely. Let me load the most important ones: significance-routing, adr-authoring (with template), delta-spec, spine-contracts-gate, nfr-design.

Let me also check the remaining docs (vendor-rfp.md) briefly. And I should check whether there's an OpenSpec directory anywhere.

Actually the repo structure is clear. Let me focus on the methodology skills. I'll read several skills in parallel.

Let me first read the adr-template, significance-routing, delta-spec, nfr-design, spine-contracts-gate SKILL.md files.
Я изучил спайн, ADR, контракты, NFR и handoff-пакет. Теперь загружу методические скиллы, чтобы следовать принятой в репозитории дисциплине (значимость/маршрут, ADR, дельта-изменения, контрактный гейт, NFR).

  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.qwen/skills/nfr-design/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.qwen/skills/spine-contracts-gate/SKILL)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.qwen/skills/readiness-gate/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/.qwen/skills/spine-invariants/reference)`

Now let me read the remaining important skills: nfr-design, spine-contracts-gate, readiness-gate, and the spine-invariants skill. Also I want to check the vendor-rfp.md and the contracts gate skill. Let me also read the spine-contracts-gate and fitness skills.

Actually, let me focus. The task is clear. I need to produce an architectural package. Let me determine the proper methodology:

1. **Significance assessment**: The change is "recurring C2B debits by payer consent (subscriptions/автоплатежи)". This touches:
   - api_contract_change (new endpoints or modified contract)
   - financial_impact (recurring debits = money movement)
   - new datastore? (consent store, mandate store)
   - new_component? (scheduler, mandate manager)
   - consistency_model_change? (new state machine for consent/mandate)
   - security_boundary_change? (consent is a new sensitive data)
   - data_contract_change (consent/mandate data)
   - significant_nfr (scheduled debits, retry windows)
   - Possibly regulatory (115-ФЗ, 152-ФЗ for consent data)

This is clearly Critical path. Recurring debits are financial operations with payer consent (mandate) — a new financial primitive. This is Critical.

2. **How to change accepted decision files**: The repo uses ADR + spine prose. Changes go via:
   - New ADR-008 (Status: Proposed) for the recurring debit decision
   - New spine block AD-009 (Status: Proposed) — or extend
   - The spine Deferred section already has "C2C-переводы и выплаты" but not "автоплатежи". Actually solutioning.md lists автоплатежи as roadmap (вне scope). So I need to bring it into scope.

Wait — actually, let me check the spine "Deferred" section again. It lists:
- Мультивалютность...
- C2C-переводы и выплаты B2C/B2B: roadmap после стабилизации C2B
- Диспуты/претензии (disputes)...

But "автоплатежи" is NOT in the spine Deferred. It's only in solutioning.md roadmap. So the recurring debits are a NEW feature being brought into the C2B-приём scope.

The instruction says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — meaning: the accepted files (ARCHITECTURE-SPINE.md, ADR files) should only be changed via the repo's accepted way: ADR + spine blocks with status Proposed, not by directly editing ADOPTED blocks.

The key accepted files:
- ARCHITECTURE-SPINE.md: AD-008 is [ADOPTED]. I should NOT modify AD-008. Instead add AD-009 (Proposed) for the recurring debit invariant.
- docs/adr/*.md: add ADR-008 (Proposed).
- docs/contracts/tsp-api.md and openapi/tsp-api.yaml: this is "Spec" level (A1), version 0.1 draft. I can propose changes here (additive, non-breaking).
- docs/spec/state-machine.md: add consent/mandate state machine.
- docs/nfr.md: add NFR for recurring.

Now the question: should I actually EDIT files, or produce a package? The task says "Подготовь архитектурный пакет этого изменения поверх принятого решения" and "Код не пиши." and "Когда закончишь, кратко перечисли созданные и изменённые файлы."

So I DO need to create/modify files — the architectural package. This means:
1. New ADR-008 (recurring C2B / автоплатежи decision)
2. New spine block AD-009 (Proposed) in ARCHITECTURE-SPINE.md
3. Update the Deferred section / roadmap (remove автоплатежи from deferred, since now in scope)
4. New spec doc for consent/mandate state machine (docs/spec/recurring-mandate.md)
5. Contract changes: docs/contracts/tsp-api.md (additive sections) + openapi/tsp-api.yaml (additive endpoints)
6. NFR additions: docs/nfr.md
7. Maybe an impact assessment doc (docs/recurring-c2b/impact-assessment.md) and acceptance criteria + rollback.

But wait — I need to be careful. The task says "подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям." So the package should be presentable at A3 (human architecture decision) and then handoff to implementers.

Let me think about what's the most appropriate structure. Given the repo conventions:

The change is Critical path → full Solutioning. So I need:
1. Significance assessment (route)
2. Impact on accepted architecture (which invariants touched)
3. ADR with alternatives, consequences, reversibility
4. Contract changes (non-breaking)
5. Measurable NFR
6. Acceptance criteria + rollback plan
7. What remains for human architect

I should produce a focused "change package" in a dedicated directory to keep it self-contained and reviewable, plus the necessary edits to accepted files (spine gets a new Proposed block; ADR gets new Proposed record). 

Actually, let me reconsider. The instruction "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" is key. The accepted files are:
- ARCHITECTURE-SPINE.md (AD-001..008)
- docs/adr/ADR-001..007.md
- docs/solutioning.md (references the roadmap)
- docs/nfr.md, docs/contracts/*, docs/spec/*, openapi/*

The "accepted way" to change these:
- Spine: add new AD block with Status: Proposed (referencing the ADR), do NOT rewrite ADOPTED blocks.
- ADR: add new ADR-NNN with Status: Proposed.
- Contracts: additive changes preserving v0.1, or new version. Since contract is "0.1 draft", additive optional fields are backward compatible. Non-breaking.

Let me verify the delta_guard / delta-spec approach. The repo has a `delta_guard` MCP tool: "Гейт прямых правок спайна мимо дельты (модель 5.2): каждый изменённый файл под защищёнными путями (по умолчанию model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml...)". But the repo doesn't have model/ dir — it's prose-based. And CONSTRAINTS.yaml is under .arch-handoff/. So the delta_guard might flag ARCHITECTURE-SPINE.md edits. But there's no openspec/ directory. Hmm.

Actually, I think the cleanest and most correct approach given the repo's actual conventions (prose ADR + prose spine) is:

**Primary deliverable**: a new change package. Given the task, I'll create:

1. `docs/adr/ADR-008-recurrent-c2b-mandate.md` — the ADR (Status: Proposed) for recurring C2B debits via payer consent (mandate/подписка).
2. New spine block in `ARCHITECTURE-SPINE.md` — AD-009 (Proposed) for consent/mandate invariant.
3. Update `ARCHITECTURE-SPINE.md` Deferred section — remove автоплатежи implication (actually it's not there; but solutioning roadmap lists it). Actually I'll add a note.
4. `docs/spec/mandate-state-machine.md` — consent/mandate lifecycle state machine.
5. `docs/contracts/tsp-api.md` — additive sections for mandate/consent endpoints (non-breaking).
6. `openapi/tsp-api.yaml` — additive paths + schemas (non-breaking).
7. `docs/nfr.md` — additive NFR section for recurring.
8. A top-level change package doc: `docs/recurring-c2b/change-package.md` (or `docs/changes/...`) summarizing: significance/route, impact, acceptance criteria, rollback plan, human decision points.

Actually, to keep it reviewable and cohesive, I think a single change-package directory is better, PLUS the minimal edits to accepted files (spine new block + new ADR). Let me structure:

Option A (recommended): 
- Create `docs/changes/recurrent-c2b-debit/` directory containing:
  - `01-significance-and-route.md`
  - `02-impact-assessment.md`
  - `03-ADR-008-...md` (or link to docs/adr)
  - `04-contract-changes.md`
  - `05-nfr.md`
  - `06-acceptance-and-rollback.md`
  - `07-human-decisions.md`
- Plus edits: new ADR-008 in docs/adr/, new AD-009 in spine.

Hmm, but this might be over-structured. Let me think about what "архитектурный пакет" means here and what's most useful.

Actually, re-reading the task: "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям."

The 7 deliverables are the content requirements. I think the cleanest is:

1. **ADR-008** (the core decision, Proposed) — in `docs/adr/ADR-008-recurrent-c2b-mandate.md`, following the repo's ADR template and format exactly.

2. **Spine block AD-009** (Proposed) — added to `ARCHITECTURE-SPINE.md`.

3. **A change package document** — a single overview doc that ties together significance, impact, contract changes, NFR, acceptance/rollback, human decisions. This could be `docs/recurring-c2b-change.md` or in a `docs/changes/` folder.

4. **Contract updates** — `docs/contracts/tsp-api.md` and `openapi/tsp-api.yaml` (additive, non-breaking).

5. **NFR additions** — `docs/nfr.md`.

6. **State machine spec** — `docs/spec/mandate-state-machine.md`.

Let me reconsider scope to avoid over-engineering. The task explicitly lists 7 things that "should come out". I'll produce a comprehensive but cohesive package. Let me decide on a structure that maps cleanly to the 7 deliverables and the repo layout.

Proposed file structure (new/modified):

**Modified (accepted files, via accepted way):**
1. `ARCHITECTURE-SPINE.md` — add AD-009 block (Proposed), update Deferred/roadmap note.
2. `docs/nfr.md` — add section 7 "Рекуррентные C2B-списания" (additive).

**New files:**
3. `docs/adr/ADR-008-recurrent-c2b-mandate.md` — the ADR (Proposed).
4. `docs/spec/mandate-state-machine.md` — consent/mandate state machine.
5. `docs/contracts/tsp-api.md` — wait, this is an existing accepted file too (contract v0.1 draft). I should MODIFY it additively.

Actually `docs/contracts/tsp-api.md` and `openapi/tsp-api.yaml` are the "Spec" artifacts (A1 gate). They're draft (v0.1). The task explicitly asks for "Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей." So I should modify both the markdown contract doc and the OpenAPI YAML additively.

6. A top-level change package / index doc that has the 7 deliverables. I'll make it `docs/changes/recurrent-c2b-debits/README.md` or a single `docs/recurring-c2b-change-package.md`.

Actually, I realize I should keep this clean. Let me create a single change-package directory `docs/changes/recurrent-c2b/` with:
- `README.md` — the change package: significance/route, impact, summary of all decisions, acceptance criteria, rollback, human decision points (deliverables 1, 2, 6, 7).

And keep the ADR and spine and contracts in their canonical locations (ADR in docs/adr/, spine block in ARCHITECTURE-SPINE.md, contract in docs/contracts/ + openapi/, NFR in docs/nfr.md, spec in docs/spec/).

This respects "меняй только тем способом, который принят в репозитории" — ADR in docs/adr, spine in ARCHITECTURE-SPINE.md, contracts in canonical locations, and the package README as the presentation layer.

Let me finalize the plan. Before writing, let me quickly:
1. Read the remaining skills I'll rely on: nfr-design, spine-contracts-gate, readiness-gate (for acceptance criteria). Also maybe spine-invariants for the spine block format.
2. Read vendor-rfp.md briefly (not critical).
3. Check the spine-invariants template for the AD block format.

Actually I already know the spine AD block format from ARCHITECTURE-SPINE.md (Binds/Prevents/Rule). Let me read nfr-design and spine-contracts-gate and readiness-gate skills, and the spine-invariants reference template to be precise.

Let me also verify: are there spine MCP tools I should run to ground the significance score? I could use `significance_score` or `significance_from_diff`. Since I haven't made changes yet, `significance_from_diff` would show the current diff (just .qwen/settings.json, unrelated). Better to use `significance_score` with the 15 triggers manually, or just reason it out. Actually the task asks for "Оценка значимости изменения и маршрута" — I can use the `significance_score` MCP tool if it accepts trigger inputs, but its schema I'd need to review. Let me check its schema via tool_search.

Actually, let me be efficient. I'll read the remaining skills and check the significance_score tool schema in parallel.

  `tool_search(query="select:mcp__spine__significance_score,mcp__spine__spine_lint,mcp__spine__fitness_check,mcp__spine__openapi_lint,mcp__spine__trace_check")`

Now I have a full understanding of the methodology. Let me verify the spine MCP tools availability and check the significance_score tool. Actually, I'll use the spine MCP tools to ground the significance assessment and to validate my changes. Let me review the significance_score schema and the spine_lint, fitness_check schemas.

Actually, let me first check if there's an existing openspec/ directory or model/ directory (the delta_guard tool mentions model/). There isn't (from glob). The repo is prose-based.

Let me check the significance_score tool to see if it can compute a score from my trigger list. Let me use tool_search.

Actually, I think I have enough. Let me also verify the exact format for spine AD blocks by re-reading the ARCHITECTURE-SPINE.md format (I have it). The format is:

```
## AD-00X. <title>

- Status: Proposed (ADR-00X)
- **Binds**: ...
- **Prevents**: ...
- **Rule**: ...
```

Note AD-008 uses "Status: Adopted (A3 от 2026-08-15, ADR-007 Accepted)" and "**Binds**:" (bold). The earlier ones use plain "Status: Proposed (ADR-001)". I'll follow the dominant format (plain, no bold, matching AD-001..007).

Now let me plan the actual deliverables concretely.

## The change: recurring C2B debits (автоплатежи / подписки СБП)

Business context: ТСП (online cinemas, housing/ЖКХ, telecom) want recurring C2B debits by payer consent — SBP subscriptions. Today each payment requires QR + client action. 

Key domain concepts:
- **Согласие (consent/mandate)**: a payer authorizes a TSP to initiate recurring debits up to a max amount/frequency/period. In SBP terms, this is a "mandate" (поручение/согласие на списание).
- **Подписка (subscription/agreement)**: binding a consent to a specific TSP and payer.
- **Рекуррентный платёж (recurring debit)**: initiated by TSP without payer action, based on active consent.

In СБП, recurring C2B debits are done via the "C2B подписки/автоплатежи" mechanism. The technical mechanism involves:
- A consent/mandate registered in the ОПКЦ (НСПК) or via bank
- Recurring debit initiation without QR (a "C2B списание по согласию" — оплата по подписке/периодический платёж).

Actually, let me be careful about what's actually true about СБП. The real-world СБП has a "платежи по подписке" (recurring payments) mechanism — "C2B-подписки" via "СБП подписка" / автоплатежи. The exact protocol details are subject to [ТРЕБУЕТ ПРОВЕРКИ] from НСПК documentation. I should mark protocol-level details as such, consistent with the repo's approach.

So my ADR should NOT invent protocol details. I mark them [ТРЕБУЕТ ПРОВЕРКИ].

Key architectural decisions to make:

1. **Consent (mandate) as a first-class domain entity with its own state machine** — the consent lifecycle (PENDING → ACTIVE → CANCELLED/EXPIRED/REVOKED) is the source of truth for whether a recurring debit is allowed. This is a NEW state machine (or extends the existing one).

2. **Recurring debit reuses the existing payment state machine** — a recurring debit produces a payment that goes through CREATED→...→COMPLETED, BUT:
   - It's initiated by the TSP without QR, referencing an active consent.
   - The payment state machine's `QR_ISSUED` state doesn't apply — recurring debits don't need QR. So either a variant path or a separate "payment method = recurring" flag that skips QR_ISSUED and goes CREATED → (debit initiated in НСПК) → PAID.
   - This touches AD-005 (зачисление только из PAID) — still holds: debit confirmation = PAID.

3. **Scheduler**: recurring debits are time-based. TSP requests a debit (on a billing date) OR bank has a scheduler that triggers them. Decision: TSP-initiated (pull) vs bank-scheduled (push). For СБП автоплатежи, typically TSP initiates each debit (on the billing date) referencing the consent. So the shлюз provides "create recurring debit" endpoint that TSP calls. No internal cron scheduler needed (that's the TSP's job). But we may need a scheduler for consent expiry and for "mandate status sync".

4. **Consent storage & security**: consent contains payer PII (consent to debit from payer's account). This is sensitive data (152-ФЗ). Storage in the gateway DB with encryption, minimization. Actually, does the consent store payer's account/bank details? In СБП, the payer's account is identified via the payer's bank, and the debit authorization is anchored to the payer's consent registered in НСПК (or via bank's "СБП-подписка"). The exact mechanism [ТРЕБУЕТ ПРОВЕРКИ].

5. **Idempotency**: recurring debit needs idempotency — a TSP could retry a debit; must not double-debit. Reuse Idempotency-Key + paymentId. Plus consent-scoped limits (max amount, period) must be enforced atomically.

6. **Revocation / cancellation**: payer can revoke consent (in their bank app, or via НСПК). This must propagate to the gateway and stop future debits immediately. This is a new inbound event (consent revoked).

7. **Regulatory**: recurring debits are financial + PII → still Critical, same AD-006/AD-007 invariants apply. New: consent revocation right (отзыв согласия), 152-ФЗ for consent data.

8. **Settlement flow**: recurring debit confirmation → зачисление in АБС → CREDITED → COMPLETED. Same as one-time, but triggered differently.

Now the key architecture decision (the ADR) is: **how to model consent + recurring debit in the existing C2B gateway**:
- Option A: Consent as separate entity + recurring debit as a variant of payment (paymentType=recurring, skips QR).
- Option B: Extend payment state machine with new states (rejected: pollutes the QR-centric model).
- Option C: Separate "subscription service" component (rejected: over-engineering, reuses gateway).

The recommended decision: **Option A** — consent (mandate) as a first-class entity with its own state machine + recurring debit reuses the payment machine with a `paymentType=recurring` that binds to consentId and skips QR_ISSUED (or goes through a parallel "debit" branch). 

This is the cleanest because:
- Reuses AD-002/AD-005 invariants (зачисление только из PAID, атомарные переходы, идемпотентность).
- Doesn't break existing one-time flow.
- Adds one new invariant: "списание возможно только по активному согласию" (recurring debit must reference an ACTIVE consent, and cumulative/periodic limits enforced atomically).

Now for spine AD-009 (Proposed): "Рекуррентные списания — только по активному согласию". Rule: recurring debit created only referencing consent in state ACTIVE; limits enforced in the same transaction; revocation stops future debits immediately.

Let me now also think about what stays for the human architect (deliverable 7):
1. Business/legal: consent model details (who registers consent — ТСП vs банк vs плательщик; where the mandate is stored — НСПК vs банк; legal form of consent under 161-ФЗ/ГК). This needs legal + product sign-off, not architecture.
2. Exact НСПК recurring-debit protocol — external input [ТРЕБУЕТ ПРОВЕРКИ].
3. Whether recurring is in first wave or later (scope/roadmap priority) — business.
4. Commission/tariff model for recurring debits (affects reporting) — business.
5. Consent revocation UX and where payer manages subscriptions (bank app vs ТСП) — product.
6. AML/fraud thresholds for recurring debits — risk.
7. Whether to enforce a bank-side scheduler vs TSP-initiated only — this is an architectural decision I'll make in the ADR (TSP-initiated with bank-side safety), but the human confirms.

Actually the human A3 decision should be crisp: the ADR-008 decision (recurring as variant + consent entity) gets a machine-readable A3 package like ADR-007 did. The human decision points are those that can't be resolved by architecture: legal form of consent, НСПК protocol, wave priority, tariffs.

Now, let me also determine the significance score. Using the 15 triggers:

For recurring C2B debits:
1. `financial_impact` — YES (money moves without payer action per debit; risk of unauthorized debit).
2. `api_contract_change` — YES (new endpoints for consent/mandate + debit).
3. `data_contract_change` — YES (consent/mandate entity, new data).
4. `security_boundary_change` — possibly (consent = new sensitive PII; revocation channel from НСПК). This is a critical trigger.
5. `consistency_model_change` — YES (new consent state machine, cross-entity invariant: consent ACTIVE ↔ debit allowed).
6. `significant_nfr` — YES (scheduling windows, debit throughput peaks at billing dates).
7. `new_component` — maybe (mandate/consent manager; but it's within the gateway — I'd argue it's a new logical component, not a new container). Borderline.
8. `cross_domain_integration` — YES (consent revocation from payer bank/НСПК; AML).
9. `new_datastore` — no (reuse gateway DB; consent is a new table, not new store).
10. `rto_rpo_targets` — no change (same RPO=0/RTO≤1h).
11. `criticality_or_exception` — the base gateway is already Critical; recurring is financial + PII.

So score is clearly ≥5, and it includes security_boundary_change (consent data / revocation boundary) → **Critical** route.

So: **Critical** (значимость ≥5, содержит financial_impact + api_contract_change + data_contract_change + consistency_model_change + security_boundary_change). Full Solutioning → ADR + spine + NFR + human A3 + walking skeleton.

This aligns with the existing repo: base is Critical 11/15, recurring is also Critical.

Now let me write everything. I'll be thorough but concise.

Let me first run the spine tools to validate my current understanding and prepare ground truth:
- spine_lint on ARCHITECTURE-SPINE.md (to see current lint state)
- fitness_check (to see current gate)
- Actually, more useful: after I write, run spine_lint and fitness_check to verify my changes don't break the gate.

But I should check the significance_score tool — let me see if it's worth calling. Let me use tool_search to review the significance_score and spine_lint schemas.

Actually, I'll be pragmatic. The significance_score MCP tool likely needs trigger inputs. Let me check its schema quickly via tool_search, plus spine_lint, fitness_check, openapi_lint, trace_check.

  `tool_call(name="mcp__spine__significance_score", arguments={"triggers": {"financial_impact": true, "api_contract_change": true, "data_contract_change": true, "consistency_model_change": true, "securi)`
  `tool_call(name="mcp__spine__spine_lint", arguments={"path": "<HARNESS>/runs-clean/cells/wwd3ti3/ws/ARCHITECTURE-SPINE.md"})`
  `tool_call(name="mcp__spine__fitness_check", arguments={"path": "<HARNESS>/runs-clean/cells/wwd3ti3/ws"})`

Let me run the significance_score tool and also run spine_lint and fitness_check and trace_check to establish baseline before making changes.

Let me first run significance_score with the triggers I identified.

  `write_file(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisa, content="# ADR-008. Рекуррентные C2B-списания (автоплатежи/подписки СБП): согласие как сущность первого класса, переиспользование статусной машины п)`

Baseline established:
- significance_score: **Critical, score 7** (fired: api_contract_change, consistency_model_change, cross_domain_integration, data_contract_change, financial_impact, security_boundary_change, significant_nfr).
- spine_lint: passed (0 issues).
- fitness_check: passed (0 issues).

Now let me plan and write the deliverables. I'll present a plan first, then write files.

Actually, given the task is clear and I've done thorough investigation, I don't need to enter plan mode (user didn't ask for it). I'll proceed to produce the architectural package.

Let me determine the concrete files to create/modify:

**Modified (accepted files — via accepted way):**
1. `ARCHITECTURE-SPINE.md` — add AD-009 block (Status: Proposed), update Deferred section to note автоплатежи are now being brought into scope (the Deferred currently doesn't list автоплатежи explicitly, but solutioning.md roadmap does; I'll add a small note). Actually, I should add AD-009 and update the header/scope note. Let me be careful not to touch ADOPTED blocks.

2. `docs/nfr.md` — add section "8. Рекуррентные C2B-списания (автоплатежи)" with measurable NFRs.

3. `docs/contracts/tsp-api.md` — add additive sections for consent/mandate + recurring debit (new endpoints, non-breaking, in a new section or extended methods).

4. `openapi/tsp-api.yaml` — add additive paths + schemas (non-breaking).

**New files:**
5. `docs/adr/ADR-008-recurrent-c2b-mandate.md` — the ADR (Proposed).

6. `docs/spec/mandate-state-machine.md` — consent/mandate state machine + recurring debit lifecycle.

7. `docs/changes/recurrent-c2b-debits/README.md` — the change package (significance/route, impact assessment, acceptance criteria, rollback, human decisions). This is the "package" summary that ties everything and can be presented at A3.

Actually, maybe I should put the change package as a single document rather than a directory. But a directory allows a clear index. Let me think about what's cleanest and matches repo conventions (which use flat files in docs/ subdirs).

I'll create:
- `docs/changes/recurrent-c2b/` — new directory with the change package. Inside:
  - `README.md` — index + the 7 deliverables summary (significance/route, impact, human decisions, acceptance/rollback). Actually, I'll make it a single cohesive doc.

Hmm, let me reconsider. The 7 deliverables map to:
1. Significance + route → in the change package README (and grounded by significance_score=7 Critical).
2. Impact on accepted architecture → change package README + spine AD-009.
3. ADR with alternatives/consequences/reversibility → docs/adr/ADR-008.
4. Contract changes → docs/contracts/tsp-api.md + openapi/tsp-api.yaml (+ change package notes).
5. Measurable NFR → docs/nfr.md section.
6. Acceptance criteria + rollback plan → change package README (+ possibly a dedicated doc).
7. Human architect decisions → change package README.

To keep the package cohesive and presentable, I'll structure the change package as a single directory `docs/changes/recurrent-c2b-debits/` containing:
- `README.md` — the full change package (deliverables 1, 2, 6, 7, and cross-references to 3, 4, 5).

And put the "source of truth" artifacts in their canonical locations (ADR, spine, contract, NFR, spec).

This is clean. Let me finalize.

Actually, wait — let me reconsider whether to modify `docs/solutioning.md`. It lists "автоплатежи" in the roadmap (вне scope). I should update that roadmap line to reference the new change package. But solutioning.md is an accepted decision file. Modifying it is fine as long as I do it additively/minimally — update the roadmap to point to the new change package, and update the "Разбиение на решения" table? No, I shouldn't over-edit. I'll add a note in solutioning.md section 1 (roadmap) that автоплатежи are now covered by ADR-008 / change package. Actually, minimal: update the roadmap line to link the new change package. And maybe add a row to the ADR table. But that's a bit invasive.

Let me keep the edits focused:
- ARCHITECTURE-SPINE.md: add AD-009 + note in Deferred about автоплатежи now in scope (pointing to ADR-008).
- docs/nfr.md: new section.
- docs/contracts/tsp-api.md: new endpoints (additive).
- openapi/tsp-api.yaml: new paths/schemas (additive).
- docs/adr/ADR-008: new ADR.
- docs/spec/mandate-state-machine.md: new spec.
- docs/changes/recurrent-c2b-debits/README.md: the package.

I'll also update docs/solutioning.md roadmap line minimally to reference the change (since it explicitly lists автоплатежи as out-of-scope, and now we're bringing it in — leaving it stale would be wrong). I'll make a small, precise edit.

And README.md at root — maybe add a pointer to the change package. Optional. I'll add a brief line to keep the repo navigable. Actually, minimal edits are better; I'll skip root README unless needed. Actually the root README says "Статус: решение подготовлено, ожидает человеческого решения A3". Adding a pointer to the new change package would help navigability. I'll add one line.

Let me now write the content. I need to be careful and precise.

Let me define the domain model precisely:

### Согласие (Consent / Mandate)

**Consent** — согласие плательщика на рекуррентные C2B-списания в пользу конкретного ТСП. Поля:
- `consentId` (id шлюза)
- `tspId`
- payer identity (минимизировано: идентификатор плательщика в СБП — как НСПК определяет плательщика [ТРЕБУЕТ ПРОВЕРКИ]; возможно, телефон/счёт, но минимизируем ПДн)
- `maxAmount` (максимальная сумма одного списания, копейки)
- `maxAmountPerPeriod` + `period` (лимит за период — day/week/month) [опционально]
- `status`: PENDING → ACTIVE → (CANCELLED | EXPIRED | REVOKED | SUSPENDED)
- `expiresAt` (срок действия согласия)
- `createdAt`, `revokedAt`

### Подписка/мандат (Mandate)

In СБП, the "мандат" may be registered in НСПК. So the consent has a dual existence: bank-side (gateway) + НСПК-side (mandate id in ОПКЦ). The consentId is the gateway's source of truth; the mandate registration in НСПК is via the ОПКЦ adapter (like TSP registration). I'll mark the НСПК mandate mechanism [ТРЕБУЕТ ПРОВЕРКИ].

### Рекуррентный платёж (Recurring debit)

A payment created with `paymentType=recurring`, referencing `consentId`. Skips QR. Goes:
- `CREATED` → (debit submitted to НСПК via adapter) → `PAID` (confirmed) → `CREDITED` → `COMPLETED`.
- No `QR_ISSUED`/`EXPIRED` in the recurring branch (or EXPIRED could apply if the debit window passes).

Actually, to keep the payment state machine clean, I'll define the recurring debit as using the SAME payment states but with a distinct path that skips QR_ISSUED. The state machine spec already has states CREATED → QR_ISSUED → PAID... So for recurring, T1 (CREATED) then a new transition CREATED → PAID (debit confirmed) without QR_ISSUED.

This is the key "impact on accepted architecture" — AD-005 still holds (зачисление только из PAID), AD-002 (atomic transitions) holds, AD-003 (idempotency) holds with new keys (consentId for consent creation, paymentId for debit).

### New inbound event: consent revocation

Payer revokes consent (in their bank / НСПК). Gateway receives a `consent.revoked` event → consent → REVOKED → future debits blocked (guard on consent status).

### Key invariants (new spine AD-009):

**AD-009. Рекуррентное списание — только по активному согласию**
- Binds: согласие (consent), статусная машина платежа, адаптер ОПКЦ, АБС-адаптер.
- Prevents: списание без согласия; превышение лимитов согласия; списание после отзыва согласия; двойное списание при ретрае ТСП.
- Rule: Рекуррентный платёж создаётся только если есть согласие в статусе ACTIVE; сумма и период проверяются по лимитам согласия в той же транзакции, что и создание платежа; отзыв согласия (REVOKED/CANCELLED/EXPIRED) делает невозможным создание новых списаний. Fitness: попытка списания по REVOKED-согласию недостижима.

This is a new invariant that Binds the new consent entity and Prevents unauthorized debits.

Now let me write all the files. I'll start with the ADR (the core), then spine block, then spec, then contract, then NFR, then the change package README.

Let me write the ADR-008 following the template exactly.

For the ADR, I need:
- Title: ADR-008. Рекуррентные C2B-списания (автоплатежи/подписки СБП): согласие как сущность первого класса + переиспользование статусной машины платежа
- Date: 2026-09-28 (today)
- Status: Proposed
- Owner: solution-architect (платёжный контур)
- Related: ADR-002, ADR-004, ADR-005, ADR-006, AD-002, AD-003, AD-005, AD-009

Context, Decision, Alternatives, Consequences, Reversibility, References.

Let me write it thoroughly.

I'll also need to update the ADR table in solutioning.md? I'll do minimal — actually, let me not touch solutioning.md's table (it's a "Разбиение на решения" for ADR-001..007). I'll just update the roadmap line in section 1 to reference the new change. Actually, simpler: add a note in the "Открытые вопросы" or just update roadmap. Let me update section 1's roadmap line: "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." → change "автоплатежи" to point to ADR-008. I'll edit precisely.

Actually, let me reconsider the scope of edits to solutioning.md. The minimal correct change: the roadmap line currently says автоплатежи is "вне scope". Now it's being brought into scope as a change package. I'll edit that line to reflect "автоплатежи — см. ADR-008 (в разработке)". This is a small, correct, additive edit.

Let me now also verify: should I run the OpenAPI lint after editing openapi/tsp-api.yaml? Yes, I should. And re-run spine_lint + fitness_check after edits.

Let me also run trace_check to understand the current traceability state (it may complain about AD without CMP etc. since there's no model/ dir). Actually trace_check requires "каталог с model/" — there's no model/ dir in this repo. It might error or return nothing. I'll skip trace_check since the repo is prose-based (no model/ directory), and it's not part of the accepted gate here (CONSTRAINTS.yaml is prose file_exists/must_contain rules).

Let me proceed to write files now.

First, let me write the ADR-008. I need a good filename following the repo's convention (lowercase, descriptive, transliterated). Existing: `ADR-005-integraciya-s-abs-...`, `ADR-007-proposed-a3`. So I'll use: `ADR-008-rekurrentnye-c2b-spisaniya-soglasie-i-mandat.md`.

Let me draft the ADR content carefully.

Actually, let me think about the decision more rigorously, considering the alternatives properly.

**Decision options for recurring C2B:**

The core question: how to add recurring debits to the existing C2B gateway.

Option A: **Согласие (mandate) как отдельная сущность + рекуррентный платёж как вариант существующего платежа** (paymentType=recurring, пропуск QR_ISSUED). Consent has its own state machine. Recurring debit reuses payment machine, зачисление только из PAID (AD-005). [RECOMMENDED]

Option B: **Полностью отдельный сервис «Подписки»** со своей БД и статусной моделью. Плюсы: изоляция. Минусы: дублирование статусной машины, outbox, сверки, АБС-адаптера; второй источник истины; рост стоимости владения.

Option C: **Расширить статусную машину платежа новыми состояниями** (например, SUBSCRIPTION_ACTIVE). Минусы: засоряет QR-центричную модель, ломает инварианты AD-002/AD-005, смешивает жизненный цикл подписки и платежа.

Option D: **Внешний сервис ТСП держит согласие, шлюз просто выполняет списание по «одноразовой ссылке» каждый раз** — т.е. не хранить согласие в шлюзе вообще, ТСП каждый раз создаёт обычный платёж, а согласие хранится у ТСП. Минусы: шлюз не контролирует лимиты/отзыв, нарушение AD-001 (финансовая логика в произвольных сервисах), невозможно гарантировать «только по активному согласию», регуляторный риск.

Actually, option D is important — it's the "ТСП сам управляет подпиской" option. The key architectural insight is that consent MUST live in the bank's control (gateway) to enforce the invariant "debit only by active consent" — otherwise the gateway can't independently guarantee compliance. This ties to AD-001 (финансовая логика в контуре банка).

I'll pick Option A and clearly reject B/C/D.

Now for the consent lifecycle, let me define states:
- `PENDING` — consent created, awaiting НСПК mandate registration/confirmation (or payer confirmation).
- `ACTIVE` — consent active, debits allowed.
- `SUSPENDED` — temporarily blocked (e.g., AML hold, failed debit attempts).
- `EXPIRED` — expiresAt reached.
- `CANCELLED` — ТСП cancelled (e.g., subscription ended).
- `REVOKED` — payer revoked consent.

Terminal: EXPIRED, CANCELLED, REVOKED. SUSPENDED is reversible → ACTIVE.

Transitions:
- PENDING → ACTIVE (НСПК подтвердил мандат / payer confirmed)
- PENDING → CANCELLED (ТСП/банк отклонил)
- ACTIVE → SUSPENDED (AML-hold, or repeated failed debits)
- SUSPENDED → ACTIVE (hold lifted)
- ACTIVE → EXPIRED (expiresAt)
- ACTIVE → CANCELLED (ТСП)
- ACTIVE → REVOKED (payer / НСПК)

Invariant: recurring debit allowed ONLY from ACTIVE.

Now the recurring debit lifecycle (payment machine):
- `CREATED` (debit requested by ТСП with consentId) → `PAID` (НСПК confirmed debit) → `CREDITED` → `COMPLETED`.
- `CREATED` → `FAILED` (НСПК rejected debit, e.g., insufficient funds / consent not found in НСПК).
- No `QR_ISSUED`/`EXPIRED` on the recurring path (though a debit could time out → FAILED or a "retry later" state; but keep it simple: the ТСП re-initiates).

Wait, is EXPIRED meaningful for recurring? A debit attempt might have a deadline. But let me keep it minimal and mark protocol timing [ТРЕБУЕТ ПРОВЕРКИ].

Now, the payment machine currently has `PAID → CREDITED → COMPLETED`. For recurring, the same holds. Good.

Let me also think about idempotency keys for the new entities:
- Consent creation: `Idempotency-Key` → consentId (24h mapping).
- Recurring debit: `Idempotency-Key` → paymentId. Plus consentId + a "debit reference" so ТСП doesn't double-debit the same billing period. I'll add an optional `debitReference` (e.g., billing period id) that the ТСП provides, and the gateway enforces idempotency by (consentId + debitReference) → unique paymentId. This prevents double debit for the same billing period even without Idempotency-Key.

That's a good, concrete design point: **idempotency by (consentId, billingReference)**.

Now the НСПК side: the mandate/consent needs to be registered with НСПК. The ОПКЦ adapter gets new operations:
- `registerMandate` (consent registration in ОПКЦ)
- `createRecurringDebit` (debit initiation referencing the mandate) — or reuse `createPaymentLink` with a mandate flag.
- `revokeMandate` / notify revocation.

I'll note these as additive to the ОПКЦ adapter contract, marked [ТРЕБУЕТ ПРОВЕРКИ].

Now let me write everything. Let me be efficient and write the files.

Let me start writing. I'll write the ADR first.

For dates, today is 2026-09-28.

Let me write ADR-008.
Контур готов: значимость **Critical (score 7)**, спайн и fitness-гейт сейчас зелёные (baseline). Теперь сформирую архитектурный пакет. Начну с ядра — нового ADR, затем спайн-инвариант, спеку, контракты, NFR и сводный пакет изменения.

  `edit(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/ARCHITECTURE-SPINE.md", old_string="---\n\n## Deferred (с причиной и условием возврата)", new_string="## AD-009. Рекуррентное списание — только по активному согласию\n\n- Status: Proposed (ADR-008)\n- **Binds**: согласие (consent/мандат), ст)`

Now add the AD-009 spine block to ARCHITECTURE-SPINE.md. I need to insert it after AD-008 and before the Deferred section. Let me read the exact text around there to do a precise edit.

The current spine ends with AD-008 block, then:

```
## Deferred (с причиной и условием возврата)

- **Мультивалютность и иностранные платёжные системы**: ...
- **C2C-переводы и выплаты B2C/B2B**: roadmap после стабилизации C2B; ...
- **Диспуты/претензии (disputes)**: ...
```

I'll insert AD-009 before "## Deferred". Let me do the edit.

I'll add the new block. Following the format of AD-001..007 (plain "Status: Proposed (ADR-00X)").

Also, I should update the Deferred section to note автоплатежи are now brought into scope (they weren't explicitly in Deferred, but solutioning.md listed them). Actually the spine Deferred doesn't list автоплатежи. But to be safe and clear, I'll add a note. Actually, I'll keep Deferred unchanged (it correctly doesn't list автоплатежи), but I might add a note in the header scope line or leave it. The header says "Платёжный шлюз СБП (C2B-приём)". Recurring C2B is still C2B-приём, so no header change needed.

Actually, let me add a short note at the top of the Deferred section or after AD-009 clarifying the scope change. Simpler: just add AD-009. The ADR and change package will carry the scope context.

Let me do the precise edit to insert AD-009 before "## Deferred".

  `write_file(content="# Статусные машины согласия и рекуррентного списания — спецификация переходов\n\n- Status: Draft (для ревью на гейте A1; связано с ADR-008), file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/spec/mandate-state-machine.md")`

The spine block is added. There's a minor inconsistency: AD-008 uses "**Binds**:" with bold, but AD-001..007 use plain "**Binds**:" — wait, let me check. Looking back at the original spine:

AD-001: `- **Binds**: ...` — yes, they ALL use `**Binds**:` (bold). And AD-008 also uses `**Binds**:`. So my AD-009 uses `**Binds**:` consistently. Good.

Wait, let me re-check. The original AD-001 to AD-007 all use `**Binds**:` (bold). AD-008 uses `**Binds**:`. My AD-009 uses `**Binds**:`. Consistent. Good.

Now let me verify the spine lints clean. Actually, let me continue writing the other files first, then run all validations at the end.

Next: the mandate state machine spec (docs/spec/mandate-state-machine.md).

  `edit(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/contracts/tsp-api.md", old_string="```json\n{\n  \"tspId\": \"tsp_9f3c2a1b\",\n  \"amount\": 149990,                // копейки, int\n  \"currency\": \"RUB\",\n  \"qrType\": \, new_string="```json\n{\n  \"tspId\": \"tsp_9f3c2a1b\",\n  \"amount\": 149990,                // копейки, int\n  \"currency\": \"RUB\",\n  \"qrType\": \)`

Now update the contract. Let me update `docs/contracts/tsp-api.md` (additive) and `openapi/tsp-api.yaml` (additive).

For the contract doc, I'll add:
- New section for consents (methods: create consent, get consent, cancel consent, list?).
- Extend §3.2 payment with `paymentType` and `consentId`/`billingReference` optional fields.
- Add recurring-specific notes.

Let me read the exact current content of the tsp-api.md sections to do precise edits. I already have it. Let me do targeted edits.

For the contract doc, I'll:
1. Modify §3.2 request schema to add `paymentType`, `consentId`, `billingReference` (optional, backward-compatible).
2. Add new §3.6 "Согласие (consent/мандат)" methods.
3. Update webhook events to add consent events.

Let me be careful and precise. Let me edit §3.2's request JSON first.

Current §3.2 request:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "amount": 149990,                // копейки, int
  "currency": "RUB",
  "qrType": "dynamic",             // dynamic | static | link
  "paymentPurpose": "Заказ № 12345",
  "ttlSeconds": 900,               // опц.; лимит — по НСПК [ТРЕБУЕТ ПРОВЕРКИ]
  "redirectUrl": "https://merchant.example.com/order/12345/return",
  "merchantOrderId": "order-12345" // опц., сквозной для ТСП
}
```

I'll add fields:
```json
  "paymentType": "one_time",        // опц.; one_time (default) | recurring
  "consentId": "cs_…",              // обязателен при paymentType=recurring
  "billingReference": "bill-2026-09" // опц.; ключ дедупликации списания за период (recurring)
```

And add rules for recurring.

Then add a new section after §3.5 (Статус возврата) for consent methods.

Let me also update §3.3 status (payment status for recurring has no QR_ISSUED/EXPIRED; but the enum in response stays the same; I'll note it).

Let me do these edits carefully.

Actually, let me reconsider the paymentType values. The repo uses `qrType: dynamic | static | link`. For recurring, I'll add `paymentType: one_time | recurring`. Default `one_time` when absent (backward compatible).

Let me edit the contract doc §3.2 request.

  `edit(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/contracts/tsp-api.md", old_string="Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (AD, new_string="Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (AD)`

Now I need to add rules for recurring after the "Правила:" line in §3.2, and add a new section for consent methods. Let me look at the exact text around the "Правила" paragraph of §3.2.

Current (from earlier read):
```
Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (ADR-002). Максимальная сумма — по лимитам НСПК [ТРЕБУЕТ ПРОВЕРКИ].
```

I'll add a paragraph about recurring rules.

  `edit(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/contracts/tsp-api.md", new_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n, old_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n)`

Now add a new section for consent methods. I'll insert after §3.5 (Статус возврата) and before §4 (Ошибки). Let me find the exact text.

Current §3.5:
```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`

## 4. Ошибки (RFC 9457, Problem Details)
```

I'll insert a new §3.6 for consents between §3.5 and §4.

  `edit(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/contracts/tsp-api.md", new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`

Now update the webhooks section (§5) to add consent events, and update the error codes to include recurring-specific codes. Let me look at §5 webhook events and error codes.

Current §5 events:
- `payment.completed`
- `payment.failed`
- `payment.expired`
- `refund.completed` / `refund.failed`

I'll add:
- `consent.activated`
- `consent.expired`
- `consent.cancelled`
- `consent.revoked`

And error codes: add `CONSENT_NOT_ACTIVE` (422), `CONSENT_LIMIT_EXCEEDED` (422), `CONSENT_NOT_FOUND` (404), `BILLING_REFERENCE_CONFLICT` (409 or reuse idempotency). Actually billingReference conflict should return the existing payment (200), not error. So I'll add `CONSENT_NOT_ACTIVE`, `CONSENT_LIMIT_EXCEEDED`, `CONSENT_NOT_FOUND`.

Let me edit the webhook events list and error codes.

  `edit(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/contracts/tsp-api.md", new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`
  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.1.0\npaths:\n  /v1/payments:\n    post:\n      operationId: createPayment\, file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/openapi/tsp-api.yaml")`

Now update the OpenAPI YAML additively. The current openapi/tsp-api.yaml has:
- POST /v1/payments
- GET /v1/payments/{paymentId}
- PaymentRequest schema: required [amount, merchantOrderId]
- Payment schema

I'll add:
- POST /v1/consents
- GET /v1/consents/{consentId}
- POST /v1/consents/{consentId}/cancel
- Add paymentType/consentId/billingReference to PaymentRequest (optional)
- Add Consent, ConsentRequest schemas

Let me read the current openapi file exactly to do a clean rewrite (it's small enough).

I already have the full content:
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

I'll rewrite it to add the new paths and schemas. Since it's small, I'll use write_file to replace it entirely (I already read it, so overwrite is fine).

Actually, I should use edit to be safe, but a full rewrite via write_file is cleaner and I've already read the file. Let me write the full new version.

Note: the version stays 0.1.0 (additive, non-breaking). I'll keep it. Actually, contract_diff would compare versions; keeping 0.1.0 with additive changes is fine (no breaking changes). Good.

Let me write the full OpenAPI.

I need to add:
- paths:
  - /v1/payments (post) — keep, add paymentType etc to PaymentRequest
  - /v1/payments/{paymentId} (get) — keep
  - /v1/consents (post)
  - /v1/consents/{consentId} (get)
  - /v1/consents/{consentId}/cancel (post)
- schemas:
  - PaymentRequest: add paymentType, consentId, billingReference
  - Payment: keep (status enum same)
  - ConsentRequest
  - Consent

Let me write it.

  `edit(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/nfr.md", new_string="## 7. Рекуррентные C2B-списания (автоплатежи/подписки) — ADR-008\n\nЦели аддитивны к базовым NFR (разделы 1–6); рекуррентные операции насле, old_string="## Зависимости (внешние входы для NFR)")`

Now update docs/nfr.md with a new section for recurring C2B debits. Let me read the end of nfr.md to append. I have the full content already. The doc ends with "## Зависимости (внешние входы для NFR)". I'll add a new section "## 7. Рекуррентные C2B-списания (автоплатежи)" before the "Зависимости" section, or after section 6. Let me insert after section 6 (Наблюдаемость) and before "Зависимости".

Actually the sections are numbered 1-6. I'll add section 7 "Рекуррентные C2B-списания" before "## Зависимости".

Let me do a precise edit.

  `write_file(content="# Изменение: рекуррентные C2B-списания (автоплатежи/подписки СБП)\n\nПакет изменения поверх принятого решения «Платёжный шлюз СБП (C2B-приё, file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/changes/recurrent-c2b-debits/READM)`

Now create the change package README in docs/changes/recurrent-c2b-debits/. This is the presentation layer that ties everything: significance/route, impact, acceptance criteria, rollback plan, human decisions.

Let me write it comprehensively. It should reference the ADR, spine, spec, contract, NFR files.

Let me structure it:
1. Суть изменения
2. Оценка значимости и маршрута (score 7 Critical, with triggers)
3. Влияние на принятую архитектуру (затронутые инварианты, что меняется/нет)
4. Архитектурное решение (резюме ADR-008)
5. Изменения контрактов (резюме, non-breaking)
6. NFR (резюме)
7. Критерии приёмки (EARS)
8. План отката
9. Что остаётся на решение человека-архитектора
10. Readiness-вердикт (CONCERNS, with gaps)
11. Список файлов

Let me write it.

For the impact assessment, I need to be precise about which invariants are touched:

- AD-001 (изоляция платёжного контура): **не меняется**, но расширяется Binds — согласие живёт в контуре шлюза (подтверждает).
- AD-002 (единый источник истины — статусная машина): **расширяется** — добавляется машина согласия; правило атомарности распространяется на неё.
- AD-003 (идемпотентность): **расширяется** — новые ключи (consentId, billingReference).
- AD-004 (единственный адаптер ОПКЦ): **не меняется**, но адаптер получает новые операции (mandate).
- AD-005 (зачисление только из PAID): **не меняется** — это ключевой момент.
- AD-006 (trust-зоны): **не меняется**, но согласие = новые ПДн.
- AD-007 (НПС/КИИ/ПДн): **не меняется**, но расширяется поверхность ПДн (согласия).
- AD-008 (гибрид): **не меняется**.
- AD-009: **новый инвариант**.

So: touched = AD-002, AD-003 (расширяются); AD-001, AD-004, AD-005, AD-006, AD-007, AD-008 — не меняются, но расширяется сфера применения. New AD-009.

What changes: new consent entity + machine; payment gets paymentType; adapter gets mandate ops; contract additive; NFR additive.
What doesn't change: зачисление из PAID (AD-005), outbox pattern, сверка, АБС-адаптер, гибридная стратегия, trust-зоны.

Let me write the acceptance criteria in EARS notation and rollback plan.

Rollback plan:
- Pre-production: don't enable; feature flag.
- Feature flag: `recurring_debits_enabled` per TSP. Before launch: off. Rollback = disable flag + block new consents. Existing one-time payments unaffected.
- After launch: disable flag (stop-new) → no new consents/debits; already-created debits complete normally; consents remain (data retained, no reverse migration). Rolling release rollback.
- Emergency: DLQ + runbook; consent reconciliation stops debits on revoked-at-НСПК-but-active-here.
- Signal for rollback: double debit, debit on revoked consent, reconciliation mismatch, debit throughput exceeding NFR, AML/fraud alerts.
- Owner: платёжный контур + дежурная смена.

Human architect decisions (deliverable 7):
1. Юридическая форма согласия и порядок отзыва (ГК, 161-ФЗ) — комплаенс/юристы, не архитектура.
2. Где хранится мандат — НСПК vs банк (влияет на синхронизацию; зависит от документации НСПК) — внешний вход.
3. Волна запуска (сразу ли recurring или после стабилизации одноразовых) — бизнес/roadmap.
4. Тарифы/комиссии по рекуррентным списаниям — бизнес (влияет на отчётность).
5. Пороги AML/антифрод для рекуррентных (серия списаний = риск) — риск-подразделение.
6. UX отзыва согласия плательщиком (где: банковское приложение vs ТСП) — продукт.
7. Подтвердить A3-выбор ADR-008 (choice + constraints + rejected options).

Also the readiness verdict: CONCERNS, with gaps (НСПК протокол, юридическая форма, AML-пороги, тарифы, отзыв UX). These are external inputs, so the gate is CONCERNS (can start design but not implementation of НСПК-specific parts).

Let me write the change package README.

Actually, I want to also note the significance score grounding: score=7 (from significance_score tool). Fired triggers list.

Let me write the file.

  `edit(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/docs/solutioning.md", new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop, old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop)`

Now update docs/solutioning.md roadmap line to reference the new change package (since it explicitly lists автоплатежи as out-of-scope). Let me do a precise edit.

Current section 1 line:
"Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

I'll update "автоплатежи" → reference ADR-008. Let me edit.

  `tool_call(name="mcp__spine__spine_lint", arguments={"path": "<HARNESS>/runs-clean/cells/wwd3ti3/ws/ARCHITECTURE-SPINE.md"})`
  `tool_call(name="mcp__spine__fitness_check", arguments={"path": "<HARNESS>/runs-clean/cells/wwd3ti3/ws"})`
  `tool_call(name="mcp__spine__openapi_lint", arguments={"path": "<HARNESS>/runs-clean/cells/wwd3ti3/ws/openapi/tsp-api.yaml"})`

Now let me validate the changes by running the spine tools:
1. spine_lint on ARCHITECTURE-SPINE.md (should still pass, with AD-009)
2. fitness_check (should still pass)
3. openapi_lint on openapi/tsp-api.yaml

Let me run these in parallel.
Пакет собран. Прогоняю валидацию: спайн-линтер, fitness-гейт и контрактный линт OpenAPI.

  `edit(file_path="<HARNESS>/runs-clean/cells/wwd3ti3/ws/openapi/tsp-api.yaml", new_string="  /v1/consents/{consentId}/cancel:\n    post:\n      operationId: cancelConsent\n      parameters:\n        - {in: path, name: consentId, r, old_string="  /v1/consents/{consentId}/cancel:\n    post:\n      operationId: cancelConsent\n      parameters:\n        - {in: path, name: consentId, r)`

The openapi_lint found an error: OA-003 — POST without Idempotency-Key header. The `cancel` endpoint (POST /v1/consents/{consentId}/cancel) lacks the Idempotency-Key header parameter. But cancellation is idempotent by nature (cancelling an already-cancelled consent is a no-op), but the lint requires Idempotency-Key on mutating endpoints (OA-003 = идемпотентность mutating-endpoint'ов).

Actually, cancel is idempotent by design (POST on a subresource that transitions ACTIVE→CANCELLED, and terminal CANCELLED means repeated cancel is a no-op). But the lint rule OA-003 requires Idempotency-Key on mutating endpoints. To satisfy the lint and be consistent with the repo's idempotency discipline, I should add the Idempotency-Key header to the cancel endpoint.

Actually, is the cancel idempotent? Yes — cancel is naturally idempotent (cancel an already-cancelled consent = no-op, return same resource). But the contract doc's §2 says "Idempotency-Key обязателен для всех POST". So I should add it to the cancel endpoint too, for consistency.

Let me add the Idempotency-Key header parameter to the cancel endpoint in openapi/tsp-api.yaml.

Let me edit the openapi file.
Линт OpenAPI нашёл одну ошибку: `POST /v1/consents/{consentId}/cancel` без `Idempotency-Key` (OA-003 — идемпотентность mutating-endpoint). Добавлю заголовок для соответствия дисциплине идемпотентности (§2 контракта).

  `tool_call(name="mcp__spine__openapi_lint", arguments={"path": "<HARNESS>/runs-clean/cells/wwd3ti3/ws/openapi/tsp-api.yaml"})`

Also, I should update the contract doc §3.6.3 to mention Idempotency-Key is required (already implied by §2 "Idempotency-Key обязателен для всех POST"). Actually §2 already says it's required for all POST. But the cancel endpoint's doc doesn't explicitly say. §2 covers it globally. But to be safe and consistent, I'll add a note in §3.6.3 that Idempotency-Key applies. Actually, §2 global rule covers it. But the doc's §3.6.3 says "Отмена ТСП..." without mentioning idempotency. Since §2 says "Idempotency-Key обязателен для всех POST", it's covered. I'll leave it, but maybe add a brief note. Actually, let me not over-edit; §2 covers it. 

Now re-run openapi_lint to confirm it passes.

  `run_shell_command(command="git status --short && echo \"---DIFF STAT---\" && git diff --stat", description="Check changed files")`

All validations pass:
- spine_lint: passed
- fitness_check: passed
- openapi_lint: PASS (after fix)

Let me also verify there are no issues with the contract_doc change vs the tsp-api.md markdown doc. Actually the markdown doc §3.6.3 doesn't mention Idempotency-Key explicitly, but §2 global covers it. It's fine.

Now let me verify the overall git status to confirm what I've changed, and do a final review of the key files to make sure they're coherent.

Let me run git status and git diff --stat to summarize.

Actually, let me also double check: the `.qwen/settings.json` was already modified (pre-existing, not by me). I should NOT touch it or stage it. I'll just report my changes.

Let me run git status to list my changed files.


There's a `.arch-handoff/mcp-calls.jsonl` untracked file — this is likely auto-generated by the spine MCP server logging my tool calls. It's not mine to include in the change. I'll leave it as-is (untracked, not staged). Actually it appeared because of my MCP calls. It's a side effect of the spine MCP server. I should not modify or delete it (it's tool-generated). I'll just note it's not part of my deliverable.

Actually wait — is `.arch-handoff/mcp-calls.jsonl` something I should worry about? It's untracked and auto-generated by the MCP server (journal of calls). It's not part of my architectural package. I'll leave it alone.

Now everything is done. Let me do a final review of the key deliverables to make sure they're coherent and correct. Let me quickly re-read the final ARCHITECTURE-SPINE.md AD-009 block and the ADR to confirm correctness (already reviewed during edits).

Actually, I'm confident in the content. Let me summarize the results for the user.

Let me write a concise final summary in Russian (matching the user's language), covering the 7 deliverables and listing created/modified files, plus the validation results.

Let me be concise but complete.
Готово. Архитектурный пакет изменения «рекуррентные C2B-списания» собран поверх принятого решения и провалидирован контуром Spine. Резюме по семи пунктам задачи:

## 1. Значимость и маршрут
`significance_score` → **score = 7 → Critical** (сработали `financial_impact`, `api_contract_change`, `data_contract_change`, `consistency_model_change`, `security_boundary_change`, `significant_nfr`, `cross_domain_integration`). Рекуррентное списание — самый рискованный класс C2B (деньги без действия клиента + ПДн согласия + право отзыва), поэтому полный Solutioning, а не дельта-спека.

## 2. Влияние на принятую архитектуру
- **Не меняются**: AD-005 (зачисление только из `PAID`), AD-008 (гибрид), trust-зоны, outbox/сверка/АБС-адаптер, одноразовый C2B-поток.
- **Расширяются**: AD-002 (машина согласия), AD-003 (ключи `consentId`/`billingReference`).
- **Новый**: **AD-009 «рекуррентное списание — только по активному согласию»**.

## 3. Решение (ADR-008, Proposed)
Согласие как сущность первого класса + рекуррентный платёж как `paymentType=recurring` (переиспользует машину платежа без `QR_ISSUED`/`EXPIRED`). Отклонены: отдельный сервис «Подписки», расширение машины платежа, согласие на стороне ТСП. Обратимость: reversible на старте, costly после боевой эксплуатации.

## 4. Контракты
`openapi/tsp-api.yaml` + `docs/contracts/tsp-api.md` — **аддитивно, версия 0.1.0**: новые `/v1/consents/*`, опциональные `paymentType`/`consentId`/`billingReference` в `POST /v1/payments`. Breaking-изменений нет.

## 5. NFR
`docs/nfr.md` §7: лимиты p95<100 мс, 0 двойных списаний за период, 0 списаний по неактивному согласию, блокировка ≤1 с от отзыва, пик биллинга 1000 TPS без деградации, ежесуточная сверка мандатов.

## 6. Приёмка и откат
Критерии в EARS (7 шт.), план отката — фиче-флаг `recurring_debits_enabled` (per TSP) + `stop-new` + rolling, сигналы отката и владелец решения зафиксированы.

## 7. Человеку-архитектору
A3-выбор ADR-008 + регуляторные/бизнес-решения, которые архитектор не уполномочен принимать: юридическая форма согласия и отзыв (ГК/161-ФЗ/152-ФЗ), протокол НСПК (внешний вход), AML-пороги, тарифы, UX отзыва, волна запуска.

## Валидация
- `spine_lint` — **passed** (0 находок).
- `fitness_check` — **passed** (7 правил, 0 нарушений, ослаблений нет).
- `openapi_lint` — **PASS** (после добавления `Idempotency-Key` на `cancel`).

## Файлы
**Созданы:**
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-soglasie-i-mandat.md`
- `docs/spec/mandate-state-machine.md`
- `docs/changes/recurrent-c2b-debits/README.md` (сводный пакет)

**Изменены (принятым в репозитории способом — новый ADR + Proposed-блок спайна + аддитивные правки):**
- `ARCHITECTURE-SPINE.md` — добавлен AD-009 (Proposed)
- `docs/contracts/tsp-api.md` — аддитивные эндпоинты согласий
- `openapi/tsp-api.yaml` — аддитивные пути/схемы
- `docs/nfr.md` — раздел 7
- `docs/solutioning.md` — возврат автоплатежей в scope (ссылка на ADR-008)

Не трогал: `.qwen/settings.json` (предсуществующее изменение) и `.arch-handoff/mcp-calls.jsonl` (журнал MCP-вызовов, сгенерирован сервером). Принятые блоки AD-001…AD-008 и ADR-001…007 не переписывались.
