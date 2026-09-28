<!-- источник: <HARNESS>/runs-v2-pilot/cells/wub9ahe/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-v2-pilot-cells-wub9ahe-ws/chats/d0baff6e-b1e2-4faf-904f-4ccca8cf3898.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/ARCHITECTURE-SPINE.md")`

I'll start by understanding the repository's conventions and the accepted decision before proposing anything.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/nfr.md")`

Let me read the docs and .arch-handoff to understand conventions.
Now let me read the core documents and the handoff package to understand the accepted decision and its conventions.

  `run_shell_command(command="ls -la docs/adr docs/contracts docs/spec docs/rfp openapi .arch-handoff .arch-handoff/adr 2>&1", description="List repository documentation structure")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/.arch-handoff/CONSTRAINTS.yaml")`

Now let me read the ADRs, contracts, state machine, handoff package.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/openapi/tsp-api.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/contracts/tsp-api.md")`

Let me read the ADR format (one full ADR), the tsp-api.yaml, tsp-api.md, state-machine.md, TASK.md, MANIFEST.json, ARCHITECTURE.md, RUBRIC.yaml, and MANIFEST.

Let me read ADR-007 (the strategy one, since it's A3 and Accepted in .arch-handoff? it says proposed-a3), ADR-002, and the tsp-api.yaml.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/adr/ADR-002-model-konsistentnos)`

Now let me read a full ADR to understand the ADR format, and the state machine, TASK.md, ARCHITECTURE.md, RUBRIC.yaml, MANIFEST.json, connect-manifest.json.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/.arch-handoff/TASK.md")`

Now let's look at the state machine, TASK.md, ARCHITECTURE.md (handoff), RUBRIC, MANIFEST. Let me also check the .qwen/settings.json and connect-manifest.json, and the skills installed in .qwen/skills.

  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wub9ahe/ws && git status --short && echo \"-, description="Inspect git state, skills, settings, connect manifest")`

Now let me check the skills installed in the project and settings.json, and see what Spine tools are available. Also check the git status / whether the openapi/tsp-api.yaml was recently added (it's modified since 13:21 today, whereas other files are сен 18). Let me check git status/diff.

Also I should read ARCHITECTURE.md (handoff) and RUBRIC.yaml.

Let me also check .qwen/settings.json and .qwen/skills.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/.qwen/settings.json")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/.arch-handoff/connect-manifest.json")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/.arch-handoff/RUBRIC.yaml")`

The output was truncated. Let me get settings.json and connect-manifest separately.

Also note: git status shows only .qwen/settings.json modified, and openapi/tsp-api.yaml is untracked? No — git status --short showed only " M .qwen/settings.json". But openapi/tsp-api.yaml exists with mtime today. If it were untracked it would show "??". Since it doesn't show, it must be tracked and unmodified... but wait, .gitignore maybe. Actually git status --short shows untracked files by default. Hmm, openapi/tsp-api.yaml not shown means it's tracked and unchanged, OR ignored. Let me check.

Actually the git snapshot at conversation start says "M .qwen/settings.json" only. And openapi/tsp-api.yaml modified сен 28 13:21 — that's before the session start (13:23). So it was probably committed or added in the baseline. Let me check git ls-files.

Let me get settings.json, connect-manifest, and check openapi tracking.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/.arch-handoff/ARCHITECTURE.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/.arch-handoff/MANIFEST.json")`

Now I understand the repository. Let me check the Spine tools available. The .arch-handoff/ARCHITECTURE.md is the handoff architecture. Let me read it, and MANIFEST.json.

Also, importantly, I should use the Spine MCP tools: significance_score, architect_review, change_impact, model_query, fitness_check, trace_check, spine_lint, delta_guard, rules_suggest, rubric tools. Also check the project's memory conventions: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — this means: accepted decision files should only be changed in the way accepted in this repo. The repo has a delta protocol (delta-spec skill, delta_guard) — changes to protected paths (model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml) must go through delta. So new change should be a delta: probably create an OpenSpec-style change or a delta directory.

Let me read ARCHITECTURE.md (handoff) and MANIFEST.json, and check for openspec directory, model directory.

Let me look at whether there is a delta protocol / openspec dir.

  `skill(skill="significance-routing")`
  `skill(skill="delta-spec")`

Now let me check the Spine MCP tools. First, let me understand the delta protocol. The task says: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The repo uses Spine with a delta protocol (delta_guard protects model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml). Also there's a skill `delta-spec` (OpenSpec delta). And `spine-content-bootstrap`, `fitness-functions` etc.

Let me check whether there's a model/ directory or openspec/ directory. From the folder structure at start: no model/, no openspec/. So the model is not present. The repo has ARCHITECTURE-SPINE.md, docs/, openapi/, .arch-handoff/.

Let me run the Spine tools to get grounded data:
1. significance_score — for the change
2. architect_review — full review
3. spine_lint — lint spine
4. trace_check
5. fitness_check
6. rules_suggest
7. rubric_list

Also let me check the skills for significance-routing, fitness-functions, delta-spec, adr-authoring, nfr-design, handoff-packaging, adversarial-review, semantic-review — these are the methodological skills I should apply.

Given the instruction "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению", I should load relevant skills. But loading all is expensive. Let me prioritize:
- significance-routing (required: significance assessment & route)
- fitness-functions (required: NFR/criteria, executable checks)
- delta-spec (required: change to accepted decision via delta — the repo's accepted way)
- adr-authoring (required: architectural decision with alternatives/consequences/reversibility)
- nfr-design (required: measurable NFR)
- handoff-packaging (required: передать исполнителям)
- adversarial-review / semantic-review (optional, for review)
- readiness-gate (optional)

Let me first query the Spine tools to ground the work. Let me start with architect_review (composite) — it gives route, control loop, model, contracts. And significance_from_diff, spine_lint, trace_check, fitness_check.

Let me check tool schemas first via tool_search for the ones I need.

Actually the MCP tools are described with names mcp__spine__*. I need to use tool_search to review schema then tool_call. Let me do that.

Let me batch: tool_search for several tools. But tool_search returns declarations; I can query multiple with select:. Let me select a set: mcp__spine__architect_review, mcp__spine__significance_score, mcp__spine__spine_lint, mcp__spine__trace_check, mcp__spine__fitness_check, mcp__spine__rules_suggest, mcp__spine__rubric_list, mcp__spine__kb_search, mcp__spine__skill_search.

Let me do tool_search with select for the key ones.
Now let me consult the installed methodological skills and the Spine control loop. First, I'll load the key skills that govern this task's shape.

  `tool_search(query="select:mcp__spine__architect_review,mcp__spine__significance_score,mcp__spine__spine_lint,mcp__spine__trace_check,mcp__spine__fitness_check)`

Key insight: Critical Path requires full Solutioning, delta alone insufficient. This change (recurring C2B debits / subscriptions СБП) is on payments + likely financial impact + security boundary change (mandate/consent handling) → Critical route. So full solutioning + ADR + NFR + human A3.

Now let me use Spine tools to ground: significance_score from diff, architect_review, spine_lint, trace_check, fitness_check, rules_suggest, change_impact.

Let me review tool schemas. I'll do tool_search select for several at once.
The change touches payments and consent handling — let me ground the route and impact with the Spine control loop rather than by eye.

  `tool_call(name="mcp__spine__significance_score", arguments={"triggers": {"new_component": true, "new_datastore": true, "new_vendor": false, "domain_ownership_change": true, "cross_domain_integration")`
  `tool_call(name="mcp__spine__architect_review", arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws"})`
  `tool_call(name="mcp__spine__spine_lint", arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/ARCHITECTURE-SPINE.md"})`

Let me call architect_review and significance_score and spine_lint and fitness_check. Actually architect_review is composite and includes most. Let me run it first with the repo path.

Let me run architect_review, spine_lint, fitness_check in parallel. Also significance_score needs triggers.

Let me define triggers for "рекуррентные C2B-списания по согласию плательщика (подписки СБП)":
- new_component: likely yes — new mandate/consent service? Possibly a new component "сервис согласий/подписок" + scheduler. I'd say true.
- new_datastore: yes — new storage of mandates/consents & schedule. true.
- new_vendor: probably no (reuse existing transport adapter / same NSPK). false.
- domain_ownership_change: maybe — subscriptions touch acquiring domain vs new subscription domain. Hmm. Possibly true (new domain "подписки/согласия").
- cross_domain_integration: yes — НСПК subscription protocol, ТСП, АБС. true.
- api_contract_change: yes — extend TSP API (mandate endpoints, subscription payments). true.
- data_contract_change: yes — new data (mandate id, consent). true.
- security_boundary_change: yes — consent for recurring debit, PII, mandate signing. Likely true → forces Critical.
- trust_zone_change: maybe false (same zones). Could be true if new consent store in different zone. I'll mark false to be conservative? Hmm. Let's be honest: consent storage may sit in payment loop (same trust zone), no new zone. false.
- consistency_model_change: yes — new scheduled execution, mandate lifecycle, idempotency per mandate, new saga for subscription debit. true.
- significant_nfr: yes — new NFRs (scheduler latency, retry windows). true.
- rto_rpo_targets: probably no new targets (same RPO=0). false.
- irreversible_migration: false (no migration).
- financial_impact: yes — recurring debits move money. true.
- criticality_or_exception: yes — КИИ/payments. true.

That's ~11 triggers → Critical. Let me feed to significance_score to get the machine verdict.

Let me call the tools.

  `skill(skill="adr-authoring")`
  `skill(skill="nfr-design")`

The significance_score gave Critical with score 11, matching the existing solutioning's 11/15. Good — but note my triggers may be questionable. The instruction says the tool validates. It fired 11. Note the baseline document said "значимость 11/15" too. Good consistency, though I chose some. Let me double-check the ones I set false: new_vendor (reuse existing ОПКЦ vendor — subscriptions may require a new capability in the same adapter, not a new vendor → false is fair), trust_zone_change (same zones; consent store inside payment loop → false), rto_rpo_targets (no new DR targets; reuse RPO=0 → false), irreversible_migration (false). That's defensible.

Actually wait — should `new_component` be true? Recurring payments need a scheduler/mandate service. Yes, new component (subscription/mandate orchestrator + scheduler). Good.

Hmm, but should I be careful: the baseline solutioning says 11/15 for the *initial* solution. My score also 11. That's fine, but it may look like I just copied. Let me be honest and note the specific triggers. Actually the initial solution's 11 included new_vendor (choosing vendor transport) — mine doesn't, but mine adds domain_ownership_change. Let me not over-engineer; I'll report the machine verdict and my trigger rationale.

Now let me check the toolbox for the delta protocol. The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." There's `delta_guard` protecting model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. And OpenSpec-style delta. Since there's no model/ dir and no openspec/ dir, the accepted way in this repo is: spine blocks are Proposed and act after ADR ratification; docs/adr/*.md for ADRs; ARCHITECTURE-SPINE.md AD-* blocks. The delta_guard defaults protect model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml.

So modifying ARCHITECTURE-SPINE.md directly would be blocked by delta_guard unless through delta. Let me check the delta_guard tool to understand.

Let me also check `rules_suggest` for candidates, `kb_search` for subscription СБП knowledge, `skill_search`/`skill_load` for relevant skills (nfr-design, adr-authoring, fitness-functions, handoff-packaging, adversarial-review).

Let me read the delta-spec skill's reference on how this repo does deltas. Also read the `spine-content-bootstrap`, `fitness-functions` skills. Actually let me load adr-authoring, nfr-design, fitness-functions, handoff-packaging, adversarial-review? That's a lot. Let me be judicious: load adr-authoring, nfr-design, fitness-functions, handoff-packaging.

Actually, per the instruction to use the methodology skills, and these directly shape the deliverables (ADR fields, NFR budgets, executable checks, handoff), I'll load them. Let me load 4 skills in parallel (skill tool one at a time? I can call multiple in one message).

Let me also call delta_guard schema and rules_suggest.

Let me batch: skill adr-authoring, skill nfr-design, skill fitness-functions, skill handoff-packaging.

Wait — the task deliverables: significance, impact on architecture, decision with alternatives, contract changes, NFR, acceptance criteria + rollback plan, what's left for human architect. Handoff to executors. So handoff-packaging matters. And adversarial-review maybe for the review lens. Let me load adr-authoring, nfr-design, fitness-functions, handoff-packaging first.
Machine verdict: **Critical, score 11** — consistent with the baseline route. Now let me load the remaining methodology skills that shape the deliverables.

  `skill(skill="fitness-functions")`
  `skill(skill="handoff-packaging")`

Now let me load fitness-functions and handoff-packaging. Also I should check delta_guard schema and rules_suggest. Let me batch those.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/adr/ADR-005-integraciya-s-abs-z)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/adr/ADR-004-at-least-once-dlq.m)`

Now let me check delta_guard schema and rules_suggest, kb_search, skill_search for relevant knowledge about СБП subscriptions. Also I should look at whether there's a delta protocol folder / how "принятые файлы решения" should be changed. Let me look at the delta_guard tool and possibly the delta-spec's references. Also check if there's a `delta` CLI.

Let me also query kb_search for "подписка СБП" / "рекуррент" and rules_suggest. And check `rubric_list` to see available rubrics.

Let me first check the remaining ADRs briefly to know what invariants exist and avoid contradictions: ADR-003, ADR-004, ADR-005, ADR-006. I've read 001 (in handoff), 002, 007. Let me read 003, 004, 005, 006 — needed to assess impact. And opkc-adapter.md, vendor-rfp.md.

Let me read them in parallel (4 files).
Let me read the remaining ADRs and the adapter contract to assess impact precisely.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/adr/ADR-006-trust.md")`

Let me read ADR-003 and ADR-006, and the opkc-adapter.md contract quickly. Also let me check the delta_guard tool schema and rules_suggest. And kb_search.

Actually, let me be efficient. I have enough on ADR-003/006 from spine and descriptions. But for impact analysis I want to know: adapter contract (opkc-adapter.md) — what interface the core depends on; that's key for adding subscription operations. Let me read opkc-adapter.md. And ADR-003 (transport/adapters) briefly.

Let me batch: read opkc-adapter.md, ADR-003, ADR-006.

Then query the tools.

Actually I'll delegate broad exploration to a subagent? No — I've got it mostly. Let me just read the 3 files.

  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wub9ahe/ws && which arch-be && arch-be --hel, description="Inspect arch-be CLI top-level commands")`
  `tool_search(query="select:mcp__spine__delta_guard,mcp__spine__rules_suggest,mcp__spine__rubric_list,mcp__spine__kb_search")`

Now let me check the delta protocol — how this repo expects engine changes to be made. There's `delta_guard` and skills mention `arch-be delta new <name>`. Let me check the delta_guard tool schema and the CLI availability (`arch-be delta ...`). Also check `rules_suggest`, `kb_search`, `rubric_list`.

Let me do tool_search select for delta_guard and rules_suggest, and also check if `arch-be` CLI is available with help.

Actually, the task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The repo's accepted way: spine blocks are Proposed until ADR ratified; changes go as new ADRs + spine deltas. delta_guard protects model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. Since there's no model/ dir, the protected set is ARCHITECTURE-SPINE.md and CONSTRAINTS.yaml. So if I need to change the spine (add new invariant AD-009 or modify), it must be via a delta (openspec-style change) rather than direct edit — otherwise delta_guard flags it.

Let me check `arch-be delta --help` / the CLI. Let me run `arch-be --help` and `arch-be delta --help`.

Actually, I should not over-rely on CLI; the MCP delta_guard tool is read-only check. Let me inspect the CLI to understand the accepted delta mechanism.

Let me run shell: `arch-be --help`, `arch-be delta --help`, `arch-be rules template list` maybe.

Let me do it.
Let me check the repository's accepted mechanism for changing protected decision files (delta protocol) and gather rule suggestions.

  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wub9ahe/ws && echo \"=== control --help ===\, description="Inspect control/rules CLI and delta layout")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws"}, name="mcp__spine__delta_guard")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws"}, name="mcp__spine__rules_suggest")`
  `tool_call(arguments={"query": "подписки рекуррентные списания согласие плательщика СБП mandate", "limit": 10}, name="mcp__spine__kb_search")`

Let me run delta_guard to check current state, rules_suggest, kb_search for "подписки рекуррентные СБП согласие", rubric_list. Also check `arch-be delta --help` (is there a delta command? Not in the top-level list. Hmm — top-level commands don't include `delta`. So the delta protocol is file-based: `changes/<name>/DELTA.md`). Let me check if `arch-be control` has delta subcommand, and whether there's a changes/ dir.

The top-level `gate` mentions "гейт прямых правок спайна (delta guard)". And delta_guard expects `changes/<name>/DELTA.md`. So the accepted mechanism = create `changes/<name>/DELTA.md` listing the protected files changed.

Let me verify there's no `delta` CLI and check the openspec/delta skill references. Let me look at the delta-spec skill directory for references.

Let me run:
- ls of skill dirs for delta-spec, fitness-functions (references)
- `arch-be control --help`
- `arch-be rules --help`

And MCP calls: delta_guard, rules_suggest, kb_search, rubric_list.

Let me batch these.

  `tool_search(query="select:mcp__spine__openapi_lint,mcp__spine__contract_diff,mcp__spine__nfr_check,mcp__spine__rubric_list,mcp__spine__skill_search")`
  `skill(skill="fitness-function-catalog")`

No `delta` CLI subcommand — the delta protocol is directory-based: `changes/<name>/DELTA.md`. delta_guard default protect = model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. But no model/ exists. So protected = ARCHITECTURE-SPINE.md + CONSTRAINTS.yaml.

So the accepted way to change the spine/CONSTRAINTS is to create a delta under `changes/<name>/DELTA.md` that mentions those files.

Now let me check the skill_search for relevant methodology, and rubric_list. Also let me check the delta-spec skill's references dir and fitness-function-catalog which mentions delta protocol. Let me use skill_load or read the skill files directly.

Actually, I should check `.qwen/skills/delta-spec` for references, and `fitness-function-catalog` skill (which describes the delta card template and CONSTRAINTS waves). Let me read those two skills via skill tool or read_file.

Also load `adversarial-review` and `semantic-review`? Maybe later for the review step.

Let me now think about the actual architecture work — the core of the deliverable. Let me plan the output artifacts.

## Understanding the change: СБП subscriptions (рекуррентные C2B-списания по согласию плательщика)

Business: ТСП (online cinemas, ЖКХ, telecom) want recurring C2B debits with payer consent — "подписки СБП". Currently each payment requires QR + client action.

What SBП actually offers: НСПК has "СБП Подписки" / "рекуррентные платежи" / "автоплатежи" — a mechanism where the payer's bank obtains consent once, and then the merchant can initiate debits (with notification to payer, possibility to revoke). In СБП this is realized via "Платные подписки" / "рекуррентный платёж" (the mechanism is described in НСПК rules; details [ТРЕБУЕТ ПРОВЕРКИ]). There's also "СБП: автоплатёж" with mandate (согласие) stored.

Key architectural differences from one-shot QR:
1. **Mandate/consent lifecycle** — new entity: согласие плательщика (mandate): created (with payer confirmation through their bank / QR from payer app), active, suspended, revoked, expired. Binding: payer account/masked PAN? and merchant, limits.
2. **Recurring debit initiation without payer action** — a scheduled/orchestrated debit at due time: merchant calls debit by mandateId; NSPK routes to payer's bank; requires notification to payer before each debit (по правилам НСПК); the payer may reject.
3. **Scheduler** — but a key architectural decision: who owns the schedule? Two options: (a) ТСП owns schedule and calls "debit by mandate" on due date (stateless шлюз, external trigger); (b) шлюз owns schedule (subscription service with cron/planner) and initiates debits autonomously. This is THE key architectural fork → ADR with alternatives. I'd recommend (a) — ТСП owns schedule, шлюз is executor — because: it keeps шлюз stateless wrt business calendar, avoids a scheduler as a new SPOF, avoids storing tenant billing rules, and matches the existing pull model (ТСП already calls API). But the business asked "ТСП просят рекуррентные списания по согласию" — they want to be able to debit. Hmm. The mandate itself is the NSPK-governed part. The billing calendar is the ТСП's business. So (a) is the right default. But maybe they want the gateway to also schedule. I'll present both and recommend (a) with a note that a "planned debits" service is deliberately deferred.

Actually wait — СБП subscriptions model in НСПК: The mechanism "СБП-подписка" (also called "Автоплатёж СБП" or "Рекуррентные платежи") — the merchant (ТСП) initiates each recurring payment via НСПК using a "mandate ID"/"subscription ID"; НСПК asks payer's bank; payer bank may auto-confirm within limits or require confirmation. There's a pre-debit notification requirement. So the шлюз acts as the channel: it receives "debit by subscription" requests from ТСП and translates to the adapter. So option (a) aligns with real protocol.

4. **Idempotency key for recurring debits** — each debit is a payment attempt with its own idempotency; also need business key (mandateId + billing period + amount) to prevent double-debit for the same period. This is an important new invariant: "не более одного списания за период по согласию" — a dedupe key distinct from Idempotency-Key. Actually the ТСП may retry with the same period; NSPK/шлюз must not double-charge. So mandate-scoped idempotency.

5. **Pre-notification and payer right to reject** — НСПК rules require the payer be notified (обычно за N дней/часов) and can cancel; the шлюз must support mandate revocation → stop future debits; already-charged needs refund/saga.

6. **New states for mandate** and new states for recurring payment: the payment state machine can reuse CREATED→PAID→CREDITED→COMPLETED etc., but the trigger is "mandate debit" instead of QR. Need to add payment type/subtype. Potentially a new terminal state? Payer rejection maps to FAILED with a specific reason. Mandate revocation mid-flight.

7. **Consent storage + PII** — mandate contains payer identifier (phone/account masked), consent text/version, timestamp, evidence of consent (signature/QR confirmation). PII + consent proof → 152-ФЗ, audit. Security boundary change: storing consent artifacts and using them to move money without active payer action raises the bar.

8. **Contract changes**: 
   - New endpoints: mandate registration/creation, mandate status, mandate revocation; recurring debit initiation; maybe list mandates.
   - Existing endpoints unchanged → backward compatible. `PaymentRequest` gets optional fields (paymentType: one_time|recurring, mandateId). `Payment` gets optional mandateId, and status enum may get new values (e.g., PENDING_CONSENT, REJECTED_BY_PAYER) — adding enum values is a breaking change for strict clients! Important: adding new values to an existing enum in a response is technically breaking for clients that switch exhaustively. Need to handle: either new enum values only for new types, or version bump. The skill says path /v2 for breaking changes. Adding optional response fields is compatible per §6 of tsp-api.md; adding enum values is NOT explicitly covered. This is exactly a point for the human architect / contract gate. I'll flag it and propose: introduce new statuses but document as additive with client guidance, OR keep payment.status enum stable and put recurring-specific states in a separate field. Safer: keep `status` enum stable; add `paymentType` + `mandateId` + `recurringStatus` optional. Hmm, but a recurring payment still goes through CREATED→...→COMPLETED, so the same enum works. The rejection case: payer rejects debit → FAILED with errorCode = PAYER_REJECTED. So no new enum values required! Good — that keeps compatibility. Mandate has its own status enum in its own resource (new endpoint), so no impact on Payment enum.

   Also idempotency: existing `Idempotency-Key` covers POST. New POST endpoints follow same rule.

9. **Fitness/invariants affected**:
   - AD-001 (isolation) — new component (mandate store/service) inside payment loop; must not leak. Reinforced.
   - AD-002 (single source of truth) — extend state machine to mandate lifecycle; still atomic transitions.
   - AD-003 (idempotency) — extended: mandate-scoped dedupe key; repeated debit initiation for same period doesn't double-charge.
   - AD-004 (single adapter ОПКЦ) — new operations in adapter contract (create mandate, debit by mandate, revoke) — adapter stays single; but the adapter contract changes (new methods) and vendor RFP must cover recurring capability. This is the big external dependency (NSPK subscription protocol [ТРЕБУЕТ ПРОВЕРКИ]) and vendor must support it.
   - AD-005 (credit only from PAID) — **unchanged and critical**: recurring debit also credits only from confirmed PAID. Reinforced.
   - AD-006 (trust zones) — consent/PII handling; no new zone but stronger requirements; unlikely change to spine block.
   - AD-007 (НПС/КИИ/ПДн) — consent as legal basis, immutable consent log; extended.
   - AD-008 (strategy hybrid) — vendor transport must support recurring operations; still hybrid. Reinforced but adds a constraint on vendor selection.

   New invariant candidate: **AD-009 «Списание по согласию — только при действующем согласии и в пределах его условий»** (mandate-based debit only when mandate ACTIVE, within amount/period limits, with pre-notification; one debit per period key). This is the parallel of AD-005 for recurring. Should be added by delta.

   Also potentially: consent revocation takes effect immediately for future debits (no new debit after revocation), and a revoked mandate cannot be reactivated silently.

10. **NFR**: 
   - Mandate creation latency p95 < X
   - Recurring debit initiation p95 < 500ms (core)
   - Debit execution from due to PAID — depends on payer bank; notification lag.
   - Pre-notification lead time ≥ N hours (regulatory) — must be enforced.
   - Availability same 99.95%.
   - Throughput: recurring debits add load, especially mass billing windows (salary day, month start) → burst. Scheduler-free design pushes bursts to ТСП callers; need rate limiting per ТСП and bulk API. This matters: subscriptions create synchronized bursts (all subs billed on the 1st). → NFR for burst + admission control.
   - Zero double debits per period.
   - Mandate revocation processed ≤ X seconds (stop future debits).
   - Consent audit 100%.
   - RPO=0 for mandates.

11. **Acceptance criteria**: EARS-form, negative scenarios (repeat debit with same period key → one effect; revocation race with in-flight debit; payer rejects; mandate expired; adapter unavailable; late notification).

12. **Rollback plan**: feature flag per ТСП; stop-new-mandates; revoke in-flight; keep existing one-shot; no data migration back.

13. **What stays for the human architect (A3)**: 
   - The key fork: who owns the billing schedule (ТСП-driven debit vs шлюз scheduler). This is a business/architecture decision with product implications → A3.
   - Whether to expose mandate management to ТСП at all vs keep it in payer app / bank only.
   - Commercial: fees, limits per ТСП.
   - Whether to start implementation before NSPK subscription protocol docs and vendor capability confirmed (external input) — ADR-007 constraint (4) applies.
   - Category КИИ / consent legal basis wording — ИБ/юрист.
   - Enum compatibility policy decision (if new statuses needed).

Since this is Critical, full solutioning is required. The deliverable is an "архитектурный пакет изменения" that can go to A3 then handoff.

## What files to create

Following repo conventions:
- `docs/adr/ADR-008-<name>.md` — new ADR for the subscription/recurring decision (with alternatives, consequences, reversibility). Wait — ADR numbering: existing 001..007. The spine references AD-001..AD-008 (spine blocks), separate numbering. So new ADR = ADR-008.
  Actually, should I create one ADR or several? The change is substantial. Per adr-authoring: one decision per ADR, >1 page → split. Key decisions:
  - ADR-008: Модель подписок СБП — рекуррентные списания по согласию: где живёт расписание/инициация (ТСП-driven vs scheduler), and the mandate model. This is the main fork.
  - Possibly ADR-009: расширение контракта адаптера ОПКЦ и стратегия совместимости API ТСП.
  - The change package may include multiple ADRs. But keeping it focused: I'll write ADR-008 (mandate model + who initiates) and ADR-009 (API/contract extension & compatibility) — maybe. Hmm, the task asks for "Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью" (singular). I'll write a primary ADR-008 covering the mandate/recurring model with alternatives, and mention contract extension within it, OR write two ADRs. Given the repo has 7 ADRs for the base solution, adding 2 for a substantial feature is proportionate. But I also must be careful about scope creep and time.

Let me decide: 
- **ADR-008**: «Рекуррентные C2B-списания по согласию плательщика: модель согласия и инициация списаний» — the core decision (mandate lifecycle in шлюз; ТСП initiates each debit; шлюз does not own billing calendar; pre-notification; mandate-scoped idempotency). Alternatives: scheduler-in-gateway, full NSPK-managed auto-debit without mandate store, "subscription as pseudo-card", etc.
- **ADR-009**: «Расширение контрактов (API ТСП и адаптер ОПКЦ): обратно совместимое добавление операций согласий» — contract versioning and compatibility. 
- **Spine delta**: new block AD-009 (mandate invariant) added via delta; AD-004/AD-008 bindings extended.
- **Delta package** `changes/sbp-subscriptions/DELTA.md` (accepted way to change protected ARCHITECTURE-SPINE.md and CONSTRAINTS.yaml): ADDED/MODIFIED/REMOVED.
- **Impact assessment** doc: `docs/changes/sbp-subscriptions-impact.md` or fold into a solutioning addendum. Hmm — repo has docs/solutioning.md. The accepted way: maybe add `docs/solutioning-sbp-subscriptions.md`? Or an addendum. Let me think about "Принятые файлы решения меняй только тем способом, который принят в этом репозитории": means don't rewrite ARCHITECTURE-SPINE.md / existing ADRs freely; use delta. New files (ADR-008, delta dir, impact doc) are fine.

Let me structure the deliverables to map 1:1 to the 7 requested outputs and place them in repo-conventional paths:

1. Significance & route → section in the impact/change package (and delta justification). Use machine verdict.
2. Impact on architecture (invariants affected, changed/unchanged) → `docs/changes/sbp-subscriptions/IMPACT.md` (or inside DELTA). Recommend: put impact in the delta package as `changes/sbp-subscriptions/IMPACT.md` plus DELTA.md.
3. ADR → `docs/adr/ADR-008-*.md`, `docs/adr/ADR-009-*.md`.
4. Contract changes → `openapi/tsp-api.yaml` (extend, backward compatible) + update `docs/contracts/tsp-api.md` (add §) + `docs/contracts/opkc-adapter.md` (new operations) — but changing existing accepted contract docs? The contract docs are Draft, not protected. The task explicitly asks to change `openapi/tsp-api.yaml`. So edit it, backward compatibly.
5. NFR → `docs/nfr-sbp-subscriptions.md` (new, additive) — don't rewrite docs/nfr.md? Task says accepted decision files change only in accepted way. nfr.md isn't protected (not in delta protect list). But it's an accepted artifact. Safer: add a new section/appendix doc and reference. Hmm, but "Принятые файлы решения меняй только тем способом, который принят" — protects model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml per delta_guard defaults. I'll create `docs/nfr-sbp-subscriptions.md` as an addendum to avoid rewriting accepted NFR, and note it.
6. Acceptance criteria + rollback plan → `changes/sbp-subscriptions/ACCEPTANCE.md` or inside DELTA/TASK.
7. Human architect decisions → section in change package (A3 package).

Plus handoff → `.arch-handoff/` update? The task says "затем передать исполнителям". The handoff package is `.arch-handoff/` (TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, MANIFEST.json, adr/). Updating it is the accepted way to hand off. But regenerating via `arch-be handoff` would need the harness build. The `.arch-handoff` is a generated artifact. I could create a supplementary handoff for the change: `.arch-handoff/` is the current walking-skeleton handoff. For the change, maybe create `changes/sbp-subscriptions/HANDOFF.md`? Hmm.

Actually, let me reconsider scope. The user asked for a single "архитектурный пакет этого изменения". Concretely 7 outputs. I should produce files that are coherent and repo-conventional without inventing an over-complex structure. Let me settle on:

```
changes/sbp-subscriptions/
  DELTA.md              # accepted-way delta for protected files: ADDED/MODIFIED (spine AD-009, CONSTRAINTS rules)
  IMPACT.md             # significance + route + impact on invariants (outputs 1,2)
  ACCEPTANCE.md         # acceptance criteria (EARS) + rollback plan (output 6)
  A3-DECISION-PACKAGE.md# human architect decisions + rationale (output 7) — machine-readable {choice, rationale, constraints, rejected_options, expiry}
  HANDOFF.md            # epic-context for executors (output handoff)
docs/adr/ADR-008-...md  # decision with alternatives/consequences/reversibility (output 3)
docs/adr/ADR-009-...md  # contract/versioning decision (output 3/4)
docs/nfr-sbp-subscriptions.md  # measurable NFR (output 5)
openapi/tsp-api.yaml    # extended contract (output 4)
docs/contracts/tsp-api.md  # prose contract addendum (output 4)
```

Hmm, that's a lot of files. But the task is large and explicitly asks for a package that goes to A3 and then to executors. I think this is appropriate. However, I want to avoid over-engineering / "40 changes in one package" antipattern. Let me consolidate:

Maybe consolidate IMPACT + A3 decision package into one `changes/sbp-subscriptions/CHANGE.md`? But clarity matters. Let me do:

- `changes/sbp-subscriptions/DELTA.md` — the delta (propose), including its own justification/significance. This is the primary artifact and the accepted mechanism.
- `changes/sbp-subscriptions/IMPACT.md` — impact on accepted architecture (invariants, contracts, components, what doesn't change).
- `changes/sbp-subscriptions/ACCEPTANCE.md` — EARS acceptance criteria + rollback.
- `changes/sbp-subscriptions/A3.md` — machine-readable human decision package.
- `changes/sbp-subscriptions/HANDOFF.md` — executor handoff (epic-context + result contract).
- `docs/adr/ADR-008-...md` — decision.
- `docs/adr/ADR-009-...md` — contract extension/versioning decision (maybe fold into ADR-008? The contract decision is distinct enough: compatibility policy. But to limit sprawl, I could make ADR-008 the single decision and cover contract in it. Hmm. The task says "Изменения контрактов ... без поломки существующих потребителей" — that's a design decision worth an ADR (versioning/compat). I'll write two ADRs: ADR-008 (mandate/recurring model), ADR-009 (backward-compatible contract extension). This mirrors the base repo's pattern of one decision per ADR.
- `docs/nfr-sbp-subscriptions.md` — NFR addendum.
- `openapi/tsp-api.yaml` — extended.
- `docs/contracts/tsp-api.md` — add sections for new endpoints.
- `docs/contracts/opkc-adapter.md` — add new adapter operations (recuring/mandate). Since adapter is vendor boundary — important. Add § for subscription operations.

Also update `docs/spec/state-machine.md`? Add mandate states + recurring transitions. That's an accepted spec doc (Draft). Adding a section is fine and needed. Hmm, but scope. The state machine must cover recurring payment (reuses payment SM) + mandate lifecycle (new). I'll add a section to state-machine.md for mandate lifecycle, or put it in a new `docs/spec/mandate-state-machine.md`. To avoid rewriting accepted spec, create `docs/spec/mandate-state-machine.md` (new) and reference it. Actually the delta could say MODIFIED state-machine.md to add recurring triggers. Let me keep it clean: new file `docs/spec/mandate-lifecycle.md`, and DELTA MODIFIED state-machine notes recurring payment reuses payment SM with new trigger T4r.

Hmm, I'm expanding. Let me be decisive and produce a focused but complete package. Given the 7 required outputs, I'll create:

**Core package** (change dir, following delta protocol):
1. `changes/sbp-subscriptions/DELTA.md` — significance/route + delta (ADDED/MODIFIED/REMOVED), justification. (outputs 1 partially, and the propose step)
2. `changes/sbp-subscriptions/IMPACT.md` — impact on accepted architecture / invariants (output 2)
3. `changes/sbp-subscriptions/ACCEPTANCE.md` — EARS acceptance criteria + rollback plan + fitness rules (outputs 6, and part of 5)
4. `changes/sbp-subscriptions/A3-PACKAGE.md` — human decision package machine-readable (output 7)

**Decisions**:
5. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md` (output 3)
6. `docs/adr/ADR-009-obratno-sovmestimoe-rasshirenie-kontraktov.md` (output 3/4)

**Specs**:
7. `docs/nfr-sbp-subscriptions.md` (output 5)
8. `docs/spec/mandate-lifecycle.md` (mandate state machine — supports outputs 2,4,6)
9. `openapi/tsp-api.yaml` (edited — output 4)
10. `docs/contracts/tsp-api.md` (edited — output 4)
11. `docs/contracts/opkc-adapter.md` (edited — output 4)
12. `changes/sbp-subscriptions/HANDOFF.md` (executor handoff)

That's 12 artifacts. Reasonable for a Critical package. But is it too many? The task explicitly wants a full architectural package. I'll go with it but keep each tight.

Hmm, wait. Let me reconsider: maybe the repo expects changes under `changes/<name>/` for delta. delta_guard looks for `changes/<name>/DELTA.md`. Good.

Also the spine change: add AD-009. Where does AD-009 text live? In ARCHITECTURE-SPINE.md (protected) — must be via delta. So DELTA.md must contain the ADDED block text for AD-009 and the MODIFIED notes for AD-004/AD-008. And I should NOT directly edit ARCHITECTURE-SPINE.md (that would be a delta violation if I then run gate). Actually the accepted way: the delta is proposed; the architect applies it via `arch-be delta`? There's no delta CLI. Hmm. Let me check `arch-be control` — no delta. The gate `arch-be gate` includes delta guard. And delta_guard checks that changed protected files are mentioned in `changes/<name>/DELTA.md`.

So the mechanism: if you change ARCHITECTURE-SPINE.md directly, delta_guard requires that `changes/<name>/DELTA.md` mentions that file. So the accepted way IS: create the delta file AND make the change. i.e., the delta documents the change; the mention covers it.

Given "Принятые файлы решения меняй только тем способом, который принят в этом репозитории", I think the right move is:
- Create `changes/sbp-subscriptions/DELTA.md` that lists ADDED/MODIFIED for ARCHITECTURE-SPINE.md and CONSTRAINTS.yaml.
- Then actually apply the spine addition (AD-009) and CONSTRAINTS rules, so that the mention in DELTA covers them (delta_guard passes because the file is mentioned in the delta).
- Then run fitness_check/gate to verify green.

But careful: is it accepted to hand-apply, or should the delta be left unapplied for the architect? In OpenSpec flow: propose → apply → archive. Since this is Critical and A3-not-yet-decided, the *spine change that ratifies new invariants* should arguably happen only after the ADR is Accepted. But the spine blocks are "Proposed (ADR-008)" style — Proposed status acts after ratification. So adding AD-009 as `Status: Proposed (ADR-008)` is consistent with the repo's convention: blocks in Proposed status act after the ADR is ratified. That means I CAN add AD-009 as Proposed now, and it becomes binding once ADR-008 is accepted. This matches AD-001..AD-007 being "Proposed".

So: apply the spine delta now (AD-009 Proposed) + CONSTRAINTS rules, covered by DELTA.md. Good — and it keeps the repo's invariant surface complete.

But wait — should I modify ARCHITECTURE-SPINE.md at all? The user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The accepted way = via delta. So yes, modify it, but ONLY with an accompanying active delta that mentions it. Good.

Also CONSTRAINTS.yaml (.arch-handoff/) — protected; add rules via delta mention. Rules candidate from rules_suggest: EARS acceptance criteria. And I should add executable rules for the new invariants (e.g., mandate debit idempotency). But CONSTRAINTS at decision stage has mostly file_exists/must_contain. I can add must_contain rules for the new invariant (AD-009) and for the delta/acceptance artifacts. Also perhaps a rule that openapi stays backward compatible — but that's `command_succeeds` (contract_diff) which is a diff tool, not a stable rule. I could add a rule "docs/nfr-sbp-subscriptions.md contains проценты" etc. Let me add a couple of meaningful rules:
- `mandate-debit-only-active`: must_contain in ARCHITECTURE-SPINE.md pattern 'действующ... согласи' (traces AD-009)
- `subscription-nfr-measurable`: must_contain in docs/nfr-sbp-subscriptions.md '99,95' or specific number
- `contract-backward-compatible`: file_exists? no. Maybe `openapi/tsp-api.yaml` must contain '/v1/mandates'. Traces the contract change.
- `ears_acceptance_criteria` (from rules_suggest, warn).

Hmm, but adding rules that reference files I create is fine. And rule_weakened check: adding rules is strengthening, fine. Also `evidence_verify`? Not needed.

Now, will `fitness_check` pass with new rules? I must ensure patterns match. Let me design carefully.

Also `delta_guard` — after I edit ARCHITECTURE-SPINE.md and CONSTRAINTS.yaml, it must see them mentioned in `changes/sbp-subscriptions/DELTA.md`. The delta_guard looks for the file path mentioned in DELTA.md text. I'll include the literal paths `ARCHITECTURE-SPINE.md` and `.arch-handoff/CONSTRAINTS.yaml` in DELTA.md. Good.

Then `architect_review` / `gate` should pass.

Let me also verify by running fitness_check and gate after edits.

## Now the technical design details

Let me think hard about the subscription/recurring model in СБП to make the architecture credible. I should mark protocol specifics [ТРЕБУЕТ ПРОВЕРКИ] as the repo does.

Real-world СБП recurring: НСПК launched "СБП-подписки"/"Рекуррентные платежи" — actually there is "СБП: Платные подписки" and "Автоплатежи". The mechanism generally:
- Payer gives consent (согласие) in their bank app; a `subscriptionId`/`mandateId` is created, tied to merchant (ТСП) and payer.
- On each billing, merchant (via its bank/эквайер, i.e., our шлюз → ОПКЦ) initiates a payment by subscription. НСПК routes to payer bank. Payer bank may auto-debit within the consent terms, and must notify payer (pre-notification) — rules may require notification N days before or option to cancel.
- Payer can revoke consent at any time in their bank; revocation propagates to merchant via НСПК.
- Limits: amount per debit / per period, max total, period.

So the шлюз needs:
- Consent/mandate store & lifecycle
- Initiation of debits by mandate
- Handling payer rejection & revocation events
- Pre-notification obligation (who notifies? In СБП, payer's bank notifies the payer; merchant must ensure notification if required by rules — [ТРЕБУЕТ ПРОВЕРКИ]). I'll model a "notify-before-debit lead time" as a rule that must be verified, and design the API to accept a planned debit date so the шлюз/adapter can enforce the lead time.

Key architectural fork (ADR-008): **who initiates the recurring debit?**
- A) ТСП-driven: ТСП calls `POST /v1/mandates/{id}/debits` (or `POST /v1/payments` with mandateId) on due date. Шлюз = stateless executor. Recommended.
- B) Gateway scheduler: шлюз stores billing plans and initiates automatically (new scheduler component, owns business calendar, mass-burst management, dunning). More powerful, more complexity, higher blast radius, duplicates ТСП's billing system.
- C) Payer-bank-pull (НСПК-side auto): mandate stored only in НСПК/payer bank; шлюз doesn't store mandates, just relays. Least control, but maybe closest to protocol? Actually NSPK still notifies merchant, so merchant needs the mandate ID and status. Storing mandate state locally is needed for idempotency/audit.

Recommend A, with mandate state mirrored in шлюз.

Second decision within ADR-008: **mandate-scoped idempotency / dedupe** — business key (mandateId, billingPeriod) plus Idempotency-Key. Prevent double debit for the same period even under retries/different keys.

Third: **pre-debit notification & payer rejection handling**: model as payment FAILED with errorCode PAYER_REJECTED; mandate stays ACTIVE (rejection of one debit isn't revocation) unless revocation event.

Fourth: **revocation semantics**: on mandate.revoked (from НСПК or ТСП), all future debits forbidden immediately; in-flight debit → outcome UNKNOWN → query status, never blind-retry (eight-failure-modes!). This is a nice place to apply "eight failure modes" and "idempotent consumer" and "avoiding fallback".

Fifth: **avoiding fallback** — don't design "if mandate debit fails, fall back to QR". The skill avoiding-fallback warns against fallback. I could mention explicitly: no silent fallback from recurring debit to one-shot QR; failure is returned to ТСП (which may then send a QR flow itself). Good architectural nuance.

Contract changes (ADR-009 + openapi):
- New resource `/v1/mandates`:
  - `POST /v1/mandates` — register a mandate (create consent request). Request: tspId, payerRef (phone/identifier), maxAmountPerDebit?, periodLimit?, period (MONTH/etc.), purpose, notificationLeadHours?, redirectUrl/webhook. Response 201: {mandateId, status: PENDING_CONSENT, consentUrl or qrUrl}. The payer confirms in their bank.
  - `GET /v1/mandates/{mandateId}` — status: PENDING_CONSENT | ACTIVE | REJECTED | SUSPENDED | REVOKED | EXPIRED.
  - `POST /v1/mandates/{mandateId}/revoke` — ТСП-initiated revocation.
  - `GET /v1/mandates` — list (optional; maybe deferred).
  - `POST /v1/mandates/{mandateId}/debits` — initiate a recurring debit. Request: amount, billingPeriod (idempotency key part), paymentPurpose, plannedDebitDate?, Idempotency-Key header. Response 201: {paymentId, mandateId, status}.
  - Alternatively reuse `POST /v1/payments` with `mandateId` + `billingPeriod`. Which is better for backward compatibility & clarity? Two options:
    - Extend `POST /v1/payments` with optional `mandateId`, `billingPeriod`, `paymentType`. Pros: single payment resource, reuses status machine, GET /payments/{id} works. Cons: blurs semantics; risk.
    - Dedicated `POST /v1/mandates/{id}/debits` that creates a payment resource under the hood. Pros: clear intent, mandate-scoped dedupe natural, doesn't overload existing endpoint. Cons: new endpoint.
    I'll recommend dedicated endpoint that **returns a `paymentId`** (so payment retrieval/webhooks are unified), and mark it in ADR-009. This keeps existing `POST /v1/payments` contract untouched → backward compatible.

- `Payment` schema: add optional `mandateId`, `billingPeriod`, `paymentType`. Do NOT add enum values to `status` (payer rejection → FAILED). This preserves compatibility.
- Webhooks: add events `mandate.activated`, `mandate.revoked`, `mandate.rejected`, `payment.rejected_by_payer`? Better: reuse `payment.failed` with errorCode; add `mandate.*` events (new event types are additive for consumers that ignore unknown types — but a consumer might fail on unknown. Typically event consumers should ignore unknown; document as compatible). Note as a compatibility caveat.
- Errors: add codes: `MANDATE_NOT_ACTIVE` (409/422), `MANDATE_LIMIT_EXCEEDED` (422), `MANDATE_REVOKED` (410/409), `DUPLICATE_BILLING_PERIOD` (409) — reuse `IDEMPOTENCY_CONFLICT` semantics for same (mandate, period) with different body → 409.
- Idempotency section update: for debit endpoint, key = (mandateId, billingPeriod) additionally; store mapping 24h → but billing period dedupe must be long-lived (≥ period + buffer), not 24h. Important nuance: 24h idempotency window is insufficient for billing-period dedupe (retries may come days later). So mandate dedupe must be persisted for the mandate lifetime / at least the period. → New rule.

Adapter contract additions (opkc-adapter.md):
- `createMandate` (reference = mandateId), `getMandateStatus`, `revokeMandate`, `createRecurringDebit` (reference = paymentId, mandateRef, amount, plannedDate, billingPeriod), events `mandate.activated/rejected/revoked`, `payment.rejected_by_payer`. Vendor must support recurring operations → RFP extension [ТРЕБУЕТ ПРОВЕРКИ].

NFR addendum:
- Mandate creation p95 < 1s (core, excl NSPK).
- Debit initiation p95 < 500ms (core).
- Consent-to-active latency: ≤ N (по регламенту НСПК) [ТРЕБУЕТ ПРОВЕРКИ].
- Pre-debit notification lead: ≥ statutory hours, enforced; 100% of debits have notification event.
- Revocation propagation → stop future debits: ≤ 60s from receiving event; 0 debits after revocation (strong invariant).
- Double debit per (mandate, period): 0.
- Burst: subscriptions cause synchronized monthly peaks → sustained 200 TPS unchanged, burst 500/1000 must hold under "1st of month" pattern; add per-ТСП rate limit and bulk/idempotent batching recommendation.
- Availability 99.95% unchanged; RPO=0 for mandates & debit registrations.
- Audit: 100% consent lifecycle transitions in immutable log; consent artifacts retained per 152-ФЗ.

Acceptance criteria (EARS): ~10 criteria including negatives.

Rollback:
- Feature flag per ТСП; stop-new-mandates; existing mandates: continue or revoke per decision; one-shot path unaffected.
- Data: mandates are new, no migration back needed; if rolled back, mandates become inert; keep for audit.
- Signals: double-debit detected, revocation not honored, adapter recurring unavailable, mandate store errors → kill switch.
- Owner: architect + product owner; A3 approves.

What stays for human architect (A3):
- Choice A/B/C for initiation ownership (business/product).
- Whether шлюз exposes mandate management to ТСП or mandates are created only via payer app/bank.
- Commercial terms, per-ТСП limits.
- Go/no-go on starting implementation before NSPK subscription docs + vendor capability (AD-008 constraint).
- Enum/versioning policy if contract consumers are strict.
- КИИ/legal basis for consent.

Also the machine-readable A3 package {choice, rationale, constraints, rejected_options, expiry}.

Now, about "не сломать существующих потребителей": specifically
- Keep `/v1` paths, existing operations unchanged.
- New endpoints add to same document (additive).
- Optional fields only.
- No new enum values in existing `status` (rejection→FAILED+errorCode).
- New webhook event types: consumers must ignore unknown — document; consider opt-in subscription to mandate events to avoid breaking strict consumers. Possibly gate mandate events by ТСП flag.
- Validate with `openapi_lint` and `contract_diff` (diff old vs new must show no breaking changes CD-001..CD-010). I can actually run contract_diff between HEAD version and new version! Great verification. And openapi_lint.

Let me verify: contract_diff tool compares two versions of a contract. I can keep the original in git and diff. Let me plan to run `openapi_lint` on the new file, and `contract_diff` original vs new.

Let me check contract_diff schema.

Also let me check `openapi_lint` schema. And `nfr_check`, `evidence_verify`, `rubric_list`, `skill_search`.

Let me now also decide: do I need to modify the existing `docs/contracts/tsp-api.md` and `opkc-adapter.md`? The task says contracts changes in `openapi/tsp-api.yaml` without breaking consumers. I'll edit openapi/tsp-api.yaml (required) and add prose sections to docs/contracts/tsp-api.md and opkc-adapter.md (these are Draft, and the repo keeps prose contract alongside). This is consistent.

Hmm, editing many accepted docs could be considered scope creep. But the package needs the prose contract updated for executors. I'll do it as additive sections with a note "v0.2-draft (дельта подписок)".

Let me reduce: I'll edit `openapi/tsp-api.yaml` (required), and add sections to `docs/contracts/tsp-api.md` and `docs/contracts/opkc-adapter.md`. And create `docs/spec/mandate-lifecycle.md`. And new NFR addendum. OK.

Let me now check remaining tool schemas: openapi_lint, contract_diff, nfr_check, rubric_list, skill_search. Then I'll start writing.

Actually, let me also load the `fitness-function-catalog` skill? It has the delta card template (7 fields). And `spine-content-bootstrap`? Maybe not needed. Let me check the `fitness-function-catalog` skill since it describes the card template for distilling source into rule — useful for CONSTRAINTS additions. Let me load it, plus `adversarial-review` for the review step.

Hmm, context budget. Let me load `fitness-function-catalog` (relevant to CONSTRAINTS delta) and skip adversarial-review (I know how to self-review, and I have the checklist). Actually the task said "используй их по назначению" — I've used significance-routing, delta-spec, adr-authoring, nfr-design, fitness-functions, handoff-packaging. That's the core set. I'll optionally use adversarial-review as a final self-check. Let me at least run the review tools (architect_review, openapi_lint, contract_diff, fitness_check, spine_lint, trace_check) as verification.

Let me get the remaining schemas.
Let me review the remaining verification-tool schemas and the rule-library skill, then I'll have everything to design the package.

  `tool_call(arguments={}, name="mcp__spine__rubric_list")`
  `tool_call(arguments={"query": "согласие mandate рекуррентные подписки безопасность consent", "limit": 8}, name="mcp__spine__skill_search")`

Now I have a clear picture. Let me also do a quick skill_search for "подписки"/"согласие"/"mandate" to ensure no existing methodology, and rubric_list to know rubrics for judging (adr_quality, handoff_quality). Let me call those.

Also let me check the base ADR-001 and ADR-003 (I read ADR-001 via handoff, partially). I have enough.

Let me call rubric_list and skill_search quickly.

  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wub9ahe/ws && mkdir -p .qwen/tmp && cp opena, description="Save baseline copy of the contract")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/openapi/tsp-api.yaml"}, name="mcp__spine__openapi_lint")`

The rubrics dir is missing in this environment, so rubric judging via rubric_run won't work; but rubric_prompt/rubric_verify might use bundled? The error says missing assets/rubrics. So I'll skip rubric judging (or note it). I can still self-assess.

Now, I have enough to design. Let me write the plan. Given the size, let me consider whether to use plan mode. The user gave a clear, detailed request; they didn't ask for plan mode. I should just execute (interaction mode is default/agentic). But this is a large multi-file change; the instructions say "Plan before uncertain work" but also don't enter plan mode on my own. I can present a brief approach in text then execute. I'll just proceed.

Let me decide the exact file set and write it. I'll be careful with facts and mark [ТРЕБУЕТ ПРОВЕРКИ] for protocol specifics.

### Files to create/modify

**Create:**
1. `changes/sbp-subscriptions/DELTA.md` — propose: significance/route, ADDED/MODIFIED/REMOVED for protected files + scope, justification, evidence.
2. `changes/sbp-subscriptions/IMPACT.md` — impact on accepted architecture (invariants AD-001..AD-008, components, contracts, data), what changes / what doesn't.
3. `changes/sbp-subscriptions/ACCEPTANCE.md` — EARS acceptance criteria (positive+negative) + rollback plan + fitness rules mapping.
4. `changes/sbp-subscriptions/A3-PACKAGE.md` — human decision package (machine-readable JSON block).
5. `changes/sbp-subscriptions/HANDOFF.md` — executors handoff (epic-context + result contract + forbidden changes).
6. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`
7. `docs/adr/ADR-009-obratno-sovmestimoe-rasshirenie-kontraktov-podpisok.md`
8. `docs/nfr-sbp-subscriptions.md`
9. `docs/spec/mandate-lifecycle.md`

**Modify:**
10. `ARCHITECTURE-SPINE.md` — ADD AD-009 (Proposed (ADR-008)); MODIFIED note in AD-004/AD-008 (bindings), via delta.
11. `.arch-handoff/CONSTRAINTS.yaml` — add rules.
12. `openapi/tsp-api.yaml` — additive: new paths, schemas, optional fields, new error codes; version 0.2.0.
13. `docs/contracts/tsp-api.md` — add §8 subscription endpoints (additive).
14. `docs/contracts/opkc-adapter.md` — add §10 subscription operations for adapter/vendor.
15. `docs/spec/state-machine.md` — add recurring payment trigger + mandate states reference (MODIFIED).
16. `docs/solutioning.md` — maybe add a section? It's an accepted doc. Better not rewrite; the IMPACT.md covers it. I'll reference. Actually the README says solutioning is the full design. For the change, adding a pointer in solutioning could be good but risks rewriting accepted doc. I'll skip and keep change package self-contained. Hmm, but then solutioning is stale. The delta IMPACT notes it. Fine.
17. `.arch-handoff/TASK.md`? That's the walking-skeleton handoff for the base. The change handoff is separate at changes/.../HANDOFF.md. Actually the task says "передать исполнителям" — I'll produce HANDOFF.md and optionally update .arch-handoff/. I'll keep the base handoff untouched (it's for the base walking skeleton) and provide the change handoff in the delta dir. That respects "accepted files changed only in accepted way".

Wait, but `readme.md` says `.arch-handoff/` is the handoff package. Should the change handoff be regenerated there? The handoff generation requires `arch-be handoff` (harness build). I could run it, but it would overwrite. Safer: keep change handoff in changes dir as an addendum package. I'll mention in DELTA that when the delta is applied/accepted, handoff-regeneration folds HANDOFF.md into `.arch-handoff/`.

Hmm, that's 17 items — quite large. Let me trim to keep signal high and avoid the "delta-простыня" antipattern. The antipattern warns against 40 changes in one package. This change is genuinely one feature ("подписки СБП") but big. I'll keep ~14 files but make each focused. Actually creating one ADR instead of two reduces sprawl. Let me reconsider ADR-009: contract versioning decision could be a section in ADR-008? No — decisions differ in kind (one functional model, one compatibility policy). The repo's style is one decision per ADR. Two is fine and more auditable. Keep two.

Let me reconsider whether to modify `docs/spec/state-machine.md` vs creating mandate-lifecycle. I'll do both: mandate-lifecycle.md new (mandate SM), and state-machine.md MODIFIED (add recurring debit trigger T4r and note). Actually to minimize edits to accepted docs, I'll create mandate-lifecycle.md and add only a short "MODIFIED" note to state-machine.md pointing to it. That's the delta MODIFIED entry.

OK. Let me also decide about `docs/contracts/opkc-adapter.md`: add section "10. Операции подписок (рекуррентные списания)" with new sync ops and events, plus RFP requirement. Yes.

Now let me carefully design the spine addition AD-009.

**AD-009. Списание по согласию — только при действующем согласии**
- Status: Proposed (ADR-008)
- Binds: сервис согласий (mandate store), статусная машина, адаптер ОПКЦ, нотификатор ТСП, аудит-лог.
- Prevents: списание без действующего согласия плательщика; двойное списание за один период обязательства; списание сверх лимитов согласия; продолжение списаний после отзыва согласия; сокрытие отзыва.
- Rule: Рекуррентное списание инициируется ТОЛЬКО при статусе согласия `ACTIVE`, в пределах лимитов согласия (сумма/период), с выполнением требования предварительного уведомления; ключ дедупликации обязательства — (`mandateId`, `billingPeriod`), повтор не создаёт второе списание; после события отзыва согласия новые списания запрещены немедленно. Зачисление — по-прежнему только из `PAID` (AD-005). Fitness: тесты «повтор за период → одно списание», «отзыв → ноль новых списаний», «списание вне лимита отклонено».

That's a strong, testable invariant. Good.

MODIFIED:
- AD-004: Binds add "адаптер ОПКЦ — операции согласий"; Rule extend? Careful: don't change the Rule semantics. I'll add a note under AD-004: recurring operations go through the single adapter. Actually AD-004 is about "single adapter" — Binds already ties transport. I can add to Binds: "операции подписок (согласия, рекуррентные списания)". And note in the DELTA. Keep Rule unchanged.
- AD-008: Binds add "вендорский адаптер обязан поддержать операции подписок"; add constraint that implementation of recurring transport starts after NSPK subscription docs + vendor confirmation.

Be careful: AD-008 is `[ADOPTED]` (ratified reality). Modifying an adopted block needs care. I'll add a derived constraint, not change the Rule. In DELTA, mark as MODIFIED with justification.

Also update the "Deferred" section? The base spine says "Диспуты" deferred and solutioning roadmap says "автоплатежи" out of scope. Now автоплатежи/подписки come into scope. So DELTA REMOVED from Deferred: "автоплатежи" (it was in solutioning §1 roadmap, not in spine Deferred). The spine Deferred doesn't list автоплатежи. But solutioning §1 says "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." So the change is: автоплатежи move from roadmap to scope. I'll note as MODIFIED in DELTA (scope change), and in IMPACT.

Now CONSTRAINTS.yaml additions. Current rules: adr-set-complete, spine-present, nfr-measurable, abs-credit-only-from-paid, adr-no-placeholders, readme-exists, spine-lints-clean. I'll add (all additive):
- `adr-008-present`: file_exists docs/adr/ADR-008-...md — error (traces the new decision). Hmm, filenames are long. Let me pick a stable name: `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`.
- `mandate-debit-only-active`: must_contain glob ARCHITECTURE-SPINE.md pattern 'действующ' — hmm too loose. Better pattern: `статусе согласия` ... Let me use pattern `только при действующем согласии` in ARCHITECTURE-SPINE.md. I'll write AD-009 Rule containing exactly "Рекуррентное списание инициируется ТОЛЬКО при статусе согласия `ACTIVE`" — I'll set pattern accordingly. Let me use a distinctive literal: `при статусе согласия` — but for must_contain, regex. I'll use `только при статусе согласия` (regex-safe, backticks fine as literal in regex? backtick is literal). Let me include pattern `только при статусе согласия`.
- `mandate-period-idempotency`: must_contain in ARCHITECTURE-SPINE.md pattern 'mandateId.*billingPeriod|billingPeriod' — must_contain matches whole file (not multiline issue). Use pattern `billingPeriod` — traces dedupe key. Maybe better in ADR-008 + spine. I'll target docs/adr/ADR-008*.md with pattern 'billingPeriod'. And a separate rule for spine.
- `subscription-nfr-measurable`: must_contain glob docs/nfr-sbp-subscriptions.md pattern '99,95' (availability) — error.
- `contract-mandates-endpoint`: must_contain glob openapi/tsp-api.yaml pattern '/v1/mandates' — error (traces contract change).
- `contract-contract-diff-clean`: can't easily (command). Skip; verification done by tool.
- `ears_acceptance_criteria`: must_contain glob 'changes/**/*.md' pattern EARS — warn (from rules_suggest, adapted to change dir).
- `delta-present`: file_exists changes/sbp-subscriptions/DELTA.md — warn.
- `mandate-events-integrity`: maybe skip.

Also include `rationale`, `fix_hint`, `skill`, `owner`, `expiry` fields? The catalog card has 7 fields but CONSTRAINTS schema in this repo uses name/type/glob/pattern/severity. rules-report mentions owner/expiry/exclude_glob/effort_hours. Adding owner/expiry improves quality (rules-report flags missing owner/expiry). Let me add `owner` and `expiry` to new rules to be exemplary. Let me check schema support: rules-report reads owner, expiry. Likely fields `owner:` and `expiry:`. I'll add them; if unknown, fitness may ignore. Risk: unknown fields could cause parse error. Hmm. Let me test with fitness_check after. I could keep it minimal to be safe. The skill card mentions owner/expiry, and rules-report reads them, so they're supported. I'll add `owner` and `expiry` (date). Let me use `owner: solution-architect`, `expiry: 2027-03-31`. And `rationale`. Let me verify by running fitness_check after and adjusting.

Actually to reduce risk, I'll add owner/expiry/rationale only, and validate.

Now openapi/tsp-api.yaml extension. Let me write it carefully to be valid OpenAPI 3.0.3 and pass openapi_lint (versioning, idempotency on mutating endpoints, RFC 7807 errors). Current file has NO error responses defined (no 4xx/5xx), and lint may flag that. Let me check: openapi_lint checks "идемпотентность mutating-endpoint'ов, ошибки RFC 7807". The existing file likely already fails those checks? Let me run openapi_lint on the ORIGINAL first to know the baseline, so I don't get blamed for pre-existing issues. Good idea.

Let me run openapi_lint on openapi/tsp-api.yaml now, and contract_diff against a copy of the original.

Plan: 
1. Run openapi_lint on current file (baseline).
2. Save baseline copy of original to /tmp for contract_diff later.
3. Write new file.
4. Run openapi_lint (new) and contract_diff(old, new).

Let me do steps 1-2 now.

Also, let me check `contract_diff` requires old and new files. I'll copy original to `.qwen/tmp/` (intermediate, record_as_artifact=false not needed since cp) or /tmp. Use /tmp.

Let me run openapi_lint baseline and copy.

Actually, I realize I should also verify the existing `openapi/tsp-api.yaml` passes lint as-is. Let me do it.

Let me also think about what fields to add to Payment enum question. I'll keep status enum unchanged.

Let me now run baseline lint + copy.
Baseline check of the contract before I touch it — so pre-existing lint findings aren't attributed to this change.

  `write_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/adr/ADR-008-rekurrentnye-c2b-sp, content="# ADR-008. Рекуррентные C2B-списания по согласию плательщика: модель согласия и инициация списаний\n\n- Date: 2026-09-28\n- Status: Propose)`

Baseline contract passes lint. Good. Now the new file must also pass.

Now let me write everything. I'll start with the ADRs (they're the anchor), then spine delta + CONSTRAINTS, then spec/contracts, then change package docs.

Let me be efficient and write files. I'll write ADR-008 first.

Let me draft ADR-008 carefully following the repo's ADR format (header: Title, Date, Status, Owner, Related; Context; Decision; Alternatives Considered table; Consequences Positive/Negative; Reversibility; References). Use the accepted way: don't modify existing ADRs; create new ones with Supersedes/Related links.

ADR-008 title: "Рекуррентные C2B-списания по согласию плательщика: модель согласия и инициация списаний"

Date: 2026-09-28 (today). Status: Proposed. Owner: solution-architect (платёжный контур) + продукт. Related: ADR-002, ADR-004, ADR-005, ADR-007, AD-003, AD-009 (spine).

Context: business need: ТСП (онлайн-кинотеатры, ЖКХ, связь) просят подписки; сейчас каждый платёж требует QR и действия клиента. НСПК предоставляет механизм рекуррентных C2B-списаний по согласию плательщика (детали протокола — внешний вход [ТРЕБУЕТ ПРОВЕРКИ]). Forces: согласие — правовое основание списания (152-ФЗ/161-ФЗ); плательщик должен получать предварительное уведомление и иметь возможность отзыва; финансовые последствия двойного списания; at-least-once; не хочется тащить биллинговый календарь в шлюз.

Decision (one paragraph + numbered):
1. Согласие (mandate) — новый ресурс и конечный автомат в шлюзе (PENDING_CONSENT→ACTIVE→{SUSPENDED}→REVOKED/EXPIRED/REJECTED), единый источник истины; согласие создаётся по инициативе ТСП, подтверждается плательщиком в его банке; в шлюзе хранится минимальный набор + ссылка на подтверждение.
2. Инициация списаний — ТСП-driven: на дату обязательства ТСП вызывает шлюз; шлюз НЕ хранит биллинговый календарь и НЕ инициирует списания самостоятельно (нет нового планировщика как SPOF).
3. Каждое списание — платёж в существующей статусной машине (ADR-002), создаётся из состояния действующего согласия; зачисление — только из PAID (AD-005).
4. Дедупликация обязательства по (mandateId, billingPeriod) в дополнение к Idempotency-Key; окно хранения — не менее периода согласия (не 24 ч).
5. Предварительное уведомление плательщика и лимиты согласия (макс. сумма списания/период) — условие инициации; при нарушении списание отклоняется шлюзом до вызова ОПКЦ.
6. Отзыв согласия — немедленный запрет новых списаний; списание «в полёте» — исход UNKNOWN → дозапрос статуса, без слепого повтора; отзыв и его обработка — в неизменяемом аудит-логе.
7. Ядро не знает протокола НСПК: операции согласий — через расширение внутреннего контракта адаптера (ADR-009), вендор обязан их поддержать.

Alternatives Considered table:
- ТСП-driven инициация (выбран)
- Планировщик подписок в шлюзе (шлюз владеет календарём) — плюсы: не нужен внешний триггер, удобно малому ТСП; минусы: новый stateful-планировщик = SPOF, дублирует биллинг ТСП, синхронные «зарплатные» пики, ответственность за пропуск списания, рост blast radius, RPO для календаря. Отвергнут для MVP; может стать отдельным сервисом позже (deferred).
- Полностью на стороне НСПК/банка плательщика (шлюз не хранит согласие) — плюсы: минимум данных; минусы: нет локального источника истины для дедупликации/аудита/сверки, нельзя гарантировать «одно списание за период», нарушает AD-002 по духу. Отвергнут.
- Fallback на разовый QR при отказе рекуррентного списания — отвергнут (avoiding-fallback): скрытая деградация, непредсказуемость; ошибку обрабатывает ТСП (сам инициирует QR-поток).

Consequences Positive/Negative. Reversibility: reversible (feature-flagged, additive; no data migration; mandates inert on rollback). Expiry: revise when NSPK subscription protocol docs obtained / if vendor can't support; planned review 12 months.

References: [ТРЕБУЕТ ПРОВЕРКИ] NSPK docs; ADR-002/004/005/007; skills avoiding-fallback, idempotent-consumer, eight-failure-modes... (references to patterns, fine).

Now ADR-009 title: "Обратно совместимое расширение контрактов (API ТСП и адаптер ОПКЦ) для подписок"

Decision:
1. API ТСП остаётся `/v1`; существующие операции и схемы не меняются (no breaking). Additive: new paths `/v1/mandates...`; optional fields in `Payment` (`mandateId`, `billingPeriod`, `paymentType`).
2. Enum `Payment.status` НЕ расширяется: отказ плательщика = `FAILED` + `errorCode=PAYER_REJECTED`; жизненный цикл согласия вынесен в отдельный ресурс со своим enum.
3. Новые типы вебхуков (`mandate.*`, `payment.rejected_by_payer`?) — additive; потребители обязаны игнорировать неизвестные типы; включаются по флагу ТСП (opt-in), чтобы не ломать строгих потребителей. Actually payment.rejected → use payment.failed. New events: mandate.activated, mandate.rejected, mandate.revoked. opt-in per ТСП (подписка на новые события) — but webhook events are just delivered; a consumer that errors on unknown type would break. So opt-in flag is the safe compat mechanism.
4. Новые коды ошибок additive.
5. Adapter contract extended with new operations; vendor dependency; RFP change request.
6. Breaking changes only in `/v2` (unchanged policy).
7. Verification: contract_diff old→new shows 0 breaking (CD-001..CD-010), openapi_lint PASS — evidence for A4.

Alternatives:
- Добавить подписки в `POST /v1/payments` c полями (без новых endpoint) — плюсы: минимум новых сущностей; минусы: перегрузка семантики, неявная дедупликация, риск для существующих потребителей (обязательные/условные поля), сложнее лимиты согласия. Отвергнут в пользу отдельного ресурса `mandates` + отдельного endpoint списания, возвращающего `paymentId`.
- Расширить enum `Payment.status` новыми значениями — минусы: ломает строгих потребителей (exhaustive switch); отвергнут.
- Новая major-версия `/v2` для всех — минусы: лишний миграционный overhead, ломает всех; отвергнут (изменения аддитивны).

Good.

Now mandate-lifecycle.md spec:
States: PENDING_CONSENT → ACTIVE → REVOKED / EXPIRED / REJECTED; ACTIVE → SUSPENDED → ACTIVE (e.g., temporary block by payer/bank); SUSPENDED → REVOKED. Technical: none needed.
Transitions table with triggers, guards, actions, idempotency keys.
Invariants: single active consent per (payer, merchant, purpose)? maybe. Debit only from ACTIVE. Revocation immediate. Pre-notification required. Limits.
Debit → payment mapping: creating a payment from mandate; billingPeriod dedupe.
Reconciliation: mandates vs NSPK status; revocation events.

NFR addendum: table.

Acceptance (EARS): 
- When ТСП создаёт согласие, the шлюз shall вернуть mandateId со статусом PENDING_CONSENT ≤ 1 с (p95, без НСПК).
- When плательщик подтверждает согласие, the шлюз shall перевести согласие в ACTIVE и опубликовать mandate.activated ≤ 60 с от события НСПК.
- While согласие ACTIVE, when ТСП инициирует списание в пределах лимитов и с уведомлением, the шлюз shall зарегистрировать платёж и вернуть paymentId ≤ 500 мс (p95, без НСПК).
- If согласие не ACTIVE (REVOKED/EXPIRED/REJECTED/SUSPENDED), then the шлюз shall отклонить списание кодом MANDATE_NOT_ACTIVE без вызова ОПКЦ.
- If сумма списания превышает лимит согласия, then the шлюз shall отклонить списание кодом MANDATE_LIMIT_EXCEEDED.
- When ТСП повторяет списание с тем же (mandateId, billingPeriod), the шлюз shall вернуть ранее созданный платёж и не создавать второе списание (property).
- When приходит событие отзыва согласия, the шлюз shall немедленно запретить новые списания (0 списаний после отзыва) и зафиксировать отзыв в аудит-логе.
- If предварительное уведомление не выполнено (нарушен lead time), then the шлюз shall отклонить инициацию (код PRE_NOTIFICATION_REQUIRED). 
- When плательщик отклоняет конкретное списание, the шлюз shall перевести платёж в FAILED с errorCode PAYER_REJECTED, согласие остаётся ACTIVE.
- While согласие ACTIVE, if ОПКЦ недоступен, then списание не теряется (DLQ + сверка), двойное списание за период — 0.
- Existing one-shot: When ТСП создаёт разовый платёж без mandateId, the шлюз shall обработать его как прежде (регресс: NFR базового решения без изменений).

Rollback plan section.

Fitness rules mapping.

A3-PACKAGE.md: machine-readable JSON with {choice, rationale, constraints, rejected_options, expiry} for the primary fork + a list of human decisions with options and recommendation.

HANDOFF.md: epic-context 800-1500 tokens (dense, by meaning): goal, boundaries, invariants (verbatim Rules), interfaces, forbidden changes, acceptance, result contract JSON.

IMPACT.md: significance (11/Critical, 11 triggers list), route A0-A5 with what's needed, affected invariants table (AD-001..AD-008 + new AD-009; changed/unchanged), components changed/new, contracts, data, what's NOT changed.

DELTA.md: the propose artifact: scope, ADDED/MODIFIED/REMOVED for protected files, justification, evidence, status. Must mention `ARCHITECTURE-SPINE.md` and `.arch-handoff/CONSTRAINTS.yaml` literally.

Let me now write the files. I'll do writes in batches. Start with ADR-008 and ADR-009.

Note on comments: keep minimal. These are docs; content is the deliverable.

Let me write ADR-008.

I need to be careful: the repo uses Russian; write in Russian. Filenames transliterated.

Let me write.
I have the full picture. This is a Critical-route change, so it needs a full solutioning package. Let me write the two decision records first — they anchor everything else.

  `write_file(content="# ADR-009. Обратно совместимое расширение контрактов (API ТСП и адаптер ОПКЦ) для подписок\n\n- Date: 2026-09-28\n- Status: Proposed\n- Own, file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/adr/ADR-009-obratno-sovmestimoe)`

Now ADR-009.

  `write_file(content="# Жизненный цикл согласия плательщика (mandate) — спецификация\n\n- Status: Draft (для ревью на гейте A1 дельты «подписки СБП»)\n- Owner: s, file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/spec/mandate-lifecycle.md")`

Now the mandate lifecycle spec.
Now the mandate lifecycle spec that ADR-008 binds to.

  `write_file(content="# NFR (дополнение) — Подписки СБП: рекуррентные C2B-списания по согласию\n\n- Status: Draft (baseline; финал — на гейте A1 дельты «подписки, file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/nfr-sbp-subscriptions.md")`

Now the NFR addendum.
Now the measurable NFR addendum for the new functionality.

  `write_file(content="# DELTA — Подписки СБП: рекуррентные C2B-списания по согласию плательщика\n\n- Status: Proposed (ожидает A3 — человеческое решение по ADR-0, file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/changes/sbp-subscriptions/DELTA.md")`

Now the spine delta: modify ARCHITECTURE-SPINE.md (add AD-009, MODIFIED notes for AD-004/AD-008). And CONSTRAINTS.yaml. But first create the DELTA.md that mentions them (so delta_guard passes). Actually order doesn't matter for the final state; delta_guard checks the working tree diff vs HEAD. So I need DELTA.md present mentioning the files. Let me write DELTA.md first, then edit spine and CONSTRAINTS.

Let me write DELTA.md. It must contain literal mentions of `ARCHITECTURE-SPINE.md` and `.arch-handoff/CONSTRAINTS.yaml`. It should have ADDED/MODIFIED/REMOVED sections.

Also include significance and route, justification, evidence, status.

Let me write it.
Now the delta artifact (the repository's accepted way to change protected files), which also carries the significance assessment.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/ARCHITECTURE-SPINE.md", old_string="## AD-004. Единственный адаптер ОПКЦ СБП\n\n- Status: Proposed (ADR-003)\n- **Binds**: транспорт к НСПК (mTLS/ГОСТ, сертификаты УЦ НСПК, СК, new_string="## AD-004. Единственный адаптер ОПКЦ СБП\n\n- Status: Proposed (ADR-003; расширено дельтой подписок — ADR-008, ADR-009)\n- **Binds**: транс)`

Now apply the spine modifications: add AD-009 and MODIFIED notes to AD-004/AD-008 in ARCHITECTURE-SPINE.md, and REMOVED/scope note. Also update the "Контракты и версии" section to mention v0.2.

Let me edit ARCHITECTURE-SPINE.md.

First, AD-004 Binds add. Current:
```
## AD-004. Единственный адаптер ОПКЦ СБП

- Status: Proposed (ADR-003)
- **Binds**: транспорт к НСПК (mTLS/ГОСТ, сертификаты УЦ НСПК, СКЗИ), контракт `docs/contracts/nspk-contract.md`.
- **Prevents**: расползание протокола НСПК по кодовой базе; несертифицированную криптографию; несоответствие тестовым испытаниям НСПК.
- **Rule**: Протокол НСПК знает только адаптер ОПКЦ; внутренний контракт шлюза — единственный интерфейс для остальных компонентов.
```
Add to Binds: ", операции подписок (согласия, рекуррентные списания)". And Status: Proposed (ADR-003, ADR-008).

AD-008:
```
## AD-008. Стратегия реализации — гибрид [ADOPTED]

- Status: Adopted (A3 от 2026-08-15, ADR-007 Accepted)
- **Binds**: ADR-007, ядро шлюза, вендорский транспортный адаптер ОПКЦ.
- **Prevents**: связывание ядра шлюза с конкретным транспортным адаптером; начало реализации транспорта до контракта с вендором и получения документации НСПК.
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.
```
Add Binds: ", операции подписок (согласия, рекуррентные списания)". Add to Rule: "Вендор обязан поддержать операции согласий и рекуррентных списаний; реализация этих операций начинается только после подтверждения поддержки вендором и получения документации НСПК по подпискам." And Prevents add "начало реализации операций подписок без подтверждённой поддержки вендора".

Then add AD-009 block after AD-008, before "## Deferred".

Then update Deferred/scope: add note that подписки/автоплатежи now in scope via ADR-008. Actually Deferred list doesn't include автоплатежи. I'll add a line in "Deferred" ... no. Better: add a scope note. Hmm. Let me add to the "Deferred" section a clarification? The DELTA says REMOVED from Roadmap in solutioning. For spine, I'll leave Deferred as is (it doesn't mention автоплатежи). But the solutioning.md §1 Roadmap mentions автоплатежи — DELTA MODIFIED says solutioning §1 updated by reference. Should I edit solutioning.md? The DELTA says "переносятся ... (ссылкой на эту дельту)". To be honest, I should make that edit too, small. Let me add a line to solutioning.md §1. I'll do it.

Also update "Контракты и версии" in spine to mention v0.2.0? It says "Внутренний контракт шлюза (API ТСП): версия 0.1 draft". I'll update to note v0.2 (подписки) — but careful: modifying that text. It's part of the spine (protected) and covered by DELTA mention. Fine.

Let me make the edits.

Now, importantly: spine_lint checks "непиннутые версии" and links to non-existent AD. AD-009 references AD-005 etc. Fine.

Let me apply edits.
Now applying the spine delta — new invariant AD-009 plus the notes on AD-004/AD-008.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/ARCHITECTURE-SPINE.md", new_string="## AD-008. Стратегия реализации — гибрид [ADOPTED]\n\n- Status: Adopted (A3 от 2026-08-15, ADR-007 Accepted; расширено дельтой подписок — A, old_string="## AD-008. Стратегия реализации — гибрид [ADOPTED]\n\n- Status: Adopted (A3 от 2026-08-15, ADR-007 Accepted)\n- **Binds**: ADR-007, ядро шл)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/ARCHITECTURE-SPINE.md", offset=74)`

Now update the "Контракты и версии" section and the "Deferred" (add scheduler deferral). Let me view the tail of the spine to edit precisely.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/ARCHITECTURE-SPINE.md", new_string="- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.\n- **Планировщик под, old_string="- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.\n\n## Контракты и ве)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="  - name: spine-lints-clean\n    type: must_not_contain\n    glob: \"ARCHITECTURE-SPINE.md\"\n    pattern: 'TODO|TBD|XXX'\n    severity: wa, old_string="  - name: spine-lints-clean\n    type: must_not_contain\n    glob: \"ARCHITECTURE-SPINE.md\"\n    pattern: 'TODO|TBD|XXX'\n    severity: wa)`

Now add the CONSTRAINTS rules. Let me edit .arch-handoff/CONSTRAINTS.yaml. Add after the last rule (spine-lints-clean) the new rules. Add fields owner/expiry/rationale.

Note: filename with Cyrillic? No, ADR filenames transliterated. Good.

For `delta-acceptance-ears` glob `changes/**/*.md` — glob supports `**`. Good. Pattern for EARS: `(?m)^\s*[-*]?\s*\**\s*(When|While|If|Where)\b`. In YAML single quotes, backslashes are literal. Good.

Let me write the additions. Also need `mandate-revocation-stops-debits` pattern exact substring from spine: "после события отзыва согласия новые списания запрещены". must_contain matches against whole file; regex `.` etc. The pattern has no special chars except none. Fine. But note `must_contain` regex: the text contains no regex metachars. OK.

`mandate-debit-only-active`: pattern `только при статусе согласия` — present in AD-009 Rule. Good.

`mandate-period-idempotency`: glob `docs/adr/ADR-008*.md` pattern `billingPeriod`. Good.

`subscription-nfr-measurable`: glob `docs/nfr-sbp-subscriptions.md` pattern `99,95`. The NFR doc contains "99,95" in the intro line: "доступность ≥ 99,95 %". Good.

`mandates-endpoint-present`: glob `openapi/tsp-api.yaml` pattern `/v1/mandates`. Good.

`adr-008-present`: file_exists path docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md. Good.
`adr-009-present`: path docs/adr/ADR-009-obratno-sovmestimoe-rasshirenie-kontraktov-podpisok.md. Good.

`delta-present`: file_exists changes/sbp-subscriptions/DELTA.md.

Let me add owner/expiry. Use `owner: solution-architect (платёжный контур)` and `expiry: 2027-03-31`. Hmm quoting. I'll add `owner: solution-architect` simple, `expiry: 2027-03-31`.

Let me do the edit.
Now adding the fitness rules that trace the new invariants.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\n  description: >\n    Мерчант-API СБП-шлюза. v0.2.0 — аддитивное расш, file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/openapi/tsp-api.yaml")`

Now the openapi contract. I need to write the extended openapi/tsp-api.yaml (v0.2.0) additively and ensure it passes openapi_lint.

Current file content:
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

Interesting: the openapi file is a minimal subset (doesn't include /v1/tsp, refunds, error schemas) — it's a distilled machine-checkable contract. openapi_lint checks versioning, idempotency of mutating endpoints, RFC 7807 errors. The baseline passed with 0 findings. Let me keep the same style: add paths and schemas in the same compact style.

I need to add:
- paths:
  - /v1/mandates (post: createMandate, Idempotency-Key; get? no)
  - /v1/mandates/{mandateId} (get)
  - /v1/mandates/{mandateId}/revoke (post)
  - /v1/mandates/{mandateId}/debits (post)
- components schemas: MandateRequest, Mandate, DebitRequest, plus add optional fields to Payment (mandateId, billingPeriod, paymentType).

Constraints for openapi_lint:
- versioning: major/minor? It checks versioning — maybe requires info.version to be semver. 0.2.0 fine. Possibly checks that breaking changes bump major — that's contract_diff, not lint.
- idempotency mutating-endpoint: POST must have Idempotency-Key header param. So each POST needs Idempotency-Key. Baseline createPayment has it. I'll add to all new POSTs.
- RFC 7807 errors: maybe lint checks that responses include 4xx with problem+json? But baseline has no error responses and passed. So it's not required. I'll add error responses anyway? Might introduce issues if schema malformed. Keep consistent with baseline (no error responses) to avoid lint surprises. Actually adding `Error` responses with `application/problem+json` could be flagged if not exactly right. Let me keep it minimal and consistent: no error responses (as baseline). Hmm, but the prose contract defines errors. The openapi file is minimal. Keep minimal.

Wait — but will `contract_diff` treat adding new paths/schemas as non-breaking? Yes, adding endpoints and optional fields is non-breaking. Adding a new required field would be breaking (CD checks request body). I'll make new fields optional. Also adding a new enum value to Payment.status would be breaking maybe — I won't.

Also: contract_diff detects CD-007 "ломающий дифф без смены major info.version". If diff is non-breaking, no issue. If I change version 0.1.0→0.2.0 (minor bump) that's fine for additive. Good.

Let me be careful: contract_diff might consider `version` change alone as fine.

One concern: adding `paymentType` optional to Payment is additive response field → non-breaking. Adding `mandateId`, `billingPeriod` optional → non-breaking.

Let me also add `Mandate` enum status. And `DebitRequest` requires amount and billingPeriod; `DebitRequest` amount required → but it's a NEW schema, so no breaking.

Now, should the new endpoint `/v1/mandates/{mandateId}/debits` request include Idempotency-Key? Yes required.

Let me write the full new file. Keep the style with inline flow mappings where compact, but for new schemas maybe block style for readability. openapi_lint parses YAML; both fine.

Let me write.

Important: openapi_lint "идемпотентность mutating-endpoint'ов" — maybe it requires the header name exactly `Idempotency-Key` and required: true. I'll include.

Also path params need `required: true`.

Let me write the file.

Also description fields in Russian with `—` fine.

Let me draft:

```yaml
openapi: 3.0.3
info:
  title: СБП-шлюз — API ТСП
  version: 0.2.0
  description: >
    Мерчант-API СБП-шлюза. v0.2.0 — аддитивное расширение v0.1.0:
    согласия плательщика (mandates) и рекуррентные C2B-списания (ADR-008, ADR-009).
    Существующие операции и enum Payment.status не изменены.
paths:
  /v1/payments:
    post:
      operationId: createPayment
      ... (unchanged)
  /v1/payments/{paymentId}:
    get: (unchanged)
  /v1/mandates:
    post:
      operationId: createMandate
      parameters:
        - in: header
          name: Idempotency-Key
          required: true
          schema: {type: string}
      requestBody:
        required: true
        content:
          application/json:
            schema: {$ref: '#/components/schemas/MandateRequest'}
      responses:
        '201':
          description: Согласие зарегистрировано (ожидает подтверждения плательщика)
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Mandate'}
  /v1/mandates/{mandateId}:
    get:
      operationId: getMandate
      parameters:
        - {in: path, name: mandateId, required: true, schema: {type: string}}
      responses:
        '200':
          description: Статус согласия
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Mandate'}
  /v1/mandates/{mandateId}/revoke:
    post:
      operationId: revokeMandate
      parameters:
        - {in: path, name: mandateId, required: true, schema: {type: string}}
        - in: header
          name: Idempotency-Key
          required: true
          schema: {type: string}
      responses:
        '200':
          description: Согласие отозвано
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Mandate'}
  /v1/mandates/{mandateId}/debits:
    post:
      operationId: createRecurringDebit
      parameters:
        - {in: path, name: mandateId, required: true, schema: {type: string}}
        - in: header
          name: Idempotency-Key
          required: true
          schema: {type: string}
      requestBody:
        required: true
        content:
          application/json:
            schema: {$ref: '#/components/schemas/DebitRequest'}
      responses:
        '201':
          description: Рекуррентное списание зарегистрировано как платёж
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Payment'}
components:
  schemas:
    PaymentRequest: (unchanged)
    Payment:
      type: object
      required: [paymentId, amount, status]
      properties:
        paymentId: {type: string}
        amount: {type: integer, description: Сумма в копейках}
        status:
          type: string
          enum: [...]
        mandateId: {type: string, description: 'ADR-008: согласие, по которому создано рекуррентное списание (только для подписок)'}
        billingPeriod: {type: string, description: 'ADR-008/009: период обязательства, напр. 2026-10 (только для подписок)'}
        paymentType: {type: string, enum: [ONE_TIME, RECURRING], description: 'Тип платежа; по умолчанию ONE_TIME'}
    MandateRequest:
      type: object
      required: [tspId, payerRef, period]
      properties:
        tspId: {type: string}
        payerRef: {type: string, description: 'Идентификатор плательщика для подтверждения согласия (минимизирован; ПДн)'}
        period: {type: string, enum: [WEEK, MONTH, YEAR], description: 'Периодичность списаний'}
        maxAmountPerDebit: {type: integer, description: 'Лимит суммы одного списания, копейки'}
        maxAmountPerPeriod: {type: integer, description: 'Лимит суммы за период, копейки'}
        paymentPurpose: {type: string}
        notificationLeadHours: {type: integer, description: 'Требуемый lead time предуведомления, часы [ТРЕБУЕТ ПРОВЕРКИ: регламент НСПК]'}
        webhookUrl: {type: string}
    Mandate:
      type: object
      required: [mandateId, status]
      properties:
        mandateId: {type: string}
        tspId: {type: string}
        status:
          type: string
          enum: [PENDING_CONSENT, ACTIVE, SUSPENDED, REVOKED, REJECTED, EXPIRED]
        period: {type: string, enum: [WEEK, MONTH, YEAR]}
        maxAmountPerDebit: {type: integer}
        maxAmountPerPeriod: {type: integer}
        consentProofRef: {type: string, description: 'Ссылка на артефакт подтверждения согласия (152-ФЗ)'}
        createdAt: {type: string, format: date-time}
        expiresAt: {type: string, format: date-time}
    DebitRequest:
      type: object
      required: [amount, billingPeriod]
      properties:
        amount: {type: integer, description: 'Сумма в копейках'}
        billingPeriod: {type: string, description: 'Период обязательства, напр. 2026-10; часть ключа дедупликации (mandateId, billingPeriod)'}
        paymentPurpose: {type: string}
        plannedDebitDate: {type: string, format: date}
```

Wait: `payerRef` — is it PII? fine.

One concern: openapi_lint may flag `format: date` or `date-time`? Unlikely.

Another: openapi_lint might require `info.version` to match path version? Baseline had version 0.1.0 and /v1 paths, passed. So no.

Another: the lint check for "версионирование" might check that version has major.minor.patch. 0.2.0 ok.

Let me also double check: does openapi_lint require every operation to have `operationId`? Baseline has operationIds. I'll add.

Also does it require `responses` for each? yes provided.

I think it's fine. But there's risk with the lint's RFC 7807 check: maybe it requires POST responses to include 400 with problem+json? Baseline createPayment lacks it and passed → so not required.

Now, does contract_diff consider `Payment.status` unchanged? I keep the enum identical. Good. But I'm adding fields to Payment — non-breaking for response.

Potential breaking: I add a NEW schema `Mandate` etc. — non-breaking.

Potential issue: contract_diff might flag that `info.version` changed from 0.1.0 to 0.2.0 as CD-007 only if there's a breaking diff; there isn't. Good.

Let me write the file. I'll preserve the existing compact style for existing parts exactly (to minimize diff), and add new parts.

Let me write full content.

Actually, I should be careful to preserve the exact existing lines so contract_diff sees only additions. Let me reproduce existing content verbatim.

Existing:
```
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

I'll change version to 0.2.0 and add description. Then add paths after /v1/payments/{paymentId} block, before components. Then add fields to Payment and new schemas.

Note: I must not change the enum line (keep identical) — good.

Let me use edit operations instead of full rewrite to reduce risk? Editing a YAML with multiple insertions is doable:
1. version: 0.1.0 → 0.2.0 + description.
2. Insert new paths before `components:`.
3. Insert optional fields into Payment properties (after status enum block).
4. Insert new schemas at end.

Let me do 4 edits. Actually simpler: write_file full content. But write_file requires prior read — I've read it. It's fine to overwrite. But then diff is larger? No, diff is computed by git; content identical lines produce minimal diff. Since write_file writes exact text, unchanged lines remain identical → git diff minimal. Good. I'll use write_file for clarity.

Hmm, but the instruction: "With prior-read enforcement enabled, blind overwrites are rejected." I've read it. Fine.

Let me write.
Now the contract — additive v0.2.0, existing operations and the `status` enum left byte-identical.

  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/openapi/tsp-api.yaml"}, name="mcp__spine__openapi_lint")`
  `tool_call(arguments={"old": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/.qwen<TMP>.orig.yaml", name="mcp__spine__contract_diff")`

Now verify: openapi_lint on new, and contract_diff old vs new. Let me run those now before writing the remaining docs, to catch problems early.
Verifying contract compatibility before writing the rest.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/contracts/tsp-api.md", new_string="# Контракт API ТСП (мерчант-API) — v0.2 draft\n\n- Status: Draft (для ревью на гейте A1 дельты «подписки СБП»)\n- Версия контракта: **0.2**, old_string="# Контракт API ТСП (мерчант-API) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фикс)`

Excellent: openapi_lint PASS, contract_diff breaking: 0, non-breaking: 4. That's machine evidence for output 4.

Now write the remaining docs:
- docs/contracts/tsp-api.md — add §8 (prose contract)
- docs/contracts/opkc-adapter.md — add §10
- docs/spec/state-machine.md — add section
- docs/solutioning.md — update Roadmap §1
- changes/sbp-subscriptions/IMPACT.md
- changes/sbp-subscriptions/ACCEPTANCE.md
- changes/sbp-subscriptions/A3-PACKAGE.md
- changes/sbp-subscriptions/HANDOFF.md

Let me do the contract prose edits. For tsp-api.md, add after §7 (Открытые вопросы)? Better insert §8 before "## 7. Открытые вопросы" or append §8 after §7. The numbered sections: 1..7 with 7 being open questions. I'll append §8 after §7? That's odd ordering. Better: insert new §7 "Согласия и рекуррентные списания" and renumber open questions to §8. Renumbering accepted doc... it's Draft, and additive. Hmm, renumbering causes churn. Simpler: append "## 8. Согласия и рекуррентные списания (v0.2)" at the end, and in §7 note. Actually open questions should stay last. Let me insert the new section as "## 7. Согласия и рекуррентные списания (v0.2 — ADR-008/009)" and change existing "## 7. Открытые вопросы (для A1)" to "## 8. Открытые вопросы (для A1)". That's a clean insert. Also update header "Версия контракта: 0.1" → note 0.2.

Let me read tsp-api.md tail to edit precisely — I already have full content. Let me edit:
- Header block: add v0.2 note.
- Insert section 7 and renumber 7→8.

Let me do it.

For opkc-adapter.md: append §10 after §9 Открытые вопросы? Again ordering. I'll insert "## 9. Операции подписок (рекуррентные списания)" before "## 9. Открытые вопросы" and renumber open questions to 10. Current sections: 1..9 with 9 = Открытые вопросы. So insert new "## 9. Операции подписок" and change "## 9. Открытые вопросы" → "## 10. Открытые вопросы".

Let me do these edits.
Contract checks are green (0 breaking). Now the prose contract addenda and the state-machine note.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/contracts/tsp-api.md", new_string="## 7. Согласия и рекуррентные списания (v0.2 — ADR-008, ADR-009)\n\n**Расширение аддитивное:** существующие методы §3.1–3.5, схемы и enum `, old_string="## 7. Открытые вопросы (для A1)\n\n1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — road)`

Now insert the new section 7 before "## 7. Открытые вопросы (для A1)". Let me find the exact text.

The existing section 7 is:
```
## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
```

I'll replace "## 7. Открытые вопросы (для A1)" ... keeping items but renumber to 8, and insert section 7 before it.

Let me construct the edit: old_string = the whole section 7 block; new_string = new section 7 + section 8 (same items, renumbered). Let me do it.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/contracts/opkc-adapter.md", new_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.2 draft\n\n- Status: Draft (для ревью на гейте A1 дельты «подписки СБП»; основа для , old_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1; основа для RFP вендора)\n- Owner:)`

Wait — section 6 "Версионирование и совместимость" says "Путь /v1; изменения, ломающие контракт, — только в /v2..." and the new §7 comes after §6. But I inserted §7 before the original §7 (open questions). Good ordering: 1..6, 7 (new), 8 (open). The read shows §6 content then §7. Good.

Now opkc-adapter.md — insert §9 and renumber open questions to §10. Let me edit.

Original tail:
```
## 8. Требования к вендору (для RFP)

1. Реализует настоящий контракт поверх протокола НСПК; нормализует статусы/ошибки.
2. Сертификаты ФСТЭК/соответствие требованиям НСПК; СКЗИ/HSM (ADR-003, ADR-006).
3. Тестовый контур НСПК: возможность гонять сценарии (paid/rejected/expired, повторы) — для тестов ядра.
4. Идемпотентность мутирующих операций по `reference` (§5) — **обязательно**.
5. SLA, поддержка, референсы в банках сопоставимого масштаба.
6. Эксплуатация: метрики, алерты, документация runbook.

## 9. Открытые вопросы

1. Нужен ли синхронный `getReconciliationReport` ...
2. Нормализованные `reasonCode` ...
3. Поведение ядра при `transport.unavailable` (приём QR в очередь vs отклонение) — политика, утверждается на A2.
```

Insert new "## 9. Операции подписок (рекуррентные списания) — ADR-008, ADR-009" before "## 9. Открытые вопросы", renumber to 10.

Section 9 content: new sync ops: createMandate, getMandateStatus, revokeMandate, createRecurringDebit; new events: mandate.activated/rejected/revoked, payment.rejected_by_payer? Actually the debit result comes as payment.paid / payment.rejected with reasonCode PAYER_REJECTED. Add to events table. And add RFP requirement.

Let me write it. Table format similar.

Also update header "Версия контракта"? The opkc-adapter.md header: "# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.1 draft". Update to v0.2 draft with related ADR-008/009.

Let me do two edits.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/contracts/opkc-adapter.md", new_string="## 9. Операции подписок (согласия и рекуррентные списания) — ADR-008, ADR-009\n\nАддитивное расширение границы ядро↔адаптер (AD-004): прото, old_string="## 9. Открытые вопросы\n\n1. Нужен ли синхронный `getReconciliationReport` или сверку делать событиями/файлами — решить с вендором на RFP ()`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/spec/state-machine.md", new_string="Маппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `EXPIRED`, `REFUNDED` — без техн, old_string="Маппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `EXPIRED`, `REFUNDED` — без техн)`

Now update docs/spec/state-machine.md to add the recurring payment note (MODIFIED). Insert a subsection or a note. I'll add to §2 transition table a note about recurring, and add a new §7 "Рекуррентные списания (дельта подписок)". Simpler: add a section before "## 6. Согласованность с API ТСП"? Or after. Let me add "## 7. Рекуррентные списания (подписки) — ADR-008" at the end.

Also §6 mentions mapping; fine.

Let me append section 7.

Actually the file has sections 1-6. Append section 7 after §6. Let me edit the tail: the last line is the §6 paragraph. I'll append.

Let me read the last lines to anchor. From earlier read: file ends with:
```
## 6. Согласованность с API ТСП

Маппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `EXPIRED`, `REFUNDED` — без технических подсостояний (`ABS_PENDING`, `NOTIFY_PENDING` наружу не выставляются; `ABS_PENDING` отражается как `PAID` + поле `creditingStatus`).
```

I'll append after that paragraph.

Also update the header "Связано:" to include ADR-008/AD-009 and AD-009. Let me do a combined edit for header + append. Actually two edits.

Let me do the append edit with anchor the final paragraph.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/solutioning.md", new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop, old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop)`

Now update docs/solutioning.md §1 Roadmap line (автоплатежи out of scope → in scope). Edit that line.

Original in solutioning.md §1: "Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

Change to move автоплатежи into scope via delta, referencing changes/sbp-subscriptions/DELTA.md.

Let me edit.

  `write_file(content="# Impact — дельта «подписки СБП»: влияние на принятую архитектуру\n\n- Status: Draft (вход на A3)\n- Дата: 2026-09-28\n- Связано: `changes/, file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/changes/sbp-subscriptions/IMPACT.md")`

Now write the change package docs: IMPACT.md, ACCEPTANCE.md, A3-PACKAGE.md, HANDOFF.md.

### IMPACT.md (outputs 1 & 2)

Sections:
1. Что меняется / что не меняется (summary)
2. Оценка значимости (machine verdict, triggers, why Critical, route A0-A5)
3. Влияние на инварианты (table AD-001..AD-009: затронут/как/меняется ли Rule)
4. Влияние на компоненты (new: mandate service/store; changed: API layer, state machine, notifier, reconciler, audit; unchanged: adapter boundary shape, ABS adapter, transport)
5. Влияние на контракты (TSP API additive; adapter additive; events; compatibility evidence)
6. Влияние на данные/PII (new consent store, retention, audit)
7. Влияние на NFR (burst, latency; base SLO unchanged)
8. Риски (risk list with mitigation) — maybe short
9. Что НЕ меняется (explicit)

Let me write it.

### ACCEPTANCE.md (output 6)
- EARS criteria (numbered, positive+negative)
- Откат (rollback) plan: signals, steps, owner
- Fitness rules mapping
- Definition of done / gates

### A3-PACKAGE.md (output 7)
- Human decisions list with options, recommendation, why human
- Machine-readable JSON {choice, rationale, constraints, rejected_options, expiry}
- Machine-readable secondary decisions

### HANDOFF.md
- epic-context 800-1500 tokens
- invariant Rules verbatim
- forbidden changes
- acceptance summary
- result contract JSON

Let me write IMPACT.md.
Now the change-package documents. First the impact assessment (outputs 1 and 2).

  `write_file(content="# Приёмка и план отката — дельта «подписки СБП»\n\n- Status: Draft (вход на A1/A3)\n- Дата: 2026-09-28\n- Связано: ADR-008, ADR-009, AD-009, file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/changes/sbp-subscriptions/ACCEPTANCE)`

Now ACCEPTANCE.md with EARS criteria and rollback plan. The fitness rule `delta-acceptance-ears` pattern requires lines starting with When/While/If/Where (optionally bulleted/bold). I need to ensure the file contains such lines. I'll format criteria as bullet list: `- When ... , the шлюз shall ...`. That matches `^\s*[-*]?\s*\**\s*(When|While|If|Where)\b`.

Let me write.

Include:
- Gate criteria (A1-A5)
- EARS acceptance criteria (positive + negative)
- Property-test criteria (executable)
- Compatibility criteria
- Rollback plan (signals, steps, owner)
- Fitness rules mapping

Let me write it.

  `write_file(content="# A3 — пакет человеческого решения по дельте «подписки СБП»\n\n- Status: **ОЖИДАЕТ РЕШЕНИЯ A3** (человек-архитектор + владелец продукта)\n-, file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/changes/sbp-subscriptions/A3-PACKAGE)`

Now A3-PACKAGE.md (output 7). Human decisions with machine-readable JSON.

The A3 package per significance-routing: machine-readable итог {choice, rationale, constraints, rejected options, expiry}. And the explicit "что остаётся на решение человека-архитектора".

Primary human decision: model of initiation (ТСП-driven vs gateway scheduler vs NSPK-only). Recommendation: ТСП-driven (option A). But it's a HUMAN decision — so I present options, recommendation, and note it can't be decided by the agent because it changes commercial responsibility/SLA with ТСП and product scope.

Also secondary human decisions:
1. Инициация: ТСП-driven vs планировщик (primary).
2. Экспозиция управления согласиями ТСП (кто создаёт согласие — ТСП через API vs только банк/приложение плательщика).
3. Коммерческие условия и лимиты по умолчанию.
4. Go/no-go на старт транспортного слоя подписок до документации НСПК и подтверждения вендора.
5. Политика хранения артефакта подтверждения согласия (ИБ/юрист).
6. Дата/условия пересмотра ADR-008.

Machine-readable block for the primary decision. Also note which are blocking (A3) vs delegated.

Let me write.

  `write_file(content="# HANDOFF — дельта «подписки СБП» кодовому харнессу\n\n- Status: Draft (готов после A3; до A3 использовать как A2-заготовку walking skeleto, file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/changes/sbp-subscriptions/HANDOFF.md)`

Now HANDOFF.md — epic-context for executors (800-1500 tokens by meaning), invariants verbatim, forbidden changes, acceptance, result contract JSON.

Following handoff-packaging: TASK + contract result. I'll write a dense epic-context.

Let me write it, being mindful of token budget (~800-1500 tokens). I'll aim for a compact but complete package reference (it can reference files, not copy everything). The skill says compile by meaning, invariants verbatim.

Let me write.
Finally, the executor handoff package (epic-context, invariants, result contract).

  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws"}, name="mcp__spine__fitness_check")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/ARCHITECTURE-SPINE.md"}, name="mcp__spine__spine_lint")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws"}, name="mcp__spine__delta_guard")`

Now verify everything: run fitness_check, spine_lint, delta_guard, architect_review, trace_check (SKIP, no model), nfr_check (needs model → SKIP). Let me run the gate-level checks.

The critical ones:
- fitness_check (new rules must pass) — check the owner/expiry/rationale fields don't break parsing.
- spine_lint (AD-009 added, no issues).
- delta_guard (ARCHITECTURE-SPINE.md and CONSTRAINTS.yaml changed, must be mentioned in changes/sbp-subscriptions/DELTA.md).
- architect_review composite.

Let me run them.

Note: fitness_check's `delta-acceptance-ears` rule glob changes/sbp-subscriptions/ACCEPTANCE.md — file exists and has EARS lines. Good.
`mandates-endpoint-present` glob openapi/tsp-api.yaml pattern /v1/mandates — present.
`subscription-nfr-measurable` — docs/nfr-sbp-subscriptions.md contains 99,95. Yes ("доступность ≥ 99,95 %").
`mandate-debit-only-active` — ARCHITECTURE-SPINE.md contains "только при статусе согласия". Yes in AD-009 Rule.
`mandate-revocation-stops-debits` — pattern 'после события отзыва согласия новые списания запрещены' — yes in AD-009 Rule.
`mandate-period-idempotency` — docs/adr/ADR-008*.md contains 'billingPeriod' — yes.
`adr-008-present`, `adr-009-present` files exist.
`delta-present` exists.

Let me run fitness_check and others.

Also there may be a concern: rule `adr-no-placeholders` must_not_contain glob docs/adr/*.md pattern '<!--' — my new ADRs have no `<!--`. Good. Actually I wrote "Supersedes: —" (em dash), not `<!--`. Good.

Also `spine-lints-clean` must_not_contain 'TODO|TBD|XXX' in ARCHITECTURE-SPINE.md — I added "Deferred" text; no TODO/TBD/XXX. Good.

Let me run the checks in parallel.
All artifacts written. Now verifying the whole control loop is green.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="    pattern: '(?i)только при статусе согласия'", old_string="    pattern: 'только при статусе согласия'")`

Interesting findings:
1. fitness_check FAILED on `mandate-debit-only-active`: pattern 'только при статусе согласия' not found in ARCHITECTURE-SPINE.md. But I added it: "инициируется ТОЛЬКО при статусе согласия `ACTIVE`". Wait — I wrote "ТОЛЬКО" in uppercase (Cyrillic "ТОЛЬКО"). The pattern 'только при статусе согласия' uses lowercase "только". Regex is case-sensitive by default. So it doesn't match "ТОЛЬКО при статусе согласия". Need to make pattern case-insensitive or match. Options: change the rule pattern to '(?i)только при статусе согласия' or rewrite spine text to lowercase. The spine AD-009 says "инициируется ТОЛЬКО при статусе согласия". Hmm, and DELTA.md has "только при статусе согласия" but glob is ARCHITECTURE-SPINE.md. 

Let me fix the rule pattern to `(?i)только при статусе согласия`. That's cleaner. Actually the delta's candidate said pattern `только при статусе согласия`. I'll make it case-insensitive.

Also note `mandate-revocation-stops-debits` matched? It passed since only 1 issue. Good.

2. delta_guard passed, but `protected_changed` lists only ARCHITECTURE-SPINE.md — CONSTRAINTS.yaml is under `.arch-handoff/` not `.arch-handoff/CONSTRAINTS.yaml`? The default protect includes "CONSTRAINTS.yaml" (maybe as a path or prefix). It says protected_changed: ["ARCHITECTURE-SPINE.md"]; changed files 19. So CONSTRAINTS.yaml wasn't flagged as protected (maybe because protect default is "model/", "ARCHITECTURE-SPINE.md", "CONSTRAINTS.yaml" and matching is by exact path relative to root — `.arch-handoff/CONSTRAINTS.yaml` != `CONSTRAINTS.yaml`). Fine, no violation anyway.

3. `issues` count 1 — only the casing issue. Good.

Let me fix the pattern. Then re-run fitness_check.

Also note errors: 12 (error rules) and my new rules added. Fine.

Let me fix CONSTRAINTS pattern to `(?i)только при статусе согласия`.

Also, `constraints` fingerprint shows rules: 16 (7 original + 9 new). Good.

Let me edit the pattern.
One fitness rule caught a real mismatch — my trace pattern was case-sensitive against the spine's uppercase `ТОЛЬКО`. Fixing the rule to be case-insensitive.

  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws"}, name="mcp__spine__fitness_check")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws"}, name="mcp__spine__architect_review")`
  `grep_search(pattern="opkc-adapter|контракт адаптера|требовани", path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/rfp/vendor-rfp.md")`

fitness_check now passes (16 rules, 0 violations). Interesting: the fingerprint didn't change (66d4f24e) — because fingerprint is over the rule set (names/types), not patterns? Anyway green.

Now run the composite architect_review to confirm overall PASS, and also verify the RFP doc mentions? Also I should add the requirement to vendor-rfp.md? The task asked for contract changes; RFP is optional. The opkc-adapter.md §9.3 says "Дополнение к требованиям вендора (RFP, §8)". It might be good to also add to docs/rfp/vendor-rfp.md. Let me check if it's worth it. The DELTA didn't list vendor-rfp.md. To keep scope tight and consistent with DELTA, I could skip. But "передать исполнителям" and vendor selection is affected. Hmm. The task's 7 outputs don't require RFP update. I'll leave RFP untouched (the adapter contract §9.3 is the source; RFP references it). Actually, a careful architect would note it. Let me check vendor-rfp.md quickly to see if it references opkc-adapter.md as the source of requirements — if so, no edit needed.

Let me run architect_review and read vendor-rfp briefly.

Actually let me just run architect_review (composite) and trace_check (will SKIP). And read vendor-rfp.md to decide.

Let me do architect_review and read vendor-rfp head.
Green. Running the composite review and checking whether the vendor RFP needs a pointer.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/rfp/vendor-rfp.md", limit=50)`

architect_review PASS. Note route "Fast" auto — because it computes route from git diff (only api_contract_change detected), not from the business change. That's the tool's anti-bypass detector on the diff, and it says route auto = Fast with score 1. This is a discrepancy worth flagging: the git-diff-based detector under-rates because most artifacts are docs. I should mention this honestly — the business change is Critical (per significance_score with explicit triggers), while the diff-based detector says Fast because it sees only the contract file change. This is exactly the kind of nuance to report: I used significance_score with reasoning, and the auto-detector on the diff is not authoritative for a docs-only package. Actually — does this matter? The gate passed either way. But I should note the discrepancy transparently. Hmm, also the delta_guard says "изменённых файлов 19" — that includes all new files.

Actually wait: the architect_review route_auto says "score 1 (api_contract_change)". This is because `significance_from_diff` analyses only certain file patterns. My openapi change triggered api_contract_change. But the change is genuinely Critical because of financial/subscription semantics that a diff detector can't see (new_component, security_boundary_change are semantic). I'll mention this as a known limitation and that I anchored on the semantic trigger set. Good honesty.

Now, vendor-rfp.md: it references opkc-adapter.md as source of requirements and checklists §§3–4, and G4 "Реализация полного набора методов/событий контракта opkc-adapter §3–4". Since I added §9, the RFP should reference §3–4, §9 to be complete. This is a real gap: if I don't update, the RFP's checklist won't require subscription operations. The DELTA didn't list vendor-rfp.md. Given "changing accepted files only in the accepted way", I should add vendor-rfp.md to the DELTA MODIFIED table and make a minimal edit (add §9 to G4 and the checklist reference). That's the thorough move and matches the architect instruction "Fulfill the user's request thoroughly."

But careful about scope creep — is it needed? The task item 4 is contract changes; the RFP is a derived externality. The IMPACT/DELTA mention "требования RFP". I think a small, precise edit to vendor-rfp.md is warranted and I'll add it to DELTA MODIFIED. Let me read the relevant lines to edit precisely.

Let me read vendor-rfp.md lines 1-50 and 110-120.

Actually the grep gave enough: line 27 "G4 | Реализация полного набора методов/событий контракта opkc-adapter §3–4", line 118 checklist "Контракт opkc-adapter.md зафиксирован как v1.0-draft (после ревью A1)."

I'll update line 27 to "§3–4, §9" and add a row or note. And line 36 "Соответствие контракту opkc-adapter (полнота...)" fine. Maybe add G-row for subscription ops. Minimal: change G4 to include §9, and add a criterion row about подписки. Let me read the file to edit properly.
The composite review is green. The vendor RFP references the adapter contract's §3–4 only, so it currently wouldn't require the new subscription operations — let me close that gap.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/rfp/vendor-rfp.md", offset=45, limit=18)`

I'll edit:
1. Header "Связано" add ADR-008, ADR-009.
2. Scope list add item 7: поддержка операций согласий/рекуррентных списаний (§9 контракта).
3. G4 change to "§3–4, §9".
4. §4 Технические требования add bullet for Методы §9 and События §9.2.

Also the DELTA MODIFIED table should list vendor-rfp.md. Let me add it.

Let me read lines 50-60 to see the events bullet end. Actually I have enough: line ~50 ends "**События** (§4): ...". Let me read a bit more to anchor the edit.

Let me read 48-60.

Actually, I can edit with the bullet I saw and add after it. But I need exact text of the next line. Let me read 44-60.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/rfp/vendor-rfp.md", new_string="- Связано: ADR-007 (гибрид), ADR-003, ADR-008 (подписки), ADR-009 (совместимость), AD-004, AD-008, `docs/contracts/opkc-adapter.md`", old_string="- Связано: ADR-007 (гибрид), ADR-003, AD-004, AD-008, `docs/contracts/opkc-adapter.md`")`

Now make the edits to vendor-rfp.md. I'll do a few edits:

1. Header line 5: add ADR-008, ADR-009.
2. Scope item list: add item 7.
3. G4: §3–4, §9.
4. §4 bullets: add Методы §9 and События §9.2.

Let me do them.

Edit 1 + scope (lines 5-16 region). Let me target the "Связано" line and the numbered list.

Actually, simpler: 
- Edit A: replace "- Связано: ADR-007 (гибрид), ADR-003, AD-004, AD-008, `docs/contracts/opkc-adapter.md`" with added ADR-008, ADR-009.
- Edit B: replace "6. Поддержка и SLA." + the "Не входит..." line? Add item 7 after 6. Target:
```
6. Поддержка и SLA.

**Не входит в scope вендора:**
```
replace with
```
6. Поддержка и SLA.
7. Поддержка операций согласий и рекуррентных списаний (СБП-подписки) — `opkc-adapter.md` §9: методы и события, идемпотентность по `reference`.

**Не входит в scope вендора:**
```
- Edit C: G4 row.
- Edit D: §4 bullets add.

Let me do all 4 edits.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/rfp/vendor-rfp.md", new_string="6. Поддержку и SLA.\n7. Поддержку операций согласий и рекуррентных списаний (СБП-подписки) — `opkc-adapter.md` §9: методы, события, идемпот, old_string="6. Поддержку и SLA.\n\n**Не входит в scope вендора:**")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/rfp/vendor-rfp.md", new_string="| G4 | Реализация полного набора методов/событий контракта opkc-adapter §3–4, **§9 (подписки)** | Сверка по чек-листу контракта |", old_string="| G4 | Реализация полного набора методов/событий контракта opkc-adapter §3–4 | Сверка по чек-листу контракта |")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/rfp/vendor-rfp.md", new_string="- **NFR** (§7): нагрузка, latency, потеря событий = 0, доступность ≥ 99,95 %, Prometheus-метрики, trace id.\n- **Операции подписок** (§9): , old_string="- **NFR** (§7): нагрузка, latency, потеря событий = 0, доступность ≥ 99,95 %, Prometheus-метрики, trace id.")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/changes/sbp-subscriptions/DELTA.md", new_string="| `docs/contracts/opkc-adapter.md` | Добавляется §10 «Операции подписок» + требование RFP | Граница ядро↔вендор |\n| `docs/rfp/vendor-rfp.m, old_string="| `docs/contracts/opkc-adapter.md` | Добавляется §10 «Операции подписок» + требование RFP | Граница ядро↔вендор |\n| `docs/solutioning.md` )`

Now add vendor-rfp.md to the DELTA MODIFIED table. Edit DELTA.md: add a row.

Current MODIFIED table rows end with:
| `docs/solutioning.md` §1 (Roadmap) | «автоплатежи» переносятся из Roadmap в scope (ссылкой на эту дельту) | Граница scope изменилась по запросу бизнеса |

Add row for vendor-rfp.md.

Let me also add to DELTA §2 "Что дельта НЕ трогает" — fine.

Let me edit.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/changes/sbp-subscriptions/DELTA.md", new_string="| `docs/contracts/tsp-api.md` | Добавляется §7 «Согласия и рекуррентные списания» (открытые вопросы → §8) | Прозаическое зеркало контракта , old_string="| `docs/contracts/tsp-api.md` | Добавляется §8 «Согласия и рекуррентные списания» | Прозаическое зеркало контракта |\n| `docs/contracts/opk)`

Now, let me do a final adversarial self-review pass. Let me load the adversarial-review skill and apply it, since this is exactly "before handoff to implementation" and "подготовка к архитектурному комитету". This aligns with the instruction to use the methodology skills. Let me load it and then run a review pass, and also consider using a fork/subagent for independent review. Actually the adversarial-review skill is a methodology; let me load it and then apply its lenses myself. Given time/context, loading the skill and doing a focused pass is good.

Also I should run the final verification: architect_review again (already green), plus maybe `verdict_explain` to produce a verdict passport? That could be a nice artifact. And `trust_report`? Not required.

Let me load adversarial-review skill and then do the review. Also, I realize I should double-check one semantic issue: I claimed AD-001 "усиление" etc. Fine.

Let me also verify there's no contradiction: NFR doc says "PENDING_CONSENT/..." fine.

Potential issue: In DELTA.md I referenced `docs/contracts/tsp-api.md` "Добавляется §8" but actually I inserted §7 (new) and renumbered open questions to §8. So the DELTA text "Добавляется §8 «Согласия и рекуррентные списания»" is WRONG — it's §7. Let me fix that in DELTA.md and in IMPACT.md (which says "добавлен §7" — correct in IMPACT §4 table? Let me check: IMPACT says "docs/contracts/tsp-api.md | добавлен §7 «Согласия и рекуррентные списания»" — correct). DELTA says "Добавляется §8" — wrong. Fix to §7.

Similarly DELTA says opkc-adapter "Добавляется §10 «Операции подписок»" but actually inserted §9 and renumbered open questions to §10. So DELTA wrong for opkc too: should be §9. And IMPACT says "добавлен §9 «Операции подписок»" — correct. Let me fix DELTA rows.

Let me fix those two in DELTA.

Also ACCEPTANCE references? no.

Let me fix.
Let me fix two section-number references in the delta to match the actual contract docs.

  `skill(skill="adversarial-review")`

Now let me run the adversarial review as a final quality gate. Let me load the skill and apply. Actually, I could delegate an independent adversarial review to a subagent (fork) to genuinely get an independent contour. The task says "используй их по назначению" and adversarial-review says "независимым контуром". A fork would inherit context and could review. But the instructions caution about background agents and not duplicating work. Given the value, let me do a focused self-review using the skill's lenses rather than spawning an agent (the skill is designed to be applied). Actually, spawning a fork for independent adversarial review is a strong fit and demonstrates proper tool use. But it adds latency and the user is waiting. Hmm.

The task is a documentation package; the deliverable is complete and verified. An independent adversarial review would strengthen it, but I can perform the review myself with the skill. Let me load the skill and do a concise review, reporting findings honestly (including the route-detector discrepancy).

Let me load adversarial-review.
Let me apply the adversarial-review lens as a final gate before reporting.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/openapi/tsp-api.yaml", new_string="        maxAmountPerDebit: {type: integer}\n        maxAmountPerPeriod: {type: integer}\n        consentUrl: {type: string, description: 'С, old_string="        maxAmountPerDebit: {type: integer}\n        maxAmountPerPeriod: {type: integer}\n        consentProofRef: {type: string, descriptio)`

Let me apply the adversarial lenses to my own package and report honest findings. I'll inspect for real evidence-based issues.

Lens 1 — Interfaces/contracts:
- The debit endpoint returns Payment with status CREATED; but the TSP API's `Payment.status` enum includes QR_ISSUED. For recurring, no QR_ISSUED. Clients might expect QR fields. Not a blocker.
- Webhook opt-in: I say events delivered only with flag; but if a TSP has the flag off, they cannot learn mandate status except polling GET. Acceptable.
- Adapter `createMandate` returns consentRef/consentUrl; the TSP API `POST /v1/mandates` response example returns `consentUrl` but the openapi `Mandate` schema doesn't define `consentUrl` (it has consentProofRef). Inconsistency: prose example returns consentUrl, openapi Mandate schema lacks it. That's a real minor/major finding: contract inconsistency between prose §7.1 and openapi schema Mandate. Let me check: openapi Mandate has fields: mandateId, tspId, status, period, maxAmountPerDebit, maxAmountPerPeriod, consentProofRef, createdAt, expiresAt. No consentUrl. Prose §7.1 response: `{ mandateId, status, consentUrl }`. So `consentUrl` is missing in the machine schema. Also prose §7.2 lists `consentProofRef` — present. So `consentUrl` (where payer confirms) is needed but not in schema. This is a genuine gap → major (верification-safety). I should fix it: add `consentUrl` to Mandate schema (optional). Good catch — I'll fix.

Lens 2 — Data:
- RPO=0 for mandates claimed; mandate store persistence — fine.
- Dedup window ≥ mandate lifetime — ok.
- PII: payerRef minimized. ok.

Lens 3 — Security/compliance:
- Consent proof artifact: consentProofRef; retention per 152-ФЗ. Delegated to ИБ. Fine.
- Audit: covered.
- Revocation race: covered.

Lens 4 — NFR/ops:
- Burst handled.
- DLQ/recon covered.
- Rollback covered.

Lens 5 — Implementability:
- "predварительное уведомление" — whose mechanism? I say guard requires it performed; but WHO performs notification and how does шлюз know it was performed? In real СБП, the payer's bank notifies; merchant/шлюз may need to trigger notification via НСПК. This is ambiguous: I model `notificationLeadHours` and guard "выполнено предуведомление" but no mechanism defines how compliance is evidenced. That's a real "here a miracle happens" finding → major. I should address: add to mandate-lifecycle/NFR a note that notification mechanism is external input [ТРЕБУЕТ ПРОВЕРКИ] and the guard checks `plannedDebitDate - now >= notificationLeadHours` as the enforceable proxy, with the actual notification performed by НСПК/payer bank per regulation; if НСПК requires merchant-side notification, adapter gets a `notifyDebit` operation. Let me at least make it explicit and honest rather than hand-wave. I'll add a clarification in mandate-lifecycle.md §3 and openapi description. Actually the DebitRequest plannedDebitDate + notificationLeadHours gives an enforceable check: debit allowed only if plannedDebitDate ≥ now + lead. That IS a mechanism (the шлюз enforces the lead window). But who sends the notice? I'll state: notice is delivered by the payer's bank per НСПК; if regulation requires merchant-side notice, it's an additional adapter operation [ТРЕБУЕТ ПРОВЕРКИ]. Let me add that to mandate-lifecycle §3 or the NFR open questions. This is worth adding.

Also: the `notificationLeadHours` is on MandateRequest, but the guard uses plannedDebitDate from DebitRequest. If plannedDebitDate omitted, how to check lead time? Then notification presumed done externally. Ambiguity. I'll clarify: if plannedDebitDate omitted → шлюз не может проверить lead time → either reject (require plannedDebitDate) or rely on external notice. That's a design decision. Hmm, this is getting deep. Better: make `plannedDebitDate` required for debits? Or make it optional and state that when omitted, lead-time check is not enforced by шлюз (responsibility of ТСП/НСПК). To be safe and testable, I think the AC "If требование предуведомления не выполнено, then reject PRE_NOTIFICATION_REQUIRED" requires a checkable input. I'll state plannedDebitDate is required when notificationLeadHours > 0 (conditional). That's a clean rule. Let me add.

This is a good adversarial finding to fix.

Lens 1 more: The adapter §9.1 `createMandate` returns consentRef/consentUrl; the core mandate store needs consentUrl to give ТСП. ok.

Another: In DELTA "MODIFIED docs/contracts/tsp-api.md — Добавляется §7 (открытые вопросы → §8)". Earlier the file's section 6 was "Версионирование"; wait, I inserted §7 before "Открытые вопросы" which was §7. But hold on — the original tsp-api.md sections: 1 Общие, 2 Идемпотентность, 3 Методы, 4 Ошибки, 5 Вебхуки, 6 Версионирование, 7 Открытые вопросы. So inserting new §7 before open questions → §8. Correct as fixed.

Another potential: IMPACT says contract_diff non-breaking 4 — but actually it found 4 added paths (CD-005 warn), and 0 breaking. Good.

Another: `mandate-debit-only-active` pattern case-insensitive now. Good.

Now, the route discrepancy: architect_review route_auto = Fast (score 1) while significance_score = Critical (11). I should report this honestly as a finding: the diff-based detector under-rates a docs-only change; the semantic trigger assessment is authoritative. Note it in the response, maybe also add a note in DELTA §1. Actually DELTA §1 already says Critical with triggers. I'll add a one-line note about the diff-detector discrepancy to DELTA/IMPACT so the committee isn't confused when the gate prints "Fast". That's valuable. Let me add to IMPACT §1 a note.

Let me make these fixes:
1. Add `consentUrl` (and maybe `webhookUrl`?) to openapi Mandate schema.
2. Clarify notification mechanism + conditional plannedDebitDate in mandate-lifecycle.md and openapi description / tsp-api.md §7.4.
3. Add note about route-detector discrepancy in IMPACT §1.

Let me implement.

Fix 1: openapi Mandate schema add `consentUrl: {type: string, description: 'URL/ссылка для подтверждения согласия плательщиком'}`. Adding an optional property to a NEW schema is non-breaking (schema is new anyway, so no diff impact). Good.

Fix 2a: mandate-lifecycle.md §3 add a bullet clarifying: "Предуведомление обеспечивается регламентом НСПК (уведомляет банк плательщика/НСПК); если регламент возлагает уведомление на мерчанта — это отдельная операция адаптера [ТРЕБУЕТ ПРОВЕРКИ]. Проверяемый шлюзом прокси — окно: plannedDebitDate - now ≥ notificationLeadHours."
Fix 2b: openapi DebitRequest plannedDebitDate description: "Обязателен, если у согласия notificationLeadHours > 0; ...".
Fix 2c: tsp-api.md §7.4 rules bullet adjust: "выполнено предуведомление (окно plannedDebitDate − now ≥ notificationLeadHours; иначе PRE_NOTIFICATION_REQUIRED)".

Fix 3: IMPACT §1 note.

Let me do the edits. Also update ACCEPTANCE EARS criterion on pre-notification to reflect the window check? It currently says "If требование предварительного уведомления не выполнено (нарушен lead time)". That's fine with the window mechanism.

Let me apply.
My adversarial pass surfaced three real gaps. Fixing them:

**(1)** `consentUrl` appears in the prose response but is missing from the OpenAPI `Mandate` schema.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/spec/mandate-lifecycle.md", new_string="- **Предуведомление обязательно** при инициации: не выполнено — списание не регистрируется. Проверяемый шлюзом прокси: окно `plannedDebitDa, old_string="- **Предуведомление обязательно** при инициации: не выполнено — списание не регистрируется.\n- Согласие нельзя подтвердить без ссылки на по)`

**(2a)** Clarify notification mechanism in mandate-lifecycle.md §3. Add a bullet.

The §3 invariants list currently ends with:
"- Согласие нельзя подтвердить без ссылки на подтверждение (M2) — согласие без доказуемого основания недействительно (152-ФЗ)."

Add a bullet about предуведомление mechanism.

**(2b)** DebitRequest plannedDebitDate description: conditional required.

**(2c)** tsp-api.md §7.4 rule bullet.

Let me edit mandate-lifecycle.md.
**(2)** The pre-notification requirement had no enforceable mechanism — making it a checkable window and naming the external dependency.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/openapi/tsp-api.yaml", new_string="        plannedDebitDate: {type: string, format: date, description: 'Плановая дата списания. Обязательна, если у согласия notificationLeadH, old_string="        plannedDebitDate: {type: string, format: date, description: 'Плановая дата списания (для проверки lead time предуведомления)'}")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/docs/contracts/tsp-api.md", new_string="- выполнено предуведомление: окно `plannedDebitDate − now ≥ notificationLeadHours` (при `notificationLeadHours > 0` поле `plannedDebitDate`, old_string="- выполнено предуведомление (иначе `PRE_NOTIFICATION_REQUIRED`);")`

Now fix tsp-api.md §7.4 rules bullet to reflect the window mechanism.

Current: "- выполнено предуведомление (иначе `PRE_NOTIFICATION_REQUIRED`);"
Change to: "- выполнено предуведомление: окно `plannedDebitDate − now ≥ notificationLeadHours` (при `notificationLeadHours > 0` поле `plannedDebitDate` обязательно; иначе `PRE_NOTIFICATION_REQUIRED`);"

Let me edit.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/changes/sbp-subscriptions/IMPACT.md", new_string="- **Маршрут и гейты:** A0 fit (аддитивность, ядро независимо от транспорта) → A1 Spec (mandate-lifecycle, NFR, контракты) → A2 Plan (walkin, old_string="- **Маршрут и гейты:** A0 fit (аддитивность, ядро независимо от транспорта) → A1 Spec (mandate-lifecycle, NFR, контракты) → A2 Plan (walkin)`

**(3)** Add the route-detector discrepancy note to IMPACT §1.

Let me edit IMPACT §1 to add a note after the route/gates bullet.

Current §1 ends with:
"- **Маршрут и гейты:** A0 fit ... → A5 drift (...)."

Add: "> Примечание: композитный `architect_review` печатает маршрут из git-диффа (для docs-пакета — `Fast`, score 1, только `api_contract_change`). Это не противоречие: дифф-детектор видит лишь изменение контракта, но не семантику денег без действия плательщика. Авторитетна оценка по триггерам (`significance_score`, Critical/11); при реализации код и контракты поднимут дифф-маршрут."

Let me add.
**(3)** Recording the honest discrepancy between the semantic route and the diff-based detector.

  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/openapi/tsp-api.yaml"}, name="mcp__spine__openapi_lint")`
  `tool_call(arguments={"format": "openapi", "new": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws/openapi, name="mcp__spine__contract_diff")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2-pilot/cells/wub9ahe/ws"}, name="mcp__spine__architect_review")`

Now re-verify contract lint/diff after the openapi edits, and fitness (delta-acceptance-ears requires EARS lines in ACCEPTANCE.md — present). Also openapi change added consentUrl to a new schema — no breaking impact on old. Let me re-run openapi_lint and contract_diff, and fitness_check + architect_review final.

Let me run openapi_lint, contract_diff, fitness_check in parallel. Then architect_review final.

Actually architect_review includes fitness. Let me run openapi_lint, contract_diff, architect_review.

Let me do it.
Re-verifying after the fixes.

  `run_shell_command(command="cd <HARNESS>/runs-v2-pilot/cells/wub9ahe/ws && rm -f .qwen<TMP>.orig.y, description="Clean scratch file and list final change set")`

All green: fitness PASS (16 rules, 0 violations), delta_guard PASS (20 changed files, ARCHITECTURE-SPINE.md covered by delta), rule_weakened PASS, spine_lint PASS, openapi_lint PASS, contract_diff 0 breaking.

Now cleanup: remove `.qwen<TMP>.orig.yaml`? The instruction says delete intermediate files when done. It's under .qwen/tmp/ which is fine (not recorded as artifact). But cleanup is good. However, it's useful as evidence base for the A4 contract_diff. Hmm — the orig is a copy of the unchanged original which exists in git (HEAD) anyway. I'll delete it to avoid leaving clutter; the original is recoverable via git. Let me delete it. Actually, leaving it in .qwen/tmp is harmless and it's the "old" baseline for the recorded contract_diff evidence. But it's cleaner to remove. I'll remove it since git has the original.

Let me delete `.qwen<TMP>.orig.yaml`.

Then do a final `git status --short` to list created/modified files for the report.

Let me run those.

Also I should double check no other accepted files were inadvertently changed. git status will show.

Let me run: rm the tmp file, git status --short, and also `ls changes/sbp-subscriptions`.

Also: should I save a memory? The task instructions include auto memory. Durable knowledge worth remembering: project context (this repo/case). Hmm — "Do not save code patterns, project structure". Project memory: ongoing work not derivable from code. The fact that "spine blocks are Proposed and act after ADR ratification; spine changes must go through changes/<name>/DELTA.md" is a convention derivable from repo (delta_guard). Not needed. 

What about a user/feedback memory? The user is a solution-architect at a bank working with Spine. Could be useful cross-conversation: "User works as solution architect at a bank, uses Spine harness with Qwen Code; expects full Critical-route packages." That's user knowledge. Might be worth saving. But the instruction says avoid negative judgement; role/goals are fine. Given this is a one-shot evaluation-like environment, saving memory may be appropriate. Let me save a concise user memory and a project memory about the ongoing delta (project memory: the sbp-subscriptions delta is proposed awaiting A3 — that's ongoing work not derivable... actually it IS derivable from the files now. So skip project). 

I'll save one user memory: role and working style. Actually, is that valuable/durable? "User — solution-architect at a bank, working in repo 'Платёжный шлюз СБП' with Spine harness via Qwen Code; expects methodology skills (significance, ADR, NFR, fitness, handoff) applied and machine-verified gates." That's reasonable user-scoped memory. Let me save it.

Hmm, but auto memory instructions say memory dirs exist and to write directly. Let me write user memory file + MEMORY.md index. Two files: memories/user/role.md and memories/MEMORY.md.

Given effort, I'll do it briefly.

Let me first cleanup + git status.
All checks green. Cleaning up the scratch baseline and listing the final change set.


Note: `.arch-handoff/mcp-calls.jsonl` untracked — that's the Spine call journal, generated by the tools, not by me directly. Leave it (it's the tool's journal; don't delete). `.qwen/settings.json` was pre-existing modified (not mine). Good — I didn't touch it.

Now, let me save a brief user memory. Actually, let me reconsider — the memory dirs are under a home path in the cell. Writing memory is optional. The guidance says save when learning something worth remembering across conversations. The user's role is clear from the prompt ("Ты — solution-архитектор банка" — that's the persona I'm told to adopt, not necessarily the human user's identity!). Hmm — the prompt says "Ты — solution-архитектор банка" = I should act as the architect. So the human user is likely evaluating/the architect. Saving a user memory about "user is a bank solution architect" might be a wrong inference (it's my role in the scenario). Better not to save a speculative user memory. I'll skip memory to avoid storing a wrong inference. Per "Do not save ... ephemeral task state".

Actually, is there anything durable? Not clearly. I'll skip memory writes. That's the disciplined choice.

Now write the final report. It should:
- Summarize what was delivered against the 7 requested outputs.
- Give verification evidence (machine results).
- List created/modified files.
- Note what remains for the human architect (A3) and open external dependencies.
- Be honest: no code written; contract checks; adversarial findings fixed; route-detector discrepancy.

Let me also mention the files changed list precisely.

Created:
- changes/sbp-subscriptions/DELTA.md
- changes/sbp-subscriptions/IMPACT.md
- changes/sbp-subscriptions/ACCEPTANCE.md
- changes/sbp-subscriptions/A3-PACKAGE.md
- changes/sbp-subscriptions/HANDOFF.md
- docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md
- docs/adr/ADR-009-obratno-sovmestimoe-rasshirenie-kontraktov-podpisok.md
- docs/nfr-sbp-subscriptions.md
- docs/spec/mandate-lifecycle.md

Modified:
- ARCHITECTURE-SPINE.md (AD-009 added; AD-004/AD-008 extended; Deferred/contracts notes)
- .arch-handoff/CONSTRAINTS.yaml (9 rules)
- openapi/tsp-api.yaml (v0.2.0 additive)
- docs/contracts/tsp-api.md (§7)
- docs/contracts/opkc-adapter.md (§9)
- docs/rfp/vendor-rfp.md (scope/G4/§4)
- docs/spec/state-machine.md (§7)
- docs/solutioning.md (§1 roadmap note)

Not touched: .qwen/settings.json (pre-existing), .arch-handoff/mcp-calls.jsonl (tool journal).

Verification: significance_score Critical/11; fitness_check PASS 16/0; delta_guard PASS (spine covered by delta); spine_lint PASS; openapi_lint PASS; contract_diff 0 breaking/4 non-breaking; architect_review PASS.

Also mention: rubric tools unavailable (assets/rubrics missing) — so I didn't run rubric judging; noted honestly. And nfr_check/trace_check SKIP (no model/ dir).

I'll structure the response. Keep it clear but not bloated. Use headings matching the 7 outputs.

Let me write the final answer in Russian (user wrote in Russian).
Готово. Собрал архитектурный пакет изменения поверх принятого решения, не переписывая систему целиком: спайн и реестр правил изменены через дельту (`changes/sbp-subscriptions/DELTA.md`), решения — новыми ADR, контракты — аддитивно.

## Что получилось по вашим 7 пунктам

**1. Значимость и маршрут.** `significance_score` → **Critical, 11/15**. Сработали `new_component`, `new_datastore`, `domain_ownership_change`, `cross_domain_integration`, `api_contract_change`, `data_contract_change`, `security_boundary_change`, `consistency_model_change`, `significant_nfr`, `financial_impact`, `criticality_or_exception`. Причина Critical, а не дельты: движение денег **без активного действия плательщика** на каждый платёж + новый аспект security boundary. План гейтов A0–A5 — в `DELTA.md` §1 и `IMPACT.md`.

**2. Влияние на принятую архитектуру.** `changes/sbp-subscriptions/IMPACT.md` — таблица по AD-001…AD-008: ни один инвариант не ослаблен, **AD-005 подтверждён**, добавлен **AD-009**. Новый компонент — сервис согласий; контракт АБС и trust-зоны не меняются.

**3. Решение.** `docs/adr/ADR-008-…md` (модель согласия + инициация списаний ТСП-driven; альтернативы с причинами отказа; negative-последствия; reversible) и `docs/adr/ADR-009-…md` (обратно совместимое расширение контрактов). Машиночитаемый A3-пакет — `changes/sbp-subscriptions/A3-PACKAGE.md`.

**4. Контракты без поломки потребителей.** `openapi/tsp-api.yaml` → v0.2.0 аддитивно (ресурсы `/v1/mandates…`, опциональные поля, `enum Payment.status` **не** менялся). Проверено машинно: `openapi_lint` PASS, `contract_diff` v0.1.0→v0.2.0 — **breaking 0**, non-breaking 4. Границы: `docs/contracts/tsp-api.md` §7, `docs/contracts/opkc-adapter.md` §9, `docs/rfp/vendor-rfp.md`.

**5. Измеримые NFR.** `docs/nfr-sbp-subscriptions.md`: инициация списания p95 < 500 мс, отзыв → 0 новых списаний ≤ 60 с, «двойное списание за период = 0», пик биллинга 500/1000 TPS, плюс метод проверки на каждую цель.

**6. Критерии приёмки и откат.** `changes/sbp-subscriptions/ACCEPTANCE.md`: EARS-критерии (позитив + негатив: повтор периода, отзыв, лимиты, предуведомление, отказ плательщика, недоступность ОПКЦ, регресс разового приёма), property-тесты с обязательной «нарушающей реализацией», план отката с сигналами и владельцем.

**7. Что оставлено человеку.** `A3-PACKAGE.md`: главный форк — модель инициации (ТСП-driven рекомендована; планировщик и «только НСПК» отвергнуты), экспозиция управления согласиями ТСП, коммерческие лимиты, go/no-go на старт транспорта подписок до документации НСПК. Делегировано ИБ/юристу и закупкам.

## Проверка (машинные свидетельства)

- `fitness_check`: **PASS**, 16 правил, 0 нарушений (9 новых правил трассируют AD-009/ADR-008/009/NFR/контракт).
- `delta_guard`: **PASS** — `ARCHITECTURE-SPINE.md` покрыт активной дельтой `sbp-subscriptions`; `rule_weakened` — без ослаблений.
- `spine_lint`: PASS; `openapi_lint`: PASS; `contract_diff`: 0 breaking.
- `architect_review`: **PASS** (fitness, delta_guard, spine_lint зелёные).
- Не запускались: `trace_check`/`nfr_check` — SKIP (в кейсе нет каталога `model/`); рубрики — недоступны (в окружении нет `assets/rubrics`).

## Состязательный проход (что нашёл и починил)

1. `consentUrl` был в прозе ответа, но отсутствовал в схеме OpenAPI `Mandate` → **добавлен**.
2. Требование предуведомления было без механизма («здесь произойдёт чудо») → сделано проверяемое окно `plannedDebitDate − now ≥ notificationLeadHours`, доставка уведомления отнесена к НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`.
3. Расхождение маршрута: дифф-детектор `architect_review` печатает `Fast` (видит только `api_contract_change`), семантическая оценка — Critical/11 → зафиксировано явно в `IMPACT.md`, чтобы не путало комитет.

## Созданные и изменённые файлы

**Созданы (9):**
- `changes/sbp-subscriptions/{DELTA,IMPACT,ACCEPTANCE,A3-PACKAGE,HANDOFF}.md`
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`
- `docs/adr/ADR-009-obratno-sovmestimoe-rasshirenie-kontraktov-podpisok.md`
- `docs/nfr-sbp-subscriptions.md`
- `docs/spec/mandate-lifecycle.md`

**Изменены (8):**
- `ARCHITECTURE-SPINE.md` (AD-009 добавлен; AD-004/AD-008 расширены; Deferred/версии — через дельту)
- `.arch-handoff/CONSTRAINTS.yaml` (+9 правил)
- `openapi/tsp-api.yaml` (v0.2.0, аддитивно)
- `docs/contracts/tsp-api.md` (§7), `docs/contracts/opkc-adapter.md` (§9), `docs/rfp/vendor-rfp.md`, `docs/spec/state-machine.md` (§7), `docs/solutioning.md` (§1)

Не трогал: `.qwen/settings.json` (изменён до старта) и `.arch-handoff/mcp-calls.jsonl` (журнал инструмента).

Следующий шаг — A3 по `A3-PACKAGE.md`; после ратификации ADR-008/009 дельта переходит в `apply`, а `HANDOFF.md` передаётся исполнителям. Код не писал.
