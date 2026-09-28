<!-- источник: <HARNESS>/runs-v2-pilot/cells/wttdsvq/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-v2-pilot-cells-wttdsvq-ws/chats/4e2f9c0a-3c2f-45e7-aa5f-7cc0c751b380.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.arch-handoff/MANIFEST.json")`

Let me start by exploring the repository to understand the accepted decision, invariants, docs, and handoff rules.

Let me read the key files first.
Начну с изучения принятого решения: спайн, документы, контракты и правила репозитория.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.arch-handoff/ARCHITECTURE.md")`

Let me read the docs: solutioning.md, nfr.md, ADRs, contracts, state-machine, and the .arch-handoff files (CONSTRAINTS.yaml, ARCHITECTURE.md, RUBRIC.yaml, connect-manifest.json). Let me also check .qwen/settings.json and skills.

Let me batch reads.
Изучаю дизайн-документы, NFR, ADR, контракты и правила гейта.

  `glob(pattern="**/*", path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs")`
  `glob(pattern="**/*", path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/openapi")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/openapi/tsp-api.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.arch-handoff/connect-manifest.json")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/settings.json")`

Let me read the rest: docs/adr/*.md (all), docs/contracts/*, docs/spec/state-machine.md, docs/rfp/vendor-rfp.md, openapi/tsp-api.yaml, .arch-handoff/RUBRIC.yaml, connect-manifest.json, .qwen/settings.json, and the skills directory.

Let me list the docs directory and .arch-handoff.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/adr/ADR-002-model-konsistentnos)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/adr/ADR-004-at-least-once-dlq.m)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/adr/ADR-005-integraciya-s-abs-z)`

Now let me read the ADRs fully (they're important), contracts, state-machine, rfp, and the skills directory listing.

The ADR files: ADR-001 already read fully. Let me read the rest.
Читаю ADR-002…007, контракты и статусную машину.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/spec/state-machine.md")`

Now let me read ADR-006, ADR-007, contracts, state-machine, rfp, and the skills.

  `glob(path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen", pattern="**/*")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/rfp/vendor-rfp.md")`
  `run_shell_command(command="arch-be --help 2>&1 | head -60", description="Show arch-be CLI help")`

Now I have a good understanding. Let me read the OPKC adapter contract and the vendor RFP to understand the internal contract, and check the skills directory.

Also need to understand "принятый способ изменения" for the accepted decision files. The .arch-handoff has delta_guard — protected paths: model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. And there's a "дельта-протокол" (model 5.2). Let me check if there's a model/ dir or openspec/ dir. There's no model/ in the tree. Hmm. The delta_guard mentions "изменённый файл под защищёнными путями (по умолчанию model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml)". So the accepted way to change the spine is via a delta (openspec change?). Let me check settings.json (project) and skills. Also check if `arch-be` CLI is available and what commands exist (`arch-be --help`, `arch-be rules template`, etc.).

Let me also check the .qwen/skills directory (installed spine playbooks).

Let me look at the skills available. The available_skills list includes many project skills — these are likely in .qwen/skills. Let me list them.

Key skills relevant here:
- significance-routing (оценка значимости)
- spine-invariants (ARCHITECTURE-SPINE, AD-n)
- adr-authoring
- delta-spec (OpenSpec delta — «Дельта-спецификации для brownfield-потока (по OpenSpec)»)
- nfr-design
- docx-solution-design (SAD docx)
- fitness-functions
- readiness-gate
- adversarial-review
- handoff-packaging
- spine-contracts-gate (OpenAPI lint/diff)
- c4-mermaid
- rubric-judging / spine-adr-judge
- semantic-review

The task: prepare an architectural package of this change on top of the accepted decision, for architectural decision and handoff. Deliverables 1-7.

The accepted way to change files: This repo uses spine + delta protocol. `delta_guard` gate: direct edits to protected paths (model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml) are blocked; changes must go through a delta. OpenSpec delta-spec skill: change described as ADDED/MODIFIED/REMOVED relative to current truth, cycle propose → apply → archive.

Let me check whether there's an openspec/ directory — no. The tree showed only docs, openapi, .arch-handoff, .qwen. So maybe the "принятый способ" is: create a change delta. Let me check `arch-be` CLI capabilities and the delta-spec skill.

Also note: the Stop hook runs `arch-be gate --route auto --base bench-baseline`. So any change must pass the gate before finishing. Let me run `arch-be gate` eventually. But careful — gate compares to base bench-baseline.

Let me first check tools: run `arch-be --help`.

Let me look at skills dir and run arch-be help.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/skills/significance-routing/SK)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/skills/spine-invariants/SKILL.)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/skills/adr-authoring/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/skills/delta-spec/SKILL.md")`

Let me read the relevant skills: significance-routing, spine-invariants, adr-authoring, delta-spec, nfr-design, spine-contracts-gate, handoff-packaging, adversarial-review, readiness-gate, spine-fitness-gate.

Also, importantly, understand the "принятый способ изменения" of accepted decision files. Let me check the delta-spec skill and delta_guard defaults. Also check `arch-be gate` current state and `arch-be control --help`, `arch-be rules --help`.

Let me be efficient. Read skills: delta-spec, significance-routing, adr-authoring, nfr-design, spine-contracts-gate, handoff-packaging.

Also check git log to understand baseline commit.

Let me batch.
Читаю методические навыки, задающие принятый порядок (значимость, инварианты, ADR, дельта-спека, NFR, контрактный гейт, handoff).

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be control --help 2>&, description="Show arch-be control help")`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be gate --help 2>&1 |, description="Show arch-be gate help")`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be rules --help 2>&1 , description="Show arch-be rules help")`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && git log --oneline -10 && e, description="Show git history and branches")`

Now let me read nfr-design, spine-contracts-gate, handoff-packaging, readiness-gate, fitness-functions. Also check `arch-be gate` current state, `arch-be control --help`, `arch-be rules template list`, `arch-be handoff --help`, and the delta_guard defaults.

Also important: the `.arch-handoff` is the handoff package. The task says "передать исполнителям" — so we should produce an updated handoff package (epic-context + CONSTRAINTS + TASK) for the new functionality. And "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — the accepted way = delta protocol: direct edits to protected paths (ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml, model/) are blocked by delta_guard. So we must create a delta (openspec change set) rather than directly editing spine/CONSTRAINTS.

Let me verify what paths delta_guard protects by running the gate and delta guard. Let me look at `arch-be control --help` and `arch-be gate`.

Let me run several CLI introspection commands.

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be gate --route auto , description="Run architecture gate against baseline")`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be control gate --hel, description="Show control gate and handoff help")`

Now let me check the current gate state (baseline), and the delta guard protected paths. Let me run `arch-be gate --route auto --base bench-baseline` to see the current state. Also `arch-be control gate --help` and try delta guard directly. Actually let me run the gate.

Also, I should check `arch-be handoff --help` to see how the handoff package is generated (the accepted way to update .arch-handoff).

Let me run gate now to see baseline status.
Смотрю текущее состояние гейта и правила дельта-протокола (защищённые пути).

  `tool_search(query="select:mcp__spine__delta_guard,mcp__spine__significance_score,mcp__spine__openapi_lint,mcp__spine__contract_diff,mcp__spine__rules_suggest")`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && ls -la && echo \"=== find , description="List repo and search for openspec/model/delta dirs")`

Now I understand. Let me check the delta guard defaults — protected paths. Let me look for the arch-be binary help for delta guard, maybe `arch-be control spine --help`. But the gate says delta_guard — protected paths default model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml.

So to modify the "accepted decision files" — I should not directly rewrite them, but follow the delta/openspec protocol. But there's no openspec/ dir currently. Let me check whether the repo has an `openspec` skill and directories. The delta-spec skill describes OpenSpec-like delta. The gate has `delta_guard`. So the accepted way to change ARCHITECTURE-SPINE.md / CONSTRAINTS.yaml is via a delta that delta_guard recognizes.

Let me check what delta_guard recognizes. Perhaps via MCP tool `delta_guard` (deferred tool mcp__spine__delta_guard: "Гейт прямых правок спайна мимо дельты (модель 5.2): каждый изменённый файл под защищёнными путями (по умолчанию model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.ya...").

Let me inspect the delta_guard schema to learn how to legitimately change protected files. Let me use tool_search to get the schema.

Also, I should check `arch-be` docs about the delta protocol. Maybe there's a `docs/control.md` referenced. Not in this repo. Let me search the repo for "дельта" references and also check kb.

Let me use tool_search for delta_guard and for openspec-related tools.

Actually let me be strategic. The deliverables:
1. Оценка значимости и маршрута — use `significance_score` (MCP) / `arch-be control score`.
2. Влияние на принятую архитектуру — analysis, invariants affected. Deliverable in a document (e.g., impact assessment / delta).
3. Архитектурное решение (ADR) with alternatives, consequences, reversibility — write ADR-008 (new ADR file in docs/adr/). Following ADR-011? No, next is ADR-008. Use adr-authoring skill.
4. Изменения контрактов openapi/tsp-api.yaml without breaking existing consumers — modify OpenAPI with additive changes, run openapi_lint + contract_diff.
5. Измеримые NFR — update docs/nfr.md or add NFR doc.
6. Критерии приёмки и план отката.
7. Что остаётся на решение человека-архитектора (A3) — open questions.

Plus update handoff package for executors (epic-context + TASK + CONSTRAINTS) — since task says "затем передать исполнителям".

And the change to accepted files (spine, CONSTRAINTS) must go through the accepted mechanism (delta).

Let me learn delta_guard schema and check how to create a delta. Let me search tools.

Let me also run `arch-be control score` with triggers to get a deterministic score. And run `arch-be control rules-suggest`.

Let me first get delta_guard schema and check for openspec dirs.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/skills/spine-fitness-gate/SKIL)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/skills/spine-contracts-gate/SK)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/skills/handoff-packaging/SKILL)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/skills/nfr-design/SKILL.md")`

delta_guard: each changed file under protected paths must be mentioned in an active delta `changes/<name>/DELTA.md`. So the accepted way to change ARCHITECTURE-SPINE.md / CONSTRAINTS.yaml is to create `changes/<name>/DELTA.md` that mentions them.

Let me read spine-fitness-gate skill and fitness-functions skill to understand delta protocol and gate details. Also spine-bundle. Let me read those.

Let me also read the nfr-design, spine-contracts-gate, handoff-packaging, readiness-gate skills.

Let me batch read the most relevant.

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be --help 2>&1 | sed , description="Check arch-be top-level commands and delta subcommand")`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/skills/spine-bundle/SKILL.md")`

Now I understand the mechanism for changes: `arch-be delta new <name>` — creates `changes/<name>/DELTA.md`. Let me check `arch-be delta --help` to see the commands (new, apply, archive?). Let's check.

Also, I want to read the spine-bundle skill and delta-spec references. But let me first check `arch-be delta --help`.

Let me run.

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be delta --help 2>&1 , description="Check delta subcommand availability")`

No `delta` subcommand in the top-level help listing? Let me check full list. The help output earlier was truncated at head -60. Let me get the full command list. Actually `arch-be delta --help` returned nothing visible (the output only showed the tail of --help). Let me run separately.

Actually the spine-bundle skill says "дельта-протокол работает от базы". And delta_guard needs `changes/<name>/DELTA.md`. The spine-fitness-gate skill said `arch-be delta new <name>`. Let me confirm.

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be gate --route criti, description="Run gate forcing critical route to see requirements")`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be control score --he, description="Show significance score CLI help")`

Now I understand the accepted mechanism: `arch-be delta new <name>` creates `changes/<name>/DELTA.md`. Changing ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml requires the file to be mentioned in an active delta.

Let me now plan the deliverables. Given the criticality (payments, KII, financial), this is Critical route. Let me compute the significance score deterministically.

Let me run `arch-be control score --trigger ...` to get the official score. Triggers for this change (recurring C2B subscriptions via payer consent — СБП subscriptions):
- api_contract_change: true (new endpoints in TSP API, new permissions on existing)
- data_contract_change: true (new mandate/consent entity, new fields)
- consistency_model_change: maybe true (new deferred charge model)
- security_boundary_change: true (storing payer consent + mandate; new capability to debit without client action)
- trust_zone_change: likely (payer consent handling, new data of payer)
- financial_impact: true (recurring debits)
- significant_nfr: true
- new_component: maybe not (new component? We might add a "mandate/subscriptions" component). Could be true.
- new_datastore: possibly (mandate store)
- criticality_or_exception: true (КИИ / payments)
- cross_domain_integration: maybe
- rto_rpo_targets: yes (recurring is critical)
- domain_ownership_change: maybe
- new_vendor: false
- irreversible_migration: false

Anyway it's clearly Critical. Let me run the score tool with a defensible set.

Let me now think about the architecture solution for recurring C2B payments (СБП подписки).

In СБП, recurring C2B payments are implemented via "Платежный сервис СБП" — actually СБП has "Автоплатежи" / "Периодические платежи" via "СБП Подписки". In real СБП, there is a mechanism: ТСП registers a recurring payment mandate ("Соглашение") once, payer confirms in their bank app, and then ТСП can initiate debits (C2B) without payer action for each period. The СБП API has "Запрос на согласие" (consent/mandate), "Списание по согласию" etc. But here the protocol is [ТРЕБУЕТ ПРОВЕРКИ] — we should design contract-agnostically.

So the architecture change: introduce a new aggregate "Согласие плательщика на рекуррентные списания (mandate/subscription)" as a first-class entity with its own state machine; recurring charges are ordinary C2B payments initiated by the gateway against an active mandate (no QR, initiated server-side, authorized by mandate). The key invariants:
- AD-005: зачисление только из PAID — still holds (each charge must be confirmed by НСПК).
- AD-002: status machine single source of truth — extended with mandate state machine, atomic transitions.
- AD-003: idempotency — each charge needs idempotency key; mandate operations too.
- AD-001: isolation — mandate logic inside gateway.
- AD-004: single OPKC adapter — mandate operations go through the adapter contract (new adapter methods: createConsent, getConsentStatus, revokeConsent, and events consent.activated/consent.revoked).
- AD-007: audit — consent must be auditable (payer consent proof), also 152-ФЗ ПДн, 161-ФЗ.

Key architectural risks:
- Consent/authorization is a legal artifact: who proves the payer consented? Must be provable and audit-logged. Payer revocation must immediately stop future charges.
- Need "no charge without active mandate", "mandate amount limits", "maximum per-charge and total limit", "period".
- Revocation race: revocation concurrent with a charge — need defined semantics (charge in flight that got PAID must still be credited; but new charges blocked). This is a saga/ordering problem; must be explicit.
- Idempotency of recurring charge and mandate; double-charge prevention.
- Notifications to ТСП and payer; mandatory pre-notification of debits (regulation may require notifying payer before debit).

Alternatives for consent ownership:
1. Mandate stored only in OPKC/НСПК (bank is stateless) — no local source of truth, breaks RPO=0 and offline behavior.
2. Local mandate store as projection of OPKC consent with reconciliation (chosen) — consistent with AD-002.
3. Vendor-managed subscriptions module — vendor lock-in, financial logic outside bank.

Alternatives for charge initiation:
1. Scheduled job initiates charges (puller) — needs scheduler, risk of duplicate runs.
2. Event-driven / order-driven from ТСП (ТСП requests each charge) — chosen maybe, or hybrid: gateway schedules based on mandate, or TSP asks.
Actually in СБП subscriptions, typically the ТСП initiates each debit request within the mandate parameters. Let me design: two modes — (a) ТСП-initiated charge (ТСП sends POST /subscriptions/{id}/charges with amount), (b) auto-scheduling (gateway schedules per mandate schedule). Business says "рекуррентные C2B-списания по согласию плательщика — подписки СБП". Ambiguous. I'll present as a decision point / alternative: ТСП-initiated (recommended, simpler, matches merchant billing) vs gateway-scheduled. Actually I should keep it as an alternative in the ADR and mark what remains for the human architect.

Alternatives for consent lifecycle model:
- Consent as attribute on payment vs first-class entity with state machine (chosen).
- OAuth-like token grant vs mandate entity.

Alternatives for the contract versioning: extend /v1 additively vs /v2. Chosen: additive to /v1 (new paths + optional fields), no breaking changes — since v0.1 is not yet released (draft, pre-A1). Actually the contract is v0.1.0 draft; so we can extend in v0.1.0/0.2.0 without breaking consumers. Need to run openapi_lint and contract_diff.

Now the deliverable structure. Let me design the file set:

Given the repo's accepted way:
- Changes to protected files (ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml) must be via delta: `changes/<name>/DELTA.md`.
- Non-protected: docs/**, openapi/** can be edited directly, but best to put the whole change as a delta package.

I'll create:
1. `changes/sbp-recurring-subscriptions/DELTA.md` — the delta spec (ADDED/MODIFIED), mentions ARCHITECTURE-SPINE.md and .arch-handoff/CONSTRAINTS.yaml so delta_guard passes.
2. `docs/adr/ADR-008-...md` — architectural decision with alternatives, consequences, reversibility. (new ADR; next number ADR-008)
3. `docs/spike/...` no. 
4. Update `ARCHITECTURE-SPINE.md` — add AD-009 (consent/mandate invariant) and AD-010? And modify AD-002/AD-003? Careful: "Принятые файлы решения меняй только тем способом, который принят" — via delta, we can modify spine, but the delta must mention it. Since we must add new invariants for recurring, we should add AD-009 (рекуррентные списания только по активному согласию) and maybe AD-010. Also we need to record that permission to change spine is via delta. But should the spine modification be done now, or proposed in the delta? The delta's "propose" phase describes ADDED/MODIFIED; the actual edit to the spine happens in "apply". Hmm.

Let me think about what's cleanest and honest: The delta describes the proposed change. Then we "apply" — edit spine + CONSTRAINTS. Then archive? The cycle is propose → apply → archive. Since we're preparing the package for arch decision (A3) and handoff, we are in "propose" phase. But delta_guard requires the changed protected file to be mentioned in an active delta — meaning if we edit ARCHITECTURE-SPINE.md now, we must have an active delta mentioning it. Whether we edit it now (apply) or just propose — the deliverable expects the architectural package to be ready for decision and handoff. I think we should:

- Create the delta (propose).
- Apply the spine change (add AD-009/AD-010) and CONSTRAINTS additions — because handoff package must carry the new invariants and fitness rules. Keep the delta active (not archived) until A3 approves — that's honest: status "Proposed". Actually the delta-spec says archive after apply. But this is a decision-required change (A3), so it should stay Proposed/open until signed. I'll keep it open and note that archiving happens after A3.

Hmm, but there's a subtlety: leaving DELTA.md active is what lets delta_guard pass. Good.

Let me check `arch-be delta new` output template and `delta validate` requirements, and `arch-be delta guard` semantics (based on git diff). Let me create the delta and inspect.

Also need to consider: the Stop hook runs `arch-be gate --route auto --base bench-baseline`. The route is auto from git diff. If our diff includes new component/vendor/api contract etc., route becomes Critical, and then gate requires NFR + evidence bundles + decision_quality possibly (config gate.required). Let me check if there's a config file (arch-harness.toml). There's no arch-harness.toml in the repo listing. So defaults apply. On Critical route, gate checks: "на маршрутах Standard/Critical — количественные NFR и проверка evidence-бандлов". This might FAIL because there's no model/ and no evidence bundle. Let me check what happens. The hook would block my completion if gate FAILs. Hmm — that's a real risk: adding significant change may make auto-route Critical and gate FAIL on missing evidence/model, blocking the Stop hook (exit 2).

Let me investigate: what does gate require on Critical: nfr_check needs model/; evidence needs EVIDENCE.yaml. Both absent → could FAIL.

I need to handle this. Options:
- Keep changes such that auto-route stays low? Not honest.
- Provide the required artifacts: model/ directory with typed model, EVIDENCE.yaml bundle, etc. That's a big lift but maybe expected ("подготовь архитектурный пакет ... вынести на архитектурное решение и передать исполнителям"). Actually the repo has no model/ at all, and baseline gate is Fast with trace_check/model_validate SKIP. Let me test what gate says when route is critical.

Let me test by running gate with `--route critical` now to see what fails. That will tell me exactly what artifacts are needed.

Let me run that.
Проверю, что потребует гейт на маршруте Critical, — чтобы пакет был выпускаемым, а не просто документами.

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be control sensors --, description="Inspect spec sensors and current findings")`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be delta new --help 2, description="Show delta subcommand help")`

The critical gate FAILs on `sensors` — docs/spec/state-machine.md missing sections ## Проблема, ## Критерии приёмки, ## Риски. Also "Не проверено (обязательно для маршрута Critical): trace_check, nfr, model_validate, evidence_verify" — these are SKIP because no model/. Note: SKIP isn't FAIL for the exit code (FAIL is only the sensors +). Wait, "Не проверено (обязательно...)" — these are SKIP, not FAIL. So gate FAIL count = 1 (sensors). So to make the gate PASS on Critical, I need sensors to pass — i.e., add the required sections to docs/spec/state-machine.md (or our new spec files). Interesting: sensors checks required sections in spec files. Let me check `arch-be control sensors --help` to know which files/required sections.

Actually the sensor "required-sections" applied to ./docs/spec/state-machine.md requires ## Проблема, ## Критерии приёмки, ## Риски. That's likely a config-defined sensor. Since the file already exists (pre-existing) and fails, this is a pre-existing condition? Wait — baseline gate was Fast and sensors wasn't run on Fast. On Critical it runs. So the case is "not critical-ready" currently — the baseline accepts Fast because auto-route detected 0 triggers (no diff vs baseline). Hmm, the baseline commit is the "condition set" (plain+spine-hook). The case is intentionally incomplete for critical.

The Stop hook runs `--route auto --base bench-baseline`. Auto route from git diff vs bench-baseline. If my diff introduces triggers (api_contract_change, security_boundary_change, financial_impact...), route becomes Critical, and then sensors FAIL → hook exit 2 → blocks. And also "Не проверено обязательно" — maybe for auto critical it also fails? The FAIL list only showed sensors. Exit 1. But the "Не проверено (обязательно...)" listing suggests incomplete, maybe exit 3 (INCOMPLETE) in machine formats. The text said "Итог: FAIL — провалено составляющих: 1 (exit 1)". So exit 1.

So I must ensure the gate passes. That means:
1. Fix sensors: add required sections to docs/spec/state-machine.md (## Проблема, ## Критерии приёмки, ## Риски). But wait, is that in scope? The task is about recurring payments. The sensor is a pre-existing finding on an existing file. Adding required sections to state-machine.md is arguably improving readiness for a critical change. Hmm. But careful: modifying accepted files must be via accepted mechanism. state-machine.md is not a protected path (protected: model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml). So direct edit is fine. But is it right to edit the M0 state machine spec for a critical route sensor? Let me check what the sensor config expects — maybe it applies to all docs/spec/*.md. Let me check `arch-be control sensors --help` and run it.

2. To be fully "critical-ready" per the gate, we need model/, NFR (model-based), evidence bundle. But those are SKIP, not FAIL. The "Не проверено" is informational. However, the message says "обязательно для маршрута Critical". For an honest package for a Critical change, we should probably create the model/ and evidence bundle. That's a substantial but valuable deliverable (typed model + traceability + NFR check + evidence bundle). The task asks for a full architectural package to bring to arch decision and handoff. The spine skills (spine-content-bootstrap, spine-bundle) suggest this is expected.

Given the effort budget, let me consider: The gate only FAILs on sensors. SKIPs don't fail. But `evidence_verify` SKIP because no EVIDENCE.yaml. Hmm. Actually wait, maybe on auto route, if route is critical AND required components are skipped, is that FAIL? Let me test: the output shows SKIP and итог FAIL only due to sensors. So missing model is not fatal to exit code. But it says "Не проверено (обязательно для маршрута Critical)". Possibly a stricter mode? No.

Let me focus: make gate PASS on the auto route that my diff will produce. Let me first determine the auto route once I make changes — likely Critical due to api_contract_change + financial_impact + security_boundary_change. Then sensors must pass.

Let me check sensors: run `arch-be control sensors --help` and `arch-be control sensors .`.

Also note: our new/modified spec files (state-machine delta, new subscription spec) may add required-sections checks. The sensor found the existing state-machine.md lacking sections. If I add a new spec file, does it also need those sections? Possibly the sensor requires certain sections in files matching a pattern. Let me inspect.

Let me check sensors and the required sections config. There's no arch-harness.toml, so it might be built-in defaults. Let me run.

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be delta new sbp-recu, description="Create delta skeleton and show template")`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be control sensors ./, description="Run spec sensors on docs and docs/spec")`

Sensor `required_sections` operates on all docs? "Каталог спецификаций" = `.` and it scanned ARCHITECTURE-SPINE.md and README.md, requiring ## Проблема, ## Критерии приёмки, ## Риски. But in the gate, only ./docs/spec/state-machine.md was reported. Hmm — the gate reported only one sensor fail (state-machine.md) while `sensors .` shows ARCHITECTURE-SPINE.md and README.md. Different scoping? Actually gate said "сенсоров прогнано: 2, провалено: 1" and only state-machine. Maybe the gate scans a specific directory (docs/spec/?) — no, it said ./docs/spec/state-machine.md. Hmm, maybe gate's sensor scope is different: it may scan only files matching a "spec" glob, or the gate uses a different config. Actually `sensors .` scanned ARCHITECTURE-SPINE.md and README.md but not docs/spec/state-machine.md. Interesting inverse.

Wait: `arch-be control sensors .` scanned ARCHITECTURE-SPINE.md and README.md (4 sensors: required_sections + upstream_coverage each). The gate sensors scanned ./docs/spec/state-machine.md only ("сенсоров прогнано: 2, провалено: 1" → 1 required_sections + 1 upstream_coverage for state-machine.md). So gate uses a spec directory of `docs/spec` maybe, while CLI arg `.` scans root files only (maxdepth 1?). Let me run `arch-be control sensors ./docs/spec`.

Let me understand the required sections rule: it requires "## Проблема", "## Критерии приёмки", "## Риски" in spec docs. That seems like a "unified spec template" (like a spec-of-change with problem/acceptance/risks). The docs/spec/state-machine.md doesn't have them.

So for the gate to pass, docs/spec/state-machine.md must contain those three sections. But does adding those sections make sense? A "state machine spec" having "## Проблема / ## Критерии приёмки / ## Риски" — yes, it's the change-spec template. Adding them is reasonable and improves the spec. But careful: edited accepted file — allowed (not protected). I'll add the sections meaningfully (problem statement of the state machine, acceptance criteria, risks). Actually, better: my new subscription spec will also be under docs/spec/ and must carry those sections. And the existing state-machine.md must be updated too (otherwise gate fails even if my new file is perfect). Hmm — but is that a pre-existing failure that I'm now forced to fix? Yes, because route becomes Critical. That's acceptable: it's a real readiness finding.

Wait, but actually maybe the gate's sensor scope is only files that changed? No — state-machine.md is unchanged at baseline yet flagged. So it's a fixed scan of docs/spec. Let me confirm by running `arch-be control sensors ./docs/spec`.

Let me also double check the gate sensor message: "сенсоров прогнано: 2, провалено: 1" → 2 sensors = required_sections + upstream_coverage for the one file. So it scanned exactly one file: docs/spec/state-machine.md. So gate scans docs/spec/*.md for required sections.

Let me verify.

Also, I realize the more important question: will the auto route become Critical and thus run sensors? Let me plan to make the gate green regardless. I'll:
- Add required sections to docs/spec/state-machine.md (Проблема/Критерии приёмки/Риски) — small, meaningful.
- Ensure my new spec files include those sections.
- Possibly create model/ + evidence to satisfy "обязательно". But those are SKIP not FAIL. However, to be a genuinely complete Critical package, creating model/ is likely expected by skills (trace_check, nfr_check). But it's a large lift. Let me gauge: `model_validate`, `trace_check`, `nfr_check` need model/ in a specific format (typed model: REQ, NFR, AD, CMP, INT, CONT...). Given the MCP tools and skills (spine-content-bootstrap), creating a model is feasible but risky/time-consuming. The gate does not fail on missing model (SKIP). The task says "подготовь архитектурный пакет" with 7 items. It doesn't explicitly require a typed model or evidence bundle. But the repo's accepted way and the critical route suggest it.

Let me reconsider scope and effort. The user's 7 deliverables are document-level: significance, impact, decision (ADR), contract changes, NFR, acceptance+rollback, human decisions. Plus "передать исполнителям" → update handoff package. The gate must pass (Stop hook). Minimal to pass gate: sensors must pass. Let me also try to add model/ if time permits — but the instruction "Не пиши код" refers to not implementing; architecture model is fine.

Hmm, actually creating a typed model and evidence bundle would strongly align with "архитектурный пакет ... передать исполнителям" and the Critical route. But risk of breaking the gate: model_validate/trace_check/nfr_check become active (no longer SKIP) and could FAIL. If I create a partial model, it may cause failures. Given uncertainty, safer to NOT create model/ (keeps them SKIP) unless I can validate it. Let me check model schema via MCP `model_validate` and the spine-content-bootstrap skill. Actually, let me first focus on the core deliverables and the gate; I'll evaluate model creation after.

Let me now think about the risk of auto-route. Let me compute the score deterministically with `arch-be control score` and also `--from-diff` after changes. The gate auto uses `--route auto` computed from git-diff. Let me check `significance_from_diff` detectors: new_component, new_vendor, api_contract_change, ... Adding endpoints to openapi/tsp-api.yaml likely triggers api_contract_change. Modifying docs likely not. Let me just proceed and then run the gate; adjust as needed.

Actually, wait. Let me reconsider: The Stop hook gate could block me. But I control the final answer; the hook runs on Stop. If gate FAILs, the hook exits 2 and the session continues, prompting me to fix. I should pre-emptively ensure gate PASS.

Let me now run sensors on docs/spec and check the required sections template.

Let me also inspect `arch-be delta new` template by creating the delta early (it's needed anyway).

Plan of files to create/modify:

A. Delta package (mechanism):
- `changes/sbp-recurring-subscriptions/DELTA.md` (created via `arch-be delta new`), then filled with ADDED/MODIFIED/REMOVED, mentioning ARCHITECTURE-SPINE.md and .arch-handoff/CONSTRAINTS.yaml.

B. Accepted decision files (via delta, i.e., protected but covered):
- `ARCHITECTURE-SPINE.md`: add AD-009 (recurring charges only under active payer mandate; revocation stops future charges; charge is a normal payment subject to AD-005), AD-010 (mandate is a first-class auditable entity; consent proof; ПДн minimization). Possibly extend AD-003/AD-005 Binds. Keep minimal: add AD-009, AD-010.
- `.arch-handoff/CONSTRAINTS.yaml`: add fitness rules for new invariants (e.g., mandate-only-charge, consent audit log, no charge without active mandate; openapi contract rule; NFR rule).

C. New/updated docs:
- `docs/adr/ADR-008-...md` — decision: recurring C2B via payer mandate; alternatives (mandate-first-class vs attribute; TSP-initiated vs gateway-scheduled; local store vs OPKC-only vs vendor), consequences, reversibility, expiry.
- `docs/solutioning-recurring.md` (or extend docs/solutioning.md) — impact on architecture, components, flows (consent flow, charge flow, revocation), what changes/doesn't.
   Better: create `docs/changes/…`? Let me use `docs/solutioning-subscriptions.md`. Or keep the change package self-contained under `changes/sbp-recurring-subscriptions/` with subdocs. The repo convention: docs/ holds design. I'll add `docs/subscriptions.md` (solution design delta) and update `docs/nfr.md` (add NFR rows for subscriptions), update `docs/spec/state-machine.md` (mandate state machine + required sections), update `docs/contracts/tsp-api.md` (new endpoints doc), update `openapi/tsp-api.yaml` (new paths/schemas additively).
- `docs/nfr.md`: add measurable NFRs for recurring (charge latency, mandate activation, revocation propagation ≤ X, availability, idempotency, no double charge).
- Acceptance criteria + rollback plan: put in the delta / a dedicated `changes/.../ACCEPTANCE.md`? The delta template may have sections. Let me see template.

D. Handoff package update:
- `.arch-handoff/ARCHITECTURE.md` (epic-context for the new epic) — regenerate via `arch-be handoff`? That command is "harness build only" and requires --task/--spec; may work. But it might overwrite existing. The handoff-packaging skill: "CONSTRAINTS.yaml — пользовательские правки не затираются". Safer: create a NEW handoff package for the subscriptions epic in a separate dir, e.g. `changes/sbp-recurring-subscriptions/handoff/` or update `.arch-handoff/`. The task: "затем передать исполнителям" — I'll produce an updated handoff package for the subscriptions increment. I could update `.arch-handoff/TASK.md` and `.arch-handoff/ARCHITECTURE.md` and `MANIFEST.json` via `arch-be handoff`. But `.arch-handoff` is the accepted handoff package for the walking skeleton. Adding a second task might be cleaner as a separate package dir. Let me check `arch-be handoff` behavior.

Given complexity, let me define the concrete deliverable map and start implementing. But first, let me read a few more skills quickly (readiness-gate, adversarial-review, fitness-functions) and inspect delta template + sensors. Let me batch.

Actually, I've spent a lot on reading. Let me be efficient now: create the delta to see template, and inspect sensors on docs/spec.

Let me also decide on using skills: The task says "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." I should invoke the Skill tool for the key skills? The Skill tool invokes a skill in the main conversation (loads its content). But I've already read them via read_file. The instruction to "invoke a skill by passing its name to the Skill tool" — but these are project skills (files). The `skill` tool description says available skills are listed in system-reminder and to invoke via Skill tool. However reading them directly works too. To honor "используй их по назначению", I'll apply their methods. I might invoke the Skill tool for a couple. But invoking a skill just loads the doc I already read. I'll rely on applying them.

Let me proceed: create delta, inspect template, run sensors on docs/spec.
Создаю дельту (принятый в репозитории способ менять спайн/правила) и смотрю её каркас, параллельно — сенсоры по `docs/spec`.

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be control score --tr, description="Compute architecture significance score for the change")`

Interesting: `sensors <dir>` scans only top-level *.md in the given dir (not recursive). Gate scans ./docs/spec (found state-machine.md). So gate sensor scope = docs/spec/*.md. Thus I must ensure every *.md in docs/spec has ## Проблема, ## Критерии приёмки, ## Риски. Currently only state-machine.md. If I add a new file docs/spec/subscriptions.md, it must have these sections too.

Required sections: "## Проблема", "## Критерии приёмки", "## Риски" — I'll add them to state-machine.md and include in new subscription spec.

Wait, but is docs/spec the sensor dir in gate? The gate reported ./docs/spec/state-machine.md. Yes.

Hmm, but actually maybe the gate scans `spec/` dirs findable. Let me not overthink: ensure docs/spec/*.md all have those sections.

Now the delta template has: Проблема, ADDED, MODIFIED, REMOVED, План отката, Критерии приёмки. It says "Route: Fast|Standard (Critical — полный Solutioning, дельты недостаточно)". For our Critical change, delta alone insufficient — full Solutioning needed. But delta_guard still requires the delta to mention protected files. So we keep the delta as the change record + full Solutioning docs.

Now, is our change Critical? Let me compute score. Let me run `arch-be control score` with triggers.

Let me think about which triggers honestly apply:
- new_component: Maybe — we add a "Подписки/Мандаты" module. I'd say true (new logical component). But could be argued as extension. Let's mark true.
- new_datastore: mandate store — could be part of existing DB (new tables). Not necessarily new datastore. Mark false (tables in existing DB). Hmm but "new_datastore" is strict. I'll mark false.
- new_vendor: false (no new vendor).
- domain_ownership_change: new domain (subscriptions) — maybe true. Could mark false (same payment domain). I'll mark false.
- cross_domain_integration: false.
- api_contract_change: true.
- data_contract_change: true (new mandate entity, events).
- security_boundary_change: TRUE — the whole point: recurring debit without client action changes the authorization boundary; mandate/consent handling, storing consent evidence. This is the critical trigger.
- trust_zone_change: false (same zones). Maybe true because payer data. I'll mark false.
- consistency_model_change: true (mandate-charge consistency, revocation race).
- significant_nfr: true.
- rto_rpo_targets: true.
- irreversible_migration: false.
- financial_impact: true.
- criticality_or_exception: true.

That's ~9 triggers → Critical anyway, and security_boundary_change alone forces Critical.

Let me run the score tool to have a deterministic number, using the MCP significance_score or CLI. CLI: `arch-be control score --trigger name=true ...`.

Let me run it.

Then I'll write the deliverables. Let me also check the delta validate requirements after writing (structure). And check `arch-be delta guard` behavior for untracked files (needs --base or git add -N; the Stop hook does `git add -A -N` first — good, so untracked files are staged as intent-to-add and appear in diff).

Important: The delta must "mention" the protected files. Let me confirm what "mention" means: probably the file path string appears in DELTA.md. I'll include explicit lines like "Изменяемые защищённые файлы: `ARCHITECTURE-SPINE.md`, `.arch-handoff/CONSTRAINTS.yaml`." to be safe. Let me test after.

Let me now compute significance and read readiness-gate + fitness-functions + adversarial-review quickly for the acceptance/rollback and ADA rubric.

Actually let me just compute score and proceed.

Let me also decide: do I need the typed model/? The critical gate SKIPs them. Given effort, I'll skip model/ but I'll note in the package what remains (the human architect items). Hmm, but "Не проверено (обязательно для маршрута Critical)" might be considered incomplete by the user. The user asked for a package to bring to arch decision and hand off. I think providing model/ + evidence is beyond the 7 listed deliverables and risky. But the repo's own "первый зелёный критического маршрута" expects a bundle. Let me weigh: The task explicitly lists 7 deliverables which map to documents, not a typed model or evidence bundle. And "Принятые файлы решения меняй только тем способом, который принят" strongly hints at the delta mechanism. I'll deliver documents + delta + ADR + contracts + NFR + handoff, and ensure the gate PASSES (fix sensors). I'll also try to make route Critical but gate green.

Wait — if gate route is Critical and I don't have model/, the sensors must still pass (they're independent). Let me ensure that.

Let me run the score now and then start writing.

Actually, one concern: if route auto becomes Critical, the gate will run sensors on docs/spec. If I add docs/spec/subscriptions.md with required sections and fix state-machine.md, sensors pass. Good. trace/nfr/model/evidence remain SKIP. So gate PASS.

But hold on: will `--route auto` detect triggers from diff? Let me check detectors: it said "auto: score 0 (триггеров нет)" at baseline. Let me see `significance_from_diff` detectors: new_component / new_vendor / api_contract... Let me get its schema/CLI help. It's an MCP tool. Let me check via tool_search later if needed. Let me just proceed and run gate at the end.

Let me compute score deterministically.

  `tool_call(name="mcp__spine__openapi_lint", arguments={"path": "openapi/tsp-api.yaml", "cwd": "<HARNESS>/runs-v2-pilot/cells/wttdsvq)`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && echo \"=== RULES REPORT ==, description="Show rules report and suggested rules")`

Score 9 → Critical. 

Now let me plan and write the deliverables. Let me think carefully about the architecture content — this is the core value.

## Architecture design: Рекуррентные C2B-списания СБП (подписки)

### Concept
Introduce a new first-class aggregate: **Согласие плательщика (mandate / подписка)** — a payer-authorized instruction that allows the ТСП (via the gateway) to initiate C2B debits without the payer's per-payment action, within defined parameters (payee ТСП, amount limits, period, purpose, validity).

The mandate has its own lifecycle state machine:
`INITIATED → PENDING_PAYER (ожидание подтверждения в банке плательщика) → ACTIVE → (SUSPENDED?) → REVOKED` and terminal `EXPIRED`/`REJECTED`.

A recurring charge is a **normal C2B payment** (same payment state machine, AD-002/AD-005) that is *initiated by the gateway против активного mandate* rather than by a QR scan. It must be confirmed PAID by НСПК before crediting (AD-005 unchanged).

### Where the mandate lives
Decision: mandate is a first-class entity in the gateway's DB (single source of truth for the bank side), created via the OPKC adapter (protocol to НСПК — normalization), reconciled with НСПК. The bank is the "capturer" for its ТСП; the payer's consent is proven by the bank-плательщика side and reflected via НСПК consent status. Gateway stores the consent reference + audit trail (consent proof, parameters, timestamps) — minimizes ПДн.

### Key flows
1. **Оформление согласия (mandate init)**: ТСП → `POST /v1/subscriptions` (ТСП, параметры: payer ref/phone, amount limit per charge, max total, period, purpose). Gateway creates mandate `INITIATED`, calls adapter `createConsent`, returns `subscriptionId` + `consentUrl`/QR for the payer to confirm in the payer's bank app. Плательщик подтверждает в приложении банка-плательщика → НСПК event `consent.activated` → gateway `ACTIVE` (atomic + outbox + audit).
2. **Списание (charge)**: ТСП → `POST /v1/subscriptions/{id}/charges` (Idempotency-Key, amount) OR gateway-scheduled. Guard: mandate ACTIVE, amount ≤ per-charge limit, cumulative ≤ max total, not revoked, purpose match. Gateway creates a `payment` (CREATED) tied to `mandateId` and calls adapter `createPaymentLink`/debit-by-consent. Then normal PAID→CREDITED→COMPLETED path (AD-005).
3. **Отзыв согласия (revoke)**: Плательщик отзывает в своём банке (или ТСП/банк по правилам) → НСПК event `consent.revoked` → gateway `REVOKED` + block new charges. **In-flight charge semantics**: a charge already confirmed PAID by НСПК is completed (it was authorized before revocation took effect); new charges after REVOKED are rejected. Revocation propagation target ≤ N minutes (NFR).
4. **Истечение/приостановка**: mandate can expire by validity or be suspended (e.g., payer request).

### Invariants affected
- AD-001 (isolation): unchanged; mandate logic inside gateway; no direct ABS/OPKC.
- AD-002 (single source of truth, atomic transitions): **extended** — mandate state machine also atomic (status + outbox + audit). New invariant needed for mandate transitions.
- AD-003 (idempotency): **extended** — charge idempotency key; mandate creation idempotency; consent events dedup by eventId.
- AD-004 (single OPKC adapter): **extended** — new adapter methods (createConsent/getConsentStatus/revokeConsent) + events (consent.activated/revoked) — protocol stays inside adapter. No spine change needed (AD-004 already covers "протокол НСКП знает только адаптер"); but internal contract opkc-adapter.md must be extended.
- AD-005 (credit only from PAID): **unchanged and reasserted** — recurring charge also only credits from PAID; mandate authorization does NOT substitute for НСПК confirmation.
- AD-006/AD-007 (trust/НПС/КИИ/ПДн): **extended** — consent is a new class of ПДн (payer identifier, consent evidence); retention/audit; consent proof immutable audit.
- AD-008 (hybrid): unchanged; new adapter methods go to the vendor adapter contract (RFP scope changes).

New invariants (spine AD-009, AD-010):
- **AD-009. Рекуррентное списание — только по активному согласию плательщика.**
  Binds: сервис подписок (mandate), статусная машина платежа, адаптер ОПКЦ, АБС-адаптер, аудит-лог.
  Prevents: списание без согласия или за пределами его параметров (лимит суммы, период, получатель); списание по отозванному/истёкшему согласию; «тихое» списание без доказуемого согласия.
  Rule: Инициирование списания возможно только из состояния согласия ACTIVE, в пределах параметров согласия (сумма ≤ лимит, кумулятив ≤ максимум, назначение совпадает), и каждое списание — это платёж, зачисляемый только из PAID (AD-005). Отзыв согласия немедленно блокирует новые списания. Fitness: тест «списание при REVOKED/EXPIRED/превышении лимита → отказ 4xx, платежа не создаётся».
- **AD-010. Согласие плательщика — доказуемая запись с неизменяемым аудитом.**
  Binds: сервис подписок, аудит-лог, ПДн-контур, сверка с НСПК.
  Prevents: недоказуемость согласия при споре/проверке ЦБ; хранение избыточных ПДн плательщика; расхождение «банк считает ACTIVE, НСПК — нет».
  Rule: Факт, параметры и отзыв согласия фиксируются в неизменяемом аудит-логе; ПДн плательщика минимизируются (хранится идентификатор/референс согласия, не полные реквизиты); статус согласия сверяется с НСПК (как минимум ежедневно). Fitness: наличие записи аудита на каждое изменение согласия; тест минимизации ПДн (скан полей).

Hmm — but adding two AD blocks extends the spine to 10 blocks — within norm 5-15. Good.

### Alternatives (for ADR-008)
Decision to record: "Рекуррентные C2B-списания реализуются как платежи, инициируемые против первоклассного агрегата «согласие плательщика», с хранением согласия в шлюзе и сверкой с НСПК."

Alternatives:
1. **Согласие как атрибут платежа** (храним mandate-токен в платеже, без отдельной сущности) — минусы: нет единого источника истины для лимитов/отзыва, невозможно доказать согласие, нельзя атомарно заблокировать списания при отзыве. Rejected.
2. **Согласие только на стороне НСПК/ОПКЦ (банк без своей модели)** — минусы: нарушает RPO=0/AD-002 (нет локального источника истины), зависимость каждого списания от доступности НСПК, невозможно офлайн-блокировать/аудировать. Rejected.
3. **Вендорский модуль подписок «коробка»** — минусы: финансовая логика и лимиты вне контроля банка, vendor lock-in, сложный аудит, противоречит ADR-007 (ядро — собственная разработка). Rejected.
4. **Инициирование списаний планировщиком шлюза (pull) vs ТСП-инициируемые (push)** — this is a sub-decision; present both, recommend ТСП-инициируемые с опциональным планировщиком; mark as open (business/НСПК rules).
Chosen: first-class mandate aggregate in gateway + ТСП-инициируемые списания (gateway validates against mandate), сверка с НСПК.

Reversibility: **costly** — once recurring debits are live and ТСП integrate, changing the consent model (e.g., to vendor) requires data migration of consents and re-consent of payers (regulatory/UX impact). But before go-live — reversible. So: reversible до боевой эксплуатации; costly после (переоформление согласий).

Expiry: пересмотр при (а) получении документации НСПК/регламента по автоплатежам, если протокол диктует иную модель согласия; (б) изменении требований ЦБ к согласиям/уведомлениям; плановая ревизия 12 мес.

### Contract changes (openapi/tsp-api.yaml)
Must be additive (no breaking changes). New paths:
- `POST /v1/subscriptions` — create mandate (Idempotency-Key required) → 201 {subscriptionId, status, consentUrl, expiresAt}
- `GET /v1/subscriptions/{subscriptionId}` — status
- `POST /v1/subscriptions/{subscriptionId}/charges` — initiate charge (Idempotency-Key) → 201 {chargeId (=paymentId), status}
- `POST /v1/subscriptions/{subscriptionId}/revoke` — revoke (or DELETE) 
- Maybe `GET /v1/subscriptions/{subscriptionId}/charges` list.
New schemas: Subscription, SubscriptionRequest, SubscriptionStatus enum (INITIATED/PENDING_PAYER/ACTIVE/SUSPENDED/REVOKED/EXPIRED/REJECTED), ChargeRequest, MandateParameters (amountLimitPerCharge, totalLimit, period, purpose).
New webhook events: `subscription.activated`, `subscription.revoked`, `charge.completed` (or reuse payment.completed with subscriptionId).
Additive: adding an optional `subscriptionId` field to Payment and PaymentRequest; new optional `chargeType`.
Errors: new codes `SUBSCRIPTION_NOT_ACTIVE` (409/422), `SUBSCRIPTION_LIMIT_EXCEEDED` (422), `SUBSCRIPTION_REVOKED` (409).
Bump version 0.1.0 → 0.2.0 (minor, additive). Since contract is draft pre-A1, no consumer breakage; run openapi_lint + contract_diff to prove no breaking changes (compare old vs new file — I'll keep a copy of old).

Note openapi_lint checks idempotency on mutating endpoints and RFC7807 errors; I must ensure new POSTs have Idempotency-Key param. And responses include problem+json for errors? The lint (T1) may require error responses defined with RFC7807. The current file has no error responses and lint passed? Let me check `openapi_lint` on the current file to see baseline findings, then design to not add errors.

Let me run openapi_lint now on the current file.

### NFR (new, measurable)
- Активация согласия (mandate ACTIVE) after payer confirmation: p95 ≤ 30 s from payer action (excluding НСПК).
- Charge initiation latency (ТСП → 202/201): p95 ≤ 500 ms (without НСПК time).
- Отзыв согласия: блокировка новых списаний ≤ 60 s от события НСПК; сквозное распространение (до отказа списаний) ≤ 5 мин.
- Двойные списания за период: 0 (идемпотентность + лимиты).
- Charge success/credit: p95 ≤ 60 s (same as credit SLA).
- Availability: mandate service ≥ 99,95%; при недоступности НСПК новые списания не создаются (fail-closed), приём платежей не деградирует.
- Reconciliation: mandate status сверка с НСПК ≥ ежедневно; расхождений по активным согласиям = 0.
- Лимиты: refuse charge over limit — 100%.
- Audit: 100% mandate transitions in immutable log.
- ПДн: 0 полных PAN/реквизитов плательщика в шлюзе (only reference).

### Acceptance criteria (testable)
- A charge without ACTIVE mandate → rejected, no payment created, error code.
- Charge exceeding per-charge/total limit → rejected.
- Revoke then charge → rejected; in-flight PAID charge completes.
- Duplicate charge request (same Idempotency-Key) → same chargeId, no double.
- Duplicate consent event (same eventId) → idempotent.
- Consenting flow: consent activation event → mandate ACTIVE, audit record, webhook.
- Credit only from PAID for charge (fitness).
- Contract: contract_diff old→new has no breaking changes; openapi_lint passes.
- Rollback rehearsal.

### Rollback plan
- Before go-live: don't enable (feature-flag `subscriptions_enabled` off by default); all changes additive.
- After go-live: feature flag stop-new-charges (block new charges; active mandates preserved); existing charges continue; mandates can be revoked normally; revert release rolling; no data migration back (mandates remain readable/revocable); notification of ТСП about停.
- Trigger signals: double charge, unauthorized charge, revocation not blocking, reconciliation discrepancy.
- Owner: solution architect / платёжный контур owner; decision by A3.

### What remains for human architect (A3)
- Choice between ТСП-инициируемые vs gateway-scheduled charges (and whether pre-notification of payer is mandatory) — depends on НСПК regulation.
- Maximum limits & consent TTL (per НСПК rules).
- Whether consent is stored as reference only vs full evidence (ПДн vs provability) — ИБ/юридическое.
- The mandate model itself (ADR-008) must be signed A3 (choice ≠ agent).
- Whether revocation must also cancel scheduled charges and how to handle in-flight (business/regulator).
- Approval of new spine invariants AD-009/AD-010 (spine change requires A3? The spine is accepted; changing it via delta needs architect sign-off).
- Vendor contract change (new adapter methods) — RFP scope.
- Route sign-off.

Now, files to create/modify:

1. `changes/sbp-recurring-subscriptions/DELTA.md` (fill) — change record, Delta ADDED/MODIFIED, rollback, acceptance, mentions protected files.
2. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-soglasie-platelshchika.md` — ADR.
3. `docs/solutioning-subscriptions.md` — impact/design (deliverable 2 + parts).
   Hmm, but sensors scan docs/spec only (gate). docs/solutioning-subscriptions.md is in docs/ root, not scanned by gate. Good.
4. `docs/spec/subscriptions.md` — mandate state machine spec (must include ## Проблема, ## Критерии приёмки, ## Риски).
5. `docs/spec/state-machine.md` — add required sections (## Проблема, ## Критерии приёмки, ## Риски) — fix sensor. Also add mandate-related transitions? Better keep separate; just add required sections with meaningful content.
6. `docs/nfr.md` — add subscription NFR rows (and required sections? docs/nfr.md is not in docs/spec, so gate doesn't scan; no need).
7. `docs/contracts/tsp-api.md` — document new endpoints (optional; the openapi yaml is the contract). I'll update it to reflect v0.2 additions.
8. `openapi/tsp-api.yaml` — add paths/schemas additively (deliverable 4).
9. `ARCHITECTURE-SPINE.md` — add AD-009, AD-010 (via delta). Also maybe add note in Deferred that "автоплатежи" moves from Deferred to scope. Note: docs/solutioning.md §1 says roadmap (вне scope): ... автоплатежи. So this change moves autopayments into scope. I should update that mention? It's in docs/solutioning.md; not protected; but it's "принятое решение". I can update it or note the change in delta. I'll add a MODIFIED entry and update solutioning.md's roadmap line. Hmm, careful: modifying accepted docs is allowed if not protected, but should be done via delta discipline. I'll mention in DELTA MODIFIED.
10. `.arch-handoff/CONSTRAINTS.yaml` — add new fitness rules (via delta). But wait: rule_weakened checks registry not weakened; adding rules is fine. Also rule_weakened compares to baseline; adding rules with owner/expiry? The rules_report checks owner/expiry. Adding minimal rules. Let me check the CONSTRAINTS schema for rule fields (name, type, glob/path/pattern, severity, owner, expiry?). I'll add:
    - `subscription-charge-requires-active-mandate` (must_contain in ADR-008? or a spec) — hmm, these text rules are weak. Better use must_contain on docs to assert invariants text.
    - Maybe `nfr-subscriptions-measurable` must_contain docs/nfr.md pattern for revocation.
    Let me look at fitness-function-catalog / rules_suggest to craft meaningful rules. Actually `arch-be rules suggest` gives candidates. Let me run `rules_suggest` on the repo to get candidates and apply the relevant ones.
    But careful: any `command_succeeds` rule would execute commands (risky) and might fail. I'll add only must_contain/file_exists rules with owner/expiry.

11. Handoff package for executors: create `changes/sbp-recurring-subscriptions/handoff/` with TASK.md, ARCHITECTURE.md (epic-context), CONSTRAINTS.yaml (copy), RUBRIC.yaml, MANIFEST.json, adr/ (ADR-008). Or update `.arch-handoff/`. Let me think: `.arch-handoff` is the existing package (walking skeleton). The new increment should get its own package so as not to clobber. The `handoff` CLI writes to `.arch-handoff`. The `delta_guard` protects model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml — but `.arch-handoff/CONSTRAINTS.yaml`? The protect list is "model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml" — the guard default shows "CONSTRAINTS.yaml" which likely matches any CONSTRAINTS.yaml path (suffix match). The baseline gate delta_guard said "изменённых файлов: 1, защищённых среди них: 0" and the 1 changed file was .qwen/settings.json. The handoff CLI `--refresh-constraints` mentions "правки архитектора в пакете сохраняются". 

Hmm, to avoid delta_guard complications, my DELTA.md will mention both `ARCHITECTURE-SPINE.md` and `CONSTRAINTS.yaml` and `.arch-handoff/CONSTRAINTS.yaml`. But if the handoff package generates its own CONSTRAINTS.yaml at `.arch-handoff/CONSTRAINTS.yaml`, delta_guard might flag it. Since my delta mentions "CONSTRAINTS.yaml", it should be covered (mention is likely substring match). Let me test delta guard after changes.

Actually, simpler: I'll update `.arch-handoff/` in place (it IS the handoff package destination) — regenerate via `arch-be handoff qwen-code --repo . --task ... --spec ... --route critical`. But that might overwrite TASK.md/ARCHITECTURE.md and CONSTRAINTS.yaml (with --refresh-constraints). Risk: it may pull in defaults and lose customizations. Alternatively, create a separate handoff dir for the increment. The `handoff` CLI likely always writes `.arch-handoff`. Let me check by reading its behavior — no docs. Hmm.

Given the risk, I'll hand-craft the handoff package for the increment under `.arch-handoff/` (update TASK.md to include the new epic? No — that breaks the existing walking skeleton task). Better: create `changes/sbp-recurring-subscriptions/handoff/` with the 5 files. This keeps it self-contained and reviewable, consistent with "передать исполнителям". And mention it in the delta/ADR.

Actually, let me reconsider: maybe update `.arch-handoff/TASK.md` by appending an "Этап 2" section, since it's the repo's handoff package. But the MANIFEST/token budget... The handoff-packaging skill says epic-context 800–1500 tokens. Adding a second epic would double it. A separate package is cleaner.

Decision: create `changes/sbp-recurring-subscriptions/handoff/` with TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, adr/ADR-008 copy. This is the handoff for executors. Also mention in `.arch-handoff/TASK.md`? No, leave the accepted package untouched (avoid modifying accepted files unnecessarily). Hmm, but "Принятые файлы решения меняй только тем способом, который принят" — I won't touch .arch-handoff except via delta if needed.

Wait — actually, if I don't touch .arch-handoff, delta_guard only cares about ARCHITECTURE-SPINE.md (protected) and CONSTRAINTS.yaml. If I add rules to `.arch-handoff/CONSTRAINTS.yaml`, that's the live registry used by fitness. Adding rules there is the accepted way (rules live in CONSTRAINTS.yaml). And delta must mention it. Fine.

Hmm, but do I even need to modify CONSTRAINTS.yaml? The task doesn't require new fitness rules explicitly, but "используй инструменты по назначению" and "передать исполнителям" imply fitness rules for the new invariants. Adding them strengthens the package. I'll add 2-3 rules targeting the new ADR/spec (must_contain), each with owner/expiry to pass rules_report checks. Let me check rules_report current findings to match style.

Let me now run: openapi_lint on current, rules suggest, rules report. And check CONSTRAINTS schema (full field set) — current file has name/type/glob/pattern/severity only. rules_report mentions owner, expiry, exclude_glob, effort_hours — optional. Let me check rules_report output for findings; if I add rules without owner → warn findings, could cause fitness warn (not error) → gate fitness PASS (0 error). The baseline fitness PASS had 0 warn too. If I add rules without owner, warn appears → gate still PASS (warn allowed?). The gate PASS line showed "(error: 0, warn: 0)". If warn>0, does fitness FAIL? Probably not (only error fails). But to be clean, add owner/expiry.

Let me run the introspection commands.

Let me batch: openapi_lint (MCP), rules suggest, rules report, delta validate current.

Actually openapi_lint is MCP deferred; I need tool_call. Let me use tool_call for mcp__spine__openapi_lint. And CLI for rules.

Let me do it.
Оцениваю контрактный линт, кандидатные правила и реестр правил — чтобы новые правила и контракт встали без регрессий.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/skills/readiness-gate/SKILL.md)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/skills/fitness-functions/SKILL)`
  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.qwen/skills/adr-authoring/reference)`

Good. The rules all lack owner/expiry (pre-existing warns). I'll add my new rules WITH owner/expiry to be exemplary. And I can add the ears_acceptance_criteria rule (severity warn) since I'll write EARS acceptance criteria — this will pass.

Note: rules_suggest recommends EARS criteria — I'll write acceptance criteria in EARS form in the delta and spec.

Now let me get the delta validate guard semantics. Let me test delta guard now (with only untracked delta + modified settings).

Actually let me just proceed to write. But before writing a lot, let me test delta_guard mention behavior with a quick experiment: create a temp change to a protected file? No, don't want to dirty the spine. Instead, let me read the guard's matching by testing: I'll write DELTA.md mentioning ARCHITECTURE-SPINE.md, then modify ARCHITECTURE-SPINE.md, then run `arch-be delta guard --base bench-baseline` (or with git add -N). Let me just do it for real as part of implementation.

Let me now also check readiness-gate and adversarial-review and fitness-functions skills briefly — they inform acceptance criteria, review, and rules. Also docx-solution-design? The task doesn't ask for docx; it asks for an architectural package. Markdown files are the repo convention. I won't produce docx (not requested, and repo uses md). Actually deliverable "архитектурный пакет ... вынести на архитектурное решение" — the repo convention is md docs + ADR. Good.

Let me read readiness-gate and fitness-functions quickly.

Actually, to conserve effort, I have enough. Let me read readiness-gate (for EARS/acceptance format) and fitness-functions (rule schema) — short.

Let me read them + the ADR template.

  `write_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/adr/ADR-008-rekurrentnye-c2b-sp, content="# ADR-008. Рекуррентные C2B-списания СБП: согласие плательщика как первоклассная сущность\n\n- Date: 2026-09-28\n- Status: Proposed (ожидае)`

I now have everything I need. Let me write the deliverables.

Let me define the exact file list:

Protected (via delta):
1. `ARCHITECTURE-SPINE.md` — add AD-009, AD-010; update Deferred (автоплатежи → в scope; add deferred for "gateway-scheduled auto-charges"? Actually keep). Also add reference to new spec/ADR.
2. `.arch-handoff/CONSTRAINTS.yaml` — add rules.

Delta:
3. `changes/sbp-recurring-subscriptions/DELTA.md`

New docs:
4. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`
5. `docs/solutioning-subscriptions.md` (impact + design; deliverable 2, 3, 5, 6 partly)
6. `docs/spec/subscriptions.md` (mandate state machine + required sections)
7. `docs/spec/state-machine.md` — add required sections (fix sensor)
8. `docs/nfr.md` — add subscription NFR table
9. `docs/contracts/tsp-api.md` — add §8 subscription endpoints
10. `openapi/tsp-api.yaml` — add paths/schemas (v0.2.0)
11. `.arch-handoff/...` — do NOT touch? Or update handoff. I'll create the increment handoff package:
    `changes/sbp-recurring-subscriptions/handoff/TASK.md`
    `changes/sbp-recurring-subscriptions/handoff/ARCHITECTURE.md`
    `changes/sbp-recurring-subscriptions/handoff/CONSTRAINTS.yaml`
    `changes/sbp-recurring-subscriptions/handoff/RUBRIC.yaml`
    `changes/sbp-recurring-subscriptions/handoff/MANIFEST.json`
    `changes/sbp-recurring-subscriptions/handoff/adr/ADR-008...md` (copy)

Hmm, wait: if handoff/CONSTRAINTS.yaml is a copy, delta_guard "CONSTRAINTS.yaml" match would require it mentioned in delta. My delta will mention CONSTRAINTS.yaml generically — likely covered. But to be safe, mention the specific paths too. Actually, mentioning the substring "CONSTRAINTS.yaml" may cover both. Let me test.

Also, adding a `changes/.../handoff/CONSTRAINTS.yaml` — does the fitness check scan all CONSTRAINTS.yaml? No, fitness uses `.arch-handoff/CONSTRAINTS.yaml` explicitly (rule fingerprint 72d0bf4f — file .arch-handoff/CONSTRAINTS.yaml). Good. But delta_guard protect "CONSTRAINTS.yaml" — untracked new file; with `git add -A -N` it's in diff. If delta mentions it, fine.

Hmm, but the handoff package copy of CONSTRAINTS.yaml might conflict with rule_weakened? rule_weakened compares the registry `.arch-handoff/CONSTRAINTS.yaml` to baseline. My addition of rules strengthens, not weakens. Fine.

Also, an important consideration: the delta `changes/sbp-recurring-subscriptions/DELTA.md` mentions protected files; but delta_guard requires the *changed* protected files to be mentioned. If I mention ARCHITECTURE-SPINE.md and CONSTRAINTS.yaml, and I only change ARCHITECTURE-SPINE.md and .arch-handoff/CONSTRAINTS.yaml, the mention "CONSTRAINTS.yaml" should match the latter (substring) and "ARCHITECTURE-SPINE.md" match the former. Good.

Let me write the arch spine additions. I need to keep Binds/Prevents/Rule non-empty and machine-checkable Rule.

AD-009:
## AD-009. Рекуррентное списание — только по действующему согласию плательщика
- Status: Proposed (ADR-008)
- Binds: сервис согласий (mandate), статусная машина платежа, адаптер ОПКЦ, АБС-адаптер, аудит-лог.
- Prevents: списание без согласия или вне его параметров (получатель, лимит на списание, суммарный лимит, период); списание по отозванному/истёкшему согласию; «тихое» безакцептное списание без доказуемого согласия.
- Rule: Инициировать списание можно только при согласии в состоянии `ACTIVE` и в пределах его параметров; каждое списание — это платёж, зачисляемый только из `PAID` (AD-005); отзыв согласия немедленно (см. NFR) запрещает новые списания. Fitness: тест «списание при `REVOKED`/`EXPIRED`/превышении лимита → отказ, платёж не создаётся»; правило CONSTRAINTS.yaml `subscription-charge-requires-active-mandate`.

AD-010:
## AD-010. Согласие плательщика — доказуемая запись с неизменяемым аудитом
- Status: Proposed (ADR-008)
- Binds: сервис согласий, аудит-лог, контур ПДн, сверка с НСПК.
- Prevents: недоказуемость согласия при споре/проверке; хранение избыточных ПДн плательщика; расхождение «у банка согласие `ACTIVE`, у НСПК — нет».
- Rule: Создание, изменение параметров и отзыв согласия фиксируются в неизменяемом аудит-логе; ПДн плательщика минимизируются (хранится референс/идентификатор согласия, не полные реквизиты); состояние согласия сверяется с НСПК не реже ежедневно. Fitness: правило `mandate-audit-and-pdn-minimal`.

Update Deferred: remove "автоплатежи" from roadmap deferred (since now in scope), add note. Actually docs/solutioning.md says roadmap (вне scope): ... автоплатежи. And spine Deferred lists мультивалютность, C2C, диспуты — not автоплатежи. So spine Deferred doesn't mention autopayments. Only solutioning.md does. I'll add a MODIFIED entry in DELTA and update solutioning.md roadmap line.

Should I add a Deferred entry for "gateway-side scheduler (автоплатежи по расписанию)": deferred with reason. Hmm — the decision recommends ТСП-initiated charges; gateway-scheduler deferred. I'll add to spine Deferred: "Планировщик списаний на стороне шлюза (автоплатежи по расписанию): вне scope первой волны; вернуть при требовании бизнеса/регламента; реализуется поверх AD-009 без смены модели согласия." That's good and honest.

Now the OpenAPI additions. Let me design carefully to pass openapi_lint (idempotency on mutating endpoints, error RFC7807). Current file passes with no error responses. I'll mirror the existing style (no explicit error responses) to keep lint passing. Actually the lint (T1) checks idempotency for mutating endpoints — I must include `Idempotency-Key` header param on POST. Let me include it on all POSTs.

New paths:
- `/v1/subscriptions` POST createSubscription
- `/v1/subscriptions/{subscriptionId}` GET getSubscription
- `/v1/subscriptions/{subscriptionId}/charges` POST createSubscriptionCharge (+ GET list? optional)
- `/v1/subscriptions/{subscriptionId}/revoke` POST revokeSubscription

Schemas:
- SubscriptionRequest: {amountLimitPerCharge (int, optional), totalLimit (int, optional), currency, period, paymentPurpose, payerRef (string), merchantOrderId?, webhookUrl?}
  Required: [paymentPurpose] maybe. Keep minimal: required [paymentPurpose].
- Subscription: {subscriptionId, status, amountLimitPerCharge, totalLimit, currency, period, purpose, createdAt, activatedAt?, expiresAt?, revokedAt?, consentUrl?}
  status enum: [INITIATED, PENDING_PAYER, ACTIVE, SUSPENDED, REVOKED, EXPIRED, REJECTED]
- SubscriptionChargeRequest: {amount (int), chargeId?/merchantOrderId?, paymentPurpose?}
  Required [amount].
- SubscriptionCharge: {chargeId, paymentId, amount, status, createdAt}
- Payment: add optional `subscriptionId`.

Additive only. Version 0.1.0 → 0.2.0.

Now, the delta ADDED requirements in EARS form. And acceptance criteria EARS.

Let me also create the impact/design doc `docs/solutioning-subscriptions.md` with:
- Маршрут и значимость (score 9, Critical, triggers list)
- Влияние на принятую архитектуру (per AD-*: затронут/не затронут, что меняется/нет)
- Компоненты и потоки (mermaid: consent flow, charge flow, revoke)
- Варианты и выбранное решение (summary)
- Изменения контрактов (link)
- NFR (link)
- Критерии приёмки (EARS)
- План отката
- Что остаётся на решение человека (A3)
- Gaps/внешние входы

Actually deliverables 1,2,5,6,7 all naturally live in one "пакет изменения" doc. Let me structure `docs/solutioning-subscriptions.md` to cover 1,2,3(summary),5,6,7; ADR-008 covers 3 fully; openapi covers 4; delta covers change record.

Let me also add a top-level `changes/sbp-recurring-subscriptions/README.md`? Not necessary; DELTA.md is the index.

Let me write files now. I'll start with the ADR (most important), then solutioning, spec, spine, constraints, openapi, nfr, contracts, delta, handoff.

Let me be careful about the "Принятые файлы решения меняй только тем способом, который принят" — I'm using delta for protected files (ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml). For non-protected accepted docs (solutioning.md, nfr.md, state-machine.md, tsp-api.md, openapi), direct edits are allowed by the mechanism, but I should be transparent. I'll record MODIFIED entries in DELTA for state-machine.md and solutioning.md. Fine.

Wait — is openapi/tsp-api.yaml protected? protect default: model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. Not openapi. OK.

Now let me write. First, ADR-008.

I need a date: today is 2026-09-28. ADR date 2026-09-28. Status: Proposed (human A3 to sign). Owner: solution-architect.

Let me write ADR-008 content.

Also include `- Модель-автор: <model>`? The adr-authoring says header may include author-model. The decision_quality judge reads it. Since I (Qwen) authored, I could add `- Модель-автор: qwen3-max`? Hmm, I shouldn't guess a model name. I'll add `- Author-model: qwen-code` ... Actually the field is optional; but for A3/rubric it's useful. The existing ADRs don't have it. To match convention, I'll omit it (existing ADRs omit it). Actually the skill says write `human` or model label. But existing ADRs (baseline) don't include it, and decision_quality isn't enabled. I'll omit to match the repo's established ADR form. Hmm, but "Conflicts with prior decisions" — matching convention is safer. Omit.

Let me write ADR-008.

Then the rest.

Let me draft ADR-008:

# ADR-008. Рекуррентные C2B-списания СБП: согласие плательщика как первоклассная сущность

- Date: 2026-09-28
- Status: Proposed (ожидает человеческого решения A3)
- Owner: solution-architect (платёжный контур) + владелец продукта «Эквайринг»
- Related: ADR-001, ADR-002, ADR-003, ADR-004, ADR-005, ADR-006, AD-001..AD-010

## Context
... business need, forces: recurring without QR, payer consent must be provable, НСПК rules external input, regulation (161-ФЗ, 152-ФЗ), ПДн, КИИ. Existing solution: payment requires QR & client action; AD-005 requires PAID for credit. Recurring means debits initiated server-side. Risks: unauthorized debit, revocation race, double charge, consent proof, ПДн.

## Decision
Согласие плательщика (mandate) — первоклассная сущность со своей статусной машиной в БД шлюза; рекуррентное списание — обычный платёж, инициируемый сервисом шлюза против активного согласия и доводимый по той же модели (AD-002/AD-005). Согласие создаётся/активируется/отзывается через адаптер ОПКЦ; факт и параметры согласия аудируются; ПДн минимизируются; состояние согласия сверяется с НСПК.

## Alternatives Considered (table with why rejected)
1. Согласие как атрибут платежа (mandate-токен в теле платежа) ...
2. Согласие только на стороне НСПК (банк stateless) ...
3. Вендорский модуль подписок ...
4. Шлюз-планировщик списаний (pull) как основная модель ...
Chosen #? — first-class + ТСП-инициируемые; scheduler deferred.

Actually alternatives should include the chosen one? Convention: "Alternatives Considered" = rejected ones; Decision states chosen. The existing ADRs list rejected options only. I'll list rejected options (4) and state chosen in Decision. But the skill says table variant/plus/minus/why rejected — includes chosen? Existing ADR-001 table lists only alternatives. I'll follow: list alternatives with "почему отвергнут", and chosen described in Decision.

Hmm, but for the "ТСП-initiated vs gateway-scheduled" — the gateway-scheduler could be a rejected alternative for the first wave (deferred). Good.

## Consequences: Positive / Negative.

## Reversibility: reversible до боевой эксплуатации; costly после (переоформление согласий, миграция) — обоснование. Expiry: пересмотр при получении документации НСПК/регламента по автоплатежам; плановая ревизия 12 мес.

## References.

Let me write it.

Now the solutioning-subscriptions doc. Include significance triggers and route.

Let me write everything now. I'll write files with write_file.

Let me start.

One more: the sensor requires exact sections "## Проблема", "## Критерии приёмки", "## Риски" in docs/spec/*.md. I'll ensure both docs/spec/state-machine.md and docs/spec/subscriptions.md contain those headings exactly.

Let me write docs/spec/state-machine.md additions: I'll append sections at the end. Need to read current file end to append. It ends with section 6. I'll append:

## Проблема
<why the state machine / what problem it solves — the change context>

## Критерии приёмки
EARS bullets.

## Риски
table.

But wait — this is the seller's spec of the existing state machine; adding "Проблема/Критерии приёмки/Риски" is a template requirement. I'll write them meaningfully and also include the mandate section? Better: reference docs/spec/subscriptions.md for the mandate machine.

Now let me write. Start with ADR-008.

Let me also decide the mandate state machine detail to put in docs/spec/subscriptions.md:
States: INITIATED (создано в шлюзе, запрос в ОПКЦ), PENDING_PAYER (ожидает подтверждения плательщика), ACTIVE, SUSPENDED (приостановлено, напр. по требованию), REVOKED (отозвано плательщиком/банком), EXPIRED (истёк срок/лимит), REJECTED (отклонено ОПКЦ/банком плательщика). Terminal: REVOKED, EXPIRED, REJECTED. (SUSPENDED non-terminal.)
Transitions table:
M1 — → INITIATED (POST /subscriptions) 
M2 INITIATED → PENDING_PAYER (адаптер вернул consentUrl/согласие зарегистрировано)
M3 INITIATED → REJECTED (ошибка регистрации)
M4 PENDING_PAYER → ACTIVE (событие consent.activated / сверка)
M5 PENDING_PAYER → REJECTED (событие consent.rejected)
M6 PENDING_PAYER → EXPIRED (TTL ожидания подтверждения)
M7 ACTIVE → SUSPENDED (запрос ТСП/банка, не НСПК-терминал)
M8 SUSPENDED → ACTIVE (возобновление)
M9 ACTIVE → REVOKED (событие consent.revoked / требование плательщика)
M10 SUSPENDED → REVOKED
M11 ACTIVE → EXPIRED (истёк срок согласия)
Forbidden: charges from non-ACTIVE; REVOKED/EXPIRED/REJECTED terminal; ACTIVE cannot go to PENDING_PAYER.
Idempotency: create by Idempotency-Key; events by eventId; revoke by reference.
Reconciliation: daily status sync.

Also link charges: each charge references mandateId; charge blocked unless ACTIVE.

Good.

Now NFR additions (docs/nfr.md). Add a section "## 7. Рекуррентные списания (подписки)" with table. But docs/nfr.md is not sensor-scanned (only docs/spec). Fine. But note: `docs/nfr.md` is referenced in CONSTRAINTS rule `nfr-measurable` pattern '99,95' — keep it.

Add NFR rows:
- Активация согласия (PENDING_PAYER→ACTIVE) после действия плательщика: p95 ≤ 30 с (без учёта НСПК).
- Инициирование списания (API ТСП → принято): p95 ≤ 500 мс.
- Блокировка новых списаний после отзыва: ≤ 60 с от события НСПК; сквозное ≤ 5 мин.
- Двойные списания за период: 0.
- Зачисление по списанию: p95 ≤ 60 с (как §2).
- Сверка статусов согласий с НСПК: ежедневно; расхождений по активным = 0.
- Отказ при превышении лимитов: 100 %.
- Аудит переходов согласия: 100 %.
- ПДн: 0 полных реквизитов плательщика в шлюзе.
- Доступность сервиса согласий ≥ 99,95 %.

Also add to nfr §5/§6? Keep a new section.

Now CONSTRAINTS additions. Current rules 7. Add:
  - name: subscription-charge-requires-active-mandate
    type: must_contain
    glob: "docs/adr/ADR-008-*.md"
    pattern: 'только при согласии в состоянии `ACTIVE`'
    severity: error
    owner: solution-architect
    expiry: 2027-09-28
    rationale: 'AD-009: списание только по активному согласию'
    fix_hint: 'вернуть формулировку инварианта AD-009 в ADR-008'
  - name: mandate-audit-and-pdn-minimal
    type: must_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'неизменяемом аудит-логе'
    severity: error
    owner: solution-architect
    expiry: 2027-09-28
  - name: nfr-subscription-revocation-measurable
    type: must_contain
    glob: "docs/nfr.md"
    pattern: 'Блокировка новых списаний после отзыва'
    severity: error
    owner: solution-architect
    expiry: 2027-09-28
  - name: ears_acceptance_criteria
    type: must_contain
    glob: 'docs/**/*.md'
    pattern: '(?m)^\s*[-*]?\s*\**\s*(When|While|If|Where)\b'
    severity: warn
    owner: solution-architect
    expiry: 2027-09-28
    rationale: 'критерии приёмки без EARS-формы непроверяемы формально'

Wait: glob "docs/**/*.md" — must_contain matches at least one file. `(?m)^...` with the pattern. My EARS criteria must literally start lines with When/While/If/Where. I'll ensure the delta and specs have EARS lines. But note the delta-spec skill example uses English "When ... the ... shall". EARS keywords are English. I'll write criteria like:
- When плательщик отзывает согласие, the шлюз shall прекратить приём новых списаний по этому согласию.
Hmm, mixing English/Russian. The regex `(When|While|If|Where)\b` — English keywords. I'll use "When"/"If" at line start (after bullet). Let me format:
`- When ТСП запрашивает списание по согласию не в состоянии ACTIVE, the шлюз shall отклонить запрос...`
Good.

But careful: must_contain glob `docs/**/*.md` and pattern multiline with `(?m)`. The docs/spec files are under docs/spec, matched by docs/**/*.md. Good.

However there's a subtlety: the `fitness_check` must_contain scans whole file content; `(?m)` anchor start-of-line. My line begins with "- When ..." → `^\s*[-*]?\s*\**\s*(When...)`. "- When" matches. Good.

Now, also I might add a `file_exists` rule for the new spec? Not necessary.

Let me be careful not to break rule_weakened: adding rules is fine (it checks weakening of existing rules? "реестр правил не ослаблен" — removing/loosening). Adding is strengthening.

Now the handoff package. Let me create `changes/sbp-recurring-subscriptions/handoff/`:
- TASK.md
- ARCHITECTURE.md (epic-context ~1200 tokens)
- CONSTRAINTS.yaml (copy of updated .arch-handoff/CONSTRAINTS.yaml)
- RUBRIC.yaml (copy of .arch-handoff/RUBRIC.yaml)
- MANIFEST.json
- adr/ADR-008...md (copy)

Hmm, wait: copying ADR-008 into the handoff dir means delta_guard? No, ADR-008 is not protected. But the copy path under changes/... fine.

Actually, should the handoff be a separate `handoff/` under changes, or should I use the `arch-be handoff` CLI into `.arch-handoff`? Let me try the CLI to see if it works and what it writes; if it's clean, use it against a separate dir? It writes to `<repo>/.arch-handoff` presumably. I don't want to clobber. So I'll hand-craft. That's fine and matches handoff-packaging skill content (TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, adr/, MANIFEST.json).

Let me now write all files. This is a lot of content; let me be thorough but efficient.

Let me write ADR-008 first.

Actually, let me reconsider deliverable 3 wording: "Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью." ADR-008 covers it. Good.

Let me write.

For date format in ADR header: existing use `- Date: 2026-08-15`. I'll use same.

Let me write ADR-008 file.

Note the ADR file name convention: `ADR-008-<translit-slug>.md`. Existing: `ADR-005-integraciya-s-abs-zachislenie-po-podtverzhdyonnomu-statusu-vozvraty-kak-saga.md`. I'll name `ADR-008-rekurrentnye-c2b-spisaniya-soglasie-platelshchika.md`.

Let me write.
Материала достаточно. Приступаю к пакету: сначала ADR-008 (ядро решения).

  `write_file(content="# Solutioning изменения: рекуррентные C2B-списания СБП (подписки)\n\n- Status: Proposed (готовится к архитектурному решению A3)\n- Date: 20, file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/solutioning-subscriptions.md")`

Now the solutioning-subscriptions.md (impact + significance + design). Let me write it.
Теперь дизайн изменения: значимость, влияние на принятую архитектуру, потоки, NFR, приёмка, откат, вопросы к человеку.

  `write_file(content="# Согласие плательщика (подписка) — статусная машина\n\n- Status: Draft (для ревью на гейте A1; ожидает A3 по ADR-008)\n- Owner: solution-a, file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/spec/subscriptions.md")`

Now docs/spec/subscriptions.md — mandate state machine, with required sections. And docs/spec/state-machine.md need appended sections.

Let me write docs/spec/subscriptions.md.
Пишу спецификацию статусной машины согласия (с обязательными секциями сенсора).

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/spec/state-machine.md", old_string="## 6. Согласованность с API ТСП\n\nМаппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED, new_string="## 6. Согласованность с API ТСП\n\nМаппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED)`

Now append required sections to docs/spec/state-machine.md. I'll add a section 7 with ## Проблема, ## Критерии приёмки, ## Риски. But the file is the payment state machine; it already has content. I need to append at the end. Let me use edit with the last lines as context.

The file ends with:
```
## 6. Согласованность с API ТСП

Маппинг статусов наружу (TSP API §3.3): ... (`ABS_PENDING`, `NOTIFY_PENDING` наружу не выставляются; `ABS_PENDING` отражается как `PAID` + поле `creditingStatus`).
```

I'll append after that. Let me do an edit replacing the last paragraph with itself + new sections. Need exact text. Let me use the edit tool with the final line as anchor.

Actually, simpler and safe: read the tail to get exact text, then edit. I already have the content from earlier read. The last line is:

"Маппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `EXPIRED`, `REFUNDED` — без технических подсостояний (`ABS_PENDING`, `NOTIFY_PENDING` наружу не выставляются; `ABS_PENDING` отражается как `PAID` + поле `creditingStatus`)."

I'll append. But also I want to add mandate-charge linkage notes referencing subscriptions. I'll add a section 7 noting recurring charge uses the same machine, plus required sections.

Let me edit.
Дополняю спецификацию статусной машины платежа обязательными секциями сенсора и связью со списанием по согласию.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

I need to continue. I was about to edit ARCHITECTURE-SPINE.md to add AD-009, AD-010 and adjust Deferred. Let me do that now.

Note: previous suffix ended with the sentence about spine. So I must not repeat that line. I'll just proceed with the edits.

Let me edit ARCHITECTURE-SPINE.md. Add AD-009/AD-010 after AD-008 block, before the "---" and Deferred section. And update Deferred to move autopayments into scope and add gateway scheduler deferred. Also update the intro maybe.

Let me construct the edit. The current text around AD-008 end:

```
## AD-008. Стратегия реализации — гибрид [ADOPTED]
...
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта ... Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)

- **Мультивалютность и иностранные платёжные системы**: ...
- **C2C-переводы и выплаты B2C/B2B**: ...
- **Диспуты/претензии (disputes)**: ...
```

I'll insert AD-009 and AD-010 between AD-008 and the `---`. And add a Deferred entry.

Let me do the edit with anchor on the end of AD-008 Rule + the "---\n\n## Deferred".

The exact AD-008 Rule text: "- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК."

Then:
"\n\n---\n\n## Deferred (с причиной и условием возврата)\n"

Let me edit.
Вношу инварианты AD-009/AD-010 и корректировку Deferred в спайн (защищённый файл — покрываю дельтой).

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/ARCHITECTURE-SPINE.md", offset=80, limit=30)`

Now update Deferred to reflect autopayments moved into scope and add gateway-scheduler deferred. Also the intro line "Данный spine — уровень feature" stays. Let me add a Deferred bullet. Also update the "Контракты и версии" section to reference v0.2.0 and subscriptions spec.

Let me read the current tail of the spine to edit precisely.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/ARCHITECTURE-SPINE.md", new_string="---\n\n## Deferred (с причиной и условием возврата)\n\n- **Мультивалютность и иностранные платёжные системы**: не в scope C2B-приёма СБП; в, old_string="---\n\n---\n\n## Deferred (с причиной и условием возврата)\n\n- **Мультивалютность и иностранные платёжные системы**: не в scope C2B-приёма)`

There's a doubled "---\n\n---" now (lines 81-83). My insert added a "---" then the existing "---". Let me fix: the file now has:

```
...Fitness: правило `mandate-audit-and-pdn-minimal`.

---

---

## Deferred ...
```

So there's a duplicate horizontal rule. Let me fix by replacing the double with single, and add deferred entries + contracts update.

Let me edit the block.

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/ARCHITECTURE-SPINE.md", offset=76, limit=14)`

The issue: there might be 3 dashes or trailing spaces. Let me read the exact region with line numbers to see whitespace. The read_file showed lines 81-94 with "---" twice but maybe there are blank lines between. Let me read 78-94 again carefully — it showed:

```
81	---
82	
83	---
84	
85	## Deferred ...
```

Hmm actually the output showed:
```
---

---

## Deferred (с причиной и условием возврата)
```
The line numbers weren't shown in the last read (it doesn't show line numbers). Let me re-read with offset to see. Actually read_file output doesn't show line numbers. Let me just do two smaller edits: (1) fix the duplicate "---" by replacing "---\n\n---\n\n## Deferred" — but that failed, meaning maybe it's "---\n\n\n---" or the dashes differ.

Let me grep for the pattern. Use grep_search for "\n---" hard. Simpler: read the file fully and inspect. Let me read the whole file.

Actually, maybe the double is: after my inserted block I added "\n\n---\n\n## Deferred" and the original had "---\n\n## Deferred", so result is "---\n\n---\n\n## Deferred". That's what I tried. But maybe there's a difference: the original line before Deferred. Let me just read raw around lines 78-86 using offset=77, limit=10.

Let me read.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/ARCHITECTURE-SPINE.md", new_string="- **Мультивалютность и иностранные платёжные системы**: не в scope C2B-приёма СБП; вернуть при расширении на валютные счета ТСП.\n- **Плани, old_string="- **Мультивалютность и иностранные платёжные системы**: не в scope C2B-приёма СБП; вернуть при расширении на валютные счета ТСП.\n- **C2C-п)`

So the current file has only ONE "---" before Deferred (line 77 is "---"? Actually output started at line 77 showing "---"). There's no duplicate. My earlier read at offset 80 showed duplicated because it started at line 81 which was the second "---"? Confusing. Anyway, current state: single "---" then Deferred. Good — no duplicate to fix.

So now I only need to add the Deferred entries and update the Contracts section. Let me edit using the exact current text (which I now see). The old_string will be the Deferred bullets + Contracts section.

Let me edit.
Дубля нет. Добавляю Deferred-записи и обновляю раздел контрактов.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/nfr.md", new_string="## 7. Рекуррентные списания (подписки, ADR-008)\n\nБюджеты нового функционала; базовые цели §1–§6 распространяются и на списания по согласи, old_string="## Зависимости (внешние входы для NFR)")`

Now update the NFR doc — append §7. Let me edit docs/nfr.md: add a new section before "## Зависимости (внешние входы для NFR)". Let me anchor on the "## Зависимости" heading.

Also, I should add the subscription NFR. Let me edit.
Добавляю измеримые NFR нового функционала.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.1.0\npaths:\n  /v1/payments:\n    post:\n      operationId: createPayment\, file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/changes/sbp-recurring-subscriptions/)`
  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\n  description: |\n    Контракт мерчант-API. v0.2.0 — аддитивное расши, file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/openapi/tsp-api.yaml")`

Now update openapi/tsp-api.yaml with additive subscription endpoints. Let me write the new file carefully, keeping existing content and adding new paths/schemas, bumping version to 0.2.0.

I must ensure openapi_lint passes (idempotency on mutating endpoints → Idempotency-Key header on POSTs; RFC7807 errors). The current file has no error responses and passed. New POSTs need Idempotency-Key.

Let me write the full file.

Also I'll save a copy of the old version to run contract_diff: copy current openapi/tsp-api.yaml to a temp old file before overwriting. Actually I already have the old content (read). I'll create `openapi/tsp-api.v0.1.0.yaml`? Hmm, adding a second contract file might confuse linters/sensors? The gate's openapi lint (in `review`) might lint all openapi files. Better to place the old copy under the change dir: `changes/sbp-recurring-subscriptions/openapi-v0.1.0.yaml` for the diff evidence. That keeps openapi/ clean. Let me do that: write old content to `changes/sbp-recurring-subscriptions/tsp-api.v0.1.0.yaml`, then overwrite `openapi/tsp-api.yaml` with v0.2.0, then run contract_diff old→new.

Let me write the old copy first (exact original content), then the new.

Original content (from earlier read):

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

Now the new v0.2.0. Add:
paths:
  /v1/subscriptions:
    post: createSubscription
  /v1/subscriptions/{subscriptionId}:
    get: getSubscription
  /v1/subscriptions/{subscriptionId}/charges:
    post: createSubscriptionCharge
  /v1/subscriptions/{subscriptionId}/revoke:
    post: revokeSubscription

Schemas:
  SubscriptionRequest (required: [paymentPurpose])
    payerRef (string)
    amountLimitPerCharge (integer)
    totalLimit (integer)
    currency (string, default RUB)
    period (string, enum [DAILY, WEEKLY, MONTHLY, QUARTERLY, YEARLY]? or free)
    paymentPurpose (string)
    merchantOrderId (string)
    webhookUrl (string)
  Subscription (required: [subscriptionId, status])
    subscriptionId, status (enum), consentRef, consentUrl, amountLimitPerCharge, totalLimit, currency, period, paymentPurpose, createdAt, activatedAt, expiresAt, revokedAt
  SubscriptionChargeRequest (required: [amount])
    amount (integer), merchantOrderId (string), paymentPurpose (string)
  SubscriptionCharge (required: [chargeId, paymentId, amount, status])
    chargeId, paymentId, amount, status (enum of payment statuses), createdAt
  Payment: add optional subscriptionId.

Also add PUT? no.

Keep style consistent (inline maps). Let me write.

I'll add enums and descriptions. Ensure YAML valid.

Let me write the old copy and new file.
Фиксирую контракт: сохраняю версию v0.1.0 для диффа и дописываю в v0.2.0 аддитивные методы (согласия/списания) без ломающих изменений.

  `tool_call(arguments={"path": "openapi/tsp-api.yaml", "cwd": "<HARNESS>/runs-v2-pilot/cells/wttdsvq, name="mcp__spine__openapi_lint")`
  `tool_call(arguments={"old": "changes/sbp-recurring-subscriptions/tsp-api.v0.1.0.yaml", "new": "openapi/tsp-api.yaml", "format": "openapi", "cwd": "<HOME>/З, name="mcp__spine__contract_diff")`

Now let me validate the openapi (lint) and contract_diff old→new. Let me run both. Also I need to consider: `contract_diff` old path = changes/.../tsp-api.v0.1.0.yaml, new = openapi/tsp-api.yaml.

Let me run MCP openapi_lint on new and contract_diff.

Also update docs/contracts/tsp-api.md with §8. Let me do that after validation.

Let me run lint+diff now.
Проверяю контракт: линт новой версии и дифф на ломающие изменения.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/contracts/tsp-api.md", old_string="- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)\n- Owner: solution-architect , new_string="- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.2 (нестабильная; до A1 фиксируется v1.0-draft). v0.1 → v0.2 — **аддитивное**)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/contracts/tsp-api.md", old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`

Contract diff: 0 breaking, 4 non-breaking (added paths). openapi_lint PASS. 

Now update docs/contracts/tsp-api.md with §8 (and maybe bump version note). Let me add a section before "## 6. Версионирование и совместимость"? Order: §5 webhooks, §6 versioning, §7 open questions. I'll insert §5.1 events? Simpler: add a new section "## 6. Рекуррентные списания (подписки) — v0.2" and renumber? Renumbering is messy. I'll insert as "## 5a" — no. Let me insert a new section after §5 and before §6, titled "## 6. Рекуррентные списания и согласия (подписки) — v0.2.0" and renumber the following sections 6→7, 7→8. That's cleaner. Let me do edits: change "## 6. Версионирование и совместимость" → "## 7. Версионирование и совместимость", "## 7. Открытые вопросы (для A1)" → "## 8. Открытые вопросы (для A1)", and insert new §6 before §7.

Also update header "v0.1 draft" → v0.2. Let me do targeted edits.

Let me first insert new section by replacing "## 6. Версионирование и совместимость" with new section + "## 7. Версионирование и совместимость". Then replace "## 7. Открытые вопросы (для A1)" with "## 8. Открытые вопросы (для A1)".

Also update the header line and §3.3 status enum maybe mention subscriptionId. And errors §4 add new codes. Let me do a few edits.

Edit 1: header.
old:
"- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)"
new:
"- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.2 (нестабильная; до A1 фиксируется v1.0-draft); v0.1 → v0.2 — аддитивное расширение (согласия/подписки, ADR-008)"

Edit 2: §4 error codes — add new codes. old line: "Канонические коды: `INVALID_REQUEST` (400), ... `RATE_LIMITED` (429), `INTERNAL` (500)." Add subscription codes.

Edit 3: insert §6 and renumber.

Edit 4: renumber §7 → §8.

Let me read the current tsp-api.md tail to get exact strings. I have it from earlier. Let me apply edits.
Обновляю документацию контракта ТСП (v0.2: новые методы и коды ошибок).

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/contracts/tsp-api.md", new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/contracts/tsp-api.md", new_string="## 6. Рекуррентные списания и согласия (подписки) — v0.2.0\n\nНовый функционал (ADR-008, AD-009): согласие плательщика (mandate) и рекуррен, old_string="## 6. Версионирование и совместимость")`

Now insert §6 (subscriptions endpoints doc) before "## 6. Версионирование и совместимость", and renumber. Let me do the edit replacing "## 6. Версионирование и совместимость" with the new section + "## 7. Версионирование и совместимость".

Also add webhook events for subscriptions in §5. Let me add to the events list. The current §5 events list:
"События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`"

Add subscription events. Let me edit.

Then insert §6.

Let me do both edits.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/contracts/tsp-api.md", new_string="## 8. Открытые вопросы (для A1)\n\n1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — road, old_string="## 7. Открытые вопросы (для A1)\n\n1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — road)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/contracts/tsp-api.md", new_string="# Контракт API ТСП (мерчант-API) — v0.2 draft", old_string="# Контракт API ТСП (мерчант-API) — v0.1 draft")`

Now renumber the last section "## 7. Открытые вопросы (для A1)" → "## 8. Открытые вопросы (для A1)" and add subscription open questions. Also update the header title (v0.1 draft → v0.2). Let me edit.

Also §1 general: "Авторизация ТСП" etc unchanged. Fine.

Let me edit the open questions section.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/contracts/opkc-adapter.md", new_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t, old_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/contracts/opkc-adapter.md", new_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |\n| `consent.activated` | , old_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |")`

Now extend docs/contracts/opkc-adapter.md with consent operations (internal contract). This is important for deliverable 4/2. Let me add new methods to §3, events to §4, and note in §1 scope and §9 open questions. Let me do targeted edits.

Edit §3 table: add rows registerConsent, getConsentStatus, revokeConsent.
Edit §4 events: add consent.activated, consent.rejected, consent.revoked.

Let me do it.
Расширяю внутренний контракт адаптера ОПКЦ consent-операциями (это граница ядро↔транспорт, AD-008).

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="  - name: spine-lints-clean\n    type: must_not_contain\n    glob: \"ARCHITECTURE-SPINE.md\"\n    pattern: 'TODO|TBD|XXX'\n    severity: wa, old_string="  - name: spine-lints-clean\n    type: must_not_contain\n    glob: \"ARCHITECTURE-SPINE.md\"\n    pattern: 'TODO|TBD|XXX'\n    severity: wa)`

Now update the CONSTRAINTS.yaml with new rules. Then write the DELTA.md. Then the handoff package. Then run gate.

Let me add rules to `.arch-handoff/CONSTRAINTS.yaml`. I'll append to the rules list.

Current content ends with:
```
  - name: spine-lints-clean
    type: must_not_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'TODO|TBD|XXX'
    severity: warn
```

I'll append new rules. Need to check the rule schema supports owner/expiry/rationale/fix_hint. The rules_suggest fragment used: name, type, glob, pattern, severity, rationale, fix_hint, skill. rules_report mentions owner, expiry, exclude_glob, effort_hours. Let me include owner, expiry, rationale, fix_hint.

Rules to add:
1. subscription-charge-requires-active-mandate — must_contain "docs/adr/ADR-008-*.md" pattern 'только при согласии в состоянии `ACTIVE`' severity error, owner, expiry.
   Wait: my ADR-008 says "инициирование списания разрешено **только при согласии в состоянии `ACTIVE`**" — the pattern with markdown bold between... The text is "разрешено **только при согласии в состоянии `ACTIVE`** и **в пределах". The literal substring "только при согласии в состоянии `ACTIVE`" appears (with ** before "только" but after "**только при согласии в состоянии `ACTIVE`**"). Actually the bold wraps: `**только при согласии в состоянии \`ACTIVE\`**`. So the substring "только при согласии в состоянии `ACTIVE`" is present inside the bold markers. Good. must_contain is a regex over whole file; backticks are literal. The pattern contains backticks — need to be careful in YAML quoting: use single quotes for pattern; backticks fine inside single quotes.

2. mandate-audit-and-pdn-minimal — must_contain "ARCHITECTURE-SPINE.md" pattern 'неизменяемом аудит-логе' severity error. AD-010 Rule has "фиксируются в неизменяемом аудит-логе" — good.

3. nfr-subscription-revocation-measurable — must_contain "docs/nfr.md" pattern 'Блокировка новых списаний после отзыва' severity error.

4. ears_acceptance_criteria — must_contain glob 'docs/**/*.md' pattern '(?m)^\s*[-*]?\s*\**\s*(When|While|If|Where)\b' severity warn.

Wait — but rule_weakened compares registry to baseline. Adding rules is fine. But there might be an issue: the `fitness_check` uses `.arch-handoff/CONSTRAINTS.yaml`. The `adr-no-placeholders` rule: must_not_contain glob "docs/adr/*.md" pattern '<!--'. My ADR-008 has no '<!--'. Good. 

Also rule `abs-credit-only-from-paid` requires ADR-005 file contains 'только из состояния `PAID`' — unchanged.

`nfr-measurable` requires docs/nfr.md contains '99,95' — still present. Good.

Now, there's a concern: my new rule `ears_acceptance_criteria` glob 'docs/**/*.md' — does the glob matcher support `**`? Yes. And must_contain checks at least one file matches. My docs/solutioning-subscriptions.md and docs/spec/*.md have EARS lines. Good.

Let me write the CONSTRAINTS addition via edit (append after spine-lints-clean).

Let me also double check the schema: does it accept `rationale`/`fix_hint`/`owner`/`expiry`? The rules_suggest fragment is the canonical form, so yes. rules_report reads owner/expiry. Let me include.

Let me edit.
Добавляю fitness-правила под новые инварианты в реестр ограничений.

  `write_file(content="# Дельта: sbp-recurring-subscriptions\n\n- Route: **Critical** (score 9/15; security_boundary_change + financial_impact — полный Solutionin, file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/changes/sbp-recurring-subscriptions/)`

Now write DELTA.md. Must mention protected files: ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml (and .arch-handoff/CONSTRAINTS.yaml). Include ADDED/MODIFIED/REMOVED, Проблема, План отката, Критерии приёмки (EARS). Route: Critical (full Solutioning).

Let me write.
Заполняю дельту изменения (упоминание защищённых файлов — обязательное условие delta-guard).

  `read_file(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/changes/sbp-recurring-subscriptions/)`

I need to read the DELTA.md first (it was created by the CLI). Let me read it then write.

Actually I already know its content from earlier cat. But the tool requires reading in session. Let me read it.

  `write_file(content="# Дельта: sbp-recurring-subscriptions\n\n- Route: **Critical** (score 9/15; security_boundary_change + financial_impact — полный Solutionin, file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/changes/sbp-recurring-subscriptions/)`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/solutioning.md", new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты, **рекуррентные сп, old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop)`

Now update docs/solutioning.md §1 roadmap line to remove "автоплатежи" from out-of-scope (per MODIFIED). Let me find the exact text: "Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

I'll update to move автоплатежи into scope and reference ADR-008.

Let me edit.

  `write_file(content="# Задача для кодового харнесса — инкремент «Подписки СБП (рекуррентные C2B-списания)»\n\nРеализовать поверх walking skeleton платёжного шлю, file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/changes/sbp-recurring-subscriptions/)`

Now build the handoff package for executors. Let me create `changes/sbp-recurring-subscriptions/handoff/` with the standard files. Let me write:
- TASK.md
- ARCHITECTURE.md (epic-context ~1200 tokens)
- CONSTRAINTS.yaml (copy of the updated .arch-handoff/CONSTRAINTS.yaml)
- RUBRIC.yaml (copy)
- MANIFEST.json
- adr/ADR-008...md (copy)

Actually, per handoff-packaging skill, the package is `.arch-handoff/`. But I'll put the increment package under the change dir to avoid clobbering the accepted walking-skeleton package. Hmm, but "передать исполнителям" — maybe they expect the standard `.arch-handoff/`. Let me reconsider.

The task: "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям." → The package for the change. A separate handoff dir for the increment is clean and reviewable. But maybe the reviewer expects `.arch-handoff/` updated (that's the repo's handoff mechanism). 

Option: update `.arch-handoff/TASK.md` and `ARCHITECTURE.md` would destroy the baseline walking-skeleton task, which is accepted. Bad. So separate package is right. I could name it `changes/sbp-recurring-subscriptions/handoff/` — consistent with delta-scoped artifacts.

Actually, better: the handoff CLI writes to `.arch-handoff`. But I don't want to clobber. I'll create the increment package under the change dir and clearly reference it. Good.

Also, since the handoff CONSTRAINTS.yaml is a copy, delta_guard might flag it as protected "CONSTRAINTS.yaml". My DELTA mentions `.arch-handoff/CONSTRAINTS.yaml` explicitly and "CONSTRAINTS.yaml" generally appears. The guard match is likely substring on path. Let me make sure DELTA mentions the handoff copy path too? It's new untracked; with git add -N it appears in diff. To be safe, I'll add a line in DELTA listing it. Actually I'll test delta guard after and fix if needed.

Hmm, actually — to avoid delta_guard noise, maybe I should NOT create a second CONSTRAINTS.yaml. But the handoff package by convention includes CONSTRAINTS.yaml. The skill says the package contains CONSTRAINTS.yaml. A second copy is legitimate. I'll keep it and mention it in DELTA.

Let me write the handoff files.

ARCHITECTURE.md (epic-context, 800–1500 tokens): compile goal, invariants AD-002/003/005/009/010 verbatim-ish, new contract surface, hard constraints. Let me write ~1200 tokens.

TASK.md: task + result contract JSON.

Let me write.

Let me first read the current .arch-handoff/CONSTRAINTS.yaml (updated) to copy content accurately. I have it. I'll write the copy.

Let me create the handoff files.
Собираю handoff-пакет инкремента для исполнителей (epic-context, задача, ограничения, рубрика, манифест, ADR).

  `write_file(content="# Архитектурный контекст: инкремент «Подписки СБП» (epic-context)\n\nКомпиляция по смыслу (не по источнику). Источники: `ARCHITECTURE-SPINE, file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/changes/sbp-recurring-subscriptions/)`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/changes/sbp-recurring-subscript, description="Copy constraints, rubric and ADR into handoff package")`

Now copy CONSTRAINTS.yaml and RUBRIC.yaml into handoff, and ADR-008. I'll use shell cp (allowed — file operation via shell? The guidance says prefer dedicated tools, but copying is fine with shell). Actually I should use read+write to be safe? cp is a system command; acceptable. But the delta_guard concern: the copy paths will be new files. Let me use cp.

Then MANIFEST.json.

Then validate delta and run gate.

Let me copy.

  `write_file(content="{\n  \"created_at\": \"2026-09-28\",\n  \"change\": \"sbp-recurring-subscriptions\",\n  \"route\": \"critical\",\n  \"task\": \"Реализовать, file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/changes/sbp-recurring-subscriptions/)`

Now MANIFEST.json for the handoff package. Let me write it.

Then validate delta structure: `arch-be delta validate sbp-recurring-subscriptions`. Then run gate `--route auto --base bench-baseline` (like the Stop hook) after `git add -A -N`. Also run delta guard explicitly.

Let me write MANIFEST.json.

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && git add -A -N >/dev/null 2, description="Validate delta structure and run delta guard")`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && echo \"=== FITNESS ===\"; , description="Run fitness check and spine lint")`

Now validate: delta validate, delta guard, fitness check, spine lint, and the unified gate with auto route. Let me run git add -A -N first (like the Stop hook) so untracked files are in diff, then gate --route auto --base bench-baseline.

Let me run several commands.
Проверяю пакет инструментами репозитория: дельта, fitness, линтер спайна, дельта-гвард и единый гейт.

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && echo \"=== SPINE LINT ===\, description="Run spine lint and spec sensors")`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && git add -A -N >/dev/null 2, description="Run unified architecture gate as the Stop hook does")`

- delta validate: no violations.
- delta guard: PASS, ARCHITECTURE-SPINE.md covered. Note: it says protected among changed = 1 (only ARCHITECTURE-SPINE.md). `.arch-handoff/CONSTRAINTS.yaml` and the handoff copy were NOT flagged as protected — interesting, so the guard's protect "CONSTRAINTS.yaml" maybe only matches root or specific? Anyway PASS.
- fitness: 11 rules, 0 violations, PASS, no weakening. Great — my new rules pass.
- spine lint: my invocation wrong (`arch-be control spine .` treats . as file). Let me run `arch-be control spine --help` or just `arch-be control spine` with no arg. Actually the command is `arch-be control spine`.

Let me run `arch-be control spine` and the unified gate.

Let me also run `arch-be control sensors ./docs/spec` to confirm sensors pass now (state-machine + subscriptions).

Let me run the full gate with auto route and base bench-baseline (exactly as Stop hook).

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && echo \"=== GATE critical =, description="Verify critical gate and significance score with anti-bypass floor")`

The gate PASSes. But route auto = Fast (score 0, no triggers detected from diff). Interesting — the auto detector didn't detect triggers. That's a gap: the change is Critical but auto-route says Fast. Anti-bypass (ADR-034) detectors only catch specific things (new_component/new_vendor/api_contract...). It didn't catch our additions. Hmm — but I declared route Critical based on the significance score. The gate auto says Fast; the Stop hook uses auto, so it passes as Fast. That's fine for passing, but for honesty the package declares Critical explicitly.

Wait — the gate on auto route didn't run `sensors` at all (Fast route doesn't run sensors). But when I forced `--route critical` earlier it ran sensors and failed. Now sensors pass anyway. Let me confirm the critical gate passes fully now (sensors pass). Let me run `--route critical` to verify the package is critical-ready (it will still SKIP nfr/model/evidence but those are not FAIL).

Also note: the auto-route detector did not flag `api_contract_change` even though openapi changed. That's a detector limitation (maybe it looks for new files in openapi/ or path patterns). Anyway.

Let me run the critical gate to confirm no FAIL.

Also `--from-diff` for control score to see anti-bypass floor. Let me run `arch-be control score --from-diff bench-baseline` with my declared triggers too. Actually to be safe let me run `arch-be control score --from-diff bench-baseline` to see what the mechanical floor adds.

Let me run critical gate + score from diff.

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && echo \"=== DELTA LIST ===\, description="Show delta list, rules report and suggestions")`
  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && arch-be review . 2>&1 | he, description="Run composite architecture review")`

Critical gate: FAIL list empty; sensors PASS; but "Итог: INCOMPLETE — обязательные составляющие без входа: trace_check, nfr, model_validate, evidence_verify (exit 3)". So on Critical route the gate returns INCOMPLETE (exit 3) because model/ and EVIDENCE.yaml are absent. Exit 3 is not exit 1 — the Stop hook: `out=$(arch-be gate ...) || { ... exit 2; }`. exit 3 is non-zero → the `||` triggers → hook prints FAIL message and exits 2 → blocks completion. 

BUT the Stop hook uses `--route auto`, and auto detected Fast (score 0). So the hook gate PASSed (exit 0) as we saw. So Stop won't block. Good — the auto route is Fast.

However, is that a problem? The change is Critical by my declared score, but the mechanical auto-detector says Fast. The task asks me to assess significance and route — I did (Critical). The gate's auto detector has limited detectors and didn't catch it. This is actually a notable finding worth reporting: anti-bypass detector didn't flag the contract/spine change. Hmm, should I report it? Could mention as an observation/open point. But careful — maybe the detector intentionally only detects new files (new component/vendor) not modifications. Our change modifies openapi and spine, which arguably should be api_contract_change. The detector missed it. I'll note this as a residual risk for the human (the mechanical floor under-detected; route declared Critical explicitly).

Now, should I make the package Critical-complete by adding model/ and EVIDENCE.yaml? That would require building a typed model (REQ/NFR/AD/CMP/INT) and evidence bundle — substantial. The task's 7 deliverables don't include a typed model or evidence bundle. And forcing `--route critical` to INCOMPLETE could be seen as "package not ready for critical". But the repo's baseline itself lacks model/ and evidence (it was Fast). The accepted decision was prepared without model/. The handoff MANIFEST/ARCHITECTURE doesn't reference model.

Given the effort/risk and that the task lists specific deliverables, I'll not build the full typed model/evidence. But I should be honest in the final report: the package passes the repo gate on auto route; under an explicit Critical route the gate reports INCOMPLETE for the artifacts that the repository doesn't yet have (model/, EVIDENCE.yaml) — those are pre-existing gaps in the accepted solution, not introduced by this change, and are listed as remaining work for the architect / next stage (A3→A4). That's faithful reporting.

Hmm, but wait — would it be better to actually create model/ to make it critical-complete? Let me weigh the user's ask: "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям." The deliverables enumerated are docs. I think documents + delta + contracts + handoff is the expected deliverable. Creating a typed model is an extra, and could fail validation (risky). I'll keep to the plan and report the gap.

Actually, let me reconsider: the repo has skills (spine-content-bootstrap, spine-bundle) and MCP tools (model_validate, trace_check, nfr_check, evidence_verify) that are designed exactly for this. The "правильный" critical package would include model/ and EVIDENCE.yaml. But the models require a specific schema I haven't seen, and getting it wrong could turn SKIP into FAIL and block the Stop hook. Given uncertainty, and that the task didn't ask for a typed model, I'll not create it. I'll explicitly list it as remaining (it's already listed as "обязательно для Critical" by the tool).

Hmm, but there's a tension: I declare Critical but don't make the package Critical-complete. The honest framing: the architectural *decision* package (evidence for A3) is complete; the *conformance evidence bundle* (A4) is a later stage, not part of "вынести на архитектурное решение". The gate's INCOMPLETE is about A4 artifacts. That's a legitimate argument. I'll state it.

Now let me also run a self-review with the adversarial-review lens? The task says "используй методические навыки по назначению". I've applied: significance-routing (score), spine-invariants (AD-009/010), adr-authoring (ADR-008), delta-spec (delta), nfr-design (NFR §7), spine-contracts-gate (lint+diff), handoff-packaging (handoff package), fitness-functions (rules), readiness-gate (EARS + traceability). Good coverage.

Should I run `arch-be review` (composite) or a rubric? Could be valuable evidence. Let me run `arch-be review .` (composite) to get a full verification, and maybe `adversarial-review` mentally. Let me run `arch-be review .` — it might exit 1 if something fails. Let me try; it's read-only. Actually the review may run the critical gate and return INCOMPLETE/fail. Let me just run it to see.

Also I should run `arch-be rules suggest .` again to confirm EARS found, and `rules-report` to show new rules with owner/expiry.

Let me also double check: did I break the existing CONSTRAINTS rule `adr-no-placeholders` (must_not_contain '<!--' in docs/adr/*.md)? ADR-008 has no '<!--'. Good. Fitness PASS confirms.

Let me run `arch-be review .` and `rules-report`.

Also verify delta list shows the delta active.

Let me batch.
Проверяю составным ревью и отчётом по правилам; смотрю реестр дельт.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/spec/subscriptions.md", new_string="| Отзыв согласия | `reference`/`subscriptionId` | повторный отзыв идемпотентен |\n\n### 4.1 Порядок проверок при инициировании списания (ко, old_string="| Отзыв согласия | `reference`/`subscriptionId` | повторный отзыв идемпотентен |\n\n## 5. Конкурентность отзыва и списания")`

Interesting: `arch-be review .` now shows "Маршрут: Fast (auto: score 1 (api_contract_change))" — so the review's diff-based detector DID catch api_contract_change (score 1). Earlier gate auto showed score 0. Difference: review uses base HEAD (working tree vs HEAD), while gate used `--base bench-baseline`. With base HEAD, untracked files? Actually with `git add -A -N`, the diff vs HEAD includes new files. So detector caught api_contract_change → score 1 → Fast (0-1). Still Fast, not Critical, because detector only counts api_contract_change=1. So mechanical floor = Fast. Hmm. But score 1 with only api_contract_change → Fast (0-1). 

Wait, but our declared score is 9. The anti-bypass only ADDS detected triggers; declared score is what the architect sets. The mechanical floor being Fast is a detector limitation. I'll note it.

Also `contracts — нет контрактных файлов (ни INT.contract, ни contracts/*.{yaml,yml,json})` SKIP — the review's contract lint looks for contracts/ dir at root, but our contract is in openapi/. That's a repo layout mismatch, pre-existing. I already linted openapi directly.

Also note review route base is HEAD (not bench-baseline) so score 1. Fine.

rules suggest: no candidates now — my EARS rule and rules satisfied the detectors. 

Now, the review exit 0 PASS. Good.

Now let me do a final adversarial self-check on the content (the skill adversarial-review): "я не проектировал — найди, что сломается". Key things to verify in my design:

1. **Revocation semantics**: I claim in-flight PAID charges complete. But there's a subtle race: what if revocation happens between charge request and НСПК PAID? Then the charge was initiated while ACTIVE (allowed), НСПК approves → we complete. That's consistent (authorized at initiation). Good, and it's documented as open question for exact "вступление в силу".

2. **Idempotency of charge across mandate revocation**: If a charge request is retried after revocation with same Idempotency-Key, should return same chargeId (not reject). The guard order matters: idempotency lookup should precede ACTIVE check. I didn't specify order explicitly. This is a real subtlety. I should note it. Actually this could cause: first request creates charge; mandate revoked; retry with same key → if guard checks ACTIVE first, it rejects with SUBSCRIPTION_REVOKED, but idempotent replay should return the existing charge. This is a genuine defect risk. Let me add a note to docs/spec/subscriptions.md §4 or a guard-ordering clarification: "Идемпотентный повтор (тот же ключ) возвращает ранее созданный ресурс независимо от текущего статуса согласия; проверка ACTIVE применяется только к новым запросам." Good catch — adds real value. Let me add it.

3. **Double charge within a period**: The design prevents duplicate by Idempotency-Key, but ТСП could send two DIFFERENT keys for the same period → double charge. The "period" guard: do we enforce one charge per period? My design says "в пределах параметров ... период" but doesn't enforce uniqueness per period. This is a real gap: recurring billing should prevent charging twice for the same billing period. Since charges are ТСП-initiated, ТСП controls periods; but a mandate with `period=MONTHLY` should perhaps enforce at most one charge per period, or at least the total limit bounds it. I should note this as a risk/open question: whether the gateway enforces period uniqueness or only limits. Let me add to risks/open questions. This is important honesty.

4. **Limit accounting concurrency**: cumulative total limit must be enforced atomically with charge creation (to avoid two concurrent charges exceeding total). Should be atomic with the charge creation transaction (AD-002 spirit). I should specify: guard + charge creation in one transaction (or reservation). Add.

5. **Consent creation idempotency with payerRef**: fine.

6. **ПДн**: payerRef might be phone number → ПДн. Minimization noted.

7. **New component vs existing**: fine.

8. **Contract**: `POST .../revoke` returns 202; idempotency header required — ok. Note the revoke endpoint is "mutating" and has Idempotency-Key. openapi_lint passed.

9. **Breaking changes**: adding `subscriptionId` optional to Payment — non-breaking. Good.

Let me improve docs/spec/subscriptions.md with guard ordering, period uniqueness, and atomic limit accounting. And add these to solutioning §8 open questions/risks.

Let me add a subsection 5.1 "Порядок guard'ов и атомарность" or extend §4.

I'll edit §4 table area and add notes.

Let me craft the edit: after the §4 table, add:

**Порядок проверок при инициировании списания (важно для конкурентности):**
1. Идемпотентность: повтор с тем же `Idempotency-Key` → вернуть существующий `chargeId` (независимо от текущего статуса согласия — иначе ретрай «после отзыва» теряет результат).
2. Guard согласия: `ACTIVE` (иначе `SUBSCRIPTION_NOT_ACTIVE`/`SUBSCRIPTION_REVOKED`).
3. Guard лимитов и периода: сумма ≤ лимит на списание; кумулятив + сумма ≤ суммарный лимит; период.
4. Проверка и создание платежа-списания и учёт кумулятива — **в одной транзакции** (иначе две параллельные заявки превысят суммарный лимит).

And add risk: "Два списания за один период с разными ключами" — gateway bounds by лимиты, но не гарантирует «одно списание на период», если этого требует бизнес → решить (open question).

Let me apply.

Also add to solutioning §8 questions list (A3) item about period uniqueness. And maybe note in §3.2.

Let me edit the spec.
Усиливаю спецификацию по слабым местам гонок (порядок guard'ов, атомарность лимитов, повторы после отзыва) — это то, что ломает безакцептные списания.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/spec/subscriptions.md", new_string="| Двойное списание при повторе | Прямой ущерб плательщику | Идемпотентность по ключу/`eventId`; тесты повторной доставки |\n| **Два списани, old_string="| Двойное списание при повторе | Прямой ущерб плательщику | Идемпотентность по ключу/`eventId`; тесты повторной доставки |")`
  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/docs/solutioning-subscriptions.md", new_string="| 8 | **Семантика отзыва при списании «в полёте»** (какой момент считать «вступлением отзыва») | Может регулироваться НСПК; финансово значи, old_string="| 8 | **Семантика отзыва при списании «в полёте»** (какой момент считать «вступлением отзыва») | Может регулироваться НСПК; финансово значи)`

Now add the two risks/open questions: period uniqueness (two charges per period with different keys) and guard ordering already covered. Let me add to the Risks table in subscriptions.md and to solutioning §8 (A3 questions) and §6 negative scenarios.

Add risk row: "Два списания за один период с разными Idempotency-Key" → "ТСП списывает дважды за период" → "Суммарный лимит ограничивает; при необходимости — уникальность «одно списание на период» (open question A3)".

Also add to solutioning §8 a question "9. Уникальность списания на период".

Let me edit the risks table in subscriptions.md.

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/README.md", new_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITEC, old_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITEC)`

Now let me re-run the gate/fitness/sensors to confirm still green after edits. Then finalize.

Also, I should consider whether to update README.md to reference the new change/artifacts. The README lists structure. Adding the change package reference would help discoverability. But README isn't protected; updating is fine and improves the package. Let me update README structure to mention changes/ and docs/solutioning-subscriptions.md, ADR-008. Also the baseline README says "Статус: решение подготовлено, ожидает A3 по ADR-007". Now ADR-007 is Accepted. I could add a line about the new change. Let me update minimally.

Let me update README:
- Kлючевые документы: add docs/solutioning-subscriptions.md, docs/spec/subscriptions.md, docs/adr/ADR-008.
- Status: add "изменение «подписки СБП» — на решении A3 (ADR-008)".
- Structure: add changes/sbp-recurring-subscriptions/.

Let me edit README. Need exact text. README content from earlier:

```
- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).

## Структура
...
```

Let me edit the "Ключевые документы"/"Статус" and add changes/ to structure. Let me read README to get exact current content (it may have changed? no).

I have it from earlier read. Let me edit.

Actually careful: the README "Статус" says ADR-007 A3 pending, but ADR-007 is now Accepted (per ADR-007 file and AD-008 adopted). The README is stale. I could correct it, but that's beyond scope. However, adding the new change status is in scope. Let me update both (correcting stale is low-risk and improves accuracy, and I'll mention it in the report). Hmm, "Не вноси не относящиеся изменения". The stale README status about ADR-007 is tangential. I'll only add the new change line and keep the rest, to minimize unrelated edits. Actually the README status already contradicts ADR-007 Accepted — but that's pre-existing; not mine to fix. I'll add a bullet.

Let me edit README minimally: add key docs and change status line.

Let me do it.
Обновляю README — добавляю ссылки на артефакты изменения (обнаружимость пакета).

  `edit(file_path="<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws/README.md", new_string="```\nARCHITECTURE-SPINE.md        инварианты AD-001..AD-010\ndocs/\n  solutioning.md             полный дизайн: компоненты, потоки, гейты, , old_string="```\nARCHITECTURE-SPINE.md        инварианты AD-001..AD-008\ndocs/\n  solutioning.md             полный дизайн: компоненты, потоки, гейты, )`

Now update the structure block in README to include AD-008 and the change dir? The structure block says "ARCHITECTURE-SPINE.md        инварианты AD-001..AD-008". Let me update to AD-001..AD-010 and add docs/solutioning-subscriptions.md, docs/spec/subscriptions.md, openapi/, changes/. Let me read the structure block exactly.

From earlier:
```
## Структура

```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-008
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps
  nfr.md                     измеримые NFR
  contracts/tsp-api.md       контракт API ТСП v0.1 (мерчант-API)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.1 (ядро ↔ транспорт; основа RFP)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  adr/ADR-001..007.md        архитектурные решения
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton)
```
```

Let me update this block. I'll replace it wholesale.

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && git add -A -N >/dev/null 2, description="Re-run fitness, sensors, spine lint, delta guard and gate")`
  `tool_call(arguments={"cwd": "<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws", "new": "openapi/tsp-api.ya, name="mcp__spine__contract_diff")`

Now re-run the full verification suite one more time to confirm green after all edits: fitness, sensors docs/spec, spine lint, delta guard, gate auto, gate critical (expect INCOMPLETE due to model/evidence). Also openapi lint + contract diff (already pass, but contract unchanged since). Let me run the key ones.

Let me run: `arch-be control check .`, `arch-be control sensors ./docs/spec`, `arch-be control spine ARCHITECTURE-SPINE.md`, `arch-be delta guard --base bench-baseline`, `arch-be gate --route auto --base bench-baseline`, and openapi_lint + contract_diff again (cheap).

Let me batch.
Финальная проверка всего пакета инструментами репозитория.

  `run_shell_command(command="cd \"<HARNESS>/runs-v2-pilot/cells/wttdsvq/ws\" && git status --short", description="List changed and new files")`

All green:
- fitness PASS (11 rules, 0 violations, no weakening)
- sensors PASS (docs/spec)
- spine lint: no violations
- delta guard PASS
- gate auto PASS
- contract_diff: 0 breaking, 4 non-breaking; openapi_lint PASS

Now let me produce the final report. Also list created/modified files.

Before that, let me get a clean `git status` to enumerate files precisely. Let me run git status --short.

Also, should I consider committing? The user didn't ask to commit. No.

Let me get git status.


Note `.arch-handoff/mcp-calls.jsonl` (A) — created by the MCP calls journal, not by me intentionally; and `.qwen/settings.json` (M) was pre-existing (baseline had it modified). `.arch-handoff/mcp-calls.jsonl` is a side-effect artifact of using the MCP spine tools. Should I leave it? It's a tool journal. It appeared because MCP calls are logged. It's untracked-added. I'll mention it as a byproduct (not part of the package) — or remove it? It's evidence of the control contour being used (trust metric reads it). Removing might be wrong. I'll leave it and note.

Also `.qwen/settings.json` was modified before I started (baseline git status showed M .qwen/settings.json). So not mine.

Now, let me write the final report. Structure:
- What was done (correspondence to 7 deliverables).
- Verification results (gate, fitness, sensors, spine lint, delta guard, contract diff, openapi lint).
- Files created/modified.
- What remains for human architect.
- Honest caveats: auto-route detector reported Fast while declared Critical; Critical route gate = INCOMPLETE due to absent model/ and EVIDENCE.yaml (pre-existing repo gaps, A4 stage).

The task asks: "Когда закончишь, кратко перечисли созданные и изменённые файлы." So final response should be concise but cover the 7 items mapping and file list. Let me write in Russian (user wrote Russian).

Let me keep it structured and not overly long. Include evidence numbers.

Let me also save a memory? The memory guidance: save durable cross-conversation knowledge. Is there anything worth saving? Possibly project memory about this repo's change mechanism (delta + gate). But "Do not save ... project structure / file paths" and "code patterns" — the delta mechanism is derivable from the repo. I think no memory needed. The system says memory empty; I can skip. Actually a reference memory pointing to the accepted change mechanism could be useful, but it's derivable from repo/skills. Skip to avoid low-value memory.

Now final answer.

Let me draft:

## Итог
Пакет изменения «подписки СБП» подготовлен поверх принятого решения; гейт репозитория зелёный.

### 1. Значимость и маршрут
Score 9/15 → Critical. Triggers list. Реализовано deterministic via arch-be control score. Обоснование.

### 2. Влияние на архитектуру
- Не меняется: AD-001, AD-004, AD-005 (усилен), AD-008, ADR-007.
- Расширяется: AD-002, AD-003, AD-006/007.
- Новое: AD-009, AD-010; Deferred скорректирован.
- Новый компонент: сервис согласий.

### 3. Решение
ADR-008: согласие как первоклассная сущность; alternatives (4 rejected) — attribute, НСПК-only, vendor, gateway-scheduler; consequences ± ; reversibility reversible→costly; expiry.

### 4. Контракты
openapi v0.1.0→v0.2.0 additive: 4 new paths, new schemas, optional subscriptionId, new events/errors. contract_diff 0 breaking; openapi_lint PASS. Internal adapter contract extended.

### 5. NFR
docs/nfr.md §7: table with numbers.

### 6. Приёмка и откат
EARS criteria + rollback (flag stop-new-charges).

### 7. Человек-архитектор (A3)
9 items.

### Верификация (evidence)
- delta validate: no violations; delta guard PASS; fitness PASS 11/0; spine lint 0; sensors PASS; gate auto PASS; contract_diff 0 breaking; openapi_lint PASS.
- Caveats.

### Файлы
Created / Modified lists.

Let me write it concisely but complete.

The change mechanism note: protected files (spine, CONSTRAINTS) changed via active delta — the accepted way.

Let me write.
Готово. Пакет изменения собран, прогнан инструментами репозитория и зелёный по гейту.

## Что сделано (по вашим 7 пунктам)

**1. Значимость и маршрут.** `arch-be control score` → **9/15, маршрут Critical**. Триггеры: `security_boundary_change` (появляется безакцептное списание без действия клиента), `financial_impact`, `criticality_or_exception`, `api_contract_change`, `data_contract_change`, `consistency_model_change`, `significant_nfr`, `rto_rpo_targets`, `new_component`. Следствие — полный Solutioning, обязательная человеческая точка A3, walking skeleton. Обоснование — `docs/solutioning-subscriptions.md` §1.

**2. Влияние на принятую архитектуру.** Не меняются AD-001 (изоляция), AD-004 (единственный адаптер ОПКЦ), AD-008/ADR-007 (гибрид); **усилен** AD-005 (согласие `ACTIVE` не подменяет `PAID`); **расширены** AD-002 (второй агрегат — согласие), AD-003 (новые ключи идемпотентности), AD-006/AD-007 (новый класс ПДн, аудит согласий). Добавлены инварианты **AD-009** (списание только по действующему согласию) и **AD-010** (доказуемое согласие, неизменяемый аудит, минимизация ПДн); скорректирован Deferred (автоплатежи → в scope, планировщик шлюза → Deferred). Новый компонент — сервис согласий в контуре шлюза.

**3. Решение.** `docs/adr/ADR-008-*.md` (Proposed, ждёт A3): согласие плательщика — первоклассная сущность со своей статусной машиной; списание — обычный платёж. Рассмотрены и отвергнуты 4 альтернативы (согласие как атрибут платежа; хранение только на стороне НСПК; вендорский модуль; планировщик шлюза как основная модель), заполнены отрицательные последствия, оценена обратимость (**reversible до боевой эксплуатации, costly после** — переоформление согласий), задан expiry.

**4. Контракты без поломки потребителей.** `openapi/tsp-api.yaml` v0.1.0 → **v0.2.0** аддитивно: 4 новых пути `/v1/subscriptions*`, новые схемы, опциональное `Payment.subscriptionId`, события `subscription.activated/revoked`, `charge.completed`. Проверено: `contract_diff` = **0 breaking** (4 non-breaking), `openapi_lint` — **PASS**. Внутренний контракт адаптера ОПКЦ расширен consent-операциями (`registerConsent/getConsentStatus/revokeConsent`).

**5. NFR.** `docs/nfr.md` §7: активация согласия p95 ≤ 30 с; инициирование списания p95 ≤ 500 мс; блокировка новых списаний после отзыва ≤ 60 с (сквозное ≤ 5 мин); двойных списаний — 0; сверка согласий ежедневно; доступность ≥ 99,95 %; ПДн — только референс.

**6. Приёмка и откат.** EARS-критерии и негативные сценарии (не-`ACTIVE`, превышение лимитов, дубль события, гонка отзыва/списания, недоступность НСПК). Откат: фиче-флаг `subscriptions_enabled` (по умолчанию off) → `stop-new-charges` без остановки начатых операций и отзыва согласий; сигналы и владелец решения названы; репетиция — A4.

**7. На решение человека-архитектора (A3).** 9 пунктов в `docs/solutioning-subscriptions.md` §8: подписать ADR-008; ратифицировать AD-009/AD-010; модель инициирования списаний (ТСП vs планировщик); обязательность уведомления плательщика; лимиты/TTL; хранение доказательства согласия (152-ФЗ); scope RFP; семантика отзыва «в полёте»; уникальность списания на период.

## Принятый способ изменения (соблюдён)
Защищённые файлы (`ARCHITECTURE-SPINE.md`, `.arch-handoff/CONSTRAINTS.yaml`) изменены **через активную дельту** `changes/sbp-recurring-subscriptions/DELTA.md` — иначе `delta_guard` блокирует правки спайна.

## Верификация (инструменты репозитория)
```
fitness_check        PASS — 11 правил, 0 нарушений, ослаблений нет
spine_lint           нарушений нет (0)
control sensors      PASS — docs/spec: 4/4 (state-machine.md, subscriptions.md)
delta validate       нарушений нет;  delta guard PASS (спайн покрыт дельтой)
gate --route auto    PASS  (для явного Critical — INCOMPLETE: нет model/ и EVIDENCE.yaml — этап A4)
openapi_lint         PASS;  contract_diff v0.1.0→v0.2.0 = 0 breaking (4 non-breaking)
rules_suggest        пробелов не найдено
```

**Честные оговорки:** (а) механический детектор маршрута в `gate --route auto` увидел только `api_contract_change` (Fast), т.е. anti‑bypass floor недооценивает изменение — маршрут Critical заявлен архитектурно, это стоит отметить на A3; (б) на явном Critical-маршруте гейт даёт `INCOMPLETE` из-за отсутствующих `model/` и `EVIDENCE.yaml` — это pre-existing пробел принятого решения (этап A4), а не дефект пакета; (в) реальный протокол НСПК по автоплатежам остаётся внешним входом `[ТРЕБУЕТ ПРОВЕРКИ]`.

## Созданные файлы
- `changes/sbp-recurring-subscriptions/DELTA.md` — дельта (ADDED/MODIFIED/REMOVED, откат, приёмка)
- `changes/sbp-recurring-subscriptions/tsp-api.v0.1.0.yaml` — снимок старого контракта (для `contract_diff`)
- `changes/sbp-recurring-subscriptions/handoff/{TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, adr/ADR-008-*.md}` — handoff-пакет исполнителям
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-soglasie-platelshchika.md` — решение
- `docs/solutioning-subscriptions.md` — дизайн изменения (значимость, влияние, потоки, NFR, приёмка, откат, вопросы A3)
- `docs/spec/subscriptions.md` — статусная машина согласия

## Изменённые файлы
- `ARCHITECTURE-SPINE.md` — AD-009, AD-010, Deferred, «Контракты и версии» *(через дельту)*
- `.arch-handoff/CONSTRAINTS.yaml` — 4 новых fitness-правила *(через дельту)*
- `openapi/tsp-api.yaml` — v0.2.0 (аддитивно)
- `docs/contracts/tsp-api.md` — §6 (подписки), v0.2, коды ошибок
- `docs/contracts/opkc-adapter.md` — consent-операции и события
- `docs/spec/state-machine.md` — §7 (связь со списанием) + обязательные секции сенсора
- `docs/nfr.md` — §7 (бюджеты подписок)
- `docs/solutioning.md` — §1 (автоплатежи в scope)
- `README.md` — раздел изменения и структура

Побочно (не часть пакета): `.arch-handoff/mcp-calls.jsonl` — журнал MCP-вызовов контура контроля; `.qwen/settings.json` был изменён до начала работы.

Коммит не делал — не просили.
