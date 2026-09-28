<!-- источник: <HARNESS>/runs/cells/openspec-r1/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-cells-openspec-r1-ws/chats/a001f3fa-da47-4a61-a38f-48515d53496e.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `skill(skill="openspec-propose")`

The user is asking me to prepare an architectural package for a change on top of an accepted solution. This is a substantial task involving understanding the repository, the existing architecture, and producing a set of artifacts. The user explicitly mentions OpenSpec skills and methodology tools are available in the project, and I should use them.

Let me first understand the repository structure and the accepted solution. This is clearly an OpenSpec-based project (there's `openspec/` directory, `.arch-handoff/`, and multiple openspec skills available).

Let me think about the workflow. The user wants:
1. Оценка значимости изменения и маршрута (significance assessment and route)
2. Влияние на принятую архитектуру (impact on invariants AD-001..AD-008)
3. Архитектурное решение с альтернативами (architecture decision with alternatives)
4. Изменения контрактов openapi/tsp-api.yaml без поломки
5. Измеримые NFR
6. Критерии приёмки и план отката
7. Что остаётся на решение человека-архитектора

The user says: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" (Change accepted solution files only in the way accepted in this repository). And "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению" (There may be methodology skills and tools installed — use them as intended).

So this is an OpenSpec proposal task. The available skills include `openspec-propose` / `opsx-propose` which is exactly for "Propose a new OpenSpec change with all artifacts generated in one step."

I should start by exploring the repository to understand the accepted solution, then use the OpenSpec propose skill to create the change.

Let me first read the key files. I should understand:
- ARCHITECTURE-SPINE.md (invariants AD-001..AD-008)
- docs/ (solutioning, NFR, ADRs, contracts, state machine)
- openapi/tsp-api.yaml
- .arch-handoff/ (rules and handoff package)
- openspec/ structure

Let me start by reading these. This is a big task, so I should be systematic. Let me begin with reading the key files in parallel.

Actually, first, let me note this is a "plan before uncertain work" situation but the user has given a very clear, detailed brief. The task is to prepare an architectural package. The right approach is to use the OpenSpec workflow since that's what the repository uses.

Let me invoke the openspec-propose skill since that's the designated methodology. But wait — I should first understand the repo. Actually the skill itself will guide me. Let me read the skill first by invoking it, or should I read the repo first?

The instruction says: "When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action". The openspec-propose skill is directly relevant. But I also need to understand the repository first to make a good proposal.

Actually, let me think. The task is essentially "openspec propose" for this business change. The skill `openspec-propose` will guide the process. Let me invoke it.

But actually, I should first do a bit of exploration to understand what's there, because the skill might assume certain things. However, the guidance is clear: invoke the relevant skill immediately. The openspec-propose skill is the designated tool for this exact task.

Let me invoke the skill first, and it will tell me how to proceed. Actually, let me be careful — the skill invocation will load instructions into context. Let me do that first.

Actually, I'll invoke the openspec-propose skill as my first action since it's clearly the designated methodology for this task.

Let me go.

  `run_shell_command(command="openspec list --json 2>&1; echo \"---EXIT:$?---\"", description="Check OpenSpec project root")`
  `run_shell_command(command="openspec context --json 2>&1; echo \"---EXIT:$?---\"", description="Load OpenSpec project context")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/ARCHITECTURE-SPINE.md")`

Let me follow the workflow. First, I need to understand the request and check the project. The user's request is clear enough - they want an architectural package for adding recurrent C2B debits (СБП subscriptions) to the accepted solution.

Let me first check the project's OpenSpec setup and understand the repository. Let me run the project check commands and read key files in parallel.

Let me start with:
1. `openspec list --json` to check root
2. `openspec context --json`
3. Read key files: ARCHITECTURE-SPINE.md, docs/, openapi/tsp-api.yaml, .arch-handoff/

Let me do the project check first and read key files in parallel.

  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/openspec/config.yaml")`
  `run_shell_command(command="cd <HARNESS>/runs/cells/openspec-r1/ws && find openspec docs openapi .arch-ha, description="List all files in openspec, docs, openapi, arch-handoff")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/openapi/tsp-api.yaml")`

The project root is set up. Now I need to read the config.yaml to get project context, and read the key docs. Let me read:
1. openspec/config.yaml
2. docs/solutioning.md
3. docs/nfr.md
4. docs/adr/ (ADR-001..007)
5. docs/contracts/
6. openapi/tsp-api.yaml
7. .arch-handoff/ (TASK.md, RUBRIC.yaml, CONSTRAINTS.yaml, ARCHITECTURE.md, MANIFEST.json)

Let me read these in parallel. First, let me check what's in the openspec directory structure and config.

  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/docs/contracts/opkc-adapter.md")`

Let me read the key docs. I need:
1. docs/solutioning.md
2. docs/nfr.md
3. docs/spec/state-machine.md
4. docs/contracts/tsp-api.md
5. docs/contracts/opkc-adapter.md
6. docs/adr/ADR-007-proposed-a3.md (the hybrid strategy)
7. .arch-handoff/TASK.md, RUBRIC.yaml, CONSTRAINTS.yaml, ARCHITECTURE.md, MANIFEST.json

Let me read these in parallel.

  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/.arch-handoff/ARCHITECTURE.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/.arch-handoff/MANIFEST.json")`

Now let me read the ADRs and the .arch-handoff files. Let me read the key ones: ADR-005 (зачисление и возвраты), ADR-007 (strategy), and the .arch-handoff TASK.md, RUBRIC.yaml, CONSTRAINTS.yaml, ARCHITECTURE.md, MANIFEST.json.

Let me read these.

  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/docs/adr/ADR-005-integraciya-s-abs-zachis)`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/docs/adr/ADR-004-at-least-once-dlq.md")`

I now have a good understanding of the repository. Let me read the remaining ADRs that are important for this change, particularly ADR-005 (зачисление/возвраты saga), ADR-007 (strategy), and maybe ADR-004 (notifications), ADR-006 (trust). Let me read the actual ADR files (not the truncated ARCHITECTURE.md).

Actually, I have a good enough understanding already from solutioning.md, state-machine.md, tsp-api.md, opkc-adapter.md. But I should read ADR-005 and ADR-007 fully since the change (recurrent debits / СБП подписки) touches the saga/refund model and the strategy.

Let me read the key ADR files.

  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/docs/rfp/vendor-rfp.md")`
  `run_shell_command(command="cd <HARNESS>/runs/cells/openspec-r1/ws && openspec schemas --json 2>&1 | head, description="List OpenSpec workflow schemas")`

I now have a thorough understanding of the repository. Let me also check the README.md and the ADR-006 (trust) briefly, and check the openspec specs directory structure. Actually I have enough. Let me also check if there's a `openspec/specs/` with existing capabilities, and check the `docs/rfp/vendor-rfp.md` briefly.

Actually, let me quickly check the README and openspec specs directory to understand established capability organization.

  `run_shell_command(command="cd <HARNESS>/runs/cells/openspec-r1/ws && openspec new change \"add-recurring, description="Create OpenSpec change add-recurring-debits")`

Now I have a thorough understanding of the repository. The project uses the spec-driven schema (default). I understand the accepted architecture, the invariants AD-001..AD-008, the contracts, the state machine, NFRs, etc.

Now the user wants an architectural package for a new change: **рекуррентные C2B-списания по согласию плательщика — подписки СБП** (recurrent C2B debits / СБП subscriptions).

This is clearly an OpenSpec proposal task. I should create a change using the OpenSpec spec-driven workflow. The change name should be kebab-case. Something like `sbp-recurring-debits` or `add-recurring-subscriptions`.

Let me think about what this change involves technically before creating the change.

**Business context**: ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента.

This is essentially the СБП "Согласие на списание" / "автоплатежи" (recurring payments). In СБП terms, this is the "согласие плательщика на списание" (standing order / mandate) - НСПК has a specific service for this. There's a payment type where the payer gives consent (согласие) to a ТСП to debit funds without QR per transaction.

This maps to the СБП "списание по согласию" (pull payment with mandate). In the current accepted solution, `Автоплатежи` (autopayments) are explicitly listed in the Roadmap (вне scope): "C2C, выплаты B2C/B2B, диспуты, автоплатежи."

So this change brings "автоплатежи" / рекуррентные списания into scope. This is a significant change.

Let me think about the architectural implications:

1. **Significance/route assessment**: This is a significant change. It introduces:
   - A new first-class entity: "согласие плательщика" (mandate/consent) — lifecycle (создание, подтверждение, отзыв, истечение).
   - A new payment type: списание по согласию (without QR), where the ТСП initiates the debit and the payer's bank automatically authorizes.
   - This touches the status machine (new states/flows), the API contract (new endpoints), the ОПКЦ adapter contract (new methods/events for consent registration and recurring debits), the state machine, NFRs, and compliance (recurring payments have specific regulatory requirements: notification of payer, cancellation rights, limits).

2. **Impact on invariants**: 
   - AD-001 (isolation): unchanged — still all through adapters.
   - AD-002 (status machine single source of truth): extended — consent becomes part of the single source of truth; consent + debit statuses.
   - AD-003 (idempotency): extended — consent idempotency key, debit idempotency.
   - AD-004 (single ОПКЦ adapter): unchanged in principle — the adapter contract extends.
   - AD-005 (зачисление only from PAID): this is the key one. For debits, the flow is DIFFERENT: it's a debit (списание), not a зачисление to ТСП. Actually wait — for C2B, the merchant receives money. Recurring C2B debits: the payer's money is debited and credited to the merchant. So the "зачисление на счёт ТСП" still happens, but the authorization (consent) replaces the QR action. So AD-005's invariant "зачисление только из подтверждённого статуса" still holds, but the "подтверждённый статус" now comes from consent-based authorization rather than QR+payer action. Need to think about whether AD-005 needs a new analogous invariant for debits: "дебетование возможно только по активному согласию" (debit only with active consent).
   - AD-006 (trust zones): unchanged.
   - AD-007 (compliance): extended — new regulatory obligations for recurring payments (notifying payer, consent revocation, refund/cancellation rights).
   - AD-008 (strategy): unchanged in principle, but the vendor must support consent/recurring methods in the ОПКЦ adapter → RFP extension.

3. **The "Платежи из воздуха" prevention**: for debits, we need a new invariant: "списание по согласию только при активном, подтверждённом согласии" — analogous to AD-005.

Now, this is a substantial architectural change. The key question for the route/assessment: is this a new AD (spine invariant) or does it fit within existing invariants?

The change likely introduces:
- New entity "Согласие" (consent/mandate) with its own state machine.
- New payment type "RECURRING" debit.
- Extends status machine for payments (maybe a parallel state machine for debits, or reuse).
- New API endpoints: `POST /v1/consents` (create consent), `GET /v1/consents/{consentId}`, `POST /v1/consents/{consentId}/revoke`, `POST /v1/consents/{consentId}/debits` (initiate debit), `GET /v1/debits/{debitId}`, refunds for debits.
- Extends ОПКЦ adapter contract: `registerConsent`, `revokeConsent`, `createDebit` (or the consent/debit operations), new events `debit.paid`, `consent.activated`, `consent.revoked`, etc.
- New NFRs: consent activation latency, debit throughput, notification to payer (регуляторное требование), refund window for debits.
- Compliance: 161-ФЗ (НПС), 152-ФЗ (ПДн of consent), 115-ФЗ, and specific СБП recurring rules (право плательщика на отзыв согласия, уведомление, лимиты).

This is definitely a "significant" change requiring deep design — probably a new ADR (ADR-008 for recurring) plus extension of contracts and specs. Route: it's a feature-level change on top of an existing Critical initiative. Significance is high (financial, compliance, new entity).

Actually, I need to be careful about the route. The repository already has a "route" concept (Critical, significance 11/15). The user asks for "Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему)". So I need to assess: is this a new ADR + spec change + contract change, and does it need a human decision (like A3)?

Key human decisions likely:
1. Whether to support "списание по согласию" as a first-class СБП service or to reuse the existing C2B flow with a new "consent" authorization model — this is a product/architecture decision.
2. The consent confirmation channel (how the payer confirms consent — this is critical: in СБП, consent confirmation typically happens in the payer's bank app; the ТСП initiates, the payer confirms via СБП). Need to clarify the flow.
3. Regulatory limits and notification policy (liмиты на списания, уведомление плательщика).
4. Whether the ОПКЦ adapter vendor supports recurring (extends RFP) — this ties to ADR-007/AD-008.

Now, per the OpenSpec propose workflow, I should:
1. Create the change.
2. Generate proposal.md, specs/, design.md, tasks.md.

The user's request explicitly lists 7 deliverables which map well to the OpenSpec artifacts:
1. Significance/route → proposal.md
2. Impact on invariants → proposal.md + design.md
3. Architecture decision with alternatives → design.md
4. Contract changes → specs/ + design.md (and the actual contract delta)
5. Measurable NFR → specs/ or design.md
6. Acceptance criteria + rollback → tasks.md + proposal.md/design.md
7. What remains for human architect → proposal.md (open questions) / design.md

Wait — but there's a nuance. The user's request is broader than a typical OpenSpec "change" — they want a full "архитектурный пакет" that can be taken to "архитектурное решение" (architectural review/decision) and then handed to implementers.

The OpenSpec spec-driven schema produces: proposal.md, specs/<capability>/spec.md, design.md, tasks.md.

I need to map the 7 deliverables into these artifacts:
- proposal.md: significance assessment + route, impact on invariants, what changes/what doesn't, human decisions remaining, rollback summary.
- specs/<capability>/spec.md: the delta spec — the new capability (recurring debits / consent) with SHALL requirements, including NFRs, contract changes.
- design.md: the architecture decision with alternatives, consequences, reversibility, contract changes detail.
- tasks.md: implementation steps (the handoff to implementers).

Now, about the contract change (openapi/tsp-api.yaml): The user says "Изменения контрактов (openapi/tsp-api.yaml) без поломки существующих потребителей". But the OpenSpec propose workflow has a **planning boundary**: "Do not edit project code." Is editing the openapi contract file "code"? The openapi/tsp-api.yaml is a contract artifact, not code. However, the workflow guardrail says "Do NOT implement the change, start the apply workflow, or edit project code during this workflow."

Hmm. But the contract change is part of the planning artifacts. In OpenSpec, the spec delta captures "what the system must do" — the contract change would be described in the spec/design. Actually editing the actual `openapi/tsp-api.yaml` file is a change to a non-OpenSpec project file. The propose workflow creates artifacts under `openspec/changes/<name>/`.

I think the right approach: The planning artifacts (proposal, spec, design, tasks) should DESCRIBE the contract changes precisely (the new endpoints, schemas, fields) so that they can be applied during the apply phase. The actual editing of `openapi/tsp-api.yaml` happens during apply, not propose.

But wait — the user explicitly asked for "Изменения контрактов (openapi/tsp-api.yaml) без поломки существующих потребителей" as a deliverable. I should include the concrete contract delta as part of the design/spec artifact (described in the delta spec), with the exact YAML additions, so the change is reviewable. That's the OpenSpec way: the spec delta contains the requirements, and the design describes how. I should NOT directly edit openapi/tsp-api.yaml during propose (that's apply territory), but I should capture the full contract delta in the change artifacts.

Actually, let me reconsider. The user says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" (Change accepted solution files only in the way accepted in this repository). The accepted way in this repo is OpenSpec (the repo has openspec/ structure, config.yaml, and the .arch-handoff). So the way to change is: create an OpenSpec change with proposal/specs/design/tasks, which will later be applied (which is when the actual contract file and spine/ADR files get updated).

So I'll create the OpenSpec change, and within it capture:
- The significance/route assessment
- Impact on invariants
- The ADR (with alternatives)
- The contract delta (full, in the spec/design)
- NFRs
- Acceptance criteria + rollback
- Human decisions remaining

This maps perfectly to the spec-driven schema.

Now let me plan the change name. Something like `recurring-debits` or `sbp-recurring-consent` or `add-recurring-debits`. Let me use `add-recurring-debits` (kebab-case). Actually, given the business term "подписки СБП" / "рекуррентные списания по согласию", I'll name it `sbp-recurring-debits` or `recurring-consent-debits`. Let me use `add-recurring-debits`.

Actually, let me think about what's the best capability path for specs. The existing specs directory is empty (only .gitkeep). So I need to establish the capability organization. Given the project structure has `docs/` for solutioning etc., but OpenSpec specs should be under `openspec/specs/`.

The capability path should reflect the domain. Since this is a new capability "recurring debits" (рекуррентные списания / подписки), I'll use a capability like `recurring-debits` or `payments/recurring-debits`. Given the existing main specs are empty, I'll start a clean organization. Maybe `sbp-recurring-debits` or just `recurring-debits`.

Let me check the openspec specs directory to understand any existing organization. It only has .gitkeep. So it's greenfield for specs.

Let me think about what the spec capability should be named. The change is about recurring C2B debits (consent-based). I'll create the capability as `recurring-debits`.

Actually, let me reconsider whether I should ask the user any clarifying questions first. The workflow says: "If the request contains ambiguity that would materially affect scope... ask the user before creating the change."

There are some material ambiguities:
1. Scope of the first wave: full "consent lifecycle + recurring debit" or just a minimal version? The user is clear: "рекуррентные C2B-списания по согласию плательщика — подписки СБП." So consent + recurring debits.
2. How the consent is confirmed (channel): In СБП, this is important. But this is a protocol detail that's `[ТРЕБУЕТ ПРОВЕРКИ]` (external input from НСПК documentation). So I can record it as an assumption/open question rather than block.

Actually, I think the request is clear enough in scope. The main architectural decisions (which are the point of this task) should be presented as part of the ADR with alternatives, and the "human decisions remaining" are exactly what the user asked for in point 7.

However, I want to be careful. There's a genuinely material ambiguity: **does the merchant get to initiate arbitrary debits, or is each debit tied to a specific consent with a max amount / frequency limit?** This is a regulatory+product decision. But actually, this is exactly the kind of thing I should present as a design decision with alternatives and flag for human decision, rather than block on.

Another material point: **The consent confirmation flow**. In СБП recurring payments, the flow is typically:
- ТСП creates a consent (согласие) referencing the payer.
- The payer confirms consent in their bank's app (СБП push/QR to confirm consent).
- After confirmation, ТСП can initiate debits (списания) up to consent limits without further payer action.
- The payer can revoke consent at any time.

This is the key architecture. I should model it: consent has states (PENDING → ACTIVE → REVOKED/EXPIRED), and debits reference consent.

I think I have enough to proceed without blocking questions. The task is explicitly to prepare an architectural package, and the human decisions are part of the deliverable. I'll record assumptions and open questions in the artifacts.

Actually, wait — let me reconsider the materiality. The workflow says ask about "ambiguity that would materially affect scope, externally observable behavior, compatibility, or acceptance criteria." 

One genuinely material question: **Should this be a full new ADR + spine invariant addition, or a change that fits within existing invariants?** The user explicitly asks me to "assess impact on invariants: which invariants are touched, what changes, what doesn't." So they want me to do that analysis, not ask them.

I'll proceed. I have enough context. Let me note a couple of genuinely important design forks and present them as decisions-with-alternatives + open questions, which is the architect's job here.

Let me now determine the schema is spec-driven (default), and create the change.

Let me plan the actual content deeply before writing, since this is the meat of the task.

---

## DEEP ANALYSIS FOR THE CHANGE

### 1. Significance & Route Assessment

The change introduces "рекуррентные C2B-списания по согласию плательщика" (СБП subscriptions / autopayments). This was explicitly in the "Deferred / Roadmap" of the accepted solution ("автоплатежи" — roadmap after C2B stabilization).

Significance:
- New first-class domain entity: **Согласие (consent/mandate)** with its own lifecycle and state machine.
- New financial operation: **дебетование по согласию** (debit) — no QR, no per-payment payer action.
- New compliance surface: recurring payments have specific regulatory obligations (НПС 161-ФЗ, consent revocation rights, payer notification, limits), ПДн (consent data), 115-ФЗ (AML on recurring), КИИ.
- Touches: API contract, ОПКЦ adapter contract (vendor), status machine, NFRs, reconciliation.

Route: **High / near-Critical**. It's a feature-level change on an existing Critical initiative. It does NOT change the parent spine (still C2B acquisition), but it adds a new sub-domain. Needs: new ADR (ADR-008 for recurring) + spec delta + design + contract extension + updated RFP (vendor must support consent/recurring). Deep design required because: financial significance, new entity, compliance, and a new invariant ("списание только по активному согласию" — analogous to AD-005).

Why deep design (not just a small change):
- New invariant needed (debit only with active consent) — extends the spine AD set.
- New state machine (consent) + new payment type (debit) — extends ADR-002/005.
- New API surface (consents + debits + their refunds).
- Vendor/ОПКЦ adapter contract extension — touches ADR-007/AD-008 boundary.
- Regulatory/compliance analysis required.

### 2. Impact on invariants AD-001..AD-008

| Invariant | Impact | Change |
|---|---|---|
| AD-001 (изоляция контура) | не затронут | debits go through same adapters; no new direct access |
| AD-002 (статусная машина = единый источник истины) | расширен | consent gets its own status machine in the same БД + outbox; debits reuse payment FSM or get a parallel FSM; atomic transitions + outbox apply to consent transitions too |
| AD-003 (идемпотентность) | расширен | new idempotency keys: consentId (consent creation), debitId (debit initiation), eventId for consent/debit notifications |
| AD-004 (единственный адаптер ОПКЦ) | не затронут в принципе | contract extends; still single adapter; vendor must add consent/debit methods (RFP extension) |
| AD-005 (зачисление только из PAID) | частично затронут / аналог | the debit authorization replaces QR action; the "зачисление на счёт ТСП" still only from confirmed debit status. NEW analogous invariant required: "списание/дебетование по согласию — только при ACTIVE согласии" (AD-009) |
| AD-006 (trust-зоны) | не затронут | same zones |
| AD-007 (соответствие НПС/КИИ/ПДн) | расширен | new compliance: consent data (ПДн), recurring notification, revocation rights, limits; audit of consent lifecycle |
| AD-008 (стратегия реализации) | не затронут в принципе, но расширяет RFP | vendor adapter must implement consent/debit contract; kernel still contract-independent |

What changes:
- New entity "Согласие" (consent) with states: `PENDING_CONSENT` → `ACTIVE` → `REVOKED` / `EXPIRED` / `FAILED`.
- New payment type / debit operation with states (reuse payment FSM or a debit FSM): debit is essentially a payment with `initiatedByConsent`, no QR.
- Status machine: debits go through a flow analogous to C2B but skip `QR_ISSUED` (no QR); instead `CREATED` → `PAID` (confirmed by НСПК via consent) → `CREDITED` → `COMPLETED`.
- API: new endpoints for consent lifecycle + debit initiation + debit status + refunds of debits.
- ОПКЦ adapter: new methods/events.
- NFR: new metrics.
- RFP: vendor must support recurring.

What does NOT change:
- Parent spine (still C2B acquisition; C2C/B2C/B2B still out of scope).
- Trust zones, transport isolation, outbox mechanism, reconciliation approach.
- The hybrid strategy (AD-008).
- Existing C2B QR flow (backward compatible).

### 3. Architecture decision with alternatives

The core decision: **How to model recurring debits in the gateway.**

Decision: Introduce a first-class **Consent (согласие)** entity with its own state machine, and treat each recurring debit as a Payment of a new `paymentType=RECURRING` (or a distinct "Debit" entity) that references the consent and skips QR. Debit authorization comes from the ACTIVE consent, not from QR.

Alternatives:
1. **Reuse existing Payment FSM + add consent as authorization context** (chosen): minimal new states, reuse зачисление/refund/saga machinery, debit = payment without QR. Consent = separate entity controlling whether debits are allowed.
2. **Fully separate "Debit" domain** (separate FSM, separate tables, separate API): cleaner isolation but duplicates reconciliation/refund/idempotency machinery, higher cost.
3. **Delegate recurring entirely to vendor/НСПК** ("вендорский сервис подписок"): vendor manages consent + debits; gateway only relays. Violates AD-001/AD-002 (financial logic must be in gateway), vendor lock-in, harder audit — rejected.
4. **Consent as a flag on ТСП without per-payer consent**: violates regulatory requirement (consent must be per payer, revocable) — rejected.

Chosen: (1) with consent as separate state machine. Reversibility: mostly reversible (consent is additive; the payment FSM extension is additive). The "no QR" path is a new transition — careful not to break existing QR flows.

Also a sub-decision: **Consent confirmation channel** — ТСП initiates consent, payer confirms in payer's bank app via СБП (НСПК push). This is protocol-level `[ТРЕБУЕТ ПРОВЕРКИ]`. Alternatives: (a) payer confirms via QR-based consent link (scans QR once to authorize future debits); (b) НСПК push notification; (c) out-of-band (ТСП's own channel + bank). The actual mechanism is dictated by НСПК protocol — flag for verification. Chosen: follow НСПК protocol, but architect the gateway to be channel-agnostic (consent status comes from adapter events, not from gateway's own UI).

### 4. Contract changes (openapi/tsp-api.yaml)

New endpoints (all additive, backward compatible):
- `POST /v1/consents` — create consent (Idempotency-Key). Returns consentId + status PENDING.
- `GET /v1/consents/{consentId}` — consent status.
- `POST /v1/consents/{consentId}/revoke` — revoke consent (merchant or payer initiated).
- `POST /v1/consents/{consentId}/debits` — initiate debit (Idempotency-Key, amount, purpose). Returns debitId.
- `GET /v1/debits/{debitId}` — debit status (reuse Payment schema or a Debit schema).
- `POST /v1/debits/{debitId}/refunds` — refund a debit (reuse refund).
- Possibly `GET /v1/consents` (list, optional).

New schemas: `Consent`, `ConsentRequest`, `Debit` (or reuse Payment with `paymentType`), `DebitRequest`.

Webhooks: new events `consent.activated`, `consent.revoked`, `consent.expired`, `debit.completed`, `debit.failed`, `debit.refunded`.

Backward compatibility: existing `/v1/payments` unchanged; new endpoints added under `/v1/consents` and `/v1/debits` (no version bump needed — additive). Optionally extend Payment schema with `paymentType` enum (`QR`, `RECURRING`) — but adding an optional field is backward compatible. The `status` enum already includes needed states; debits may not use `QR_ISSUED`/`EXPIRED` (or reuse them).

I need to decide: **Debit as a separate resource or as a Payment with type?** This is a real design fork. Options:
- (A) Debit = Payment with `paymentType=RECURRING` (reuse `/v1/payments` for debits too, add `consentId` + `paymentType`). Fewer new endpoints, reuses refund/status. But mixes semantics (QR vs consent) in one resource.
- (B) Separate `/v1/debits` resource. Cleaner, but duplicates refund/status endpoints.

I'll present this as a decision in design.md with recommendation. Given backward-compat and reuse of the status/saga machinery, I lean towards (A) reusing Payment with a `paymentType` discriminator + separate `/v1/consents` resource for consent lifecycle, and debits initiated via `POST /v1/payments` with `paymentType=RECURRING` + `consentId`. Actually that's cleaner: consent is its own resource (it's not a payment), debits ARE payments (just authorized by consent instead of QR).

Hmm, but there's nuance: a "debit" (списание) in the merchant's perspective is still a C2B payment to the merchant — money flows payer→merchant. So it IS a payment. The only difference is authorization: consent instead of QR+payer-action. So reusing Payment with `paymentType=RECURRING` + `consentId` reference is architecturally clean and minimal.

Let me go with: 
- **Consent** = new resource `/v1/consents` (lifecycle: create → PENDING → ACTIVE → REVOKED/EXPIRED).
- **Debit** = a Payment (`/v1/payments`) with `paymentType: "RECURRING"` and `consentId`. No QR fields. Status flow: `CREATED → PAID → CREDITED → COMPLETED` (skipping QR_ISSUED; or a new state). Refunds via existing `/v1/payments/{paymentId}/refunds`.

This is the minimal, backward-compatible approach. The Payment schema gains optional `paymentType` (enum `QR`|`RECURRING`, default `QR`) and optional `consentId`. The `qrType`/`qrUrl`/`qrImage` fields become conditional (only for QR type). No breaking change.

Actually, I realize I should also think about whether the debit should skip `QR_ISSUED` state. In the current FSM, `QR_ISSUED` means "QR/ссылка получена". For recurring, there's no QR, but there's still a step "debit registered with НСПК, awaiting НСПК to debit payer's account". So the state machine for a debit is: `CREATED → PAID → CREDITED → COMPLETED` (and FAILED/REFUNDED). It skips QR_ISSUED and EXPIRED. The state machine spec would need a note: "for paymentType=RECURRING, QR_ISSUED and EXPIRED are not reachable; the flow is CREATED → PAID".

This is a clean extension: the FSM already supports `CREATED → PAID` conceptually, but currently only via `QR_ISSUED`. Adding a direct `CREATED → PAID` transition guarded by `paymentType=RECURRING AND consent=ACTIVE`.

Let me also think about the new invariant (AD-009): "Дебетование (списание) по согласию возможно только при активном, подтверждённом согласии плательщика; согласие отзывается плательщиком в любой момент и отзыв немедленно прекращает новые дебеты." This is the recurring analog of AD-005. Fitness: "списание невозможно при REVOKED/EXPIRED/PENDING согласии".

Now let me also think about NFRs (deliverable 5):
- Consent activation latency: p95 < 5 s (from payer confirmation to ACTIVE + webhook).
- Debit initiation latency: p95 < 500 ms (registration), analogous to QR registration.
- Debit completion: зачисление p95 < 60 s (same as C2B).
- Revocation effectiveness: revoke → new debits rejected within ≤ 1 s (guarantee: no debit after revoke).
- Consent availability ≥ 99.95% (same as gateway).
- Idempotency: double debit = 0; double consent = 0.
- Reconciliation: consent/debit reconciliation hourly with НСПК, daily with АБС.
- Throughput: recurring debits may be batch-scheduled (ЖКХ/связь — массовые списания в начале месяца) → need burst capacity. Add: "массовые дебеты (wave) — 1000 TPS burst, 200 TPS sustained" (extend existing).
- Compliance: payer notification 100% for each debit (if required), consent revocation 100% honored.
- New: consent data retention / ПДн.

### 6. Acceptance criteria + rollback

Acceptance criteria:
- Consent lifecycle works (create→confirm→active→revoke).
- Debit only with ACTIVE consent; revoked consent blocks debits (fitness test).
- Idempotent consent creation and debit initiation (no double debits).
- Backward compatible API (existing C2B QR tests still pass).
- NFR metrics met (latency, throughput, revocation effectiveness).
- Reconciliation covers consents and debits.
- Compliance: payer notification, audit of consent lifecycle.

Rollback:
- Pre-production: don't enable; reversible.
- Post: feature flag `recurring.enabled`; stop-new (disable new consent creation + new debits) without affecting existing C2B and already-active consents; rolling release rollback; consent data not migrated back (gateway remains source of truth); existing QR payments unaffected (separate flag/path).
- Emergency: kill-switch on debit initiation; DLQ + runbook; reconciliation compensates.

### 7. What remains for human architect

- Confirm the СБП recurring service semantics with НСПК (protocol for consent + recurring debit) — external input `[ТРЕБУЕТ ПРОВЕРКИ]`.
- Regulatory sign-off: consent revocation rights, payer notification obligations, limits (max amount/frequency), ПДн handling — ИБ/комплаенс.
- Product scope: which ТСП segments first (кинотеатры/ЖКХ/связь), limits, refund window for debits.
- Vendor: whether chosen ОПКЦ adapter vendor supports consent/recurring (extends ADR-007/RFP); possibly new RFP round.
- New spine invariant AD-009 (debit only with active consent) — needs ratification (like ADR → spine Proposed).
- Business decision on debit refund/cancel policy (some recurring debits have mandatory refund window — e.g., 3-5 days for certain categories).

OK. I now have a comprehensive analysis. Let me proceed with the OpenSpec workflow.

Now let me create the change. Name: `add-recurring-debits` (or `sbp-recurring-debits`). I'll use `add-recurring-debits`.

Wait, let me reconsider the name. The business feature is "подписки СБП" / "рекуррентные C2B-списания по согласию". A good kebab name: `recurring-debits` or `sbp-recurring-debits` or `add-sbp-subscriptions`. I'll go with `add-recurring-debits` — descriptive and clear.

Let me now create the change and check its status.

Actually, before that — the workflow step 3 says determine the schema. Default is spec-driven (config.yaml has `schema: spec-driven`). So no `--schema` flag needed.

Let me create the change.

Actually, let me reconsider whether I need to ask any clarifying questions. I've identified the material ambiguities but they're mostly:
1. Consent confirmation channel — protocol-level, `[ТРЕБУЕТ ПРОВЕРКИ]`, I'll record as open question.
2. Debit as separate resource vs Payment type — I'll present as a design decision with a recommendation.
3. Refund window / limits — product decision, I'll flag.

These are all things the task explicitly asks me to produce ("рассмотренные альтернативы", "что остаётся на решение человека"). So I should proceed and record them. I don't think I need to block with ask_user_question — the task is to produce the package with these as deliverables, not to have them resolved now.

Let me proceed to create the change.

Let me first create the change and check status.
Понял задачу и изучил принятое решение. Теперь подготовлю архитектурный пакет изменения по принятой в репозитории методике OpenSpec (spec-driven). Сначала создам change.

  `run_shell_command(command="cd <HARNESS>/runs/cells/openspec-r1/ws && openspec status --change \"add-recu, description="Get artifact build order for the change")`
  `run_shell_command(command="cd <HARNESS>/runs/cells/openspec-r1/ws && openspec instructions proposal --ch, description="Get proposal artifact instructions")`

The artifact order is: proposal (ready) → specs, design (blocked on proposal) → tasks (blocked on specs, design).

Required set: applyRequires = ["tasks"], transitively → proposal, specs, design, tasks.

Let me get the instructions for proposal first.

  `run_shell_command(command="cd <HARNESS>/runs/cells/openspec-r1/ws && openspec list --specs --json 2>&1", description="List existing capability specs")`

Let me check the existing specs inventory.

  `write_file(file_path="<HARNESS>/runs/cells/openspec-r1/ws/openspec/changes/add-recurring-debits/pro, content="# Proposal\n\n## Why\n\nТСП с повторяющимися платежами (онлайн-кинотеатры, ЖКХ, связь) требуют рекуррентных C2B-списаний по заранее оформле)`

The specs inventory is empty (openspec/specs/ only has .gitkeep). So this is the first change establishing capabilities. I need to introduce new capabilities.

For this change, the natural capability organization. Given the domain (СБП платёжный шлюз), I'll introduce capabilities:
- `consent` (согласие плательщика — lifecycle) — new capability
- `recurring-debits` (рекуррентные списания/дебиты по согласию) — new capability

Or a single capability `recurring-debits` covering both consent and debit. 

Actually, let me think about the cleanest capability decomposition. The domain entities are:
1. **Consent (согласие)** — a first-class entity with its own lifecycle.
2. **Recurring debit (списание)** — a payment initiated by consent.

Since the existing C2B "payments" flow is described in `docs/` (not in openspec/specs), and openspec/specs is empty, I'm establishing the OpenSpec capability structure now. I think two capabilities is cleaner:
- `consents` — consent lifecycle (create, confirm, revoke, expire).
- `recurring-debits` — recurring debit initiation, status, refunds.

But to keep it simple and avoid over-fragmentation, I could do a single capability `recurring-debits` that covers consent + debit. However, consent is genuinely a separate concern with its own lifecycle and will be reused (e.g., C2C auto-transfers, B2C payouts could also use consent). So separating `consents` is justified.

Actually, let me reconsider. The user's task is about "рекуррентные C2B-списания по согласию плательщика — подписки СБП". The core new concepts:
1. Согласие (consent/mandate) — new entity.
2. Рекуррентное списание (debit) — new operation type.

I'll go with two capabilities:
- `consents` — the consent lifecycle.
- `recurring-debits` — the recurring debit operation (списание по согласию).

This is clean and maps to two spec files:
- `specs/consents/spec.md`
- `specs/recurring-debits/spec.md`

Now let me write the proposal. It should be concise (1-2 pages), in Russian, keep SHALL/MUST in English where structural.

Let me write proposal.md with:
- Why
- What Changes
- Capabilities (new: consents, recurring-debits)
- Impact

Then I'll do the specs, design, tasks.

Let me write the proposal now. I'll include the significance/route assessment briefly in "Why" and "What Changes" (since the user wants significance + route assessment, but proposal is about "why"). Actually, the significance/route assessment is a deliverable. Where does it go best? The proposal's "Why" covers the motivation and why-now. The detailed route assessment (significance score, why deep design) can go into design.md or the proposal's "What Changes". 

Actually, the 7 deliverables map to OpenSpec artifacts as follows:
1. Significance & route → proposal (Why + What Changes) + design (Route/decision depth).
2. Impact on invariants → proposal (Impact) + design (detailed invariant-by-invariant table).
3. ADR with alternatives → design.md (this is the "how").
4. Contract changes → specs (delta requirements) + design (the concrete YAML).
5. NFR → specs (requirements) + design.
6. Acceptance criteria + rollback → tasks.md + proposal/design.
7. Human decisions → proposal (open questions) + design.

Actually, the proposal template doesn't have an "open questions" section explicitly, but I can add it. The spec-driven proposal is flexible. Let me keep proposal concise and put the deep analysis in design.md.

Let me write proposal.md now. I need to be thoughtful and concise. I'll write in Russian.

Let me write the proposal content.

For "What Changes" I'll mark no breaking changes (all additive). The only "breaking" consideration: none — existing consumers unaffected.

Let me draft.

---

# Proposal: Рекуррентные C2B-списания по согласию плательщика (подписки СБП)

## Why

ТСП-категории с повторяющимися платежами (онлайн-кинотеатры, ЖКХ, связь) требуют рекуррентных C2B-списаний без участия плательщика в каждом платеже. Сейчас каждый платёж требует QR и действия клиента, что блокирует подписочную модель. Это выводит в scope ранее отложенную возможность «автоплатежи» (docs/solutioning.md, Deferred).

Significance / route: ... (I'll add a short route note here or in design).

## What Changes
- Новая сущность «Согласие плательщика» (consent) ...
- Новый тип операции «рекуррентное списание» ...
- ...

## Capabilities
### New Capabilities
- consents: ...
- recurring-debits: ...

## Impact
...

Let me write it fully.

Actually, I realize I should think carefully about where to put the "significance/route assessment" since it's deliverable #1 and important. The proposal "Why" can carry a concise version. But the full route assessment (significance score, comparison to the parent Critical, why deep design needed, what ADRs/artifacts it produces) is substantial. I'll put a concise route statement in proposal and the full analysis in design.md under a "Маршрут и значимость" section (design is allowed to have this kind of content since it's "how" at the architecture level).

Let me write proposal now.

  `run_shell_command(command="cd <HARNESS>/runs/cells/openspec-r1/ws && openspec instructions specs --chang, description="Get specs artifact instructions")`
  `run_shell_command(command="cd <HARNESS>/runs/cells/openspec-r1/ws && openspec instructions design --chan, description="Get design artifact instructions")`

Created proposal. Now let me get instructions for specs and design (both unblocked by proposal). Let me run status to confirm, then get instructions for both specs and design in parallel.

  `write_file(content="# Spec Delta\n\n## Purpose\n\nУправляет согласием плательщика (consent) на рекуррентные C2B-списания: создание, подтверждение, активация, о, file_path="<HARNESS>/runs/cells/openspec-r1/ws/openspec/changes/add-recurring-debits/spe)`

Now I'll create the two spec files and the design.md. Both specs and design are unblocked (depend only on proposal, which is done). I can write them in parallel conceptually, but they're separate write_file calls. Let me write the specs first (two files), then design, then tasks.

Actually I can write the spec files and design in parallel since they're independent files. But design should reference specs, and the specs should be coherent with design. Let me write them carefully.

Let me write:
1. `specs/consents/spec.md` — consent lifecycle.
2. `specs/recurring-debits/spec.md` — recurring debits.
3. `design.md` — the ADR, route, invariants impact, contract changes, NFR, acceptance criteria, rollback, human decisions.

The design.md instruction says design covers "how" — decisions, alternatives, risks, migration/rollback, open questions. The user's deliverables map well here:
- Deliverable 3 (ADR with alternatives, consequences, reversibility) → Decisions section.
- Deliverable 1 (route assessment) → I can put a "Маршрут и значимость" section (context/decisions). Actually the design template has "Context", "Goals/Non-Goals", "Decisions", "Risks/Trade-offs", "Migration Plan", "Open Questions". The route assessment fits in "Context" or a dedicated section. I'll add it to Context or as a leading part.
- Deliverable 2 (impact on invariants) → Context or a dedicated section.
- Deliverable 4 (contract changes) → Decisions (with concrete YAML delta) or a dedicated section.
- Deliverable 5 (NFR) → can go in design as part of decisions, or in the specs. The NFRs are externally observable behavior, so they belong in specs (as requirements). But the user wants "измеримые NFR" as a deliverable. I'll put the detailed NFR table in design.md (since it's "how we'll measure"), and reference key NFRs as requirements in the spec.
- Deliverable 6 (acceptance criteria + rollback) → Migration Plan (rollback) + tasks.md (acceptance criteria as task checks). Actually acceptance criteria fit in tasks.md (each task with verification) and in design's Migration Plan for rollback.
- Deliverable 7 (human decisions) → Open Questions section.

Let me be careful: the design template's "Open Questions" is for "genuinely deferrable unknowns, not decisions you skipped." But the user's deliverable 7 is "что остаётся на решение человека-архитектора" — these ARE decisions that need a human architect (regulatory sign-off, vendor capability, product scope). Some of these are genuinely "can't be resolved by me" (external inputs, human authority). I'll put them in Open Questions but clearly framed as "requires human architectural decision" with why. This is appropriate.

Actually, I want to distinguish:
- "Open Questions" (deferrable, can be answered later without changing specs) 
- vs "Decisions requiring human architect" (authority/external input).

The user's deliverable 7 is specifically "что остаётся на решение человека-архитектора и почему". I'll create a dedicated section "Требует решения человека-архитектора" in design.md. This is fine — the template is a guide, I can add sections.

Let me now write the specs first.

### Spec: consents

Purpose: manages the payer's consent (согласие) for recurring C2B debits.

Requirements:
1. Create consent (idempotent) → PENDING.
2. Consent confirmation/activation (from payer's bank via НСПК, delivered as adapter event) → ACTIVE.
3. Consent revocation (by ТСП or плательщик) → REVOKED.
4. Consent expiry → EXPIRED.
5. Consent status query.
6. Webhook notifications on consent status change.
7. Consent idempotency (no duplicate consent).
8. Consent data (ПДн) minimization + audit.

Scenarios for each.

### Spec: recurring-debits

Purpose: recurring C2B debits by active consent.

Requirements:
1. Initiate debit (idempotent) — only if consent ACTIVE.
2. Debit authorization: no QR, authorized by consent; зачисление only from confirmed status (PAID).
3. Debit must be rejected if consent not ACTIVE (invariant).
4. Debit refund (saga).
5. Debit reconciliation.
6. Debit status query.
7. Payer notification (if required).
8. Mass wave debits (throughput).

Let me write these specs carefully, using SHALL/MUST and #### scenarios (4 hashtags).

Let me write spec for consents.

Actually, let me think about the consent states and flow more concretely:

Consent states:
- `PENDING` — consent created by ТСП, awaiting payer confirmation.
- `ACTIVE` — payer confirmed; debits allowed.
- `REVOKED` — revoked by payer or ТСП (terminal).
- `EXPIRED` — TTL/validity expired (terminal).
- `FAILED` — payer declined confirmation / НСПК rejected (terminal).

Consent transitions:
- — → PENDING: POST /consents (idempotent).
- PENDING → ACTIVE: payer confirms (НСПК event consent.activated).
- PENDING → FAILED: payer declines / НСПК rejects.
- ACTIVE → REVOKED: payer revokes (НСПК event) or ТСП revokes (API).
- ACTIVE → EXPIRED: validity period ends.
- PENDING → REVOKED: ТСП cancels before confirmation.

Consent has fields: consentId, tspId, payerRef (some payer identifier — actually in СБП the payer is identified via their bank; the consent references the payer's account/phone), amount limits (maxAmount, maxFrequency/period), purpose, validity (expiresAt), status.

Important: consent carries limits — max amount per debit, max total per period, validity. This is key for compliance. The gateway MUST enforce: debit ≤ consent limit, consent not expired, consent not revoked.

Debit states (reuse payment FSM with paymentType=RECURRING):
- CREATED → PAID → CREDITED → COMPLETED (and FAILED/REFUNDED).
- No QR_ISSUED, no EXPIRED (or EXPIRED = НСПК didn't confirm within window).

Now the invariant: "Дебетование (списание) возможно только при ACTIVE согласии, в пределах лимитов согласия." Fitness: debit rejected when consent REVOKED/EXPIRED/PENDING or exceeds limit.

Let me now write the spec files.

I'll write the consents spec first.

Let me carefully craft requirements with scenarios. Keep in Russian but SHALL/MUST in English (per context rule: "Keep OpenSpec structural headings and SHALL/MUST keywords in English").

Let me write.

  `write_file(content="# Spec Delta\n\n## Purpose\n\nОбеспечивает рекуррентные C2B-списания (дебиты) по активному согласию плательщика: инициацию без QR и действи, file_path="<HARNESS>/runs/cells/openspec-r1/ws/openspec/changes/add-recurring-debits/spe)`
  `write_file(content="# Design\n\n## Context\n\nСм. `proposal.md` — Why. Здесь — оценка значимости/маршрута, влияние на инварианты принятой архитектуры и техниче, file_path="<HARNESS>/runs/cells/openspec-r1/ws/openspec/changes/add-recurring-debits/des)`

Now the design.md. This is the biggest and most important artifact, carrying deliverables 1, 2, 3, 4 (concrete), 5, 6 (rollback), 7.

Let me write a comprehensive design.md in Russian. I'll include:

1. Context (route/significance assessment — deliverable 1)
2. Goals / Non-Goals
3. Impact on invariants AD-001..AD-008 (deliverable 2) — table
4. Decisions (deliverable 3 — ADR with alternatives, consequences, reversibility):
   - Decision 1: Consent as first-class entity + debit as Payment with paymentType=RECURRING (alternatives, consequences, reversibility).
   - Decision 2: New spine invariant AD-009 (дебит только по активному согласию).
   - Decision 3: Consent confirmation channel (channel-agnostic, follow НСПК).
   - Decision 4: Consent limits enforcement (maxAmount, frequency, validity).
5. Contract changes (deliverable 4) — concrete openapi delta + opkc-adapter delta.
6. NFR (deliverable 5) — measurable table.
7. Risks / Trade-offs.
8. Migration Plan (deliverable 6 — rollback).
9. Acceptance criteria (deliverable 6) — I'll put here or in tasks.
10. Open Questions / human decisions (deliverable 7).

The design template has: Context, Goals/Non-Goals, Decisions, Risks/Trade-offs, Migration Plan, Open Questions. I'll extend with additional sections (Invariants impact, Contract changes, NFR, Acceptance criteria, Human decisions). That's fine — the template is a guide.

Let me write it carefully and completely. This is the core deliverable.

Let me be precise about the contract changes. I'll write the concrete OpenAPI YAML additions and the opkc-adapter contract additions.

For the OpenAPI contract, the additive changes:
- New paths: `/v1/consents`, `/v1/consents/{consentId}`, `/v1/consents/{consentId}/revoke`.
- Modified `PaymentRequest`: add `paymentType` (enum QR|RECURRING, default QR), `consentId` (optional, required when paymentType=RECURRING). `qrType` becomes conditional.
- Modified `Payment`: add `paymentType`, `consentId` optional.
- New schemas: `ConsentRequest`, `Consent`.

Let me write the full YAML delta as it would appear, clearly marked as additive.

Actually, I should write the design with the concrete contract delta embedded, so the human architect can review the exact contract change. Let me include a YAML snippet.

Let me also think about the consent schema fields:
- ConsentRequest: tspId, payerIdentifier (phone or bank account ref — `[ТРЕБУЕТ ПРОВЕРКИ]` per НСПК), maxAmount (per debit, копейки), maxTotalAmountPerPeriod (опц.), period (DAY/WEEK/MONTH), purpose, expiresAt (validity), redirectUrl (for confirmation), merchantConsentId (опц.).
- Consent (response): consentId, status (PENDING/ACTIVE/REVOKED/EXPIRED/FAILED), maxAmount, period, expiresAt, createdAt, activatedAt, revokedAt.

For PaymentRequest additions:
- paymentType: enum [QR, RECURRING], default QR.
- consentId: string, required when paymentType=RECURRING.
- When RECURRING: qrType/ttlSeconds/redirectUrl not applicable.

Payment response additions:
- paymentType, consentId (optional).

New error codes: CONSENT_NOT_ACTIVE, CONSENT_LIMIT_EXCEEDED, CONSENT_NOT_FOUND, CONSENT_CONFLICT.

New webhooks: consent.activated, consent.revoked, consent.expired, consent.failed, debit.completed (or reuse payment.completed with paymentType), debit.failed.

Actually the webhooks: for debits, reuse `payment.completed`/`payment.failed` with `paymentType` field, plus consent webhooks. That keeps it simple.

opkc-adapter contract additions:
- Methods: `registerConsent` (reference=consentId, payerRef, limits, purpose) → ACCEPTED; `revokeConsent` (reference=consentId, reason) → ACCEPTED; `createDebit` (reference=debitId/paymentId, consentRef, amount) → ACCEPTED (или синхронный ответ как createPaymentLink); `getDebitStatus` (by qrId/debitRef) — actually reuse getPaymentStatus; `getConsentStatus` (consentRef) → status.
- Events: `consent.activated`, `consent.revoked`, `consent.expired`, `consent.rejected`, `debit.paid` (or reuse payment.paid with correlationRef), `debit.rejected`.

Let me keep the opkc-adapter delta concise but concrete.

Now let me write the design. I need to be thorough but not bloated. Let me write it.

For the route assessment, let me give a significance score consistent with the existing "Critical (11/15)" for the parent. This change: I'll assess it as "High / значимость ~10/15" or "Critical-adjacent" — a feature-level change on an existing Critical initiative. It's not a new initiative, but it's a significant feature with new financial entity and compliance surface. I'll say: маршрут "Полное проектирование (аналог Solutioning для feature)" — needs new ADR + spec delta + contract extension + NFR + RFP extension. Not a trivial change.

Actually the repo uses a route vocabulary: "Critical (значимость 11/15)", "полный Solutioning", gates A0-A5, A3 = human decision. I'll frame the route in these terms: this is a feature-level change that reuses the parent initiative's machinery but introduces a new AD (AD-009) and a new entity → requires the same solutioning rigor for the new sub-domain: new ADR, spec delta, contract deltas, NFR delta, RFP delta, and a human A3-style decision (regulatory + vendor capability + product scope).

Let me write it now.

Let me write the full design.md.

  `run_shell_command(command="cd <HARNESS>/runs/cells/openspec-r1/ws && openspec instructions tasks --chang, description="Get tasks artifact instructions")`

Now tasks.md. Let me get the instructions for tasks.

  `write_file(content="# Tasks\n\n## 1. Человеческое решение (гейт, аналог A3)\n\n- [ ] 1.1 Зафиксировать решения из `design.md` → «Open Questions» (регуляторная , file_path="<HARNESS>/runs/cells/openspec-r1/ws/openspec/changes/add-recurring-debits/tas)`

Now write tasks.md. The design's Open Questions are all human decisions that change the spec/approach — but they're flagged as "requires human decision before implementation" and don't need to be resolved to write the task list (they're the point of deliverable 7; the tasks should include a first task that gates on them). Actually, the instruction says "check design.md for Open Questions. If any of them would change what gets built, resolve them with the user first - do not bake an unstated assumption into the task list."

But these open questions are exactly the deliverable the user asked for ("что остаётся на решение человека-архитектора"). They're NOT things I should resolve now via ask_user_question — they're the output of the architectural package, meant to be resolved at the human architecture decision gate. So I should NOT bake assumptions into tasks, but I CAN structure tasks so that the first task is the human decision gate (like A3), and subsequent protocol-dependent tasks are marked as gated on `[ТРЕБУЕТ ПРОВЕРКИ]`.

Actually, the instruction is about "resolve them with the user first" if they'd change what gets built. But the whole point here is that the user (the architect) WILL resolve them, and asked me to enumerate them. The task list should reflect that the protocol-specific implementation is gated on НСПК documentation (external input), which is consistent with the existing repo pattern (walking skeleton uses mock adapter, real protocol NOT implemented).

So I'll write tasks that:
1. Gate on the human decisions (task 1.x: fix decisions, ratify AD-009).
2. Extend contracts (API ТСП, adapter ОПКЦ, RFP).
3. Extend state machine (consent FSM + paymentType=RECURRING branch).
4. Implement consent API + idempotency.
5. Implement debit initiation + consent validation (AD-009).
6. Mock adapter extensions (consent + debit events).
7. Notifications/webhooks + reconciliation.
8. NFR tests + fitness tests + acceptance.

Each task with verification.

Let me write tasks.md following the template exactly (checkbox format).

Let me write it.

  `run_shell_command(command="cd <HARNESS>/runs/cells/openspec-r1/ws && openspec validate --change \"add-re, description="Validate change and show final status")`

All artifacts created: proposal, specs (consents + recurring-debits), design, tasks. Now let me validate the change and show final status.

  `run_shell_command(command="cd <HARNESS>/runs/cells/openspec-r1/ws && openspec validate \"add-recurring-d, description="Validate the change (normal and strict)")`

The status shows all 4 artifacts complete. The validate command used the wrong flag. Let me check the correct validate syntax. Actually, `openspec validate` with `--change` is wrong. Let me run the correct validate. Let me check `openspec validate --help` or just run `openspec validate add-recurring-debits`.


Пакет изменения подготовлен и валиден (обычная и strict-проверка — PASS).

## Что сделано

Создал архитектурный пакет поверх принятого решения по методике OpenSpec (spec-driven), как принято в репозитории. Change: `add-recurring-debits` в `openspec/changes/add-recurring-debits/`.

| Файл | Содержит |
|---|---|
| `proposal.md` | Why/What, значимость и маршрут (кратко), новые capabilities, влияние, обратная совместимость |
| `specs/consents/spec.md` | Жизненный цикл согласия: создание→подтверждение→отзыв→истечение, идемпотентность, аудит ПДн |
| `specs/recurring-debits/spec.md` | Дебит по согласию: инициация без QR, инвариант «только активное согласие», зачисление из `PAID`, возврат-сага, сверка, уведомление плательщика |
| `design.md` | Оценка значимости/маршрута, таблица влияния на AD-001…008, 4 решения (D1–D4) с альтернативами/последствиями/обратимостью, конкретная дельта `openapi/tsp-api.yaml` и `opkc-adapter.md`, новые NFR, риски, план отката, критерии приёмки, открытые вопросы для человека-архитектора |
| `tasks.md` | 8 групп задач с проверками (гейт A3-решения, контракты, машины состояний, ядро, моки, нотификации/сверка, NFR/fitness/приёмка) |

## Ключевые архитектурные выводы

- **Маршрут**: высокая значимость (≈10/15), «глубокое проектирование под-домена» — новый финансовый объект + новый инвариант, а не малое изменение. Родительский spine (C2B-приём) не меняется.
- **Инварианты**: AD-002/003/007 расширяются; для AD-005 появляется аналог — новый инвариант «дебетование только по активному согласию» (проект AD-009, требует ратификации). AD-001/004/006/008 — без изменения принципа.
- **Главное решение (D1)**: `Согласие` — отдельная сущность со своей машиной; дебит — `Payment` с `paymentType=RECURRING` + `consentId`, переиспользуя зачисление/возврат/сверку (минимум нового кода, аддитивно, reversible).
- **Контракт**: только аддитивно под `/v1` (новые `/v1/consents` + опциональные поля), существующие C2B-QR потребители не ломаются.

## Осталось на человека-архитектора (deliverable 7)

1. Семантика рекуррентного сервиса НСПК (формат согласия, канал подтверждения) — внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`.
2. Регуляторная модель (отзыв, уведомления, лимиты, окно возврата) — ИБ/комплаенс.
3. Поддержка вендором ОПКЦ рекуррентного сервиса (или новый раунд RFP).
4. Ратификация нового spine-инварианта «дебетование только по активному согласию».
5. Продуктовые лимиты по сегментам (кинотеатры/ЖКХ/связь).

Пакет готов к ревью. Для передачи в работу — `/opsx-apply` или попросите меня применить изменение (в этой фазе я код не писал и принятые файлы решения не менял).
