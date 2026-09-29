<!-- источник: <HARNESS>/runs-v2.1/cells/w79dnbp/home/.qwen/projects/-home-architect-project/chats/1ba68896-7fab-43a5-896f-79a54b710079.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `read_file(file_path="/home/architect/project/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="/home/architect/project/README.md")`
  `read_file(file_path="/home/architect/project/.arch-handoff/TASK.md")`
  `read_file(file_path="/home/architect/project/.arch-handoff/MANIFEST.json")`

I'll start by exploring the repository structure and understanding the established conventions, then check for project-specific skills and tools.

  `read_file(file_path="/home/architect/project/docs/solutioning.md")`
  `read_file(file_path="/home/architect/project/docs/nfr.md")`
  `run_shell_command(command="find /home/architect/project/openspec /home/architect/project/.qwen /home/architect/project/docs /home/architect/project/openapi -type f | , description="List all files in key directories")`

Let me explore the docs directory, the openspec directory, and skills/commands.
Now let me read the core design documents and check the OpenSpec workflow setup.

  `read_file(file_path="/home/architect/project/openspec/config.yaml")`
  `read_file(file_path="/home/architect/project/.qwen/skills/openspec-propose/SKILL.md")`
  `read_file(file_path="/home/architect/project/.qwen/commands/opsx-propose.md")`
  `read_file(file_path="/home/architect/project/docs/contracts/tsp-api.md")`

This is an OpenSpec project. The task is to prepare an architectural package for a change (recurring C2B payments / SBP subscriptions) on top of the accepted decision. The right tool is the OpenSpec propose workflow (`openspec-propose` skill / `opsx-propose` command).

Let me read the OpenSpec config, the skills, and remaining docs.
This is an OpenSpec-managed project. Let me read the OpenSpec config and the propose workflow skill, plus remaining contracts.

  `read_file(file_path="/home/architect/project/docs/spec/state-machine.md")`
  `read_file(file_path="/home/architect/project/openapi/tsp-api.yaml")`
  `read_file(file_path="/home/architect/project/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="/home/architect/project/.arch-handoff/CONSTRAINTS.yaml")`

Now let's read the ADRs, the state machine, opkc-adapter, the openapi spec, the handoff files (CONSTRAINTS, RUBRIC, ARCHITECTURE), and the docs/nfr. Let me also check openspec CLI availability.

Let me batch read.
Let me read the ADRs, state machine, openapi contract, and the handoff/rubric files.

  `read_file(file_path="/home/architect/project/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="/home/architect/project/docs/adr/ADR-005-integraciya-s-abs-zachislenie-po-podtverzhdyonnomu-statusu-vozvraty-kak-saga.md")`
  `read_file(file_path="/home/architect/project/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="/home/architect/project/.arch-handoff/ARCHITECTURE.md")`
  `run_shell_command(command="cd /home/architect/project && openspec --version 2>&1; echo \"---\"; openspec context --json 2>&1 | head -50; echo \"---LIST---\"; openspec, description="Check OpenSpec CLI and project root")`

Now let me read the ADRs (particularly ADR-005, ADR-007), the opkc-adapter contract, .arch-handoff/ARCHITECTURE.md, and check the openspec CLI.

Let me batch.
Now let me read the ADRs, OPKC adapter contract, handoff architecture, and verify the OpenSpec CLI.

  `read_file(file_path="/home/architect/project/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="/home/architect/project/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="/home/architect/project/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="/home/architect/project/docs/rfp/vendor-rfp.md")`
  `run_shell_command(command="ls -la /home/architect/project/.arch-handoff/adr/ 2>&1; echo \"---\"; cd /home/architect/project && git log --oneline -10", description="List handoff adr dir and git log")`

Good. OpenSpec is set up, no changes yet. Now I understand the project deeply. Let me check the remaining ADRs briefly (ADR-001 outbox, ADR-003 mtls, ADR-004, ADR-006) — I mostly have their content via the ARCHITECTURE.md digest but let me read ADR-004 and ADR-006 quickly and the remaining ones, plus vendor RFP. Actually I have enough of the gist. But to write an accurate design, I should know ADR-003 and ADR-004 details. Let me read them.

Also important: the user asks about "рекуррентные C2B-списания по согласию плательщика — подписки СБП". In SBP, this is actually... There's a real thing: СБП подписки / "СБП recurrent payments"? Actually in the Russian market, there are "автоплатежи СБП" / "подписки" via SBP - the mechanism is that the payer gives consent in their bank app (in the СБП app), and then the merchant can initiate payments without the payer's action. Actually I recall "СБП: автоплатежи" — the payment is initiated by the merchant via ОПКЦ using a "СБП ID"/token obtained with the payer's consent. There's an СБП "подписка" scenario where the payer scans once and confirms recurring mandate.

Now, the task is explicitly: prepare architectural package for this change over the accepted decision. This is an OpenSpec propose workflow. The user references skills/tools — "методические навыки и инструменты" — the opsx skills.

So the right approach: run the `openspec-propose` workflow (skill). It's an explicit OpenSpec project. The user didn't explicitly say "openspec propose" but the project uses OpenSpec as the accepted method ("Принятые файлы решения меняй только тем способом, который принят в этом репозитории"). The OpenSpec workflow is the accepted way to change the decision. So I should use the openspec-propose skill.

Let me invoke the skill. Actually, I should first clarify material ambiguity? The skill says ask if ambiguity materially affects scope. Let me think about what's ambiguous:

1. Is the change in scope for the current accepted decision, or a new adjacent capability? The user says "поверх принятого решения" — on top of the accepted decision.
2. Key ambiguity: does the change include the full mandate lifecycle (mandate registration/consent, recurring debit initiation, revocation, limits), and what's the consent mechanism? But this is architectural design — I can propose.
3. Whether it's a new OpenSpec change (separate from the existing walking skeleton handoff) — yes, clearly.

Given the instruction: "Для minor details make reasonable assumptions and record them." The user wants a full package. Ambiguity that matters: the change name and the consent model (СБП "подписки" token vs. bank-side mandate). But these are things I should design as alternatives.

However, there's one genuinely material question: is the payer consent obtained via СБП (ОПКЦ-issued token, "СБП-подписка") or via the bank's own channel? This affects whether ОПКЦ adapter contract changes and whether we need a new external input. Since НСПК protocol is [ТРЕБУЕТ ПРОВЕРКИ] anyway, I can treat both as variants.

I think I should ask 1-2 clarifying questions per the skill: material ambiguity affecting scope. Actually, let me consider whether asking is worthwhile. The user gave a very detailed set of deliverables and expects an autonomous architectural package. Over-asking could annoy. But the skill explicitly says ask about material ambiguity. Let me ask a focused set of questions — maybe 2-3 — via ask_user_question. Hmm. But the user's prompt is quite prescriptive; they want an architectural package. The main material ambiguity: 

(a) Change granularity: one change "sbp-subscriptions" vs. split. 
(b) Whether mandate/consent storage and the "СБП token" model is in scope.
(c) Whether the ОПКЦ adapter contract (vendor) must change → affects RFP.

Actually I think the most material ambiguity is scope depth: does the deliverable include changes to the accepted decision files themselves (spine/ADR) as new ADRs, or only planning artifacts? The user says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — meaning change accepted decision files only via the accepted method. In OpenSpec, changes are proposed as delta artifacts; spine/ADR updates happen through... hmm. The repository uses both OpenSpec (proposal/specs/design/tasks) and the arch documents (ARCHITECTURE-SPINE.md, docs/adr/). The accepted method for changing the decision: I think OpenSpec change + new ADR proposals. The handoff RUBRIC suggests a workflow.

Let me read the opsx-explore and opsx-update to understand the accepted method for changing accepted artifacts. Also let me check docs/adr/ADR-006 and 004 and the vendor-rfp.

Actually, let me be efficient. I'll read the remaining ADRs and the opsx-propose command is already known. Let me also check whether there's a convention like a "handoff" regeneration. Let me look at .arch-handoff/adr/ directory.

From the earlier find, .arch-handoff/adr/ exists but contained "..." in the initial listing. Let me list it.

Let me batch: read ADR-003, ADR-004, ADR-006, ADR-001 (already have digest but ok), list .arch-handoff/adr, read vendor-rfp.

Given the size, let me focus: I need enough to write good artifacts. Let me read ADR-004 (notifications), ADR-006 (trust), and list handoff dir.

Actually the key design question: recurring SBP payments. Let me think about the domain properly since I need to produce real architecture.

**Domain: СБП рекуррентные платежи / подписки**

Real-world СБП C2B mechanisms (as of 2024-2025): НСПК introduced "СБП-подписки" / "регулярные платежи СБП". The mechanism (per public sources): The payer, in their bank app, when paying via SBP, can save the payment as a recurring/subscription — issuing a "токен подписки" / "идентификатор подписки" (СБП ID / subscriptionId). The merchant (ТСП) then initiates subsequent charges by referencing this token via ОПКЦ, and the payer's bank can either auto-debit or require confirmation depending on the amount/limits/risk. НСПК roles: ОПКЦ stores the subscription; the payer can revoke consent in their bank app.

Key architectural implications:
1. New entity: **подписка/мандат (mandate)** with its own lifecycle: DRAFT/REGISTERING → ACTIVE → SUSPENDED → REVOKED/EXPIRED. It binds payer, ТСП, limits (max per charge, max total, period), currency, purpose.
2. New operation: **charge (списание по подписке)** — initiated by ТСП without payer action; goes through the same PAID-gated crediting path.
3. Consent/revocation: payer revokes in their bank app → ОПКЦ notifies merchant/gateway (event). This is a new async event from ОПКЦ: `subscription.revoked`.
4. Idempotency: each recurring charge needs its own idempotency key (chargeId) derived from mandate + billing period/order.
5. New regulatory dimension: mandate scope + revocation must be auditable; consumer protection (право на отзыв согласия); limits; НСПК rules on recurring.
6. АБС impact: same crediting path — no change to AD-005; but possibly need to handle "charge without prior QR".
7. Contract changes: new endpoints for mandates (create mandate registration → returns consent link/QR for payer), charge creation, mandate status/list, revocation; new events `subscription.*`; backward compatible (additive).
8. New invariant needed? "Списание по подписке возможно только из ACTIVE-мандата с действующим согласием и в пределах лимитов" — analogous to AD-005. And "мандат — единый источник истины", "отзыв согласия немедленно блокирует новые списания". These would be new spine invariants AD-009, AD-010 (proposed).

Also: mandates can be created only via payer action (consent), so there's a new flow: ТСП creates "mandate registration" → gateway asks ОПКЦ → returns a QR/link → payer confirms in bank app → ОПКЦ notifies `subscription.activated` → mandate ACTIVE.

Also no-payment-without-consent: the first charge might be the consent payment (СБП requires an initial payment? In some models the subscription is registered during a first payment). This is a material design variant: **registration via first payment (связанная подписка при первой оплате)** vs **standalone mandate registration (без списания)**. That's a real alternative to consider.

Also **amount confirmation model**: СБП may require payer confirmation per charge above a threshold ("с подтверждением плательщика") vs silent auto-debit. This affects UX/NFR and status machine (new state CHARGE_PENDING_CONFIRMATION?). Real НСПК subscriptions: there's a limit up to which debiting happens without confirmation, and larger amounts need confirmation in the bank app.

OK. This is rich. I'll design it as:

- New capability delta specs: `sbp-subscriptions` (mandate lifecycle), `recurring-charges` maybe combined; `tsp-api` modifications (contract).
- design.md with alternatives: (a) consent model — standalone mandate vs first-payment-linked; (b) where mandate state lives — gateway as source of truth vs ОПКЦ as authority (hybrid with reconciliation); (c) charge initiation — merchant-pull via ОПКЦ token vs bank-side scheduled pull; (d) auto-debit vs confirm-each.
- proposal.md with route significance assessment (significance score).
- tasks.md.

The user also asks for items 1-7 specifically. The OpenSpec artifacts map:
1. Significance/route → proposal.md (Why, impact) + design.md
2. Impact on architecture / invariants → design.md (ChangeImpact/Context) + proposal
3. ADR with alternatives/consequences/reversibility → design.md decisions + new ADR proposal(s). Hmm — should I create new ADR files in docs/adr/? The accepted method for changing the decision: In this repo, ADRs live in docs/adr/ and spine in ARCHITECTURE-SPINE.md. "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." 

What is the accepted way? The repo has OpenSpec + the arch docs. The task says "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям." So the package is a proposal to be taken to a human architectural decision (A3-like gate), then handed to implementers. So we should NOT edit accepted files (spine, existing ADRs) directly — instead propose. But "меняй только тем способом, который принят" — the accepted way in this repo for a change to the decision seems to be via OpenSpec change (proposal/specs/design/tasks) plus ADR proposals.

Hmm, but the deliverable 3 says "Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью" — that's an ADR. And deliverable 4 "Изменения контрактов (openapi/tsp-api.yaml)". So the user does expect concrete file changes: openapi/tsp-api.yaml updated. And ADRs. And NFR. And acceptance criteria + rollback.

So the package likely should:
- Create an OpenSpec change (`sbp-recurring-payments` or `sbp-subscriptions`) with proposal.md, specs deltas, design.md, tasks.md.
- Add proposed ADRs (e.g., ADR-008 mandate model, ADR-009 ...). But changing spine requires ratification. The spine says "Статусы: блоки в статусе Proposed действуют после ратификации соответствующего ADR." So new spine blocks AD-009+ proposed, new ADR files Proposed status. That's the accepted method: propose ADRs, don't ratify.
- Update openapi/tsp-api.yaml additively (new paths/schemas) — it's v0.1 draft, so extending is fine; but "без поломки существующих потребителей" — additive only.
- New NFR entries (docs/nfr.md) — but docs/nfr.md is an "accepted" file? It's baseline. Could add a section for new functionality. Hmm, "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." Editing docs/nfr.md additively is probably fine, or better: put NFRs in the OpenSpec spec delta (specs/nfr or in the capability spec with measurable requirements). 

I need to be careful: OpenSpec propose workflow says "Do not edit project code" and planning artifacts only. Does editing docs/* and openapi/* count as project code? The workflow says "Do NOT implement the change, start the apply workflow, or edit project code during this workflow." The openapi contract is arguably part of planning/spec (contracts are design artifacts). Hmm. But the OpenSpec guardrail is about not implementing.

The user explicitly wants deliverable 4 = changes to openapi/tsp-api.yaml. So I should update it. That's a spec artifact, planning-level.

I think the cleanest: use OpenSpec propose to create the change with artifacts, where the specs delta includes the TSP API contract changes, and also directly update openapi/tsp-api.yaml (the contract file is a planning artifact that the repo maintains alongside docs/contracts/tsp-api.md). And add proposed ADR files + spine entries (as Proposed, unratified).

But wait — should I decide schema? config is spec-driven. Good.

Let me consider the ambiguity questions to ask the user. The skill says ask about material ambiguity. I think there are 2 genuinely material ones:

Q1: Consent/mandate model — how is the subscription registered? Options: (a) standalone mandate registration (payer confirms in bank app, no charge) — this is the "СБП-подписка" proper; (b) first payment linked (mandate created as part of an initial payment); (c) both. This affects contracts and state machine. However, as an architect I can present this as alternatives in design.md and make a recommendation. The task explicitly wants "рассмотренными альтернативами". So maybe I shouldn't ask — I should analyze. 

Q2: Scope of the change: only merchant-initiated recurring C2B charges, or also payer-initiated/scheduled? The business says "ТСП просят рекуррентные C2B-списания по согласию плательщика — подписки СБП". So merchant-initiated (pull) recurring. Clear enough.

Q3: Is this a new OpenSpec change separate from the ongoing walking skeleton handoff? Yes.

Q4: Where consent is captured / whose app: СБП app / payer's bank. External input.

Hmm, I think the user wants me to produce the package, not to be interrogated. But the skill mandates asking on material ambiguity. Let me ask a small number of high-value questions. Actually — the risk: the user is testing whether the agent follows the methodology (uses opsx skills) and produces the package. A clarifying question about scope depth is reasonable.

Let me identify truly decision-changing ambiguities where a wrong assumption wastes the whole package:

A. **Регуляторный/протокольный статус механизма**: рекуррентные СБП-списания (подписки) — это подтверждённая возможность ОПКЦ, или гипотеза? In reality НСПК has this. But если механизма нет, весь пакет — другое. Since protocol is [ТРЕБУЕТ ПРОВЕРКИ] anyway, treat as external input.

B. **Change granularity**: one epic vs. split into (consent/mandate) + (recurring charges). Material for tasks and gates.

C. **Whether to modify accepted files (spine/ADR) now or only propose.** User said "меняй только тем способом, который принят" — so propose. I'll propose new ADRs and spine additions marked Proposed, not edit existing ADRs. But I might need to edit the spine to add proposed blocks. Is adding Proposed blocks to spine "changing accepted files"? The spine already contains Proposed blocks awaiting ADR ratification, so the accepted method includes adding Proposed blocks. I'll do that, carefully and additively, marking clearly.

Hmm, actually — re-reading: "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение". So the package is for a decision meeting. The decision (A3-like) hasn't happened for this change. So everything new should be Proposed. I should NOT ratify. I can add proposed ADR files and proposed spine blocks. That matches the repo's convention (ADR-007 was "proposed-a3" then Accepted after A3).

Let me ask the user 2 questions to nail scope:
1. Объём изменения / глубина: (a) полноценный архитектурный пакет с новыми ADR и правками документов решения + OpenSpec-изменение (recommended); (b) только OpenSpec-изменение (proposal/specs/design/tasks) без правки docs/ADRs/spine; (c) другое.
Actually the user already enumerated deliverables 1-7 which include ADR, contracts, NFR, acceptance/rollback. So (a) is clearly intended. Asking is somewhat pointless.

2. Модель согласия (мандата): (a) отдельная регистрация подписки без первого платежа; (b) подписка оформляется при первой оплате; (c) обе; (d) решает архитектор — рассмотреть как альтернативы. The task says "рассмотренными альтернативами" so (d)/present alternatives is acceptable. But knowing business preference helps recommend.

I think a good approach: ask 1-2 questions max, focused on the things that materially change the artifacts, and offer "рассмотреть как альтернативы" as an option. This respects both the skill and the user.

Actually, let me reconsider. The user's message is a detailed work order. They likely want execution. The skill says: "If the request contains ambiguity that would materially affect scope, externally observable behavior, compatibility, or acceptance criteria, ask the user before creating the change." I'll ask one consolidated question set (2 questions) — the consent model and whether to also produce proposed ADR/spine edits + contract file edits. Hmm, but the latter is answered by deliverables.

Let me ask about:
- Q1: Change packaging — one OpenSpec change for the whole feature vs. split into two changes (consent/mandate + recurring charges). Material for tasks/gates.
Hmm, that's a bit process-y; I could just decide (one change with multiple capabilities, since it's one business initiative and the mandate is a prerequisite).

- Q1 (real): Модель оформления подписки: standalone consent vs. first-payment-linked vs. both → affects contract & state machine.
- Q2 (real): Подтверждение каждого списания: silent auto-debit within limits vs. per-charge confirmation above threshold vs. configurable per mandate. Affects state machine, NFR, payer UX.

These two are genuinely material and architecturally interesting. I'll ask these, plus maybe a third about sources of truth for mandate (gateway vs ОПКЦ). Actually Q3 relates to deliverable "альтернативы" — I'll analyze it.

Actually — better: I'll ask and offer the option "рассмотреть оба варианта как альтернативы в design.md" so the user can delegate. Let me ask 3 questions in one call.

Wait, but there's a risk the user just wants me to go. Let me keep it to 2-3 crisp questions with recommended options. This is within guidance.

Hmm, let me reconsider once more. The instruction in the system prompt: "Confirm Ambiguity/Expansion: Do not take significant actions beyond the clear scope of the request without following the active interaction mode's question guidance. If asked how to do something, explain first, don't just do it." And "Use ask_user_question when you need clarification or want to validate assumptions."

I'll ask. But I should first do enough research to ask good questions. I've done research. Let me also quickly read ADR-004 and ADR-006 and the vendor-rfp to ground. And check .arch-handoff/adr dir. Let me do that before asking, so I don't need another round.

Let me batch read.
Let me read the remaining ADRs and RFP to ground the design before proposing.

  `ask_user_question(questions=[{"question": "Как оформляется согласие плательщика (мандат подписки)? Это определяет контракт, статусную машину и первую бизнес-операцию.",)`

I now have a complete picture. Let me check if there's a project methodology skill beyond opsx — maybe there's an "arch" skill mentioned (`.arch-handoff/` rules mention `arch control check`). Let me check for any `arch` CLI or skills in ~/.qwen. The available skills listed are bundled + openspec project skills. No "arch" skill. But there might be commands. Let me check .qwen/commands — only opsx-*. And check for AGENTS.md/QWEN.md.

Let me quickly check for QWEN.md / AGENTS.md and any `arch` tool.

Actually the system reminder says skills available: agent-delegation, batch, browser-use, computer-use, dataviz, extension-creator, goal-draft, loop, new-app, openspec-*, qc-helper, review, simplify, stuck, workflow-authoring, workflow-creator. And opsx-*. No "arch" skill. The `.arch-handoff` is a handoff package with rubric/constraints, not a tool.

So the methodology tool = OpenSpec (`openspec-propose`). Good.

Now, the deliverable map to OpenSpec:
- proposal.md — significance/route assessment (item 1) + what/why + impact summary (item 2)
- specs/<capability>/spec.md delta — requirements incl. NFR (item 5), acceptance criteria (item 6)
- design.md — architecture decision with alternatives, consequences, reversibility (items 2,3,7), contract changes (item 4)
- tasks.md — implementation steps + rollback plan tasks (item 6)

Plus separately:
- docs/adr/ADR-008, ADR-009 (new proposed ADRs) — item 3 properly as ADRs
- ARCHITECTURE-SPINE.md — add proposed AD-009/AD-010 (new invariants)
- openapi/tsp-api.yaml — additive contract changes (item 4)
- docs/nfr.md — new measurable NFRs (item 5)
- docs/spec/state-machine.md — new states/transitions (or put in delta spec)
- docs/contracts/opkc-adapter.md — new adapter operations/events (mandate)
- docs/contracts/tsp-api.md — contract doc update

Hmm, that's a lot. But the user asked for an "architectural package". Should I update docs/contracts/tsp-api.md too (the .md, alongside openapi yaml)? The openapi is the machine contract; the .md is the human contract. Deliverable 4 says only `openapi/tsp-api.yaml`. So I'll update the yaml, and reference the delta spec. Maybe also update the .md for coherence—but the user said "изменения контрактов (openapi/tsp-api.yaml)". I'll focus on the yaml and describe changes in design/spec. Actually, to be a coherent package, updating docs/contracts/tsp-api.md would be good. But it risks scope creep. Hmm.

Let me reconsider the framing: The user wants (a) an architectural package to take to an architectural decision, and (b) then hand to implementers. The repo's accepted method for change = OpenSpec change + proposed ADRs/spine (Proposed, awaiting ratification). So:

Deliverables:
1. OpenSpec change `sbp-recurring-payments` (or `sbp-subscriptions`) with 4 artifacts. This is the core package (items 1-7 all captured).
2. New proposed ADRs: ADR-008 (Модель подписок/мандатов и согласия), ADR-009 (Порядок списаний и подтверждений / лимиты). Or fold into one ADR-008 with alternatives. Maybe two ADRs: ADR-008 "Мандат-модель подписок СБП: источник истины, жизненный цикл, отзыв согласия"; ADR-009 "Инициирование рекуррентных списаний: pull-модель ТСП, лимиты и подтверждение плательщика". Hmm.
   Actually the design.md in OpenSpec already holds decisions with alternatives. The user separately asks for "Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью" — that's ADR-style. I'll produce ADR files (proposed) AND design.md. To avoid duplication, design.md can be the OpenSpec "how" and ADR-008/009 the ratified-form decision records. That's normal.

3. Spine additions AD-009/AD-010 (Proposed).
4. openapi/tsp-api.yaml additive extension.
5. docs/nfr.md new section.
6. docs/spec/state-machine.md new mandate state machine + new payment states? Maybe add a new file docs/spec/mandate-state-machine.md instead of editing. Hmm. Better: add `docs/spec/subscription-state-machine.md` (new file) and reference. Keeps accepted file untouched.

Wait — but "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." Which files are "принятые файлы решения"? ARCHITECTURE-SPINE.md, docs/adr/*, docs/solutioning.md, docs/nfr.md, docs/contracts/*, docs/spec/*, openapi/*. The accepted way to change: add Proposed blocks / proposed ADRs, per the spine's own status system. And OpenSpec for the change. I think:
- ARCHITECTURE-SPINE.md: append new Proposed invariants (AD-009, AD-010) and note in "Deferred" that автоплатежи move from deferred roadmap into scope. Actually the spine's deferred list says "автоплатежи" — wait, solutioning.md §1 says roadmap (вне scope): C2C, выплаты, диспуты, автоплатежи. And spine Deferred doesn't mention autopayments explicitly but mentions C2C/B2C. So this change pulls "автоплатежи" (recurring) from deferred into scope. That's a key impact: deferred item reactivated. Good — I must note that.
- docs/nfr.md: additive section (baseline doc, additive is safe).
- openapi/tsp-api.yaml: additive.
- New ADRs: docs/adr/ADR-008-....md, ADR-009-....md (Proposed).
- New spec files: docs/spec/mandate-state-machine.md maybe; and docs/contracts/opkc-adapter-subscriptions.md? Or extend existing contracts via additive section.

Hmm, I'm at risk of over-producing. Let me scope tightly to the 7 deliverables and the "architectural package" purpose, and keep the repo's conventions:

**Package contents (final):**
1. `openspec/changes/<name>/proposal.md` — items 1, 2 (significance/route, impact, invariants touched, what changes/doesn't).
2. `openspec/changes/<name>/specs/<capability>/spec.md` (delta) — items 5, 6 requirements (NFR measurable + acceptance criteria + rollback requirements). Possibly multiple capabilities: `sbp-subscriptions` (mandate lifecycle + consent) and `tsp-api` (contract delta). Let me see schema instructions first.
3. `openspec/changes/<name>/design.md` — items 2,3,4,7 (decisions/alternatives/consequences/reversibility, contract delta, open human decisions).
4. `openspec/changes/<name>/tasks.md` — implementation + verification + rollback steps.
5. `docs/adr/ADR-008-...md` (Proposed) — mandate/consent model. Maybe ADR-008 & ADR-009.
6. `ARCHITECTURE-SPINE.md` — add AD-009/AD-010 Proposed + note deferred reactivation.
7. `openapi/tsp-api.yaml` — additive extensions.
8. `docs/nfr.md` — new measurable NFR section for subscriptions.
9. New: `docs/spec/mandate-state-machine.md` — mandate lifecycle (analogous to state-machine.md). This is a real needed artifact.
10. Update `docs/contracts/opkc-adapter.md` additively? The mandate registration/token is an ОПКЦ capability → adapter contract must gain methods/events. This is material. I'll add a new section (additive) — "§10 Подписки (рекуррентные платежи) — расширение контракта" or a separate file `docs/contracts/opkc-adapter-subscriptions.md`. Hmm.

Hold on. Let me reconsider: maybe I'm overcomplicating. The user says "Код не пиши" and asks for an architectural package. The OpenSpec propose flow produces the package. The extra doc edits (spine, ADR, openapi, nfr) are what makes it a full architectural package. I'll do them but keep them tight and additive.

Actually — important nuance. In this repo, the OpenSpec `openspec/specs/` is EMPTY (only .gitkeep). So there are no main specs; the "specs" live in docs/. The OpenSpec change delta specs would be the first specs. Hmm, that's interesting: the repo's real specs are docs/spec and docs/contracts. OpenSpec is set up but unused. So "принятый в репозитории способ" for a change = OpenSpec (the tooling installed) — and the openspec-propose skill exists precisely for that.

Given the project config context says language ru and OpenSpec structural headings in English.

Now, decision on ambiguous material points. Let me ask the user a focused question. Given the depth, I'll ask about:

1. Consent/mandate registration model (standalone vs first-payment-linked vs both) — materially changes contract & state machine.
2. Per-charge confirmation model (silent within limits vs confirm each vs configurable) — materially changes state machine & NFR.
3. Possibly: scope of the package — do they want me to also update accepted docs (spine/ADR/openapi/nfr) or only produce the OpenSpec change. 

Hmm, #3: The user's deliverables 4,5,6 require changing contracts and NFR. And item 3 requires an ADR. So they clearly want the docs updated. I won't ask #3.

But wait — maybe I should ask whether they want me to add new ADRs to docs/adr/ (making it ADR-008/009) vs just design.md. The user says "Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью" — the repo's form for that is ADR. So yes.

Alternatively, I could avoid asking entirely and present alternatives in design.md (which satisfies "рассмотренными альтернативами"). The user might appreciate autonomous execution. But the skill mandates asking when material. The consent model is material and the business may have a preference (it affects payer UX and contract). I'll ask 2 questions with a recommended option, and include "рассмотреть как альтернативы" implicitly by making options that include "оба/конфигурируемо".

Let me ask 3 questions:
Q1 (Модель оформления подписки): (a) Отдельная регистрация мандата без первого платежа (Recommended); (b) Подписка оформляется при первой оплате; (c) Обе модели — как альтернативы в design.md.
Q2 (Списание): (a) Тихие списания в пределах лимитов мандата + подтверждение сверх порога (Recommended); (b) Всегда подтверждение плательщика; (c) Всегда тихо; (d) рассмотреть как альтернативы.
Q3 (Где источник истины по мандату): (a) Шлюз — источник истины, ОПКЦ — сверка (Recommended); (b) ОПКЦ — авторитет, шлюз кэширует; (c) рассмотреть альтернативы.

Hmm Q3 is quite architectural. Maybe fold into alternatives myself. I'll ask Q1 and Q2 only, plus maybe a scope question about whether to include payer-side revocation flow in scope (it's necessary).

Actually, let me limit to 2 questions to keep momentum. And I'll present Q3 as an alternative in design.md.

Hmm, wait. Let me reconsider whether to ask at all. Re-reading the user's task: "Архитектурное решение с рассмотренными альтернативами" — they explicitly want alternatives analyzed. Asking "which alternative" partially defeats that. But knowing the business constraint reduces rework. I think asking is net-positive and aligned with the skill. I'll ask 2 crisp questions.

Let me also consider: the changes name. I'll derive `sbp-subscriptions` or `sbp-recurring-payments`. Russian context: "подписки СБП". I'll use `sbp-recurring-payments`.

Let me first check the schema/instructions to know capability paths. I'll run `openspec new change` after the questions. But I can pre-check instructions with a placeholder? No — instructions need a change. Let me check `openspec schemas --json` to see templates. Actually let me just ask questions first (parallel with nothing). Then create.

Let me ask the questions now.

Actually, I realize I should be careful about the user's phrase: "методические навыки и инструменты — используй их по назначению." → clearly hints at opsx skills. Good, I'll use openspec-propose.

Let me ask the clarifying questions. I'll do it in Russian (output language = user's language = Russian).

One more consideration: should I enter plan mode? No — the user didn't ask, and the opsx-propose workflow is the plan. Don't enter plan mode on my own.

Let me ask.
I've now mapped the accepted solution (spine AD-001…AD-008, ADR-001…007, contracts, state machine, NFR, handoff) and confirmed the project's methodology tooling: OpenSpec (`openspec` 1.13.2) with the project `opsx-*` skills, and the arch-handoff package with fitness rules. That is the accepted way to change the decision here.

Two points materially shape scope, contracts and the state machine, so let me confirm them before drafting.

  `run_shell_command(command="cd /home/architect/project && openspec new change \"sbp-recurring-payments\" 2>&1; echo \"=== STATUS ===\"; openspec status --change \"sbp-, description="Create OpenSpec change and read status")`

The user chose: standalone mandate registration, and silent within limits + confirmation above threshold.

Now I'll run the OpenSpec propose workflow. Per the skill: load context (done), determine schema (default spec-driven, no --schema), create change, get status, create artifacts.

Change name: `sbp-subscriptions` or `sbp-recurring-payments`. I'll use `sbp-recurring-payments`.

Let me create the change and get status.
Decisions recorded: standalone mandate registration; silent charging within mandate limits, payer confirmation above threshold. Now I'll create the OpenSpec change and generate its artifacts.

  `run_shell_command(command="cd /home/architect/project && openspec instructions proposal --change \"sbp-recurring-payments\" --json 2>&1", description="Get proposal artifact instructions")`

Now get instructions for proposal.

  `run_shell_command(command="cd /home/architect/project && openspec list --specs --json 2>&1", description="List existing spec inventory")`

There are no existing specs (openspec/specs empty). Let me verify: `openspec list --specs`. Let me also check the specs instruction to know capability path conventions. But first, note: the repo's real spec organization is `docs/spec/` and `docs/contracts/`, but OpenSpec specs dir is empty. The instruction says "follow the project's existing spec organization" and "Use the exact existing path under openspec/specs/". Since none exist, I define new capabilities.

Let me check `openspec list --specs --json`.

I'll design capabilities:
- `sbp-mandates` (new): mandate lifecycle, consent, revocation, limits — the payer consent capability.
- `sbp-recurring-charges` (new): recurring charge initiation, silent/confirm, crediting.
- `tsp-api` (modified?) — no existing spec, so it'd be new. Hmm, but the contract modification belongs to new capability spec or a delta on a new `tsp-api` spec. Since there's no main spec, "modified capabilities" must be empty (nothing exists). So I'll express contract changes within the new capabilities' specs plus design.md, and update openapi/tsp-api.yaml directly.

Actually, maybe cleaner: capabilities:
1. `sbp-mandates` — управление мандатами и согласием плательщика (registration, activation, revocation, limits, state machine).
2. `sbp-recurring-charges` — инициирование рекуррентных списаний ТСП (charge, silent/confirm, crediting through PAID path, idempotency).
3. `tsp-api-recurring` — the TSP contract delta (endpoints, events, error codes, backward compat). Hmm, is contract a "capability"? In OpenSpec, a capability = a behavior area. The TSP API contract is behavior for ТСП. I could name it `tsp-api-recurring` as a new capability.

Actually, let me fold the contract into the two capabilities to avoid over-splitting. The TSP API additions are: mandate endpoints (belong to sbp-mandates) and charge endpoints (belong to sbp-recurring-charges). That's clean. The design.md covers contract change approach + backward compat.

Hmm, but the contract file changes (openapi) are cross-cutting; spec deltas per capability can include "contract" requirements with SHALL statements. Good.

Let me define capabilities:
- `sbp-mandates`: жизненный цикл мандата/согласия, лимиты, отзыв, статусная машина мандата, идемпотентность регистрации, contract endpoints for mandates.
- `sbp-recurring-charges`: инициирование списания по мандату, тихое в пределах лимитов, подтверждение сверх порога, зачисление только из PAID (unchanged invariant), идемпотентность chargeId, вебхуки, contract endpoints for charges.
- Possibly `sbp-opkc-subscription-transport` — adapter contract delta for mandate registration/token and revocation events. Hmm. That's the vendor boundary — important for RFP. Could be a third capability `opkc-adapter-subscriptions`. But it's a contract, not user-facing behavior. I think putting adapter requirements in design.md + updating opkc-adapter.md doc is enough; but the spec delta is where requirements live. Since the vendor must implement new methods, it's arguably a capability. I'll include a third capability `opkc-subscription-transport` to capture vendor-facing requirements. Hmm — that might be over-engineering for OpenSpec specs. 

Let me keep 2 capabilities and cover the adapter boundary in design.md + docs/contracts/opkc-adapter.md update. Actually, the adapter requirements are testable behaviors ("адаптер SHALL идемпотентно регистрировать мандат по reference"). The vendor RFP needs them. I think 3 capabilities is defensible and thorough. But then tasks multiply.

Decision: 2 new capabilities (`sbp-mandates`, `sbp-recurring-charges`), and I'll add adapter-facing requirements into `sbp-mandates`/`sbp-recurring-charges` specs as they relate. Plus design.md handles the transport boundary. And I'll update docs/contracts/opkc-adapter.md additively to carry vendor requirements. That keeps OpenSpec lean while the arch package is complete.

Hmm, wait. Let me reconsider: the user wants this "вынести на архитектурное решение и затем передать исполнителям". The spec deltas are what implementers consume. The vendor adapter is a separate implementer (вендор). So a third capability `opkc-subscription-transport` genuinely helps handoff. I'll include it. Three capabilities:
1. `sbp-mandates`
2. `sbp-recurring-charges`
3. `opkc-subscription-transport`

Hmm, that's a lot of writing but it's the right thing. Let me be pragmatic: 2 core + cover transport in design and opkc-adapter.md doc. Actually you know, I'll include the transport capability because the ОПКЦ adapter is a key external boundary and the RFP needs requirements. Let me do 3.

Hmm, but each capability spec needs SHALL requirements with scenarios. Let me keep each focused with ~6-10 requirements.

Let me check list --specs first, then check the specs instruction.

Let me now write the proposal. Keep concise (1-2 pages).

Significance/route assessment (deliverable 1): The repo uses a significance score (11/15 → Critical). Need to assess for this change. Criteria presumably: новизна, интеграции, финансовое влияние, КИИ/регуляторика, обратимость... I don't know the exact rubric used to get 11/15. I should reconstruct a plausible axis set consistent with the repo. The repo says "Маршрут: Critical (значимость 11/15)". Let me define axes matching: 
- Финансовое влияние (деньги без действия клиента) — high
- Внешняя интеграция/регуляторика (НСПК, согласие клиента, 161-ФЗ/152-ФЗ, КИИ) — high
- Новизна сущности (новый агрегат «мандат», новая статусная машина, отзыв согласия) — high
- Влияние на существующее ядро (статусная машина, контракты, сверка, АБС) — medium-high
- Обратимость — costly/irreversible
- Данные/ПДн — рост (связка плательщик↔ТСП, реквизиты) 
Score out of 15.

Given the base was 11/15 Critical, and this change adds a new external consent-based financial primitive with regulatory weight while reusing the existing spine, I'd rate it... let me construct a 5-axis × 3 scale = 15. Base: 11. For this change I'd compute similar or slightly lower since core is reused: maybe 10/15 → Critical (or "Significant"?). The repo only names Critical for 11. I need a route ladder. Hmm, I don't know the repo's route names beyond Critical. Let me define: Critical ≥ 11, Significant 7–10, Moderate ≤ 6 (labels in ru: Критичный/Значимый/Умеренный). I'll present assessment transparently as an assumption since the source methodology doc isn't in the repo.

Let me score axes:
1. Финансовое влияние и риск двойных списаний — 3/3
2. Регуляторика/НПС/ПДн/право на отзыв согласия — 3/3
3. Внешняя интеграция (НСПК: новый механизм, токен/мандат) — 3/3
4. Влияние на ядро/контракты/сверку/АБС — 2/3
5. Новизна данных и модели (новый агрегат, ПДн связки) — 2/3
Total 13/15 → Critical. Hmm base was 11/15. Let me tune: maybe 4 axes? The repo doesn't tell. 13/15 Critical is fine and justified. Actually to be careful, I should note the scale is inherited from the base decision (11/15 Critical) and my scoring is an assessment. I'll say ≈ 12–13/15 → Critical.

Hmm, maybe better to reuse base axes but I can't know them. I'll present a 5-axis assessment and mark assumption.

Let me now write proposal.md.

Impact on invariants (deliverable 2):
- AD-001 (isolation): unaffected — mandate/charges live in the same isolated gateway; new ОПКЦ calls still only via adapter. Actually it reinforces.
- AD-002 (single source of truth, atomic status+outbox): extends — new mandate state machine must obey same atomic transition+outbox+audit rule. Touched/extended.
- AD-003 (idempotency): extends to mandate registration (reference), charge initiation (chargeId), revocation events (eventId). Touched/extended.
- AD-004 (single ОПКЦ adapter): touched — adapter contract must gain mandate operations/events; still the only path.
- AD-005 (credit only from PAID): preserved and re-affirmed — recurring charges must credit only from PAID. Key: a "confirmed" charge still goes through PAID. Not weakened.
- AD-006 (trust zones): extends — payer consent data, revocation, new PII relations.
- AD-007 (hybrid): untouched — still core own + vendor transport; vendor adapter scope grows (RFP addendum).
- AD-008 (adopted strategy): untouched, but the RFP/contract for vendor must be extended before transport work — a new external input.

What changes:
- New aggregate "мандат/подписка" + its own state machine + storage + audit.
- New payer consent flow (registration → confirmation in payer bank app → ОПКЦ event).
- New charge initiation path (ТСП → шлюз → ОПКЦ charge by mandate token) and new states for "ожидание подтверждения плательщика".
- New ОПКЦ adapter methods/events (mandate registration, mandate status, charge, revocation events).
- New TSP API endpoints + webhook events, additive.
- New NFRs (charge latency, consent activation, revocation propagation ≤ X).
- New reconciliation dimension (mandates vs ОПКЦ).
- RFP addendum for vendor (mandate support) — external input, blocking for transport.

What does NOT change:
- Crediting gate AD-005 (only from PAID), outbox pattern, idempotency principles, trust zones, AБС saga for refunds, reporting core, existing QR flows (fully backward compatible).
- Existing API methods and their semantics; existing state machine transitions.
- No change to the accepted hybrid strategy (AD-008).

Now design.md decisions with alternatives. Let me outline decisions:

D1. Мандат — самостоятельный агрегат со своей статусной машиной в БД шлюза (единый источник истины), ОПКЦ — источник согласия. Alternative: мандат только у ОПКЦ, шлюз stateless; мандат в АБС. Chosen: hybrid — consent authoritative at ОПКЦ/НСПК, commercial mandate state in gateway with reconciliation (consistent with AD-002 model of gateway as source of truth for operations, but consent is inherently external). Hmm — careful: consent is granted by payer to ТСП via ОПКЦ. The gateway must mirror it. I'll say: «согласие» (authoritative) — ОПКЦ; «мандат как коммерческий объект + связь с ТСП/лимиты» — шлюз; both reconciled. Actually simpler and defensible: шлюз хранит мандат как единый источник истины для операций, синхронизируется с ОПКЦ событиями и сверкой; ОПКЦ — первичный источник факта согласия/отзыва. I'll state clearly with reconciliation direction.

D2. Оформление мандата — отдельная регистрация без первого платежа (user chose). Alternatives: first-payment-linked; both. Consequence: need consent-confirmation UX outside ТСП (payer app), unique mandateId, no funds movement at registration.

D3. Списание — тихое в пределах лимитов мандата, подтверждение сверх порога (user chose). Alternatives: always silent; always confirm. Implementation: mandate carries maxAmountPerCharge, maxAmountPerPeriod, period, currency, remainingLimit; charge within limit → straight to ОПКЦ debit (which still yields PAID); above → new state CHARGE_AWAITING_PAYER (pending confirmation) with TTL and a confirmation link delivered via ОПКЦ? Hmm — how does confirmation reach payer? Via payer bank app notification (ОПКЦ). So the charge is submitted, ОПКЦ returns PENDING_CONFIRMATION, payer confirms in app → event → PAID. So the state machine gains a pre-PAID branch: charge → CHARGE_REQUESTED → (PENDING_CONFIRMATION) → PAID | FAILED | EXPIRED/REJECTED. Good.

D4. Идентичность и идемпотентность списания — детерминированный chargeId от (mandateId, billingPeriod/order) + Idempotency-Key. Prevents double charge on retry/duplicate scheduler.

D5. Двойной зачёт/лимиты — enforcement: шлюз ведёт счётчик использования лимита в одной транзакции со статусом (AD-002 pattern). Prevents limit overrun under concurrency.

D6. Отзыв согласия — обязателен: событие от ОПКЦ → мандат REVOKED → немедленный стоп новых списаний; в-полёте списания — по политике (завершить/отменить); фиксируется приоритет отзыва. New invariant AD-010: «Отзыв согласия плательщика немедленно и необратимо блокирует новые списания по мандату; мандат из REVOKED не возвращается в ACTIVE».

D7. Транспортная граница — расширение контракта адаптера ОПКЦ (новые методы/события); вендор обязан поддержать; RFP addendum; это внешний вход, блокирует транспортную реализацию (не блокирует ядро — мок-адаптер).

D8. Обратная совместимость контракта ТСП — только аддитивные изменения в /v1 (новые пути/поля/события), без изменения существующих; новые enum-значения статусов не вводятся в существующий Payment.status (charge — отдельный ресурс Charge с собственным статусом). This is important: do NOT add new values to existing Payment.status enum (breaking for strict consumers). Instead new resource. Good design point.

Hmm — but charges result in a Payment? A recurring charge produces a payment. Let me model: Charge resource (chargeId) which creates/settles a Payment? Or Charge IS a payment with type=recurring? To preserve compatibility, adding a new optional field `paymentType` to Payment is additive-safe; adding new enum values to status is risky for clients with strict enums. The existing enum already includes FAILED/EXPIRED. A charge needs "awaiting payer confirmation" which is a state not in the Payment enum. Options: (a) map to existing states — awaiting confirmation could be represented as a new internal state exposed as PAID? No. (b) introduce a separate Charge resource with its own status enum, and on success it produces a Payment (or the Charge references the resulting payment). 

Cleaner: `Charge` is a new resource with statuses: CREATED, AWAITING_PAYER, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REVOKED... Hmm, duplicating. Alternative: reuse Payment with `paymentType: recurring` and add a new status `AWAITING_CONFIRMATION` — but that's an additive enum value; strictly, adding enum values is a breaking change for consumers that fail on unknown values. The contract doc §6 says "Добавление опциональных полей — обратно совместимо". Enum additions are not covered. To be safe: introduce new status only in a NEW field or new resource. 

I'll design: recurring charge = a `Payment` with `paymentType: "recurring"` (new optional field, additive), and the pre-payment "awaiting payer" phase is represented as... Hmm, the Payment status enum would need a value. 

Better approach: model the recurring charge as its own resource `/v1/subscriptions/{mandateId}/charges` returning a `Charge` object with `status` enum that includes AWAITING_CONFIRMATION; a successful Charge yields a `paymentId` referencing the standard Payment resource. This keeps Payment.status enum untouched → zero breakage. Slight duplication in state but clean compatibility. I like it. Actually, to reduce duplication: Charge.status can mirror the payment lifecycle subset: CREATED → AWAITING_CONFIRMATION → PAID → CREDITED → COMPLETED / FAILED / EXPIRED, plus REFUNDED linkage. And Charge.paymentId is populated once the charge is accepted (PAID path creates the underlying payment). Hmm, or Charge IS the payment and we just don't expose Payment. 

Let me simplify to avoid overdesign: **Расширяем Payment аддитивно**: new optional field `paymentType` (`oneoff` default | `recurring`), new optional field `mandateId`, and introduce the pending-confirmation phase as a new status value in a **new enum present only in v2 of the response**? No, too complex.

Decision: new resource `Charge` (рекуррентное списание) under the mandate, with its own status enum incl. `AWAITING_CONFIRMATION`. It is the safest for backward compatibility and matches "no new enum values in existing Payment.status". design.md will state this explicitly as the compatibility strategy, and note the rejected alternative (adding enum value to Payment.status = breaking for strict clients). 

Hmm, but then do we get two parallel lifecycles? The Charge, once PAID, triggers crediting exactly like Payment (AD-005: credit only from PAID — here "из подтверждённого статуса"). The spine AD-005 says "Вызов АБС на зачисление возможен только из состояния PAID". For charges, the equivalent confirmed state is Charge.status=PAID. I should propose a spine clarification: AD-005 rule is about "подтверждённый НСПК статус"; new invariant AD-009/AD-010. I'll phrase the new invariant to cover charges: "Зачисление по рекуррентному списанию возможно только из подтверждённого ОПКЦ статуса (PAID); ожидание подтверждения плательщика не является подтверждением."

OK. Let me also consider: mandate registration also uses the idempotency and outbox.

New spine invariants proposal:
- **AD-009 (Proposed): Единый источник истины мандата и приоритет отзыва согласия.** Rule: состояние мандата (ACTIVE/SUSPENDED/REVOKED/EXPIRED) и счётчики лимитов хранятся в БД шлюза; любой переход мандата — атомарно (статус+outbox+аудит); отзыв согласия плательщика немедленно блокирует новые списания и необратим (REVOKED — терминальное).
- **AD-010 (Proposed): Списание только по действующему мандату в пределах лимитов.** Rule: рекуррентное списание инициируется только из ACTIVE-мандата, в пределах лимитов (сумма/период), с проверкой и резервированием лимита в той же транзакции; зачисление — только из подтверждённого ОПКЦ статуса. Fitness: недостижимость списания из не-ACTIVE мандата и превышения лимита.
- Maybe AD-011: согласие и ПДн — but that's covered by AD-007/006. I'll keep 2 new invariants.

Now, deferred item update: spine Deferred lists "Мультивалютность", "C2C и выплаты", "Диспуты". It doesn't list автоплатежи, but solutioning.md §1 roadmap does. So impact: solutioning.md roadmap item "автоплатежи" moves into scope → must note and (additively) update solutioning? Hmm. The user said accepted files change only by accepted method. Adding a note to solutioning.md §1 marking автоплатежи as now-in-scope-via-change... I could, but maybe better to leave solutioning.md and note in proposal/design that this change reactivates a deferred roadmap item, and update spine Deferred only if it lists it. It doesn't. So I'll note in the change and not edit solutioning (avoid touching the full design doc). Actually coherence matters: a reviewer will ask "you changed scope; where is it recorded?" — the OpenSpec change IS the record. Fine.

Hmm, but the spine has a Deferred section and a "Контракты и версии" section. Should I add to spine? Adding AD-009/AD-010 Proposed is the key. I'll also add a line under Deferred or a new "Change under review" pointer to the OpenSpec change. Let me add a short "Изменения в рассмотрении" section referencing the change + new proposed ADs. That's additive and clearly non-ratifying.

Now NFR (deliverable 5) — new measurable:
- Активация мандата (от подтверждения плательщика до ACTIVE у шлюза): p95 < 5 с.
- Инициирование списания (ТСП → шлюз → принято ОПКЦ), тихое в лимите: p95 < 1 с (без ОПКЦ), зачисление p95 < 60 с (наследует).
- Списание с подтверждением: TTL подтверждения ≤ 15 мин (по регламенту НСПК [ТРЕБУЕТ ПРОВЕРКИ]).
- Распространение отзыва согласия (ОПКЦ событие → блокировка списаний): p95 < 5 с, 100% новых списаний после отзыва отклоняются.
- Идемпотентность: 0 дублей списаний при повторной доставке/ретрае; 0 превышений лимита.
- Сверка мандатов с ОПКЦ: ежечасная; расхождений 0.
- Throughput: +recurring не ухудшает 200 TPS sustained; доля рекуррентных списаний — целевой профиль (напр., burst 500 TPS).
- Ошибки: charge rejected/reconciled 0 lost.
- Аудит: 100% переходов мандата и списаний в неизменяемом аудит-логе.
- Security: ключи/токены мандата не в логах; ПДн минимизированы.

Acceptance criteria (deliverable 6) — testable, incl. negative:
- Mandate: registration idempotent (same reference → same mandateId, no duplicate consent request).
- Charge within limit → PAID → credited once; double delivery of ОПКЦ notification → no second crediting.
- Charge above threshold → AWAITING_CONFIRMATION; no crediting before PAID; expired confirmation → no charge.
- Revoked mandate → new charge rejected (code MANDATE_NOT_ACTIVE), 0 debits.
- Limit overrun under concurrency (two parallel charges) → only up to limit consumed; second rejected.
- Existing consumers unaffected: existing endpoints/schemas unchanged (contract diff additive only; existing Payment.status enum unchanged) — regression test with v0.1 client.
- Reconciliation: revoked mandate mirrored; charge divergence resolved.
- Rollback criterion: disabling recurring capability (feature flag) returns system to QR-only behavior with no impact on existing flows; in-flight charges either complete or expire; mandates preserved read-only; RTO ≤ 1h.

Rollback plan (deliverable 6):
- Pre-prod: reversible, just don't enable.
- Feature flag per capability: stop-new-charges → stop accepting new charge initiations & new mandate registrations; existing mandates frozen; in-flight charges drained or expired; no data migration back; rollback release rolling; spine source of truth remains.
- Signals/triggers: double-charge incident, limit overrun, revocation not honored, mandate divergence — immediate stop-new; owner: solution-architect + платежный мониторинг, decision by A3/дежурный.
- Owner of rollback decision: бизнес-владелец + архитектор (A3), SRE исполняет.

What remains for the human architect (deliverable 7):
1. Регуляторная проверка: подтвердить, что механизм рекуррентных СБП-списаний (мандат/подписка) существует в актуальных Правилах ОПКЦ СБП и его точный протокол/лимиты — внешний вход [ТРЕБУЕТ ПРОВЕРКИ]. Это может изменить модель (token vs mandate).
2. Объём первой волны и тип ТСП (кинотеатры/ЖКХ/связь) — приоритизация; ЖКХ может требовать иной cadence.
3. Лимиты и порог подтверждения: бизнес-значения maxAmountPerCharge/period, порог подтверждения — влияние на клиентский опыт и конверсию.
4. Правовая модель согласия/мандата и право на отзыв (152-ФЗ, 161-ФЗ, ГК: ст. 438? согласие на периодические списания) — юристы/комплаенс.
5. Изменение scope вендора (RFP addendum) и влияние на ADR-007: подтвердить, что вендорский транспорт поддерживает мандаты; иначе пересмотр ADR-007.
6. Нужен ли отдельный ресурс Charge vs расширение Payment — архитектурное подтверждение (рекомендация дана, обратимо).
7. Категория КИИ/ПДн расширение и оценка влияния на объект КИИ — ИБ.
8. Ратификация новых spine-инвариантов AD-009/AD-010 и принятие новых ADR-008/009.
9. Решение о поведении in-flight списаний при отзыве/остановке (дозавершить/отменить) — баланс клиентского риска и обязательств.

Good.

Now ADRs:
- ADR-008: «Модель подписок СБП: мандат как самостоятельный агрегат, приоритет отзыва согласия» — covers D1, D2 (standalone registration), D6 (revocation).
- ADR-009: «Инициирование рекуррентных списаний: тихое в пределах лимитов с подтверждением сверх порога; идемпотентность и учёт лимитов» — covers D3, D4, D5, and the Charge-resource compatibility decision D8.

Each with Context/Decision/Alternatives/Consequences/Reversibility/References, Status: Proposed.

Now the OpenSpec artifacts. Let me write proposal first, then specs, then design, then tasks.

Capabilities decision: I'll go with two new capabilities to keep OpenSpec focused, plus a third for the vendor transport boundary? Let me decide: three:
- `sbp-mandates`
- `sbp-recurring-charges`
- `sbp-opkc-subscription-transport`

Hmm. The opkc transport delta is really part of the vendor contract; including it as a capability makes the RFP traceable. I'll include it. Total 3 spec files.

Wait, but that increases the required set and writing. It's fine; thoroughness is wanted.

Hmm, let me reconsider though: capability specs should describe externally observable behavior. The ОПКЦ adapter contract is externally observable (to the vendor). Yes, include.

Actually, I worry about scope/time. But the user wants a complete package. I'll do 3.

Let me reduce: combine transport into `sbp-mandates`? No — cleaner separate. OK, 3 capabilities.

Now, let me check `openspec list --specs` to confirm empty, then write proposal.

Let me also get the specs and design and tasks instructions after writing proposal (in sequence).

Let me run list --specs.

  `write_file(file_path="/home/architect/project/openspec/changes/sbp-recurring-payments/proposal.md", content="# Proposal\n\n## Why\n\nТСП (онлайн-кинотеатры, ЖКХ, связь) просят принимать платежи в СБП **без участия плательщика на каждой оплате** — п)`

Empty specs. Now write proposal.md.

Let me write it carefully, in Russian, keeping OpenSpec structural headings in English (## Why, ## What Changes, ## Capabilities, ### New Capabilities, ### Modified Capabilities, ## Impact).

Keep concise 1-2 pages. Include significance/route assessment in Why or Impact. The proposal template doesn't have a "significance" section, but I can put it in Why/Impact. The user's deliverable 1 asks for significance/route assessment. I'll put a compact assessment in the proposal (maybe under Why with a small table) — but the template says keep concise. I can add a "## Why" with the assessment paragraph + table. Adding extra sections is allowed? The instruction says sections: Why, What Changes, Capabilities, Impact. I'll keep to those but embed the significance table in Why. Hmm, or add "## Significance" — deviating from template. The skill says use template as structure. I'll embed in Why as a compact table. Actually, design.md can hold detailed significance. Let me put a compact route assessment in proposal Why, and detailed in design.md (design has room). 

Let me write.

Note: OpenSpec SHALL/MUST keywords in English in specs; proposal is prose.

Let me write proposal.md now.
OpenSpec change scaffolded. Now writing the artifacts in dependency order, starting with the proposal.

  `run_shell_command(command="cd /home/architect/project && openspec instructions specs --change \"sbp-recurring-payments\" --json 2>&1", description="Get specs artifact instructions")`

Now get specs instructions.
Proposal created. Now the spec deltas — let me read the specs instructions.

  `write_file(content="# Spec Delta\n\n## Purpose\n\nУправление мандатом подписки СБП — согласием плательщика на рекуррентные списания в пользу ТСП: регистрация м, file_path="/home/architect/project/openspec/changes/sbp-recurring-payments/specs/sbp-mandates/spec.md")`

Now I'll write three spec files:

1. `specs/sbp-mandates/spec.md`
2. `specs/sbp-recurring-charges/spec.md`
3. `specs/sbp-opkc-subscription-transport/spec.md`

Each: # Spec Delta, ## Purpose (new capability), ## ADDED Requirements, requirements with SHALL/MUST and #### Scenario with WHEN/THEN.

Language ru, structural headings English, SHALL/MUST keywords English.

Let me write sbp-mandates.

Requirements:

R1. Регистрация мандата (отдельно от платежа)
- ТСП SHALL создавать мандат через API с идемпотентностью; мандат SHALL NOT приводить к списанию.
- Scenario: успешная регистрация → статус PENDING_CONSENT, идентификатор мандата и ссылка на согласие.
- Scenario: повторная регистрация с тем же Idempotency-Key → тот же mandateId, без дубля.

R2. Подтверждение согласия плательщиком
- Мандат SHALL переходить в ACTIVE только после подтверждения плательщиком в приложении банка плательщика (событие ОПКЦ); до этого списания по мандату SHALL быть недоступны.
- Scenario: плательщик подтвердил → ACTIVE + вебхук subscription.activated.
- Scenario: плательщик не подтвердил в течение TTL → EXPIRED, списаний 0.

R3. Лимиты мандата
- Мандат SHALL содержать лимит суммы на списание, лимит суммы за период, длительность периода, валюту; изменения лимитов только через новый мандат (иммутабельность после ACTIVE).
- Scenario: попытка списания в пределах лимита разрешена; сверх — требует подтверждения; сверх жёсткого максимума — отклоняется.

R4. Отзыв согласия
- Отзыв согласия плательщиком SHALL немедленно переводить мандат в REVOKED; REVOKED SHALL быть терминальным; все новые списания по мандату SHALL отклоняться с MANDATE_NOT_ACTIVE; отзыв SHALL быть зафиксирован в неизменяемом аудит-логе.
- Scenario: отзыв → новые списания отклоняются, счётчик не растёт.
- Scenario: мандат REVOKED не возвращается в ACTIVE (повторная активация невозможна без нового мандата).

R5. Атомарность переходов мандата и учёт лимитов
- Каждый переход состояния мандата и изменение счётчика использования лимита SHALL выполняться в одной локальной транзакции с записью исходящего события (outbox) и аудит-логом; повторная доставка событий от ОПКЦ SHALL NOT менять состояние (дедупликация по eventId).
- Scenario: повторное событие ОПКЦ → состояние не меняется.
- Scenario: параллельные списания не превышают лимит (учёт и резервирование в одной транзакции).

R6. Сверка мандатов с ОПКЦ
- Шлюз SHALL периодически сверять состояние мандатов с ОПКЦ; расхождение «у ОПКЦ REVOKED, у шлюза ACTIVE» SHALL приводить к немедленной блокировке списаний и алерту.
- Scenario: расхождение обнаружено → списания блокируются, инцидент эскалирован.

R7. Аудит и ПДн мандата
- Данные согласия и ПДн плательщика SHALL храниться минимизированно и шифроваться в покое; идентификаторы мандата SHALL NOT попадать в логи в открытом виде.
- Scenario: (testable) аудит-лог содержит 100% переходов; в логах нет ПДн.

Hmm R7 scenario needs WHEN/THEN. Fine.

R8. Совместимость контракта ТСП для мандатов
- Новые методы мандатов SHALL быть аддитивными в /v1; существующие методы/схемы SHALL NOT изменяться; новые ошибки SHALL возвращаться в формате Problem Details с новыми кодами.
- Scenario: существующий потребитель v0.1 продолжает работать без изменений.
- Scenario: ошибка по мандату → Problem Details с кодом MANDATE_NOT_ACTIVE.

Good. Now sbp-recurring-charges:

R1. Инициирование рекуррентного списания
- ТСП SHALL инициировать списание по активному мандату; шлюз SHALL NOT принимать списание по мандату не в ACTIVE.
- Scenario: ACTIVE мандат → списание принято; Scenario: не-ACTIVE → MANDATE_NOT_ACTIVE, 0 списаний.

R2. Тихое списание в пределах лимита
- Если сумма ≤ остатка лимита мандата (и ≤ порога подтверждения), списание SHALL проводиться без действия плательщика.
- Scenario: тихое списание → статус CHARGE PAID после подтверждения ОПКЦ.

R3. Подтверждение сверх порога
- Если сумма > порога подтверждения (но ≤ жёсткого максимума мандата), списание SHALL требовать подтверждения плательщика; до подтверждения списание SHALL NOT приводить к зачислению; при отсутствии подтверждения в TTL — истекает без списания.
- Scenario: сверх порога → AWAITING_CONFIRMATION, зачисления нет; Scenario: подтверждено → PAID; Scenario: TTL истёк → EXPIRED без зачисления.

R4. Зачисление только из подтверждённого статуса
- Зачисление по рекуррентному списанию SHALL выполняться только из подтверждённого ОПКЦ статуса (PAID); ожидание подтверждения плательщика SHALL NOT считать подтверждением.
- Scenario: попытка зачисления из AWAITING_CONFIRMATION недостижима (fitness).
- Scenario: PAID → ровно одно зачисление, CREDITED → COMPLETED.

R5. Идемпотентность списания
- Повторные запросы/повторные события SHALL NOT приводить к повторному списанию или зачислению; ключ идемпотентности списания детерминирован и уникален для итерации подписки.
- Scenario: повторная инициация → тот же chargeId, второе списание не создаётся.
- Scenario: повторная нотификация ОПКЦ → одно зачисление.

R6. Учёт лимитов и период
- Шлюз SHALL резервировать/учитывать сумму списания в лимите мандата в одной транзакции с переходом состояния; превышение SHALL отклоняться.
- Scenario: два параллельных списания → лимит не превышен.

R7. Вебхуки и статусы списания
- Шлюз SHALL доставлять ТСП события charge.* (at-least-once, HMAC, дедуп по eventId); технические подсостояния наружу не выставляются.
- Scenario: charge.completed доставлен; Scenario: повтор доставки → ТСП дедуплицирует, шлюз ретраит.

R8. Обратная совместимость статусов
- Новые состояния списания SHALL NOT добавляться в enum Payment.status; списание SHALL представляться отдельным ресурсом с собственным статусом; поля существующих ответов SHALL NOT меняться.
- Scenario: клиент v0.1, строго валидирующий enum Payment.status, продолжает работать.

R9. Совместимость с возвратами
- Возврат по рекуррентному списанию SHALL использовать существующую сагу возвратов (refundId) без изменения инвариантов AD-005.
- Scenario: возврат по charge → REFUNDED, проводка одна.

Good.

Now sbp-opkc-subscription-transport:

Purpose: define internal contract of ОПКЦ adapter for mandates + recurring charges.

R1. Операции мандата
- Адаптер SHALL предоставлять операции регистрации мандата, запроса статуса мандата, отмены мандата; все мутирующие вызовы идемпотентны по reference.
- Scenario: повторная регистрация с тем же reference → тот же mandate ОПКЦ, без дубля.

R2. Инициирование списания
- Адаптер SHALL предоставлять операцию инициирования списания по мандату, включая сценарий подтверждения плательщиком, с нормализованными ответами.
- Scenario: списание в лимите → ответ ACCEPTED/PAID; Scenario: требуется подтверждение → PENDING_CONFIRMATION.

R3. События мандата и списания
- Адаптер SHALL публиковать события activation/revocation/suspension мандата и результаты списаний с eventId и correlationRef ядра; at-least-once; устойчивость к поздним событиям.
- Scenario: событие отзыва доставлено повторно → ядро дедуплицирует.

R4. Нормализация
- Адаптер SHALL нормализовать статусы/ошибки протокола НСПК; ядро SHALL NOT зависеть от протокольных значений.
- Scenario: протокольная ошибка → нормализованный код.

R5. Идемпотентность и корреляция
- Адаптер SHALL обеспечивать идемпотентность мутирующих операций по reference и не создавать дублей в ОПКЦ.
- Scenario: POC — повтор createCharge с тем же reference → один charge.

R6. Таймауты/ретраи/circuit breaker и NFR
- SHALL соответствовать NFR шлюза (таймауты p99.9, ≥200 TPS, потеря событий 0, доступность ≥99.95%), метрики/trace id.
- Scenario: канал вниз → 503 TRANSPORT_UNAVAILABLE + transport.unavailable.

R7. Тестовый контур
- Вендор SHALL предоставить тестовый контур НСПК со сценариями мандатов/списаний, включая подтверждение, отзыв, повторы.
- Scenario: сценарий подтверждения/отзыва воспроизводим на тестовом контуре.

Good.

Let me now write these three files. Must ensure `## Purpose` present (new capabilities). Use `####` for scenarios exactly.

Let me write.
Now the three capability spec deltas.

  `write_file(content="# Spec Delta\n\n## Purpose\n\nИнициирование и проведение рекуррентных C2B-списаний по действующему мандату подписки: тихое списание в преде, file_path="/home/architect/project/openspec/changes/sbp-recurring-payments/specs/sbp-recurring-charges/spec.md")`

Now sbp-recurring-charges.

  `write_file(content="# Spec Delta\n\n## Purpose\n\nТребования к внутреннему контракту адаптера ОПКЦ для мандатов подписки и рекуррентных списаний — единственной, file_path="/home/architect/project/openspec/changes/sbp-recurring-payments/specs/sbp-opkc-subscription-transport/spec.md")`

Now the transport spec.

  `run_shell_command(command="cd /home/architect/project && openspec status --change \"sbp-recurring-payments\" --json 2>&1 | head -60; echo \"=== DESIGN INSTR ===\"; op, description="Check status and design instructions")`

Now check status and get design instructions.

  `write_file(content="# Design\n\n## Context\n\nСм. `proposal.md` — Why. Принятое решение (`ARCHITECTURE-SPINE.md` AD-001…AD-008, `docs/adr/ADR-001…007`, `docs/s, file_path="/home/architect/project/openspec/changes/sbp-recurring-payments/design.md")`

Now write design.md. This is the core architectural decision doc: impact on architecture/invariants, decisions with alternatives, contract change design, consequences, reversibility, open questions for the human architect, NFR design-level, rollback.

Note: design.md should not restate specs; reference them. But the user wants deliverables 2,3,4,7 captured. I'll include sections: Context, Goals/Non-Goals, Impact on the accepted architecture (invariants), Decisions (D1..D8 with alternatives), Contract change strategy (openapi), NFR (design-level targets, reference), Risks/Trade-offs, Migration Plan & Rollback, Open Questions (human architect decisions).

Let me write it comprehensively but not bloated.

Impact on invariants table:
| Инвариант | Влияние | Что меняется |
AD-001 Изоляция — Reinforced/unchanged: мандаты и списания живут в том же платёжном контуре; новые вызовы ОПКЦ только через адаптер. Не меняется (правило расширяется по объектам).
AD-002 Единый источник истины — Extended: новая статусная машина мандата подчиняется тому же правилу «статус+outbox+аудит атомарно». Меняется состав объекта, не правило.
AD-003 Идемпотентность — Extended: добавляются ключи mandate reference, chargeId, события мандата/списания. Правило не меняется.
AD-004 Единственный адаптер ОПКЦ — Extended: контракт адаптера расширяется методами/событиями мандата; правило (только адаптер) сохраняется.
AD-005 Зачисление только из подтверждённого статуса — Preserved/Усилен: новое подсостояние AWAITING_CONFIRMATION не является подтверждением; требуется явное расширение формулировки на «списание» (charge) — предлагается AD-010.
AD-006 Trust-зоны — Extended: рост ПДн-периметра (связка плательщик↔ТСП), те же зоны.
AD-007 Стратегия (гибрид) — Touched (externally): scope вендора расширяется; нужен addendum RFP.
AD-008 Adopted — Unchanged: ядро остаётся контрактно-независимым; транспорт по-прежнему после документации НСПК.

What changes / what doesn't (also in proposal). Good.

Decisions:

D1. Мандат — самостоятельный агрегат; согласие авторитетно у ОПКЦ, коммерческое состояние — у шлюза, сверка.
Alternatives: (a) мандат только у ОПКЦ (шлюз stateless) — нет локального источника для лимитов/аудита/идемпотентности, потеря RPO=0; (b) мандат в АБС — размывает границу, AD-001/005; (c) выбранный hybrid.
Rationale ties to AD-002/AD-001.

D2. Отдельная регистрация мандата без первого платежа (user decision).
Alternatives: first-payment-linked; both. Consequences: no funds movement at registration; consent UX outside ТСП; needs mandateId lifecycle; clearer legal basis (согласие как отдельный акт). Non-goal: первая оплата не является активацией.

D3. Списание: тихое в пределах лимита, подтверждение сверх порога (user decision).
Alternatives: always silent; always confirm. New state AWAITING_CONFIRMATION. Threshold = min(mandate confirmation threshold, hard max).

D4. Отдельный ресурс Charge с собственным статусом; не расширяем enum Payment.status.
Alternatives: (a) добавить статус в Payment.status — BREAKING для строгих потребителей; (b) флаг paymentType внутри Payment — не выражает ожидание подтверждения; (c) выбранный отдельный ресурс + ссылка на paymentId/chargeId.
Rationale: сохранить обратную совместимость (deliverable 4).

D5. Детерминированный ключ идемпотентности списания (mandateId + период/номер итерации, либо явный Idempotency-Key ТСП) с уникальным ограничением в БД.
Alternatives: только Idempotency-Key ТСП (риск дубля при новом ключе на ретрае у ТСП); auto-generated (риск дубля при сетевом ретрае). Chosen: оба — детерминированное ограничение уникальности в БД + ключ ТСП.

D6. Учёт лимитов в транзакции перехода (резерв/освобождение).
Alternatives: отдельный счётчик вне транзакции (гонка → превышение); внешний rate-limiter (не транзакционно).

D7. Отзыв согласия — приоритетный, необратимый; политика для in-flight списаний.
Alternatives: (a) отменять все in-flight — риск незавершённых обязательств/диспутов; (b) дозавершать уже подтверждённые (PAID) и отменять не-подтверждённые — chosen; (c) дозавершать всё — конфликт с волей плательщика. Chosen (b), финальная политика — на решение архитектора/юристов (open question).

D8. Транспортная граница: расширение контракта адаптера ОПКЦ + addendum RFP; ядро стартует на мок-адаптере.
Alternatives: ждать протокол НСПК (блокирует весь прогресс); делать транспорт самим (нарушает ADR-007/AD-008).

D9. Расширение контракта ТСП — только аддитивно в /v1 (new paths/schemas/enum values), deprecation/versioning rule unchanged; новые вебхуки.

Risks:
- Регуляторная неопределённость механизма подписок в СБП [ТРЕБУЕТ ПРОВЕРКИ] → если ОПКЦ не поддерживает, модель пересматривается; митигация: ранний запрос в НСПК, внешний вход до разработки транспорта.
- Двойное списание при ретраях/расписании ТСП → детерминированный ключ + уникальный индекс + тесты.
- Превышение лимита под конкуренцией → транзакционный учёт.
- Отзыв согласия не проброшен вовремя → сверка + приоритетное событие + алерт; invariant «0 списаний после отзыва».
- Рост ПДн и поверхности → минимизация, шифрование, маскирование, ИБ-ревью.
- Scope creep: доп. ресурс Charge дублирует Payment → митигация: charge ссылается на стандартный paymentId, единый путь зачисления и сага.
- Зависимость от вендора (scope expands) → addendum, kill criteria.
- Обратная совместимость enum → запрет на изменение Payment.status (fitness).

Migration Plan + rollback:
- Фича-флаг на уровне capability (mandates/charges) и на уровне ТСП (пилот).
- Порядок деплоя: схема (аддитивно) → read-only справочники → за флагом endpoints (404/403 когда off) → включение пилота → расширение.
- Rollback: stop-new (запрет регистрации мандатов и новых списаний), дренаж in-flight, мандаты read-only, отключение флага; данные не мигрируются назад; существующие QR-потоки не затрагиваются; RTO ≤ 1 ч. Сигналы-триггеры и владелец решения.
- БД-миграции аддитивны и обратно совместимы (новые таблицы/столбцы), откат релиза не требует отката схемы.

NFR: reference docs/nfr.md new section; list targets here briefly.

Open Questions for human architect (deliverable 7):
1. Регуляторная проверка механизма (Правила ОПКЦ СБП, протокол, лимиты, TTL подтверждения) — внешний вход [ТРЕБУЕТ ПРОВЕРКИ].
2. Юридическая модель согласия и отзыва (152/161-ФЗ, ГК), политика in-flight списаний при отзыве.
3. Бизнес-значения лимитов и порога подтверждения (по типам ТСП).
4. Подтверждение/изменение scope вендора (addendum RFP) и влияние на ADR-007.
5. Ратификация AD-009/AD-010 и принятие ADR-008/009.
6. Приоритизация первой волны ТСП и целевой профиль нагрузки.
7. КИИ-категория и расширение ПДн-периметра — ИБ.
8. Принятие решения по ресурсу Charge vs расширение Payment (рекомендация дана).

Good. Let me write design.md.

I must be careful: design.md "Open Questions" per instruction is for genuinely deferrable unknowns. But the user explicitly wants "Что остаётся на решение человека-архитектора" — that's a distinct concept: human decision gate. I'll title it "## Open Questions (решение человека-архитектора)" and frame them as decisions requiring the A3-type gate, which is legitimate — they don't require guessing, they're escalated. That's consistent: the instruction says if a question would change specs/approach/tasks, resolve now or ask user. Some of these are genuinely external (regulatory), which is a valid blocker/escalation. I'll note that none blocks the artifact set; they block transport implementation/gate.

Also note: the design instruction says include design.md "only if any apply" — cross-cutting, new external dependency, data model changes → yes.

Let me write.
Now the design document — the architectural core of the package.

  `run_shell_command(command="cd /home/architect/project && openspec instructions tasks --change \"sbp-recurring-payments\" --json 2>&1 | python3 -c \"import json,sys; d, description="Get tasks artifact instructions")`

Now tasks.md. Get instructions.
Now the tasks artifact.

  `run_shell_command(command="cd /home/architect/project && openspec instructions tasks --change \"sbp-recurring-payments\" --json 2>&1", description="Get tasks artifact instructions")`
  `write_file(content="# Tasks\n\n## 1. Гейт архитектурного решения (человеческий)\n\n- [ ] 1.1 Внести на архитектурный гейт (тип A3) пакет изменения `openspec/ch, file_path="/home/architect/project/openspec/changes/sbp-recurring-payments/tasks.md")`

Now write tasks.md. Groups by dependency, each with verification, tests/docs inside each group. Group numbering.

Groups:
1. Решение и гейт (архитектурные артефакты) — ADRs, spine, NFR, contract docs, state machine doc. Verification: files exist; openspec validate passes; fitness rules pass.
   Actually, these doc updates I'm going to do as part of this package. Hmm — tasks.md is the implementation checklist for the apply phase. The arch docs (ADR/spine/NFR) — should they be tasks or done now? The user wants the package to include ADR/NFR/contracts changes. I think I should produce those files NOW as part of the package (deliverables 3,4,5), and tasks.md focuses on the implementation (code + verification) that follows the ratifation. But tasks can also include "принять ADR/ратитьицировать spine" as tasks for the human gate.

Let me structure:
1. Гейт решения (человеческий) — ратификация AD-009/AD-010, принятие ADR-008/009, addendum RFP, регуляторная проверка. Verification: gate A3 record.
2. Модель данных и миграция мандата/списания — schema, counters, indexes. Verify: migration up/down on clean+existing DB; unique index test.
3. Ядро: статусная машина мандата — register/activate/revoke/suspend, events, audit, reconciliation. Verify: unit/integration tests incl. duplicate event, revoke→no charge.
4. Ядро: рекуррентное списание — charge create, silent/confirm branch, limit reserve/release, idempotency, crediting only from PAID, refunds. Verify tests.
5. Транспорт (мок-адаптер) — new methods/events, idempotency by reference. Verify: mock contract conformance tests, POC scenarios.
6. Контракт API ТСП и вебхуки — openapi additive, backward-compat check, webhook types. Verify: openapi diff additive-only, regression client v0.1.
7. NFR/нагрузка и fitness — fitness checks for invariants, load tests, reconciliation reports. Verify commands.
8. Наблюдаемость, аудит, безопасность — metrics, alerts, masking, audit log; AML/SIEM. Verify.
9. Пилот и раскатка/откат — feature flag, pilot, runbook, rollback drill. Verify.

Each task with verification in description.

Since the docs (ADR/spine/NFR/openapi) are deliverables I produce now, group 1 can be "Архитектурный пакет и гейт" with tasks to ratify + maintain. But I've already created them. Tasks are for the apply phase though. Hmm — OpenSpec tasks are "what implementation work remains". The arch docs are planning artifacts already produced. But the user explicitly wants the package to contain the ADRs/NFR/contract updates. I'll create them now (as part of the package), and tasks.md will reference them as inputs, with remaining tasks: ратификация, и затем реализация.

Actually wait — the OpenSpec propose workflow's planning boundary says produce planning artifacts; ADRs/NFR/spine/contract are design/planning artifacts, not code. Producing them now is consistent with "prepare the architectural package". Good.

But careful: tasks.md should not re-list "write ADR-008" since I'm doing it. I'll include "ратифицировать/принять" tasks in the gate group.

Let me write tasks.md.

Let me make tasks concrete with verification.

I'll write ~9 groups, ~3-5 tasks each.

Let me write.

  `run_shell_command(command="cd /home/architect/project && openspec validate \"sbp-recurring-payments\" --strict 2>&1; echo \"=== STATUS ===\"; openspec status --change, description="Validate change and show status")`

Now validate the change and check status, then create the remaining arch files:
- docs/adr/ADR-008-...md and ADR-009-...md (Proposed)
- docs/spec/mandate-state-machine.md
- ARCHITECTURE-SPINE.md additions (AD-009, AD-010 Proposed, and a pointer)
- docs/nfr.md new section
- openapi/tsp-api.yaml additive changes
- docs/contracts/tsp-api.md additive? and docs/contracts/opkc-adapter.md additive?

Let me validate first.
All four OpenSpec artifacts are written. Let me validate the change.

  `write_file(content="# ADR-008. Модель подписок СБП: мандат как самостоятельный агрегат, приоритет отзыва согласия\n\n- Date: 2026-09-29\n- Status: Proposed (вы, file_path="/home/architect/project/docs/adr/ADR-008-model-podpisok-sbp-mandat-i-prioritet-otzyva-soglasiya.md")`

Change valid and complete. Now produce the accepted-decision-side artifacts (the "architectural package" tail), following the repo's own conventions (Status: Proposed, numbered ADRs, additive edits, `[ТРЕБУЕТ ПРОВЕРКИ]` markers).

Deliverable 3: ADR-008 and ADR-009 (Proposed).
Deliverable 5: docs/nfr.md new section.
Deliverable 4: openapi/tsp-api.yaml additive changes.
Also: docs/spec/mandate-state-machine.md, ARCHITECTURE-SPINE.md Proposed blocks, and additive updates to docs/contracts/tsp-api.md + opkc-adapter.md for coherence.

Let me be careful about the "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — the accepted method: ADRs are added as new files with Status: Proposed; spine blocks added as Proposed; docs are additive/baseline. I'll do additive edits only, and not modify existing ADR/spine rules.

Let me write ADR-008 first.

ADR-008: Модель подписок СБП: мандат как самостоятельный агрегат, приоритет отзыва согласия.
Sections matching repo style: title, Date, Status, Owner, Related, Context, Decision, Alternatives Considered (table), Consequences (Positive/Negative), Reversibility, References.

Date: use current date 2026-09-29? The repo ADRs are 2026-08-15. Current date is 2026-09-29. I'll use 2026-09-29.

Let me write ADR-008.

Then ADR-009: Инициирование рекуррентных списаний: лимиты, подтверждение сверх порога, отдельный ресурс Charge.

Then docs/spec/mandate-state-machine.md.

Then spine edits: add AD-009 and AD-010 after AD-008, before Deferred. And add a note in Deferred/roadmap? The Deferred section doesn't mention autopayments; but solutioning roadmap does. I'll add to spine a new subsection "Изменения в рассмотрении" referencing the OpenSpec change and new ADRs. Also update the "Контракты и версии" maybe. Keep minimal.

Let me write ADR-008 and ADR-009 now.

Naming convention for files: docs/adr/ADR-008-<translit>.md. Existing: ADR-008 doesn't exist. I'll name:
- ADR-008-model-podpisok-sbp-mandat-kak-samostoyatelnyy-agregat-prioritet-otzyva-soglasiya.md — too long. Existing names are long transliterations. I'll use:
  - ADR-008-model-podpisok-sbp-mandat-i-prioritet-otzyva-soglasiya.md
  - ADR-009-rekurrentnye-spisaniya-po-mandatu-limity-i-podtverzhdenie.md

Good.

Let me write ADR-008.
Change validates cleanly. Now I'll produce the accepted-decision-side artifacts in the repo's own convention (new ADRs as `Proposed`, additive edits), starting with the two ADRs.

  `write_file(content="# ADR-009. Рекуррентные списания по мандату: тихие списания в лимитах, подтверждение сверх порога, отдельный ресурс `Charge`\n\n- Date: 202, file_path="/home/architect/project/docs/adr/ADR-009-rekurrentnye-spisaniya-po-mandatu-limity-i-podtverzhdenie.md")`
  `write_file(content="# Статусная машина мандата подписки — спецификация переходов\n\n- Status: Draft (для ревью на архитектурном гейте; связанное изменение — `o, file_path="/home/architect/project/docs/spec/mandate-state-machine.md")`

Now the mandate state machine spec file. Let me create docs/spec/mandate-state-machine.md, mirroring the style of state-machine.md.

Then spine edits, nfr, openapi, contracts.

Let me write mandate-state-machine.md.
Now the mandate state-machine spec, mirroring the existing `docs/spec/state-machine.md` style.

  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now spine edits: add AD-009, AD-010 (Proposed) and a pointer to the change, plus update Deferred (reactivated autopayments). Let me re-read the relevant part of the spine to make precise edits. I have it. The spine structure:

- AD-001..AD-008
- --- 
- ## Deferred (с причиной и условием возврата)
- ## Контракты и версии

I'll insert after AD-008 block (before the `---` preceding Deferred) two new blocks AD-009, AD-010. And add to Deferred a note about автоплатежи reactivated. And add a line under "Контракты и версии" about new contract v0.1 additions? Better: add a new small section "## Изменения в рассмотрении" after Контракты и версии, referencing the change and new ADRs.

Let me do the edits.

First, insert AD-009/AD-010 after the AD-008 block. The AD-008 block ends with:
"- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)"

I'll insert the new blocks between the AD-008 rule and the `---`.

Let me use edit with old_string = the AD-008 rule line + "\n\n---\n\n## Deferred" and new_string = AD-008 rule + new blocks + "---" + Deferred.

Let me craft the new blocks carefully with exact Rule text.

AD-009:
```
## AD-009. Единый источник истины мандата подписки и приоритет отзыва согласия

- Status: Proposed (ADR-008)
- **Binds**: БД шлюза (состояние мандата, лимиты, счётчики), outbox, аудит-лог, сверка с ОПКЦ.
- **Prevents**: списание по мандату без действующего согласия; реактивацию отозванного согласия; расхождение «у ОПКЦ отозвано, у шлюза ACTIVE».
- **Rule**: Коммерческое состояние мандата (PENDING_CONSENT/ACTIVE/SUSPENDED/REVOKED/EXPIRED) и счётчики использования лимитов хранятся в БД шлюза; каждый переход мандата — атомарно с записью outbox и аудит-лога (AD-002). Факт согласия и отзыва авторитетно определяется ОПКЦ; отзыв согласия немедленно и необратимо запрещает новые списания, `REVOKED` — терминальное состояние. Новое списание допустимо только из `ACTIVE`.
```

AD-010:
```
## AD-010. Рекуррентное списание только по активному мандату в пределах лимитов

- Status: Proposed (ADR-009)
- **Binds**: статусная машина списания, учёт лимитов, АБС-адаптер, нотификации.
- **Prevents**: двойное списание при ретрае/повторе планировщика ТСП; превышение лимитов мандата при параллельных списаниях; зачисление из ожидания подтверждения плательщика.
- **Rule**: Рекуррентное списание инициируется только по мандату в состоянии `ACTIVE`, в пределах лимитов; резерв/освобождение лимита — в одной транзакции с переходом состояния списания. Зачисление в АБС возможно только из подтверждённого ОПКЦ состояния `PAID` (AD-005); `AWAITING_CONFIRMATION` подтверждением не является. Fitness: недостижимость списания из не-`ACTIVE`, превышения лимита и зачисления из ожидания подтверждения.
```

Good.

Then under Deferred, add a note. Actually the Deferred list has "C2C-переводы и выплаты B2C/B2B". Add an item for автоплатежи? It says "Dispуты" etc. Since автоплатежи weren't in spine Deferred, I'll add a line noting it's now in scope via the change. Let me add after the Disputes bullet:
"- **Автоплатежи/подписки СБП**: ранее в roadmap `docs/solutioning.md` как вне scope; переведены в scope изменением `sbp-recurring-payments` (см. AD-009/AD-010, ADR-008/009)."

Hmm, Deferred is for deferred items; adding a "no longer deferred" note there is a bit odd but useful. Better to add a new section "## Изменения в рассмотрении". Let me do both minimally: add the new section at the end and not touch Deferred. Actually touching Deferred is fine and informative. I'll add a "Пересмотрено" note. Simpler: add new section "## Изменения в рассмотрении (Proposed)" after "Контракты и версии". Let me append.

Let me read the end of the spine to append precisely. I have the content. The file ends with:
"- Пиннинг версий зависимостей — в CONSTRAINTS.yaml (.arch-handoff) при передаче кодовому харнессу."

I'll append a new section.

Let me do the edits.
Now updating the architecture spine with the new Proposed invariants — additively, preserving all existing rules.

  `read_file(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", offset=75, limit=20)`

Now append a section "Изменения в рассмотрении" at the end of the spine, and update the Deferred/roadmap note about автоплатежи. Let me read the end of the spine to append correctly.

The spine ends with:
"## Контракты и версии
- Контракт НСПК: ...
- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec).
- Пиннинг версий зависимостей — в CONSTRAINTS.yaml (.arch-handoff) при передаче кодовому харнессу."

Let me read the current full spine tail to be safe.

  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", old_string="## Контракты и версии\n\n- Контракт НСПК: `docs/contracts/nspk-contract.md` — создаётся после получения документации НСПК; до этого все ссы, new_string="## Контракты и версии\n\n- Контракт НСПК: `docs/contracts/nspk-contract.md` — создаётся после получения документации НСПК; до этого все ссы)`
  `edit(file_path="/home/architect/project/docs/nfr.md", new_string="| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |\n\n## 7. Рекуррентные списания (подписки СБП)\n\nЦели раздела относ, old_string="| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |\n\n## Зависимости (внешние входы для NFR)")`

Now docs/nfr.md — add a new section for subscriptions. Additive; append after section 6 (Наблюдаемость) and before "Зависимости (внешние входы для NFR)". Let me add "## 7. Рекуррентные списания (подписки СБП)" with measurable targets and method. Renumber? The existing sections 1-6 then "Зависимости". Appending a section 7 before "Зависимости" is fine.

Let me edit: old_string = "## 6. Наблюдаемость\n\n| ... |\n...\n\n## Зависимости (внешние входы для NFR)". I need the exact text. From earlier read:

```
## 6. Наблюдаемость

| Метрика | Цель | Метод проверки |
|---|---|---|
| Trace id на операцию | 100 % операций | APM |
| Алерт на DLQ | DLQ > 0 → алерт за ≤ 5 мин | Мониторинг |
| Лаг очереди нотификаций | ≤ 60 с в норме | Мониторинг |
| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |

## Зависимости (внешние входы для NFR)
```

I'll insert section 7 between the observability table and "## Зависимости".

Let me write the new section content.

## 7. Рекуррентные списания (подписки СБП)

| Метрика | Цель | Метод проверки |
| Активация мандата (подтверждение плательщика → ACTIVE в шлюзе) | p95 < 5 с | Метрика процесса |
| Регистрация мандата (API ТСП, без учёта ОПКЦ) | p95 < 500 мс | Нагрузочный тест |
| Инициирование тихого списания (API ТСП, без учёта ОПКЦ) | p95 < 1 с, p99 < 2 с | Нагрузочный тест |
| Зачисление по списанию от подтверждения | p95 < 60 с (SLA с АБС, наследует) | Метрика процесса |
| TTL подтверждения плательщика сверх порога | по регламенту НСПК [ТРЕБУЕТ ПРОВЕРКИ] | Конфигурация + тест |
| Распространение отзыва согласия до блокировки новых списаний | p95 < 5 с | Тест + метрика |
| Доля отказов новых списаний после отзыва | 100 % | Тест |
| Дубли рекуррентных списаний при повторах | 0 | Тест идемпотентности |
| Превышения лимита мандата | 0 | Тест параллельных списаний |
| Сверка мандатов с ОПКЦ | ежечасная; расхождений 0 | Reconciliation-отчёт |
| Throughput с профилем подписок | 200 TPS sustained, пик 500 TPS (не хуже базового) | Нагрузочный тест |
| Аудит переходов мандата и списания | 100 %, лог неизменяем | Аудит |
| ПДн мандата | минимизированы, шифрование в покое, маскирование в логах | ИБ-ревью |

And update the "Зависимости" section to add НСПК subscription regulations. Let me add a bullet there too.

Let me do the edit.
Now extending NFR with measurable targets for the new functionality.

  `edit(file_path="/home/architect/project/docs/nfr.md", new_string="- Регламенты НСПК: таймауты, сроки уведомлений, требования к доступности [ТРЕБУЕТ ПРОВЕРКИ — из документации НСПК].\n- Регламенты НСПК по п, old_string="- Регламенты НСПК: таймауты, сроки уведомлений, требования к доступности [ТРЕБУЕТ ПРОВЕРКИ — из документации НСПК].\n- SLA АБС на зачислени)`

Now add a dependency bullet for НСПК subscription regulations. Let me edit the "Зависимости" list.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\n  # 0.1.0 → 0.2.0: аддитивное расширение — мандаты подписки и рекурре, file_path="/home/architect/project/openapi/tsp-api.yaml")`

Now the openapi/tsp-api.yaml — additive changes. Deliverable 4: contract changes without breaking existing consumers.

Current yaml is minimal. I'll extend additively:
- Add paths: 
  - /v1/mandates (POST createMandate)
  - /v1/mandates/{mandateId} (GET getMandate)
  - /v1/mandates/{mandateId}/revoke (POST) — hmm, revocation is payer-side; ТСП may also stop. Add POST /v1/mandates/{mandateId}/suspend and /resume? Keep minimal: revocation by payer is event; ТСП can cancel/suspend. I'll add POST /v1/mandates/{mandateId}:suspend? OpenAPI path style. Let me use:
    - POST /v1/mandates/{mandateId}/suspend (operationId suspendMandate)
    - POST /v1/mandates/{mandateId}/resume (operationId resumeMandate)
  - /v1/mandates/{mandateId}/charges (POST createCharge)
  - /v1/charges/{chargeId} (GET getCharge)
  - /v1/charges/{chargeId}/refunds (POST? existing refunds are under /v1/payments/{paymentId}/refunds). For charges, add POST /v1/charges/{chargeId}/refunds (createChargeRefund) and GET.
- Add schemas: MandateRequest, Mandate, MandateLimits, ChargeRequest, Charge, ChargeStatus enum, MandateStatus enum.
- Add error codes? The yaml has no error schemas. I'll not add a full ProblemDetails; keep additive minimal but mention new codes. Actually adding components/schemas/Problem would be additive and useful. But keep it modest — I'll add new paths + schemas. Add idempotency header on POSTs.
- Also add webhook event types? Not in openapi; documented in tsp-api.md. I'll update docs/contracts/tsp-api.md with the new methods/events.

I must keep the existing content intact and only append. Also add `version: 0.2.0`? The info.version is 0.1.0. Changing version is a modification but additive/semver-minor; not breaking. I'll bump to 0.2.0 and note additive. Hmm — "без поломки существующих потребителей" — bumping minor version is fine. But is changing info.version "breaking"? No. I'll bump to 0.2.0.

Wait, the design/tasks said openapi additive; version bump communicates additive change. I'll do it.

Let me rewrite the whole file? I must be careful — read_file showed the full content (it's short). I'll use write_file to rewrite it with additions, preserving existing paths/schemas exactly. Since the file is small and I have full content, that's safe. But the instruction says read before write — done.

Let me construct the new yaml.

```yaml
openapi: 3.0.3
info:
  title: СБП-шлюз — API ТСП
  version: 0.2.0   # 0.1.0 → 0.2.0: аддитивное расширение (мандаты и рекуррентные списания); существующие методы и схемы не изменены
paths:
  /v1/payments:
    ... unchanged ...
  /v1/payments/{paymentId}:
    ... unchanged ...
  /v1/mandates:
    post:
      operationId: createMandate
      summary: Регистрация мандата подписки (без списания)
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
          description: Мандат зарегистрирован, ожидает подтверждения плательщика
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
          description: Состояние мандата
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Mandate'}
  /v1/mandates/{mandateId}/suspend:
    post:
      operationId: suspendMandate
      ...
      responses: '200' Mandate
  /v1/mandates/{mandateId}/resume:
    post:
      operationId: resumeMandate
  /v1/mandates/{mandateId}/charges:
    post:
      operationId: createCharge
      parameters: Idempotency-Key required
      requestBody: ChargeRequest
      responses: '201' Charge
  /v1/charges/{chargeId}:
    get:
      operationId: getCharge
      responses: '200' Charge
  /v1/charges/{chargeId}/refunds:
    post:
      operationId: createChargeRefund
      requestBody: ChargeRefundRequest
      responses: '201' ChargeRefund
  /v1/charges/{chargeId}/refunds/{refundId}:
    get:
      operationId: getChargeRefund
      responses: '200' ChargeRefund
components:
  schemas:
    PaymentRequest: unchanged
    Payment: unchanged
    MandateRequest:
      type: object
      required: [tspId, limits, paymentPurpose]  ... hmm
      properties:
        tspId: {type: string}
        paymentPurpose: {type: string}
        limits: {$ref: '#/components/schemas/MandateLimits'}
        confirmationThreshold: {type: integer, description: Порог суммы, выше которого требуется подтверждение плательщика, в копейках}
        period: {type: string, enum: [DAY, WEEK, MONTH, YEAR]}? maybe in limits
        webhookUrl: {type: string, format: uri}? optional override
    MandateLimits:
      type: object
      required: [currency, maxAmountPerCharge, maxAmountPerPeriod]
      properties:
        currency: {type: string, enum: [RUB]}
        maxAmountPerCharge: {type: integer}
        maxAmountPerPeriod: {type: integer}
        period: {type: string, enum: [DAY, WEEK, MONTH, YEAR]}
        confirmationThreshold: {type: integer}
    Mandate:
      type: object
      required: [mandateId, tspId, status, limits, currency]
      properties:
        mandateId: {type: string}
        tspId: {type: string}
        status: {type: string, enum: [PENDING_CONSENT, ACTIVE, SUSPENDED, REVOKED, EXPIRED]}
        limits: {$ref: MandateLimits}
        consentUrl: {type: string, nullable: true}
        consentQrImage: {type: string, nullable: true}
        activatedAt: {type: string, format: date-time, nullable: true}
        expiresAt: {type: string, format: date-time, nullable: true}
        createdAt: ...
    ChargeRequest:
      type: object
      required: [amount, billingPeriod]
      properties:
        amount: {type: integer, description: Сумма в копейках}
        billingPeriod: {type: string, description: Идентификатор итерации подписки (например, 2026-10), детерминирует ключ идемпотентности}
        merchantOrderId: {type: string}
        description: {type: string}
    Charge:
      type: object
      required: [chargeId, mandateId, amount, status]
      properties:
        chargeId: {type: string}
        mandateId: {type: string}
        amount: {type: integer}
        status: {type: string, enum: [CREATED, AWAITING_CONFIRMATION, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED]}
        confirmationRequired: {type: boolean}
        confirmationExpiresAt: {type: string, format: date-time, nullable: true}
        paymentId: {type: string, nullable: true}
        merchantOrderId: {type: string}
        createdAt: ...
        errorCode: {type: string, nullable: true}
    ChargeRefundRequest:
      type: object
      properties:
        amount: {type: integer}
        reason: {type: string}
    ChargeRefund:
      type: object
      required: [refundId, chargeId, amount, status]
      properties:
        refundId, chargeId, amount, status {enum: [PENDING, COMPLETED, FAILED]}, completedAt
```

Add a note comment at top about additive.

Also add headers X-Trace-Id? not present originally; skip to avoid scope.

I should also add descriptions noting new error codes. I'll add error responses with inline schema refs? Keep simple: descriptions.

Let me write it. Ensure YAML valid.

Also, for suspend/resume POST responses, include Idempotency-Key required.

Let me write the file.

I'll note in a comment: "Все добавления — аддитивны; существующие методы и схемы не изменены."

YAML comments with Cyrillic are fine.

Let me write.
Now the additive contract changes in `openapi/tsp-api.yaml` (existing paths/schemas preserved verbatim).

  `run_shell_command(command="cd /home/architect/project && (command -v node && node -e \"const fs=require('fs');const s=fs.readFileSync('openapi/tsp-api.yaml','utf8');c, description="Check node/yaml availability and save original")`

Let me validate the YAML and confirm existing parts unchanged. Let me run a quick YAML parse. Python isn't available (python3 not found). Maybe `python`? Or node? Let me try node or ruby. Actually openspec is node-based; there might be node. Let me check for a validator. Simpler: use `openspec` to validate? No. Let me try `node -e` with a YAML lib? Not guaranteed.

Let me just check with a simple tool. Try `python` (not python3). Or `yq`. Let me test.

Actually, I can verify YAML syntax by checking if any tool exists. Let me try `node --version` and `ruby -v`, `yq --version`.

Let me run a command.
Let me validate the YAML syntax and confirm the pre-existing contract sections are byte-identical to the original.

  `run_shell_command(command="cd /home/architect/project && git diff --no-color -- openapi/tsp-api.yaml | head -80", description="Review openapi diff (first part)")`

No yaml lib. Let me diff the original vs new to confirm only additions in the Payment paths/schemas. Use `git diff` on the file. Let me view diff.

  `run_shell_command(command="cd /home/architect/project && git diff --no-color -- openapi/tsp-api.yaml | grep -E \"^-\" | grep -v \"^---\" ; echo \"=== deletions above , description="Show all deleted lines in openapi")`

Let me check the rest of the diff to confirm Payment/PaymentRequest schemas unchanged (only additions after them).

  `run_shell_command(command="command -v ruby php yq perl 2>&1; echo \"---\"; ls /node/lib/node_modules 2>&1 | head; echo \"--- find yaml ---\"; find / -maxdepth 6 -type, description="Look for a YAML parser")`

Only the version line changed, everything else additive. 

Now let me verify YAML validity somehow. No yaml lib, no python. Maybe ruby available? Or use `openspec`'s bundled yaml (it's a node CLI). Let me check if there's a global npm module. Try `npx --no-install yaml`? Not available offline. 

Alternative: I can do a lightweight structural check via node by requiring the yaml parser from openspec's install location. Too fragile.

Let me just try `ruby -ryaml -e`. Check ruby.

Actually, another approach: find the yaml module in the openspec package or qwen. Let me search for node_modules/yaml. Let me just try a few.

Hmm, simpler: install nothing. I'll do a manual sanity review — the YAML is straightforward and I wrote consistent indentation. But a syntax error would be bad. Let me check for a YAML parser.

Let me try `ls /node/lib/node_modules`, and `command -v ruby php`.

  `run_shell_command(command="cd /home/architect/project && NODE_PATH=/node/lib/node_modules/openclaw/node_modules node -e \"\nconst YAML=require('yaml');\nconst fs=requ, description="Parse openapi YAML and verify structure")`

There's a yaml module at /node/lib/node_modules/openclaw/node_modules/yaml. Let me use node with NODE_PATH to parse.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n, old_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n)`

YAML valid, Payment.status enum unchanged. 

Now update docs/contracts/tsp-api.md additively (document new methods/schemas/events/error codes) and docs/contracts/opkc-adapter.md (add mandate methods/events). The user deliverable 3 mentions contracts (openapi). But coherence demands the .md contract updated too. My tasks.md references it. Let me add sections to both docs additively — appended sections, not modifying existing.

For docs/contracts/tsp-api.md: append a new section "## 8. Подписки СБП (v0.2.0, аддитивно)" documenting:
- mandate endpoints, charge endpoints, refunds by charge
- statuses (mandate, charge)
- new webhook events subscription.*/charge.*
- new error codes MANDATE_NOT_ACTIVE, LIMIT_EXCEEDED
- compatibility note
Also update header "Версия контракта: 0.1" → mention 0.2 additive? The header says "Версия контракта: 0.1 (нестабильная...)". I could append note. Editing the header is a modification. Additive approach: add a note. Let me update the Status/version line minimally to reference v0.2? Hmm, "меняй только тем способом, который принят". The contract .md is draft; adding a section is fine. I'll also add one line to §6 Версионирование? Not necessary.

I'll append section 8 and note the additive version. Actually the doc's §7 "Открытые вопросы (для A1)" exists. I'll insert section 8 after §7? Better to insert before §7 or after. I'll append after §7 as "## 8. Подписки СБП — расширение v0.2.0 (аддитивно)".

Hmm, but §7 is "Открытые вопросы" — appending a content section after open questions is odd. Let me insert the new section between §6 and §7. Let me find the anchor: "## 7. Открытые вопросы (для A1)". I'll insert before it.

Let me construct.

For opkc-adapter.md: append new section "## 10. Подписки (рекуррентные платежи) — расширение контракта" documenting methods registerMandate/getMandateState/cancelMandate/createCharge and events mandate.activated/mandate.suspended/mandate.revoked/charge.result. Insert before "## 9. Открытые вопросы". Actually §9 is "Открытые вопросы". Insert new section §10 after §9? Or before. I'll append a section after §9 as §10, or better insert as new §9 and renumber? Renumbering edits existing headings — avoid. I'll add "## 10. Расширение: мандаты подписки и рекуррентные списания (v0.2, для addendum RFP)" after §9. Slight ordering oddity but avoids renumbering.

Hmm, cleaner: insert before "## 9. Открытые вопросы" as "## 8.1..."? no.

I'll insert the new section right after §8 (Требования к вендору) and before "## 9. Открытые вопросы", naming it "## 8a."? Ugly. Let me just append after §9 as "## 10. ...". Actually the doc ends at §9. Appending §10 preserves numbering and reads fine.

Wait, opkc-adapter sections: 1 Назначение, 2 Транспорт, 3 Синхронные, 4 Асинхронные события, 5 Идемпотентность, 6 Таймауты, 7 NFR, 8 Требования к вендору, 9 Открытые вопросы. I'll append §10? That places new functionality after open questions. Acceptable but not ideal. Alternatively I can append the new methods to the §3 and §4 tables — that's modifying tables (additive rows, still additive). Additive rows to an existing table is fine and natural. But then section naming. Hmm.

Simplest coherent: insert a new section between §8 and §9, numbered "## 9. Подписки..." and renumber "Открытые вопросы" to 10. Renumbering one heading is a minor edit. But it changes existing text. The user said change accepted files only by the accepted method — renumbering a draft contract's section is not a semantic change. I think it's fine, but to be safe and strictly additive, I'll append "## 10. Расширение контракта: мандаты подписки и рекуррентные списания" at the end and add a forward reference line. Good enough.

Actually, let me reconsider: is updating these two .md contracts in scope? The user's deliverable 4 explicitly says openapi/tsp-api.yaml. But deliverable 3 (architecture decision) and the handoff to implementers benefit from the contract docs. My tasks.md lists updating them as tasks (6.2, 5.4) — i.e., part of apply, not necessarily now. Hmm. I wrote tasks 5.4 and 6.2 as future tasks. So maybe I should NOT update them now, and let apply do it. But then the "architectural package" is less complete.

Decision: I'll add the additive sections now for coherence (the package should be self-contained), and update tasks 6.2/5.4 to reflect they're drafted (or keep as verification). Actually the tasks say "Обновить ... синхронно" — if I do it now, the task becomes partially done. That's fine; tasks track apply work and can be checked off/adjusted. But to avoid inconsistency, I'll keep tasks as is (they'll be verified in apply). Hmm, but guidance says don't collect docs into final group; each group lands its own docs. Group 5 and 6 include doc updates — good.

I think the cleanest story: The architectural package includes the contract *delta* expressed in the OpenSpec spec + openapi yaml (the machine contract). The human-readable .md contracts are updated during apply (tasks 5.4, 6.2). But leaving them inconsistent now (yaml v0.2 vs md v0.1) is a coherence gap a reviewer would flag.

I'll add concise additive sections to both .md files now, so the package is coherent. Then adjust tasks 5.4/6.2 to be verification tasks ("проверить синхронность") rather than "обновить". Let me do that.

Let me write the tsp-api.md section.

Insert before "## 7. Открытые вопросы (для A1)".

Content:

## 7. Подписки СБП — расширение контракта (v0.2.0, аддитивно)

Статус: Draft (связанное изменение — `openspec/changes/sbp-recurring-payments`). Все изменения аддитивны: существующие методы §3, схемы и перечисление `Payment.status` не изменены; `openapi/tsp-api.yaml` — v0.2.0.

Общие правила: те же транспорт, авторизация, идемпотентность (`Idempotency-Key` обязателен для всех POST) и коды ошибок, что в §1–2 и §4; добавляются коды `MANDATE_NOT_ACTIVE` (422), `LIMIT_EXCEEDED` (422).

Методы:
- POST /v1/mandates — регистрация мандата подписки (без списания); ответ 201 Mandate (PENDING_CONSENT, consentUrl).
- GET /v1/mandates/{mandateId}
- POST /v1/mandates/{mandateId}/suspend; POST .../resume (приостановка/возобновление со стороны ТСП)
- POST /v1/mandates/{mandateId}/charges — инициирование списания; ответ 201 Charge
- GET /v1/charges/{chargeId}
- POST /v1/charges/{chargeId}/refunds; GET .../refunds/{refundId}

Статусы мандата: PENDING_CONSENT | ACTIVE | SUSPENDED | REVOKED | EXPIRED; REVOKED/EXPIRED терминальны.
Статусы списания: CREATED | AWAITING_CONFIRMATION | PAID | CREDITED | COMPLETED | FAILED | EXPIRED | REFUNDED. AWAITING_CONFIRMATION — сумма выше порога, требуется подтверждение плательщика.

Ключевой инвариант: зачисление только из PAID (AD-005/AD-010); AWAITING_CONFIRMATION подтверждением не является.

События вебхуков (дополняют §5): subscription.activated, subscription.suspended, subscription.revoked, subscription.expired, charge.completed, charge.failed, charge.expired; заголовки и подпись — как в §5, дедупликация по X-SBP-Event-Id.

Идемпотентность списания: Idempotency-Key + детерминированный ключ (mandateId + billingPeriod).

Then §7 Открытые вопросы stays as §7? That would duplicate number 7. Ugh. I'd be inserting "7" before existing "7". Bad.

Rename the inserted heading to "## 7. Подписки СБП ..." and existing "## 7. Открытые вопросы" stays — duplicate numbering. Not acceptable.

Better: insert as "## 8." at the end (after §7 Открытые вопросы). Ordering: §7 open questions then §8 new section — acceptable? Reads oddly.

Alternative: append to §3 as subsection "### 3.6 ..."? The methods section is §3 with 3.1-3.5. Add "### 3.6 Подписки СБП (v0.2.0)"? That's additive and keeps numbering. But it's a large addition inside §3. Then add webhook events to §5 as a bullet. And new error codes in §4 list. Additive edits: adding rows/items to existing lists. This is the most natural and truly additive (no renumbering).

Plan for tsp-api.md:
- In §4 canonical codes line, append new codes. Edit: "Канонические коды: ... `INTERNAL` (500)." → add "Дополнительно (v0.2.0, подписки): `MANDATE_NOT_ACTIVE` (422), `LIMIT_EXCEEDED` (422)."
- In §5 events list, append subscription/charge events line.
- Add §3.6 with mandate/charge methods.
- In §6 versioning, optionally note additive. Skip.

Actually adding 3.6 after 3.5 and before "## 4." — fine.

Hmm, but §3 is titled "Методы" with 3.1-3.5. Adding 3.6 "Подписки СБП (v0.2.0)" is clean.

Let me do that. And §4 codes, §5 events.

For opkc-adapter.md: add rows to §3 table? Additive rows to table — good. And §4 events table new rows. And a note. That's natural. But the table columns for mandate ops need "Метод | Направление смысла | ...". I can add rows:
| `registerMandate` | регистрация мандата подписки | `reference` (=`mandateId`), реквизиты ТСП, лимиты | `jobId`/`ACCEPTED` (результат — событием) | 5 c |
| `getMandateState` | состояние мандата | `mandateRef` | `ACTIVE`/`PENDING`/`SUSPENDED`/`REVOKED`/`EXPIRED`/`UNKNOWN` | 3 c |
| `cancelMandate` | отмена мандата (со стороны ТСП) | `mandateRef`, `reason` | `CANCELLED` | 3 c |
| `createCharge` | инициирование списания по мандату | `reference` (=`chargeId`), `mandateRef`, `amount` | `ACCEPTED` (результат — событием) | 5 c |

And §4 events:
| `mandate.activated` | согласие подтверждено | `mandateRef`, `activatedAt` |
| `mandate.suspended` | мандат приостановлен | `mandateRef`, `reasonCode?` |
| `mandate.revoked` | согласие отозвано | `mandateRef`, `revokedAt` |
| `mandate.expired` | мандат истёк | `mandateRef` |
| `charge.settled` | результат списания (оплачено/отклонено/истекло) | `chargeRef` (=`chargeId`), `qrId?`, `amount`, `status`, `reasonCode?` |

Good — additive rows.

This is cleaner than new sections. Let me do edits on both .md files with additive rows/items.

Let me read the exact snippets to edit.

For tsp-api.md §3.5 ends with:
"### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`

## 4. Ошибки (RFC 9457, Problem Details)"

I'll insert 3.6 before "## 4. Ошибки".

Insert text:

### 3.6 Подписки СБП — мандаты и рекуррентные списания (v0.2.0, аддитивно)

Статус: Draft; связанное изменение — `openspec/changes/sbp-recurring-payments`. Существующие методы §3.1–3.5 и схемы не изменены.

- `POST /v1/mandates` — регистрация мандата подписки без списания; `Idempotency-Key` обязателен. Ответ `201 { mandateId, tspId, status: "PENDING_CONSENT", limits, consentUrl }`. Лимиты иммутабельны после активации.
- `GET /v1/mandates/{mandateId}` — состояние мандата (`PENDING_CONSENT | ACTIVE | SUSPENDED | REVOKED | EXPIRED`; `REVOKED`/`EXPIRED` терминальны).
- `POST /v1/mandates/{mandateId}/suspend` и `POST /v1/mandates/{mandateId}/resume` — приостановка и возобновление списаний со стороны ТСП.
- `POST /v1/mandates/{mandateId}/charges` — инициирование рекуррентного списания; `Idempotency-Key` обязателен. Тело `{ amount, billingPeriod, merchantOrderId?, description? }`. Ответ `201 Charge`. Статусы: `CREATED | AWAITING_CONFIRMATION | PAID | CREDITED | COMPLETED | FAILED | EXPIRED | REFUNDED`; `AWAITING_CONFIRMATION` — сумма выше порога подтверждения, требуется действие плательщика.
- `GET /v1/charges/{chargeId}` — состояние списания.
- `POST /v1/charges/{chargeId}/refunds` и `GET /v1/charges/{chargeId}/refunds/{refundId}` — возврат по списанию (существующая сага, `refundId`).

Ключевой инвариант: зачисление возможно только из `PAID` (AD-005, AD-010); `AWAITING_CONFIRMATION` подтверждением не является. Идемпотентность списания: `Idempotency-Key` + детерминированный ключ `mandateId`+`billingPeriod`.

Then §4 codes: edit the line.
Old: "Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку."
New: append "Дополнительно (v0.2.0, подписки): `MANDATE_NOT_ACTIVE` (422), `LIMIT_EXCEEDED` (422)."

Then §5 events list:
Old:
"События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`"
New: add lines:
"- `subscription.activated` / `subscription.suspended` / `subscription.revoked` / `subscription.expired` — события мандата (v0.2.0)
- `charge.completed` / `charge.failed` / `charge.expired` — события рекуррентного списания (v0.2.0)"

Good.

Now opkc-adapter.md edits: add table rows.

§3 table last row: "| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |"

Add after it:
"| `registerMandate` | регистрация мандата подписки | `reference` (= `mandateId` ядра), реквизиты ТСП, лимиты | `jobId`, статус `ACCEPTED` (результат — событием) | 5 c |
| `getMandateState` | состояние мандата (сверка) | `mandateId` (ОПКЦ) | `ACTIVE`/`PENDING`/`SUSPENDED`/`REVOKED`/`EXPIRED`/`UNKNOWN` | 3 c |
| `cancelMandate` | отмена мандата (со стороны ТСП) | `mandateId`, `reason` | `CANCELLED` | 3 c |
| `createCharge` | инициирование рекуррентного списания | `reference` (= `chargeId` ядра), `mandateId`, `amount` | `ACCEPTED` (результат — событием) | 5 c |"

§4 events table last row: "| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |"
Add after:
"| `mandate.activated` | согласие плательщика подтверждено | `mandateRef` (= `mandateId` ядра), `activatedAt` |
| `mandate.suspended` | мандат приостановлен | `mandateRef`, `reasonCode?` |
| `mandate.revoked` | согласие отозвано плательщиком | `mandateRef`, `revokedAt` |
| `mandate.expired` | мандат истёк | `mandateRef` |
| `charge.settled` | результат рекуррентного списания | `chargeRef` (= `chargeId` ядра), `status`, `amount`, `reasonCode?`, `paidAt?` |"

Also the §3 intro "Статусные модели ОПКЦ (`PAID`, ...)" — fine.

Let me apply the edits.

Also note: these are "Draft" contract docs, so additive edits are the accepted method.

Let me do the edits with the edit tool.
Now aligning the human-readable contracts with the additive delta (additive rows/sections only).

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`
  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` — истёк TTL, old_string="- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` — истёк TTL)`
  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t, old_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t)`

Now opkc-adapter.md additive rows.

§3 table last row: "| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |"

Add 4 rows after.

§4 events table last row: "| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |"

Add 5 rows after.

Let me do the edits.

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |\n| `mandate.activated` | , old_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |")`
  `edit(file_path="/home/architect/project/openspec/changes/sbp-recurring-payments/tasks.md", new_string="- [ ] 5.4 Синхронизировать `docs/contracts/opkc-adapter.md` с реализацией (новые методы/события/NFR) как основу addendum RFP; проверка — до, old_string="- [ ] 5.4 Обновить `docs/contracts/opkc-adapter.md` (новые методы/события/NFR) как основу addendum RFP; проверка — документ покрывает пункт)`

Now update the vendor-rfp.md? tasks 1.6 says addendum is a gate task, not done now. I'll leave RFP as-is (it's a gate task). Good.

Also tasks 5.4 and 6.2 said "Обновить ... документ" — I've now done those updates proactively. To keep coherence, let me adjust those two tasks to be verification tasks. Actually, re-reading task 5.4: "Обновить `docs/contracts/opkc-adapter.md` (новые методы/события/NFR) как основу addendum RFP; проверка — документ покрывает пункты спеки". I did update it. Task 6.2: "Обновить `docs/contracts/tsp-api.md` ... синхронно". I did.

Options: (a) leave tasks as-is (apply will verify), (b) adjust to "Проверить, что ...". Since the package now includes those doc updates, marking/rewording is more accurate. But tasks are a plan for the future apply phase — the docs may still need finalization after gate decisions (e.g., лимиты values). I'll reword slightly to reflect they exist and must be kept in sync / finalized. Let me update:

5.4 → "Синхронизировать `docs/contracts/opkc-adapter.md` с реализацией (новые методы/события/NFR) как основу addendum RFP; проверка — документ покрывает пункты спеки `sbp-opkc-subscription-transport`"

6.2 → "Поддерживать `docs/contracts/tsp-api.md` синхронно с `openapi/tsp-api.yaml` (новые методы, события, коды); проверка — документ и YAML не расходятся"

Minor. Let me edit.

Actually, this is fine-tuning; worth it for coherence. Let me do both edits.

Then: check CONSTRAINTS.yaml fitness — the rule "adr-no-placeholders" is must_not_contain pattern '<!--' in docs/adr/*.md. My new ADR files — do they contain '<!--'? No. Good. rule "nfr-measurable" must_contain '99,95' — still present. "abs-credit-only-from-paid" must_contain 'только из состояния `PAID`' in ADR-005 — unchanged. Good.

Also "adr-set-complete" file_exists ADR-001 — fine.

Is there an `arch` CLI to run `arch control check`? Probably not installed. Let me check `command -v arch`. If available, run it. Let me check.

Also I should run openspec validate again and maybe `openspec doctor`.

Also: the change uses capabilities whose spec dirs are under the change; main specs empty. Fine.

Let me also consider: should I add a new "capability" spec for tsp-api? Not needed.

Let me also double-check: the `.arch-handoff/CONSTRAINTS.yaml` mentions fitness rules for the decision stage. Could add new rules for the subscriptions (e.g., spine contains AD-009). That'd be "handoff regeneration" — the MANIFEST/RUBRIC mention handoff regenerates constraints after stack choice. Adding a fitness rule could be nice but the user didn't ask, and tasks cover fitness. I'll skip to avoid scope creep. Hmm — but "методические навыки и инструменты — используй их по назначению" might imply regenerating the handoff package. The handoff TASK.md is for the walking skeleton (previous change), not this one. This change has no code yet (planning). So no handoff regeneration needed now. I'll note it.

Now let me run the arch check if the tool exists, and re-validate openspec.

Let me also verify the new ADRs don't contain '<!--'.

Let me batch: command -v arch; openspec validate --strict; grep for '<!--' in docs/adr.

Actually grep_search for '<!--' in docs/adr/*.

Let me run.
Now let me reword the two doc-sync tasks for accuracy, then run the repo's checks (fitness rules + OpenSpec validation).

  `edit(file_path="/home/architect/project/openspec/changes/sbp-recurring-payments/tasks.md", new_string="- [ ] 6.2 Поддерживать `docs/contracts/tsp-api.md` синхронно с `openapi/tsp-api.yaml` (новые методы, события, коды); проверка — документ и , old_string="- [ ] 6.2 Обновить `docs/contracts/tsp-api.md` (новые методы, события, коды) синхронно с `openapi/tsp-api.yaml`; проверка — документ и YAML)`
  `edit(file_path="/home/architect/project/openspec/changes/sbp-recurring-payments/tasks.md", new_string="- [ ] 6.1 Подтвердить на ревью аддитивные изменения `openapi/tsp-api.yaml` (мандаты и списания, версия 0.2.0) и зафиксировать их как v1.0-d, old_string="- [ ] 6.1 Внести аддитивные изменения в `openapi/tsp-api.yaml` (пути мандатов и списаний, новые схемы, новые коды ошибок); проверка — валид)`

Now run checks: check for `arch` CLI, validate openspec, and grep for forbidden `<!--` in new ADRs.

Note: task 6.1 says "Внести аддитивные изменения в openapi/tsp-api.yaml" as a future task, but I already did it. Similar tension. Hmm. To avoid inconsistency, I could mark 6.1 as done `- [x]`. Actually the apply phase parses checkboxes; marking done reflects reality. But the package is being "prepared", and 6.1 delivered. Let me mark 6.1 as [x] since openapi is already updated? Hmm — but then the tasks file reflects partial completion which is odd for a proposal artifact. 

Better: leave tasks as a clean plan; the artifacts being pre-drafted is fine (the apply phase verifies). OpenSpec tasks describe remaining implementation steps; the contract YAML is a planning artifact I produced (spec-level). Actually the contract IS part of the design/spec, so having it done at planning time is normal; the task 6.1 then is redundant. 

I think the cleanest is to reframe 6.1 as verification rather than authoring, or mark done. Let me reframe: "6.1 Утвердить аддитивные изменения `openapi/tsp-api.yaml` (уже подготовлены) — проверка: валидация OpenAPI проходит, diff содержит только добавления". Hmm, that's awkward too.

Honestly, small thing. Let me leave 6.1 as is — a reviewer understands openapi changes are proposed in the package and ratified/applied. But "Внести" implies future. The openapi change is already in the working tree. To be accurate, I'll mark 6.1 checked `- [x]` since done. And 5.4/6.2 are sync tasks (partially done). Hmm, inconsistent.

Let me step back: OpenSpec tasks track apply-phase progress. The proposal/design/specs are the plan. The openapi yaml is the contract artifact — I updated it as part of the architectural package (deliverable 4). It's legitimate for tasks to omit authoring it, but I listed it. I'll change 6.1 to reflect that it's authored and needs ratification/verification:

"- [ ] 6.1 Подтвердить на ревью аддитивные изменения `openapi/tsp-api.yaml` (мандаты и списания) и зафиксировать версию 0.2.0; проверка — валидация OpenAPI проходит, diff содержит только добавления"

That's honest. Let me do that.

Similarly 5.4/6.2 now say synchronize/keep in sync — fine.

Let me edit 6.1.

Then run checks.

  `run_shell_command(command="cd /home/architect/project && echo \"=== arch CLI ===\"; command -v arch || echo \"arch not installed\"; echo \"=== openspec validate ===\", description="Run repo fitness rules and OpenSpec validation")`

Now running the repository's own checks: fitness rules from `CONSTRAINTS.yaml` and OpenSpec validation.

  `run_shell_command(command="cd /home/architect/project && git status --short && echo \"=== diffstat ===\" && git diff --stat && echo \"=== untracked ===\" && git statu, description="Show final git status and diffstat")`

`/usr/bin/arch` is the Unix `arch` command (prints machine arch), not the arch CLI. So no arch control check tool. Fitness rules manually verified — all pass.

OpenSpec validates: 0/41 tasks, valid.

Now, let me do a final review of everything: git status, diff stat. And verify the design/specs consistency (e.g., error codes used: MANDATE_NOT_ACTIVE, LIMIT_EXCEEDED — consistent across spec, design, contracts, openapi). Yes.

Let me also check that the proposal's capability paths match the spec dirs: sbp-mandates, sbp-recurring-charges, sbp-opkc-subscription-transport. Proposal lists exactly these. Good.

Now a couple of refinements to consider:
1. The user asked for "Оценка значимости изменения и маршрута" — in proposal Why. Good.
2. "Влияние на принятую архитектуру" — design table. Good.
3. "Архитектурное решение с альтернативами, последствиями, обратимостью" — ADR-008/009 + design decisions. Good.
4. "Изменения контрактов без поломки" — openapi + design D9 + tsp-api.md. Good.
5. "Измеримые NFR" — docs/nfr.md §7 + design. Good.
6. "Критерии приёмки и план отката" — specs scenarios + tasks group 9 + design Migration Plan. Good.
7. "Что остаётся на решение человека-архитектора" — design Open Questions + tasks group 1. Good.

One more: the user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." I added Proposed blocks to the spine and new Proposed ADRs — consistent with the repo's own status system. I did not modify existing ADRs or ratify anything. Good.

Should I also record memory? The system prompt has auto memory. It says save durable cross-conversation knowledge. Hmm — is there something worth saving? Possibly a project memory about the OpenSpec methodology being the accepted way to change decisions, and that автоплатежи moved into scope. But "Do not save: Content already in QWEN.md or AGENTS.md", "project structure", "git history". The fact that this repo uses openspec as the method for changes — that's derivable from the repo. Hmm. The memory guidance says save explicitly when user asks; user didn't. I could save a project memory that a new architectural change "sbp-recurring-payments" is under review (ongoing work). That's a legitimate project memory (ongoing work/initiative not derivable from code... though it IS in the repo now). Since it's recorded in the repo (openspec change + spine section), it's derivable. I'll skip memory writes — the repo is the source of truth, and the guidance says don't save what's in the project.

Hmm, actually there is one durable, non-obvious thing: the project's method = OpenSpec change + Proposed ADR/spine additions for changing the accepted decision, and that `/usr/bin/arch` is NOT the arch CLI (no arch control tool installed). The latter is an environment fact. Eh, minor. And the output-language preference is already set. I'll add one concise project memory about the accepted method for changing the decision, since the user explicitly framed it ("меняй только тем способом, который принят в этом репозитории") — that's project-wide convention guidance, arguably "feedback" type (project-scoped). Actually the guidance says feedback memories: "guidance on how to approach work... project only for project-wide conventions." This qualifies. And it's non-obvious (spine Proposed blocks + OpenSpec + proposed ADRs, not editing accepted ADRs). Let me save it. But careful: "Do not save: project structure, conventions, architecture" — hmm, "conventions" are excluded. This is a workflow convention. The exclusion says "Code patterns, conventions, architecture, file paths, or project structure (read the project instead)". So a convention → don't save. Ugh. I'll skip memory. Fine.

Actually the user didn't ask to remember anything. Skip.

Now let me do a final git status/diff summary and present the result.

Let me get git status and a compact file list.
All checks pass. Let me review the final state of the working tree.


Everything is in place. 2 deletions total (version line in openapi + one line in tsp-api.md? Let me not worry; diffstat says 2 deletions across files. Actually tsp-api.md shows "19 ++++++-" -> 18 insertions 1 deletion? The deletion is the canonical codes line replaced (same line + addition = counted as 1 del/1 add). That's fine, it's an additive edit within a line. Hmm — technically that replaced line. It's additive semantics. Fine.)

Let me present the final summary: created/modified files, and the 7 deliverables mapping, plus what remains for the human architect, verification results.

The user asked: "Когда закончишь, кратко перечисли созданные и изменённые файлы."

Let me write a concise but complete final response in Russian.

I should mention:
- Method used: OpenSpec change (opsx-propose) as the accepted way; new ADRs/spine blocks as Proposed (not ratified).
- Verification: openspec validate --strict passes; YAML parses; only additive diff (only info.version line changed in openapi); fitness rules from CONSTRAINTS.yaml pass.
- Mapping to the 7 deliverables.
- Files created/modified.
- Note: code not written; transport blocked on external input.

Also mention the two decisions the user made were baked in.

Let me keep it structured but not overly long.

One caveat to be honest about: there's no `arch control check` CLI installed (the `arch` binary is the Unix arch command), so I verified the CONSTRAINTS.yaml fitness rules manually with equivalent checks. State that.

Also note the significance scoring axes are my reconstruction (the repo only records "11/15"), so marked as assessment.

Let me write the final answer.
# Архитектурный пакет подготовлен

Изменение оформлено принятым в репозитории способом: **OpenSpec-изменение** `sbp-recurring-payments` (через методический навык `openspec-propose`) + новые ADR и spine-блоки **в статусе Proposed** (ратифицируется человеком на гейте). Принятые файлы решения не переписывались: изменения только аддитивные, существующие ADR-001…007 и правила AD-001…008 не затронуты.

Принятые вами решения зафиксированы: **отдельная регистрация мандата без первого платежа**; **тихое списание в пределах лимитов, подтверждение плательщика сверх порога**.

## Соответствие запрошенным пунктам

| # | Что просили | Где |
|---|---|---|
| 1 | Оценка значимости и маршрута | `proposal.md` — таблица 5 осей, **13/15 → Critical** (осознанно помечено как оценка: источник хранит только «11/15») |
| 2 | Влияние на архитектуру и инварианты | `design.md` — таблица «Preserved / Extended / Touched / Unchanged» по AD-001…AD-008 |
| 3 | Архитектурное решение: альтернативы, последствия, обратимость | `ADR-008` (мандат, отзыв), `ADR-009` (списания, `Charge`), `design.md` — решения D1–D9 |
| 4 | Изменения контрактов без поломки | `openapi/tsp-api.yaml` (v0.2.0, только добавления), `docs/contracts/tsp-api.md`, `docs/contracts/opkc-adapter.md` |
| 5 | Измеримые NFR | `docs/nfr.md` §7 + сводка в `design.md` |
| 6 | Критерии приёмки и план отката | сценарии WHEN/THEN в трёх спеках, `design.md` → Migration Plan, `tasks.md` группа 9 |
| 7 | Что остаётся человеку-архитектору | `design.md` → Open Questions + `tasks.md` группа 1 (гейт A3) |

## Проверки (выполнены)

- `openspec validate sbp-recurring-payments --strict` → **valid**; `openspec status` → `4/4 artifacts complete`.
- `openapi/tsp-api.yaml` — YAML парсится; `Payment.status` неизменён; в diff **единственное удаление — строка `version`** (0.1.0→0.2.0), остальное только добавления.
- Fitness-правила `CONSTRAINTS.yaml` — прошли (нет `<!--` в ADR, spine без TODO/TBD/XXX, NFR измеримы, правило AD-005 на месте). Оговорка: отдельного CLI `arch control check` в окружении нет (`/usr/bin/arch` — системная утилита), поэтому правила проверены эквивалентными командами вручную.

## Созданные файлы

- `openspec/changes/sbp-recurring-payments/proposal.md`
- `openspec/changes/sbp-recurring-payments/design.md`
- `openspec/changes/sbp-recurring-payments/tasks.md` (41 задача, 9 групп)
- `openspec/changes/sbp-recurring-payments/specs/sbp-mandates/spec.md`
- `openspec/changes/sbp-recurring-payments/specs/sbp-recurring-charges/spec.md`
- `openspec/changes/sbp-recurring-payments/specs/sbp-opkc-subscription-transport/spec.md`
- `docs/adr/ADR-008-model-podpisok-sbp-mandat-i-prioritet-otzyva-soglasiya.md` (Proposed)
- `docs/adr/ADR-009-rekurrentnye-spisaniya-po-mandatu-limity-i-podtverzhdenie.md` (Proposed)
- `docs/spec/mandate-state-machine.md`

## Изменённые файлы (аддитивно)

- `ARCHITECTURE-SPINE.md` — новые Proposed-инварианты **AD-009/AD-010** + раздел «Изменения в рассмотрении» (пункт roadmap «автоплатежи» переведён в scope)
- `docs/nfr.md` — раздел §7 «Рекуррентные списания» + внешний вход по регламентам НСПК
- `openapi/tsp-api.yaml` — пути и схемы мандатов/списаний (v0.2.0)
- `docs/contracts/tsp-api.md` — §3.6, новые коды ошибок и вебхуки
- `docs/contracts/opkc-adapter.md` — методы и события мандатов в контракте адаптера (основа addendum RFP)

## Ключевые развилки, оставленные человеку

Регуляторное подтверждение механизма подписок ОПКЦ (`[ТРЕБУЕТ ПРОВЕРКИ]` — блокирует транспорт, не ядро); юридическая модель согласия/отзыва и политика для списаний «в полёте»; бизнес-значения лимитов и порога; addendum к RFP вендора (влияет на ADR-007); ратификация AD-009/AD-010 и принятие ADR-008/009.

Код не писался. Дальнейшие шаги по методологии: ревью пакета → `/opsx-apply` для реализации, после прохождения гейта.
