<!-- источник: <HARNESS>/runs/cells/spine-r2/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-cells-spine-r2-ws/chats/8ec7b279-a73c-41f5-a316-620c5ab9521e.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `glob(pattern="**/*")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/.arch-handoff/ARCHITECTURE.md")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/.arch-handoff/RUBRIC.yaml")`

Let me understand the task. The user is a bank solution architect. I need to prepare an architectural package for a new feature: recurring C2B debits (subscriptions) for the SBP payment gateway, layered on top of the accepted architecture.

This is a documentation/architecture task, no code. I need to:
1. Significance assessment and route (Fast/Standard/Critical)
2. Impact on accepted architecture: which invariants are affected
3. Architectural decision with alternatives, consequences, reversibility (ADR)
4. Contract changes (openapi/tsp-api.yaml) without breaking existing consumers
5. Measurable NFRs for new functionality
6. Acceptance criteria and rollback plan
7. What remains for human architect decision and why

I should use the established methodologies and tools in this repo. There are many skills available. Key ones:
- `spine-architect-review` — architectural review through Spine
- `significance-routing` — significance scoring
- `adr-authoring` — ADR discipline
- `nfr-design` — measurable NFRs
- `spine-contracts-gate` — contract gate
- `readiness-gate` — acceptance criteria
- `spine-invariants` — invariants

Also there's the Spine MCP server with tools like `significance_score`, `model_query`, `model_graph`, `trace_check`, `contract_diff`, `nfr_check`, etc.

The task is substantial. Let me start by exploring the repository to understand the accepted architecture. I need to read the actual files, not assume.

Let me plan my approach:
1. First, explore the repo: read ARCHITECTURE-SPINE.md, docs/, openapi/, .arch-handoff/
2. Use significance-routing skill to assess the route
3. Understand the existing architecture deeply
4. Draft the ADR for the new feature
5. Prepare contract changes
6. NFRs
7. Acceptance criteria + rollback
8. Human architect decision items

Let me first read the key files. I should do this in parallel where possible.

The working directory is `<HARNESS>/runs/cells/spine-r2/ws`.

Let me start reading. I'll read the main files in parallel.

Actually, I should first invoke the significance-routing skill since it's directly relevant to task #1, and also start reading the repo files. But skills should be invoked BEFORE generating other response about the task. Let me think about the order.

The instructions say: "When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action."

The most relevant skills here are several. But I can't invoke all at once meaningfully — actually I can call multiple in parallel? The skill tool executes a skill within the main conversation. Let me think.

Actually, let me be strategic. The task is complex and involves multiple disciplines. The most foundational first step is to understand the repo (read files) and assess significance. The significance-routing skill is directly about task #1.

But I also need to explore the codebase first to understand what's there. Let me read the files first, then invoke skills as needed.

Actually, re-reading the skill instruction: "When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action." This suggests I should invoke a relevant skill first.

Given the breadth, let me start by reading the repository structure and key files, AND check what Spine tools are available. Actually, the most important thing is to ground myself in the actual repo content.

Let me be pragmatic. I'll:
1. Read the key files in parallel (ARCHITECTURE-SPINE.md, README.md, .arch-handoff/ files, docs structure)
2. Then invoke skills as appropriate

Let me first do a broad read. I'll read ARCHITECTURE-SPINE.md, README.md, .arch-handoff/TASK.md, .arch-handoff/MANIFEST.json, .arch-handoff/CONSTRAINTS.yaml, .arch-handoff/ARCHITECTURE.md.

Let me also glob to see the full structure of docs/ and openapi/.

Let me start.

Actually, given the significance of using established methodology, and the instruction to invoke skills immediately, I'll invoke the `significance-routing` skill first since task #1 is exactly significance assessment. But wait — I should read the repo first to have context for everything. The significance routing skill will give me the methodology.

Let me do a hybrid: read files first (parallel reads), and also I can invoke the significance skill. Actually skills load methodology text into context. Let me first read the actual repo to understand, then invoke skills.

I think the cleanest approach: 
1. Glob to understand structure
2. Read key files
3. Invoke relevant skills (significance-routing, adr-authoring, nfr-design, spine-invariants, readiness-gate) as I need their methodology
4. Use Spine MCP tools for significance scoring, trace_check, contract analysis

Let me begin with parallel reads and globs.

Let me write out my first message: state what I'm about to do, then fire off parallel read/glob calls.

I'll start with exploration.
Я подготовлю архитектурный пакет для рекуррентных C2B-списаний (подписки СБП) поверх принятого решения. Начну с изучения репозитория — прочитаю инварианты, документы, контракты и пакет передачи, затем применю методики Spine и навыки репозитория.

  `glob(pattern="docs/**/*")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/openapi/tsp-api.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/nfr.md")`

I have a good overview. Now I need to read the key docs in detail: solutioning.md, nfr.md, contracts, state-machine.md, and the openapi/tsp-api.yaml. Also the ADR files (docs/adr) for full content, especially ADR-002 (state machine), ADR-004 (at-least-once DLQ), ADR-005 (ABS integration).

Let me read the remaining files. There's a discrepancy: README says `docs/contracts/tsp-api.md` and `docs/contracts/opkc-adapter.md`, `docs/spec/state-machine.md`, `docs/rfp/vendor-rfp.md`, but glob only showed `openapi/tsp-api.yaml` and `docs/adr/*` and `docs/nfr.md` and `docs/solutioning.md`. Let me check the full glob - it was truncated (110 files, 10 truncated). Let me glob specifically for docs/.

Let me read the docs in parallel.

  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/adr/ADR-002-model-konsistentnosti-plate)`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/adr/ADR-005-integraciya-s-abs-zachislen)`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/adr/ADR-001-outbox.md")`

Now let me read the remaining docs: the ADR files (docs/adr/*), state-machine.md, contracts (tsp-api.md, opkc-adapter.md), vendor-rfp.md, and the full content of ADR-002, ADR-004, ADR-005, ADR-007. These are crucial for understanding the existing architecture and how the new feature (recurring/subscription C2B) would affect it.

Let me read them in parallel.

  `skill(skill="significance-routing")`
  `skill(skill="adr-authoring")`
  `skill(skill="nfr-design")`
  `glob(pattern="model/**/*")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/rfp/vendor-rfp.md")`

I now have a very thorough understanding of the accepted architecture. Let me now use the Spine MCP tools to formalize the significance assessment and trace the impact. Also, I should use the skills: significance-routing, adr-authoring, nfr-design, spine-invariants, readiness-gate, and possibly delta-spec for the contract change.

Let me first invoke the significance-routing skill (it's directly relevant for task #1), and use the Spine tools significance_score and model_graph/trace_check to understand the current model state.

Actually, let me check what the model/ directory contains - I noticed the glob didn't show a model/ directory. Let me check. The ARCHITECTURE-SPINE.md mentions "типизированная модель архитектуры (каталог model/)" but there's no model/ directory in the file listing. Let me verify by checking. The glob for docs/**/* showed only 13 files, no model/. The top-level glob (110 files) didn't show a model/ directory either — but it was truncated at 20 items + "10 files truncated". Actually the full glob showed files sorted by modification time, and included .qwen/skills/*. Let me check if there's a model/ directory.

Actually, looking at the first glob output, it was truncated ("[10 files truncated]"). The visible files include .qwen/skills and .arch-handoff and docs. There's no model/ directory visible. Let me check specifically.

Let me now:
1. Invoke the significance-routing skill to get the methodology.
2. Use Spine MCP tools: significance_score / significance_from_diff, trace_check, model_graph to understand model state.

Actually, since there's no code written yet (this is a design task), the significance_from_diff might not apply (no diff yet). significance_score takes 15 triggers as input — I need to provide the trigger assessment.

Let me first invoke the significance-routing skill, and also do a model check. Let me also check if there's a model/ directory.

Let me invoke the significance-routing skill and check model directory in parallel.

Actually, the skill tool loads methodology. Let me think about which skills I genuinely need to load vs. which I can apply from the MCP descriptions.

Key deliverables and their methodologies:
1. Significance/route → significance-routing skill (and Spine significance_score tool)
2. Impact on invariants → spine-invariants skill (and trace_check/model tools)
3. ADR → adr-authoring skill (and adr-template reference)
4. Contract changes → spine-contracts-gate skill (and contract_diff, openapi_lint tools)
5. NFR → nfr-design skill (and nfr_check tool)
6. Acceptance criteria + rollback → readiness-gate skill
7. Human architect decision → from analysis

I should invoke these skills to follow the established methodology. But I don't want to overload context. Let me be strategic: invoke the most critical ones.

Actually, the instructions say "When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action." Since multiple skills are relevant, and I've already done initial exploration (which is fine — exploration is needed first), now I should invoke the relevant skills.

Let me invoke the key skills. I'll invoke significance-routing first (it's the entry point for task #1), then adr-authoring, nfr-design, readiness-gate, spine-invariants, spine-contracts-gate. These are the core methodology skills.

Actually, I can invoke multiple skills. But each skill invocation loads a SKILL.md into context. Let me be judicious. The most important for the actual work:

1. `significance-routing` — for route assessment
2. `adr-authoring` — for the ADR (task #3)
3. `nfr-design` — for NFRs (task #5)
4. `readiness-gate` — acceptance criteria (task #6)
5. `spine-invariants` — for impact on invariants (task #2)
6. `spine-contracts-gate` — for contract changes (task #4)

Let me invoke these. I'll do them one at a time or in parallel. The skill tool executes a skill "within the main conversation" — I think I can call multiple in parallel.

Actually, let me check the significance-routing skill first, and check for a model/ directory and run Spine's significance/trace tools.

Let me first check if there's a model directory and read the vendor-rfp and remaining bits, and invoke the significance-routing skill.

Let me prioritize. I'll invoke significance-routing skill and adr-authoring skill in parallel (both relevant), and check model dir + run a couple Spine tools.

Actually, running Spine MCP tools requires tool_search/tool_call. Let me do that too. Let me be careful about the order — I'll first load the significance-routing skill (most foundational for the whole task), and check for model/ dir, and read vendor-rfp.md.

Let me do these in parallel:
- skill: significance-routing
- glob for model/**/*
- read vendor-rfp.md (to understand what's already there re: roadmap mention of "автоплатежи")

Wait, vendor-rfp is about vendor RFP for transport — probably not directly relevant to recurring payments. But it may mention roadmap. The solutioning.md already said roadmap out of scope includes "автоплатежи" (autopayments). Interesting — the roadmap already anticipated this feature. So "рекуррентные C2B-списания по согласию плательщика — подписки СБП" is essentially "автоплатежи" / recurring payments / СБП pull payments with consent.

This is a key insight: the feature is a NEW payment model (pull/auto-debit with payer consent) on top of C2B. In SBP terms, this is likely the "СБП автоплатежи" / "recurring" / "pull payments" (СБП-подписки). It fundamentally changes the flow: instead of payer-initiated QR payment, it's a merchant/payee-initiated debit with a pre-authorized consent (mandate).

This has significant architectural impact:
- New consent/mandate entity (согласие плательщика) with its own lifecycle
- New payment initiation flow: ТСП initiates debit → шлюз → ОПКЦ → банк плательщика → списание со счёта плательщика → зачисление ТСП
- This touches the state machine (new states? or a parallel state machine for mandates/debits?)
- New contract endpoints
- New NFRs (recurring scheduling, consent revocation, retry windows)
- Regulatory: consent management per 161-ФЗ, ПДн, 115-ФЗ (AML on recurring), tokenization of payer payment method

Let me get the methodology loaded. Let me invoke skills and do parallel exploration.

I'll invoke the significance-routing skill, adr-authoring skill, nfr-design skill, readiness-gate skill, spine-invariants skill, and spine-contracts-gate skill. Actually that's a lot at once. Let me do the most critical ones now: significance-routing, adr-authoring, nfr-design. And check model dir + vendor-rfp in parallel.

Let me do it.
Я изучил принятую архитектуру. Теперь подключу методические навыки репозитория и проверю модель/инструменты Spine, чтобы формализовать оценку значимости и влияние на инварианты.

  `tool_search(query="select:mcp__spine__significance_score,mcp__spine__trace_check,mcp__spine__model_graph,mcp__spine__nfr_check,mcp__spine__openapi_lint,mcp__s)`

There's no model/ directory. So the Spine model tools (model_query, model_graph, trace_check, model_validate) won't have much to work with. The trace_check "case" needs a model/ directory. Let me verify by running the Spine tools — significance_score and trace_check and architect_review. Actually, since there's no model/, trace_check might report "no model found" or similar. But the significance_score tool is key for task #1 — it takes 15 triggers and returns a route.

Let me check the significance_score schema and run it. Also I should run the Spine tools to ground the assessment: significance_score, and maybe trace_check (to see what's covered), model_validate (will report no model), nfr_check (needs model). Let me run significance_score first — it's the most important for the deliverable #1.

Actually, let me think about whether I need to run Spine tools at all. The task says "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." So I should use the Spine tools where they add value.

The significance_score tool: "Architecture Significance Score по 15 триггерам → маршрут изменения". This is the canonical tool for deliverable #1. Let me use it.

Let me review the schema of significance_score and trace_check and architect_review via tool_search.

Actually, I can directly call tool_call with mcp__spine__significance_score, but I need to know its schema first. Let me use tool_search to get the schema.

Let me search for the significance_score schema, and also check trace_check and model_graph and nfr_check schemas, and openapi_lint/contract_diff.

Let me do tool_search for these.

  `tool_call(name="mcp__spine__significance_score", arguments={"triggers": {"new_component": true, "new_datastore": true, "new_vendor": false, "domain_ownership_change": false, "cross_domain_integration)`
  `tool_call(name="mcp__spine__openapi_lint", arguments={"path": "openapi/tsp-api.yaml", "cwd": "<HARNESS>/runs/cells/spine-r2/ws"})`

I have the schemas for significance_score, trace_check, model_graph, nfr_check, openapi_lint. Let me now run significance_score with the triggers for the recurring payment feature.

Let me think about the 15 triggers for this feature (recurring C2B debits / subscriptions with payer consent):

1. new_component — Is there a new component? The recurring payment feature adds a "consent/mandate manager" (согласие плательщика), a scheduler/initiator (планировщик рекуррентных списаний). This is likely a new component or at least a significant new subsystem. TRUE.

2. new_datastore — new storage for consents (mandates), tokens of payer's payment method? Probably the consent store is new data. Could be part of existing DB but a new entity. This is borderline. It's a new data domain (consent/mandate). I'd say TRUE (new datastore for consents/schedules).

3. new_vendor — No new vendor (transport adapter already covered). FALSE. Unless the recurring debit needs new NSPK protocol support from the vendor. Actually, SBP recurring/pull payments (автоплатежи) are a specific NSPK service that the transport adapter would need to support — the existing vendor would extend. Not a NEW vendor, but new capability. FALSE for new_vendor.

4. domain_ownership_change — No ownership change of existing domains. FALSE.

5. cross_domain_integration — Recurring involves consent management (payer-facing, possibly via payer's bank app), a new integration with payer's bank via NSPK pull mechanism. It's a new cross-domain flow. Hmm. The flow is ТСП initiates → шлюз → ОПКЦ → банк плательщика (списание). This is a new direction (pull vs push). Could be TRUE for cross_domain_integration. Actually, it's the same external NSPK domain, but the payer-side (bank плательщика) becomes a direct participant in the flow. Let me think... The existing C2B already involves the payer's bank (payer scans QR and pays in their own bank). For recurring, the payer's bank is still involved but via a consent/mandate. It's arguably still within the existing NSPK integration domain. I'll mark cross_domain_integration TRUE — there's a new integration surface: consent management, and possibly the payer's consent is established via the payer's bank (СБП consent is often created through the payer's bank app / ОПКЦ). This is a meaningful new cross-domain touchpoint.

6. api_contract_change — YES, definitely. New endpoints for consent/mandate management + recurring payment initiation, plus changes to payment model. TRUE.

7. data_contract_change — YES, new data: consent/mandate entity, recurring schedule, tokenized payer account. TRUE.

8. security_boundary_change — This is a critical trigger. Does recurring change security boundaries? The consent data (payer's consent, payment details/token) is sensitive. But does it change security boundaries/trust zones? Not fundamentally — the trust zones remain. However, storing payer consent + tokenized payment instrument adds a new sensitive data boundary. Borderline. I'd lean FALSE for a genuine "security boundary change" (no new trust zone crossing), but consent/token storage is a new sensitive data surface. Hmm, actually the critical trigger list says security_boundary_change is critical. Let me be careful and honest. The feature doesn't move trust zone boundaries — the DMZ/payment/ABS zones stay. It adds a consent store within the payment zone. I'll mark FALSE but note it in the impact. Actually, "security_boundary_change" could also cover "new external trust boundary" — here there's no new external party (still NSPK). I'll mark FALSE.

Actually wait — let me reconsider. The recurring consent requires capturing the payer's consent and, critically, in SBP the consent (согласие) is often registered with ОПКЦ/банк плательщика. This introduces a consent lifecycle involving the payer's bank. But that's still through NSPK. Not a new trust zone. FALSE.

9. trust_zone_change — No new trust zone. FALSE.

10. consistency_model_change — This is significant. Recurring payments introduce a new consistency model: a consent/mandate has its own state machine (active/revoked/expired), and a recurring debit is a new financial operation type with its own state machine (scheduled → initiated → paid → credited). The existing state machine is payment-centric. This is a consistency model extension, arguably a change. TRUE (the consistency model extends to cover consent lifecycle + scheduled debit). Actually is it a "change" or an "extension"? It's a meaningful change to the state model. I'll mark TRUE.

11. significant_nfr — New NFRs: recurring processing throughput, scheduling precision, consent revocation latency, retry windows. But are they "significant"? The existing NFRs (200 TPS) may need to handle scheduled batch processing at scale. I'd mark TRUE — new NFRs for scheduling, consent revocation propagation, and a different load profile (batch/off-peak scheduling).

12. rto_rpo_targets — RPO=0 already established; recurring inherits it. No change to RTO/RPO targets. FALSE.

13. irreversible_migration — Critical trigger. No irreversible migration here (consent store is new, no data migration of existing systems). FALSE.

14. financial_impact — YES, definitely. Recurring debits are financial operations; double-debit or unauthorized debit is a serious financial/regulatory risk. TRUE.

15. criticality_or_exception — Critical trigger. Is this a "criticality or exception" situation? It's a new financial product (subscriptions) on a Critical-route system. The parent is already Critical. But this specific change... "criticality_or_exception" is for things that require exception handling. The recurring payment itself is a financial feature, high criticality, but not an "exception" to the norm. Hmm. Given financial_impact is already TRUE and this is a payment product change, I'll mark criticality_or_exception as FALSE (it's not an exception — it's a planned roadmap feature; the feature is significant but not an exceptional/one-off). Actually, let me reconsider: recurring C2B (подписки) is a new payment modality that may have distinct regulatory treatment (consent under 161-ФЗ, recurring authorization rules). It's high criticality. But "criticality_or_exception" trigger is more about "this is critical enough to need exception handling" — I think for a financial product on a financial system, this is genuinely critical. However, I should avoid over-inflating. The honest count matters.

Let me tally honestly:

1. new_component — TRUE (consent/mandate manager + scheduler/initiator)
2. new_datastore — TRUE (consent/mandate + tokenized payer instrument store)
3. new_vendor — FALSE
4. domain_ownership_change — FALSE
5. cross_domain_integration — TRUE (payer-consent lifecycle via NSPK/банк плательщика; new pull flow)
6. api_contract_change — TRUE
7. data_contract_change — TRUE
8. security_boundary_change — FALSE (no new trust zone)
9. trust_zone_change — FALSE
10. consistency_model_change — TRUE (consent + debit state machines)
11. significant_nfr — TRUE (scheduling, consent revocation, batch load profile)
12. rto_rpo_targets — FALSE
13. irreversible_migration — FALSE
14. financial_impact — TRUE
15. criticality_or_exception — FALSE

Count of TRUE: new_component, new_datastore, cross_domain_integration, api_contract_change, data_contract_change, consistency_model_change, significant_nfr, financial_impact = 8.

That's 8 ≥ 5 → Critical.

Also, none of the three critical triggers (security_boundary_change, irreversible_migration, criticality_or_exception) are set, but 8 ≥ 5 means Critical anyway.

Let me verify my assessment with the actual tool. Let me run significance_score with these triggers.

Actually, let me reconsider cross_domain_integration and consistency_model_change to be honest:

- cross_domain_integration: "интеграция между доменами". The recurring feature adds a consent domain (payer consent), which is a new domain concept. It integrates with NSPK (existing) and the payer's bank (via NSPK). I think this is legitimately a cross-domain integration — the consent/mandate is a new domain that crosses into the payer's bank. TRUE is defensible.

- consistency_model_change: The existing model is a single payment state machine with ACID. Recurring adds: (a) consent/mandate lifecycle, (b) scheduled debit operations that are initiated by the system (not by TSP interactive call), (c) new consistency concerns (e.g., consent revocation vs in-flight debit race). This is a real consistency model change. TRUE.

- new_datastore: consent store + schedule store. New entities, possibly a new table set in the same DB or a separate store. Since ADR-001 says "новая БД шлюза" already exists, the recurring feature would add tables/entities to it (not necessarily a new physical datastore). But "new_datastore" trigger is about a new datastore (logical or physical). The consent/mandate store is a new data domain. I'll keep TRUE but note it may be co-located. Actually, to be precise and honest: this is likely a new logical datastore (consent registry), which is significant. TRUE.

- new_component: The scheduler + consent manager. Whether these are "new components" (new deployable) or modules within the gateway is an open design question. This is precisely a design decision I'll make in the ADR (module within gateway vs separate component). For significance purposes, it introduces a new component/module with new responsibility. TRUE.

So 8 triggers → Critical. That's my honest assessment, and it makes sense: recurring financial debits with consent is a Critical change requiring full Solutioning + A3 human decision.

Let me run the tool to confirm and get the machine-readable route.

Actually, let me also consider: should I run trace_check, model_graph, nfr_check? There's no model/ directory, so those tools (trace_check, model_graph, nfr_check, model_validate) would report "no model found" — they operate on the typed model directory which doesn't exist in this repo. The repo's "model" is implicit in ARCHITECTURE-SPINE.md + docs. So those tools won't add value here (no typed model). Let me verify quickly with model_graph or trace_check to confirm there's no model — actually the glob already confirmed no model/ directory. I'll skip those.

The openapi_lint tool could be useful for task #4 (contract changes) — I could lint the current tsp-api.yaml and then lint my modified version. But openapi_lint checks versioning, idempotency of mutating endpoints, RFC 7807 errors. Let me use it on the current file to understand baseline, then on my proposed version.

Let me run significance_score now with my triggers.

Let me construct the triggers array. I'll use the object form or array form. Array of "name=true"/"name=false".

Let me run it.

  `skill(skill="spine-invariants")`
  `skill(skill="delta-spec")`
  `skill(skill="spine-contracts-gate")`
  `skill(skill="readiness-gate")`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/.qwen/skills/adr-authoring/references/adr-te)`
  `read_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/.qwen/skills/spine-invariants/references/spi)`

The significance_score tool confirms: route = Critical, score = 8, fired 8 triggers. This aligns with my assessment.

The openapi_lint passes on the current contract (0 findings).

Now let me look at the ADR template reference, and the spine-invariants skill + spine template, to understand how to structure the ADR and how to modify ARCHITECTURE-SPINE.md (since the task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории").

Key question: how are files changed in this repo? The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории."

Looking at the repo:
- There's a delta-spec skill ("Дельта-спецификации для brownfield-потока (по OpenSpec)"). But wait, this repo doesn't have an openspec/ directory (the openspec_coverage tool mentions openspec/specs/ but the glob didn't show openspec/). 
- The delta_guard MCP tool: "Гейт прямых правок спайна мимо дельты (модель 5.2)". So there's a "delta protocol" — spine changes must go through a delta, not direct edits.

But actually, more relevant: the repo uses ADR files (docs/adr/ADR-NNN.md) and ARCHITECTURE-SPINE.md. The accepted method for adding a new architectural decision is to ADD a new ADR file (ADR-008) and NOT modify existing accepted ADRs (they use Superseded chain if changed).

Let me look at the delta-spec skill and the spine-invariants skill to understand the exact "way accepted in this repo" for changing decision files.

Actually, the task says: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." This means: when I change the accepted decision files (ARCHITECTURE-SPINE.md, docs/adr/*, docs/contracts/*, openapi/*), I should follow the repo's conventions:
1. ADRs: add NEW ADR (ADR-008), don't rewrite ADR-001..007. Status Proposed. Reference existing ADRs.
2. ARCHITECTURE-SPINE.md: add new AD-009 (or extend Deferred list) — the "Deferred" list already mentions "автоплатежи" in roadmap. Actually the solutioning says roadmap out of scope includes "автоплатежи". So I need to add a new invariant AD-009 for recurring/subscription consent, OR modify the spine. The spine-invariants skill will tell me how.
3. Contracts: openapi/tsp-api.yaml — add new endpoints/fields backward-compatibly (additive, optional fields). The delta-spec skill might be relevant for "дельта-спецификации" — describe the change as ADDED/MODIFIED/REMOVED relative to current truth.

Let me read the spine-invariants skill, the delta-spec skill, the spine-contracts-gate skill, and the readiness-gate skill, plus the adr-template reference. Also I should read the spine-invariants references/spine-template.md.

Let me also check: is there a "openspec/" directory? The glob didn't show it. Let me verify. Also check .arch-handoff/adr/ vs docs/adr/ — there are duplicate ADRs in .arch-handoff/adr/. The .arch-handoff is the handoff package (epic-context compiled). The docs/adr/ is the source of truth.

Let me read the key skills I still need: spine-invariants, delta-spec, spine-contracts-gate, readiness-gate, and the adr-template.md reference.

Let me do these reads in parallel.
Маршрут подтверждён инструментом Spine: **Critical (score 8/15)**. Теперь изучу методики для изменений инвариантов, контрактов и критериев приёмки, а также шаблон ADR.

  `write_file(file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-, content="# ADR-008. Рекуррентные C2B-списания: согласие плательщика как мандат, повторное использование платёжной модели\n\n- Date: 2026-09-28\n- St)`

I now have a complete understanding of the methodology. Let me formulate the plan for the deliverables.

Key insight: The task is to prepare an architectural PACKAGE for the recurring C2B debits (subscriptions) feature, layered on top of the accepted architecture. This is a Critical route, so full Solutioning is needed (not just delta-spec). The delta-spec skill notes: "Critical Path (платежи, КИИ, необратимые миграции, смена security boundary) — полный Solutioning, дельта недостаточна."

The accepted way to change decision files in this repo:
1. Add a NEW ADR (ADR-008) — don't rewrite ADR-001..007. Status Proposed, with Alternatives/Consequences/Reversibility.
2. Modify ARCHITECTURE-SPINE.md by ADDING a new AD block (AD-009) for the recurring/subscription invariant, and possibly update the "Deferred" section (which currently lists "автоплатежи" under roadmap out of scope — actually it's listed under solutioning "Roadmap (вне scope): ... автоплатежи"). Wait, let me check the spine's Deferred section. The ARCHITECTURE-SPINE.md Deferred section lists: мультивалютность, C2C/B2C/B2B, диспуты. It does NOT list "автоплатежи". The solutioning.md Roadmap lists "автоплатежи" as out of scope.

So the recurring/subscription feature is currently OUT OF SCOPE (roadmap). This change BRINGS IT INTO SCOPE. This is an important framing: this is a scope expansion of an existing initiative, and it must be reflected properly.

Now, the deliverables:
1. Significance assessment → Critical, score 8, reasons. (done — I'll write it up)
2. Impact on invariants → which AD-XXX are affected, what changes, what doesn't.
3. ADR-008 with alternatives, consequences, reversibility.
4. Contract changes to openapi/tsp-api.yaml without breaking existing consumers.
5. Measurable NFRs.
6. Acceptance criteria + rollback plan.
7. What remains for human architect (A3) decision.

Let me think carefully about the DOMAIN of the feature first, so the architecture is correct.

**Business feature: рекуррентные C2B-списания по согласию плательщика — подписки СБП.**

Current state: C2B = payer-initiated. Payer scans QR / clicks link and pays. Every payment needs QR + payer action.

Target: Recurring debits where the payer gives a ONE-TIME consent (mandate), and then the TSP (merchant) can initiate subsequent debits without the payer re-authenticating each time (subscriptions: online cinemas, ЖКХ, telecom).

In SBP (НСПК) terms, this maps to the СБП "автоплатежи" / "рекуррентные платежи" / "подписки" capability. The NSPK has a specific service for recurring/pull payments with consent (согласие). This is analogous to card-based recurring payments / mandates (like SEPA Direct Debit mandate, or card-on-file with network token / CIT/MIT).

Key architectural concepts introduced:
1. **Согласие плательщика (consent / mandate / "подписка")** — a new entity with its own lifecycle: CREATED (draft) → ACTIVE (consent confirmed) → REVOKED (payer revoked) → EXPIRED (TTL) → SUSPENDED (temporary). The consent captures: payer identity, TSP, max amount per debit, max frequency/period, total amount cap, expiry date, and the payer's payment instrument reference (tokenized account in payer's bank, via NSPK).

2. **Рекуррентное списание (recurring debit)** — a new financial operation type, distinct from the one-off payment. Flow: TSP (or scheduler) initiates debit → шлюз → ОПКЦ → банк плательщика (списание со счёта плательщика по согласию) → подтверждение → зачисление на счёт ТСП. The debit is initiated by the MERCHANT/SYSTEM, not by the payer.

3. **Инициация**: two modes — (a) TSP initiates each debit via API (pull on demand), (b) the gateway schedules recurring debits according to the subscription schedule. The scheduler is a new component (or module).

4. **Tokenization / payment instrument reference**: The consent references the payer's payment method (банк плательщика + счёт/карта), which in СБП is established via the payer's bank app (первичная аутентификация при выдаче согласия).

This has significant impacts:

**Impact on state machine (AD-002, AD-005):**
- New state machine(s): consent lifecycle + recurring debit lifecycle.
- The recurring debit is NOT `CREATED → QR_ISSUED → PAID` — there's no QR. It's `SCHEDULED/INITIATED → PROCESSING → PAID (подтверждён НСПК) → CREDITED → COMPLETED`, with terminal FAILED (недостаточно средств / отклонено банком плательщика) and REVOKED-BY-CONSENT.
- Critical invariant: a recurring debit can only be initiated from an ACTIVE consent, within limits (amount ≤ consent max, frequency, total cap), and only until consent expiry/revocation. This is the NEW key invariant (analogous to "зачисление только из PAID").

**Impact on AD-005 (зачисление только из PAID):** The "PAID" concept still holds — the debit must be confirmed by НСПК (payer's bank actually debited) before crediting TSP. So AD-005 extends naturally: зачисление только из подтверждённого статуса списания. The consent adds a PRE-condition (consent active) but the "зачисление только из PAID" invariant is preserved and reinforced.

**Impact on AD-003 (идемпотентность):** Now extends to recurring debit idempotency: a debit initiated twice (retry / scheduler double-fire) must not double-debit. The Idempotency-Key applies to the debit initiation; and the consent itself must be idempotent. The critical new idempotency concern: a scheduled debit must be keyed by (consentId + period/cycle) to prevent double-scheduling.

**Impact on AD-001 (изоляция):** The consent manager and scheduler live inside the gateway's payment contour (not in arbitrary services). The TSP API remains the only entry. No change to the isolation principle; extended to cover the new components.

**Impact on AD-004 (единственный адаптер ОПКЦ):** The NSPK protocol for recurring/consent is still only known by the adapter. The adapter contract must be EXTENDED with consent registration + recurring debit initiation methods. This is a new capability the vendor must support (extends opkc-adapter.md contract + RFP). AD-004 unchanged in principle; adapter contract extended.

**Impact on AD-006 (trust zones):** No new trust zones. But consent data (payer consent, tokenized instrument) is new sensitive data → ПДн handling extended (AD-007). Storage of consent/token in the gateway DB → encryption at rest, minimization. No new boundary.

**Impact on AD-007 (НПС/КИИ/ПДн):** Recurring consents are ПДн + financial. Consent management has regulatory requirements (161-ФЗ: consent to recurring debits, revocation rights). AML monitoring of recurring flows. This strengthens AD-007 but doesn't change it.

**Impact on AD-008 (гибрид):** The vendor adapter must now also support NSPK recurring/consent services. AD-008 (hybrid) is unchanged — it's still "core in-house + vendor transport". But the RFP scope and opkc-adapter contract grow. This is a "what changes" item.

So the invariant impact is: 
- AD-001: unchanged (isolation extended to new components)
- AD-002: extended (new state machines: consent + recurring debit)
- AD-003: extended (idempotency for debit initiation + consent + schedule)
- AD-004: unchanged in principle; adapter contract extended
- AD-005: extended/reinforced (зачисление только из подтверждённого списания; consent-active as precondition)
- AD-006: unchanged (no new zones)
- AD-007: unchanged; consent adds ПДн/AML surface
- AD-008: unchanged (hybrid), RFP scope grows

The NEW invariant to add: AD-009 — "Рекуррентное списание только из активного согласия плательщика" (consent-gated debit). This is the key binding invariant that independent executors could get wrong.

Actually, let me think about whether AD-009 should be ONE invariant or the consent lifecycle is a separate concern. The spine-invariants test: "could two independent units choose incompatibly?" Yes — one unit might implement "debit allowed if consent exists" while another implements "debit allowed if consent ACTIVE and within limits". This is exactly the kind of thing to pin. So AD-009: "Рекуррентное списание — только из активного согласия в пределах лимитов".

Should I also pin the consent lifecycle states? That's more of a spec detail (state-machine.md), not necessarily a spine invariant. But the key financial-safety invariant (consent must be active + within limits + not expired/revoked) IS a spine-level invariant.

Let me also think about reversibility and the "what stays for human A3" items.

**What stays for human architect (A3) decisions:**
1. **Product scope & consent model**: Which consent types (amount-based, period-based, open-ended vs fixed-term)? This is a business decision affecting the consent model. The human architect (or business) must decide the consent authorization model.
2. **Consent capture UX / channel**: How is the payer consent established — via СБП (payer's bank app), via the TSP's own flow, via the gateway's own consent page? This depends on NSPK's recurring service capabilities (external input [ТРЕБУЕТ ПРОВЕРКИ]) and bank's product strategy. This is a business+product+regulatory decision.
3. **NSPK recurring service capabilities**: Does NSPK even support pull/recurring C2B with consent today, and what's the exact protocol? This is the external gap. Human decision: whether to build against an assumed protocol or wait for NSPK documentation (like ADR-007's constraint on transport).
4. **Scope of first wave**: Which TSP verticals (кинотеатры, ЖКХ, связь) and which debit model (scheduled vs on-demand pull). Business decision.
5. **Chargeback/dispute handling for recurring**: The Deferred list already says "Диспуты/претензии" is deferred. Recurring amplifies dispute risk (payer disputes a subscription debit). Human decision: does the first wave need dispute handling or defer it further? This affects the consent revocation → refund flow.
6. **AML/compliance thresholds for recurring**: consent-level vs debit-level monitoring.
7. **Whether consent/дeбит should be a separate initiative (parent spine change)** vs an extension of the existing feature spine. The Deferred list and solutioning roadmap said "автоплатежи" is out of scope / roadmap. Bringing it in-scope is a scope decision — does it stay within this feature spine (AD-009 added) or become a new initiative? Given it's a new payment modality, one could argue it's a new initiative. But it reuses the same gateway, same adapter, same АБС integration, so it's an extension of the same feature spine (feature → feature extension). Human decision on scope/ownership.

Actually, let me reconsider #7: the task explicitly says "Подготовь архитектурный пакет этого изменения поверх принятого решения". So it's an extension on top of the accepted decision. It stays within this repo/spine (feature level). Good.

Now, the contract changes (task #4). The openapi/tsp-api.yaml currently has:
- POST /v1/payments (createPayment)
- GET /v1/payments/{paymentId} (getPayment)
- schemas: PaymentRequest {amount, merchantOrderId}, Payment {paymentId, amount, status enum}

For recurring, I need to add (backward-compatible, additive only):
1. New resource: consent/mandate (subscription). 
   - POST /v1/subscriptions (create consent) — new path, doesn't break existing.
   - GET /v1/subscriptions/{subscriptionId} (status)
   - POST /v1/subscriptions/{subscriptionId}/cancel (revoke) — or DELETE.
   Actually, let me use "mandate" vs "subscription" terminology. In SBP context, the standard term is "согласие" (consent) / "подписка" (subscription) / "автоплатёж". I'll use "subscription" for the TSP-facing API entity (recurring agreement) and "consent"/"согласие" for the payer's mandate. Hmm, to avoid confusion, let me use a single entity: `subscription` (подписка) = согласие плательщика на рекуррентные списания.

2. New payment type / fields: the PaymentRequest needs a `type` or `recurring` field to distinguish recurring debit from one-off. To be backward-compatible, add OPTIONAL fields:
   - `subscriptionId` (optional) — if present, this payment is a recurring debit under an existing consent.
   - Or a new `paymentType` enum: `oneOff` (default) | `recurring`.
   Adding an optional field is backward-compatible.

3. New schema for subscription:
   - subscriptionId, tspId, status (PENDING_ACTIVATION, ACTIVE, REVOKED, EXPIRED, SUSPENDED), amount limit, period, maxDebits, expiresAt, etc.

4. Payment status enum: currently `[CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED]`. Recurring debit doesn't have QR_ISSUED. But I must NOT break the existing enum (existing consumers depend on it). The status enum for recurring debit would use a subset/reinterpretation. Options:
   - Keep the existing status enum and reuse it: recurring debit goes CREATED (initiated) → PAID → CREDITED → COMPLETED, skipping QR_ISSUED. This avoids adding enum values (backward compatible). The status "QR_ISSUED" simply isn't used for recurring. This is the cleanest backward-compatible approach.
   - Alternatively add new statuses like `SCHEDULED`, `PENDING_CONSENT` — but adding enum values is technically backward-compatible (existing consumers ignore new values). But the existing enum is a closed set; adding values could surprise strict consumers. The contract spec (§6) says "Добавление опциональных полей — обратно совместимо". Enum extension is trickier.

Best approach: Add a separate `subscription` resource and a `recurringDebit`/`subscriptionCharge` resource, OR reuse `/payments` with an optional `subscriptionId` and a new payment `kind` field. Reuse the Payment schema with additive optional fields.

Let me design the contract changes cleanly:

**Additive changes to openapi/tsp-api.yaml:**
1. New path `POST /v1/subscriptions` — create a subscription (consent). Requires Idempotency-Key.
2. New path `GET /v1/subscriptions/{subscriptionId}` — get subscription status.
3. New path `POST /v1/subscriptions/{subscriptionId}/revoke` — payer-initiated or TSP-initiated revocation (with reason). Actually revocation is usually payer-initiated (via payer's bank), but TSP may need to notify. Let me include `DELETE /v1/subscriptions/{subscriptionId}` (or POST .../cancel) for TSP to cancel. I'll use `POST /v1/subscriptions/{subscriptionId}/cancel`.
4. New path `POST /v1/subscriptions/{subscriptionId}/charges` — initiate a recurring debit under the consent (TSP pull mode). This returns a chargeId (or reuses paymentId). Actually, to keep consistency with the existing Payment state machine and AD-005, the recurring charge should be a Payment (or a subtype). Let me introduce `charge` as a distinct resource to avoid overloading `payment` semantics, OR reuse `payment`.

Hmm, this is a key design decision. Let me think about what's cleanest and matches the existing architecture:

Option A: Reuse `/payments` for recurring charges. `POST /v1/payments` with `subscriptionId` field → creates a recurring payment. The existing state machine handles it (CREATED → PAID → CREDITED → COMPLETED, skipping QR_ISSUED). This reuses everything (idempotency, state machine, АБС, notifications). Minimal new surface. But it conflates two different financial semantics (one-off QR vs consent-based debit) in one resource — the state machine needs a `kind` field.

Option B: New resource `/subscriptions/{id}/charges` for recurring debits, distinct from `/payments`. Cleaner semantics, but duplicates the state machine / АБС integration / notifications.

I think Option A (reuse payment + `kind`/`subscriptionId` field) is architecturally cleaner because AD-005 (зачисление из PAID), the state machine, outbox, АБС integration, and notifications all already work on the payment entity. The recurring charge IS a payment (a debit to the payer → credit to the TSP), just initiated differently (consent-based, no QR). Reusing the payment entity with a discriminator field `paymentType: oneOff|recurring` + optional `subscriptionId` is the minimal, backward-compatible, invariant-preserving approach.

So the contract change:
- `PaymentRequest`: add optional `paymentType` (enum `oneOff` default | `recurring`), optional `subscriptionId` (required if paymentType=recurring), optional `periodKey`/`chargeCycle` (for idempotency of scheduled debits). All optional → backward compatible.
- `Payment`: add optional `paymentType`, `subscriptionId`, `payerConsentRef` fields.
- New `Subscription` schema + paths.

For idempotency of recurring debits: the debit must be keyed so that the same scheduled cycle doesn't fire twice. Use `Idempotency-Key` (existing) + a new optional `chargeKey` field (unique per consent+cycle). Actually, `Idempotency-Key` alone is insufficient for scheduled debits because each scheduled cycle is a DIFFERENT debit with a DIFFERENT idempotency key — but the risk is double-scheduling the SAME cycle. So the subscription needs a `nextChargeKey` or the scheduler needs a deterministic idempotency key = `subscriptionId + periodKey` (e.g., `sub_123:2026-10`). I'll pin this in the ADR: the idempotency key for a scheduled debit is deterministic `{subscriptionId}:{periodKey}`.

Let me now also consider: should the TSP API expose `charges` as a sub-resource? I'll go with reusing `/payments` and `paymentType=recurring`. But I'll ALSO add a convenience `POST /v1/subscriptions/{subscriptionId}/charges` endpoint that maps to a recurring payment. Actually, having both is redundant. Let me keep it minimal: 
- `POST /v1/subscriptions` (create consent)
- `GET /v1/subscriptions/{subscriptionId}` (status)
- `POST /v1/subscriptions/{subscriptionId}/cancel` (revoke)
- Recurring debit = `POST /v1/payments` with `paymentType: recurring` + `subscriptionId`.

Actually, re-reading the task: "Изменения контрактов (openapi/tsp-api.yaml) без поломки существующих потребителей." So I need to show the contract delta. Let me produce a clean additive OpenAPI diff.

But wait — there are TWO contract files: `openapi/tsp-api.yaml` (the actual machine-readable OpenAPI) and `docs/contracts/tsp-api.md` (the prose contract spec). The task specifically says `openapi/tsp-api.yaml`. So I should modify `openapi/tsp-api.yaml`. Should I also update `docs/contracts/tsp-api.md`? The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." and "кратко перечисли созданные и изменённые файлы". The primary contract file to change is openapi/tsp-api.yaml (that's what the task names). But the prose spec docs/contracts/tsp-api.md is the "source" that README points to. Hmm.

Actually, the README says "docs/contracts/tsp-api.md контракт API ТСП v0.1 (мерчант-API)". And there's also openapi/tsp-api.yaml. The openapi file is a machine-readable summary (it's much smaller than the prose). The task explicitly names openapi/tsp-api.yaml as the file to change. I'll focus on openapi/tsp-api.yaml for the contract change (deliverable #4), and note that docs/contracts/tsp-api.md should be updated in a follow-up (or I can add a small delta note). Actually, to be thorough and correct, I should treat openapi/tsp-api.yaml as the authoritative machine contract and update it. I'll also update docs/contracts/tsp-api.md to stay consistent? The task says "когда закончишь, кратко перечисли созданные и изменённые файлы" — so the deliverable is files. Let me be focused:

Files I will create/change:
1. **CREATE** `docs/adr/ADR-008-recurring-c2b-consent.md` — the ADR (deliverable #3, and #1 + #2 partially).
2. **MODIFY** `ARCHITECTURE-SPINE.md` — add AD-009 invariant + update Deferred (remove "автоплатежи" from roadmap/out-of-scope, or add a note). Actually the spine Deferred doesn't list автоплатежи; the solutioning roadmap does. I'll add AD-009 to the spine and note the scope expansion.
3. **MODIFY** `openapi/tsp-api.yaml` — additive contract changes (deliverable #4).
4. **CREATE** `docs/spec/recurring-state-machine.md` — the consent + recurring debit state machines (part of deliverable #2/#5, and needed for readiness).
5. **CREATE** `docs/recurring-solutioning.md` — the full solutioning delta for the feature: significance, impact on invariants, NFRs, acceptance criteria, rollback, open questions/human decisions. This consolidates deliverables #1, #2, #5, #6, #7.

Actually, let me reconsider the file structure to match repo conventions:
- The repo has `docs/solutioning.md` (main solutioning). For a Critical change, the delta-spec skill says "полный Solutioning, дельта недостаточна". But the repo's solutioning.md is the whole system solutioning. For an incremental feature on top, I should add a focused solutioning document OR extend. Given the scale (new payment modality), I'll create a focused doc `docs/recurring-solutioning.md` (or `docs/spec/recurring-c2b.md`) plus the ADR. 

Let me settle on a clean, minimal, convention-following set:

1. `docs/adr/ADR-008-recurring-c2b-soglasie.md` — ADR (deliverable #3, plus significance & impact summary).
2. `docs/spec/recurring-state-machine.md` — consent + recurring debit state machines (deliverable #2 detail, #5 acceptance).
3. `docs/recurring-solutioning.md` — the feature solutioning: significance/route (#1), invariant impact matrix (#2), NFR (#5), acceptance criteria + rollback (#6), human A3 decisions (#7).
4. `openapi/tsp-api.yaml` — modified (additive) (#4).
5. `ARCHITECTURE-SPINE.md` — modified: add AD-009 (#2).

Hmm, but I want to avoid over-fragmenting. Let me consolidate:
- The ADR is the core decision artifact.
- The solutioning doc holds significance, impact, NFR, acceptance, rollback, human decisions.
- The state-machine doc holds the concrete state machines (needed for A1/A2, referenced by ADR and solutioning).
- The spine gets AD-009.
- The openapi gets the additive contract.

That's 3 new files + 2 modified files. Reasonable for a Critical architectural package.

Actually, I realize I should reconsider whether to modify ARCHITECTURE-SPINE.md directly, given the delta_guard tool ("Гейт прямых правок спайна мимо дельты"). The MCP description says "каждый изменённый файл под защищёнными путями (по умолчанию model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml...)". So there's a notion that ARCHITECTURE-SPINE.md changes should go through a "delta". But the delta-spec skill says Critical path = full Solutioning, delta insufficient. And the spine-invariants skill shows how to add AD blocks. 

The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The accepted way in this repo:
- ADRs: add new ADR file (don't rewrite).
- Spine: add new AD block (AD-009) — the spine-invariants skill shows blocks are added. There's no formal "delta file" for the spine in this repo (no openspec/ dir, no delta files). The delta_guard tool's "delta protocol" is a Spine-BE harness feature, but this repo doesn't appear to use a delta directory. Let me check if there's any delta/ directory or openspec/ directory.

Actually, the glob didn't show openspec/ or delta/ or model/ or changes/ directories. So the repo is in "решение" (decision) stage with docs/ + ARCHITECTURE-SPINE.md + .arch-handoff/. The "accepted way" to change the spine here is: add a new AD block in ARCHITECTURE-SPINE.md with Proposed status (like all the others are "Proposed" except AD-008 which is Adopted), and reference it from a new ADR.

Let me verify there's no openspec/ dir by checking. Actually the first glob (110 files) was truncated but I saw the top-level structure: ARCHITECTURE-SPINE.md, README.md, .arch-handoff/, .git/, .qwen/, docs/, openapi/. No openspec/, no model/, no delta/. Confirmed from the initial system reminder folder structure too.

So I'll directly add AD-009 to ARCHITECTURE-SPINE.md (following the existing block format) and mark it Proposed.

Now let me also run spine_lint after modifying the spine to make sure it's clean, and openapi_lint + contract_diff on the modified contract.

Let me now think about the CONTENT in detail for each deliverable.

---

**Deliverable #1: Significance assessment**

Route: Critical, score 8/15. Fired triggers (from tool):
1. new_component — consent manager + scheduler/initiator (new responsibility in the gateway)
2. new_datastore — consent/mandate registry + tokenized payer instrument store + debit schedule store
3. cross_domain_integration — consent lifecycle crosses into payer's bank via NSPK (new pull flow)
4. api_contract_change — new endpoints (subscriptions) + payment type extension
5. data_contract_change — new entities (consent, schedule, recurring debit)
6. consistency_model_change — new state machines (consent lifecycle, recurring debit)
7. significant_nfr — scheduling precision, consent revocation propagation, batch load profile
8. financial_impact — double-debit / unauthorized debit is financial + regulatory

Why deep design: Critical → full Solutioning + ADR + NFR + A3 human decision + walking skeleton + evidence gates. Not delta-spec (Critical path).

**Deliverable #2: Impact on invariants**

Matrix (what changes / what doesn't):

| AD | Invariant | Impact | Change? |
|---|---|---|---|
| AD-001 | Изоляция платёжного контура | Новые компоненты (consent manager, scheduler) живут в платёжном контуре шлюза; единая точка вызова АБС/ОПКЦ сохраняется | Расширяется scope, принцип неизменен |
| AD-002 | Единый источник истины — статусная машина | Добавляются две статусные машины: согласие и рекуррентное списание; атомарность «статус + outbox + аудит» сохраняется | Расширяется |
| AD-003 | Идемпотентность финансовых операций | Новые ключи: детерминированный ключ планового списания `{subscriptionId}:{periodKey}`, идемпотентность создания согласия, повторная инициация списания | Расширяется |
| AD-004 | Единственный адаптер ОПКЦ | Протокол рекуррентных списаний/согласий знает только адаптер; контракт opkc-adapter расширяется новыми методами | Принцип неизменен, контракт адаптера расширяется |
| AD-005 | Зачисление только из подтверждённого статуса | Сохраняется: зачисление ТСП только из подтверждённого НСПК статуса списания; добавляется предусловие «согласие активно» | Усиливается новым предусловием |
| AD-006 | Trust-зоны | Новых зон нет; согласие/токен — новые чувствительные данные внутри существующего контура | Не меняется |
| AD-007 | НПС/КИИ/ПДн | Согласие и токен плательщика — ПДн, новый аудит-журнал отзыва согласия; AML-мониторинг рекуррентных потоков | Усиливается (новая ПДн-поверхность) |
| AD-008 | Гибрид | Не меняется: ядро in-house + вендорский транспорт; scope RFP и контракта адаптера растёт | Не меняется (scope RFP растёт) |

NEW: AD-009 — "Рекуррентное списание — только из активного согласия плательщика в пределах лимитов".

**Deliverable #3: ADR-008** — the core decision.

Title: "Рекуррентные C2B-списания (подписки): согласие плательщика как мандат + повторное использование платёжной модели".

Context: 
- Business wants recurring C2B (subscriptions). Currently every payment = QR + payer action. Roadmap listed "автоплатежи" out of scope — this brings it in.
- SBP recurring = consent-based pull debit (analogous to card recurring / SEPA mandate). Payer authorizes once; TSP initiates subsequent debits without payer re-auth.
- Forces: financial safety (no double/unaututhorized debit), regulatory (161-ФЗ consent + revocation rights, ПДн, AML), NSPK protocol for recurring is external [ТРЕБУЕТ ПРОВЕРКИ], reuse of existing state machine/outbox/АБС/notifications.

Decision (one paragraph): 
Introduce a **"Согласие плательщика" (subscription/mandate)** as a first-class entity in the gateway with its own lifecycle state machine, and model each recurring debit as a **payment of type `recurring`** that reuses the existing payment state machine (CREATED→PAID→CREDITED→COMPLETED, no QR_ISSUED), the outbox, АБС integration (зачисление из PAID), and notifications. The consent manager + scheduler live INSIDE the payment contour (AD-001). Recurring debit is gated by AD-009 (active consent, within limits). The NSPK recurring protocol is only in the vendor adapter (AD-004), extended via opkc-adapter contract.

Key sub-decisions:
1. Consent = new entity + new state machine (PENDING_ACTIVATION → ACTIVE → REVOKED | EXPIRED | SUSPENDED).
2. Recurring debit = payment with `paymentType: recurring` + `subscriptionId`; reuse payment state machine (skip QR_ISSUED). NOT a separate financial entity.
3. Two initiation modes: (a) TSP pull (POST /payments with subscriptionId), (b) gateway scheduler (deterministic idempotency key {subscriptionId}:{periodKey}).
4. Consent capture channel: payer's bank app via NSPK (external, [ТРЕБУЕТ ПРОВЕРКИ]) — consent confirmation arrives as NSPK notification (eventId).
5. Limits enforced at gateway: per-debit max, period frequency, total cap, expiry.

Alternatives:
A. Separate "charge" financial entity + separate state machine (rejected: duplicates state machine/АБС/notifications; two financial models to reconcile).
B. Build recurring in a separate new service/initiative (rejected: same gateway/adapter/АБС, would duplicate trust zones, АБС integration, outbox; cost of a new component + БД).
C. Pure vendor recurring (rejected: vendor lock-in on financial logic, contradicts ADR-007).
D. Token-based card-on-file approach (store payer payment token and use card rails) (rejected: not SBP, different rails, doesn't meet "СБП-подписки" requirement).

Consequences:
Positive: reuse of proven state machine/idempotency/АБС/notifications; single source of truth for both one-off and recurring; minimal new surface (consent + scheduler); consent revocation is a first-class, auditable action; no double-debit (deterministic keys + limits).
Negative: consent lifecycle adds complexity (revocation race with in-flight debit → needs conflict resolution); scheduler adds a new component with its own failure modes (missed schedule, double-fire → mitigated by deterministic keys + сверка); NSPK recurring protocol is external gap [ТРЕБУЕТ ПРОВЕРКИ]; AML/dispute risk rises (revoked consent + in-flight debit, payer disputes); ПДн surface grows (consent + token).

Reversibility: reversible at the contract/entity level (consent can be deprecated, recurring debits can be stopped without affecting one-off payments); costly to reverse if consent data accumulates and NSPK recurring is deeply integrated. The `paymentType` discriminator keeps one-off path isolated → the recurring path can be feature-flagged off.

Expiry/trigger for revisit: when NSPK recurring protocol documentation is received (may change the consent capture flow); when regulator issues specific recurring-consent rules.

**Deliverable #4: Contract changes** (openapi/tsp-api.yaml).

Additive only:
1. `POST /v1/subscriptions` (create consent) — Idempotency-Key required.
2. `GET /v1/subscriptions/{subscriptionId}` (status).
3. `POST /v1/subscriptions/{subscriptionId}/cancel` (revoke by TSP, e.g. customer churn).
4. Extend `PaymentRequest` with optional `paymentType` (`oneOff` default | `recurring`), optional `subscriptionId`, optional `periodKey` (for scheduler idempotency).
5. Extend `Payment` with optional `paymentType`, `subscriptionId`.
6. New `Subscription` schema + `SubscriptionRequest`.
7. New webhook events (documented in prose; openapi may not cover webhooks — OpenAPI 3.0 doesn't natively model webhooks well, so I'll note them but the primary machine change is paths/schemas). Actually OpenAPI 3.0.3 doesn't have webhooks (that's 3.1). I'll keep webhooks out of the yaml or add a note. The current yaml doesn't include webhooks either (the prose tsp-api.md does). So I'll keep webhooks in prose only.

I need to make sure: no required fields added to existing request (PaymentRequest currently requires [amount, merchantOrderId] — I keep those required and add optional fields). No removal of existing paths/fields. No narrowing of types. The status enum stays the same (recurring debits reuse existing statuses). New enum `paymentType` is a NEW field with default.

Let me write the actual modified yaml.

**Deliverable #5: NFRs** (measurable, for the new functionality):

| NFR | Target | Method |
|---|---|---|
| Consent activation latency (from NSPK confirmation) | p95 < 2 s | APM |
| Consent revocation propagation to gate in-flight debits | ≤ 1 s to block new debits; in-flight debit → compensation per ADR | Test |
| Recurring debit initiation (TSP pull) | p95 < 500 ms (same as createPayment) | Load test |
| Scheduler on-time rate (debit fired within window) | ≥ 99,9 % within ±5 min of scheduled time | Metrics |
| Scheduler double-fire | 0 (deterministic idempotency key) | Test |
| Unauthorized debit (consent inactive/over-limit) | 0 — blocked at gateway | Test |
| Recurring throughput | sustains 200 TPS aggregate; scheduler batch 10k debits/hour without affecting interactive latency | Load test |
| Consent store availability | ≥ 99,95 % (same as gateway) | SLO |
| RPO/RTO | RPO=0, RTO ≤ 1 h (inherited) | DR |
| ПДн: consent/token encryption at rest | 100 % | Audit |
| AML: recurring flows to AML | 100 % of debits above threshold | Test |
| Double-debit (ретрай/повтор инициации) | 0 | Test |

**Deliverable #6: Acceptance criteria (EARS) + rollback.**

Acceptance criteria (readiness-gate, EARS):
- When ТСП создаёт согласие с корректными лимитами, the шлюз shall зарегистрировать согласие в состоянии PENDING_ACTIVATION и вернуть subscriptionId.
- When НСПК подтверждает согласие плательщика (eventId), the шлюз shall перевести согласие в ACTIVE идемпотентно по eventId.
- When плательщик отзывает согласие, the шлюз shall перевести согласие в REVOKED и заблокировать новые списания ≤ 1 с.
- When ТСП инициирует рекуррентное списание по активному согласию в пределах лимитов, the шлюз shall создать payment type=recurring и провести его по статусной машине.
- While согласие не ACTIVE (revoked/expired/suspended) or лимит превышен, the шлюз shall отклонить списание (403/422) без обращения к ОПКЦ.
- When scheduler повторно запускает тот же период, the шлюз shall вернуть существующий payment (идемпотентность по {subscriptionId}:{periodKey}), не создав дубль.
- When рекуррентное списание подтверждено НСПК, the шлюз shall зачислить средства на счёт ТСП только из PAID (AD-005).
- When отзыв согласия и in-flight списание конкурируют, the шлюз shall разрешить гонку детерминированно (списание, уже подтверждённое НСПК, завершается; не подтверждённое — отменяется/компенсируется).

Rollback:
- До боевой эксплуатации: откат = не включать feature-flag; всё обратимо.
- После включения: feature-flag отключает создание новых согласий и новых рекуррентных списаний; уже открытые списания доводятся по саге/сверке. One-off payments unaffected (изолированы по paymentType).
- Сигнал отката: доля отклонённых рекуррентных списаний (по вине шлюза) > X%; двойное списание (событие, отличное от 0); рассогласование сверки с НСПК по рекуррентным операциям > 0.
- Владелец решения: человек-архитектор + бизнес (A3/A5).

**Deliverable #7: Human architect (A3) decisions** — what stays open and why:
1. NSPK recurring protocol / consent capture channel — external gap [ТРЕБУЕТ ПРОВЕРКИ]. Can't be designed further without NSPK documentation. Decide: wait (like ADR-007 transport) vs build against assumption.
2. Consent model parameters (types: fixed-amount vs variable; max amount/frequency; open-ended vs fixed-term) — product/business + risk decision.
3. Scope of first wave (which verticals, pull-only vs scheduler) — business.
4. Dispute/chargeback handling for recurring — deferred, but recurring raises dispute risk; decide whether first wave needs it.
5. Whether to extend current feature spine (AD-009) vs promote to new initiative/parent spine — governance/ownership.
6. AML/compliance thresholds and consent-level monitoring — compliance.

Now, let me also think about the "what changes / what doesn't" more precisely for AD-005. The current invariant AD-005 is "Зачисление только из подтверждённого статуса" with binds to `PAID`. For recurring, the "confirmed status" is still PAID (NSPK confirms the debit). So AD-005 is unchanged in its rule, but there's a new PREcondition (consent active) that's NOT the same as AD-005 — it's a new invariant (AD-009). I'll articulate this clearly.

Now, let me think about whether I should also update docs/contracts/tsp-api.md and docs/contracts/opkc-adapter.md and docs/nfr.md and docs/solutioning.md. The task says "кратко перечисли созданные и изменённые файлы" and "Принятые файлы решения меняй только тем способом, который принят в этом репозитории". 

I think the cleanest, most defensible deliverable is:
- NEW files: ADR-008, recurring-state-machine spec, recurring-solutioning doc.
- MODIFIED: ARCHITECTURE-SPINE.md (add AD-009), openapi/tsp-api.yaml (additive).

I should NOT rewrite the existing ADRs, nfr.md, solutioning.md, or contracts prose — those are "accepted" and I'd extend via the new files + note deltas. Actually, docs/nfr.md and docs/contracts/tsp-api.md and docs/contracts/opkc-adapter.md could be extended, but the task specifically scopes contract changes to openapi/tsp-api.yaml. And for NFRs, the task says "Измеримые NFR для нового функционала" — I'll put them in the recurring-solutioning doc (a NEW file) rather than editing nfr.md, to avoid touching the accepted baseline. Similarly, the adapter contract extension (opkc-adapter.md) — I'll describe it as a delta in the solutioning doc and note it in the ADR, rather than editing the accepted file. Actually, extending opkc-adapter.md with new methods IS a legitimate change that the ADR references. But to keep the package focused and not over-edit accepted files, I'll document the adapter contract extension as a delta in the solutioning/ADR, and flag it as a follow-up to opkc-adapter.md + RFP.

Hmm, but actually the task item #2 says "Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет." This is about the ARCHITECTURE-SPINE.md invariants, which I'm addressing by adding AD-009 and describing impact in the solutioning doc.

Let me finalize the file plan and write the content. I'll write concise, high-quality documents following repo conventions (Russian, same header style as existing ADRs).

Let me draft the ADR-008 content carefully.

Actually, let me also double check: does the existing payment state machine have `REVERSED`? The state-machine.md spec lists states: CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED (financial) + ABS_PENDING, NOTIFY_PENDING (technical). ADR-002 mentions `REVERSED` as a state but the state-machine.md spec doesn't list it in the table. The openapi enum is [CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED]. So the canonical states are those 8. For recurring, I reuse these minus QR_ISSUED.

Now for the recurring debit, there's a subtlety: the debit can fail because the payer's account has insufficient funds or payer's bank rejects it. This maps to `FAILED` state. Also, a debit can be "pending" while waiting for NSPK confirmation — maps to `CREATED` (initiated, awaiting NSPK). So the recurring debit state machine:
`CREATED (инициировано) → PAID (подтверждено НСПК) → CREDITED (зачислено ТСП) → COMPLETED`, with `FAILED` (отклонено/недостаточно средств) and (for in-flight vs revocation) potentially a compensation → FAILED or REFUNDED.

This reuses the existing machine. Clean.

For the consent state machine:
`PENDING_ACTIVATION → ACTIVE → REVOKED | EXPIRED | SUSPENDED`, with REVOKED/EXPIRED terminal, SUSPENDED → ACTIVE (resume) possible. Actually, let me define: 
- `PENDING_ACTIVATION` (created, awaiting payer confirmation via NSPK)
- `ACTIVE` (payer confirmed)
- `REVOKED` (payer revoked — terminal)
- `EXPIRED` (TTL reached — terminal)
- `SUSPENDED` (temporary hold, e.g. failed debit too many times / risk — can return to ACTIVE)

That's clean.

Let me also address the "consent capture" flow concretely:
1. TSP creates subscription via API (POST /v1/subscriptions) → gateway registers consent in PENDING_ACTIVATION, requests NSPK to initiate consent (adapter: new method `initiateConsent`).
2. NSPK / payer's bank presents consent to payer in their app; payer approves.
3. NSPK sends confirmation notification (`consent.confirmed` eventId) → gateway transitions to ACTIVE.
4. Payer can revoke via their bank → NSPK sends `consent.revoked` → gateway transitions REVOKED. (Also TSP can cancel → gateway initiates revocation → NSPK confirms.)

This requires adapter contract additions:
- `initiateConsent` (ядро → адаптер)
- `getConsentStatus`
- `cancelConsent`
- `initiateRecurringDebit` (or reuse createPaymentLink with consent reference)
- events: `consent.confirmed`, `consent.revoked`, `consent.expired`, plus existing `payment.paid` etc. reused for debits.

Actually, whether the recurring debit reuses `createPaymentLink` or needs a new `initiateDebit` depends on NSPK protocol (external). I'll note this as a contract extension + [ТРЕБУЕТ ПРОВЕРКИ] flag, and keep the adapter contract extension as a documented delta (not editing the accepted opkc-adapter.md, but describing the delta in the solutioning doc). Actually, I think it's cleaner to add a short "delta" section describing the adapter contract extension in the solutioning doc, and note it as a follow-up to formalize in opkc-adapter.md + RFP.

OK. I think I have enough to write. Let me also verify the current date for ADR header: 2026-09-28 (today).

Now let me write the files. Let me be careful and thorough but concise.

Let me start with the ADR-008 file. I'll follow the existing ADR format (matching ADR-001..007 style: header with Date/Status/Owner/Related, then Context/Decision/Alternatives Considered/Consequences/Reversibility/References).

Then the spine AD-009 block.

Then the openapi yaml modification.

Then the state machine spec doc.

Then the solutioning doc (consolidating #1, #2, #5, #6, #7).

Let me write them. I'll write ADR-008 first.

Actually, let me reconsider the ordering of writes and whether I should run spine_lint + openapi_lint + contract_diff after. I'll write everything, then run spine_lint on ARCHITECTURE-SPINE.md, openapi_lint on the modified yaml, and contract_diff (old vs new) to verify backward compatibility.

For contract_diff, I need the OLD and NEW versions. I'll keep the old version in memory (I have it) and create the new version, then run contract_diff with a temp old copy? contract_diff takes old/new paths. I can write the old yaml to a temp file and diff. Actually, simpler: I'll rely on openapi_lint for the new file (which checks versioning/idempotency/errors) and manually ensure backward-compat (additive only). But the contract-gate skill says to run contract_diff. Let me do it properly: save a copy of the current yaml as a temp reference, then diff. Actually I can write the old content to `.qwen<TMP>.yaml` and diff against the new `openapi/tsp-api.yaml`.

Hmm, but I should minimize temp files. I'll create the new openapi/tsp-api.yaml by editing the existing file (additive edits), and I already have the old content captured in my context (I read it). I can write the old to a temp file for contract_diff. Let me do that.

Let me now also decide the exact openapi additions. Let me write the new full yaml (it's small, I'll just write the whole file with additions).

Current yaml:
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

New yaml — I'll add:
- PaymentRequest: add optional `paymentType` (enum oneOff/recurring, default oneOff), optional `subscriptionId`, optional `periodKey`.
- Payment: add optional `paymentType`, `subscriptionId`.
- New paths /v1/subscriptions (post), /v1/subscriptions/{subscriptionId} (get), /v1/subscriptions/{subscriptionId}/cancel (post).
- New schemas: SubscriptionRequest, Subscription, plus SubscriptionStatus enum.

For version: The info.version stays 0.1.0? The contract spec says v0.1 draft, path /v1, breaking changes → /v2. Additive changes are backward compatible within /v1. But should I bump info.version to 0.2.0? The openapi_lint checks "версионирование". Let me keep version 0.1.0 → actually, adding new endpoints is a MINOR additive change, so bumping to 0.2.0 would be semantically correct (minor). But the contract is pre-v1 (0.1 draft), not yet stable. The prose says "нестабильная; до A1 фиксируется v1.0-draft". So the version is 0.1.0 draft and these additions are still pre-v1. I'll bump to 0.2.0 to signal additive change, OR keep 0.1.0. 

The openapi_lint "версионирование" check — let me not overthink; I'll keep info.version 0.1.0 but actually, adding new endpoints IS a minor version bump. Let me bump to 0.2.0 (additive/minor). This is cleaner and signals the change. Actually, for a pre-1.0 draft that's still unstable, the exact number is less critical. But to be safe with openapi_lint's versioning check (which likely checks that info.version is semver and that breaking changes align with major version), additive changes with a minor bump should PASS. I'll use 0.2.0.

Wait, let me check what openapi_lint actually checks for versioning. The tool description: "версионирование, идемпотентность mutating-endpoint'ов, ошибки RFC 7807". It probably checks: (a) info.version is present and semver, (b) mutating endpoints (post/put/patch/delete) have Idempotency-Key or documented idempotency, (c) error responses use RFC 7807/problem+json.

Current yaml has NO error responses defined (no RFC 7807 components), yet openapi_lint returned PASS with 0 findings. So the lint is lenient here (maybe only checks what's present). So I shouldn't worry too much, but I'll keep idempotency headers on the new POST endpoints (Idempotency-Key required, matching createPayment).

Let me keep info.version at 0.2.0 for the additive change. Actually, let me reconsider — keeping it simple and consistent with the repo (which is at 0.1.0 everywhere and "pre-v1"), and the task is "без поломки существующих потребителей". A minor bump 0.1.0 → 0.2.0 is the correct signal. I'll do 0.2.0.

Now let me write all the files. I'll do the writes in sequence (they're independent, but I'll batch where possible). Actually write_file calls are independent, but I need to be careful about content. Let me write them one at a time to ensure quality, but I can batch the independent writes.

Let me write:
1. ADR-008 (new file)
2. ARCHITECTURE-SPINE.md edit (add AD-009 + update Deferred)
3. openapi/tsp-api.yaml (rewrite with additions)
4. docs/spec/recurring-state-machine.md (new)
5. docs/recurring-solutioning.md (new)

Let me draft each carefully now.

First, the ADR-008. Let me write it following the existing ADR header style exactly:

Existing ADR header format:
```
# ADR-001. Топология платёжного шлюза СБП: выделенный компонент с транзакционным outbox

- Date: 2026-08-15
- Status: Proposed
- Owner: solution-architect (платёжный контур)
- Related: ADR-002, ADR-004, AD-001, AD-002
```

I'll match this. ADR-008.

Let me write comprehensive but focused content.

For the ADR-008, I'll include the A3 decision marker note (that it needs human A3 decision) since it's a Critical route.

Let me write everything now.

Actually, one more consideration: the task says "чтобы его можно было вынести на архитектурное решение и затем передать исполнителям." So the package must be ready for A3 (human decision) AND handoff. This means the ADR should be "Proposed" (awaiting A3), and the solutioning doc should clearly separate what's decided vs what's open for A3.

Also note: the repo has a `.arch-handoff/` directory with a handoff package (TASK.md, ARCHITECTURE.md epic-context, CONSTRAINTS.yaml, etc.). Should I update the handoff package? The task says "затем передать исполнителям" — but the handoff package is for the CODE harneess (walking skeleton). For this new feature, the handoff would be a separate/new handoff. I don't think I need to modify .arch-handoff/ now — the task is to prepare the ARCHITECTURAL package (ADR, spine, contracts, NFR, acceptance), which comes BEFORE handoff packaging. I'll note handoff as a next step. I won't touch .arch-handoff/ (it's the accepted baseline for the walking skeleton, not for this new feature).

OK let me write. I'll be efficient and write all files.

Let me write the ADR-008 first.

For the amount of detail — the ADR should be one page-ish (not a 10-page epic). I'll keep it tight.

Let me write now.

Actually, I want to also reconsider the naming/terminology for the entity to be consistent. Options: "подписка" (subscription), "согласие" (consent/mandate), "автоплатёж". 

In SBP/NSPK terminology, the recurring consent is often called "согласие на автоплатёж" or "подписка". For the API, I'll use `subscription` as the resource name (ТСП-facing "подписка"), but internally the entity is "согласие плательщика" (consent/mandate). Let me use "Согласие (подписка)" and API resource `/v1/subscriptions`. In the ADR I'll clarify: subscription (ТСП) = согласие плательщика (mandate).

Actually, to reduce ambiguity, let me use a single consistent term in the docs: "Согласие плательщика на рекуррентные списания" (short: "согласие"/"подписка"), API entity `subscription`. I'll be explicit.

Let me write.

I'll write the ADR now with full content.
Инструменты подтвердили маршрут **Critical (8/15)**, и я изучил все методики. Ключевое наблюдение: в принятой архитектуре «автоплатежи» явно вынесены в roadmap/вне scope (`docs/solutioning.md` §1), а значит это расширение scope уже существующего фича-spine. Теперь готовлю пакет: ADR-008, инвариант AD-009, контракт, спецификацию состояний и solutioning-документ.

  `write_file(content="# Рекуррентные C2B-списания — спецификация статусных машин\n\n- Status: Draft (для ревью на гейте A1)\n- Owner: solution-architect (платёжн, file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/spec/recurring-state-machine.md")`

Now let me write the state machine spec doc.

  `write_file(content="# Solutioning — Рекуррентные C2B-списания (подписки СБП)\n\nИзменение поверх принятого решения «Платёжный шлюз СБП (C2B-приём)» (`docs/solu, file_path="<HARNESS>/runs/cells/spine-r2/ws/docs/recurring-solutioning.md")`

Now let me write the solutioning doc that consolidates #1, #2, #5, #6, #7.

Then modify ARCHITECTURE-SPINE.md to add AD-009, and modify openapi/tsp-api.yaml.

Let me write the solutioning doc.

  `edit(file_path="<HARNESS>/runs/cells/spine-r2/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now let me modify ARCHITECTURE-SPINE.md to add AD-009. I'll insert it after AD-008 and before the "Deferred" section. Also I should update the "Deferred" section? The Deferred section lists мультивалютность, C2C/B2C/B2B, диспуты. "Автоплатежи" is not in the spine's Deferred (it's in solutioning's roadmap). So I just add AD-009.

Let me read the exact current text around AD-008 and Deferred to do a precise edit.

I already have the full ARCHITECTURE-SPINE.md content from earlier. The relevant section:

```
## AD-008. Стратегия реализации — гибрид [ADOPTED]
...
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll insert AD-009 between AD-008 and the `---` + Deferred section.

Let me craft the AD-009 block following the existing format:

```
## AD-009. Рекуррентное списание — только из активного согласия плательщика

- Status: Proposed (ADR-008)
- **Binds**: менеджер согласий, статусная машина платежа, планировщик (scheduler), адаптер ОПКЦ, нотификатор ТСП.
- **Prevents**: списание без действующего согласия, превышение лимитов согласия, двойное списание одного расчётного окна, «зависшие» списания при отзыве согласия.
- **Rule**: Рекуррентное C2B-списание инициируется только из согласия в состоянии `ACTIVE`, в пределах его лимитов (max-сумма, частота/период, суммарный потолок) и срока действия; отзыв/истечение согласия блокирует новые списания. Гонка «отзыв vs списание в полёте» разрешается детерминированно: списание, подтверждённое НСПК (`PAID`), доводится до конца; неподтверждённое — отменяется. Плановое списание идемпотентно по ключу `{subscriptionId}:{periodKey}`. Проверка: fitness-тест «списание из не-`ACTIVE` недостижимо» + «повторное окно не создаёт дубль».
```

Now let me do the edit. I need the exact old_string with enough context.

Let me use the edit tool with the AD-008 Rule + the `---` + Deferred as context.

Actually, let me construct the precise old_string. From the read:

```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll replace this with the AD-008 Rule + `---` + AD-009 + `---` + Deferred.

Let me write the edit.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\npaths:\n  /v1/payments:\n    post:\n      operationId: createPayment\, file_path="<HARNESS>/runs/cells/spine-r2/ws/openapi/tsp-api.yaml")`

Now let me modify the openapi/tsp-api.yaml. I'll write the full new version with additive changes.

New version:
- version 0.2.0
- Add PaymentRequest optional fields: paymentType (enum oneOff|recurring, default oneOff), subscriptionId, periodKey
- Add Payment optional fields: paymentType, subscriptionId
- Add paths: /v1/subscriptions (post), /v1/subscriptions/{subscriptionId} (get), /v1/subscriptions/{subscriptionId}/cancel (post)
- Add schemas: SubscriptionRequest, Subscription, SubscriptionStatus enum

Let me write it. I need to preserve the existing structure exactly and only add.

For the POST /v1/subscriptions and cancel, I need Idempotency-Key header (mutating endpoints). The cancel is a mutation but idempotent by nature (revoking an already-revoked subscription returns the same state). Should cancel require Idempotency-Key? The existing createPayment requires it for POST. For consistency, I'll add Idempotency-Key to POST /v1/subscriptions (create). For /cancel, it's idempotent by nature (revoke is idempotent — revoking an already-revoked subscription is a no-op returning the same state). I'll add Idempotency-Key optional to cancel for safety, or just document idempotency. Actually, to keep it simple and match openapi_lint's expectation (mutating endpoints should have idempotency), I'll add Idempotency-Key required to POST /v1/subscriptions, and for /cancel I'll make it required too (harmless). Actually cancel/revoke is naturally idempotent. But to be safe with lint, let me add Idempotency-Key to both POST endpoints.

Hmm, but the existing lint passed with just createPayment having Idempotency-Key. Let me not over-engineer. I'll add Idempotency-Key required to POST /v1/subscriptions (create, needs idempotency), and for /cancel I'll note it's idempotent by nature (no key needed — like GET). Actually cancel is a POST mutation; to be safe I'll add Idempotency-Key as optional/required. Let me make it required for consistency with the "Idempotency-Key обязателен для всех POST" rule in the prose contract.

Wait, the prose contract says "Заголовок Idempotency-Key обязателен для всех POST." So both new POST endpoints should require it. Good.

Let me write the full yaml.

For the subscription schemas:

SubscriptionRequest:
- tspId (string, required)
- amountLimit (integer, optional — max amount per debit in kopecks; if absent, open-ended per-debit amount? but AD-009 says limits. Let me make amountLimit required for safety — actually "в пределах лимитов" means limits must exist. But product may allow open-ended. Let me make maxAmount optional with a note, and period required. Actually let me define a clean minimal set.)
- period (string, required — e.g. "P1M" ISO 8601 duration, or enum. Let me use ISO 8601 duration string.)
- maxAmountPerDebit (integer, optional, kopecks — max per single debit)
- maxTotalAmount (integer, optional — total cap)
- expiresAt (string, optional — date-time)
- paymentPurpose (string, optional)
- merchantSubscriptionId (string, optional — merchant's own reference)

Actually, let me keep it aligned with the existing PaymentRequest style (which is minimal). I'll define:

SubscriptionRequest:
- tspId: string (required)
- amountLimit: integer (max per debit, kopecks) — required (for safety/AD-009)
- period: string (ISO 8601 duration, e.g. "P1M") — required
- totalLimit: integer (optional, total cap in kopecks)
- expiresAt: string (optional, date-time)
- merchantSubscriptionId: string (optional)

Subscription:
- subscriptionId: string (required)
- status: enum [PENDING_ACTIVATION, ACTIVE, SUSPENDED, REVOKED, EXPIRED] (required)
- tspId: string
- amountLimit: integer
- period: string
- totalLimit: integer
- expiresAt: string
- merchantSubscriptionId: string

Let me write the full file now.

For the enum, I'll define a reusable `SubscriptionStatus` but inline is fine. I'll inline for simplicity, matching existing style (inline enum in Payment.status).

Let me write the whole yaml file.

  `tool_call(name="mcp__spine__spine_lint", arguments={"path": "ARCHITECTURE-SPINE.md", "cwd": "<HARNESS>/runs/cells/spine-r2/ws"})`
  `tool_call(name="mcp__spine__openapi_lint", arguments={"path": "openapi/tsp-api.yaml", "cwd": "<HARNESS>/runs/cells/spine-r2/ws"})`
  `tool_search(query="select:mcp__spine__contract_diff,mcp__spine__model_validate")`

Now let me verify:
1. spine_lint on ARCHITECTURE-SPINE.md (to ensure no dup AD-ids, empty fields, etc.)
2. openapi_lint on the modified yaml
3. contract_diff old vs new to confirm backward compatibility (no breaking changes)

For contract_diff, I need the old yaml saved. Let me save the old content to a temp file and run contract_diff. Actually, I have the old content. Let me write it to .qwen<TMP>.yaml, then run contract_diff.

Let me first get the contract_diff schema (I need old/new params).

Let me do these in parallel: run spine_lint, openapi_lint, and write the old yaml temp file + get contract_diff schema.

Actually, I need contract_diff schema first. Let me search for it.
Теперь проверю результат: линт спайна, линт контракта и diff-проверку обратной совместимости.

  `tool_call(name="mcp__spine__spine_lint", arguments={"path": "<HARNESS>/runs/cells/spine-r2/ws/ARCHITECTURE-SPINE.md"})`
  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.1.0\npaths:\n  /v1/payments:\n    post:\n      operationId: createPayment\, file_path="<HARNESS>/runs/cells/spine-r2/ws/.qwen<TMP>.yaml", record_as_artifact=false)`

spine_lint doesn't accept cwd. Let me re-run spine_lint with just path. Also I need to run contract_diff. For contract_diff I need old and new files. Let me write the old yaml to a temp file and run contract_diff.

Let me write the old yaml to .qwen<TMP>.yaml, and re-run spine_lint without cwd.

Let me do these in parallel:
1. spine_lint (path only)
2. write old yaml temp file

Then run contract_diff.

Actually, I need to write the old yaml first, then run contract_diff (dependent). Let me do spine_lint (retry) and write temp file in parallel, then contract_diff after.

For the temp file, I'll use .qwen/tmp/ which is appropriate for intermediate files.

Let me write the old yaml content to the temp file.

  `tool_call(arguments={"old": "<HARNESS>/runs/cells/spine-r2/ws/.qwen<TMP>.yaml", "new": , name="mcp__spine__contract_diff")`

spine_lint passes (0 issues). openapi_lint passes. Now let me run contract_diff old vs new to confirm no breaking changes.

  `tool_search(query="select:mcp__spine__fitness_check")`

All checks pass:
- spine_lint: 0 issues
- openapi_lint: PASS (0 findings)
- contract_diff: breaking=0, non-breaking=3 (only added paths)

Interesting — contract_diff detected only the 3 new paths as changes, but did NOT flag the added optional fields in PaymentRequest/Payment or the new schemas, nor the version bump 0.1.0 → 0.2.0. That's because the CD rules may only track paths as breaking/non-breaking, and optional field additions within existing schemas are non-breaking (and possibly the diff tool doesn't report schema-internal additive fields as findings). Anyway, the result is clear: 0 breaking changes, 3 non-breaking additions. 

Wait — there's a subtle concern: I bumped info.version from 0.1.0 to 0.2.0. The CD-007 rule is "ломающий дифф без смены major info.version". Since my diff is non-breaking (no major bump needed), 0.2.0 is a minor bump which is correct. And contract_diff passed. Good.

Actually, let me double check: the contract_diff found "breaking: 0" but only listed 3 path additions. It didn't mention the version change or the schema additions. But it returned passed=true. That's sufficient — no breaking changes.

Now let me clean up the temp file (delete it). Actually, it's in .qwen/tmp/ which is fine to leave, but let me remove it to be clean. Actually, the instruction says intermediate files in .qwen/tmp/ are fine and don't get registered as artifacts. I set record_as_artifact=false. I could delete it, but it's harmless in .qwen/tmp/. I'll leave it (it's in .qwen/tmp/ which is the designated temp area). Actually, let me delete it to be clean since it's an intermediate. But deleting requires a shell rm. It's low-risk. Actually, I'll just leave it — .qwen/tmp is explicitly for intermediates and won't be committed (it's likely gitignored). Let me verify it's not going to show up as an artifact concern. I set record_as_artifact=false, so it's not registered. It's fine.

Now, let me also run the fitness_check to make sure the CONSTRAINTS.yaml rules still pass (the existing rules reference docs/adr/ADR-001, docs/adr/ADR-005, docs/nfr.md, ARCHITECTURE-SPINE.md). My changes:
- Added docs/adr/ADR-008 — new file (adr-set-complete checks ADR-001 exists, still there). The `adr-no-placeholders` rule: `must_not_contain` pattern `<!--` in docs/adr/*.md. My new ADR-008 has no `<!--` comments. Good.
- ARCHITECTURE-SPINE.md: added AD-009, no TODO/TBD/XXX. Good.

Let me run fitness_check to be thorough (the MCP description says "Вызывать ПЕРЕД коммитом"). Since I'm not committing, but the task wants verification. Let me run it.

Also, I should consider whether to run trace_check — but there's no model/ directory, so it would report no model. Let me skip that (already confirmed no model/ dir).

Let me run fitness_check.

Actually, let me get the fitness_check schema. From the earlier tool descriptions, fitness_check has signature. Let me search it.

Actually, I recall from the system reminder the fitness_check tool exists. Let me just check its schema via tool_search, or I can try calling it with a cwd/path. Let me search.

  `tool_call(arguments={"path": "<HARNESS>/runs/cells/spine-r2/ws"}, name="mcp__spine__fitness_check")`
  `run_shell_command(command="rm -f \"<HARNESS>/runs/cells/spine-r2/ws/.qwen<TMP>.yaml\"", description="Удалить временный файл старого контракта")`

All checks pass:
- fitness_check: passed=true, 0 issues, no weakening.
- spine_lint: passed
- openapi_lint: PASS
- contract_diff: breaking=0

Now let me clean up the temp file (optional). I'll leave it since it's in .qwen/tmp/. Actually, let me remove it to be tidy. It's a low-risk delete of a temp file I created. I'll use run_shell_command rm. Actually, I could just leave it — .qwen/tmp is the temp area. But being clean is better. Let me delete it.

Actually, the instruction says intermediate files should be deleted when done. Let me delete the temp file.

Let me also verify the final state of the files I've created/modified is coherent. I think everything is in place. Let me do a final review of what I've produced and write the summary.

Actually, let me reconsider one thing: should I also check that there are no other places that need consistency. The README.md mentions the roadmap and "docs/contracts/tsp-api.md" as the contract. My openapi changes bump version to 0.2.0 but docs/contracts/tsp-api.md still says "v0.1 draft". I noted in the solutioning doc §8 "Зафиксировать openapi/tsp-api.yaml как v0.2 draft; обновить прозу docs/contracts/tsp-api.md". So this is a documented follow-up, not something I need to do now (the task scope item #4 is specifically openapi/tsp-api.yaml).

Also, the .arch-handoff/ package (TASK.md, ARCHITECTURE.md, etc.) is for the walking-skeleton handoff, not for this new feature. I correctly didn't touch it.

Let me also consider: did I miss updating the "Deferred" section of the spine? The spine's Deferred lists: мультивалютность, C2C/B2C/B2B, диспуты. "Автоплатежи" is NOT in the spine's Deferred (it's in solutioning.md's roadmap). So no spine Deferred change needed. Good. But wait — I should double-check: is "автоплатежи" mentioned anywhere in the spine? The ARCHITECTURE-SPINE.md I read doesn't mention автоплатежи/подписки/recurring anywhere. The solutioning.md roadmap mentions "автоплатежи". So the spine doesn't need a Deferred change; adding AD-009 is the correct change.

However, I realize I should also note in the spine or solutioning that this scope expansion removes "автоплатежи" from the roadmap/out-of-scope. My solutioning doc §1 already frames it as "вводит их в scope текущего фича-spine". The ADR context also says this. That's sufficient.

Now, let me do a final cleanup: delete the temp file. Then provide the summary.

Actually, let me reconsider whether deleting via rm is necessary or if I should just leave it. The temp file is in .qwen/tmp/. It's an intermediate. Per instructions: "Delete those intermediates when done." I'll delete it.

Let me delete it with a simple rm command.


Everything is done. Let me provide the final summary.

Let me summarize what was produced and the key results. The user asked for:
1. Significance assessment → Critical, 8/15 (done, in recurring-solutioning.md §1)
2. Impact on invariants → matrix in recurring-solutioning.md §2, AD-009 added to spine
3. ADR → ADR-008
4. Contract changes → openapi/tsp-api.yaml (additive)
5. NFRs → recurring-solutioning.md §5
6. Acceptance criteria + rollback → recurring-solutioning.md §6
7. Human architect decisions → recurring-solutioning.md §7

Files created/modified:
Created:
- docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-soglasie-platelshchika-kak-mandat.md
- docs/spec/recurring-state-machine.md
- docs/recurring-solutioning.md

Modified:
- ARCHITECTURE-SPINE.md (added AD-009)
- openapi/tsp-api.yaml (additive: subscriptions paths, paymentType fields, version 0.1.0 → 0.2.0)

Verification:
- significance_score: Critical, 8/15
- spine_lint: passed (0 issues)
- openapi_lint: PASS
- contract_diff: 0 breaking, 3 non-breaking
- fitness_check: passed (7 rules, 0 violations, no weakening)

Let me write a concise but complete final response in Russian (matching user's language). I'll present the 7 deliverables briefly and the file list.

I should be concise but cover all 7 deliverables since the user explicitly asked for a full package. Let me structure the final answer clearly.
Пакет подготовлен и проверен инструментами Spine. Итог по всем семи пунктам и список файлов.

## 1. Значимость и маршрут
`significance_score` → **Critical, 8/15** (сработало 8 триггеров: `new_component`, `new_datastore`, `cross_domain_integration`, `api_contract_change`, `data_contract_change`, `consistency_model_change`, `significant_nfr`, `financial_impact`). Поэтому — полный Solutioning + ADR + NFR, обязательная человеческая точка **A3**, walking skeleton до массовой реализации; дельта-спека недостаточна.

## 2. Влияние на инварианты
Сведено в матрицу (§2 `docs/recurring-solutioning.md`). Коротко: AD-001/AD-002/AD-003/AD-005 **расширяются** (новые компоненты и машины внутри контура, новые ключи идемпотентности, гейт активного согласия), AD-004/AD-008 **принципиально не меняются** (протокол НСПК — только в адаптере; scope RFP растёт), AD-006 **не меняется** (новых зон нет), AD-007 **усиливается** (новая ПДн-поверхность). Добавлен новый инвариант **AD-009** в `ARCHITECTURE-SPINE.md`.

## 3. Архитектурное решение
`ADR-008` (статус Proposed, ждёт A3): согласие плательщика — сущность первого класса со своей статусной машиной; рекуррентное списание — платёж `paymentType: recurring` поверх существующей машины (без `QR_ISSUED`); инициация pull/планировщиком с детерминированным ключом `{subscriptionId}:{periodKey}`. 4 отвергнутые альтернативы, последствия, обратимость `reversible`→`costly`, условие пересмотра.

## 4. Контракт `openapi/tsp-api.yaml`
Только аддитивно: пути `/v1/subscriptions` (POST/GET/cancel), опциональные поля `paymentType`/`subscriptionId`/`periodKey` в `PaymentRequest`/`Payment`, новые схемы `Subscription*`. `contract_diff` подтвердил **breaking: 0, non-breaking: 3**; `openapi_lint` → PASS; `info.version` 0.1.0 → 0.2.0.

## 5. NFR
Таблица (§5) — лаг активации согласия, лаг блокировки при отзыве (≤1 с), своевременность планировщика (≥99,9 % окон в ±5 мин), двойной запуск окна = 0, неавторизованное списание = 0, пакетная пропускная способность 10k/час, ПДн-шифрование 100 %, AML 100 %, RPO=0/RTO≤1 ч.

## 6. Критерии приёмки и откат
EARS-критерии (§6.1) + негативные сценарии; план отката (§6.2) — feature-flag, изоляция разового пути по `paymentType`, триггеры отката и владелец решения.

## 7. На решение человека (A3)
6 пунктов (§7): протокол/канал захвата согласия НСПК (`[ТРЕБУЕТ ПРОВЕРКИ]`), параметры модели согласия, состав первой волны, диспуты по рекурренту, граница фича-spine vs новый initiative, пороги AML.

## Проверка
`spine_lint` 0 находок · `fitness_check` passed (7 правил, 0 нарушений, ослаблений нет) · `openapi_lint` PASS · `contract_diff` 0 breaking.

## Файлы
**Созданы:**
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-soglasie-platelshchika-kak-mandat.md`
- `docs/spec/recurring-state-machine.md`
- `docs/recurring-solutioning.md`

**Изменены:**
- `ARCHITECTURE-SPINE.md` — добавлен AD-009
- `openapi/tsp-api.yaml` — аддитивные изменения контракта

Следующие шаги после A3 перечислены в §8 solutioning-документа (расширение `opkc-adapter.md`/RFP, фиксация контракта v0.2, walking skeleton, fitness-функции для AD-009).
