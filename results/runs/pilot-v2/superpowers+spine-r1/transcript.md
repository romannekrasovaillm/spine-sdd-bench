<!-- источник: <HARNESS>/runs-v2-pilot/cells/wyku3ck/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-v2-pilot-cells-wyku3ck-ws/chats/62962c9e-f5cd-4108-90ef-8b02ad590946.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `skill(skill="superpowers:using-superpowers")`

I'll start by loading the superpowers discipline skill, then explore the repository to understand the accepted decision.

  `glob(pattern="**/*")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/README.md")`

Let me explore the repository structure and read key files. Let me batch reads.

Let me look at the files: README.md, ARCHITECTURE-SPINE.md, .arch-handoff/ARCHITECTURE.md, TASK.md, CONSTRAINTS.yaml, MANIFEST.json, RUBRIC.yaml, connect-manifest.json, docs/*.

Let me glob first.
I'll now explore the repository to understand the accepted decision and its conventions.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/solutioning.md")`

Let me read the key architecture files. Let me batch several reads.
Let me read the core architecture documents in parallel.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/.arch-handoff/RUBRIC.yaml")`

Now let me read the handoff package, ADRs, NFR, contracts, and state machine. Let me batch.
Now let me read the handoff package, NFR, contracts, and state machine.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/openapi/tsp-api.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-007-proposed-a3.md")`

Now let me read the NFR, contracts, state machine, ADR-007, and openapi. Let me batch.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-001-outbox.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-002-model-konsistentnos)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-004-at-least-once-dlq.m)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-005-integraciya-s-abs-z)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-006-trust.md")`

Now let me read the remaining ADRs, contracts, state machine. Also the .arch-handoff/ARCHITECTURE.md and connect-manifest.json. And check .qwen/settings.json for MCP config.

Let me batch reads.

  `glob(pattern="docs/**/*")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/.arch-handoff/connect-manifest.json")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/.qwen/settings.json")`

Now let me read the contracts and state machine, and the .arch-handoff/ARCHITECTURE.md and connect-manifest.json. And check the docs/contracts directory. Let me glob docs.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/.arch-handoff/ARCHITECTURE.md")`

Let me read the contracts, state machine, and .arch-handoff/ARCHITECTURE.md. Also read the tsp-api.md contract (v0.1 in markdown). Also the openapi. Note the openapi/tsp-api.yaml is a minimal contract. Let me read.

  `skill(skill="delta-spec")`
  `skill(skill="significance-routing")`
  `skill(skill="adr-authoring")`

I now have a good understanding of the repository. Let me also check the RFP vendor doc briefly and understand the conventions for how decisions are recorded. The task asks to prepare an "architecture package" for the change — subscription/recurrent C2B payments (СБП subscriptions) on top of the accepted solution.

Key question: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — Accepted decision files must be changed only in the manner accepted in this repository. What is the way? The repo uses:
- ARCHITECTURE-SPINE.md — spine of invariants
- docs/adr/ ADR-NNN
- docs/solutioning.md
- docs/nfr.md
- contracts

There's a delta_guard concept (from the MCP server description): "Гейт прямых правок спайна мимо дельты (модель 5.2): каждый изменённый файл под защищёнными путями (по умолчанию model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.ya...". So there's a delta protocol — protected paths must be changed via a delta. There's a skill `delta-spec` (OpenSpec-style delta ADDED/MODIFIED/REMOVED). Also `adr-authoring` skill, `significance-routing`, `nfr-design`, `readiness-gate`, `semantic-review`, `adversarial-review`, `spine-invariants`, `spine-contracts-gate`, `fitness-functions`.

Let me check .git status/log to understand. Also, I should check whether there's an `openspec/` directory or a `model/` directory — they weren't in the file list. The delta protocol mentions "model/" and "ARCHITECTURE-SPINE.md", "CONSTRAINTS.yaml". There's no model/ dir here. Let me check the delta-spec skill and adr-authoring skill to understand the accepted way.

Also important: the task is architectural package preparation, not code. Let me determine the right skill set. Process skills first: the task is "подготовь архитектурный пакет изменения" — a design/creative work. superpowers:brainstorming says use before creative work. But this is a bank architecture task with its own methodology skills. The using-superpowers rule says process skills come first. Hmm. But brainstorming skill is about exploring user intent with questions. The user has given a very detailed request. Let me consider whether brainstorming applies. It says "You MUST use this before any creative work - creating features, building components, adding functionality". This is adding functionality (subscriptions) to an architecture. But the repo has domain skills specifically for this (adr-authoring, delta-spec, significance-routing, nfr-design). The instruction says "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению."

Given the guidance and the superpowers rule (1% chance → invoke), I should at least consider brainstorming. But brainstorming with a user who gave a fully specified deliverable list may be counterproductive; the task is quite specified. However, the rule is strict. Let me read the brainstorming skill to see if it applies... Actually, invoking a skill means loading its content. Let me be pragmatic: the highest-value skills here are the domain ones. The user explicitly enumerated deliverables — intent is clear. I'll load the domain skills that are directly relevant.

Actually, let me reconsider. The rule is extremely firm: "If you think there is even a 1% chance a skill might apply... you ABSOLUTELY MUST invoke the skill." And "Before entering plan mode: if you haven't already brainstormed, invoke the brainstorming skill first." I don't necessarily need plan mode. But "creative work — creating features... or modifying behavior" applies. Hmm.

However, there's also: "User instructions ... take precedence over skills". The user gave a concrete task. I think the intent is clear enough. But to be safe and compliant, let me quickly invoke brainstorming? That skill likely demands asking questions one at a time and designing. That could be a long detour. But the environment is a pilot/benchmark ("live-tui/runs-v2-pilot/cells/wyku3ck"). The task seems designed to test whether the agent produces an architecture package.

I think the best approach: use the domain methodology skills (adr-authoring, delta-spec, significance-routing, nfr-design, spine-invariants, fitness-functions, handoff-packaging, adversarial-review, readiness-gate). These are the "методические навыки" the user points at. And also use the Spine MCP tools: significance_score, change_impact, delta_guard, model_query, fitness_check, spine_lint, rules_suggest.

Given "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — protected paths (ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml, model/) must go through delta protocol. Let me inspect the delta-spec skill and check if there's a delta directory convention. Let me also invoke adr-authoring and significance-routing.

Let me first invoke the most relevant process/domain skills. Let me start with brainstorming to comply? Hmm, let me think about cost/benefit. Actually let me check the skill list: there is `superpowers:brainstorming`. The user's task is well-specified with 7 explicit deliverables. Brainstorming skill would have me ask the user questions. That's arguably appropriate but the user is not interactive here probably (pilot). Actually there is ask_user_question available. 

The user's request is explicit and comprehensive: "Что должно получиться: 1..7". This is essentially a spec/requirements given to me. So brainstorming (exploring requirements) is already satisfied by the user's detailed list. I'll note that.

Let me prioritize domain skills. Let me load several in parallel: adr-authoring, delta-spec, significance-routing, nfr-design, spine-invariants, fitness-functions, handoff-packaging. That's a lot of context. Let me be judicious: 
- significance-routing (deliverable 1)
- adr-authoring (deliverable 3)
- delta-spec (how to change accepted files)
- nfr-design (deliverable 5)
- fitness-functions (criterii priyomki)
- spine-invariants (deliverable 2)
- handoff-packaging (deliverable 7 / transfer)
- adversarial-review (self-review)
- readiness-gate (acceptance)
- spine-contracts-gate (deliverable 4)

Let me load them progressively. Start with the process-critical ones: delta-spec, significance-routing, adr-authoring.

Actually, since I must "announce 'Using [skill] to [purpose]' and follow the skill exactly. If it has a checklist, create a todo per item." — I should load and follow.

Let me load a first batch.
I have a clear picture of the accepted solution. Now let me load the project's methodology skills that govern this exact kind of work.

  `skill(skill="nfr-design")`
  `skill(skill="spine-invariants")`
  `skill(skill="fitness-functions")`
  `tool_search(query="select:mcp__spine__significance_score,mcp__spine__change_impact,mcp__spine__delta_guard,mcp__spine__fitness_check,mcp__spine__spine_lint")`

Now let me understand the delta/protected-paths mechanism. The delta_guard tool mentions protected paths. Let me check the spine tools available and run some. Also load nfr-design, spine-invariants, fitness-functions, handoff-packaging, spine-contracts-gate.

Let me also check git status and whether there's a `model/` dir or openspec. Glob showed no model/ dir. Let me check hidden dirs.

Let me run significance_score via spine MCP and delta_guard/change_impact. First, I need to understand tool schemas. Let me use tool_search to select: mcp__spine__significance_score, mcp__spine__change_impact, mcp__spine__delta_guard, mcp__spine__fitness_check, mcp__spine__spine_lint, mcp__spine__rules_suggest, mcp__spine__architect_review.

Actually, the MCP tools are "deferred" — I must review schema via tool_search then invoke via tool_call. Let me do that.

Also load remaining skills. Let me batch: skill loads (nfr-design, spine-invariants, fitness-functions, handoff-packaging, spine-contracts-gate) and tool_search selects.

Note skills and tool_search are independent — can be parallel. Let me do several.

Actually skill tool calls — can I make multiple skill calls in one block? Yes.

Let me batch: nfr-design, spine-invariants, fitness-functions. And tool_search for significance_score, change_impact, delta_guard, fitness_check, spine_lint.

Hmm, but loading too much at once floods context. Let me be measured but efficient. I'll load 3 skills + one tool_search.

  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && git status && echo \"---LOG---, description="Check git state and arch-be CLI availability")`
  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && arch-be delta --help 2>&1 | he, description="Inspect arch-be delta command help")`

Now let me check the delta guard mechanism: it mentions `changes/<name>/DELTA.md`. Let me inspect the repo for a `changes/` dir or `openspec/`. Glob earlier found no such dir. Let me check git log/status. Also let me run delta_guard and significance_score.

Actually, the task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." Since there's no `changes/` dir yet, the accepted way is the delta protocol (`arch-be delta new <name>`), which creates `changes/<name>/DELTA.md`. The delta_guard reads that. Let me verify: `arch-be delta new <name>`. I can run the CLI via shell to create the delta. Let me check arch-be availability.

Let me run a few things:
1. `arch-be --help` maybe
2. git status/log
3. significance_score via MCP
4. delta_guard via MCP (to see current violations)

Let me first check the repo state and arch-be CLI.

Also note: the task is Critical route (financial, security boundary). Per delta-spec skill: "Critical Path (платежи, КИИ, необратимые миграции, смена security boundary) — полный Solutioning, дельта недостаточна". So subscriptions (recurrent payments with payer consent) is a new security boundary (consent storage), financial impact, api_contract_change, consistency_model_change, criticality. So it's Critical → full Solutioning + human A3.

But protected files must still be changed via delta. The delta mechanism seems to be the repo's accepted way to modify spine/CONSTRAINTS. So I should create a delta that mentions the changed protected files, while also producing full solutioning artifacts (new ADRs, solutioning delta doc, NFR updates, contract changes, etc.).

Let me now gather tool outputs. Let me run the CLI and MCP tools.

Let me check arch-be CLI help for delta and rules.
Now let me check the repository's delta mechanism and run the Spine analysis tools.

  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && echo \"=== delta new ===\" && , description="Inspect delta subcommands and repository layout")`
  `tool_call(name="mcp__spine__significance_score", arguments={"triggers": ["api_contract_change", "data_contract_change", "security_boundary_change", "consistency_model_change", "significant_nfr", "new)`

Let me inspect `arch-be delta new --help`, `delta validate --help`, and check for `openspec` / specs. Also run significance_score and change_impact.

Let me also check `arch-be rules suggest`, `arch-be control check`, `arch-be evidence`.

Let me batch shell commands and MCP calls.

  `tool_call(arguments={"triggers": ["api_contract_change", "data_contract_change", "security_boundary_change", "consistency_model_change", "significant_nfr", "cro, name="mcp__spine__significance_score")`
  `tool_call(arguments={"path": "ARCHITECTURE-SPINE.md"}, name="mcp__spine__spine_lint")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws"}, name="mcp__spine__fitness_check")`
  `tool_call(arguments={"paths": ["openapi/tsp-api.yaml"], "cwd": "<HARNESS>/runs-v2-pilot/cells/wyku, name="mcp__spine__change_impact")`

Score 10 → Critical. Good. But let me also check `significance_from_diff` later, and `significance_score` with a well-justified set. Let me consider which triggers genuinely fire. I included 10; let me be honest about each:

- api_contract_change: yes (new endpoints/fields in tsp-api)
- data_contract_change: yes (new consent entity, new state, mandate data)
- security_boundary_change: yes — payer consent / mandate storage, recurring debit changes the trust model; new third-party (payer bank) interaction. Actually security_boundary_change is critical trigger. Recurring debits by consent = new authorization model. I'd argue yes.
- consistency_model_change: yes — recurring schedule, new saga (subscription lifecycle), possibly new state.
- significant_nfr: yes — recurring batch processing, peak windows.
- new_vendor: hmm — subscriptions in СБП use "СБП-подписки" / "автоплатежи" and may require a new ОПКЦ service. Does it need a new vendor? The existing transport adapter could be extended; the vendor's module must support subscription protocol. So not a new vendor per se, but a scope extension requiring vendor confirmation. I'd mark new_vendor=false to be honest (same НСПК channel, same vendor). Actually the transport adapter is vendor-supplied; subscriptions add new methods to the same contract — vendor capability extension, not a new vendor. So false.
- cross_domain_integration: yes — payer bank, ТСП subscription management, possibly new external domain (payer's bank consent).
- financial_impact: yes (recurring debits, refunds of subscriptions).
- criticality_or_exception: the payment gateway is КИИ/critical — yes.
- new_component: possibly a subscription/mandate service as a new component. Could be yes if we introduce a new component; or we can reuse the gateway. Since it's a significant new capability, a new component (Subscription Orchestrator / Mandate Registry) is likely. Mark true but note it's a design choice.

Even without new_component and new_vendor, score = 8 → Critical. So route is robustly Critical. Let me run significance_score with the honest set to get an accurate number, and also run significance_from_diff? The diff is empty (no changes yet). Better: run significance_score with honest triggers.

Actually the 15 triggers include "new_component" and "new_vendor". Let me be precise. I'll run with the honest set: api_contract_change, data_contract_change, security_boundary_change, consistency_model_change, significant_nfr, cross_domain_integration, financial_impact, criticality_or_exception → 8, Critical. And note new_component/new_vendor as design-dependent (deferred to A3). That's more defensible.

Let me run that.

Also run change_impact (no model/ dir → gaps). And delta_guard to see behavior. And rules_suggest. And model_query / trace_check / fitness_check to establish baseline.

Let me batch MCP calls. Need schemas for rules_suggest, trace_check, model_query, rules_report, evidence_verify, rubric_list, rubric_prompt, rule_template_list. Let me tool_search for those.

Actually let me be efficient. Steps:

1. establish baseline gates: fitness_check, spine_lint, trace_check, model_validate, nfr_check.
2. run significance_score honest.
3. change_impact.
4. rules_suggest.

Let me get schemas for the tools I need: fitness_check (have), spine_lint (have), change_impact (have), significance_score (have). Need: trace_check, model_validate, nfr_check, rules_suggest, rules_report, model_query, architect_review, verdict_explain, evidence_verify, rubric_list, rubric_prompt, rule_template_list, openspec_coverage.

Let me tool_search select a batch.

Let me first run the baseline checks I have schemas for, plus the honest significance score, in parallel.

  `tool_search(query="select:mcp__spine__trace_check,mcp__spine__model_validate,mcp__spine__nfr_check,mcp__spine__rules_suggest,mcp__spine__rules_report,mcp__spi)`

Baseline: spine lint clean, fitness passed, no model/ dir (change_impact needs model/). So the repo has a spine + constraints + ADRs, but no typed model/ directory. The trace_check may also fail due to no model. Let me check trace_check and rules_suggest.

Note: delta_guard default protected paths: model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. So if I modify ARCHITECTURE-SPINE.md I must have a delta mentioning it.

The accepted way in this repo to change protected files = delta protocol: `arch-be delta new <name>` then edit `changes/<name>/DELTA.md` to mention the protected files, then run `arch-be delta guard` to confirm passed=true. That's clearly "принятый способ".

Now, let me get more tool schemas: rules_suggest, rules_report, trace_check, model_validate, nfr_check, verdict_explain, rule_template_list, rubric_list, rubric_prompt, openspec_coverage, architect_review.

Let me tool_search select them. Max 20 results per query. Let me do a couple of queries.

Then run: trace_check, model_validate, nfr_check, rules_suggest, rules_report, rule_template_list.

Let me batch tool_search.

  `tool_search(query="select:mcp__spine__rule_template_list,mcp__spine__verdict_explain,mcp__spine__rubric_list,mcp__spine__architect_review,mcp__spine__openspec)`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws"}, name="mcp__spine__rules_suggest")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws"}, name="mcp__spine__rules_report")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws"}, name="mcp__spine__trace_check")`

Let me get the rest and run the checks. Let me batch: tool_search for remaining 5, plus run trace_check, model_validate, nfr_check, rules_suggest, rules_report.

Actually nfr_check/model_validate/trace_check require model/ which doesn't exist → they'll error. Let me still run rules_suggest and rules_report.

Let me run trace_check and model_validate to confirm, and rules_suggest + rules_report. And tool_search remaining.

Actually, to save round-trips: run rules_suggest, rules_report, trace_check, model_validate, nfr_check in parallel + tool_search remaining.

Wait — the repo has no model/ dir, so trace_check will error. But I should confirm. Let me run them anyway; errors are informative (they show the repo uses ADR+spine only, no typed model — an important finding for "gaps").

Let me do it.

  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && echo \"=== arch-be --help ===\, description="List arch-be CLI commands")`
  `tool_call(arguments={"cwd": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws"}, name="mcp__spine__rule_template_list")`
  `skill(skill="handoff-packaging")`
  `skill(skill="spine-contracts-gate")`

Good. Now I have a clear understanding:

- Route: Critical (score 8, robustly Critical regardless of new_component/new_vendor).
- Baseline gates: spine lint PASS, fitness PASS (7 rules, 0 behavior-checking rules).
- No model/ dir → typed model absent (trace_check, change_impact, nfr_check unavailable). This is a gap.
- rules_report: 0/7 rules check behavior. Candidate rule: ears_acceptance_criteria.
- Protected paths: model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. Delta protocol is the accepted way.

Now let me load remaining relevant skills: handoff-packaging, spine-contracts-gate, adversarial-review, readiness-gate, semantic-review, rubric-judging, spine-architect-review maybe. Let me load handoff-packaging and spine-contracts-gate (for contract changes) and readiness-gate (acceptance criteria EARS) and adversarial-review (self-review before A3).

Also rule_template_list to find executable rule templates (for fitness functions on new invariants like consent/mandate). And rubric_list + rubric_prompt for judging the ADR.

Let me be pragmatic. Key deliverables:
1. Significance + route — done (score 8 → Critical), will write doc.
2. Impact on architecture — invariants affected, what changes, what doesn't. → need spine delta + impact analysis.
3. Architectural decision with alternatives, consequences, reversibility → new ADR(s).
4. Contract changes (openapi/tsp-api.yaml) backward-compatible → edit openapi + docs/contracts/tsp-api.md.
5. Measurable NFR → docs/nfr additions.
6. Acceptance criteria + rollback plan → new doc (docs/spec or docs/acceptance).
7. What remains for human architect → A3 pack.

Plus: delta (propose) with DELTA.md to legitimately modify ARCHITECTURE-SPINE.md and CONSTRAINTS.yaml.

Let me decide the concrete artifact plan:

Artifacts to create:
- `changes/sbp-subscriptions/DELTA.md` — delta (propose) describing ADDED/MODIFIED/REMOVED, listing protected files it touches.
- `docs/adr/ADR-008-...` — new ADR for the subscriptions decision (mandate/consent model, recurrence engine, idempotency per charge, revocation). Possibly split into 2 ADRs: (ADR-008) subscription/mandate model & consent storage; (ADR-009) recurring charge execution & failover. Let me think about the single most load-bearing decision.

Actually, the request says "Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью." — one architectural decision (with alternatives). Given ADR discipline of "one decision per ADR", and route Critical, I could produce:
- ADR-008: Модель подписки СБП: рекуррентные C2B-списания по согласию плательщика (mandate) — core decision.
Potentially ADR-009: Хранение и проверка согласия плательщика (consent/mandate) — but that might be part of ADR-008.

I think a clean split:
- ADR-008: Модель подписки и мандата (mandate) — единый источник согласия, статусная модель подписки, связь платежей с мандатом.
- ADR-009: Рекуррентный движок списаний (scheduling, retries, dunning, failover) — or fold into 008.

Hmm. To keep it focused and avoid "ADR-эпос", two ADRs is reasonable: one for the mandate/consent domain model (data + lifecycle), one for the recurrence execution engine (scheduling/consistency). But we must be careful: "Рассмотренные альтернативы обязательны" per ADR. And alternatives across many axes.

Actually let me reconsider — the change is significant. A good package:
1. `docs/solutioning-sbp-subscriptions.md` — solutioning delta (full Solutioning since Critical): context, scope, components, flows, status model, gates, rollback, gaps. Actually the repo has `docs/solutioning.md`. Following delta discipline, I should create a change-scoped solutioning doc rather than rewrite the accepted one. The delta gets archived into the living truth later.
2. New ADRs.
3. NFR additions.
4. Contract updates (openapi + tsp-api.md).
5. Acceptance criteria + rollback.
6. A3 decision pack (human decision).
7. Delta file + protected file changes to spine and CONSTRAINTS.

Modifying ARCHITECTURE-SPINE.md: add new AD blocks (AD-009…?) and update Deferred (remove "автоплатежи" from roadmap? Actually solutioning §1 lists "автоплатежи" as roadmap/out of scope; now it's in scope). Per delta-spec, the delta should record ADDED/MODIFIED. Then ARCHITECTURE-SPINE.md is updated to reflect the live truth. But changing spine requires the delta to mention it.

Hmm, but should I actually modify ARCHITECTURE-SPINE.md, or leave it to `apply`/`archive`? The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The accepted way includes the delta protocol. In propose phase, the delta describes intent; the actual protected-file edit happens... The delta_guard checks that changed protected files are mentioned in the delta. So both the delta and the spine edit coexist in the change (propose), and `archive` merges into living truth. Given the deliverable is "prepare the package so it can go to architecture decision and then be handed to implementers", the cleanest is:

- Propose delta with DELTA.md (intent + affected invariants).
- Apply spine changes directly (AD blocks) BUT guarded by the delta mentioning ARCHITECTURE-SPINE.md. Actually, wait: is modifying the spine part of "propose" or "apply"? The delta-spec cycle: propose = delta + обоснование (audit trail of intent BEFORE implementation). apply = implementation. archive = delta merges into living truth.

"Живая истина" = the spine/specs. So the spine gets updated at archive time, not propose. But delta_guard's model 5.2 explicitly allows protected-path edits as long as they're in an active delta. So the mechanism supports editing spine during the change, tracked by delta.

Given the task wants the invariant impact described and the package ready for A3, I think the right approach:
- Create the delta (propose) with DELTA.md.
- Edit ARCHITECTURE-SPINE.md to add the new invariant blocks (marked Proposed, pending A3), and update Deferred. This is "the accepted way" (delta-tracked).
- Update CONSTRAINTS.yaml with new fitness rules.
- Create ADRs (Proposed).
- Update openapi + contracts.
- Update nfr.
- Create solutioning delta doc, acceptance criteria + rollback doc, A3 pack.
- Run gates: delta guard, fitness, spine lint.

But wait — should new AD blocks be `Proposed`? Yes, since A3 is human and not yet given. Spine says "блоки в статусе Proposed действуют после ратификации соответствующего ADR". Perfect fit.

Now, is there an `adr_new` tool? The skill mentions tool `adr_new` and `/adr new`. Let me check if arch-be has `adr` command. Let me check `arch-be --help`.

Let me also check `arch-be rules template list` via `rule_template_list` MCP.

Let me run: arch-be --help, arch-be adr --help, and tool_call rule_template_list.

Also load skills handoff-packaging, spine-contracts-gate, readiness-gate, adversarial-review, rubric-judging. Let me load a batch (they're needed for deliverables).

I'll be mindful of context, but it's fine.

Let me do parallel: shell help + rule_template_list + skill loads (handoff-packaging, spine-contracts-gate, readiness-gate).

  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && echo \"=== adr ===\" && arch-b, description="Inspect arch-be adr, handoff, control subcommands")`
  `tool_search(query="select:mcp__spine__openapi_lint,mcp__spine__contract_diff,mcp__spine__evidence_verify,mcp__spine__rubric_prompt")`

Now I have all the mechanism knowledge. Let me also check `arch-be adr --help`, `arch-be handoff --help`, `arch-be rubric --help`, and whether `adr new` exists for creating ADR. Let me check quickly. Also `arch-be control --help`, `arch-be rules template show consent-before-auto-action`.

Actually, the `rule_template_list` shows a very relevant template: `consent-before-auto-action` — "Согласие до автодействия: без записи о согласия действие не создаётся". Perfect for subscriptions (recurring debit requires consent). Also `idempotency-key`, `append-only-journal` (audit), `single-source-of-truth`.

Now let me check the CLI for adr creation and rules template apply dry-run.

Let me run: arch-be adr --help, arch-be handoff --help, arch-be rubric --help, arch-be control --help.

Also I want to verify openapi_lint on current tsp-api.yaml and contract_diff capability. Let me look at openapi_lint schema and run it on current file to see baseline findings.

Let me tool_search select openapi_lint, contract_diff, asyncapi_lint, rubric_list, rubric_prompt, evidence_verify.

Actually I already have schemas for rubric_list? No — rubric_list was in the select list but truncated? Let me re-check: the second tool_search returned rule_template_list, verdict_explain, rubric_list, architect_review, openspec_coverage. Yes rubric_list and architect_review are available.

I still need openapi_lint and contract_diff schemas. Let me select them.

Let me batch: shell (adr/handoff/rubric help) + tool_search (openapi_lint, contract_diff, evidence_verify, rubric_prompt).

Then run openapi_lint on current tsp-api.yaml baseline.

Let me proceed.

  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && echo \"=== control adr new ===, description="Inspect ADR-new, score, rubric, and consent rule template")`
  `tool_call(arguments={"path": "openapi/tsp-api.yaml", "cwd": "<HARNESS>/runs-v2-pilot/cells/wyku3ck, name="mcp__spine__openapi_lint")`

`arch-be control adr` = "Новый ADR". Let me check its help. That's the accepted way to create a new ADR.

Let me run `arch-be control adr --help`, and `arch-be control score --help` to see how significance is computed (to record exact invocation), and `arch-be control gate --help`.

Also run openapi_lint on the current contract for baseline.

Let me batch.

  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && arch-be delta new sbp-subscrip, description="Create delta skeleton for the subscriptions change")`
  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && echo \"=== control (full) ===\, description="List all control subcommands and gate help")`

The `rules template show` output was truncated at "Согласие до автодейс" — probably it tried to render with some terminal width. Let me get full output with `--help`? Actually let me try `arch-be rules template show consent-before-auto-action 2>&1 | cat` or check exit. Let me instead use `arch-be rules template show consent-before-auto-action` with a wider approach. Maybe output has ANSI. Let me try piping through `sed`? Better: capture to a file and read it. Actually, output truncation "Согласие до автодейс" suggests a bug/truncation in the description line. Let me try the MCP `rule_template_show`.

Let me use mcp__spine__rule_template_show for consent-before-auto-action and idempotency-key and single-source-of-truth.

Now baseline openapi_lint on the current contract PASSES. Good.

Now, let me also consider: do I need to run `arch-be control score --from-diff`? The diff is empty. Once I make changes, I can run it to demonstrate anti-bypass floor. Good idea to run after edits.

Let me now plan the actual work. I should write a plan/todo. The task is complex and multi-step. I'm in default mode (not plan mode). I don't need to enter plan mode (user didn't ask). I'll proceed with implementation but keep a todo list mentally/in responses.

Let me define the artifact set precisely.

## Deliverables mapping

1. **Оценка значимости и маршрут** → section in a new change document `changes/sbp-subscriptions/DELTA.md` + dedicated doc `docs/changes/sbp-subscriptions/00-significance.md`? Hmm. Let me think about repo conventions. The repo keeps docs/ flat-ish: solutioning.md, nfr.md, adr/, contracts/, spec/, rfp/. There's no changes/ dir yet (delta creates it).

I think the cleanest: create the change package under `changes/sbp-subscriptions/`:
- `DELTA.md` (required by delta protocol) — ADDED/MODIFIED/REMOVED + affected protected files.
- `SOLUTIONING.md` (or `DESIGN.md`) — full solutioning delta answering items 1–3,6,7.
- `NFR.md` — new NFR (item 5) OR update docs/nfr.md.
- `ACCEPTANCE.md` — criteria + rollback (item 6).
- `A3-DECISION.md` — human decision pack (item 7).
- `ADR-008...`, `ADR-009...` — new ADRs (item 3).

Hmm, but ADRs conventionally live in `docs/adr/`. The `arch-be control adr <title> --dir` command creates a new ADR in docs/adr by default. The delta references them. I'll create ADRs in `docs/adr/` (accepted location), and the rest under `changes/sbp-subscriptions/`.

But wait — creating ADRs in docs/adr/ modifies the "accepted solution" repo. Is that allowed? Adding new files is fine; the delta documents them. The protected path default is model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml — docs/ is not protected. So new ADRs in docs/adr are fine.

Also should I update `docs/solutioning.md`? It's not a protected path, but it's an "accepted decision file". The user says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The repo's accepted way for evolving the living truth is the delta + archive. So I should NOT rewrite docs/solutioning.md wholesale; instead the delta describes MODIFIED and I can add a change-scoped solutioning. Actually, modifying docs/solutioning.md directly is allowed (not protected) but the delta discipline says the truth gets updated at archive. To be safe and idiomatic: put the delta content in changes/, add small "MODIFIED" pointers if needed. I will avoid rewriting accepted docs; instead I'll append cross-references? Hmm.

Let me reconsider. The task explicitly asks: "Подготовь архитектурный пакет этого изменения поверх принятого решения" — prepare the architecture package of this change on top of the accepted solution. So a change-scoped package is exactly right: `changes/sbp-subscriptions/` with DELTA + ADRs + NFR + acceptance + A3 pack. The accepted files (spine, solutioning, nfr) get touched via the delta mechanism where needed.

Now, what about ARCHITECTURE-SPINE.md? Item 2 asks impact on invariants. Options:
(a) Add new AD blocks to the spine (AD-009...), status Proposed, and modify Deferred (remove автоплатежи from out-of-scope). This is the "living truth" evolution — normally at archive. But the delta protocol explicitly supports protected edits during a change. Since the user wants the package ready for A3 and then handoff, adding Proposed blocks now (tracked by delta) is defensible and demonstrates the mechanism.
(b) Only describe invariant impact in the delta, without editing the spine. Then handoff happens at apply/archive.

Hmm. The instruction "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" strongly implies I AM expected to change accepted files, but via the delta. So I'll do (a): create the delta, then edit the spine (ADV-... new blocks + AD-008 unchanged + Deferred update + Contracts/versions), and update CONSTRAINTS.yaml with new rules — both mentioned in DELTA.md, then run delta_guard to prove passed.

Wait — careful. Are new invariants needed at all? Per spine-invariants test: "Могут ли две единицы уровнем ниже, построенные независимо, выбрать несовместимо?" For subscriptions: 
- Mandate/consent as single source of truth & immutability of consent (who can create/cancel consent, what constitutes proof) → yes.
- Recurring charge idempotency key: each scheduled charge must have a deterministic key (mandateId + period + amount) so retries don't double-charge → yes, different from payment idempotency.
- No charge without active consent (consent-before-auto-action) → yes.
- Charge amount/date must match mandate terms; changes require new consent → yes.
- Revocation must stop future charges immediately but not orphan in-flight → yes (cancellation semantics).
- Payer notification before each debit (per НСПК rules) → likely.
- Refund of recurring charge follows existing refund saga → reuse.

So new spine blocks: 
- AD-009. Согласие плательщика (мандат) — единственный источник разрешения на рекуррентное списание. Binds: mandate registry, periodic charge engine, API ТСП, аудит-лог. Prevents: списание без действующего согласия; «вечное» согласие без срока/лимитов; подмену условий. Rule: заряд создаётся только при активном мандате; fitness: consent-before-auto-action.
- AD-010. Идемпотентность периодического списания по детерминированному ключу. Binds: движок списаний, статусная машина, адаптер ОПКЦ. Prevents: двойное списание при ретрае/перезапуске планировщика. Rule: ключ = (mandateId, periodStart, amount, currency); повтор → тот же chargeId, состояние не меняется. fitness: idempotency-key.
- AD-011. Жизненный цикл подписки отделён от платежа; отмена/приостановка останавливает будущие списания, не откатывая завершённые. Binds: subscription SM, scheduler, notifications. Prevents: списание после отзыва; откат уже проведённых платежей вместо возврата. Rule: после состояния REVOKED/PAUSED новые charges не создаются; отмена активного charge — только через возврат.
- Maybe AD-012. Прослеживаемость charge→mandate→payment in audit (already covered by AD-007). Probably not needed.

Keep spine 5–15 blocks. Currently 8; adding 3 = 11. Fine.

Hmm, but I should be careful not to over-engineer. The core load-bearing invariants for parallel implementers: consent authority (AD-009), charge idempotency (AD-010), lifecycle/revocation semantics (AD-011). Yes, three.

Now ADRs. Two ADRs:
- ADR-008: Модель подписки СБП: мандат плательщика как источник согласия, рекуррентные списания (domain model + charge lifecycle + idempotency). Alternatives: (a) хранить согласие на стороне ТСП, шлюз доверяет ТСП; (b) использовать существующий REQ_... ? Let me think of realistic alternatives for СБП subscriptions:
   1. **Мандат в шлюзе (выбран)** — банк хранит мандат, инициирует charges.
   2. **Доверие ТСП (шлюз — тонкий исполнитель)** — ТСП сам хранит согласие и присылает его; шлюз не проверяет мандат. Minus: нет доказательства согласия для регулятора/диспутов, риск списаний без согласия, банк несёт ответственность.
   3. **Регулярные платёжные ссылки (без мандата)** — напоминания плательщику, каждый платёж вручную (не рекуррентно, не решает задачу).
   4. **Вендорский модуль подписок** — vendor lock-in, закрытая логика consent (see ADR-007 hybrid constraints).

- ADR-009: Исполнение рекуррентных списаний: планировщик, распределённость и идемпотентность (single-writer per charge, outbox, retries/dunning, failover). Alternatives: (a) cron/scheduler per node without coordination → duplicate charges; (b) leader-election / sharded scheduler; (c) event-driven (queue with delay) via outbox; (d) external scheduler (vendor). Choose: outbox-based scheduler with per-charge idempotency + leader election for the tick. Hmm.

Actually maybe I'm overcomplicating. Let me consolidate: the request asks for "Архитектурное решение" (singular) with alternatives/consequences/reversibility. But Critical route + multiple load-bearing decisions → 2 ADRs is appropriate and ADR discipline says one decision per ADR. I'll write 2 ADRs:
- ADR-008 Модель мандата и подписки (согласие, домен, статусы).
- ADR-009 Исполнение рекуррентных списаний (планировщик, ключи идемпотентности, распределённость, ретраи/dunning).

Alternatively, ADR-009 could be "Отзыв согласия и остановка списаний" — but that's part of domain model.

I'll go with ADR-008 (mandate/subscription model) and ADR-009 (scheduler/execution semantics). Both Proposed, pending A3.

Also possibly ADR-010: Хранение согласия и ПДн (security) — but ADR-006 covers trust zones; mandate storage is PII, so I'll fold security into ADR-008/006 references.

Hmm, wait. There's another important decision: **how the charge reaches the payer's consent path in СБП**. In СБП, subscription/auto-payment (СБП-подписка) works via a "mandate" registered with the payer's bank through a payment (payer confirms once in their bank app), then the merchant/PSP can initiate charges. This is the realistic mechanism. The exact НСПК protocol details are [ТРЕБУЕТ ПРОВЕРКИ]. So ADR-008 should state the model at logical level and mark protocol details as external input.

Good — that aligns with AD-008 [ADOPTED] (core contract-independent of transport) and the existing pattern of marking НСПК details [ТРЕБУЕТ ПРОВЕРКИ].

Now contract changes (item 4): extend openapi/tsp-api.yaml + docs/contracts/tsp-api.md with subscription endpoints, strictly backward-compatible (additive):
- `POST /v1/subscriptions` (+Idempotency-Key) — создать подписку/мандат на согласие (инициировать регистрацию согласия; возвращает subscriptionId + consentUrl/QR для подтверждения плательщиком).
- `GET /v1/subscriptions/{subscriptionId}` — статус.
- `POST /v1/subscriptions/{subscriptionId}/suspend` and `/resume` and `DELETE /v1/subscriptions/{subscriptionId}` (revoke)? RESTful: `POST /v1/subscriptions/{id}/revoke`. Hmm, cancellation. Let me define:
  - `POST /v1/subscriptions/{subscriptionId}/revoke` — отзыв согласия/остановка будущих списаний (идемпотентно).
  - `GET /v1/subscriptions/{subscriptionId}/charges` — list charges.
- Extend `PaymentRequest` optionally with `subscriptionId` (optional) → additive.
- New webhook events: `subscription.activated`, `subscription.revoked`, `charge.completed`, `charge.failed`, `subscription.expiring`.
- Extend `Payment` enum? statuses unchanged. Add `chargeId` optional field.

Backward compatibility: all additive; existing consumers unaffected. Must not add required fields to existing schemas. Verify via contract_diff (old file vs new file) — need to produce new version file. Contract diff requires two files. I can create a copy? Better: run contract_diff with old = git show of original. I can create a temp file `openapi/tsp-api.yaml` original saved, e.g. write to .qwen/tmp? Actually contract_diff takes paths. I can create a saved copy of the original version and the new version. But the repo has only one file. Approach: 
- Save original to a temp path (e.g. `changes/sbp-subscriptions/contract/tsp-api.v0.1.yaml` as the "old baseline" evidence) — hmm, that pollutes.
- Or use `git show HEAD:openapi/tsp-api.yaml > /tmp/...`. Then contract_diff old=<TMP>.yaml new=openapi/tsp-api.yaml. That's clean. But temp outside workspace is fine for a check.

Actually better: bump version to 0.2.0 (minor, additive). Then contract_diff proves no breaking. Also openapi_lint both versions.

Wait: same file old vs new — contract_diff needs old content. I'll dump HEAD version to a temp file under `/tmp` or `.qwen/tmp/`. write_file is for content; but I can use shell redirection for `git show`. The tool guidance says avoid cat/echo redirection for writing files, prefer write_file. But `git show > file` is a legitimate shell operation producing a file from git (not echo). Hmm, instructions say "Write files: Use write_file (NOT echo >/cat <<EOF)". `git show HEAD:path > <TMP>.yaml` is a git operation; I think acceptable. Alternatively read the file via `git show` and write with write_file. Simpler: contract_diff accepts `old` path. I'll do `git show HEAD:openapi/tsp-api.yaml` piped into a temp file. It's a read-only extraction. Fine.

Now NFR (item 5): add subscription NFRs:
- Charge scheduling accuracy: scheduled charge initiated at T±X (e.g. ≤ 60 s of scheduled time), p95.
- Charge initiation→result latency; success rate.
- Consent registration success rate; consent confirmation latency.
- Duplicate charges = 0 (idempotency).
- Charge attempts per period bounded (max N retries) before dunning.
- Revocation propagation: stop future charges ≤ 5 min (or immediate before next scheduled).
- Scheduler scale: X subscriptions, Y charges/day sustained, Z peak on a billing day (e.g. 1st of month) — capacity.
- Availability of charge engine ≥ 99.95%.
- Audit: 100% charges traceable to mandate and consent evidence.
- Data: payer PII minimization, consent evidence retention (152-ФЗ + НСПК retention).
- Reconciliation: charges vs НСПК vs АБС.

I'll add a section to `docs/nfr.md`? That's an accepted doc, not protected. Hmm. Better: put new NFR in the change package (`changes/sbp-subscriptions/NFR.md`) as a delta (ADDED), referencing existing NFR. Or append to docs/nfr.md via MODIFIED delta. The delta discipline: delta describes MODIFIED; archive merges. For the package, I'll create `changes/sbp-subscriptions/NFR.md` containing the delta NFRs and note they're to be merged into docs/nfr.md at archive. Actually to keep everything self-contained for the arch committee + handoff, a change-scoped NFR doc is good. But the handoff packaging tool (arch-be handoff) reads --spec files. I'll produce a handoff package too? The task says "передать исполнителям" — but the request item list doesn't explicitly ask to generate the handoff package; item 7 is "что остаётся на решение человека-архитектора". Hmm: "чтобы его можно было вынести на архитектурное решение и затем передать исполнителям". So the package should be ready to be handed off. I should probably also refresh `.arch-handoff/` package for the new epic? The existing .arch-handoff is for the walking skeleton (baseline). I could generate a new handoff package via `arch-be handoff` (harness build?) — depends on whether the binary supports it ("Только сборка harness"). Let me check if `arch-be handoff` works in this build. Probably yes since it listed. But generating a full package may overwrite .arch-handoff. Risky. Better: include a "handoff readiness" section and the exact next command. Also perhaps create `changes/sbp-subscriptions/HANDOFF.md`. Actually the deliverable 7 explicitly covers "что остаётся на решение человека-архитектора", not the handoff generation. I'll include a handoff note.

Let me not overproduce. Let me define final artifact list:

Under `changes/sbp-subscriptions/`:
1. `DELTA.md` — delta spec (ADDED/MODIFIED/REMOVED), protected files mentioned, mapping to spine/ADR/NFR. Also includes significance+route (item 1) — or separate.
2. `DESIGN.md` — solutioning delta: context, scope in/out, components (C4 mermaid), flows (mermaid sequence for consent registration + charge), domain model (subscription states + charge states), impact on architecture (item 2), alternatives summary (item 3 pointer), rollback (item 6), gaps/open questions, A3 human decision pack (item 7). Maybe split into `DESIGN.md` + `ACCEPTANCE.md` + `A3.md`.

Let me make it cleaner with separate files:
1. `changes/sbp-subscriptions/DELTA.md` — delta + significance/route.
2. `changes/sbp-subscriptions/DESIGN.md` — impact + solutioning + flows + alternatives pointers + rollback.
3. `changes/sbp-subscriptions/NFR.md` — measurable NFR (item 5).
4. `changes/sbp-subscriptions/ACCEPTANCE.md` — acceptance criteria (EARS) + rollback plan (item 6).
5. `changes/sbp-subscriptions/A3-DECISION.md` — what's for the human (item 7) + machine-readable A3 pack {choice, rationale, constraints, rejected options, expiry}.
6. `changes/sbp-subscriptions/IMPACT.md` — maybe fold into DESIGN.
7. `changes/sbp-subscriptions/EVIDENCE.yaml`? Evidence bundle is for route profile. Could add if profile requires. Let me check evidence profile requirements — `evidence_verify` needs EVIDENCE.yaml in change dir. The route is Critical; evidence profile likely requires certain artifacts. I could generate it but without knowing the exact schema, risky. Let me check `arch-be gate --help` and `control gate --help` and maybe `evidence` command. Earlier `control gate` help says "A4 — conformance evidence: репетиция отката handoff-пакета". And `evidence_verify` mentions EVIDENCE.yaml. There may be a CLI to create it. Let me check `arch-be gate --help` and `arch-be control evidence --help`? control subcommands list was truncated at "fp". Let me get full list.

Let me run `arch-be control --help` fully (all subcommands) and `arch-be gate --help`.

This matters because the task wants a package ready for A3/acceptance, and evidence bundle is part of Critical route. But maybe too deep. Let me check.

Also I need the exact `delta new` output format to know DELTA.md structure. Let me just create the delta now via CLI (it creates changes/<name>/DELTA.md skeleton) and read it. That's the safest way to follow the accepted format.

Steps now:
1. Create delta skeleton: `arch-be delta new sbp-subscriptions`.
2. Read changes/sbp-subscriptions/DELTA.md.
3. Check control subcommands + gate help.

Let me do that.

Also: item ordering. Let me first create the delta (this is the "accepted way" and gives me the template).

Let me run.
Now let me create the delta (the repository's accepted mechanism for changing protected files) and inspect its required structure.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/DELTA.md")`
  `tool_call(arguments={"cwd": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws"}, name="mcp__spine__rubric_list")`
  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && arch-be control gate --help 2>, description="Inspect A4 evidence gate help")`

Let me read the generated DELTA.md skeleton to follow the format, and run `arch-be control gate --help` for evidence rehearsal details.

Also let me check `arch-be rubric list` for available rubrics (adr_quality, handoff_quality, etc.).

Let me batch read DELTA.md + rubric list.

  `skill(skill="readiness-gate")`
  `skill(skill="adversarial-review")`
  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && arch-be control adr \"Модель п, description="Create ADR-008 and ADR-009 skeletons via arch-be")`

The rubric assets dir is missing (home/.arch-harness/assets/rubrics). So rubric tools unavailable (no assets). That's fine — I'll note it. The `rubric_run` requires API keys anyway. I can use the RUBRIC.yaml in .arch-handoff as a rubric file path for `rubric run`? `arch-be rubric run <rubric> <file>` where rubric can be a path. But LLM judge needs API key. There's split-judge via MCP rubric_prompt + rubric_verify. Could be used for ADR quality. But rubric_list failed (no rubrics dir). rubric_prompt with a rubric path might work. I could do split-judge for my ADR using `.arch-handoff/RUBRIC.yaml` (handoff_quality) — but that rubric is for handoff packages, not ADRs. There's no adr_quality rubric available. So skip formal judging; note as gap. Actually the ADR skill mentions rubric `adr_quality`; but assets missing → would need API. I'll note that human/independent judging remains for A3.

Now, note the delta skeleton says: "Route: Fast|Standard (Critical — полный Solutioning, дельты недостаточной)". Interesting — the template's first line suggests delta is for Fast/Standard; for Critical, full Solutioning. But the delta mechanism is still the accepted way to touch protected paths. The user's task IS Critical. So I must do full Solutioning (change-scoped) AND use delta for protected edits.

Let me now plan and write. This is a big authoring task. Let me set up a todo list. Actually I can't create todos with a tool except write_todos via deferred? The Gemini mapping mentions write_todos but the available tools here don't include it (it's in the Gemini reference; the actual harness is Qwen Code). There's no todo tool exposed. I'll track mentally and in text.

Let me now decide file-by-file content. I need to be thorough but not bloated.

Given the scale, let me consider delegating some independent authoring to subagents. The Agent tool is available. Could delegate: (a) author ADR-008/009, (b) author NFR delta, (c) author acceptance+rollback, (d) author contract changes. But these need consistent domain reasoning; coordination cost is high, and they're interdependent (contract depends on domain model). The guidance says keep critical-path work local. I'll do the core design (DESIGN, ADRs, spine, delta) myself and could delegate the more mechanical parts. Actually, given quality matters and consistency, I'll author all myself — it's a coherent single design. Subagents would risk incoherence. But the task is large; delegation could help. Hmm. Let me consider delegating the contract file edit (openapi + tsp-api.md) after I fix the domain model in DESIGN. And maybe delegate the board/committee deck? The user didn't ask for pptx/docx. Skills like docx-* / pptx-* exist but the request didn't ask for documents in Office formats; it asked for an architecture package. I'll keep it in-repo markdown (the repo's convention). Good — repo convention is markdown files.

Let me be careful about scope creep: user listed exactly 7 outputs. I'll produce a package that maps 1:1 to those plus the mandatory delta.

Final artifact plan (concrete):

**Protected edits (via delta):**
- `ARCHITECTURE-SPINE.md`: ADD AD-009, AD-010, AD-011 (Proposed); MODIFY Deferred (автоплатежи/подписки removed from roadmap, now in scope); MODIFY "Контракты и версии" to mention tsp-api v0.2.
- `.arch-handoff/CONSTRAINTS.yaml`: ADD rules for new invariants (consent-before-auto-action, charge idempotency, revocation stops charges, audit) — but careful: adding `command_succeeds` requires the template skeleton (tests) which we don't have (no code). Since the stage is pre-code, `must_contain`/`file_exists`/`must_not_contain` rules are appropriate, plus we can add `command_succeeds`? No code → would fail. The existing CONSTRAINTS notes "Этап: решение (до кода)". So add text/traceability rules now, and note executable templates to apply at implementation. Actually the fitness-functions skill says have ≥1 executable per invariant that can be violated by code. But pre-code, there's no code. The `rule_template_apply` would create skeleton tests + lock file and print the rule fragment; applying it now creates skeleton/rule_templates/... That could be valuable: it produces the executable property tests for consent + idempotency that handoff uses. Hmm — but the skill says "apply кладёт тест, фейк и эталонную реализацию в skeleton/rule_templates/<id>/". Since the task says "Код не пиши" (don't write code), applying rule templates writes test code. That violates "Код не пиши". So I should NOT apply templates (they generate code). Instead: add non-executable traceability rules + explicitly record in DELTA the executable templates to apply at implementation (`consent-before-auto-action`, `idempotency-key`, `append-only-journal`), and add the rule fragment from rule_template_show? Adding a `command_succeeds` rule now would break the gate (no test file). So: add only rules that pass now, and put the executable ones into the delta's plan + a `rules_suggest`-style candidate section. Good.

  New rules to add (must pass baseline):
  - `consent_invariant_documented` must_contain ARCHITECTURE-SPINE.md pattern 'AD-009' (file_exists-like traceability) — actually must_contain regex.
  - `subscriptions_design_present` file_exists changes/sbp-subscriptions/DESIGN.md
  - `no-charge-without-consent-doc` must_contain DESIGN.md pattern 'без действующего мандата' (traceability)
  - `charge-idempotency-doc` must_contain DESIGN.md pattern 'mandateId.*period'
  - `revocation-stops-charges-doc` must_contain DESIGN.md pattern 'REVOKED'
  - `adr-008-present` file_exists docs/adr/ADR-008-*.md
  - `ears-criteria` warn must_contain ACCEPTANCE.md pattern EARS
  Hmm, that's a lot. Keep it moderate: 4–6 rules. But beware: rules with `owner/expiry` recommended. The existing rules lack owner/expiry. I'll add owner/expiry to new rules to be exemplary? The rules_report flags missing owner/expiry. Adding them to new ones is good practice. Let me include `owner:` and `expiry:` fields in new rules.

  Wait — do I actually need to modify CONSTRAINTS.yaml? The task says invariants affected and contract changes; fitness rules are the operationalization. It's "accepted way" to add rules via delta. Adding rules demonstrates the fitness-function discipline. I think yes, add a small set, guarded by the delta. But must ensure fitness_check still passes after adding.

  Actually, careful: `fitness_check` has anti-weakening check vs baseline; adding rules is fine.

- Also `delta_guard` protects `model/`, `ARCHITECTURE-SPINE.md`, `CONSTRAINTS.yaml` by default. I will edit ARCHITECTURE-SPINE.md and .arch-handoff/CONSTRAINTS.yaml. Note the protect default includes "CONSTRAINTS.yaml" — does it match `.arch-handoff/CONSTRAINTS.yaml`? The description says "по умолчанию model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml". It may match by basename/path suffix. The delta must mention them. i.e. `changes/sbp-subscriptions/DELTA.md` must mention those file paths. I'll include a "Protected files touched" section listing exact paths.

**Non-protected created files:**
- `changes/sbp-subscriptions/DELTA.md` (edited)
- `changes/sbp-subscriptions/IMPACT.md` — item 1 (significance/route) + item 2 (impact on invariants: touched/untouched).
  Actually let me name it `changes/sbp-subscriptions/SIGNIFICANCE-AND-IMPACT.md`. Hmm, long. Let me use `01-significance-impact.md`? The repo doesn't use numeric prefixes in docs/. I'll use `IMPACT.md` covering significance + impact (items 1–2).
- `changes/sbp-subscriptions/DESIGN.md` — solutioning delta: scope, components, flows, state models, alternatives summary, rollback (items 2/3/6 partial).
- `changes/sbp-subscriptions/NFR.md` — item 5.
- `changes/sbp-subscriptions/ACCEPTANCE.md` — item 6 (EARS criteria + rollback + handoff readiness).
- `changes/sbp-subscriptions/A3-DECISION.md` — item 7 + machine-readable A3 pack (item 3's human gate).
- `docs/adr/ADR-008-....md`, `docs/adr/ADR-009-....md` — item 3.
- `openapi/tsp-api.yaml` — item 4 (version 0.2.0, additive).
- `docs/contracts/tsp-api.md` — item 4 (doc).
- `docs/contracts/opkc-adapter.md` — extend adapter contract with subscription operations (mandate register, charge, revoke). This is needed because the core must speak to the transport for mandates. Yes, item 4 includes "Изменения контрактов". Add.
- `docs/spec/subscription-state-machine.md` — new spec (state machines for subscription & charge). This complements docs/spec/state-machine.md. Good.
- `docs/nfr.md` — should I modify? I'll keep NFR delta in changes/ and add a pointer line to docs/nfr.md? Modifying accepted doc directly is allowed (not protected) but delta discipline prefers archive merge. I'll add the NFRs in changes/ and add a short "MODIFIED/ADDED (delta)" note... Actually to be useful for handoff, arch-be handoff reads --spec files which can include changes/... . I'll keep docs/nfr.md untouched and reference the delta NFR. Hmm, but then "измеримые NFR для нового функционала" lives in changes/NFR.md — fine and self-contained.
  
  Wait, but the delta spec should record MODIFIED to docs/nfr.md? If I don't modify it, no need. I'll record in DELTA: "docs/nfr.md — не меняется; NFR-дельта в changes/.../NFR.md, вливается при archive". That's honest.

- Handoff readiness: `changes/sbp-subscriptions/HANDOFF.md`? Item 7 covers human decision, not handoff. I'll include handoff readiness inside ACCEPTANCE.md § and A3-DECISION.md. Plus mention `.arch-handoff/` refresh command. Actually the user said "чтобы его можно было ... затем передать исполнителям" — so I should at least state precisely how to generate the handoff (command + spec list) and what must be added. I'll put a "Handoff-готовность" section in A3-DECISION.md or ACCEPTANCE.md. Let me create a dedicated `changes/sbp-subscriptions/HANDOFF-READY.md`? Might be overkill. I'll fold into A3-DECISION.md as final section "После A3: путь к handoff".

Also should I update README.md? It describes the accepted solution status. Adding a line about the in-flight change would help. Not required. I'll add a brief "Изменения в работе" section — low risk, improves discoverability. Hmm, but "Принятые файлы решения меняй только тем способом, который принят" — README is not a decision file per se. I'll add a minimal pointer. Actually, let me be conservative and mention the change in the DELTA + add README pointer only if clean. I'll do a small README edit (it's a project index). Let me include it; it helps reviewers. Actually — to minimize risk of "changing accepted files unnecessarily", I'll skip README and note it. Hmm, but discoverability matters for the committee. Let me add one short subsection. I'll decide later.

Let me now think hard about the actual architecture design so the content is correct and high-quality.

## Domain design: СБП subscriptions (рекуррентные C2B-списания по согласию)

Terminology (Russian): «СБП-подписка» / «автоплатёж» / «рекуррентный платёж». Key entities:
- **Mandate (мандат/согласие)** — запись о согласии плательщика на периодические списания в пользу ТСП с параметрами: плательщик (payerRef), ТСП (tspId), счёт/маска, лимит суммы (per-charge max, при необходимости total), период/расписание (например monthly, day-of-month), срок действия, дата создания, статус.
- **Subscription (подписка)** — логическая привязка ТСП↔плательщик↔мандат↔услуга, управляемая ТСП (create/pause/resume/revoke), с расписанием.
- **Charge (списание)** — единичная попытка списания в рамках мандата за период; материализуется в платёж/операцию.

Question: is a charge a "payment" (reuse existing payment SM) or a separate entity? Design decision: reuse the payment domain (a charge creates a payment record linked to subscription/mandate) so that АБС crediting, refunds, notifier, reconciliation — all reuse. So Charge = Payment with `origin=SUBSCRIPTION` and `mandateId`/`subscriptionId`. This preserves AD-002/AD-005. Good: less new machinery, aligns with existing invariants. The new states are on the *subscription/mandate* aggregate, not on payment.

Subscription states: `PENDING_CONSENT` (создана, ждём подтверждения плательщиком в его банке) → `ACTIVE` → (`PAUSED` ⇄ `ACTIVE`) → `REVOKED`; plus `EXPIRED` (срок мандата), `FAILED_CONSENT` (плательщик отказал / таймаут). Terminal: REVOKED, EXPIRED, FAILED_CONSENT.
Charge states (within a billing attempt): reuse payment SM (CREATED→QR? no — recurring charge has no QR; it's a direct debit authorization). Hmm — this is important: for a mandate-based charge, the flow differs: no QR; the gateway sends charge instruction to ОПКЦ referencing mandate; НСПК debits payer; notification. So charge states: `SCHEDULED → INITIATED → (PAID) → CREDITED → COMPLETED`, with `FAILED`/`EXPIRED`. Possibly reuse payment statuses CREATED/PAID/CREDITED/COMPLETED and add SCHEDULED. And there's "payer notification before debit" — possibly a pre-notification window. Mark [ТРЕБУЕТ ПРОВЕРКИ] НСПК rules.

Also: charge idempotency key = `mandateId + periodStart + attemptSeq`? Must be deterministic across scheduler restarts: `(subscriptionId, periodStart)` for the logical charge; each retry reuses same chargeId; amount fixed at scheduling. Good: AD-010.

Authorization for charges from ТСП: Should ТСП be able to trigger an off-schedule charge (e.g., variable amount like ЖКХ)? Yes — some ТСП (ЖКХ, связь) charge variable amounts monthly. So there are two modes:
- **Scheduled fixed** (subscription with fixed amount) — engine initiates.
- **Merchant-initiated debit within mandate** (ТСП requests a charge ≤ limit within mandate terms) — e.g. variable utility bill. This is the СБП "автоплатёж" where ТСП can init charges with consent limits.
This is a key design axis → an ADR alternative/decision. I'll support both via `POST /v1/subscriptions/{id}/charges` (merchant-initiated) plus engine-generated charges for fixed schedules. Idempotency-Key required. Good.

Consent acquisition flow (logical):
1. ТСП calls `POST /v1/subscriptions` with terms (amount mode, limit, schedule, зачем).
2. Шлюз creates subscription PENDING_CONSENT + outbox → adapter registers mandate with ОПКЦ → returns consent URL/QR/deeplink.
3. Плательщик подтверждает в приложении своего банка (СБП).
4. ОПКЦ event `mandate.activated` (normalized) → subscription ACTIVE, store mandateRef, consent evidence (timestamp, channel, terms snapshot, payload hash) in immutable audit.
5. Charges proceed per schedule or merchant request.
6. Revoke: ТСП `POST /{id}/revoke` OR плательщик отзывает в своём банке (СБП event `mandate.revoked`) → REVOKED; future charges stop; in-flight charge completes or is cancelled per rules.

Impact on existing invariants:
- AD-001 (isolation): unchanged; subscriptions live inside gateway; adapter still only channel. Binds extended to mandate registry + charge engine.
- AD-002 (single source of truth, atomic transitions + outbox): applies equally to subscription state transitions; extend to subscription SM. MODIFIED in wording? The rule is generic; I'd say Binds extended. Add explicit mention.
- AD-003 (idempotency): extended with deterministic charge key (new AD-010) and mandate/consent dedup. Existing AD-003 covers messages; charge scheduling is new → AD-010.
- AD-004 (single ОПКЦ adapter): unchanged; adapter contract extended with mandate operations.
- AD-005 (credit only from PAID): unchanged and *critical* — recurring charge must also credit only from confirmed PAID. Reuse.
- AD-006 (trust zones): extended — mandate stores payer PII + consent evidence; new sensitive data class; consent evidence retention.
- AD-007 (audit/НПС/КИИ): extended — consent evidence must be immutable & auditable (new audit event types). AD-007 already requires audit of every financial transition; consent lifecycle is not financial but is regulatory evidence → AD-011? or fold into AD-007 wording. The new invariant AD-009 covers "no charge without active mandate" and consent evidence.
- AD-008 [ADOPTED] (hybrid, core contract-independent): unchanged and *binding* — subscription capability must be expressed via the internal adapter contract, so vendor module must support mandate operations (RFP constraint). This is a key "what changes/doesn't change" point: the vendor transport must support subscription protocol — RFP criteria extended. Also, if the current vendor can't, expiry condition of ADR-007 triggers.
- Deferred list: "автоплатежи" was listed as roadmap outside scope → now in scope → MODIFIED Deferred. Also "Диспуты" remain deferred; note that subscription disputes (payer disputes charge) may need to be added later.

New invariants (spine blocks):
- AD-009. Согласие плательщика — обязательное условие автоматического списания.
- AD-010. Идемпотентность периодического списания по детерминированному ключу.
- AD-011. Отзыв/приостановка согласия немедленно останавливает будущие списания; завершённые операции не отменяются (только возврат).

Do we need an ADR for the "где хранится согласие" (bank vs ТСП)? That's ADR-008 alternatives. Yes.

ADR-008: Модель подписки СБП: мандат плательщика как единственный источник согласия
- Context: business need, НСПК rules external, financial/regulatory (consent proof), ТСП in cinema/utilities/telecom, variable vs fixed amounts.
- Decision: gateway owns Mandate & Subscription aggregate; charge materialized as a payment (reuse SM/АБС/refunds/recon); consent evidence immutable; ТСП can initiate charges within mandate limits; engine drives fixed schedules.
- Alternatives: 
  1. Доверие ТСП (шлюз не хранит мандат) — rejected (no proof, risk, regulatory).
  2. Отдельная платёжная система/внешний сервис подписок (не через СБП, напр. рекуррентные карты) — rejected (не СБП, ТСП просят СБП; карты вне scope).
  3. Регулярные ссылки без мандата (напоминания) — rejected (не автоматизирует, не решает задачу).
  4. Полностью вендорский модуль подписок — rejected (см. ADR-007; consent — конкурентная зона/регуляторный след).
- Consequences +/- , Reversibility costly.
- Rejected: delegated to ТСП; card-based recurring; reminder links; full-vendor.

ADR-009: Исполнение периодических списаний: детерминированный ключ, единственный писатель, дunning и отказоустойчивость
- Context: scheduler must not double-charge; must survive restarts/scale; retries; payer funds may be insufficient (dunning); billing peaks (1st of month).
- Decision: (1) charge = детерминированный id `(subscriptionId, periodStart)`; idempotency by construction; (2) planning via outbox/delayed queue, single-writer per charge (leader-election/sharding by subscription hash), no distributed cron double-fire; (3) retries limited with backoff; dunning policy + notifications; (4) charges reuse payment SM & AD-005; (5) reconciliation includes mandates/charges; (6) capacity/peaks.
- Alternatives: naive per-node cron (double charges); external scheduler (vendor) — lock-in/opaque; pure event-driven without leader election (at-least-once duplicate planning) → mitigated by deterministic keys (chosen combined); synchronous batch at billing time (thundering herd) → offload with queue-load-leveling & jitter.
- Reversibility reversible/costly.

Hmm, these two ADRs are solid. Should I also add ADR-010 for security/PII of consent? Could fold into ADR-008 Consequences + ADR-006 reference. I'll fold and mention that security measures are an extension of ADR-006 requiring ИБ sign-off (part of A3). Good.

Now NFR (item 5), measurable, new:
- Scheduler accuracy: charge initiated within ±60 s of scheduled time (p95) for scheduled charges; and merchant-initiated charge accept p95 < 500 ms.
- Scale: base X subscriptions; sustained charges/day; peak on billing day (e.g., 5000 charges in a 1-hour window? need numbers). I'll propose baseline numbers consistent with existing gateway NFR (200 TPS sustained / 500 TPS peak). Charges: assume portfolio of N subscriptions; peak burst of charges on billing day. Let me set: sustained 50 charges/s, peak 300 charges/s for 10 min on billing day; scheduler lag p95 < 60 s. Mark as baseline to be confirmed with business/НСПК.
- Success/idempotency: duplicate charges per billing period = 0; charge attempts per period ≤ 3 default before dunning; idempotent replay keeps same chargeId.
- Consent: registration→activation p95 < X min? Depends on payer action. Consent activation event processed p95 < 5 s. Consent evidence completeness 100%.
- Revocation propagation: after REVOKED, no new charge attempts; any in-flight attempt either completes or is cancelled; guaranteed within ≤ 5 min (event processing) and never after the next scheduled window.
- Availability: charge engine ≥ 99.95%; consent registration ≥ 99.9%.
- Failure isolation: charge failure for one subscription must not delay others (bulkhead/queue).
- Audit: 100% charges traceable to mandate + consent evidence; immutable.
- Reconciliation: mandate/charge reconciliation with НСПК hourly, 0 discrepancies on completed.
- Data: consent evidence retention per НСПК/regulator; PII minimization.
- Notifications: payer pre-debit notification (per НСПК) delivered 100% before debit [ТРЕБУЕТ ПРОВЕРКИ].

Contract changes (item 4):
Extend `openapi/tsp-api.yaml` to v0.2.0 additive:
- paths: `/v1/subscriptions` (POST), `/v1/subscriptions/{subscriptionId}` (GET), `/v1/subscriptions/{subscriptionId}/revoke` (POST), `/v1/subscriptions/{subscriptionId}/charges` (POST create merchant-initiated charge; GET list), `/v1/subscriptions/{subscriptionId}/suspend`, `/v1/subscriptions/{subscriptionId}/resume`.
- schemas: SubscriptionRequest, Subscription, ChargeRequest, Charge, MandateTerms; extend Payment with optional `subscriptionId`, `chargeId`, `origin`.
- webhooks: add events.
- Keep everything additive; no changes to existing required fields; existing endpoints untouched.
Note ADR-003/ADR-014? The openapi_lint checks idempotency on mutating endpoints & RFC7807 errors. So new POSTs must have Idempotency-Key parameter and error responses RFC 9457. Let me check what openapi_lint verifies: "версионирование, идемпотентность mutating-endpoint'ов, ошибки RFC 7807". The current contract has none of the 4xx responses and only one endpoint with Idempotency-Key; lint still passed (0 findings) — maybe lenient. I'll add Idempotency-Key to all POSTs and problem+json responses to be safe.

Wait: does lint require `Idempotency-Key` header named exactly? Probably checks presence of a header param named idempotency-ish on POST. I'll add `Idempotency-Key` to each POST.

Also the current yaml uses `$ref:` inline with `{}` — valid YAML flow mapping with $ref key. version 0.1.0. I'll bump to 0.2.0. Minor bump for additive is right; openapi_lint may complain about breaking without major (CD-007) only if contract_diff finds breaking. Additive → no breaking → fine.

opkc-adapter.md additions: mandate register/revoke, charge initiation, events mandate.activated/revoked, charge.paid/rejected; normalized statuses; idempotency by reference; RFP constraint: vendor must support subscription protocol; test contour scenarios.

docs/spec/subscription-state-machine.md: tables for subscription states & charge lifecycle, forbidden transitions, idempotency, reconciliation, API mapping.

Acceptance (item 6) with EARS:
- When ТСП создаёт подписку without active mandate, the gateway shall not initiate any charge.
- When плательщик подтверждает мандат, the gateway shall activate the subscription and record immutable consent evidence ≤ 5 s from НСПК event.
- When наступает scheduled charge time, the engine shall create exactly one charge per (subscription, period) — duplicate planning yields same chargeId.
- When ТСП повторяет POST charge с тем же Idempotency-Key, the gateway shall return the same charge, no second debit.
- When мандат отозван, the gateway shall not create new charges after revocation; in-flight charge handled per policy.
- When charge подтверждён НСПК (PAID), the gateway shall credit АБС only from PAID (existing AD-005).
- When АБС недоступна, charge remains PAID and is retried/reconciled; not lost.
- When платёж отклонён (insufficient funds), dunning policy applies; ≤ N attempts; notifications.
- Backward compatibility: existing single-payment consumers unaffected.
- Rollback criteria.

Rollback plan (item 6):
- Pre-production: feature flag off by default; subscriptions capability behind flag; no migration of existing payments; rollback = disable flag (reversible).
- Post-launch: stop creating new charges (kill switch) while preserving existing mandates' data; revoke/settle in-flight; coordinate with НСПК for mandates (can't silently drop — must revoke mandates per protocol); data not deleted; no reverse migration.
- Signals/triggers: duplicate-charge metric > 0; consent evidence gap; charge success rate < threshold; АБС/НСПК errors.
- Owner of rollback decision: solution-architect + платёжный SRE lead + бизнес owner; A3 sign-off.
- RTO/RPO unaffected.

Human decisions (item 7):
- A3 approval of ADR-008/ADR-009 + spine AD-009..011.
- Choice of charge modes supported (fixed scheduled vs merchant-initiated variable vs both) — business/ТСП contracts.
- Dunning policy & number of attempts, notification windows (business + regulatory).
- Consent evidence retention period and PII scope (ИБ/комплаенс).
- Vendor capability confirmation: does the transport vendor support СБП subscription/mandate protocol? If not → ADR-007 expiry trigger; possible new vendor/RFP (human decision).
- Whether disputes for subscription charges are in scope (currently Deferred).
- Commercial: tariffs/limits per ТСП; max amounts.
- НСПК protocol specifics [ТРЕБУЕТ ПРОВЕРКИ] — external input.
- Whether to store mandate consent evidence in HSM-signed form / separate immutable store (ИБ).

Machine-readable A3 pack: {choice, rationale, constraints, rejected options, expiry}.

Also note dependencies/gaps: no model/ dir (trace_check/nfr_check/change_impact unavailable) → recommend authoring typed model for subscriptions or accept ADR+spine-only; vendor support; НСПК docs; АБС contract for partial refunds of charges; payer notification rules.

OK. Now also significance/route (item 1): score 8 (honest triggers) → Critical. Present the 8 fired triggers + 2 design-dependent (new_component/new_vendor) and why route robustly Critical. Also note the `--from-diff` anti-bypass floor will confirm after edits.

Now let me also think: does the task want me to actually run gates and show evidence? Likely good. I'll run delta guard, fitness, spine lint, openapi lint, contract diff at the end and report.

Alright. Also I should consider the adversarial-review and readiness-gate skills for the self-check. Let me load adversarial-review and readiness-gate and rubric-judging? I loaded neither adversarial-review nor readiness-gate yet. Let me load readiness-gate (for EARS criteria) and adversarial-review (self-critique before A3). And maybe semantic-review for the ADR-vs-spine check. Let me load those three — they're directly relevant deliverables (6 and Q7 quality).

Actually context is getting large. Let me load readiness-gate and adversarial-review now (needed), and defer semantic-review unless needed.

Hmm, adversarial-review and readiness-gate add value. Let me load them.

Then write files.

Let me plan the writing order:
1. ADRs (ADR-008, ADR-009) — core.
2. ARCHITECTURE-SPINE.md edits.
3. DELTA.md.
4. IMPACT.md, DESIGN.md, NFR.md, ACCEPTANCE.md, A3-DECISION.md.
5. docs/spec/subscription-state-machine.md.
6. openapi/tsp-api.yaml + docs/contracts/tsp-api.md + docs/contracts/opkc-adapter.md.
7. CONSTRAINTS.yaml rules.
8. Gates + contract diff.
9. Final summary.

Let me load the two skills, then write ADRs.

Also, should I create the ADRs with `arch-be control adr new` to get the repo's template? The skill says use adr_new tool (`arch-be control adr`). That creates a numbered ADR file with template. Let me try it to follow the accepted convention. Let me run `arch-be control adr "Модель подписки..." --dir docs/adr` and see. It will create ADR-008. Then I edit it. Let me do that for both. Actually creating with the tool ensures correct numbering + header format the parser understands. Let me do it.

Risk: it might create file with a slug that includes Cyrillic. The existing files have transliterated slugs (e.g. ADR-002-model-konsistentnosti-...). So the tool transliterates. Good.

Let me run adr new for both titles.

Let me also load readiness-gate + adversarial-review in parallel with the adr creation.
Let me load the remaining methodology skills and scaffold the new ADRs using the repository's own ADR tool.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-008-model-podpiski-sbp-)`

Let me read the generated ADR template to follow it exactly.

  `write_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-008-model-podpiski-sbp-, content="# ADR-008. Модель подписки СБП: мандат плательщика как единственный источник согласия\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: s)`

Note: the template lacks `Owner`, `Related`, and `Author model` lines, and uses HTML comments which the fitness rule `adr-no-placeholders` (must_not_contain `<!--`) will catch. So I must remove all `<!--` comments. Also I should add header lines Date/Status plus Owner/Related and `Модель-автор: qwen...`? The adr-authoring skill says the header should include date, status; and `- Модель-автор: <model>` is read by the judge. I'll add `- Модель-автор: qwen3-coder` (or "qwen-code (agent)"). The skill says write the label of the model if an agent assembled it. I'll use `- Модель-автор: qwen-code-agent`? Hmm, better a real model label. I don't know the exact model name. I'll write `- Модель-автор: qwen-code (agent)`. Hmm the parser reads `- Модель-автор: claude-opus-4` or `- Author-model: human`. Any value is fine. I'll use `qwen3-coder`.

Let me now write both ADRs fully. Then spine edits.

Let me write ADR-008.

Content for ADR-008:

Title: Модель подписки СБП: мандат плательщика как единственный источник согласия

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур) + владелец продукта C2B
- Related: ADR-002, ADR-005, ADR-006, ADR-009, AD-002, AD-003, AD-005, AD-009, AD-010, AD-011
- Модель-автор: qwen3-coder

## Context
Business: ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика («СБП-подписки»). Сейчас каждый платёж требует QR и действия клиента → отток подписчиков, ручные напоминания.
Gateway already has: status machine, outbox, idempotency, refund safari, credits from PAID, reconciliation (ADR-001..005), trust zones (ADR-006), hybrid strategy core/vendor transport (ADR-007, AD-008 adopted).
Forces: consent is a regulatory artifact (proof of authorization) and PII; НСПК subscription protocol details are external input [ТРЕБУЕТ ПРОВЕРКИ]; ТСП need both fixed recurring amounts (cinema) and variable (utilities); charges are financial → must reuse «credit only from PAID», idempotency, immutable audit; no new external vendor wanted beyond existing transport; competition zone — consent model is bank's responsibility.

## Decision
1. Gateway owns the **Mandate (мандат)** and **Subscription (подписка)** aggregates: единственный источник истины согласия плательщика, хранится в платёжном контуре (БД шлюза, AD-001/AD-002, trust zone ADR-006).
2. **Согласие обязательно до любого списания** (AD-009): charge создаётся только при действующем мандате, покрывающем сумму/период/ТСП; запись о согласии и его условиях — неизменяемое свидетельство (audit, AD-007).
3. **Charge материализуется как платёж**: единичное списание в рамках мандата создаёт платёжную операцию, переиспользующую существующую статусную машину, зачисление только из `PAID` (AD-005), возвраты (ADR-005), нотификации/сверку (ADR-004). Новых финансовых состояний не вводится.
4. **Два способа инициации** в рамках мандата: (а) плановые списания по расписанию — инициирует движок шлюза (ADR-009); (б) списания по запросу ТСП (переменная сумма, ЖКХ/связь) — ТСП запрашивает charge в пределах лимитов мандата с `Idempotency-Key`. Оба пути ведут к одной модели charge.
5. **Жизненный цикл подписки** — отдельный от платежа автомат: `PENDING_CONSENT → ACTIVE ⇄ PAUSED → REVOKED`, терминальные `FAILED_CONSENT`, `EXPIRED`. Отзыв (ТСП или плательщик через его банк) переводит в `REVOKED` и **останавливает будущие списания** (AD-011); завершённые операции не откатываются — только возврат по саге (ADR-005).
6. **Граница с транспортом** — по AD-008 [ADOPTED]: операции мандата (регистрация/активация/отзыв) и списания выражаются во внутреннем контракте адаптера ОПКЦ (`docs/contracts/opkc-adapter.md`); протокол НСПК знает только адаптер. Вендор обязан поддержать подписочные операции (расширение constraints RFP, ADR-007).
7. Детали протокола НСПК (схема подтверждения согласия плательщиком, сроки, предварительное уведомление, лимиты) — `[ТРЕБУЕТ ПРОВЕРКИ]`, уточняются по договору; логическая модель от них не зависит.

## Alternatives Considered
| Вариант | Плюсы | Минусы |
| Мандат в шлюзе (выбран) | Доказательство согласия и аудит у банка; контроль лимитов/периодичности; переиспользование финансового ядра и возвратов; нет нового вендора | Новый домен (мандат/подписка) и БД-сущности; ответственность за PII согласия; расширение контракта адаптера и требований к вендору |
| Доверие ТСП (ТСП хранит согласие, шлюз — исполнитель) | Минимум работы в шлюзе | Нет банковского доказательства согласия → регуляторный и диспутный риск; списание без проверяемого мандата; ПДн и ответственность размазаны |
| Рекуррентные карты вместо СБП | Зрелые схемы | Не СБП; ТСП просят именно СБП; вне границ текущего решения |
| Регулярные платёжные ссылки/напоминания без мандата | Ничего не меняем | Не автоматизирует: клиент всё равно платит вручную; задачу бизнеса не решает |
| Полностью вендорский модуль подписок | Быстрее старт | Consent и лимиты — зона ответственности банка; закрытая логика и аудит (см. ADR-007); lock-in |

Wait, the table format requires 3 columns (Вариант | Плюсы | Минусы). My rows have only 3 cells — good. But I need the header row and separator. In the template it's exactly `| Вариант | Плюсы | Минусы |`. I'll keep 3 columns.

## Consequences
Positive:
- Рекуррентные списания по согласию — новый бизнес для ТСП (кино, ЖКХ, связь) поверх уже принятого ядра.
- Consent-модель даёт банку проверяемое доказательство согласия (регуляторика, диспуты).
- Переиспользование статусной машины/АБС/возвратов/сверки: минимальное расширение финансовой логики.
- Лимиты и периодичность контролируются шлюзом, а не ТСП.
Negative:
- Новый домен мандата/подписки: сущности, миграции, эксплуатация; больше поверхность для ИБ/PII.
- Ответственность за корректность согласия, сроков хранения и предварительных уведомлений — на банке.
- Расширение контракта адаптера ОПКЦ и обязательств вендора; если вендор не поддержит — триггер пересмотра ADR-007 (смена транспорта — costly).
- Рост числа операций (много мелких списаний) → нагрузка на АБС/НСПК в пиковые дни.
- Частичные/неуспешные списания требуют dunning-политики (бизнес-решение, ADR-009).

## Reversibility
**costly.** До боевой эксплуатации — reversible (фиче-флаг, схема расширяема). После — отказ от модели мандата означает пересмотр согласий с плательщиками/НСПК и миграцию; данные и отчётность уже накоплены. Границы финансового ядра при этом не меняются.

## References
- AD-002, AD-003, AD-005, AD-009, AD-010, AD-011 (spine)
- ADR-001, ADR-002, ADR-004, ADR-005, ADR-006, ADR-007, ADR-009
- `docs/solutioning.md`, `changes/sbp-subscriptions/DESIGN.md`, `docs/spec/subscription-state-machine.md`
- НСПК: протокол подписок/автоплатежей — `[ТРЕБУЕТ ПРОВЕРКИ]` (документация Портала поддержки НСПК)

Good. Now ADR-009.

Title: Исполнение периодических списаний: детерминированный ключ, единственный писатель, dunning

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур) + SRE платёжного контура
- Related: ADR-002, ADR-004, ADR-005, ADR-008, AD-002, AD-003, AD-010, AD-011
- Модель-автор: qwen3-coder

## Context
Подписки порождают плановые списания по расписанию (напр., 1-е число месяца) и по запросу ТСП. Планировщик — источник риска дублей (двойное списание), пропусков (не списали) и штормов (все подписки в один момент). Шлюз масштабируется горизонтально (NFR ×2); несколько инстансов не должны «выстрелить» одним и тем же списанием. Канал к ОПКЦ — at-least-once; результат списания неопределён (ADR-002 forces: UNKNOWN). АБС/НСПК деградируют (ADR-004/005).

Forces: детерминизм (один charge на (подписка, период)), отказоустойчивость к рестартам/масштабированию, ограниченное число попыток, изоляция сбоя одной подписки, пиковые дни (первое число), наблюдаемость, откат без потери денег.

## Decision
1. **Детерминированный идентификатор charge**: `chargeId = f(subscriptionId, periodStart)` (плюс `attemptSeq` только как подсостояние попытки, не как новый charge). Повторное планирование/рестарт даёт тот же `chargeId`; идемпотентность — по построению (AD-010), а не «по удаче».
2. **Единственный писатель на charge**: планирование через **transactional outbox** (AD-002, ADR-001) и очередь с задержкой; «тик» планировщика защищён **leader election/lease** (ADR-*-см. leader-election) либо шардированием по `hash(subscriptionId)`; конкурирующие инстансы не создают дубль (идемпотентный INSERT по `chargeId`). Никаких независимых cron на каждом узле.
3. **Изоляция и сглаживание**: шардирование очереди по подпискам (bulkhead), сглаживание пиковой нагрузки (queue-based load leveling) и **джиттер** времени старта в окне ±N минут (не «все в 00:00:00»). Сбой одной подписки не задерживает остальные (competing consumers, DLQ).
4. **Повторные попытки и dunning**: ограниченное число попыток с экспоненциальной задержкой и джиттером (timeouts-backoff-jitter); при исчерпании — dunning-статус/уведомление, повтор в следующем окне; политика (число попыток, окна, уведомления) — бизнес-решение (A3).
5. **Неопределённый исход**: вызов списания при таймауте трактуется как UNKNOWN и **не повторяется вслепую** — разрешается сверкой/запросом статуса по `chargeId` (reuse ADR-004), затем либо продолжение, либо компенсация (avoiding-fallback / unknown-outcome-no-resend).
6. **Переиспользование финансового ядра**: charge не заводит новой логики зачисления — он создаёт платёж и далее AD-005 (`PAID` → АБС), ADR-005 (возврат сагой). Сверка (ADR-004/005) расширяется на подписки/charges (мандат ↔ charge ↔ платёж ↔ АБС).
7. **Наблюдаемость и kill switch**: метрики (плановые/созданные/успешные/дубли/лаг планировщика/DLQ), алерты, и отдельный «stop-new-charges» переключатель для отката (ACCEPTANCE).

## Alternatives Considered
| Вариант | Плюсы | Минусы |
| Детерминированный ключ + единственный писатель + очередь (выбран) | Дубли исключены по построению; переживает рестарт/масштабирование; сглаживание пиков; переиспользует outbox | Нужны leader election/шардирование и очередь с задержкой; сложнее отладка |
| Планировщик-cron на каждом узле без координации | Просто | Дубли при нескольких инстансах; «все в 00:00» → шторм; рестарт теряет/дублирует |
| Внешний планировщик (вендор/платформа) | Готовое расписание | Закрытая логика/иная семантика; не связано с транзакцией шлюза → риск рассинхрона; lock-in |
| Синхронный batch «списать всё в момент T» | Просто понять | Thundering herd на НСПК/АБС; нет backpressure; хрупко |
| Только event-driven без детерминированного ключа | Гибко | at-least-once → дубли; нет гарантии «один charge на период» |

## Consequences
Positive:
- «Один charge на период» — доказуемо (детерминированный ключ) и проверяемо тестом.
- Отказоустойчивость: рестарты/масштабирование не дублируют списания.
- Пиковые дни сглажены, сбой одной подписки не роняет поток.
- Переиспользование сверки/возвратов/АБС-идемпотентности.
Negative:
- Инфраструктурная сложность: очередь с задержкой, leader election/шардирование, DLQ — эксплуатационная нагрузка.
- Возможные задержки списания относительно «идеального» времени (окно ±N) — нужно согласовать с бизнесом/ТСП.
- Dunning и повторные попытки — новая бизнес-логика и уведомления.
- UNKNOWN-исход требует дисциплины сверки (иначе «висит» или двоится).

## Reversibility
**reversible.** Механику исполнения (очередь/планировщик/шардирование) можно заменить без смены модели мандата (ADR-008) и финансового ядра; ключ идемпотентности и контракт адаптера сохраняются.

## References
- AD-002, AD-003, AD-005, AD-010, AD-011 (spine)
- ADR-001 (outbox), ADR-002 (идемпотентность), ADR-004 (DLQ/сверка), ADR-005 (АБС/сага), ADR-008 (модель подписки)
- `changes/sbp-subscriptions/DESIGN.md`, `changes/sbp-subscriptions/NFR.md`, `docs/spec/subscription-state-machine.md`

Wait: template requires `## References` with placeholder; I'll fill. Also I must keep the exact section headings the parser expects: Context, Decision, Alternatives Considered, Consequences (Positive/Negative), Reversibility, References. Good.

One concern: ADR-009 references "leader-election" skill concept; fine.

Now, the spine. Let me write AD-009, AD-010, AD-011 blocks. Format:

## AD-009. Согласие плательщика — обязательное условие автоматического списания
- Status: Proposed (ADR-008)
- **Binds**: реестр мандатов, движок списаний, API ТСП, аудит-лог.
- **Prevents**: списание без действующего согласия; «вечный» мандат без срока/лимитов; подмену условий согласия после активации.
- **Rule**: `charge` создаётся только при мандате в состоянии `ACTIVE`, покрывающем ТСП, сумму и период; запись о согласии и его условиях неизменяема (append-only). Проверка: fitness `consent-before-auto-action` (executable-шаблон) + аудит.

## AD-010. Идемпотентность периодического списания по детерминированному ключу
- Status: Proposed (ADR-009)
- **Binds**: движок списаний, планировщик, статусная машина, адаптер ОПКЦ.
- **Prevents**: двойное списание при повторном планировании/рестарте/ретрае; разные `chargeId` для одного периода.
- **Rule**: `chargeId = f(subscriptionId, periodStart)`; повторное создание не создаёт второй эффект (тот же `chargeId`, состояние идемпотентно). Проверка: fitness `idempotency-key` (executable-шаблон).

## AD-011. Отзыв согласия останавливает будущие списания
- Status: Proposed (ADR-008, ADR-009)
- **Binds**: подписка (состояние), движок списаний, API ТСП, нотификации, адаптер ОПКЦ.
- **Prevents**: списание после отзыва/приостановки; откат уже проведённых списаний вместо возврата.
- **Rule**: после перехода подписки в `REVOKED`/`PAUSED` новые `charge` не создаются; зачисленные ранее операции не откатываются — только возврат (сага ADR-005). Fitness: проверка недостижимости создания charge из `REVOKED`/`PAUSED`.

Also I need to update Deferred: currently "- **C2C-переводы и выплаты B2C/B2B**..." and "- **Диспуты/претензии (disputes)**...". The solutioning §1 roadmap lists "автоплатежи" out of scope — but ARCHITECTURE-SPINE Deferred doesn't explicitly list автоплатежи. Let me re-check spine Deferred: it lists мультивалютность, C2C/выплаты, диспуты. No "автоплатежи". So no need to remove. But the solutioning.md roadmap (section 1) says "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." Since subscriptions now in scope, solutioning.md would need a MODIFIED note. Since solutioning.md is not protected but is an accepted decision doc, I'll record it in the DELTA as MODIFIED (текстовая правка при archive) and note it in IMPACT.md. Should I actually edit docs/solutioning.md? The delta discipline: MODIFIED entries describe changes; the living doc updates at archive. But leaving stale "автоплатежи вне scope" could mislead. Hmm. To keep the accepted doc truthful, I could make a minimal targeted edit to docs/solutioning.md line removing "автоплатежи" from out-of-scope and adding pointer to change. That's a legitimate MODIFIED. But the user said change accepted files only via accepted means — delta is the means; docs/solutioning.md isn't a protected path but the delta should still note it. I'll do a minimal edit and note it in DELTA.

Actually, wait. Let me reconsider whether to edit the spine at all vs just the delta. The instruction: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." I interpret: if you change accepted files, use the repo's mechanism (delta). I'll demonstrate it properly: edit spine + constraints + solutioning, all listed in DELTA, then delta_guard passes. Good — that's the strongest demonstration.

Let me also add to the spine's "Контракты и версии" a line: API ТСП v0.2 (delta подписок). And maybe add to Contracts section.

Now, the delta file itself must mention protected files. Let me design DELTA.md content:
- Title, Route: Critical, Created, Change name.
- Проблема.
- ADDED (requirements with EARS)
- MODIFIED (spine blocks, contracts, solutioning scope)
- REMOVED (none; or note nothing removed)
- Затронутые защищённые файлы (protected) — explicit list: ARCHITECTURE-SPINE.md, .arch-handoff/CONSTRAINTS.yaml. (delta_guard looks for mentions.)
- Новые артефакты
- Матрица влияния на инварианты
- План отката
- Критерии приёмки
- Гейты (что запускалось)

Hmm, but the delta format is fixed-ish (sections Проблема, ADDED, MODIFIED, REMOVED, План отката, Критерии приёмки). I'll keep those headings and add extra sections. `delta validate` may check structure. Let me keep the canonical headings and append "## Затронутые защищённые файлы" etc. Let me run `delta validate` after writing to confirm.

Now IMPACT.md: significance + route + invariant impact matrix (touched/not). DESIGN.md: full solutioning delta with C4 + flows + state models + alternatives summary + security + gaps. Actually I put state machines in docs/spec/subscription-state-machine.md. DESIGN can reference.

To avoid duplication, let me define:
- IMPACT.md: item 1 (significance/route, with the trigger table + tool output) + item 2 (what changes / what doesn't; invariant matrix).
- DESIGN.md: solutioning delta (context, scope, components C4, flows, state model summary, alternatives overview + pointers to ADRs, security/PII, integration/RFP impact, gaps, rollback summary pointer).
- NFR.md: item 5.
- ACCEPTANCE.md: item 6 (EARS acceptance criteria + rollback plan detail + readiness verdict).
- A3-DECISION.md: item 7 + machine-readable A3 + handoff path.

Also a review note: adversarial review findings — I should include a self-adversarial-review section (verdict NOT-READY/READY with findings) since the skill demands it and it strengthens the package. Where? Maybe `changes/sbp-subscriptions/REVIEW.md` — an adversarial self-review with open findings that feed A3. That's valuable and matches the "adversarial-review" skill (independent lens ideally, but I'll be honest it's a self-review; recommend independent review before A3). Hmm — the skill says reviewer=author is an antipattern. So labeling a self-review as "adversarial review" would violate the discipline. Better: produce `changes/sbp-subscriptions/OPEN-QUESTIONS.md`? Or fold open findings into A3-DECISION. I'll include a section "Состязательные находки (черновой проход, НЕ независимое ревью)" in A3-DECISION.md, explicitly flagged as needing an independent reviewer. That's honest and useful.

Alternatively, I could actually run an independent review via a subagent (fresh context, adversarial prompt) — that would satisfy the "independent contour" much better! The Agent tool with general-purpose subagent, run_in_background: false, given the design files and an adversarial brief. That's a strong move and matches the skill "independent contour". Cost: time. But high value and the task explicitly says "вынести на архитектурное решение" — should be reviewed. Let me do that after writing the design: dispatch a subagent with adversarial-review brief to review the package. Then incorporate findings.

Good plan. Let me now write files.

Let me start writing. I'll write ADR-008 first (edit the skeleton file fully via write_file), ADR-009 similarly.

Actually I must remove the `<!--` comments. I'll overwrite the whole files.

Let me write ADR-008.
Now I'll author the two ADRs. Let me write ADR-008.

  `write_file(content="# ADR-009. Исполнение периодических списаний: детерминированный ключ, единственный писатель, dunning\n\n- Date: 2026-09-28\n- Status: Propo, file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-009-ispolnenie-periodic)`

Now ADR-009.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-009-ispolnenie-periodic)`

I need to read ADR-009 first (it was created by CLI, I haven't read it). Let me read it, then write.

  `write_file(content="# ADR-009. Исполнение периодических списаний: детерминированный ключ, единственный писатель, dunning\n\n- Date: 2026-09-28\n- Status: Propo, file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-009-ispolnenie-periodic)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now let me update ARCHITECTURE-SPINE.md: add AD-009..011 and update Contracts/versions section. Let me use edit tool with precise context.

The spine file ends with "## Deferred..." then "## Контракты и версии". I'll insert new AD blocks after AD-008 and before "## Deferred".

Let me construct the edit. Old string: the AD-008 block ending + "---\n\n## Deferred".

AD-008 block ends with:
```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll replace `- **Rule**: ... НСПК.\n\n---\n\n## Deferred` with the rule + new blocks + --- + Deferred.

Let me write the new blocks.

Also update "## Контракты и версии" — add subscription contract line. Old:
```
- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec).
```
I'll add lines about v0.2 delta.

Let me do the edit. I'll do two edits.

Edit 1: insert AD-009..011.
Edit 2: update contracts section.

Let me be careful with exact text. From the read earlier:

```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

Good.

Contracts section:
```
## Контракты и версии

- Контракт НСПК: `docs/contracts/nspk-contract.md` — создаётся после получения документации НСПК; до этого все ссылки на протокол помечены `[ТРЕБУЕТ ПРОВЕРКИ]`.
- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec).
- Пиннинг версий зависимостей — в CONSTRAINTS.yaml (.arch-handoff) при передаче кодовому харнессу.
```

I'll add a second bullet for subscriptions. But careful — modifying existing bullet? I'll add new bullets rather than change the existing v0.1 line, plus a note that delta bumps to v0.2.

Let me do edits.
Now I'll extend the spine with the three new invariants (the protected edit that the delta authorizes).

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/ARCHITECTURE-SPINE.md", new_string="- Контракт НСПК: `docs/contracts/nspk-contract.md` — создаётся после получения документации НСПК; до этого все ссылки на протокол помечены , old_string="- Контракт НСПК: `docs/contracts/nspk-contract.md` — создаётся после получения документации НСПК; до этого все ссылки на протокол помечены )`

Now update the Contracts and versions section. Also add a Delta pointer. Let me edit.

Current text (from read):
```
## Контракты и версии

- Контракт НСПК: `docs/contracts/nspk-contract.md` — создаётся после получения документации НСПК; до этого все ссылки на протокол помечены `[ТРЕБУЕТ ПРОВЕРКИ]`.
- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec).
- Пиннинг версий зависимостей — в CONSTRAINTS.yaml (.arch-handoff) при передаче кодовому харнессу.
```

Add:
- Внутренний контракт шлюза (API ТСП): версия 0.2 (дельта подписок — `changes/sbp-subscriptions/DELTA.md`); v0.1 остаётся совместимой, изменения аддитивные — `openapi/tsp-api.yaml`, `docs/contracts/tsp-api.md`.
- Внутренний контракт адаптера ОПКЦ: расширен подписочными операциями (мандат/списание/отзыв) — `docs/contracts/opkc-adapter.md`.

Let me edit.

  `write_file(content="# Дельта: sbp-subscriptions — рекуррентные C2B-списания (СБП-подписки)\n\n- Route: **Critical** — значимость 8/15, полный Solutioning; одно, file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/DELTA.md")`

Good. Let me verify spine lint still passes (new blocks have Binds/Prevents/Rule, statuses). Let me run spine_lint. Actually I'll batch later. Let me continue writing.

Now let me write the DELTA.md (the key document). It must mention protected files: ARCHITECTURE-SPINE.md and .arch-handoff/CONSTRAINTS.yaml.

Let me write it with canonical sections. I'll include:
- header (Дельта: sbp-subscriptions, Route: Critical, Created, Owner)
- ## Проблема
- ## ADDED (EARS requirements)
- ## MODIFIED (spine blocks, contracts, scope)
- ## REMOVED
- ## Затронутые защищённые файлы (delta guard)
- ## Матрица влияния на инварианты (touched/untouched)
- ## Новые артефакты
- ## План отката
- ## Критерии приёмки
- ## Гейты и доказательства

But note: delta validate may require structure. Let me keep the required section names exactly (## Проблема, ## ADDED, ## MODIFIED, ## REMOVED, ## План отката, ## Критерии приёмки). Extra sections should be fine. Let me verify with delta validate after.

EARS requirements for ADDED — good to be concrete.

Let me write DELTA.md now. Actually, I want IMPACT/DESIGN etc. to exist before ACCEPTANCE references. Order doesn't matter for writing. But delta_guard will complain if I edit protected files without mention — I already edited spine; delta_guard must pass with DELTA mentioning it. So write DELTA now.

Let me compose carefully but not excessively long. This is the central change record.

Content:

# Дельта: sbp-subscriptions — рекуррентные C2B-списания (СБП-подписки)

- Route: Critical (значимость 8/15 → полный Solutioning; дельты недостаточно)
- Created: 2026-09-28
- Owner: solution-architect (платёжный контур)
- Паттерн: BMAD/OpenSpec delta (propose → apply → archive)

## Проблема
ТСП (онлайн-кинотеатры, ЖКХ, связь) просят списывать платежи автоматически по согласию плательщика. Сейчас каждый C2B-платёж требует QR и действия клиента. Нужны рекуррентные списания в рамках проверяемого согласия, без изменения финансовых инвариантов принятого решения.

## ADDED
Требования в нотации EARS (When <событие>, the <система> shall <реакция>):

- R1 Мандат. When ТСП создаёт подписку, the СБП-шлюз shall создать мандат в состоянии `PENDING_CONSENT` и инициировать подтверждение согласия плательщиком через ОПКЦ.
- R2 Активация. When ОПКЦ подтверждает согласие, the СБП-шлюз shall перевести подписку в `ACTIVE` и сохранить неизменяемое свидетельство согласия (условия, время, канал, хэш) ≤ 5 с.
- R3 Плановое списание. When наступает плановый период подписки, the движок списаний shall создать ровно один `charge` с `chargeId = f(subscriptionId, periodStart)`.
- R4 Списание по запросу ТСП. When ТСП запрашивает списание в пределах мандата, the шлюз shall принять его идемпотентно по `Idempotency-Key` и не превысить лимиты мандата.
- R5 Согласие обязательно. If мандат не `ACTIVE` или условия не покрывают списание, then the шлюз shall отказать в создании `charge` (AD-009).
- R6 Зачисление. When ОПКЦ подтверждает списание (`PAID`), the шлюз shall зачислить средства в АБС только из `PAID` (AD-005) и уведомить ТСП.
- R7 Отзыв. When ТСП или плательщик отзывает согласие, the шлюз shall перевести подписку в `REVOKED` и не создавать новые `charge` (AD-011).
- R8 Приостановка. While подписка `PAUSED`, the движок shall не создавать плановые `charge`.
- R9 Отклонение. If списание отклонено (недостаток средств и т. п.), then the шлюз shall применить ограниченную dunning-политику (повторы с джиттером, уведомления) и не терять операцию.
- R10 Неопределённый исход. If вызов списания вернул UNKNOWN/таймаут, then the шлюз shall разрешить исход сверкой/запросом статуса, не повторяя вслепую.
- R11 Совместимость. While существует потребитель v0.1, the API ТСП shall не ломать существующие пути/поля (только аддитивные изменения).
- R12 Изоляция сбоя. While один ТСП/подписка деградирует, the движок shall не задерживать списания остальных (bulkhead/шардинг).

## MODIFIED
- `ARCHITECTURE-SPINE.md`: добавлены AD-009, AD-010, AD-011 (Status: Proposed; действуют после A3/ратификации ADR-008/009). Секция «Контракты и версии» дополнена v0.2 API ТСП и расширением контракта адаптера ОПКЦ.
- `docs/solutioning.md`: в §1 из roadmap вне-scope выводится «автоплатежи» (становятся scope дельты); добавляется ссылка на дельту. Остальные инварианты/потоки — без изменений.
- `docs/nfr.md`: не переписывается; NFR нового функционала — в `changes/sbp-subscriptions/NFR.md`, вливается при `archive`.
- `docs/contracts/tsp-api.md` и `openapi/tsp-api.yaml`: версия 0.1 → 0.2 (аддитивно).
- `docs/contracts/opkc-adapter.md`: добавлены подписочные операции и события.
- `.arch-handoff/CONSTRAINTS.yaml`: добавлены fitness-правила дельты (см. ниже), включая исполнительные шаблоны на этапе реализации.

## REMOVED
Нет удаляемых требований/контрактов. Никаких REMOVED без замены (антипаттерн delta-spec).

## Затронутые защищённые файлы (для delta guard)
- `ARCHITECTURE-SPINE.md` — AD-009/010/011 + контракты.
- `.arch-handoff/CONSTRAINTS.yaml` — новые правила.
(ожидаемо `delta guard --base HEAD` → passed=true)

Hmm — delta_guard default protect is model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. Mentioning `.arch-handoff/CONSTRAINTS.yaml` — does the guard match "CONSTRAINTS.yaml" as prefix/suffix? Unclear. To be safe, mention both `.arch-handoff/CONSTRAINTS.yaml` and plain `CONSTRAINTS.yaml`. Let me phrase: "`.arch-handoff/CONSTRAINTS.yaml` (CONSTRAINTS.yaml)".

## Матрица влияния на инварианты
| Инвариант | Влияние | Что именно |
|---|---|---|
| AD-001 Изоляция | Без изменения правила | Подписки живут в том же платёжном контуре; новых каналов к АБС/НСПК нет. Binds расширен (реестр мандатов). |
| AD-002 Истина/outbox | Без изменения правила | Переходы подписки/charge — тоже атомарны с outbox/аудитом. |
| AD-003 Идемпотентность | Усилен | Добавлен детерминированный ключ charge (AD-010). |
| AD-004 Единый адаптер ОПКЦ | Без изменения | Контракт адаптера расширяется подписочными операциями. |
| AD-005 Зачисление из PAID | Без изменения (критично) | Charge зачисляется только из PAID. |
| AD-006 Trust-зоны | Усилен | Мандат хранит ПДн/свидетельство согласия — новый класс данных. |
| AD-007 НПС/КИИ/аудит | Усилен | Свидетельство согласия — неизменяемый аудит; новые события. |
| AD-008 Стратегия [ADOPTED] | Без изменения, но расширяет требования | Вендор транспорта обязан поддержать подписки; иначе — триггер пересмотра ADR-007 (human). |
| AD-009/010/011 | Новые | Согласие, идемпотентность списания, остановка при отзыве. |

## Новые артефакты
- `docs/adr/ADR-008-...` (Proposed), `docs/adr/ADR-009-...` (Proposed).
- `changes/sbp-subscriptions/IMPACT.md`, `DESIGN.md`, `NFR.md`, `ACCEPTANCE.md`, `A3-DECISION.md`.
- `docs/spec/subscription-state-machine.md`.
- Обновлённые контракты.

## План отката
(кратко, детали ACCEPTANCE.md)
- До прода: фиче-флаг, откат = выключить; миграций нет.
- После: stop-new-charges; отзыв мандатов по протоколу; завершение/сверка in-flight; данные не удаляются.
- Триггеры: дубли > 0, пробел в свидетельствах согласия, падение успешности, деградация АБС/НСПК.
- Владелец решения об откате: solution-architect + SRE-лид + бизнес-владелец (A3).

## Критерии приёмки
- [ ] Все R1–R12 покрыты EARS-критериями в ACCEPTANCE.md
- [ ] `fitness_check` passed=true; `spine_lint` passed=true; `delta guard` passed=true
- [ ] `contract_diff v0.1→v0.2` — 0 breaking; `openapi_lint` PASS
- [ ] Нет двойных списаний на тесте идемпотентности (R3/R4)
- [ ] Свидетельство согласия сохранено для 100% charges (R2/R5)
- [ ] Нет новых charge после REVOKED (R7)
- [ ] Совместимость v0.1 подтверждена

## Гейты и доказательства
- `arch-be control score` → Critical (8)
- `arch-be delta guard` → passed
- `arch-be control check` / `fitness_check` → passed
- `arch-be control spine` / `spine_lint` → passed
- `openapi_lint` → PASS; `contract_diff` → 0 breaking
- Оценка ADR рубрикой — не выполнена (нет активов рубрик `adr_quality`; требуется независимый судья/человек — см. A3-DECISION.md)

OK. Also mention "Независимое состязательное ревью — см. A3-DECISION/review". I'll add after subagent review.

Let me write DELTA.md. It's long but central.

Wait: delta_guard compares diff vs base HEAD. If I edited spine and constraints, guard checks DELTA mentions. Good.

Let me write it.
Now the central change record — the delta that authorizes the protected edits.

  `write_file(content="# IMPACT — значимость, маршрут и влияние на принятую архитектуру\n\nИзменение: **рекуррентные C2B-списания по согласию плательщика («СБП-по, file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/IMPACT.md")`

Now IMPACT.md (items 1–2). Let me write it with the significance trigger table, route rationale, and detailed impact.

Then DESIGN.md.

Let me write IMPACT.md.

Content plan:
# IMPACT — значимость, маршрут и влияние на принятую архитектуру

## 1. Оценка значимости
- Trigger table with 8 fired (+ 2 design-dependent).
- score 8 → Critical.
- Why Critical matters: full Solutioning, mandatory human A3, walking skeleton before mass generation, evidence gates.
- Anti-bypass note: `control score --from-diff` after edits should confirm floor.

## 2. Влияние на принятую архитектуру
### 2.1 Что НЕ меняется (стабильные основания)
- AD-001..AD-008 rules unchanged; AD-008 adopted.
- Financial core: статусная машина платежа, зачисление только из PAID, возвраты-сага, outbox, нотификации, сверка, адаптер ОПКЦ как единственный канал.
- Trust zones and crypto.
### 2.2 Что меняется
- New domain: mandate/subscription (new entities, new BД tables, new state machines).
- New component-ish: charge scheduler (logical component within payment contour) — new_component (design-dependent).
- New data class: consent evidence + payer PII.
- Extended adapter contract (vendor obligations) — potential new_vendor trigger if vendor can't.
- API v0.2 additive.
- New audit event types.
- NFR additions.
### 2.3 Затронутые инварианты (таблица) — cite DELTA matrix.
### 2.4 Пробелы и допущения
- No model/ dir → no trace_check/nfr_check/change_impact; recommend model authoring.
- НСПК protocol [ТРЕБУЕТ ПРОВЕРКИ].
- Vendor support unconfirmed.
- АБС contract not confirmed for variable/partial charges.
- No rubric assets.

Let me write.

Also include the exact triggers and why not new_vendor/new_component (or mark as design-dependent). Let me present a table of 15 triggers with true/false/design-dependent.

Let me write IMPACT.md.
Now the impact/significance assessment (deliverables 1–2).

  `write_file(content="# DESIGN — дельта решения: СБП-подписки (рекуррентные C2B-списания)\n\nSolutioning-дельта к принятому решению (`docs/solutioning.md`). Марш, file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/DESIGN.md")`

Now DESIGN.md — the solutioning delta. Include C4 mermaid, flows, state model summary, alternatives summary (pointers to ADRs), security, integration/RFP impact, gaps, rollback pointer.

Let me write it.

Sections:
# DESIGN — дельта решения: СБП-подписки
1. Контекст и границы (in/out scope)
2. Компоненты (C4 mermaid)
3. Доменные сущности и статусные модели (summary + pointer to spec)
4. Ключевые потоки (mermaid sequence: регистрация согласия; плановое списание; отзыв)
5. Границы и стыки (adapter contract, АБС, НСПК/банк плательщика, ТСП)
6. Рассмотренные альтернативы (summary table + pointers to ADR-008/009) — item 3 pointer
7. Последствия и обратимость (summary + pointer)
8. Безопасность, ПДн, комплаенс
9. Наблюдаемость и эксплуатация
10. План отката (pointer)
11. Пробелы и открытые вопросы

Let me write. Mermaid diagrams must render (mermaid_render supports flowchart, sequenceDiagram). Good.

Let me keep diagrams correct.

For consent registration sequence:
```
sequenceDiagram
    participant T as ТСП
    participant G as СБП-шлюз (ядро)
    participant A as Адаптер ОПКЦ
    participant N as ОПКЦ СБП (НСПК)
    participant P as Плательщик (банк плательщика)

    T->>G: POST /v1/subscriptions (Idempotency-Key, условия)
    G->>G: мандат PENDING_CONSENT + outbox
    G->>A: registerMandate(reference, условия)
    A->>N: регистрация согласия (протокол НСПК)
    N-->>A: consentUrl / qrId
    A-->>G: consentUrl
    G-->>T: 201 {subscriptionId, consentUrl}
    P->>N: подтверждает согласие в своём банке
    N-->>A: событие mandate.activated
    A-->>G: mandate.activated (eventId)
    G->>G: дедуп по eventId, ACTIVE + свидетельство согласия (append-only)
    G-->>T: вебхук subscription.activated
```

Scheduled charge:
```
sequenceDiagram
    participant S as Планировщик
    participant G as СБП-шлюз (ядро)
    participant A as Адаптер ОПКЦ
    participant N as ОПКЦ/банк плательщика
    participant B as АБС

    S->>G: тик (leader/lease, шардинг)
    G->>G: chargeId=f(sub,period); проверка мандата ACTIVE
    G->>G: платёж CREATED(origin=SUBSCRIPTION) + outbox
    G->>A: initiateCharge(reference=chargeId)
    A->>N: списание по мандату
    N-->>A: событие charge.paid
    A-->>G: charge.paid (eventId)
    G->>G: дедуп, статус PAID
    G->>B: зачисление (chargeId/paymentId, идемпотентно)
    B-->>G: absDocId
    G->>G: CREDITED → COMPLETED + outbox
    G-->>T[ТСП]: вебхук charge.completed
```

Hmm participant T referenced in last line but not declared. Let me add participant T as ТСП at start.

Revocation:
```
sequenceDiagram
    participant T as ТСП
    participant G as СБП-шлюз
    participant A as Адаптер ОПКЦ
    T->>G: POST /v1/subscriptions/{id}/revoke (Idempotency-Key)
    G->>A: revokeMandate(reference)
    A-->>G: подтверждение/событие mandate.revoked
    G->>G: REVOKED + outbox; новые charge недостижимы
    G-->>T: вебхук subscription.revoked
    Note over G: плательщик также может отозвать в своём банке — событие mandate.revoked от ОПКЦ
```

OK.

Let me write DESIGN.md.
Now the solutioning delta — components, flows and state model (deliverable 2–3 design context).

  `write_file(content="# Статусная машина подписки и charge — спецификация переходов (дельта)\n\n- Status: Draft (для ревью на гейте A1 дельты)\n- Owner: solution, file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine)`

Now the subscription state machine spec: docs/spec/subscription-state-machine.md. Include subscription states, charge states, transition tables, forbidden transitions, idempotency, reconciliation, API mapping.

Let me write it.

Subscription states:
| State | Meaning | Visible to ТСП |
| PENDING_CONSENT | создана, ждём подтверждения плательщиком | да |
| ACTIVE | согласие подтверждено, списания разрешены | да |
| PAUSED | приостановлена ТСП, будущие списания не создаются | да |
| REVOKED | отозвана (ТСП/плательщик), терминальная | да |
| EXPIRED | истёк срок мандата, терминальная | да |
| FAILED_CONSENT | плательщик отказал/таймаут подтверждения, терминальная | да |

Transitions:
S1 — → PENDING_CONSENT (POST /subscriptions)
S2 PENDING_CONSENT → ACTIVE (mandate.activated)
S3 PENDING_CONSENT → FAILED_CONSENT (mandate.rejected / timeout)
S4 ACTIVE → PAUSED (pause)
S5 PAUSED → ACTIVE (resume)
S6 ACTIVE → REVOKED (revoke / mandate.revoked)
S7 PAUSED → REVOKED
S8 ACTIVE → EXPIRED (срок мандата)
S9 PAUSED → EXPIRED
(also PENDING_CONSENT → REVOKED — ТСП отменяет до подтверждения)

Forbidden: no charge from REVOKED/PAUSED/EXPIRED/FAILED_CONSENT/PENDING_CONSENT; terminal states have no outgoing except revoked can't un-revoke; no transition from REVOKED back.

Charge lifecycle: SCHEDULED → INITIATED → PAID → CREDITED → COMPLETED; FAILED, DUNNING, EXPIRED? Let me define:
- Planned charge materialized as payment with statuses; the charge aggregate mirrors: SCHEDULED → INITIATED → (PAID) → CREDITED → COMPLETED; FAILED (terminal for the attempt/period); RETRY/DUNNING as substate; UNKNOWN resolved by recon.
- Retry attempts do not create new charge, only attemptSeq.

Idempotency table:
- POST /subscriptions: Idempotency-Key → same subscriptionId.
- mandate events: eventId dedup.
- charge creation (planner): chargeId deterministic → idempotent insert.
- POST /subscriptions/{id}/charges: Idempotency-Key → same chargeId.
- АБС confirmation: chargeId/paymentId.
- revoke: idempotent.

Reconciliation & recovery.

API mapping: subscription states exposed; charge visible via charges endpoint / payment status.

Let me write it in the style of docs/spec/state-machine.md.

Then contracts. Then NFR, ACCEPTANCE, A3.

Let me write the spec now.
Now the subscription/charge state machine spec.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine, old_string="- Сверка с НСПК (чащеhour): мандаты `ACTIVE`", new_string="- Сверка с НСПК (ежечасная): мандаты `ACTIVE`")`

I noticed a typo: "чащеhour" — I meant "ежечасная". Let me fix that later or now. Let me fix now with edit.

Also "разбор UNKNOWN" fine.

Let me fix "чащеhour" → "ежечасная".

  `write_file(content="# NFR (дельта) — СБП-подписки: рекуррентные C2B-списания\n\n- Status: Draft (для ревью на A1/A4 дельты)\n- Owner: solution-architect (платё, file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/NFR.md")`

Now NFR.md (item 5). Let me write measurable NFRs for subscriptions.

Sections:
# NFR (delta) — СБП-подписки
- baseline note: values baseline, confirm with business/НСПК.
1. Согласие (consent)
2. Планировщик и списания (accuracy, scale)
3. Идемпотентность/корректность
4. Отзыв и остановка
5. Dunning/устойчивость
6. Доступность/производительность
7. Сверка
8. Безопасность/ПДн/аудит
9. Наблюдаемость

Each with метрика, цель, метод проверки, consequence of violation.

Numbers baseline:
- Consent activation event processing p95 < 5 s (from НСПК event to ACTIVE).
- Consent registration request accept p95 < 500 ms.
- Scheduler accuracy: плановый charge создан в окне ±N; set N=±5 мин with jitter window; p95 initiation lag ≤ 60 s from scheduled (excluding НСПК). Let me define: time from scheduled slot to INITIATED p95 ≤ 60 s, p99 ≤ 5 мин.
- Scale: sustained 50 charges/s; peak 300 charges/s over 10 min on billing day; portfolio baseline 1 млн активных подписок (baseline to confirm). x2 without redesign.
- Charge cycle latency: INITIATED → PAID depends on НСПК; from PAID → CREDITED p95 < 60 s (reuse existing SLA); PAID → COMPLETED (webhook) p95 < 5 s.
- Merchant-initiated charge accept p95 < 500 ms.
- Duplicate charges per (subscription, period) = 0.
- Charge attempts per period ≤ 3 (default, configurable).
- Consents without evidence = 0.
- Revocation propagation: new charges created after REVOKED = 0; revocation event processed p95 < 5 s.
- UNKNOWN resolution ≤ 4 h (runbook), 100% visibility.
- Availability: subscription/consent API ≥ 99.9%; charge engine ≥ 99.95%.
- Reconciliation: hourly mandates/charges, discrepancies on completed = 0.
- Audit: 100% charge→mandate link; consent evidence immutable.
- PII: minimization, encryption at rest, masking.
- Observability: trace id 100%, DLQ alert ≤5 min, scheduler lag metric.
- Failure isolation: single ТСП failure doesn't delay others (>X% of other charges on time).

Let me write with tables and explicit "следствие нарушения".

Then ACCEPTANCE.md.

Let me write NFR.md.
Now the measurable NFRs for the new functionality.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\n  description: >\n    Мерчант-API платёжного шлюза СБП (C2B-приём). В, file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/openapi/tsp-api.yaml")`

Now the contracts. First update openapi/tsp-api.yaml to v0.2.0 additive. Then docs/contracts/tsp-api.md §3.6–3.8 and webhooks + versioning. Then docs/contracts/opkc-adapter.md additions.

Let me write the new openapi file. I'll keep existing content and add. I must ensure openapi_lint passes. Let me look at what lint checks: versioning, idempotency of mutating endpoints, RFC 7807 errors. The current file passed with minimal content. I'll add Idempotency-Key on POSTs and 4xx problem responses to be safe.

Design new openapi:

```yaml
openapi: 3.0.3
info:
  title: СБП-шлюз — API ТСП
  version: 0.2.0
  description: >
    Мерчант-API платёжного шлюза СБП (C2B-приём). v0.2 добавляет подписки
    (рекуррентные списания по согласию плательщика) аддитивно: существующие
    пути и поля v0.1 не изменены.
paths:
  /v1/payments:
    post:
      operationId: createPayment
      summary: Создать платёж (динамический QR / ссылка)
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
        '409':
          description: Конфликт идемпотентности
          content:
            application/problem+json:
              schema: {$ref: '#/components/schemas/Problem'}
  /v1/payments/{paymentId}:
    get:
      ...
  /v1/subscriptions:
    post:
      operationId: createSubscription
      summary: Создать подписку (инициировать согласие плательщика)
      parameters: [Idempotency-Key required]
      requestBody: SubscriptionRequest
      responses: 201 Subscription, 409 Problem
  /v1/subscriptions/{subscriptionId}:
    get: getSubscription -> 200 Subscription
  /v1/subscriptions/{subscriptionId}/suspend:
    post: suspendSubscription
  /v1/subscriptions/{subscriptionId}/resume:
    post: resumeSubscription
  /v1/subscriptions/{subscriptionId}/revoke:
    post: revokeSubscription
  /v1/subscriptions/{subscriptionId}/charges:
    post: createCharge (Idempotency-Key)
    get: listCharges
components:
  schemas:
    Problem:
      type: object
      required: [type, title, status]
      properties:
        type: {type: string, format: uri}
        title: {type: string}
        status: {type: integer}
        detail: {type: string}
        code: {type: string}
        traceId: {type: string}
    PaymentRequest: (unchanged) + optional subscriptionId? Better not change existing schema's required; adding optional fields is fine.
      properties:
        amount, merchantOrderId, currency?, qrType?, ...
      Actually keep as-is but add optional `subscriptionId` and `chargeId` nullable optional. Additive.
    Payment: existing + optional subscriptionId, chargeId, origin.
    SubscriptionRequest:
      required: [tspId, amountMode, currency]
      properties: tspId, amountMode (FIXED|VARIABLE), amount (required if FIXED), maxAmount (for VARIABLE), currency, schedule (period), ttl... , merchantOrderId?, description?
    Subscription:
      required: [subscriptionId, status, amountMode, currency]
      properties: subscriptionId, status enum, amountMode, amount?, maxAmount?, currency, consentUrl?, mandateRef?, nextChargeAt?, createdAt, activatedAt, revokedAt, merchantOrderId?
    ChargeRequest:
      required: [amount]
      properties: amount, billingReference, description?
    Charge:
      required: [chargeId, subscriptionId, amount, status]
      properties: chargeId, subscriptionId, paymentId?, amount, status enum, billingPeriod?, dunning (bool), createdAt, completedAt?, errorCode?
```

Need to be careful: openapi_lint may require `info.version` semantic and mutating endpoints idempotent. Adding Idempotency-Key to all POSTs. Also maybe requires 4xx problem+json for POST. I'll add 400/409 problem responses on POSTs.

Let me write it. Keep it valid YAML. Use flow style consistent with existing.

Then run openapi_lint.

Let me write the openapi file. I already read it, so write_file is allowed (I read it earlier). Yes, I read openapi/tsp-api.yaml earlier in this session.

Let me write.
Now the additive contract changes. First the OpenAPI file (v0.1 → v0.2, strictly additive).

  `run_shell_command(command="git -C <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws show HEAD:openapi/tsp-api.yam, description="Export committed v0.1 contract for compatibility diff")`
  `tool_call(arguments={"cwd": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws", "path": "openapi/tsp-api.y, name="mcp__spine__openapi_lint")`

Now run openapi_lint on the new contract to verify it passes. And save old version for contract_diff. Let me extract old from git and run contract_diff.

Let me do:
1. openapi_lint new.
2. `git show HEAD:openapi/tsp-api.yaml > <TMP>.1.yaml` then contract_diff old /tmp/... new openapi/tsp-api.yaml.

I'll run shell for git show and then tool_call contract_diff. These are dependent (need file first). Let me run shell first, then tool_call.

Actually I can run both tool calls in one block only if independent. Shell creates the file; contract_diff needs it. So sequential.

Let me run shell to create temp and also run openapi_lint (MCP) in parallel? openapi_lint is independent. Let me batch: shell (git show > /tmp) + tool_call openapi_lint.

The directory for shell — I should avoid cd. Use `git -C <repo> show HEAD:openapi/tsp-api.yaml > <TMP>.1.yaml`. That's fine.

Then contract_diff.

Let me do.

  `tool_call(arguments={"cwd": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws", "old": "<TMP>.1., name="mcp__spine__contract_diff")`

openapi_lint PASS on v0.2. Now contract_diff old→new.

  `write_file(content="# Контракт API ТСП (мерчант-API) — v0.2 draft (дельта подписок)\n\n- Status: Draft (для ревью на гейте A1 дельты `changes/sbp-subscriptions, file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/tsp-api.md")`

Excellent: contract_diff → 0 breaking, 9 non-breaking additions. 

Now update docs/contracts/tsp-api.md to v0.2: add sections 3.6–3.8 (subscriptions, charges), webhook events, versioning note, and mark §7 open questions. I must be careful editing the existing doc: change version lines and add sections. Let me do targeted edits.

Edits to docs/contracts/tsp-api.md:
1. Header: version line 0.1 → 0.2 with note; Status line.
2. §3 add 3.6–3.8.
3. §5 webhooks: add subscription/charge events.
4. §6 versioning: note v0.2 additive.
5. §7 open questions: add subscription-related.

Let me read current content again? I have it from earlier read. Let me make edits with exact strings.

Header:
```
# Контракт API ТСП (мерчант-API) — v0.1 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), AD-003 (spine)
```
Change to v0.2 and add delta link.

§3.5 ends with:
```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`
```
Then `## 4. Ошибки...`. I'll insert 3.6–3.8 before `## 4.`.

§5 events list:
```
События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
```
Add subscription/charge events.

§6:
```
- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.
- Добавление опциональных полей — обратно совместимо, не требует новой версии.
```
Add v0.2 note.

§7 open questions add subscription items.

Let me perform edits. I need to re-read the file to be safe? I read it earlier in this session, so content is known. But edits require exact match. Let me carefully use the text I saw.

Let me batch edits (multiple edit calls in one message). They're on the same file — sequential edits to same file could conflict if performed in parallel. Safer to do them one by one? The tool applies each; but parallel edits on same file risk mismatch. I'll do them in separate messages or use a few at a time carefully with disjoint old_strings. Since old_strings are disjoint, parallel should be OK, but to be safe I'll do sequentially in 2 batches.

Actually, let me just do them sequentially in individual calls. Or rewrite the whole file via write_file (I've read it). Rewriting ensures consistency. The doc is long (~150 lines). I'll rewrite it fully with v0.2 additions — cleaner and avoids fragile edits. I have the full content from earlier read. Let me reconstruct it carefully, preserving all existing text and adding new sections.

Let me rewrite docs/contracts/tsp-api.md.
Now update the human-readable contract doc to v0.2.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/opkc-adapter.md", new_string="- Status: Draft (для ревью на гейте A1; основа для RFP вендора)\n- Owner: solution-architect (платёжный контур)\n- Связано: ADR-003, ADR-00, old_string="- Status: Draft (для ревью на гейте A1; основа для RFP вендора)\n- Owner: solution-architect (платёжный контур)\n- Связано: ADR-003, ADR-00)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/opkc-adapter.md", new_string="Статусные модели ОПКЦ (`PAID`, `REJECTED`, `EXPIRED`, `CONFIRMED`) — **нормализованные адаптером** из протокола НСПК; ядро не зависит от ко, old_string="Статусные модели ОПКЦ (`PAID`, `REJECTED`, `EXPIRED`, `CONFIRMED`) — **нормализованные адаптером** из протокола НСПК; ядро не зависит от ко)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/opkc-adapter.md", new_string="| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |\n| `refund.rejected` | возв, old_string="| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |\n| `refund.rejected` | возв)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/opkc-adapter.md", new_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`/`subscriptionId`/`chargeId`) в каждый мутирующий вызов.", old_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/opkc-adapter.md", new_string="6. Эксплуатация: метрики, алерты, документация runbook.\n7. **Поддержка подписочного протокола СБП**: регистрация/отзыв согласия, инициация, old_string="6. Эксплуатация: метрики, алерты, документация runbook.\n\n## 9. Открытые вопросы")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/opkc-adapter.md", new_string="3. Поведение ядра при `transport.unavailable` (приём QR в очередь vs отклонение) — политика, утверждается на A2.\n4. Подписочный протокол: , old_string="3. Поведение ядра при `transport.unavailable` (приём QR в очередь vs отклонение) — политика, утверждается на A2.")`

Now update docs/contracts/opkc-adapter.md with subscription operations. I read it earlier. Let me do targeted edits rather than full rewrite (it's long and I want to preserve). Actually edits risk; but full rewrite is also large. Let me do targeted edits:

1. Header "Связано: ADR-003, ADR-004, AD-004, AD-008" → add ADR-008, ADR-009, AD-009, AD-010.
2. §3 table: add rows for registerMandate, revokeMandate, initiateCharge, getMandateStatus, getChargeStatus.
3. §4 events table: add mandate.activated/rejected/revoked, charge.paid/rejected/unknown.
4. §5 idempotency: add references for mandate/charge.
5. §8 RFP requirements: add subscription support.
6. §9 open questions: add subscription items.

Let me do these edits carefully. I'll batch a few edits with disjoint old_strings — but same file parallel edits might be risky. Let me do them sequentially (multiple messages) or combine into one big edit? The sections are spread out. I'll do several edit calls in sequence.

Actually, I can do multiple edit calls in a single assistant message; the tool executes them in order? The instruction says parallel calls for independent operations. Edits to the same file are not truly independent, but disjoint old_strings should be safe if applied sequentially by the runtime. Risk: if one fails, others still apply. To be safe, I'll do 2-3 messages.

Let me start with the header and §3 table.

Header:
```
- Status: Draft (для ревью на гейте A1; основа для RFP вендора)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-003, ADR-004, AD-004, AD-008
```
→ add ADR-008, ADR-009 and AD-009, AD-010.

§3 table header:
```
| Метод | Направление смысла | Ключевые поля запроса | Ответ | Таймаут (p99.9) |
|---|---|---|---|---|
| `registerTsp` | ...
```
I'll insert new rows after `registerTsp` row or after `cancelPaymentLink`. Let me add a subsection "### 3.1 Подписочные операции (v0.2)" after the table, or add rows to the table. Adding rows to the table is cleaner. The table ends with `getReconciliationReport` row then `Статусные модели ОПКЦ...`. Let me insert rows before `| `getReconciliationReport`` or after it. I'll add a new subsection 3.1 to avoid disturbing the existing table format and make it explicit. Simpler: add a new subsection after the table paragraph.

Let me read the exact §3 ending text again:
```
| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |

Статусные модели ОПКЦ (`PAID`, `REJECTED`, `EXPIRED`, `CONFIRMED`) — **нормализованные адаптером** из протокола НСПК; ядро не зависит от конкретных значений НСПК.

## 4. Асинхронные события (адаптер → ядро)
```

I'll insert a subsection between the paragraph and `## 4`.

Let me write the subscription ops subsection:

### 3.1 Подписочные операции (v0.2, расширение)

| Метод | Направление смысла | Ключевые поля запроса | Ответ | Таймаут (p99.9) |
|---|---|---|---|---|
| `registerMandate` | регистрация согласия плательщика | `reference` (= `subscriptionId` ядра), `tspId`, `amountMode`, `amount|maxAmount`, `currency`, `period`, `expiresAt` | `mandateRef`, `consentUrl`, статус `PENDING` (результат — событием) | 5 c |
| `getMandateStatus` | статус согласия (сверка/опрос) | `reference` / `mandateRef` | `ACTIVE` / `PENDING` / `REJECTED` / `REVOKED` / `EXPIRED` | 3 c |
| `revokeMandate` | отзыв согласия | `reference`, `reason` | `REVOKED` | 5 c |
| `initiateCharge` | инициация списания по мандату | `reference` (= `chargeId` ядра), `mandateRef`, `amount`, `currency`, `billingReference?` | `ACCEPTED` (результат — событием) | 5 c |
| `getChargeStatus` | статус списания | `reference` (= `chargeId`) | `PAID` / `PENDING` / `REJECTED` / `UNKNOWN` | 3 c |

Статусные модели ОПКЦ для подписок (`mandate`, `charge`) нормализуются адаптером так же, как платёжные; ядро не зависит от конкретных значений НСПК. Все мутирующие операции идемпотентны по `reference` (§5). Обязательство вендора поддержать подписочный протокол — новое требование RFP (§8).

§4 events: add:
```
| `mandate.activated` | согласие подтверждено плательщиком | `reference` (= `subscriptionId`), `mandateRef`, `activatedAt` |
| `mandate.rejected` | согласие не получено/отклонено | `reference`, `reasonCode`, `reasonText` |
| `mandate.revoked` | согласие отозвано (в т.ч. плательщиком) | `reference`, `mandateRef`, `revokedAt` |
| `charge.paid` | списание подтверждено | `reference` (= `chargeId`), `mandateRef`, `amount`, `paidAt` |
| `charge.rejected` | списание отклонено | `reference`, `reasonCode`, `reasonText` |
| `charge.unknown` | исход списания не определён (таймаут) | `reference`, `detail` |
```
Insert after `refund.rejected` row and before `transport.unavailable`? Order doesn't matter. Insert after `tsp.rejected` maybe. Let me insert before `| `transport.unavailable``.

§5: add bullet about mandate/charge references. Current:
```
- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.
```
→ add `/subscriptionId`/`chargeId` and note mandate idempotency.

§8 RFP: add item:
```
7. Поддержка подписочного протокола СБП: регистрация/отзыв согласия, инициация списаний, события `mandate.*`/`charge.*`, идемпотентность по `reference`. Без этого подписочный функционал нереализуем (условие пересмотра ADR-007).
```

§9 open questions: add:
```
4. Подписочный протокол: точные поля/тайминги регистрации согласия и списаний — `[ТРЕБУЕТ ПРОВЕРКИ]` (документация НСПК).
5. Поддерживает ли текущий транспортный вендор подписки — подтверждение до старта реализации.
```

Let me execute the edits. I'll do them in a few calls.

Let me do edit 1 (header), edit 2 (§3 subsection), edit 3 (§4 events), edit 4 (§5), edit 5 (§8), edit 6 (§9). I'll batch 3 at a time to reduce risk? Let me just do them sequentially in separate messages to be safe... that's 6 round trips. Alternatively one message with 6 edits; the runtime likely applies sequentially. Given the instruction "Call independent tools in parallel", and edits on the same file with disjoint anchors are effectively independent, I'll try a single message with all 6. If any fails, I'll fix.

Hmm, risk: after first edit, file content changes; subsequent old_strings still match because they're in different regions. Should be fine.

Let me write them.
Now extend the internal adapter contract with the subscription operations (this is what makes the vendor obligation explicit).

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/opkc-adapter.md", new_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.2 draft (расширение: подписки)", old_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.1 draft")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/solutioning.md", new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop, old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop)`

All 6 edits applied. Now update the adapter contract title from v0.1 to v0.2? The title says "v0.1 draft". I should bump it to reflect the extension: "v0.2 draft (расширение: подписки)". Let me edit the H1.

Also update `docs/solutioning.md` §1 scope change (MODIFIED). Let me do a targeted edit: remove "автоплатежи" from roadmap list and add a scope note.

Location in solutioning.md §1:
"Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

I'll edit to:
"Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты.
Расширение (дельта `changes/sbp-subscriptions`, маршрут Critical): рекуррентные C2B-списания по согласию плательщика («СБП-подписки») — выведены из roadmap в scope; см. `changes/sbp-subscriptions/DESIGN.md`."

Also §6 NFR pointer and §7 gates could mention delta, but minimal is fine. Let me also add to §9 gaps? Not necessary.

Let me do 2 edits: adapter title + solutioning scope.

Also README: add a short "Изменения в работе" pointer. I'll do it.

Let me do these edits.

  `write_file(content="# ACCEPTANCE — критерии приёмки и план отката\n\n- Status: Draft (для ревью A1/A4 дельты; финальная приёмка — после A3)\n- Owner: solution-, file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/ACCEPTANCE)`

Now ACCEPTANCE.md (item 6) with EARS criteria and rollback plan. Then A3-DECISION.md (item 7). Then CONSTRAINTS.yaml rules. Then README pointer. Then gates + adversarial review.

Let me write ACCEPTANCE.md.

Content:
# ACCEPTANCE — критерии приёмки и план отката
- Status, owner, related.
## 1. Критерии приёмки (EARS) — R1..R12 mapped to testable criteria
Table: ID | Requirement (EARS) | Как проверяется (тест/команда/метрика) | Негативный сценарий
Include negative scenarios: duplicate, revocation race, АБС down, НСПК timeout, replay, boundary (limit exceeded), downgrade compatibility.
## 2. Негативные и граничные сценарии (обязательные)
## 3. Traceability (R → AD → ADR → NFR)
## 4. Readiness verdict (readiness-gate) — PASS/CONCERNS with gaps
## 5. План отката (пошаговый, сигналы, владелец, критерий успешного отката)
## 6. Handoff-готовность

Let me write it thoroughly.

Readiness verdict: CONCERNS — because external inputs (НСПК protocol, vendor support, АБС variable amounts) not closed; but design is ready for A3. Per readiness-gate, CONCERNS with addressable items. Actually readiness-gate is about "can implementer implement without inventing". Given open external inputs, verdict CONCERNS with each gap addressed. Good.

Rollback plan details:
- Pre-prod: reversible; feature flag `subscriptions.enabled` off; no data migration; rollback = deploy previous version/revert delta.
- Post-launch: 
  1. Signal triggers (duplicate charge metric > 0; consent evidence gap; charge success below threshold; НСПК/АБС degradation).
  2. Actions: stop-new-charges kill switch (≤1 min); freeze scheduler; keep processing in-flight; notify ТСП; revoke mandates per protocol if full withdrawal needed; reconcile.
  3. Owner: solution-architect + SRE lead + business owner; decision within X.
  4. Success criterion of rollback: no new charges created; all in-flight charges resolved to terminal or reconciled; no duplicate charges; mandates status consistent with НСПК; existing single-payment flows unaffected.
- What is NOT rolled back: completed charges/credits; data retained; no reverse migration.

Handoff readiness: list spec files for `arch-be handoff` and note it requires human A3 first; command example.

Let me write.
Now acceptance criteria and the rollback plan (deliverable 6).

  `write_file(content="# A3-DECISION — что остаётся на решение человека-архитектора\n\n- Status: Draft (вход на гейт A3; до решения реализация не начинается)\n- O, file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/A3-DECISIO)`

Now A3-DECISION.md (item 7 + machine-readable A3 pack). Include:
- Что именно должен решить человек (A3) — list of decisions with options/recommendations.
- Machine-readable A3 pack {choice, rationale, constraints, rejected options, expiry} for the main decision.
- Допущения (assumptions requiring confirmation).
- Открытые вопросы.
- Что НЕ решает человек (агентская зона).
- Путь после A3 (handoff).
- Состязательные находки (self-review) — flag as non-independent, need independent reviewer.

Let me write.

Main A3 decision: choice = "Подписки СБП на базе мандата в ядре шлюза с двумя режимами инициации (плановый + по запросу ТСП)".

Human decisions list:
1. A3-1: Утвердить модель мандата в шлюзе (ADR-008) vs доверие ТСП vs вендор. Recommendation: мандат в шлюзе.
2. A3-2: Режимы списаний — FIXED+FIXED/VARIABLE/both. Recommendation: оба (FIXED по расписанию + VARIABLE по запросу), т.к. ТСП разные.
3. A3-3: Dunning policy (attempts, windows, notifications). Recommendation baseline ≤3, backoff+dither.
4. A3-4: Вендор — подтвердить поддержку подписок; при отказе — RFP/смена транспорта (пересмотр ADR-007).
5. A3-5: ПДн/сроки хранения согласия (ИБ/комплаенс).
6. A3-6: Диспуты по подпискам — scope vs Deferred.
7. A3-7: Коммерческие параметры (лимиты, тарифы, max amounts).
8. A3-8: Заводить ли каталог model/ (трассировка/NFR-проверки).
9. A3-9: Независимая оценка ADR рубрикой (нет активов; назначить судью).

Machine-readable A3 pack:
```json
{
  "choice": "hybrid-mandate-in-core",
  "rationale": "...",
  "constraints": [...],
  "rejected_options": [...],
  "expiry": "..."
}
```

Let me write the doc.

Also include "Допущения" (assumptions from the package) and "Открытые вопросы".

Let me write.
Now the human decision pack (deliverable 7) with a machine-readable A3 block.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="  - name: spine-lints-clean\n    type: must_not_contain\n    glob: \"ARCHITECTURE-SPINE.md\"\n    pattern: 'TODO|TBD|XXX'\n    severity: wa, old_string="  - name: spine-lints-clean\n    type: must_not_contain\n    glob: \"ARCHITECTURE-SPINE.md\"\n    pattern: 'TODO|TBD|XXX'\n    severity: wa)`

Now update CONSTRAINTS.yaml with new fitness rules. Must ensure fitness_check passes. Add rules that reference existing/created files.

New rules (with owner/expiry to be exemplary):
- name: subscriptions-delta-present
  type: file_exists
  path: changes/sbp-subscriptions/DELTA.md
  severity: error
- name: subscriptions-design-present
  type: file_exists
  path: changes/sbp-subscriptions/DESIGN.md
  severity: error
- name: adr-subscriptions-present
  type: file_exists
  path: docs/adr/ADR-008-model-podpiski-sbp-mandat-platelschika-kak-edinstvennyy-istochnik-soglasiya.md
  severity: error
- name: spine-consent-invariant
  type: must_contain
  glob: "ARCHITECTURE-SPINE.md"
  pattern: 'AD-009\. Согласие плательщика'
  severity: error
- name: spine-charge-idempotency-invariant
  type: must_contain
  glob: "ARCHITECTURE-SPINE.md"
  pattern: 'chargeId = f\(subscriptionId, periodStart\)'
  severity: error
- name: no-charge-without-consent
  type: must_contain
  glob: "changes/sbp-subscriptions/DESIGN.md"
  pattern: 'PENDING_CONSENT|REVOKED'
  severity: warn
  Hmm weak. Better: must_contain in ACCEPTANCE/DESIGN of the rule text.
- name: ears-acceptance-subscriptions (from rules_suggest, but scoped): must_contain changes/sbp-subscriptions/ACCEPTANCE.md pattern '(?m)^\|\s*AC-' severity: warn
- name: subscriptions-contract-additive
  type: must_contain
  glob: "docs/contracts/tsp-api.md"
  pattern: '0 breaking'
  severity: warn

Also careful: `must_not_contain` is line-based; `must_contain` matches whole file (need (?m) for anchors). Fine.

Also the existing rule `adr-no-placeholders` uses must_not_contain glob "docs/adr/*.md" pattern '<!--'. My ADRs have no `<!--`. Good.

But note: the existing CONSTRAINTS file has no `owner`/`expiry` fields on existing rules; rules_report flagged that. I'll add owner/expiry to new rules. The schema may support `owner:`, `expiry:`. The rules_report shows columns owner/expiry, so fields exist. I'll add.

Let me also add a comment noting stage.

Actually, careful: adding a `must_contain` rule with regex containing parentheses etc. YAML — I'll quote it. Pattern: 'chargeId = f\(subscriptionId, periodStart\)'. In YAML single quotes, backslash is literal; regex `\(` matches literal paren. Good.

Also the existing file has a top comment. Let me append rules under `rules:`.

Let me read CONSTRAINTS.yaml again? I have it. I'll use edit to append after the last rule (spine-lints-clean).

Last rule:
```
  - name: spine-lints-clean
    type: must_not_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'TODO|TBD|XXX'
    severity: warn
```

I'll replace it with itself + new rules.

Let me craft new rules. I want to keep it modest (5-7 rules) and all passing.

Rules to add:
```
  # --- Дельта sbp-subscriptions (Critical) ---
  - name: subscriptions-delta-present
    type: file_exists
    path: changes/sbp-subscriptions/DELTA.md
    severity: error
    owner: solution-architect
    expiry: 2027-03-31
  - name: subscriptions-design-present
    type: file_exists
    path: changes/sbp-subscriptions/DESIGN.md
    severity: error
    owner: solution-architect
    expiry: 2027-03-31
  - name: adr-subscriptions-present
    type: file_exists
    path: docs/adr/ADR-008-model-podpiski-sbp-mandat-platelschika-kak-edinstvennyy-istochnik-soglasiya.md
    severity: error
    owner: solution-architect
    expiry: 2027-03-31
  - name: spine-consent-invariant
    type: must_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'AD-009\. Согласие плательщика — обязательное условие'
    severity: error
    owner: solution-architect
    expiry: 2027-03-31
    rationale: 'инвариант AD-009 должен присутствовать в spine после дельты'
  - name: spine-charge-idempotency-invariant
    type: must_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'chargeId = f\(subscriptionId, periodStart\)'
    severity: error
    owner: solution-architect
    expiry: 2027-03-31
  - name: subscriptions-ears-acceptance
    type: must_contain
    glob: "changes/sbp-subscriptions/ACCEPTANCE.md"
    pattern: '(?m)^\|\s*AC-\d+'
    severity: warn
    owner: solution-architect
    expiry: 2027-03-31
  - name: subscriptions-contract-additive
    type: must_contain
    glob: "docs/contracts/tsp-api.md"
    pattern: '0 breaking'
    severity: warn
    owner: solution-architect
    expiry: 2027-03-31
```

Wait — `must_contain` matches against the whole file; the pattern 'AD-009\. Согласие плательщика — обязательное условие' — my spine heading is "## AD-009. Согласие плательщика — обязательное условие автоматического списания". So it matches. Good.

The `subscriptions-ears-acceptance` with `(?m)^\|\s*AC-\d+` — ACCEPTANCE.md has table rows starting with "| AC-1 |". Good.

`subscriptions-contract-additive` pattern '0 breaking' — tsp-api.md has "0 breaking" in header and §6. Good.

Now, potential issue: adding `must_contain` rules may trigger `rule_weakened` anti-weakening? No — adding is fine. But the fitness_check anti-weakening compares rule composition vs base — adding rules is not weakening.

Another potential: the `adr-set-complete` file_exists checks ADR-001 exists — yes.

Also there's `nfr-measurable` must_contain docs/nfr.md pattern '99,95' — still there.

Let me apply the edit.

Then run fitness_check.

Let me do it.
Now register the delta's fitness rules in the constraints registry.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/README.md", new_string="- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (прото, old_string="- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (прото)`

Now add README pointer. Let me read README (I have it) and add a section. Actually I read README at start. Let me edit: add after the status line or before "## Структура".

README content:
```
# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): ...

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: ...
- Статус: решение подготовлено, **ожидает человеческого решения A3** ...

## Структура
```

Add a section "## Изменения в работе" after status. Let me insert before "## Структура".

Content:
```
## Изменения в работе

- [`changes/sbp-subscriptions/`](changes/sbp-subscriptions/) — дельта **«СБП-подписки»** (рекуррентные C2B-списания по согласию плательщика), маршрут **Critical** (значимость 8/15). Вход на A3: `A3-DECISION.md`; решения — ADR-008/ADR-009; инварианты — AD-009…AD-011.
```

Let me edit.

Then run the gates: delta_guard, fitness_check, spine_lint, control score --from-diff, architect_review. And render mermaid? Not needed.

Let me do README edit + delta guard + fitness + spine lint in parallel (edits independent of MCP calls? The delta guard reads DELTA.md and git diff; README edit doesn't affect. But running gates after all edits is better. Let me do README edit first, then gates.)

Actually, let me do README edit now, then run all gates together.

  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws", "base": "HEAD"}, name="mcp__spine__delta_guard")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws"}, name="mcp__spine__fitness_check")`
  `tool_call(arguments={"path": "ARCHITECTURE-SPINE.md"}, name="mcp__spine__spine_lint")`
  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && arch-be control score --from-d, description="Run anti-bypass significance score from git diff")`

Now run gates: delta_guard, fitness_check, spine_lint, and control score --from-diff (shell). Also architect_review (composite) — but it runs command_succeeds? CONSTRAINTS has no command_succeeds, so fine. architect_review may also run trace_check which needs model/ → might error but it's composite; let me try.

Let me run:
- tool_call delta_guard {path: repo, base: HEAD}
- tool_call fitness_check
- tool_call spine_lint
- shell: arch-be control score --from-diff

Batch them (independent).

Note delta_guard protect default may or may not include .arch-handoff/CONSTRAINTS.yaml. Let me see result.

Also verify the spine file still valid with spine_lint.

Let me run.
Now let me run the repository's gates against the change.

  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && echo \"=== score (declared + d, description="Run union significance score and validate the delta")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws"}, name="mcp__spine__architect_review")`

Interesting: `control score --from-diff` only detected api_contract_change (1) → Fast, and flagged a discrepancy vs declared flags. But `--from-diff` without declared triggers just shows floor. The message "ВНИМАНИЕ — расхождение: заявлено флагами vs видно по диффу: api_contract_change" — hmm, it says declared vs diff. I didn't pass declared flags, so it compares empty declared vs diff-found. Actually the output route Fast is the *mechanical floor* from diff alone (it only detects file-pattern triggers). The declared score (8 via significance_score) is higher. Combined (union) = 8 → Critical. The tool description says "механически вывести триггеры из git-диффа и объединить с заявленными (fail-safe — детектор только добавляет)". So I should run with declared triggers too: `arch-be control score --trigger ... --from-diff`. Let me do that to show union = Critical.

Let me run: `arch-be control score --from-diff --trigger api_contract_change=true --trigger data_contract_change=true ...`. Actually `--trigger <TRIGGER>` format "имя=true". Multiple `--trigger` flags.

Let me run with the 8 declared. This demonstrates the anti-bypass union = Critical.

Also delta_guard: passed, protected_changed only ARCHITECTURE-SPINE.md — interesting, it didn't count .arch-handoff/CONSTRAINTS.yaml as protected (default protect probably only matches top-level CONSTRAINTS.yaml, and model/, ARCHITECTURE-SPINE.md). So only spine was protected. Our DELTA mentions both, so covered. passed=true. Good.

fitness: 14 rules, 0 violations, passed. Good.
spine_lint: passed.

Now run score with declared triggers + from-diff. Also run architect_review composite and deltas validate. Let me also run `arch-be delta validate sbp-subscriptions` and `arch-be delta list`.

Let me batch: shell (score with declared + delta validate + delta list) and tool_call architect_review.

Actually architect_review might be heavy and could flag things. Let me run it to see. It also runs trace_check (needs model/) → might FAIL/SKIP. Let's see.

Let me run.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/IMPACT.md", new_string="**Итог: 8 подтверждённых триггеров → маршрут `Critical`** (порог 5+; критический триггер `security_boundary_change` присутствует). С проект, old_string="**Итог: 8 подтверждённых триггеров → маршрут `Critical`** (порог 5+; критический триггер `security_boundary_change` присутствует). Даже без)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/DELTA.md", new_string="| Гейт | Команда/инструмент | Результат |\n|---|---|---|\n| Маршрут | `significance_score`, `control score --from-diff` | Critical, 8/15 (с, old_string="| Гейт | Команда/инструмент | Результат |\n|---|---|---|\n| Маршрут | `significance_score` | Critical, 8/15 (`IMPACT.md`) |\n| Дельта-гейт )`
  `tool_search(query="select:mcp__spine__mermaid_render")`

Gates all PASS (fitness, delta_guard, rule_weakened, spine_lint). trace/model SKIP (no model/). architect_review auto-route Fast (mechanical diff floor) — but declared union is Critical (9). This is an important nuance: the mechanical auto-route is a *floor*; declared triggers raise it. The `route_note` says "auto: score 1". I should note in IMPACT.md/DELTA that the mechanical diff-floor is Fast but declared triggers raise to Critical, and that the Critical route is what governs. Actually the anti-bypass floor is meant to prevent *lowering*; here declared > floor, which is allowed (it's not a bypass). But architect_review's auto-route uses only the diff. Hmm — this could be seen as the tool reporting Fast. Let me reconcile: the honest thing is to state both: diff-floor = 1 (Fast), declared = 9 (Critical), route = Critical (union/max). The `control score --from-diff` with declared flags gave Critical 9. So the package's route is Critical.

I should record this precisely in IMPACT.md §1.1 and DELTA gates. Let me update IMPACT to include the tool outputs and the floor/declared nuance. I already wrote "score 8". Now with new_component=true it's 9. Let me update to reflect: confirmed 8 + design-dependent new_component → 9 declared; diff-floor 1; route = Critical.

Let me update IMPACT.md §1.1 table note and add tool evidence, and DELTA gate table.

Also I should update the DELTA gate row for significance: "significance_score → Critical, 8/15 (declared +new_component → 9); diff-floor 1 (Fast) — маршрут поднят заявленными триггерами".

Let me edit IMPACT.md: change "Итог: 8 подтверждённых триггеров → маршрут Critical" to mention 8 confirmed + new_component = 9 and floor.

Actually, in IMPACT I marked new_component as "зависит от решения" and count 8 confirmed. The tool run with new_component=true gave 9. I'll present: confirmed 8; with new_component (design decision to introduce the engine as a component) → 9. Critical either way.

Let me make a small edit to IMPACT.md to add tool evidence lines. And DELTA gates table row.

Let me also verify the mermaid diagrams render (optional). Let me run mermaid_render on one diagram to be safe? The design has 3 diagrams + C4. Rendering is a nice validation. Let me test the C4/flowchart and one sequence quickly. But if rendering fails due to syntax, I should fix. Let me run mermaid_render for the flowchart and one sequenceDiagram via tool_call. Need schema. Let me select mcp__spine__mermaid_render.

Actually, mermaid rendering correctness is a "nice to have"; the diagrams are standard. But the skill c4-mermaid urges verification. Let me quickly verify with mermaid_render to avoid shipping broken diagrams. I'll select schema and render the two sequence diagrams + flowchart. That's 3 calls. Let me first get schema.

Let me batch: edit IMPACT.md + DELTA.md gate row, and tool_search mermaid_render.

Let me do the edits first (2 edits) + tool_search.

IMPACT edit: replace the "**Итог: 8 подтверждённых триггеров → маршрут `Critical`**..." paragraph.

Current text:
```
**Итог: 8 подтверждённых триггеров → маршрут `Critical`** (порог 5+; критический триггер `security_boundary_change` присутствует). Даже без «зависимых» триггеров маршрут остаётся Critical.
```

Replace with:
```
**Итог: 8 подтверждённых триггеров → маршрут `Critical`** (порог 5+; критический триггер `security_boundary_change` присутствует). С проектным решением «новый компонент — движок списаний» — 9 триггеров. Даже без «зависимых» триггеров маршрут остаётся Critical.

Машинное свидетельство:
- `significance_score` (заявленные триггеры): **Critical, 8/15**; с `new_component=true` — **Critical, 9/15**.
- `control score --from-diff` (механический пол, ADR-034): 1 триггер (`api_contract_change`) → Fast. Механический пол не занижает и не заменяет заявленный маршрут; объединение даёт Critical.
```

DELTA gate table row:
```
| Маршрут | `significance_score` | Critical, 8/15 (`IMPACT.md`) |
```
→
```
| Маршрут | `significance_score` | Critical, 8/15 (с `new_component` — 9/15); diff-пол 1 → Fast, объединение — Critical (`IMPACT.md`) |
```
And update the "ожидается passed" rows to actual results, since gates have now run. Let me update the gate table to actual:
| Дельта-гейт | `delta guard` | **passed=true** (protected: ARCHITECTURE-SPINE.md покрыт; violations: 0) |
| Fitness | `fitness_check` | **passed=true** (14 правил, 0 нарушений; ослаблений нет) |
| Spine | `spine_lint` | **passed=true** (0 находок) |
| Контракт | `openapi_lint` / `contract_diff` | **PASS** / **0 breaking**, 9 non-breaking |

Let me apply edits.

Let me do tool_search for mermaid_render + the two edits in one message.
All gates pass. Let me record the exact evidence in the package and validate the diagrams render.

  `tool_call(arguments={"code": "flowchart LR\n    subgraph Ext[\"Внешний мир\"]\n        TSP[\"ТСП / мерчант<br/>(подписки, charges)\"]\n        NSPK[\"ОПКЦ СБП (, name="mcp__spine__mermaid_render")`

Let me render the three diagrams to verify syntax. I'll pass code inline. Let me test the flowchart and the two sequence diagrams.

Let me batch 3 tool_calls with mermaid_render.

Diagram 1 (flowchart) — from DESIGN §2. Copy exactly.
Diagram 2 (sequence 4.1).
Diagram 3 (sequence 4.2).

Rendering may output large ASCII. That's a lot of context. Hmm. Maybe just verify one or two. Actually the risk is syntax errors. Let me render the flowchart and sequence 4.2 (most complex). Two calls.

Let me be economical: render all three but they may be long. I'll do two: flowchart + sequence 4.2. If both fine, high confidence.

Actually, let me just render the flowchart and one sequence. Let me do it.

Hmm, but large ASCII output will bloat context. Let me accept it; it's the correct verification per c4-mermaid skill.

Actually — a cheaper check: mermaid syntax errors would be caught. But given context budget, let me render just the flowchart (C4-ish) and the scheduled-charge sequence. Two calls.

Let me do.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/DESIGN.md", new_string="            DB[(БД шлюза<br/>платежи + мандаты + outbox + аудит)]", old_string="            DB[(\"БД шлюза<br/>платежи + мандаты + outbox + аудит\")]")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/DESIGN.md", new_string="            Q[(Очередь + DLQ)]", old_string="            Q[(\"Очередь + DLQ\")]")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/DESIGN.md", new_string="        ABS[(АБС: счета ТСП)]", old_string="        ABS[(\"АБС: счета ТСП\")]")`
  `tool_call(arguments={"code": "sequenceDiagram\n    participant S as Планировщик\n    participant G as СБП-шлюз (ядро)\n    participant A as Адаптер ОПКЦ\n    pa, name="mcp__spine__mermaid_render")`

The flowchart renders (subgraphs are skipped by the renderer, but syntax is valid). Note the DB node labels used `[("...")]` which rendered as literal `("...")` — the cylinder shape `[( )]` is mermaid database shape, but here it produced literal quotes because of `DB[("БД шлюза<br/>...")]`. Hmm, in mermaid `[(text)]` is the cylinder/database shape; the renderer shows `("БД шлюза...")` literally, meaning it may not support `[(` shape and treated the content as text including parentheses/quotes. That's a minor rendering cosmetic in this ASCII renderer. The source is valid mermaid (database shape). It's fine — mermaid.js would render it as a DB cylinder. The ASCII renderer is limited.

Actually wait: `DB[("...")]` — mermaid syntax for cylinder is `id[(text)]`. The text should not include quotes. I wrote `DB[("БД шлюза<br/>...")]` which includes quotes in the label → renders as `("БД шлюза")`. Slightly ugly. Let me fix by removing the inner quotes: `DB[("БД шлюза<br/>платежи + мандаты + outbox + аудит")]` → `DB[(БД шлюза<br/>платежи + мандаты + outbox + аудит)]`. Similarly ABS and Q. Let me fix those three in DESIGN.md.

Let me check my DESIGN.md exact strings:
```
            DB[("БД шлюза<br/>платежи + мандаты + outbox + аудит")]
            ...
            Q[("Очередь + DLQ")]
        ...
        ABS[("АБС: счета ТСП")]
```
Yes. Let me fix to `[(...)]` without quotes.

Also the sequence diagrams — let me verify one. Let me fix DESIGN DB labels and render the scheduled-charge sequence.

Let me do the edits (3 replacements via replace_all? They differ). Use three separate edits or one edit each. Let me do a single edit covering the DB, Q lines? They're not adjacent. I'll do 3 edits.

Then render sequence 4.2.

Let me batch the 3 edits + mermaid render (independent tools? edits to DESIGN and render reading DESIGN — but I'll pass code inline, so independent). Actually I'll render inline code, so no dependency. Batch all 4.

Sequence 4.2 code:
```
sequenceDiagram
    participant S as Планировщик
    participant G as СБП-шлюз (ядро)
    participant A as Адаптер ОПКЦ
    participant N as ОПКЦ / банк плательщика
    participant B as АБС
    participant T as ТСП

    S->>G: тик (leader/lease, шардинг по подпискам, джиттер)
    G->>G: chargeId = f(sub, period); проверка мандата ACTIVE
    G->>G: платёж CREATED (origin=SUBSCRIPTION) + outbox
    G->>A: initiateCharge(reference = chargeId)
    A->>N: списание по мандату
    N-->>A: событие charge.paid
    A-->>G: charge.paid (eventId)
    G->>G: дедуп по eventId → PAID
    G->>B: зачисление (paymentId, идемпотентно)
    B-->>G: absDocId
    G->>G: CREDITED → COMPLETED + outbox
    G-->>T: вебхук charge.completed
    Note over G: UNKNOWN/таймаут → разрешение сверкой, без слепого повтора
```

Let me render it. Also the consent sequence (4.1) has participant P declared and used — fine.

Let me batch.

  `skill(skill="agent-delegation")`

The second edit's confirmation echoed the pre-edit state for Q (showing `Q[("Очередь + DLQ")]` before) but the third's output shows `Q[(Очередь + DLQ)]` — so both applied. And the fourth shows `ABS[(АБС: счета ТСП)]`. Good, all three applied.

Sequence renders fine (Note skipped by renderer, normal).

Now: independent adversarial review. The adversarial-review skill requires an independent contour. Let me dispatch a subagent (general-purpose) with the adversarial brief to review the package, run_in_background: false so I get the result inline. This satisfies "independent reviewer ≠ author". The subagent gets a fresh context and the files.

But careful: subagents don't see my conversation. I'll give it the repo path and the specific files to review + adversarial prompt + output format. It can read files itself.

Let me load the agent-delegation skill first? The Agent tool description says to load the `agent-delegation` skill before writing a delegation prompt. Let me invoke it quickly.

Actually that's an extra step but instructed. Let me load it and then dispatch.

Hmm, context budget. The skill is a reference. Let me load it (bundled skill).

Then dispatch the review agent with run_in_background: false.

Let me do: skill agent-delegation, then Agent.

Actually I can do both in one message? The Agent prompt depends on the skill content. Sequential: load skill first.

Let me load agent-delegation.
The package is drafted and gates pass. Now, per the adversarial-review discipline (reviewer ≠ author), let me get an independent review. First the delegation guidance.

  `agent(description="Adversarial review of subscriptions package", subagent_type="general-purpose", run_in_background=false)`

Now dispatch an independent adversarial reviewer subagent. Use general-purpose, run_in_background: false (need result inline). Provide concrete file paths, adversarial lenses, output format (VERDICT READY/NOT-READY + findings with evidence), and read-only scope (no code changes). Keep it bounded.

Let me write the prompt.

Prompt:
- Context: repo path, the change is "СБП-подписки" delta on an accepted payment gateway architecture.
- Your role: independent adversarial reviewer; you did NOT design it.
- Read files: ARCHITECTURE-SPINE.md, docs/solutioning.md, docs/nfr.md, docs/adr/ADR-001..009, docs/contracts/tsp-api.md, docs/contracts/opkc-adapter.md, docs/spec/state-machine.md, docs/spec/subscription-state-machine.md, openapi/tsp-api.yaml, changes/sbp-subscriptions/*, .arch-handoff/CONSTRAINTS.yaml.
- Task: find what breaks in prod/regulatory/operations; evidence-based (quote file:line/section); verdict READY/NOT-READY with severity blocker/major/minor; do not redesign, do not edit files.
- Lenses: contracts/interfaces (timeouts, retries, idempotency, versioning), data/consistency, security/compliance (152-ФЗ, КИИ, consent evidence, PII), NFR/operations (degradation, backpressure, DLQ, rollback), feasibility ("magic steps" without owner/mechanism), consistency with existing AD-001..008 and invariants.
- Output: concise; VERDICT + findings list (severity, finding, evidence, why it breaks) + up to 5 questions to the author. Max ~600 words.
- Explicit: research only, no file writes.

Let me dispatch with run_in_background: false.

I must be careful: the subagent is general-purpose with tools; I'll tell it read-only.

Let me go.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/rfp/vendor-rfp.md")`

The independent adversarial review returned NOT-READY with real, evidence-based findings. This is valuable. I should address the valid findings by revising the package. Per the receiving-code-review discipline (superpowers:receiving-code-review), I should verify each finding on the technical merits, not perform agreement. Let me assess:

Finding 1 [blocker] — revocation not enforced at charge initiation (C2 guard empty; delayed queue). VALID. The transition table C2 lacks a guard, and ADR-009 delayed queue means a charge created while ACTIVE could be initiated after revocation. Fix: add guard to C2 (re-check subscription ACTIVE + global switch at dequeue), and specify in-flight charge policy (revoke → cancel if not yet INITIATED; if INITIATED, complete or cancel per НСПК, never create new). Also add NFR/ACCEPTANCE accordingly. This is a genuine gap. FIX.

Finding 2 [blocker] — consent scope not enforceable for variable charges; billingReference optional; no per-period cap; FIXED still exposes POST /charges; two different keys → two charges per period. VALID and important. Fixes:
- Make `billingReference` REQUIRED for merchant-initiated charges (or define key = f(subscriptionId, billingReference)).
- Add per-period/aggregate cap to mandate (maxAmountPerPeriod / total) and enforce.
- For FIXED subscriptions, either disallow merchant-initiated charges or define explicitly. Better: allow only if mandate `amountMode=VARIABLE`; FIXED subscriptions are engine-driven only. Add `422 CHARGE_NOT_ALLOWED_FOR_FIXED`.
- Clarify AD-010 key for variable mode and that scheduled key and TSP key must be unified: define period key = normalized period identifier; for scheduled use `periodStart`; for merchant-initiated require `billingReference` which IS the period identifier. To avoid double-charge for the same period across both paths, define a single "charge slot" key = f(subscriptionId, periodKey) where periodKey is either the schedule period or the billingReference; and document that a period already charged cannot be charged again. Good.
- Add per-period cap to SubscriptionRequest/Subscription.

FIX.

Finding 3 [major] — payment FSM has no edge for subscription debit; state-machine.md not in MODIFIED. VALID. The DESIGN says "платёж CREATED (origin=SUBSCRIPTION) → PAID" but the baseline FSM only has QR_ISSUED→PAID. Need to either add a transition (T13: CREATED → PAID for mandate debit) or clarify charge has its own status machine and the payment record uses a variant. Better: extend docs/spec/state-machine.md with a subscription-origin path and add it to DELTA MODIFIED. FIX: add T13/T14 to docs/spec/state-machine.md and list in DELTA; also make subscription-state-machine consistent.

Actually cleaner: define that for `origin=SUBSCRIPTION`, the payment is created directly in a state equivalent to `PAID`-pending and the QR_ISSUED state is skipped. Add transition in state-machine.md: T13 `CREATED → PAID` (триггер — подтверждение списания по мандату; Guard — origin=SUBSCRIPTION, мандат ACTIVE) and note QR_ISSUED not applicable. And C1 in subscription-state-machine creates charge/payment accordingly. Let me add.

Finding 4 [major] — RFP not updated. VALID. docs/rfp/vendor-rfp.md not modified, but ADR-008/opkc-adapter make subscription support mandatory. Fix: update docs/rfp/vendor-rfp.md §4 to include subscription methods/events and a criterion. FIX. Let me read the RFP file to edit.

Finding 5 [major] — bulkhead sharding by subscriptionId doesn't isolate noisy TSP. VALID nuance: sharding by subscriptionId spreads a TSP across shards. To isolate a TSP you need sharding by tspId (or two-level). Fix: shard by tspId (or hash(tspId)) for bulkhead isolation; within TSP, ordering per subscription guaranteed by per-subscription serialization. Update ADR-009 §3 and DESIGN/NFR to say sharding key = tspId (bulkhead) with per-subscription ordering via key/partition. FIX.

Finding 6 [major] — scheduler accuracy vs jitter vs capacity contradiction: 1M subscriptions × peak; ±N minutes vs p95 ≤60s; 300 charges/s. VALID arithmetic concern: if all 1M subscriptions are monthly on day 1, then ~1M charges must be spread; a ±N-minutes window for all is too tight. Need to reconcile: distribute across a "billing window" (e.g., hours) rather than ±minutes; or lower portfolio baseline; or raise peak. Honest fix: state the daily/billing-window model: charges are spread over a billing window (default several hours) with jitter; per-charge accuracy is p95 ≤ 60 s *relative to its assigned slot*, and slots are spread across the window to satisfy ≤ peak charges/s. Compute: 1M charges over, say, 6 h = ~46 charges/s average; peak 300 charges/s allows burst. Actually 1M/300 per s = ~55 min minimum; so a 1-hour window would be tight; 6-hour window is fine. Let me set billing window baseline = 6 h for the full portfolio, slot jitter ±5 min, accuracy p95 ≤60 s to assigned slot, and reconcile NFR §2/§3. Also clarify N=5 min. FIX by editing NFR and ADR-009 wording.

Finding 7 [major] — no resource-level authorization (IDOR risk). VALID. Fix: state that every subscription/charge/payment resource is bound to the authenticated TSP (mTLS cert subject / X-API-Key ↔ tspId); requests for resources of another ТСП → 403/404. Add to tsp-api.md §1 authorization and to ACCEPTANCE (AC-15). FIX.

Finding 8 [major] — catch-up after downtime undefined; N missed periods could mass-backfill. VALID. Fix: add catch-up policy: on recovery, missed periods for the same subscription are processed sequentially with backpressure, bounded catch-up window/limit; policy for >K missed periods (skip/dunning/manual). Add to subscription-state-machine §6 and NFR/ACCEPTANCE. FIX.

Finding 9 [minor] — charge status exposure differs. VALID. tsp-api/openapi expose SCHEDULED|INITIATED|PAID|CREDITED|COMPLETED|FAILED but spec §7 says TSP sees only SCHEDULED|PAID|COMPLETED|FAILED. Fix: align — either expose the full enum or restrict. I'll align to the API enum (simpler) and fix spec §7 to match openapi. FIX.

Finding 10 [minor] — S2 guard "условия совпадают" unverifiable; mandate.activated lacks conditions. VALID. Fix: add `termsHash` to mandate.activated event (adapter normalizes) OR change guard to compare stored mandateRef/terms via getMandateStatus. Simplest: mandate.activated carries `termsHash` (hash of agreed terms) and AD-009 requires matching; or state that conditions are stored at registration and activation only flips state (verification via `getMandateStatus` reconciliation). Fix: mandate.activated includes `termsHash`; S2 guard = termsHash matches the registered mandate. FIX (edit opkc-adapter event fields + spec S2).

Finding 11 [minor] — SubscriptionRequest can't machine-enforce conditionality (description-only), period free string, dayOfPeriod unbounded. VALID. Fix with someOf/oneOf or constraints; at minimum document validation and add fitness. I'll add `oneOf`/validation notes and bounds. Keep pragmatic: add `minimum`/`maximum` for dayOfPeriod (1–28/31) and make period an enum (MONTHLY|WEEKLY|...); add conditional requirement note. openapi 3.0 doesn't have if/then (3.1 does); use oneOf with two object variants or document validation. I'll use `period` enum + dayOfPeriod bounds + note that amount/maxAmount are conditionally required (server enforces; test AC). FIX partially.

Great — all 11 findings are legitimate. I should fix them and re-run gates + re-review? Re-review would be ideal but costly; at minimum I fix and note. The adversarial skill wants READY/NOT-READY. I'll incorporate fixes, then update A3-DECISION review section to reflect the independent review outcome (NOT-READY → findings), and record resolutions in a new doc or in A3-DECISION. Then optionally re-dispatch review. Given "measure twice", I'll fix and do a focused re-review of the specific blocker/major items. But re-dispatching another agent costs; I think one re-review is warranted for a Critical package. Let me fix first, then reply.

Let me plan edits:

A) docs/spec/subscription-state-machine.md:
 - C2 guard: "подписка `ACTIVE` **на момент инициации**, глобальный stop-new-charges выключен; мандат не отозван".
 - Add in-flight policy: revoke/suspend during SCHEDULED → charge cancelled; during INITIATED → завершается или отменяется по протоколу, новый не создаётся.
 - C1 guard: for FIXED mode only engine; merchant-initiated only for VARIABLE.
 - Add per-period uniqueness: one charge per (subscriptionId, periodKey); periodKey = normalized period (scheduled) or billingReference (merchant-initiated); if a charge for the period exists → return it.
 - §6 catch-up policy.
 - §7 align statuses with API enum.
 - S2 guard termsHash.
 - Add "stop-new-charges" re-check at C2.

B) docs/spec/state-machine.md: add T13 (CREATED → PAID for origin=SUBSCRIPTION) + note; list in DELTA MODIFIED.

C) openapi/tsp-api.yaml: 
 - ChargeRequest: require amount + billingReference; add description.
 - SubscriptionRequest: period enum; dayOfPeriod minimum/maximum; maxAmountPerPeriod; note conditional.
 - Subscription: add maxAmountPerPeriod.
 - Charge enum keep as is (already includes INITIATED/CREDITED).
 - Add 403 problem to charges/revoke? optional.

D) docs/contracts/tsp-api.md:
 - §1 authorization: resource bound to authenticated TSP (403/404).
 - §3.6 add maxAmountPerPeriod; period enum; dayOfPeriod bounds.
 - §3.8 billingReference required; FIXED disallows merchant charge (422 CHARGE_NOT_ALLOWED_FOR_FIXED); per-period uniqueness; add error codes.
 - §4 error codes add CHARGE_NOT_ALLOWED_FOR_FIXED, PERIOD_ALREADY_CHARGED (or reuse idempotent return), FORBIDDEN_RESOURCE.
 - §7 statuses note.
 
E) docs/contracts/opkc-adapter.md: mandate.activated add termsHash.

F) ADR-009 §3: sharding by tspId (bulkhead), per-subscription ordering; jitter window wording; catch-up.
 
G) ADR-008 §3/6? mention per-period cap and variable-only merchant charge? Add constraint. Maybe minimal.

H) NFR.md: reconcile §2/§3 (billing window), add catch-up, per-period cap, add authorization/no-cross-TSP, statuses.

I) ACCEPTANCE.md: add AC-15 (authorization/IDOR), AC-16 (revoke during in-flight), AC-17 (per-period cap & billingReference), AC-18 (catch-up bound); update readiness verdict (independent review NOT-READY, findings addressed). Update §5 rollback maybe.

J) A3-DECISION.md: replace "черновой проход" §5 with the independent adversarial review verdict + resolutions; keep questions.

K) docs/rfp/vendor-rfp.md: add subscription methods/events + criterion. Need to read it first.

L) DELTA.md: add MODIFIED docs/spec/state-machine.md, docs/rfp/vendor-rfp.md; mention fixes.

M) CONSTRAINTS.yaml: maybe add rule for RFP? Not needed.

That's a lot but necessary. Let me read the RFP file and the state-machine.md exactly (I have state-machine.md from earlier read). Let me read vendor-rfp.md.

Let me read docs/rfp/vendor-rfp.md.

Then perform edits.

Let me be efficient: read RFP, then do edits in batches.

Let me start.
The independent review found real, evidence-based gaps. I'll verify each against the files and fix them. First, the RFP file I haven't read yet.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/rfp/vendor-rfp.md", new_string="5. Эксплуатационную документацию, метрики, runbook.\n6. Поддержку и SLA.\n7. **Подписочный транспорт СБП** (расширение дельты `sbp-subscrip, old_string="5. Эксплуатационную документацию, метрики, runbook.\n6. Поддержку и SLA.\n\n**Не входит в scope вендора:** ядро шлюза (API ТСП, статусная м)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/rfp/vendor-rfp.md", new_string="| G7 | Передача исходного кода/эскроу на случай прекращения поддержки | Условия эскроу в контракте |\n| G8 | **Поддержка подписочного прото, old_string="| G7 | Передача исходного кода/эскроу на случай прекращения поддержки | Условия эскроу в контракте |")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/rfp/vendor-rfp.md", new_string="| Соответствие контракту opkc-adapter (полнота, нормализация, идемпотентность, включая подписочные операции §3.1) | 25 | Сверка спецификаци, old_string="| Соответствие контракту opkc-adapter (полнота, нормализация, идемпотентность) | 25 | Сверка спецификации + POC |")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/rfp/vendor-rfp.md", new_string="- **Методы** (§3): `registerTsp`, `createPaymentLink`, `getPaymentStatus`, `cancelPaymentLink`, `createRefund`, `getRefundStatus`, `getReco, old_string="- **Методы** (§3): `registerTsp`, `createPaymentLink`, `getPaymentStatus`, `cancelPaymentLink`, `createRefund`, `getRefundStatus`, `getReco)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/rfp/vendor-rfp.md", new_string="| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |\n| P9 | Подп, old_string="| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/rfp/vendor-rfp.md", new_string="**Kill criteria** (стоп в любой момент): не подтверждён G3 (идемпотентность); не подтверждён G8 (подписки); POC не проходит P2/P4/P10; венд, old_string="**Kill criteria** (стоп в любой момент): не подтверждён G3 (идемпотентность); POC не проходит P2/P4; вендор не может предоставить тестовый )`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/rfp/vendor-rfp.md", new_string="- [ ] Контракт opkc-adapter.md зафиксирован как v1.0-draft (после ревью A1), включая подписочные операции §3.1.\n- [ ] Подтверждена поддерж, old_string="- [ ] Контракт opkc-adapter.md зафиксирован как v1.0-draft (после ревью A1).")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/rfp/vendor-rfp.md", new_string="- Связано: ADR-007 (гибрид), ADR-008, ADR-009, ADR-003, AD-004, AD-008, AD-009, AD-010, `docs/contracts/opkc-adapter.md`", old_string="- Связано: ADR-007 (гибрид), ADR-003, AD-004, AD-008, `docs/contracts/opkc-adapter.md`")`

Good. Now let me make all the fixes. Let me do them methodically. This is a lot of edits; I'll batch where possible on different files (parallel safe across files).

Let me start with the RFP (Finding 4), the state-machine.md (Finding 3), opkc-adapter mandate.activated termsHash (Finding 10), and ADR-009 sharding (Finding 5).

Then subscription-state-machine (Findings 1, 2, 8, 9, 10), openapi (2, 11), tsp-api (2, 7, 9, 11), NFR (6, 1, 8), ACCEPTANCE (add ACs, readiness), A3-DECISION (review update), DELTA (MODIFIED list).

Let me do RFP edits:

RFP §1 scope list: add item for subscriptions:
"7. Подписочный транспорт: регистрация/отзыв мандата, инициация списаний по мандату, события `mandate.*`/`charge.*` (операции §3.1 контракта). "

RFP §2 G4: "Реализация полного набора методов/событий контракта opkc-adapter §3–4" → add "включая подписочные §3.1". Or add G8. Let me modify G4 to mention §3–§4 including §3.1, and add a dedicated gate row G8 for subscription support. I'll add G8:
"| G8 | **Поддержка подписочного протокола СБП** (opkc-adapter §3.1): регистрация/отзыв мандата, инициация списаний, события `mandate.*`/`charge.*`, идемпотентность по `reference` | Демо POC: registerMandate → mandate.activated; initiateCharge → charge.paid; повтор initiateCharge → дубля нет |"

RFP §3 weights: add subscription criterion or fold. Add row:
"| Поддержка подписок (мандат/списания): полнота и корректность §3.1 | 10 | POC-сценарии |" — and adjust others? Weights must sum 100. Currently 25+15+10+15+10+10+10+5 = 100. Adding 10 requires reducing. Simpler: fold into existing "Соответствие контракту" weight 25 (mention §3.1) and "Дорожная карта" 5. I'll change the first row description to include §3.1 and note subscriptions. Avoid rebalancing.

RFP §4 technical: add subscription methods/events bullet.

RFP §5 POC: add P9/P10:
"| P9 | Подписка: registerMandate → mandate.activated | `mandateRef`, событие с `eventId` |
| P10 | **Повтор initiateCharge с тем же `reference`** | одно списание, дубля нет |
| P11 | Отзыв: revokeMandate → mandate.revoked | событие, дальнейшие initiateCharge отклоняются |

RFP §11 checklist: add subscription item.

RFP kill criteria: add "не подтверждён G8".

Let me do these edits.

Actually to limit scope, I'll make targeted edits: §1 add item 7; §2 add G8; §3 first row desc; §4 add bullet; §5 add P9-P11; §9 kill criteria add; §11 add checklist item. That's ~7 edits. Fine.

Let me batch them.

Then state-machine.md T13.

Then opkc-adapter termsHash.

Then ADR-009 §3 sharding + jitter.

Let me do batch 1 (RFP + state-machine + opkc + ADR-009 = different files, parallel-safe).

RFP edits: 7 edits same file — do sequentially in one message; disjoint anchors.

Let me write them.

RFP §1 current:
```
5. Эксплуатационную документацию, метрики, runbook.
6. Поддержку и SLA.

**Не входит в scope вендора:** ...
```
Add item 7 before the "Не входит" line.

RFP §2 table last row G7 then §3. Add G8 after G7.

RFP §3 first row:
"| Соответствие контракту opkc-adapter (полнота, нормализация, идемпотентность) | 25 | Сверка спецификации + POC |"
→ "... включая подписочные операции §3.1 | 25 | ..."

RFP §4 Методы bullet: add subscription ops.

RFP §5 table: after P8 row add P9-P11.

RFP §9 kill criteria: append.

RFP §11 checklist: add.

Let me do it.

state-machine.md: I need the exact text. From earlier read, §2 table ends:
```
| T12 | `COMPLETED` | (остаётся `COMPLETED`) | **частичный** возврат завершён | сумма возврата < суммы платежа | запись в `refunds[]`, вебхук `refund.completed` |

## 3. Запрещённые переходы (инварианты)
```
I'll add T13 and T14 rows before `## 3`.

T13: `CREATED` → `PAID` | подтверждение списания по мандату (нотификация/сверка ОПКЦ) | `origin=SUBSCRIPTION`, мандат `ACTIVE`, сумма в пределах мандата | outbox «зачисление в АБС»
T14: `CREATED` → `FAILED` | отклонение списания по мандату | `origin=SUBSCRIPTION` | errorCode, dunning по политике

Also add a note that QR_ISSUED is skipped for subscription-origin payments.

And in §3 forbidden transitions, add "Для `origin=SUBSCRIPTION` переход `QR_ISSUED` не применяется; зачисление — только из `PAID` после подтверждённого списания (AD-005)."

opkc-adapter: `mandate.activated` row add `termsHash`:
"| `mandate.activated` | согласие подтверждено плательщиком | `reference` (= `subscriptionId`), `mandateRef`, `activatedAt` |"
→ add `termsHash`.
Also §3.1 registerMandate response includes termsHash? The registration returns consentUrl; the hash is computed by core and echoed by adapter. I'll say adapter echoes `termsHash` in `mandate.activated` equal to the hash of accepted terms provided at registration. Add to §3.1 note maybe. Keep simple: add field + one sentence.

ADR-009 §3 bullet currently:
"3. **Изоляция и сглаживание.** Очереди шардируются по подпискам (bulkhead — сбой «шумного» ТСП не роняет остальных), нагрузка сглаживается (queue-based load leveling), время старта списания получает **джиттер** в окне ±N минут (не «все в 00:00:00»). Конкурирующие потребители дают масштабирование, DLQ — изоляцию ядовитых сообщений."
→ Rewrite: shard by tspId (bulkhead isolation per ТСП), ordering per subscription within partition; billing window with jitter; catch-up.

Let me write the replacement:
"3. **Изоляция и сглаживание.** Очереди шардируются по **`tspId`** (bulkhead: сбой «шумного» ТСП не роняет остальных), внутри шарда порядок гарантируется по ключу `subscriptionId`; нагрузка сглаживается (queue-based load leveling), а плановые списания раскладываются по **окну списаний** (baseline — несколько часов, а не минуты) с джиттером слота, чтобы не собирать портфель в одну секунду. Конкурирующие потребители дают масштабирование, DLQ — изоляцию ядовитых сообщений. Пропущенные за простой периоды обрабатываются ограниченной догоняющей очередью (catch-up) с backpressure — см. `NFR.md` §3."

Also ADR-009 §2 mentions sharding by hash(subscriptionId) — update to tspId? §2: "«тик» планировщика защищён leader election/lease либо шардированием по `hash(subscriptionId)`". Change to `hash(tspId)` for bulkhead? Hmm, leadership protects the tick; shard key for processing is tspId. Let me edit §2: "шардированием по `hash(tspId)` (bulkhead по ТСП)". Actually the tick leader election is separate from processing shards. To keep consistent, I'll say "шардированием потребителей по `hash(tspId)`".

Let me apply.

Also ADR-009 Consequences negative mentions "окне ±N относительно идеального времени" — update to billing window wording maybe. Minor; I'll leave "окне ±N" but NFR clarifies. Actually finding 6 was about NFR; I'll fix NFR to define billing window explicitly.

Let me do batch 1 now.

Then batch 2: subscription-state-machine edits, openapi, tsp-api, NFR, ACCEPTANCE, A3-DECISION, DELTA.

Let me go.
All 11 findings are legitimate. Let me fix them, starting with the RFP gap, the payment-FSM edge, the mandate event, and the sharding key.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/state-machine.md", new_string="| T12 | `COMPLETED` | (остаётся `COMPLETED`) | **частичный** возврат завершён | сумма возврата < суммы платежа | запись в `refunds[]`, вебх, old_string="| T12 | `COMPLETED` | (остаётся `COMPLETED`) | **частичный** возврат завершён | сумма возврата < суммы платежа | запись в `refunds[]`, вебх)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/opkc-adapter.md", new_string="| `mandate.activated` | согласие подтверждено плательщиком | `reference` (= `subscriptionId`), `mandateRef`, `activatedAt`, `termsHash` (хэ, old_string="| `mandate.activated` | согласие подтверждено плательщиком | `reference` (= `subscriptionId`), `mandateRef`, `activatedAt` |")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/opkc-adapter.md", new_string="Статусные модели ОПКЦ для мандата и списания нормализуются адаптером так же, как платёжные; ядро не зависит от конкретных значений НСПК. Вс, old_string="Статусные модели ОПКЦ для мандата и списания нормализуются адаптером так же, как платёжные; ядро не зависит от конкретных значений НСПК. Вс)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-009-ispolnenie-periodic, new_string="2. **Единственный писатель на charge.** Планирование выполняется через **транзакционный outbox** (ADR-001, AD-002) и очередь с задержкой; «, old_string="2. **Единственный писатель на charge.** Планирование выполняется через **транзакционный outbox** (ADR-001, AD-002) и очередь с задержкой; «)`

RFP fixed. Now state-machine.md (Finding 3), opkc-adapter termsHash (Finding 10), ADR-009 sharding (Finding 5), and DESIGN references to sharding maybe.

state-machine.md edit: add T13/T14 + note.

Let me apply the edits.

state-machine §2 end + §3 head:
```
| T12 | `COMPLETED` | (остаётся `COMPLETED`) | **частичный** возврат завершён | сумма возврата < суммы платежа | запись в `refunds[]`, вебхук `refund.completed` |

## 3. Запрещённые переходы (инварианты)

- **Зачисление в АБС невозможно из любого состояния, кроме `PAID`** (AD-005). Из `CREATED`/`QR_ISSUED` — недостижимо; проверяется fitness-тестом.
```
Replace with T12 + T13/T14 + note + §3 head + added bullet.

Let me write.

opkc-adapter: mandate.activated row → add termsHash.
Also §3.1 registerMandate row mention termsHash returned? Add to note. Minimal: event row + a sentence.

ADR-009 §2 and §3.

Let me batch these across 3 files.

ADR-009 §2 line:
"2. **Единственный писатель на charge.** Планирование выполняется через **транзакционный outbox** (ADR-001, AD-002) и очередь с задержкой; «тик» планировщика защищён **leader election/lease** либо **шардированием по `hash(subscriptionId)`**. Конкурирующие инстансы не создают дубль: вставка идемпотентна по `chargeId`. Никаких независимых cron-задач на каждом узле."
→ change "шардированием по `hash(subscriptionId)`" to "шардированием потребителей по `hash(tspId)` (bulkhead по ТСП), порядок внутри шарда — по `subscriptionId`".

ADR-009 §3 line replace as planned.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine, new_string="| S2 | `PENDING_CONSENT` | `ACTIVE` | событие `mandate.activated` | `eventId` не обработан; **`termsHash` события совпадает** с хэшем зарег, old_string="| S2 | `PENDING_CONSENT` | `ACTIVE` | событие `mandate.activated` | `eventId` не обработан; условия совпадают | свидетельство согласия (`ap)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine, new_string="Charge создаётся только при `ACTIVE`-подписке (S7/S8 делают создание недостижимым, AD-011).\n\n**Периодный ключ.** `chargeId = f(subscripti, old_string="Charge создаётся только при `ACTIVE`-подписке (S7/S8 делают создание недостижимым, AD-011).\n\n| Состояние charge | Смысл |")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine, new_string="| C1 | — | `SCHEDULED` | тик планировщика / `POST /v1/subscriptions/{id}/charges` | мандат `ACTIVE` и покрывает ТСП/сумму/период; для `POST, old_string="| C1 | — | `SCHEDULED` | тик планировщика / `POST /v1/subscriptions/{id}/charges` | мандат `ACTIVE` и покрывает сумму/период | идемпотентна)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine, new_string="| C8 | `INITIATED` | `UNKNOWN` | таймаут/ошибка канала | — | **без слепого повтора**: дозапрос статуса/сверка |\n| C9 | `SCHEDULED` | `FAIL, old_string="| C8 | `INITIATED` | `UNKNOWN` | таймаут/ошибка канала | — | **без слепого повтора**: дозапрос статуса/сверка |")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine, new_string="| Тик планировщика | `chargeId = f(subscriptionId, periodKey)` | идемпотентная вставка, второй charge не создаётся |\n| `POST /subscription, old_string="| Тик планировщика | `chargeId = f(subscriptionId, periodStart)` | идемпотентная вставка, второй charge не создаётся |\n| `POST /subscripti)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine, new_string="| `revoke`/`suspend`/`resume` | `Idempotency-Key` | идемпотентно |\n\n> Повторный `POST charges` с **другим** `Idempotency-Key`, но тем же , old_string="| `revoke`/`suspend`/`resume` | `Idempotency-Key` | идемпотентно |")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine, new_string="- **Catch-up после простоя**: пропущенные периоды перепланируются тем же `periodKey` (идемпотентно) через **ограниченную догоняющую очередь, old_string="- Пропущенный плановый charge (пропуск тика) — перепланируется тем же `chargeId` (идемпотентно), не теряется.")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine, new_string="Маппинг наружу: `PENDING_CONSENT`, `ACTIVE`, `PAUSED`, `REVOKED`, `EXPIRED`, `FAILED_CONSENT`. Для charge наружу выставляются состояния `SC, old_string="Маппинг наружу: `PENDING_CONSENT`, `ACTIVE`, `PAUSED`, `REVOKED`, `EXPIRED`, `FAILED_CONSENT`. Технические подсостояния charge (`DUNNING`, )`

Now the subscription-state-machine.md fixes (findings 1, 2, 8, 9, 10) — substantial. Let me rewrite the relevant sections.

I'll do targeted edits:

1. §2 S2 guard: "условия совпадают" → "`termsHash` события совпадает с хэшем зарегистрированного мандата". Also S2 uses mandate.activated.

2. §3 table: 
 - Add "периодный ключ" concept.
 - C1 guard: ACTIVE + (FIXED → только плановый; VARIABLE → плановый или по запросу ТСП) + per-period uniqueness.
 - C2 guard: "подписка `ACTIVE` **на момент инициации**, stop-new-charges выключен, мандат не отозван".
 - C8 unchanged.
 - Add C9: charge cancellation on revoke/suspend.

Let me restructure §3: add a paragraph before the table defining charge key and in-flight policy, then modify C1/C2, add C9.

3. §5 idempotency table: add per-period uniqueness row / clarify billingReference.

4. §6 catch-up policy.

5. §7 status alignment.

Let me do it as a few edits.

Edit A: S2 guard.
Old: "| S2 | `PENDING_CONSENT` | `ACTIVE` | событие `mandate.activated` | `eventId` не обработан; условия совпадают | свидетельство согласия (`append-only`), outbox, вебхук `subscription.activated` |"
New: "| S2 | `PENDING_CONSENT` | `ACTIVE` | событие `mandate.activated` | `eventId` не обработан; **`termsHash` события совпадает** с хэшем зарегистрированного мандата | свидетельство согласия (`append-only`), outbox, вебхук `subscription.activated` |"

Edit B: §3 intro + table rows. The §3 section:
```
## 3. Жизненный цикл charge

Charge создаётся только при `ACTIVE`-подписке (S7/S8 делают создание недостижимым, AD-011).

| Состояние charge | Смысл |
...
Технические подсостояния: ...

| № | From | To | Триггер | Guard | Действие |
|---|---|---|---|---|---|
| C1 | — | `SCHEDULED` | тик планировщика / `POST /v1/subscriptions/{id}/charges` | мандат `ACTIVE` и покрывает сумму/период | идемпотентная вставка по `chargeId` + outbox |
| C2 | `SCHEDULED` | `INITIATED` | отправка `initiateCharge` адаптеру | — | `attemptSeq += 1` |
| C3 | ...
| C8 | `INITIATED` | `UNKNOWN` | таймаут/ошибка канала | — | **без слепого повтора**: дозапрос статуса/сверка |
```

I'll replace the "Charge создаётся только..." paragraph + C1 + C2, and add C9 after C8.

Let me write:

"Charge создаётся только при `ACTIVE`-подписке (S7/S8 делают создание недостижимым, AD-011). **Ключ списания — периодный**: `chargeId = f(subscriptionId, periodKey)`, где `periodKey` = нормализованный плановый период (для планового списания) либо `billingReference` ТСП (для списания по запросу). Один `periodKey` → ровно один charge: повторный тик или повторный запрос возвращает существующий charge, второй дебет не создаётся (AD-010). Списание по запросу ТСП разрешено **только для `amountMode=VARIABLE`**; для `FIXED` списания инициирует исключительно движок. Мандат несёт per-charge лимит (`maxAmount`) и **лимит за период** (`maxAmountPerPeriod`), которые проверяются при создании charge.

**Политика in-flight при отзыве/паузе:** подписка, перешедшая в `PAUSED`/`REVOKED`, не создаёт новые charge; уже созданный charge в `SCHEDULED` — отменяется (C9); charge в `INITIATED` — доводится до терминального состояния либо отменяется по протоколу, повторно не инициируется."

Then C1 row:
"| C1 | — | `SCHEDULED` | тик планировщика / `POST /v1/subscriptions/{id}/charges` | мандат `ACTIVE` и покрывает ТСП/сумму/период; для `POST` — `amountMode=VARIABLE`; `periodKey` ещё не заряжен (иначе возврат существующего charge) | идемпотентная вставка по `chargeId` + outbox |"

C2 row:
"| C2 | `SCHEDULED` | `INITIATED` | отправка `initiateCharge` адаптеру | **на момент инициации**: подписка `ACTIVE`, мандат не отозван, глобальный stop-new-charges выключен (перепроверка при де-очереди) | `attemptSeq += 1` |"

Add C9 after C8:
"| C9 | `SCHEDULED` | `FAILED` (отменён) | отзыв/пауза подписки или stop-new-charges до инициации | charge ещё не `INITIATED` | закрытие без списания, outbox, отчёт |"

Also note: C4 row references SCHEULED/DUNNING; fine.

Edit C: §5 idempotency — add row:
"| Тик и `POST charges` за один период | `periodKey` (→ `chargeId`) | тот же charge; второй дебет не создаётся |"
Actually there's already "Тик планировщика | chargeId = f(...)". Let me update it to periodKey and add POST charges row (exists: "POST /subscriptions/{id}/charges | Idempotency-Key | тот же chargeId"). I'll add explicit note about period collision: "Повтор запроса с другим `Idempotency-Key`, но тем же `billingReference` → тот же charge (период уже заряжен), не второй дебет."

Let me add a bullet after the idempotency table.

Edit D: §6 catch-up:
Replace "Пропущенный плановый charge (пропуск тика) — перепланируется тем же `chargeId` (идемпотентно), не теряется."
with catch-up policy:
"- **Catch-up после простоя**: пропущенные периоды перепланируются тем же `periodKey` (идемпотентно) через **ограниченную догоняющую очередь с backpressure**. Число пропущенных периодов, обрабатываемых автоматически, ограничено (baseline ≤ 2); при большем пропуске — политика `skip`/эскалация в dunning по решению бизнеса, без «лавины» задним числом (NFR §3)."

Edit E: §7 statuses align:
Old: "Технические подсостояния charge (`DUNNING`, `UNKNOWN`, `ABS_PENDING`) наружу не выставляются; для charge ТСП видит агрегированные статусы (`SCHEDULED`, `PAID`, `COMPLETED`, `FAILED`) и флаг `dunning`."
New: "Наружу выставляются состояния charge `SCHEDULED`, `INITIATED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED` (совпадает с `openapi/tsp-api.yaml`); технические подсостояния (`DUNNING`, `UNKNOWN`, `ABS_PENDING`) наружу не выставляются, но отражаются флагом `dunning`."

Let me apply these 5 edits.

Then openapi edits (Findings 2, 7, 11), tsp-api edits (2,7,9,11), NFR (6,1,8), ACCEPTANCE (new ACs + readiness update), A3-DECISION (review section), DELTA (MODIFIED list + gates remain).

Let me do the subscription-state-machine edits now.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/openapi/tsp-api.yaml", new_string="    SubscriptionRequest:\n      type: object\n      required: [tspId, amountMode, currency, period]\n      properties:\n        tspId: {typ, old_string="    SubscriptionRequest:\n      type: object\n      required: [tspId, amountMode, currency]\n      properties:\n        tspId: {type: strin)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/openapi/tsp-api.yaml", new_string="        amountMode: {type: string, enum: [FIXED, VARIABLE]}\n        amount: {type: integer}\n        maxAmount: {type: integer}\n        m, old_string="        amountMode: {type: string, enum: [FIXED, VARIABLE]}\n        amount: {type: integer}\n        maxAmount: {type: integer}\n        c)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/openapi/tsp-api.yaml", new_string="    ChargeRequest:\n      type: object\n      required: [amount, billingReference]\n      properties:\n        amount: {type: integer, desc, old_string="    ChargeRequest:\n      type: object\n      required: [amount]\n      properties:\n        amount: {type: integer, description: Сумма в к)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/openapi/tsp-api.yaml", new_string="        '201':\n          description: Списание принято\n          content:\n            application/json:\n              schema: {$ref: '#, old_string="        '201':\n          description: Списание принято\n          content:\n            application/json:\n              schema: {$ref: '#)`

Now openapi edits (findings 2, 11): ChargeRequest billingReference required; SubscriptionRequest period enum + dayOfPeriod bounds + maxAmountPerPeriod; Subscription add maxAmountPerPeriod; also add 403 problem? Optional. Let me edit the openapi.

Current relevant snippets:
```
    SubscriptionRequest:
      type: object
      required: [tspId, amountMode, currency]
      properties:
        tspId: {type: string}
        amountMode: {type: string, enum: [FIXED, VARIABLE]}
        amount: {type: integer, description: 'Обязательно при amountMode=FIXED (копейки)'}
        maxAmount: {type: integer, description: 'Обязательно при amountMode=VARIABLE — лимит одного списания (копейки)'}
        currency: {type: string, default: RUB}
        period: {type: string, description: 'Периодичность плановых списаний, напр. MONTHLY'}
        dayOfPeriod: {type: integer, description: 'День периода для планового списания'}
        expiresAt: {type: string, format: date-time, description: 'Срок действия согласия'}
        merchantOrderId: {type: string}
        description: {type: string}
```
Change period to enum, dayOfPeriod bounds, add maxAmountPerPeriod.

```
    ChargeRequest:
      type: object
      required: [amount]
      properties:
        amount: {type: integer, description: Сумма в копейках}
        billingReference: {type: string, description: 'Сквозная ссылка периода ТСП (для детерминированного chargeId)'}
        description: {type: string}
```
Change required to [amount, billingReference].

Subscription schema: add maxAmountPerPeriod.

Also add to charges endpoint responses a 403? Let me add 403 to a couple of endpoints for authz (Finding 7). Actually authorization is better documented in tsp-api.md §1; adding 403 to openapi is a plus. Let me add '403' to the charges POST and revoke POST? Keep minimal but meaningful: add 403 to `/v1/subscriptions/{subscriptionId}/charges` POST and to `/v1/subscriptions` POST? Authz for resource binding affects GET/paths with subscriptionId. I'll add a shared 403 to the charges and revoke operations. Hmm, editing openapi again risks lint. Let me add to charges POST only + document in md. Actually Finding 7 is about resource-level authz; documenting in tsp-api.md §1 + ACCEPTANCE is sufficient, plus adding 403 in openapi strengthens. Let me add 403 to the charges POST and revoke POST.

Let me make the edits.

Also `Subscription` schema add maxAmountPerPeriod.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/tsp-api.md", new_string="- Авторизация ТСП: **mTLS** (сертификат ТСП, выпущенный УЦ банка) + `X-API-Key`. Детали финализирует ИБ на A4; для v0.1 — mTLS обязателен.\, old_string="- Авторизация ТСП: **mTLS** (сертификат ТСП, выпущенный УЦ банка) + `X-API-Key`. Детали финализирует ИБ на A4; для v0.1 — mTLS обязателен.")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/tsp-api.md", new_string="Правила: до подтверждения плательщиком (`ACTIVE`) ни одно `charge` не создаётся (AD-009). Условия мандата (лимит, режим суммы, период) имму, old_string="Правила: до подтверждения плательщиком (`ACTIVE`) ни одно `charge` не создаётся (AD-009). Условия мандата (лимит, режим суммы, период) имму)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/tsp-api.md", new_string="`POST /v1/subscriptions/{subscriptionId}/charges` (обязателен `Idempotency-Key`) — **только для `amountMode=VARIABLE`**; для `FIXED`-подпис, old_string="`POST /v1/subscriptions/{subscriptionId}/charges` (обязателен `Idempotency-Key`) — для переменных сумм и внеплановых списаний в пределах ма)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/tsp-api.md", new_string="Коды подписок (v0.2): `SUBSCRIPTION_NOT_ACTIVE` (422), `AMOUNT_EXCEEDS_MANDATE` (422), `AMOUNT_EXCEEDS_PERIOD` (422), `CHARGE_NOT_ALLOWED_F, old_string="Коды подписок (v0.2): `SUBSCRIPTION_NOT_ACTIVE` (422), `AMOUNT_EXCEEDS_MANDATE` (422), `SUBSCRIPTION_TERMINAL` (422 — операция над `REVOKED)`

Now tsp-api.md edits (findings 2, 7, 9, 11). Let me patch:
- §1 authorization: add resource binding + 403.
- §3.6 SubscriptionRequest example: add maxAmountPerPeriod, period enum, dayOfPeriod bounds.
- §3.8: billingReference required; FIXED disallows; per-period uniqueness; add error codes.
- §4 error codes: add CHARGE_NOT_ALLOWED_FOR_FIXED, AMOUNT_EXCEEDS_PERIOD, FORBIDDEN_RESOURCE.
- §7 statuses already align (openapi) — I stated "SCHEDULED | INITIATED | PAID | CREDITED | COMPLETED | FAILED" in §3.8; good.

Let me apply edits.

§1 line:
"- Авторизация ТСП: **mTLS** (сертификат ТСП, выпущенный УЦ банка) + `X-API-Key`. Детали финализирует ИБ на A4; для v0.1 — mTLS обязателен."
Add after: "- **Привязка ресурсов к ТСП:** каждый ресурс (`paymentId`/`subscriptionId`/`chargeId`/`refundId`) принадлежит аутентифицированному ТСП (сертификат mTLS ↔ `tspId`); доступ к чужому ресурсу → `403 FORBIDDEN_RESOURCE` (без раскрытия существования)."

§3.6 example: add maxAmountPerPeriod? The example is FIXED mode; per-period cap optional for FIXED. Add note in rules. And update `dayOfPeriod`/`period`. The example uses `"period": "MONTHLY"` already; fine. Add rule sentence: "Для `VARIABLE` обязательны `maxAmount` и `maxAmountPerPeriod`; сервер отвергает несогласованные комбинации (валидация на A4, тест AC)."

§3.8: 
Current:
"`POST /v1/subscriptions/{subscriptionId}/charges` (обязателен `Idempotency-Key`) — для переменных сумм и внеплановых списаний в пределах мандата."
→ clarify only VARIABLE.
Request example has `billingReference` required.
Rules add: per-period uniqueness; FIXED → 422 CHARGE_NOT_ALLOWED_FOR_FIXED; amount > maxAmount/maxAmountPerPeriod → 422.

§4 codes add.

Let me edit.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/NFR.md", new_string="| Точность расписания: от **назначенного слота** до `INITIATED` | p95 ≤ 60 с, p99 ≤ 5 мин (слот — внутри окна списаний §3, джиттер ±5 мин) , old_string="| Точность расписания: от планового слота до `INITIATED` | p95 ≤ 60 с, p99 ≤ 5 мин (окно ±N с джиттером) | метрика лага планировщика | ЖКХ/)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/NFR.md", new_string="| Метрика | Цель | Метод проверки | Следствие нарушения |\n|---|---|---|---|\n| Окно списаний портфеля (baseline) | плановые списания одног, old_string="| Метрика | Цель | Метод проверки | Следствие нарушения |\n|---|---|---|---|\n| Устойчивая пропускная способность списаний | ≥ 50 charges/s)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/NFR.md", new_string="| Пропущенный тик | charge перепланируется, не теряется | тест восстановления | недосписанные деньги |\n| Один charge на `periodKey` | 0 вт, old_string="| Пропущенный тик | charge перепланируется, не теряется | тест восстановления | недосписанные деньги |")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/NFR.md", new_string="| Новые charge после `REVOKED`/`PAUSED` | 0 — проверка **на момент инициации** (перепроверка при де-очереди), не только при создании | fitn, old_string="| Новые charge после `REVOKED`/`PAUSED` | 0 | fitness + тест недостижимости | списание без согласия |")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/NFR.md", new_string="| Доступ операторов к ручным операциям (dunning, UNKNOWN) | 4-eyes | RBAC-проверка | неаудируемое вмешательство |\n| Привязка ресурса к ТСП, old_string="| Доступ операторов к ручным операциям (dunning, UNKNOWN) | 4-eyes | RBAC-проверка | неаудируемое вмешательство |")`

Now NFR.md fixes (finding 6 reconciliation of accuracy/capacity, finding 1 revocation at initiation, finding 8 catch-up, plus per-period cap and authz). Let me edit NFR §2, §3, §5.

§2 accuracy row currently:
"| Точность расписания: от планового слота до `INITIATED` | p95 ≤ 60 с, p99 ≤ 5 мин (окно ±N с джиттером) | метрика лага планировщика | ЖКХ/связь списывают не в срок; жалобы |"
→ change to "от назначенного слота до INITIATED" and mention billing window.

§3 currently:
"| Устойчивая пропускная способность списаний | ≥ 50 charges/s sustained | ... |
| Пик списаний | ≥ 300 charges/s в течение 10 мин (первое число/зарплатный период) | ... |
| Портфель подписок (baseline) | ≥ 1 000 000 активных; уточняется бизнесом | ёмкостное моделирование | ... |
| Масштабируемость | ×2 ... |
| Изоляция сбоя | сбой одного ТСП/подписки не задерживает > 1 % остальных списаний | chaos-тест (bulkhead) | ... |"

Need to add billing window consistency: to charge 1M subscriptions at 300/s needs ~55 min; so define billing window ≥ 6 h for full portfolio monthly on one day, with assigned slots and jitter. Add a row:
"| Окно списаний портфеля | baseline: плановые списания одного дня раскладываются на окно ≥ 6 ч (1 000 000 charges ≈ 46 charges/s среднего темпа) | ёмкостное моделирование + мониторинг | «лавина» в одну секунду, перегрузка НСПК/АБС |"

And change "Пик списаний" to reference billing window burst.

Also isolation row: change "сбой одного ТСП/подписки" to "сбой одного ТСП" and mention sharding by tspId.

§5 revocation row:
"| Новые charge после `REVOKED`/`PAUSED` | 0 | fitness + тест недостижимости | списание без согласия |"
→ strengthen: add "проверка на момент инициации (перепроверка при де-очереди), не только при создании". Add metric row for in-flight cancellation.

Add §4 rows for period cap and TSP binding? Put in §4 (correctness) / §9 (security). Let me add to §4:
"| Один charge на periodKey | 0 вторых дебетов | тест на повтор тика/запроса | двойное списание |"
"| Соблюдение maxAmountPerPeriod | 100% отказов при превышении | тест | списание сверх согласия |"

And §9 add authz row:
"| Доступ к чужому ресурсу (ТСП↔ресурс) | 0 успешных (403) | тест авторизации | IDOR/утечка/несанкционированное списание |"

And §3 add catch-up bound row:
"| Catch-up после простоя | ≤ 2 периода автоматически; больший простой — эскалация; без превышения пика | chaos-тест | лавина задним числом |"

Let me apply edits to NFR.

Then ACCEPTANCE (add ACs 15-18 + update readiness verdict + review section reference), A3-DECISION (replace §5 with independent review + resolutions), DELTA (MODIFIED list add state-machine.md, vendor-rfp.md, NFR note; and note fixes).

Let me do NFR edits.

§2 row edit:
old: "| Точность расписания: от планового слота до `INITIATED` | p95 ≤ 60 с, p99 ≤ 5 мин (окно ±N с джиттером) | метрика лага планировщика | ЖКХ/связь списывают не в срок; жалобы |"
new: "| Точность расписания: от **назначенного слота** до `INITIATED` | p95 ≤ 60 с, p99 ≤ 5 мин (слот внутри окна списаний + джиттер ±5 мин; см. §3) | метрика лага планировщика | ЖКХ/связь списывают не в срок; жалобы |"

§3 edit block: replace the whole §3 table body rows for throughput/capacity. Let me target the specific rows.

Actually simplest: replace the §3 table entirely.

Current §3:
```
## 3. Нагрузка и масштабирование

| Метрика | Цель | Метод проверки | Следствие нарушения |
|---|---|---|---|
| Устойчивая пропускная способность списаний | ≥ 50 charges/s sustained | нагрузочный тест | не успеть в пиковый день |
| Пик списаний | ≥ 300 charges/s в течение 10 мин (первое число/зарплатный период) | нагрузочный тест | просрочка списаний |
| Портфель подписок (baseline) | ≥ 1 000 000 активных; уточняется бизнесом | ёмкостное моделирование | недооценка инфраструктуры |
| Масштабируемость | ×2 без изменения архитектуры (шардирование/потребители) | load-test на удвоенном профиле | перепроектирование под нагрузкой |
| Изоляция сбоя | сбой одного ТСП/подписки не задерживает > 1 % остальных списаний | chaos-тест (bulkhead) | «шумный сосед» роняет поток |
```

Replace with corrected.

Let me write.

Then §4 add rows; §5 add row; §9 add row.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/ACCEPTANCE, new_string="| AC-14 | **Where** согласие хранится, the система shall минимизировать ПДн и маскировать их в логах | ИБ-ревью, скан логов |\n| AC-15 | **, old_string="| AC-14 | **Where** согласие хранится, the система shall минимизировать ПДн и маскировать их в логах | ИБ-ревью, скан логов |")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/ACCEPTANCE, new_string="9. **Идемпотентность возврата charge**: полный/частичный возврат по существующей саге.\n10. **Простой планировщика**: N пропущенных периодо, old_string="9. **Идемпотентность возврата charge**: полный/частичный возврат по существующей саге.")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/ACCEPTANCE, new_string="`R1…R12 (DELTA.md) → AD-009/010/011 → ADR-008/ADR-009 → AC-1…AC-18 → NFR.md`.\nОтдельно: `AC-6` опирается на существующий AD-005 и не вводи, old_string="`R1…R12 (DELTA.md) → AD-009/010/011 → ADR-008/ADR-009 → AC-1…AC-14 → NFR.md`.\nОтдельно: `AC-6` опирается на существующий AD-005 и не вводи)`

Now ACCEPTANCE.md: add AC-15..AC-18 and update readiness verdict referencing independent review; also add negative scenarios 10-12. Let me edit.

Add rows after AC-14:
| AC-15 | **If** ТСП обращается к ресурсу другого ТСП, **then** the СБП-шлюз shall вернуть `403` и не раскрывать существование | тест авторизации (IDOR) |
| AC-16 | **If** отзыв/пауза/stop-new-charges срабатывает до инициации charge, **then** the СБП-шлюз shall отменить `SCHEDULED` charge без списания; для `INITIATED` — довести до терминального/отменить по протоколу | тест гонки отзыва и списания |
| AC-17 | **When** ТСП запрашивает списание, the СБП-шлюз shall требовать `billingReference`, возвращать существующий charge при повторном периоде и отвергать превышение `maxAmount`/`maxAmountPerPeriod` и режим `FIXED` | контрактный тест (границы, повтор, FIXED) |
| AC-18 | **If** планировщик пропустил периоды (простой), **then** the СБП-шлюз shall перепланировать ≤ 2 периода с backpressure, не превышая пик | chaos-тест простоя |

§2 negative: add 10-12:
10. **Простой планировщика**: N пропущенных периодов → ограниченный catch-up, без лавины (AC-18).
11. **Гонка отзыва до инициации**: SCHEDULED отменяется, debit не происходит (AC-16).
12. **Кросс-ТСП доступ**: чужой subscriptionId → 403 (AC-15).

§4 readiness: update to reference independent adversarial review (NOT-READY findings fixed). Change:
"## 4. Readiness-вердикт (черновой, до A3)"
Add a paragraph: Independent adversarial review (17..., actually) returned NOT-READY with 11 findings; all addressed; list mapping. Let me add a subsection §4.1 with the review outcome and resolution table, and note re-review recommended.

Actually A3-DECISION §5 will carry the full review record. In ACCEPTANCE I'll add a line pointing there and update verdict.

Let me edit ACCEPTANCE: add AC rows, negative rows, and update §4 with review note.

Also traceability line update.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine, new_string="**Периодный ключ.** `chargeId = f(subscriptionId, periodKey)`, где `periodKey` — нормализованный плановый период (для планового списания) л, old_string="**Периодный ключ.** `chargeId = f(subscriptionId, periodKey)`, где `periodKey` — нормализованный плановый период (для планового списания) л)`

Now update A3-DECISION.md §5: replace the "черновой проход" section with the independent adversarial review result + resolutions. Also update §5.3 (F5 self-note) since catch-up now addressed. And §1 A3-7 (per-period cap) mention. Let me replace §5 entirely.

New §5 content:

## 5. Независимое состязательное ревью и его отработка

Independent reviewer (not the author) reviewed the package on 2026-09-28 and returned VERDICT: NOT-READY with 11 findings (1 blocker-class in evidence: 2 blockers, 6 major, 3 minor). All findings verified against the artifacts and addressed; re-review recommended before A3 sign-off.

Table: # | Severity | Finding (short) | Resolution | Where fixed
1 blocker revoke not enforced at initiation → C2 guard re-check + C9 cancellation + NFR §5 → subscription-state-machine.md §3, NFR §5, AC-16
2 blocker consent scope for variable → billingReference required, maxAmountPerPeriod, FIXED disallowed, single periodKey → openapi, tsp-api §3.6/3.8, subscription-state-machine §3/§5, AC-17
3 major payment FSM edge → T13/T14 added, origin=SUBSCRIPTION path documented → docs/spec/state-machine.md, DELTA MODIFIED
4 major RFP not updated → G8 + POC P9–P11 + scope/tech/checklist → docs/rfp/vendor-rfp.md
5 major bulkhead sharding → shard by tspId, order by subscriptionId → ADR-009 §2–3, NFR §3, AC-12
6 major accuracy/capacity contradiction → billing window ≥6h + slot jitter, NFR §2/§3 reconciled → NFR §2/§3
7 major resource-level authz → resource↔TSP binding, 403, AC-15 → tsp-api §1, openapi 403, NFR §9, AC-15
8 major catch-up undefined → bounded catch-up ≤2 periods + backpressure → subscription-state-machine §6, ADR-009 §3, NFR §3, AC-18
9 minor charge status exposure → aligned to openapi enum → subscription-state-machine §7
10 minor S2 guard unverifiable → termsHash in mandate.activated → opkc-adapter §3.1/§4, subscription-state-machine §2
11 minor SubscriptionRequest validation → period enum, dayOfPeriod 1–28, required period, validation note → openapi, tsp-api §3.6

Then "Открытые вопросы ревьюера" (5 questions) — I should answer them, since they were asks. Let me add answers:
Q1 revoke during SCHEDULED/INITIATED — answered by C9/C2 policy.
Q2 FIXED vs POST charges, per-period cap, billingReference — answered.
Q3 payment FSM edge — answered T13.
Q4 vendor-rfp G4 — answered G8.
Q5 periodStart normalization/timezone — need to answer! I haven't specified period normalization. Add: periodKey normalized in the платёжный контур timezone (MSK) using the subscription's schedule; dayOfPeriod bounded 1–28 so all months valid; periodKey format e.g. `YYYY-MM`. Let me add this to subscription-state-machine §3 periodKey paragraph or a note, and answer Q5.

Let me add a sentence to subscription-state-machine periodKey: "`periodKey` нормализуется в часовом поясе банка (MSK) по расписанию подписки; формат периода — `YYYY-MM` (или `YYYY-Www` для WEEKLY); `dayOfPeriod` ограничен 1–28, чтобы период существовал в любом месяце."

Let me edit subscription-state-machine §3 periodKey sentence to add normalization. Then write A3 §5.

Let me do the periodKey edit + A3-DECISION replacement.

Also update A3-DECISION §1 A3-7 row to mention per-period cap baseline.

And §5 "Путь после A3" step 2 says independent review to be done — but we did it. Update: "Повторное независимое ревью после правок — рекомендуется."

Let me do the edits.

First subscription-state-machine periodKey normalization.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/A3-DECISIO, new_string="## 5. Независимое состязательное ревью и его отработка\n\nПакет прошёл **независимое состязательное ревью** (ревьюер ≠ автор, отдельный кон, old_string="## 5. Состязательные находки (черновой проход)\n\n> Это **не независимое ревью** (принцип: «ревьюер не равен автору»). Пакет требует незави)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/A3-DECISIO, new_string="1. Утвердить §1–§2 (заполнить/переопределить `choice`), закрыть/принять допущения.\n2. **Повторный** прогон независимого состязательного ре, old_string="1. Утвердить §1–§2 (заполнить/переопределить `choice`), закрыть/принять допущения.\n2. Независимое состязательное ревью и оценка ADR рубрик)`

Now replace A3-DECISION §5 (the "черновой проход" self-review) with the independent review + resolutions + answered questions. Let me read the current §5 text exactly (I wrote it). It starts with "## 5. Состязательные находки (черновой проход)" and ends before "## 6. Путь после A3".

Let me replace from that heading through the questions paragraph.

The old text:
```
## 5. Состязательные находки (черновой проход)

> Это **не независимое ревью** (принцип: «ревьюер не равен автору»). Пакет требует независимого состязательного ревью и оценки ADR рубрикой перед A3. Ниже — самокритика, чтобы ревьюеру было от чего отталкиваться.

| № | Severity | Находка | Свидетельство |
|---|---|---|---|
| F1 | major | Пиковые значения NFR (1 млн подписок, 300 charges/s) — baseline без бизнес-подтверждения; ошибка в разы меняет ёмкость | `NFR.md` §3, помечено baseline |
| F2 | major | Схема подтверждения согласия плательщиком и предуведомление не специфицированы (внешний вход) — возможно изменение UX/потока | `DESIGN.md` §5, `[ТРЕБУЕТ ПРОВЕРКИ]` |
| F3 | major | Обязательство вендора по подпискам не подтверждено; при отказе — смена транспорта (costly) | `docs/contracts/opkc-adapter.md` §8 п.7, ADR-007 expiry |
| F4 | minor | Политика dunning (попытки/окна) влияет на успешность и нагрузку; в NFR только baseline ≤ 3 | `NFR.md` §6 |
| F5 | minor | «Пропущенный тик перепланируется тем же chargeId» — нужен явный механизм восстановления расписания при длительном простое | `docs/spec/subscription-state-machine.md` §6 |
| F6 | minor | Отсутствие `model/` лишает механической трассировки REQ→NFR→AD | `IMPACT.md` §2.4 |

Вопросы автору для независимого ревьюера: как ведёт себя шлюз при отзыве мандата в момент `INITIATED`? кто владелец charge при смене ТСП? как reconcilируется расхождение частичного возврата charge?
```

Replace with the independent review section. Let me write it.

Also update §6 step 2 (independent review already done) — edit that line.

Let me do both edits.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine, new_string="Списание по запросу ТСП разрешено **только для `amountMode=VARIABLE`** (для `FIXED` списания инициирует исключительно движок). Симметрично,, old_string="Списание по запросу ТСП разрешено **только для `amountMode=VARIABLE`** (для `FIXED` списания инициирует исключительно движок). Мандат несёт)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/DELTA.md", new_string="- `docs/contracts/tsp-api.md`, `openapi/tsp-api.yaml` — версия 0.1 → 0.2 (строго аддитивно).\n- `docs/contracts/opkc-adapter.md` — добавлен, old_string="- `docs/contracts/tsp-api.md`, `openapi/tsp-api.yaml` — версия 0.1 → 0.2 (строго аддитивно).\n- `docs/contracts/opkc-adapter.md` — добавлен)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/DELTA.md", new_string="| Совместимость | `contract_diff` v0.1→v0.2 | **0 breaking**, 9 не-breaking (аддитивные пути/поля) |\n| Независимое ревью | состязательный , old_string="| Совместимость | `contract_diff` v0.1→v0.2 | **0 breaking**, 9 не-breaking (аддитивные пути/поля) |")`

Now update DELTA.md MODIFIED list to include docs/spec/state-machine.md, docs/rfp/vendor-rfp.md, and note NFR/ACCEPTANCE/A3 updates. Also update the delta's "Новые артефакты" maybe. And add a note about independent review in gates. Let me edit DELTA MODIFIED section.

Current MODIFIED:
```
## MODIFIED

- `ARCHITECTURE-SPINE.md` — добавлены **AD-009, AD-010, AD-011** ...
- `docs/solutioning.md` — ...
- `docs/nfr.md` — **не переписывается**; ...
- `docs/contracts/tsp-api.md`, `openapi/tsp-api.yaml` — версия 0.1 → 0.2 ...
- `docs/contracts/opkc-adapter.md` — добавлены подписочные операции ...
- `.arch-handoff/CONSTRAINTS.yaml` (далее `CONSTRAINTS.yaml`) — добавлены fitness-правила дельты ...
```

Add bullets:
- `docs/spec/state-machine.md` — добавлены T13/T14 и путь `origin=SUBSCRIPTION` (подписочное списание без `QR_ISSUED`).
- `docs/rfp/vendor-rfp.md` — подписки вынесены в обязательные критерии: scope §1, gate G8, POC P9–P11, kill criteria, чек-лист.
- `docs/spec/subscription-state-machine.md` (новый) etc — already in new artifacts.
- `README.md` — указатель на дельту.

Also add a "Отработка независимого ревью" note in gates or a new section. Let me add a short section before "## План отката": "## Независимое состязательное ревью" summarizing NOT-READY → addressed. Actually A3-DECISION §5 has it; DELTA can reference. I'll add one line to gates.

Let me edit DELTA.

Also I realize: the RFP is under docs/ and not a contract; the `architect_review` contracts section said "нет контрактных файлов (ни INT.contract, ни contracts/*.{yaml,yml,json})" — it looks for contracts/ dir at root, not docs/contracts or openapi. Not important.

Let me edit DELTA MODIFIED and add the review line.

Then re-run gates (fitness, spine lint, delta guard, openapi lint, contract diff) to confirm still green after edits. The CONSTRAINT rule `subscriptions-contract-additive` pattern '0 breaking' still present in tsp-api.md. `spine-charge-idempotency-invariant` pattern 'chargeId = f\(subscriptionId, periodStart\)' — WAIT: I changed ADR/spec text to periodKey, but the SPINE AD-010 still says "chargeId = f(subscriptionId, periodStart)". Good, spine unchanged. The rule matches spine. Fine.

But ADR-009 §1 still says `chargeId = f(subscriptionId, periodStart)` — that's fine (scheduled case). And AD-010 spine says periodStart. The spec now says periodKey (generalization). Slight terminology mismatch: spine AD-010 says periodStart, spec says periodKey with periodStart as one case. Acceptable: periodKey includes periodStart. But to be consistent, maybe update spine AD-010 to mention periodKey? That would break the CONSTRAINT rule pattern 'chargeId = f\(subscriptionId, periodStart\)'. Let me keep spine as-is (periodStart for scheduled) and rule matches. Fine.

Actually the adversarial finding 2 noted "scheduled key periodStart vs TSP key billingReference are different keys → two charges for one period". I resolved by defining periodKey as the general key, with periodStart/billingReference as its instantiations, and "one periodKey = one charge". But if scheduled uses periodStart=YYYY-MM-01 and TSP uses billingReference=2026-09, they're literally different strings → still two keys. My spec says periodKey is "нормализованный плановый период ... либо billingReference ТСП". For collision avoidance, both must normalize to the same canonical period. I stated normalization MSK/YYYY-MM. But a scheduled period produces periodKey=2026-09 (month), and billingReference must also be normalized to 2026-09. So a FIXED subscription can't receive TSP charges (disallowed), and a VARIABLE subscription is not engine-scheduled? Hmm — VARIABLE subscriptions may also have a schedule (period) for reminders, but charges are TSP-initiated. To be coherent: for VARIABLE, charges come from TSP with billingReference; the engine may create a charge only if no charge exists for the period and mandate is VARIABLE... This is getting intricate. Let me state: for `VARIABLE`, only TSP-initiated charges; the engine does not auto-charge (it may notify). For `FIXED`, only engine charges. Thus one path per mode → no cross-path collision. That's clean. Let me add that clarification to subscription-state-machine §3 and tsp-api §3.8 (already says POST only VARIABLE; add "движок плановых списаний — только FIXED"). And NFR/ADR-009 mention.

Let me add a sentence: "Плановые списания движка выполняются только для `amountMode=FIXED`; для `VARIABLE` списания инициирует ТСП (движок может формировать напоминание, но не debit)." This fully closes R2.

Let me edit subscription-state-machine §3 periodKey paragraph to add this, and ADR-009 maybe. Minimal: add to §3. And tsp-api §3.8 already says FIXED only engine; add symmetric "engine auto-charge only FIXED" in §3.6/3.8. I'll add to spec §3.

Let me edit.

Then DELTA edits + re-run gates.

Let me do the spec addition + DELTA edits.

  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws"}, name="mcp__spine__fitness_check")`
  `tool_call(arguments={"path": "ARCHITECTURE-SPINE.md"}, name="mcp__spine__spine_lint")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws", "base": "HEAD"}, name="mcp__spine__delta_guard")`
  `tool_call(arguments={"cwd": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws", "path": "openapi/tsp-api.y, name="mcp__spine__openapi_lint")`
  `tool_call(arguments={"cwd": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws", "format": "openapi", "new", name="mcp__spine__contract_diff")`

Now re-run all gates to confirm the package is still green after fixes: delta_guard, fitness_check, spine_lint, openapi_lint, contract_diff, and the union score. Let me batch.

Also delta validate.

Let me run.
Now let me re-run every gate after the fixes.

  `agent(description="Re-review corrected subscriptions package", prompt="You are an INDEPENDENT adversarial architecture reviewer. You did NOT design this system and you have not seen any prior review. Find what , run_in_background=false)`

All green after fixes. Wait — the 403 response I added to openapi didn't show in contract_diff findings? The diff shows only 9 additions; my 403 addition to charges POST... The old had no such path at all, so the whole new path is "added path /v1/subscriptions/{subscriptionId}/charges" — the 403 is inside it, not separately reported. Fine.

Now, let me consider whether to re-run the independent adversarial review on the fixed package. The discipline says before A3, an independent reviewer should confirm READY. Given the value and that I fixed 11 findings, a focused re-review is warranted. But it costs another agent run. The task is substantial and Critical; I think one re-review is justified to close the loop honestly. However, the instructions warn "Don't relaunch" — but that applies to not relaunching due to missing notification, not to iterating after fixes. It's a legitimate new review of a changed artifact.

Hmm. Time/context budget. I've done a lot. The user asked for an architecture package; delivering with a documented independent review (NOT-READY) + resolutions is already strong and honest. A re-review would strengthen but is optional. The adversarial skill says verdict READY/NOT-READY and the "before handoff" spirit. I labeled status as "рекомендуется повторный прогон". That's honest.

Given the guidance to be thorough but also not runaway, I think re-running the review is the right call for a Critical package that will go to A3 — it verifies my fixes actually closed the findings (and that I didn't introduce new issues). Let me do one re-review, focused, read-only. I'll dispatch a fresh general-purpose agent (fresh context = independent) with the same adversarial brief plus the list of previously found issues to verify resolution and hunt for new ones.

Actually, a fresh agent with the same brief will re-derive findings; that's genuinely independent. Let me do it. I'll ask it to (a) verify R1–R11 resolutions, (b) report any remaining/new findings, (c) verdict READY/NOT-READY, concise.

Let me dispatch, run_in_background: false.

Then update A3-DECISION §5 with the re-review outcome and DELTA if needed.

Let me do it.

I should be mindful: the previous review took one turn. Fine.

Let me write the prompt.
All gates green after the fixes. Let me close the loop with a fresh independent re-review of the corrected package.

  `tool_search(query="select:mcp__spine__rule_template_show,mcp__spine__rule_template_list")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws"}, name="mcp__spine__verdict_explain")`

The re-review confirms R1,3-10 resolved, R2/R11 partial, and raises new findings N1–N7. These are genuine:

N1 [blocker] — invariants AD-009/010/011 have no executable check; the green fitness gate is structural-only. This is valid and I partly acknowledged it (executable templates applied at implementation). But the reviewer says presenting green gate as evidence overstates assurance. Fix: 
- Add explicit `unverifiable`/`verified_by` annotations + a warning about assurance in DELTA/ACCEPTANCE, and add at least a candidate executable rule spec (the `rules template` fragment) in the delta so it's ready to apply at implementation, plus a CONSTRAINTS rule that is `warn` and notes `verified_by` pending. But adding a `command_succeeds` now would fail (no code). 
- Better: add a "Assurance gap" note (honest) and include the exact executable-rule fragments (from `rule_template_show`) in the delta as pending, plus a plan. Also the `verdict_explain` tool has a "что зелёный НЕ означает" page — I could run it and attach, which directly addresses overstating. Let me run `verdict_explain` and include its attestation in the package. That's a strong, honest fix.
- Also I can add to DELTA criteria: "executable-проверки AD-009/010/011 применяются на A4 (templates consent-before-auto-action, idempotency-key); до этого зелёный fitness — структурный, не поведенческий." and cite verdict_explain.

N2 [major] — maxAmountPerPeriod window undefined; billingReference free string can be fragmented. Valid. Fix: define the per-period window deterministically: for VARIABLE, the period is derived from the subscription schedule (not from TSP string): `periodKey` computed by the gateway from `period` + `dayOfPeriod` and the charge's date, and `billingReference` is only a correlation id, NOT the period identity. Then fragmentation impossible. Actually cleaner: periodKey = gateway-computed from schedule (YYYY-MM), and billingReference is optional correlation. But then two TSP charges in same month collide → returns existing charge (one per period). That enforces consent scope. Let me change: `periodKey` is always gateway-computed from `subscription.period` and charge date (MSK), never taken from TSP input; `billingReference` becomes optional correlation only. And per-period cap window = that calendar period. This also addresses R2 fully and R11 partial (billingReference no longer critical).

But AD-010 spine says chargeId=f(subscriptionId, periodStart). Good — matches gateway-computed period. Let me update spec/openapi/contract: periodKey computed; billingReference optional correlation; maxAmountPerPeriod enforced over the calendar period for VARIABLE. And N7 vocabulary: align spec to use `periodStart` (spine term) or update spine to `periodKey`. Better: update the spine AD-010 rule to use `periodKey` and update CONSTRAINT regex accordingly. But then the must_contain pattern changes. I can update both spine and CONSTRAINTS rule pattern to match. Let me do that to remove drift: AD-010 Rule: "chargeId = f(subscriptionId, periodKey); ...". Update CONSTRAINTS rule `spine-charge-idempotency-invariant` pattern to match new text. And ADR-009 §1 to use periodKey.

Hmm, but AD-010 also says periodStart. Let me unify on `periodKey`. Update:
- spine AD-010 Rule text: `chargeId = f(subscriptionId, periodKey)`
- CONSTRAINTS pattern: 'chargeId = f\(subscriptionId, periodKey\)'
- ADR-009 §1: `chargeId = f(subscriptionId, periodKey)`, where periodKey computed from schedule (fixed) or billingReference? No — unify: periodKey computed from schedule/date.
- subscription-state-machine §3: periodKey always gateway-computed.
Run gates after.

N3 [major] — two FSMs for one operation; need to state charge is projection or define sync. Valid. Fix: state explicitly that the **payment** (адрес истины) is the financial truth (AD-002), and the charge object is a projection/index over the payment for the subscription domain, kept consistent by the same atomic transition (charge status derived from payment status + dunning substate); reconciliation compares. Add to subscription-state-machine §1 or §3 and DESIGN. Also map charge states to payment states.

N4 [major] — NFR §5 contradiction: 0 new INITIATED vs ≤1 min propagation. Valid. Fix: change target to "0 новых `INITIATED` **после распространения** (≤1 мин); на интервале распространения допускается затухание" and AC-16 accordingly. Actually better: kill switch should be enforced with a fail-safe (default deny) so propagation is effectively immediate; but acknowledge propagation bound. I'll phrase: "0 новых INITIATED после распространения (≤ 1 мин); распространение обеспечивается fail-safe конфигурацией (default-deny при недоступности флага)". AC-16 → "after propagation".

N5 [minor] — 403 only on charges path. Fix: add 403 to other subscription/payment operations (or document that all resource-scoped endpoints return 403). Simplest: add a note in tsp-api §1 "все resource-scoped методы возвращают 403" and add 403 to a couple of openapi operations. I'll add 403 to GET subscription, suspend/resume/revoke, and payment GET? To limit churn, add 403 to the subscription GET/suspend/resume/revoke and charges GET. Hmm many edits. Alternatively state in §4 that 403 is generic for all resource-scoped endpoints and lint doesn't require per-op. I'll add a sentence to §1 and add 403 to the four subscription management ops quickly. Actually I can add 403 to each via a shared pattern... openapi doesn't support components.responses reuse easily with the current style, but I can define a response component and $ref it. Let me add to `components.responses` a `Forbidden` and reference in ops. That's cleaner but more edits. Given "minor", documenting in §1 + adding to the mutation ops (suspend/resume/revoke) is enough. Let me add 403 to those three and to GET subscription.

N6 [minor] — in-flight dunning vs revocation ambiguous. Valid. Fix: state explicitly: after REVOKED/PAUSED or stop-new-charges, an `INITIATED` charge may complete (if already authorized with payer) but **dunning/retries stop**; no re-attempt after revocation. Update §3 C2/C4 and the in-flight policy + spec §3/C4 guard.

N7 [minor] — vocabulary drift periodStart vs periodKey. Fix by unifying (see N2).

Let me implement these fixes. Then re-run gates. Given the reviewer still says NOT-READY, I should fix and ideally re-review again — but that risks an endless loop. The reviewer's blockers: N1 (assurance) and R2 partial (N2). N1 is largely about honesty of the green gate — I'll fix by (a) adding executable-rule fragments ready to apply, (b) running verdict_explain and embedding the "what green does NOT mean" attestation, (c) marking the assurance gap explicitly. N2 fix is concrete.

After fixes, the remaining NOT-READY is essentially "must implement executable checks" which is inherently post-A3 (implementation). I'll document that the package is ready for A3 decision but NOT for implementation until executable checks land — which matches the readiness verdict CONCERNS. I'll set the honest framing: package is ready for human A3; implementation gated on executable checks + external inputs. That's defensible and honest, and I'll stop iterating reviews after this round (documenting residual risks).

Let me implement fixes efficiently.

Plan of edits:
1. N2/N7: unify periodKey as gateway-computed.
   - spine AD-010 Rule text → periodKey; update CONSTRAINTS regex.
   - ADR-009 §1 text.
   - subscription-state-machine §3 periodKey paragraph: gateway-computed; billingReference = correlation only.
   - openapi ChargeRequest: billingReference optional again (correlation), keep amount required; add note.
   - tsp-api §3.8: billingReference optional correlation; periodKey computed by gateway; per-period window = calendar period.
   
   Wait — if billingReference is optional correlation and periodKey is gateway-computed, then "one charge per period" is enforced by gateway. Good. But then merchant-initiated repeated charges in the same period collide → returns existing. That's intended (one debit per period). For ТСП needing multiple charges per period (e.g., utilities charge once a month — fine). For cinema fixed monthly — engine. OK.

   Actually careful: if VARIABLE and the gateway computes periodKey from charge date + schedule, then the TSP's billingReference isn't needed for identity. Good. Keep billingReference optional for reconciliation/correlation. Update R2 resolution.

2. N3: add projection clause. subscription-state-machine §1 or a new note; DESIGN §3.
3. N4: NFR §5 + ACCEPTANCE AC-16 wording.
4. N5: tsp-api §1 note + openapi 403 on subscription management ops.
5. N6: spec §3/C4 dunning-stops clause.
6. N1: 
   - Add a CONSTRAINTS section? Add commented candidate rules? Better: add to DELTA/ACCEPTANCE an explicit "Assurance" note + run verdict_explain and embed.
   - Also add to CONSTRAINTS a `warn` rule documenting the pending executable check? A rule must pass now. `must_contain` can't check code that doesn't exist. I could add a `file_exists` rule for a planned test file — but it doesn't exist → fail. So instead, add a comment in CONSTRAINTS (already have a comment) and add explicit `verified_by: pending` notation? The schema may not support arbitrary fields; rules_report showed owner/expiry/exclude_glob/effort_hours. Adding unknown fields might be ignored or error. Avoid.
   - Instead: create a machine-readable artifact `changes/sbp-subscriptions/EXECUTABLE-CHECKS.md` listing the exact templates + fragments to apply at implementation, with the `rules template show` output. That documents the plan concretely. And embed verdict_explain attestation.

Let me run verdict_explain first (it's a tool) to get the "what green does NOT mean" page, then write EXECUTABLE-CHECKS.md and update docs.

Actually, let me also get `rule_template_show` for consent-before-auto-action and idempotency-key to embed fragments. Let me use the MCP rule_template_show (need schema). I have rule_template_list; show not fetched. Let me select it. Or use CLI `arch-be rules template show <id>` — earlier it truncated oddly. Let me use MCP.

Given budget, let me fetch: verdict_explain + rule_template_show (2 tools, need schema for show). Let me tool_search rule_template_show + call verdict_explain.

Let me do that now.

Then apply text fixes.

Let me proceed: tool_search select rule_template_show; tool_call verdict_explain.
The re-review confirms the blockers are resolved but raises new valid findings (assurance honesty, per-period window, two-FSM sync). Let me gather the verdict-boundary and rule-template evidence, then fix.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/ARCHITECTURE-SPINE.md", new_string="- **Rule**: `chargeId = f(subscriptionId, periodKey)`, где `periodKey` — нормализованный период, вычисляемый шлюзом из расписания подписки , old_string="- **Rule**: `chargeId = f(subscriptionId, periodStart)` (для переменной суммы — `f(subscriptionId, billingReference)`); повторное создание )`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="    pattern: 'chargeId = f\\(subscriptionId, periodKey\\)'", old_string="    pattern: 'chargeId = f\\(subscriptionId, periodStart\\)'")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/adr/ADR-009-ispolnenie-periodic, new_string="1. **Детерминированный идентификатор charge.** `chargeId = f(subscriptionId, periodKey)`, где `periodKey` — нормализованный период, **вычис, old_string="1. **Детерминированный идентификатор charge.** `chargeId = f(subscriptionId, periodStart)` (для переменных сумм — `f(subscriptionId, billin)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/spec/subscription-state-machine, new_string="Charge создаётся только при `ACTIVE`-подписке (S7/S8 делают создание недостижимым, AD-011).\n\n**Charge — проекция финансового состояния.**, old_string="Charge создаётся только при `ACTIVE`-подписке (S7/S8 делают создание недостижимым, AD-011).\n\n**Периодный ключ.** `chargeId = f(subscripti)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/openapi/tsp-api.yaml", new_string="    ChargeRequest:\n      type: object\n      required: [amount]\n      properties:\n        amount: {type: integer, description: Сумма в к, old_string="    ChargeRequest:\n      type: object\n      required: [amount, billingReference]\n      properties:\n        amount: {type: integer, desc)`

The verdict_explain gives exactly the "what green does NOT mean" page, including "14 из 14 правил судят по тексту; исполняемых проверок поведения: 0". This directly addresses N1 honestly. I'll embed this attestation in the package.

Now let me apply the fixes:

N2/N7: unify periodKey.
- spine AD-010 Rule → periodKey.
- CONSTRAINTS rule pattern.
- ADR-009 §1.
- subscription-state-machine §3: periodKey computed by gateway from schedule; billingReference optional correlation.
- openapi ChargeRequest: billingReference optional (correlation); keep amount required.
- tsp-api §3.8: periodKey gateway-computed; billingReference optional correlation; per-period window = calendar period defined by schedule.

Wait: if the subscription is VARIABLE, what's the schedule period? The mandate has `period` (e.g., MONTHLY) regardless of mode. So periodKey = gateway-computed calendar period from `period` and charge date. Good. For VARIABLE, engine doesn't debit but period defines the consent window.

N3: add projection clause.
- subscription-state-machine §1 (or §3): "charge — производная (проекция) состояния платежа: финансовую истину хранит платёж (AD-002); charge.status выводится из payment.status + подсостояния попытки и не может расходиться (одна транзакция); сверка сверяет charge ↔ payment ↔ ОПКЦ."
- Also DESIGN §3 note.

N4: NFR §5 wording + ACCEPTANCE AC-16.
N5: tsp-api §1 note + openapi 403 to subscription management ops.
N6: spec §3 in-flight dunning clause.

N1: create `changes/sbp-subscriptions/EXECUTABLE-CHECKS.md` with the two templates + verdict attestation; reference from DELTA/ACCEPTANCE/A3-DECISION. Also update ACCEPTANCE §4 readiness to mention assurance gap.

Let me write EXECUTABLE-CHECKS.md using the template list info I have (id, what it checks) + the verdict_explain "claimed_not_verified" text. I don't have rule_template_show details (files/commands), but I can describe the property and the apply command. That's enough.

Let me do the edits. Many; let me batch by file.

Batch A (spine + CONSTRAINTS + ADR-009 + openapi + spec):
1. spine AD-010 rule edit.
2. CONSTRAINTS regex edit.
3. ADR-009 §1 edit.
4. subscription-state-machine §3 periodKey paragraph edit (replace).
5. subscription-state-machine §3 in-flight add dunning clause.
6. subscription-state-machine §1 add projection? Let me add to §3 intro or a new bullet in §4 forbidden. I'll add a note right after "Charge создаётся только..." Actually add a paragraph "**Charge как проекция платежа.**".
7. openapi ChargeRequest billingReference optional + description.
8. tsp-api §3.8 edit.
9. tsp-api §1 note (already has resource binding; add "403 для всех resource-scoped методов").
10. NFR §5 row edit.
11. ACCEPTANCE AC-16 edit.

Let me be careful with openapi: if billingReference optional, then R2 resolution changes: the period identity is gateway-computed, so optional billingReference is fine. Good.

Let me apply batch A edits.

spine AD-010 Rule current:
"- **Rule**: `chargeId = f(subscriptionId, periodStart)` (для переменной суммы — `f(subscriptionId, billingReference)`); повторное создание возвращает тот же `chargeId` и не создаёт второй финансовый эффект. Проверка: fitness `idempotency-key` (executable-шаблон)."
→
"- **Rule**: `chargeId = f(subscriptionId, periodKey)`, где `periodKey` — нормализованный период, вычисляемый шлюзом из расписания подписки и даты; повторное создание возвращает тот же `chargeId` и не создаёт второй финансовый эффект. Проверка: fitness `idempotency-key` (executable-шаблон)."

CONSTRAINTS regex: 'chargeId = f\(subscriptionId, periodStart\)' → 'chargeId = f\(subscriptionId, periodKey\)'.

ADR-009 §1: "1. **Детерминированный идентификатор charge.** `chargeId = f(subscriptionId, periodStart)` (для переменных сумм — `f(subscriptionId, billingReference)`, где `billingReference` задаёт ТСП). ..." → "`chargeId = f(subscriptionId, periodKey)`, где `periodKey` — нормализованный период, вычисляемый шлюзом из расписания подписки и даты (MSK; `YYYY-MM` или `YYYY-Www`). `billingReference` ТСП — необязательная корреляционная ссылка, а не идентификатор периода. ..."

subscription-state-machine §3 periodKey paragraph: replace with gateway-computed version.

Let me write the new paragraph:
"**Периодный ключ.** `chargeId = f(subscriptionId, periodKey)`, где `periodKey` — период, **вычисляемый шлюзом** из расписания подписки (`period`/`dayOfPeriod`) и даты операции в часовом поясе банка (MSK), формат `YYYY-MM` (для `WEEKLY` — `YYYY-Www`). `billingReference` ТСП — необязательная корреляционная ссылка, **не** идентификатор периода. Один `periodKey` → ровно один charge: повторный тик или повторный запрос за тот же период возвращает существующий charge, второй дебет не создаётся (AD-010). ..."

Keep the rest (mode rules, window): add "Окно лимита за период = тот же календарный период `periodKey`."

Let me write full replacement.

Then in-flight paragraph add dunning clause:
"**Политика in-flight при отзыве/паузе.** ... Charge в `INITIATED` — доводится до терминального состояния либо отменяется по протоколу и **не инициируется повторно**. **Dunning/повторы после отзыва не выполняются**: если инициированный charge отклонён после `REVOKED`/`PAUSED`/stop-new-charges, он переходит в `FAILED` без новых попыток (в отличие от обычного dunning)."

Projection paragraph: add after "Charge создаётся только при ACTIVE...":
"**Charge — проекция финансового состояния.** Финансовую истину хранит платёж (AD-002); `charge.status` выводится из состояния платежа и подсостояния попытки в **той же** атомарной транзакции, не может расходиться с ним и не является вторым источником истины. Сверка сверяет цепочку `charge ↔ платёж ↔ ОПКЦ ↔ АБС`; расхождение — дефект."

Let me apply.

openapi ChargeRequest:
"    ChargeRequest:
      type: object
      required: [amount, billingReference]
      properties:
        amount: {...}
        billingReference: {type: string, description: '...обязательна'}
        description: {type: string}"
→ required: [amount]; billingReference optional correlation.

tsp-api §3.8: adjust. And §3.6 note `maxAmountPerPeriod` окно = период. And §1 add 403 note.

Let me apply.

I'll do these edits now in one batch (different files + disjoint same-file anchors).
The re-review's new findings are valid. Let me fix them — starting with period identity (no TSP-controlled key fragmentation), FSM projection, dunning-on-revoke, and kill-switch wording.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/tsp-api.md", new_string="Правила: `periodKey` **вычисляет шлюз** из расписания подписки и даты (MSK), а не ТСП; `billingReference` — необязательная корреляционная с, old_string="Правила: `billingReference` обязателен и нормализуется (напр. `YYYY-MM`); `(subscriptionId, billingReference)` задаёт `periodKey` — **один )`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/tsp-api.md", new_string="  \"billingReference\": \"2026-09\",   // опц.: корреляционная ссылка ТСП (период определяет шлюз из расписания)", old_string="  \"billingReference\": \"2026-09\",   // ОБЯЗАТЕЛЬНО: сквозная ссылка нормализованного периода ТСП — часть детерминированного chargeId")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/docs/contracts/tsp-api.md", new_string="- **Привязка ресурсов к ТСП (v0.2):** каждый ресурс (`paymentId`, `subscriptionId`, `chargeId`, `refundId`) принадлежит аутентифицированном, old_string="- **Привязка ресурсов к ТСП (v0.2):** каждый ресурс (`paymentId`, `subscriptionId`, `chargeId`, `refundId`) принадлежит аутентифицированном)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/NFR.md", new_string="| Charge после stop-new-charges | 0 новых `INITIATED` **после распространения флага** (≤ 1 мин; fail-safe default-deny при недоступности фл, old_string="| Charge после stop-new-charges | 0 новых `INITIATED`; charge в `SCHEDULED` отменяется без списания (C9) | тест kill switch | откат не оста)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/ACCEPTANCE, new_string="| AC-16 | **If** отзыв/пауза/stop-new-charges срабатывает до инициации charge, **then** the СБП-шлюз shall отменить `SCHEDULED`-charge без , old_string="| AC-16 | **If** отзыв/пауза/stop-new-charges срабатывает до инициации charge, **then** the СБП-шлюз shall отменить `SCHEDULED`-charge без )`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/openapi/tsp-api.yaml", new_string="        '200':\n          description: Подписка приостановлена\n          content:\n            application/json:\n              schema: {$, old_string="        '200':\n          description: Подписка приостановлена\n          content:\n            application/json:\n              schema: {$)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/openapi/tsp-api.yaml", new_string="        '200':\n          description: Подписка возобновлена\n          content:\n            application/json:\n              schema: {$re, old_string="        '200':\n          description: Подписка возобновлена\n          content:\n            application/json:\n              schema: {$re)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/openapi/tsp-api.yaml", new_string="        '200':\n          description: Подписка отозвана\n          content:\n            application/json:\n              schema: {$ref: ', old_string="        '200':\n          description: Подписка отозвана\n          content:\n            application/json:\n              schema: {$ref: ')`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/openapi/tsp-api.yaml", new_string="        '200':\n          description: Подписка\n          content:\n            application/json:\n              schema: {$ref: '#/compone, old_string="        '200':\n          description: Подписка\n          content:\n            application/json:\n              schema: {$ref: '#/compone)`

Now tsp-api §3.8 and §3.6 and §1 (403 note), NFR §5, ACCEPTANCE AC-16, and openapi 403 on management ops (N5).

tsp-api §3.8 current (after my earlier edit):
"Правила: `billingReference` обязателен и нормализуется (напр. `YYYY-MM`); `(subscriptionId, billingReference)` задаёт `periodKey` — **один periodKey = один charge** (AD-010). Повтор того же периода (даже с другим `Idempotency-Key`) возвращает существующий charge, а не создаёт второй дебет. Для `FIXED` → `422 CHARGE_NOT_ALLOWED_FOR_FIXED`; превышение `maxAmount`/`maxAmountPerPeriod` → `422 AMOUNT_EXCEEDS_MANDATE`/`422 AMOUNT_EXCEEDS_PERIOD`."

New:
"Правила: `periodKey` **вычисляет шлюз** из расписания подписки и даты (MSK), а не ТСП; `billingReference` — необязательная корреляционная ссылка. **Один periodKey = один charge** (AD-010): повтор за тот же календарный период (даже с другим `Idempotency-Key`) возвращает существующий charge, а не создаёт второй дебет. Лимит `maxAmountPerPeriod` действует на тот же календарный период. Для `FIXED` → `422 CHARGE_NOT_ALLOWED_FOR_FIXED`; превышение `maxAmount`/`maxAmountPerPeriod` → `422 AMOUNT_EXCEEDS_MANDATE`/`422 AMOUNT_EXCEEDS_PERIOD`."

Also the request example comment says "ОБЯЗАТЕЛЬНО" — update:
```
  "billingReference": "2026-09",   // ОБЯЗАТЕЛЬНО: ...
```
→ `// опц.: корреляционная ссылка ТСП (период определяет шлюз)`.

tsp-api §3.6 rules: add maxAmountPerPeriod window note? Already says обязательны maxAmount и maxAmountPerPeriod. Add "окно — календарный период расписания". Fine, minor; I'll append.

tsp-api §1 add: "`403 FORBIDDEN_RESOURCE` возвращается всеми resource-scoped методами (платежи, подписки, списания, возвраты), а не только списаниями."

NFR §5 row "Charge после stop-new-charges | 0 новых `INITIATED`; ..." → "0 новых `INITIATED` **после распространения флага** (≤ 1 мин, fail-safe default-deny); charge в `SCHEDULED` отменяется (C9)".

ACCEPTANCE AC-16 → add "после распространения флага (≤ 1 мин)".

openapi 403 on management ops: add '403' to GET subscription, suspend, resume, revoke, charges get. Let me add to suspend/resume/revoke and GET subscription. That's 4 edits; each has a '409' response block. For suspend/resume/revoke the structure:
```
      responses:
        '200':
          description: Подписка приостановлена
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Subscription'}
        '409':
          description: Конфликт идемпотентности
```
I'll insert 403 before 409. But the descriptions differ per op, making anchors unique. Let me do 3 edits (suspend, resume, revoke) + GET subscription. Actually to reduce churn, I'll just do GET subscription + suspend + revoke (representative). Hmm N5 wants coverage. Let me add to all: GET subscription, suspend, resume, revoke. 4 edits.

Given effort, and it's minor, I'll add to all four quickly.

GET subscription block:
```
      responses:
        '200':
          description: Подписка
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Subscription'}
        '404':
          description: Подписка не найдена
```
Insert 403 before 404.

suspend:
```
        '200':
          description: Подписка приостановлена
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Subscription'}
        '409':
```
resume: "Подписка возобновлена"
revoke: "Подписка отозвана"

Let me do these plus NFR/ACCEPTANCE/tsp-api. Batch.

Then write EXECUTABLE-CHECKS.md and update DELTA/ACCEPTANCE/A3-DECISION for N1 assurance + re-review outcome.

Let me apply this batch.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/ACCEPTANCE, new_string="| AC-17 | **When** ТСП запрашивает списание, the СБП-шлюз shall вычислить `periodKey` из расписания, вернуть существующий charge при повтор, old_string="| AC-17 | **When** ТСП запрашивает списание, the СБП-шлюз shall требовать `billingReference`, возвращать существующий charge при повторном )`
  `write_file(content="# EXECUTABLE-CHECKS — исполняемые проверки инвариантов подписок (передаются в реализацию)\n\n- Status: план к A4 (применяется на этапе реал, file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/EXECUTABLE)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/A3-DECISIO, new_string="**Остаточные внешние входы** (не закрываются инженерией): протокол НСПК, поддержка вендором, контракт АБС для переменных сумм, политика dun, old_string="**Остаточные внешние входы** (не закрываются инженерией): протокол НСПК, поддержка вендором, контракт АБС для переменных сумм, политика dun)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/DELTA.md", new_string="| Независимое ревью | состязательный контур (ревьюер ≠ автор), раунд 1 | **NOT-READY**, 11 находок (R1–R11) — адресованы правками пакета |\, old_string="| Независимое ревью | состязательный контур (ревьюер ≠ автор) | **NOT-READY**, 11 находок (R1–R11) — все адресованы правками пакета; разреш)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/DELTA.md", new_string="- `changes/sbp-subscriptions/ACCEPTANCE.md` — критерии приёмки (EARS) и план отката.\n- `changes/sbp-subscriptions/A3-DECISION.md` — что ос, old_string="- `changes/sbp-subscriptions/ACCEPTANCE.md` — критерии приёмки (EARS) и план отката.\n- `changes/sbp-subscriptions/A3-DECISION.md` — что ос)`

Now AC-17 still says "требовать billingReference" — since billingReference is now optional, fix AC-17 wording: "the СБП-шлюз shall вычислять periodKey и возвращать существующий charge при повторе периода; отвергать превышение лимитов и режим FIXED". Let me edit AC-17.

Then write EXECUTABLE-CHECKS.md (N1). Then update A3-DECISION §5 with re-review round 2 (N1–N7) and DELTA gates row + assurance note.

Let me edit AC-17 first.

AC-17 current:
"| AC-17 | **When** ТСП запрашивает списание, the СБП-шлюз shall требовать `billingReference`, возвращать существующий charge при повторном периоде и отвергать превышение `maxAmount`/`maxAmountPerPeriod` и режим `FIXED` | контрактный тест (повтор периода, границы лимитов, `FIXED`) |"
→ new:
"| AC-17 | **When** ТСП запрашивает списание, the СБП-шлюз shall вычислить `periodKey` из расписания, вернуть существующий charge при повторе периода и отвергнуть превышение `maxAmount`/`maxAmountPerPeriod` и режим `FIXED` | контрактный тест (повтор периода, границы лимитов, `FIXED`) |"

Let me also update the negative scenario 13 (fine) and 7 mention.

Now EXECUTABLE-CHECKS.md content:
- Purpose: close the assurance gap (N1): the current green gate is structural (14/14 text rules; 0 behavior checks). This doc lists executable checks to apply at implementation (A4).
- Named templates: consent-before-auto-action (AD-009), idempotency-key (AD-010), append-only-journal (AD-007/AD-009 evidence), single-source-of-truth (AD-002/charge projection), unknown-outcome-no-resend (ADR-009 UNKNOWN).
- For each: property, template id, apply command, where it lands.
- Embed verdict_explain attestation (sha256 + quotes).
- Note: applying writes test code → deferred to implementation ("Код не пиши" honored here).
- Also list the CONSTRAINTS rules to add at apply (from rule_template_apply print).

Let me write it.

Then update A3-DECISION §5 add round-2 subsection (N1–N7 + resolutions) and DELTA gates row + a note in "Гейты и доказательства" about assurance limitation. And ACCEPTANCE §4 note.

Let me do these.

For A3-DECISION §5, append a subsection after the round-1 table and Q&A:
"### Повторное ревью (раунд 2)
Fresh independent reviewer verified R1–R11 (R1, R3–R10 RESOLVED; R2/R11 PARTIAL) and raised N1–N7. Resolutions:
- N1 assurance → `EXECUTABLE-CHECKS.md` + attested verdict passport (14/14 text rules, 0 behavior checks) — реализация обязана применить шаблоны на A4.
- N2 per-period window → periodKey gateway-computed; billingReference correlation only.
- N3 two FSMs → charge = проекция платежа, одна транзакция.
- N4 kill switch wording → "после распространения ≤1 мин, fail-safe default-deny".
- N5 403 coverage → все resource-scoped методы.
- N6 dunning vs revoke → повторы после отзыва не выполняются.
- N7 vocabulary → unified periodKey (spine/ADR/CONSTRAINTS).
Remaining NOT-READY driver: executable checks land at implementation (post-A3) — this is a staging fact, not a design gap; package is ready for A3, not for implementation."

Let me write.

Then final gate re-run (fitness/spine/delta/openapi/contract_diff).

Let me do AC-17, EXECUTABLE-CHECKS.md, A3-DECISION appends, DELTA gates note, ACCEPTANCE note, then gates.

Let me batch AC-17 + new file write + A3 edit + DELTA edit + ACCEPTANCE edit.

For A3-DECISION, I need to insert the round-2 subsection. Let me anchor after the "Остаточные внешние входы" line and before "## 6. Путь после A3".

Let me craft.

Also update DELTA gates row for re-review. Current row:
"| Независимое ревью | состязательный контур (ревьюер ≠ автор) | **NOT-READY**, 11 находок (R1–R11) — все адресованы правками пакета; разрешение и ответы — `A3-DECISION.md` §5 |"
→ add second review:
"| Независимое ревью | состязательный контур (ревьюер ≠ автор), раунд 1 | **NOT-READY**, 11 находок (R1–R11) — адресованы |
| Повторное независимое ревью | раунд 2 (свежий контур) | R1, R3–R10 **RESOLVED**; R2/R11 закрыты правками; новые N1–N7 адресованы; остаточный драйвер — исполняемые проверки на A4 → `EXECUTABLE-CHECKS.md` |"

And add assurance note under the table (the existing "> ADR-оценка..." note). Add:
"> ⚠ Assurance: зелёный fitness **структурный** — 14/14 правил проверяют текст, исполняемых проверок поведения 0 (паспорт вердикта `sha256:619fa10a…`). Инварианты AD-009/AD-010/AD-011 получают исполняемые проверки на A4 — `EXECUTABLE-CHECKS.md`."

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws/changes/sbp-subscriptions/ACCEPTANCE, new_string="Независимое состязательное ревью (ревьюер ≠ автор) вернуло **NOT-READY**: раунд 1 — 11 находок (R1–R11), раунд 2 — подтвердил закрытие R1, , old_string="Независимое состязательное ревью (обзор ≠ автор) вернуло **NOT-READY** с 11 находками; все адресованы правками пакета (список и разрешение )`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws"}, name="mcp__spine__fitness_check")`
  `tool_call(arguments={"path": "ARCHITECTURE-SPINE.md"}, name="mcp__spine__spine_lint")`
  `tool_call(arguments={"cwd": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws", "path": "openapi/tsp-api.y, name="mcp__spine__openapi_lint")`

Now update ACCEPTANCE §4 readiness to mention the assurance gap and the round-2 review. And update the §4 text I edited earlier to mention N1–N7 too. Let me tweak the sentence I added:

Current: "Независимое состязательное ревью (обзор ≠ автор) вернуло **NOT-READY** с 11 находками; все адресованы правками пакета (список и разрешение — `A3-DECISION.md` §5). Остаточные пробелы ниже — внешние входы; они не блокируют вынесение на A3, но блокируют реализацию."

Update to mention round 2 and assurance:
"Независимое состязательное ревью (ревьюер ≠ автор) вернуло **NOT-READY**: раунд 1 — 11 находок (R1–R11), раунд 2 — подтвердил закрытие R1, R3–R10 и добавил N1–N7; все адресованы (список — `A3-DECISION.md` §5). **Граница зелёного**: `fitness_check` структурный (14/14 текстовых, 0 поведенческих), инварианты AD-009/010/011 получают исполняемые проверки на A4 (`EXECUTABLE-CHECKS.md`). Остаточные пробелы ниже — внешние входы; пакет готов к A3, но не к реализации."

Let me edit. Then re-run gates.

Also update IMPACT "Пробелы" to mention assurance gap maybe. Minor; skip.

Let me edit ACCEPTANCE and then re-run gates: fitness, spine_lint, delta_guard, openapi_lint, contract_diff.

Note: the CONSTRAINTS rule pattern changed from periodStart to periodKey; spine now contains periodKey → rule passes. Good.

openapi_lint after adding 403 responses — should still pass. contract_diff — more non-breaking additions.

Let me do.

  `tool_call(arguments={"base": "HEAD", "path": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws"}, name="mcp__spine__delta_guard")`
  `tool_call(arguments={"cwd": "<HARNESS>/runs-v2-pilot/cells/wyku3ck/ws", "format": "openapi", "new", name="mcp__spine__contract_diff")`
  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wyku3ck/ws && echo \"=== delta validate ===\, description="Final gate, delta validation, and file inventory")`

All green. Let me do a final delta_guard + contract_diff + delta validate to confirm, and check git status for the final file list.

Then write the final summary.

Let me run final checks and the file listing.

Also I should double check: the CONSTRAINTS rule `subscriptions-contract-additive` pattern '0 breaking' still in tsp-api.md — yes (header). And `spine-consent-invariant` pattern matches. Good (fitness passed).

Let me run final delta guard + contract diff + delta validate + git status.

Also I want to verify the mermaid C4 diagram still renders after edits (I changed DB/Q/ABS labels only). Fine.

Let me run.


Everything green and consistent. Note `.arch-handoff/mcp-calls.jsonl` is an untracked artifact created by the MCP server (call journal) — not mine to manage; leave it (it's a runtime journal). Actually it's a side effect of MCP calls. I shouldn't commit it. I'm not committing anyway. I'll mention it or ignore. It's not part of my package. I'll leave it and note nothing.

Now let me produce the final summary. The user asked: when finished, briefly list created and modified files.

Let me also double-check the `arch-be adr registry` sees the new ADRs (optional). And `rules_report` now shows 14 rules with owners. Let me quickly run rules_report to confirm the new rules have owner/expiry (nice evidence) — optional. I'll skip to save budget; fitness passed is enough.

Actually one more: `arch-be adr registry` would confirm ADR-008/009 parsed with Status/Authors. The adr-authoring skill says the parser reads Date/Status/Модель-автор. My ADRs have those. Let me quickly verify via adr_registry MCP? It's read-only. Might be nice but not essential. I'll skip.

Let me now write the final response: concise but complete, mapping to the 7 requested items, listing files, noting gates evidence and the review outcome, and the human-decision pointer.

Structure:
- What was done + route Critical.
- Mapping to 1–7.
- Gates/evidence (green) + honest boundary.
- Independent review.
- Created/modified files list.
- Note: accepted files changed via delta mechanism; changes not committed (awaiting A3).

Keep it professional, GFM.

Files created:
- changes/sbp-subscriptions/{DELTA.md, IMPACT.md, DESIGN.md, NFR.md, ACCEPTANCE.md, A3-DECISION.md, EXECUTABLE-CHECKS.md}
- docs/adr/ADR-008-….md
- docs/adr/ADR-009-….md
- docs/spec/subscription-state-machine.md

Modified:
- ARCHITECTURE-SPINE.md (AD-009..011, contracts)
- .arch-handoff/CONSTRAINTS.yaml (7 new rules)
- README.md
- docs/solutioning.md
- docs/nfr.md? No — not modified. Good (delta says not rewritten).
- docs/contracts/tsp-api.md
- docs/contracts/opkc-adapter.md
- docs/rfp/vendor-rfp.md
- docs/spec/state-machine.md
- openapi/tsp-api.yaml

Also untracked .arch-handoff/mcp-calls.jsonl (runtime journal from MCP, not authored by me) — I'll mention it's a byproduct.

Note: use `skill`? Not needed further.

Let me write the final answer. Also mention that I did not commit, per instructions (only commit when asked). The user didn't ask to commit.

Let me produce the final summary.
Готово. Пакет изменения «СБП-подписки» подготовлен поверх принятого решения, вынесен на A3 и проверен гейтами. Код не писал.

## Что получилось (по пунктам задачи)

1. **Значимость и маршрут** — `changes/sbp-subscriptions/IMPACT.md`: `significance_score` → **Critical, 8/15** (с проектным `new_component` — 9/15); механический diff-пол даёт 1 → Fast, объединение — Critical. Подтверждённые триггеры: `security_boundary_change`, `financial_impact`, `consistency_model_change`, `data/api_contract_change`, `cross_domain_integration`, `significant_nfr`, `criticality_or_exception`.
2. **Влияние на архитектуру** — там же: что не меняется (AD-001/002/004/005/008, финансовое ядро, trust-зоны) и что меняется (новый домен мандата/подписки, движок списаний, класс данных «согласие/ПДн», обязательство вендора). Новые инварианты: **AD-009** (согласие обязательно), **AD-010** (идемпотентность списания по `periodKey`), **AD-011** (отзыв останавливает будущие списания) — `Proposed`.
3. **Архитектурное решение** — **ADR-008** (модель мандата/подписки) и **ADR-009** (исполнение списаний), с альтернативами, отрицательными последствиями и оценкой обратимости (`costly`/`reversible`).
4. **Контракты** — `openapi/tsp-api.yaml` v0.1→**0.2** (аддитивно) + `docs/contracts/tsp-api.md` и `docs/contracts/opkc-adapter.md` (подписочные операции/события, `termsHash`). `contract_diff`: **0 breaking**, 9 не-breaking.
5. **NFR** — `changes/sbp-subscriptions/NFR.md`: измеримые цели (окно списаний ≥6 ч, лаг p95 ≤60 с, дубли=0, отзыв ≤5 с, catch-up ≤2 периода, авторизация/ПДн/аудит).
6. **Приёмка и откат** — `ACCEPTANCE.md`: AC-1…AC-18 в EARS, негативные сценарии, пошаговый rollback с сигналами и владельцем, readiness = CONCERNS.
7. **Что решает человек** — `A3-DECISION.md`: 9 решений A3 + машиночитаемый пакет `{choice, rationale, constraints, rejected_options, expiry}`; готовность к handoff.

## Гейты (после правок — всё зелёное)

`fitness_check` PASS (14 правил, 0 нарушений, ослаблений нет) · `spine_lint` PASS · `delta_guard` PASS (изменённых 20, защищённый 1 — покрыт дельтой) · `delta validate` — нарушений нет · `openapi_lint` PASS · `contract_diff` 0 breaking.

**Граница зелёного (честно):** fitness здесь **структурный** — 14/14 правил проверяют текст, исполняемых проверок поведения 0 (паспорт вердикта приложен). Инварианты AD-009/010/011 получают исполняемые шаблоны на A4 — `EXECUTABLE-CHECKS.md`. Пакет готов к **A3**, не к реализации.

**Независимое ревью (ревьюер ≠ автор):** раунд 1 — NOT-READY, 11 находок (R1–R11) → адресованы; раунд 2 подтвердил закрытие R1, R3–R10 и поднял N1–N7 → тоже адресованы (включая вычисление `periodKey` шлюзом, charge как проекцию платежа, wording kill-switch, 403 на всех resource-scoped методах, запрет dunning после отзыва).

Принятые файлы менялись **принятым в репозитории способом** — через дельту `changes/sbp-subscriptions/DELTA.md` (`arch-be delta new`/`guard`), защищённый `ARCHITECTURE-SPINE.md` покрыт дельтой. Коммит не делал — жду решения/указания.

## Созданные файлы
- `changes/sbp-subscriptions/DELTA.md`, `IMPACT.md`, `DESIGN.md`, `NFR.md`, `ACCEPTANCE.md`, `A3-DECISION.md`, `EXECUTABLE-CHECKS.md`
- `docs/adr/ADR-008-model-podpiski-sbp-mandat-platelschika-kak-edinstvennyy-istochnik-soglasiya.md`
- `docs/adr/ADR-009-ispolnenie-periodicheskih-spisaniy-determinirovannyy-klyuch-edinstvennyy-pisatel-dunning.md`
- `docs/spec/subscription-state-machine.md`

## Изменённые файлы
- `ARCHITECTURE-SPINE.md` (AD-009…AD-011, секция контрактов)
- `.arch-handoff/CONSTRAINTS.yaml` (+7 правил дельты)
- `openapi/tsp-api.yaml` (v0.2), `docs/contracts/tsp-api.md`, `docs/contracts/opkc-adapter.md`
- `docs/spec/state-machine.md` (T13/T14, путь `origin=SUBSCRIPTION`)
- `docs/rfp/vendor-rfp.md` (gate G8, POC P9–P11), `docs/solutioning.md` (scope), `README.md` (указатель)

Служебный `.arch-handoff/mcp-calls.jsonl` — журнал вызовов MCP-сервера, мной не создавался (не часть пакета).
