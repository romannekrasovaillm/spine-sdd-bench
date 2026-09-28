<!-- источник: <HARNESS>/runs-clean/cells/wd33eb5/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-clean-cells-wd33eb5-ws/chats/d84e0c43-13f4-4cd0-9a2f-a2a77b36f956.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `glob(pattern="**/*")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/README.md")`

Let me start by understanding the repository. This is a significant architectural task for a bank payment gateway (СБП C2B). The user wants an architectural package for recurring C2B payments (subscriptions) on top of an accepted solution.

I need to:
1. Assess significance and route
2. Impact on accepted architecture (invariants)
3. Architectural decision with alternatives, consequences, reversibility
4. Contract changes without breaking consumers
5. Measurable NFRs
6. Acceptance criteria and rollback plan
7. What remains for a human architect

The repository has Spine tools available, and there's a rich set of skills. Let me first read the actual files to understand the accepted solution.

Let me start by exploring the repository structure and reading key files. I should use the skills that are relevant — particularly significance-routing, spine-invariants, adr-authoring, nfr-design, delta-spec (since this is a change on top of existing system), and possibly spine-architect-review.

Actually, the task is quite clear. Let me be systematic. First, read the key files:
- ARCHITECTURE-SPINE.md (invariants AD-001..AD-008)
- docs/solutioning.md
- docs/nfr.md
- docs/adr/* (ADR-001..007)
- docs/contracts/*
- openapi/tsp-api.yaml
- .arch-handoff/* (CONSTRAINTS.yaml, TASK.md, etc.)

Let me also check what's in the docs directory more fully.

Let me start with parallel reads and globs.
Начинаю с изучения принятого решения. Сначала составлю карту репозитория и прочитаю ключевые файлы.

  `glob(pattern="docs/**/*")`
  `glob(pattern=".arch-handoff/**/*")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/nfr.md")`

Let me read the key documents. I need to read the full list of docs, ADRs, contracts, solutioning, nfr, state machine, CONSTRAINTS.yaml, TASK.md, MANIFEST, and the openapi contract.

Let me read the docs directory contents fully.
Читаю ключевые документы принятого решения: solutioning, NFR, контракты, статусную машину, ADR и handoff-пакет.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/openapi/tsp-api.yaml")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/spec/state-machine.md")`

Now let me read the contracts, state machine, ADRs, and handoff files.
Читаю контракты, статусную машину, ADR и handoff-пакет.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/adr/ADR-001-outbox.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/adr/ADR-002-model-konsistentnosti-)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/adr/ADR-004-at-least-once-dlq.md")`

Now let me read the ADRs (001-007), CONSTRAINTS.yaml, TASK.md, MANIFEST.json, RUBRIC.yaml, connect-manifest.json, and ARCHITECTURE.md in .arch-handoff.
Читаю ADR и handoff-пакет, чтобы понять принятые правила и способ внесения изменений.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/adr/ADR-005-integraciya-s-abs-zach)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.arch-handoff/CONSTRAINTS.yaml")`

Let me read the remaining ADRs (005, 006, 007), and the handoff files (CONSTRAINTS.yaml, TASK.md, MANIFEST.json, RUBRIC.yaml, connect-manifest.json, ARCHITECTURE.md).

  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.arch-handoff/connect-manifest.json")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.arch-handoff/ARCHITECTURE.md")`

Now let me read the remaining handoff files: TASK.md, MANIFEST.json, RUBRIC.yaml, connect-manifest.json, ARCHITECTURE.md.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.qwen/skills/significance-routing/SKILL)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.qwen/skills/spine-invariants/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.qwen/skills/adr-authoring/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.qwen/skills/delta-spec/SKILL.md")`

Now I have a complete understanding of the repository. Let me also look at the key skills I need to use. The task is quite clear now. I need to prepare an architectural package for a change: recurring C2B payments (subscriptions) by payer consent.

The key question is: what does "рекуррентные C2B-списания по согласию плательщика — подписки СБП" actually mean in the СБП context? This is the "подписки СБП" / "автоплатежи" — recurring payments via СБП using a previously issued consent (согласие). In СБП there's a mechanism for this.

Actually, in the СБП ecosystem, recurring/auto-payments work via "согласие" (consent) that the payer gives in their bank's app. The merchant then initiates debits against that consent without the payer needing to scan QR each time. This is the "подписка СБП" (СБП-подписка / автоплатеж).

Note: the solutioning.md explicitly lists "автоплатежи" as roadmap (out of scope). So this change is pulling one roadmap item into scope.

Let me think about what the change means architecturally:

1. **New concept: Consent (согласие плательщика)** — a persistent authorization. The payer, in their bank app (via СБП), grants consent to a specific ТСП for recurring debits (with max amount, period, expiry, etc.).

2. **New concept: Recurring payment / debit (рекуррентный платёж)** — initiated by ТСП against a consent, without QR/payer action.

3. New API endpoints: register consent, list consents, cancel consent, create recurring payment.

4. New status machine for consent and for recurring payments (or extension of existing payment machine).

5. New ОПКЦ adapter operations: consent registration/status, recurring debit initiation.

Now, the task says: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — meaning: how to modify accepted decision files. Looking at the repo, the way changes are made is via delta-spec (OpenSpec) — actually there's a skill "delta-spec" for brownfield changes. But also the ADR authoring skill and spine-invariants skill.

Wait, let me check: is there an OpenSpec setup? The MCP tools mention openspec_coverage, delta_guard. But the repo has `docs/adr/`, `ARCHITECTURE-SPINE.md`, `.arch-handoff/`. There's no `openspec/` directory in the glob results. So the "accepted way" here is:
- ADR files in `docs/adr/ADR-NNN-*.md`
- Spine invariants in `ARCHITECTURE-SPINE.md`
- Contracts in `docs/contracts/*.md` and `openapi/tsp-api.yaml`
- NFR in `docs/nfr.md`
- solutioning in `docs/solutioning.md`

The delta-spec skill is about OpenSpec's propose/apply/archive. But there's no openspec dir. Let me check the delta-spec skill and spine-invariants skill and adr-authoring skill to understand the canonical way.

Actually, the key instruction is: "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." So I should use:
- `significance-routing` skill → assess significance/route
- `spine-invariants` skill → how to modify the spine
- `adr-authoring` skill → how to write ADRs
- `nfr-design` skill → NFRs
- `delta-spec` skill → brownfield change (delta)
- `spine-contracts-gate` / openapi lint → contract changes

Let me load the most relevant skills to follow the canonical method. Actually, I should be judicious. The task is essentially to produce an architectural package. Let me load a few key skills:

1. `significance-routing` — for the significance assessment (item 1)
2. `adr-authoring` — for the ADR (item 3)
3. `spine-invariants` — for impact on invariants (item 2)
4. `delta-spec` — for how to structure the change (brownfield)

Actually, since these are project skills already loaded into my context via the system reminder (their descriptions), but the actual SKILL.md content has methodology. Let me load the key ones to follow the canonical method properly.

Let me also check the significance_score MCP tool — I can actually call it to get the significance route programmatically. But it takes a diff. Actually there's `significance_from_diff` and `significance_score` (15 triggers). Let me consider using the MCP tools.

Actually, the most important thing: I should use the Spine MCP tools as they're the "инструменты" mentioned. But wait — I need to be careful. Let me first understand what the canonical way to change is.

Let me load the skills that matter. Let me read:
- significance-routing SKILL.md
- spine-invariants SKILL.md
- adr-authoring SKILL.md
- delta-spec SKILL.md
- nfr-design SKILL.md (maybe)

Let me read these in parallel.
Я получил полную картину принятого решения. Теперь изучу методические навыки, чтобы следовать канону репозитория (значимость, инварианты, ADR, дельта-изменение, NFR).

  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.qwen/skills/adr-authoring/references/a)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.qwen/skills/spine-invariants/reference)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.qwen/skills/nfr-design/SKILL.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.qwen/skills/spine-contracts-gate/SKILL)`

I now have all the context I need. Let me also check the adr-template.md and spine-template.md reference files briefly, and the nfr-design skill and spine-contracts-gate skill (for how contract changes are done).

Actually, let me think about the significance. This is clearly a Critical-path change. Let me evaluate the 15 triggers:

For recurring C2B payments (subscriptions):
- new_component: possibly a new "consent manager" / "subscription engine" component — yes
- new_datastore: consent store — yes (new data store for consents)
- new_vendor: no (same НСПК/ОПКЦ transport)
- domain_ownership_change: no
- cross_domain_integration: no
- api_contract_change: yes (new endpoints, extend contract)
- data_contract_change: yes (consent data model)
- security_boundary_change: no
- trust_zone_change: no (consent handled in same trust zones)
- consistency_model_change: yes (consent lifecycle is a new state machine / consistency model)
- significant_nfr: potentially yes (recurring debits, scheduled processing)
- rto_rpo_targets: same (RPO=0)
- irreversible_migration: no
- financial_impact: yes (money moves without payer action per event — HIGH financial impact)
- criticality_or_exception: the whole gateway is already Critical

So triggers: new_component, new_datastore, api_contract_change, data_contract_change, consistency_model_change, financial_impact = 6 triggers → Critical route.

This is a Critical path change → full Solutioning (not delta-spec). So I need:
- ADR (new ADR-008)
- Spine impact (possibly new AD-009, or modifications to existing)
- NFR additions
- Contract changes (OpenAPI + tsp-api.md)
- Acceptance criteria + rollback
- Human decision points

Now, the key architectural question for this change: **How do СБП subscriptions/recurring payments work?**

In СБП, the mechanism for recurring payments is the "согласие" (consent). The payer authorizes recurring debits in their bank app. This is governed by the СБП rules and the НСПК documentation (which is external input [ТРЕБУЕТ ПРОВЕРКИ]).

Architecturally, the important decision points are:

1. **Consent model**: where is consent stored, what's its lifecycle (создание, подтверждение плательщиком в приложении банка плательщика, отмена, истечение). Consent has: payer ID, merchant (ТСП), max amount per period, periodicity, expiry, status.

2. **Recurring payment vs one-time**: A recurring debit is initiated by ТСП referencing a consent. It goes through the same ОПКЦ/НСПК channel but with a flag/type indicating "recurring" — no QR, no payer action.

3. **Status machine extension**: recurring payment can reuse the payment state machine (CREATED → PAID → CREDITED → COMPLETED) but with a new trigger path (no QR_ISSUED; goes directly from CREATED → PAID upon НСПК confirmation). Or a separate "recurring debit" state machine.

4. **Idempotency**: recurring debits need strong idempotency (avoid double-charging subscriptions). The ТСП sends Idempotency-Key; the шлюз needs a schedule + dedup.

5. **Scheduling**: who triggers the recurring debit? Two models:
   - (a) ТСП initiates each debit via API (merchant-driven) — pull by merchant
   - (b) Шлюз holds a schedule and initiates (bank-driven) — but СБП subscriptions are typically merchant-driven, where ТСП calls the bank to initiate a debit against a consent.

Actually in СБП, recurring payments: the consent is registered, and then the ТСП (merchant) initiates each payment against the consent. The шлюз validates the consent is active and within limits, then debits.

6. **Security/AML**: consent is a high-risk channel (no payer action per transaction) — needs stricter AML/fraud controls, consent limits, velocity checks.

7. **Contract versioning**: existing consumers (ТСП) must not break. Add new endpoints under /v1 (backward compatible additions) or /v2? Adding new endpoints is backward-compatible. But changing the Payment schema (e.g., adding `recurring` fields) must be additive.

Now, let me think about what the "accepted way to modify files" is:
- ADRs are in `docs/adr/ADR-NNN-slug.md` with a specific header format (Date, Status, Owner, Related).
- Spine: `ARCHITECTURE-SPINE.md` with AD-n blocks.
- Contracts: `docs/contracts/*.md` + `openapi/tsp-api.yaml`.
- NFR: `docs/nfr.md`.
- solutioning: `docs/solutioning.md`.

The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." This means:
- New ADR gets a new number ADR-008 (not modifying ADR-001..007).
- Spine: add AD-009 (new invariant) rather than rewrite AD-001..008; possibly update Deferred section (remove "автоплатежи" from roadmap/Deferred).
- Contracts: additive changes, version bump consideration.

Let me also check the spine-template and adr-template references, and the nfr-design skill, and spine-contracts-gate skill (which is about openapi_lint and contract_diff).

Actually, I think I have enough. But let me quickly load the nfr-design skill and the spine-contracts-gate skill and adr-template, spine-template to follow canonical formats precisely. And I should check whether there's a model/ directory (the MCP tools reference model/ — but glob showed no model/ directory). So the "model" tools won't apply here — this repo uses prose ADRs + spine, not the typed model/ directory. Good to note.

Let me read the templates and the contracts-gate + nfr-design skills.
Изучаю шаблоны и канон NFR/контрактов, чтобы менять файлы принятым способом.

  `tool_search(query="select:mcp__spine__significance_score,mcp__spine__openapi_lint,mcp__spine__contract_diff,mcp__spine__spine_lint,mcp__spine__fitness_check")`

I now have everything I need. Let me plan the work.

The task is a Critical-path architectural change: recurring C2B payments (СБП subscriptions) by payer consent. I need to produce an architectural package.

Let me structure the deliverables:

1. **Significance assessment** → this is Critical route (6 triggers). I should write this into a new ADR (ADR-008) and possibly a significance summary.

2. **Spine impact**: new AD-009 (consent/recurring invariant) added to ARCHITECTURE-SPINE.md. Also update the Deferred section — "автоплатежи" is listed as out of scope in solutioning.md §1 and in ADR-001 alternatives. Actually in ARCHITECTURE-SPINE.md, Deferred lists "C2C-переводы и выплаты", "Диспуты", "Мультивалютность" — not автоплатежи explicitly. Wait, let me check. The Deferred in spine lists:
- Мультивалютность и иностранные платёжные системы
- C2C-переводы и выплаты B2C/B2B
- Диспуты/претензии

"автоплатежи" is in solutioning.md §1 as roadmap out of scope ("Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи").

So the change pulls "автоплатежи" (recurring) from roadmap into scope. This is consistent.

3. **New ADR-008**: recurring C2B via payer consent (согласие). Decision: consent-based model, merchant-driven initiation, consent as first-class entity with its own lifecycle/state machine, validation against limits, idempotent recurring debits, reuse of payment state machine with a "recurring" payment type. Alternatives considered. Consequences. Reversibility.

Actually, there might need to be more than one ADR. The recurring change touches:
- Consent model & lifecycle (ADR-008)
- Recurring debit flow / how it reuses payment machine (could be in ADR-008)
- Possibly a separate ADR on scheduling/initiation model (merchant-driven vs bank-driven)
- AML/limits for the no-payer-action channel (could be part of ADR-006 or a new one)

For a clean package, I'll do ONE main ADR-008 (the recurring/consent decision) with the merchant-driven model and consent lifecycle, and keep the rest as sections. Actually, given the adr-authoring skill says ">1 page → разбить на несколько ADR", but this is a coherent single decision (recurring model). I think one ADR-008 is appropriate, possibly with a second ADR-009 for the AML/consent limits if it's a distinct decision. Let me keep it to ONE ADR to avoid over-engineering, but the ADR should note the AML considerations as a human-decision point.

Actually, let me reconsider. The recurring change has two genuinely distinct architectural decisions:
1. **Consent as first-class entity + merchant-driven recurring debit** (the core model) — ADR-008.
2. **Security/AML posture for the no-payer-action channel** (limits, velocity, consent revocation, fraud) — this is significant enough and involves a new trust/risk consideration, but it's really an extension of ADR-006 (НПС/КИИ/ПДн) + AD-007. Could be a sub-part.

I'll do one ADR-008 covering the core model, and explicitly list the AML/consent-limit as human-decision points (item 7 of the task). That's cleaner and honest.

4. **Contract changes**: 
- `openapi/tsp-api.yaml`: add endpoints `/v1/consents`, `/v1/consents/{consentId}`, `/v1/consents/{consentId}/cancel`, and extend `/v1/payments` to support recurring debit (add `consentId` + `paymentType` optional fields). Backward compatible (additive only). I need to actually edit the YAML.
- `docs/contracts/tsp-api.md`: add §3.6 Consent endpoints + §3.7 recurring payment, extend §2 idempotency note about consent, §6 versioning note.
- `docs/contracts/opkc-adapter.md`: add consent operations to the adapter contract (registerConsent, cancelConsent, getConsentStatus, and recurring debit initiation).

5. **NFR**: add a new section to docs/nfr.md for recurring payments (latency for consent creation, debit throughput, consent validation latency, no-double-charge = 0, etc.).

6. **Acceptance criteria + rollback plan**: these go into a new document or into solutioning.md. I think the cleanest is to add a new section to solutioning.md OR create a dedicated document. Given the repo structure, I think:
   - Update solutioning.md to add recurring as a new section (components, flows, state machine extension, gaps, open questions, rollback).
   - Actually solutioning.md is the "полный дизайн". I should extend it with a recurring section, but carefully (it's a big file). Alternatively create `docs/recurring-c2b.md` as a focused solutioning addendum. 

Hmm. The task says "Подготовь архитектурный пакет этого изменения поверх принятого решения". And "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." This means: when I DO modify accepted decision files, do it the accepted way. It doesn't say I must modify solutioning.md. 

I think the cleanest, most reviewable approach is:
- **New ADR-008** (the decision) — this is the "accepted way" to add a decision.
- **Extend ARCHITECTURE-SPINE.md** with AD-009 (consent invariant) — the accepted way to add an invariant.
- **Extend openapi/tsp-api.yaml** (additive) — contract change.
- **Extend docs/contracts/tsp-api.md** and **opkc-adapter.md** (additive sections).
- **Extend docs/nfr.md** with a recurring section.
- **Update docs/solutioning.md** — add a recurring section, and update the "roadmap out of scope" note to remove автоплатежи.
- **Update .arch-handoff/TASK.md**? No — TASK.md is for the walking skeleton of the BASE solution. The task is to prepare the package for a human A3 decision, not to hand off to coders yet. The task explicitly says "чтобы его можно было вынести на архитектурное решение и затем передать исполнителям" — so the package is for the A3 decision, and handoff comes later.

Let me also reconsider: the task says "Оценка значимости изменения и маршрута" — I should run significance_score or at least document the triggers. I can use the MCP tool `significance_score` or `significance_from_diff`. Actually, since there's no diff yet (I haven't changed files), significance_from_diff won't work well. I can use `significance_score` with explicit triggers? Let me check its schema. Actually, the significance_score tool computes from "15 triggers" — I should check what input it takes. Let me look.

Actually, let me use the MCP tools available. The key ones I could meaningfully use:
- `significance_score` — to formally get the route. But it may need a diff or specific inputs.
- `spine_lint` — to validate my spine changes.
- `openapi_lint` — to validate my contract changes.
- `contract_diff` — to show the contract change is non-breaking.
- `fitness_check` — to verify CONSTRAINTS.yaml still passes.

These are genuinely useful for verification. Let me use them after making changes.

Let me first check the significance_score schema and the significance_from_diff, openapi_lint, contract_diff, spine_lint schemas.

Actually, let me be efficient. I'll use tool_search to review the schemas of significance_score, openapi_lint, contract_diff, spine_lint, fitness_check.

Let me think about whether I should run these tools. The task says "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." The Spine MCP tools are the "инструменты". Using them to verify my work is exactly "по назначению". And they're read-only/deterministic (openapi_lint, contract_diff, spine_lint, fitness_check, significance_score). Good.

Let me review schemas first.

Actually, let me plan my actual edits and then verify.

Let me now think carefully about the CONTENT of the architecture. This is the substantive part.

## The domain: СБП subscriptions / recurring payments

In СБП, recurring C2B debits (подписки, автоплатежи) work via **согласие плательщика** (payer consent). The flow:
1. ТСП requests a consent from the payer via the шлюз (consent creation request).
2. The payer approves the consent in their own bank's app (via СБП/НСПК — the consent is registered in НСПК).
3. Once active, ТСП can initiate recurring debits against the consent — each debit goes through НСПК and is debited from the payer's account without the payer's per-transaction action.
4. Consent has limits (max amount per debit, max total per period, expiry, allowed periodicity). Consent can be revoked by payer or ТСП or on AML grounds.

The precise НСПК protocol details for consents are external input [ТРЕБУЕТ ПРОВЕРКИ] — consistent with the rest of the repo where protocol details are marked.

Key architectural decisions for the шлюз:

### ADR-008: Consent-first recurring model

**Decision**: Introduce "согласие плательщика" (consent) as a first-class domain entity with its own lifecycle state machine in the шлюз БД. Recurring debits are merchant-driven: ТСП initiates each debit via `POST /v1/payments` referencing `consentId`; the шлюз validates the consent (active, within limits, not expired), then routes through the same ОПКЦ adapter and payment state machine (CREATED → PAID → CREDITED → COMPLETED, no QR_ISSUED for recurring). Consent limits are enforced by the шлюз as the authoritative guard (НСПК may also enforce, but шлюз does not rely on it).

**Consent state machine**: `PENDING` (created, awaiting payer approval in НСПК) → `ACTIVE` → `CANCELLED` | `EXPIRED` | `REVOKED`. Possibly `SUSPENDED` for AML.

**Consent fields**: consentId, tspId, payerRef (opaque, minimal ПДн), merchantOrderId, maxAmountPerDebit, maxTotalPerPeriod, period, expiresAt, status, revokedReason, limits.

**Recurring debit**: reuse payment machine with `paymentType=recurring` and `consentId`. Transition: CREATED → PAID (skips QR_ISSUED). Idempotency by Idempotency-Key + consentId + periodKey (to prevent double-charging the same subscription period). A "periodKey"/"billingPeriod" dedup key prevents double-debit for the same subscription billing cycle.

**Alternatives**:
- A. Bank-driven scheduler (шлюз holds the schedule and auto-debits) — pros: centralized control; cons: шлюз becomes a scheduler (clock, time zones, cron), more complexity, СБП consents are typically merchant-initiated, and the merchant knows its own billing cycle. Rejected.
- B. No consent entity, just "recurring flag" on payment — pros: minimal; cons: no way to enforce limits/revocation, no audit trail of consent, violates "одна сумма" discipline. Rejected.
- C. Consent stored only in НСПК, шлюз passes through — pros: less storage; cons: шлюз loses authoritative limit enforcement and RPO=0 on consent state; depends on НСПК availability for every validation. Rejected.

**Consequences**:
- Positive: no double-charging (periodKey + idempotency), payer control (revocation), limits enforced locally, audit trail, reuse of existing machine/outbox/adapter.
- Negative: new entity + lifecycle + store; consent state must be reconciled with НСПК (second source of truth like АБС); merchant-driven model means шлюз trusts ТСП to not over-bill (mitigated by limits + AML); consent revocation propagation to in-flight debits.

**Reversibility**: reversible — the consent entity and merchant-driven model can be extended (bank-driven scheduler later) without rework of the payment machine; limits can be tightened. Not irreversible migration.

### Spine AD-009

Test of belonging: "Могут ли два независимых исполнителя выбрать несовместимо?" — Yes: one team might make consent just a flag on payment, another a full entity; one might skip limit enforcement; one might not dedupe subscription periods. So a new invariant AD-009 is warranted:

**AD-009. Рекуррентное списание — только по активному согласию с локальным enforcement лимитов**
- Binds: БД шлюза (состояние согласия), статусная машина, вход ТСП (`consentId`), адаптер ОПКЦ.
- Prevents: списание без активного согласия; превышение лимитов согласия (сумма/период); двойное списание за один период подписки.
- Rule: Рекуррентный платёж создаётся только при активном согласии; сумма ≤ лимита; уникальность по `consentId + periodKey`; переход в `PAID` без `QR_ISSUED`. Fitness: тест «неактивное/истёкшее согласие → отказ», «повтор periodKey → идемпотентно».

Also I need to update Deferred section? The spine Deferred doesn't list автоплатежи explicitly. But solutioning.md roadmap lists автоплатежи as out of scope. I should update solutioning.md to move автоплатежи into scope.

Actually wait — I should double check: does AD-008 (strategy) or anything reference автоплатежи as out of scope? solutioning.md §1: "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." So yes, update that.

### Contract changes (backward-compatible)

**openapi/tsp-api.yaml** — additive:
- Add `paymentType` enum (optional) to PaymentRequest: `one_time` (default) | `recurring`. And optional `consentId` + `periodKey`.
- Add new paths: `/v1/consents` (POST), `/v1/consents/{consentId}` (GET), `/v1/consents/{consentId}/cancel` (POST).
- Add Consent schema, ConsentRequest schema.
- Add `paymentType`, `consentId`, `periodKey` to Payment schema (additive).
- Bump version 0.1.0 → 0.2.0 (minor, non-breaking). Actually since existing version is 0.1.0 draft and adding features, bump to 0.2.0. Keep `/v1` path.

Wait, version: The info.version is 0.1.0. The tsp-api.md says "версия 0.1 draft". The contract_diff rule: non-breaking additions = minor bump. 0.1.0 → 0.2.0.

**tsp-api.md** — add §3.6 (consents) and extend §3.2 (recurring payment fields), update §6 versioning note.

**opkc-adapter.md** — add consent operations to the adapter contract table and events. Actually, the consent registration with НСПК: the adapter needs `registerConsent`, `getConsentStatus`, `cancelConsent`, and recurring debit uses existing `createPaymentLink`? No — recurring debit doesn't create a QR/link. It's a different operation: "initiate recurring debit". So add `initiateRecurringDebit` operation to the adapter, plus consent events (`consent.activated`, `consent.revoked`, `consent.expired`).

Hmm, but the precise НСПК protocol for consents/recurring is external [ТРЕБУЕТ ПРОВЕРКИ]. I should mark those adapter operations as [ТРЕБУЕТ ПРОВЕРКИ] and note they're normalized.

### NFR additions

New section for recurring:
- Consent creation/registration latency p95.
- Recurring debit initiation latency p95.
- Double-debit (same period) = 0.
- Debit without active consent = 0.
- Consent validation (active + limits) must be enforced 100% on шлюз side.
- Reconciliation of consent state with НСПК.
- Throughput for recurring debit (same 200 TPS baseline, but subscriptions can cluster at month-start — burst consideration).
- AML: 100% of recurring debits pass velocity/limit checks.

### Acceptance criteria + rollback

Acceptance criteria (EARS): recurring debit only from ACTIVE consent, within limits, dedup by periodKey, revocation blocks new debits, existing in-flight debits complete or fail cleanly.

Rollback: feature-flag on recurring (per-ТСП enable), stop-new consent registration, revocation of consent = immediate stop of new debits without stopping one-time payments. Recurring can be rolled back independently of one-time because it's additive.

### Human decision points (item 7)

1. Exact НСПК consent protocol / recurring debit semantics — external input, must be confirmed before implementation (like base solution).
2. Consent limit/AML policy: what limits, velocity, thresholds; is there a need for a separate AML approval flow for consents? Business + AML owner.
3. Merchant-driven vs bank-driven: I recommend merchant-driven, but the business must confirm (some ТСП want bank-driven auto-renewal). Actually this is an architectural decision I'm making, but there's a business angle (whether subscriptions auto-renew on шлюз side).
4. Whether to support "пробное списание" / zero-amount validation debit (token verification) — НСПК may require a test debit on consent activation.
5. Payer consent revocation propagation: how fast does a payer's revocation in their bank app reach the шлюз (push from НСПК vs poll) — depends on НСПК.
6. Regulatory: 161-ФЗ clause about consents/autopayments — ИБ/комплаенс confirm exact requirements.
7. Refund/chargeback on recurring — existing refund saga applies, but consent re-activation after refund is a business question.

Now, let me also decide the file plan concretely. I'll:

1. Create `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md` (new ADR).
2. Edit `ARCHITECTURE-SPINE.md` — add AD-009 block; update the header comment if needed. Also update Deferred? автоплатежи not in spine Deferred. But I could add a note. Actually no change to Deferred needed in spine.
3. Edit `openapi/tsp-api.yaml` — additive changes + version bump.
4. Edit `docs/contracts/tsp-api.md` — add consent + recurring sections, update versioning.
5. Edit `docs/contracts/opkc-adapter.md` — add consent/recurring adapter operations + events.
6. Edit `docs/nfr.md` — add recurring NFR section.
7. Edit `docs/solutioning.md` — add recurring section, update roadmap note (автоплатежи → in scope), update open questions.
8. Optionally update `.arch-handoff/CONSTRAINTS.yaml`? No — the CONSTRAINTS.yaml currently has rules about the base. Adding a fitness rule for the new invariant would be consistent with the fitness-functions skill. But the task is about the A3 package, not handoff. I think adding a couple of fitness rules for AD-009 would be appropriate and "по назначению" — but let me be careful. Actually, the CONSTRAINTS.yaml is "Этап: решение (до кода)". Adding a must_contain rule for the new ADR and the consent invariant would be consistent. But I'll keep it minimal — maybe add a rule for the new ADR existence and the consent invariant phrase, mirroring the existing `abs-credit-only-from-paid` rule.

Actually, let me focus. The core deliverables are items 1-7. Let me map:

1. Значимость → ADR-008 (Context includes significance) + I'll present it in my final summary. Maybe a dedicated note. I'll put the significance assessment in the ADR context and in solutioning.

2. Влияние на архитектуру → spine AD-009 + the ADR's "Related" and a section. Also solutioning update.

3. ADR → ADR-008.

4. Контракты → openapi + tsp-api.md + opkc-adapter.md.

5. NFR → nfr.md.

6. Критерии приёмки + откат → ADR-008 has rollback? No, ADR has Reversibility. Acceptance criteria + rollback go to solutioning.md (which has §7 гейты/приёмка and §8 план отката). I'll add recurring-specific acceptance criteria and rollback to solutioning.md.

7. Остаётся на человека → solutioning.md "Открытые вопросы" + ADR "человеческая точка A3" section + my final summary.

Let me now also decide whether to add a new dedicated doc vs. editing solutioning.md. Given solutioning.md is "полный дизайн", editing it is the accepted way. But it's large. I'll add a new section "11. Рекуррентные C2B-списания (подписки СБП)" — actually I'll insert it as a new top-level section. Let me add after section 4 (flows) or after section 5. Hmm, cleaner to add a dedicated section at the end (before gaps?) or integrate. 

Actually, the cleanest and most reviewable: add a new major section to solutioning.md, e.g., "## 11. Изменение: рекуррентные C2B-списания (подписки СБП)" at the end, plus update §1 (roadmap) and §9 (gaps) and §10 (open questions). But solutioning.md's sections are numbered 1-10. I'll add a section 11 and also update §1 roadmap and §9 gaps and §10 open questions. Wait, but that would put the new section after "open questions" which is §10. That's a bit awkward but acceptable. Alternatively, I create a separate file `docs/recurring-c2b.md` for the focused change package, and cross-reference from solutioning.md §1 (moving автоплатежи out of roadmap).

Hmm. Given the instruction "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" and the fact that this is a "пакет изменения поверх принятого решения", I think a cleaner approach that respects the repo's conventions:

- The **decision** goes in `docs/adr/ADR-008-*.md` (the accepted way for decisions).
- The **invariant** goes in `ARCHITECTURE-SPINE.md` (accepted way for invariants).
- The **contract** goes in `openapi/tsp-api.yaml` + `docs/contracts/*.md` (accepted way).
- The **NFR** goes in `docs/nfr.md` (accepted way).
- The **design/acceptance/rollback/gaps** — I'll add to `docs/solutioning.md` (the full design doc) with a new section, and update its roadmap note. This is the accepted way for design.

I'll also update `.arch-handoff/CONSTRAINTS.yaml` minimally to add a fitness rule guarding the new invariant (mirrors existing pattern `abs-credit-only-from-paid`), since the fitness-functions skill says invariants should have machine checks. This is "по назначению". Actually, I'll add:
```yaml
  - name: recurring-credit-requires-active-consent
    type: must_contain
    glob: "docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md"
    pattern: 'только при активном согласии'
    severity: error
```

Hmm wait, but CONSTRAINTS.yaml is currently the "decision-stage" fitness rules. Adding a rule referencing the new ADR is consistent. But is it necessary? The task doesn't explicitly ask for it. But item 2 says "какие инварианты затронуты, что меняется". Adding the invariant to spine is the main thing. I'll add the fitness rule too as it's the accepted mechanism and the fitness-functions skill strongly implies invariants → fitness functions. I'll keep it to one rule.

Actually, let me reconsider scope. The task is substantial and asks for a lot. I should be thorough but not over-engineer. Let me finalize the plan:

**Files to create:**
1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`

**Files to edit:**
2. `ARCHITECTURE-SPINE.md` — add AD-009
3. `openapi/tsp-api.yaml` — additive + version bump
4. `docs/contracts/tsp-api.md` — consent + recurring sections
5. `docs/contracts/opkc-adapter.md` — consent/recurring adapter ops + events
6. `docs/nfr.md` — recurring NFR section
7. `docs/solutioning.md` — new section + roadmap update + gaps + open questions
8. `.arch-handoff/CONSTRAINTS.yaml` — add fitness rule

Then verify with Spine tools (spine_lint, openapi_lint, contract_diff, fitness_check, significance_score).

Let me also check the significance_score tool schema to see if I can formally run it. And openapi_lint, contract_diff, spine_lint, fitness_check schemas.

Let me now proceed. First, review tool schemas.
Я получил полную картину. Теперь проверю схемы инструментов Spine для верификации (значимость, линты, diff, fitness).

  `tool_call(name="mcp__spine__significance_score", arguments={"triggers": {"new_component": true, "new_datastore": true, "new_vendor": false, "domain_ownership_change": false, "cross_domain_integration)`

Let me run the significance_score tool first to formally establish the route. The 15 canonical triggers are: new_component, new_datastore, new_vendor, domain_ownership_change, cross_domain_integration, api_contract_change, data_contract_change, security_boundary_change, trust_zone_change, consistency_model_change, significant_nfr, rto_rpo_targets, irreversible_migration, financial_impact, criticality_or_exception.

My assessment:
- new_component: true (consent manager / subscription engine as new logical component)
- new_datastore: true (consent store)
- new_vendor: false
- domain_ownership_change: false
- cross_domain_integration: false
- api_contract_change: true (new endpoints)
- data_contract_change: true (consent data model)
- security_boundary_change: false
- trust_zone_change: false
- consistency_model_change: true (consent lifecycle = new state machine / consistency)
- significant_nfr: false? or true? Recurring adds burst considerations but not really a change to significant NFR targets. I'll say false (targets unchanged, just extended).
- rto_rpo_targets: false (unchanged)
- irreversible_migration: false
- financial_impact: true (money moves without per-transaction payer action)
- criticality_or_exception: true? The whole gateway is already Critical. Adding recurring doesn't add a NEW criticality. But it does add a new high-risk channel. Hmm. I'll leave criticality_or_exception as false to be honest (the project is already Critical, this change doesn't change criticality classification). Actually "criticality_or_exception" — is this an exception/high-criticality change? The change is on top of an already-critical system. I'll set false.

So: new_component, new_datastore, api_contract_change, data_contract_change, consistency_model_change, financial_impact = 6 triggers → Critical.

Let me run significance_score with these to formally get the route. I'll run it now as part of my evidence.

Actually, I can run it in parallel with the initial work. But it's cheap. Let me run it now.

Let me run significance_score.
Формально фиксирую маршрут значимости через инструмент Spine.

  `write_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisa, content="# ADR-008. Рекуррентные C2B-списания: согласие плательщика как сущность первого класса с локальным enforcement лимитов\n\n- Date: 2026-09-2)`

Route confirmed: Critical, score 6. Now I'll proceed to write the files.

Let me write the files. First the ADR-008 (the core decision), then spine AD-009, then contracts, NFR, solutioning, CONSTRAINTS.

Let me carefully write the ADR-008. The header format used in existing ADRs:
```
# ADR-008. <title>

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур)
- Related: ADR-001, ADR-002, ADR-003, ADR-004, ADR-006, AD-009
```

I should also add the `- Author-model:` / model-author field? The adr-authoring skill says the parser understands `- Модель-автор:`, `- Author-model:`, `- Автор-модель:`. Since I (an AI agent) am writing this, I should mark the author honestly. The existing ADRs have "Owner: solution-architect (платёжный контур)" but no Author-model field. To be consistent with the repo AND honest about authorship, I'll add `- Author-model: qwen` or similar. Actually, let me look at what the rubric judge expects. The skill says "Пишите `human` или `human:<имя>`, если документ писал человек, и метку модели, если его собрал агент." Since I'm an agent, I should write a model label. I'll add `- Author-model: qwen-code`. Hmm, but this might introduce inconsistency with existing ADRs which don't have it. But the skill is explicit that this field is important for the judge. I'll add it to the new ADR (and it's honest). I won't retro-add to existing ADRs.

Actually, let me reconsider. The existing ADRs don't have Author-model. Adding it only to my new ADR is fine and correct — it's a new document. I'll add `- Author-model: qwen-code` right after Owner, or as a standalone line. Let me use the format the parser recognizes. The skill lists:
- `- Модель-автор: claude-opus-4`
- `- Author-model: human`

I'll use `- Author-model: qwen-code`.

Now let me write the ADR content. It should be thorough but focused (one decision). The decision is the recurring model. Let me structure:

# ADR-008. Рекуррентные C2B-списания: согласие плательщика как сущность первого класса с локальным enforcement лимитов

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур)
- Author-model: qwen-code
- Related: ADR-001, ADR-002, ADR-003, ADR-004, ADR-006, AD-003, AD-009

## Context
- Бизнес-драйвер: ТСП (онлайн-кинотеатры, ЖКХ, связь) просят подписки/автоплатежи — рекуррентные списания по согласию плательщика. Сейчас каждый платёж = QR + действие клиента.
- Значимость: Critical, score 6 (триггеры: api_contract_change, consistency_model_change, data_contract_change, financial_impact, new_component, new_datastore). Финансовое влияние высокое: деньги списываются без действия плательщика на каждую транзакцию — ошибка (двойное списание, списание без согласия, превышение лимита) = регуляторный и репутационный инцидент.
- Существующий ландшафт: шлюз уже имеет статусную машину платежа (ADR-002), outbox (ADR-001), адаптер ОПКЦ (ADR-003), идемпотентность (AD-003), зачисление из PAID (AD-005). Автоплатежи были в roadmap вне scope.
- Точный протокол НСПК для согласий/рекуррентных списаний — внешний вход [ТРЕБУЕТ ПРОВЕРКИ] (как и весь протокол участника).

## Decision
Ввести «согласие плательщика» (consent) как сущность первого класса со своей статусной машиной и локальным хранением в БД шлюза; рекуррентное списание — merchant-driven: ТСП инициирует каждый платёж через существующий `POST /v1/payments`, ссылаясь на `consentId`; шлюз валидирует согласие (активно, в лимитах, не истекло) и проводит платёж через ту же статусную машину и адаптер ОПКЦ, пропуская состояние `QR_ISSUED`. Enforcement лимитов и дедупликации периода — на стороне шлюза (не полагаясь только на НСПК).

(Далее — детали: consent state machine, fields, recurring payment path, periodKey, idempotency.)

## Alternatives Considered
| Вариант | Плюсы | Минусы | Почему отвергнут |
- Bank-driven scheduler (шлюз сам планирует списания)
- Consent как флаг на платеже (без сущности)
- Consent только в НСПК (шлюз pass-through)

## Consequences
Positive / Negative

## Reversibility
reversible / costly + expiry

## References

Let me write this carefully and completely. I'll aim for a complete but not bloated ADR.

Now the spine AD-009. The existing spine uses blocks with `- Status:` and `- Binds:` etc. Actually the spine format is:

```
## AD-009. ...
- Status: Proposed (ADR-008)
- **Binds**: ...
- **Prevents**: ...
- **Rule**: ...
```

Let me match the existing format exactly (they use `- Status:`, `- **Binds**:`, etc.).

AD-009 content:
```
## AD-009. Рекуррентное списание — только по активному согласию с локальным enforcement

- Status: Proposed (ADR-008)
- **Binds**: БД шлюза (состояние согласия), статусная машина, вход ТСП (`consentId`, `periodKey`), адаптер ОПКЦ.
- **Prevents**: списание без активного согласия; превышение лимитов согласия (сумма за списание/период); двойное списание за один период подписки; рекуррентное списание через путь `QR_ISSUED`.
- **Rule**: Рекуррентный платёж создаётся только при активном согласии (`ACTIVE`) и `amount ≤ maxAmountPerDebit` и не превышены лимиты периода; уникальность по `consentId + periodKey` (повтор → идемпотентно); переход в `PAID` без `QR_ISSUED`. Fitness: тест «неактивное/истёкшее согласие → отказ», «повтор periodKey → идемпотентно», «сумма > лимита → отказ».
```

This passes the spine_lint checks (non-empty Binds/Prevents/Rule, unique ID, no TODO).

Now the openapi changes. Current openapi/tsp-api.yaml is minimal (only createPayment, getPayment). The tsp-api.md is much richer than the yaml. Interesting — the yaml is a subset. I should extend the yaml to include the consent + recurring endpoints, matching the richness needed. But I should be careful: the yaml is the machine-readable contract. The tsp-api.md is the prose contract. There's a slight drift between them already (the yaml is minimal). For my change, I'll add to the yaml:
- `info.version: 0.2.0` (bump)
- New path `/v1/consents` POST (createConsent)
- New path `/v1/consents/{consentId}` GET (getConsent)
- New path `/v1/consents/{consentId}/cancel` POST (cancelConsent)
- Extend PaymentRequest with optional `paymentType` (default `one_time`), `consentId`, `periodKey`
- Extend Payment with `paymentType`, `consentId`
- Add ConsentRequest, Consent, ConsentStatus schemas
- Add Idempotency-Key header to new POST endpoints (consistency with AD-003)

Note: the existing yaml's PaymentRequest has `required: [amount, merchantOrderId]` and properties amount, merchantOrderId. For recurring, `amount` is still required (each debit has an amount), `consentId` required when paymentType=recurring. I'll make paymentType optional with default one_time, consentId optional, periodKey optional (required only for recurring). To keep it simple and non-breaking: add these as optional properties; the semantic constraint "consentId required when recurring" goes in the prose contract and can be a conditional. Actually, for OpenAPI, I can use oneOf/discriminator, but that's over-engineering for a draft. I'll keep additive optional fields and document the conditional requirement in prose.

Let me also think about the `status` enum in Payment schema. For recurring payments, the status machine skips QR_ISSUED but the enum already includes all needed states. No change needed to enum.

Now let me write the openapi yaml. I'll rewrite the whole file with additive changes (it's small enough).

Actually, I need to preserve the existing content exactly and only add. Let me carefully edit.

Let me now also think about the tsp-api.md additions:
- §2 Idempotency: add note about `periodKey` for recurring dedup.
- §3.2 Create payment: add recurring fields (paymentType, consentId, periodKey), note that recurring skips QR.
- New §3.6 Consent creation, §3.7 Consent status, §3.8 Consent cancel, §3.9 Recurring payment (or fold recurring payment into 3.2).
- §5 Webhooks: add `consent.*` events? Consent activation/revocation webhooks to ТСП.
- §6 Versioning: note that consent endpoints are additive, version 0.2.

Actually let me keep tsp-api.md additions focused: add §3.6-3.8 for consents, extend §3.2 with recurring, add webhook events, update versioning.

For opkc-adapter.md:
- Add to §3 sync operations table: `registerConsent`, `getConsentStatus`, `cancelConsent`, `initiateRecurringDebit` (or note recurring uses a new operation).
- Add to §4 events: `consent.activated`, `consent.revoked`, `consent.expired`.
- Mark all as [ТРЕБУЕТ ПРОВЕРКИ] since НСПК consent protocol is external.
- Note the idempotency (§5) applies to consent operations by `reference`.

For nfr.md: add §7 "Рекуррентные списания (подписки СБП)" with a table.

For solutioning.md: 
- §1 roadmap: remove автоплатежи from "вне scope" — actually change "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." to "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты. Автоплатежи/подписки — выведены из roadmap в scope данным изменением (ADR-008)."
- Add a new section "## 11. Изменение: рекуррентные C2B-списания (подписки СБП)" with: context, consent model, state machine, flow, acceptance criteria, rollback, gaps, open questions, human decision points.

Actually, wait — solutioning.md already has §7 (гейты/приёмка) and §8 (план отката) and §9 (gaps) and §10 (open questions). Adding a full §11 is a bit redundant but the cleanest is to add the recurring-specific content as §11. Alternatively, I can add the recurring acceptance criteria and rollback directly within §11. Let me do §11.

Let me also update §9 gaps table and §10 open questions to include recurring-specific items. Actually to keep it clean, I'll put recurring-specific gaps/open questions inside §11, and just add a pointer. But the existing structure has a single gaps table and single open-questions list. Adding rows to §9 and §10 is more consistent. Let me:
- §9 gaps table: add rows for "Протокол НСПК для согласий/рекуррентных списаний", "Политика лимитов/AML для подписок".
- §10 open questions: add recurring questions.

Hmm, but I also want the recurring design to be self-contained. Let me add §11 with the full recurring design including its own acceptance criteria and rollback, and add pointers in §1, §9, §10. This is the most reviewable.

Let me now write everything. I'll start with the ADR-008 (new file), then edits.

Let me write ADR-008 now.

Actually, I realize I should double-check one thing about the consent model and whether it should reuse the payment machine or be a new "debit" machine. Let me settle on a clean design:

**Consent** entity:
- States: `PENDING` (created, awaiting payer approval in НСПК) → `ACTIVE` → `CANCELLED` (by ТСП or payer) | `EXPIRED` (endDate reached) | `REVOKED` (AML/ИБ/regulatory) | `FAILED` (НСПК rejected registration).
- Fields: consentId, tspId, payerRef (opaque token, minimal ПДн — only what НСПК requires), merchantOrderId, maxAmountPerDebit, maxTotalPerPeriod, period (day/week/month), startDate, endDate, status, revokedReason, limits...

**Recurring debit**:
- Reuses Payment entity with `paymentType=recurring`, `consentId`, `periodKey`.
- State machine: `CREATED → PAID → CREDITED → COMPLETED` (skip QR_ISSUED; no QR generated). Terminal: FAILED (НСПК rejected / consent invalid), and the existing REFUNDED via saga. EXPIRED doesn't apply to recurring debits (they're immediate). Actually a recurring debit could be rejected immediately, not "expire".
- Idempotency: `Idempotency-Key` (per-request) + `consentId + periodKey` (business-level dedup for the billing cycle). The шлюз stores `(consentId, periodKey) → paymentId` mapping to guarantee no double-debit for the same billing period even across different Idempotency-Keys (e.g., ТСП retries with a new key after losing the old one).

This periodKey dedup is a critical design point — it's the "subscription period dedup" that prevents double-charging a subscriber in the same billing cycle. This is a genuinely important invariant.

OK. Let me write the ADR now. I'll keep it tight.

Let me write all the files now. I'll begin with the ADR.

For the Date, today is 2026-09-28.

Let me write ADR-008.
Маршрут подтверждён: **Critical (score 6)**. Приступаю к созданию пакета. Начну с нового ADR-008 (принятый способ фиксации решения).

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/ARCHITECTURE-SPINE.md", old_string="## AD-008. Стратегия реализации — гибрид [ADOPTED]\n\n- Status: Adopted (A3 от 2026-08-15, ADR-007 Accepted)\n- **Binds**: ADR-007, ядро шл, new_string="## AD-008. Стратегия реализации — гибрид [ADOPTED]\n\n- Status: Adopted (A3 от 2026-08-15, ADR-007 Accepted)\n- **Binds**: ADR-007, ядро шл)`

Now add AD-009 to ARCHITECTURE-SPINE.md. I need to add it after AD-008 and before the "Deferred" section.
Добавляю инвариант AD-009 в spine (принятый способ фиксации инвариантов).

  `write_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/openapi/tsp-api.yaml", content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\npaths:\n  /v1/payments:\n    post:\n      operationId: createPayment\)`

Now update openapi/tsp-api.yaml. I'll rewrite the whole file with additive changes. Let me carefully construct it, preserving existing content and adding consent endpoints + recurring fields.

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

I'll write a new version. Let me write the full file with:
- version 0.2.0
- Add paymentType, consentId, periodKey to PaymentRequest (optional)
- Add paymentType, consentId to Payment
- Add consent endpoints
- Add ConsentRequest, Consent, ConsentStatus schemas

For the consent endpoints, Idempotency-Key required on POST (consistency).

Let me write it. I'll preserve the compact style used in the existing file ({type: string} inline).

New openapi yaml content:

```yaml
openapi: 3.0.3
info:
  title: СБП-шлюз — API ТСП
  version: 0.2.0
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
  /v1/consents:
    post:
      operationId: createConsent
      parameters:
        - in: header
          name: Idempotency-Key
          required: true
          schema: {type: string}
      requestBody:
        required: true
        content:
          application/json:
            schema: {$ref: '#/components/schemas/ConsentRequest'}
      responses:
        '201':
          description: Согласие создано (ожидает подтверждения плательщиком)
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Consent'}
  /v1/consents/{consentId}:
    get:
      operationId: getConsent
      parameters:
        - {in: path, name: consentId, required: true, schema: {type: string}}
      responses:
        '200':
          description: Статус согласия
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Consent'}
  /v1/consents/{consentId}/cancel:
    post:
      operationId: cancelConsent
      parameters:
        - in: path
          name: consentId
          required: true
          schema: {type: string}
        - in: header
          name: Idempotency-Key
          required: true
          schema: {type: string}
      responses:
        '200':
          description: Согласие отозвано
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Consent'}
components:
  schemas:
    PaymentRequest:
      type: object
      required: [amount, merchantOrderId]
      properties:
        amount: {type: integer, description: Сумма в копейках}
        merchantOrderId: {type: string}
        paymentType:
          type: string
          enum: [one_time, recurring]
          default: one_time
          description: one_time — разовый QR/ссылка; recurring — рекуррентное списание по согласию
        consentId: {type: string, description: Обязателен при paymentType=recurring}
        periodKey: {type: string, description: Ключ биллингового периода (обязателен при paymentType=recurring) для дедупликации}
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
          enum: [one_time, recurring]
        consentId: {type: string}
    ConsentRequest:
      type: object
      required: [tspId, merchantOrderId, maxAmountPerDebit, period, endDate]
      properties:
        tspId: {type: string}
        merchantOrderId: {type: string}
        payerRef: {type: string, description: Непрозрачная ссылка на плательщика (минимально необходимые ПДн для НСПК)}
        maxAmountPerDebit: {type: integer, description: Максимальная сумма одного списания, копейки}
        maxTotalPerPeriod: {type: integer, description: Максимальная сумма за период, копейки}
        period: {type: string, enum: [day, week, month], description: Периодичность лимита}
        startDate: {type: string, format: date}
        endDate: {type: string, format: date, description: Срок действия согласия}
        webhookUrl: {type: string}
    Consent:
      type: object
      required: [consentId, tspId, status]
      properties:
        consentId: {type: string}
        tspId: {type: string}
        merchantOrderId: {type: string}
        maxAmountPerDebit: {type: integer}
        maxTotalPerPeriod: {type: integer}
        period: {type: string, enum: [day, week, month]}
        startDate: {type: string, format: date}
        endDate: {type: string, format: date}
        status:
          type: string
          enum: [PENDING, ACTIVE, CANCELLED, EXPIRED, REVOKED, FAILED]
```

This is additive and backward-compatible. version bump 0.1.0 → 0.2.0.

Let me write the full file.
Обновляю OpenAPI-контракт аддитивно (без ломающих изменений), бамп версии 0.1.0 → 0.2.0.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/tsp-api.md", old_string="- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)\n- Owner: solution-architect , new_string="- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.2 (аддитивное расширение: рекуррентные списания и согласия; до A1 фиксируетс)`

Now update docs/contracts/tsp-api.md. I need to:
1. Update the version note in header (0.1 → 0.2).
2. Extend §3.2 (create payment) with recurring fields.
3. Add §3.6-3.8 consent endpoints.
4. Add consent webhook events in §5.
5. Update §6 versioning note.

Let me read the exact text around those sections to do precise edits. I already have the full content from earlier. Let me make the edits.

First, header update. Current header:
```
- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), AD-003 (spine)
```

Change to:
```
- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (аддитивное расширение: рекуррентные списания, согласия; до A1 фиксируется v1.0-draft)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-002 (идемпотентность), ADR-004 (нотификации), ADR-008 (согласия/рекуррентные), AD-003, AD-009 (spine)
```

Then §3.2 — I need to add recurring fields to the request and a note. The current §3.2 request:
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

I'll add a note after the rules about recurring, or add fields. Actually, better to add a separate subsection §3.2.1 "Рекуррентное списание (подписка)" after §3.2 rules, rather than pollute the main one-time flow. But the task says "Изменения контрактов без поломки существующих потребителей". The cleanest is to add a dedicated subsection. Let me add §3.6 for consents and a note in §3.2 about the additional optional fields.

Let me look at the §3.2 "Правила" paragraph and add recurring info there, and then add §3.6/3.7/3.8 after §3.5.

Actually, I'll do:
1. Header edit.
2. In §3.2, after the "Правила:" paragraph, add a note about recurring fields.
3. After §3.5 (статус возврата), add §3.6 (создание согласия), §3.7 (статус согласия), §3.8 (отзыв согласия).
4. §5 webhooks: add consent events.
5. §6 versioning: update note.

Let me do the header edit first.

Actually, let me re-read the exact current text for the sections I'll edit to ensure precise matches. I have the full content from the earlier read. Let me use precise old_string values.

Header edit:
Расширяю prose-контракт `tsp-api.md` (заголовок, рекуррентные поля, секции согласий, вебхуки, версионирование).

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/tsp-api.md", old_string="Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (AD, new_string="Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (AD)`

Now let me update §3.2 to add recurring fields note. The "Правила" paragraph is:

```
Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (ADR-002). Максимальная сумма — по лимитам НСПК [ТРЕБУЕТ ПРОВЕРКИ].
```

I'll add a subsection after it. Actually let me add after the §3.2 response and rules, a "### 3.2.1 Рекуррентное списание (подписка)". But cleaner to add to the §3.2 request and rules. Let me add after the "Правила:" line a new paragraph about recurring.

Let me target the §3.2 rules paragraph precisely and append a recurring block.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/tsp-api.md", old_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n, new_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n)`

Now add consent endpoints §3.6-3.8 after §3.5 (статус возврата). Let me find the §3.5 text and add after it.

§3.5 is:
```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`

## 4. Ошибки (RFC 9457, Problem Details)
```

I'll insert the consent sections between §3.5 and §4.
Добавляю секции согласий (§3.6–3.8) и коды ошибок.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/tsp-api.md", old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`

Now add error codes to §4 and consent webhooks to §5, and update §6 versioning.

The §4 canonical codes list is:
```
Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.
```

I'll add `CONSENT_INACTIVE` (403), `CONSENT_LIMIT_EXCEEDED` (422), `CONSENT_NOT_FOUND` (404), `PERIOD_KEY_CONFLICT` (409).

Let me edit.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/tsp-api.md", old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`

Now add consent webhook events to §5. The §5 events list is:
```
События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
```

I'll add:
- `consent.activated` — согласие подтверждено плательщиком
- `consent.revoked` — согласие отозвано (плательщик/ТСП/AML)
- `consent.expired` — истёк срок действия

And update §6 versioning note. Let me do the webhooks edit.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/tsp-api.md", new_string="## 6. Версионирование и совместимость\n\n- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6, old_string="## 6. Версионирование и совместимость\n\n- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6)`

Now update §6 versioning note. The §6 is:
```
## 6. Версионирование и совместимость

- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.
- Добавление опциональных полей — обратно совместимо, не требует новой версии.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.
```

I'll add a note about the 0.2 additive change. Let me edit.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/opkc-adapter.md", new_string="| `createPaymentLink` | создание QR/ссылки | `reference` (= `paymentId` ядра), `amount` (копейки), `currency`, `qrType`, `ttlSeconds?`, `pu, old_string="| `createPaymentLink` | создание QR/ссылки | `reference` (= `paymentId` ядра), `amount` (копейки), `currency`, `qrType`, `ttlSeconds?`, `pu)`

Now update opkc-adapter.md to add consent operations. I need to add:
1. §3 sync operations table: add rows for `registerConsent`, `getConsentStatus`, `cancelConsent`, `initiateRecurringDebit`.
2. §4 events table: add `consent.activated`, `consent.revoked`, `consent.expired`.
3. §9 open questions: add consent-related question.

Let me look at the current §3 table (already read earlier). The table ends with `getReconciliationReport`. I'll add rows after `getRefundStatus` (before `getReconciliationReport`), and after `getReconciliationReport`.

Actually let me add consent rows after `getRefundStatus` row and `initiateRecurringDebit` after `createPaymentLink` (since it's a payment operation). Let me do a clean edit.

The §3 table:
```
| Метод | Направление смысла | Ключевые поля запроса | Ответ | Таймаут (p99.9) |
|---|---|---|---|---|
| `registerTsp` | ... | ... | ... | 5 c |
| `createPaymentLink` | ... | ... | ... | 3 c |
| `getPaymentStatus` | ... | ... | ... | 3 c |
| `cancelPaymentLink` | ... | ... | ... | 3 c |
| `createRefund` | ... | ... | ... | 5 c |
| `getRefundStatus` | ... | ... | ... | 3 c |
| `getReconciliationReport` | ... | ... | ... | 10 c |
```

I'll add `initiateRecurringDebit` after `createPaymentLink`, and consent operations after `getRefundStatus` (before `getReconciliationReport`).

Let me do a targeted edit. I'll replace the row for `getRefundStatus` and `getReconciliationReport` block, inserting consent rows between them, and add `initiateRecurringDebit` after `createPaymentLink`.

Actually, cleaner to do two edits:
1. Insert `initiateRecurringDebit` after `createPaymentLink` row.
2. Insert consent rows after `getRefundStatus` row (before `getReconciliationReport`).

Let me get the exact text. From my earlier read:

```
| `createPaymentLink` | создание QR/ссылки | `reference` (= `paymentId` ядра), `amount` (копейки), `currency`, `qrType`, `ttlSeconds?`, `purpose?`, `redirectUrl?` | `qrId`, `qrUrl`, `expiresAt` | 3 c |
| `getPaymentStatus` | запрос статуса по `qrId` (сверка/опрос) | `qrId` | статус ОПКЦ: `PAID` / `PENDING` / `REJECTED` / `EXPIRED` / `UNKNOWN`, `paidAmount?`, `paidAt?` | 3 c |
```

and

```
| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |
| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |
```

Let me do the edits.

Edit 1: insert initiateRecurringDebit after createPaymentLink row.
Обновляю контракт адаптера ОПКЦ — операции согласий и рекуррентного списания.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/opkc-adapter.md", new_string="| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |\n| `registerConsent` | регистрация, old_string="| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |\n| `getReconciliationReport` | вып)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/opkc-adapter.md", new_string="| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |\n| `refund.rejected` | возв, old_string="| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |\n| `refund.rejected` | возв)`

Now add consent events to §4 (events table). Current events table:

```
| Тип события | Смысл | Ключевые поля |
|---|---|---|
| `payment.paid` | платёж подтверждён ОПКЦ | `qrId`, `reference` (= `paymentId`), `amount`, `paidAt` |
| `payment.rejected` | платёж отклонён | `qrId`, `reference`, `reasonCode` (нормализованный), `reasonText` |
| `payment.expired` | ссылка истекла по TTL | `qrId`, `reference` |
| `tsp.registered` | ТСП активирован в ОПКЦ | `reference` (= `tspId` ядра) |
| `tsp.rejected` | ТСП отклонён ОПКЦ | `reference`, `reasonCode`, `reasonText` |
| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |
| `refund.rejected` | возврат отклонён | `refundRef`, `reasonCode`, `reasonText` |
| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |
```

I'll add consent events after `refund.rejected` (before `transport.unavailable`).

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/opkc-adapter.md", new_string="## 5. Идемпотентность и ссылки\n\n- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`/`consentId`) в каждый мутирующий вызов.\, old_string="## 5. Идемпотентность и ссылки\n\n- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.\n- **Адаптер)`

Now add an idempotency note for consent operations in §5 and an open question in §9. Also update the §5 idempotency paragraph to mention consent `reference`. Actually §5 already covers the general principle: "Ядро передаёт `reference` ... в каждый мутирующий вызов." and "Адаптер обязан обеспечить идемпотентность". This already generalizes to consent. I can add a brief note that `consentRef` follows the same idempotency discipline. Let me add a small line to §5.

Actually, the §5 text is:
```
## 5. Идемпотентность и ссылки

- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.
- **Адаптер обязан обеспечить идемпотентность**: повторный вызов с тем же `reference` возвращает тот же результат и **не создаёт дубль в ОПКЦ**. Если протокол НСПК не даёт идемпотентности «из коробки» — вендор реализует маппинг `reference → операция ОПКЦ` у себя. **Это обязательное требование RFP** (без него ретраи ядра дают двойные QR/возвраты).
- Повторная доставка события с тем же `eventId` — игнорируется ядром (ADR-003).
```

I'll update the first bullet to include consentId, and note that recurring debits also carry `periodKey` (dedup). Let me edit.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/contracts/opkc-adapter.md", new_string="1. Нужен ли синхронный `getReconciliationReport` или сверку делать событиями/файлами — решить с вендором на RFP (формат выписки может дикто, old_string="1. Нужен ли синхронный `getReconciliationReport` или сверку делать событиями/файлами — решить с вендором на RFP (формат выписки может дикто)`

Now add an open question to §9 of opkc-adapter.md. The §9 is:
```
## 9. Открытые вопросы

1. Нужен ли синхронный `getReconciliationReport` или сверку делать событиями/файлами — решить с вендором на RFP (формат выписки может диктовать НСПК).
2. Нормализованные `reasonCode` — расширяемый справочник, финализируется после получения протокола НСПК.
3. Поведение ядра при `transport.unavailable` (приём QR в очередь vs отклонение) — политика, утверждается на A2.
```

I'll add a question about consent/recurring protocol being external.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/nfr.md", new_string="| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |\n\n## 7. Рекуррентные списания (подписки СБП)\n\nЦелевые значения —, old_string="| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |\n\n## Зависимости (внешние входы для NFR)")`

Now add NFR section §7 to docs/nfr.md. Let me append after §6 (Наблюдаемость) and before the "Зависимости" section.

Actually, the nfr.md ends with:
```
## 6. Наблюдаемость
... table ...

## Зависимости (внешние входы для NFR)
```

I'll insert a new §7 "Рекуррентные списания (подписки СБП)" between §6 and "Зависимости". Let me find the exact text.

The §6 table ends with:
```
| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |

## Зависимости (внешние входы для NFR)
```

Let me insert before "## Зависимости".

New NFR section content:

## 7. Рекуррентные списания (подписки СБП)

| Метрика | Цель | Метод проверки |
|---|---|---|
| Создание согласия (API ТСП) | p95 < 500 мс | Нагрузочный тест |
| Валидация согласия + создание рекуррентного списания | p95 < 500 мс (без учёта НСПК) | Нагрузочный тест, APM |
| Списанный без активного согласия | 0 (hard invariant AD-009) | Fitness-тест, аудит |
| Превышение лимита согласия | 0 (отказ до вызова НСПК) | Fitness-тест |
| Двойное списание за один период (consentId+periodKey) | 0 | Тест на повтор/новый Idempotency-Key |
| Двойное списание при ретрае НСПК | 0 (идемпотентность) | Тест повторной доставки |
| Throughput рекуррентных списаний | 200 TPS sustained; пик (день списаний подписок) до 500 TPS, burst 1000 TPS/мин | Нагрузочный тест |
| Сверка согласий с НСПК | ежечасная; расхождений по завершённым — 0 | Reconciliation-отчёт |
| Доставка события отзыва согласия до блокировки новых списаний | p95 < 5 с от события НСПК | Метрика лага очереди |
| AML/velocity-проверка рекуррентного канала | 100 % списаний через антифрод-контур | Тест-кейсы |

Note about burst: subscriptions cluster at month-start. Add a note.

Let me write it.
Добавляю раздел NFR для рекуррентных списаний.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/solutioning.md", new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Рекуррентные C2B-, old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop)`

Now update solutioning.md. I need to:
1. Update §1 roadmap (remove автоплатежи from "вне scope").
2. Add a new section §11 for the recurring change (design, state machine, acceptance criteria, rollback, gaps, open questions, human decision points).
3. Update §9 gaps table and §10 open questions with pointers (or add recurring-specific rows).

Let me do these edits.

First, §1 roadmap:
```
Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи.
```

Change to:
```
Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Рекуррентные C2B-списания (подписки/автоплатежи по согласию плательщика) — выведены из roadmap в scope изменением ADR-008 (см. §11). Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты.
```

Let me edit §1.

Actually, let me read the exact current §1 line to be safe. From my earlier read:

```
Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи.
```

Yes. Let me edit.
Обновляю `solutioning.md` — вывожу автоплатежи из roadmap в scope и добавляю секцию изменений.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/solutioning.md", new_string="| Категория объекта КИИ, состав мер ФСТЭК | ИБ/КИИ банка | ИБ |\n| Выбор конкретного вендора транспорта ОПКЦ | RFP по критериям ADR-007 (се, old_string="| Категория объекта КИИ, состав мер ФСТЭК | ИБ/КИИ банка | ИБ |\n| Выбор конкретного вендора транспорта ОПКЦ | RFP по критериям ADR-007 (се)`

Now add §11 at the end of solutioning.md. The file ends with §10 open questions. Let me read the exact end of the file to append correctly.

From my earlier read, §10 is:
```
## 10. Открытые вопросы

1. Объём первой волны: только C2B-приём или сразу C2C/выплаты? (влияет на состав адаптеров, но не на ядро).
2. Требования бизнеса к комиссиям и тарифам ТСП (влияет на модель отчётности).
3. Лимиты/пороги для AML-интеграции.
4. Доступность АБС в ночные окна (влияет на SLA зачисления).
```

I'll append §11 after this. Also, I should add recurring rows to §9 gaps table and §10 open questions. Let me do it in a combined way: add §11 with its own "gaps" and "open questions / human decisions" subsections, AND add rows to §9 and §10. Actually to keep it clean and avoid duplication, I'll:
- Add 2 rows to §9 gaps table (for НСПК consent protocol + AML policy).
- Add 2 items to §10 open questions.
- Add full §11 with the change design, acceptance criteria, rollback.

Let me first read the exact §9 gaps table and §10 to edit precisely. I have them from the earlier full read. §9:

```
## 9. Gaps и внешние входы

| Gap | Что закроет | Владелец |
|---|---|---|
| Точный протокол НСПК (поля, тайминги, TLS-профили) | Документация НСПК по договору (Портал поддержки) | Проектный офис / НСПК |
| Регламенты НСПК (таймауты, сроки уведомлений, доступность) | Документация НСПК, правила ОПКЦ СБП | Проектный офис |
| Номер/редакция Положения ЦБ о защите информации при переводах | ИБ/комплаенс банка | ИБ |
| Контракт АБС на зачисление/списание (идемпотентность, SLA) | Интервью с владельцем АБС | Архитектор + АБС |
| Категория объекта КИИ, состав мер ФСТЭК | ИБ/КИИ банка | ИБ |
| Выбор конкретного вендора транспорта ОПКЦ | RFP по критериям ADR-007 (сертификаты ФСТЭК, тестовый контур, SLA, референсы) | Проектный офис / закупки |
```

I'll add two rows. Let me edit the table to add rows.

Actually, I'll do it efficiently: add the recurring gaps to §9 table and recurring open questions to §10, then append §11.

Let me add rows to §9.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/solutioning.md", new_string="1. Объём первой волны: только C2B-приём или сразу C2C/выплаты? (влияет на состав адаптеров, но не на ядро).\n2. Требования бизнеса к комисс, old_string="1. Объём первой волны: только C2B-приём или сразу C2C/выплаты? (влияет на состав адаптеров, но не на ядро).\n2. Требования бизнеса к комисс)`

Now append §11 after §10. Let me read the end of the file to get the exact §10 ending.

§10 currently:
```
## 10. Открытые вопросы

1. Объём первой волны: только C2B-приём или сразу C2C/выплаты? (влияет на состав адаптеров, но не на ядро).
2. Требования бизнеса к комиссиям и тарифам ТСП (влияет на модель отчётности).
3. Лимиты/пороги для AML-интеграции.
4. Доступность АБС в ночные окна (влияет на SLA зачисления).
```

I'll append §11 after item 4. Let me use the edit to add after item 4.

I'll add the recurring open questions to §10 AND append §11. Actually, let me just append §11 after §10, and include the recurring-specific "человеческие решения" inside §11. To avoid duplicating §10, I'll add one pointer item to §10 and put the full human-decision list in §11.

Actually simpler: append §11 directly after item 4 of §10. §11 will contain its own "что остаётся на человека" subsection. Let me do that.

Let me construct §11 content:

## 11. Изменение: рекуррентные C2B-списания (подписки СБП)

### 11.1 Маршрут и значимость
Critical, score 6 (значимость: api_contract_change, consistency_model_change, data_contract_change, financial_impact, new_component, new_datastore). Полный Solutioning: ADR-008 + spine AD-009 + NFR §7 + контракты. Человеческая точка A3 — обязательна до реализации.

### 11.2 Что меняется в архитектуре
- Новый доменный объект: согласие плательщика (consent) со своей статусной машиной.
- Новый логический компонент: менеджер согласий (внутри ядра, не отдельный сервис).
- Расширение статусной машины платежа: рекуррентный платёж идёт CREATED→PAID→CREDITED→COMPLETED без QR_ISSUED.
- Расширение адаптера ОПКЦ: операции registerConsent/getConsentStatus/cancelConsent/initiateRecurringDebit + события consent.*/recurring_debit.*.
- Не меняется: AD-001 (изоляция), AD-002 (outbox/источник истины), AD-003 (идемпотентность), AD-004 (адаптер ОПКЦ), AD-005 (зачисление из PAID), AD-006/007 (trust/НПС), AD-008 (гибрид). Все существующие разовые потоки нетронуты.

### 11.3 Статусная машина согласия
PENDING → ACTIVE → CANCELLED | EXPIRED | REVOKED | FAILED

### 11.4 Поток (рекуррентное списание)
sequence... (optional). I'll keep a compact textual flow.

### 11.5 Критерии приёмки (EARS)
### 11.6 План отката
### 11.7 Что остаётся на решение человека-архитектора

Let me write it compactly but completely. This is the acceptance criteria + rollback + human decisions, which are the key deliverables (items 6 and 7).

Let me write it.

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="  - name: abs-credit-only-from-paid\n    type: must_contain\n    glob: \"docs/adr/ADR-005-integraciya-s-abs-zachislenie-po-podtverzhdyonnom, old_string="  - name: abs-credit-only-from-paid\n    type: must_contain\n    glob: \"docs/adr/ADR-005-integraciya-s-abs-zachislenie-po-podtverzhdyonnom)`

Now update CONSTRAINTS.yaml to add a fitness rule for the new invariant (mirroring the existing `abs-credit-only-from-paid` rule). This is the "accepted way" per the fitness-functions skill — invariants should have machine checks.

Let me add a rule:
```yaml
  - name: recurring-credit-requires-active-consent
    type: must_contain
    glob: "docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md"
    pattern: 'только при согласии в `ACTIVE`'
    severity: error
```

Wait, the pattern needs to match the ADR content. The ADR says "рекуррентный платёж создаётся только при согласии в `ACTIVE`". Let me use a pattern that's in the ADR. Actually, the spine AD-009 Rule says "создаётся только при согласии в `ACTIVE`". The ADR Decision #3 says "рекуррентный платёж создаётся только при согласии в `ACTIVE`". Let me use pattern 'только при согласии в `ACTIVE`'.

Actually, let me match the existing rule style. Existing `abs-credit-only-from-paid` points to the ADR file and checks for 'только из состояния `PAID`'. I'll add:
```yaml
  - name: recurring-credit-requires-active-consent
    type: must_contain
    glob: "docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md"
    pattern: 'только при согласии в `ACTIVE`'
    severity: error
```

Let me verify the exact text in ADR-008. In the Decision #3 I wrote: "рекуррентный платёж создаётся только при согласии в `ACTIVE`, `amount ≤ maxAmountPerDebit`, не превышен лимит периода, `now < endDate`". So the pattern 'только при согласии в `ACTIVE`' will match.

Let me add this rule to CONSTRAINTS.yaml.

Let me read the exact current CONSTRAINTS.yaml content to do the edit. I already have it from earlier read. The rules list ends with `spine-lints-clean`. Let me add after `abs-credit-only-from-paid` rule or at the end. I'll add after `abs-credit-only-from-paid` for logical grouping.

Actually, let me add it right after the `abs-credit-only-from-paid` rule.
Добавляю fitness-правило для нового инварианта (принятый механизм закрепления AD-*).

  `tool_call(arguments={"path": "ARCHITECTURE-SPINE.md"}, name="mcp__spine__spine_lint")`
  `tool_call(arguments={"path": "openapi/tsp-api.yaml", "cwd": "<HARNESS>/runs-clean/cells/wd33eb5/ws, name="mcp__spine__openapi_lint")`
  `tool_call(arguments={"path": "<HARNESS>/runs-clean/cells/wd33eb5/ws", "constraints": "<HOME>/, name="mcp__spine__fitness_check")`

Now let me verify with the Spine tools. Let me run:
1. spine_lint on ARCHITECTURE-SPINE.md
2. openapi_lint on openapi/tsp-api.yaml
3. contract_diff — but I don't have the old version saved. I overwrote the yaml. I need the old version to diff. I can get it from git (git show HEAD:openapi/tsp-api.yaml). Let me do a contract_diff using git to produce the old version, or just verify via openapi_lint and note the additive nature manually.

Actually, the contract_diff tool takes old and new file paths. I overwrote the file, so old is in git. Let me get the old version via git and save it to a temp file, then run contract_diff. Alternatively, I can just run openapi_lint (which validates versioning) and manually confirm backward compatibility (which I already documented in §6).

Let me run spine_lint and openapi_lint and fitness_check in parallel.

For contract_diff, let me extract old yaml from git to a temp file. Let me do that with a shell command, then run contract_diff.

Actually, let me first run the three deterministic checks in parallel (spine_lint, openapi_lint, fitness_check), then handle contract_diff separately.

Let me run these via tool_call.
Проверяю пакет инструментами Spine: линтер спайна, линт OpenAPI, fitness-контроль.

  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wd33eb5/ws && git show HEAD:openapi/tsp-api.yam, description="Извлечь старую версию контракта из git для diff")`

All three checks pass:
- spine_lint: passed (0 issues)
- openapi_lint: PASS (0 findings)
- fitness_check: passed (8 rules, 0 violations, no ослаблений)

Now let me do the contract_diff to formally verify backward compatibility. I need the old version. Let me get it from git.

git show HEAD:openapi/tsp-api.yaml

Let me extract the old version to a temp file and run contract_diff.
Спайн, OpenAPI и fitness — все PASS. Проверю обратную совместимость контракта через `contract_diff` (старая версия — из git).

  `tool_call(arguments={"old": "<TMP>.yaml", "new": "<HARNESS>/runs-clean/cells/wd33eb5/ws, name="mcp__spine__contract_diff")`
  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wd33eb5/ws && git status --short && echo \"---\, description="Проверить статус и сводку изменений")`

contract_diff: 0 breaking changes, 3 non-breaking (new paths). It only reported the new paths (CD-005), not the schema additions — that's because contract_diff's OpenAPI detector focuses on paths/breaking changes. The schema additions (optional fields to PaymentRequest/Payment, new schemas Consent/ConsentRequest) are non-breaking. The version bump 0.1.0 → 0.2.0 is a minor bump, which is fine for additive changes (no CD-007 warning about breaking diff without major bump, since there are no breaking changes).

Wait, the contract_diff only flagged the 3 new paths, not the version bump or schema additions. Let me note that the schema additions are additive (optional properties, new schemas) and don't remove/rename anything. The `status` enum in Payment is unchanged. So backward compatible confirmed.

Actually, one thing to double-check: I changed `info.version` from 0.1.0 to 0.2.0. contract_diff didn't flag anything about version. Good.

Also, I added `paymentType` with `default: one_time` to PaymentRequest — that's additive (new optional property). I added `paymentType` and `consentId` to Payment (new optional properties, not in `required`). All non-breaking.

Now, there's one subtle thing: I should double check the git status to make sure I haven't left /tmp files in the repo or done anything unexpected. Also clean up /tmp file? Not necessary — it's in /tmp, outside repo.

Let me also verify the git status to see the full list of changed files, and make sure I haven't accidentally modified anything unexpected (like .qwen/settings.json which was already modified per the git snapshot).

Let me run git status and git diff --stat.
Все проверки зелёные. Смотрю итоговое состояние репозитория.

  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wd33eb5/ws && head -c 400 .arch-handoff/mcp-cal, description="Проверить природу mcp-calls.jsonl и diff settings.json")`

I notice two things:
1. `.qwen/settings.json` was modified (it was already modified before I started — the git snapshot said "M .qwen/settings.json"). So that's pre-existing user-owned change, not mine. I should NOT touch it.
2. `.arch-handoff/mcp-calls.jsonl` appeared as untracked — this is likely created by the Spine MCP server recording my tool calls (mcp-calls.jsonl). This is an artifact of my tool usage. It's untracked. I should probably leave it or note it. It's not something I intentionally created as part of the package. Actually it's a byproduct of the MCP server logging. Let me check — it's a new untracked file. This is likely the Spine MCP server's call log.

Let me verify the mcp-calls.jsonl is indeed the MCP call log (created by the spine tool) and not something I should include. It's untracked, so it won't be committed unless staged. It's a byproduct of running the spine tools. I should note it but not include it in my summary of "created files" as it's not part of the architectural package.

Actually, let me check its content briefly to understand it.

Actually, the key point: my changes are exactly:
- New: docs/adr/ADR-008-...md
- Modified: .arch-handoff/CONSTRAINTS.yaml, ARCHITECTURE-SPINE.md, docs/contracts/opkc-adapter.md, docs/contracts/tsp-api.md, docs/nfr.md, docs/solutioning.md, openapi/tsp-api.yaml

The `.qwen/settings.json` was already modified before I started (pre-existing, in the git snapshot). The `.arch-handoff/mcp-calls.jsonl` is a byproduct of the MCP server.

Let me verify .qwen/settings.json was pre-existing by checking git diff — actually the snapshot at conversation start already showed "M .qwen/settings.json". So it's user-owned, I leave it alone.

Let me quickly check what mcp-calls.jsonl is (just to be sure it's the MCP log, and to report honestly).

  `read_file(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisa, offset=44, limit=30)`

Confirmed:
1. `.arch-handoff/mcp-calls.jsonl` is the MCP server's call log (created by the spine MCP server as a byproduct of my tool invocations). This is not part of the architectural package — it's a runtime artifact. I should note it and probably leave it (it's untracked). I won't include it as a created file of the package. Actually, it's a byproduct; the user may want to know about it. I'll mention it briefly in the final summary as a runtime artifact, or better, since it's untracked noise from tool usage, I'll mention it's a byproduct. I won't delete it (it's the MCP server's own log, and deleting could be seen as tampering). Actually, it's reasonable to leave it — it's evidence of the control loop working (trust metric). I'll note it.

2. `.qwen/settings.json` was modified (`$version: 4` added) — this is a pre-existing user-owned change (it was "M" in the git snapshot at conversation start). The diff shows `+  "$version": 4` which is likely from the Qwen Code host itself, not me. I didn't touch it. I leave it alone.

Now, everything is done. Let me do a final review of my changes to ensure quality and completeness against the 7 deliverables:

1. ✅ Significance assessment → ADR-008 Context + §11.1 + significance_score (Critical, score 6)
2. ✅ Impact on invariants → spine AD-009 + §11.2 (what changes / what doesn't)
3. ✅ ADR with alternatives, consequences, reversibility → ADR-008
4. ✅ Contract changes without breaking consumers → openapi/tsp-api.yaml + tsp-api.md + opkc-adapter.md (verified non-breaking via contract_diff)
5. ✅ Measurable NFR → nfr.md §7
6. ✅ Acceptance criteria + rollback → §11.5 + §11.6
7. ✅ Human decisions → §11.7

Let me do a final read of the ADR-008 to make sure it's well-formed and the header is parseable. The header I wrote:
```
- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур)
- Author-model: qwen-code
- Related: ADR-001, ADR-002, ADR-003, ADR-004, ADR-006, AD-003, AD-009
```

This is parseable. Good.

Now, one thing I should verify: does the adr-authoring skill's `adr_registry` / the rubric judge need the ADR to be in a specific location? The repo uses `docs/adr/ADR-NNN-slug.md`. My new file is `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`. Consistent with existing naming. Good.

Also, I should consider whether the `.arch-handoff/adr/` directory needs a copy of ADR-008. Looking at the structure: `.arch-handoff/adr/` contains copies of ADR-001..007 (the handoff package). The `.arch-handoff/` is the handoff package for the BASE walking skeleton. Since my task is to prepare the package for A3 decision (not to hand off to coders yet), I should NOT add ADR-008 to `.arch-handoff/adr/` — that package is for the walking skeleton handoff which hasn't been updated for recurring yet. The task says "чтобы его можно было вынести на архитектурное решение и затем передать исполнителям" — the handoff comes after A3. So leaving .arch-handoff/adr/ untouched is correct.

Actually wait — let me reconsider. The `.arch-handoff/CONSTRAINTS.yaml` I did update (added the fitness rule). Is that consistent? The CONSTRAINTS.yaml is the "decision-stage" fitness rules. The MANIFEST.json lists "sources" which includes the ADRs. Hmm. But the .arch-handoff/ is described in README as "handoff-пакет кодовому харнессу (этап: walking skeleton)". 

Actually, let me reconsider whether updating CONSTRAINTS.yaml is right. The CONSTRAINTS.yaml currently has decision-stage rules (file_exists, must_contain). Adding my rule there is consistent with the existing pattern and the fitness-functions skill ("инвариант → fitness rule"). The fitness_check passed. This is fine — it's the "accepted way" to encode the invariant as a machine check. I'll keep it.

But should I also update MANIFEST.json sources or the .arch-handoff/ARCHITECTURE.md epic-context? No — those are for the walking-skeleton handoff, which is a separate downstream step after A3. My task is the A3 package. I'll leave those untouched. The CONSTRAINTS.yaml rule addition is defensible as "the invariant is now machine-checked" and doesn't preempt the handoff.

Actually, let me reconsider once more. There's a subtlety: the fitness_check I ran uses CONSTRAINTS.yaml and it passed, and it verified "ослаблений нет" (no weakening) vs the merge-base. Adding a NEW error rule is a strengthening, which is fine.

Everything is consistent. Let me now also double check: did I leave the <TMP>.yaml file? It's in /tmp, outside the repo. It won't be committed. Fine to leave (it's in /tmp and will be cleaned by OS). Actually, to be tidy, I could remove it, but it's harmless and in /tmp. I'll leave it.

Let me now write the final summary. I should be concise but cover the 7 deliverables, list created/modified files, and mention the verification results.

Actually, let me do a final sanity check on the ADR file to make sure it reads well and there are no issues (like the "Negative (регуляторные/операционные)" having a duplicate "### Negative" heading — I have two Negative sub-headings, one "### Negative" and one "### Negative (регуляторные/операционные)". That's slightly awkward. Let me check the ADR.

Actually, in my ADR-008 I wrote:
```
### Positive
...
### Negative
...
### Negative (регуляторные/операционные)
...
```

Having two "Negative" subsections is a bit unusual. The adr-authoring skill says "Positive и Negative (обе секции непустые)". Having a second "Negative (регуляторные/операционные)" heading is a bit non-standard but not wrong. However, to keep it clean and match the canonical format (one Positive, one Negative), I should merge them. Let me fix that — merge the regulatory negative into the main Negative section.

Let me read the ADR to see the exact text and fix.
Заметил в ADR-008 два подзаголовка Negative — приведу к канону (один Positive, один Negative).

  `edit(file_path="<HARNESS>/runs-clean/cells/wd33eb5/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisa, new_string="### Negative\n\n- Новый доменный объект и хранилище: жизненный цикл согласия, сверка согласий с НСПК (второй источник истины, как АБС — ADR, old_string="### Negative\n\n- Новый доменный объект и хранилище: жизненный цикл согласия, сверка согласий с НСПК (второй источник истины, как АБС — ADR)`
  `tool_call(arguments={"constraints": "<HARNESS>/runs-clean/cells/wd33eb5/ws/.arch-handoff/CONSTRAIN, name="mcp__spine__fitness_check")`

Now let me re-run the fitness_check quickly to make sure the ADR edit didn't break the `recurring-credit-requires-active-consent` rule (the pattern 'только при согласии в `ACTIVE`' is still in the ADR Decision #3, not in the Negative section, so it's unaffected). But let me verify quickly to be safe — actually the pattern is in Decision #3, and I only edited the Negative section. The rule should still pass. But let me re-run fitness_check and spine_lint to be thorough, since I made an edit.

Actually, the ADR edit only touched the Negative section, which doesn't contain the pattern. The pattern 'только при согласии в `ACTIVE`' is in Decision #3. Still present. I'm confident. But a quick re-run of fitness_check is cheap and gives final green confirmation. Let me do it once more to close the loop.
Финальная перепроверка после правки ADR.


All green. Now let me write the final summary.

The summary should cover the 7 deliverables concisely and list created/modified files.

Let me be concise but complete. I'll structure the final answer in Russian (matching the user's input language).

Files created:
- docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md

Files modified:
- ARCHITECTURE-SPINE.md (AD-009)
- openapi/tsp-api.yaml (v0.2)
- docs/contracts/tsp-api.md
- docs/contracts/opkc-adapter.md
- docs/nfr.md (§7)
- docs/solutioning.md (§1, §9, §11)
- .arch-handoff/CONSTRAINTS.yaml (fitness rule)

Note: .qwen/settings.json was already modified before I started (pre-existing, not mine). .arch-handoff/mcp-calls.jsonl is a runtime byproduct of the Spine MCP tools.

Verification: significance_score = Critical score 6; spine_lint PASS; openapi_lint PASS; contract_diff = 0 breaking / 3 non-breaking; fitness_check PASS (8 rules, 0 violations).

Let me write the final answer.
Пакет готов. Все проверки Spine зелёные.

## Что подготовлено (7 пунктов задачи)

**1. Значимость и маршрут** — `significance_score` дал **Critical, score 6** (триггеры: `api_contract_change`, `consistency_model_change`, `data_contract_change`, `financial_impact`, `new_component`, `new_datastore`). Причина глубины: списание происходит **без действия плательщика на каждую операцию** — ошибка (двойное списание периода, списание после отзыва, превышение лимита) = регуляторный инцидент по 161-ФЗ, а не «баг в UI». Требует полного Solutioning + обязательную человеческую точку A3.

**2. Влияние на архитектуру** — в `ARCHITECTURE-SPINE.md` добавлен **AD-009** (рекуррентное списание только по активному согласию с локальным enforcement лимитов). Существующие AD-001…AD-008 **не меняются** — рекуррентный платёж переиспользует машину платежа (сужает путь: `CREATED→PAID` без `QR_ISSUED`), зачисление по-прежнему только из `PAID`.

**3. Архитектурное решение** — новый **ADR-008**: согласие как сущность первого класса со своей статусной машиной (`PENDING→ACTIVE→CANCELLED|EXPIRED|REVOKED|FAILED`), merchant-driven инициация, дедупликация периода `consentId+periodKey`. Три альтернативы с причинами отказа, негативные последствия, обратимость `reversible` + условие пересмотра.

**4. Контракты без поломки потребителей** — `openapi/tsp-api.yaml` v0.1→**0.2** (строго аддитивно): новые эндпоинты `/v1/consents*`, опциональные поля `paymentType`/`consentId`/`periodKey`. `contract_diff`: **0 breaking / 3 non-breaking**. Проза-контракт `tsp-api.md` (§3.6–3.8, §3.2.1) и `opkc-adapter.md` (операции `registerConsent`/`initiateRecurringDebit` + события `consent.*`) расширены аддитивно.

**5. NFR** — `docs/nfr.md` §7: `0` списаний без согласия/сверх лимита/двойных за период, p95 < 500 мс, throughput с бимодальным пиком «дня списаний», ежечасная сверка согласий.

**6. Критерии приёмки и откат** — `docs/solutioning.md` §11.5 (EARS, 8 проверяемых критериев с негативными сценариями) и §11.6 (фиче-флаг per-ТСП, `stop-new` без остановки разовых платежей, сигналы отката и владелец решения).

**7. На человека** — §11.7: точный протокол НСПК (внешний вход), политика лимитов/AML, подтверждение merchant-driven, семантика `periodKey`, сглаживание пика, пробное списание.

## Созданные и изменённые файлы

**Создан:**
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`

**Изменены:**
- `ARCHITECTURE-SPINE.md` — добавлен AD-009
- `openapi/tsp-api.yaml` — v0.2, эндпоинты согласий + рекуррентные поля
- `docs/contracts/tsp-api.md` — секции согласий/рекуррентных списаний, коды ошибок, вебхуки, версионирование
- `docs/contracts/opkc-adapter.md` — операции/события согласий и рекуррентного списания
- `docs/nfr.md` — раздел §7
- `docs/solutioning.md` — §1 (scope), §9 (gaps), §11 (дизайн, приёмка, откат, решения человека)
- `.arch-handoff/CONSTRAINTS.yaml` — fitness-правило `recurring-credit-requires-active-consent`

## Верификация (инструменты Spine)

`spine_lint` PASS · `openapi_lint` PASS · `contract_diff` 0 breaking · `fitness_check` PASS (8 правил, 0 нарушений, ослаблений нет).

Два замечания: `.qwen/settings.json` был изменён до начала работы (не трогал); `.arch-handoff/mcp-calls.jsonl` — runtime-журнал вызовов Spine-инструментов, не входит в пакет.
