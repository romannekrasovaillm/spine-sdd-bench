<!-- источник: <HARNESS>/runs-v2/cells/wtnkjmc/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-v2-cells-wtnkjmc-ws/chats/dac6aa72-6aab-43ec-a573-26dd710cfb39.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.arch-handoff/ARCHITECTURE.md")`

I'll start by getting oriented: reading the accepted architecture package, the handoff rules, and the installed skills/tools that govern how this repo expects changes to be made.

  `run_shell_command(command="find . -path ./.git -prune -o -type f -print | sort", description="List all files in the repo")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.arch-handoff/connect-manifest.json")`

Let me read the rest of the key files. Let me look at the structure more fully.
Let me read the full decision documents, handoff rules, and available skills.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/settings.json")`

Let me read the solutioning, nfr, contracts, state-machine, ADRs fully. Also check settings.json for MCP, and check whether Spine is connected.

Key: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — The repo seems to have a delta protocol (delta_guard mentions model/ and ARCHITECTURE-SPINE.md protected paths). But this repo doesn't have a `model/` directory or `openspec/`. Hmm. Let me check .qwen/settings.json and see if there's a delta protocol defined. Actually delta_guard says: default protected paths model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. We need to check what's actually installed.

Let's read everything.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/openapi/tsp-api.yaml")`

Now let me read the contracts, state machine, ADR-003..007, and the tsp-api.yaml. Also read the relevant skills: delta-spec, significance-routing, adr-authoring, handoff-packaging, readiness-gate, nfr-design, fitness-functions, spine-* skills.

Let me check what's installed: `.qwen/skills/` — there are many skills. The task says "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." So I should use them.

Let me read the remaining docs.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-005-integraciya-s-abs-zachisl)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-007-proposed-a3.md")`

Now let me read the remaining ADRs (003-007) and the RFP. Also read important skills. And check the "delta protocol" mentioned in .arch-handoff/CONSTRAINTS.yaml and delta_guard — likely no openspec/ dir. Let me check the git log and the skills that matter.

Let me read ADR-003..007 and rfp.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/delta-spec/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/significance-routing/SKILL.md)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/adr-authoring/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/spine-contracts-gate/SKILL.md)`

Now let me check the git log and the delta protocol. The key phrase: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." That means SPINE is protected — use delta protocol (delta_guard). Let me check if there's a `openspec/` folder or a documented protocol. There's no `openspec/`. Let me check the delta_guard tool and the spine skills for the protocol. Let me read the delta-spec skill and spine-related skills, plus significance-routing and adr-authoring.

Actually let me check whether Spine MCP is available and what its config expects. Let me call spine tools: rubric_list, skill_search, plugin_list. But first, let me understand the repo's accepted way of changing accepted files.

delta_guard: "Гейт прямых правок спайна мимо дельты (модель 5.2): каждый изменённый файл под защищёнными путями (по умолчанию model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.ya..."

So the accepted way to modify ARCHITECTURE-SPINE.md is via a delta — i.e., openspec-style change with delta spec, or an ADR + spine update. Let me look at the delta-spec skill and also check whether there's an `openspec/` directory (there isn't in the file listing). Hmm, but maybe arch-be delta_guard has a default delta dir like `openspec/changes/`. Let me check the spine skill `delta-spec` and `spine-bundle`, and get the tool schemas.

Let me also run the spine tools to inspect. First let me check the tools available via tool_search select.

Let me read the relevant skills.
Now let me read the methodology skills that govern how changes are made here, and check the installed toolchain.

  `tool_search(query="select:mcp__spine__significance_score,mcp__spine__fitness_check,mcp__spine__spine_lint,mcp__spine__trace_check,mcp__spine__openapi_lint,mcp)`
  `tool_search(query="select:mcp__spine__rubric_list,mcp__spine__rubric_prompt,mcp__spine__rubric_verify,mcp__spine__model_validate,mcp__spine__evidence_verify,m)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/handoff-packaging/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/nfr-design/SKILL.md")`

The route is Critical. So full Solutioning is required, not delta-spec. The repo has `.arch-handoff/` for handoff, and the accepted way to modify ARCHITECTURE-SPINE.md presumably is adding an AD block + ADR + A3 human decision. Let me check delta_guard tool schema and the spine skills about "spine-content-bootstrap" / how to change spine. Also there's no `openspec/` dir, so delta_guard defaults. Let me check the tools.

Let me look at the spine-* skills available and use skill_search via spine MCP. Also check plugin_list, rubric_list, model_validate, fitness_check, significance_score, trace_check, spine_lint against this repo to establish baseline.

Let me read a few more skills: handoff-packaging, nfr-design, fitness-functions, readiness-gate, and the spine-* ones. And check the "check-spine-be-docs" for how arch-be works (delta protocol).

Let me be efficient: read handoff-packaging, nfr-design, readiness-gate, fitness-functions, spine-invariants, spine-fitness-gate, spine-bundle, adversarial-review.

Actually, the task is big. Let me first establish the baseline by running the spine tools, then read skills.

Let me check tool schemas for the spine tools I'll need: significance_score, fitness_check, spine_lint, trace_check, openapi_lint, contract_diff, delta_guard, rubric_run, rubric_list, model_validate, evidence_verify, rules_suggest, change_impact, architect_review.

Let me use tool_search to get schemas for a batch.
Now let me establish the baseline with the installed Spine toolchain and read the remaining methodology skills.

  `tool_call(name="mcp__spine__significance_score", arguments={"triggers": ["new_component=false", "new_datastore=true", "new_vendor=false", "domain_ownership_change=true", "cross_domain_integration=tru)`
  `tool_call(name="mcp__spine__fitness_check", arguments={"path": "<HARNESS>/runs-v2/cells/wtnkjmc/ws"})`
  `tool_call(name="mcp__spine__spine_lint", arguments={"path": "<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md"})`
  `tool_call(name="mcp__spine__openapi_lint", arguments={"path": "openapi/tsp-api.yaml", "cwd": "<HARNESS>/runs-v2/cells/wtnkjmc/ws"})`
  `tool_call(name="mcp__spine__rubric_list", arguments={"cwd": "<HARNESS>/runs-v2/cells/wtnkjmc/ws"})`

Let me now run baseline Spine checks. Also, I should check the delta_guard schema and the rules_suggest, change_impact. And check whether there's an `openspec/` or a delta protocol dir expected. Let me run the tools now.

First run: significance_score for the change (recurring C2B), fitness_check on repo, spine_lint, openapi_lint on existing contract, rubric_list, skill_search for relevant methodologies.

Also read the remaining skills: readiness-gate, fitness-functions, spine-invariants, adversarial-review, rubric-judging, spine-architect-review, spine-bundle, spine-fitness-gate, spine-content-bootstrap, spine-judge-handover, spine-semantic-judge. And check-spine-be-docs to learn about delta protocol.

Let me batch the tool calls.

  `tool_search(query="select:mcp__spine__delta_guard,mcp__spine__rules_suggest,mcp__spine__change_impact,mcp__spine__contract_diff,mcp__spine__architect_review,m)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/check-spine-be-docs/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/spine-bundle/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/fitness-functions/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/readiness-gate/SKILL.md")`

Baseline: fitness PASS, spine_lint PASS, openapi_lint PASS. rubric_list fails (no assets dir) — so rubric_run likely unavailable; but split-judge (rubric_prompt/rubric_verify) needs rubrics too. RUBRIC.yaml exists in .arch-handoff. Hmm, rubric_prompt takes a "path to YAML" too. So we can use `.arch-handoff/RUBRIC.yaml` as rubric path! Good — that's the handoff_quality rubric. But for ADR quality we'd want `adr_quality` rubric which may not exist. Let's check later.

Significance: score 10 → Critical. Good, matches.

Now, key question: how do we modify ARCHITECTURE-SPINE.md and accepted files "тем способом, который принят в этом репозитории"? Let's investigate the delta_guard tool and check-spine-be-docs skill to understand the delta protocol and what dir it expects (openspec/changes or .arch-handoff?). Let me read check-spine-be-docs skill and delta_guard schema.

Also I should check `lists` — there is no `model/` dir and no `openspec/`. So trace_check needs a case root with model/. Let me try trace_check anyway to see.

Let me read: check-spine-be-docs SKILL.md, spine-content-bootstrap, spine-architect-review, spine-bundle, spine-judge-handover, spine-semantic-judge, spine-adr-judge, fitness-functions, readiness-gate, rubric-judging, adversarial-review, spine-invariants.

That's a lot. Let me prioritize based on the task: 
- significance-routing ✓
- adr-authoring ✓
- delta-spec ✓
- handoff-packaging ✓
- nfr-design ✓
- spine-contracts-gate ✓
- Need: how to write the delta / change proposal in THIS repo, how to record A3 decision, how to append spine AD block, rubric judging, adversarial review.

Let me read check-spine-be-docs (tells about arch-be features), spine-bundle, spine-judge-handover, spine-semantic-judge, fitness-functions, readiness-gate, rubric-judging, adversarial-review, spine-invariants, spine-fitness-gate, spine-architect-review.

Let me batch reads.

  `run_shell_command(command="which arch-be; arch-be --version 2>&1 | head -5; echo \"---- delta help ----\"; arch-be delta --help 2>&1 | head -60", description="Check arch-be CLI availability and delta protocol")`
  `run_shell_command(command="git log --oneline -10; echo \"---- status ----\"; git status --short; echo \"---- branches ----\"; git branch -a", description="Inspect git history and status")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/spine-invariants/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/adversarial-review/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/rubric-judging/SKILL.md")`

Now I understand the delta protocol: `changes/<name>/DELTA.md` — protected paths are model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. So to modify ARCHITECTURE-SPINE.md, the accepted way is: create `changes/<name>/DELTA.md` mentioning the file. Let's verify by checking `arch-be` CLI availability and its `delta new` command. Let me check if `arch-be` CLI is available in the environment.

Also there's no `model/` dir, so trace_check may fail. Let's check whether `arch-be` CLI exists and what version.

Let me run: which arch-be, arch-be --help, arch-be delta --help.

Also I want to check `docs/` for extra files? No. Let me check git status and log fully.

Let me also read the remaining important skills: spine-invariants, spine-architect-review, spine-judge-handover, spine-semantic-judge, adversarial-review, rubric-judging, spine-content-bootstrap, spine-fitness-gate, spine-quickstart.

Batch: shell commands + reads.

  `run_shell_command(command="arch-be delta list 2>&1 | head -20; echo \"---- delta new help ----\"; arch-be delta new --help 2>&1; echo \"---- delta guard help ----\"; , description="Inspect delta subcommands and existing deltas")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/spine-architect-review/SKILL.)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/spine-judge-handover/SKILL.md)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/spine-semantic-judge/SKILL.md)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/adr-authoring/references/adr-)`

Now I have a good understanding. Let me check the delta guard + active deltas. There is no `changes/` dir. Let me verify by running `arch-be delta list` and `arch-be delta new --help`.

Also important: the task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." So modifying ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml, and possibly docs/ requires a delta. The delta-spec skill says Critical path requires full Solutioning, delta insufficient. But the delta here is the *mechanism* for the audit trail of spine changes, not the entire design approach. Actually the `delta-spec` skill says delta-only is insufficient for Critical; that means we need full Solutioning artifacts (ADR, NFR, etc.), AND the delta mechanism for protected files. So: create `changes/sbp-recurring-c2b/DELTA.md` covering the spine changes, plus full Solutioning package.

Let me verify delta new options and the default protected paths.

Let me also read the remaining skills: spine-architect-review, spine-judge-handover, spine-semantic-judge, spine-content-bootstrap, spine-fitness-gate, spine-quickstart, spine-adr-judge, spine-archify-viz. I'll read the most relevant: spine-architect-review, spine-judge-handover, spine-semantic-judge, spine-content-bootstrap.

Also read the ADR template and the fitness-function-catalog (for CONSTRAINTS additions).

Let me batch.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/fitness-function-catalog/SKIL)`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wtnkjmc/ws && arch-be delta new sbp-subscriptions , description="Create delta scaffold and inspect it")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wtnkjmc/ws && echo \"==== gate help ====\"; arch-b, description="Check gate command and baseline verdict")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wtnkjmc/ws"}, name="mcp__spine__trace_check")`

Now I have all the mechanics. Let me plan.

## Understanding the change

Business: recurring C2B debits by payer consent — СБП subscriptions. TSPs (online cinemas, utilities, telecom) want subscriptions. Currently each payment requires QR + client action.

СБП has a mechanism: "СБП Подписки" / recurring payments via СБП — payer gives consent (in their bank app) for periodic debits; the merchant initiates debits without a new QR scan each time. This is real: "СБП: автоплатежи/подписки" (СБП recurring / СБП Подписки, launched ~2023-2024). Mechanism: merchant registers a "подписка" (mandate) — payer confirms in bank app via QR/link; then merchant initiates debits with the subscription ID; payer's bank authorizes each debit (or auto-debits within limits).

This is a new capability: mandate/subscription lifecycle (creation, activation, amendment, revocation, debits), new consent objects, new statuses, new API resources, new notification events, revoke by payer, limits, etc.

Now the architectural package must include:
1. Significance assessment + route.
2. Impact on the accepted architecture: which invariants affected, what changes, what doesn't.
3. Architecture decision with alternatives, consequences, reversibility.
4. Contract changes (openapi/tsp-api.yaml) without breaking existing consumers.
5. Measurable NFR for the new functionality.
6. Acceptance criteria and rollback plan.
7. What remains for the human architect and why.

Also: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — i.e., use the delta protocol (`changes/<name>/DELTA.md`) to change protected files (ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml). And use ADRs (new ADR-008...) for new decisions, and A3 human decision point.

Now, how deep should I go? This is a substantial architectural package. Let me design:

### Deliverables plan

New directory: `changes/sbp-subscriptions/` (delta) with `DELTA.md` — the OpenSpec-style delta relative to current truth, covering:
- ADDED: new requirements/behaviors.
- MODIFIED: spine invariants (AD-002 status machine extended; AD-003 idempotency extended; AD-005 crediting; AD-007 compliance unchanged...), contract.
- REMOVED: nothing.

New ADRs (docs/adr/):
- ADR-008: Доменная модель подписок СБП (мандат/согласие) и место в принятой топологии — extends status machine with mandate domain.
- ADR-009: Идемпотентность и консистентность рекуррентных списаний (auto-debit saga, mandates, retry policy, dunning).
- ADR-010: Изменение контракта API ТСП — additive versioning strategy (v1.1 additive), mandate resources, webhook events.
- ADR-011: Стратегия миграции/внедрения и откат (feature flag, staged rollout, kill-switch for auto-debits).
- Possibly ADR-012: NFR/budget for recurring (latency, throughput, revocation SLA).

Hmm, but I should not over-engineer. The task asks for "архитектурный пакет этого изменения поверх принятого решения". Let me define a coherent set:

- `changes/sbp-subscriptions/DELTA.md` — delta spec (propose).
- `docs/adr/ADR-008-sbp-subscriptions-mandate-domain.md` — core decision: mandait lifecycle as a first-class domain alongside payments; new states; reuse of outbox/idempotency.
- `docs/adr/ADR-009-recurring-debit-consistency-and-consent.md` — consistency/idempotency/anti-duplicate for auto-debits (mandate + debit + payer bank authorization), "only from confirmed mandate", revocation.
- `docs/adr/ADR-010-tsp-api-additive-evolution.md` — contract evolution: additive v1.1, no breaking; webhook events; idempotency; versioning.
- `docs/adr/ADR-011-recurring-rollout-rollback.md` — rollout/rollback & human decision (A3).

Hmm, maybe combine. But ADR discipline says one decision per ADR. Let me keep 4 ADRs:
- ADR-008: расширение доменной модели шлюза: согласие плательщика (мандат) как отдельная сущность + расширение статусной машины (recurring debit as a payment subtype).
- ADR-009: консистентность и идемпотентность рекуррентных операций (mandate→debit saga, idempotency keys, no double debit, revocation).
- ADR-010: эволюция контракта API ТСП v1.1 (additive-only, backwards compatible).
- ADR-011: внедрение и откат (feature-flag staged rollout, kill-switch, A3 human gate).

Plus changes to accepted files via delta:
- ARCHITECTURE-SPINE.md: add AD-009 (Согласие плательщика — мандат; списание только по активному мандату) and AD-010 (рекуррентные списания — отдельный поток, не ломающий C2B-приём; additive contract). Also MODIFIED note in AD-002 (status machine extended with mandate-linked debits), AD-003 (idempotency key extends), AD-005 (crediting only from confirmed debit-confirmed status). Wait — careful: the spine says "Локальное переопределение родительских ограничений запрещено". Adding new AD blocks is fine; modifying existing AD rules is a delta MODIFIED.

Actually, the delta-spec skill: MODIFIED requirement (e.g., AD-005 rule extension). Let me be careful and minimal: new invariants AD-009, AD-010; MODIFIED entries for AD-002 and AD-005 that extend (not weaken) rules.

- CONSTRAINTS.yaml (.arch-handoff): add fitness rules for new invariants (e.g., mandate-required-for-debit, no debit without active mandate, contract additive check). But careful: `fitness_check` checks anti-weakening vs base — adding rules is fine (strengthening). But CONSTRAINTS.yaml is a protected path → must be mentioned in delta.

Wait — but the CONSTRAINTS.yaml in .arch-handoff is a derived handoff artifact for the *implementation* stage ("Этап: решение (до кода)"). Adding rules there could break the gate? Let me add carefully and re-run fitness_check.

- openapi/tsp-api.yaml: ADDITIVE changes. Problem: `contract_diff` v1→v2 will flag breaking if we change version. Additive optional fields and new paths are non-breaking. We bump info.version 0.1.0 → 0.2.0 (minor). Actually openapi_lint checks versioning; let me check what it expects. It passed on 0.1.0.

But there's a subtlety: the existing `PaymentRequest` requires `[amount, merchantOrderId]`. New mandate/debit endpoints are new paths → additive. Adding optional `mandateId` etc. is additive. Also adding new enum values to `Payment.status`? Adding enum values is technically a breaking change for strict clients (enum widening is usually considered... in OpenAPI, adding enum values breaks clients that validate enums). For consumers, adding new status like `AWAITING_MANDATE`/`DEBIT_*` might break. Better: keep payment status enum unchanged; introduce separate `mandateStatus` and a `debit` resource with its own statuses. Good — that's the "without breaking existing consumers" answer.

But contracts: the openapi file is quite minimal (only 2 paths). The docs/contracts/tsp-api.md is the fuller narrative. Should I update both? The task says "Изменения контрактов (openapi/tsp-api.yaml)". So yes update the openapi yaml, and probably also the narrative contract doc. But the narrative doc is `docs/contracts/tsp-api.md` — a decision artifact. Changing it is fine but should be consistent and via delta? Protected paths are only model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml. docs/ is not protected. But the delta should list all changed files for traceability (delta guard only checks protected). I'll mention all in DELTA.md.

Hmm — wait. Let me reconsider: The task explicitly lists 7 deliverables. It's an "архитектурный пакет" for an architectural decision, then handoff. So I should produce:

1. Significance assessment — can be a section in the change proposal / a report. Use significance_score (done: Critical, 10).
2. Impact on accepted architecture — section.
3. ADR(s).
4. Contract changes.
5. NFR.
6. Acceptance criteria + rollback plan.
7. Human-architect decisions.

Best packaging: create a change directory `changes/sbp-subscriptions/` containing:
- `DELTA.md` — the delta spec (change proposal; ADDED/MODIFIED/REMOVED).
- `PROPOSAL.md` — the full change package (significance, impact, ADR pointers, contract changes summary, NFR, acceptance, rollback, human decisions). Or split into several files. The delta protocol's `changes/<name>/DELTA.md` is required for delta_guard. Additional files in the change dir are fine.

Actually the repo's convention: docs/ holds artifacts. Let me follow both:
- `changes/sbp-subscriptions/DELTA.md` (delta protocol, protected-file coverage)
- `changes/sbp-subscriptions/PROPOSAL.md` (the reviewable package: significance, impact, decisions index, contract changes, NFR, acceptance/rollback, human decisions)
- `changes/sbp-subscriptions/IMPACT.md` maybe. Hmm, keep it tight: DELTA.md + PROPOSAL.md. Maybe an `adversarial-review.md` with VERDICT. Let me include `REVIEW.md` with adversarial review verdict (needed for readiness gate / evidence). 

Wait — evidence_verify expects `changes/<name>/EVIDENCE.yaml`. And spine-bundle says critical route requires 13 artifacts. But that's for a full case bootstrap. This repo wasn't bootstrapped via `arch-be bootstrap` (no model/, no openspec/). Should I bootstrap an evidence bundle? The task doesn't explicitly require it, but "передать исполнителям" (handoff) and "вынести на архитектурное решение" — an evidence bundle would be the repo's way. However, `arch-be bootstrap` may create a lot of scaffolding. Let me check if there's a lighter path. Actually, let me check what the gate expects: `arch-be gate --repo`. Let me check if gate is available and what it requires.

Hmm, let me be pragmatic and focused. The core ask is the 7 items. The repo's accepted *mechanism* for changing accepted files is the delta protocol. Let me:
1. Create delta via `arch-be delta new sbp-subscriptions`.
2. Fill DELTA.md with ADDED/MODIFIED/REMOVED covering spine + constraints.
3. Add new ADRs under docs/adr/.
4. Update ARCHITECTURE-SPINE.md (new AD-009/AD-010 + MODIFIED notes).
5. Update openapi/tsp-api.yaml additively + narrative contract doc.
6. Update docs/nfr.md with new NFR section.
7. Update DOCS: solutioning addendum? Maybe `docs/solutioning-subscriptions.md` (full solutioning for the change) — because Critical route requires full Solutioning, not just delta.
8. Update docs/spec/state-machine.md with mandate states + debits (or a separate spec doc). Hmm.
9. Update .arch-handoff CONSTRAINTS.yaml with new fitness rules + refresh the handoff package (TASK.md/ARCHITECTURE.md) for implementers.
10. ARCHITECTURE.md epic-context refresh in .arch-handoff.
11. Run gates: fitness_check, spine_lint, openapi_lint, contract_diff (old vs new), delta_guard, trace_check maybe.
12. Rubric judging via split-judge (rubric_prompt/rubric_verify) with the handoff_quality or adr_quality rubric. But rubric assets missing (rubric_list failed: no assets dir). Let me test rubric_prompt with rubric path `.arch-handoff/RUBRIC.yaml`. Actually target would be the ADR, rubric = handoff_quality (mentions handoff). For ADR quality, I can use the RUBRIC.yaml? It's handoff-specific. Could work for the package. Let me test.

Hmm, hold on. Let me reconsider scope and avoid overproduction. The user asked for a specific 7-part package. I should produce exactly that, well-formed, using repo conventions. Let me not create a `model/` (no model exists; trace_check requires model/ — it's absent, so trace_check will fail; I shouldn't invent a whole typed model unless needed). Let me test trace_check to see.

Let me also reconsider: should I present a plan to the user first? The task is large and multi-file. Per instructions, "For complex, ambiguous, or multi-step work, form a concise, outcome-oriented approach". I'm not in plan mode (user didn't ask). I can proceed but should be careful about ambiguity. There is one real ambiguity: how much to change accepted files (spine/ADR/contracts) vs produce a proposal-only package. The user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — implies changes ARE expected, done via the accepted mechanism (delta). So proceed.

Another ambiguity: status of new ADRs — Proposed (created before human A3). Yes, Proposed; human A3 decides. Good.

Let me also decide about the actual СБП subscriptions mechanism details. I must be accurate and flag unverified protocol details as `[ТРЕБУЕТ ПРОВЕРКИ]` per repo convention. Key architectural points for СБП подписки/автоплатежи:

- A mandate (согласие плательщика) is registered once; payer confirms in their bank (via QR/link at merchant or in bank app).
- Then merchant initiates debits (списания) referencing the mandate; each debit goes to payer's bank via ОПКЦ; can succeed or be rejected (insufficient funds, revoked).
- Payer can revoke consent anytime in their bank; merchant gets notification.
- Limits: max amount per debit, max per period (day/month), notification before debit (payer must be notified), cooling-off, etc. — regulated by НСПК rules and 161-ФЗ/Положение ЦБ. Details must be verified.
- The debit is asynchronous: initiated → confirmed/rejected via notification; also может быть «средства зарезервированы»/«списаны» stages.

Architecturally significant:
- **New aggregate: Mandate (согласие/подписка)** with its own lifecycle and status machine (CREATED → PENDING_PAYER → ACTIVE → SUSPENDED → REVOKED → EXPIRED), stored in gateway DB.
- **Debit as a variant of payment**: reuse status machine? Better: a recurring debit is still a payment (C2B) but with `paymentType=recurring`/`mandateId`, and the QR_ISSUED stage is replaced by a mandate reference. Critical invariant: **списание только по ACTIVE мандату** and **зачисление только из PAID** (AD-005 preserved). So the payment FSM gets an entry path: CREATED → (AUTHORIZING) → PAID without QR_ISSUED, or we keep QR_ISSUED semantics out. Since AD-005 says credit only from PAID, and AD-002 defines canonical states — we extend: for recurring debits, `QR_ISSUED` is not entered; instead `MANDATE_BOUND`/`DEBIT_SUBMITTED` (technical) → PAID. That's a MODIFIED to AD-002's canonical states, but preserving the safety invariant. Good.

- **Payer consent identity & PII**: mandate stores payer identifier (phone/masked), consent terms, limits. PII minimization (AD-007/ADR-006). Consent is the legal basis — important.
- **Idempotency**: debit initiation idempotent by (mandateId, billingPeriod) or Idempotency-Key; НСПК event dedup by eventId (existing). New: **no double debit for the same billing period** — new invariant.
- **Revocation**: payer revokes in bank → notification → gateway must stop future debits immediately; in-flight debit may still settle (race). Need: revocation SLA (e.g., stop initiating new debits ≤ N sec from notification), and handling of debit that arrives after revocation (→ refund? per rules). This is a real consistency challenge — good ADR material.
- **Dunning/retry**: failed debit (insufficient funds) — retry policy (limited, no aggressive retries), suspend after N failures. Must not be "fallback" antipattern (avoiding-fallback skill).
- **Notification to payer before debit** — regulatory; gateway/vendor responsibility? Possibly the payer's bank or the ОПКЦ. [ТРЕБУЕТ ПРОВЕРКИ].
- **Contract**: new paths `/v1/mandates` (POST create, GET status, DELETE/revoke), `/v1/mandates/{id}/debits` (POST initiate debit, GET status/list), maybe `/v1/payments?mandateId=`. New webhooks: `mandate.activated`, `mandate.revoked`, `debit.completed`, `debit.failed`. Additive to v1 → new minor 0.2.0 (or v1.1). Existing consumers unaffected.
- Vendor/ОПКЦ adapter contract extension: `registerMandate`, `getMandateStatus`, `revokeMandate`, `createRecurringDebit`, `getDebitStatus`, events `mandate.*`, `debit.*`. Extend `docs/contracts/opkc-adapter.md` (internal contract — additive).
- **Significance**: Critical (financial impact, new datastore? no — same DB; new domain objects; api_contract_change; consistency_model_change; significant_nfr; rto_rpo; criticality_or_exception). Score 10 → Critical. Requires full solutioning + human A3.
- **NFR**: 
  - Revocation propagation: payer revokes → gateway stops new debits within ≤ 60 s (p95), 0 new debits after revocation event processed.
  - Mandate activation latency p95 < 5 s (after payer confirms).
  - Debit initiation latency p95 < 300 ms (accept + enqueue), end-to-end debit status p95 < 5 s.
  - Throughput: billing peak — mass debits at billing date (e.g., 1st of month) → burst 3–5× base. Need sustained 200 TPS + peak 1000 TPS for debits, or queue-based load leveling. Set: sustained 300 TPS debit initiations, burst 1500 TPS for 10 min on peak billing hours; p99.
  - Double debits per billing period: 0.
  - Debits without active mandate: 0 (fitness).
  - Availability of debit flow ≥ 99,95%.
  - Auto-debit success rate target (business KPI) — not NFR per se.
  - RTO ≤ 1 h keeps; RPO=0 extends to mandate data.
  - Reconciliation: existing hourly NSPK + daily ABS extends to mandates/debits.
  - PII: mandate consent data minimization, retention.
- **Acceptance criteria** (EARS) + negative scenarios (duplicate debit, revocation race, mandate revoked then debit, insufficient funds, vendor unavailable during mass billing).
- **Rollback plan**: new capability behind feature flag; disable debit initiation (stop-new) while keeping mandate view/revocation working; existing QR flow untouched → rollback = turn off; data preserved.

Now, the "что остаётся на решение человека-архитектора" (A3): 
- Choice of consent/mandate model scope (full СБП Подписки vs simpler merchant-managed с recuring within СБП autopayment).
- Whether to extend v1 additively or introduce v2 (I recommend additive v1.x).
- Dunning policy (retry count, suspension thresholds) — business+compliance.
- Whether mandate storage goes in the same DB/aggregate or separate service — architecture choice.
- Handling race "debit settled after revocation" — policy with legal.
- Whether to vendor-extend the ОПКЦ adapter (same vendor or new RFP) — A3/business.
- Compliance: 161-ФЗ / Положение ЦБ 719? and NSPK rules for recurring — requires ИБ/legal sign-off; unverified inputs.
- The exact protocol details for recurring in НСПК (mandate API) — external input.

Now, "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — so:
- ARCHITECTURE-SPINE.md changes must be covered by `changes/sbp-subscriptions/DELTA.md` (delta_guard).
- Also CONSTRAINTS.yaml if changed.
- ADRs: new files (ADR-008…), don't modify accepted ADR-007.
- docs/nfr.md is not protected; but should be updated consistently. I'll add a section rather than rewrite.

Let me also verify: does `arch-be delta new` create the dir? Let me run it. And check `arch-be` config existence (arch-harness.toml). Let me run delta new and inspect generated DELTA.md.

Also, let me check whether there's a hidden `.arch-handoff/mcp-calls.jsonl` (created by MCP) — untracked, ignore.

Let me also check the gate command and whether evidence bundle is required. Let me run `arch-be gate --help` and `arch-be gate --repo .` to see baseline.

Let me proceed step by step. First, create the delta scaffold and check gate/evidence baseline.

Actually, wait. Let me reconsider whether to touch `.arch-handoff/CONSTRAINTS.yaml`. It's a protected path. Adding rules there is a strengthening; `fitness_check` compares rule composition with base and reports weakening. Adding is fine. But `arch-be rules allow` trust... the new rules are must_contain/file_exists (no command_succeeds) → no exec trust issue. Good.

Also the handoff package (TASK.md/ARCHITECTURE.md) is for the *implementation* stage; the task asks to prepare the architectural package so it can "затем передать исполнителям". So maybe I should also prepare an updated handoff package for the *new* change? Hmm — "чтобы его можно было вынести на архитектурное решение и затем передать исполнителям" — the package goes to architectural decision first, then to executors. So the primary deliverable is the decision package. A refreshed handoff could be a bonus. Given the A3 decision is still pending, generating a full implementation handoff now would be premature (ADR-007 says transport implementation only after contract). I'll prepare the handoff as a *proposal-stage* update: update `.arch-handoff/ARCHITECTURE.md` (epic-context) and TASK.md? That risks conflicting with the existing walking-skeleton handoff. Better: keep `.arch-handoff/` as-is (it's for the existing walking skeleton) and note in the proposal that after A3 the handoff must be regenerated. Actually the CONSTRAINTS.yaml in .arch-handoff — modifying it affects the existing handoff gate. Hmm.

Alternative: put the new fitness rules in the delta/change dir as a fragment and NOT modify .arch-handoff/CONSTRAINTS.yaml, to avoid destabilizing the existing handoff. But the delta mechanism's protected path IS CONSTRAINTS.yaml. And the fitness-functions skill says rule fragments are brought into the registry by the architect via delta. Since `CONSTRAINTS.yaml` default path is `.arch-handoff/CONSTRAINTS.yaml`, and the delta must *mention* protected files that were changed — if I don't change it, no mention needed.

Decision: I'll add the new fitness rules to `.arch-handoff/CONSTRAINTS.yaml` (strengthening, with the delta covering it), and re-run fitness_check. This demonstrates the repo's accepted path: rule → delta. And it's genuinely useful for the A4 gate later. But careful: rules must not break the current gate. I'll craft them so they pass now (e.g., must_contain on the new ADR/spine docs that I add). Actually rules that assert new content will pass only after my changes — fine, they will exist.

Hmm, but anti-weakening check compares with base HEAD. Adding rules = strengthening → fine.

Wait, actually there's a subtlety: `must_contain` on `docs/adr/ADR-008...md` — if the file exists with the content, passes.

Let me now also decide on the fitness rules for the new invariants. Good candidates (textual, since no code yet):
- `subscription-mandate-required`: must_contain in ARCHITECTURE-SPINE.md pattern 'AD-009'.
- `debit-only-from-active-mandate`: must_contain in `docs/adr/ADR-009-*.md` pattern 'только по активному мандату' or in spine AD-009 Rule.
- `contract-additive-only`: must_contain in `changes/sbp-subscriptions/DELTA.md` pattern 'совместим' — weak.
- Better: a `must_not_contain` guard: openapi/tsp-api.yaml must not remove v1 paths — can't express removal via regex. Could use `must_contain` on each existing path to prevent deletion: `/v1/payments` etc. That's a real anti-breaking guard! Add rules:
  - `tsp-api-keeps-payment-paths`: must_contain glob openapi/tsp-api.yaml pattern '^  /v1/payments:' (with (?m)).
  - `tsp-api-keeps-payment-status-enum`: must_contain pattern 'CREATED, QR_ISSUED' — enum unchanged.
  These are meaningful "no breaking change" fitness guards. 
- `mandate-idempotency`: must_contain in ADR-009 pattern 'billingPeriod' or 'Idempotency-Key'.

Also the fitness-function-catalog skill has 20 ready regexes. Let me read it for precise patterns (e.g., problem+json, idempotency). Let me read fitness-function-catalog and rule-library-antipatterns quickly.

Also read `spine-fitness-gate` maybe. And `fitness-function-catalog` for templates.

Let me read those two, then run delta new + gate baseline.

Actually, I realize I should also consider: the repo has `.qwen/skills/` with many skills; the user says use them. I've been doing that. Also there's `spine-archify-viz`, `c4-mermaid` — maybe a diagram would help. The proposal could include a mermaid diagram of the mandate/debit flow using `mermaid_render` to validate syntax. Good idea for the package.

Let me now read fitness-function-catalog + rule-library-antipatterns, and run delta new + gate baseline + trace_check.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/rfp/vendor-rfp.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/rule-library-antipatterns/SKI)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.qwen/skills/spine-content-bootstrap/SKILL)`

Important finding: `arch-be gate` auto-detects route as **Fast** for the current working tree (score 0) — because the diff has no code and the detectors look at file changes. Baseline HEAD is Fast scored 0. The `significance_score` route Critical is what we assert. The gate auto-route depends on git-diff detectors; once I add files, it may detect triggers (api_contract_change because openapi/tsp-api.yaml changes, etc.). Good — that's the mechanism.

Also note: gate baseline route "Fast (auto: score 0 (триггеров нет); исключено по манифесту connect/.spineignore: 1 файлов)" — there's a connect manifest with .spineignore excluding 1 file. That's `.arch-handoff/connect-manifest.json`? Anyway.

No `model/` dir → trace_check/model_validate SKIP. Fine. I won't invent a model — but wait, trace could be required for Critical. `arch-be gate` SKIPs if no model/. So it's acceptable in this repo.

Now: `changes/sbp-subscriptions/DELTA.md` scaffold created with a placeholder template. Note `Route: Fast|Standard (Critical — полный Solutioning, дельты недостаточно)` — good, the template itself reminds.

Now let me design the deliverable set concretely and write it. Let me plan the file list:

**New (change package):**
1. `changes/sbp-subscriptions/DELTA.md` — delta spec (fill scaffold).
2. `changes/sbp-subscriptions/PROPOSAL.md` — full change package: significance, impact, decisions index, contract changes, NFR, acceptance, rollback, human decisions. Maybe split into:
   - `PROPOSAL.md` (main: significance, impact, decision index, contract summary, NFR, acceptance, rollback, human decisions).
   - `IMPACT.md`? I'll fold into PROPOSAL.
   - `REVIEW.md` — adversarial review verdict (I'll run the review lenses honestly and record findings; ideally by an independent agent — I can delegate to a subagent for independence! That matches "независимый контур". Good idea: use the Agent tool to get independent adversarial review of my package. But that adds time; the task says "используй их по назначению" and adversarial-review skill is installed. I think an independent review is valuable and demonstrates the discipline. I could delegate to a `general-purpose` subagent with the adversarial-review prompt. But the subagent won't have repo context unless I give it. I can point it at the files. Let me consider doing it after writing, as a verification step, and record VERDICT: READY/NOT-READY. That's genuinely useful.
   - `EVIDENCE.yaml` — evidence bundle (critical route). Hmm, evidence_verify expects specific keys. Let me check the expected schema by running evidence_verify on a dir. Actually spine-bundle lists 13 keys: problem, spec_or_delta, risk_level, acceptance, rollback, adr_or_pattern, spine, decision_a3, walking_skeleton, adversarial_review, rollback_rehearsal, validation, fitness_report. But decision_a3 must be signed by human (decided_by empty → a3_not_signed). Since A3 is pending human, the bundle would be red — which is *correct and honest*: the package is ready for the architectural decision, not for release. Maybe I should NOT create an EVIDENCE.yaml that pretends completeness. But creating a stub bundle that's honestly red on a3 is arguably good. Hmm, but it might be seen as noise. The task doesn't ask for evidence bundle. I'll skip EVIDENCE.yaml and instead include a "gate/evidence" section in PROPOSAL describing what remains red and why (A3). Actually, let me reconsider — "вынести на архитектурное решение" = A3. The human decision is the point. So a bundle with `decision_a3.decided_by` empty is the honest state. I'll mention it. Let me not fabricate an evidence bundle.

**New ADRs (docs/adr/):**
3. `ADR-008-sbp-podpiski-domennaya-model-mandata.md` — mandate domain + payment extension.
4. `ADR-009-rekurrentnye-spisaniya-konsistentnost-i-idempotentnost.md` — consistency/idempotency/revocation.
5. `ADR-010-evolyuciya-kontrakta-tsp-additive-minor.md` — contract evolution.
6. `ADR-011-vnedrenie-i-otkat-podpisok.md` — rollout/rollback (A3 pending).

Maybe also:
7. `ADR-012-nfr-rekurrentnyh-spisanij.md`? NFR can live in docs/nfr.md section; no ADR needed. But there's a trade-off (peak billing load vs availability → queue load leveling) that is a real decision → could be ADR. Hmm, maybe fold into ADR-009 (consistency + peak handling is different). Let me think about whether "queue-based load leveling for mass billing peaks" deserves its own ADR. Yes — it's a decision affecting the flow, with alternatives. But I risk over-producing. I'll include it as a decision inside ADR-009? ADR-009 is "consistency and idempotency of recurring debits". Peak load handling is arguably NFR/infra. Let me make ADR-012: "Пиковая нагрузка биллинговых дат: очередь и выравнивание" — actually that's good architectural content and uses the queue-load-leveling skill. Hmm.

Let me settle on 5 ADRs (008–012):
- ADR-008: Доменная модель согласия плательщика (мандата) и интеграция со статусной машиной платежа.
- ADR-009: Консистентность и идемпотентность рекуррентных списаний; отзыв согласия.
- ADR-010: Эволюция контракта API ТСП — аддитивные минорные версии (без поломки потребителей).
- ADR-011: Пиковая нагрузка биллинговых дат — очередь и выравнивание (load leveling) + защита от перегрузки.
- ADR-012: Внедрение, обратимость и откат подписок (staged rollout, kill-switch) — A3.

That's a coherent set, each with alternatives/negatives/reversibility.

**Modified accepted files (via delta):**
8. `ARCHITECTURE-SPINE.md` — add AD-009 (мандат: списание только по активному согласию), AD-010 (аддитивная эволюция контракта ТСП), AD-011 (изоляция рекуррентного потока / выравнивание пиков?) Hmm — spine should be minimal (5–15 blocks; now 8 → adding 2–3 → 10–11 OK). Let me add:
   - AD-009. Согласие плательщика — обязательное условие рекуррентного списания (mandate). Binds: mandate store, debit flow, ОПКЦ adapter, TSP API. Prevents: списание без действующего согласия; «забытый» отзыв; PII/consent хранение без основания. Rule: рекуррентное списание возможно только при статусе мандата ACTIVE и действующем billingPeriod-ключе идемпотентности; отзыв вступает в силу ≤ N с и блокирует новые списания. Status: Proposed (ADR-008, ADR-009).
   - AD-010. Аддитивная эволюция контракта ТСП (no breaking in /v1). Binds: openapi/tsp-api.yaml, TSP clients. Prevents: поломку существующих потребителей C2B-приёма; смену семантики существующих полей/статусов. Rule: новые возможности — только новыми путями/полями/ресурсами; существующие пути/поля/enum не удаляются и не сужаются; payment.status enum неизменен. Status: Proposed (ADR-010).
   - AD-011. Пиковое выравнивание рекуррентных списаний (queue + shed/prioritize). Binds: очередь списаний, планировщик, ТСП API. Prevents: каскадный отказ в биллинговые даты; списание без учёта лимитов. Rule: инициирование списаний — через очередь с выравниванием; при перегрузке — backpressure/shed, никогда не «всё сразу». Status: Proposed (ADR-011).
   - MODIFIED: AD-002 (extend canonical states with mandate-binding path), AD-003 (idempotency: new keys — mandateId + billingPeriod / debitId; debit initiation idempotent), AD-005 (unchanged core: credit only from PAID — reaffirm; add: debit settlement only from confirmed ОПКЦ status). I'll express MODIFIED as explicit delta lines and add short "(расширено дельтой sbp-subscriptions …)" notes where needed. Careful: spine_lint must stay clean.
   - AD-007 compliance: no change (ГОСТ, trust zones apply to recurring too). Note that mandate data is PII → AD-007 covers it; reaffirm.
   - Update "Deferred": remove/annotate "автоплатежи" from Deferred (solutioning says autopayments roadmap out of scope). Now they're in scope → MODIFIED in delta.

9. `.arch-handoff/CONSTRAINTS.yaml` — add fitness rules (new invariants + anti-breaking guards).
10. `openapi/tsp-api.yaml` — additive: bump to 0.2.0, add mandate & debit paths/schemas, new webhook events (maybe as description), keep payment paths/enum intact.
11. `docs/nfr.md` — add section "Рекуррентные C2B-списания (подписки)" with measurable NFR.
12. `docs/contracts/tsp-api.md` — add mandate/debit sections (narrative), version notes.
13. `docs/contracts/opkc-adapter.md` — add mandate/debit operations/events (internal contract; additive; [ТРЕБУЕТ ПРОВЕРКИ]).
14. `docs/spec/state-machine.md` — add mandate FSM + debit path; or a new `docs/spec/mandate-state-machine.md`. I'll add a new spec file to avoid rewriting accepted spec? It's a spec, not protected. Better: new file `docs/spec/mandate-state-machine.md` and add a cross-ref line in state-machine.md. Hmm, minimal edits: create new spec file, and reference it from the delta. Also update `docs/solutioning.md`? I'd rather create `docs/solutioning-subscriptions.md` (the full Solutioning for the change) — Critical route demands full Solutioning. Yes! That's the "полный Solutioning" for the change. Good.

So:
15. `docs/solutioning-subscriptions.md` — full solutioning of the change (context, components delta, flows, ADR split, gates, rollback, gaps, open questions).

That's a lot of files but appropriate for a Critical change. Let me also add:
16. `README.md` — update status/structure? The README lists key docs and status. Adding a line about the change package would be consistent. Minimal edit.

Also maybe `docs/rfp/vendor-rfp.md` — extend RFP with recurring/mandate requirements. Since transport vendor must support mandates. That's a real impact: the internal contract with the vendor changes → RFP criteria must add mandate operations. Let me add a section to vendor-rfp.md (read it first).

Let me read `docs/rfp/vendor-rfp.md` before deciding.

Now, about REVIEW.md via independent agent: I'll do it. And possibly rubric judging via split-judge.

Let me also double-check: the user asked "Изменения контрактов (openapi/tsp-api.yaml) без поломки существующих потребителей." So contract diff proof is important: I'll run `contract_diff` old vs new and `openapi_lint` on new. But contract_diff needs the old file — I can copy the current file to a temp location before editing (or use `git show HEAD:openapi/tsp-api.yaml`). I'll save old to `.qwen/tmp/`? Hmm, temp files: write under `.qwen/tmp/` (per artifact rules). Actually simpler: `git show HEAD:openapi/tsp-api.yaml > <TMP>.1.yaml` — outside repo. But tool says intermediate files under .qwen/tmp. Let me use `changes/sbp-subscriptions/contracts/tsp-api-v0.1.baseline.yaml`? That pollutes. I'll use `git show` to `/tmp`. Fine.

Now let me read vendor-rfp.md and then start writing. Let me also read the state-machine (done) and check `arch-be rules` CLI for adding rules? I'll edit YAML directly.

Let me read vendor-rfp.md.

Also, I should double check how `arch-be` treats `.arch-handoff/CONSTRAINTS.yaml` glob patterns and whether `must_contain` with `(?m)^  /v1/payments:` works. YAML anonymous strings need quoting. I'll test after writing.

Let me read vendor-rfp.md and also the `spine-content-bootstrap` and `spine-fitness-gate` skills quickly (they may define the exact way to add rules/spine blocks in this ecosystem). And `rule-library-antipatterns`.

Actually, I have enough. Let me read vendor-rfp.md and rule-library-antipatterns (to avoid antipatterns), then write.

Let me also verify: is there a `docs/SOURCE_BRIEF.md` referenced by RUBRIC.yaml? Not present. Never mind.

Let me read vendor-rfp.md.

  `tool_call(arguments={"triggers": ["new_component=false", "new_datastore=false", "new_vendor=false", "domain_ownership_change=true", "cross_domain_integration=tr, name="mcp__spine__significance_score")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wtnkjmc/ws && mkdir -p .qwen/tmp && git show HEAD:, description="Save baseline contract and spine for diffing")`

I have enough context. Let me write the plan and then execute.

Given the size, let me use a todo-like approach mentally and just produce files carefully. I'll write substantive, precise Russian docs.

Let me fix the design details now, precisely enough to be consistent across files.

### Domain design (recurring СБП C2B)

New aggregates:
1. **Mandate** (согласие плательщика / подписка) — identifies: `mandateId` (gateway), `mandateRef` (ОПКЦ), `tspId`, payer identifier (masked phone), consent terms: max amount per debit (`maxAmountPerDebit`), period limit (`maxAmountPerPeriod`, `period`=DAY|MONTH), schedule (`frequency`: DAILY|WEEKLY|MONTHLY|ON_DEMAND?), validity (`validFrom`, `validUntil`), purpose, ТСП-provided `merchantSubscriptionId`. Statuses: `DRAFT → PENDING_CONSENT → ACTIVE → SUSPENDED → REVOKED → EXPIRED`, terminal `REJECTED`, `REVOKED`, `EXPIRED`.
2. **Debit** (рекуррентное списание) — an operation within a mandate. Modeled as a *payment with mandate binding*: `paymentId`, `mandateId`, `billingPeriod` (e.g., `2026-10`), amount, status. Reuses payment FSM but replaces the QR path: `CREATED → DEBIT_SUBMITTED (техн.) → PAID → CREDITED → COMPLETED`, terminals `FAILED`/`REJECTED`/`EXPIRED`(retry budget exhausted)/`REVERSED`? For recurring, `FAILED` + retry policy.

Key invariants:
- Debit initiation only with mandate status `ACTIVE` and current time within validity, amount ≤ limits, and no successful debit for the same (`mandateId`, `billingPeriod`).
- Credit only from confirmed `PAID` (AD-005 preserved).
- Revocation: as soon as revocation event received, no NEW debit may be initiated (guard); in-flight debit already submitted to ОПКЦ may settle → handle per rules (refund or credit per НСПК rules) — a documented exception path, not silent.
- Idempotency: debit initiation keyed by `Idempotency-Key` + unique constraint on (`mandateId`, `billingPeriod`); ОПКЦ events deduped by `eventId` (existing).
- Mandate change (terms) → requires new payer consent → new mandate (immutable terms), analogous to payment immutability.

FSM addition to payment: `QR_ISSUED` not used for mandate debits; add technical state `MANDATE_BOUND`/`DEBIT_SUBMITTED`. Existing states unchanged → contract enum for `Payment.status` unchanged (no breaking). Hmm, but `DEBIT_SUBMITTED` would be a new status visible? Keep it internal (technical), not in the API enum. Good: contract stays additive.

### Significance / route
Score 10 → Critical. Triggers: api_contract_change, consistency_model_change, criticality_or_exception, cross_domain_integration, data_contract_change, domain_ownership_change, financial_impact, new_datastore (mandate store — could argue same DB, but new tables/store), rto_rpo_targets, significant_nfr. Note significance_score marks new_datastore true because we add a new stored aggregate. Also arguably `security_boundary_change`? No. `trust_zone_change`? No. `irreversible_migration`? No. I'll present the trigger table with true/false and note that route is a function of declared triggers.

Actually let me double check whether "new_datastore" is honest. We're adding mandate/debit tables in the same gateway DB. It's arguably a new data store *of record* (new aggregate). I marked true and got 10. If I mark false, score 9 → still Critical (5+). Either way Critical. I'll be honest: it's a new stored aggregate in the existing DB → I'd mark it false (same datastore). Let me re-run significance_score with new_datastore=false to get an accurate number and verify Critical.

Let me compute: fired without new_datastore: api_contract_change, consistency_model_change, criticality_or_exception, cross_domain_integration, data_contract_change, domain_ownership_change, financial_impact, rto_rpo_targets, significant_nfr = 9. Plus maybe domain_ownership_change? New domain object owned by gateway → yes. So 9 → Critical. I'll re-run to be precise and honest.

Let me re-run significance_score with corrected triggers.

### Alternatives (for ADRs)

ADR-008 (mandate model) alternatives:
- A: мандат как отдельная сущность ядра (выбран) vs B: мандат внутри платежа ТСП (reuse payment with merchant-managed schedule) vs C: полностью вендорский модуль подписок.
ADR-009 (consistency) alternatives:
- A: отдельный FSM мандата + debit-as-payment с idempotency (billingPeriod) — chosen; B: сторонний scheduler/оркестратор (Step Functions) для биллинга; C: синхронный дебет без очереди.
ADR-010 (contract evolution) alternatives:
- A: additive minor v1.1 (chosen); B: new /v2; C: отдельный API подписок (new service).
ADR-011 (peak load) alternatives:
- A: queue-based load leveling + admission/shed + shuffle sharding (chosen); B: direct synchronous; C: БД-дривен scheduled batches.
ADR-012 (rollout/rollback) alternatives:
- A: feature-flag staged (chosen); B: big bang; C: parallel pilot service.

### NFR numbers (new section)
- Mandate activation: от подтверждения плательщиком до `ACTIVE` в шлюзе — p95 ≤ 5 с, p99 ≤ 15 с (без учёта НСПК).
- Revocation propagation: от события отзыва до запрета новых списаний — p95 ≤ 60 с, p99 ≤ 5 мин; после обработки — 0 новых списаний (fitness/тест).
- Debit initiation API latency: p95 ≤ 300 мс, p99 ≤ 1 с (accept+enqueue).
- Debit end-to-end status (PAID/REJECTED) — p95 ≤ 5 с from initiation (excluding payer bank latency; [ТРЕБУЕТ ПРОВЕРКИ] по регламенту НСПК).
- Peak billing throughput: sustained 300 TPS initiations; burst 1500 TPS ≥ 10 мин на биллинговых пиках; ≥ 5000 mandates просрочены/… hmm. Let me give: peak day volume N; queue lag p95 ≤ 60 с.
- Duplicate debits per (mandate, billingPeriod): 0 (unique constraint + idempotency) — test.
- Debits without active mandate: 0 — test.
- Availability of debit/mandate flows: ≥ 99,95%.
- RPO=0 extends to mandate/debit data; RTO ≤ 1 h unchanged.
- Reconciliation extends: mandates/debits included in hourly NSPK recon.
- PII: payer identifier masked, stored encrypted; retention per 152-ФЗ/НСПК; consent record immutable (audit).
- Error budget for mass-billing: max доля недоставленных списаний за биллинговое окно ≤ 0.1%.

### Acceptance criteria (EARS)
Positive: mandate create→activate; debit success; partial refund of subscription payment (existing refund works since debit is a payment); webhook delivery.
Negative: duplicate debit same period; debit on revoked mandate (must be blocked); revocation race; insufficient funds; vendor unavailable during peak (queue backlog, no double debit after recovery); mandate terms change without consent (blocked); debit above limit (blocked).
Rollback: kill-switch disables new debits; existing QR flow unaffected; revocation stays functional; data retained; reconciliation continues.

### Human architect decisions (A3)
- A3-1: mandat model scope (full СБП Подписки consent model vs merchant-managed schedule) — needs НСПК documentation + business.
- A3-2: whether to require АБС/vendor support — vendor adapter extension (same RFP or amendment) — procurement/business.
- A3-3: dunning policy (retry count, suspension thresholds, notification duties) — business + compliance/legal.
- A3-4: policy for debit settling after revocation (refund vs credit) — legal + НСПК rules.
- A3-5: contract versioning choice (additive v1.1 vs v2) — architect (I recommend additive; human confirms).
- A3-6: peak-load target numbers (биллинговые пики) — business (volumes) + capacity.
- A3-7: data retention/PII for mandate consent — ИБ/ДПО.
- Also: A3 must be signed by human; my package sets `decided_by` empty.

Also unverified external inputs: exact НСПК recurring protocol (mandate API, limits, notification duties, timeout) `[ТРЕБУЕТ ПРОВЕРКИ]`; 161-ФЗ/Положение ЦБ requirements for periodic debits without each-time payer action (право на уведомление/возврат); НСПК rules on max limits.

Alright. Now let me write files. I'll start with the main solutioning + ADRs + spine + contract + NFR + delta.

Order of writing (dependency-free):
1. Re-run significance_score (honest).
2. Write `docs/solutioning-subscriptions.md`.
3. Write ADR-008..012.
4. Edit `ARCHITECTURE-SPINE.md`.
5. Edit `openapi/tsp-api.yaml` + `docs/contracts/tsp-api.md` + `docs/contracts/opkc-adapter.md` + `docs/rfp/vendor-rfp.md`.
6. Edit `docs/nfr.md`.
7. New `docs/spec/mandate-state-machine.md`.
8. Fill `changes/sbp-subscriptions/DELTA.md` + `PROPOSAL.md`.
9. Edit `.arch-handoff/CONSTRAINTS.yaml`.
10. Run gates: openapi_lint, contract_diff, fitness_check, spine_lint, delta_guard, arch gate.
11. Independent adversarial review (subagent) → REVIEW.md.
12. Maybe rubric split-judge.
13. Update README.

Given the response must be in Russian (user writes Russian). All documents in Russian (repo convention). Good.

Let me first re-run significance_score and then start writing. Also save the old openapi for diff.

Let me do the significance re-run + git show baseline contract.

Let me write. This is a large amount of content; I'll be thorough but avoid bloat. Let me start.

Actually, one more consideration about "новые обязательные поля в запросах = breaking". In my openapi changes, I must ensure new fields are optional and existing ones unchanged. Also I should keep `Payment` status enum unchanged. Add `Mandate`, `Debit` schemas and paths. Also for the debit resource I could reuse Payment but with mandateId. Let me design openapi:

Paths to add:
- `/v1/mandates` POST (create mandate request → consent link/QR) — operationId createMandate, Idempotency-Key required.
- `/v1/mandates/{mandateId}` GET — mandate status.
- `/v1/mandates/{mandateId}/revoke` POST — ТСП-initiated cancellation (payer revokes in bank; ТСП can also cancel) — Idempotency-Key.
- `/v1/mandates/{mandateId}/debits` POST — initiate debit (Idempotency-Key + billingPeriod) → returns Payment-like resource (paymentId, status).
- `/v1/mandates/{mandateId}/debits` GET — list debits (optional; maybe skip to keep tight). I'll include GET list as it's useful.
- `/v1/debits/{paymentId}` GET — or reuse `/v1/payments/{paymentId}`; a debit IS a payment so it's queryable via existing endpoint. Good — reuse! So debit gets a `paymentId`; status via existing `/v1/payments/{paymentId}`. That's elegant and reinforces "debit = payment subtype". But the Payment schema needs a new optional `mandateId` field, and a new optional `paymentType` field. Additive optional → non-breaking. And `refunds` works. 

So new paths: `/v1/mandates`, `/v1/mandates/{mandateId}`, `/v1/mandates/{mandateId}/revoke`, `/v1/mandates/{mandateId}/debits` (POST + GET).

Schemas:
- `MandateRequest`, `Mandate`, `MandateStatus` enum.
- `DebitRequest`.
- Extend `Payment` with optional `mandateId`, `paymentType` (enum `single|recurring`), `billingPeriod`. Optional → non-breaking.
- Error response schema? The current yaml doesn't define errors. openapi_lint mentioned RFC 7807 check — it passed, so maybe no error responses required. I'll add a `Problem` schema and `429`/`409` responses? That could trigger checks. Keep minimal but add `Problem` for new endpoints to follow RFC 9457 as the doc says. Hmm, openapi_lint checks "ошибки RFC 7807" — maybe it requires problem+json in error responses. Current file has no error responses at all and passed, so it's lenient. I'll add Problem schema + `429` where rate limiting. Actually to be safe and consistent with docs, add `Problem` schema and a couple of error responses on new endpoints; then re-lint.

Let me be careful: adding required new fields to existing `PaymentRequest` would break. I won't.

Version: bump `info.version` from `0.1.0` to `0.2.0`. contract_diff CD-007: "ломающий дифф без смены major info.version" — since diff is non-breaking, no issue. But careful: if contract_diff considers adding enum values to `Payment.status`... I'm not adding. Adding new enum for MandateStatus is a new schema → fine. Adding paths → fine.

Now, one risk: `contract_diff` might flag "added required path parameter"? No. It may flag anything about `required`. I'll run and see.

Let me now write everything.

Let me re-run significance and grab baseline contract.

  `write_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/solutioning-subscriptions.md", content="# Solutioning (дельта) — Рекуррентные C2B-списания СБП (подписки ТСП)\n\n- Date: 2026-09-28\n- Status: Proposed (для гейта A3; изменение по)`

Score 9 → Critical. Good.

Now let me write the documents. Start with the solutioning for the change.

I'll write `docs/solutioning-subscriptions.md` — full solutioning of the change.

Let me write it comprehensively but not bloated.

Then ADRs. Then spine edits. Then contract. Then NFR. Then spec. Then delta + proposal. Then constraints. Then gates.

Let me start writing.
Route confirmed: **Critical (9/15)**. Baseline gates are green. Now I'll write the change package. Starting with the full Solutioning for the change.

  `write_file(content="# ADR-008. Доменная модель согласия плательщика (мандата) и рекуррентное списание как вид платежа\n\n- Date: 2026-09-28\n- Status: Proposed, file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-008-mandat-soglasie-platelshc)`

Now the ADRs. Let me write ADR-008..012 following the template with Date, Status, Owner, Related, Context, Decision, Alternatives Considered (table), Consequences (Positive/Negative), Reversibility, References.

Note the adr-authoring skill mentions `Модель-автор` field: `- Author-model: human` or model tag. Since I'm an agent writing them, I should mark the model. I'm Qwen Code. Let me set `- Модель-автор: qwen-code`. The parser accepts `- Author-model:` or `- Модель-автор:`. I'll use `- Модель-автор: qwen-code`.

Wait — but the rubric judge anti-bias: author_model read from header. Good to include. The existing ADRs don't have it, but adding it is recommended by the skill ("Пишите human или метку модели"). I'll add.

Let me write ADR-008.
Now the five ADRs for the change.

  `write_file(content="# ADR-009. Консистентность и идемпотентность рекуррентных списаний; отзыв согласия\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: solu, file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-009-konsistentnost-i-idempote)`

Now ADR-009: consistency and idempotency of recurring debits, revocation. This is the core technical decision. Include the revocation race, dunning (or defer dunning policy to A3/human but define mechanism: bounded retries, no aggressive retry, suspend after N consecutive failures — with numbers as proposed), period-bounded debit.

Also include "no fallback" discipline (avoiding-fallback skill) — not falling back to alternative payment path automatically; handle errors explicitly.

Alternatives: 
- A: mandate guard + period idempotency + bounded retries in gateway, revocation-first ordering (chosen).
- B: rely on payer bank to reject duplicates (no gateway guard) — rejected.
- C: distributed lock / leader election across gateway nodes for billing (rejected: single-writer unnecessary, DB unique constraint + idempotency suffice) — reference leader-election skill.
- D: automatic fallback to QR payment on debit failure — rejected (avoiding-fallback; UX/consent issue).

Let me write.

  `write_file(content="# ADR-010. Эволюция контракта API ТСП: аддитивные минорные версии без поломки потребителей\n\n- Date: 2026-09-28\n- Status: Proposed\n- Own, file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-010-evolyuciya-kontrakta-tsp-)`

Now ADR-010: contract evolution — additive minor versions. Include the concrete proof via contract_diff, alternatives v2/separate API, and the rule. Also mention that token/vendor contract opkc-adapter extends additively too.

  `write_file(content="# ADR-011. Пиковая нагрузка биллинговых дат: выравнивание очереди, допуск и приоритеты\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: , file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-011-pikovaya-nagruzka-billing)`

Now ADR-011: peak billing load. Include load-leveling, admission control, priorities, shuffle sharding, AgeOfFirstAttempt? Keep relevant: queue-based load leveling, admission/shed, jitter to avoid thundering herd on billing datetime, priority for revocation/mandate events vs debit batches, backpressure. Alternatives: synchronous direct; cron fan-out without leveling; per-TSP staggering only.

Include numbers referencing NFR §7.

  `write_file(content="# ADR-012. Внедрение, обратимость и откат подписок: поэтапный запуск с kill-switch\n\n- Date: 2026-09-28\n- Status: Proposed (требует челов, file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-012-vnedrenie-otkat-i-kill-sw)`

Now ADR-012: rollout/rollback & A3. Include staged rollout, feature flag, kill-switch, pilot TSP, mandatory human A3, rollback criteria/signals/owner. Also include the machine-readable A3 package pointing to PROPOSAL §8.

Then the spine edit, contract, NFR, state machine, delta, proposal, constraints.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md", old_string="Статусы: блоки в статусе `Proposed` действуют после ратификации соответствующего ADR. Помеченные `[ADOPTED]` — ратифицированная реальность., new_string="Статусы: блоки в статусе `Proposed` действуют после ратификации соответствующего ADR. Помеченные `[ADOPTED]` — ратифицированная реальность.)`

Now edit ARCHITECTURE-SPINE.md. I need to:
- Add AD-009, AD-010, AD-011 after AD-008.
- MODIFIED notes for AD-002, AD-003, AD-005.
- Update Deferred (remove "автоплатежи" from... actually Deferred didn't mention autopayments; solutioning §1 roadmap mentioned autopayments out of scope. The spine Deferred lists мультивалютность, C2C/выплаты, диспуты. I should add a note that recurring C2B (подписки) is now IN scope via delta — and remove any conflict. There's no autopayments entry, so I just add nothing, or add a note. Actually solutioning.md §1 says "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." So the parent solutioning had autopayments out of scope. My change brings them in. I should note that in the delta MODIFIED and update solutioning.md? The task says "Принятые файлы решения меняй только тем способом, который принят" — solutioning.md is not protected but is an accepted decision file; the accepted way is: deltas for protected, and ADR/delta for the rest. I'll cover it in DELTA.md MODIFIED and add a line to solutioning.md §1 roadmap. Hmm, modifying solutioning.md is reasonable but let me instead add a pointer at the top of solutioning.md? Minimal: add a line in §1 to say автоплатежи/подписки выделены в дельту `docs/solutioning-subscriptions.md`. That keeps truth coherent. I'll do a small edit.

For spine MODIFIED, the cleanest approach that keeps spine_lint happy: add a short "Изменено дельтой" line inside each affected AD block? That changes the Rule line potentially. spine_lint checks Binds/Prevents/Rule non-empty and no stubs, no duplicate IDs, links to existing AD. Adding an extra line like "- Delta: sbp-subscriptions (2026-09-28) — см. AD-009…AD-011" is fine.

Actually, careful: spine_lint may check "непиннутые версии" and "ссылки на несуществующие AD". Referencing AD-009..011 (which exist) is fine.

Let me add to AD-002, AD-003, AD-005 a line: `- Delta (sbp-subscriptions, 2026-09-28): <what extends>`. And add three new blocks AD-009/010/011. Also add a "Delta" section note near top? Let me add a "Изменения (дельты)" line in the header area. Hmm, keep minimal.

Let me read the exact current tail of the spine to edit precisely. I have the content from earlier read. Let me construct edits.

Edit 1: AD-002 Rule (add delta line after Rule).
Current:
```
- **Rule**: Изменение финансового статуса платежа и запись исходящего события (outbox) выполняются в одной локальной транзакции. Нарушение — дефект блокера (ревью + fitness-тест на каждый переход).
```
Add after:
```
- **Delta (sbp-subscriptions, 2026-09-28)**: правило распространяется на сущности «мандат» и «рекуррентное списание»: их переходы — такие же атомарные транзакции «статус + outbox + аудит» (ADR-008, ADR-009).
```

Edit 2: AD-003 Rule add:
```
- **Delta (sbp-subscriptions, 2026-09-28)**: добавлены ключи идемпотентности рекуррентных операций — (`mandateId`, `billingPeriod`) и `Idempotency-Key`/`reference` для мандата и списания; повтор отзыва идемпотентен (ADR-009).
```

Edit 3: AD-005 Rule add:
```
- **Delta (sbp-subscriptions, 2026-09-28)**: для рекуррентного списания добавлен guard входа — инициация только при мандате в статусе `ACTIVE`; зачисление по-прежнему возможно только из `PAID` (ADR-008, ADR-009).
```

Edit 4: Insert new blocks after AD-008 block (before "## Deferred").

New blocks:

```
## AD-009. Рекуррентное списание — только по действующему согласию плательщика

- Status: Proposed (ADR-008, ADR-009) [proposed, до A3]
- **Binds**: мандатный модуль, рекуррентные списания, API ТСП, адаптер ОПКЦ.
- **Prevents**: списание без действующего согласия плательщика; списание сверх лимитов согласия; «забытый» отзыв согласия; подмену условий согласия после активации.
- **Rule**: рекуррентное списание инициируется только при мандате в статусе `ACTIVE`, в пределах `validFrom`/`validUntil` и лимитов, и не более одного успешного списания на (`mandateId`, `billingPeriod`). Условия мандата иммутабельны после активации; изменение — новый мандат с новым согласием. Отзыв запрещает новые списания; обработка отзыва — приоритетнее пакета списаний. Fitness: «0 списаний без ACTIVE-мандата», «0 дублей за период».

## AD-010. Аддитивная эволюция контракта API ТСП

- Status: Proposed (ADR-010)
- **Binds**: `openapi/tsp-api.yaml`, `docs/contracts/tsp-api.md`, потребители API ТСП.
- **Prevents**: поломку существующих потребителей разового C2B-приёма; смену семантики существующих полей; расширение/сужение enum `Payment.status`.
- **Rule**: новые возможности — только новыми путями, новыми ресурсами и опциональными полями; существующие пути, поля и enum `Payment.status` не удаляются, не сужаются и не меняют смысл; ломающие изменения — только в новой major-версии. Fitness: `contract_diff` v0.1→v0.2 без breaking; правила сохранности путей `/v1/payments*`.

## AD-011. Пиковые нагрузки биллинга выравниваются очередью

- Status: Proposed (ADR-011)
- **Binds**: очередь списаний, планировщик биллинга, адаптер ОПКЦ, АБС-адаптер.
- **Prevents**: каскадный отказ в биллинговые даты; «громовое стадо» на границе окна; лавину ретраев; блокировку отзыва согласия пакетом списаний.
- **Rule**: инициирование списаний проходит через очередь выравнивания с допуском (backpressure) и приоритетами (отзыв/мандатные события — вне пакетной очереди); лавина ретраев запрещена (бюджет); при перегрузке — притормаживание приёма, а не неограниченный бэклог. Fitness: метрики лага/возраста первого необработанного и пороги алертов (`docs/nfr.md` §7).
```

Also update header statuses line? The statuses line says "Помеченные [ADOPTED] — ратифицированная реальность." Fine.

Also Deferred: add note that автоплатежи/подписки выведены из Deferred в дельту. Let me add to Deferred a bullet:
```
- **Автоплатежи/подписки (рекуррентные C2B)**: были вне scope родительского решения; введены дельтой `changes/sbp-subscriptions` (AD-009…AD-011) [Proposed до A3].
```
Hmm that's not "deferred" anymore, but it documents the change. Better place: the "Контракты и версии" section — update API ТСП version to 0.2. Let me update that too:
Current:
```
- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec).
```
Change to mention v0.2 additively. Actually the spine says "создаётся на этапе Spec" — outdated already. I'll update: "версия 0.2 draft (аддитивное расширение подписками; v0.1-совместимо)".

And add a line under Deferred? I'll add a "Deferred" entry removal note not needed. Instead add to the top-level a "Delta" note. Let me add a short section right after the header paragraph:

```
Delta-протокол: изменение вводится дельтой `changes/sbp-subscriptions/DELTA.md`; блоки AD-009…AD-011 и правки AD-002/AD-003/AD-005 действуют в статусе Proposed до человеческого решения A3.
```

Good.

Let me apply edits.
Now updating the spine — adding three invariants and delta notes to the affected blocks (via the delta protocol).

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md", new_string="- **Rule**: Изменение финансового статуса платежа и запись исходящего события (outbox) выполняются в одной локальной транзакции. Нарушение , old_string="- **Rule**: Изменение финансового статуса платежа и запись исходящего события (outbox) выполняются в одной локальной транзакции. Нарушение )`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md", new_string="- **Rule**: Повторная доставка любого сообщения не изменяет уже завершённое состояние. Fitness: тест «повторная нотификация/повторный запро, old_string="- **Rule**: Повторная доставка любого сообщения не изменяет уже завершённое состояние. Fitness: тест «повторная нотификация/повторный запро)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md", new_string="- **Rule**: Вызов АБС на зачисление возможен только из состояния `PAID` (подтверждённый НСПК статус). Fitness: проверка недостижимости зачи, old_string="- **Rule**: Вызов АБС на зачисление возможен только из состояния `PAID` (подтверждённый НСПК статус). Fitness: проверка недостижимости зачи)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md", new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now insert new AD blocks after AD-008 and before "## Deferred". Let me view the region around AD-008 end.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md", new_string="- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.\n- **Рекуррентные C2, old_string="- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md", new_string="- Внутренний контракт шлюза (API ТСП): версия 0.2 draft — `docs/contracts/tsp-api.md`; расширение подписками **аддитивно** и совместимо с v, old_string="- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec).")`

Now update the Deferred / contracts section: add a note that автоплатежи/подписки выведены из roadmap в дельту, and update contract version. Let me edit the "Контракты и версии" section and add a Deferred note.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\n  description: >\n    Мерчант-API (ТСП ↔ СБП-шлюз). v0.2 — аддитивное, file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/openapi/tsp-api.yaml")`

Now update the openapi/tsp-api.yaml additively. Let me write the new version carefully. Keep existing content, add paths/components.

I need to be careful with the `Payment` schema: add optional fields. And add new schemas. Add Problem schema. Add error responses on new POST endpoints (409/422/429) with Problem.

Let me write the file. Current file content (52 lines) is known. I'll write a full new file.

Version: 0.2.0.

Let me include:
- info: title, version 0.2.0.
- paths:
  - /v1/payments (post) — unchanged
  - /v1/payments/{paymentId} (get) — unchanged
  - /v1/mandates (post)
  - /v1/mandates/{mandateId} (get)
  - /v1/mandates/{mandateId}/revoke (post)
  - /v1/mandates/{mandateId}/debits (post, get)
- components.schemas:
  - PaymentRequest (unchanged)
  - Payment (existing 3 props + optional paymentType, mandateId, billingPeriod)
  - MandateRequest, Mandate, MandateStatus
  - DebitRequest
  - Problem

Let me write it. Use inline flow style similar to existing for consistency? The existing is compact flow style. I'll use block style for new schemas for readability but keep existing compact. Mixed is fine for YAML.

Actually, to minimize risk of openapi_lint complaints, follow the same style: `{type: string}` inline. I'll use a mix.

Important: mutating endpoints must have Idempotency-Key (openapi_lint checks idempotency of mutating endpoints). Existing POST /v1/payments has it. New POSTs need it too (mandates create, revoke, debits create). Also RFC 7807 errors: include `application/problem+json` responses. Let me add error responses with default.

Let me construct.

For requestBody of new POSTs: content application/json schema.

Let me write:

```yaml
openapi: 3.0.3
info:
  title: СБП-шлюз — API ТСП
  version: 0.2.0
  description: >
    Мерчант-API (ТСП ↔ СБП-шлюз). v0.2 — аддитивное расширение подписками
    (мандаты/рекуррентные списания); совместимо с v0.1: пути /v1/payments*,
    поля и enum Payment.status не изменены (AD-010, ADR-010).
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
          description: Статус платежа (в т.ч. рекуррентного списания по mandateId)
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Payment'}
  /v1/mandates:
    post:
      operationId: createMandate
      summary: Создать согласие плательщика (мандат) и получить ссылку на подтверждение
      parameters:
        - {in: header, name: Idempotency-Key, required: true, schema: {type: string}}
      requestBody:
        required: true
        content:
          application/json:
            schema: {$ref: '#/components/schemas/MandateRequest'}
      responses:
        '201':
          description: Мандат создан, ожидается подтверждение плательщика
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Mandate'}
        '409':
          description: Конфликт идемпотентности
          content:
            application/problem+json:
              schema: {$ref: '#/components/schemas/Problem'}
        '429':
          description: Превышен лимит запросов
          content:
            application/problem+json:
              schema: {$ref: '#/components/schemas/Problem'}
  /v1/mandates/{mandateId}:
    get:
      operationId: getMandate
      parameters:
        - {in: path, name: mandateId, required: true, schema: {type: string}}
      responses:
        '200':
          description: Состояние мандата
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Mandate'}
  /v1/mandates/{mandateId}/revoke:
    post:
      operationId: revokeMandate
      summary: Отозвать согласие (ТСП-инициированный отзыв; отзыв плательщиком приходит событием)
      parameters:
        - {in: path, name: mandateId, required: true, schema: {type: string}}
        - {in: header, name: Idempotency-Key, required: true, schema: {type: string}}
      responses:
        '200':
          description: Мандат переведён в REVOKED (идемпотентно)
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Mandate'}
        '422':
          description: Мандат не может быть отозван из текущего состояния
          content:
            application/problem+json:
              schema: {$ref: '#/components/schemas/Problem'}
  /v1/mandates/{mandateId}/debits:
    post:
      operationId: createDebit
      summary: Инициировать рекуррентное списание по активному мандату
      parameters:
        - {in: path, name: mandateId, required: true, schema: {type: string}}
        - {in: header, name: Idempotency-Key, required: true, schema: {type: string}}
      requestBody:
        required: true
        content:
          application/json:
            schema: {$ref: '#/components/schemas/DebitRequest'}
      responses:
        '201':
          description: >
            Списание принято и поставлено в очередь выравнивания; статус читается
            через GET /v1/payments/{paymentId}
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Payment'}
        '409':
          description: Списание за этот billingPeriod уже существует (уникальность периода)
          content:
            application/problem+json:
              schema: {$ref: '#/components/schemas/Problem'}
        '422':
          description: Списание запрещено (мандат не ACTIVE, вне срока или сверх лимита)
          content:
            application/problem+json:
              schema: {$ref: '#/components/schemas/Problem'}
        '429':
          description: Превышен лимит запросов / сработал допуск при перегрузке
          content:
            application/problem+json:
              schema: {$ref: '#/components/schemas/Problem'}
    get:
      operationId: listDebits
      parameters:
        - {in: path, name: mandateId, required: true, schema: {type: string}}
      responses:
        '200':
          description: Списания по мандату
          content:
            application/json:
              schema:
                type: array
                items: {$ref: '#/components/schemas/Payment'}
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
        paymentType:
          type: string
          enum: [single, recurring]
          description: Вид платежа; отсутствует у v0.1-клиентов => трактуется как single
        mandateId:
          type: string
          description: Мандат, по которому проведено списание (только для paymentType=recurring)
        billingPeriod:
          type: string
          description: 'Период списания (например 2026-10); только для recurring'
    MandateRequest:
      type: object
      required: [tspId, maxAmountPerDebit, limit, frequency, purpose]
      properties:
        tspId: {type: string}
        merchantSubscriptionId: {type: string}
        maxAmountPerDebit: {type: integer, description: Максимум за одно списание, копейки}
        limit:
          type: object
          required: [amount, period]
          properties:
            amount: {type: integer, description: Лимит за период, копейки}
            period: {type: string, enum: [DAY, MONTH, TOTAL]}
        frequency: {type: string, enum: [DAILY, WEEKLY, MONTHLY, ON_DEMAND]}
        validFrom: {type: string, format: date-time}
        validUntil: {type: string, format: date-time}
        purpose: {type: string}
        redirectUrl: {type: string}
    Mandate:
      type: object
      required: [mandateId, tspId, status]
      properties:
        mandateId: {type: string}
        mandateRef: {type: string, description: Идентификатор мандата в ОПКЦ}
        tspId: {type: string}
        merchantSubscriptionId: {type: string}
        status:
          type: string
          enum: [CREATED, PENDING_CONSENT, ACTIVE, SUSPENDED, REJECTED, REVOKED, EXPIRED]
        consentUrl: {type: string, description: Ссылка/QR для подтверждения согласия плательщиком}
        maxAmountPerDebit: {type: integer}
        limit:
          type: object
          properties:
            amount: {type: integer}
            period: {type: string, enum: [DAY, MONTH, TOTAL]}
        validFrom: {type: string, format: date-time}
        validUntil: {type: string, format: date-time}
        activatedAt: {type: string, format: date-time}
        revokedAt: {type: string, format: date-time}
        revocationSource: {type: string, enum: [PAYER, MERCHANT, TSP_REQUEST]}
    DebitRequest:
      type: object
      required: [amount, billingPeriod]
      properties:
        amount: {type: integer, description: Сумма списания, копейки; <= maxAmountPerDebit}
        billingPeriod: {type: string, description: 'Период (например 2026-10) — ключ уникальности успешного списания'}
        description: {type: string}
    Problem:
      type: object
      description: Ошибка в формате RFC 9457 (application/problem+json)
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

Note: openapi_lint "идемпотентность mutating-endpoint'ов" — all POSTs have Idempotency-Key header. Good. But note `Payment` enum in MD docs uses `NULL`? no.

Wait: existing PaymentRequest requires `[amount, merchantOrderId]` but the MD contract says amount required, merchantOrderId optional. I won't change it (that WOULD be a breaking change—removing required). Keep.

Potential issue: contract_diff may treat adding optional properties to `Payment` as non-breaking. Adding new schemas/paths non-breaking. Bumping version minor is fine.

One concern: contract_diff CD-007: "ломающий дифф без смены major info.version". Our diff is non-breaking, so no issue.

Another concern: does openapi_lint complain about `application/problem+json` and about `listDebits` GET with array? Let's just run and see.

Let me write the file.
Now the contract — additive v0.2 without breaking existing consumers.

  `tool_call(arguments={"path": "openapi/tsp-api.yaml", "cwd": "<HARNESS>/runs-v2/cells/wtnkjmc/ws"}, name="mcp__spine__openapi_lint")`
  `tool_call(arguments={"old": "<TMP>.1.yaml", "new": "<HARNESS>/runs-v2/cells/wtnkjmc/ws/o, name="mcp__spine__contract_diff")`

Now run openapi_lint on new contract and contract_diff old→new to verify non-breaking.

  `write_file(content="# Статусная машина мандата (согласия плательщика) и рекуррентного списания — спецификация\n\n- Status: Draft (для ревью на гейте A2; дельта, file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/mandate-state-machine.md")`

Contract lint PASS, contract_diff: 0 breaking, 4 non-breaking (new paths). Note it didn't flag the `Payment` optional fields as changes — maybe it doesn't diff component props deeply or considers them non-breaking silently. Good enough; 0 breaking.

Now: mandate state machine spec, NFR update, contracts docs (tsp-api.md, opkc-adapter.md), rfp update, solutioning.md small edit, README, DELTA.md, PROPOSAL.md, CONSTRAINTS.yaml.

Let me write the mandate state machine spec.
Contract diff is clean: **0 breaking, 4 non-breaking**. Now the mandate state machine spec and NFR.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/nfr.md", new_string="## 7. Рекуррентные C2B-списания (подписки) — новый функционал\n\nДополнение к §1–6 для изменения `changes/sbp-subscriptions` (ADR-008…ADR-0, old_string="## Зависимости (внешние входы для NFR)\n\n- Регламенты НСПК: таймауты, сроки уведомлений, требования к доступности [ТРЕБУЕТ ПРОВЕРКИ — из д)`

Now NFR: append section 7 to docs/nfr.md. Need to keep the existing file intact and add §7 + update the dependencies. Let me edit by inserting before "## Зависимости (внешние входы для NFR)".

Let me read the tail to be precise: the file ends with "## Зависимости (внешние входы для NFR)" list. I'll insert §7 before it and add dependency lines.

Content §7:
```
## 7. Рекуррентные C2B-списания (подписки) — новый функционал

Цели — дополнение к §1–6; измеримы на гейте A4 (моки + тестовый контур НСПК).

| Метрика | Цель | Метод проверки |
|---|---|---|
| Распространение отзыва согласия: от события до запрета новых списаний | p95 ≤ 60 с, p99 ≤ 5 мин; после обработки — 0 новых списаний | Тест «отзыв при активном биллинге», метрика задержки, аудит |
| Активация мандата (от подтверждения плательщиком до `ACTIVE` в шлюзе) | p95 ≤ 5 с, p99 ≤ 15 с (без учёта НСПК) | Метрика процесса |
| Инициация списания (`POST .../debits`, приём + постановка в очередь) | p95 ≤ 300 мс, p99 ≤ 1 с | Нагрузочный тест, APM |
| Завершение списания (инициация → `PAID`/`FAILED`) | p95 ≤ 5 с (без учёта банка плательщика) [ТРЕБУЕТ ПРОВЕРКИ по регламенту НСПК] | Метрика процесса |
| Пиковая пропускная способность биллинга | sustained 300 TPS, burst 1500 TPS ≥ 10 мин в биллинговое окно | Нагрузочный тест пикового профиля |
| Лаг очереди списаний | p95 ≤ 60 с в норме; возраст первого необработанного — алерт по порогу | Мониторинг очереди |
| Дублей списания за период (`mandateId`, `billingPeriod`) | 0 | Тест уникальности периода + сверка |
| Списаний без `ACTIVE`-мандата | 0 | Fitness/тест guard'а |
| Списаний после обработанного отзыва | 0 | Тест гонки «отзыв ↔ списание» |
| Доступность потоков мандатов и списаний | ≥ 99,95 % | SLO-отчёт |
| Недоставленные списания в биллинговое окно | ≤ 0,1 % от инициированных (остальные — в отчёте незавершённых) | Отчёт биллингового окна |
| RPO / RTO (мандаты и списания) | RPO = 0; RTO ≤ 1 ч (без изменений §3) | Chaos-тест, учения DR |
| Сверка мандатов/списаний с НСПК | ежечасная, включена в общую сверку; расхождений — 0 | Reconciliation-отчёт |
| ПДн согласия | маскирование плательщика, шифрование в покое, неизменяемая запись согласия | ИБ-ревью, аудит |

Последствие нарушения (почему цифры): дубль списания или списание без согласия — финансовый и регуляторный инцидент, а не деградация метрики; поэтому целевые значения дублей и списаний без согласия — строго 0, а не «доля».
```

And add dependency lines:
- Регламенты НСПК по подпискам/автоплатежам (лимиты, обязанность уведомления плательщика, тайминги, поведение при отзыве) [ТРЕБУЕТ ПРОВЕРКИ].
- Пиковый профиль биллинга (число ТСП/списаний в окне) — от бизнеса.

Let me edit.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md", new_string="# Контракт API ТСП (мерчант-API) — v0.2 draft\n\n- Status: Draft (для ревью на гейте A1; v0.2 — дельта подписок, для A2/A3)\n- Версия контр, old_string="# Контракт API ТСП (мерчант-API) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фикс)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md", new_string="`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n\n### 3.6 Подписки: согласи, old_string="`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`")`

Now update the narrative contracts:
- `docs/contracts/tsp-api.md` — add §3.6+ mandate/debit sections, update version header to 0.2, §5 webhooks new events, §6 versioning note, §7 open questions. I'll append new sections and update the header/version. To keep it coherent, I'll edit the header and add a new section before "## 6. Версионирование и совместимость", plus update §5 event list and §7.

Actually simpler and cleaner: edit header (version 0.2), then insert a new §3.6 after §3.5, add webhook events in §5, and add open questions. Let me do targeted edits.

Header current:
```
# Контракт API ТСП (мерчант-API) — v0.1 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), AD-003 (spine)
```
Change to v0.2 draft, add delta note, related ADR-008..010.

Then insert §3.6 after §3.5 block. §3.5 ends with:
```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`
```
Then "## 4. Ошибки". Insert between.

§3.6 Mandates and debits (narrative matching openapi).

§5 webhooks: add mandate events.

§6 versioning: add note that v0.2 additive, enum unchanged.

§7 open questions: add mandate-specific.

Let me do edits.
Now the narrative contract docs — additive sections for mandates/debits.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md", new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md", new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`); для рекуррентного списания — то же событие (`paymentType: recurrin, old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md", new_string="- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.\n- Добавление опциональных полей — , old_string="- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.\n- Добавление опциональных полей — )`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md", new_string="1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса., old_string="1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.)`

Now update §4 canonical error codes (add DEBIT_PERIOD_EXISTS, MANDATE_NOT_ACTIVE, MANDATE_REVOKED), §5 webhooks (mandate events), §6 versioning note, §7 open questions.

Let me do targeted edits. Read §4 lines to match exactly.

§4 current codes line:
"Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку."

Add mandate codes.

§5 events list:
"События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`"

Add mandate events.

§6 versioning:
"- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.
- Добавление опциональных полей — обратно совместимо, не требует новой версии."

Add note: v0.1→v0.2 additive, enum unchanged, breaking only in v2.

§7 open questions: add mandate questions.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-011-pikovaya-nagruzka-billing, new_string="**reversible.** Механику выравнивания, допуска и приоритетов можно менять (пороги, размеры пакетов, политику) без смены финансовой модели. , old_string="**reversible.** Механику выравнивания, допуска и приоритетов можно менять (пороги, размеры пакетов, политику) без смены финансовой модели. )`

There's an issue in ADR-011 references: I wrote "ADR-001, ADR-002" as "ADR-001" ok, but I wrote «согласован с уже принятыми» with a typo "già" (Italian). Let me fix that. Also in ADR-011 references I wrote "ADR-004, ADR-009, ADR-012, AD-011" — need to check header. Let me grep for the typo later.

Also need to update the opkc-adapter contract and vendor RFP. Then solutioning.md small note, README, delta, proposal, constraints.

Let me fix the typo in ADR-011 now.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.2 draft\n\n- Status: Draft (для ревью на гейте A1; основа для RFP вендора; v0.2 — ад, old_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1; основа для RFP вендора)\n- Owner:)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |\n| `registerMandate` (v0.2) | реги, old_string="| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |\n| `getReconciliationReport` | вып)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |\n| `mandate.activated` (v, old_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |")`

Now update `docs/contracts/opkc-adapter.md` (internal contract) — add mandate/debit operations and events, bump to v0.2, additive. Then vendor RFP delta.

Let me edit opkc-adapter.md:
- header version 0.2
- §3 add rows to sync operations table
- §4 add events
- §5 reference covers mandate/debit
- §7 NFR add mandate/debit
- §9 open questions

Let me do targeted edits.

Header current:
```
# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.1 draft

- Status: Draft (для ревью на гейте A1; основа для RFP вендора)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-003, ADR-004, AD-004, AD-008
```

Table §3 rows currently:
| `registerTsp` | ... |
| `createPaymentLink` | ... |
| `getPaymentStatus` | ... |
| `cancelPaymentLink` | ... |
| `createRefund` | ... |
| `getRefundStatus` | ... |
| `getReconciliationReport` | ... |

Add after getRefundStatus (or after createRefund) new rows: `registerMandate`, `getMandateStatus`, `revokeMandate`, `createRecurringDebit`, `getDebitStatus`. And extend `getReconciliationReport` type to include mandates/debits (note).

Let me insert rows before `| \`getReconciliationReport\` |`.

Events §4 table: add mandate.* and debit.* rows.

Let me apply edits.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`/`mandateId`; для списания — `paymentId` ядра) в каждый мутирующий вызов.", old_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="| Дубли при ретрае | 0 (идемпотентность по `reference`) | Тест на повторный вызов |\n| Дубли мандатов/списаний при ретрае (v0.2) | 0 (идемп, old_string="| Дубли при ретрае | 0 (идемпотентность по `reference`) | Тест на повторный вызов |")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="3. Поведение ядра при `transport.unavailable` (приём QR в очередь vs отклонение) — политика, утверждается на A2.\n4. (v0.2) **Набор методов, old_string="3. Поведение ядра при `transport.unavailable` (приём QR в очередь vs отклонение) — политика, утверждается на A2.")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="4. Идемпотентность мутирующих операций по `reference` (§5) — **обязательно** (включая v0.2 мандатные операции и списания).", old_string="4. Идемпотентность мутирующих операций по `reference` (§5) — **обязательно**.")`

Now update opkc-adapter §5 (reference for mandate/debit), §7 NFR, §9 open questions, and §8 vendor requirements. Let me do targeted edits.

§5 currently:
```
- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.
```
Change to include mandateId/debit (paymentId).

§7 add rows for mandate/debit (idempotency, reconciliation). Actually §7 NFR table already covers adapter throughput/latency; add mandate/debit specifics:
- Идемпотентность мандатных/списательных операций по `reference` — 0 дублей.
- Сверка мандатов/списаний через `getReconciliationReport type=mandate|debit`.
Let me add two rows.

§9 open questions: add recurring protocol questions.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/rfp/vendor-rfp.md", new_string="**Не входит в scope вендора:** ядро шлюза (API ТСП, статусная машина, сверка, АБС-интеграция) — собственная разработка банка.\n\nДополнение, old_string="**Не входит в scope вендора:** ядро шлюза (API ТСП, статусная машина, сверка, АБС-интеграция) — собственная разработка банка.")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/rfp/vendor-rfp.md", new_string="## 5. Сценарии POC (обязательный этап перед финальным решением)", old_string="## 5. Сценарии POC (обязательный этап перед финальным решением)\n\nНа тестовом контуре НСПК вендор демонстрирует:")`

Now the vendor RFP delta. Add a section §4а or amend §1 scope + §2 gate + §5 POC scenarios. I'll add a new section "## 4а. Дельта подписок (v0.2, ADR-008…ADR-012)" with mandatory criteria and POC scenarios, and add a line in §1. Minimal but real.

Let me insert after §4 (before §5 POC). Add:
- gate G8: мандатные операции + идемпотентность + тестовый контур мандатов.
- POC scenarios P9-P12.
- Weighted criterion note.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/rfp/vendor-rfp.md", new_string="## 5. Сценарии POC (обязательный этап перед финальным решением)\n\nНа тестовом контуре НСПК вендор демонстрирует:\n\n| # | Сценарий | Ожида, old_string="## 5. Сценарии POC (обязательный этап перед финальным решением)\n\n| # | Сценарий | Ожидаемый результат |\n|---|---|---|\n| P1 | Счастливый)`

I accidentally removed the line "На тестовом контуре НСПК вендор демонстрирует:". Let me re-add it before the table. The edit replaced the heading + that line with just the heading. Let me fix.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/rfp/vendor-rfp.md", new_string="| G7 | Передача исходного кода/эскроу на случай прекращения поддержки | Условия эскроу в контракте |\n| G8 (v0.2) | Поддержка мандатных опе, old_string="| G7 | Передача исходного кода/эскроу на случай прекращения поддержки | Условия эскроу в контракте |")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/rfp/vendor-rfp.md", new_string="| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |\n| P9 (v0.2), old_string="| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |")`

Now add gate criterion G8 and POC scenarios P9-P12. Insert G8 after G7 in §2 table, and P9-P12 after P8 in §5 table.

§2 table ends with:
| G7 | Передача исходного кода/эскроу на случай прекращения поддержки | Условия эскроу в контракте |

§5 table ends with:
| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |

Let me add.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/solutioning.md", new_string="Маршрут: **Critical** (значимость 11/15). Настоящий документ — полный Solutioning: контекст, компоненты, потоки, разбиение на ADR, NFR, пла, old_string="Маршрут: **Critical** (значимость 11/15). Настоящий документ — полный Solutioning: контекст, компоненты, потоки, разбиение на ADR, NFR, пла)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/solutioning.md", new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop, old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop)`

Also update §3 weighted criterion "Соответствие контракту opkc-adapter" — mentions §3-4; fine. And §11 checklist. Not essential.

Now update `docs/solutioning.md` §1 roadmap line and add a pointer to the delta. Let me edit the roadmap line:
"Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."
→ "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты. **Автоплатежи/подписки** выведены из roadmap дельтой `changes/sbp-subscriptions` (2026-09-28, ADR-008…ADR-012, `docs/solutioning-subscriptions.md`)."

Also §5 ADR table — maybe add a pointer? Not necessary but good. Let me just edit the roadmap line and add a header note near the top of solutioning.md pointing to the delta.

Header:
```
# Solutioning — Платёжный шлюз СБП (C2B-приём)

Маршрут: **Critical** (значимость 11/15). Настоящий документ — полный Solutioning: контекст, компоненты, потоки, разбиение на ADR, NFR, план гейтов A0–A5, план отката, gaps.
```
Add line: "Дельта «Рекуррентные C2B-списания (подписки)» — `docs/solutioning-subscriptions.md` (2026-09-28)."

Let me apply.

  `write_file(content="# Дельта: sbp-subscriptions — Рекуррентные C2B-списания (подписки ТСП)\n\n- Route: **Critical** (значимость 9/15, `significance_score`) — п, file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md")`

Now the DELTA.md (the required delta covering protected files) and the PROPOSAL.md (the reviewable package with 7 deliverables). Then CONSTRAINTS.yaml rules, README, and gates.

Let me write DELTA.md. It must mention protected files: ARCHITECTURE-SPINE.md, .arch-handoff/CONSTRAINTS.yaml (if changed), and model/ (not changed). delta_guard checks that each changed protected file is mentioned in an active delta's DELTA.md. So DELTA.md must contain the path strings "ARCHITECTURE-SPINE.md" and "CONSTRAINTS.yaml" (or ".arch-handoff/CONSTRAINTS.yaml"). Let me include an explicit "## Затронутые защищённые файлы" section listing them verbatim.

Let me write a full DELTA.md in OpenSpec style + the repo template sections.

Content:
- Route: Critical (полный Solutioning)
- Проблема
- Затронутые защищённые файлы (explicit)
- ADDED (requirements EARS)
- MODIFIED
- REMOVED (none)
- План отката
- Критерии приёмки (checklist)
- Fitness (the rules to add) — mention C-numbers.

Let me write it.

EARS requirements: let me define REQ IDs like REQ-SUB-1..N with EARS.

ADDED:
- REQ-SUB-1: When ТСП регистрирует согласие плательщика (POST /v1/mandates), the шлюз shall создать мандат и вернуть consentUrl за ≤ 5 с (p95), не создавая дубль при повторе с тем же Idempotency-Key.
- REQ-SUB-2: When плательщик подтверждает согласие, the шлюз shall перевести мандат в ACTIVE и записать неизменяемую аудит-запись согласия ≤ 5 с (p95) от события.
- REQ-SUB-3: If мандат не в статусе ACTIVE, then the шлюз shall отклонить инициацию списания (422) и не создавать списание.
- REQ-SUB-4: When ТСП инициирует списание с billingPeriod, the шлюз shall создать не более одного успешного списания на (mandateId, billingPeriod) и вернуть 409 при повторе периода после успеха.
- REQ-SUB-5: When поступает событие отзыва согласия, the шлюз shall запретить новые списания по мандату; while мандат REVOKED, the шлюз shall не создавать ни одного нового списания; запрет вступает в силу ≤ 60 с (p95).
- REQ-SUB-6: When списание подтверждено ОПКЦ (debit.paid), the шлюз shall зачислить средства в АБС только из состояния PAID (AD-005) и не более одного раза.
- REQ-SUB-7: While биллинговое окно перегружено, the шлюз shall выравнивать списания очередью с приоритетом мандатных событий/отзыва и притормаживать приём (429/503), не создавая неограниченный бэклог.
- REQ-SUB-8: If ТСП-клиент использует только v0.1 (нет знания о мандатах), then the шлюз shall обслуживать его без изменений (совместимость v0.1).
- REQ-SUB-9: The шлюз shall не допускать автоматического fallback списания на другой способ оплаты.

MODIFIED:
- AD-002: extend to mandate/debit atomic transitions.
- AD-003: idempotency keys extended.
- AD-005: guard added.
- AD-007: consent PII/audit covered (no rule change).
- solutioning.md scope: автоплатежи из roadmap → в scope.
- contract v0.1 → v0.2.
- nfr.md: new §7.
- opkc-adapter v0.1 → v0.2.
- RFP: +G8, P9–P12.

REMOVED: none. Explicitly state "нет; ничего не удаляется и не сужается (AD-010)".

Fitness: list the new rules with ids C-101.. maybe. Let me define in CONSTRAINTS.yaml as C-101..C-107 and mention.

Let me write DELTA.md then PROPOSAL.md.

I'll use the repo's delta template structure (Проблема/ADDED/MODIFIED/REMOVED/План отката/Критерии приёмки) plus extra sections.

Let me write.
Now the delta (covers protected files) and the reviewable change package.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md")`

I created the file with `arch-be delta new` earlier; write_file requires I read it first. I already saw its content via cat earlier, but the tool requires read_file. Let me read then write.

  `write_file(content="# Дельта: sbp-subscriptions — Рекуррентные C2B-списания (подписки ТСП)\n\n- Route: **Critical** (значимость 9/15, `significance_score`) — п, file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md")`
  `write_file(content="# Пакет изменения: Рекуррентные C2B-списания СБП (подписки ТСП)\n\n- Date: 2026-09-28\n- Status: **Proposed — выносится на архитектурное ре, file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md")`

Now the PROPOSAL.md — the reviewable package covering the 7 deliverables explicitly, including the A3 machine-readable package with decided_by empty. This is the main artifact for the architectural decision. Let me write it well: significance table, impact, decision summary (ADR index), contract changes, NFR summary, acceptance criteria + rollback, human decisions.

Let me include the significance trigger table (true/false) and note that route is a function of declared triggers.

Also include the A3 package.

Write it.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="# Fitness-правила для `arch control check` (схема control::check).\n# Этап: решение (до кода). После выбора стека и начала реализации hando, old_string="# Fitness-правила для `arch control check` (схема control::check).\n# Этап: решение (до кода). После выбора стека и начала реализации hando)`

Now update `.arch-handoff/CONSTRAINTS.yaml` to add rules C-101..C-107. I need to read it again (already have). Let me craft rules that pass now.

Rules (textual, no command_succeeds to avoid exec trust issues):
- C-101 mandate-required-for-debit: must_contain glob ARCHITECTURE-SPINE.md pattern 'AD-009' — trivial. Better: must_contain in docs/adr/ADR-009*.md pattern 'только при мандате в статусе `ACTIVE`'? Let me use a pattern that exists.
  Let me define rules checking the new invariants are recorded (traceability), plus contract preservation.

Design:
```yaml
  - id: C-101
    name: mandate-required-for-recurring-debit
    type: must_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'только при мандате в статусе `ACTIVE`'
    severity: error
  - id: C-102
    name: debit-unique-per-billing-period
    type: must_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: '\(`mandateId`, `billingPeriod`\)'
    severity: error
  - id: C-103
    name: revocation-blocks-new-debits
    type: must_contain
    glob: "docs/adr/ADR-009-*.md"
    pattern: 'запрещает все \*\*новые\*\* списания'
    severity: error
  - id: C-104
    name: credit-only-from-paid-preserved
    type: must_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'зачисление по-прежнему возможно только из `PAID`'
    severity: error
  - id: C-105
    name: tsp-api-payment-paths-preserved
    type: must_contain
    glob: "openapi/tsp-api.yaml"
    pattern: '(?m)^  /v1/payments:'
    severity: error
  - id: C-106
    name: tsp-api-payment-status-enum-unchanged
    type: must_contain
    glob: "openapi/tsp-api.yaml"
    pattern: 'enum: \[CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED\]'
    severity: error
  - id: C-107
    name: retries-bounded-with-jitter
    type: must_contain
    glob: "docs/adr/ADR-011-*.md"
    pattern: 'экспоненциальный backoff с джиттером'
    severity: warn
```

Wait — the existing file uses `name:` only, no `id`. The schema in existing file:
```yaml
rules:
  - name: adr-set-complete
    type: file_exists
    path: docs/adr/ADR-001-outbox.md
    severity: error
```
No `id` field used but fitness-function-catalog shows `id`. Adding `id` might be fine, but to be safe and consistent with the repo, I'll follow existing style (name/type/glob/pattern/severity) and prefix names with c101- etc. Actually DELTA.md references C-101…C-107 as ids. Hmm. Let me include `id:` field too — the catalog examples show `id` is accepted (`- id: C-01`). But the repo's existing file doesn't use ids. Risk: the engine might reject unknown field or might accept. The catalog says example `- id: C-01 ... type: must_not_contain`. So `id` is a known field. I'll include both `id` and `name` — should be fine. If fitness_check fails I'll adjust.

Also need to double-check the `(?m)^  /v1/payments:` pattern — the YAML value contains a colon; I must quote the whole pattern. And must_contain matches against whole file with regex; `^` without (?m) is start of file — I add (?m). Good.

Also note: `must_contain` glob `docs/adr/ADR-009-*.md` — matches the new file. Good. Ensure the exact text exists: I wrote in ADR-009: "он запрещает все **новые** списания" — let me check exact: "он запрещает все **новые** списания и передаёт «осевшее»..." Yes. Pattern `запрещает все \*\*новые\*\* списания`. In YAML single-quoted string, backslashes are literal, so `'запрещает все \*\*новые\*\* списания'` gives regex `запрещает все \*\*новые\*\* списания` which matches literal `запрещает все **новые** списания`. Good.

ADR-011 text: "внутри адаптера — экспоненциальный backoff с джиттером (ADR-003)". Yes matches pattern 'экспоненциальный backoff с джиттером'.

Spine text AD-009: "рекуррентное списание инициируется только при мандате в статусе `ACTIVE`, в пределах..." — pattern 'только при мандате в статусе `ACTIVE`' matches. Note backticks in single-quoted YAML are fine.

Spine AD-005 delta: "зачисление по-прежнему возможно только из `PAID` (ADR-008, ADR-009)" — pattern matches.

Spine AD-009: "не более одного **успешного** списания на (`mandateId`, `billingPeriod`)" — pattern `\(`mandateId`, `billingPeriod`\)` — in YAML single quotes, backslash-paren literal → regex escaped parens. Good.

Let me read CONSTRAINTS.yaml and edit.

Also: anti-weakening check compares rule composition with base; adding rules is strengthening — fine. But there's a risk: `fitness_check` compares and might complain if rules have no `severity`? Existing has severity. Fine.

Let me edit.
Now adding the fitness rules for the new invariants (protected file — covered by the delta).

  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wtnkjmc/ws"}, name="mcp__spine__fitness_check")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md"}, name="mcp__spine__spine_lint")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wtnkjmc/ws && echo \"==== delta list ====\"; arch-, description="Validate delta structure and guard coverage")`

Now run fitness_check to verify the new rules pass and the anti-weakening doesn't complain.

Then run spine_lint, delta_guard, and the gate.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wtnkjmc/ws && arch-be gate --repo . 2>&1 | head -6, description="Run the unified architectural gate")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wtnkjmc/ws"}, name="mcp__spine__architect_review")`

Interesting: delta_guard says protected among changed: 1 — only ARCHITECTURE-SPINE.md. It didn't count `.arch-handoff/CONSTRAINTS.yaml` as protected? Default protect list is `model/`, `ARCHITECTURE-SPINE.md`, `CONSTRAINTS.yaml` (basename?). It says protected: 1. Maybe the default protects literal path `CONSTRAINTS.yaml` at root, not `.arch-handoff/CONSTRAINTS.yaml`. Hmm — the helps said default: `model/, ARCHITECTURE-SPINE.md, CONSTRAINTS.yaml`. So it matched only ARCHITECTURE-SPINE.md. Anyway PASS. And DELTA.md mentions both — fine.

fitness_check: 14 rules, 0 violations, no weakening. 

Now run the full gate `arch-be gate --repo .` and `architect_review` to see the overall verdict and the auto-route. Also let me run `evidence_verify`? Not needed.

Let me run gate.

Also I should update README.md (structure/status) — the README mentions docs and status. Let me add the change to the structure list. And note the §7 NFR. Let me do that after gate.

Let me run gate + architect_review.
All green so far. Now the full gate and composite architectural review.

  `skill(skill="agent-delegation")`

Gate PASS. Note: auto-route detected Fast (score 1, only api_contract_change) because the diff-based detector only sees openapi change; it doesn't know about the ADRs/spine (detectors look at code/contracts). This is a discrepancy worth calling out honestly in PROPOSAL/report: the gate's auto-route is derived mechanically from the git diff and under-detects here (no code, no model), whereas the declared significance is Critical. I should note that in the final summary and perhaps in PROPOSAL. Actually, the significant thing: route auto = Fast because diff has no new component/vendor/security-boundary markers. The declared route via significance_score is Critical. Per skill, "Всегда помечай, что маршрут — функция ЗАЯВЛЕННЫХ триггеров". I already did. Let me add a short "Verification" note to PROPOSAL §1 or a separate section mentioning the gate outcome and this discrepancy. Good idea — honest reporting.

Now: run the split-judge rubric on one ADR and/or the PROPOSAL. rubric_list failed (no assets rubrics dir). But rubric_prompt accepts a rubric path OR name. Let me test rubric_prompt with rubric = `.arch-handoff/RUBRIC.yaml` and target = the PROPOSAL. Then I'd have to produce k answers myself and call rubric_verify — that's the split-judge. It's a fair amount of work, and the RUBRIC is `handoff_quality`, aimed at handoff packages, not this proposal. Hmm.

Alternatively, since the repo installed the `spine-adr-judge` skill and rubric assets are missing, the judge route may not be available. Let me test `rubric_list`/`rubric_prompt` quickly to see if it works with the repo's RUBRIC.yaml. If it does, I'll run a judge on one ADR (say ADR-009) using a dynamic-ish approach? Actually handoff_quality doesn't fit ADR. There's no adr_quality rubric file in the repo. Without assets, I can't use the anchor rubrics.

Option: Run the `adversarial-review` skill via an independent subagent (fresh context) — that's the more valuable independent check, and it's explicitly an installed methodology. I'll delegate to a general-purpose subagent with a precise prompt: read the package files, apply the 5 lenses, return VERDICT READY/NOT-READY with evidence-based findings. It runs in a separate context → genuine independence from my authorship.

Let me also test rubric_prompt with the repo RUBRIC against the handoff-ish PROPOSAL? It's about handoff_quality; PROPOSAL isn't a handoff. Marginal value. I'll skip rubric and do adversarial review by subagent, plus a `verdict_explain` passport maybe.

Actually the task says "используй их по назначению" (use skills/tools as intended). The adversarial review is directly named in the user's requested deliverable implicitly? The user asked for "архитектурный пакет ... чтобы его можно было вынести на архитектурное решение". Adversarial review strengthens it. I'll do it.

Let me launch the subagent in foreground (I need the result before finalizing). Per instructions, top-level subagents run in background by default; set run_in_background: false to get result inline. Let me do that.

Wait — the adversarial review should be of MY package. The subagent must have repo access (same cwd). It's a general-purpose agent with tools. I'll give it a precise brief and ask for the verdict format. Since it's a fresh context, it's independent.

Let me write the delegation prompt carefully (load agent-delegation skill? The instruction says load before writing a delegation prompt. Let me load it to be compliant... It's a bundled skill. I'll invoke it. Actually invoking the skill tool loads guidance; it's cheap. But it may be verbose. The instruction in the Agent tool description: "Before writing a delegation prompt, load the `agent-delegation` skill". Let me do it quickly.

Hmm, that adds a round-trip. But guidance compliance matters. Let me load it.

Actually, let me reconsider: is delegating worth it? It gives genuine independent review (adversarial-review skill demands independent reviewer: "Ревьюер = автор" is an antipattern). Yes, worth it. Let me load the skill then delegate.

Also, I should add README update and a note about gate/auto-route mismatch. And write REVIEW.md consolidating the adversarial verdict.

Let me load agent-delegation skill first.
Gate is PASS. The auto-route detector reads only the diff and scores it Fast — the declared (and correct) route is Critical; I'll flag that explicitly. Now let me run an independent adversarial review of the package.

  `agent(description="Adversarial review of change package", subagent_type="general-purpose", run_in_background=false)`

Now delegate the adversarial review. Fresh context; give all needed context: files, the change, the lenses, output format. Ask for research only (read-only) — no code changes. Return verdict + findings with evidence.

I'll set run_in_background: false to get it inline.

Prompt should instruct: read the specified files; apply adversarial-review lenses; verdict READY/NOT-READY; findings with severity blocker/major/minor and evidence (file:section quote); focus on: gaps in the package w.r.t. the 7 requested deliverables, inconsistencies between docs, unverified claims, missing negative scenarios, contract breaking risk, NFR measurability, rollback feasibility, spine/ADR contradictions, and whether ADR alternatives/negatives/reversibility are genuinely present. Also verify claims mechanically where possible (contract_diff, openapi_lint) — it has tools.

Also ask it to check consistency: e.g., does DELTA.md claim match files; does openapi enum match C-106; does ADR-011 reference numbering correct; does PROPOSAL §4 claims match actual files.

Keep output concise-ish but with findings.

Let me launch.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-009-konsistentnost-i-idempote, offset=18, limit=45)`

Excellent, the independent adversarial review found real, material defects. Verdict NOT-READY. I should address the blockers/majors in the package, then re-run the review or at least fix and note. The task is to deliver a good package; I should fix the legitimate findings. This is exactly the value.

Let me triage:

1. **[blocker] Double debit under concurrency** — Real. The mechanism must reserve the period at initiation. Fix: unique constraint on (mandateId, billingPeriod) for **all non-terminal** debits (or a separate reservation row), plus handle constraint hit at initiation with 409. And define behaviour if a second PAID arrives for an already-won period (constraint hit at PAID → alert + refund policy path). Update ADR-009 Decision 2, spec T1r, NFR. Also re-validate at dispatch.

2. **[blocker] Refund of debits not transportable** — Real. `createRefund` keyed by `qrId`; debit has no qrId. Fix: add debit reference to refund operations/events in opkc-adapter (§3 createRefund accepts `debitRef`/`reference`; §4 refund.confirmed carries debitRef), and note refund path for debits. Update ADR-008/009 or contract.

3. **[major] Payer identity missing** — Real. Add payer reference fields to MandateRequest/Mandate (masked) and mandate events. Note: in СБП, the payer is identified by the consent link/QR issued by ОПКЦ, and the mandate binds at the bank; the merchant may not know the payer. But the design claims masked payer id stored. Add optional `payerId` (masked) — provider may populate it after activation; and mandate events carry it. I'll add `payerRef` (opaque/masked) to Mandate and mandate.activated event, and note it's populated on activation, `[ТРЕБУЕТ ПРОВЕРКИ]`.

4. **[major] Guard only at initiation, queue defers** — Real. Add dispatch-time re-validation (ре-валидация при отправке) as a rule + test.

5. **[major] frequency/limit not enforced** — Real. Specify per-period counter/consumption mechanism and frequency check. Add to ADR-009 Decision 1 and spec.

6. **[major] fitness textual vs behavior** — Real. Label C-101..C-104/C-107 as traceability guards, and note behavioral checks required at A4 (rules template / command_succeeds). Update DELTA/PROPOSAL wording + rules names/comments.

7. **[major] C-105 too narrow** — Real. Add sub-path pattern and a comment; maybe add C-108 for `/v1/payments/{paymentId}` and C-109 checking PaymentRequest required unchanged. Let me extend C-105 pattern to match both paths, or add C-108.

8. **[major] Event naming contradiction (debit.completed vs payment.completed)** — Real. ADR-010 Decision 4 says new webhook events `debit.completed/debit.failed` normalized to payment.completed/failed — contradictory. Fix ADR-010 to state the canonical set: debits reuse `payment.completed`/`payment.failed`; internal/ОПКЦ events are `debit.paid`/`debit.rejected` but TSP-facing stays payment.*. Remove debit.completed/failed from ADR-010.

9. **[major] NFR contradictions** — Real. Qualify: "0 новых инициаций после отзыва" (not zero settled in-flight); "0 потерянных; ≤0.1% отложенных/в отчёте незавершённых". Fix NFR §7 + DELTA acceptance wording.

10. **[major] Rollback triggers not numeric** — Real. Add numeric thresholds and fate of queued accepted debits. Fix ADR-012 + PROPOSAL §7.

11. **[major] Peak target has no capacity basis / conflicts with 200/500** — Real. Add a capacity budget statement incl. one-off flow, raise adapter/gateway capacity requirement accordingly, and update RFP weight/P6. Fix NFR §7 (note capacity budget), opkc-adapter §7 (raise to 1500 burst), vendor-rfp §3/§5 P6 & §4. Or lower target. I'll add a capacity note and raise adapter requirement + RFP P13.

12. **[minor] billingPeriod free-form** — Add `pattern` to DebitRequest.billingPeriod (e.g. `^[0-9]{4}-(0[1-9]|1[0-2])(-W[0-9]{2})?$` for monthly/weekly? Keep simpler: `^[0-9]{4}-[0-9]{2}$` and note DAILY uses `YYYY-MM-DD`). Let me define: canonical format per frequency: MONTHLY `YYYY-MM`, WEEKLY `YYYY-Www`, DAILY `YYYY-MM-DD`. Pattern can be broad: `^\d{4}-(\d{2}(-\d{2})?|W\d{2})(-[A-Za-z0-9]+)?$`. Simpler: add pattern `^[0-9]{4}-[0-9]{2}(-[0-9]{2})?$` and describe. I'll add a pattern and description.

13. **[minor] SUSPENDED→ACTIVE no mechanism** — Add suspend/resume endpoints (small) or name mechanism. Add `POST /v1/mandates/{id}/suspend` and `/resume`? That grows API. Simpler: state that resume is TSP-initiated via existing revoke? No. I'll add `POST /v1/mandates/{mandateId}/suspend` and `/resume` — but that's more contract surface. Alternatively define M6/M7 as triggered by ТСП through support/operational procedure (4-eyes) — but then it's not API. Given "no new optional field" concerns, adding two POST paths is additive and cheap. I'll add them to OpenAPI + spec + contract. Hmm, more edits. Let me instead make M6 automatic (dunning) and M7 a **manual operational action with 4-eyes** documented in spec (no API), matching AD-006 4-eyes for manual ops. That's defensible and minimal: name the mechanism/owner. I'll do that (spec M6/M7 fix + note).

Actually the review's point is "no mechanism exists". Naming an operational 4-eyes procedure is a mechanism. But ТСП would want self-service resume. I'll add the two endpoints — it's cleaner and reversible. Hmm, but the more I add, the more lint/consistency. Let me add endpoints; it's additive and I control it.

Let me decide: add `POST /v1/mandates/{mandateId}/suspend` and `POST /v1/mandates/{mandateId}/resume`, with Idempotency-Key. Update openapi, tsp-api.md §3.6.3 block, spec M6/M7, and error codes. And remove open question #8 (which asked whether suspend is needed) → now resolved. Good.

14. **[minor] parent spec not updated** — Fix: state explicit override in mandate-state-machine header, or edit state-machine.md. Cleanest: add a short "Изменения дельтой" note to `docs/spec/state-machine.md` (it's not protected; delta covers mention). Let me add a note section referencing the recurring entry and reconciliation extension. This resolves "parent spec now incomplete".

15. **[minor] RFP stale** — Fix §4 "все 8 типов" → "все типы (14–15 с v0.2)", weights P6, add peak POC. Sync.

16. **[minor] new_component=false vs new module** — The review says flag true or justify. I'll justify in PROPOSAL §1: mandate module is a module inside the existing gateway component, not a new deployable component; and note the queue/scheduler is a new infra element but not a new bounded context. Hmm — but honestly, a new queue/scheduler + module could be "new_component". Since route unaffected, and to be honest, I'll set `new_component: true` and re-run significance_score (score would be 10 → still Critical). Let me set true and update the table + re-run. That's more honest.

17. **[minor] POST /v1/mandates failure semantics** — Define: if adapter call to ОПКЦ times out, mandate stays `CREATED` and is retried; API returns 201 with `CREATED` (async), not an error; consentUrl may be absent until `PENDING_CONSENT`. REQ-SUB-1 should say consentUrl ≤5s p95 when ОПКЦ available, otherwise `CREATED` + webhook. Fix openapi response description + tsp-api + DELTA REQ-SUB-1.

18. **[minor] delta_guard doesn't protect .arch-handoff/CONSTRAINTS.yaml** — The default protect list uses basename `CONSTRAINTS.yaml`. Actually it matched only ARCHITECTURE-SPINE.md. To gate the rules file, add `protect:` config? That's `arch-harness.toml` config or `--protect` flag. The gate runs `delta_guard` with defaults. I could add a root-level `CONSTRAINTS.yaml`? No. I could note it as a process gap and, if there's a config file, add protect. Let me check if `arch-harness.toml` exists. Earlier `ls` showed no arch-harness.toml. Creating config might change gate behavior. Alternatively, the repo's accepted way: mention in PROPOSAL as a residual gap for the architect. But it's fixable: `arch-be delta guard --protect` is a CLI flag, not persisted. Does config support `[delta] protect`? Unknown. I'll note it as a residual process gap (honest) rather than inventing config. Actually, maybe I can check `arch-be` config docs quickly. Let me not over-engineer; I'll note it in PROPOSAL §9 residual/gaps and in REVIEW. Hmm, but the review flagged it as a finding. I can partially mitigate by noting the gate's default covers ARCHITECTURE-SPINE.md and that CONSTRAINTS.yaml edits are additionally guarded by `rule_weakened` (which passed) — indeed `rule_weakened` DID cover the constraints file. So there IS a gate on that file (anti-weakening), just not delta-coverage. That's a reasonable answer: strengthening edits to rules are allowed; weakening is blocked by `rule_weakened`. I'll note that.

OK. That's a lot of fixes. Let me implement the substantive ones. I'll be efficient with edits.

Let me also add a REVIEW.md documenting the adversarial review and disposition of findings. And then re-run gates.

Given the volume, let me prioritize blockers + majors (1-11) and quick minors (8,9,10,12,13,14,15,16,17), and #18 as documented note.

Let me start.

### Fix 1: double debit + reservation + dispatch re-validation + limit/frequency accounting
Update ADR-009 Decision 1, 2, and add decision about reservation & dispatch re-validation & per-period limit counter. Rewrite parts of ADR-009.

Current ADR-009 Decision 1:
"1. **Guard «активного согласия» на инициации.** Списание может быть инициировано, только если мандат в статусе `ACTIVE`, текущее время в пределах `validFrom`/`validUntil`, сумма не превышает лимитов, а отзыв не обработан. Иначе — отказ (`422`/`409`) без создания списания. Проверка и создание списания — в одной транзакции с записью намерения в outbox (AD-002)."
Change to add: reserve period (unique key on all non-terminal debits), re-validate at dispatch, per-period limit counter.

Decision 2 currently: unique constraint on успешных. Change to "на уровне БД резервируется период: уникальный ключ (`mandateId`, `billingPeriod`) на все **неотменённые/непроваленные** списания (резервация при инициации); ..." and behavior at PAID if conflict.

Let me rewrite Decision 1 and 2 wholly, and add Decision 8 about dispatch-time re-validation and per-period counters, and mention frequency check.

This is a big rewrite of ADR-009. Let me rewrite the Decision section via edit.

Let me read ADR-009 currently to edit precisely. I wrote it, I know it. Let me do a targeted replacement of the decision block (items 1-7).

Actually simpler: replace item 1 and item 2 text, and add items 8 and 9, and fix item 3 wording ("уникальность по успешным" mention) and item 7 ("достаточно ограничения БД").

Let me do edits.

Also spec T1r guard update, and NFR already says 0 duplicates — keep but mechanism now sound.

Also §Consequences Negative mentions "уникальность «по успешным списаниям»" — update.

Let me carefully rewrite ADR-009. I'll replace the whole "## Decision" ... "## Alternatives Considered" region.

I need the exact current text. Let me read the file region.
The independent review returned **NOT-READY** with substantive findings. These are legitimate — I'll fix them. Let me read the files I need to revise precisely.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-009-konsistentnost-i-idempote, new_string="1. **Guard «активного согласия» — при инициации и повторно при отправке.** Списание может быть инициировано, только если мандат в статусе `, old_string="1. **Guard «активного согласия» на инициации.** Списание может быть инициировано, только если мандат в статусе `ACTIVE`, текущее время в пр)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-009-konsistentnost-i-idempote, new_string="3. **Списание «в полёте» не откатывается вслепую.** Если отзыв обработан после отправки списания в ОПКЦ, шлюз **не пытается отменить списан, old_string="3. **Списание «в полёте» не откатывается вслепую.** Если отзыв обработан после отправки списания в ОПКЦ, шлюз **не пытается отменить списан)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-009-konsistentnost-i-idempote, new_string="7. **Согласованность обеспечивается транзакцией и сверкой, а не распределёнными блокировками**: guard + резервация периода (уникальный ключ, old_string="7. **Согласованность обеспечивается сверкой, а не распределёнными блокировками**: уникальное ограничение периода + идемпотентность по `refe)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-009-konsistentnost-i-idempote, new_string="- Уникальность периода требует управляемого освобождения: отменённое/провалившееся до отправки списание обязано вернуть период отдельным ау, old_string="- Уникальность «по успешным списаниям» требует аккуратной работы с повторными попытками: неуспешные списания периода не должны блокировать )`

Now rewrite ADR-009 Decision items 1, 2, 3, 7 and Negative bullet. Let me apply edits.

Edit A: item 1 — add reservation, dispatch re-validation, limit/frequency accounting.

New item 1:
```
1. **Guard «активного согласия» на инициации и повторная проверка при отправке.** Списание может быть инициировано, только если мандат в статусе `ACTIVE`, текущее время в пределах `validFrom`/`validUntil`, сумма не превышает `maxAmountPerDebit`, не исчерпан лимит периода (`limit`) и не нарушена частота (`frequency`), а отзыв не обработан. Иначе — отказ (`422`) без создания списания. Проверка и создание списания (вместе с **резервацией периода**, п.2) — в одной транзакции с записью намерения в outbox (AD-002). Перед фактической отправкой в ОПКЦ (dispatch из очереди, ADR-011) guard **перепроверяется**: за время ожидания в очереди мандат мог быть отозван/приостановлен, а период — занят другим списанием.
```
Also per-period consumption: add item about counters. Put into item 1 or new item. Let me add to item 1 a sentence: "Расход лимита периода учитывается счётчиком по (mandateId, period) в той же транзакции (счётчик + резервация), чтобы конкурирующие списания не превысили лимит."

Edit B: item 2 — reservation instead of "успешных":
```
2. **Идемпотентность и резервация периода на двух уровнях:**
   - **Уровень API**: `Idempotency-Key` ТСП (ADR-002) — повтор запроса возвращает тот же `paymentId`;
   - **Уровень периода**: при инициации **безусловно резервируется** период — уникальный ключ (`mandateId`, `billingPeriod`) на все списания, кроме отменённых до отправки/проваленных до резервации; повтор (в т.ч. с другим `Idempotency-Key`) получает `409 DEBIT_PERIOD_EXISTS`. Резервация — вставка строки в той же транзакции, что и guard: конкурентная попытка упирается в уникальный ключ БД, а не в «прочитал-потом-записал». Провалившееся до отправки списание освобождает период (освобождение — отдельный статус, аудируемое действие), успешное — удерживает.
```
And add: "Если нотификация `PAID` приходит по периоду, уже удерживаемому другим списанием (аномалия/поздний дубль), шлюз **не зачисляет второй раз**: алерт + отчёт незавершённых + политика возврата (A3)."

Edit C: item 3 — clarify "осевшее" and that in-flight not counted in "0 new initiations".
```
3. **Списание «в полёте» не откатывается вслепую.** ... запрещает все **новые инициации**... «осевшее» (уже отправленное в ОПКЦ) списание ... алерт ... 
```

Edit D: item 7 — update since reservation is now in DB.
```
7. **Согласованность обеспечивается транзакцией и сверкой, а не распределёнными блокировками**: резервация периода (уникальный ключ БД) + guard в одной транзакции + идемпотентность по `reference` закрывают дубли; сверка (ADR-004) расширяется на мандаты и списания. Выборы лидера/распределённые локи не вводятся — резервация и уникальный ключ дают нужную гарантию без координации между узлами.
```

Edit E: Negative bullet update:
"Уникальность «по успешным списаниям»..." → "Резервация периода требует управляемого освобождения: отменённое/провалившееся до отправки списание должно вернуть период, иначе повторная попытка в том же периоде заблокирована (сложность модели состояний и аудита)."

Also Alternatives C wording: "Избыточно: уникальность достигается ограничением БД" — fine, reservation is the constraint.

Also add a decision item 8? I covered dispatch re-validation in item 1 and counters in item 1/2. Good.

Let me apply these edits.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/mandate-state-machine.md", offset=36, limit=45)`

Good. Now update the mandate-state-machine spec: T1r guard (reservation, limits, frequency), dispatch re-validation, M6/M7 mechanism, refunds for debits, payer field, and the "parent spec override" note.

Let me read the spec to edit precisely. I wrote it; let me edit key parts.

Edits:
1. Header: add note that this spec introduces overrides/additions to parent spec (recurring entry) — resolving finding 14.
2. §3 invariants: add "резервация периода" and "расход лимита/частота".
3. T1r guard: update.
4. §4 add dispatch re-validation row T1r-d and refund note.
5. M6/M7 mechanism: specify suspend/resume API.

Also need to add suspend/resume to openapi + tsp-api. Let me decide: add endpoints. Let me do it.

Let me first read the spec file.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/mandate-state-machine.md", new_string="- Родительская спецификация: `docs/spec/state-machine.md`. Изменение **добавляет** рекуррентный вход (`MANDATE_BOUND`/`DEBIT_SUBMITTED` вме, old_string="- Родительская спецификация: `docs/spec/state-machine.md` (статусная машина платежа — не изменяется, дополняется входом)")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/mandate-state-machine.md", new_string="## 3. Инварианты мандата\n\n- **Списание невозможно без `ACTIVE`-мандата** (AD-009): из `CREATED`/`PENDING_CONSENT`/`SUSPENDED`/`REVOKED`/`, old_string="## 3. Инварианты мандата\n\n- **Списание невозможно без `ACTIVE`-мандата** (AD-009): из `CREATED`/`PENDING_CONSENT`/`SUSPENDED`/`REVOKED`/`)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/mandate-state-machine.md", new_string="| № | From | To | Триггер | Guard | Действие |\n|---|---|---|---|---|---|\n| T1r | — | `CREATED` | `POST /v1/mandates/{mandateId}/debits` |, old_string="| № | From | To | Триггер | Guard | Действие |\n|---|---|---|---|---|---|\n| T1r | — | `CREATED` | `POST /v1/mandates/{mandateId}/debits` |)`

Let me apply edits to the spec:

Edit 1 (header note): add after "Связано:" line a note about additions/overrides. Let me read the header lines 1-9. It shows:
```
# Статусная машина мандата (согласия плательщика) и рекуррентного списания — спецификация

- Status: Draft (для ревью на гейте A2; дельта к `docs/spec/state-machine.md`)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-008, ADR-009, ADR-011, ADR-012, AD-002, AD-003, AD-005, AD-009
- Родительская спецификация: `docs/spec/state-machine.md` (статусная машина платежа — не изменяется, дополняется входом)
```
I'll change the last line to note explicit additions and that parent spec gets a cross-reference note.

Edit 2: invariants — add reservation/limit/frequency/payer fields.

Edit 3: T1r guard.

Edit 4: add T1r-d row and dispatch re-validation; add refund note.

Edit 5: M6/M7 mechanism — I'll add suspend/resume endpoints. Need to update §2 table M6/M7 triggers to reference API.

Let me do these edits. Also the spec says "Списание — платёж ... Состояния — как в docs/spec/state-machine.md §1" — add note about reconciliation list extension.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/mandate-state-machine.md", new_string="| M6 | `ACTIVE` | `SUSPENDED` | политика dunning (N неуспешных списаний) **или** `POST /v1/mandates/{id}/suspend` (ТСП) | согласие не отозв, old_string="| M6 | `ACTIVE` | `SUSPENDED` | политика dunning (N неуспешных списаний) / приостановка ТСП | — | outbox, вебхук `mandate.suspended`; новые)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/mandate-state-machine.md", new_string="- После обработки отзыва — ни одной новой **инициации** списания (AD-009); списание, «осевшее» после отзыва (уже отправленное в ОПКЦ), — от, old_string="- После обработки отзыва — ни одного нового списания (AD-009); списание, «осевшее» после отзыва, — отдельный операционный разбор по политик)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/mandate-state-machine.md", new_string="- Вебхуки ТСП: `mandate.pending`, `mandate.activated`, `mandate.rejected`, `mandate.suspended`, `mandate.resumed`, `mandate.revoked`, `mand, old_string="- Вебхуки: `mandate.pending`, `mandate.activated`, `mandate.rejected`, `mandate.suspended`, `mandate.resumed`, `mandate.revoked`, `mandate.)`

Now add refunds-for-debits note in spec §4 and M6/M7 mechanism, plus §6 webhooks naming fix (debit.* contradiction), and refunds.

Let me add after the forbidden transitions block or in §6. Let me add a §4.1 "Возвраты по списаниям" and fix §6.

Also M6/M7: let me edit §2 table rows M6/M7 to reference suspend/resume endpoints, and I'll add those endpoints.

Let me read the M6/M7 rows exact text (from earlier):
```
| M6 | `ACTIVE` | `SUSPENDED` | политика dunning (N неуспешных списаний) / приостановка ТСП | — | outbox, вебхук `mandate.suspended`; новые списания запрещены |
| M7 | `SUSPENDED` | `ACTIVE` | возобновление ТСП | согласие не отозвано, срок не истёк | outbox, вебхук `mandate.resumed` |
```
Change to mention `POST /v1/mandates/{id}/suspend` and `/resume`.

Let me apply edits.

  `grep_search(pattern="debit\\.completed|debit\\.failed|debitRef", path="<HARNESS>/runs-v2/cells/wtnkjmc/ws")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/state-machine.md", offset=55, limit=20)`

Now add §7 "Изменения дельтой" to parent spec `docs/spec/state-machine.md`. Add a section at the end.

Also fix ADR-010 Decision 4 (debit.completed/failed contradiction), add payerRef to ADR-008, add refund debitRef mention to opkc-adapter §3/§4, add suspend/resume to openapi + tsp-api, add billingPeriod pattern, fix NFR wording, fix ADR-012 numeric thresholds + queued debits fate, add capacity budget + RFP sync, fix fitness C-105 + label textual rules, fix PROPOSAL.

Let me proceed methodically.

1. Parent state machine §7.
Let me append at end of docs/spec/state-machine.md. The file ends with §6 list. Let me add:

```
## 7. Изменения дельтой (рекуррентные списания, 2026-09-28)

Дельта `changes/sbp-subscriptions` (ADR-008…ADR-012) дополняет настоящую спецификацию:
- **Новый вход платежа**: рекуррентное списание (`paymentType=recurring`) входит не через `QR_ISSUED`, а через мандат (техническое подсостояние `MANDATE_BOUND`/`DEBIT_SUBMITTED`); состояния `PAID → CREDITED → COMPLETED` и запреты §3 действуют без изменений. Детали — `docs/spec/mandate-state-machine.md` §4.
- **Сверка и отчёт незавершённых операций** (§5) распространяются на мандаты и списания: открытые списания — кандидаты сверки наравне с платежами.
- **Возвраты** (§2, T11/T12) применимы к списаниям; транспортный возврат адресуется ссылкой списания, а не `qrId` (`docs/spec/mandate-state-machine.md` §4.1).
- Прочие разделы настоящей спецификации не изменяются.
```

2. ADR-010 Decision 4 fix. Current:
"4. **Списание читается существующим статусным методом**: `GET /v1/payments/{paymentId}` (списание — вид платежа, ADR-008); `Payment` расширяется **опциональными** полями `paymentType`, `mandateId`, `billingPeriod`. Новые события вебхуков (`mandate.activated`, `mandate.revoked`, `mandate.rejected`, `debit.completed`/`debit.failed` — нормализованно к `payment.completed`/`payment.failed`) добавляются как новые типы, существующие типы неизменны."

Hmm the actual text I wrote: "Новые события вебхуков (`mandate.activated`, `mandate.revoked`, `mandate.rejected`, `debit.completed`/`debit.failed` — нормализованно к `payment.completed`/`payment.failed`)..." Let me check by grep. Actually my ADR-010 text was: "Новые события вебхуков (`mandate.activated`, `mandate.revoked`, `mandate.rejected`, `debit.completed`/`debit.failed` — нормализованно к `payment.completed`/`payment.failed`) добавляются как новые типы, существующие типы неизменны." Wait, I need to verify. Let me grep.

Let me grep for "debit.completed".

3. opkc-adapter createRefund add debitRef.

Let me do the grep and then edits.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/state-machine.md", new_string="Маппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `EXPIRED`, `REFUNDED` — без техн, old_string="Маппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `EXPIRED`, `REFUNDED` — без техн)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-010-evolyuciya-kontrakta-tsp-, new_string="4. **Списание читается существующим статусным методом**: `GET /v1/payments/{paymentId}` (списание — вид платежа, ADR-008); `Payment` расшир, old_string="4. **Списание читается существующим статусным методом**: `GET /v1/payments/{paymentId}` (списание — вид платежа, ADR-008); `Payment` расшир)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="| `createRefund` | регистрация возврата в ОПКЦ | `reference` (= `refundId` ядра), `qrId` **или** `debitRef` (для рекуррентного списания, v0, old_string="| `createRefund` | регистрация возврата в ОПКЦ | `reference` (= `refundId` ядра), `qrId`, `amount` | `ACCEPTED` (результат — событием) | 5 )`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId` **или** `debitRef` (v0.2), `amount` |", old_string="| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |")`

Now:
- Append §7 to state-machine.md.
- Fix ADR-010 §4.
- Fix opkc-adapter `createRefund` to accept debitRef.

Let me do these.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/openapi/tsp-api.yaml", new_string="        '422':\n          description: Мандат не может быть отозван из текущего состояния\n          content:\n            application/prob, old_string="        '422':\n          description: Мандат не может быть отозван из текущего состояния\n          content:\n            application/prob)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/openapi/tsp-api.yaml", new_string="    MandateRequest:\n      type: object\n      required: [tspId, maxAmountPerDebit, limit, frequency, purpose]\n      properties:\n        , old_string="    MandateRequest:\n      type: object\n      required: [tspId, maxAmountPerDebit, limit, frequency, purpose]\n      properties:\n        )`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/openapi/tsp-api.yaml", new_string="        mandateId: {type: string}\n        mandateRef: {type: string, description: Идентификатор мандата в ОПКЦ}\n        payerRef: {type: , old_string="        mandateId: {type: string}\n        mandateRef: {type: string, description: Идентификатор мандата в ОПКЦ}\n        tspId: {type: str)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/openapi/tsp-api.yaml", new_string="        amount: {type: integer, description: Сумма списания в копейках (<= maxAmountPerDebit)}\n        billingPeriod:\n          type: str, old_string="        amount: {type: integer, description: Сумма списания в копейках (<= maxAmountPerDebit)}\n        billingPeriod: {type: string, descr)`

Now:
- opkc-adapter: add payerRef to mandate.activated event and registerMandate; add suspend/resume? Add mandate.suspended/resumed already there (`mandate.suspended` / `mandate.expired`). Need payer reference. Let me edit registerMandate row and mandate.activated row to include `payerRef?`.

- openapi: add payerRef optional to Mandate/MandateRequest; add suspend/resume paths; add pattern to billingPeriod; define POST /v1/mandates failure semantics (201 with CREATED + webhook). Update Payment/MandateRequest required? Keep required as is (no new required fields, to stay safe/non-breaking; MandateRequest is new so adding required is allowed but payer is not known at request time → optional).

Actually payerRef: for a mandate, the payer is identified by ОПКЦ/consent flow; the merchant request might include payer phone optionally. Let me add optional `payerPhone`/`payerRef` to MandateRequest and `payerRef` (masked) to Mandate, populated on activation. Keep optional.

- tsp-api.md §3.6 narrative: add payerRef, suspend/resume, billingPeriod format, refunds-for-debits, failure semantics.

- NFR wording fixes.
- ADR-012 thresholds + queued debits.
- Fitness fixes.
- RFP sync.
- PROPOSAL significance new_component true + capacity note + residual.
- Also update DELTA MODIFIED/NFR mention? Add suspend/resume to openapi list in DELTA and PROPOSAL §4. And REQ-SUB-1 wording.

Let me do openapi edits.

openapi paths: add `/v1/mandates/{mandateId}/suspend` and `/resume`.

And `MandateRequest.properties.payerPhone` (optional) + `Mandate.properties.payerRef`.

And `DebitRequest.billingPeriod` add pattern + description.

And POST /v1/mandates responses: add description clarifying async semantics.

Let me edit openapi. I'll insert new paths after `/v1/mandates/{mandateId}/revoke` block. Let me find the exact text of the revoke block end and debits start.

The revoke block:
```
  /v1/mandates/{mandateId}/revoke:
    post:
      operationId: revokeMandate
      summary: Отозвать согласие (отзыв ТСП; отзыв плательщиком приходит событием от ОПКЦ)
      parameters:
        - {in: path, name: mandateId, required: true, schema: {type: string}}
        - {in: header, name: Idempotency-Key, required: true, schema: {type: string}}
      responses:
        '200':
          description: Мандат в REVOKED (повторный отзыв идемпотентен)
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Mandate'}
        '422':
          description: Мандат не может быть отозван из текущего состояния
          content:
            application/problem+json:
              schema: {$ref: '#/components/schemas/Problem'}
  /v1/mandates/{mandateId}/debits:
```
Insert suspend/resume before `/v1/mandates/{mandateId}/debits:`.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md", new_string="```json\n{\n  \"tspId\": \"tsp_9f3c2a1b\",\n  \"merchantSubscriptionId\": \"sub-movie-42\",\n  \"payerPhone\": \"+79001234567\",         //, old_string="```json\n{\n  \"tspId\": \"tsp_9f3c2a1b\",\n  \"merchantSubscriptionId\": \"sub-movie-42\",\n  \"maxAmountPerDebit\": 39900,          // ма)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md", new_string="{\n  \"mandateId\": \"man_…\",\n  \"mandateRef\": \"OPKC-…\",\n  \"payerRef\": \"payer_***6789\",         // маскированная ссылка; заполняе, old_string="{\n  \"mandateId\": \"man_…\",\n  \"mandateRef\": \"OPKC-…\",\n  \"tspId\": \"tsp_9f3c2a1b\",")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md", new_string="#### 3.6.3 Отзыв и приостановка мандата\n\n`POST /v1/mandates/{mandateId}/revoke` (заголовок `Idempotency-Key`) → `200` с мандатом в `REVOK, old_string="#### 3.6.3 Отзыв мандата (инициированный ТСП)\n\n`POST /v1/mandates/{mandateId}/revoke` (заголовок `Idempotency-Key`) → `200` с мандатом в )`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md", new_string="```json\n{ \"amount\": 39900, \"billingPeriod\": \"2026-10\", \"description\": \"Подписка за октябрь\" }\n```\n\n`billingPeriod` — канониче, old_string="```json\n{ \"amount\": 39900, \"billingPeriod\": \"2026-10\", \"description\": \"Подписка за октябрь\" }\n```\n\nОтвет `201`: объект `Payme)`

Now update `docs/contracts/tsp-api.md` §3.6 to add payerPhone/payerRef, suspend/resume, failure semantics, billingPeriod format, refunds-for-debits. Let me do targeted edits.

Add after §3.6.2 (state) the suspend/resume as §3.6.3? Currently §3.6.3 is revoke, §3.6.4 debits, §3.6.5 Payment. Let me insert suspend/resume into §3.6.3 block (rename to "Отзыв и приостановка") or add a new section. Simplest: extend §3.6.3 with suspend/resume paragraph, and add payer/billingPeriod/refund notes.

Let me edit §3.6.1 (add payerPhone + failure semantics), §3.6.2 (add payerRef), §3.6.3 (add suspend/resume), §3.6.4 (billingPeriod format), and add §3.6.6 refunds/debits.

Let me apply edits.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md", new_string="#### 3.6.5 Возвраты по списаниям\n\nВозврат по списанию — существующая сага (ADR-005): `POST /v1/payments/{paymentId}/refunds` работает и д, old_string="#### 3.6.6 Возвраты по списаниям\n\nВозврат по списанию — существующая сага (ADR-005): `POST /v1/payments/{paymentId}/refunds` работает и д)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="| `registerMandate` (v0.2) | регистрация согласия плательщика (мандата) в ОПКЦ | `reference` (= `mandateId` ядра), реквизиты ТСП, `payerRef, old_string="| `registerMandate` (v0.2) | регистрация согласия плательщика (мандата) в ОПКЦ | `reference` (= `mandateId` ядра), реквизиты ТСП, лимиты/пе)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="| `mandate.activated` (v0.2) | согласие плательщика получено | `mandateRef`, `reference` (= `mandateId` ядра), `payerRef` (маскированный, о, old_string="| `mandate.activated` (v0.2) | согласие плательщика получено | `mandateRef`, `reference` (= `mandateId` ядра), `activatedAt`, `limits` |")`

Section numbering got out of order: 3.6.6 appears before 3.6.5. Let me fix by moving: rename 3.6.6 (refunds) to appear after 3.6.5, or renumber. Simplest: change "#### 3.6.6 Возвраты по списаниям" to "#### 3.6.7 Возвраты по списаниям" and move? Actually order in file: 3.6.4, then 3.6.6 (refunds), then 3.6.5. Better fix: swap the headings — make the refunds block 3.6.5 and the Payment-extension block 3.6.6, but then ordering would be 3.6.4, 3.6.5(refunds), 3.6.6(Payment) — correct ascending. Let me do that: rename refunds heading to 3.6.5 and Payment heading to 3.6.6.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/nfr.md", new_string="| Пиковая пропускная способность биллинга | sustained 300 TPS, burst 1500 TPS ≥ 10 мин в биллинговое окно | Нагрузочный тест пикового профи, old_string="| Пиковая пропускная способность биллинга | sustained 300 TPS, burst 1500 TPS ≥ 10 мин в биллинговое окно | Нагрузочный тест пикового профи)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/nfr.md", new_string="**Почему именно 0:** дубль списания и списание без действующего согласия — финансовый и регуляторный инцидент, а не деградация метрики. Поэ, old_string="**Почему именно 0:** дубль списания и списание без действующего согласия — финансовый и регуляторный инцидент, а не деградация метрики. Поэ)`

Now NFR wording fixes (finding 9 and 10, 11).

NFR §7 rows:
- "Списаний после обработанного отзыва | **0**" → qualify: "Новых инициаций списаний после обработанного отзыва — 0 (уже отправленные в ОПКЦ — в отчёте незавершённых, политика A3)"
- "Недоставленные списания в биллинговое окно | ≤ 0,1 % от инициированных (прочие — в отчёте незавершённых)" → clarify: "Потерянных (не учтённых нигде) списаний — 0; отложенных за пределы окна — ≤ 0,1 % (остальные видны в отчёте незавершённых)". Also "0 потерянных" vs acceptance "потерь 0": acceptance says "потерь 0" meaning lost; consistent now.

Also add capacity budget note & align with 200/500 (finding 11). Add a row/section: "Пиковая пропускная способность (биллинг) | ... | ...; бюджет мощности: пик биллинга и разовый поток используют общий шлюз/адаптер/АБС; ёмкость адаптера и шлюза увеличивается до 1500 TPS burst — требование к вендору (opkc-adapter §7) и RFP". And note capacity budget needed as A3/business input.

Also "Лаг очереди" row has threshold "алерт по порогу" — add numeric: "лаг p95 ≤ 60 с; возраст первого необработанного > 5 мин → алерт".

Also add rollback thresholds reference? Rollback thresholds numeric go in ADR-012.

Let me edit NFR rows.

Current NFR §7 rows (from earlier):
```
| Распространение отзыва согласия: от события до запрета новых списаний | p95 ≤ 60 с, p99 ≤ 5 мин; после обработки — 0 новых списаний | Тест «отзыв при активном биллинге»; метрика задержки; аудит |
| Активация мандата (подтверждение плательщиком → `ACTIVE` в шлюзе) | p95 ≤ 5 с, p99 ≤ 15 с (без учёта НСПК) | Метрика процесса |
| Инициация списания (`POST /v1/mandates/{id}/debits`: приём + очередь) | p95 ≤ 300 мс, p99 ≤ 1 с | Нагрузочный тест, APM |
| Завершение списания (инициация → `PAID`/`FAILED`) | p95 ≤ 5 с (без учёта банка плательщика) `[ТРЕБУЕТ ПРОВЕРКИ — регламент НСПК]` | Метрика процесса |
| Пиковая пропускная способность биллинга | sustained 300 TPS, burst 1500 TPS ≥ 10 мин в биллинговое окно | Нагрузочный тест пикового профиля |
| Лаг очереди списаний | p95 ≤ 60 с в норме; возраст первого необработанного — алерт по порогу | Мониторинг очереди |
| Дублей списания за период (`mandateId`, `billingPeriod`) | **0** | Тест уникальности периода + сверка |
| Списаний без `ACTIVE`-мандата | **0** | Fitness/тест guard'а |
| Списаний после обработанного отзыва | **0** | Тест гонки «отзыв ↔ списание» |
| Доступность потоков мандатов и списаний | ≥ 99,95 % | SLO-отчёт |
| Недоставленные списания в биллинговое окно | ≤ 0,1 % от инициированных (прочие — в отчёте незавершённых) | Отчёт биллингового окна |
| RPO / RTO (мандаты и списания) | RPO = 0; RTO ≤ 1 ч (без изменений §3) | Chaos-тест, учения DR |
| Сверка мандатов/списаний с НСПК | ежечасная, в составе общей сверки; расхождений — 0 | Reconciliation-отчёт |
| ПДн согласия | маскирование плательщика, шифрование в покое, неизменяемая запись согласия | ИБ-ревью, аудит |
```

Let me rewrite this table block with fixes.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-012-vnedrenie-otkat-i-kill-sw, new_string="2. **Kill-switch на новые списания** — мгновенная остановка **инициации новых** списаний без остановки уже открытых операций, обработки ман, old_string="2. **Kill-switch на новые списания** — мгновенная остановка **инициации новых** списаний без остановки уже открытых операций, обработки ман)`

Now ADR-012: numeric thresholds + fate of queued accepted debits. Let me update §3 signals and §4 owner, and add the queued-debits disposition.

Current ADR-012 §3:
```
3. **Сигналы отката (триггеры)** — измеримые, а не «на глаз»:
   - превышение целевого распространения отзыва (`docs/nfr.md` §7);
   - любой случай списания без `ACTIVE`-мандата или дубля за период (нарушение AD-009 — стоп-сигнал, не «снижение метрики»);
   - доля расхождений сверки по списаниям выше порога;
   - устойчивый лаг очереди / рост DLQ при биллинговом окне выше порога.
```
Add numeric thresholds:
- распространение отзыва > 5 мин (p99 цель) на 3 из 5 событий → старшая эскалация; > 15 мин — стоп.
- любой случай AD-009 → немедленный kill-switch.
- расхождения сверки по списаниям > 0 по завершённым операциям → разбор; > 0.1% за окно → стоп.
- лаг очереди p95 > 5 мин или возраст первого > 15 мин, или DLQ > 0 → старшая эскалация; устойчиво > 15 мин за 30 мин → стоп.

Also §2/§4: fate of already-accepted (HTTP 201) debits in queue when kill-switch flips: they remain queued and are NOT dispatched while flag off? But that leaves customer accepted debits unprocessed. Policy: on kill-switch, accepted-but-not-dispatched debits are **held** (not dropped), surfaced in the unfinished-operations report; on resume they are dispatched with re-validated guard; if kill-switch persists beyond N hours, they are released/expired per policy with TSP notification (no silent loss). Add that.

Let me edit ADR-012 §2 (kill-switch description) and §3.

Actually §2 item 2:
"2. **Kill-switch на новые списания** — мгновенная остановка **инициации новых** списаний без остановки уже открытых операций, обработки мандатных событий и отзыва. Существующий разовый приём продолжает работать независимо."
Add after: disposition of queued accepted debits.

Let me edit.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="| `revokeMandate` (v0.2) | отзыв согласия | `mandateRef`, `reason` | `REVOKED` (идемпотентно по `reference`) | 3 c |\n| `suspendMandate` / , old_string="| `revokeMandate` (v0.2) | отзыв/приостановка согласия | `mandateRef`, `reason` | `REVOKED` (идемпотентно по `reference`) | 3 c |")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="| `mandate.suspended` / `mandate.resumed` / `mandate.expired` (v0.2) | приостановка / возобновление / истечение срока | `mandateRef`, `refe, old_string="| `mandate.suspended` / `mandate.expired` (v0.2) | приостановка / истечение срока | `mandateRef`, `reference`, `reasonCode?` |")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/opkc-adapter.md", new_string="| Пропускная способность адаптера | ≥ 300 TPS sustained, burst 1500 TPS ≥ 10 мин (пик биллинга суммарно с разовым потоком; см. `docs/nfr.md, old_string="| Пропускная способность адаптера | ≥ 200 TPS sustained, пик 500 TPS (соответствует NFR шлюза) | Нагрузочный тест на тестовом контуре НСПК )`

Now update the opkc-adapter §7 capacity requirement to sustained 300/burst 1500 (already NFR claim says "повышено"). Let me edit the first row.

Current: "| Пропускная способность адаптера | ≥ 200 TPS sustained, пик 500 TPS (соответствует NFR шлюза) | Нагрузочный тест на тестовом контуре НСПК |"
Change to: "| Пропускная способность адаптера | ≥ 300 TPS sustained, burst 1500 TPS ≥ 10 мин (с учётом пиков биллинга; суммарно с разовым потоком) | ... |"

Also §4 note about mandate.suspended/resumed from ОПКЦ vs TSP-initiated — the review asked about M7 mechanism; now endpoints exist, so fine. But opkc-adapter has `mandate.suspended` / `mandate.expired` event as incoming; suspend/resume from TSP is internal. Is there a `suspendMandate` adapter call? Add one? The mandate pause is a core-level state (limits/consent not changed) — does ОПКЦ need to know? Probably yes to stop debits at payer side. Let me add `suspendMandate`/`resumeMandate` to adapter §3 to be coherent. Minimal.

Add rows:
| `suspendMandate` (v0.2) | приостановка списаний по согласию | `mandateRef`, `reason` | `SUSPENDED` (идемпотентно по `reference`) | 3 c |
| `resumeMandate` (v0.2) | возобновление списаний | `mandateRef` | `ACTIVE`/`RESUMED` (идемпотентно) | 3 c |

Events: `mandate.suspended` / `mandate.resumed`? Currently I have `mandate.suspended` / `mandate.expired` as one row. That's fine — it includes suspended. Add resumed? Row says "приостановка / истечение срока". Let me update to include resumed: `mandate.suspended`/`mandate.resumed`/`mandate.expired`. Let me edit.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/rfp/vendor-rfp.md", new_string="- **События** (§4): все типы (14+, включая `mandate.*` и `debit.*` в v0.2) с `eventId`; at-least-once; устойчивость к поздним/повторным соб, old_string="- **События** (§4): все 8 типов с `eventId`; at-least-once; устойчивость к поздним/повторным событиям.")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/rfp/vendor-rfp.md", new_string="| Соответствие контракту opkc-adapter (полнота, нормализация, идемпотентность; включая мандатные операции v0.2) | 25 | Сверка спецификации , old_string="| Соответствие контракту opkc-adapter (полнота, нормализация, идемпотентность) | 25 | Сверка спецификации + POC |\n| Производительность (NF)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/rfp/vendor-rfp.md", new_string="| P6 | Нагрузка 300 TPS sustained, пик 500 TPS (разовый поток) | latency в допусках, потерь 0 |", old_string="| P6 | Нагрузка 200 TPS sustained, пик 500 TPS | latency в допусках, потерь 0 |")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/rfp/vendor-rfp.md", new_string="| P12 (v0.2) | Массовые списания: burst биллингового профиля | потерь 0, latency в допусках; поведение при серверных лимитах/окнах НСПК док, old_string="| P12 (v0.2) | Массовые списания: burst биллингового профиля | потерь 0, latency в допусках; поведение при серверных лимитах/окнах НСПК док)`

Now RFP sync (finding 15): §3 weights (add recurring), §4 "все 8 типов" → update, §5 P6 → add P13 peak, §11 checklist. Let me do minimal but real.

§4 line: "- **События** (§4): все 8 типов с `eventId`; at-least-once; устойчивость к поздним/повторным событиям."
→ "все типы (14+ с v0.2, включая `mandate.*` и `debit.*`)".

§3 weights: "Соответствие контракту opkc-adapter (полнота, нормализация, идемпотентность) | 25" and "Производительность (NFR §7 контракта: ≥200 TPS sustained, p95 createPaymentLink <1 c) | 15" → update to ≥300/1500 and mention мандаты.

§5 P6: "Нагрузка 200 TPS sustained, пик 500 TPS" → add note + P13 peak billing. Let me update P6 to "200→300 TPS sustained, пик 500→1500" and add P13.

Minimal edits.

Also G4 says "полного набора методов/событий контракта opkc-adapter §3–4" — fine.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="  # --- C-101…C-109: рекуррентные списания (подписки), delta sbp-subscriptions ---\n  # C-101…C-104, C-107 — правила ТРАССИРУЕМОСТИ (провер, old_string="  # --- C-101…C-107: рекуррентные списания (подписки), delta sbp-subscriptions ---\n  - id: C-101\n    name: mandate-required-for-recurring)`

Now fitness fixes (findings 6,7): 
- Extend C-105 to cover the subpath, or add C-108. Let me split into two rules: C-105 collection path, C-108 subpath; and clarify C-101..C-104/C-107 as traceability guards (comment/labels). Also update DELTA/PROPOSAL wording that these are traceability guards requiring behavioural checks at A4.

Change C-105 pattern to match both? A single `must_contain` with alternation: `(?m)^  /v1/payments(/[A-Za-z{}]+)?:` — better to add C-108 explicitly for subpath. Let me modify C-105 to `(?m)^  /v1/payments:` (keep) and add C-108 `(?m)^  /v1/payments/\{paymentId\}:`. Also add C-109 to guard `PaymentRequest` required unchanged? That's harder via regex. The review noted "adding a required field to PaymentRequest leaves gate green". Add C-109 must_contain `required: [amount, merchantOrderId]` for PaymentRequest. Good.

Also add a note in CONSTRAINTS.yaml comment that C-101..C-104/C-107 are traceability guards (mention), behavior checks required at A4.

But careful: new rules must pass. C-108 pattern `(?m)^  /v1/payments/\{paymentId\}:` — in YAML single quotes, `\{` is literal backslash-brace, regex `\{` matches `{`. Actual line: `  /v1/payments/{paymentId}:`. Good.
C-109 pattern `(?m)^\s+required: \[amount, merchantOrderId\]` — actual: `      required: [amount, merchantOrderId]`. Good.

Let me edit CONSTRAINTS.yaml: add comment + C-108/C-109.

Then update DELTA.md §Fitness wording and PROPOSAL §4 wording to say traceability + behavioural at A4. Also PROPOSAL §4 says "Fitness-правила C-105/C-106 ... сторожат неразрушаемость" — fine, but add C-108. And add note about label.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="    pattern: 'запрещает все \\*\\*новые инициации\\*\\* списаний'", old_string="    pattern: 'запрещает все \\*\\*новые\\*\\* инициации\\*\\* списаний'")`

I changed C-103 pattern to 'запрещает все \*\*новые\*\* инициации\*\* списаний' — but the ADR-009 text is "он запрещает все **новые инициации** списаний". The pattern `запрещает все \*\*новые\*\* инициации\*\* списаний` would require `**новые** инициации** списаний` — wrong (extra **). Let me fix: actual text "запрещает все **новые инициации** списаний". Pattern should be `запрещает все \*\*новые инициации\*\* списаний`.

Let me fix that.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", new_string="- `.arch-handoff/CONSTRAINTS.yaml` — добавлены fitness-правила C-101…C-109 (трассируемость новых инвариантов и сохранность контракта).", old_string="- `.arch-handoff/CONSTRAINTS.yaml` — добавлены fitness-правила C-101…C-107 (проверки новых инвариантов и сохранности контракта).")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", new_string="- **REQ-SUB-1**: When ТСП регистрирует согласие плательщика (`POST /v1/mandates`), the СБП-шлюз shall создать мандат и, при доступном ОПКЦ,, old_string="- **REQ-SUB-1**: When ТСП регистрирует согласие плательщика (`POST /v1/mandates`), the СБП-шлюз shall создать мандат и вернуть `consentUrl`)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", new_string="- **REQ-SUB-4**: When ТСП инициирует списание с `billingPeriod`, the СБП-шлюз shall **зарезервировать период** (уникальный ключ на (`mandat, old_string="- **REQ-SUB-4**: When ТСП инициирует списание с `billingPeriod`, the СБП-шлюз shall создать не более одного **успешного** списания на (`man)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", new_string="- [ ] Мандат: `POST /v1/mandates` идемпотентен; `ACTIVE` по событию; условия иммутабельны после активации; при недоступности ОПКЦ — `CREATE, old_string="- [ ] Мандат: `POST /v1/mandates` идемпотентен; `ACTIVE` по событию; условия иммутабельны после активации.\n- [ ] Списание без `ACTIVE`-ман)`

Now update DELTA.md §Fitness and PROPOSAL §4 + §1 new_component + §7 thresholds.

DELTA §Fitness currently:
"C-101 мандат обязателен для списания · C-102 уникальность периода · C-103 отзыв → 0 новых списаний · C-104 зачисление только из `PAID` · C-105 аддитивность контракта (сохранность путей) · C-106 enum `Payment.status` неизменен · C-107 ретраи с джиттером/бюджетом. Формулировки правил — в `CONSTRAINTS.yaml` (внесены этой дельтой)."

Update to C-101..C-109 and note traceability vs behavioural.

Also DELTA "Затронутые защищённые файлы" mentions C-101…C-107 → update to C-101…C-109.

Also DELTA MODIFIED: add suspend/resume, refunds debitRef, reservation. Actually MODIFIED bullet for contract mentions new paths `/v1/mandates*` — covers. Add mention of reservation in AD-003/AD-005 bullets? The AD-003 bullet says "добавлены (`mandateId`, `billingPeriod`)". Add "резервация периода" mention. Let me update the AD-003 and AD-005 bullets slightly and add a note about "0 дублей обеспечивается резервацией".

Also acceptance criteria list in DELTA: add "0 потерянных", "suspend/resume", "refund by debitRef". Let me update.

Also REQ-SUB-1 wording about consentUrl. Update to "при доступном ОПКЦ — p95 ≤5с, иначе CREATED + вебхук".

Let me edit DELTA.

Then PROPOSAL: §1 new_component → true (and re-run significance), §4 mention C-108/C-109 and traceability label, §5 maybe unchanged, §7 thresholds pointer, §2.2 new module note, and add a "Верификация" section noting gate outcome + auto-route caveat + adversarial review disposition.

Let me do DELTA edits.

  `grep_search(path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", pattern="REQ-SUB-4|REQ-SUB-5")`

REQ-SUB-4 edit: the "было" version still shows in the file? The output shows REQ-SUB-4 as the new version ("зарезервировать период..."). Wait, the third edit's output showed the file with REQ-SUB-4 as "создать не более одного **успешного**..." — that was the pre-edit content? No: the edit result output shows the *file after edit* for the changed region. Hmm, the third edit explicitly replaced REQ-SUB-4, and the result shows REQ-SUB-4 line as the OLD text "создать не более одного **успешного**". Wait, look: third tool result output shows:
"- **REQ-SUB-4**: When ТСП инициирует списание с `billingPeriod`, the СБП-шлюз shall создать не более одного **успешного** списания на (`mandateId`, `billingPeriod`) и вернуть `409` при повторе уже успешного периода."

That's confusing — it seems the edit output window was showing surrounding lines but with old content? Then the fourth edit output (acceptance criteria) shows REQ-SUB lines 19-27 including REQ-SUB-4 as "зарезервировать период". So the file DID change. The third result just showed a stale window? Actually the third result outputs lines with old REQ-SUB-4 — possibly because edits display a window and concurrent edits raced. The final state (4th output) shows REQ-SUB-4 updated. Let me verify by grep to be safe.

Also REQ-SUB-5 still says "не создавать ни одного нового списания" — should say "ни одной новой инициации". Let me fix.

Let me grep REQ-SUB-4/5 to confirm final state.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", new_string="- **REQ-SUB-5**: When поступает событие отзыва согласия, the СБП-шлюз shall запретить новые инициации списаний по мандату; while мандат `RE, old_string="- **REQ-SUB-5**: When поступает событие отзыва согласия, the СБП-шлюз shall запретить новые списания по мандату; while мандат `REVOKED`, th)`

Fix REQ-SUB-5 wording: "не создавать ни одного нового списания" → "не создавать ни одной новой инициации списания (уже отправленные — в отчёте незавершённых)". Let me edit.

Also REQ-SUB-3 "сверх лимита" ok.

Then PROPOSAL edits.

  `tool_call(arguments={"triggers": ["new_component=true", "new_datastore=false", "new_vendor=false", "domain_ownership_change=true", "cross_domain_integration=tru, name="mcp__spine__significance_score")`

Now PROPOSAL edits:
- §1 trigger table: new_component true.
- §2.2 note about module vs component.
- §4: mention suspend/resume, C-108/C-109, traceability note.
- §7 thresholds.
- Add §10 "Верификация пакета" with gate outcome, auto-route caveat, adversarial review disposition.

Also add MODIFIED bullet in DELTA for suspend/resume and refunds? The MODIFIED contract bullets mention new paths `/v1/mandates*` (covers suspend/resume) and opkc-adapter. Add refund debitRef mention. Minor; I'll add to opkc-adapter bullet.

Let me first apply PROPOSAL edits.

§1 table row: `| \`new_component\` | false | Новый модуль внутри существующего шлюза, не новый компонент-контур |` → true.

Also significance_score with new_component=true gives 10; update the header "9/15" → "10/15" and route note. Let me re-run significance_score first to get exact.

Let me re-run significance_score with new_component true.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", new_string="**Маршрут: Critical.** Инструмент `significance_score` (MCP Spine) на заявленных триггерах даёт **10/15 → Critical** (`criticality_or_excep, old_string="**Маршрут: Critical.** Инструмент `significance_score` (MCP Spine) на заявленных триггерах даёт **9/15 → Critical** (`criticality_or_except)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", new_string="| `new_component` | **true** | Новый модуль (мандат) + планировщик/очередь списаний внутри платёжного контура (новая единица владения в код, old_string="| `new_component` | false | Новый модуль внутри существующего шлюза, не новый компонент-контур |\n| `new_datastore` | false | Новые таблицы)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", new_string="Новые сущности: `Mandate` (согласие) и рекуррентное списание как вид платежа (`paymentType=recurring`). Новые единицы: мандатный модуль, пл, old_string="Новые сущности: `Mandate` (согласие) и рекуррентное списание как вид платежа (`paymentType=recurring`). Новый модуль: мандатный модуль + пл)`

Score 10 → Critical. Update DELTA and PROPOSAL headers/table. DELTA says "значимость 9/15". Change to 10/15. PROPOSAL §1 header "9/15" and table.

Let me apply PROPOSAL edits.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", new_string="- **Новые пути**: `POST /v1/mandates`, `GET /v1/mandates/{mandateId}`, `POST /v1/mandates/{mandateId}/revoke`, `POST /v1/mandates/{mandateI, old_string="- **Новые пути**: `POST /v1/mandates`, `GET /v1/mandates/{mandateId}`, `POST /v1/mandates/{mandateId}/revoke`, `POST|GET /v1/mandates/{mand)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", new_string="- `openapi_lint openapi/tsp-api.yaml` → **PASS** (0 error, 0 warn).\n- `contract_diff` v0.1 → v0.2 → **0 breaking, 4 non-breaking** (только, old_string="- `openapi_lint openapi/tsp-api.yaml` → **PASS** (0 error, 0 warn).\n- `contract_diff` v0.1 → v0.2 → **0 breaking, 4 non-breaking** (только)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", new_string="| Что | Как | Триггер | Владелец |\n|---|---|---|---|\n| Инициация новых списаний | Kill-switch (фиче-флаг `recurring-debits` → off) | Нару, old_string="| Что | Как | Триггер | Владелец |\n|---|---|---|---|\n| Инициация новых списаний | Kill-switch (фиче-флаг `recurring-debits` → off) | Нару)`

Now PROPOSAL §4 update: mention suspend/resume paths, C-108/C-109, traceability note. Let me edit the contract-changes section.

Current §4 bullets:
"- **Новые пути**: `POST /v1/mandates`, `GET /v1/mandates/{mandateId}`, `POST /v1/mandates/{mandateId}/revoke`, `POST|GET /v1/mandates/{mandateId}/debits`."
Add suspend/resume.
"- **Доказательство...**" bullets: add C-108/C-109 and traceability note.

Let me edit.

Also §7 thresholds: replace "Триггер" column entries with numeric. Current §7 table:
```
| Инициация новых списаний | Kill-switch (фиче-флаг `recurring-debits` → off) | Нарушение AD-009 (дубль/списание без согласия) — немедленно | Дежурный SRE по runbook |
...
| Откат этапа запуска (пилот → остановка волны) | Выключение флага для группы ТСП | Доля расхождений сверки / лаг / DLQ выше порога | Архитектор + продукт |
```
Update "выше порога" → numeric; add queued debits row.

Let me apply.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", new_string="Внутренний контракт `docs/contracts/opkc-adapter.md` (v0.1 → v0.2) расширен аддитивно: мандатные операции (`registerMandate`, `getMandateSt, old_string="Внутренний контракт `docs/contracts/opkc-adapter.md` (v0.1 → v0.2) расширен аддитивно: мандатные операции (`registerMandate`, `getMandateSt)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/solutioning-subscriptions.md", new_string="- возвраты — существующая сага (ADR-005); транспортный возврат адресуется ссылкой списания (`debitRef`/`reference`), а не `qrId` (`docs/spe, old_string="- возвраты — существующая сага (ADR-005) без изменений.")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", new_string="- **AD-003**: ключи идемпотентности (`Idempotency-Key`, `eventId`, `paymentId`/`refundId`) → **добавлены** (`mandateId`, `billingPeriod`) и, old_string="- **AD-003**: ключи идемпотентности (`Idempotency-Key`, `eventId`, `paymentId`/`refundId`) → **добавлены** (`mandateId`, `billingPeriod`) и)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", new_string="- **Контракт адаптера ОПКЦ** v0.1 → **v0.2** (`docs/contracts/opkc-adapter.md`): аддитивно добавлены мандатные операции (`registerMandate`,, old_string="- **Контракт адаптера ОПКЦ** v0.1 → **v0.2** (`docs/contracts/opkc-adapter.md`): аддитивно добавлены мандатные операции и события `mandate.)`

Update the "Внутренний контракт opkc-adapter" line in PROPOSAL §4 to include suspend/resume + refund debitRef. And update DELTA MODIFIED opkc bullet. And add PROPOSAL §10 verification section. Also update solutioning-subscriptions §1 "автоплатежи" already? It says "точный протокол..." fine. Also solutioning-subscriptions §3.2 says "возвраты — существующая сага (ADR-005) без изменений" — now qualified with debitRef. Let me update that line. Also §3.1 mentions payer masked — now consistent with payerRef.

Let me apply:
1. PROPOSAL §4 opkc line.
2. solutioning-subscriptions §3.2 returns line.
3. Add PROPOSAL §10.
4. DELTA MODIFIED opkc bullet + AD-003/AD-005 bullets mention reservation.

Then re-run gates (fitness, openapi_lint, contract_diff, delta_guard, gate), then re-run adversarial review (or at least a focused re-review). Given time, I'll re-run the same subagent? The review was foreground; I can launch a new focused review to verify fixes. Let me do a focused re-review after gates.

Let me apply edits.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/solutioning-subscriptions.md", new_string="- уникальность периода: **резервация** периода при инициации — уникальный ключ БД на (`mandateId`, `billingPeriod`) для всех списаний, кром, old_string="- уникальность периода: ограничение БД на (`mandateId`, `billingPeriod`) — не более одного **успешного** списания за период;")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", new_string="- **RFP** (`docs/rfp/vendor-rfp.md`): добавлены критерий допуска G8, POC-сценарии P9–P13 и повышенная ёмкость (≥300 sustained / 1500 burst), old_string="- **RFP** (`docs/rfp/vendor-rfp.md`): добавлены критерий допуска G8 и POC-сценарии P9–P12 (мандаты/списания).\n- **Спецификация** (`docs/sp)`

solutioning-subscriptions §3.2 still says "не более одного **успешного** списания за период" — update to reservation. Let me fix.

Also DELTA RFP bullet P9–P12 → P9–P13, and spec bullet "который не изменяется" → now §7 added. Fix.

Then add PROPOSAL §10 verification.

Then re-run gates.

  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wtnkjmc/ws"}, name="mcp__spine__fitness_check")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md"}, name="mcp__spine__spine_lint")`
  `tool_call(arguments={"cwd": "<HARNESS>/runs-v2/cells/wtnkjmc/ws", "path": "openapi/tsp-api.yaml"}, name="mcp__spine__openapi_lint")`
  `tool_call(arguments={"format": "openapi", "new": "<HARNESS>/runs-v2/cells/wtnkjmc/ws/openapi/tsp-a, name="mcp__spine__contract_diff")`

Now add PROPOSAL §10 "Верификация пакета" before "## 9. Что дальше" or at the end. Let me append after §9. Let me read the end of PROPOSAL to append properly. §9 is the last. I'll append §10.

Content:
```
## 10. Верификация пакета (машинные проверки и независимое ревью)

Прогон контура контроля Spine на состоянии пакета:

- `fitness_check` — PASS, 14 правил, 0 нарушений; ослаблений правил относительно baseline нет.
- `spine_lint` — PASS, 0 находок.
- `delta_guard` — PASS: правка `ARCHITECTURE-SPINE.md` покрыта активной дельтой `sbp-subscriptions`.
- `openapi_lint openapi/tsp-api.yaml` — PASS (0 error, 0 warn).
- `contract_diff` v0.1→v0.2 — 0 breaking, 4 non-breaking.
- `arch-be gate --repo .` — PASS (fitness, delta_guard, rule_weakened, spine_lint).

**Находка о маршруте (важно).** Авто-режим гейта вывел маршрут **Fast** (score 1: `api_contract_change`), потому что механический детектор читает только git-дифф (нет кода/модели и слабые маркеры). Заявленная значимость по 15 триггерам — **Critical (10/15)**. Пакет выносится как Critical; расхождение — ограничение авто-детектора на репозитории без кода, а не основание снижать маршрут.

**Независимое состязательное ревью** (отдельный контур, свежий контекст, вердикт в `changes/sbp-subscriptions/REVIEW.md`): первый прогон — NOT-READY, 2 blocker + 10 major/minor; после правок пакета — повторный прогон (см. REVIEW.md §«Повторная проверка»).

**Что остаётся не закрытым механикой:** `trace_check`/`model_validate` — SKIP (в репозитории нет каталога `model/`); `decision_quality`/`semantic_quality` — не включены. Рекомендация: на этапе A3/A4 поднять планку (semantic/decision quality) и, при необходимости, завести типизированную модель.
```

I'll fill REVIEW.md after re-review, so reference it.

Let me append §10. Then run gates, then re-review.

Actually better to run gates first to fill exact numbers, then write REVIEW + §10. But §10 content is mostly known. Let me run gates now, then write REVIEW.md (with re-review), then finalize §10 numbers.

Let me run: fitness_check, spine_lint, openapi_lint, contract_diff, delta_guard, gate.
Fixes applied. Now re-running the full verification suite.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", new_string="- `contract_diff` v0.1 → v0.2 → **0 breaking, 6 non-breaking** (только новые пути; CD-007 «ломающий дифф без смены major» не сработал).", old_string="- `contract_diff` v0.1 → v0.2 → **0 breaking, 4 non-breaking** (только новые пути; CD-007 «ломающий дифф без смены major» не сработал).")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", new_string="- **Контракт API ТСП** v0.1 → **v0.2** (`openapi/tsp-api.yaml`, `docs/contracts/tsp-api.md`): аддитивно — новые пути `/v1/mandates*`, новые, old_string="- **Контракт API ТСП** v0.1 → **v0.2** (`openapi/tsp-api.yaml`, `docs/contracts/tsp-api.md`): аддитивно — новые пути `/v1/mandates*`, новые)`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wtnkjmc/ws && echo \"==== delta validate ====\"; a, description="Re-run delta validation, guard and gate")`

All PASS: fitness 16 rules 0 violations, no weakening; spine_lint clean; openapi_lint PASS; contract_diff 0 breaking / 6 non-breaking (update PROPOSAL from 4 to 6).

Update PROPOSAL §4 diff numbers "4 non-breaking" → "6 non-breaking". And DELTA MODIFIED contract bullet "4 non-breaking" → "6". Also contract tsp-api.md header says "0 breaking" (no count) — fine.

Then run gate and delta_guard. Then re-review.

Let me update counts and run gate.

  `agent(description="Verify fixes to change package", prompt="You are an independent adversarial architecture reviewer doing a RE-CHECK. You did not write this work. Read-only: do NOT modify/create/del, run_in_background=false)`

All green. Now launch a focused re-review by an independent agent to verify the earlier findings are addressed (and check for new inconsistencies introduced by edits). Use a fresh general-purpose agent, foreground.

Prompt: verify each of the 18 findings' disposition by reading files; verdict READY/NOT-READY; only report remaining/new issues with evidence. Keep concise.

Let me launch.
All gates green. Now a focused independent re-review to verify the findings are actually resolved.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md", new_string="- **Rule**: рекуррентное списание инициируется только при мандате в статусе `ACTIVE`, в пределах `validFrom`/`validUntil` и лимитов; **пери, old_string="- **Rule**: рекуррентное списание инициируется только при мандате в статусе `ACTIVE`, в пределах `validFrom`/`validUntil` и лимитов, и не б)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/openapi/tsp-api.yaml", new_string="        '409':\n          description: Списание за этот billingPeriod уже зарезервировано/существует\n          content:", old_string="        '409':\n          description: Успешное списание за этот billingPeriod уже существует\n          content:")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/openapi/tsp-api.yaml", new_string="          description: 'Канонический период: MONTHLY — YYYY-MM, DAILY — YYYY-MM-DD; ключ резервации периода (уникальность списания)'", old_string="          description: 'Канонический период: MONTHLY — YYYY-MM, DAILY — YYYY-MM-DD; ключ уникальности успешного списания'")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/contracts/tsp-api.md", new_string="Коды подписок (v0.2): `DEBIT_PERIOD_EXISTS` (409 — списание за период уже существует/зарезервировано), `MANDATE_NOT_ACTIVE` (422 — мандат н, old_string="Коды подписок (v0.2): `DEBIT_PERIOD_EXISTS` (409 — успешное списание за период уже есть), `MANDATE_NOT_ACTIVE` (422 — мандат не `ACTIVE`/вн)`

Good re-review. Remaining defects are concrete. Let me fix:

1. [major] `arch-be gate --route critical` FAILS on `sensors` — required_sections missing `## Проблема`, `## Критерии приёмки`, `## Риски` in `docs/spec/mandate-state-machine.md` and `docs/spec/state-machine.md`. Wait — it says both files. But state-machine.md is an accepted file; the sensor requires sections in docs/spec/*.md. Since the baseline state-machine.md presumably also lacked them, was the gate red before my change? Let me check: the baseline repo gate is Fast by default and sensors only run on Standard/Critical. So `--route critical` was likely already red on state-machine.md before my change. But my change declares Critical, so I must make it green. I need to add `## Проблема`, `## Критерии приёмки`, `## Риски` sections to both spec files. Adding to the accepted state-machine.md — allowed (not protected), and covered by delta mention. Let me check the sensor config: required_sections sensors for docs/spec. Let me just add the three sections to both files.

Actually, is editing `docs/spec/state-machine.md` acceptable? Yes, it's a doc; the delta covers mention. Add sections that are meaningful (problem, acceptance criteria, risks).

2. [major] AD-009 success-scoped wording + openapi descriptions + tsp-api §4 DEBIT_PERIOD_EXISTS wording. Fix: 
- spine AD-009 Rule: change "не более одного **успешного** списания" → "не более одного списания на (`mandateId`, `billingPeriod`), кроме отменённых до отправки (период резервируется при инициации)".
- C-102 pattern: currently matches `(mandateId, billingPeriod)` — still matches. Fine. But to guard the reservation wording, maybe add C-110 must_contain "период **безусловно резервируется**" in ADR-009. Optional. Let me update C-102 pattern to include the reservation phrase? Simpler: keep C-102 and add nothing; the review says C-102 guards the weak wording, so updating spine text makes it correct. Also update openapi description "ключ уникальности успешного списания" → "ключ уникальности списания (резервация периода)" and 409 description "Успешное списание за этот billingPeriod уже существует" → "Списание за этот billingPeriod уже зарезервировано/существует". And tsp-api §4 "DEBIT_PERIOD_EXISTS (409 — успешное списание за период уже есть)" → "списание за период уже существует/зарезервировано".
- Also DELTA MODIFIED AD-003 bullet mentions reservation — fine.
- Add C-110 for reservation wording to lock it: must_contain in ARCHITECTURE-SPINE.md pattern 'период резервируется при инициации'. Good.

3. [major] nfr §2 vs §7 numeric contradiction. Fix: add explicit supersede note in §2 or update §2. Better: update §2 rows to reflect new totals (sustained 300, burst 1500) OR add a note that §2 figures are superseded for the combined contour by §7. The cleanest: update §2 throughput rows to "200 TPS (разовый C2B) / 300 TPS суммарно с подписками; пик 500 → burst 1500 ≥10 мин (см. §7)". Let me update §2 rows with a note.

Current §2 rows:
"| Throughput sustained | 200 TPS | Нагрузочный тест |
| Throughput пик (burst) | 500 TPS, допустимый burst 1000 TPS на 1 мин | Нагрузочный тест |
| Масштабируемость | ×2 без изменения архитектуры (горизонтальное масштабирование) | Load-test на 400 TPS |"

Update to:
"| Throughput sustained | 200 TPS (разовый C2B); 300 TPS суммарно с рекуррентными списаниями (§7) | Нагрузочный тест |
| Throughput пик (burst) | 500 TPS разовый; суммарно с биллинговым пиком — burst 1500 TPS ≥ 10 мин (§7) | Нагрузочный тест |
| Масштабируемость | ×2 без изменения архитектуры (горизонтальное масштабирование) | Load-test на 400 TPS |"

4. [minor] DELTA "9/15" → "10/15".
5. [minor] ADR-010 §3 enumerate suspend/resume.
6. [minor] RFP §9 "G1–G7" → "G1–G8". Also §11? Let me grep G1–G7.
7. [minor] DELTA mislabels CONSTRAINTS.yaml as delta-guard-protected; fix wording, add residual note. And PROPOSAL §10 residual note.

Also, add PROPOSAL §10 verification section (I haven't added it yet). Include the gate --route critical result after fixing.

Let me implement these fixes.

First, spec required sections. Let me find what sections sensor expects: "## Проблема, ## Критерии приёмки, ## Риски". I'll add these to both spec files with meaningful content.

For `docs/spec/state-machine.md`, add at the end (after §7):
```
## Проблема
... 
## Критерии приёмки
...
## Риски
...
```
Hmm, ordering: sensor just checks presence. But logically "Проблема" should be near top. The sensor likely checks presence anywhere. I'll add all three at the end as a consolidated section block to avoid restructuring the accepted doc — but that's awkward. Alternatively add them at the top. The parent doc starts with title then `- Status:` metadata. Adding `## Проблема` at top is cleaner. But then existing §1..§7 numbering stays. Let me add at end; sensor is presence-based. Actually to be safe about regex like `(?m)^## Проблема$` — any location works.

Let me add at end of both files.

Wait, does the sensor also require sections in docs/spec/*.md only? It flagged both spec files. Are there other docs/spec files? Only these two. Good.

Let me write content.

For state-machine.md, add:
```
## Проблема

Канал к ОПКЦ СБП не даёт гарантий «ровно один раз», а финансовое последствие ошибки (двойное зачисление/потерянный платёж) недопустимо. Нужна однозначная модель состояний платежа с атомарными переходами и идемпотентностью, на которой строятся и разовые платежи, и рекуррентные списания (дельта §7).

## Критерии приёмки

- Каждый переход таблицы §2 выполняется как атомарная транзакция «статус + outbox + аудит» (AD-002); тест на каждый переход.
- Зачисление в АБС недостижимо из `CREATED`/`QR_ISSUED` (AD-005); тест негативного сценария.
- Повторные триггеры (§4) не меняют завершённое состояние; тесты идемпотентности.
- Открытые состояния (§5) попадают в сверку; расхождения обрабатываются по runbook.
- Для рекуррентных списаний — резервация периода и зачисление только из `PAID` (§7).

## Риски

- Неточная нормализация статусов ОПКЦ → неверный переход (митигация: адаптер нормализует, сверка страхует).
- Потерянная нотификация → незачисленный платёж (митигация: опрос статусов и ежечасная сверка).
- Гонка при отзыве согласия (дельта §7) → «осевшее» списание (митигация: приоритет отзыва, отчёт незавершённых, политика A3).
- Расширение enum `Payment.status` нарушило бы потребителей (митигация: AD-010 — статусы не расширяются, технические подсостояния скрыты).
```

For mandate-state-machine.md, add similar.

Also for the reserved-period wording guard, C-110.

Let me apply all fixes now. I'll batch edits.

First: DELTA 9/15 → 10/15.
Then spine AD-009 Rule.
Then openapi descriptions.
Then tsp-api §4 code desc.
Then nfr §2.
Then ADR-010 §3.
Then RFP §9.
Then DELTA protected-files wording.
Then CONSTRAINTS C-110.
Then spec sections.

Let me start.
Re-review found remaining concrete defects (including a Critical-route sensor failure). Fixing them all.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/nfr.md", new_string="| Throughput sustained | 200 TPS (разовый C2B); 300 TPS суммарно с рекуррентными списаниями — см. §7 | Нагрузочный тест |\n| Throughput пик, old_string="| Throughput sustained | 200 TPS | Нагрузочный тест |\n| Throughput пик (burst) | 500 TPS, допустимый burst 1000 TPS на 1 мин | Нагрузочный)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-010-evolyuciya-kontrakta-tsp-, new_string="3. **Новые ресурсы**: `POST /v1/mandates`, `GET /v1/mandates/{mandateId}`, `POST /v1/mandates/{mandateId}/revoke`, `POST /v1/mandates/{mand, old_string="3. **Новые ресурсы**: `POST /v1/mandates`, `GET /v1/mandates/{mandateId}`, `POST /v1/mandates/{mandateId}/revoke`, `POST|GET /v1/mandates/{)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", new_string="- Route: **Critical** (значимость 10/15, `significance_score`) — полный Solutioning, дельты недостаточно; человеческое решение A3 обязатель, old_string="- Route: **Critical** (значимость 9/15, `significance_score`) — полный Solutioning, дельты недостаточно; человеческое решение A3 обязательн)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", new_string="## Затронутые защищённые файлы (для delta-guard)\n\n- `ARCHITECTURE-SPINE.md` — добавлены AD-009…AD-011; правки-расширения в AD-002, AD-003, old_string="## Затронутые защищённые файлы (для delta-guard)\n\n- `ARCHITECTURE-SPINE.md` — добавлены AD-009…AD-011; правки-расширения в AD-002, AD-003)`

Now nfr §2, ADR-010 §3, RFP §9, DELTA 9/15 + protected wording, CONSTRAINTS C-110, spec sections.

Let me apply nfr §2 edit.

  `grep_search(path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/rfp/vendor-rfp.md", pattern="G1.G7|G1..G7")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/adr/ADR-010-evolyuciya-kontrakta-tsp-, new_string="6. **Внутренний контракт с вендором** (`opkc-adapter.md`) расширяется так же аддитивно: новые методы (`registerMandate`, `getMandateStatus`, old_string="6. **Внутренний контракт с вендором** (`opkc-adapter.md`) расширяется так же аддитивно: новые методы (`registerMandate`, `getMandateStatus`)`

Now:
- ADR-010 §6 enumerate suspend/resume (optional). Let me update to include.
- RFP §9 "G1–G7" → "G1–G8"; also §11 checklist. Let me grep.
- CONSTRAINTS C-110.
- spec sections (required_sections).
- PROPOSAL §10.

Let me grep for G1–G7.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/rfp/vendor-rfp.md", new_string="1. RFI (2 нед): квалификация по G1–G8, резюме решения, цены-ориентиры.", old_string="1. RFI (2 нед): квалификация по G1–G7, резюме решения, цены-ориентиры.")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="  - id: C-109\n    name: tsp-api-payment-request-required-unchanged\n    type: must_contain\n    glob: \"openapi/tsp-api.yaml\"\n    patter, old_string="  - id: C-109\n    name: tsp-api-payment-request-required-unchanged\n    type: must_contain\n    glob: \"openapi/tsp-api.yaml\"\n    patter)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/mandate-state-machine.md", new_string="- Вебхуки ТСП: `mandate.pending`, `mandate.activated`, `mandate.rejected`, `mandate.suspended`, `mandate.resumed`, `mandate.revoked`, `mand, old_string="- Вебхуки ТСП: `mandate.pending`, `mandate.activated`, `mandate.rejected`, `mandate.suspended`, `mandate.resumed`, `mandate.revoked`, `mand)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/docs/spec/state-machine.md", new_string="- **§4 «Идемпотентность»**: для списаний добавлен ключ (`mandateId`, `billingPeriod`) — уникальность периода (AD-009, ADR-009).\n- Прочие р, old_string="- **§4 «Идемпотентность»**: для списаний добавлен ключ (`mandateId`, `billingPeriod`) — уникальность периода (AD-009, ADR-009).\n- Прочие р)`

Now add required sections to spec files. Let me append to both.

`docs/spec/mandate-state-machine.md` — add at end:
```
## Проблема
...
## Критерии приёмки
...
## Риски
...
```

`docs/spec/state-machine.md` — same.

Let me write them.

Note: the sensor may require exact heading text `## Проблема`, `## Критерии приёмки`, `## Риски`. I'll use those exact headings.

Also DELTA §Fitness mentions C-101..C-110 — update to C-110 and mention. And DELTA protected bullet already says C-101…C-110. Fitness section says C-109. Let me update Fitness line to include C-110.

Let me append spec sections.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/DELTA.md", new_string="C-101 мандат обязателен для списания · C-102 уникальность периода · C-103 отзыв → 0 новых инициаций · C-104 зачисление только из `PAID` · C, old_string="C-101 мандат обязателен для списания · C-102 уникальность периода · C-103 отзыв → 0 новых инициаций · C-104 зачисление только из `PAID` · C)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", new_string="4. Гейт A4: fitness-правила C-101…C-110 + нагрузочный тест биллингового пика + ИБ-ревью ПДн согласия; репетиция отката.\n\n## 10. Верификац, old_string="4. Гейт A4: fitness-правила C-101…C-107 + нагрузочный тест биллингового пика + ИБ-ревью ПДН согласия; репетиция отката.")`

Now update DELTA Fitness to C-110 and add mention. Then add PROPOSAL §10. Then run `arch-be gate --route critical` and other gates.

DELTA Fitness line currently: "C-101 ... · C-109 `PaymentRequest.required` неизменён. Формулировки — ..."
Add C-110.

Let me edit.

Then PROPOSAL §10 — add after §9.

Let me find §9 end. PROPOSAL ends with "## 9. Что дальше (после A3)" section. Append §10 after.

Let me apply.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", offset=160, limit=25)`

The PROPOSAL §9 last numbered item may differ. Let me read the tail of PROPOSAL.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", new_string="4. Гейт A4: fitness-правила C-101…C-110 + нагрузочный тест биллингового пика + ИБ-ревью ПДн согласия; репетиция отката.\n\n## 10. Верификац, old_string="4. Гейт A4: fitness-правила C-101…C-107 + нагрузочный тест биллингового пика + ИБ-ревью ПДн согласия; репетиция отката.")`

The old_string I used had "ПДН" vs actual "ПДн". Let me append §10 using the exact text.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wtnkjmc/ws && echo \"==== gate --route critical ==, description="Run critical-route gate and default gate")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wtnkjmc/ws"}, name="mcp__spine__fitness_check")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wtnkjmc/ws/ARCHITECTURE-SPINE.md"}, name="mcp__spine__spine_lint")`

Now run `arch-be gate --route critical` to verify sensors pass, plus all other gates. Then write REVIEW.md. Then update README, then final re-review maybe quickly.

Let me run the gates.
Now verifying the Critical-route gate passes and all checks stay green.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", new_string="- `fitness_check` — PASS: 17 правил, нарушений 0; ослаблений правил относительно baseline (20807e7) нет.\n- `spine_lint` — PASS, 0 находок , old_string="- `fitness_check` — PASS: 16 правил, нарушений 0; ослаблений правил относительно baseline (20807e7) нет.\n- `spine_lint` — PASS, 0 находок )`

`gate --route critical`: all components PASS or SKIP; sensors PASS now. Overall INCOMPLETE (exit 3) because Critical requires trace_check/nfr/model_validate/evidence_verify which have no input (no model/, no EVIDENCE.yaml). That's a structural lack in the repo (no model/), not a defect I introduced — and it's honest: INCOMPLETE ≠ FAIL. I should document this accurately in PROPOSAL §10 (I wrote "проверено ... секции проходят; trace/model/nfr/evidence SKIP" but didn't mention INCOMPLETE/exit 3). Let me refine §10 wording to state: sensors PASS; итог INCOMPLETE (exit 3) из-за отсутствия model/ и evidence-бандла — обязательные для Critical составляющие без входа. That's precise.

Options: create an EVIDENCE.yaml bundle? spine-bundle says Critical requires 13 artifacts and A3 signed by human. Since A3 is pending, a bundle would be `a3_not_signed` (red). Creating a bundle with a stub would be dishonest. Better to document INCOMPLETE honestly. Also could create `model/` — but that's a big addition and not requested; it's noted as a recommendation.

Let me refine §10 to mention INCOMPLETE and what remains.

Also update PROPOSAL §10 bullet counts (17 rules now).

Let me edit §10.

Then write REVIEW.md documenting the adversarial review (both rounds) and dispositions. Then update README. Then optional final quick re-review — I think I can verify the remaining items myself and note in REVIEW. But an independent confirmation would be best. Given the re-review already confirmed most, and my fixes for the remainder are mechanical (sections added, wording) — I'll do a final targeted verification myself (grep) plus run the gates (done). I'll write REVIEW.md honestly stating round 2 verdict NOT-READY with 7 remaining defects, all now fixed, verified by gates and by the author (not independently re-verified a second time) — being transparent. Actually better: run one more short independent check on just the 7 remaining defects. It's cheap and closes the loop honestly. Let me do a final short re-review focused on the 7 items.

Let me first fix §10 numbers/wording.

  `agent(description="Final check of 7 residual defects", prompt="Independent adversarial verification, round 3. Read-only (no file writes except under /tmp). Evidence only (path + quote). Repo root: /home, run_in_background=false)`

Now write REVIEW.md and then a final focused independent verification of the 7 remaining defects. Let me first do the final verification via subagent, then write REVIEW.md with its result.

Actually, let me write REVIEW.md after the final check so it's accurate. Launch the final focused re-review now.

Prompt: verify the 7 remaining defects from round 2 are closed in current files, plus confirm no new inconsistency. Keep short.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/PROPOSAL.md", new_string="Полный список — `changes/sbp-subscriptions/DELTA.md` §Критерии приёмки (14 пунктов, проверяемые). Обязательные негативные сценарии:", old_string="Полный список — `changes/sbp-subscriptions/DELTA.md` §Критерии приёмки (11 пунктов, проверяемые). Обязательные негативные сценарии:")`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="# Правила C-101…C-110 внесены дельтой changes/sbp-subscriptions (2026-09-28, AD-009…AD-011):\n# проверяют запись новых инвариантов и неразр, old_string="# Правила C-101…C-107 внесены дельтой changes/sbp-subscriptions (2026-09-28, AD-009…AD-011):\n# проверяют запись новых инвариантов и неразр)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="  # --- C-101…C-110: рекуррентные списания (подписки), delta sbp-subscriptions ---\n  # C-101…C-104, C-107 — правила ТРАССИРУЕМОСТИ (провер, old_string="  # --- C-101…C-109: рекуррентные списания (подписки), delta sbp-subscriptions ---\n  # C-101…C-104, C-107 — правила ТРАССИРУЕМОСТИ (провер)`

Round 3: READY. Two minor staleness issues to fix:
- PROPOSAL §6 "11 пунктов" → 14.
- CONSTRAINTS.yaml header comments "C-101…C-107" and "# --- C-101…C-109" → C-101…C-110.

Let me fix those, then write REVIEW.md, then update README, then final gate re-run (cheap) and finish.

Let me fix the two staleness items.
**Round 3 verdict: READY.** Two minor stale counts remain — fixing those, then recording the review trail.

  `write_file(content="# Состязательное ревью пакета изменения: `sbp-subscriptions`\n\n- Date: 2026-09-28\n- Область: `changes/sbp-subscriptions/` + сопутствующие, file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/changes/sbp-subscriptions/REVIEW.md")`

Now write REVIEW.md (the adversarial review record). Include round 1 verdict NOT-READY with findings summarized, fixes, round 2 NOT-READY with 7, fixes, round 3 READY. This is the artifact referenced by PROPOSAL §10.

Then update README.md to list the change package.

Then final gate re-run.

Let me write REVIEW.md.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/README.md")`

Now update README.md to include the change package and status. Let me read README and edit.

README content (from earlier):
```
# Платёжный шлюз СБП (C2B-приём)
...
- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: ...
- Статус: решение подготовлено, **ожидает человеческого решения A3** ...

## Структура
...
```

Add a section about the change / delta, and add files. Let me edit: add a line under status about the subscriptions change, and add files to structure.

Let me do minimal edits.

  `edit(file_path="<HARNESS>/runs-v2/cells/wtnkjmc/ws/README.md", new_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITEC, old_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITEC)`

The README earlier content:
```
# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).

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

Let me update: add change package line, update contract versions, spine AD-001..AD-011, add new files.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wtnkjmc/ws && echo \"==== gate ====\"; arch-be gat, description="Final gate run and file inventory")`
  `tool_call(arguments={"path": "<HARNESS>/runs-v2/cells/wtnkjmc/ws"}, name="mcp__spine__fitness_check")`

Final gate re-run to confirm everything still green after last edits (README edit doesn't affect gates; CONSTRAINTS comment edit does affect fingerprint but rules unchanged). Let me run final gate + fitness + delta guard quickly. Also check git status to list created/modified files for the final report.

Then write the final summary answer.

Let me run.
Final verification pass and file inventory.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wtnkjmc/ws && rmdir .qwen/tmp 2>/dev/null; ls chan, description="Clean empty temp dir and list change package")`

Everything green. Note `.qwen/settings.json` was already modified before I started (pre-existing, per git snapshot) — I must not touch it. `.arch-handoff/mcp-calls.jsonl` is a side-effect of MCP calls (untracked log) — not mine intentionally; I should mention it. Actually it was already untracked at start (`?? .arch-handoff/mcp-calls.jsonl` appeared in the very first git status). So it's pre-existing/unrelated — leave it.

Also I created `.qwen/tmp/` (mkdir) — empty, not shown in git status (empty dirs aren't tracked). I should clean it up since it's empty and I only made it for a tmp dir I didn't use. Let me remove it to leave the tree clean. It's empty; `rmdir`. Is that safe? Yes, empty dir I created. Let me remove.

Let me also verify no stray files in changes/ besides the 3.

`changes/` untracked shows as directory; contains DELTA.md, PROPOSAL.md, REVIEW.md. Good.

Let me clean .qwen/tmp.

Then produce the final summary in Russian, listing created/modified files, the 7 deliverables, verification evidence, and what remains for the human.

Let me rmdir .qwen/tmp.


Note `.qwen/settings.json` was modified before I started (pre-existing per the initial git snapshot: "M .qwen/settings.json"). I did not modify it. Good — I'll note it's pre-existing.

Now write the final answer in Russian. Structure:
1. Кратко: что сделано, маршрут, где пакет.
2. 7 деливераблов — по пунктам с ключевыми решениями.
3. Верификация (машинные гейты + независимое ревью 3 прогона).
4. Что остаётся человеку.
5. Список созданных/изменённых файлов.

Keep it reasonably concise but complete. Note the auto-route caveat. Note the residual gaps.

Let me write.
Готово. Пакет изменения подготовлен, проверен машинным контуром и тремя раундами независимого состязательного ревью (финальный вердикт — **READY**).

## Что сделано

Изменение встроено **поверх** принятого решения, без отмены ADR-001…007 и AD-008: добавлена долгоживущая сущность «согласие плательщика» (мандат) и рекуррентное списание как **вид платежа** (переиспользует статусную машину, outbox, идемпотентность, сагу возвратов, АБС). Принятые файлы (spine, CONSTRAINTS) менялись только принятым в репозитории способом — **дельтой** `changes/sbp-subscriptions`.

## 1. Значимость и маршрут
`significance_score` → **Critical, 10/15** (`criticality_or_exception`, `financial_impact`, `consistency_model_change`, `api_contract_change`, `new_component`…). Отсюда — полный Solutioning + обязательная человеческая точка A3. `docs/solutioning-subscriptions.md`, `PROPOSAL.md §1`.

## 2. Влияние на принятую архитектуру
**Не меняются**: AD-001, AD-004, AD-006, AD-007, AD-008/ADR-007, АБС-интеграция (ADR-005), trust-зоны, стратегия «гибрид». **Расширяются**: AD-002, AD-003, AD-005 (усиление). **Новые**: AD-009 (списание только по `ACTIVE`-мандату, резервация периода), AD-010 (аддитивная эволюция контракта), AD-011 (пики биллинга — очередью). Автоплатежи выведены из Deferred. `PROPOSAL.md §2`, `ARCHITECTURE-SPINE.md`.

## 3. Архитектурное решение
Пять ADR (по одному решению, с альтернативами, отрицательными последствиями и обратимостью): **ADR-008** мандат/списание-как-платёж, **ADR-009** консистентность и резервация периода + отзыв-приоритет + ограниченные ретраи (без fallback), **ADR-010** аддитивные минорные версии, **ADR-011** выравнивание/допуск/приоритеты, **ADR-012** поэтапный запуск + kill-switch.

## 4. Контракты без поломки потребителей
`openapi/tsp-api.yaml` v0.1.0 → **v0.2.0** аддитивно: новые пути `/v1/mandates*`, опциональные поля `Payment`, enum `Payment.status` **не изменён**. Доказательство механическое: `openapi_lint` PASS, `contract_diff` — **0 breaking, 6 non-breaking**; fitness C-105/C-106/C-108/C-109 сторожат сохранность путей/enum/required.

## 5. Измеримые NFR
`docs/nfr.md §7`: распространение отзыва p95 ≤ 60 с; дубли за период = **0**; списания без `ACTIVE`-мандата = **0**; инициация p95 ≤ 300 мс; пик биллинга sustained 300 / burst 1500 TPS; RPO=0 распространяется на мандаты/списания. Согласовано с §2 (бюджет мощности), opkc-adapter §7 и RFP.

## 6. Критерии приёмки и откат
14 проверяемых критериев (включая негативные: дубль, гонка «отзыв↔списание», списание без согласия, недоступность вендора в пик) — `DELTA.md`. Откат: фиче-флаг `recurring-debits` + kill-switch (числовые триггеры в ADR-012 §3); принятые списания **удерживаются, не теряются**; обслуживание выданных согласий продолжается; разовый приём не зависит от флага.

## 7. Что остаётся человеку-архитектору (A3)
Машинно-читаемый пакет в `PROPOSAL.md §8` (`decided_by` пуст — подписывает человек): модель согласия (зависит от протокола НСПК), версия контракта, политика dunning, политика «осевшего» после отзыва списания, пиковые цели (нужен бизнес-профиль), расширение вендора (текущий vs RFP), правовая модель согласия/уведомлений, ПДн и срок хранения, объём пилота. Протокольные и коммерческие входы помечены `[ТРЕБУЕТ ПРОВЕРКИ]`.

## Верификация
- **Машинно**: `fitness_check` PASS (17 правил, 0 нарушений, ослаблений нет), `spine_lint` PASS, `delta_guard` PASS (spine покрыт дельтой), `openapi_lint` PASS, `contract_diff` 0 breaking, `arch-be gate --repo .` **PASS**, `gate --route critical` — все составляющие PASS (в т.ч. `sensors`); итог **INCOMPLETE (exit 3)** только из-за отсутствия в репозитории `model/` и evidence-бандла («нечем проверить», а не «проверено и плохо»).
- **Честная оговорка**: авто-маршрут гейта дал **Fast** (детектор читает только git-дифф и не видит ADR/спайн/NFR), заявленный маршрут — **Critical**; в CI запускать `--route critical`. Зафиксировано в `PROPOSAL §10`.
- **Независимое ревью**: 3 прогона; прогон 1 — NOT-READY (2 blocker, 10 major/minor), прогон 2 — NOT-READY (7 остаточных), прогон 3 — **READY**. Все находки закрыты (в т.ч. blocker про конкурентный дубль → безусловная резервация периода; blocker про возврат без `qrId` → адресация `debitRef`). Журнал — `changes/sbp-subscriptions/REVIEW.md`.

## Созданные и изменённые файлы

**Создано:**
- `changes/sbp-subscriptions/DELTA.md` — дельта-спека (ADDED/MODIFIED/REMOVED, критерии, fitness), покрывает защищённые файлы
- `changes/sbp-subscriptions/PROPOSAL.md` — пакет на архрешение (7 разделов + A3-пакет + верификация)
- `changes/sbp-subscriptions/REVIEW.md` — журнал независимого ревью
- `docs/solutioning-subscriptions.md` — Solutioning дельты
- `docs/spec/mandate-state-machine.md` — статусная машина мандата и вход списания
- `docs/adr/ADR-008…ADR-012` (5 файлов) — решения дельты

**Изменено:**
- `ARCHITECTURE-SPINE.md` — AD-009…AD-011, правки AD-002/003/005, Deferred/контракты
- `.arch-handoff/CONSTRAINTS.yaml` — правила C-101…C-110
- `openapi/tsp-api.yaml` — контракт v0.2 (аддитивно)
- `docs/contracts/tsp-api.md`, `docs/contracts/opkc-adapter.md` — контракты v0.2
- `docs/nfr.md` — §7 и бюджет мощности; `docs/rfp/vendor-rfp.md` — G8/P9–P13; `docs/spec/state-machine.md` — §7 и обязательные секции; `docs/solutioning.md` — указатель на дельту и границы scope; `README.md` — структура и статус

*(`.`qwen/settings.json` был изменён до начала работы — не трогал; `.arch-handoff/mcp-calls.jsonl` — служебный лог MCP-вызовов, тоже не мой артефакт.)*
