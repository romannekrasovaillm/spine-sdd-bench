<!-- источник: <HARNESS>/runs-v2/cells/wrpc5sz/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-v2-cells-wrpc5sz-ws/chats/33396bdc-06fd-48dc-9ecf-47ac57971adc.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `run_shell_command(command="find <HARNESS>/runs-v2/cells/wrpc5sz/ws -type f -not -path '*/.git/*' | head , description="List repository files")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/ARCHITECTURE-SPINE.md")`

I'll start by exploring the repository to understand the accepted decision, conventions, and available tooling.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/nfr.md")`

Let me read the key documents: solutioning.md, nfr.md, contracts, state machine, handoff package.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/openapi/tsp-api.yaml")`

Now let's read the ADRs, contracts, state machine, and handoff package.

  `run_shell_command(command="find <HARNESS>/runs-v2/cells/wrpc5sz/ws/.arch-handoff <HOME>/Загрузки/Qw, description="List handoff and qwen files")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/.arch-handoff/ARCHITECTURE.md")`

Now let's look at the .arch-handoff directory, ADRs, and .qwen settings.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/.arch-handoff/connect-manifest.json")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/.arch-handoff/RUBRIC.yaml")`

Let me read the remaining ADRs (especially ADR-007, ADR-006, ADR-003, ADR-004), the handoff TASK.md, MANIFEST.json, connect-manifest.json, RUBRIC.yaml, and .qwen/settings.json.

Important note: the user says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — meaning changes to accepted decision files must be done only in the manner accepted in this repo. This likely means using the delta protocol (delta_guard, OpenSpec delta specs) rather than direct edits to spine/model. Let me check delta_guard's description: "Гейт прямых правок спайна мимо дельты (модель 5.2): каждый изменённый файл под защищёнными путями (по умолчанию model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.ya..."

So the accepted way is delta specs. Let me check if there's an openspec directory or delta protocol. There's no openspec/ dir visible. Let me look more.

Let me read more files.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/adr/ADR-005-integraciya-s-abs-zachisl)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/adr/ADR-004-at-least-once-dlq.md")`

Now let me look at the .qwen/settings.json and check whether Spine MCP tools are usable, and check the ADR-007 (proposed A3) and other ADRs. Also need to figure out "принятый в этом репозитории способ" изменения принятых файлов — this is probably the delta protocol using OpenSpec. Let me check for openspec directory and arch config.

The delta_guard description references protected paths: model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. There's no model/ directory. Let me check.

Let me read remaining ADRs and settings, and check for any openspec/arch config.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/.qwen/settings.json")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/adr/ADR-006-trust.md")`

Now let me read the remaining ADRs (003, 006, 001, 002 full), the .qwen/settings.json, the opkc-adapter.md, vendor-rfp.md, and check for openapi/tsp-api.yaml (which is minimal — note it doesn't reflect docs/contracts/tsp-api.md fully; interesting).

Also I need to understand "принятый в этом репозитории способ" изменения accepted files. There's no `openspec/` directory, no `model/` directory. The delta_guard mentions protected paths. Let me check .qwen/settings.json and whether there's an `arch` config. Also check git log for how previous changes were made (commit "case: исходный кейс", "baseline: условие bmad+spine-hook установлено").

Let me check the .qwen/settings.json and look for hooks.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && arch-be --help 2>&1 | head -80", description="Show arch-be CLI help")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && arch-be gate --help 2>&1 | head -60;, description="Show gate and delta subcommand help")`

Now I understand the repository well. Let me check the "target" of this task: "Архитектурный пакет этого изменения поверх принятого решения". The key phrase: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории."

There's a Stop hook: `arch-be gate --route auto --base bench-baseline`. So after I finish (Stop event), the gate runs. This means whatever I create must pass the gate. Let me investigate the gate and delta protocol. The delta_guard tool mentions protected paths (model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml). So the accepted way to change accepted files is via **delta specs** (OpenSpec delta protocol: propose → apply → archive). Since the repo has no openspec/ dir yet, I may need to create one.

Let me examine the arch-be CLI to understand the gate and delta protocol. Let me look at `arch-be --help`, `arch-be gate --help`, and maybe docs about delta protocol.

Actually, let me be careful: the instructions say don't write code, produce an architecture package. And "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — meaning: to change ARCHITECTURE-SPINE.md / CONSTRAINTS.yaml / docs, use the delta protocol (OpenSpec delta) rather than direct edits, if that's the convention. Or it may mean: the repo convention is that accepted files (ADR-007 Accepted, AD-008 Adopted) can only be changed via a new ADR / delta.

Let me check the arch-be CLI, and also try tools. Let me first run `arch-be --help`.

Also I have Spine MCP tools available. Let me do tool_search for the relevant ones and use them: significance_from_diff / significance_score, delta_guard, spine_lint, fitness_check, rules_suggest, change_impact, trace_check, etc. These are the "methodical skills and tools" the task wants me to use.

Let me plan the deliverables. The user wants an "архитектурный пакет изменения" (architecture change package) containing 7 items. Deliverables likely as files in a delta change directory. Let me discover the accepted repo convention for deltas — check arch-be CLI docs.

Let me run some CLI help commands.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && arch-be delta new --help 2>&1 | head, description="Inspect delta protocol and control commands")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && ls -la; echo \"=== config ===\"; ls , description="Check repo root, local and global arch config")`

The accepted way to modify protected spine files is the delta protocol: `arch-be delta new`, changes/<name>/DELTA.md. Let me read the delta help and current delta list, plus `arch-be control --help`. Also let's check if there's a `changes/` dir or openspec config.

Let me run `arch-be delta list`, `arch-be delta new --help`, and check config.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && echo \"=== control adr ===\"; arch-b, description="Inspect ADR, score, rules, delta validate help")`
  `run_shell_command(command="which arch-be; ls -la $(dirname $(which arch-be)) 2>/dev/null | head; echo \"=== git ===\"; cd <HOME>/Загрузки/Qwen_Code_Spine_OpenSpe, description="Locate arch-be binary and inspect git refs")`

No arch-harness.toml. Config may be embedded in .qwen. Let me check if there's a global config in a different location, or if gate works with defaults. Let me run `arch-be gate --route auto --base bench-baseline` as the hook does, to see the current baseline state. Note: `bench-baseline` may be a git ref. Let me check git branches/tags.

Actually before that, let me understand fully. The task: build an architecture package for the change. The "accepted way to change accepted files" = delta protocol (`arch-be delta new`, `changes/<name>/DELTA.md`), and delta guard requires modified protected files to be mentioned in the active delta.

So the plan:
1. Create a delta via `arch-be delta new subscriptions-recurring-c2b` (or similar).
2. Fill DELTA.md with the change description (ADDED/MODIFIED/REMOVED sections).
3. Create the architecture package documents: significance assessment, impact, ADR (new ADR-008?), contract changes, NFR additions, acceptance criteria + rollback, human-decision items.
4. Modify ARCHITECTURE-SPINE.md (protected) to add AD-009? And CONSTRAINTS.yaml rules? — only via delta (declared in DELTA.md).
5. Update openapi/tsp-api.yaml with additive changes (no breaking).
6. Run `arch-be gate` to verify.

But wait — the user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." This could mean: use the delta protocol. Let me confirm by reading the arch-be docs about delta. Let me look for docs in the arch-be installation, or run `arch-be delta new` in a dry manner. Actually let me check the delta_guard schema via tool_search, and read DELTA template by creating one. But first, let me search for arch-be docs on delta (maybe in a repo alongside). Let me find the arch-be binary location and docs.

Let me also check `arch-be rules --help`, `arch-be control adr --help` (for creating new ADR the accepted way), and `arch-be control score --help` for significance.

Key: the repo convention for new ADRs seems to be `arch-be control adr`. Let me check.

Let me also search for the arch-be source/docs directory.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && arch-be gate --route auto --base ben, description="Run baseline gate to see current state")`

Now I understand the setup:
- `bench-baseline` tag = baseline state.
- Stop hook runs `arch-be gate --route auto --base bench-baseline`. The gate runs on the diff from bench-baseline. So my changes must pass the gate relative to baseline.

Important: gate uses `--route auto` derived from git diff. Since I'll add new component docs and modify contracts/spine, the route will be Critical/Standard. On Standard/Critical, gate checks quantitative NFR and evidence bundles. I need to be careful about what triggers.

Let me first run the gate now (before changes) to see the current state — the baseline should be green.

Then run significance score. Let me also read arch-be's docs on delta protocol — maybe there are docs installed. Let me search the filesystem for arch-be docs / DeltaGuard. Actually, I can create the delta skeleton and see the template.

Let me run the gate at baseline and `arch-be delta new` with a chosen name. Actually before creating, let me look for documentation of the delta's DELTA.md format. Let's create it and read the generated skeleton — that's the fastest. But I should ask? No, creating a delta is a local reversible action.

Let me name it: `sbp-subscription-recurring-c2b`.

Let me run baseline gate first.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && arch-be delta new sbp-recurring-c2b , description="Create delta skeleton for the change")`
  `skill(skill="significance-routing")`

Baseline gate passes, route Fast (no triggers). Note the diff includes `.qwen/settings.json` (1 changed file) — that's the M state.

Now, if I add docs (new ADR, new delta, modify openapi), route auto will derive triggers from git diff. Note: gate uses `--base bench-baseline` and computes diff between baseline and working tree. New untracked files are not seen by git diff unless `git add -N` (the hook does `git add -A -N`). Fine.

Key: The delta_guard checks that modified protected files are mentioned in an active delta. Protected paths default: model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. So if I modify ARCHITECTURE-SPINE.md and .arch-handoff/CONSTRAINTS.yaml, they must be mentioned in changes/<name>/DELTA.md.

Let me now create the delta and read the skeleton. Let me also run `arch-be control score --from-diff` after staging to see derived triggers — but better after I make changes.

Plan of deliverables. The user wants a package "поверх принятого решения", to be taken to architecture decision (A3-like human decision) and then handed to executors. Items 1-7. Files:

1. Delta directory: `changes/sbp-recurring-c2b/DELTA.md` (the change proposal, ADDED/MODIFIED/REMOVED) — required by delta_guard.
2. `docs/solutioning-recurring-c2b.md` — significance assessment + impact + design (или отдельный doc). Actually better: a dedicated change package doc: `docs/changes/sbp-recurring-c2b/solutioning.md`? Let me keep consistent with repo: docs/ holds solutioning.md, nfr.md, contracts/, spec/, adr/, rfp/.

Proposed new files:
- `docs/adr/ADR-008-sbp-subscriptions-recurring-c2b.md` — the architectural decision with alternatives/consequences/reversibility (created via `arch-be control adr`).
- `docs/spec/subscription-machine.md` — recurring subscription state machine + mandate lifecycle (or add to state-machine.md — but that's modifying accepted files; better a new doc + delta MODIFIED mention).
- `docs/solutioning-recurring-c2b.md` — significance, impact on spine, design, rollout/rollback.
- `docs/nfr-recurring-c2b.md` — measurable NFR for new functionality.
- `changes/sbp-recurring-c2b/DELTA.md` — delta spec (ADDED/MODIFIED/REMOVED).
- Modify `openapi/tsp-api.yaml` — additive: subscription endpoints, new webhook event types, new status fields; keep existing consumers working.
- Modify `ARCHITECTURE-SPINE.md` — add AD-009 (or MODIFIED AD-005) binding for recurring debits. This is protected → must be declared in delta.
- Modify `.arch-handoff/CONSTRAINTS.yaml` — add fitness rules for new invariants. Protected → declared in delta.
- Possibly update `docs/nfr.md`? Better not modify accepted file unnecessarily; add new NFR doc referenced. But the user explicitly asks NFR for new functionality — a new file is fine and non-breaking. Yet "влияние на принятую архитектуру" — the delta captures it.
- `docs/rfp/vendor-rfp.md` — probably no change.
- Handoff: maybe a delta-stage handoff package? The repo convention: `.arch-handoff/` is the handoff. The user asks "затем передать исполнителям" — so the package should be ready; maybe add a TASK for the change. But maybe overkill. Let me focus on the 7 items.

Actually, let me reconsider: The user says "Подготовь архитектурный пакет этого изменения поверх принятого решения". The delta protocol is exactly "поверх принятого решения" — change relative to current truth. So the core is the delta change directory with documents.

Let me check what `arch-be delta new` scaffold generates and whether it expects certain files. Let me create it.

Also let me examine what triggers significance score has, to write item 1 properly. Let me run `arch-be control score --help` — done. Need the list of 15 triggers. Let me check the skill `significance-routing` (project skill). Use the Skill tool? The instructions say to use skills when relevant. `significance-routing` is exactly relevant. Also `delta-spec`, `adr-authoring`, `nfr-design`, `fitness-functions`, `adversarial-review`. Let me load the most relevant skills. But loading skills via `skill` tool executes them as prompts in main conversation. Let me use those.

Actually, the task explicitly says: "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." So yes, I should use skills. Let me invoke `significance-routing` first.

Let me also look at the available Spine MCP tools via tool_search to use them properly.

Let me proceed: create delta skeleton + invoke skill significance-routing.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/changes/sbp-recurring-c2b/DELTA.md")`
  `tool_search(query="select:mcp__spine__significance_from_diff,mcp__spine__delta_guard,mcp__spine__change_impact,mcp__spine__spine_lint,mcp__spine__fitness_chec)`

Now let me read the delta skeleton to understand the expected structure.

  `skill(skill="adr-authoring")`
  `skill(skill="nfr-design")`
  `skill(skill="delta-spec")`

Now let me understand the delta route rules: "Critical — полный Solutioning, дельты недостаточно". Since this change is Critical (financial, security boundary, new contract changes), the delta alone isn't sufficient — need full solutioning. Good: the user asks for a full architecture package. So we create a delta (to legally modify protected files) AND full solutioning docs.

Now, the key question about what triggers: Let me determine the significance score for this change. Triggers likely true:
- api_contract_change (yes — TSP API extended)
- data_contract_change (new subscription/mandate data model) — maybe
- new_component? (new subscription/mandate service) — maybe, or extension of existing gateway
- consistency_model_change (new recurring schedule/executions) — arguably
- financial_impact (yes)
- significant_nfr (yes)
- rto_rpo_targets? (existing targets apply)
- criticality_or_exception (payment/CII — likely)
- security_boundary_change? (new consent/mandate storage, possibly new channel) — maybe
- trust_zone_change? maybe not (same zones)
- new_datastore? maybe (mandates table) — could be within existing DB
- cross_domain_integration? maybe (consent registry? new partner ACS)
- new_vendor? no
- domain_ownership_change? no
- irreversible_migration? no

Critical threshold: 5+ or any of security_boundary_change/irreversible_migration/criticality_or_exception. So Critical.

Let me run `arch-be control score` with declared triggers and `--from-diff` to get the mechanical floor. But first I should decide which triggers to declare. Let me consult the significance-routing skill (done) and the spine tool. Let me get the full trigger list and scoring via CLI.

Let me now also load the relevant skills: `adr-authoring`, `nfr-design`, `delta-spec`, `fitness-functions`, `adversarial-review`. Also `spine-invariants`, `handoff-packaging`.

Let me be efficient. Let me invoke skills one at a time (they're prompt expansions). Actually I can call multiple skill tools in parallel? Skills are "executed within main conversation" — probably returns instructions. Let me invoke a couple in parallel: adr-authoring, nfr-design, delta-spec.

Actually, let me first check the ADR template generated by `arch-be control adr` and decide file names. Let me create the ADR.

But careful: `arch-be control adr` creates ./docs/adr/ADR-NNN-... . It might auto-number. Let me test. But first, let's gather the score mechanically.

Let me run: `arch-be control score --from-diff bench-baseline --trigger ...`. But currently the only diff is .qwen/settings.json + new changes/ dir + new untracked DELTA.md. The mechanical detection will not see much until I write files. I'll declare triggers manually.

Let me run the score with declared triggers to see the route.

Triggers to declare true: api_contract_change, data_contract_change, consistency_model_change, financial_impact, significant_nfr, criticality_or_exception, new_component(?), security_boundary_change(?).

Hmm, I should be careful and honest. Let me think about the architecture:

Recurring C2B payments (СБП подписки) — in the real SBP, recurring payments use "СБП-подписки" / автоплатежи, where the payer's bank stores a mandate (согласие) and the merchant initiates periodic charges. Actually the mechanism: "Платежи по подписке" — СБП supports "СБП-автоплатёж" where the ТСП registers a recurring "подписка" with the payer's consent; each period the merchant initiates a debit that the payer's bank authorizes (possibly automatically, or with notification).

Key architecture implications:
1. New entity: **Согласие/мандат (mandate/subscription consent)** — who consented, amount limits, period, validity, revocation. It must be stored and be the single source of truth (analogous to payment SM).
2. New entity: **Подписка (subscription)** and **Периодические списания (executions/charges)** — each charge is a payment-like operation with its own idempotency and status, but tied to the mandate.
3. New states: mandate lifecycle (`DRAFT/ACTIVE/SUSPENDED/REVOKED/EXPIRED`), charge states (reuse payment SM with a new origin).
4. New invariant: recurring debit possible **only** with an ACTIVE mandate and within limits (analogous to AD-005 "credit only from PAID" → "charge only from ACTIVE mandate within limit").
5. Idempotency: each scheduled charge must be idempotent per (mandate, period) — prevents double debits.
6. Consent must be obtained via the payer's bank / НСПК flow; revoke must be honored immediately; revocation propagation.
7. NFR: schedule accuracy, revocation latency, no unauthorized charges.
8. Contract changes: additive endpoints for mandates/subscriptions, new webhook events (`subscription.*`, `charge.*`), new fields. Backward compatible (additive optional fields, new paths).
9. Regulatory: consent per 161-ФЗ/НПС, PДн, dispute handling.
10. Impact on spine: AD-003 (idempotency key now must include subscription period), AD-005 (crediting only from PAID still holds — each charge still goes through PAID), AD-002 (single source of truth extends to mandate), AD-001 (isolation — recurring scheduler is part of gateway core), AD-004 (new notification types), AD-006/007 (consent storage = PДн; new audit).

Alternatives:
- A) Extend existing gateway core with subscription module (mandate + scheduler + charge reuse) — chosen.
- B) Separate microservice «subscription service» with its own DB — more isolation but new consistency boundary, split-brain with payments.
- C) Delegate entirely to НСПК/merchant (merchant-side scheduler; bank only processes payments) — least control, no guarantee, double-charge risk, no revocation single point.
- D) Use ACS (Automatic Clearing System) / (that's for C2C? no). Maybe "ОПКЦ СБП «СБП-подписки» mechanism" vs "acquirer-initiated recurring on card rails". Hmm.

Let me research the actual SBP recurring mechanism to ground the design. But I should rely on repo context; the repo marks НСПК protocol as `[ТРЕБУЕТ ПРОВЕРКИ]`. I'll mark protocol specifics as pending.

Let me check kb_search for relevant knowledge (Spine knowledge base). Also skill_search for "recurring"/"subscription"/"mandate". Let me try.

Actually, let me be pragmatic and efficient. Let me:
1. Load skills: adr-authoring, nfr-design, delta-spec (in parallel).
2. Query kb_search for SBP subscriptions.
3. Determine significance score.

Let me do these.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && arch-be gate --route critical --base, description="Probe gate requirements on critical route")`
  `tool_call(name="mcp__spine__kb_search", arguments={"query": "рекуррентные платежи подписки СБП согласие плательщика мандат", "limit": 8})`
  `tool_call(name="mcp__spine__skill_search", arguments={"query": "subscription recurring mandate consent"})`

Now let me determine significance and query knowledge base for SBP recurring/subscriptions. Let me also check the Spirit MCP tools list for kb_search, skill_search.

Let me run kb_search for "подписк" / "рекуррент" / "автоплатёж" and skill_search "subscription".

Let me use tool_call for kb_search and skill_search. And run significance score CLI.

For significance: let me declare triggers. I'll run `arch-be control score` with triggers. Let me determine which:

- new_component: The subscription/mandate module — is it a new component? It extends the gateway core. If I design a "Subscription & Mandate Service" as a new container, then yes. But architecture-wise, better to keep within gateway core (AD-001 isolation). Hmm. Actually adding a new logical component inside the payment contour (scheduler + mandate store). I'd say `new_component=true` is arguable. Let me think about what's honest: we add a new module, not a new deployable necessarily. But significance detector from diff counts new code roots/components. I'll declare true if I add a new component to the C4 container diagram. I plan to add "Подписки/мандаты" module — a new logical component. I'll declare `new_component=true`.

- new_datastore: mandates/subscriptions stored in the same gateway DB (extend schema). Not a new datastore. Declare false? But there may be a scheduler store. I'll say false (same БД шлюза) — but adding a new table is not a new datastore. Hmm, but be conservative: the anti-bypass detector may flag new migrations. I'll declare false and note.

Actually, let me be careful: the score route matters for gate. If route becomes Critical, gate on Critical may require evidence bundles and quantitative NFR — which could make the gate FAIL unless I produce evidence. Let me check what gate does on Critical: "на маршрутах Standard/Critical — количественные NFR и проверка evidence-бандлов". So if my diff triggers Critical, the Stop hook gate will require quantitative NFR + evidence bundle. That could be hard to satisfy. But the task explicitly is a Critical-class change, and the existing case is Critical. Hmm — but the baseline gate reported Fast because no diff.

Wait, but the change is docs-only (no code). The auto-route from diff detects triggers like new_component based on new source dirs? It might detect `api_contract_change` from openapi/tsp-api.yaml changes, and `new_vendor`? Let me check what the detectors look for. Let me just run significance_from_diff after staging to see.

Actually, the important thing: I must produce a package that passes the gate. Let me first understand gate requirements on Standard/Critical. Let me check `arch-be gate` with `--route critical` now to see what it demands (on current diff). That will show me the required evidence. Let me run it (read-only, doesn't change state).

Let me run:
1. `arch-be gate --route critical --base bench-baseline` (to see requirements)
2. kb_search / skill_search for subscriptions.

Let me do that.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && echo \"=== STANDARD ===\"; arch-be g, description="Probe standard route gate and sensors help")`

Important findings:
1. On Critical route, the gate fails because `docs/spec/state-machine.md` lacks required sections: `## Проблема`, `## Критерии приёмки`, `## Риски`. This is a pre-existing failure (sensors required_sections) — not caused by my change, but the hook runs `--route auto`, so if auto resolves to Critical, the Stop hook will fail. Wait — the spec-drift sensor checks existing spec files regardless of diff. At baseline Fast route it's not checked. If my change makes auto-route Critical, then sensors run and fail on state-machine.md.

Hmm, but wait: will auto route become Critical? `--route auto` derives from git diff triggers. My changes: modify `openapi/tsp-api.yaml` (api_contract_change → true, detected), add new ADR/docs, modify spine (not a trigger by itself), add CONSTRAINTS rules. Possibly `financial_impact`, `significant_nfr`, `criticality_or_exception` are "declared" only — auto can't detect them from diff. Let me check the actual detector list for diff: description says detectors new_component / new_vendor / api_contract_change / irreversible_migration / new_datastore. So auto-route will detect api_contract_change at minimum (touching openapi/ dir). Score 1-2 → Standard? Let me check thresholds: Fast 0–1, Standard 2–4, Critical 5+. api_contract_change alone = 1 → Fast. Plus new_component if I add new code root dirs (docs don't count). Plus new_datastore if I add migrations. So auto-route likely Standard (2-4) if api_contract_change + new_component detected.

On Standard route, gate checks? Let me probe `--route standard` to see requirements. Standard requires quantitative NFR (nfr) and evidence? The description: "на маршрутах Standard/Critical — количественные NFR и проверка evidence-бандлов". But nfr SKIPs without model/. evidence_verify SKIPs without EVIDENCE.yaml.

Let me probe standard route.

Also, I could optionally fix the state-machine.md required sections — but that's modifying an accepted file and would be a scope expansion; however it's needed if route goes Critical. Better: keep auto-route at Standard by not tripping 5+ triggers, OR fix the spec file (which is legitimately part of a delta). Hmm. Actually, the task is a Critical-class change; the honest route is Critical. But the gate then demands model/ absent → trace_check/nfr/model_validate SKIP (counted as "не проверено (обязательно для маршрута Critical)") and evidence_verify SKIP + sensors FAIL. Exit 1 anyway due to sensors.

Wait: "Не проверено (обязательно для маршрута Critical): trace_check, nfr, model_validate, evidence_verify" — these are SKIPs, but the exit was FAIL only because of sensors. The hook requires exit 0. So if my change routes Critical, I must:
- Fix sensors (add required sections to state-machine.md — but that's the existing spec; adding ## Проблема/## Критерии приёмки/## Риски to it is within scope of the change package? It's an accepted file, so must be declared in delta).
- Provide EVIDENCE.yaml for the change? evidence_verify SKIP means it's not failing, just not checked. Actually it SKIPs → not a failure. So maybe acceptable.

Hmm, but wait: would the sensors fail even at Standard? Let me probe standard.

Let me also consider: should I create a `model/` directory? That would enable trace_check etc. The repo has no model/. Creating a full typed model is substantial. The task says "Код не пиши" — model is YAML entity cards, not code. Hmm, but that might be over-engineering. However the accepted repo style already has docs. Let me not create model/ unless needed.

Let me probe standard route and also check sensors help to understand which files it scans.

Also important: `docs/spec/state-machine.md` required sections — the sensor checks docs/spec/*. Let me see `arch-be control sensors --help`.

Let me run these probes.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && git add -A -N >/dev/null 2>&1; echo , description="Compute significance from diff and sensors detail")`

So even Standard route fails on sensors because `docs/spec/state-machine.md` lacks the required sections. This is a pre-existing red finding that the Stop hook would catch at Standard/Critical. Since the hook runs `--route auto`, and my change will likely route Standard (api_contract_change + maybe new_component), the hook will FAIL unless I fix the sensors.

So part of my package must include fixing `docs/spec/state-machine.md` to have `## Проблема`, `## Критерии приёмки`, `## Риски` sections (declared in the delta). Actually — the sensor probably requires these sections in each spec file. Let me check which files it scanned: "сенсоров прогнано: 2" — likely docs/spec/state-machine.md and maybe openapi? Let's see: it found 1 failed of 2. The other spec (docs/contracts?) — hmm. required_sections likely configured for `docs/spec/*.md`. There's only one file in docs/spec/.

Wait "сенсоров прогнано: 2" — maybe required-sections + upstream-coverage. Or 2 files. Let me check by running `arch-be control sensors docs/spec` to see details.

Let me run that. Also let me determine the auto route by staging changes at the end.

Given the gate constraints, my plan must ensure:
1. delta_guard PASS: protected modified files mentioned in changes/sbp-recurring-c2b/DELTA.md.
2. rule_weakened PASS: don't weaken CONSTRAINTS rules relative to baseline (adding rules is fine).
3. spine_lint PASS: new AD-009 must have Binds/Prevents/Rule, no TODO/TBD, no dup IDs, no dangling refs.
4. sensors PASS: docs/spec/*.md must contain `## Проблема`, `## Критерии приёмки`, `## Риски`. So I need to add these sections to state-machine.md (and any new spec file I add must contain them too).
5. fitness PASS: don't violate rules; new rules must not have placeholders etc.
6. nfr SKIP (no model/) — fine.
7. evidence_verify SKIP (no EVIDENCE.yaml) — fine.

Also I should check `rule_weakened` semantics: if I modify CONSTRAINTS.yaml, ensure no rule is weakened. Adding rules is fine. But note: `adr-no-placeholders` rule uses must_not_contain glob "docs/adr/*.md" pattern '<!--'. So new ADR must not contain `<!--`. Fine.

Also `spine-lints-clean` warn: no TODO/TBD/XXX in ARCHITECTURE-SPINE.md. I must avoid TODO/TBD. Careful: my new AD-009 text must not contain "TODO|TBD|XXX". Note spine_lint checks for "заглушки (TODO/TBD)". So avoid those tokens.

Also note `adr-set-complete` requires docs/adr/ADR-001-outbox.md exists — it does.

Now, let me also check: does the Stop hook `git add -A -N` then gate `--base bench-baseline`. Yes. So all my files will be included.

Now let me determine the auto-route. Let me check `arch-be control score --from-diff bench-baseline` after creating files. But I can pre-check now with current diff (baseline + changes/ untracked + .qwen). Let me run it.

Actually the git diff for untracked files requires add -N. Let me just run `git add -A -N` then `arch-be control score --from-diff bench-baseline`. Let me do that.

Wait — `git add -A -N` marks untracked files as intent-to-add. That's what the hook does. It's safe/reversible. Let me run it and then score.

Let me also run `arch-be control sensors docs/spec`.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && arch-be control adr \"Рекуррентные C, description="Generate ADR-008 scaffold")`
  `tool_call(name="mcp__spine__openapi_lint", arguments={"path": "<HARNESS>/runs-v2/cells/wrpc5sz/ws/openapi/tsp-api.yaml"})`

Interesting: currently score from diff = 0. The detectors didn't fire (no openapi change yet, no new code root). So auto-route is Fast right now. When I modify openapi/tsp-api.yaml, `api_contract_change` should fire. Let me verify later.

Sensors scan docs/spec/*.md, requiring sections `## Проблема`, `## Критерии приёмки`, `## Риски`. So state-machine.md needs those sections. Since the sensor runs at Standard/Critical only, and my change likely triggers Standard at least (api_contract_change), I must fix state-machine.md.

Hmm, but will api_contract_change alone give score 1 → Fast (0–1)? Then sensors won't run and no need. But adding new openapi paths + new ADR... new_component detector might fire if new code roots. Let me just be safe and fix state-machine.md anyway (it's a legit improvement and part of the delta, keeps gate green under any route). Also any new spec file I add under docs/spec/ must have those 3 sections.

Actually wait — would adding a new file `docs/spec/subscription-machine.md` without those sections cause sensor failure? Yes, if route Standard/Critical. So include the 3 required sections in any new spec, or place spec content elsewhere (e.g., docs/ not docs/spec). Let me place the subscription state machine in `docs/spec/subscription-lifecycle.md` and include the required sections.

Now let me plan the whole package concretely.

### Deliverables plan

**A. Delta (the accepted mechanism to change accepted files)**
- `changes/sbp-recurring-c2b/DELTA.md` — delta spec: Проблема, ADDED (EARS), MODIFIED, REMOVED, План отката, Критерии приёмки. Declares protected file modifications (ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml) so delta_guard passes.

**B. Significance & impact**
- `docs/changes/sbp-recurring-c2b/solutioning.md`? Hmm. Better keep flat-ish consistent with docs. Let me create:
  - `docs/solutioning-recurring-c2b.md` — significance assessment (triggers, route), impact on accepted architecture (invariants touched, what changes/doesn't), design (components, flows, state machines), alternatives, rollout/rollback, open questions, human-decision items. This covers items 1,2,6,7 plus design.
  - Actually item 3 (architectural decision with alternatives/consequences/reversibility) belongs in an ADR. Create `docs/adr/ADR-008-...md`.

Let me structure:

1. `changes/sbp-recurring-c2b/DELTA.md` — delta (item 1 route + items 2,6 criteria), declares protected edits.
2. `docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya.md` — item 3 (decision, alternatives, consequences, reversibility). Maybe also ADR-009? Could be one ADR. But there might be two decisions: (a) recurring architecture (mandate + scheduler inside gateway core, reuse payment SM), (b) consent/mandate retrieval mechanism via НСПК vs bank-owned. Let me keep to one primary ADR-008 with the core decision, and capture the consent-source sub-decision as an alternative/open question. Hmm, adr-authoring says one decision per ADR. The recurring design is one coherent decision. I'll do ADR-008 for architecture of recurring; and maybe ADR-009 for "источник согласия (мандат): НСПК-центричный vs банк-центричный". Actually that's an important fork. Let me include ADR-009 as a second decision if warranted.

Actually simpler and cleaner: 
- ADR-008 "Рекуррентные C2B-списания: мандат плательщика как единый источник истины и планировщик списаний в ядре шлюза" — covers topology + consistency.
- ADR-009 "Получение и отзыв согласия плательщика (мандата): схема с подтверждением в банке плательщика" — covers the consent acquisition/revocation mechanism.

Hmm, but ADR-009 depends on НСПК protocol which is `[ТРЕБУЕТ ПРОВЕРКИ]`. I can still write it as Proposed with the mechanism choices and mark protocol specifics pending. Or fold into ADR-008. The repo has ADR-001..007 each a distinct concern. Two ADRs is reasonable. But scope creep risk. Let me decide: the core change is one decision; the consent mechanism is intrinsic to it. I'll write one ADR-008 with the full decision (mandate-first, scheduler in core, reuse payment SM), and note the consent-acquisition channel as a bounded constraint/open item (since it's external-input-dependent). That keeps it focused and honest. Actually alternatives must cover consent acquisition anyway.

Hmm, but then item 7 "что остаётся на решение человека-архитектора" — the consent-acquisition mechanism and commercial/limit policy are human decisions. Good.

Let me go with **ADR-008** (single) + **ADR-009** only if needed. I'll write ADR-008 comprehensive but ≤1 page-ish per adr-authoring (>1 page → split). Let me maybe split into two: ADR-008 mandate/consistency, ADR-009 scheduler+contract? Hmm. The adr rule: "ADR-эпос >1 страницы — разбить". I'll aim for concise ADR-008 covering the recurring model; and ADR-009 for "Идемпотентность периодических списаний и защита от двойного списания" — that's a distinct decision with alternatives. Actually that's naturally part of ADR-008's decision.

Let me do two ADRs:
- **ADR-008**: Рекуррентные C2B-списания: мандат плательщика и планировщик в ядре шлюза (topology/consistency/state model).
- **ADR-009**: Согласие (мандат) плательщика: получение, хранение, отзыв и запрет списаний без действующего мандата (security/consent/regulatory decision).

That maps nicely to "затронутые инварианты" and gives two alternatives sets.

3. `docs/solutioning-recurring-c2b.md` — significance + impact + design + NFR summary + acceptance + rollback + human decisions. (item 1,2,6,7)
4. `docs/nfr-recurring-c2b.md` — item 5 measurable NFR.
5. `docs/spec/subscription-lifecycle.md` — mandate & charge state machine (new spec; include `## Проблема`, `## Критерии приёмки`, `## Риски` sections to satisfy sensor).
6. `docs/contracts/tsp-api-recurring-c2b.md` — contract changes description + compatibility analysis (item 4).
7. `openapi/tsp-api.yaml` — additive changes (item 4).
8. `ARCHITECTURE-SPINE.md` — add AD-009 (recurring debits only with active mandate and within limits; idempotency per period), maybe modify AD-003 to extend. Declare in delta.
9. `.arch-handoff/CONSTRAINTS.yaml` — add fitness rules for new invariants. Declare in delta.
10. Fix `docs/spec/state-machine.md` — add required sections (Проблема/Критерии приёмки/Риски) + mark recurring extension. Declare in delta.
11. Maybe `docs/rfp/vendor-rfp.md` — no change needed? The recurring flow may need НСПК support; the RFP for transport should mention recurring ops. Hmm, opkc-adapter contract would need new methods (`createSubscription`, `getMandateStatus`, `revokeMandate`, events `mandate.*`, `charge.*`). So `docs/contracts/opkc-adapter.md` should be extended. That's an accepted file — declare in delta. But is it needed for the package? Yes, since core↔transport boundary must support recurring. I'll extend it additively.

That's a lot of files. It's a Critical change package, so reasonable. But I must be careful about time/effort and correctness. Let me scope sensibly: the user asked for 7 specific outcomes; files should serve them. Let me not over-produce. I'll produce:

- `changes/sbp-recurring-c2b/DELTA.md` (delta; declares protected edits)
- `docs/adr/ADR-008-...md`
- `docs/adr/ADR-009-...md`
- `docs/solutioning-recurring-c2b.md` (items 1,2,6,7 + design + impact)
- `docs/nfr-recurring-c2b.md` (item 5)
- `docs/spec/subscription-lifecycle.md` (state machine for mandate/charge; supports design)
- `docs/contracts/tsp-api-recurring-c2b.md` (item 4: contract changes + compatibility)
- `openapi/tsp-api.yaml` (item 4: additive)
- `ARCHITECTURE-SPINE.md` (MODIFIED: AD-003 extension + AD-009 new)
- `.arch-handoff/CONSTRAINTS.yaml` (MODIFIED: new fitness rules)
- `docs/spec/state-machine.md` (MODIFIED: required sections + pointer)
- `docs/contracts/opkc-adapter.md` (MODIFIED: recurring methods/events)

Hmm, that's 12 files. Might be OK but let me consider whether modifying opkc-adapter.md and state-machine.md is needed. The sensor requires state-machine.md fix if route Standard/Critical. Contract boundary (opkc-adapter) is genuinely needed for the change to be implementable — but the user's item 4 focuses on `openapi/tsp-api.yaml`. I'll include opkc-adapter extension because the recurring flow requires НСПК operations (mandate registration/charge) — otherwise the package is incomplete. But to limit scope, I could describe the required adapter contract changes inside the solutioning doc and the delta. Hmm.

Given "Не пиши код" and "передать исполнителям", the package should be complete. I'll extend opkc-adapter.md additively but concisely.

Actually, let me reconsider: maybe I'm overcomplicating. The essential deliverables per the user:
1. Significance/routing → solutioning doc section + delta route.
2. Impact on architecture → solutioning doc section + spine changes.
3. Architectural decision w/ alternatives/consequences/reversibility → ADR-008 (and ADR-009).
4. Contract changes in openapi/tsp-api.yaml without breaking → edit yaml + contract doc.
5. Measurable NFR → nfr doc.
6. Acceptance criteria + rollback → delta + solutioning.
7. Human-architect decisions → solutioning section + ADR-009 status Proposed.

So required files: delta, solutioning, ADR(s), nfr, contract doc, openapi yaml, spine, constraints, state-machine fix. opkc-adapter extension optional — I'll include as a MODIFIED section in the delta and a short subsection in the solutioning doc rather than rewriting the whole file. Hmm, but delta_guard only checks protected paths (model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml). docs/ files are not protected. So I don't strictly need the delta to mention docs edits, but the delta should still describe MODIFIED requirements. Good.

Let me be decisive and produce a focused, high-quality package:

Files to create:
1. `changes/sbp-recurring-c2b/DELTA.md`
2. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-mandat-platelshchika-i-planirovshchik.md`
3. `docs/adr/ADR-009-soglasie-mandat-platelshchika-poluchenie-otzyv-i-zapret-spisaniy.md`
4. `docs/solutioning-recurring-c2b.md`
5. `docs/nfr-recurring-c2b.md`
6. `docs/spec/subscription-lifecycle.md`
7. `docs/contracts/tsp-api-recurring-c2b.md`

Files to modify:
8. `openapi/tsp-api.yaml`
9. `ARCHITECTURE-SPINE.md`
10. `.arch-handoff/CONSTRAINTS.yaml`
11. `docs/spec/state-machine.md`
12. `docs/contracts/opkc-adapter.md` (add recurring ops) — I'll decide after writing core.

Also maybe `.arch-handoff/ARCHITECTURE.md` (epic-context) is stale/regenerated by handoff — I won't touch it (it's a generated snapshot).

Let me now create the ADR files using `arch-be control adr`. Let me test it: `arch-be control adr "Рекуррентные C2B-списания..."`. It generates ADR-NNN. Let me run it.

But first, let me think through the actual architecture design in depth so the docs are coherent and correct. This is the crux.

## Domain: СБП подписки (recurring C2B)

Business: ТСП (online cinemas, ЖКХ, telecom) want recurring debits with payer consent, without QR/action each time.

Mechanism (real НСПК СБП): There is "СБП-подписка"/"Автоплатёж" — the payer gives consent (in their bank app) to a merchant for recurring debits; the merchant/acquirer initiates charges. In SBP, the mechanism (as of ~2023-2024) is "Платежи по подписке" / "СБП Автоплатёж": ТСП registers a "подписка" (mandate) linking payer's phone/account token; each charge is initiated by the acquirer and confirmed by the payer's bank, either automatically within the mandate terms or with a push notification.

However — precise protocol is `[ТРЕБУЕТ ПРОВЕРКИ]`. I'll design the logical model and mark protocol dependencies.

Key architectural elements:

### Entities
- **Mandate (Согласие/Подписка)** — the payer's authorization to debit. Fields: mandateId, tspId, payerRef (tokenized, no raw PII), payerBankRef, maxAmountPerCharge, maxAmountPerPeriod, period (month/week/custom), currency, validFrom, validTo, status, receivedAt, revokedAt, consentRef (НСПК consent id / document ref), version.
- **Charge (Периодическое списание)** — an actual debit attempt under a mandate; it's a payment-like operation. Fields: chargeId, mandateId, periodKey (e.g. 2026-09), amount, paymentId (link to existing payment SM), scheduledAt, initiatedAt, status.
- **Schedule / mandate period plan** — derived from mandate.

### State machines
Mandate: `CREATED → PENDING_CONSENT → ACTIVE → (SUSPENDED) → REVOKED / EXPIRED`. Plus `REJECTED`, `PENDING_OPKC`.
Charge: reuse payment SM (CREATED→QR_ISSUED? no QR) — Hmm. For recurring, there is no QR. The payment SM starts at CREATED → QR_ISSUED. For a recurring charge, the "QR_ISSUED" equivalent is "charge registered at НСПК awaiting payer bank authorization" → we can map to `QR_ISSUED` semantic = "presented to payer/payer bank". Better to introduce a distinct representation: origin=RECURRING and state names? The existing SM is the accepted truth. Options:
- (a) Reuse payment SM unchanged, with `qrType=recurring` and QR_ISSUED meaning "charge presented". This preserves AD-005 (credit only from PAID) and AD-002/AD-003, minimizing change. But it distorts naming (no QR).
- (b) Extend the SM with a new state `AWAITING_AUTH` for recurring charges, i.e., CREATED → AWAITING_AUTH → PAID → CREDITED → COMPLETED. This modifies the accepted status machine (ADR-002) → needs a superseding/modifying decision. That's a real architecture change and should be declared as MODIFIED.
- (c) Keep payment SM for the money movement and model charge as a separate operation type with its own lifecycle, where the charge triggers a payment.

I think the cleanest: **the charge IS a payment** with `origin=RECURRING` and `mandateId`, reusing the payment SM; the pre-payment state `QR_ISSUED` is generalized to `PRESENTED` / keep `QR_ISSUED` for compatibility but add alias. Hmm — changing state names breaks consumers. Since openapi status enum includes QR_ISSUED and consumers may depend on it, I should NOT rename. Add a new state `AWAITING_CONFIRMATION`? That would require modifying the enum (additive — new enum value is backward compatible for consumers? Adding a value to an enum is technically a breaking change for strict clients, but generally additive). Docs say "Добавление опциональных полей — обратно совместимо". Adding enum values is riskier. 

Alternative: keep `QR_ISSUED` as the state after the charge is presented (document it as "presented to payer; for recurring charges — awaiting payer bank authorization"). No enum change. That's the least breaking. But semantically muddy; document mapping in the recurring spec.

Hmm, but AD-002 said "Канонические состояния ... плюс терминальные FAILED, EXPIRED, REVERSED, REFUNDED. Промежуточные технические состояния (NOTIFY_SENT, ABS_IN_PROGRESS) допустимы как подсостояния." So adding a sub-state is allowed without changing the canonical set. Great — I can model recurring charge as: create payment in `CREATED`, then transition to `QR_ISSUED` (generalized "presented to payer"), then PAID etc. Or introduce sub-state `CHARGE_PRESENTED`. I'll go with: reuse canonical states; `QR_ISSUED` means "предъявлено плательщику/банку плательщика" for recurring origin; document as MODIFIED (widening the meaning). That's a MODIFIED requirement — worth declaring (semantic widening, no contract break). Good.

Actually, to be cleaner and preserve backward compat while being explicit, I'll add a **new optional field `origin`** (`qr | link | recurring`) and `mandateId`, and document that for `origin=recurring` the payment skips QR generation and `qrId/qrUrl` are absent while `qrImage` absent. `QR_ISSUED` then means "зарегистрировано в ОПКЦ, ожидает подтверждения". Good.

### New invariant (spine AD-009)
"Списание по подписке возможно только при действующем (ACTIVE, не отозванном, не истёкшем) мандате плательщика и в пределах лимитов мандата; каждое списание идемпотентно по (mandateId, periodKey)." Analogous to AD-005.

Also modify AD-003 to include `(mandateId, periodKey)` idempotency key for recurring charges, and mandate `consentId` idempotency.

### Consistency & no double debit
- Scheduler selects due mandates; for each, creates a charge with a deterministic idempotency key = hash(mandateId, periodKey). Unique constraint prevents duplicates even with scheduler retries/multi-instance.
- Charge proceeds through payment SM; crediting only from PAID (AD-005 holds).
- Revocation: when mandate revoked, immediately stop new charges (guard) and handle in-flight charges per policy (release/void or complete?). Regulatory: revocation must prevent further charges; in-flight charge not yet PAID must be cancelled.
- Mandate status is authoritative; charges check ACTIVE at initiation AND at PAID processing? At least at initiation.

### Reuse vs new component
Chosen: mandate store + scheduler as a new **module inside the payment contour** of the gateway (same DB, same outbox, same audit), because:
- AD-001 isolation already gives the right home.
- AD-002 single source of truth: mandate + charge in same transactional boundary → atomic "charge created + outbox" (no distributed consistency).
- Avoid split-brain between subscription service and payment SM.
Alternative: separate service (microservice) — rejected (new consistency boundary, need saga between subscription and payment; higher risk).
Alternative: merchant-side scheduling (bank provides only "charge by mandate" API) — rejected (bank can't guarantee no double charge, revocation semantics across many merchants, weaker audit).
Alternative: full vendor (НСПК подписки as vendor module) — rejected for core logic; but the НСПК mandate registration goes via the existing ОПКЦ adapter (vendor transport).

### Consent acquisition
The mandate originates from the payer's consent obtained through the payer's bank (СБП flow): user confirms in their bank app. So the bank-acquirer registers a "subscription/mandate request" via ОПКЦ; the payer's bank collects consent; НСПК notifies the acquirer of the confirmed mandate with a `mandateId`. The acquirer stores `consentRef`. This mechanism lives in the ОПКЦ adapter (transport), core gets normalized events.

Human decision: exact consent acquisition flow (which channel: НСПК-центрично vs bank-центрично) and limits policy / tariffs.

### Regulatory
- 161-ФЗ / НПС: authorization must be documented; mandates stored; revocation honored.
- 152-ФЗ: payer PII minimized, tokenized.
- 115-ФЗ: AML thresholds.
- Disputes (chargebacks) — deferred? Currently disputes are Deferred in spine. Recurring increases dispute risk. Note as open/risk.

### NFR additions (measurable)
- Scheduler: charge initiation lag from scheduledAt: p95 ≤ 5 min, p99 ≤ 15 min.
- Scheduler correctness: 100% of due charges created exactly once (no missed, no duplicate); duplicate charges = 0.
- Revocation: new charges after revocation = 0; revocation propagation to effective stop ≤ 60 s.
- Mandate status query latency p95 < 300 ms.
- Consent confirmation → ACTIVE: p95 ≤ 60 s (protocol-dependent).
- Throughput: recurring charges add up to X TPS; total must stay within existing 200/500 TPS budget — define share, e.g., recurring ≤ 100 TPS sustained, 300 peak.
- Availability of scheduler: ≥ 99,95%; missed schedule catch-up ≤ 1 h.
- Audit: 100% mandate lifecycle events + charges in immutable log.
- Data locality, RPO=0 for mandates as for payments.

### Contract changes (additive, backward compatible)
New endpoints (versioned under /v1, additive):
- `POST /v1/mandates` — ТСП initiates mandate (subscription consent) request for a payer. Returns mandateId, status PENDING_CONSENT, consentUrl? (deep link / QR for payer).
- `GET /v1/mandates/{mandateId}` — status.
- `POST /v1/mandates/{mandateId}/revoke` — merchant-initiated revocation (or only payer? Usually payer revokes in bank; merchant can cancel subscription). Add `cancel`.
- `GET /v1/mandates?tspId=&status=&payerRef=` — list.
- `POST /v1/mandates/{mandateId}/charges` — initiate an immediate/ad-hoc charge under mandate (for merchant push charges) — idempotent by mandate+period or client key.
- `GET /v1/mandates/{mandateId}/charges` and `GET /v1/charges/{chargeId}` — charge status (or reuse /v1/payments/{paymentId}).
- New webhook events: `mandate.activated`, `mandate.rejected`, `mandate.revoked`, `mandate.expired`, `charge.completed` (or reuse payment.completed with mandateId), `charge.failed`.

Compatibility: existing endpoints unchanged; `Payment` schema gains optional `mandateId`, `origin`, `periodKey`; `PaymentRequest` gains optional `mandateId`, `origin`, `periodKey`; new optional `mandate` object. All optional → backward compatible. New paths don't break. Do NOT remove/rename existing fields. Do NOT change enum values. Existing consumers (merchant) unaffected.

`openapi/tsp-api.yaml` currently is minimal (only createPayment + getPayment). I'll extend it additively: add mandate paths/schemas, add optional fields to Payment/PaymentRequest, add refunds path maybe. Keep existing structure. Also bump info.version? The doc says "Добавление опциональных полей — обратно совместимо, не требует новой версии". But bumping the minor version 0.1.0 → 0.2.0 signals additive change. `contract_diff` tool checks CD-007: breaking diff without major version change. Additive with minor bump is fine. I'll set version 0.2.0.

Wait — changing `info.version` from 0.1.0 to 0.2.0 is a non-breaking version change. Good. And `openapi_lint` checks versioning/idempotency/RFC7807. The current yaml is minimal and may already fail lint? Baseline gate fitness passed, but openapi_lint wasn't run in gate. Let me run openapi_lint on current file to know the baseline, then on modified. Also note: mutating endpoints need Idempotency-Key and RFC 7807 errors. My new POST endpoints must declare Idempotency-Key and error responses. I should improve the yaml to satisfy lint: add error responses (RFC 7807 component), idempotency.

Let me check `openapi_lint` on current file.

### Acceptance criteria
- Mandate cannot be created without НСПК confirmation; status transitions per spec.
- Charge only from ACTIVE mandate within limits; else rejected (no debit).
- Duplicate charge attempts (same mandate+period) → single debit.
- Revocation → zero subsequent charges; in-flight not-yet-PAID cancelled.
- Webhook events delivered idempotently.
- Regulatory: audit log complete.
- Contract: existing v0.1 consumers still work (contract_diff no breaking).
- Rollback: feature flag per-ТСП; stop scheduler; revocation all test mandates; no data migration needed (recurring is additive). Rollback trigger: any unauthorized debit, duplicate debit, or revocation not honored.

### Human architect decisions (item 7)
- Consent acquisition channel/regulatory interpretation (НСПК support for recurring in C2B; exact flow) — external input + compliance.
- Limits/tariff policy and periodic charge rules (commercial).
- Whether in-flight charges at revocation are cancelled or completed (commercial/regulatory).
- Whether recurring is a separate initiative-level capability requiring parent spine change (parent spine "Подключение банка к СБП (эквайринг C2B)" — recurring may be a new feature under it; escalation).
- Dispute/chargeback handling for recurring (currently deferred) — must be re-scoped.
- Route: Critical → A3 required.

Now, the parent spine note: "Родительский spine: initiative «Подключение банка к СБП (эквайринг C2B)». Данный spine — уровень feature." Recurring подписки could be a new feature under the same initiative, or a child spine. The change affects the feature spine → this is a change to the accepted spine → delta + escalation to parent? Since no parent spine file present, note escalation.

Now let me think about the delta_guard protected paths. Default protected: `model/`, `ARCHITECTURE-SPINE.md`, `CONSTRAINTS.yaml`. My modifications to ARCHITECTURE-SPINE.md and .arch-handoff/CONSTRAINTS.yaml must be "mentioned" in DELTA.md. The guard checks mentions — probably by filename substring in DELTA.md. Let me verify with the tool after editing. I'll mention exact paths.

Hmm — the default protected path is "CONSTRAINTS.yaml" (not ".arch-handoff/CONSTRAINTS.yaml"). The changed file is `.arch-handoff/CONSTRAINTS.yaml`. The guard likely matches basename or suffix. I'll mention both `CONSTRAINTS.yaml` and the full path to be safe.

Now, let's also verify `rule_weakened`: compares rule set to baseline; adding rules is fine, but if I modify the spine-lints-clean regex etc., could be seen as weakening. I'll only ADD rules.

Also careful: `adr-no-placeholders` must_not_contain glob "docs/adr/*.md" pattern '<!--'. My new ADRs must not contain `<!--`. And existing ADRs don't. Good. Also note the generated ADR template from `arch-be control adr` might include `<!-- -->` HTML comments! Let me check and remove them if so.

Let me now start creating. First, run `arch-be control adr` for the two ADRs to get proper numbering/template. Let me try one.

Actually, let me check openapi_lint baseline and openapi-lint behavior now, and create first ADR.

Let me also verify `arch-be control adr` output.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisaniy)`

Let me read the generated ADR-008 template.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && arch-be control adr \"Согласие плате, description="Generate ADR-009 scaffold")`
  `skill(skill="fitness-functions")`

The template contains `<!-- ... -->` which would violate the `adr-no-placeholders` rule (must_not_contain '<!--'). So I must fill/remove all HTML comments. Good to know.

Now let me generate ADR-009 too, then write content.

Let me generate ADR-009.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && arch-be control score \\\n  --trigge, description="Compute significance score with declared triggers")`

Now I have enough context. Let me also load `handoff-packaging` maybe later. And `adversarial-review` for a final self-review. Let me proceed with writing.

Before writing, let me reconsider the deliverable set and check the `adr_registry` / `landscape_report` — not needed.

Let me also verify how delta_guard "mentions" work, to ensure DELTA.md coverage. I'll just mention the protected paths explicitly and verify with the tool at the end.

Now, one more consideration: the Stop hook runs gate with `--route auto --base bench-baseline`. I need the auto route to be one where gate passes. Sensors fail on docs/spec/state-machine.md at Standard/Critical. I will fix state-machine.md (add required sections) — then sensors pass. Also any new docs/spec file gets required sections. Good, then any route passes (assuming other checks pass). But if route = Critical, gate reports "Не проверено (обязательно ...)" for trace_check/nfr/model_validate/evidence_verify — are SKIPs fatal? In the probe, exit was FAIL only because sensors failed. The "Не проверено" line didn't cause exit 1 by itself (well, it said Итог: FAIL — провалено составляющих: 1). So SKIPs are okay. But wait, if all required pass but some are SKIP (not checked), does the gate exit 0? Likely yes (SKIP is not FAIL). Let me test after fixing sensors. Actually let me test now by temporarily... no, I'll test at the end.

But hold on — the probe showed sensors FAIL because of the existing file. If auto-route ends up Fast, sensors won't run at all and I wouldn't need to fix state-machine.md. But route will likely be Standard (api_contract_change detected). Let me confirm the detector fires when I modify openapi/tsp-api.yaml. I'll check at the end.

Either way, fixing state-machine.md required sections is beneficial and low-risk (adds documentation sections). I'll do it, declared in delta.

Now let me think about whether to add a `model/` directory. If route Critical, trace_check/nfr/model_validate remain unchecked (SKIP) → acceptable. If I added model/, I'd need to populate it correctly (easy to get wrong). The task doesn't ask for the typed model. I'll skip model/ but note it as a follow-up. Hmm, but "evidence_verify" and NFR quantitative checks for Critical would be skipped. Fine.

Actually, wait: the user asked for "измеримые NFR" — I provide them as a doc. The gate's nfr check needs model/; skipped. Fine.

Now let me write the documents. I'll write them one by one with the write_file tool. Let me start with ADR-008.

Let me draft ADR-008 content carefully (in Russian, matching repo style).

---

# ADR-008. Рекуррентные C2B-списания: мандат плательщика и планировщик списаний

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур) + владелец продукта СБП
- Related: ADR-001, ADR-002, ADR-003, ADR-004, ADR-005, ADR-009, AD-001, AD-002, AD-003, AD-005, AD-009

## Context

Принятое решение (ADR-001…ADR-007) описывает разовый C2B-приём: платёж инициируется предъявлением QR/ссылки, плательщик подтверждает каждую оплату в приложении своего банка. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные списания по подписке: плательщик один раз даёт согласие (мандат), дальше ТСП инициирует периодические списания без QR и без действий клиента на каждой оплате.

Новый сценарий добавляет сущность, которой в принятой модели нет: **длящееся согласие плательщика** (мандат/подписка), живущее дольше одного платежа, и **расписание списаний**. Отсюда новые риски: списание без действующего согласия, двойное списание за период, списание после отзыва согласия, пропущенное списание (недобор выручки ТСП).

Силы: финансовое последствие ошибки (несанкционированное/двойное списание) недопустимо; канал НСПК at-least-once; требования НПС/161-ФЗ к документированности согласия и немедленности отзыва; отзыв согласия инициируется плательщиком в его банке (вне периметра эквайера). Точная поддержка рекуррентного C2B в протоколе участника НСПК — внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`.

## Decision

1. **Мандат — новый единый источник истины** в БД шлюза (рядом с платежом, AD-002): состояние согласия, лимиты (сумма/период), срок действия, ссылка на подтверждение НСПК (`consentRef`). Мандат создаётся только по подтверждению от банка плательщика через адаптер ОПКЦ; до подтверждения списания запрещены.
2. **Планировщик списаний — модуль ядра шлюза**, внутри платёжного контура (AD-001), на той же БД/outbox/аудите. Отдельного сервиса и распределённой согласованности не вводим.
3. **Списание по подписке — это платёж** существующей статусной машины (ADR-002) с признаком `origin=recurring` и ссылкой `mandateId`: те же PAID→CREDITED→COMPLETED, то же зачисление только из `PAID` (AD-005 не меняется). QR не создаётся: состояние `QR_ISSUED` для рекуррентного происхождения означает «предъявлено банку плательщика, ожидается подтверждение».
4. **Защита от двойного списания**: ключ идемпотентности периодического списания детерминирован от `(mandateId, periodKey)`; уникальность на уровне БД + outbox в одной транзакции. Повторный запуск планировщика/повторная нотификация не создаёт второе списание (расширение AD-003).
5. **Отзыв/истечение/приостановка мандата немедленно блокируют новые списания** (guard на инициации); судьба уже инициированных, но не подтверждённых списаний — по политике, утверждаемой человеком (см. ADR-009).

## Alternatives Considered

| Вариант | Плюсы | Минусы | Почему отвергнут |
|---|---|---|---|
| Мандат и планировщик в ядре шлюза (выбран) | Единая транзакционная граница «мандат+списание+outbox»; нет распределённой согласованности; переиспользование SM/АБС/нотификаций/сверки | Ядро растёт; нужен планировщик и его эксплуатация | — |
| Отдельный сервис «Подписки» со своей БД | Изоляция домена; независимое масштабирование | Две БД → сага между подписками и платежами; риск расхождения «подписка списала, платёж не создан»; двойной источник истины | Противоречит AD-002 (единый источник истины) и повышает риск двойного/несанкционированного списания |
| Планирование на стороне ТСП (шлюз даёт только «списать по мандату») | Минимум в банке | Банк не может гарантировать «ровно одно» списание за период; отзыв согласия у многих ТСП не гарантирован; аудит размазан по мерчантам | Финансовый риск и регуляторная непрозрачность остаются у банка-эквайера |
| Полностью вендорское решение подписок | Быстрый старт | Закрытая логика мандатов, vendor lock-in, нет связи с ядром/АБС/аудитом | Лишает банк контроля над финансовой логикой (ср. ADR-007) |

## Consequences

### Positive

- Мандат и списания в одной транзакционной модели: «списание создано + outbox» атомарно, RPO=0 сохраняется.
- Переиспользование проверенного контура: зачисление только из `PAID`, идемпотентность, DLQ, сверка, аудит — без нового механизма согласованности.
- Планировщик в ядре даёт единый контроль «одно списание за период» и единую точку отзыва.
- Существующий C2B-приём не меняется: рекуррентный поток — расширение, не замена.

### Negative

- Ядро шлюза расширяется двумя сущностями (мандат, периодическое списание) и планировщиком — рост объёма кода и тестов; планировщик становится новой точкой отказа.
- Guard «мандат активен» добавляет проверку на горячем пути и зависимость от актуальности статуса мандата.
- Появляется долгоживущее состояние (мандаты годы), в отличие от короткоживущего платежа: хранение, ретенция, ПДн — новая эксплуатационная нагрузка.
- Расширяется периметр споров/претензий (диспуты по рекуррентным списаниям), который в принятом решении отложен.

## Reversibility

**costly.** Отключение рекуррентного потока (фиче-флаг, остановка планировщика) обратимо и не затрагивает разовый C2B-приём; но уже выданные мандаты и их отзыв — обязательства перед плательщиками и НСПК, «выключить и забыть» нельзя. Смена модели (например, перенос мандатов в отдельный сервис) после боевых списаний потребует миграции долгоживущего состояния.

Триггер пересмотра: (а) протокол НСПК не поддерживает рекуррентный C2B в нужном виде; (б) требования регулятора к согласиям меняются; (в) объём мандатов делает планировщик в ядре узким местом.

## References

- ADR-001 (топология/outbox), ADR-002 (статусная машина/идемпотентность), ADR-003 (адаптер ОПКЦ), ADR-004 (нотификации/сверка), ADR-005 (АБС), ADR-009 (согласие/мандат)
- AD-001, AD-002, AD-003, AD-005, AD-009 (spine)
- `docs/solutioning-recurring-c2b.md`, `docs/spec/subscription-lifecycle.md`, `docs/contracts/tsp-api-recurring-c2b.md`

---

Note: avoid TODO/TBD in spine only. ADRs can have `[ТРЕБУЕТ ПРОВЕРКИ]` which is fine (existing ADRs use it). Avoid `<!--`.

Now ADR-009: consent/mandate acquisition, storage, revoke.

# ADR-009. Согласие плательщика (мандат): получение, хранение, отзыв и запрет списаний

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур) + ИБ/комплаенс + продукт
- Related: ADR-003, ADR-004, ADR-006, ADR-008, AD-003, AD-006, AD-007, AD-009

## Context

Рекуррентное списание законно только при действующем согласии плательщика (мандате). Согласие даётся плательщиком в банке плательщика; эквайер получает подтверждение через ОПКЦ. Отзыв также инициируется плательщиком (в своём банке) и должен немедленно прекращать списания. Согласие — юридически значимый документ (161-ФЗ/НПС) и одновременно носитель ПДн (152-ФЗ), хранится годами. Требования НСПК к форме согласия, идентификаторам и срокам уведомления об отзыве — внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`.

Силы: невозможность списания без действующего согласия; немедленность отзыва; аудируемость каждого согласия; минимизация ПДн; отзыв приходит извне периметра эквайера — нельзя полагаться только на локальный статус.

## Decision

1. **Согласие существует только в подтверждённом виде.** Мандат переходит в `ACTIVE` лишь после подтверждения банка плательщика (событие ОПКЦ). Внутренние «предсогласия» — состояние `PENDING_CONSENT`, списания из него невозможны.
2. **Хранение**: в БД шлюза (ADR-002) хранится нормализованное согласие — идентификаторы, лимиты, срок, статус, ссылка на подтверждение (`consentRef`), метки времени; **реквизиты плательщика — только в токенизированном виде**, без ПДн сверх необходимого (ADR-006).
3. **Отзыв — первоклассный сценарий**: событие ОПКЦ `mandate.revoked` (или плановая сверка статусов мандатов) немедленно переводит мандат в `REVOKED`; guard на инициации списания блокирует новые списания; инициированные, но не подтверждённые (`до PAID`) — отменяются/закрываются по политике.
4. **Двухконтурная проверка**: перед каждым списанием — локальный статус мандата (`ACTIVE`, не истёк, в лимитах); периодическая сверка статусов мандатов с ОПКЦ ловит «отозван у плательщика, а у нас ACTIVE» (аналог ADR-004 для платежей).
5. **Аудит**: получение, активация, отзыв, приостановка, каждое списание и его основание (мандат, лимит) — в неизменяемом аудит-логе (AD-007).
6. **ПДн-минимизация**: в мандате нет сырых реквизитов счёта/телефона плательщика; только токены ОПКЦ/банка плательщика и служебные метки.

## Alternatives Considered

| Вариант | Плюсы | Минусы | Почему |
|---|---|---|---|
| Подтверждённый мандат как единственная основа (выбран) | Списание всегда опирается на подтверждённое согласие; аудируемость | Зависимость от скорости подтверждения ОПКЦ | — |
| «Оптимистичное» списание по заявке ТСП до подтверждения | Быстрее старт подписки | Списание без согласия — регуляторный и репутационный инцидент | Недопустимо |
| Хранить полные реквизиты плательщика для удобства сверки | Проще ручной разбор | Нарушение 152-ФЗ, рост поверхности атаки | Противоречит ADR-006 |
| Доверять только локальному статусу мандата, без сверки | Проще | «Отозван у плательщика, активен у нас» → несанкционированные списания | Финансовый риск |

## Consequences

### Positive

- Списание всегда опирается на подтверждённое согласие — соответствие НПС и защита от несанкционированных списаний.
- Отзыв обрабатывается детерминированно и немедленно блокирует новые списания.
- ПДн минимизированы, аудит полный.

### Negative

- Зависимость от ОПКЦ: задержка/недоступность канала задерживает активацию мандата и обработку отзывов.
- Сверка мандатов добавляет регулярную нагрузку и второй канал.
- Политика «судьба инициированного списания при отзыве» требует человеческого решения и усложняет runbook.

## Reversibility

**irreversible** в части обязательств: выданные согласия и их отзыв — юридические факты, «откатить» их нельзя. Отдельные механические элементы (форма сверки, способ токенизации) — reversible.

Триггер пересмотра: изменение требований НСПК/регулятора к форме и сроку действия согласия.

## References

- ADR-006 (trust-зоны, ПДн), ADR-003 (адаптер ОПКЦ), ADR-004 (нотификации/сверка), ADR-008 (мандат и планировщик)
- AD-003, AD-006, AD-007, AD-009 (spine)
- `docs/spec/subscription-lifecycle.md`, `docs/nfr-recurring-c2b.md`

---

Good. Now the solutioning doc (items 1,2,6,7 + design).

# Solutioning — Рекуррентные C2B-списания по подписке (СБП)

Sections:
1. Оценка значимости и маршрут (triggers table, score, route Critical, why).
2. Влияние на принятую архитектуру (invariants touched: AD-002 extended, AD-003 extended, AD-005 unchanged but reaffirmed, AD-001 unchanged (isolation), AD-004 extended (new events), AD-006/007 extended (PДн/audit); new AD-009; what does NOT change).
3. Целевая архитектура (C4 containers delta, components, flows: mandate acquisition, scheduled charge, revocation).
4. Изменения контрактов (pointer to contract doc + summary).
5. NFR (summary + pointer).
6. Критерии приёмки и план отката.
7. Что остаётся на решение человека-архитектора (A3-like list).
8. Gaps/внешние входы.
9. Открытые вопросы.

Let me include mermaid diagrams (repo uses mermaid). Note: mermaid_render tool can render. I'll include a sequence diagram for schedule charge and a flow for mandate lifecycle.

Also include the significance triggers table with declared true/false and reasoning.

Let me determine score: triggers true:
- api_contract_change (TSP API extended) ✔
- data_contract_change (new mandate/charge data model) ✔
- consistency_model_change (new mandate state + charge idempotency) ✔
- financial_impact (debits) ✔
- significant_nfr (new latency/lag/revocation NFR) ✔
- criticality_or_exception (payments/CII) ✔
- security_boundary_change? Revocation/consent — new external dependency? Not a new trust boundary beyond existing ОПКЦ. I'd say false (no new boundary; still in existing payment contour/НСПК channel). But consent is legally significant; still, security boundary unchanged.
- new_component? The mandate+scheduler is a new logical module inside the gateway, not a new deployable. Given the detector may treat new code root as new_component later. I'll declare false for the decision doc but note that at implementation it may become new_component. Hmm — honest: it's a new logical component (module). I'll declare true (new_component) because adding a scheduler+mandate store is architecturally a new component within the container. Actually score threshold: either way we're Critical (5+). Let me declare a defensible set and explain.

Let me include: new_component=true, api_contract_change=true, data_contract_change=true, consistency_model_change=true, financial_impact=true, significant_nfr=true, criticality_or_exception=true → 7 triggers → Critical. Others false with reasons: new_datastore=false (same БД, new tables — note: if new tables count, still Critical), new_vendor=false, trust_zone_change=false, security_boundary_change=false, rto_rpo_targets=false (existing targets extended, not new), irreversible_migration=false, domain_ownership_change=false, cross_domain_integration=false.

Hmm, is `rto_rpo_targets` true? New long-lived mandate state has RPO=0 requirement — extends existing. I'd mark false (no new target class) but NFR adds them. Eh, marking true is defensible. I'll keep false and explain that existing RPO=0/RTO targets are extended to mandates.

Let me verify trigger names via `arch-be control score --trigger new_component=true ...`. Let me run it to confirm accepted names and get score.

Let me run score with my declared triggers now.

  `write_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisaniy, content="# ADR-008. Рекуррентные C2B-списания: мандат плательщика и планировщик списаний\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: solutio)`

Score 7 → Critical. Good.

Now let me write all the files. Let me begin with ADR-008 and ADR-009.

Let me write ADR-008.
Now I'll write the ADRs. First ADR-008:

  `write_file(content="# ADR-009. Согласие плательщика (мандат): получение, хранение, отзыв и запрет списаний\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: , file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/adr/ADR-009-soglasie-platelschika-man)`

Now ADR-009.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/adr/ADR-009-soglasie-platelschika-man)`

I need to read the ADR-009 file first (it was auto-generated with a template).

  `write_file(content="# ADR-009. Согласие плательщика (мандат): получение, хранение, отзыв и запрет списаний\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: , file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/adr/ADR-009-soglasie-platelschika-man)`
  `write_file(content="# Подписки СБП — жизненный цикл мандата и планового списания\n\n- Status: Draft (для ревью на гейте A1 изменения `sbp-recurring-c2b`)\n- Ow, file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/spec/subscription-lifecycle.md")`

Now the subscription lifecycle spec (docs/spec/subscription-lifecycle.md) with required sections `## Проблема`, `## Критерии приёмки`, `## Риски` (exact headings). Let me check the sensor expects exactly those headings. Yes: "нет секций: ## Проблема, ## Критерии приёмки, ## Риски".

Let me write it: mandate state machine + charge lifecycle + guards + idempotency table + reconciliation.

Include required sections near top-level. Let me structure:
# Подписки СБП — жизненный цикл мандата и планового списания
- Status, Owner, Related
## Проблема
## 1. Сущности
## 2. Статусная модель мандата
## 3. Статусная модель планового списания
## 4. Запрещённые переходы (инварианты)
## 5. Идемпотентность
## 6. Сверка и восстановление
## 7. Согласованность с API ТСП
## Критерии приёмки
## Риски

Good. Let me write it.
Now the subscription lifecycle spec (new file under `docs/spec/`, must carry the sensor-required sections):

  `write_file(content="# Solutioning — Рекуррентные C2B-списания по подписке (изменение `sbp-recurring-c2b`)\n\n- Status: Proposed (ожидает человеческого решения , file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/solutioning-recurring-c2b.md")`

Now the solutioning doc for the change (items 1, 2, 6-part, 7 + design + impact + rollout/rollback + gaps). Let me write it thoroughly.

I'll include mermaid diagrams. Let me write.

Sections:
# Solutioning — Рекуррентные C2B-списания по подписке (изменение `sbp-recurring-c2b`)
- Status, Related, Delta link.
## 0. Привязка к дельте
## 1. Оценка значимости и маршрут
   - table of 15 triggers with value & reason
   - score 7 → Critical; command to reproduce
   - why full solutioning
## 2. Влияние на принятую архитектуру
   - 2.1 инварианты: unchanged / extended / new
   - table: AD-001 … AD-008, AD-009(new)
   - 2.2 что НЕ меняется (explicit)
   - 2.3 границы: parent spine escalation
## 3. Целевая архитектура (дельта к C4)
   - containers delta diagram
   - flows: mermaid sequence for scheduled charge; sequence for revocation
## 4. Жизненные циклы
   - pointer to spec
## 5. Обработка ошибок и защита от дубля/несанкционированного списания
   - idempotency, guards, circuit/at least once, fallback avoidance note (avoid fallback)
## 6. Контракты
   - summary + pointer to contract doc & openapi
## 7. NFR (summary + pointer)
## 8. Критерии приёмки (summary + pointer to delta/spec)
## 9. План отката
## 10. Что остаётся на решение человека-архитектора
## 11. Gaps и внешние входы
## 12. Открытые вопросы

Let me write it. Keep it substantive but not insanely long.

For significance table, list all 15 with true/false.

Triggers:
1. new_component = true — планировщик списаний и хранилище мандатов как новый модуль ядра.
2. new_datastore = false — та же БД шлюза, новые таблицы; отдельного хранилища нет. (Note: if new tables count, still Critical.)
3. new_vendor = false — новых вендоров нет; рекуррентные операции ложатся на существующий транспортный адаптер ОПКЦ (ADR-007).
4. domain_ownership_change = false — владелец прежний (платёжный контур шлюза).
5. cross_domain_integration = false — интеграции внутри существующих контуров (ОПКЦ, АБС).
6. api_contract_change = true — расширение API ТСП (новые методы/поля/события).
7. data_contract_change = true — новые сущности мандат/списание, новые поля.
8. security_boundary_change = false — новых границ доверия нет; отзыв идёт по существующему каналу ОПКЦ.
9. trust_zone_change = false — зоны те же (ADR-006).
10. consistency_model_change = true — мандат как длящееся состояние + идемпотентность по периоду.
11. significant_nfr = true — новые измеримые цели (лаг планировщика, немедленность отзыва, «ноль несанкционированных/двойных»).
12. rto_rpo_targets = false — цели RPO=0/RTO≤1ч распространяются на мандаты без изменения значений.
13. irreversible_migration = false — миграций данных нет; рекуррентный поток аддитивен. (Отдельно: юридические обязательства согласий необратимы — ADR-009, но это не миграция.)
14. financial_impact = true — реальные списания со счетов плательщиков.
15. criticality_or_exception = true — платежи/КИИ, регуляторный контур.

Score = 7 → Critical (≥5).

Route reasons why critical: human A3 mandatory, walking skeleton before mass generation, evidence gates.

Impact on invariants:
- AD-001 — unchanged rule; perimeter extends to new module (same adapters only).
- AD-002 — extended: единый источник истины теперь включает мандат; атомарность сохраняется.
- AD-003 — extended: ключ идемпотентности планового списания = (mandateId, periodKey).
- AD-004 — extended: новые типы нотификаций (mandate.*), сверка мандатов.
- AD-005 — unchanged (reaffirmed): зачисление только из PAID, включая плановые списания.
- AD-006 — unchanged zones; PДн обязательства усиливаются (мандат — ПДн-носитель).
- AD-007 — unchanged: аудит расширяется на согласия; СКЗИ прежние.
- AD-008 — unchanged: ядро контрактно-независимо; рекуррентные операции идут через внутренний контракт адаптера.
- AD-009 — NEW.

What does NOT change: payment SM states, TSP API existing methods, АБС credit-from-PAID, transport adapter choice (ADR-007), trust zones, RPO/RTO targets, C2C/B2C rollout, dispute handling deferred (but flagged).

Human decisions (item 7):
1. Протокольная реализуемость (после документации НСПК) — пересмотр ADR-008/009; A3.
2. Политика лимитов и периодов списания (коммерческая): maxAmount, период, поведение при повышении суммы.
3. Судьба in-flight списания при отзыве: отменять до PAID / доводить / возврат.
4. Периметр споров/претензий по рекуррентным списаниям — расширение deferred-элемента spine; A3.
5. Повышение уровня: изменение затрагивает feature-spine под initiative «Подключение банка к СБП» — нужна ратификация на уровне initiative (parent spine), т.к. новые регуляторные обязательства.
6. Утверждение walk-through: нужен ли A3 на изменение (маршрут Critical → да).
7. Тарифы/комиссии за подписки — влияет на отчётность.

Gaps/external inputs: НСПК protocol for recurring, regulatory form of consent, agreement with payer banks, АБС readiness for recurring documents, dispute process.

Rollback: feature flag per-ТСП; stop scheduler globally; revoke test mandates; in-flight drain; no data migration; signals: unauthorized debit, duplicate debit, revocation not honored → immediate stop-new; owner: платежный SRE + архитектор; RTO of rollback ≤ 15 min (stop scheduler).

Let me write the doc.
Now the main change solutioning document:

  `write_file(content="# NFR — Рекуррентные C2B-списания по подписке СБП\n\n- Status: Draft (для ревью на гейте A1 изменения `sbp-recurring-c2b`)\n- Owner: soluti, file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/nfr-recurring-c2b.md")`

Now NFR doc for recurring. Measurable metrics with method of verification.

# NFR — Рекуррентные C2B-списания по подписке

Sections: scope, budgets tables, inherited NFR, verification.

Metrics:
Scheduler/dispatch:
- Лаг инициации планового списания от scheduledAt: p95 ≤ 5 мин, p99 ≤ 15 мин.
- Catch-up после недоступности: пропущенные списания за ≤ 1 ч, окно catch-up — 1 период.
- Точность планировщика: доля созданных списаний от должных = 100%; дубли per period = 0.
- Throughput плановых списаний: sustained ≤ 100 TPS, burst ≤ 300 TPS (в пределах бюджета шлюза 200/500 TPS).
Mandate:
- Latency API создания заявки на мандат: p95 < 500 ms; статус мандата p95 < 300 ms.
- Активация мандата (подтверждение→ACTIVE): p95 ≤ 60 с (protocol-dependent, [ТРЕБУЕТ ПРОВЕРКИ]).
- Блокировка новых списаний после отзыва: ≤ 60 с (p99), 0 списаний после отзыва.
- Сверка мандатов: ежедневно; расхождений по ACTIVE ≤ 0 (цель).
Reliability:
- Двойные списания за период: 0.
- Несанкционированные списания: 0.
- Пропущенные списания по вине шлюза: 0 (catch-up).
- RPO=0 для мандатов и списаний.
- RTO ≤ 1 ч (как у шлюза).
Security/compliance:
- Аудит жизненного цикла мандата: 100%.
- ПДн: 0 сырых реквизитов в мандате; шифрование в покое; маскирование в логах.
Observability:
- Метрики планировщика (lag, due/created/failed, dedup hits, catch-up count); алерт на lag > 15 мин.
- Trace id на мандат и списание.

Also dependency note: protocol timings [ТРЕБУЕТ ПРОВЕРКИ].

Let me write it.

  `write_file(content="# Изменения контракта API ТСП для рекуррентных C2B-списаний — v0.1 → v0.2\n\n- Status: Draft (для ревью на гейте A1 изменения `sbp-recurrin, file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/contracts/tsp-api-recurring-c2b.md")`

Now the contract changes doc `docs/contracts/tsp-api-recurring-c2b.md`, and then the openapi yaml edit.

Contract doc content:
- Status, owner, related.
- Scope: additive extension.
- Compatibility guarantees (no breaking; existing consumers unaffected).
- New endpoints table.
- New request/response schemas with examples.
- New webhook events.
- Idempotency rules for new mutations.
- Error codes additions (additive to the canonical code list).
- Versioning: /v1 remains; info.version bump 0.2.0 (additive).
- Open questions.

Let me define endpoints concretely:

1. `POST /v1/mandates` — create mandate request (ТСП → gateway). Body: tspId, payerRef (token/phone token), maxAmountPerCharge, maxAmountPerPeriod, period, currency, validTo?, description, redirectUrl?, merchantSubscriptionId. Response 201: mandateId, status PENDING_CONSENT, consentUrl (deep-link/QR for payer), expiresAt.
2. `GET /v1/mandates/{mandateId}` — status: mandateId, tspId, status, limits, period, validFrom/To, consentRef?, createdAt.
3. `POST /v1/mandates/{mandateId}/revoke` — ТСП-initiated cancellation of subscription: reason. Response 200 {mandateId, status REVOKED}. Idempotent.
4. `POST /v1/mandates/{mandateId}/suspend` and `/resume` — optional; maybe include suspend/resume for ТСП (dunning). Keep minimal: include suspend/resume as optional. Hmm — scope. I'll include `suspend`/`resume` as merchant controls (useful). Actually to limit, include revoke only, and mention suspend/resume as open question. Let me include revoke; suspend/resume as optional future.
5. `GET /v1/mandates?tspId=&status=&cursor=` — list mandates (pagination).
6. `POST /v1/mandates/{mandateId}/charges` — initiate a charge under mandate (manual/ad-hoc or retry). Body: amount, periodKey? (optional; for scheduled idempotency), description. Idempotency-Key required. Response 201: chargeId, paymentId, status.
7. `GET /v1/mandates/{mandateId}/charges?periodKey=&status=&cursor=` — list charges.
8. `GET /v1/charges/{chargeId}` — charge status (perhaps redundant with payment). I'll use `/v1/payments/{paymentId}` plus mandate fields; but a dedicated `GET /v1/mandates/{mandateId}/charges` list is enough. To keep contract lean, skip /v1/charges.

Webhook events (added):
- `mandate.pending` (optional), `mandate.activated`, `mandate.rejected`, `mandate.suspended`, `mandate.resumed`, `mandate.revoked`, `mandate.expired`
- `charge.completed`, `charge.failed` (or reuse payment.completed/failed with mandateId). I'll define charge events as aliases carrying mandateId/periodKey, to let merchants subscribe. Actually simpler: reuse `payment.*` for charge money movement (since charge is a payment) and add `mandate.*`. Hmm, but merchants want to know a charge attempted and failed. `payment.failed` already covers it with mandateId. To avoid duplication, I'll reuse `payment.*` (with new optional fields `origin`, `mandateId`, `periodKey`) and add `mandate.*` events. That's cleaner and less breaking. But the docs contract currently lists events `payment.completed/failed/expired` and `refund.*`. I'll add `mandate.*` and note charge events reuse `payment.*`.

Schema additions:
- PaymentRequest: add optional `origin` (enum qr|link|recurring; default qr), `mandateId` (required when origin=recurring), `periodKey` (optional, required when origin=recurring for idempotent scheduled charges).
- Payment: add optional `origin`, `mandateId`, `periodKey`, `chargeId`.
- New schemas: Mandate, MandateRequest, MandateList, ChargeRequest, ChargeList, Charge.
- Error codes: add `MANDATE_NOT_ACTIVE` (409/422), `MANDATE_LIMIT_EXCEEDED` (422), `MANDATE_NOT_FOUND` (404), `MANDATE_REVOKED` (409), `CHARGE_ALREADY_EXISTS` (200 with existing resource, per idempotency) — maybe not an error. Add `SUBSCRIPTION_NOT_FOUND`. Keep additive.

Now let me write the contract doc.
Now the contract changes document:

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\n  description: >\n    Контракт между ТСП и СБП-шлюзом банка. Версия 0, file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/openapi/tsp-api.yaml")`

Now edit `openapi/tsp-api.yaml` — additive. Let me construct the new YAML carefully so `openapi_lint` passes. The baseline lint passed with the minimal file. Let me keep the style (flow mapping) and add:

- info.version: 0.2.0
- new paths: /v1/mandates (post, get), /v1/mandates/{mandateId} (get), /v1/mandates/{mandateId}/revoke (post), /v1/mandates/{mandateId}/charges (post, get)
- parameters: Idempotency-Key header, path params
- responses: errors using ProblemDetails
- schemas: PaymentRequest (extended), Payment (extended), MandateRequest, Mandate, MandateStatus enum, ChargeRequest, Charge, MandateList, ChargeList, ProblemDetails

I must be careful: openapi_lint checks versioning, mutating endpoint idempotency, RFC 7807 errors. Let me check what it requires: "Проверить контракт OpenAPI 3.x: версионирование, идемпотентность mutating-endpoint'ов, ошибки RFC 7807 (транш T1, ADR-015)". Likely requires:
- info.version present and semver.
- Each POST/PUT/PATCH/DELETE either has Idempotency-Key parameter or is marked...? Possibly requires Idempotency-Key for mutating endpoints.
- Error responses should reference ProblemDetails schema with RFC 7807 fields (type/title/status/detail). Possibly requires 4xx/5xx responses defined referencing application/problem+json.

The current file has POST /v1/payments with Idempotency-Key but no error responses, yet lint PASS. So lint may only warn or check specific things. To be safe, I'll add proper problem+json responses for all mutating endpoints and define ProblemDetails.

Let me check openapi_lint rules more precisely. Maybe there's documentation. Let me look at the tool description again: "Проверить контракт OpenAPI 3.x: версионирование, идемпотентность mutating-endpoint'ов, ошибки RFC 7807 (транш T1, ADR-015)". Since baseline passes with no error responses, maybe the check is lenient (only flags described issues). Let me just write a good contract and lint it; iterate if needed.

Let me write the YAML in block style (more readable) but consistent enough. I'll preserve existing path content and extend.

Actually careful: the `PaymentRequest` currently required [amount, merchantOrderId]. If I add origin/mandateId optional, fine.

Let me write the full file.

Design:

```yaml
openapi: 3.0.3
info:
  title: СБП-шлюз — API ТСП
  version: 0.2.0
  description: >
    Контракт между ТСП и СБП-шлюзом банка. v0.2 — аддитивное расширение:
    рекуррентные C2B-списания по согласию плательщика (мандату). Существующие
    потребители v0.1 не затрагиваются.
servers:
  - url: https://api.bank.ru/sbp
paths:
  /v1/payments:
    post:
      operationId: createPayment
      summary: Создание платежа (QR/ссылка) или планового списания по мандату
      parameters:
        - $ref: '#/components/parameters/IdempotencyKey'
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
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
  /v1/payments/{paymentId}:
    get:
      operationId: getPayment
      parameters:
        - $ref: '#/components/parameters/PaymentId'
      responses:
        '200':
          description: Статус платежа
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Payment'}
        '404':
          $ref: '#/components/responses/NotFound'
  /v1/mandates:
    post:
      operationId: createMandate
      summary: Заявка на согласие плательщика (подписку)
      parameters:
        - $ref: '#/components/parameters/IdempotencyKey'
      requestBody:
        required: true
        content:
          application/json:
            schema: {$ref: '#/components/schemas/MandateRequest'}
      responses:
        '201':
          description: Заявка на мандат создана
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Mandate'}
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
    get:
      operationId: listMandates
      parameters:
        - {in: query, name: tspId, required: true, schema: {type: string}}
        - {in: query, name: status, required: false, schema: {$ref: '#/components/schemas/MandateStatus'}}
        - {in: query, name: cursor, required: false, schema: {type: string}}
      responses:
        '200':
          description: Список мандатов
          content:
            application/json:
              schema: {$ref: '#/components/schemas/MandateList'}
  /v1/mandates/{mandateId}:
    get:
      operationId: getMandate
      parameters:
        - $ref: '#/components/parameters/MandateId'
      responses:
        '200':
          description: Статус мандата
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Mandate'}
        '404':
          $ref: '#/components/responses/NotFound'
  /v1/mandates/{mandateId}/revoke:
    post:
      operationId: revokeMandate
      summary: Отмена подписки ТСП
      parameters:
        - $ref: '#/components/parameters/MandateId'
        - $ref: '#/components/parameters/IdempotencyKey'
      responses:
        '200':
          description: Мандат отозван
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Mandate'}
        '404':
          $ref: '#/components/responses/NotFound'
  /v1/mandates/{mandateId}/charges:
    post:
      operationId: createCharge
      summary: Ручное списание в рамках мандата
      parameters:
        - $ref: '#/components/parameters/MandateId'
        - $ref: '#/components/parameters/IdempotencyKey'
      requestBody:
        required: true
        content:
          application/json:
            schema: {$ref: '#/components/schemas/ChargeRequest'}
      responses:
        '201':
          description: Списание инициировано
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Charge'}
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
    get:
      operationId: listCharges
      parameters:
        - $ref: '#/components/parameters/MandateId'
        - {in: query, name: status, required: false, schema: {type: string}}
        - {in: query, name: cursor, required: false, schema: {type: string}}
      responses:
        '200':
          description: Список списаний по мандату
          content:
            application/json:
              schema: {$ref: '#/components/schemas/ChargeList'}
components:
  parameters:
    IdempotencyKey:
      in: header
      name: Idempotency-Key
      required: true
      schema: {type: string}
    PaymentId:
      in: path
      name: paymentId
      required: true
      schema: {type: string}
    MandateId:
      in: path
      name: mandateId
      required: true
      schema: {type: string}
  responses:
    NotFound:
      description: Ресурс не найден
      content:
        application/problem+json:
          schema: {$ref: '#/components/schemas/ProblemDetails'}
    Conflict:
      description: Конфликт состояния или идемпотентности
      content:
        application/problem+json:
          schema: {$ref: '#/components/schemas/ProblemDetails'}
    UnprocessableEntity:
      description: Запрос отклонён правилами (лимиты, статус мандата)
      content:
        application/problem+json:
          schema: {$ref: '#/components/schemas/ProblemDetails'}
  schemas:
    PaymentRequest:
      type: object
      required: [amount, merchantOrderId]
      properties:
        amount: {type: integer, description: Сумма в копейках}
        merchantOrderId: {type: string}
        origin:
          type: string
          enum: [qr, link, recurring]
          default: qr
          description: Источник платежа; recurring — списание по мандату
        mandateId:
          type: string
          description: Обязателен при origin=recurring
        periodKey:
          type: string
          description: Ключ периода (например 2026-10); задаёт идемпотентность планового списания
    Payment:
      type: object
      required: [paymentId, amount, status]
      properties:
        paymentId: {type: string}
        amount: {type: integer, description: Сумма в копейках}
        status:
          type: string
          enum: [CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED]
        origin: {type: string, enum: [qr, link, recurring]}
        mandateId: {type: string}
        periodKey: {type: string}
        chargeId: {type: string}
    MandateStatus:
      type: string
      enum: [PENDING_CONSENT, PENDING_OPKC, ACTIVE, SUSPENDED, REVOKED, EXPIRED, REJECTED]
    MandateRequest:
      type: object
      required: [tspId, payerRef, currency, maxAmountPerCharge, maxAmountPerPeriod, period]
      properties:
        tspId: {type: string}
        payerRef: {type: string, description: Токен плательщика (без ПДн)}
        currency: {type: string, enum: [RUB]}
        maxAmountPerCharge: {type: integer, description: Лимит на списание, копейки}
        maxAmountPerPeriod: {type: integer, description: Лимит на период, копейки}
        period:
          type: string
          enum: [MONTH, WEEK, CUSTOM]
        validTo: {type: string, format: date-time}
        description: {type: string}
        redirectUrl: {type: string, format: uri}
        merchantSubscriptionId: {type: string}
    Mandate:
      type: object
      required: [mandateId, tspId, status, currency, maxAmountPerCharge, maxAmountPerPeriod, period]
      properties:
        mandateId: {type: string}
        tspId: {type: string}
        status: {$ref: '#/components/schemas/MandateStatus'}
        currency: {type: string}
        maxAmountPerCharge: {type: integer}
        maxAmountPerPeriod: {type: integer}
        period: {type: string, enum: [MONTH, WEEK, CUSTOM]}
        validFrom: {type: string, format: date-time, nullable: true}
        validTo: {type: string, format: date-time, nullable: true}
        consentRef: {type: string, nullable: true}
        consentUrl: {type: string, format: uri, nullable: true}
        createdAt: {type: string, format: date-time}
        merchantSubscriptionId: {type: string}
    MandateList:
      type: object
      required: [items]
      properties:
        items:
          type: array
          items: {$ref: '#/components/schemas/Mandate'}
        nextCursor: {type: string, nullable: true}
    ChargeRequest:
      type: object
      required: [amount]
      properties:
        amount: {type: integer, description: Сумма в копейках}
        periodKey: {type: string}
        description: {type: string}
    Charge:
      type: object
      required: [chargeId, mandateId, paymentId, amount, status]
      properties:
        chargeId: {type: string}
        mandateId: {type: string}
        paymentId: {type: string}
        periodKey: {type: string}
        amount: {type: integer}
        status: {type: string, description: Статус платежа (Payment.status)}
        createdAt: {type: string, format: date-time}
    ChargeList:
      type: object
      required: [items]
      properties:
        items:
          type: array
          items: {$ref: '#/components/schemas/Charge'}
        nextCursor: {type: string, nullable: true}
    ProblemDetails:
      type: object
      required: [type, title, status]
      properties:
        type: {type: string, format: uri}
        title: {type: string}
        status: {type: integer}
        detail: {type: string}
        code: {type: string}
        traceId: {type: string}
        idempotencyKey: {type: string}
```

Wait — the original file did not have `servers`, and used inline parameters. Fine.

Concern: openapi_lint might require idempotency key on all POST. All my POST have it. Good. Might require `429` handling? Original had none and passed.

Concern: `nullable: true` in OpenAPI 3.0.3 is valid. Good.

Concern: The lint may check that mutating endpoint errors are RFC7807, and the original POST /v1/payments had no error responses yet passed — so no requirement. Adding them is fine.

Let me write the file. Since write_file requires reading first (already read earlier in session), it should be allowed (I read it). Good.

Let me write it.
Now I'll extend the OpenAPI contract additively:

  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wrpc5sz/ws/openapi/tsp-api.yaml"}, name="mcp__spine__openapi_lint")`
  `tool_search(query="select:mcp__spine__contract_diff")`

Now lint the openapi and run contract_diff between versions. I need two versions for contract_diff. I can use git to get the baseline file content. contract_diff takes two contracts? Let me check its schema. Let me search.

Actually let me first run openapi_lint on the new file. And check contract_diff tool schema.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && git show bench-baseline:openapi/tsp-, description="Extract baseline contract version")`

Good, openapi_lint passes. Now contract_diff: need old version file. Let me extract baseline from git to a temp location (under .qwen/tmp to avoid artifact registration... actually shell-created temp in /tmp is fine). Use `git show bench-baseline:openapi/tsp-api.yaml > <TMP>.yaml`. Then call contract_diff with old=/tmp/..., new=openapi/tsp-api.yaml. Let me do that.

  `tool_call(arguments={"old": "<TMP>.yaml", "new": "<HARNESS>/runs-v2/cells/wrpc5sz/ws/op, name="mcp__spine__contract_diff")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/ARCHITECTURE-SPINE.md", old_string="## AD-002. Единый источник истины — статусная машина платежа\n\n- Status: Proposed (ADR-002)\n- **Binds**: БД шлюза (состояние платежа), ou, new_string="## AD-002. Единый источник истины — статусная машина платежа и мандат\n\n- Status: Proposed (ADR-002, ADR-008)\n- **Binds**: БД шлюза (сост)`

Breaking: 0, PASS. 

Now update `ARCHITECTURE-SPINE.md` — add AD-009 and extend AD-003. This is a protected file → must be mentioned in DELTA.md.

Let me edit:
1. In "Контракты и версии" maybe mention ADR-008/009 and contract v0.2.
2. Extend AD-003 Binds to include mandate consent and periodKey; add to Prevents / Rule.
3. Add AD-009 block.

Let me be careful with spine_lint: each block needs Status, Binds, Prevents, Rule; no dup IDs; no TODO/TBD/XXX; references to existing ADs only. I'll reference AD-001..AD-009 which exist.

Let me add AD-009 after AD-008, and modify AD-003.

Current AD-003:
```
## AD-003. Идемпотентность финансовых операций

- Status: Proposed (ADR-002, ADR-004, ADR-005)
- **Binds**: вход ТСП (`Idempotency-Key`), нотификации НСПК (`eventId`), вызовы АБС (`paymentId`/`refundId`).
- **Prevents**: двойное зачисление, двойной возврат, дубли QR при ретрае клиента ТСП.
- **Rule**: Повторная доставка любого сообщения не изменяет уже завершённое состояние. Fitness: тест «повторная нотификация/повторный запрос → состояние не меняется, результат идемпотентен».
```

Modify to add recurring: Binds add `ключ планового списания (mandateId, periodKey)`, `согласие плательщика (consentRef)`. Prevents add `двойное списание за период`, `повторная активация согласия`. Rule add: "Плановое списание идемпотентно по (mandateId, periodKey): повтор не создаёт второй платёж."

Add AD-009:
```
## AD-009. Рекуррентные списания только по действующему согласию (мандату)

- Status: Proposed (ADR-008, ADR-009)
- **Binds**: мандат плательщика (согласие), планировщик списаний, статусная машина платежа (`origin=recurring`), лимиты и срок мандата, аудит-лог.
- **Prevents**: списание без согласия или после отзыва; списание при приостановленном/истёкшем мандате; превышение лимитов; двойное списание за период; зачисление по несогласованному списанию.
- **Rule**: Плановое списание инициируется только при мандате в статусе `ACTIVE` (не отозван, не истёк, не приостановлен) и в пределах лимитов `maxAmountPerCharge`/`maxAmountPerPeriod`; ключ идемпотентности планового списания — `(mandateId, periodKey)`; зачисление по списанию — только из `PAID` (наследует AD-005). Проверка: guard в коде + fitness-тесты на отказ при недействующем мандате и на отсутствие двойного списания.
```

Also update the "Контракты и версии" section to mention v0.2 and new docs. And maybe add to Deferred: диспуты — now flagged as prerequisite; keep deferred but note.

Careful: Don't use TODO/TBD/XXX. Also avoid "TBD".

Let me also verify spine_lint doesn't complain about "Rule:" multi-line. Existing format uses single-line Rule. I'll keep single line.

Now the "Контракты и версии" update: change "Внутренний контракт шлюза (API ТСП): версия 0.1 draft" — hmm, modifying accepted text. Add a line for v0.2. Let me add:
```
- Внутренний контракт шлюза (API ТСП): версия 0.2 — `docs/contracts/tsp-api.md`; изменения рекуррентных списаний — `docs/contracts/tsp-api-recurring-c2b.md`, машинный контракт — `openapi/tsp-api.yaml` (v0.2.0). Версия 0.1 — предыдущая, обратно совместима.
```
Actually the current text says "версия 0.1 draft — docs/contracts/tsp-api.md (создаётся на этапе Spec)". I'll append an additional bullet rather than rewrite. Let me read the tail of the file to edit precisely.

Also update the AD-002 spine? It says "Изменение финансового статуса платежа и запись исходящего события (outbox) в одной локальной транзакции" — recurring doesn't change this. But we extend "единый источник истины" to mandate. I'll modify AD-002 Binds to include "мандат плательщика (согласие)" and Rule add "мандат и плановое списание — в той же транзакционной модели". Hmm, minimal. Actually the delta declares MODIFIED for AD-002 semantics extension. Let me add a sentence to AD-002 Binds/Prevents/Rule. Keep it small.

Let me do edits.

Let me read the current spine file again (already read at start, but I'll edit with exact strings). I have the content. Let me perform edits.

Edit 1: AD-002 block.
Original:
```
## AD-002. Единый источник истины — статусная машина платежа

- Status: Proposed (ADR-002)
- **Binds**: БД шлюза (состояние платежа), outbox, аудит-лог.
- **Prevents**: расхождение «шлюз думает PAID, АБС не знает» без сверки; неатомарные обновления статуса.
- **Rule**: Изменение финансового статуса платежа и запись исходящего события (outbox) выполняются в одной локальной транзакции. Нарушение — дефект блокера (ревью + fitness-тест на каждый переход).
```
New:
```
## AD-002. Единый источник истины — статусная машина платежа и мандат

- Status: Proposed (ADR-002, ADR-008)
- **Binds**: БД шлюза (состояние платежа, мандат плательщика, плановое списание), outbox, аудит-лог.
- **Prevents**: расхождение «шлюз думает PAID, АБС не знает» без сверки; неатомарные обновления статуса; расхождение статуса мандата и списаний.
- **Rule**: Изменение финансового статуса платежа, статуса мандата и запись исходящего события (outbox) выполняются в одной локальной транзакции. Нарушение — дефект блокера (ревью + fitness-тест на каждый переход).
```

Edit 2: AD-003.

Edit 3: add AD-009 after AD-008 block (before "---\n\n## Deferred").

Edit 4: Контракты и версии — add bullet.

Let me do these edits.
Now updating the protected spine file (declared in the delta):

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/ARCHITECTURE-SPINE.md", new_string="## AD-003. Идемпотентность финансовых операций\n\n- Status: Proposed (ADR-002, ADR-004, ADR-005, ADR-008)\n- **Binds**: вход ТСП (`Idempote, old_string="## AD-003. Идемпотентность финансовых операций\n\n- Status: Proposed (ADR-002, ADR-004, ADR-005)\n- **Binds**: вход ТСП (`Idempotency-Key`))`

Now edit AD-003.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/ARCHITECTURE-SPINE.md", new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now add AD-009 after AD-008 block. Let me read the tail region to get exact text.

The AD-008 block ends with:
```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll insert AD-009 between the AD-008 rule and the `---`/Deferred. Let me edit using the tail of AD-008 rule + "\n\n---\n\n## Deferred" as anchor.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/ARCHITECTURE-SPINE.md", offset=73, limit=20)`

Now update the "Контракты и версии" section and the Deferred section (mention disputes need resolution before recurring go-live). Let me read the tail of the file to edit precisely.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/ARCHITECTURE-SPINE.md", new_string="- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора. Для рекуррентных C2B, old_string="- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.\n\n## Контракты и ве)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="  - name: spine-lints-clean\n    type: must_not_contain\n    glob: \"ARCHITECTURE-SPINE.md\"\n    pattern: 'TODO|TBD|XXX'\n    severity: wa, old_string="  - name: spine-lints-clean\n    type: must_not_contain\n    glob: \"ARCHITECTURE-SPINE.md\"\n    pattern: 'TODO|TBD|XXX'\n    severity: wa)`

Now update CONSTRAINTS.yaml — add fitness rules. Protected file. Add rules that don't require code (docs stage):
- `recurring-spine-invariant`: must_contain ARCHITECTURE-SPINE.md pattern 'AD-009'
- `recurring-mandate-guard-doc`: must_contain docs/spec/subscription-lifecycle.md pattern 'ACTIVE'
- `recurring-delta-present`: file_exists changes/sbp-recurring-c2b/DELTA.md
- `recurring-nfr-measurable`: must_contain docs/nfr-recurring-c2b.md pattern '0' maybe better pattern like '≤ 60 с' or 'дубли'
- `recurring-contract-additive`: must_contain openapi/tsp-api.yaml pattern '/v1/mandates'
- `recurring-adr-set`: file_exists docs/adr/ADR-008... (exact file name)

Must not weaken existing rules. Adding is fine. Note rule_weakened compares relative to bench-baseline — additions should be fine.

Careful: `must_contain` regexes are matched against the whole file. Patterns with special regex chars need care. Let me use safe patterns with `(?m)` anchors where needed.

Let me choose:
- name: recurring-spine-invariant; type: must_contain; glob: "ARCHITECTURE-SPINE.md"; pattern: 'AD-009'; severity: error
- name: recurring-mandate-state-machine; type: file_exists; path: docs/spec/subscription-lifecycle.md; severity: error
- name: recurring-delta-declared; type: file_exists; path: changes/sbp-recurring-c2b/DELTA.md; severity: error
- name: recurring-nfr-no-unauthorized; type: must_contain; glob: "docs/nfr-recurring-c2b.md"; pattern: 'Несанкционированные списания'; severity: error
- name: recurring-nfr-double-charge-zero; type: must_contain; glob: "docs/nfr-recurring-c2b.md"; pattern: 'Дубли на'; severity: warn
- name: recurring-api-additive; type: must_contain; glob: "openapi/tsp-api.yaml"; pattern: '/v1/mandates'; severity: error
- name: recurring-adr-008; type: file_exists; path: docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-mandat-platelschika-i-planirovschik-spisaniy.md; severity: error
- name: recurring-adr-009; type: file_exists; path: docs/adr/ADR-009-soglasie-platelschika-mandat-poluchenie-hranenie-otzyv-i-zapret-spisaniy.md; severity: error

Wait, careful: `must_contain` with glob "docs/nfr-recurring-c2b.md" — the pattern 'Несанкционированные списания' appears in the table. Good. 'Дубли на' appears as "Дубли на `(mandateId, periodKey)`". Good.

Also note the existing rule `adr-no-placeholders` glob "docs/adr/*.md" pattern '<!--' — my new ADRs have no `<!--`. Good. But wait — the `Model-author: human:...` line contains a colon; fine.

Also: `must_not_contain` pattern 'TODO|TBD|XXX' glob ARCHITECTURE-SPINE.md — my new AD-009 text: does it contain "TBD"? No. "XXX"? No. Good. But careful — "TODO" no.

Hmm, one more: the existing `spine-lints-clean` warn rule checks TODOs. Fine.

Now, potential issue: `rule_weakened` — comparing rule fingerprint. Adding rules changes the fingerprint; should still PASS since nothing weakened.

Let me also double check: the delta_guard requires modified protected files mentioned in DELTA.md. Protected defaults: model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. I'll mention both in DELTA.md.

Let me now write CONSTRAINTS.yaml additions. I'll edit by appending rules after the last one.

Current last rules:
```
  - name: spine-lints-clean
    type: must_not_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'TODO|TBD|XXX'
    severity: warn
```

I'll append after it.

Let me be careful with YAML: comments in Russian fine.

Let me edit.
Now adding fitness rules to the protected constraints registry:

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/spec/state-machine.md", new_string="## 6. Согласованность с API ТСП\n\nМаппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED, old_string="## 6. Согласованность с API ТСП\n\nМаппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED)`

Now fix `docs/spec/state-machine.md` to add required sections `## Проблема`, `## Критерии приёмки`, `## Риски`, and note the recurring extension. This file is a docs file (not protected), so no delta mention needed, but I'll declare it in the delta's MODIFIED anyway.

Let me append these sections to the end of state-machine.md, and add a note in §1/§6 about origin=recurring. Minimal: append sections at the end. Also add a sentence in "## 1. Состояния" maybe. Let me just append three sections; and add a cross-reference note near the top or in section 6.

Actually the sensor checks exact headings `## Проблема`, `## Критерии приёмки`, `## Риски`. I'll append.

Let me read the end of state-machine.md (section 6 was last). I have content. Append:

```
## Проблема

...

## Критерии приёмки

...

## Риски

...
```

And add to §6 a mention of origin=recurring pointer. Let me do two edits: one to append sections; optionally one to add pointer. I'll add pointer in §6 text.

Let me append at end using the last lines as anchor. The file ends with:
```
## 6. Согласованность с API ТСП

Маппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `EXPIRED`, `REFUNDED` — без технических подсостояний (`ABS_PENDING`, `NOTIFY_PENDING` наружу не выставляются; `ABS_PENDING` отражается как `PAID` + поле `creditingStatus`).
```

Let me edit that ending block to add the recurring note + the three sections.
Now fixing the existing spec's required sensor sections and cross-referencing the recurring extension:

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/contracts/opkc-adapter.md", new_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t, old_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t)`

Now extend `docs/contracts/opkc-adapter.md` with recurring methods/events. This is a docs file (not protected). I'll add a subsection §3bis and events. Let me do a focused edit: add rows to the sync operations table and add events, plus a note.

Actually, editing the existing tables precisely: the sync operations table rows end with getReconciliationReport. I'll add rows after it. And in the async events table add new rows. Let me do two edits.

Let me add to §3 table:
| `registerMandate` | регистрация заявки на согласие (мандат) | `reference` (= `mandateId` ядра), `tspId`, `payerRef`, лимиты, период, `validTo?` | `jobId`, статус `ACCEPTED` (результат — событием) | 5 c |
| `getMandateStatus` | статус мандата | `mandateId` (ОПКЦ) | `ACTIVE` / `PENDING` / `REVOKED` / `REJECTED` / `EXPIRED`, `consentRef?`, `validTo?` | 3 c |
| `createRecurringDebit` | инициировать списание по мандату | `reference` (= `paymentId` ядра), `mandateId`, `amount`, `periodKey` | `accepted` (результат — событием) | 3 c |
| `cancelMandate` | отмена подписки со стороны ТСП | `mandateId`, `reason` | `CANCELLED` | 3 c |
| `getMandateReconciliationReport` | выписка по мандатам за период | `from`, `to` | список мандатов: `mandateId`, `status`, `updatedAt` | 10 c |

And events:
| `mandate.activated` | согласие подтверждено | `mandateId`, `reference` (= `mandateId` ядра), `tspId`, `consentRef`, `validFrom` |
| `mandate.rejected` | согласие отклонено | `mandateId`, `reasonCode`, `reasonText` |
| `mandate.revoked` | согласие отозвано | `mandateId`, `reference`, `revokedAt` |
| `mandate.expired` | истёк срок | `mandateId`, `reference` |

Also update §5 idempotency to include mandateId/periodKey, and §2 maybe.

Let me edit §3 table and §4 table.

Note: the events table's `correlationRef` uses `reference`. Fine.

Let me perform edits.
Now extending the internal adapter contract with recurring operations (documentation level):

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/contracts/opkc-adapter.md", new_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |\n| `mandate.activated` | , old_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |")`

Now add events to the async events table. Add after `transport.unavailable` row.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/contracts/opkc-adapter.md", new_string="- Повторная доставка события с тем же `eventId` — игнорируется ядром (ADR-003).\n- Рекуррентные операции: `reference` списания — `paymentId, old_string="- Повторная доставка события с тем же `eventId` — игнорируется ядром (ADR-003).")`

Now update §5 idempotency mention and §9 open questions maybe. Let me add a bullet in §5 for recurring. Let me edit the §5 text.

Current §5:
```
## 5. Идемпотентность и ссылки

- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.
- **Адаптер обязан обеспечить идемпотентность**: повторный вызов с тем же `reference` возвращает тот же результат и **не создаёт дубль в ОПКЦ**. ...
- Повторная доставка события с тем же `eventId` — игнорируется ядром (ADR-003).
```

Add bullet: "Для рекуррентных операций: `reference` для списания — `paymentId`, ключ периода `periodKey` передаётся для трассировки; повтор `createRecurringDebit` с тем же `reference` не создаёт второе списание (ADR-008/AD-009)."

Let me edit.

  `write_file(content="# Дельта: sbp-recurring-c2b\n\n- Route: **Critical** (значимость 7/15; дельты недостаточно — полный Solutioning в `docs/solutioning-recurri, file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/changes/sbp-recurring-c2b/DELTA.md")`

Now write the DELTA.md. It must:
- have Route line (Critical)
- Проблема
- ADDED (EARS criteria)
- MODIFIED (was→now)
- REMOVED (none? or note)
- План отката
- Критерии приёмки
- Mention protected files: `ARCHITECTURE-SPINE.md` and `CONSTRAINTS.yaml` (and `.arch-handoff/CONSTRAINTS.yaml`).

Delta validate may require certain structure. The template has: Route, Created, Проблема, ADDED, MODIFIED, REMOVED, План отката, Критерии приёмки. Let me keep exactly those headings (plus maybe extra sections are fine). I'll keep the template's headings and add nothing structural that breaks validation. Let me check `arch-be delta validate` after.

Let me write DELTA.md now. Include explicit "Затронутые защищённые файлы" section — extra heading should be OK. But to be safe with validate, let me keep required headings and add the protected-file list inside MODIFIED or as an extra section. Let me first write it with an extra section and validate; if validate complains, adjust.

EARS ADDED items. Let me write ~8-10 requirements.

ADDED:
1. When ТСП отправляет POST /v1/mandates с валидным Idempotency-Key, the шлюз shall создать заявку на мандат в статусе PENDING_CONSENT и вернуть mandateId ≤ 500 мс p95.
2. When банк плательщика подтверждает согласие (событие mandate.activated), the шлюз shall перевести мандат в ACTIVE в одной транзакции со записью outbox и аудита.
3. When наступает scheduledAt для мандата ACTIVE, the планировщик shall создать плановое списание с ключом (mandateId, periodKey) не позднее p95 ≤ 5 мин от scheduledAt.
4. When повторный прогон планировщика/повторная нотификация обрабатывает уже созданное списание за тот же periodKey, the шлюз shall не создавать второй платёж и вернуть существующий.
5. When плановое списание подтверждено НСПК, the шлюз shall зачислить средства только из состояния PAID (AD-005).
6. When приходит mandate.revoked, the шлюз shall перевести мандат в REVOKED и заблокировать новые списания ≤ 60 с.
7. When списание инициируется при мандате не в ACTIVE, вне лимитов или истёкшем, the шлюз shall отклонить списание без движения денег.
8. When ТСП запрашивает GET /v1/mandates/{mandateId}, the шлюз shall вернуть статус и параметры мандата ≤ 300 мс p95.
9. When webhook mandate.activated доставляется, the шлюз shall подписать его HMAC и обеспечить дедупликацию по X-SBP-Event-Id (at-least-once).
10. When рекуррентные методы запрашиваются у адаптера ОПКЦ, the адаптер shall обеспечить идемпотентность по reference.

MODIFIED:
- AD-002 (spine): единый источник истины расширен на мандат — было «статус платежа», стало «статус платежа + мандат + плановое списание» (ADR-008).
- AD-003 (spine): идемпотентность — добавлен ключ (mandateId, periodKey).
- ADR-002 semantics: QR_ISSUED для origin=recurring = «предъявлено банку плательщика».
- API ТСП: PaymentRequest/Payment — добавлены опциональные origin/mandateId/periodKey; контракт v0.1 → v0.2 (аддитивно).
- Контракт адаптера ОПКЦ: добавлены методы мандатов/списаний и события mandate.*.
- docs/spec/state-machine.md: добавлены разделы Проблема/Критерии приёмки/Риски (сенсор required_sections), ссылка на рекуррентный поток.
- Deferred (spine): диспуты — теперь предпосылка для рекуррентных списаний до боевого включения.

REMOVED:
- Ничего не удаляется. Явно: существующие методы/поля/статусы API ТСП сохраняются (проверено contract_diff: breaking 0).

Затронутые защищённые файлы:
- `ARCHITECTURE-SPINE.md` — AD-002/AD-003 расширены, добавлен AD-009.
- `.arch-handoff/CONSTRAINTS.yaml` — добавлены fitness-правила recurring-*.

Let me write it.

Note: delta validate might require certain things. Let me write then validate.

Also: the ADDED bullets should include EARS "When ..., the ... shall ...".

Let me write the DELTA.md file (I read it earlier).
Now the delta specification — the repository's accepted mechanism for changing accepted files:

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && echo \"=== DELTA VALIDATE ===\"; arc, description="Validate delta structure")`

Now validate the delta, run delta_guard, fitness_check, spine_lint, and the gate. Let me run these checks.

First, `arch-be delta validate sbp-recurring-c2b`, then `git add -A -N` and `arch-be gate --route auto --base bench-baseline`.

But careful: there's a Stop hook that runs the gate. I should verify now. Also `delta_guard` via gate uses `--base bench-baseline`? The gate's delta_guard uses base from --base. Good.

Let me run validate + gate.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && git add -A -N >/dev/null 2>&1; echo , description="Run significance from diff and full gate")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && echo \"=== SENSORS ===\"; arch-be co, description="Verify sensors and critical-route gate")`

Gate PASS at Fast route. But note delta_guard says "защищённых среди них: 1 — покрытие: ARCHITECTURE-SPINE.md ← 'sbp-recurring-c2b'". Only 1 protected file detected — CONSTRAINTS.yaml (.arch-handoff/CONSTRAINTS.yaml) may not be counted as protected by default path matching (it looks for "CONSTRAINTS.yaml" maybe at root?). It says protected among changed: 1 (ARCHITECTURE-SPINE.md). So the default protected set is {model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml} but matches root-level CONSTRAINTS.yaml; .arch-handoff/CONSTRAINTS.yaml may not match. Anyway, PASS.

Also note auto route = Fast because the diff detectors don't detect api_contract_change from `openapi/` dir? Interesting — the detector may look for specific patterns. Score 0. So the gate passes easily at Fast. But the change is genuinely Critical by declared triggers (7). The gate's auto detector is a floor, not the truth; the documented declared score is Critical. The gate being Fast is fine for the hook.

However, I want to be sure the gate will pass in the Stop hook. The hook runs `arch-be gate --route auto --base bench-baseline` — same command → PASS. Good.

But wait: sensors didn't run at Fast. If somehow auto route later becomes Standard/Critical, sensors now pass (I fixed state-machine.md). Let me verify sensors pass now: `arch-be control sensors docs/spec`. Let me run to confirm.

Also run fitness_check, spine_lint, delta_guard explicitly via the CLI/gate — already PASS.

Let me also run `arch-be gate --route critical --base bench-baseline` to confirm no NEW failures on Critical (the "Не проверено" is acceptable, but let me ensure extra required components don't FAIL). Earlier on Critical it failed only at sensors. Now sensors should pass. But Critical also may require nfr/evidence — SKIP. Let me test to be safe.

Let me run: sensors docs/spec, gate --route critical.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && arch-be control rules-report 2>&1 | , description="Inspect rules registry report")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wrpc5sz/ws", "base": "bench-baseline"}, name="mcp__spine__delta_guard")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wrpc5sz/ws"}, name="mcp__spine__adr_registry")`

Important: On explicit Critical route, the gate exits INCOMPLETE (exit 3), not PASS. The hook uses `--route auto`, which resolves to Fast (score 0 from diff), so the hook passes. Good.

But: is that acceptable? The gate's auto route is Fast because the diff detectors don't recognize the changes as triggers. Since the hook is what runs, PASS is achieved. However, a reviewer might argue the honest route is Critical and the gate would be INCOMPLETE (missing model/ and evidence). The task is to prepare a package to take to an architecture decision and hand to executors — not necessarily to produce the typed model/evidence bundle. I'll note this in the summary as a follow-up (evidence bundle + model/ needed for A4/Critical gate completeness).

Hmm, but should I make the gate route Critical and satisfy it? That would require creating `model/` typed entities (CMP/AD/REQ/NFR...) and an EVIDENCE.yaml, plus running the model validators. That's a big additional scope, and the user asked for 7 specific outcomes, not for a typed model. The repo has no model/ at all (baseline skipped trace_check/model_validate everywhere). So the repo is at the docs-stage; producing model/ would be a major addition beyond the ask. I'll leave it and report the gap.

Actually wait — let me reconsider the "auto" detector. It returned score 0 even though I added `/v1/mandates` to openapi and new files. The `significance_from_diff` detectors (new_component/new_vendor/api_contract_change/irreversible_migration/new_datastore) apparently keyed on code paths (e.g., src/, package manifests, migrations). Docs-only changes don't trip them. That's consistent with the repo being docs-stage.

So the Stop hook will pass. Good.

Now, let me do quality checks:
1. `arch-be control rules-report` — verify no rules without owner/expiry issues? Existing rules lack owner/expiry too. Let me check the report to ensure my new rules don't create error findings.
2. Run `mcp__spine__fitness_check` (MCP) — but it's no-exec; should pass.
3. `mcp__spine__spine_lint` — pass.
4. `mcp__spine__delta_guard` — pass.
5. Maybe run `arch-be rules suggest` — not needed.

Let me also double-check `arch-be control rules-report` for new findings (e.g., "правило без owner/expiry" — likely warnings only).

Also I should verify that the ADR registry parses my ADRs (`arch-be adr registry`? The CLI has `arch-be control adr` for creation; registry tool is `mcp__spine__adr_registry`). Let me check `mcp__spine__adr_registry` to ensure ADR-008/009 parse headers (Status/Date) correctly — adr-authoring mentioned `prose_header_unparsed`. My headers use `- Date:` and `- Status:` and `- Model-author:`. Should parse.

Let me run rules-report and adr_registry.

Also: the delta mentions `.arch-handoff/CONSTRAINTS.yaml` but delta_guard only counts ARCHITECTURE-SPINE.md as protected. Fine.

Let me run these verification tools.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && arch-be control rules-report . 2>&1 , description="Rules registry report with repo arg")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wrpc5sz/ws", "base": "bench-baseline"}, name="mcp__spine__fitness_check")`

ADR registry: 9 entries, my ADR-008/009 parse correctly (Proposed, dates). The one finding (exception_unjustified on ADR-005) is pre-existing, not mine.

Now rules-report needs REPO arg. Let me run `arch-be control rules-report .`.

Also let me run fitness_check via MCP to be thorough. And I should run `spine_lint` — already PASS in gate.

Let me run rules-report . and fitness_check.

Also, I want to check the `mcp__spine__rules_suggest` for candidate rules I might have missed (optional). And `mcp__spine__change_impact` (needs model/, will report gaps). Maybe skip.

Let me run rules-report and fitness_check.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/.arch-handoff/CONSTRAINTS.yaml")`

All PASS. No weakening. Rules-report notes 0 behavioral checks — pre-existing pattern in this docs-stage repo (existing 7 rules also had 0). I could add owner/expiry to my new rules to be a good citizen (fitness-functions skill: "авторинг правил... owner/expiry"). But baseline rules lack them too; and `rules_report` doesn't fail. Adding owner/expiry to my new rules would improve quality. Should I? The skill mentions expiry and owner as good practice; the report lists rules without owner/expiry as findings. Since I'm adding rules, let me add `owner` and `expiry` to my new rules — low risk, improves report. But careful: does `owner`/`expiry` field exist in the schema? The report reads "owner, expiry, exclude_glob, effort_hours". Let me check the rules schema support — e.g., `arch-be rules template` output has `verified_by`. Let me check an example of owner/expiry usage. The fitness-function-catalog skill mentioned 7-field card. Let me just add `owner:` and `expiry:` fields and re-run fitness_check to ensure schema accepts them (it might error on unknown fields). 

Hmm, risk: unknown field might cause YAML schema error in fitness_check → gate FAIL. Let me test carefully. Actually, I'll check the reported fields suggest they're supported. But to minimize risk, maybe skip — the baseline repo doesn't use them, and the task doesn't ask. The report's finding is informational only and doesn't fail.

Actually, being a good architect, adding owner/expiry is appropriate. Let me test on one rule and run fitness_check; if it fails, revert. Let me add to all recurring rules: owner "solution-architect (платёжный контур)" and expiry "2026-12-31". Hmm, expiry means the rule is reviewed by then. For docs-stage verification rules, expiry 2027-03-31 might be better. Let me use 2027-03-31.

Wait — "Просроченные правила (expiry в прошлом)" — if I set a future date it's fine.

Let me add owner/expiry to all 7 recurring rules and re-run. Actually, to keep it minimal and avoid risk, let me add to all 7. Let me test.

Hmm, but if the schema doesn't accept `owner`, fitness_check may fail. Let me quickly test by editing one rule first, run, then proceed. Actually I'll add to all and run; if fail, remove. Let me do it.

Actually, let me reconsider whether it's worth the risk/time. The gate currently passes. The report finding "Правила без owner/expiry" includes the 7 baseline rules too — so it's the repo's existing state. Adding owner/expiry only to mine would be inconsistent but better. I'll add them — it's aligned with the fitness-functions methodology and the rules-report explicitly flags it. Let me test schema support.

Let me edit CONSTRAINTS.yaml to add owner/expiry to the 7 new rules.

Let me read the current file to edit precisely.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="  # --- Изменение sbp-recurring-c2b: рекуррентные C2B-списания по мандату ---\n  - name: recurring-spine-invariant\n    type: must_contain\, old_string="  # --- Изменение sbp-recurring-c2b: рекуррентные C2B-списания по мандату ---\n  - name: recurring-spine-invariant\n    type: must_contain\)`

Let me add owner/expiry. I'll test the schema by adding to all and running fitness_check. If it errors, I'll revert.

Actually, let me be more careful: I'll add owner/expiry and one `verified_by` maybe. Just owner/expiry.

Let me rewrite the recurring block.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && arch-be control check . 2>&1 | tail , description="Verify owner/expiry fields accepted")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisaniy, old_string="- Model-author: human:qwen-solution-architect", new_string="- Author-model: human:qwen-solution-architect")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/adr/ADR-009-soglasie-platelschika-man, old_string="- Model-author: human:qwen-solution-architect", new_string="- Author-model: human:qwen-solution-architect")`

owner/expiry accepted; only baseline rules now lack them. Good.

Now final gate run to confirm everything still passes after the CONSTRAINTS edit (fingerprint changed → rule_weakened recheck). Let me run the full gate auto again.

Also, I should double check the ADR-008 file's `Model-author` line — adr-authoring says format `- Model-author: <model>` or `- Author-model:`. I used `- Model-author: human:qwen-solution-architect`. Hmm, actually the skill says `- Модель-автор: claude-opus-4` · `- Author-model: human`. Is `Model-author` recognized? The parse may look for specific keys. If unrecognized, it may produce `prose_header_unparsed`? But adr_registry parsed date/status fine. The author field only matters for rubric judging. To be safe, let me use `- Author-model: human:qwen-solution-architect`? The skill listed English form as `- Author-model:`. Let me change to `- Author-model:` to be safe (documented form).

Actually the skill says forms: `- Модель-автор: claude-opus-4` · `- Author-model: human`. So `Model-author` is not listed. Let me fix both ADRs to `- Author-model: human:qwen-solution-architect`.

Let me edit both.

Then run final gate. Then do an adversarial self-review (optionally load adversarial-review skill) and produce final summary.

Let me fix the author lines.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && git add -A -N >/dev/null 2>&1; arch-, description="Final gate run")`
  `skill(skill="adversarial-review")`

Now let me run the final gate (auto) and also re-run contract_diff (unchanged) and openapi_lint (unchanged). Let me run gate auto once more.

Also, I realize I should double check that the `docs/spec/state-machine.md` sensor `upstream_coverage` still passes — yes, from earlier sensors run.

Let me run the final verification suite: gate auto, delta validate, adr_registry quickly. Actually gate covers most. Let me run gate auto and paste.

Also, let me do a quick adversarial self-review by loading the `adversarial-review` skill and applying it mentally. Given effort, I'll do a focused review myself rather than a separate agent. But the task said use tools/skills by purpose; adversarial-review is relevant for a package going to committee. Let me load it and then produce findings, potentially fixing gaps.

Actually, let me first run the final gate, then decide.

  `skill(skill="agent-delegation")`

Gate PASS. Now let me do the adversarial review of my own package, looking for real gaps. Since reviewer=author is an antipattern, I could delegate to a subagent for independent review. The task said "могут быть установлены методические навыки и инструменты — используй их по назначению." A proper independent adversarial review would use a subagent. Let me launch an Explore/general-purpose subagent to adversarially review the package (read-only). That adds value and follows the methodology.

Given budget, let me launch one background agent for adversarial review while I finalize. Actually, the result matters for my final answer — I should run it in foreground or wait. Let me run a foreground subagent (run_in_background: false) with a bounded review task. But instructions say "Before writing a delegation prompt, load the agent-delegation skill." Hmm. Let me load agent-delegation to write a good prompt. That's another step. Alternatively, I can do the review myself carefully — but self-review is an antipattern.

Let me be pragmatic: launch a general-purpose subagent with a clear prompt to adversarially review the change package against the repo, read-only, and report findings with evidence. I'll keep it foreground so I can act on findings.

Actually the guidance: "load the agent-delegation skill before writing a delegation prompt". Let me do that quickly, then launch.

Let me load agent-delegation.

  `agent(description="Adversarial review of change package", subagent_type="general-purpose", run_in_background=false)`

Let me launch an independent adversarial reviewer subagent (general-purpose, read-only) with a detailed prompt. Foreground to get result inline.

Prompt should include: repo path, the change package files, the task, lenses, output format READY/NOT-READY with evidence. Emphasize read-only (no edits), and to check specific things: contract compatibility, invariant consistency, gaps, "miracle steps", regulatory, NFR measurability, rollback.

Let me launch run_in_background: false so I get result inline.

Actually, per the Agent tool description, top-level regular subagents run in background by default; set run_in_background: false to get inline. Let me do that.

Let me write a thorough prompt.
Let me commission an independent adversarial review of the package before finalizing:

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/spec/subscription-lifecycle.md", new_string="| **Плановое списание** | Одно списание в рамках мандата; является платежом статусной машины | `chargeId`, `mandateId`, `periodKey`, `amoun, old_string="| **Плановое списание** | Одно списание в рамках мандата; является платежом статусной машины | `chargeId`, `mandateId`, `periodKey` (напр. )`

Excellent — the independent review found real, valid issues. I should fix the blockers and majors that are within my scope (docs/contract consistency). Let me triage:

1. [blocker] Refund of in-flight charge when mandate revoked: model gap. Fix: define policy explicitly in the spec and solutioning, and/or add a state-model provision. Since the human decision exists (§10 item 3), but the reviewer notes two of three options are unimplementable. I need to make the model support the options. Options:
   - The debit is initiated only when mandate ACTIVE; once initiated and the payer bank has debited, the money must be returned if we cannot credit. Add a return path: REVERSED/REFUNDED from PAID? The existing SM has `REVERSED` mentioned in ADR-002 canonical states but not in state-machine.md. Actually ADR-002 lists canonical states including REVERSED, but state-machine.md doesn't. I can add a transition: `PAID → REFUNDED` (via compensating return) for the revoked-mandate case, or better: model "guard checks at initiation only; if revocation arrives after confirmation (PAID), we still credit (money already moved) and then, per policy, either keep (completed obligation) or auto-refund". 
   
   Cleanest fix: clarify policy — the guard applies to **initiation** and to **pre-PAID** states. Once the payer bank confirms `PAID` (money debited), the charge is completed into `CREDITED`/`COMPLETED` (AD-005 unaffected), and if policy says refund, it uses the existing refund saga from `COMPLETED`. Revocation prevents *future* charges; an already-confirmed charge is a completed obligation. But is that compliant? Typically revocation stops future debits; an in-flight debit authorized before revocation may complete. To be safe, present both: default policy (complete if PAID; nothing if pre-PAID) and explicit note that refunding a completed charge uses existing refund saga. Remove the "guard on обработке подтверждения до PAID" as blocking PAID, and instead: guard at initiation; at confirmation, if mandate was revoked after initiation but charge not yet PAID, cancel (no money moved — because if not PAID, bank hasn't confirmed debit); if PAID arrived, credit it and (policy) optionally refund via saga.

   Actually the real semantics: PAID notification means bank confirmed the debit. Before PAID, no money moved (the charge is just presented; rejection → FAILED). So the guard "at initiation" is sufficient to prevent unauthorized debits; once presented, if mandate is revoked before PAID, we can cancel the presentation (cancelPaymentLink analog → FAILED/EXPIRED), no money moved. If PAID already arrived, money moved → credit + optional refund. So:
   - Fix §4 wording: guard at initiation (block new), and at confirmation before PAID → cancel presentation (no money). PAID is irreversible → money moved; then either credit (obligation) or refund via existing saga.
   - Fix acceptance criterion wording: "отклонено без движения денег" applies to rejections **before** the charge is presented/confirmed; a charge confirmed `PAID` is not "rejected".
   
   That resolves blocker 1 and 2 coherently.

2. [blocker] Same as above — fix acceptance criterion.

3. [major] Revocation immediacy: add `getMandateStatus` live check before each charge initiation (or before each scheduled run) to NFR/spec, and shorten reconciliation cadence for mandates OR add event. Since protocol TBD, add: "перед инициацией планового списания шлюз запрашивает актуальный статус мандата у ОПКЦ (getMandateStatus) либо полагается на событие mandate.revoked + сверку; целевой режим — live-проверка при инициации". Mark [ТРЕБУЕТ ПРОВЕРКИ]. Add to NFR: "проверка статуса мандата перед списанием — 100%". And reduce reconciliation to, e.g., "не реже ежечасной" like payments? The existing docs say mandate reconciliation daily. To satisfy "0 после отзыва ≤60с", event-based + pre-charge live check is the mechanism. Let me state that.

4. [major] periodKey for WEEK/CUSTOM + manual charges race / maxAmountPerPeriod enforcement. Fix: define periodKey formats: MONTH `YYYY-MM`; WEEK `YYYY-Www` (ISO week); CUSTOM — requires explicit periodKey provided by ТСП, and for CUSTOM the period window is defined by the mandate (`periodLengthDays`?). Also enforce maxAmountPerPeriod atomically at charge creation (sum over period within the same transaction / unique reservation). Add to spec §5 and solutioning §3.3. For manual charges without periodKey: require periodKey for all charges under a mandate (make it required in ChargeRequest) OR define default periodKey from scheduledAt. Better: make `periodKey` required for `POST /mandates/{id}/charges` (align with idempotency). That removes the race. Let me make periodKey required in ChargeRequest and PaymentRequest when origin=recurring. Also add atomic limit enforcement note.

5. [major] DELTA falsely claims docs/contracts/tsp-api.md became v0.2.0 while file unchanged. Fix: either update docs/contracts/tsp-api.md (add a v0.2 note + origin semantics) or reword the delta. Best: update the prose contract `docs/contracts/tsp-api.md` minimally to reference v0.2 and the recurring contract doc, and note QR_ISSUED widening. That makes the claim true and keeps prose/машинный consistent. Let me do that: add a header note and a §3.2 note. Actually careful — the fitness rule `abs-credit-only-from-paid` and `adr-no-placeholders` unaffected. Editing docs/contracts/tsp-api.md is fine (docs file). Let me add:
   - In header: "Версия контракта: 0.2 (рекуррентные списания — аддитивно; см. docs/contracts/tsp-api-recurring-c2b.md)".
   - In §3.2 or §2: note origin.
   Hmm, but minimal: change the version line and add a pointer. Also fix DELTA wording to be precise.

6. [major] Throughput NFR not derivable — add explicit total budget statement: "суммарная нагрузка (разовые + плановые) не превышает бюджета docs/nfr.md 200/500 TPS; доля плановых ≤ 100/300" and note volume model required to verify. Add a dependency: "модель объёма мандатов". That's honest.

7. [major] NFR 100% accuracy vs catch-up window. Fix: change "Точность планировщика (должные списания) 100%" to "доля восполненных в пределах catch-up окна — 100%; за пределами окна — сверка и ручной разбор". Or define accuracy as "100% кроме остановок дольше catch_up_horizon (инцидент)". Let me reword.

8. [major] Rollback magic step: mass freeze not available. Fix: add a defined administrative operation: "административная операция stop-new (глобальный фиче-флаг приёма/списаний) — массовая заморозка через флаг, а не поштучные revoke; поштучный revoke — для отдельных ТСП". State owner. Add to rollback plan and delta. Also add `suspend`/mass-freeze as internal admin capability (not necessarily TSP API).

9. [minor] SUSPENDED no trigger/owner → state that suspend is internal (антифрод/оператор, 4-eyes), not TSP API in v1; keep as open question. Fix wording: "приостановка — внутренняя административная операция (антифрод/SRE, 4-eyes); в TSP API v0.2 не выставляется".

10. [minor] AD-003 Binds says consentRef idempotency vs spec eventId+mandateId. Fix: align — change spine AD-003 Binds to "подтверждение/отзыв согласия (`eventId` + `mandateId`)". Actually consent dedup key is eventId (+mandateId); `consentRef` is the confirmation link, not the key. Let me fix spine text.

11. [minor] mandate.revoked mixes payer revoke and TSP cancel without actor field → add `actor` field (`PAYER`|`TSP`|`BANK`) to event and to revoke response; show TSP-revoke→cancelMandate flow. Fix: add actor field, add a short flow note.

12. [minor] payer notification of upcoming charge — component/owner missing. Fix: add to gaps/open questions as explicit dependency with owner (продукт/ИБ), not a component.

13. [minor] DELTA ADDED doesn't mention PENDING_OPKC. Fix: add a line.

Also from question 6: does docs/contracts/tsp-api.md get updated? Yes, fix #5 updates it.

This is a fair amount of edits. All are in docs (and spine). Let me apply them. The spine edit means delta must mention it (it does). Let me be efficient and batch edits.

Let me also re-run the gate at the end.

Let me start with the spec `subscription-lifecycle.md` edits (blockers 1,2,4,7,9,11,13):
- §4: rewrite the revocation/in-flight semantics.
- §1: periodKey formats.
- §5: idempotency table (periodKey required, atomic limit).
- §2 SUSPENDED note.
- §6 alignment with NFR accuracy.
- Критерии приёмки: fix "без движения денег" wording.

Let me read the file section to edit precisely. I have the content from writing it. Let me do targeted edits.

Edit A — §1 entity table: periodKey definition. Current:
"| **Плановое списание** | Одно списание в рамках мандата; является платежом статусной машины | `chargeId`, `mandateId`, `periodKey` (напр. `2026-09`), `amount`, `paymentId`, `scheduledAt`, `origin=recurring` |"

I'll add a line after the table defining periodKey formats.

Edit B — §2 SUSPENDED.
Edit C — §4 forbidden transitions (revocation semantics).
Edit D — §5 idempotency + limit atomic.
Edit E — §6 catch-up/NFR alignment.
Edit F — Критерии приёмки wording.

Then solutioning doc edits (§3.3 atomic limit; §10 policy; add pre-charge status check).
Then nfr doc edits (throughput, accuracy, revocation mechanism, notification dependency).
Then contract doc edits (periodKey required, actor field, TSP-revoke flow, suspend note).
Then openapi (ChargeRequest periodKey required; PaymentRequest periodKey? keep optional but note; MandateStatus already has values).
Then DELTA edits (periodKey, PENDING_OPKC, rollback mass freeze, version claim, accuracy).
Then spine AD-003 Binds fix.
Then docs/contracts/tsp-api.md v0.2 note.

That's a lot but let's go. I'll do them carefully.

Let me start.

Edit A: after the entity table, add periodKey definition paragraph. I'll anchor on the table's last row + the following "## 2. Статусная модель мандата".

Actually the entity table ends and then "## 2. Статусная модель мандата". Let me edit by replacing the plановое списание row to include format, then insert a definition line before "## 2".

Let me do a combined edit replacing the row + heading.

Current text:
```
| **Плановое списание** | Одно списание в рамках мандата; является платежом статусной машины | `chargeId`, `mandateId`, `periodKey` (напр. `2026-09`), `amount`, `paymentId`, `scheduledAt`, `origin=recurring` |

## 2. Статусная модель мандата
```
New:
```
| **Плановое списание** | Одно списание в рамках мандата; является платежом статусной машины | `chargeId`, `mandateId`, `periodKey`, `amount`, `paymentId`, `scheduledAt`, `origin=recurring` |

Формат `periodKey` (однозначно задаёт период и ключ идемпотентности):
- `period=MONTH` → `YYYY-MM` (напр. `2026-09`);
- `period=WEEK` → `YYYY-Www` (ISO-неделя, напр. `2026-W40`);
- `period=CUSTOM` → `periodKey` задаёт ТСП явно (строка ≤ 64 символов), окно периода определяется мандатом (`periodLengthDays`).

Для любого планового или ручного списания `periodKey` **обязателен** — он же ключ идемпотентности и знаменатель лимита `maxAmountPerPeriod`.

## 2. Статусная модель мандата
```

Edit B: SUSPENDED row: currently "| `SUSPENDED` | Приостановлен ТСП/шлюзом (напр. по антифрод-сигналу) | нет |". Change to "Приостановлен внутренней административной операцией (антифрод/оператор, 4-eyes); в API ТСП v0.2 не выставляется".

Edit C: §4. Current:
```
- **Списание невозможно, если мандат не в `ACTIVE`** или истёк `validTo` (AD-009). Проверяется guard'ом на инициации и на обработке подтверждения до `PAID`.
...
- После `REVOKED`/`EXPIRED`/`SUSPENDED` новые списания недостижимы; уже подтверждённые (`PAID` и далее) не откатываются назад — корректировка только возвратом (сага, ADR-005).
```
Rewrite the first bullet and the last bullet to be precise:

```
- **Списание не инициируется, если мандат не в `ACTIVE`,** истёк `validTo` или превышены лимиты (AD-009). Проверка выполняется **на инициации** списания по актуальному статусу мандата (см. §5, §6).
- Если отзыв пришёл **после инициации, но до `PAID`**, предъявление списания закрывается (`FAILED`/`EXPIRED`) — деньги не двинуты (банк плательщика не подтвердил списание).
- `PAID` необратим: если банк плательщика уже подтвердил списание, деньги двинуты; такое списание доводится до `CREDITED`/`COMPLETED` (AD-005), а возврат при необходимости выполняется существующей сагой возврата из `COMPLETED` (ADR-005, T11/T12 в `state-machine.md`) — не «откатом» статуса.
- После `REVOKED`/`EXPIRED`/`SUSPENDED` новые списания недостижимы.
```

Edit D: §5 idempotency table — update rows. Current:
```
| Инициация планового списания | `(mandateId, periodKey)` | возврат существующего `paymentId`, второй платёж не создаётся |
| Ручное списание ТСП под мандатом | `Idempotency-Key` ТСП | возврат того же `paymentId` |
```
New:
```
| Инициация планового списания | `(mandateId, periodKey)` | возврат существующего `paymentId`, второй платёж не создаётся |
| Ручное списание ТСП под мандатом | `Idempotency-Key` ТСП + обязательный `periodKey` | возврат того же `paymentId`; лимит периода проверяется атомарно с созданием |
```
And add a bullet after the table:
```
Лимит `maxAmountPerPeriod` проверяется **атомарно** с созданием списания (единая транзакция с учётом уже созданных за тот же `mandateId`+`periodKey`), поэтому параллельные ручные списания не могут суммарно превысить лимит; уникальный индекс `(mandateId, periodKey)` дополнительно исключает дубль планового списания.
```

Edit E: §6 catch-up line currently:
"- Пропущенное плановое списание (мандат `ACTIVE`, списания за период нет) — видно в отчёте незавершённых операций планировщика; восстановление — догоняющий прогон (catch-up), ограниченный окном `catch_up_horizon` (по умолчанию — один период)."
Add clarification aligning with NFR: "В пределах `catch_up_horizon` пропущенные списания создаются (точность 100 %); за пределами окна (простой дольше окна) — недосозданные списания попадают в отчёт как инцидент с ручным разбором (NFR: `docs/nfr-recurring-c2b.md`)."

Also §6 add mandate live check: add bullet "- Перед инициацией списания шлюз использует актуальный локальный статус мандата; для гарантии «ноль списаний после отзыва» при потере события — live-проверка статуса мандата у ОПКЦ (`getMandateStatus`) в рамках регламента сверки (целевой режим — перед каждым списанием) `[ТРЕБУЕТ ПРОВЕРКИ]`."

Edit F: Критерии приёмки wording. Current:
"- Списание при `SUSPENDED`/`REVOKED`/`EXPIRED`/истёкшем `validTo` или превышении лимита отклоняется без движения денег (негативный тест на каждый случай)."
New:
"- Списание **не инициируется** при `SUSPENDED`/`REVOKED`/`EXPIRED`/истёкшем `validTo` или превышении лимита (негативный тест на каждый случай); отклонение до `PAID` денег не двигает.
- Отзыв после инициации, но до `PAID` → предъявление закрыто (`FAILED`/`EXPIRED`), денег не двинуто; отзыв после `PAID` → списание доводится до `COMPLETED`, возврат — сагой (тест на оба случая)."

Also the §7 maybe fine.

Let me apply these edits to subscription-lifecycle.md.

I'll do them as separate edit calls. Let me go.
The review found real defects. Let me fix them, starting with the state/lifecycle model (blockers 1–2, majors 4, 7, 9, 11):

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/spec/subscription-lifecycle.md", new_string="| `SUSPENDED` | Приостановлен **внутренней административной операцией** (антифрод/оператор, 4-eyes); в API ТСП v0.2 не выставляется | нет |, old_string="| `SUSPENDED` | Приостановлен ТСП/шлюзом (напр. по антифрод-сигналу) | нет |")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/spec/subscription-lifecycle.md", offset=50, limit=50)`

Now §4 rewrite. Let me read the current §4 block to edit exactly.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/spec/subscription-lifecycle.md", new_string="## 4. Запрещённые переходы (инварианты)\n\n- **Списание не инициируется, если мандат не в `ACTIVE`,** истёк `validTo` или превышены лимиты , old_string="## 4. Запрещённые переходы (инварианты)\n\n- **Списание невозможно, если мандат не в `ACTIVE`** или истёк `validTo` (AD-009). Проверяется g)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/spec/subscription-lifecycle.md", new_string="| Инициация планового списания | `(mandateId, periodKey)` | возврат существующего `paymentId`, второй платёж не создаётся |\n| Ручное списа, old_string="| Инициация планового списания | `(mandateId, periodKey)` | возврат существующего `paymentId`, второй платёж не создаётся |\n| Ручное списа)`

Now §5 and §6 and Критерии приёмки edits.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/spec/subscription-lifecycle.md", new_string="- Мандат не становится `ACTIVE` без подтверждения ОПКЦ; из `PENDING_CONSENT` списание невозможно (негативный тест).\n- Списание **не иниции, old_string="- Мандат не становится `ACTIVE` без подтверждения ОПКЦ; из `PENDING_CONSENT` списание невозможно (негативный тест).\n- Списание при `SUSPEN)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/solutioning-recurring-c2b.md", new_string="### 3.3 Защита от дубля и несанкционированного списания\n\n- **Детерминированный ключ** `(mandateId, periodKey)` + уникальный индекс в БД →, old_string="### 3.3 Защита от дубля и несанкционированного списания\n\n- **Детерминированный ключ** `(mandateId, periodKey)` + уникальный индекс в БД →)`

Now update the solutioning doc: §3.3 atomic limit + pre-charge status check; §10 policy item 3 rewrite (now resolved in spec, so change item 3 to a narrower human decision or remove). Let me align: §10 item 3 said "судьба инициированного, но не подтверждённого списания при отзыве: отменять / доводить / возврат — человеческий выбор". Now the spec defines default semantics. I should update item 3 to: "политика возврата для уже подтверждённого (PAID) списания при отзыве: оставлять как выполненное обязательство или инициировать возврат сагой (коммерческо-регуляторный выбор; модель поддерживает оба)". That's honest and narrow.

Also §3.3: add atomic limit + live status check.

Let me edit solutioning §3.3 and §10.

Current §3.3:
```
### 3.3 Защита от дубля и несанкционированного списания

- **Детерминированный ключ** `(mandateId, periodKey)` + уникальный индекс в БД → второй платёж невозможен даже при двойном прогоне планировщика или рестарте.
- **Guard мандата** на инициации и на обработке подтверждения до `PAID` (локальный статус + сверка).
- **Без fallback** ...
```

Change bullet 2 and add bullet:
- **Guard мандата на инициации**: проверка ACTIVE/срока/лимитов до создания списания; лимит периода проверяется атомарно; при отзыве после инициации, но до `PAID`, предъявление закрывается; после `PAID` списание доводится, возврат — сагой.
- **Live-проверка статуса мандата** (`getMandateStatus`) как целевой режим перед инициацией — для «ноль списаний после отзыва» при потере события `[ТРЕБУЕТ ПРОВЕРКИ]`.

Let me edit.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/solutioning-recurring-c2b.md", new_string="3. **Политика возврата для уже подтверждённого (`PAID`) списания при отзыве**: оставить как выполненное обязательство либо инициировать воз, old_string="3. **Судьба инициированного, но не подтверждённого списания при отзыве**: отменять до `PAID` / доводить до конца / возврат после зачисления)`

Now §10 item 3 in solutioning. Let me find the exact text:
"3. **Судьба инициированного, но не подтверждённого списания при отзыве**: отменять до `PAID` / доводить до конца / возврат после зачисления — регуляторно-коммерческий выбор."

Replace with:
"3. **Политика возврата для уже подтверждённого (`PAID`) списания при отзыве**: оставить как выполненное обязательство либо инициировать возврат существующей сагой — регуляторно-коммерческий выбор (модель поддерживает оба; отмена до `PAID` определена спецификацией и выбора не требует)."

Let me edit.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/nfr-recurring-c2b.md", new_string="| Точность планировщика | 100 % должных списаний создано в пределах окна `catch_up_horizon`; простой дольше окна — инцидент с ручным разбор, old_string="| Точность планировщика (должные списания) | 100 % создано | Сверка плана и факта | Недобор выручки ТСП |\n| Дубли на `(mandateId, periodKe)`

Now update the NFR doc: throughput (fix #6), accuracy (fix #7), revocation mechanism (#3 → add pre-charge status check metric), notification dependency (#12 owner), and add volume-model dependency.

Current NFR §1 rows:
"| Точность планировщика (должные списания) | 100 % создано | Сверка плана и факта | Недобор выручки ТСП |"
"| Throughput плановых списаний (доля бюджета шлюза) | sustained ≤ 100 TPS, burst ≤ 300 TPS | Нагрузочный тест | Выход за бюджет шлюза 200/500 TPS |"

§2:
"| Блокировка новых списаний после отзыва | ≤ 60 с (p99); новых списаний после отзыва — **0** | Тест отзыва + контроль списаний | Несанкционированное списание |"

Let me edit:

Accuracy row → "| Точность планировщика | 100 % должных списаний создано в пределах окна `catch_up_horizon`; простой дольше окна — инцидент с ручным разбором | Сверка плана и факта | Недобор выручки ТСП (в пределах окна — ноль) |"

Throughput row → "| Throughput плановых списаний | sustained ≤ 100 TPS, burst ≤ 300 TPS — при условии, что **суммарная** нагрузка (разовые + плановые) не превышает бюджет `docs/nfr.md` (200/500 TPS); доля плановых выводится из модели объёма мандатов | Нагрузочный тест с профилем «разовые + плановые» | Выход за бюджет шлюза; деградация разового приёма |"

Revocation row → "| Блокировка новых списаний после отзыва | ≤ 60 с (p99); новых списаний после отзыва — **0**; статус мандата проверяется перед каждой инициацией (live-проверка `getMandateStatus`, целевой режим) | Тест отзыва (в т.ч. потеря события) + контроль списаний | Несанкционированное списание |"

Add §1 row for live status check latency? Optional. Add row: "| Live-проверка статуса мандата перед инициацией | p95 < 1 с (включая ОПКЦ) `[ТРЕБУЕТ ПРОВЕРКИ]` | Метрика планировщика | Задержка списаний / несанкционированные списания |". Hmm — but if live check is inside the call, it adds latency to scheduler, not to API. Let me add it to §1.

Add dependency: volume model. In "Зависимости" section add:
"- Модель объёма и распределения мандатов по датам (сколько активных мандатов, распределение `scheduledAt`) — без неё лаг/throughput/catch-up не проверяемы; владелец — продукт/ТСП-аналитика."
And notification:
"- Требования к уведомлению плательщика о предстоящем списании (компонент/канал) — владелец: продукт + ИБ `[ТРЕБУЕТ ПРОВЕРКИ]`."

Let me edit the NFR doc.
Now correcting the NFR contradictions and gaps:

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/nfr-recurring-c2b.md", new_string="| Блокировка новых списаний после отзыва | ≤ 60 с (p99); новых списаний после отзыва — **0**; статус мандата проверяется перед каждой иници, old_string="| Блокировка новых списаний после отзыва | ≤ 60 с (p99); новых списаний после отзыва — **0** | Тест отзыва + контроль списаний | Несанкцион)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/nfr-recurring-c2b.md", new_string="- Требования ЦБ к уведомлению плательщика о предстоящем списании и к хранению согласий `[ТРЕБУЕТ ПРОВЕРКИ]`.\n- **Модель объёма и распредел, old_string="- Требования ЦБ к уведомлению плательщика о предстоящем списании и к хранению согласий `[ТРЕБУЕТ ПРОВЕРКИ]`.")`

Now add dependencies (volume model, payer notification). Current dependencies section:
```
## Зависимости (внешние входы)

- Регламенты НСПК по рекуррентному C2B (тайминги подтверждения/отзыва, лимиты сумм и периодов) `[ТРЕБУЕТ ПРОВЕРКИ]`.
- SLA АБС на зачисление/списание для рекуррентных документов (согласуется с владельцем АБС).
- Требования ЦБ к уведомлению плательщика о предстоящем списании и к хранению согласий `[ТРЕБУЕТ ПРОВЕРКИ]`.
```
Add:
"- Модель объёма и распределения мандатов по датам — без неё лаг/throughput/catch-up не проверяемы (владелец: продукт/аналитика ТСП).
- Компонент и канал уведомления плательщика о предстоящем списании (владелец: продукт + ИБ) `[ТРЕБУЕТ ПРОВЕРКИ]`."

Let me edit.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/contracts/tsp-api-recurring-c2b.md", new_string="**`ChargeRequest`**\n```json\n{\n  \"amount\": 49900,\n  \"periodKey\": \"2026-10\",               // обязателен: ключ идемпотентности и зн, old_string="**`ChargeRequest`**\n```json\n{\n  \"amount\": 49900,\n  \"periodKey\": \"2026-10\",               // опц.; задаёт идемпотентность списания)`

Now contract doc: periodKey required for charges (#4), actor field on mandate.revoked (#11), TSP-revoke flow (cancelMandate), suspend note (§9), and mention docs/contracts/tsp-api.md version update (#5).

Edits in `docs/contracts/tsp-api-recurring-c2b.md`:
- §3 ChargeRequest: make periodKey required, note it's mandatory.
- §6 events: add `actor` field to mandate events; show TSP-revoke→cancelMandate flow.
- §9 open questions: adjust suspend/resume — already there (item 3).
- Add a note that `docs/contracts/tsp-api.md` prose is updated to v0.2.

Let me edit ChargeRequest block:
Current:
```
**`ChargeRequest`**
```json
{
  "amount": 49900,
  "periodKey": "2026-10",               // опц.; задаёт идемпотентность списания
  "description": "Внеплановое списание"
}
```
```
New: remove "опц." → "обязателен; ключ идемпотентности и знаменатель лимита периода".

Also §2 table row for charges says "Ручное (внеплановое/повторное) списание". Fine.

Events: current body example mandate.activated. Add actor to mandate.revoked description and body. Let me add a paragraph:
"Поля события мандата включают `actor` (`PAYER` | `TSP` | `BANK`) — для аудита источника перехода; `mandate.revoked` от плательщика приходит от ОПКЦ, отмена ТСП инициируется через `POST /v1/mandates/{mandateId}/revoke` → шлюз вызывает `cancelMandate` адаптера → ОПКЦ подтверждает событием `mandate.revoked` с `actor=TSP`."

Let me edit.

Also, the response of revoke: update Mandate example? Minor. Add actor in the event body example.

Let me do the edits.
Now the contract document fixes (required periodKey, revocation actor/flow):

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/contracts/tsp-api-recurring-c2b.md", new_string="Тело события (`mandate.activated`):\n```json\n{\n  \"eventId\": \"evt_…\",\n  \"type\": \"mandate.activated\",\n  \"mandateId\": \"man_5a6b, old_string="Тело события (`mandate.activated`):\n```json\n{\n  \"eventId\": \"evt_…\",\n  \"type\": \"mandate.activated\",\n  \"mandateId\": \"man_5a6b)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/openapi/tsp-api.yaml", new_string="    ChargeRequest:\n      type: object\n      required: [amount, periodKey]\n      properties:\n        amount: {type: integer, description, old_string="    ChargeRequest:\n      type: object\n      required: [amount]\n      properties:\n        amount: {type: integer, description: Сумма в к)`

Now openapi: make ChargeRequest.periodKey required. Also add `actor` to mandate event? The openapi file doesn't define webhook schemas (the prose contract does). So only ChargeRequest required update. Also maybe add `period` values already fine.

Let me edit openapi ChargeRequest: `required: [amount]` → `required: [amount, periodKey]`.

Let me also add `periodLengthDays` to MandateRequest/Mandate for CUSTOM? The spec references `periodLengthDays` for CUSTOM. To keep consistency, add optional `periodLengthDays` to MandateRequest (required when period=CUSTOM — can't express conditional easily in 3.0; just document). Let me add it.

Let me edit openapi.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/openapi/tsp-api.yaml", new_string="        period: {type: string, enum: [MONTH, WEEK, CUSTOM]}\n        periodLengthDays: {type: integer, description: \"Окно периода в днях; , old_string="        period: {type: string, enum: [MONTH, WEEK, CUSTOM]}\n        validTo: {type: string, format: date-time}\n        description: {type)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/openapi/tsp-api.yaml", new_string="        period: {type: string, enum: [MONTH, WEEK, CUSTOM]}\n        periodLengthDays: {type: integer, nullable: true}\n        validFrom: , old_string="        period: {type: string, enum: [MONTH, WEEK, CUSTOM]}\n        validFrom: {type: string, format: date-time, nullable: true}")`

Add `periodLengthDays` to MandateRequest and Mandate schema. Let me edit both.

MandateRequest period line: `period: {type: string, enum: [MONTH, WEEK, CUSTOM]}`. Add after it: `periodLengthDays: {type: integer, description: "Окно периода в днях; обязателен при period=CUSTOM"}`.

Mandate: same.

Let me do targeted edits (the two occurrences differ by context — MandateRequest has `validTo` after; Mandate has `validFrom`). Let me use replace with context.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/contracts/tsp-api.md", new_string="# Контракт API ТСП (мерчант-API) — v0.2\n\n- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.2 (добавлены рекуррентные списани, old_string="# Контракт API ТСП (мерчант-API) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фикс)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/docs/contracts/tsp-api.md", new_string="Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (AD, old_string="Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (AD)`

Now update `docs/contracts/tsp-api.md` prose to v0.2 (fix #5). Add a header note and a note in §3.2/§3.3? Minimal: change version line and add a pointer + `origin` semantics.

Current header:
```
# Контракт API ТСП (мерчант-API) — v0.1 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), AD-003 (spine)
```

Change to:
```
# Контракт API ТСП (мерчант-API) — v0.2

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (добавлены рекуррентные списания по мандату — аддитивно; см. `docs/contracts/tsp-api-recurring-c2b.md` и `openapi/tsp-api.yaml` v0.2.0)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008/ADR-009 (рекуррентные списания), AD-003, AD-009 (spine)
```

Also add note in §3.2 or a new subsection about origin=recurring. Let me add to §3.2 "Правила:" a sentence? Actually the recurring contract doc covers it. To be safe and honest, add a short paragraph after §3.2 note:
"Для рекуррентных списаний (`origin=recurring`) `qrId`/`qrUrl`/`qrImage` не возвращаются, а `status=QR_ISSUED` означает «предъявлено банку плательщика»; методы мандатов — `docs/contracts/tsp-api-recurring-c2b.md`."

Let me find the anchor in §3.2. The note paragraph:
"Примечания: регистрация ТСП в ОПКЦ выполняется асинхронно через адаптер; ..." — that's §3.1.
§3.2 ends with:
"Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (ADR-002). Максимальная сумма — по лимитам НСПК [ТРЕБУЕТ ПРОВЕРКИ]."

I'll append a sentence to that paragraph.

Let me edit both.
Now updating the base prose contract to reflect v0.2 (resolves the delta's version claim):

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/ARCHITECTURE-SPINE.md", new_string="- **Binds**: вход ТСП (`Idempotency-Key`), нотификации НСПК (`eventId`), вызовы АБС (`paymentId`/`refundId`), плановое списание (`mandateId, old_string="- **Binds**: вход ТСП (`Idempotency-Key`), нотификации НСПК (`eventId`), вызовы АБС (`paymentId`/`refundId`), плановое списание (`mandateId)`

Now fix spine AD-003 Binds (#10): "согласие плательщика (`consentRef`)" → "подтверждение/отзыв согласия (`eventId` + `mandateId`)". Let me edit.

Also fix DELTA: 
- version claim (#5) — now docs/contracts/tsp-api.md IS v0.2, so claim is true. Good. But the DELTA said "было v0.1.0, стало v0.2.0" referring to API ТСП (docs + openapi) — now accurate.
- ADDED add PENDING_OPKC (#13).
- rollback mass freeze (#8).
- accuracy wording in criteria? The delta criteria doesn't state 100% accuracy; it references NFR. Fine.

Let me edit spine AD-003 Binds.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/changes/sbp-recurring-c2b/DELTA.md", new_string="- When ТСП отправляет `POST /v1/mandates` с валидным `Idempotency-Key`, the шлюз shall создать заявку на мандат в статусе `PENDING_CONSENT`, old_string="- When ТСП отправляет `POST /v1/mandates` с валидным `Idempotency-Key`, the шлюз shall создать заявку на мандат в статусе `PENDING_CONSENT`)`

Now DELTA.md edits:
1. ADDED: add a line about PENDING_OPKC.
2. Rollback: mass freeze via admin flag, owner.
3. Maybe add pre-charge live check criterion already in ADDED? Currently ADDED has revocation ≤60s. Add "перед инициацией проверяется статус мандата".

Let me read DELTA relevant parts and edit.

For ADDED, add after the revocation bullet:
"- When шлюз инициирует плановое списание, the шлюз shall проверить статус мандата (локально и, в целевом режиме, live-запросом `getMandateStatus`) и не создавать списание вне `ACTIVE`/лимитов."

Add PENDING_OPKC: in ADDED, after first mandate bullet:
"- When ОПКЦ принимает заявку на мандат, the шлюз shall перевести мандат в `PENDING_OPKC` до получения подтверждения (списания запрещены)."

Rollback edits: current п.2 "остановить планировщик (глобально или по ТСП)". Add explicit admin stop-new + mass freeze:
"2. **После включения**: административная операция **stop-new** (глобальный фиче-флаг приёма/списаний + флаг на ТСП) немедленно прекращает новые списания — массово, без поштучных `revoke`; начатые операции доводятся существующим контуром; разовый C2B-приём не затрагивается."
And п.5 "все мандаты в терминальном/замороженном статусе" — add "через admin stop-new/заморозку (владелец — дежурный SRE), поштучный `revoke` — для отдельных ТСП".

Let me edit.

  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/changes/sbp-recurring-c2b/DELTA.md", new_string="2. **После включения**: административная операция **stop-new** (глобальный фиче-флаг приёма списаний + флаг на ТСП) немедленно прекращает н, old_string="2. **После включения**: остановить планировщик (глобально или по ТСП) — новые списания прекращаются; начатые операции доводятся существующи)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wrpc5sz/ws/changes/sbp-recurring-c2b/DELTA.md", new_string="- [ ] Списание **не инициируется** при `SUSPENDED`/`REVOKED`/`EXPIRED`/истёкшем `validTo` или превышении лимита; отклонение до `PAID` денег, old_string="- [ ] Списание при `SUSPENDED`/`REVOKED`/`EXPIRED`/истёкшем `validTo` отклонено без движения денег.\n- [ ] Превышение `maxAmountPerCharge`/)`

Now update the DELTA "Критерии приёмки" for the in-flight wording (blocker 2) to match spec. Current criteria:
"- [ ] Списание при `SUSPENDED`/`REVOKED`/`EXPIRED`/истёкшем `validTo` отклонено без движения денег.
...
- [ ] После `mandate.revoked` — ноль новых списаний; инициированные, но не `PAID`, закрыты по утверждённой политике."

Update to:
"- [ ] Списание **не инициируется** при `SUSPENDED`/`REVOKED`/`EXPIRED`/истёкшем `validTo` или превышении лимита; отклонение до `PAID` денег не двигает.
- [ ] Отзыв после инициации, но до `PAID` → предъявление закрыто, денег не двинуто; отзыв после `PAID` → списание доведено до `COMPLETED`, возврат (если выбран политикой) — сагой.
- [ ] После `mandate.revoked` — ноль новых списаний."

Let me edit. Also the throughput/precision criteria: last criterion mentions NFR reached. Fine.

Let me edit the criteria block.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && echo \"=== DELTA VALIDATE ===\"; arc, description="Re-verify delta, spine, sensors, gate")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wrpc5sz/ws/openapi/tsp-api.yaml"}, name="mcp__spine__openapi_lint")`

Also update the DELTA MODIFIED about `docs/nfr.md` — currently says "не изменяется"; fine.

Also the DELTA "REMOVED" — fine.

Now the contract §9 open question 3 about suspend/resume — fine (kept open). But I stated SUSPENDED is internal in the spec, so the open question about TSP suspend/resume remains valid.

Now re-run all checks: openapi_lint, contract_diff, delta_validate, sensors, gate. Let me run them.

Also, I should double check that `docs/contracts/tsp-api.md` mention of `origin` doesn't break the `abs-credit-only-from-paid` rule (it checks ADR-005 file). Fine.

Let me also verify spine_lint after edits.

Run: delta validate, openapi_lint, contract_diff (regenerate old from git — still same), gate auto, gate critical (to see sensors/INCOMPLETE), spine_lint.

Let me batch.
Re-running verification after the fixes:

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && git show bench-baseline:openapi/tsp-, description="Refresh baseline contract copy")`

All green. Let me re-run contract_diff to confirm still breaking 0 after adding periodLengthDays and making periodKey required in ChargeRequest (adding a required property to a NEW schema is fine; but making periodKey required where it was optional in a NEW schema added in the same version — no old version had it, so no breaking).

Let me run contract_diff quickly.

Then update memory? The task is a one-off; memory not needed unless durable. I'll skip memory (no explicit request).

Let me run contract_diff and then finalize.

Also I want to double-check the ADR-008/009 quality — the adr-authoring skill recommends assessing with rubric ≥3.5. Could run split-judge rubric, but that requires k independent answers. That's heavy. Given time, I'll note it as a next step. Actually, the task item 3 asks for ADR with alternatives/consequences/reversibility — done. I could run `rubric_list` to see if adr_quality rubric exists and maybe `rubric_prompt`/`rubric_verify`. That's a nice-to-have; the user didn't explicitly ask for a rubric score. I'll mention it as optional next step. Hmm — but "используй инструменты по назначению". Given the amount already done, I'll skip the rubric run but could quickly run `rubric_list` to reference. Let me skip to keep focus.

Let me run contract_diff.

  `tool_call(arguments={"format": "openapi", "new": "<HARNESS>/runs-v2/cells/wrpc5sz/ws/openapi/tsp-a, name="mcp__spine__contract_diff")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wrpc5sz/ws && git status --short", description="List created and modified files")`

Everything green. Now let me produce the final summary for the user, covering the 7 requested outcomes and listing created/modified files.

Let me gather the final file list (git status) to be accurate.

Let me run git status --short.


Note: `.arch-handoff/mcp-calls.jsonl` was added (A) — that's the Spine MCP call journal, auto-written by the MCP server (trust metric source). It's a side effect of using MCP tools, not my content. `.qwen/settings.json` was already modified before I started (baseline state, M). I should not touch those. I'll mention them.

Now write final summary in Russian, concise but complete, mapping to the 7 items, plus verification results and the one gap (Critical-route gate incomplete without model/evidence; auto-route Fast). And list files.

Let me also mention the adversarial review and fixes.

Let me write the final answer.
完成。下面是变更的架构包。

## 1. 重要性与路线

已明确考虑 15 个触发器，得分 **7/15 → 路线 Critical**（命令：`arch-be control score --trigger ...`）。包含：`api_contract_change`、`data_contract_change`、`consistency_model_change`、`financial_impact`、`significant_nfr`、`criticality_or_exception`、`new_component`。这意味着需要进行完整的 Solutioning 和 **必须的人工 A3 节点**；delta 可以使用，但仅作为仓库中接受的修改受保护文件的方式。评分理由见 `docs/solutioning-recurring-c2b.md` §1。

## 2. 对已接受架构的影响

在 `ARCHITECTURE-SPINE.md` 中：**AD-002**（唯一事实来源扩展为 mandate+charge）和 **AD-003**（幂等键 `(mandateId, periodKey)`）被扩展，新增了 **AD-009**（仅凭有效 mandate 且在其限额内扣款）。AD-001、AD-004、AD-005、AD-006、AD-007、AD-008 —— **不变**；从 `PAID` 入账这一禁止规则已被明确保留。未变内容清单及向上级 initiative 的升级——§2.2–2.3。

## 3. 架构决策

- `ADR-008` —— 计划和 debits 位于网关核心中（备选方案：单独的“订阅”服务、TSP 侧计划、Vendor box）。
- `ADR-009` —— 同意仅以确认形式存在，撤回是首要场景，PII 令牌化。
两者都包含备选方案、负面后果和可逆性（`costly` / `irreversible`）。

## 4. 合约

`openapi/tsp-api.yaml` 已升级至 **v0.2.0，仅增量**：新增路径 `/v1/mandates*`、可选字段 `origin/mandateId/periodKey`、新事件 `mandate.*`。对 v0.1→v0.2 执行 `contract_diff`：**breaking 0**（7 个非破坏性更改），`openapi_lint` 通过。详情——`docs/contracts/tsp-api-recurring-c2b.md`。

## 5. 可度量的非功能需求

`docs/nfr-recurring-c2b.md`：计划任务滞后 p95 ≤ 5 分钟；双重/未经授权扣款 = 0；撤回后锁定 ≤ 60 秒；同步前实时检查状态；吞吐量作为共享网关预算的一部分；额度对账。已考虑与 `docs/nfr.md` 的一致性。

## 6. 验收标准与回滚

`DELTA.md` + `subscription-lifecycle.md`：负面场景（无 mandate、已撤回、暂停、超额、某期间重复、Webhook 重复、限额竞态）。回滚：功能标志 + 管理员操作 **stop-new**（批量冻结，无需逐笔 revoke），信号为未经授权/重复扣款，所有者为值班 SRE。

## 7. 保留给架构师人工决策

`docs/solutioning-recurring-c2b.md` §9：协议可行性（НСПК）、限额政策、对已确认（PAID）扣款的退款政策、争议边界、在 initiative 层面批准、费率。

## 验证

`arch-be gate --route auto --base bench-baseline` → **PASS**（fitness 14条规则，delta_guard 已覆盖 `ARCHITECTURE-SPINE.md`，spine_lint 0条发现，sensors PASS）；`delta validate`、`openapi_lint`、`contract_diff` —— 绿色。对包进行了独立对抗性审查（子代理）—— 其阻断性/重大发现（撤回时资金边界、期间竞态、NFR 矛盾、回滚中的“魔法步骤”、delta 中关于合同版本的不准确）**已在文档中修复**。

**关于路线的诚实说明：** auto 门禁将变更评估为 Fast（其差分检测器看不到文档），因此目前是绿色；在显式的 Critical 路线下，门禁给出 INCOMPLETE（需 `model/` 和证据包）—— 这是 A4/执行阶段的一步，本次未完成。

## 创建的文件

- `changes/sbp-recurring-c2b/DELTA.md`
- `docs/adr/ADR-008-…`、`docs/adr/ADR-009-…`
- `docs/solutioning-recurring-c2b.md`、`docs/nfr-recurring-c2b.md`
- `docs/spec/subscription-lifecycle.md`
- `docs/contracts/tsp-api-recurring-c2b.md`

## 修改的文件

- `ARCHITECTURE-SPINE.md`（AD-002/AD-003、新 AD-009、contracts/Deferred 部分）
- `.arch-handoff/CONSTRAINTS.yaml`（7 条 `recurring-*` 规则，含 owner/expiry）
- `openapi/tsp-api.yaml`（v0.2.0，增量）
- `docs/contracts/tsp-api.md`（v0.2）、`docs/contracts/opkc-adapter.md`（mandate/扣款方法与事件）
- `docs/spec/state-machine.md`（+ 传感器必需部分、对 recurring 的引用）

附带说明（非我的变更）：`.qwen/settings.json` 在启动前已是修改状态；`.arch-handoff/mcp-calls.jsonl` 是 Spine MCP 调用日志，由服务器自动记录。
