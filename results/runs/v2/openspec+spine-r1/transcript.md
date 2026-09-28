<!-- источник: <HARNESS>/runs-v2/cells/wc2xy6c/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-v2-cells-wc2xy6c-ws/chats/497edde7-bab9-47bc-abc8-81ce41bd2f16.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff/MANIFEST.json")`

I'll start by reading the accepted decision artifacts to ground everything in the current truth.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff/ARCHITECTURE.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff/CONSTRAINTS.yaml")`

Let me read the rest of the repository: docs/, .arch-handoff files, openapi, openspec.

Let me parallelize reading.
Now let me read the solutioning, NFR, handoff rules, and the existing API contract.

  `glob(pattern="**/*", path="<HARNESS>/runs-v2/cells/wc2xy6c/ws")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/openapi/tsp-api.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff/connect-manifest.json")`

Let me read the ADRs, contract, state machine, and openapi. Also the openspec directory, .qwen settings, RUBRIC.yaml, connect-manifest.json.

Let me check the structure of docs, openapi, openspec.

  `glob(path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs", pattern="**/*")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/openspec/config.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.qwen/settings.json")`

Let me read the ADRs (all), docs/contracts, docs/spec/state-machine.md, openspec/config.yaml, .qwen/settings.json, and the skills relevant (significance-routing, adr-authoring, spine-invariants, delta-spec, openspec-propose, handoff-packaging, nfr-design, adversarial-review, readiness-gate, fitness-functions, spine-contracts-gate).

Let me list docs directory.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/adr/ADR-005-integraciya-s-abs-zachisl)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/adr/ADR-007-proposed-a3.md")`

Now let me read the ADRs and contracts. Let me read them in parallel.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/contracts/opkc-adapter.md")`

Now let me read the contracts, state machine, and RFP. Also read key skills: significance-routing, adr-authoring, spine-invariants, delta-spec, handoff-packaging, nfr-design, spine-contracts-gate, openspec-propose skill, adversarial-review, readiness-gate.

Let me read contracts and state machine.

  `skill(skill="significance-routing")`
  `run_shell_command(command="which openspec arch-be node python3 2>&1; echo \"---\"; openspec --version 2>&1 | head -5; echo \"---\"; arch-be --version 2>&1 | head -5", description="Check available CLI tooling")`

Now let me read the key skills. Let me read significance-routing, adr-authoring, spine-invariants, delta-spec, handoff-packaging, nfr-design, spine-contracts-gate, openspec-propose.

I'll invoke the skills via the Skill tool? Actually the skill tool executes the skill. Skill files are also readable. Let me read them directly — but the instruction says "use the Skill tool". However some skills are "project" skills that are just SKILL.md docs. Reading them is legitimate, but let me use Skill tool for the main ones supposed to be invoked. Hmm — the guidance is that when a skill is relevant, invoke the Skill tool. But invoking many skills would load instructions. Let me be strategic.

The task: prepare an architectural package for a change (recurring C2B debits / subscriptions) on top of an accepted decision, using repository conventions (OpenSpec delta specs + spine + handoff). Key skills relevant:
- significance-routing (assessment of significance and route) — critical
- adr-authoring (ADR for the new decision)
- spine-invariants (new AD block)
- delta-spec / openspec-propose (change proposal in openspec/changes)
- nfr-design (measurable NFRs)
- spine-contracts-gate (contract change without breaking consumers)
- handoff-packaging (package to hand off)
- readiness-gate, adversarial-review, rubric-judging maybe
- spine-bundle (evidence)
- fitness-functions (constraints)

The repository conventions: openspec/ directory with changes/ and specs/ (delta spec), .arch-handoff (handoff package), ARCHITECTURE-SPINE.md, docs/adr/, docs/contracts/, docs/nfr.md.

"Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — Accepted decision files should only be changed in the manner accepted in this repo. Meaning: use OpenSpec delta specs (ADDED/MODIFIED/REMOVED) rather than rewriting the truth; spine changes via new AD block with status Proposed; contract changes additively in openapi with a new version bump.

Let me invoke the key skills. First significance-routing (1), then delta-spec/openspec-propose, adr-authoring, spine-invariants, nfr-design, spine-contracts-gate, handoff-packaging.

Let me read the skill files directly to know exact instructions. Actually invoking via Skill tool is the mandated path for relevant skills. But reading is cheaper and equally informative. The mandate says "When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action". I'll invoke the most central ones via the Skill tool. But note: some skill names overlap with commands (openspec-propose etc.). There's a project skill "openspec-propose" and a command "opsx-propose".

Let me think about what actually matters: producing good artifacts. I'll invoke skills: significance-routing, delta-spec, adr-authoring, spine-invariants, nfr-design, spine-contracts-gate, handoff-packaging. That's a lot of context. Let me at least invoke significance-routing, delta-spec, adr-authoring, spine-invariants, handoff-packaging. And check openspec CLI availability.

Actually let's first check available tooling: is `arch-be` and `openspec` CLI installed? Let me check.

Let me start by invoking the significance-routing skill and reading a few skill files.

Actually, the Skill tool invocation loads the skill into conversation. Let me do the most important: significance-routing.

Let me also check the openspec CLI and arch-be availability in parallel via shell.

I'll invoke the skill tool for significance-routing first.
Now let me load the project's methodological skills that govern this work, and check the available tooling.

  `run_shell_command(command="ls ~/.local/bin 2>/dev/null | head -30; echo \"--- pipx ---\"; pipx list 2>/dev/null | head -30; echo \"--- find ---\"; find / -maxdepth 6 , description="Locate arch-be (Spine) binary")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.qwen/skills/delta-spec/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.qwen/skills/openspec-propose/SKILL.md")`

openspec CLI available (1.13.2). arch-be not in PATH (may be installed elsewhere or as python module?). Let me check. The MCP server config uses `arch-be`. Let me check pip/uv.

Let me check `python3 -c "import arch_be"` or find arch-be binary. Also check openspec commands available.

Let me also read the openspec-propose skill and delta-spec skill, plus other skills.

Let me run parallel: check arch-be presence; read skills.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.qwen/skills/adr-authoring/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.qwen/skills/adr-authoring/references/adr-)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.qwen/skills/spine-invariants/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.qwen/skills/spine-invariants/references/s)`

arch-be is at <SPINE_BANK>/target/release/arch-be. The MCP server "spine" is configured but tool list doesn't show spine tools in deferred list... The deferred tools listed don't include spine_* tools. Maybe the MCP server failed to start because arch-be isn't on PATH. Let me check MCP status. Actually the tools available through tool_search are bundled ones only. So Spine MCP may be unavailable. Let me check with a shell command whether arch-be works and whether there are spine CLI commands. But careful: it's a big tool. Let's not overinvest.

Given the task, the critical path is producing the architectural package. The repo conventions: OpenSpec (changes/ with proposal.md, specs delta, design.md, tasks.md), docs/adr, ARCHITECTURE-SPINE.md, .arch-handoff.

Let me now plan the deliverable set:

1. **Significance assessment** → in the proposal/change or a separate doc. Route: Standard vs Critical. Let me compute: recurring/subscription C2B debits. Triggers:
   - api_contract_change (yes — new endpoints, new consent model)
   - data_contract_change (yes — new entity: consent/subscription; new data: payer's consent, mandate)
   - consistency_model_change (yes — new long-lived state, scheduled debits, mandate lifecycle)
   - significant_nfr (yes — new NFR for recurring charges, revocation latency)
   - financial_impact (yes — money movements)
   - new_component? Maybe a new "subscription/consent" module within the gateway — arguably yes (new component) or extension.
   - security_boundary_change? Storing consents and mandates — touching payer's data, new delegation of authority. Possibly yes (new trust relationship: payer consent stored).
   - new_datastore? Consent store — maybe not new datastore.
   - new_vendor? NSPK requires separate service "подписки СБП" — the operator side. Possibly new external integration (МПС? no).
   - irreversible_migration? No.
   - criticality_or_exception? Payments → yes, financial.

   Actually "criticality_or_exception" is a catch-all for criticality. Hmm. Financial impact + payment domain: Critical route by default since the parent was Critical. Let's be rigorous with the 15 triggers, and honestly: the change is a material extension of a Critical system (payment gateway, КИИ, money). According to significance-routing rule: "Critical (5+ или любой из security_boundary_change / irreversible_migration / criticality_or_exception)". So if I count ≥5 triggers → Critical. Let me count carefully:
   1. api_contract_change — yes (new endpoints in tsp-api).
   2. data_contract_change — yes (new Consent/Subscription entities + persistence).
   3. consistency_model_change — yes (new long-lived state machine for consent/subscription distinct from payment; multi-step, scheduled).
   4. significant_nfr — yes (new measurable NFRs for recurring charge success rate, revocation latency, retry windows).
   5. financial_impact — yes.
   6. security_boundary_change — arguable: storing payer's consent/mandate = new authorization delegation; new data (payer identifier/masked PAN-less) and new revocation surface. I'd mark it yes with justification, since consent is a legal authorization for debits; mishandling = unauthorized debit. That pushes Critical regardless of count.
   7. new_component — subscription/consent service as new component in the gateway contour — yes, but could be "extension". I'll mark as yes (new logical component/service).
   8. cross_domain_integration — ТСП домен + платежи + НСПК subscriptions service — yes.

   So ~7-8 triggers → clearly Critical. Route: Critical → full Solutioning: spine ADD, ADR(s), NFR, A3 human decision, walking skeleton, evidence gates.

   But important nuance: don't over-route. The skill's anti-pattern is "все через комитет". However payments/КИИ → Furious. The parent was Critical 11/15. This change is a material feature on top; I'll score honestly and yield Critical but explain which triggers are "inherited vs new". Also note: not the full initiative re-run — only the delta's own Solutioning. That's the honest answer: route Critical for the delta, but scoped to the delta (delta-spec still used for the non-Critical parts? No — the skill says delta insufficient for Critical). So: full Solutioning for the delta, i.e., new spine block, new ADRs, NFR deltas, contract version, handoff package. Plus OpenSpec change artifacts for the brownfield traceability.

2. **Impact on accepted architecture**: which invariants touched (AD-005 etc.), what changes, what doesn't. Key insight: AD-005 "зачисление только из подтверждённого статуса" applies to payment credit; recurring debits add a new mandatory pre-condition — consent/mandate must be valid+active. New invariant. AD-003 idempotency extends to charge attempts. AD-002 status machine extends with consent/subscription entity. AD-004 notif extends with subscription events. AD-007/008 — does the vendor adapter cover subscriptions? This is a big open question: is the СБП subscriptions service part of the transport adapter contract (vendor) or a new adapter? Likely the NSPK "СБП-подписки" API is a distinct protocol surface from ОПКЦ QR payments. That's a genuine gap/decision: extend AD-008 vendor scope vs new adapter. That's precisely an A3-level human decision. Good, this frames "what remains to human architect".

3. **ADR with alternatives, consequences, reversibility.** ADR-008 (new, next number) — recurring debits architecture: consent-first model, mandate storage, charge scheduling, where the scheduler lives, whether the debit is initiated via НСПК subscriptions API or via recurring QR. Alternatives:
   - (a) true СБП subscriptions (mandate/consent at NSPK, debit initiated by merchant without payer action) — chosen
   - (b) recurring QR / saved-link notification (payer confirms each time) — rejects the business ask
   - (c) bank-internal auto-payment (direct debit from payer account at our bank) — only works if payer's account at our bank; not general
   - (d) card recurring (Visa/MC) — out of СБП scope, regulatory
   Consequences and reversibility (costly/irreversible due to consents stored externally and legal authorizations).

   Maybe two ADRs: ADR-008 (consent model & mandate storage / initiative) and ADR-009 (charging orchestration & retry/limit policy)? Depends. I think one ADR for the core decision (consent-first mandate architecture + where debit originates) and possibly a second for the "execution & retry/dunning semantics" since that's a distinct alternative set (retry policy, partial charge, limit checks). And an ADR for "transport/integration channel for subscriptions: extend vendor adapter (AD-008/ADR-007) vs separate adapter" — that's a genuinely separate decision with A3 implication.

   Let me keep it focused: 
   - ADR-008: Рекуррентные C2B-списания: модель согласия (mandate) и источник инициации списания — Proposed, requires A3.
   - ADR-009: Оркестрация списаний: планировщик, повторные попытки, лимиты, идемпотентность charge — Proposed.
   - Possibly ADR-010: расширение области AD-008/вендорского адаптера на подписки (или отдельный адаптер) — Proposed, requires A3 + vendor RFP amendment.

   That might be too many. But the task says "Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью" — singular "решение". I could produce one primary ADR + explicitly list sub-decisions. Hmm. The repo has ADR-001..007 for the whole initiative. Adding ADR-008 (main) and ADR-009 (transport scope, because it touches the Accepted ADR-007 and AD-008 [ADOPTED]) is defensible and honest — AD-008 in spine is Adopted and must not be silently widened. Actually the vendor-scope question is the one that requires modifying an Accepted decision, so it needs its own ADR. And the charge orchestration semantics is part of the main decision. Let me do:
   - ADR-008 (main): Модель согласия на рекуррентные списания (mandate-first) + инициация списания.
   - ADR-009: Расширение области транспорта: подписки СБП в вендорском адаптере ОПКЦ vs отдельный адаптер (supersedes/extends ADR-007 scope).
   
   Plus maybe ADR-009 covers orchestration... I'll fold orchestration into ADR-008 with a dedicated section, and keep transport scope as ADR-009. Hmm, but orchestration has real alternatives (scheduler in gateway vs external job service; retry/dunning). Let me put it as a section with alternatives in ADR-008 (since it's the same decision contour "как исполнять списание по согласию") — no, cleaner: three ADRs is fine for a Critical delta. Actually, let me reconsider the scale: producing 3 ADRs + spine block + NFR delta + contract v0.2 + openspec change + handoff package is a lot but it is what "Critical route architectural package" means. Let me aim for:

   Files to create:
   - `openspec/changes/add-sbp-recurring-payments/proposal.md`
   - `openspec/changes/add-sbp-recurring-payments/specs/...` delta (capability paths) — need to decide capability naming. Existing openspec/specs is empty (.gitkeep). So no established capability paths. I'll create `specs/sbp-recurring-payments/spec.md` with ADDED/MODIFIED/REMOVED requirements in EARS/OpenSpec format (SHALL).
   - `openspec/changes/.../design.md`
   - `openspec/changes/.../tasks.md`
   - `docs/adr/ADR-008-....md`, `docs/adr/ADR-009-....md`
   - `docs/nfr.md` — modify? The instruction: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." docs/nfr.md is an accepted artifact. Changing it: better to add a delta doc `docs/nfr-recurring.md` or append a section clearly marked as proposed? In OpenSpec convention, deltas live in openspec/changes. But docs/nfr.md is the living truth. Hmm. The repo uses OpenSpec for change management (openspec/changes), and docs/ for the accepted truth. The accepted way: OpenSpec delta in openspec/changes, plus new ADR files in docs/adr (that's how ADRs were added), plus a new contract version.

   For the living truth files (ARCHITECTURE-SPINE.md, docs/nfr.md, openapi/tsp-api.yaml): the "accepted way" to change them... The spine has statuses Proposed/Adopted; blocks in Proposed act after ratification of the ADR. So adding a new AD-00x block with Status: Proposed is exactly the accepted mechanism. Good — I can add AD-009 (next free number) to the spine as Proposed, referencing new ADRs. That is the repo's mechanism.

   For docs/nfr.md: the accepted truth has measurable NFRs. Adding a new proposed section risks conflating accepted with proposed. Safer: put NFR deltas in the change's spec delta (EARS requirements with numbers) and in a dedicated `docs/nfr-recurring.md` marked Proposed/Draft. Hmm, but creating a parallel NFR doc fragments truth. Alternative: OpenSpec delta spec is the right home for proposed requirement deltas; docs/nfr.md is the accepted truth and should be updated only at archive/sync time (the OpenSpec cycle: propose → apply → archive → truth updated). That's clean and defensible: don't touch docs/nfr.md now; the delta carries the new NFRs; sync at archive. I'll do that. But the task explicitly wants "Измеримые NFR для нового функционала" — they live in the delta spec + design doc. Good.

   For openapi/tsp-api.yaml: the task explicitly wants contract changes without breaking consumers. openapi/tsp-api.yaml is the accepted artifact (v0.1.0). "Меняй только тем способом, который принят в этом репозитории" — the contract doc (docs/contracts/tsp-api.md) declares versioning policy: "Добавление опциональных полей — обратно совместимо, не требует новой версии", "ломающие — только в /v2". For the change, the accepted approach: additive, backwards-compatible changes → minor version bump 0.1.0 → 0.2.0 within /v1, plus new optional paths. Since a fully specified proposal, I can edit openapi/tsp-api.yaml additively (version 0.2.0) and document. But is editing an accepted file allowed? The repo has OpenSpec for changes... but the contract file is code-like (openapi/). The task explicitly says "Изменения контрактов (openapi/tsp-api.yaml) без поломки существующих потребителей" → so they want me to actually modify openapi/tsp-api.yaml. And "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — additively, minor version, no breaking. Good. I'll edit it additively: version 0.2.0, add paths /v1/consents etc., add schemas, keep existing intact. Also add CHANGELOG? The contract doc has version policy. Maybe add a note in docs/contracts/tsp-api.md? That's accepted truth; better to describe in the delta spec. Hmm, but the OpenAPI is the binding artifact. I'll edit openapi/tsp-api.yaml (additive) and record the contract delta in the change's spec/design. Also I could add `docs/contracts/tsp-api-recurring.md`? Overkill. Better: edit openapi additively.

   Actually, careful: is `openapi/tsp-api.yaml` "accepted"? It's version 0.1.0, draft status in docs/contracts/tsp-api.md ("Status: Draft (для ревью на гейте A1)"). So it's not even ratified. Editing it additively with version bump is fine and in-scope.

   - `.arch-handoff/` — handoff package for implementers. Task says "затем передать исполнителям". The repo's handoff package is `.arch-handoff/` with TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, MANIFEST.json, RUBRIC.yaml, adr/. Should I modify .arch-handoff? That package is for the current walking skeleton task (already delivered?). The change would need its own handoff package. Better to create a **new** handoff package for the delta, e.g. `.arch-handoff-recurring/` — no, repo convention uses `.arch-handoff/`. Hmm. Creating a new dir like `.arch-handoff/recurring/`? Or a sibling `.arch-handoff/` update is risky (overwrites accepted handoff). The safest: create `openspec/changes/<change>/handoff/` ... but the repo's handoff-packaging skill describes a package format. Let me read handoff-packaging skill to see the exact expected structure.

Let me also read adr-authoring, spine-invariants, nfr-design, spine-contracts-gate, handoff-packaging, readiness-gate, adversarial-review, rubric-judging, fitness-functions (briefly).

Given context budget, read the most decision-critical: adr-authoring (template!), spine-invariants (template), handoff-packaging (structure), nfr-design.

Let me read those.
Let me load the remaining skills that define the artifact shapes I must follow.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.qwen/skills/handoff-packaging/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.qwen/skills/nfr-design/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.qwen/skills/spine-contracts-gate/SKILL.md)`

Now handoff-packaging and nfr-design and spine-contracts-gate.

  `tool_search(query="spine adr_new openapi_lint contract_diff rubric_evaluate", max_results=10)`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && openspec list --json 2>&1 | head -40, description="Inspect OpenSpec root and context")`

Now I have a good picture. Let me decide the deliverable structure. Also let me check if Spine MCP tools are available (adr_new, spine_lint, rubric_evaluate, contract_diff, openapi_lint). The MCP server failed maybe. Let me test whether arch-be shows in the MCP server list. I can try tool_search for "spine".

Let me do tool_search "spine" and "openapi_lint".

Actually the deferred-tools reminder lists only bundled tools (cron_create, etc.). Spine tools would come from MCP server. Since they're not listed, maybe MCP server failed to connect. Let me test by running arch-be mcp serve? No. Let me just try tool_search.

Let me also check openspec status and list.

  `run_shell_command(command="<SPINE_BANK>/target/release/arch-be --help 2>&1 | head -80", description="List arch-be (Spine) CLI commands")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && openspec new change add-sbp-recurrin, description="Scaffold OpenSpec change")`

OpenSpec is set up. Spine MCP tools are NOT available (probably server failed). Let me verify by checking whether arch-be binary runs and whether `arch-be mcp serve` works. Not necessary; I can use CLI directly if needed for linting. Let me check `arch-be` capabilities quickly from the found binary — actually the MCP config expects `arch-be` on PATH; since not found, MCP server likely failed. I could add it to PATH for CLI use: <SPINE_BANK>/target/release/arch-be. Let me check what commands it offers (spine lint, control check, adr registry, handoff).

Let me run `arch-be --help`.

Also, let me decide the OpenSpec change structure. Since openspec is configured with spec-driven schema (default). Let me run `openspec new change` to scaffold, then follow instructions.

Change name: `add-sbp-recurring-payments` (kebab-case).

Let me now run interleaved: arch-be help, and openspec new change.

Actually before creating, I should think about whether to use OpenSpec for this. The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The repo has openspec/ set up with changes/ empty and specs/ empty. The project has skills for openspec propose/apply/archive. So yes — OpenSpec change is the accepted mechanism for changing the decision.

Plan of artifacts:
A. OpenSpec change `add-sbp-recurring-payments`:
   - proposal.md
   - specs/<capability>/spec.md (delta, EARS/SHALL)
   - design.md (architecture: impacted invariants, alternatives summary, contract changes, NFRs, acceptance, rollback)
   - tasks.md
B. Spine: add AD-009 block (Proposed) to ARCHITECTURE-SPINE.md — new invariant(s) for recurring: consent-required-before-debit, mandate lifecycle, idempotent charge, revocation stops future debits. Use minimal set passing the "can two units diverge" test.
C. ADRs: docs/adr/ADR-008-*.md (main), ADR-009-*.md (transport scope vs ADR-007/AD-008 [ADOPTED]), maybe ADR-010 for charge orchestration. Let me decide: 2 ADRs to keep focus:
   - ADR-008: Модель рекуррентных списаний: согласие (mandate) как предусловие, хранение и жизненный цикл — main decision incl. orchestration & idempotency of charge.
   - ADR-009: Транспорт подписок СБП: расширение области вендорского адаптера ОПКЦ vs отдельный адаптер (затрагивает ADR-007 Accepted).
   Hmm, orchestration (scheduler/dunning/limits) is substantial; but I can include as a section in ADR-008's Decision with its own alternatives row. Actually the ADR skill says >1 page → split. Orchestration is a genuinely separate decision (where the scheduler lives, retry policy). I'll make three: ADR-008 (consent model & lifecycle), ADR-009 (charge execution & retry/limits orchestration), ADR-010 (transport scope vs vendor adapter). Hmm, three ADRs + spine + nfr + contract + openspec + handoff. That's a big but appropriate package for Critical.

   Let me reconsider: maybe combine 009 into 008 (both about "how a recurring debit is executed" — consent is the precondition, orchestration is the mechanism). And keep ADR-009 = transport scope (touching Accepted ADR-007). That gives 2 ADRs — cleaner, matches "ADR-эпос" antipattern warning. I'll fold orchestration into ADR-008 as decision points 1-N, each with alternatives in one table.

   Actually the alternatives for consent model and for orchestration differ; but a single table can hold 4-5 rows. OK.

D. NFR delta: put in the OpenSpec delta spec (EARS requirements with numbers) + design.md NFR section. Optionally also a machine-readable file. The repo's accepted NFR doc is docs/nfr.md; per OpenSpec cycle, don't rewrite truth now. But the task wants "Измеримые NFR для нового функционала" as a deliverable. I'll put them in design.md + spec delta, and mention the docs/nfr.md section to be appended at archive/sync (with exact proposed text so human just pastes). Better: include a ready-to-merge block in design.md.

   Hmm, but spine skill: NFR must be verifiable by fitness. I'll add fitness rules to the handoff CONSTRAINTS.

E. Contract: edit openapi/tsp-api.yaml additively → version 0.2.0, add paths for consents/subscriptions + charge history + webhook events, keeping existing. Verify no breaking by diffing with git (git stash not needed — use `git show HEAD:openapi/tsp-api.yaml` to get old and diff conceptually). I can run `git diff` after edit.

F. Handoff package for implementers: The repo convention `.arch-handoff/` is for the current walking-skeleton task and is an accepted artifact set. Task asks "затем передать исполнителям" — so produce a NEW handoff package. I should not overwrite the existing one (that would clobber an accepted handoff). Options: create `.arch-handoff/` variant? The spine/handoff tool `handoff_create` probably writes `.arch-handoff/`. Since I can't rely on the tool, I'll create a new directory for the delta: `.arch-handoff/` is taken; use `.arch-handoff-recurring/`? That breaks convention. Alternatively `openspec/changes/add-sbp-recurring-payments/handoff/` — but handoff-packaging says the package lives in `.arch-handoff/`.

   Decision: create the delta handoff package under `docs/handoff-recurring/`? Hmm.

   Let me reconsider: maybe I should ASK the user? No — better to make a defensible choice and flag it. The cleanest repo-consistent choice: create `.arch-handoff/` sibling that keeps the same internal structure, named per the change: `.arch-handoff/recurring/` is a subdir of the accepted package — mixing. I'll go with a sibling `.arch-handoff-sbp-recurring/` and note it. Actually... Let me think about what "accepted way" means. The existing `.arch-handoff/` is the handoff for the accepted decision (walking skeleton). The new change needs its own handoff for the delta. A sibling directory with identical structure is the least destructive and most explicit. I'll name it `.arch-handoff-recurring/` and document the convention in the design doc + README.

   Hmm, alternatively put it in the OpenSpec change dir: `openspec/changes/add-sbp-recurring-payments/handoff/`. But then it won't be discoverable by `arch-be` tooling that expects `.arch-handoff/`. Sibling is better for tooling.

   Let me check if arch-be handoff CLI supports an output dir. Check `arch-be --help` first.

G. Significance assessment: where? Deliverable #1. Best home: `proposal.md` (impact/route) + a dedicated section. I'll also produce a short `docs/` artifact? The repo has no "significance" doc. The skill says A1 Impact Assessment prepared by agent. I'll put the significance score + route + triggers in proposal.md (with a table), and mirror in design.md. Good — keeps it in the OpenSpec change.

H. "Что остаётся на решение человека-архитектора" — A3 decision package, machine-readable, per significance-routing: {choice, rationale, constraints, rejected options, expiry}. I'll put it in design.md or a separate `A3.md` in the change. I'll create `openspec/changes/add-sbp-recurring-payments/a3-decision.md`? OpenSpec might not know it, but extra files are fine (status is file-existence for known artifacts). Hmm, extra artifacts could confuse `openspec status`. It's fine — status only tracks declared artifacts. But to be safe and clean, I'll include the A3 package inside design.md as a section plus in ADR-008's "A3 Decision" like ADR-007 did. Actually ADR-007 has "## A3 Decision (машинно-читаемый пакет)". I'll mirror that pattern in ADR-008 and ADR-009.

I. Fitness rules for the delta: add to the new handoff CONSTRAINTS.yaml (repo convention: handoff package has CONSTRAINTS.yaml). But careful: modifying .arch-handoff/CONSTRAINTS.yaml would affect the accepted task. New package gets its own.

J. Verification: run openspec validate, check the delta conforms. Also maybe run a contract lint if arch-be available. Let me check arch-be.

Let me run arch-be --help and check for subcommands: adr, spine, control, contract, rubric, handoff, significance.

Let me also run `openspec new change add-sbp-recurring-payments`.

Let me do these.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && openspec status --change add-sbp-rec, description="Show change artifact status")`
  `run_shell_command(command="B=<SPINE_BANK>/target/release/arch-be; echo \"=== gate ===\"; $B gate --help 2>&1 | head -40; echo \"=== handoff ===\"; $B ha, description="Inspect arch-be gate/handoff/rules options")`

Good. Change scaffolded. Let me explore arch-be subcommands helpful: gate, rules, handoff, control, rubric. Let me see `arch-be gate --help`, `arch-be handoff --help`, `arch-be rules --help`, `arch-be mcp list`, and `arch-be control --help`.

Also get openspec status/instructions for the change.

Let me run these in parallel.

  `run_shell_command(command="B=<SPINE_BANK>/target/release/arch-be; echo \"=== handoff full ===\"; $B handoff --help 2>&1; echo; echo \"=== control ===\";, description="Full handoff and control help")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && B=<SPINE_BANK>/target/, description="Run arch-be gate baseline")`

Good. arch-be handoff writes to `.arch-handoff/` presumably. Since we mustn't clobber the existing accepted handoff, and I want the delta package... Let me check if handoff has an output dir option. Let me see full handoff help. Also check `arch-be gate --route critical` would lint the repo — could be useful to verify my artifacts. And `arch-be control check`.

But note: the gate is designed for the repo as a whole with .arch-handoff/CONSTRAINTS.yaml. If I create a new handoff dir, the gate won't see it. Maybe the intended workflow: after the change is approved and applied, the repo's `.arch-handoff/` gets regenerated for the new task. Since our task is "prepare the architectural package so it can be taken to architectural decision and then handed to implementers", the handoff package for the delta is appropriate.

Decision: I'll generate the delta handoff with `arch-be handoff` into the repo but pointing at a different task, which writes `.arch-handoff/`. That would overwrite the accepted package. Risky. Let me check handoff output options (maybe --out or --dir).

Let me view full handoff --help.

Also I realize I should check the `arch-be gate` behavior on the repo now to see the baseline state. And `arch-be control check`. Let me run those to know the starting green/red and what conventions are mechanically enforced (e.g., gate detects direct spine edits → "delta guard"). This is important: "gate ... гейт прямых правок спайна (delta guard)" — meaning direct edits to the spine are gated. That reinforces: spine changes must go through the accepted mechanism (which may be a delta/evidence). Hmm — "гейт прямых правок спайна (delta guard)" suggests the spine should not be directly edited without a delta; maybe there's a mechanism to record spine changes. Let me investigate: `arch-be rules`, and maybe `arch-be control` subcommands. Let's check `arch-be control --help` and look for spine delta guard docs.

Let me run a batch.

  `run_shell_command(command="B=<SPINE_BANK>/target/release/arch-be; $B --help 2>&1 | tail -40", description="Rest of arch-be top-level help")`
  `run_shell_command(command="cd <SPINE_BANK> && grep -rn \"delta_guard\\|delta guard\\|прямых правок спайна\" --include=*.md --include=*.rs . 2>/dev/null , description="Find delta_guard documentation")`

The gate works with route auto → Fast (score 0). Note "delta_guard — изменённых файлов: 2, защищённых среди них: 0". So the gate tracks protected files (spine). If I edit ARCHITECTURE-SPINE.md directly, delta_guard might flag it. This is the "гейт прямых правок спайна". Let me understand what it means exactly: direct edits to spine are gated — meaning they require an explicit delta mechanism? Let me look at arch-be docs. There's a skill `spine-fitness-gate` and check-spine-be-docs. But the key question: what is the ACCEPTED way to change ARCHITECTURE-SPINE.md in this repo?

Possibilities:
1. New AD block with Status: Proposed (like the existing ones — all Proposed except AD-008 [ADOPTED]). The spine itself says "Статусы: блоки в статусе Proposed действуют после ратификации соответствующего ADR." So adding a Proposed block + ADR is the documented mechanism in the file itself. That is "the way accepted in this repo".
2. The gate has a delta guard: maybe there's a file like `.spine-baseline` or the guard checks whether spine edit is accompanied by evidence/delta bundle. Let me check `arch-be control spine --help` and try running `control spine` to lint.

Let me look at what protected files are and whether there's a mechanism to record an authorized spine delta. Let me search arch-be docs? The binary is a repo at <SPINE_BANK>. Let me grep its docs for "delta_guard".

Actually, an important consideration: the gate `delta_guard` said protected among changed: 0 — changed files were .qwen/settings.json and maybe something. Let's test: if I add a Proposed AD block to spine, will the gate fail? Possibly the delta_guard requires a "spine delta" record (evidence bundle) — the mesh "spine-bundle" skill mentions `evidence verify` and findings like `evidence_stub`. Hmm, that's another tool (evidence). Let me check arch-be subcommands more (the --help output was truncated at bootstrap). Let me see the rest.

Let me get the full top-level help and look for `evidence`, `adr`, `spine` etc.

  `run_shell_command(command="cd <SPINE_BANK> && sed -n '1,60p' src/delta.rs; echo \"=== protected paths ===\"; sed -n '235,300p' src/delta.rs", description="Read delta module docs and protected paths")`

There's a `delta` mechanism in arch-be. Let me inspect delta.rs docs and find the delta CLI/MCP commands: `delta_guard`, `delta_propose`, `delta archive`. Let me look at how delta is structured: probably `.arch-delta/` or `openspec/changes`? Let's read src/delta.rs head and default protected paths.

Let me read the relevant parts of delta.rs.

  `run_shell_command(command="cd <SPINE_BANK> && grep -n \"openspec\\|changes\\b\\|DELTA.md\\|archive\" src/delta.rs | head -60", description="Find delta root resolution logic")`
  `run_shell_command(command="B=<SPINE_BANK>/target/release/arch-be; $B --help 2>&1 | grep -n \"delta\\|evidence\\|rubric\\|contract\" ", description="Grep arch-be commands for delta/evidence")`

Critical discovery. The repo's delta mechanism uses `changes/` at repo root (not `openspec/changes/`)? Wait: "Каталог изменений — `changes/` в репозитории: предложенные на верхнем уровне, заархивированные — в `changes/archive/`." So `delta` uses `changes/<name>/DELTA.md`. But the repo has `openspec/changes/`. Hmm. Two possible delta roots. Maybe `changes/` relative to a configured root. And OpenSpec's root is `openspec/`. The delta module may accept a root param. Let me check the `delta` CLI/MCP: is there a `arch-be delta` command? Top-level help didn't show `delta` in the tail... Let me look at full top-level command list. Earlier `--help | head -80` and `tail -40` overlapped; commands listed: tui, init, run, models, prompts, memory, mermaid, archify, rubric, rules, bench, kb, web, mcp, handoff, harness-run, harnesses, control, gate, trust, bootstrap, selftest, redteam, review, contract-diff. Let me see the middle part that was cut. Let me get the full list.

Actually there might be `delta` command. Let me grep the CLI definition. Let me print lines 1-80 of main.rs or the full help. Let me just run `arch-be --help` and grep for delta.

Also check: how does the guard find active deltas — from `changes/` dir (default) or openspec? Let me read more of delta.rs around the mention scanning, and check for a config for paths.

Key question for my task: ARCHITECTURE-SPINE.md is a protected path; editing it requires the change to be mentioned in the active delta. Also `CONSTRAINTS.yaml` protected — but the repo's CONSTRAINTS.yaml is at `.arch-handoff/CONSTRAINTS.yaml`, not root, so not protected by default.

So the accepted mechanism:
1. Create a delta in `changes/<name>/DELTA.md` (via `arch-be delta new` / `delta_propose`) that mentions ARCHITECTURE-SPINE.md → guard passes.
2. Edit the spine (Proposed block).

But the repo also has OpenSpec (`openspec/changes/`). Which is "accepted"? Both exist. Hmm. The `delta` module doc says catalog is `changes/`. But the repo has openspec/ initialized with config and empty changes. Possibly the harness `delta` root is configurable and this repo uses `openspec/`. Let me check delta.rs for how it locates the root — maybe it looks for `openspec/` first.

Let me grep for "openspec" in delta.rs.

  `run_shell_command(command="B=<SPINE_BANK>/target/release/arch-be; $B delta --help 2>&1 | head -40", description="arch-be delta help")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && ls -la; echo \"=== spineignore ===\", description="List repo root and spine config files")`

So `arch-be delta` exists and uses `changes/` at repo root, NOT `openspec/changes/`. But the repo has openspec. Hmm — two parallel systems. Which is the "accepted way in this repository" for changing accepted decision files?

The repo has:
- `openspec/config.yaml` + `openspec/changes/` + `openspec/specs/` (OpenSpec CLI installed, empty).
- `.qwen/skills/openspec-*` skills (OpenSpec workflow).
- `.qwen/commands/opsx-*.md`.
- arch-be `delta` uses `changes/`.

The delta guard requires protected-file edits be mentioned in a DELTA.md under `changes/`. So to modify ARCHITECTURE-SPINE.md (protected), the accepted mechanism is a delta in `changes/<name>/DELTA.md` mentioning it. Since the repo has no `changes/` dir yet, and the guard currently passes (0 protected changed).

Hmm, but wait: is `changes/` maybe configurable to `openspec/changes`? The code uses repo.join("changes") hard-coded. So the harness's guard looks at `changes/`. Unless the repo config sets a different root... let me check for arch-harness.toml or config. There's no arch-harness.toml in the repo listing. Let me check for `.arch-harness` config or `[delta]` config. Let me grep for "DEFAULT_PROTECTED" usage and config keys for protected paths, and whether guard checks openspec.

Actually maybe the repo ALSO expects `changes/` and the OpenSpec dir is a decoy/parallel. The task says "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." There are openspec skills AND spine skills. The presence of openspec/ config with schema spec-driven + the `.qwen/commands/opsx-propose.md` suggests OpenSpec is the intended change vehicle. But the mechanical gate (arch-be) checks `changes/`.

Best approach: satisfy BOTH:
- Create the OpenSpec change (`openspec/changes/add-sbp-recurring-payments/`) — the OpenSpec-native artifacts (proposal, spec delta, design, tasks).
- Also create `changes/add-sbp-recurring-payments/DELTA.md` — the arch-be delta that mentions the protected spine file, satisfying the delta guard.

Hmm, that's duplication. Alternatively, make `changes/` the delta and skip OpenSpec. But OpenSpec change is already scaffolded and openspec CLI validates it. And the task explicitly mentions openspec/ in the repo description? The task says: "`openspec/tsp-api.yaml`" — no, it says openapi. It says "`openspec/`" is in the folder structure. Task mentions: "docs/, openapi/, .arch-handoff/". It says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории."

I think the cleanest: use the arch-be delta as the authoritative change record for spine edits (because the mechanical gate enforces it), and use OpenSpec for the full planning artifacts (since OpenSpec is set up and has its own workflow/skills). But duplicating content in two places is a smell.

Let me check whether the delta guard can be pointed at openspec via config, or whether `delta` accepts `--root`. Let me look at the CLI for delta and its options. Let me also check `arch-be delta --help`.

Also check if there's a `.spineignore`/connect manifest excluding openspec (the gate said "исключено по манифесту connect/.spineignore: 1 файлов"). Let me look for .spineignore.

Let me run: `arch-be delta --help`, list hidden files in repo, and grep config for delta.

  `run_shell_command(command="B=<SPINE_BANK>/target/release/arch-be; echo \"=== score ===\"; $B control score --help 2>&1 | head -50; echo \"=== spine ===\, description="Inspect control score and spine help")`
  `run_shell_command(command="B=<SPINE_BANK>/target/release/arch-be; echo \"=== contract-diff ===\"; $B contract-diff --help 2>&1 | head -40; echo \"=== ad, description="Inspect contract-diff and adr help")`

No .spineignore / arch-harness.toml at repo root. The gate said "исключено по манифесту connect/.spineignore: 1 файлов" — probably a default ignore (maybe .arch-handoff itself).

Now: the delta guard uses `changes/<name>/DELTA.md` and requires protected files to be mentioned. I'll create both the OpenSpec change and an arch-be delta. To avoid duplication, I can make the arch-be `changes/<name>/DELTA.md` the concise spine-delta record (ADDED/MODIFIED/REMOVED + rollback + acceptance) — which is essentially the same as the OpenSpec spec delta but in arch-be's format. And keep OpenSpec for proposal/design/tasks/spec. Duplication of the delta summary is acceptable and arguably required by two installed toolchains; both are "accepted" in this repo.

Hmm, but wait: is it cleaner to put the whole change in `changes/` (arch-be) and drop OpenSpec? The OpenSpec config exists and openspec CLI is installed with generated skills — strong signal that OpenSpec is intended. Also the task description lists `openspec/` in the structure implicitly? It lists: ARCHITECTURE-SPINE.md, README.md, .arch-handoff/, docs/, openapi/, openspec/. Yes it lists openspec/ in the folder structure. So both.

Decision: do both, with clear roles:
- `openspec/changes/add-sbp-recurring-payments/` — full planning artifacts (proposal, specs delta, design, tasks). This is the primary change record.
- `changes/add-sbp-recurring-payments/DELTA.md` — the arch-be delta guard record that mentions `ARCHITECTURE-SPINE.md`, so the spine edit is "covered" mechanically. Keep it a concise delta + reference to the OpenSpec change (avoid divergent truth: state explicitly that the full artifacts live in openspec/changes/...).

That satisfies both toolchains and the mechanical gate. Good.

Now, will the gate run on route Critical and require NFR/evidence? `gate --route auto` computed Fast because score 0 (triggers none — it derives triggers from the diff/model, seemingly needs specific files). To get the honest route, I should compute significance explicitly with `arch-be control score --trigger ...`. Let me check `control score --help` and run it with the triggers I identify. That will produce the machine route. That's deliverable #1.

Let me run `arch-be control score --help`, then run with triggers.

Also `arch-be contract-diff` can verify no breaking changes in openapi/tsp-api.yaml v0.1→v0.2. I'll use it (need old file copy). And `arch-be review` maybe. Let me plan to run:
- control score with triggers → route
- control spine (lint spine after edit)
- gate (after edits)
- contract-diff old vs new openapi
- openspec validate --change

Great. Let me check control score help.

Also I should check `control spine --help` for what it lints (to make sure my AD block format passes).

Let me run these.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && B=<SPINE_BANK>/target/, description="Compute Architecture Significance Score")`

Good. I can use `arch-be control adr --dir docs/adr "<title>"` to create ADR with proper numbering/template. That's the accepted way ("инструмент adr_new"). Let me use it for ADR-008 and ADR-009. It will create files with next numbers. Let me check the existing naming: ADR-001-outbox.md ... ADR-007-proposed-a3.md. The tool probably creates `ADR-008-<slug>.md`. Good.

Let me first run the significance score with triggers.

Triggers (per significance-routing list):
new_component, new_datastore, new_vendor, domain_ownership_change, cross_domain_integration, api_contract_change, data_contract_change, security_boundary_change, trust_zone_change, consistency_model_change, significant_nfr, rto_rpo_targets, irreversible_migration, financial_impact, criticality_or_exception

For recurring СБП subscriptions:
- new_component: true (subscription/consent service as new logical component) — arguably. I'll set true; the model must be honest. Actually, is it a new component or an extension of the gateway? The gateway already exists (planned). Adding a "consent & recurring charge" module inside the gateway contour. If it's a separate deployable — new component. I'll argue yes at container level (new service for mandate lifecycle + scheduler). Hmm, it could be a module. To be honest and not inflate: I'd say new_component = true because a scheduler/mandate service is a new runtime component with its own state; two independent units could diverge. Justify.
- new_datastore: true — consent/mandate store + charge attempt journal (new tables, possibly new schema). Actually "new datastore" is a new storage system. If it's new tables in the existing gateway DB, not a new datastore. I'll set false and justify (extends existing БД шлюза). Honest.
- new_vendor: false — same vendor adapter (if extended). But transport scope is a decision; if separate adapter maybe new vendor. I'll set false, note the open decision.
- domain_ownership_change: false.
- cross_domain_integration: true — ТСП (subscription mgmt), НСПК subscriptions service, АБС (debit), payer.
- api_contract_change: true — new endpoints.
- data_contract_change: true — new event types + consent data + webhook events.
- security_boundary_change: true — payer consent/mandate = new authorization delegation; new PII/permission surface; revocation. This is the heavy one.
- trust_zone_change: false (no new zone; but new external interface to НСПК possibly different service). I'll set false, or true? If subscriptions go through a different НСПК service endpoint, still same trust zone/adapter. false.
- consistency_model_change: true — new long-lived consent state machine + scheduled charging + at-least-once charge semantics.
- significant_nfr: true — new NFR budgets (charge success rate, revocation propagation, retry windows).
- rto_rpo_targets: true — RPO=0 extended to consents/charges (a charge must not be lost/duplicated). I'd say true.
- irreversible_migration: false — no data migration; consents are new. Reversibility: costly but not irreversible (though consent revocation is legally binding; rollback of capability means stopping new consents, existing must be honored/revoked — that's costly).
- financial_impact: true.
- criticality_or_exception: true — payment system, КИИ.

Count true: new_component, cross_domain_integration, api_contract_change, data_contract_change, security_boundary_change, consistency_model_change, significant_nfr, rto_rpo_targets, financial_impact, criticality_or_exception = 10. Definitely Critical (≥5, plus security_boundary_change and criticality).

Let me run the tool to get the official score.

Then run `--from-diff` too? It would add triggers from git diff (e.g., openapi/tsp-api.yaml → api_contract_change). Good for anti-bypass. I'll run with both.

Let me run:
arch-be control score --trigger new_component=true --trigger new_datastore=false ... --trigger criticality_or_exception=true --from-diff

Let me see output format.

Then create ADRs with the adr tool.

Let me run score now.
Now let me compute the significance score mechanically with the harness tool.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && find openspec -type f | sort; echo \, description="Inspect change scaffold")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && openspec instructions proposal --cha, description="OpenSpec proposal instructions")`

Score 10/15 → Critical. Matches the parent initiative's Critical route. Note the parent README said 11/15 for the whole initiative; our delta is 10/15 — consistent, and importantly independent of the parent. So full Solutioning required: spine AD block + ADR + NFR + A3 human decision + walking skeleton + evidence gates. And delta is INSUFFICIENT per the skill.

But we still need the OpenSpec change to carry the delta (brownfield). Since route=Critical, the OpenSpec change is the vehicle but with full Solutioning content (proposal+specs+design+tasks) — good.

Now let me design the actual content. This is the core intellectual work. Let me think carefully about the СБП recurring domain realities.

**Domain: СБП subscriptions / recurring C2B debits (рекуррентные платежи / «СБП-подписки»).**
Business: ТСП (online cinemas, ЖКХ, telecom) want to debit payer's account repeatedly without the payer scanning a QR / confirming each time, based on payer consent.

In real СБП, there is a "СБП-подписка"/платежи по согласию (mandate): сценарий C2B "подписка" — клиент даёт согласие в приложении своего банка (банк плательщика), согласие регистрируется в СБП, ТСП инициирует списания в рамках согласия (лимиты, период, суммы), плательщик может отозвать согласие. Details are in NSPK docs — [ТРЕБУЕТ ПРОВЕРКИ]. I'll design transport-agnostic and mark protocol specifics as external input.

Key architecture concerns:
1. **Consent (mandate) as a first-class entity with its own lifecycle** — независимый от платежа. Lifecycle: DRAFT/CREATED → PENDING_PAYER → ACTIVE → SUSPENDED → REVOKED → EXPIRED. The consent has: payer identifier (phone/token from СБП, no PAN), ТСП, limits (max per charge, max total, max count, period), purpose, schedule, validity.
2. **New invariant: зачисление/списание по согласию возможно только при действующем (ACTIVE) согласии и в пределах его лимитов.** This is the analog of AD-005 ("зачисление только из PAID"). Call it AD-009.
3. **Idempotency of charge attempts**: each charge is a payment with a deterministic idempotency key derived from (consentId, period/attempt) so retries don't double-debit. Extends AD-003.
4. **Revocation must be immediate and must stop future debits** — race: a charge in flight while revocation arrives. Need defined semantics: revocation wins for charges not yet confirmed by NSPK; in-flight charges that NSPK already confirmed must be honored (money moved) → refund path. This is a hard, honest architectural issue → AD block.
5. **Charge scheduling / dunning**: retries on insufficient funds; windows; backoff; max attempts; notifying ТСП. Where the scheduler lives (in the gateway core vs external job scheduler). Choice: in-core scheduler with outbox-driven due charges, idempotent per attempt.
6. **Limits & fairness**: many ТСП charging at period boundaries → burst. Need queue-based load leveling + per-ТСП fairness (rate limiting). NFR: burst handling.
7. **Consent acquisition flow**: payer gives consent in their bank app; СБП returns consent status. Transport: vendor adapter must support the subscription scenario. This touches AD-008/ADR-007 [ADOPTED] scope → separate ADR (A3).
8. **Data**: payer data (phone, masked name) — ПДн, minimize; consent is a legal authorization → immutable audit.
9. **Reconciliation**: consents and charges must reconcile with НСПК (consent registry, charge results).
10. **Webhooks to ТСП**: new events consent.activated, consent.revoked, charge.succeeded/failed, subscription.*.
11. **Refunds** on subscription charges — reuse existing refund saga.
12. **Non-goals**: C2C, B2B, карты, dunning legal/collection, disputes.

**Impact on existing invariants:**
- AD-001 (isolation): unchanged; new component stays inside payment contour; all external calls via adapters. Applies.
- AD-002 (single source of truth status machine): extended — a second state machine (consent/subscription) added; must obey same atomic transition + outbox rule. Modified/extended (new entity), not broken.
- AD-003 (idempotency): extended to charge attempts (new idempotency key shape). Applies and requires new rule.
- AD-004 (single OPKC adapter): applies; but scope question — does subscription protocol live in the same adapter? → ADR-009/A3.
- AD-005 (credit only from PAID): unchanged for credit; new precondition added before initiating debit/credit.
- AD-006 (trust zones): unchanged; consent processing stays in payment contour; no new zone. But new endpoint for payer consent status might need ТСП-facing vs payer-facing clarity — payer interacts only via their bank's app, not our API. So no new public surface. Good.
- AD-007 (compliance): extended — consent storage is a legal authorization → audit; ПДн of payer, 152-ФЗ; mandate revocation must be honored (regulatory). Applies.
- AD-008 (strategy hybrid, ADOPTED): potentially widened if the vendor adapter must cover subscriptions. Must NOT be silently widened → ADR-009 explicit, requires A3.

**New invariants (spine block AD-009):** Let me draft 3 sub-invariants in one block or 3 blocks AD-009..AD-011? The spine norm is 5-15 blocks; currently 8. Adding 2-3 is fine. The skill says each block = one divergence risk. Let me define:
- AD-009 «Списание по согласию — только при действующем согласии в пределах лимитов» (Binds: consent service, charge orchestrator, OPKC adapter, ABS). Prevents: несанкционированные списания, списания сверх лимита, списания после отзыва.
- AD-010 «Жизненный цикл согласия: единственный источник истины и приоритет отзыва» (Binds: consent store, charge orchestrator, adapter, ТСП-notifier). Prevents: расхождение «клиент отозвал — шлюз продолжает списывать»; неотражённый отзыв. Rule: revocation recorded atomically; any debit not yet confirmed by OPKC must be blocked; confirmed debits → refund path; event outbox.
- AD-011 «Идемпотентность попытки списания по согласию» (Binds: charge orchestrator, ABS adapter, OPKC adapter). Rule: attempt key = deterministic (consentId + billing period + attempt seq); repeats don't create second debit.
Hmm, AD-011 partly duplicates AD-003. Better: extend AD-003's Binds and add a charge-attempt rule line inside AD-009/010 rather than a new block. But AD-003 is a Proposed block; modifying it = MODIFIED (delta must mention spine file, fine). The spine's own convention allows modifying blocks via ADR ratification. But careful: AD-003 is Proposed (not yet ratified?). Statuses: "блоки в статусе Proposed действуют после ратификации соответствующего ADR". AD-003 references ADR-002,004,005 (all Proposed). So the whole spine is Proposed except AD-008 [ADOPTED]. So modifying AD-003 by extending Binds is acceptable within a delta, but cleaner to keep existing blocks untouched (they're the accepted-ish baseline) and add new blocks. However the "single source of truth" and idempotency rules genuinely need to cover new entities; a new block that says "AD-003 extends to charge attempts" is fine.

I'll add two blocks: AD-009 and AD-010, and mention explicitly that AD-003/AD-005 extend to the new ops (a "MODIFIED" note in the delta without editing the original blocks — i.e., the new blocks bind the new components to the existing rules). Actually, to be precise and avoid ambiguity for implementers, I'll:
- Add AD-009 (consent precondition + limits)
- Add AD-010 (revocation priority / lifecycle single source of truth)
- Add AD-011 (charge idempotency & no double debit) — since two independent units (scheduler and retry worker) could genuinely diverge here, it passes the test. It's the highest-risk financial invariant of this change.

Three new blocks → spine goes to 11. Acceptable (norm 5-15). Good, and it's honest: these are the three places independent implementers would diverge.

Wait — also need: burst of period-boundary charges → fairness/backpressure is a mechanism, not an invariant (implementers can choose). Skip spine. And consent data minimization → covered by AD-007 compliance (extend applicability, no new block). Fine.

**ADR structure.** Let me do:
- ADR-008 «Рекуррентные C2B-списания: согласие (mandate) как предусловие и модель исполнения списаний» — main. Alternatives for the consent/source-of-charge model, includes orchestration/dunning/revocation semantics.
- ADR-009 «Транспорт подписок СБП: расширение области вендорского адаптера ОПКЦ» — touches ADR-007 Accepted + AD-008 [ADOPTED]; requires explicit A3 (because AD-008 rule says transport scope fixed and implementation starts only after vendor contract & NSPK docs; extending scope needs a decision).

Hmm, maybe also ADR for consent data model/PII? Fold into ADR-008.

Actually, is orchestration (scheduler/dunning) distinct enough to warrant its own ADR? Alternatives: (a) in-core due-charge scheduler driven by outbox; (b) external job scheduler (e.g., cron service) calling the API; (c) event-driven with delayed messages in the queue. This is a real choice with consequences. But it's closely tied to "how a debit is executed". I'll keep it inside ADR-008 as decision item with alternatives row — to avoid an ADR-epic. Hmm, ADR-008 would then cover: consent model, execution/orchestration, revocation semantics, limits. That's >1 page. The skill says >1 page → split. Let me split into:
- ADR-008: Модель согласия и источник инициации списания (mandate-first). Alternatives: mandate at NSPK, recurring QR with per-payment confirmation, bank-internal autopay, card recurring. Decision: mandate-first via СБП; consent stored locally as mirror + NSPK as authority.
- ADR-009: Исполнение списаний по согласию: планировщик, повторные попытки, лимиты, идемпотентность. Alternatives: in-core scheduler/outbox, external scheduler, delayed-queue events; retry policy.
- ADR-010: Область вендорского адаптера: подписки в том же адаптере vs отдельный. Alternatives: extend ADR-007 module; new separate adapter/vendor; full-vendor subscriptions.
Three ADRs for a Critical delta of this size — defensible. But is that over-engineering? Hmm. The task says "Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью" (singular). I think 2 is a good balance: ADR-008 (consent model + execution/orchestration as one decision contour "как исполняется рекуррентное списание") and ADR-009 (transport scope, because it modifies an Accepted decision and is A3-critical). 

Hmm, but ADR-008 combining consent model and scheduler... They are separable but I can present the decision with numbered items 1..6 and one alternatives table with 5-6 rows. Risk: "ADR-эпос". I'll mitigate by making ADR-008 focused: "Модель согласия и инициация списания" and put scheduler/dunning choices in the OpenSpec `design.md` (design decisions), not as ADR. That's cleaner: ADR = the irreversible-ish policy decisions; design.md = mechanism. But dunning/retry policy has a genuine architectural fork (in-core vs external scheduler) that affects multiple teams → arguably ADR. Hmm.

Decision: 3 ADRs, each tightly scoped, is the honest read of "Critical + multiple teams can diverge". But the repo already has 7 ADRs for the initiative; adding 3 for a feature is proportionate for a Critical payment change. Actually let me reduce to 2 ADRs and put the scheduler mechanism in design.md, BUT include the "where does the scheduler live" as an explicit open A2/A3 item? No — it needs a decision before implementation.

Let me settle: **2 ADRs**:
- ADR-008 «Модель согласия на рекуррентные C2B-списания и исполнение списаний» (consent authority + lifecycle + revocation semantics + charge execution/dunning + idempotency + limits). One coherent decision: "рекуррентное списание исполняется только по действующему согласию, зарегистрированному в СБП; ядро хранит зеркало согласия и планирует попытки идемпотентно". Includes alternatives for consent model and for execution.
- ADR-009 «Транспорт подписок СБП: расширение области вендорского адаптера ОПКЦ» (A3 decision; touches ADR-007/AD-008 [ADOPTED]).

I'll keep ADR-008 to ~1 page by tight writing, with a 5-row alternatives table and the execution model as a compact numbered list. If it grows, so be it; the content matters more.

Hmm, actually I realize the scheduler decision could confuse. Let me include it as a clearly separated subsection "Модель исполнения" with its own mini-alternatives. That's acceptable.

**NFR (measurable, verifiable, new):**
- Consent registration latency: p95 < 3 s (включая round-trip к НСПК?) — НСПК-dependent, mark [ТРЕБУЕТ ПРОВЕРКИ]. Our part: p95 < 500 ms до отправки.
- Charge initiation: scheduled charge starts within ±X min of due time (живучесть планировщика): например, старт попытки в пределах 5 мин от наступления срока при нормальной работе.
- Charge success rate (с учётом ретраев) ≥ 97% на действующих согласиях с достаточным балансом — hmm needs a defined denominator. Better: "доля списаний, доведённых до COMPLETED за ≤ 3 попытки в течение 72 ч, ≥ 95%".
- Duplicate debits = 0 (idempotency) — verifiable test.
- Unauthorized debit (без действующего согласия или сверх лимита) = 0 — fitness/test.
- Revocation propagation: от момента отзыва в СБП до блокировки новых попыток в шлюзе ≤ 60 s p95; 100% попыток, не подтверждённых ОПКЦ, блокируются.
- Burst: 10× к среднему в момент границ периода (например, 2000 TPS burst на 1 мин?) — Set: sustained 500 TPS for charge processing, burst 1500 TPS 1 min, by reusing queue load leveling. Hmm numbers should be justified. Existing gateway NFR: 200 TPS sustained / 500 burst. Subscription charges add a period-boundary spike. I'd set: charge scheduling sustained 500 TPS with burst 2000 TPS for 5 min (payday/first-of-month), start-lag p95 ≤ 5 min.
- Availability of charge execution ≥ 99,95% (same), RPO=0 for consent/charge state.
- Audit: 100% consent lifecycle + charge transitions in immutable log, 4-eyes for manual consent ops.
- Reconciliation: consents daily + charges daily with НСПК, 0 discrepancies.
- Retention/legal: consent records retained per regulation (min 5 years?) — [ТРЕБУЕТ ПРОВЕРКИ].

**Contract changes (openapi/tsp-api.yaml), backward compatible:**
Add:
- POST /v1/consents (create consent request; ТСП initiates consent; payer confirms in bank app) → returns consentId, status PENDING_PAYER, consentUrl/deeplink (for handing to payer) — optional field.
- GET /v1/consents/{consentId} → status, limits, payer ref (masked), validUntil.
- POST /v1/consents/{consentId}/revoke (ТСП-initiated revoke? Typically payer revokes; ТСП may cancel own subscription) → status REVOKED. Hmm. Payer revokes in их bank app; ТСП may also cancel. I'll include ТСП-side cancel.
- GET /v1/consents?tspId=&status= (list) — optional.
- POST /v1/consents/{consentId}/charges — manual/off-cycle charge attempt within limits (optional; also used to retry).
- GET /v1/consents/{consentId}/charges → history of charges.
- Payment object: add optional field `consentId` (for charges created under a consent) — backward compatible (optional).
- New webhook events: consent.activated, consent.revoked, consent.expired; charge.completed, charge.failed. Existing events unchanged.
- New error codes: CONSENT_NOT_FOUND, CONSENT_NOT_ACTIVE, CONSENT_LIMIT_EXCEEDED, CONSENT_REVOKED, CHARGE_ALREADY_EXISTS (idempotency), CONSENT_EXPIRED.
- New schema: Consent, ConsentLimits, ChargeAttempt.
- Bump version 0.1.0 → 0.2.0 (minor; additive). Keep /v1.
- Idempotency: Idempotency-Key required for new POSTs (consistent with existing).
- Also add `Idempotency-Key` required for POST /v1/consents... consistent.

Careful: Do NOT add required fields to existing Payment/PaymentRequest. Adding `consentId` as optional is fine. Adding new enum values to `status`? The existing Payment.status enum is [CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED]. Charges under consent use the same payment lifecycle → no new values needed. Good — avoids a breaking-ish enum change (adding enum values is technically breaking for strict consumers; avoid).

Wait, should a recurring charge be a "payment" (reuse lifecycle) or a separate "charge" entity? Reuse: a charge = a payment with consentId, lifecycle CREATED→...→COMPLETED. That's elegant and reuses AD-002/AD-005. The status machine for charge skips QR_ISSUED (no QR) — introduce a technical state? The public enum could stay, with charge payments going CREATED → PAID → CREDITED → COMPLETED (QR_ISSUED not used). But status-machine invariants mention QR_ISSUED. I'll define in design: charge uses the same payment machine; `QR_ISSUED` is replaced by an internal `SUBMITTED` sub-state not exposed; the debit is authorized by consent. Hmm — this is a real design detail. Simpler and cleaner: reimbursement via same machine, with T4 trigger being "charge accepted by ОПКЦ" instead of "QR issued". I'll document that the consent substitutes for the QR step and add state machine delta (MODIFIED: add transitions for consent-based charges). Put it in the spec delta (MODIFIED requirements for state machine).

Actually, careful about scope creep. Let me keep contract changes minimal and coherent:
- New endpoints for consents (create/get/list/revoke).
- New endpoints for charges (list; and `POST .../charges` for on-demand/retry) — optional.
- Payment gains optional `consentId`.
- New events + error codes.
- Version minor bump.

**Acceptance criteria (A4):** testable, incl. negative:
1. Charge without ACTIVE consent → rejected, no debit (test).
2. Charge above limit → rejected, no debit (test).
3. Revocation during in-flight charge → no new debit; confirmed charge → refund path (test with mock adapter race).
4. Duplicate charge attempt with same idempotency key → single debit (test).
5. Repeated НСПК notification → no double credit (existing invariant test extended).
6. Period-boundary burst 2000 TPS → start lag ≤ 5 min, no lost charges (load test).
7. Contract: existing consumers' requests/responses unchanged (contract-diff no breaking) — gate.
8. Consent lifecycle audit complete (check).
9. Reconciliation daily: 0 discrepancy on consents/charges (test harness).
Rollback criteria: feature flag off → new consents not created; existing active consents → must be revoked/handed over (irreversibility nuance!).

**Rollback plan:** 
- Before production: don't enable flag; all work reversible.
- After enable: stop-new (no new consents), honors existing consents until revoked or migrated; if disabling charge execution → must not leave consent without service (regulatory: consent is a payer authorization; silently stopping charges is acceptable/needed) → but money obligations to ТСП? The rollback must define: (a) freeze new consents, (b) continue honoring existing ACTIVE consents OR coordinate revocation with НСПК/ТСП, (c) never lose recorded consents (RPO=0), (d) signal-триггеры: unauthorized debit, duplicate debit, revocation not honored, NSPK protocol nonconformance. Decision owner: архитектор + владелец продукта + ИБ (4-eyes). 
- Key honest point: rollback of mandate capability is **costly/irreversible-ish** because payer consents exist in an external registry (НСПК) and carry legal weight; you can't just delete them. ADR-008 reversibility: costly; ADR-009: reversible (adapter swap).

**What remains for human architect (A3):**
1. Transport scope decision (ADR-009): extend Accepted ADR-007 vendor module vs new adapter/vendor — affects RFP, cost, timeline; touches ratify [ADOPTED] AD-008.
2. Whether consent authority = НСПК registry vs bank-local with НСПК notification — depends on NSPK protocol (external input [ТРЕБУЕТ ПРОВЕРКИ]).
3. Dunning policy limits (max attempts, windows, retry on insufficient funds) — legal/business/CX.
4. Revocation semantics for in-flight/confirmed charges — regulatory interpretation (must confirm with ИБ/юр).
5. Limits model (per-charge/per-period/total, currency, TTL) — business + NSPK.
6. Whether to expose `POST /charges` (on-demand/off-cycle) to ТСП — business.
7. Scope: which ТСП segments first (cinema/ЖКХ/telecom differ in period/limits) — business.
8. Retention period for consents/charges.
9. Whether subscriptions become a separate initiative/spine (parent spine change) or feature-level delta.
10. Ratification of new spine blocks AD-009..AD-011.

**Open questions / gaps:** NSPK subscription protocol docs, НСПК consent registry rules, revocation SLA, limits, ТСП contract amendments, ИБ review.

**Оценка значимости** output = score 10/15 Critical + explanation of triggers + why (new money-movement precondition, security boundary, consistency).

Now, where to put each deliverable:
1. Оценка значимости → proposal.md (section "Значимость и маршрут") + design.md.
2. Влияние на принятую архитектуру → design.md (section) + DELTA.md MODIFIED.
3. ADR → docs/adr/ADR-008, ADR-009.
4. Контракт → openapi/tsp-api.yaml (additive, version 0.2.0) + spec delta requirements + design.md.
5. NFR → design.md + spec delta + handoff.
6. Критерии приёмки и план отката → spec delta? OpenSpec spec.md is requirements only (SHALL). Acceptance criteria → design.md/tasks.md + DELTA.md "Критерии приёмки"+"План отката".
7. Что остаётся человеку → design.md section + ADR A3 packages.
Handoff package → `.arch-handoff-recurring/` (or generate with arch-be handoff). 

Hmm, let me reconsider handoff output dir. `arch-be handoff --repo <path>` writes `.arch-handoff/` — overwriting the accepted package's TASK/ARCHITECTURE/MANIFEST but preserving CONSTRAINTS.yaml unless --refresh-constraints. That's destructive to the accepted handoff. I will NOT run it against the repo root. Instead I'll create the delta handoff manually at `.arch-handoff-recurring/` following the skill's composition (TASK.md, ARCHITECTURE.md epic-context 800–1500 tokens, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, adr/ copies). That's the skill's structure; the directory name is the only deviation, justified by not clobbering the accepted package. I'll document it.

Alternatively: could I run `arch-be handoff` with `--repo` pointing to a copy? No. Manual creation is fine and matches the skill's spec.

Wait — maybe better idea: the accepted `.arch-handoff/` is for the walking-skeleton (already handed off; task is done or in progress). The new change's handoff naturally supersedes it *later*, at apply time. Since our task ends at "готов к вынесению на архитектурное решение и передаче исполнителям", providing the handoff for the delta as a separate dir is right. But the human might expect `.arch-handoff/` regenerated. I'll ask? No, I'll make the choice, flag it clearly, and note that at apply/archive time the human regenerates `.arch-handoff/` (or merges) — the delta package lists exactly what to merge. That's a good, explicit handoff note.

Hmm, but creating a whole second handoff dir with duplicated ADRs may be heavy. The skill says adr/ — copies of touched ADRs. I'll copy ADR-008, ADR-009 and reference the existing ADR-001..007 rather than copying all. Actually "копии затронутых ADR" → ADR-008, ADR-009, plus ADR-007 (Accepted, affected), ADR-005 (credit/refund), ADR-002 (state machine), ADR-003/004 (transport/notifications). To keep it useful, copy ADR-002, ADR-005, ADR-007, ADR-008, ADR-009? That's a lot of duplication. I'll copy the new ADRs and list the affected existing ones by path (they're in the repo the implementer has). The skill's intent is the package is self-sufficient without sources; but the implementer works in this repo. I'll include the new ADRs and the spine (as ARCHITECTURE.md includes invariants verbatim). Reasonable.

OK. Also should I add a "README" for the change dir? The OpenSpec change dir is standard; no.

Also: the task says "принятые файлы решения меняй только тем способом, который принят в этом репозитории" → I will NOT edit docs/solutioning.md, docs/nfr.md, docs/contracts/tsp-api.md, README.md. I WILL edit ARCHITECTURE-SPINE.md (adding Proposed blocks — the documented mechanism) covered by a delta. And I WILL edit openapi/tsp-api.yaml (additively, per its versioning policy). That's the correct reading. Should I also update docs/spec/state-machine.md (add consent-charge transitions)? It's an accepted draft truth file. Modifying would be another protected path? Protected = model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. state-machine.md not protected. But per the OpenSpec cycle, truth updates happen at archive. However, the task deliverable #3/#4 may need the state machine delta — I'll express it as MODIFIED requirements in the spec delta, not by editing the truth file. Cleaner. Actually the charge lifecycle is significant; expressing in delta is correct.

Hmm, but the openapi edit is also a "truth" edit. The task explicitly demands it, and it's additive per the contract's own policy. Fine.

Wait, is there a risk that editing openapi/tsp-api.yaml without an OpenSpec "apply" violates the planning boundary of openspec-propose skill? The skill's planning boundary says don't edit project code. openapi/tsp-api.yaml is a contract artifact, arguably planning artifact, not code. And the user explicitly asked for the contract change. I'll do it. But to be safe re: "planning boundary", I should treat the OpenSpec change as the record and the openapi edit as part of the architecture package deliverable (the user asked). I'm not writing implementation code. Fine.

Also I should add delta spec requirements referencing the contract.

Now OpenSpec artifacts: I need to follow the instructions from `openspec instructions <artifact>`. Let me fetch instructions for proposal, specs, design, tasks and read templates. Let me do that.

Also note the openspec config context: "Language: ru; All artifacts must be written in ru. Keep OpenSpec structural headings and SHALL/MUST keywords in English."

Let me fetch instructions for all four artifacts.

Then write files.

Let me also check `openspec/changes/add-sbp-recurring-payments/` scaffold contents (.openspec.yaml).

Let me run instructions.
OpenSpec is set up and arch-be tooling is available. Let me read the change scaffold and the OpenSpec artifact templates.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && openspec instructions specs --change, description="OpenSpec specs instructions")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && openspec instructions design --chang, description="OpenSpec design instructions")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && openspec instructions tasks --change, description="OpenSpec tasks instructions")`

Good. Now let me get instructions for specs, design, tasks. Let me batch.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && for a in specs design tasks; do echo, description="OpenSpec specs/design/tasks instructions")`

The JSON parse failed probably because the UNDICI warning lines precede the JSON. The proposal one worked with `tail -80` because warning went to stderr? Actually `2>&1 | tail` mixed. Here I piped json.load on combined stream including the warning line. Let me redirect stderr to /dev/null.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && B=<SPINE_BANK>/target/, description="Scaffold ADR-008, ADR-009 and arch-be delta")`

I have everything I need. Now let me write the artifacts. This is a large amount of writing. Let me plan the file list:

1. `openspec/changes/add-sbp-recurring-payments/proposal.md`
2. `openspec/changes/add-sbp-recurring-payments/specs/sbp-recurring-payments/spec.md` (new capability)
3. `openspec/changes/add-sbp-recurring-payments/specs/sbp-tsp-api/spec.md`? Hmm. The contract change is to the ТСП API capability. Since there are no existing specs (openspec/specs empty), all capabilities are new in OpenSpec terms. The proposal should list New Capabilities. But the accepted decision has capabilities implicitly (payments, refunds, tsp-onboarding). OpenSpec has no specs for them (empty). So per OpenSpec, everything is "new". But separating "sbp-recurring-payments" (consent/subscription behavior) from "sbp-tsp-api" (contract surface) is reasonable. However the instructions say "Do not invent a requirement just to satisfy validation" and to avoid near-duplicates. 

I'll declare two new capabilities:
- `sbp-recurring-payments` — consent/mandate lifecycle + charge execution behavior.
- `sbp-tsp-api` — the ТСП-facing API contract surface (consent & charge endpoints, webhooks, errors). Hmm, but the API surface is arguably part of the same capability. Splitting gives cleaner mapping to contract changes. But the ТСП API already exists conceptually (payments). Since openspec/specs is empty, I'd have to also spec the existing API — that's scope creep.

Better: ONE capability `sbp-recurring-payments`, containing requirements for consent lifecycle, charge execution, contract surface (new endpoints/events/errors for recurring), NFRs, and MODIFIED requirements for existing payment behavior (e.g., Payment gains consentId; state machine extension). Since it's a "new capability" delta, I can use ADDED requirements, and for changes to existing behavior use MODIFIED — but there's no existing spec file to copy from. The instructions say MODIFIED requires an existing requirement in the main spec, else archive loses detail. Since openspec/specs is empty, there's nothing to modify; so the delta should be ADDED-only, describing the full behavior including how it extends the existing payment machine.

Hmm, but the OpenSpec spec deltas are proposed requirements; the "modification" of the accepted decision (spine/ADR/contract) is expressed in the arch-be DELTA.md (MODIFIED section) and in design.md, not in the OpenSpec spec delta. Good separation: arch-be DELTA.md = what changes in the accepted architecture (spine + contract); OpenSpec spec delta = new external behavior.

Wait, but I should also reflect "without breaking existing consumers" — that's ADR/contract-delta concern (arch-be DELTA.md MODIFIED + contract-diff gate).

So: OpenSpec change → 1 new capability `sbp-recurring-payments` with ADDED requirements. Maybe better naming to reflect both: `sbp-recurring-payments`. Good.

Actually, hold on: do I want the "new capability" to include NFR requirements? OpenSpec specs are behavior contracts; NFRs (reliability/security) are explicitly listed as allowed ("External constraints (security, privacy, reliability, compatibility)"). I'll include measurable NFR requirements with scenarios (e.g., burst, revocation latency, idempotency).

4. `openspec/changes/add-sbp-recurring-payments/design.md`
5. `openspec/changes/add-sbp-recurring-payments/tasks.md`
6. `changes/add-sbp-recurring-payments/DELTA.md` (arch-be delta for spine coverage)
7. `docs/adr/ADR-008-*.md` (via arch-be control adr)
8. `docs/adr/ADR-009-*.md`
9. `ARCHITECTURE-SPINE.md` (+AD-009..AD-011, Proposed) — edit
10. `openapi/tsp-api.yaml` — edit additively, version 0.2.0
11. `.arch-handoff-recurring/` handoff package: TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, adr/ (copies of ADR-008/009), maybe README.
12. Maybe `docs/adr/ADR-007` — no edit (Accepted; don't modify; ADR-009 establishes superseding/extending scope? The rule: "отмена — через статус Superseded by ADR-NNN, не удаление". ADR-009 *extends* (not supersedes) ADR-007's scope. Should I edit ADR-007's status? No — don't edit accepted ADR. ADR-009 will say "Extends ADR-007" and note that AD-008 spine rule's transport scope is widened upon A3. But AD-008 spine block status is [ADOPTED]; widening it requires a spine delta (MODIFIED AD-008 or new block). Hmm — this is the crux. AD-008 says: "Ядро шлюза проектируется контрактно-независимым от транспорта... Реализация транспортного слоя начинается только после подписания контракта с вендором и получения документации НСПК." Extending the vendor module to subscriptions doesn't contradict it. Actually ADR-009 problem is more: "is the subscriptions transport part of the existing vendor module or a separate adapter/vendor?" That doesn't violate AD-008 (core stays contract-independent either way); it's about the RFP/vendor scope and possibly a new vendor → new_vendor trigger. So AD-008 isn't broken. Good — I don't need to modify AD-008. ADR-009 is a new decision that must respect AD-008's constraint (contract-first, cert requirements). It affects ADR-007's RFP scope (must be amended) — I'll state in ADR-009 that it amends the RFP scope, and that ADR-007 itself remains Accepted (its constraints unchanged). Clean.

Hmm, but I set new_vendor=false earlier, assuming same vendor. Let me handle: if ADR-009 chooses to extend the existing module → same vendor (new_vendor=false). But the decision is open (A3). For the score, declaring new_vendor=false is a claim. Honest approach: the decision includes a possible new vendor; but the *change* doesn't inherently require a new vendor. I'll keep false and note it. Or set true? The significance-routing anti-bypass uses --from-diff which can't detect. I think it's fine to say: no new vendor is introduced by this change; the vendor question is a sub-decision that may widen an existing vendor's scope. I'll keep false, and be explicit about the assumption in the significance section. Good, and honest.

13. `.arch-handoff-recurring/` — decide final name. Let me use `.arch-handoff-recurring/`. Hmm, or match change name: `.arch-handoff-sbp-recurring/`? Simpler: `.arch-handoff-recurring/`. I'll document.

Also should I update README.md structure? README is accepted; editing would be modifying accepted doc. But README describes structure; adding openspec mention... Not required. Skip (avoid unnecessary truth edits). Actually README currently doesn't mention openspec/. I'll leave it. Hmm — but a human reviewing the repo would benefit. The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." README isn't part of the decision per se. I'll avoid editing to minimize footprint. I'll list the new files in my final summary.

Also: the proposal should include the significance assessment. The template has Why/What Changes/Capabilities/Impact. I'll add a "## Значимость и маршрут" section? The template says follow it; extra sections are allowed (it says "Sections:" listing required ones). I'll include an extra section "## Значимость и маршрут (A1)" after Why — that's valuable and requested by the user. Keep structural headings in English? Config says "Keep OpenSpec structural headings and SHALL/MUST keywords in English." Hmm — structural headings in English. So `## Why`, `## What Changes`, `## Capabilities`, `## Impact` must stay English. Extra headings — I'll keep them English too to be safe: `## Significance and Route (A1)`. Content in Russian. Good.

Similarly spec delta: `## Purpose`, `## ADDED Requirements`, `### Requirement:`, `#### Scenario:`, WHEN/THEN in English (keywords). Requirement text in Russian with SHALL (English keyword). Config says keep SHALL/MUST in English. Good.

Now, let me write the content. I'll be thorough but tight.

Let me draft the key architecture content.

---

### Significance (proposal)
Score 10/15 (mechanically: `arch-be control score --trigger ... --from-diff`). Route: **Critical**.
Triggers (true): new_component, cross_domain_integration, api_contract_change, data_contract_change, security_boundary_change, consistency_model_change, significant_nfr, rto_rpo_targets, financial_impact, criticality_or_exception.
Not triggered: new_datastore (расширение существующей БД шлюза), new_vendor (вендор тот же / вопрос области — под-решение ADR-009), domain_ownership_change, trust_zone_change, irreversible_migration.
Why Critical: ≥5 triggers, and explicitly security_boundary_change + criticality_or_exception (payments/КИИ). Per significance-routing, Critical = полный Solutioning (spine + ADR + NFR), обязательная человеческая точка A3, walking skeleton, evidence gates. Delta-spec alone insufficient. Note: the delta is significant enough to require its own A3, but not a new initiative — parent spine read-only, feature-level extension.

Note the honest bit: the mechanical gate auto-computed Fast (score 0) because there is no diff yet; the declared+diff score is Critical. That's a nice detail: the declared route is Critical; the auto-floor must be fed after the artifacts exist. Actually I shouldn't overexplain the tooling. But mentioning "auto derived Fast from empty diff → declared 10/15 Critical" is honest and useful for the architect. I'll include a brief note.

### Impact on accepted architecture (design.md)
Table: invariant → impact → what changes/what doesn't.
- AD-001 unchanged (new component inside payment contour, adapters only).
- AD-002 extended: second state machine (consent) obeys the same atomic "status+outbox+audit" rule; payment machine gains a consent-authorized path (no QR). No contradiction.
- AD-003 extended: idempotency key generalized to charge attempts; НСПК notification dedup unchanged.
- AD-004 unchanged in force; scope of the single adapter is the subject of ADR-009 (transport for subscriptions must also live in exactly one adapter; whether same or new adapter is decided there).
- AD-005 unchanged and reinforced: credit still only from PAID; before initiating a debit, a new precondition (active consent + limits) applies.
- AD-006 unchanged: no new trust zone; consent processing in payment contour; no new public entry (payer acts in own bank).
- AD-007 extended: consent is a legal authorization → immutable audit, ПДн minimization, revocation must be honored.
- AD-008 [ADOPTED] unchanged in constraint: core stays transport-independent; vendor cert/contract-first constraints apply to subscription transport too. RFP scope amended (ADR-009).
Then "what changes / what doesn't" summary.

### ADRs
ADR-008 Context: ТСП need recurring debits; СБП supports payments by payer consent (mandate) [ТРЕБУЕТ ПРОВЕРКИ точный протокол]; current gateway is payment-per-QR. Forces: payer must not confirm each debit; consent is a legal authorization; revocation must be honored; limits; end-of-period bursts; money movement; audit; ПДн.
Decision (numbered):
1. Согласие (mandate) — first-class entity, authority = реестр СБП (НСПК); локальное зеркало в шлюзе с жизненным циклом PENDING_PAYER→ACTIVE→SUSPENDED/REVOKED/EXPIRED, single source of truth для решения о списании — локальное зеркало, синхронизируемое с НСПК (сверка).
2. Списание инициирует шлюз (планировщик) в рамках окна согласия; каждое списание — платёж существующей статусной машины с `consentId`; предусловие — ACTIVE + лимиты (AD-009).
3. Идемпотентность: attempt key = (consentId, billingPeriod, attemptSeq) → reference для адаптера/АБС; повтор не создаёт второе списание (AD-011).
4. Отзыв согласия: приоритетен. Записывается атомарно; любое списание, не подтверждённое ОПКЦ, блокируется; подтверждённое — исполняется и при необходимости возвращается (сага возврата). (AD-010)
5. Исполнение: планировщик в ядре по outbox (due-charges), ретраи с экспоненциальной задержкой+джиттер, окно и число попыток — политика (A3); сверка ежедневная.
6. Данные: минимизация ПДн, audit.
Alternatives:
- R1 mandate-first (chosen)
- R2 recurring QR: сохранить подтверждение каждого платежа (link/notification) — отвергнут: не решает задачу (нужно действие клиента каждый раз)
- R3 «автоплатёж на стороне банка плательщика» (direct debit только для клиентов нашего банка) — отвергнут: не покрывает клиентов других банков (СБП — межбанковский), фрагментация
- R4 карточный рекуррент (Visa/MC/НСПК карты) — отвергнут: вне СБП, другая регуляторика/инфраструктура, не цель
- R5 внешний job-планировщик вместо in-core outbox — отвергнут по смыслу? Actually that's execution alternative; include as row: «внешний планировщик дёргает API» — минусы: обход инвариантов, двойные запуски, нет атомарности с outbox.
Consequences +/-: positive: снимает ручное действие, покрывает межбанк, переиспользует статусную машину/АБС/возвраты/сверку. Negative: новая сущность и её жизненный цикл; взрывной характер списаний на границах периодов; отзыв и race; зависимость от протокола НСПК (внешний вход); рост регуляторной поверхности (согласие = правовое основание); операционная нагрузка dunning.
Reversibility: costly. Existing consents — во внешнем реестре и имеют юридический вес; «выключить» можно (прекратить новые + honor/отозвать существующие), но без потери данных и без нарушений. Expiry: пересмотр после получения протокола НСПК и пилота; при изменении модели согласия НСПК.

ADR-009 Context: ADR-007 (Accepted) + AD-008 [ADOPTED] зафиксировали гибрид и границу ядра/транспорта. Рекуррентные списания — иной сценарий протокола участника (реестр согласий, инициация списания, отзыв) [ТРЕБУЕТ ПРОВЕРКИ]. Нужно решить, кто реализует этот транспорт.
Alternatives:
- A: расширить область существующего вендорского адаптера ОПКЦ (same vendor) — плюсы: одна граница, один контракт, меньше интеграций; минусы: расширение scope контракта/сертификации, зависимость сроков от вендора.
- B: отдельный вендорский адаптер подписок — плюсы: независимые сроки/сертификация; минусы: второй вендор/интеграция, риск расхождения моделей, дублирование эксплуатации.
- C: реализовать транспорт подписок собственными силами — отвергнут: редкие компетенции, сертификация, риск испытаний (как rejected ADR-007).
Decision: (proposed, A3) — рекомендация A (расширить область существующего адаптера) при подтверждении, что протокол подписок доступен тому же вендору и укладывается в одну сертифицированную поставку; иначе B. Плюс: ядро остаётся контрактно-независимым; внутренний контракт адаптера расширяется новыми операциями (registerConsent, getConsentStatus, createDebit, cancel/revoke notifications), а не переиспользует QR-операции.
Constraints: не начинать транспорт подписок до подписания/расширения контракта и получения документации НСПК (AD-008); сертификаты ФСТЭК/НСПК; идемпотентность по reference; тестовый контур с сценариями отзыва/лимитов.
Consequences ±, Reversibility: reversible (граница контракта), при выборе B — costly.
A3 Decision package block {choice, rationale, constraints, rejected options, expiry} — but choice should be "recommended" not decided, since it's for human. ADR status Proposed. I'll present "A3 Decision (пакет для человеческого решения)" with `recommendation` field. Per significance-routing A3 must be machine-readable {choice, rationale, constraints, rejected options, expiry}. Since the human decides, I'll write `choice: "extend-existing-adapter (recommended)"` and note it's a recommendation pending A3.

### Contract delta (openapi)
Version 0.2.0. Add paths:
- `/v1/consents` POST createConsent
- `/v1/consents` GET listConsents (optional params tspId, status)
- `/v1/consents/{consentId}` GET getConsent
- `/v1/consents/{consentId}/cancel` POST cancelConsent (ТСП-инициируемая отмена)
- `/v1/consents/{consentId}/charges` GET listCharges
- `/v1/consents/{consentId}/charges` POST createCharge (on-demand/retry within limits)
Schemas: ConsentRequest, Consent, ConsentLimits, ConsentStatus enum, ChargeAttempt, ChargeRequest.
Payment: add optional `consentId`.
Errors added to docs; openapi currently has no error component — I'll add a Problem schema and error responses? Keep minimal but useful: add `Problem` schema and reference in new operations; but adding error responses to existing ops would be a change (additive, non-breaking). I'll not modify existing operations to avoid churn; just add `Problem` schema + use in new paths. Hmm, better to also keep consistency. Minimal: new paths get 4xx with Problem.
Webhook events are not in openapi (webhooks documented in markdown). I'll document new event types in the spec delta + design; optionally add `webhooks:` top-level (OpenAPI 3.1) — but it's 3.0.3. Skip; document in spec.

Let me keep the openapi edit careful and valid. I'll write the full new file (additive) preserving existing content. Must preserve YAML validity.

Let me now also plan the arch-be DELTA.md:
```
# Дельта: add-sbp-recurring-payments
- Route: Critical (полный Solutioning; оценка 10/15)
- Created: 2026-09-28
## Проблема
...
## ADDED
- требования (ссылка на openspec delta)
- spine AD-009..AD-011
- ADR-008, ADR-009
- контракт v0.2.0
## MODIFIED
- ARCHITECTURE-SPINE.md: добавляются блоки AD-009..AD-011 (Proposed) — правка защищённого файла покрыта этой дельтой
- распространяется область AD-003, AD-005, AD-007 на согласия/списания (без изменения текста исходных блоков)
- docs/contracts/tsp-api.md (живая истина) — обновляется на этапе archive (вливание дельты)
## REMOVED
- нет
## План отката
## Критерии приёмки
```
The delta guard: "каждый изменённый защищённый файл обязан упоминаться в активной дельте". So DELTA.md must mention "ARCHITECTURE-SPINE.md" literally. Yes.

Also the delta validator may require certain structure. Let me check `arch-be delta validate --help` / template: DELTA_TEMPLATE has sections: Проблема, ADDED, MODIFIED, REMOVED, План отката, Критерии приёмки, header with Route/Created. I'll follow exactly. Use `arch-be delta new` to scaffold, then fill with edit. That guarantees structure. Let me do that.

### Handoff package
`.arch-handoff-recurring/`:
- TASK.md — task for implementers + JSON result contract.
- ARCHITECTURE.md — epic-context 800–1500 tokens, by meaning: goal, interfaces, invariants verbatim (AD-002, AD-003, AD-005, AD-001, AD-009..AD-011 rules), prohibitions, scope.
- CONSTRAINTS.yaml — fitness rules (executable): 
  - file_exists ARCHITECTURE-SPINE.md
  - must_contain spine AD-009..AD-011 patterns
  - must_contain openapi for /v1/consents
  - must_not_contain in code: debit path without consent check? Can't easily. Use command_succeeds: a test command placeholder. Hmm, CONSTRAINTS at arch stage: the existing .arch-handoff/CONSTRAINTS.yaml uses file_exists/must_contain. I'll mirror that style plus a couple of behavioral rule templates referencing future tests. Mark command_succeeds rules as placeholders? The gate would execute them; exit 1 if they fail. In the delta handoff, tests don't exist yet → command_succeeds would fail. Better to include only static rules now + name the behavioral rules to be added at code stage (as comments/list). Actually the existing CONSTRAINTS has severity warn/error static only. I'll include static rules that pass now, plus (as comments) the behavioral rules to add at implementation. Hmm, but "rule without check" is an antipattern. I'll include static enforceable rules and note that behavioral rules land with the code.
  
  Wait — importantly, does the gate read `.arch-handoff/CONSTRAINTS.yaml` by default (`--constraints` default `<repo>/.arch-handoff/CONSTRAINTS.yaml`)? Yes. So my new package's CONSTRAINTS won't be picked up by the default gate. That's fine; it's a package for the implementer, and when they apply, they'd regenerate/merge into `.arch-handoff/`. I'll note this in TASK.md / MANIFEST.
- RUBRIC.yaml — copy the anchor rubric handoff_quality? The skill says RUBRIC.yaml = якорная рубрика приёмки. I can copy `.arch-handoff/RUBRIC.yaml` (handoff_quality) — but that rubric is about handoff quality, not the implementation. Hmm, the existing RUBRIC.yaml is `handoff_quality` used to evaluate the handoff package output. I'll reuse it (copy) since that's the repo's anchor rubric, plus maybe add a criteria set for the delta. Simplest and honest: copy the existing RUBRIC.yaml unchanged and note it. Actually better: the handoff RUBRIC evaluates the implementer's result (handoff_quality) — the existing one is exactly that. Copy it.
- adr/ → ADR-008, ADR-009 (new). 
- MANIFEST.json — meta (created_at, sources, tokens estimate, task).
- README.md (in package) — how to use + merge note. Optional; I'll include a short one to explain the two-package situation. Actually MANIFEST + TASK suffice. I'll add a short `README.md` in the package explaining why the dir is separate — helpful for the human. Hmm, maybe put that note in my final response instead and in TASK.md. I'll add a brief note at the top of MANIFEST via a "note" field. Keep files: TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, adr/ADR-008, adr/ADR-009.

Epic-context token budget: 800–1500 tokens. ARCHITECTURE.md must be by meaning. But it must include spine Rules verbatim (invariants). Rules are short. OK.

Let me now also verify: `arch-be control spine ARCHITECTURE-SPINE.md` after edit; `arch-be gate`; `arch-be contract-diff`; `openspec validate --change ... --strict`.

Let me create ADRs using the tool first (to get proper numbering), then write everything.

Let me run `arch-be control adr --dir docs/adr "..."`. Two calls. Let me check what it outputs/creates.

Titles:
- ADR-008: "Рекуррентные C2B-списания: согласие плательщика как предусловие и модель исполнения списаний"
- ADR-009: "Транспорт подписок СБП: область вендорского адаптера ОПКЦ"

Slug will be transliterated likely.

Let me run.

Also create arch-be delta via `arch-be delta new add-sbp-recurring-payments`.

Let me batch these three commands (they're independent writes but same repo; fine sequentially in one call).
I have the full picture. Let me scaffold the ADRs with the harness tool and the arch-be delta (needed to legally edit the protected spine file).

  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisaniy)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/changes/add-sbp-recurring-payments/DELTA.m)`

Let me read the scaffolds to see the format produced (adr template + delta template).

  `write_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisaniy, content="# ADR-008. Рекуррентные C2B-списания: согласие плательщика как предусловие и модель исполнения списаний\n\n- Date: 2026-09-28\n- Status: Pr)`

Now let me write all the files. I'll start with the ADRs (full content), then the spine edit, then openapi, then OpenSpec artifacts, then DELTA.md, then handoff package.

Let me write ADR-008.

I need to be careful about the ADR tool's parsing expectations: header with Date/Status, sections. Also `- Модель-автор:` line — the skill says judges read author from header. I should add `- Модель-автор: qwen3-coder (агент); ревью — human` or per the skill "Пишите human или human:<имя>, если документ писал человек, и метку модели, если его собрал агент." I'm an agent → write model label. I don't know the exact model name. I'll write `- Модель-автор: qwen-code (агент)`. Hmm, risky to guess a model name. The skill says "метку модели". I'll write `- Модель-автор: qwen-code-agent`. Let me check if other ADRs have this line — they don't (ADR-001..007 have Owner instead). To match existing repo style, ADR-001 uses `- Owner:`. The tool's template doesn't include Owner or Модель-автор. The adr-authoring skill says to include Модель-автор. Since existing ADRs use `- Owner:` and `- Related:`, I'll follow repo convention (Owner + Related) AND add `- Модель-автор: qwen-code (агент)`. Wait, but "Дата: 2026-09-28" — tool set Date. Fine.

Hmm, careful: the skill says the adr registry parser understands `- Date:`, `- Status:`, `- Модель-автор:`. Adding Owner/Related is fine. Let me match ADR-001..007 style: `- Owner:` and `- Related:`. I'll add both plus author-model.

Let me now write ADR-008 content.

I'll write in Russian, dense.

---

Let me draft ADR-008 fully.

# ADR-008. Рекуррентные C2B-списания: согласие плательщика как предусловие и модель исполнения списаний

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур) + владелец продукта СБП
- Related: ADR-002, ADR-004, ADR-005, ADR-009, AD-002, AD-003, AD-005, AD-009, AD-010, AD-011
- Модель-автор: qwen-code (агент); решение требует ратификации человеком (A3)

## Context

Принятое решение (ADR-001..007) обслуживает разовый приём C2B: платёж существует от регистрации QR до зачисления, инициатива — у плательщика (сканирование/подтверждение), ТСП получает деньги только после статуса `PAID` от НСПК. ТСП (кинотеатры, ЖКХ, связь) просят **подписки**: периодическое списание со счёта плательщика без его участия в каждом платеже.

СБП поддерживает C2B-платежи по согласию плательщика (мандат): согласие даётся плательщиком в приложении **его** банка, регистрируется в СБП, списание инициируется ТСП/эквайером в рамках условий согласия; плательщик может согласие отозвать. Точный протокол (реестр согласий, поля, сроки, отзыв, лимиты) — **внешний вход** `[ТРЕБУЕТ ПРОВЕРКИ]` (документация НСПК по договору, как в ADR-003).

Силы:
- согласие — **юридическое основание** для списания: списание без действующего согласия или сверх его лимитов недопустимо;
- отзыв согласия должен прекращать будущие списания; «уже списанное» требует возврата, а не отмены;
- согласие живёт долго (месяцы/годы) — это новая долгоживущая сущность с собственным жизненным циклом, отличным от жизненного цикла платежа;
- списания группируются на границах периодов (1-е число, биллинговый цикл) → взрывной характер нагрузки;
- финансовое последствие ошибки (несанкционированное списание, двойное списание) — инцидент с регуляторными последствиями; аудит обязателен (AD-007).

## Decision

1. **Согласие (mandate) — самостоятельная сущность** с жизненным циклом `PENDING_PAYER → ACTIVE → (SUSPENDED) → REVOKED | EXPIRED`. Источник истины по согласию — реестр СБП (НСПК); ядро шлюза хранит **зеркало согласия** и синхронизирует его событиями/сверкой. Решение о допустимости списания принимается по локальному зеркалу в состоянии `ACTIVE`.
2. **Списание невозможно без действующего согласия и в пределах лимитов** (лимит на списание, на период, суммарный, срок действия). Проверка — предусловие инициации списания в шлюзе (spine AD-009).
3. **Списание исполняется как платёж существующей статусной машины** (ADR-002) с атрибутом `consentId`: `CREATED → PAID → CREDITED → COMPLETED`; шаг выпуска QR отсутствует, его место занимает инициация списания в СБП. Зачисление по-прежнему **только из `PAID`** (AD-005). Возвраты — существующая сага (ADR-005).
4. **Идемпотентность попытки списания** (spine AD-011): ключ попытки детерминирован от `(consentId, billingPeriod, attemptSeq)` и передаётся как `reference` в адаптер и как внешний ключ в АБС; повтор (ретрай, повторная нотификация, повторный запуск планировщика) не создаёт второе списание.
5. **Отзыв согласия приоритетен** (spine AD-010): отзыв фиксируется атомарно («состояние + outbox + аудит»); попытки, не подтверждённые ОПКЦ, блокируются; подтверждённые — доводятся до конца и при необходимости компенсируются возвратом. Гонка «списание в полёте / отзыв» разрешается в пользу отзыва для всего, что ещё не подтверждено оператором.
6. **Исполнение списаний — планировщик в ядре шлюза**, работающий по outbox/очереди: наступившие сроки порождают идемпотентные попытки; повторы при транзиентных сбоях — экспоненциальная задержка + джиттер, окно и число попыток — политика (выносится на A3); очередь сглаживает пики, per-ТСП честность ограничивает влияние крупного ТСП. Сверка согласий и списаний с НСПК — по регламенту (расширение ADR-004).
7. **Данные**: минимизация ПДн плательщика (идентификатор согласия/маскированный признак, без реквизитов счёта), шифрование в покое, маскирование в логах; жизненный цикл согласия и каждое списание — в неизменяемом аудит-логе (AD-007).

## Alternatives Considered

| Вариант | Плюсы | Минусы | Почему отвергнут |
|---|---|---|---|
| A. Согласие в СБП, инициация списания эквайером (выбран) | Межбанковский охват (клиент любого банка); нет действия клиента на каждый платёж; опора на реестр СБП | Зависимость от протокола НСПК; новая сущность и её жизненный цикл; гонки при отзыве | — |
| B. Повторяющийся QR/ссылка с подтверждением каждого платежа | Ничего нового в протоколе; минимум изменений | Не решает задачу: плательщик подтверждает каждое списание | Не выполняет требование бизнеса |
| C. Автоплатёж на стороне банка (списание по внутреннему поручению) | Просто для клиентов нашего банка | Не покрывает клиентов других банков; не СБП; фрагментация предложения | СБП — межбанковский сервис; теряется охват |
| D. Карточный рекуррент (карты) | Зрелый механизм | Вне СБП: другая инфраструктура, регуляторика, комиссии | Вне границ принятого решения |
| E. Согласие хранится только локально, без реестра СБП | Нет зависимости от внешнего реестра | Нет межбанковского признания согласия плательщиком; юридически несостоятельно | Согласие должно быть подтверждено банком плательщика |
| F. Внешний планировщик вызывает API шлюза по расписанию | Проще для планирования | Обход атомарности «статус+outbox», риск двойных запусков и пропусков, дублирование источников истины | Нарушает AD-002/AD-003 |

## Consequences

### Positive

- Рекуррентные списания покрывают клиентов любого банка-участника СБП без действий плательщика на каждый платёж.
- Переиспользуются существующие контуры: статусная машина, outbox, идемпотентность, АБС-зачисление, сага возвратов, сверка (ADR-001..005) — изменение добавляет сущность, а не новый финансовый контур.
- Юридически корректная модель: согласие подтверждено банком плательщика и хранится в СБП.
- Полный аудит согласий и списаний.

### Negative

- Новая долгоживущая сущность и её жизненный цикл: расширение модели данных, миграции, операционная поддержка.
- Взрывной характер списаний на границах периодов — требуется запас мощности, сглаживание и per-ТСП честность.
- Гонка «списание в полёте / отзыв согласия» и частичные исходы требуют явных тестов и runbook; возможны компенсирующие возвраты.
- Зависимость от протокола НСПК (внешний вход) — сроки и полнота модели ограничены документацией.
- Рост регуляторной поверхности: согласие — правовое основание, ПДн плательщика, аудит, возможные требования к хранению.
- Планировщик и ретраи добавляют эксплуатационную нагрузку (наблюдаемость, DLQ, расхождения).

## Reversibility

**costly.** Технически изменение обратимо (фиче-флаг, остановка новых согласий), но у уже выданных согласий есть юридический вес и внешнее состояние в реестре СБП: их нельзя «удалить» — можно только прекратить использование и/или отозвать. Откат не должен терять записанные согласия и обязательства (RPO=0). Пересмотр: (а) при получении протокола НСПК и расхождении модели; (б) по итогам пилота (первые 3 месяца); (в) при изменении модели согласий в СБП.

## References

- AD-009, AD-010, AD-011 (spine) — новые инварианты
- ADR-002 (статусная машина/идемпотентность), ADR-004 (нотификации/сверка), ADR-005 (зачисление из PAID, сага возвратов), ADR-006 (НПС/ПДн/аудит), ADR-009 (транспорт подписок)
- `openspec/changes/add-sbp-recurring-payments/` — дельта и требования
- Протокол НСПК по подпискам — `[ТРЕБУЕТ ПРОВЕРКИ]` (внешний вход)

---

Good. Now ADR-009.

# ADR-009. Транспорт подписок СБП: область вендорского адаптера ОПКЦ

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур) + закупки/проектный офис + ИБ
- Related: ADR-003, ADR-007, ADR-008, AD-004, AD-008
- Модель-автор: qwen-code (агент); решение требует A3 (затрагивает Accepted ADR-007)

## Context

ADR-007 (Accepted, A3 от 2026-08-15) зафиксировал гибрид: ядро — собственная разработка, транспорт к ОПКЦ — сертифицированный вендорский модуль; AD-008 [ADOPTED] требует контрактной независимости ядра от транспорта и запрета реализации транспорта до подписания контракта и получения документации НСПК. RFP (docs/rfp/vendor-rfp.md) сформирован под сценарий разовых C2B-платежей (QR/ссылка, нотификации, возвраты).

Рекуррентные списания — **иной сценарий протокола участника**: реестр согласий, инициация списания по согласию, отзыв/приостановка, лимиты, возможно — отдельные нотификации. Полный состав протокола — `[ТРЕБУЕТ ПРОВЕРКИ]` до получения документации НСПК. Нужно решить, кто реализует этот транспорт и как он соотносится с уже принятой границей ядро/адаптер.

Силы: сохранить контрактную независимость ядра (AD-008); не дублировать эксплуатацию двух вендорских контуров без необходимости; не расширять scope сертификации/контракта молча; держать сроки, если протокол подписок у того же вендора недоступен.

## Decision (рекомендация к A3)

1. Ядро остаётся контрактно-независимым: протокол подписок СБП знает **только транспортный адаптер**; ядро общается с ним через **расширенный внутренний контракт** (`docs/contracts/opkc-adapter.md`: новые операции `registerConsent`, `getConsentStatus`, `cancelConsent`, `createDebit`, `getDebitStatus`; новые события `consent.*`, `debit.*`), а не через QR-операции.
2. **Рекомендуемый вариант A (по умолчанию): расширить область существующего вендорского адаптера ОПКЦ** на сценарий подписок — при условии, что вендор подтверждает поддержку протокола подписок, проходит по сертификатам ФСТЭК/НСПК и обеспечивает идемпотентность по `reference` для новых операций. Тогда RFP/контракт с вендором расширяется (это изменение scope, а не новый вендор).
3. **Если вендор не покрывает подписки** — вариант B: отдельный сертифицированный адаптер/модуль подписок с той же границей контракта; это самостоятельное решение с новым вендором и повторной процедурой RFP.
4. Ограничения (наследуются из AD-008/ADR-007): реализация транспорта подписок начинается только после расширения/подписания контракта и получения документации НСПК; сертификаты и СКЗИ/HSM — обязательны; тестовый контур должен позволять сценарии отзыва, лимитов, повторов.
5. Собственная реализация транспорта подписок (вариант C) отклоняется по тем же причинам, что в ADR-007 (компетенции, сертификация, риск испытаний).

## A3 Decision (пакет для человеческого решения)

- **choice**: рекомендовано `extend-existing-adapter` (вариант A); альтернатива `separate-subscriptions-adapter` (вариант B) — при отказе вендора.
- **rationale**: одна сертифицированная поставка и одна граница контракта дешевле в эксплуатации; ядро не зависит от выбора; вариант B сохраняется как явный fallback, не «тихий» обход.
- **constraints**: (1) поддержка протокола подписок вендором; (2) сертификаты ФСТЭК/НСПК и СКЗИ для новых операций; (3) идемпотентность новых мутирующих операций по `reference`; (4) тестовый контур со сценариями отзыва/лимитов; (5) старт транспорта — после контракта и документации НСПК (AD-008).
- **rejected options**: `in-house-subscriptions-transport`, `defer-subscriptions-transport` (переносить нельзя: без транспорта нет функционала).
- **expiry**: пересмотр при (а) недоступности подписок у текущего вендора; (б) выделении протокола подписок в отдельную сертификационную поставку; плановая ревизия — вместе с ADR-007 (12 мес. боевой эксплуатации).

## Alternatives Considered

| Вариант | Плюсы | Минусы | Почему (не) выбран |
|---|---|---|---|
| A. Расширить существующий адаптер | Одна поставка/граница; меньше интеграций и эксплуатации; единый тестовый контур | Расширение scope контракта и сертификации; зависимость сроков от вендора | Рекомендован при подтверждении вендором |
| B. Отдельный адаптер подписок | Независимые сроки/сертификация; изоляция сценария | Второй вендор/контур; дублирование эксплуатации; риск расхождения моделей | Fallback при отказе вендора A |
| C. Собственный транспорт подписок | Нет вендорской зависимости | Редкие компетенции (ГОСТ/СКЗИ/протокол), длинные сроки, риск не пройти испытания НСПК | Отклонён (как в ADR-007) |

## Consequences

### Positive

- Ядро сохраняет контрактную независимость; выбор транспорта обратим за счёт границы.
- Одна (или явно две) сертифицированные поставки вместо скрытого расползания протокола.
- RFP-процесс переиспользуется; критерии сертификации/идемпотентности уже сформулированы.

### Negative

- Расширение scope контракта/сертификации у вендора — риск сроков (вариант A) или новая закупка (вариант B).
- Внутренний контракт адаптера расширяется — требуется версионирование и тесты совместимости.
- Возможное расхождение сроков «транспорт подписок» и «ядро подписок» — планирование волн.

## Reversibility

**reversible** (вариант A и B): выбор транспорта — за границей внутреннего контракта; смена вендора не меняет ядро. Переход A→B — **costly** (повторная закупка/сертификация), но архитектурно возможен.

## References

- ADR-007 (Accepted) — гибрид и constraints; ADR-003 (транспорт/СКЗИ); ADR-008 (модель согласия)
- AD-004, AD-008 (spine)
- `docs/contracts/opkc-adapter.md`, `docs/rfp/vendor-rfp.md`

---

Good. Now the spine blocks. Append AD-009..AD-011 before "## Deferred" section? The current spine has sections: header, AD-001..AD-008, "## Deferred", "## Контракты и версии". I'll insert new blocks after AD-008 and before "## Deferred". Must match format: `## AD-009. Title`, `- Status:`, `- **Binds**:`, `- **Prevents**:`, `- **Rule**:`. Keep style consistent. Status: Proposed (ADR-008).

AD-009:
## AD-009. Списание по согласию — только при действующем согласии и в пределах лимитов
- Status: Proposed (ADR-008)
- **Binds**: сервис согласий, оркестратор списаний, адаптер ОПКЦ, адаптер АБС.
- **Prevents**: списание без действующего согласия плательщика; списание сверх лимитов согласия (на платёж/период/итог/срок); «списание из воздуха» по истёкшему или отозванному согласию.
- **Rule**: инициация любого списания требует локального состояния согласия `ACTIVE` и прохождения проверки лимитов в той же транзакции, что и создание попытки; иначе — отказ без обращения к ОПКЦ/АБС. Fitness: попытка списания при `REVOKED`/`EXPIRED`/превышении лимита не создаёт записи о списании и не вызывает адаптеры.

AD-010:
## AD-010. Приоритет отзыва согласия и единый источник истины по согласию
- Status: Proposed (ADR-008)
- **Binds**: хранилище согласий шлюза, оркестратор списаний, адаптер ОПКЦ, нотификатор ТСП, аудит-лог.
- **Prevents**: продолжение списаний после отзыва плательщиком; неотражённый/потерянный отзыв; расхождение «плательщик отозвал — шлюз считает согласие активным».
- **Rule**: изменение состояния согласия (включая отзыв/приостановку) и запись события в outbox выполняются в одной локальной транзакции; отзыв запрещает все попытки, не подтверждённые ОПКЦ, и инициирует компенсацию (возврат) для уже подтверждённых; состояние согласия — из зеркала реестра СБП, сверяемого с НСПК. Fitness: отзыв, применённый до подтверждения, делает невозможной любую новую попытку по этому согласию.

AD-011:
## AD-011. Идемпотентность попытки списания по согласию
- Status: Proposed (ADR-008)
- **Binds**: оркестратор списаний (планировщик/ретраи), адаптер ОПКЦ, адаптер АБС, outbox.
- **Prevents**: двойное списание при повторе планировщика, ретрае сети или повторной нотификации; двойное зачисление по одному billing-периоду.
- **Rule**: ключ попытки детерминирован от `(consentId, billingPeriod, attemptSeq)` и передаётся как `reference` в адаптер ОПКЦ и как внешний ключ в АБС; повторная обработка того же ключа не создаёт второй операции и возвращает существующий результат. Fitness: повторный запуск планировщика/повторная нотификация по одной попытке → ровно одно списание и одно зачисление.

Good. Now openapi. Let me write the full new file (additive). Keep existing structure and add.

I'll write version 0.2.0 and add:
- /v1/consents POST+GET
- /v1/consents/{consentId} GET
- /v1/consents/{consentId}/cancel POST
- /v1/consents/{consentId}/charges GET+POST
- components.schemas: ConsentRequest, Consent, ConsentLimits, ConsentStatus, ChargeRequest, ChargeAttempt, ChargeStatus, Problem
- Payment: add optional consentId
- Also add `description` in info? Add a note about versioning.

Be careful with YAML. Let me write it.

Also add OperationId/Idempotency-Key header for POSTs.

Now the OpenSpec files.

proposal.md — sections Why / What Changes / Capabilities / Impact + extra "## Significance and Route (A1)".

spec delta — capability `sbp-recurring-payments`, with Purpose + ADDED Requirements. Requirements (each with ≥1 scenario, 4-hashtag scenarios, WHEN/THEN):

1. Requirement: Регистрация согласия на рекуррентные списания (ТСП инициирует, плательщик подтверждает в своём банке). Scenarios: created pending; payer confirms → ACTIVE; payer declines → REJECTED.
2. Requirement: Списание только по действующему согласию и в пределах лимитов.
3. Requirement: Отзыв согласия прекращает будущие списания (priority) + компенсация подтверждённых.
4. Requirement: Идемпотентность списания (повтор не создаёт второе списание).
5. Requirement: Зачисление только по подтверждённому статусу (сохранение AD-005 для списаний по согласию) — MODIFIED? It's a new capability spec, so describe as ADDED requirement referencing preserved invariant.
6. Requirement: Нотификации ТСП о событиях согласий и списаний (at-least-once, dedup by eventId).
7. Requirement: Измеримые NFR рекуррентных списаний (burst handling, start-lag, revocation latency, availability/RPO, zero unauthorized/duplicate).
8. Requirement: Совместимость контракта ТСП (обратно совместимое расширение; существующие потребители не затронуты).
9. Requirement: Аудит и защита ПДн согласий.

Also maybe: Requirement: Сверка согласий и списаний с НСПК.

That's ~9 requirements — good spec. Each with scenarios.

design.md — Context, Goals/Non-Goals, Decisions (with alternatives), Risks/Trade-offs, Migration Plan, Open Questions. Must include: impact on spine invariants table, contract delta description, NFR table, acceptance criteria, rollback, what's for human architect. The design.md is the place for the full architecture package narrative. Also reference ADRs.

tasks.md — grouped tasks with verification per task, tests per group. Since code not written now, tasks are the implementation plan for после A3. Fine.

DELTA.md — arch-be delta.

Handoff package.

Let me now write. I'll do multiple write_file calls. Given size, I'll be efficient but complete.

Let me write ADR-008 first (replace whole file). I'll use write_file since I already read it (scaffold). Yes, I read it.

Actually for editing scaffolded ADR, I can use write_file (file was read). Good.

Let me write.
Now I'll write the ADRs. Starting with ADR-008 (consent/mandate model).

  `write_file(content="# ADR-009. Транспорт подписок СБП: область вендорского адаптера ОПКЦ\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: solution-architect, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/adr/ADR-009-transport-podpisok-sbp-ob)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/adr/ADR-009-transport-podpisok-sbp-ob)`

I need to read ADR-009 first (I only read ADR-008 scaffold). Let me read it, then write.

  `write_file(content="# ADR-009. Транспорт подписок СБП: область вендорского адаптера ОПКЦ\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: solution-architect, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/docs/adr/ADR-009-transport-podpisok-sbp-ob)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now edit ARCHITECTURE-SPINE.md: insert AD-009..AD-011 after AD-008 block, before "## Deferred".

Let me use edit with the anchor being the "---\n\n## Deferred" region. The file has:

```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll insert new blocks between "---" and "## Deferred".

Also update the header line? "Данный spine — уровень feature." Fine. Maybe add a note that AD-009..011 добавлены 2026-09-28 (delta add-sbp-recurring-payments). Good to leave an audit trail. I'll add a line in the block status referencing the change.

Let me edit.
Now the spine — adding the new invariants as `Proposed` blocks (the mechanism this spine itself documents), covered by the delta.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\n  description: >\n    Мерчант-API СБП-шлюза. Версия 0.2.0 — обратно с, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/openapi/tsp-api.yaml")`

Now edit openapi/tsp-api.yaml additively. I read it. Let me write the new full file with version 0.2.0 and new paths/schemas, preserving existing.

Careful to keep it valid YAML/OpenAPI.

Let me compose.

```yaml
openapi: 3.0.3
info:
  title: СБП-шлюз — API ТСП
  version: 0.2.0
  description: >
    Мерчант-API СБП-шлюза. Изменение 0.2.0 — обратно совместимое расширение:
    добавлены ресурсы согласий (рекуррентные списания) и опциональное поле
    consentId у платежа; существующие пути, поля и значения не изменены.
paths:
  /v1/payments: (unchanged)
  /v1/payments/{paymentId}: (unchanged)
  /v1/consents:
    post: createConsent
    get: listConsents
  /v1/consents/{consentId}:
    get: getConsent
  /v1/consents/{consentId}/cancel:
    post: cancelConsent
  /v1/consents/{consentId}/charges:
    get: listConsentCharges
    post: createConsentCharge
components:
  schemas:
    PaymentRequest: (unchanged) + optional consentId? A payment created manually? Keep unchanged.
    Payment: unchanged + consentId optional
    ConsentRequest
    Consent
    ConsentLimits
    ChargeRequest
    ChargeAttempt
    Problem
```

Let me write it carefully. Keep existing formatting minimal but consistent-ish (the file uses flow style). I'll use block style for new parts for readability, mixing is fine in YAML.

Regarding `Consent.status` enum: [PENDING_PAYER, ACTIVE, SUSPENDED, REVOKED, EXPIRED, REJECTED].
`ChargeAttempt.status`: reuse payment statuses [CREATED, PAID, CREDITED, COMPLETED, FAILED] (no QR/EXPIRED/REFUNDED? refunds possible). Simpler: ChargeAttempt returns payment fields: chargeId (=paymentId), consentId, billingPeriod, attemptSeq, amount, status, createdAt, completedAt, errorCode. reuse status enum values [CREATED, PAID, CREDITED, COMPLETED, FAILED, REFUNDED].

Payment schema: add `consentId: {type: string, nullable: true}` optional. openapi 3.0 nullable true.

Add `ConsentRequest` required [tspId, payerRef?, limits, purpose, validUntil?]. Hmm, how does ТСП specify the payer? In SБП subscriptions, the consent is tied to a payer identified by phone or by a token from СБП. Since protocol TBD, model it as `payerRef` (маскированный идентификатор плательщика, формат — по протоколу НСПК [ТРЕБУЕТ ПРОВЕРКИ]) — required? The ТСП knows subscriber (their customer) — e.g., phone. I'll make `payerRef` required (string, описание: идентификатор плательщика для СБП — телефон/токен; финальный формат — по протоколу НСПК).

ConsentLimits: maxAmountPerCharge (int kopecks), maxAmountPerPeriod, maxChargesPerPeriod, period (enum MONTH/DAY/WEEK/...), maxTotalAmount, validUntil (date-time). All optional except maybe period. I'll make them optional with description that final set — per НСПК.

Consent: consentId, status, tspId, payerRefMasked, limits, purpose, createdAt, activatedAt, revokedAt, validUntil, qrUrl/consentUrl (deeplink для передачи плательщику — опц.), nextChargeAt (опц.).

ChargeRequest: amount (int), billingPeriod (string), attemptSeq (int, opt, default auto), idempotencyKey? No — via header. description opt.

Also note Idempotency-Key required for POST /v1/consents and POST /v1/consents/{consentId}/charges and /cancel? Cancel is idempotent but let's require for consistency. I'll require Idempotency-Key on createConsent and createConsentCharge; cancel — optional.

Problem schema: type, title, status, detail, code, traceId.

New error codes documented via description.

Let me write the file.

Also, since I add new enum-ish error codes only in docs (design/spec), the openapi remains non-breaking.

One more: the existing `Payment.status` enum includes 8 values; a recurring charge may also be in these states. Fine, no change.

Also add `Idempotency-Key` to new POSTs and a 429/409/422 responses referencing Problem.

Let me write.
Now the contract — an additive, backwards-compatible extension of `openapi/tsp-api.yaml` (minor version bump, no changes to existing paths/fields).

  `write_file(content="# Proposal\n\n## Why\n\nТСП — онлайн-кинотеатры, ЖКХ, связь — просят **рекуррентные C2B-списания по согласию плательщика** (подписки СБП). , file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/openspec/changes/add-sbp-recurring-payment)`

Now the OpenSpec artifacts. Start with proposal.md.

proposal.md with sections Why, What Changes, Significance and Route (A1), Capabilities, Impact.

Let me write.

Note config: keep OpenSpec structural headings in English; content in ru.

Capabilities: New: `sbp-recurring-payments`. Modified: none (openspec/specs empty). Hmm — instruction says Modified Capabilities only if spec-level behavior changes for existing specs. There are no existing specs, so leave Modified empty and note. But I need to say no existing spec is modified (openspec/specs is empty). I'll write "нет (openspec/specs пуст; изменения принятой архитектуры зафиксированы дельтой arch-be и ADR-008/009)".

Let me write proposal.
Now the OpenSpec change artifacts. Proposal first (includes the significance/route assessment):

  `write_file(content="# Spec Delta\n\n## Purpose\n\nПозволяет ТСП инициировать повторяющиеся C2B-списания со счёта плательщика по его согласию (подписке СБП), за, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/openspec/changes/add-sbp-recurring-payment)`

Now the spec delta. Path: `openspec/changes/add-sbp-recurring-payments/specs/sbp-recurring-payments/spec.md`.

Requirements in ADDED with `### Requirement:` and `#### Scenario:` with WHEN/THEN. Language ru, SHALL kept English.

Let me draft ~9 requirements with scenarios. Keep requirement text with SHALL.

R1: Регистрация согласия плательщика
The система SHALL регистрировать согласие по запросу ТСП и SHALL переводить его в ACTIVE только после подтверждения плательщиком (через банк плательщика/СБП).
Scenarios:
- WHEN ТСП отправляет POST /v1/consents с валидными данными и Idempotency-Key, THEN система создаёт согласие в состоянии PENDING_PAYER и возвращает consentId.
- WHEN плательщик подтверждает согласие, THEN согласие переходит в ACTIVE и система отправляет вебхук consent.activated.
- WHEN плательщик отклоняет согласие, THEN согласие переходит в REJECTED, списания по нему невозможны.
- WHEN ТСП повторяет POST с тем же Idempotency-Key и телом, THEN возвращается то же consentId без создания нового согласия.

R2: Списание только по действующему согласию и в пределах лимитов
The система SHALL инициировать списание только при состоянии согласия ACTIVE и в пределах лимитов; SHALL отклонять иное без обращения к ОПКЦ и АБС.
Scenarios:
- WHEN попытка списания при ACTIVE и в пределах лимитов, THEN создаётся попытка и передаётся в ОПКЦ.
- WHEN попытка при REVOKED/EXPIRED/SUSPENDED/PENDING_PAYER, THEN отказ (CONSENT_NOT_ACTIVE/CONSENT_REVOKED/...) и ни одного обращения к ОПКЦ/АБС.
- WHEN сумма превышает лимит (на операцию, период или суммарный), THEN отказ CONSENT_LIMIT_EXCEEDED без списания.

R3: Зачисление только по подтверждённому статусу (сохранение AD-005)
Scenarios:
- WHEN списание по согласию подтверждено ОПКЦ (PAID), THEN система инициирует зачисление в АБС; WHEN статус не PAID, THEN зачисление недостижимо.

R4: Приоритет отзыва согласия
Scenarios:
- WHEN приходит отзыв (от плательщика/СБП), THEN система атомарно фиксирует REVOKED и событие; WHEN попытка не подтверждена ОПКЦ на момент отзыва, THEN она блокируется и не исполняется.
- WHEN отзыв приходит после подтверждения ОПКЦ, THEN зачисление доводится до конца и инициируется возврат; вебхук consent.revoked + refund.
- WHEN плательщик отозвал согласие, THEN ни одна новая попытка по нему не создаётся (в течение лага ≤ заданного NFR).

R5: Идемпотентность попытки списания
Scenarios:
- WHEN планировщик повторно запускает ту же попытку (тот же consentId/billingPeriod/attemptSeq), THEN возникает ровно одно списание и одно зачисление; THEN повторный POST с тем же Idempotency-Key возвращает существующую попытку (CHARGE_ALREADY_EXISTS/200).

R6: Планировщик и повторные попытки
Scenarios:
- WHEN наступает срок списания по ACTIVE согласию, THEN планировщик инициирует попытку в пределах NFR старта.
- WHEN попытка неуспешна по транзиентной причине, THEN ретрай с экспоненциальной задержкой и джиттером; WHEN исчерпаны попытки, THEN событие charge.failed и DLQ/отчёт незавершённых операций (без потери).

R7: Нотификации ТСП
Scenarios:
- WHEN происходят события consent.activated/revoked/expired и charge.completed/failed, THEN система доставляет вебхук at-least-once с X-SBP-Event-Id и HMAC; WHEN ТСП повторно получает событие, THEN дедупликация по eventId.

R8: Измеримые NFR рекуррентных списаний
Список метрик с числами в тексте. Scenarios verifying burst, revocation latency, availability/RPO, zero unauthorized/duplicate.

R9: Аудит, ПДн и сверка
Scenarios: audit log 100%; ПДн minimized; daily reconciliation 0 discrepancy.

R10: Обратная совместимость контракта
Scenarios: WHEN существующий потребитель вызывает /v1/payments как раньше, THEN ответы не изменены; contract-diff не находит ломающих изменений.

That's 10. Good.

The OpenSpec spec validator requires `## Purpose` first for new capability (50+ chars). Then `## ADDED Requirements`.

Let me write it. Use WHEN/THEN capitalized as in template: `- **WHEN** ...` `- **THEN** ...`.

Note: requirement text must use SHALL. I'll write Russian text with SHALL embedded.

Careful: `#### Scenario:` exactly 4 hashtags.

Let me write.
Now the delta spec (OpenSpec requirements for the new capability):

  `write_file(content="# Design\n\n## Context\n\nПринятое решение (ADR-001..007, `ARCHITECTURE-SPINE.md` AD-001..AD-008) обслуживает **разовый** C2B-приём: платёж, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/openspec/changes/add-sbp-recurring-payment)`

Now design.md. This is the "how" doc, and the main home for: impact on accepted architecture, alternatives summary, NFR table, contract delta, migration/rollback, open questions, what remains for human architect.

Sections per template: Context, Goals/Non-Goals, Decisions, Risks/Trade-offs, Migration Plan, Open Questions. I'll add "Impact on the accepted architecture" (within Context or as Decisions), "NFR budgets" table, "Acceptance criteria", "Rollback", "A3 items".

Let me write comprehensively but structured. Structural headings: template uses English headings; I'll keep English headings (## Context, ## Goals / Non-Goals, ## Decisions, ## Risks / Trade-offs, ## Migration Plan, ## Open Questions) and add explicit subsections in English: `### Impact on the accepted architecture (spine)`, `### Contract delta (openapi/tsp-api.yaml)`, `### NFR budgets (measurable)`, `### Acceptance criteria (A4)`, `### Rollback`, `### Decisions reserved for the human architect (A3)`.

Let me write.

Content details:

Context: current state (ADR-001..007, v0.1 API), see proposal. Constraints: Critical route, spine parent read-only, external NSPK protocol unknown, hybrid vendor boundary.

Goals: recurring debits via consent; reuse machine; no unauthorized/duplicate; measurable; backward compatible.
Non-Goals: карты; C2C; dunning/collection legal; disputes; изменение AD-001..008; multivalutность; UI/личный кабинет плательщика (делает банк плательщика).

Decisions (referencing ADR-008/009): table of decision → ADR. Then:
- D-1 consent as mirror of NSPK registry (ADR-008)
- D-2 charge = payment with consentId, reuse machine (ADR-008)
- D-3 precondition & limits in one transaction (AD-009)
- D-4 revocation priority (AD-010)
- D-5 deterministic attempt key (AD-011)
- D-6 in-core scheduler over outbox (ADR-008 item 6)
- D-7 transport scope (ADR-009, A3)

Impact on accepted architecture: table AD-001..AD-008 → impact → verdict (unchanged/extended/...). This directly answers deliverable #2.

Contract delta: list additions; note field/version; non-breaking rationale; what is NOT changed.

NFR budgets: table with metric/target/method/why.

Acceptance criteria: list, incl negative; map to spec scenarios.

Risks/Trade-offs: [Risk] → Mitigation format:
- [NSPK protocol unknown] → contract-first, ТРЕБУЕТ ПРОВЕРКИ, pilot on test contour
- [revocation race] → AD-010 semantics, compensation, tests, runbook
- [period-boundary burst] → queue load leveling, per-TSP fairness, capacity reserve, pre-warm
- [ПДн/consent legal] → minimization, legal review, audit
- [vendor scope/schedule] → ADR-009 A3, fallback B
- [consent stored externally, rollback] → costly reversibility, feature flag + honor existing
- [dunning harming payer] → policy limits, regulator/legal review (A3)
- [new entity drift from NSPK] → reconciliation daily

Migration Plan: phases: A3 → contract first (NSPK docs + vendor) → walking skeleton on mocks → pilot with 1-2 ТСП → ramp by feature flag. Data migration: none (new entities); backward compatible API (no consumer migration). Rollback: before prod = disable; after = stop-new consents + honor existing + revoke per agreement; signals; decision owner.

Open Questions: deferrable.
- retention period for consents (legal) — actually that changes spec? no, deferrable config.
- whether to expose off-cycle charge to ТСП (business) — affects spec? It's already in contract; ok deferrable.
- exact NSPK limits/periods — external.
- UI for consent handoff (product).

Decisions reserved for human architect (A3): ADR-009 transport scope; dunning policy numbers; revocation semantics legal confirmation; limits model; pilot ТСП scope; retention; spine block ratification (AD-009..011); whether subscriptions become separate initiative.

Let me write it.
Now the design document — the core of the package (impact, decisions, NFR, acceptance, rollback, A3 items):

  `write_file(content="# Tasks\n\n> Предусловие: задачи групп 2–11 начинаются только после A3 (ратификация AD-008/ADR-009 и спайн-блоков AD-009..AD-011) и получен, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/openspec/changes/add-sbp-recurring-payment)`

Now tasks.md. Grouped, each task has verification in description, tests per group (not all at end). Also must reflect A3 gating and contract-first.

Groups:
1. Решения и контракт-первый (A3, NSPK docs, RFP extend, internal adapter contract) — no code tests, but deliverables verification.
2. Модель согласия (ядро): entity, lifecycle, atomic transitions, audit, tests per group.
3. Предусловие списания и лимиты (AD-009) + tests.
4. Идемпотентность попытки (AD-011) + tests.
5. Исполнение списаний: планировщик, ретраи, outbox integration; tests.
6. Отзыв согласия и компенсация (AD-010); tests.
7. API ТСП: endpoints per contract v0.2.0; contract tests.
8. Нотификации ТСП: new events, dedup; tests.
9. Сверка и наблюдаемость: reconciliation, metrics, alerts; tests.
10. NFR/нагрузка/безопасность: load test burst, revocation latency, audit/ПДн checks.
11. Интеграция: end-to-end walking skeleton + gate; handoff rehearsal.

Each group includes its own tests and docs. Final group = integration checks only.

Let me write ~11 groups with 3-5 tasks each, verification in each.

Keep tasks small. Use `- [ ] X.Y description + verify: ...`.

Let me write.
Now the task list for implementers:

  `write_file(content="# Дельта: add-sbp-recurring-payments\n- Route: Critical (полный Solutioning; score 10/15 — дельтой-спеки покрыть нельзя)\n- Created: 2026-0, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/changes/add-sbp-recurring-payments/DELTA.m)`

Now the arch-be DELTA.md. Fill the scaffold. Must mention ARCHITECTURE-SPINE.md. Route: Critical. Include ADDED/MODIFIED/REMOVED/План отката/Критерии приёмки.

I already read the scaffold. Use write_file.

Note: the template header says "- Route: Fast|Standard (Critical — полный Solutioning, дельты недостаточно)". I'll set "- Route: Critical (полный Solutioning; score 10/15)".

Let me write.

Also I should ensure the delta validator passes — `arch-be delta validate add-sbp-recurring-payments`. Let me check its requirements after writing.
Now the arch-be delta record (this is what legally covers the protected spine edit):

  `write_file(content="# Архитектурный контекст (epic-context): рекуррентные C2B-списания СБП\n\nСобран: 2026-09-28. Источники: `ARCHITECTURE-SPINE.md` (AD-001..A, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff-recurring/ARCHITECTURE.md")`

Now the handoff package. Let me create `.arch-handoff-recurring/` with:
- TASK.md
- ARCHITECTURE.md (epic-context 800–1500 tokens)
- CONSTRAINTS.yaml
- RUBRIC.yaml (copy of .arch-handoff/RUBRIC.yaml)
- MANIFEST.json
- adr/ADR-008..., ADR-009...

Let me think about CONSTRAINTS.yaml rules that pass now (static) and add behavioral stubs marked as to-be-added at code stage. The existing style:

```yaml
rules:
  - name: adr-set-complete
    type: file_exists
    path: docs/adr/ADR-001-outbox.md
    severity: error
  ...
```

I'll create rules for the delta:
- file_exists: docs/adr/ADR-008... and ADR-009..., specs delta
- must_contain ARCHITECTURE-SPINE.md 'AD-009', 'AD-010', 'AD-011'
- must_contain openapi/tsp-api.yaml '/v1/consents'
- must_contain spec.md 'CONSENT_LIMIT_EXCEEDED'? Hmm.
- must_not_contain ARCHITECTURE-SPINE.md 'TODO|TBD|XXX' (warn)
- must_contain docs/adr/ADR-008 'приоритет' ... maybe overkill.
- Absence of placeholders in new ADRs: must_not_contain docs/adr/ADR-008*.md '<!--'

Careful with glob patterns in the existing schema: they use `glob: "docs/adr/*.md"` and `pattern`. So must_contain supports glob. For file_exists path. OK.

I should keep the rules meaningful and passing. Let me verify by running `arch-be control check` with `--constraints` pointing to the new file? `control check --help` — let me check options. It has `--constraints`? The gate has `--constraints`. control check probably too. Let me just write and test with gate --constraints.

Behavioral rules to add later (as comments or a separate section)? The schema probably doesn't have a "notes" field; unknown keys may break parsing. I'll list intended behavioral rules in RUBRIC/TASK instead, and keep CONSTRAINTS static-only. Actually the fitness-function-catalog skill mentions `command_succeeds` rules. For the code stage, the handoff CONSTRAINTS should include `command_succeeds` for tests, but tests don't exist yet → they'd fail. Since this package is handed over *after* A3, and the implementer will add tests, I can include `command_succeeds` rules with severity `warn`? They'd still run and warn. Hmm. The gate `--no-exec` skips command_succeeds. I'll include a couple of `command_succeeds` rules with severity error for the key tests, and note in TASK that they unblock as tests land. But if gate runs now it fails → but this package won't be the default gate (default is .arch-handoff/CONSTRAINTS.yaml). It's fine: the package is a spec of intended controls.

Hmm, but the instruction "правило без проверки — антипаттерн". Static rules are checks. Behavioral rules with command_succeeds referencing tests that WILL exist is fine and matches the catalog. I'll include:
- name: no-double-debit-test / command_succeeds: "cargo test ..." — but I don't know the stack (chosen by team). So command_succeeds can't be concrete. Better: keep it as intended rules documented in TASK, and provide static rules now. The catalog says `arch-be rules template` can generate templates — I could run `arch-be rules template`. But stack unknown. I'll do static rules + a documented list of behavioral rules to add once the stack is chosen. That's honest and doesn't create failing/unverifiable commands.

Let me check `arch-be rules template` quickly? Not necessary. Let me keep it pragmatic.

RUBRIC.yaml: copy existing. I need to read it (already read full content earlier). I'll copy verbatim.

MANIFEST.json: like existing but for this task, with a note about the separate directory.

Let me also include a README.md in the package explaining: this is the delta handoff; at apply time merge into `.arch-handoff/` (or regenerate with `arch-be handoff --repo . --task ... qwen-code --route critical`), and that the default gate reads `.arch-handoff/CONSTRAINTS.yaml`. Good.

Now, TASK.md: task formulation + result contract JSON.

ARCHITECTURE.md: epic-context 800–1500 tokens. Include:
- Цель (1 абзац)
- Границы (что делаем/не делаем)
- Стыки (ТСП API, адаптер ОПКЦ, АБС, СБП реестр согласий)
- Инварианты дословно (Rule) for AD-001, AD-002, AD-003, AD-005, AD-009, AD-010, AD-011 (Rule only, verbatim)
- Запреты (не менять AD-001..008, не начинать транспорт до контракта, не переопределять родительский spine, не менять существующие поля контракта)
- Критерии приёмки (кратко, с ссылкой)
- План отката
- Конфликт → стоп.

Let me write concise. Aim ~1000-1300 tokens. I'll count roughly by chars/4.

Let me write files.

For adr/ copies, I'll copy the two ADR files into the package with `cp`. That's a shell command (file operation) but copying is fine via shell; or read+write. Simpler: use shell cp. But guidance prefers dedicated tools for file ops... copying is not covered by a dedicated tool. I'll use cp via shell.

Let me write ARCHITECTURE.md, TASK.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, README.md, then cp ADRs.

Let me draft ARCHITECTURE.md carefully.

---

# Архитектурный контекст (epic-context): рекуррентные C2B-списания СБП

Собран: 2026-09-28. Источники: ARCHITECTURE-SPINE.md (AD-001..AD-011), docs/adr/ADR-008, ADR-009, openapi/tsp-api.yaml 0.2.0, openspec/changes/add-sbp-recurring-payments (proposal/design/spec/tasks).

## Цель

Добавить в платёжный шлюз СБП рекуррентные C2B-списания по согласию плательщика: ТСП регистрирует согласие, плательщик подтверждает его в своём банке, шлюз периодически инициирует списания без участия плательщика, в пределах лимитов согласия; отзыв согласия прекращает будущие списания. Приоритет — доказать архитектуру сквозным сценарием (согласие → списание → зачисление → отзыв → компенсация), а не полнотой продукта.

## Границы

В scope: согласие (жизненный цикл, зеркало реестра СБП), списание как платёж с `consentId`, планировщик и повторы, отзыв и компенсация, нотификации ТСП, сверка, NFR. Вне scope: карты, C2C, выплаты, диспуты, юридическое взыскание, UI плательщика.

## Стыки

- ТСП ↔ шлюз: REST/JSON `/v1/consents*` (openapi/tsp-api.yaml 0.2.0), mTLS, `Idempotency-Key` на POST.
- Ядро ↔ адаптер ОПКЦ: внутренний контракт `docs/contracts/opkc-adapter.md`, новые операции `registerConsent/getConsentStatus/cancelConsent/createDebit/getDebitStatus`, события `consent.*/debit.*`; протокол НСПК знает только адаптер.
- Ядро ↔ АБС: зачисление по подтверждённому статусу (`PAID`), идемпотентно по внешнему ключу = ключ попытки; возвраты — сага.
- Шлюз ↔ реестр согласий СБП: состояние согласия — зеркало; сверка ежедневная.

## Инварианты (Rule дословно)

AD-001: ...
etc.

## Запреты

...

## Критерии приёмки

...

## План отката

...

## Контракт результата

JSON...

---

Let me write it.

Actually the invariant rules are long; including 7 verbatim rules will inflate tokens beyond 1500. Let me include the most binding: AD-001 (short), AD-002, AD-003, AD-005, AD-009, AD-010, AD-011. AD-002/003/005 rules are one sentence each. Should be OK, maybe ~1200 tokens. Let me be judicious: include Rule for AD-002, AD-003, AD-005 (existing, binding), AD-009, AD-010, AD-011 (new), and summarize AD-001/004/006/007 in one line ("действуют без изменений"). That keeps budget.

Let me write.
Now the handoff package for implementers (kept in a separate directory so the already-accepted `.arch-handoff/` is not clobbered).

  `write_file(content="# Задача для кодового харнесса\n\nРеализовать **рекуррентные C2B-списания по согласию плательщика (подписки СБП)** поверх принятого решения, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff-recurring/TASK.md")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff-recurring/TASK.md", old_string="Технологический стек — по выбору команды, но с обоснованием в ADR. Приоритет — доказать архитектуру сквозным сценарием (включая гонку «спис, new_string="Технологический стек — по выбору команды, но с обоснованием в ADR. Приоритет — доказать архитектуру сквозным сценарием (включая гонку «спис)`

Oops — I wrote "`DECRIPTION`" typo in TASK.md: "Критерии приёмки — `design.md` § Acceptance criteria и `DECRIPTION`." That's a mistake; I meant something else. Let me fix that line. I'll edit it to reference DELTA.md acceptance criteria. Also I wrote "`DECRIPTION`" which doesn't exist. Fix.

Let me edit TASK.md.

  `write_file(content="# Fitness-правила для `arch control check` / `arch gate` (схема control::check).\n# Пакет дельты: рекуррентные C2B-списания СБП (Critical)., file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff-recurring/CONSTRAINTS.yaml")`

Now CONSTRAINTS.yaml for the package. Let me write rules following the existing schema (control::check). I'll verify with `arch-be control check --constraints`.

Let me check `control check --help` for the flag name.

Actually, let me just write and then test with `arch-be gate --constraints .arch-handoff-recurring/CONSTRAINTS.yaml`. Wait, gate applies to repo+diff. control check is simpler. Let me check help quickly along with writing.

Rules:
```yaml
rules:
  - name: adr-008-present
    type: file_exists
    path: docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-soglasie-platelschika-kak-preduslovie-i-model-ispolneniya-spisaniy.md
    severity: error
  - name: adr-009-present
    type: file_exists
    path: docs/adr/ADR-009-transport-podpisok-sbp-oblast-vendorskogo-adaptera-opkc.md
    severity: error
  - name: spec-delta-present
    type: file_exists
    path: openspec/changes/add-sbp-recurring-payments/specs/sbp-recurring-payments/spec.md
    severity: error
  - name: spine-consent-invariants
    type: must_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'AD-009'
    severity: error
  - name: spine-revocation-invariant
    type: must_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'AD-010'
    severity: error
  - name: spine-charge-idempotency-invariant
    type: must_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'AD-011'
    severity: error
  - name: contract-consents-path
    type: must_contain
    glob: "openapi/tsp-api.yaml"
    pattern: '/v1/consents'
    severity: error
  - name: contract-version-bumped
    type: must_contain
    glob: "openapi/tsp-api.yaml"
    pattern: 'version: 0.2.0'
    severity: error
  - name: adr-008-no-placeholders
    type: must_not_contain
    glob: "docs/adr/ADR-008-*.md"
    pattern: '<!--'
    severity: error
  - name: adr-009-no-placeholders
    type: must_not_contain
    glob: "docs/adr/ADR-009-*.md"
    pattern: '<!--'
    severity: error
  - name: spine-lints-clean
    type: must_not_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'TODO|TBD|XXX'
    severity: warn
```

Hmm the previous pattern used `<!--` — likely fine. Also should I include behavioral rules? Add as comments a section listing behavioral rules to add at code stage. Comments in YAML are fine (ignored by parser). Good.

Let me include a commented block:

```yaml
# Поведенческие правила (добавить на кодовом этапе, после выбора стека; шаблоны — arch-be rules template):
#  - AD-009: попытка списания при REVOKED/EXPIRED/превышении лимита не создаёт записи и не вызывает адаптеры
#  - AD-010: отзыв до подтверждения ОПКЦ блокирует попытку; после подтверждения — компенсирующий возврат
#  - AD-011: повтор попытки/нотификации → ровно одно списание и одно зачисление
#  - AD-005: зачисление недостижимо вне PAID
#  - контракт: arch-be contract-diff v0.1.0 → v0.2.0 без ломающих
```

Now RUBRIC.yaml — copy existing content. I have it. Write.

MANIFEST.json — write.

README.md — write.

Let me write all four.

  `write_file(content="# Рубрика качества handoff-пакета кодовому агенту (BMAD epic-context + headless-контракт,\n# docs/SOURCE_BRIEF.md §A.3): пакет должен позво, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff-recurring/RUBRIC.yaml")`

Now RUBRIC.yaml — copy the existing content verbatim.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && mkdir -p .arch-handoff-recurring/adr, description="Copy ADRs into handoff package and measure context size")`

Now MANIFEST.json and README.md in the package, then copy ADRs.

MANIFEST.json:
```json
{
  "created_at": "2026-09-28T...",
  "change": "add-sbp-recurring-payments",
  "route": "critical",
  "task": "Реализовать рекуррентные C2B-списания по согласию плательщика (подписки СБП) ...",
  "sources": [...],
  "harness": "qwen-code",
  "package_dir": ".arch-handoff-recurring",
  "note": "Отдельный каталог, чтобы не перезаписать принятый пакет .arch-handoff/ (walking skeleton разового C2B-приёма). При apply дельты: слить правила в .arch-handoff/CONSTRAINTS.yaml или перегенерировать пакет командой `arch-be handoff --repo . --task ... --route critical qwen-code`.",
  "epic_context_chars": ...,
  "epic_context_tokens": ...
}
```

Let me compute chars/tokens for ARCHITECTURE.md. I'll run wc -c after. For now put approximate; better to compute then write. Let me write README + copy ADRs, compute chars, then write MANIFEST with real numbers.

Let me do: cp ADRs; wc -c ARCHITECTURE.md.

Actually I can write MANIFEST and then correct. Let me first do shell: mkdir adr, cp, wc.

Note: `.arch-handoff-recurring` dir already created by write_file. Need `adr/` subdir.

Let me run shell.

  `write_file(content="# Архитектурный контекст (epic-context): рекуррентные C2B-списания СБП\n\nСобран: 2026-09-28. Источники: `ARCHITECTURE-SPINE.md` (AD-001..A, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff-recurring/ARCHITECTURE.md")`

ARCHITECTURE.md = 7727 bytes. Russian text in UTF-8: Cyrillic is 2 bytes/char, and tokens roughly ~2-4 chars per token for Cyrillic. 7727 bytes ≈ ~3900 Cyrillic chars ≈ maybe 1200-1800 tokens. That's near/above the 800–1500 budget. The rubric criterion weight 3 wants 800–1500 tokens. Let me estimate: For Russian, ~2.5 tokens per word; ~450 words? 7727 bytes / 2 bytes = ~3860 chars, ~600 words, ~1500-1800 tokens. Slightly over. Hmm.

The existing `.arch-handoff/ARCHITECTURE.md` was 6000 chars (MANIFEST says epic_context_chars: 6000, tokens 1500). So chars 6000 → tokens 1500 (4 chars/token, but that's mixed). My 7727 chars → ~1900 tokens by that ratio. Over budget.

I should trim ARCHITECTURE.md to ~6000 chars to match the repo's own measure (they counted 6000 chars = 1500 tokens). Let me trim: remove some verbosity. Target ≤6200 chars.

What to trim: the "Критерии приёмки" can be shortened (already short). The "Запреты" list. The invariant rules are verbatim — keep. Maybe shorten "Стыки" and "Цели". Actually 7727 → 6200 requires ~1500 chars cut. Let me reconsider: is it worth? The rubric anchors: 5 = "800–1500 токенов". Being ~1900 is a minor overrun but the rubric is applied to handoff quality. Let me trim to be safe.

Actually, the repo's own MANIFEST computed 6000 chars/1500 tokens for its ARCHITECTURE.md; the same measuring tool would report my file as ~1930 tokens. To be within budget, target ~6000 chars.

Let me trim ~1700 chars. Candidates:
- Remove the "Границы" bullet verbosity → keep concise.
- Remove "Действуют без изменений: ..." explanation? Keep short.
- Shorten AD-002/AD-003/AD-005 rules? No, must be verbatim.
- Remove "Контракт результата" section from ARCHITECTURE.md (it's in TASK.md) → saves ~300 chars. But rubric wants it in package, not necessarily in ARCHITECTURE.md. The existing MANIFEST cites epic_context only for ARCHITECTURE.md. I'll remove the JSON contract from ARCHITECTURE.md (keep in TASK.md).
- Shorten "Стыки".
- Shorten "Критерии приёмки".

Let me rewrite ARCHITECTURE.md tighter. I'll aim ~5800-6200 bytes.

Let me rewrite.

New draft (tighter):

# Архитектурный контекст (epic-context): рекуррентные C2B-списания СБП

Собран: 2026-09-28. Источники: `ARCHITECTURE-SPINE.md` (AD-001..AD-011), `docs/adr/ADR-008-*`, `ADR-009-*`, `openapi/tsp-api.yaml` 0.2.0, `openspec/changes/add-sbp-recurring-payments/`.

## Цель

Добавить в шлюз СБП **рекуррентные C2B-списания по согласию плательщика**: ТСП регистрирует согласие, плательщик подтверждает его в своём банке, шлюз периодически инициирует списания без участия плательщика в пределах лимитов; отзыв согласия прекращает будущие списания. Приоритет — доказать архитектуру сквозным сценарием (согласие → списание → зачисление → отзыв → компенсация) на моках.

## Границы

В scope: согласие (жизненный цикл, зеркало реестра СБП), списание как платёж с `consentId`, планировщик и повторы, отзыв и компенсация, нотификации, сверка, NFR. Вне scope: карты, C2C, выплаты, диспуты, взыскание, UI плательщика.

## Стыки

- **ТСП ↔ шлюз**: REST/JSON `/v1/consents*` (`openapi/tsp-api.yaml` 0.2.0), mTLS, `Idempotency-Key` на POST, вебхуки at-least-once (`X-SBP-Event-Id`, HMAC).
- **Ядро ↔ адаптер ОПКЦ**: внутренний контракт `docs/contracts/opkc-adapter.md`; новые операции `registerConsent/getConsentStatus/cancelConsent/createDebit/getDebitStatus`, события `consent.*/debit.*`. Протокол НСПК знает только адаптер.
- **Ядро ↔ АБС**: зачисление только по подтверждённому статусу, идемпотентно по внешнему ключу = ключ попытки; возвраты — сага.
- **Шлюз ↔ реестр согласий СБП**: согласие — зеркало реестра; синхронизация событиями и ежедневной сверкой.

## Инварианты (Rule дословно)

Без изменений действуют AD-001, AD-004, AD-006, AD-007, AD-008. Связывающие правила:

- **AD-002**: «Изменение финансового статуса платежа и запись исходящего события (outbox) выполняются в одной локальной транзакции. Нарушение — дефект блокера (ревью + fitness-тест на каждый переход).»
- **AD-003**: «Повторная доставка любого сообщения не изменяет уже завершённое состояние. Fitness: тест «повторная нотификация/повторный запрос → состояние не меняется, результат идемпотентен».»
- **AD-005**: «Вызов АБС на зачисление возможен только из состояния `PAID` (подтверждённый НСПК статус). Fitness: проверка недостижимости зачисления из `CREATED`/`QR_ISSUED`.»
- **AD-009**: «Инициация любого списания требует локального состояния согласия `ACTIVE` и прохождения проверки лимитов в той же транзакции, что и создание попытки; иначе — отказ без обращения к ОПКЦ и АБС.»
- **AD-010**: «Изменение состояния согласия (включая отзыв/приостановку) и запись события в outbox выполняются в одной локальной транзакции; отзыв запрещает все попытки, не подтверждённые ОПКЦ, и инициирует компенсацию (возврат) для уже подтверждённых; состояние согласия берётся из зеркала реестра СБП, сверяемого с НСПК.»
- **AD-011**: «Ключ попытки детерминирован от `(consentId, billingPeriod, attemptSeq)` и передаётся как `reference` в адаптер ОПКЦ и как внешний ключ в АБС; повторная обработка того же ключа не создаёт второй операции и возвращает существующий результат.»

## Запреты

- Не менять и не переопределять AD-001..AD-008 (родительский spine read-only; конфликт — эскалация).
- Не начинать транспорт подписок до расширения/подписания контракта с вендором и получения документации НСПК (AD-008).
- Не менять существующие пути, обязательные поля и значения перечислений контракта ТСП.
- Не хранить реквизиты счёта и лишние ПДн плательщика; не логировать ПДн в открытом виде.
- Расхождение с ADR/spine — остановка и эскалация (`conflicts_with_prior_decisions`), не молчаливое отклонение.

## Критерии приёмки

Списание невозможно при `REVOKED`/`EXPIRED`/`SUSPENDED`/`PENDING_PAYER` и сверх лимитов (без вызовов ОПКЦ/АБС); гонка «попытка / отзыв» — по AD-010; повтор попытки/нотификации → ровно одно списание и зачисление; контракт 0.2.0 без ломающих изменений; пик 2000 TPS / 5 мин при p95 старта ≤ 5 мин; лаг отзыва p95 ≤ 60 с; аудит 100 %; `arch-be gate --route critical` зелёный. Полностью — `design.md` § Acceptance criteria.

## План отката

До эксплуатации — не включать фиче-флаг. После — остановить новые согласия, обслуживать/отзывать существующие, данные не удалять (RPO=0). Сигналы и владелец — `design.md` § Rollback.

---

That's shorter. Estimated ~6300 bytes. Let me write and measure.

Also I should double check the "AD-005" rule verbatim vs spine: spine says "Вызов АБС на зачисление возможен только из состояния `PAID` (подтверждённый НСПК статус). Fitness: проверка недостижимости зачисления из `CREATED`/`QR_ISSUED`." Yes matches.
AD-002 verbatim: "Изменение финансового статуса платежа и запись исходящего события (outbox) выполняются в одной локальной транзакции. Нарушение — дефект блокера (ревью + fitness-тест на каждый переход)." yes.
AD-003 verbatim: yes.
AD-009/010/011 verbatim from what I wrote: I must match exactly the spine text. My AD-009 in spine: "Инициация любого списания требует локального состояния согласия `ACTIVE` и прохождения проверки лимитов **в той же транзакции**, что и создание попытки; иначе — отказ без обращения к ОПКЦ и АБС. Fitness: попытка списания при `REVOKED`/`EXPIRED`/превышении лимита не создаёт записи о списании и не вызывает адаптеры."
In ARCHITECTURE.md I included bold markers `**в той же транзакции**`. Rubric wants verbatim Rule — keeping the bold is fine (same words). But I omitted the Fitness sentence. Verbatim ideally includes it. Hmm, "дословные Rule" — the Rule field includes the Fitness sentence. To be strictly compliant I should include the whole Rule. That adds length but accuracy matters for the rubric (invariants weight 2, anchor 5 requires "дословные Rule"). Let me include full Rule text for AD-009/010/011 (including Fitness) and for AD-002/003/005.

AD-009 full: "Инициация любого списания требует локального состояния согласия `ACTIVE` и прохождения проверки лимитов **в той же транзакции**, что и создание попытки; иначе — отказ без обращения к ОПКЦ и АБС. Fitness: попытка списания при `REVOKED`/`EXPIRED`/превышении лимита не создаёт записи о списании и не вызывает адаптеры."
AD-010 full: "Изменение состояния согласия (включая отзыв/приостановку) и запись события в outbox выполняются в одной локальной транзакции; отзыв запрещает все попытки, **не подтверждённые ОПКЦ**, и инициирует компенсацию (возврат) для уже подтверждённых; состояние согласия берётся из зеркала реестра СБП, сверяемого с НСПК. Fitness: отзыв, применённый до подтверждения ОПКЦ, делает невозможной любую новую попытку по этому согласию."
AD-011 full: "Ключ попытки детерминирован от `(consentId, billingPeriod, attemptSeq)` и передаётся как `reference` в адаптер ОПКЦ и как внешний ключ в АБС; повторная обработка того же ключа не создаёт второй операции и возвращает существующий результат. Fitness: повтор планировщика/повторная нотификация по одной попытке → ровно одно списание и одно зачисление."

That adds ~600 chars. Total maybe ~6900. Over 6000 target but closer. Hmm.

Trade-off: verbatim invariants (rubric anchor 5) vs token budget (anchor 5 = 800-1500 tokens). The existing repo package was exactly 6000 chars. I could reduce elsewhere: drop "Границы" heading content into one line, drop "План отката" (it's in design/DELTA), drop "Критерии приёмки" details (reference design). But rubric acceptance_criteria requires criteria in the package — TASK.md and the handoff CONSTRAINTS/DELTA include them. The epic_context criterion judges ARCHITECTURE.md completeness ("цель, стыки, ограничения"). Acceptance criteria is a separate criterion that can be satisfied by other files. So I can trim acceptance criteria from ARCHITECTURE.md to one line.

Let me finalize a version ~6500 bytes with full verbatim rules and brief criteria. That's ~1625 tokens by repo's 4 chars/token → slightly over 1500. Acceptable? The rubric says "800–1500 токенов". Being 1600 is a near-miss. 

Alternative: measure tokens more accurately. Russian text tokenization: GPT-family ~1 token per ~2-3 Cyrillic chars? Actually for Russian, ~1 token ≈ 2.5-3 characters (Cyrillic is poorly tokenized). 6500 bytes ≈ 3250 Cyrillic chars → ~1100-1300 tokens. Hmm! That could be within budget. The repo's own ratio (6000 chars → 1500 tokens) used chars, not bytes. If they count chars (6000) → 1500 tokens = 4 chars/token, that's optimistic for Cyrillic; more likely they used a tokenizer: 6000 chars of mixed markdown → 1500 tokens plausible = 4 chars/token.

For my file: if it has 6500 chars (bytes~11k? no). Careful: 7727 bytes of mostly-Cyrillic ≈ 3900 chars. The repo's 6000 chars vs my 3900 chars — my file has FEWER chars than the reference! Wait: existing ARCHITECTURE.md is 6000 chars. Mine is 7727 *bytes*. Since Cyrillic = 2 bytes/char, mine ≈ 3900-5200 chars. That's actually fewer chars than 6000. So by char/token ratio (4 chars/token), mine ≈ 975-1300 tokens. Within budget!

Great — bytes ≠ chars. The MANIFEST's `epic_context_chars: 6000` was chars. My file: let me count chars not bytes: `wc -m`. Let me measure with wc -m. If ~4500 chars → ~1125 tokens. Good.

Let me not over-trim. But including full verbatim Rules adds chars; still likely under 6000 chars. Let me update the rules to be verbatim-complete, keep the rest, and measure with wc -m.

Let me rewrite ARCHITECTURE.md with full rules and slightly trimmed extras, then wc -m.

Let me rewrite.

  `write_file(content="# Handoff-пакет дельты: рекуррентные C2B-списания СБП\n\nЭто пакет передачи **изменения** `add-sbp-recurring-payments` кодовому харнессу, а, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff-recurring/README.md")`

Now write MANIFEST.json and README.md, then measure chars.

Let me write README.md first (package note), then MANIFEST with measured numbers. Let me measure chars first.

Actually I'll write README, measure, then write MANIFEST.

Let me write README.md.

  `edit(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff-recurring/README.md", new_string="- Предусловие старта: A3 (ратификация ADR-008/ADR-009 и AD-009..AD-011) и получение документации НСПК по подпискам.", old_string="- Предусловие старта: A3 (ратification ADR-008/ADR-009 и AD-009..AD-011) и получение документации НСПК по подпискам.")`

Typo: "ратification" — should be "ратификация". Let me fix.

Then measure chars.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && echo \"chars (wc -m):\" && wc -m .ar, description="Measure epic-context size in chars")`
  `write_file(content="{\n  \"created_at\": \"2026-09-28T14:24:00+03:00\",\n  \"change\": \"add-sbp-recurring-payments\",\n  \"route\": \"critical\",\n  \"harness, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff-recurring/MANIFEST.json")`

4591 chars. The reference package was 6000 chars = 1500 tokens (4 chars/token). So 4591 chars ≈ 1150 tokens. Within 800–1500. 

Now MANIFEST.json with epic_context_chars: 4591, epic_context_tokens: ~1150.

Let me write MANIFEST.json.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && echo \"=== openspec validate ===\" &, description="Validate OpenSpec change")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && B=<SPINE_BANK>/target/, description="Lint spine and validate delta")`

Now verify everything:
1. `openspec validate --change add-sbp-recurring-payments --strict`
2. `openspec status`
3. `arch-be control spine ARCHITECTURE-SPINE.md`
4. `arch-be delta validate add-sbp-recurring-payments`
5. `arch-be gate --repo .` (should show delta_guard covering the spine edit)
6. `arch-be contract-diff` old vs new openapi
7. Validate YAML of openapi (parse). openspec/adr parses.
8. Validate JSON of MANIFEST.

Let me run a batch. First openspec validate + status.

Note: openspec validate --strict may complain about the spec delta (needs Purpose ≥50 chars — ok; scenarios 4 hashtags — ok). Let's see.

Also `openspec validate` for the change: `openspec validate add-sbp-recurring-payments --strict` or `--change`. Let me check by running.

Let me run.
Now let me verify all artifacts with the repository's own gates.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && B=<SPINE_BANK>/target/, description="Check contract for breaking changes")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && B=<SPINE_BANK>/target/, description="Run repository gate and package fitness rules")`

All green. Now:
- `arch-be gate --repo .` — should show delta_guard with protected changed covered.
- contract-diff old vs new.
- Validate openapi YAML parse & MANIFEST JSON (python).
- control check with the new package constraints (to make sure rules pass / schema valid).

Let me get the old openapi from git to a temp file, then contract-diff.

`git show HEAD:openapi/tsp-api.yaml > <TMP>.1.0.yaml`. Wait, is openapi/tsp-api.yaml tracked in HEAD? The git status at start showed only .qwen/settings.json modified; openapi/tsp-api.yaml existed at HEAD (committed in baseline). Let me check `git log --oneline -- openapi/tsp-api.yaml` or just `git show HEAD:openapi/tsp-api.yaml`.

Let me run.

Also run gate.

Also control check with constraints: `arch-be control check --repo . --constraints .arch-handoff-recurring/CONSTRAINTS.yaml`? Let me check control check options. Let me just run and see; if flag differs, adjust.

Let me batch.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && B=<SPINE_BANK>/target/, description="Run fitness rules of the new handoff package")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && python3 -c \"\nimport yaml, json\nd , description="Validate YAML/JSON artifacts parse")`

Excellent:
- contract-diff: 0 breaking, 4 non-breaking (new paths) → PASS. 
- gate: PASS, delta_guard covers ARCHITECTURE-SPINE.md ← 'add-sbp-recurring-payments'. 

Note gate route auto: score 1 (api_contract_change) — because only diff-derived triggers; our declared triggers aren't passed. That's fine; the declared score is documented. But the gate route auto = Fast, which means NFR/evidence sections skipped. Should I run gate with `--route critical` to exercise the full Critical gate? The prompt's design expects Critical. Let me try `gate --route critical` to see if it demands NFR/evidence and fails (which would be a finding for the human: evidence bundle not yet built). It might fail due to missing evidence bundle — that's expected at this stage and honest. Let me check what it says, and report it. Actually the significance-routing/evidence gate for Critical requires quantitative NFR and evidence bundles. Since we're at propose stage (not A4), the Critical gate would legitimately be red. That's useful info: "Critical route gate requires evidence bundle, not yet present — expected until A4". Let me run it to know.

- control check usage: `control check <REPO>` positional, with `--constraints`. Let me run `control check . --constraints .arch-handoff-recurring/CONSTRAINTS.yaml`.

Let me run both.

Also validate openapi YAML and MANIFEST JSON.

Let me batch:
1. control check . --constraints ...
2. gate --route critical
3. python yaml.safe_load openapi + json.load manifest + json.load settings? (settings untouched besides pre-existing modification)

Let me run.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && B=<SPINE_BANK>/target/, description="Run full Critical-route gate")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && B=<SPINE_BANK>/target/, description="List rubrics and adr tooling")`

All green. Now let me run the Critical-route gate to see what it demands (NFR/evidence), for honest reporting.

`arch-be gate --repo . --route critical`.

Also let me run `arch-be review --repo .` maybe (composite). And `control rules-report` maybe. Let me at least run gate critical.

Let me also check the ADR registry parsing: `arch-be control adr registry`? The skill mentions `arch-be adr registry`. Let me check if there's such a command — top-level had control adr (new). Maybe `arch-be control adr` only has new. The skill mentioned `arch-be adr registry`. Let me check `$B adr --help`. Not critical.

Let me run gate critical + maybe rubric list to see if adr_quality available (optional). Focus: gate critical.

Also, should I run the `rubric` evaluation on my ADRs? The skill spine-adr-judge / rubric-judging suggests evaluating. That's a "nice to have" verifications. The task didn't explicitly ask to self-evaluate. But the adr-authoring checklist says "Оценка по рубрике adr_quality ≥ 3.5 (rubric_evaluate)". No API key needed if split-judge (I judge myself k times + rubric_verify). That's heavy. Given the deliverable is the package, and I've verified mechanically, I could optionally run a rubric. Let me check if `arch-be rubric list` has adr_quality and whether `rubric run` works offline. Time/context budget: I've done a lot. Let me do a quick check: `rubric list`.

Actually, let me be pragmatic: run gate critical; then optionally run the review command which is a composite gate. Then finalize.

Let me run gate critical and rubric list.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && echo \"=== git status --short ===\";, description="Review working-tree changes")`

Critical gate FAILs on one sensor unrelated to my artifacts: `./docs/spec/state-machine.md` required_sections missing ## Проблема, ## Критерии приёмки, ## Риски. That's a pre-existing accepted file (state-machine.md) which the sensors expect to have those sections. Interesting: the sensor scans docs/spec/state-machine.md. Was it failing before my change? Let me check: the earlier gate auto(Fast) didn't run sensors (sensors only on Standard/Critical). So this is a pre-existing structural gap surfaced by the Critical route — not caused by me. 

Hmm, but wait: should I fix it? The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." docs/spec/state-machine.md is an accepted artifact. Adding "## Проблема", "## Критерии приёмки", "## Риски" sections to it... The sensor `required_sections` expects those sections in spec files. This is a mechanical requirement of the harness for specs. Since our change touches the state machine (consent-based charge path), and the Critical gate is the required gate for this change, we arguably must bring the spec file to the required shape. But that's editing accepted truth...

Options:
1. Leave it and report: Critical gate has 1 pre-existing sensor failure in docs/spec/state-machine.md; unrelated to the delta; recommend fixing at archive/sync or as separate housekeeping. Also note Critical gate SKIPs nfr/evidence/model because there's no model/ dir and no EVIDENCE.yaml — mandatory for Critical, so the route isn't fully green yet by design (evidence lands at A4).
2. Fix state-machine.md by adding the required sections. But that would be modifying an accepted spec file outside the OpenSpec cycle. However — is state-machine.md actually a "spec" the sensor targets? It's at docs/spec/state-machine.md. The sensor expects spec-like sections. Given the change does extend the state machine (charge path), updating it might be legitimate... but per the repo's OpenSpec cycle, truth files update at archive.

Hmm. Which is more correct? The task explicitly says accepted decision files change only the accepted way. The accepted way for docs/ truth is OpenSpec archive/sync (per delta-spec skill: "archive: дельта вливается в живой источник истины (спека системы обновляется)"). We're at propose stage, so we should NOT edit state-machine.md now. The sensor failure is a pre-existing structural debt (the file lacked those sections all along) surfaced because we now run Critical. I should report it as a finding/next step, not silently patch accepted truth.

But wait — would a reviewer expect me to leave a red gate? The task says "когда закончишь...". The deliverable is the architectural package "чтобы его можно было вынести на архитектурное решение". At propose stage, the Critical gate legitimately isn't fully green (no evidence bundle, no model/, sensors gap). I should report precisely:
- PASS: fitness, delta_guard (spine edit covered), rule_weakened, spine_lint, contract-diff (0 breaking), openspec validate, delta validate, package fitness.
- FAIL/SKIP on Critical route: sensors (pre-existing gap in docs/spec/state-machine.md — missing ## Проблема/## Критерии приёмки/## Риски), plus SKIPs nfr/model_validate/evidence_verify because model/ and EVIDENCE.yaml don't exist yet (mandatory for Critical — to be produced at A2/A4).

Hmm, actually maybe I should consider whether the sensor failure IS in scope: the change modifies the state machine behavior, and the repo's sensor wants each spec to include those sections. If I'm delivering a package that modifies the state machine, then updating the state-machine spec to the required shape could be considered part of the delta — but only via the delta mechanism. Since we're not archiving, we shouldn't.

Let me check whether state-machine.md previously passed. Run gate --route critical on HEAD (stash-free): I can run gate against HEAD by... the gate reads working tree. The sensors component reads docs/spec/state-machine.md from the working tree, which I didn't modify. So this failure exists at HEAD too. Let me verify by running the sensor on a pristine checkout? Simpler: `git stash` is risky. I can check `git diff --stat docs/spec/state-machine.md` = empty (I didn't touch it). So yes, pre-existing.

Let me confirm git status to show I didn't modify it, and enumerate changed files.

Also note: gate says "изменённых файлов: 19" — includes openspec/, changes/, docs/adr, openapi, ARCHITECTURE-SPINE, .arch-handoff-recurring. Wait 19 seems high; untracked files count too. Fine.

Now, one more consideration: the `sensors` failure names `./docs/spec/state-machine.md` and required sections ## Проблема, ## Критерии приёмки, ## Риски. Are these required for ALL md under docs/spec? Possibly it's the "spec" artifact pattern. Hmm. If the harness convention is that spec files carry Problem/Acceptance/Risks sections, then the accepted state-machine.md violates it, and our delta could legitimately add those sections as part of the modified requirement... but again, archive-time.

Decision: report as pre-existing finding; do not edit accepted truth. Offer the fix as a next step. This is honest and respects the instruction.

Hmm, but hold on. Let me reconsider: maybe I should add the new state-machine delta into the spec delta (I did mention charge lifecycle in requirements, but not the state machine transitions table). The task deliverable #3/#4 might expect the status-machine changes. I expressed: charge = existing machine with consentId, QR_ISSUED replaced by initiation; refunds via existing saga. That's in ADR-008 and design.md. The spec delta has requirements. I think that's covered.

Now let me also double check: did I accidentally leave `.qwen/settings.json` modified? That was pre-existing (M at start). I didn't touch it. Good.

Let me run `git status --short` to list all changes, and verify state-machine.md/tests untouched. Also confirm openapi/settings.

Let me also verify ADR files parse in the ADR registry if available. `arch-be control adr` only creates. The skill mentioned `arch-be adr registry` — maybe not in this build. Skip.

Let me run git status and a final file listing. Also `openspec list` to show the change.

Then I'll write the final summary. Also consider saving memory? The instructions say memory is for durable cross-conversation knowledge. Nothing the user explicitly asked to remember. I could save a project memory about... hmm, "Do not save" excludes project structure/conventions. I'll skip memory (nothing durable beyond repo content). Actually one could argue the accepted repo convention (spine edited only via `changes/<name>/DELTA.md` covered by delta guard) is a durable, non-obvious project convention not derivable from code quickly... but it IS derivable from the repo (delta.rs docs, .arch-handoff). The exclusion says don't save project structure/conventions. Skip. Also don't save git history. Skip memory.

Let me run final checks: git status, and confirm no accidental modifications to accepted docs (docs/nfr.md, docs/solutioning.md, docs/contracts/*, README.md).

Let me run git status --short and git diff --stat.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && python3 -c \"\nimport re\nspine = op, description="Verify spine Rules are verbatim in epic-context")`

Good:
- .qwen/settings.json was modified before I started (git snapshot showed M .qwen/settings.json at conversation start). I didn't touch it. Its diff is 3 lines (probably spine MCP added). Pre-existing.
- ARCHITECTURE-SPINE.md +23 lines (new blocks).
- openapi/tsp-api.yaml +267 (additive).
- New: .arch-handoff-recurring/, changes/, two ADRs, openspec change.
- Accepted truth (nfr, solutioning, contracts, spec, README) untouched. 

Note: docs/adr/ADR-008/009 are now "modified" relative to? They're untracked (?? ) — because the scaffold creation made new files, and HEAD has no such files. Fine.

Now, the Critical gate sensor failure is pre-existing (docs/spec/state-machine.md untouched). Let me verbatim confirm it's pre-existing by checking the file lacks those sections (quick grep). Actually the sensor output already tells us. And git status shows it's not modified → pre-existing.

Let me quickly verify the sensor failure is reproducible at HEAD by running the sensor? There's `arch-be control sensors`. Let me run `control sensors --help` and then run it to confirm the finding and its scope. Actually the gate output already names it. To be thorough and honest, let me confirm the doc lacks those sections: grep for "## Проблема" in docs/spec/state-machine.md.

Let me run: `grep -c "## Проблема" docs/spec/state-machine.md` etc. Using grep_search tool would be proper. Quick shell grep is discouraged; use grep_search.

Let me use grep_search for "## Проблема" in docs/spec.

Actually simpler: the sensor said missing. Trust it.

Now let me consider whether to also produce an evidence-bundle stub? No — that's A4, out of scope (task says prepare package for architectural decision and handoff; not A4 evidence). I'll note it as a Critical-route requirement.

One more check: the openspec `specs/sbp-recurring-payments/spec.md` — validate passed strict. Good.

Also should I verify the handoff ARCHITECTURE.md AD-009/010/011 rules are byte-identical to spine Rules? Let me do a quick programmatic check to be safe (rubric judges verbatim). I'll extract Rule lines from spine and check each substring appears in ARCHITECTURE.md. Let me run a python check.

Let me do that verification — it strengthens the claim.

Also verify openapi has no breaking: done.

Let me run the verbatim check.

  `write_file(content="# Архитектурный контекст (epic-context): рекуррентные C2B-списания СБП\n\nСобран: 2026-09-28 из `ARCHITECTURE-SPINE.md`, `docs/adr/ADR-008-, file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff-recurring/ARCHITECTURE.md")`

The verification shows Rules 2,3,5,9,10,11 (the binding ones for this change) are present verbatim. Rules 1,4,6,7,8 (AD-001, AD-004, AD-006, AD-007, AD-008) are NOT included verbatim — but my ARCHITECTURE.md says "Без изменений действуют AD-001, AD-004, AD-006, AD-007, AD-008" without quoting their Rules.

The rubric criterion `invariants` anchor 5: "Все связывающие AD присутствуют с дословными Rule". Are AD-001, AD-004, AD-006, AD-007, AD-008 "связывающие" for this change? 
- AD-001 (isolation) — yes, binds new components.
- AD-004 (single OPKC adapter) — yes, binds transport for subscriptions.
- AD-006 (trust zones) — yes, binds where consent processing lives.
- AD-007 (compliance) — yes, binds audit/PII.
- AD-008 (hybrid, ADOPTED) — yes, binds transport implementation timing.

So for a perfect rubric score, I should include their Rules verbatim too. That will grow the file. Current 4591 chars; adding 5 rules (~1500 chars) → ~6100 chars ≈ 1525 tokens (by 4 chars/token) — right at the top of the 800–1500 budget. Slightly over. Hmm.

Trade-off between two rubric criteria (both weight 2 and 3): epic_context wants ≤1500 tokens; invariants wants all binding AD verbatim. The existing repo package (6000 chars) apparently didn't include all AD Rules either? Let me check: the existing .arch-handoff/ARCHITECTURE.md I read earlier — it contained ADR texts truncated, not spine Rules verbatim. So the repo's own package likely scores 3 on invariants. 

Better approach: include the binding Rules compactly. I can shorten by removing the "Источники" line and trimming other prose to fit. Let me add the 5 Rules but compress:
- AD-001 Rule: "Любое взаимодействие с АБС и ОПКЦ СБП — только через адаптеры СБП-шлюза (проверка: сетевые правила и код — единая точка вызова; fitness: отсутствие исходящих вызовов НСПК/АБС вне адаптеров)."
- AD-004 Rule: "Протокол НСПК знает только адаптер ОПКЦ; внутренний контракт шлюза — единственный интерфейс для остальных компонентов."
- AD-006 Rule: "Сеть между зонами — только через межсетевые экраны по белому списку; ключевой материал — в сертифицированном СКЗИ/HSM; доступ операторов — привилегированный контур с 4-eyes для ручных операций."
- AD-007 Rule: "Каждый финансовый переход и административное действие — в неизменяемом аудит-логе; все каналы к ОПКЦ — на сертифицированных СКЗИ. Проверка — ИБ-аудит и fitness."
- AD-008 Rule: "Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК."

Add ~1300 chars. Total ~5900 chars — likely within 1500 tokens (~1475). Let me also trim ~200 chars elsewhere to be safe (e.g., remove "Собран: ... Источники:" long line, shorten Границы). 

Let me rewrite the Инварианты section to include all 11 rules grouped (existing 8 + new 3), and trim the "Стыки"/"Границы" slightly. Then re-measure and re-verify.

Let me restructure: 
"## Инварианты (Rule дословно; AD-001..AD-011)"
- **AD-001** ... 
- ... through AD-011.

That's 11 bullets, all verbatim. Removes the "Без изменений действуют..." line.

Also shorten Запреты (it duplicates invariants a bit). Keep 4 bullets.

Let me rewrite ARCHITECTURE.md fully.

Estimate: 11 rules: AD-001 (~180), AD-002 (~165), AD-003 (~165), AD-004 (~120), AD-005 (~150), AD-006 (~150), AD-007 (~130), AD-008 (~280), AD-009 (~230), AD-010 (~300), AD-011 (~250) = ~2100 chars of rules + headings. Plus цель (~380), границы (~230), стыки (~700), запреты (~450), критерии/откат (~600), header (~150). Total ~5200-5600 chars. Good, under 6000.

Let me write it.
The epic-context should carry **all** binding invariants verbatim. Let me strengthen it with the remaining Rules.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && python3 -c \"\nimport re\nspine = op, description="Re-verify verbatim rules and context size")`

Now re-verify: all rules verbatim, and char count. Also update MANIFEST epic_context_chars if changed.

Let me run the check + wc -m.

Note: the AD-009 Rule in my epic-context uses `**в той же транзакции**` bold; spine has the same bold. The python normalization strips newlines but keeps `**`. Should match. Let's verify.

  `edit(file_path="<HARNESS>/runs-v2/cells/wc2xy6c/ws/.arch-handoff-recurring/MANIFEST.json", new_string="  \"epic_context_chars\": 5496,\n  \"epic_context_tokens\": 1375,", old_string="  \"epic_context_chars\": 4591,\n  \"epic_context_tokens\": 1150,")`

All 11 rules verbatim present; 5496 chars ≈ 1374 tokens (by 4 chars/token) — within 800–1500. 

Update MANIFEST epic_context_chars to 5496 and tokens 1375. Let me edit MANIFEST.

Then final: I want to double-check the `.arch-handoff-recurring/README.md` mentions correct command. Fine.

Also I should reconsider the Critical gate sensor FAIL. Let me check what `sensors` checks and whether docs/spec/state-machine.md is really required to gain those sections. The finding: "./docs/spec/state-machine.md required_sections — нет секций: ## Проблема, ## Критерии приёмки, ## Риски". This is a pre-existing condition. 

Should I fix it? Let me think about "the way accepted in this repo" — the sensors are part of the harness's required convention for spec files. The accepted file violates it. Fixing it would modify accepted truth outside the delta cycle. But: is it "accepted truth"? It's marked "Status: Draft (для ревью на гейте A1)". A1 gate was supposed to pass it... and it's Draft. Adding the required sections is arguably bringing the draft into conformance — a legitimate improvement, and the change does modify the state machine (new charge path) so touching it is within the delta's blast radius. But the instruction is explicit: change accepted decision files only in the accepted way. The state-machine spec is part of the accepted package (referenced by the solutioning). Modifying it directly without a delta covering it would be a "direct edit". The delta guard protects only model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml — not docs/spec. So mechanically allowed, but philosophically the repo's process (OpenSpec/archive) is the way.

I'll NOT modify it, and instead report it clearly as (a) a pre-existing sensor gap unrelated to the change, and (b) a recommended action (either tick the sensor convention or bring the spec into the required shape through the delta at archive). This is the honest, non-invasive choice, and I'll flag it prominently.

Hmm, but a reviewer might say "the gate is red, you didn't finish". Let me weigh: the task explicitly says prepare the package so it *can be taken* to architectural decision and handed to implementers. It does not say "make the Critical gate green". Evidence bundle and model/ are explicitly A2/A4 artifacts, not produceable at propose stage. So a fully-green Critical gate is not achievable (and shouldn't be) now. Reporting is correct.

Actually, wait — maybe I should double-check whether the sensor failure is even in scope of the gate for our change or a global repo condition. The sensors component scans the repo. Since it's global and pre-existing, report it.

Let me also verify by running sensors on HEAD-equivalent: the file is unmodified, so yes.

One more useful verification: `arch-be review --repo .` composite — might produce a nice consolidated verdict. Could be long. Let me skip; gate --route critical already gave the consolidated view.

Let me update MANIFEST and then do a final listing of created/changed files.

Also: should the handoff MANIFEST `created_at` be accurate? I put 14:24; fine.

Let me edit MANIFEST chars/tokens.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wc2xy6c/ws && B=<SPINE_BANK>/target/, description="Final verification and file inventory")`

Final: re-run the gate (auto) + openspec validate one more time to confirm nothing broke after the ARCHITECTURE.md rewrite (doesn't affect gate). And produce a final file listing.

Let me run a final consolidated verification and listing.

Also: I should double check that the DELTA.md is recognized and the `changes/` dir doesn't confuse OpenSpec. openspec validate passed. Good.

Let me run final check: openspec validate strict, delta validate, gate auto, and list created/changed files with sizes.

Then write the final summary answer.

One more consideration: the task asked "Критерии приёмки и план отката" — present in DELTA.md, design.md, spec. Good. "Измеримые NFR" — design.md table + spec requirement. Good. "Изменения контрактов без поломки" — openapi + contract-diff PASS. Good. "Что остаётся на решение человека" — design.md § Decisions reserved + ADR-009 A3 package. Good.

Also the numbering: I added spine AD-009..AD-011 and ADR-008/009. Good.

Let me run final verification.

Also I realize the `docs/adr/ADR-008...` file name has a very long slug (from the tool). Fine.

Let me finalize.


Everything verified. Now write the final concise but complete summary, covering the 7 requested deliverables, the created/changed files, and honestly reporting the Critical-gate findings (sensors pre-existing failure + skipped nfr/evidence/model) and what remains for the human architect.

Note: `.qwen/settings.json` was already modified before I started — I should say I didn't touch it.

Let me write the final answer in Russian (user wrote in Russian). Include:
- Brief statement of approach (route, tools used).
- 1..7 answers (concise, referencing files).
- Verification results.
- Files created/changed.
- Findings / what needs the human.

Keep it structured and not overly long, but this is a substantial deliverable so some depth is warranted. I'll aim for a well-organized summary with tables where useful.

Let me include verification evidence: score 10/15 Critical; openspec validate valid; delta validate clean; spine lint clean; gate PASS with delta_guard coverage; contract-diff 0 breaking/4 non-breaking; Critical-route gate: 1 FAIL (pre-existing sensor in docs/spec/state-machine.md) + SKIPs (no model/, no EVIDENCE.yaml) — mandatory-for-Critical but A2/A4 artifacts.

Also mention: I did not touch accepted truth files (docs/nfr.md, solutioning.md, contracts/, spec/, README.md) — deltas carried in the change; archive/sync updates them later.

List files.

Let me write.
## Что сделано

Пакет изменения `add-sbp-recurring-payments` подготовлен по маршруту **Critical** и проверен инструментами репозитория (`arch-be`, `openspec`). Принятые файлы решения я не переписывал: спайн изменён добавлением блоков `Proposed` (механизм, который спайн сам объявляет), контракт — аддитивно с минорным бампом, изменения живой истины (`docs/nfr.md`, `docs/solutioning.md`, `docs/contracts/*`, `docs/spec/*`, `README.md`) не тронуты — они вливаются дельтой на этапе `archive`.

## 1. Значимость и маршрут

`arch-be control score --trigger … --from-diff` → **10/15, маршрут Critical**. Сработали: `financial_impact`, `security_boundary_change`, `consistency_model_change`, `api_contract_change`, `data_contract_change`, `cross_domain_integration`, `new_component`, `significant_nfr`, `rto_rpo_targets`, `criticality_or_exception`. Не сработали: `new_datastore`, `new_vendor`, `domain_ownership_change`, `trust_zone_change`, `irreversible_migration`. Обоснование — `proposal.md` § Significance and Route. Важная честная деталь: `gate --route auto` показывает Fast (score 1), т.к. триггеры из диффа механически не выводятся; заявленная оценка — вход гейта.

## 2. Влияние на принятую архитектуру

Таблица в `design.md` § Impact on the accepted architecture: AD-001, AD-004, AD-005, AD-006, AD-008 — **не изменяются**; AD-002, AD-003, AD-007 — **расширяются** областью применения (согласия/попытки); добавлены **AD-009, AD-010, AD-011** (Proposed). Ключевое: зачисление остаётся «только из `PAID`» (AD-005), добавляется новое предусловие списания (AD-009), приоритет отзыва (AD-010) и идемпотентность попытки (AD-011). Область вендорского транспорта (AD-008/ADR-007 [ADOPTED]) не расширяется молча — вынесена в ADR-009.

## 3. Архитектурное решение

`docs/adr/ADR-008-*` (модель согласия + исполнение списаний: 6 альтернатив, отрицательные последствия, обратимость `costly` с обоснованием) и `docs/adr/ADR-009-*` (область транспорта подписок, `reversible`, с машинно-читаемым A3-пакетом `{choice, rationale, constraints, rejected options, expiry}`).

## 4. Контракт без поломки потребителей

`openapi/tsp-api.yaml`: `0.1.0 → 0.2.0`, добавлены `/v1/consents*`, опциональное поле `consentId`, схемы `Consent*/Charge*/Problem`; существующие пути/поля/значения enum не изменены. Проверено: `arch-be contract-diff` v0.1.0→v0.2.0 — **0 ломающих, 4 non-breaking, PASS**.

## 5–7. NFR, приёмка, откат, A3

Измеримые NFR (старт списания p95 ≤ 5 мин, лаг отзыва p95 ≤ 60 с, пик 2000 TPS/5 мин, 0 несанкционированных/двойных, RPO=0, ≥ 99,95 %) — `design.md` § NFR budgets и требование в спеке. Критерии приёмки и план отката — `design.md` § Acceptance criteria/§ Rollback и `DELTA.md`. Что остаётся человеку — `design.md` § Decisions reserved for the human architect (7 пунктов) + A3-пакет ADR-009.

## Проверки (все зелёные, кроме оговорённого)

| Проверка | Результат |
|---|---|
| `openspec validate … --strict` | `Change 'add-sbp-recurring-payments' is valid`, 4/4 артефакта |
| `arch-be delta validate` / `control spine` | нарушений нет / нарушений нет |
| `arch-be gate` | PASS; `delta_guard`: `ARCHITECTURE-SPINE.md ← 'add-sbp-recurring-payments'` |
| `arch-be contract-diff` | 0 breaking, PASS |
| `control check` по правилам пакета | 11 правил, 0 нарушений |
| Verbatim-проверка | 11/11 `Rule` из спайна дословно в epic-context (5496 знаков ≈ 1375 токенов) |

**Что не зелено (честно):** `arch-be gate --route critical` → FAIL по компоненте `sensors`: `docs/spec/state-machine.md` не имеет секций `## Проблема / ## Критерии приёмки / ## Риски`. Это **предсуществующее** состояние (файл я не менял, `git status` подтверждает) — структурный долг принятого артефакта, всплывший только на Critical-маршруте. Также на Critical пропущены `nfr`, `model_validate`, `evidence_verify` — нет `model/` и `EVIDENCE.yaml` (артефакты A2/A4, на этапе propose их быть не должно). Рекомендация: устранить `sensors`-находку отдельно (или на `archive`), не править принятую спеку «по пути».

## Созданные / изменённые файлы

Изменены: `ARCHITECTURE-SPINE.md` (+AD-009..AD-011, Proposed), `openapi/tsp-api.yaml` (0.2.0, аддитивно). Созданы: `docs/adr/ADR-008-*`, `docs/adr/ADR-009-*`; `openspec/changes/add-sbp-recurring-payments/{proposal,design,tasks}.md` и `specs/sbp-recurring-payments/spec.md`; `changes/add-sbp-recurring-payments/DELTA.md` (машинное покрытие правки спайна); `.arch-handoff-recurring/{TASK,ARCHITECTURE,README}.md + {CONSTRAINTS,RUBRIC}.yaml + MANIFEST.json + adr/ADR-008,009`. Файл `.qwen/settings.json` был изменён до начала работы — я его не трогал.

Пакет передачи вынесен в отдельный каталог `.arch-handoff-recurring/`, чтобы не перезаписать принятый `.arch-handoff/`; в `README.md` пакета описано, как слить его в основной при apply. Дальнейший шаг не за кодом: **A3** по ADR-008/ADR-009 и получение документации НСПК по подпискам, затем `opsx-apply`.
