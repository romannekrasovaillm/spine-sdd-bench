<!-- источник: <HARNESS>/runs/cells/superpowers-r2/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-cells-superpowers-r2-ws/chats/08b3b2e0-5ca3-4c5e-9cf1-2d24922fbdf4.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `skill(skill="superpowers:brainstorming")`

Let me start by understanding the task. The user wants me to act as a solution architect for a bank. The repository is an accepted decision "Payment Gateway SBP (C2B acceptance)". I need to prepare an architectural package for a change: recurring C2B debits by payer consent — SBP subscriptions.

The user explicitly says: "Код не пиши" (don't write code), but there's a mention of "Изменения контрактов (`openapi/tsp-api.yaml`)" — changes to contracts. So I'll need to modify the openapi yaml file as part of the architectural package.

Important instructions:
- "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." (Methodological skills and tools may be installed in the project — use them as intended.)
- There's a strong emphasis on skills via the GEMINI.md and superpowers using-superpowers skill. The available skills include superpowers:brainstorming, writing-plans, etc.

The using-superpowers skill says: invoke relevant skills BEFORE any response or action. The brainstorming skill says "You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior."

This is a creative/architecture work task. However, the user has given a very detailed and specific request with a clear deliverable list (7 items). The task is essentially: prepare an architectural package.

Let me think about which skills apply:
1. superpowers:using-superpowers — establishes how to use skills. Already loaded (GEMINI.md context includes it).
2. superpowers:brainstorming — "before any creative work". This task is architectural design. But the user has already specified exactly what they want (7 deliverables). Brainstorming explores intent/requirements/design. 

Actually, let me reconsider. The task is quite well-specified. But it's a complex architectural task. The brainstorming skill might be overkill, but the using-superpowers skill is extremely emphatic: "If you think there is even a 1% chance a skill might apply... you MUST invoke."

However, I also need to be pragmatic. The user has given a detailed brief. Let me think about what's actually needed here.

Actually, there's a critical consideration. The instruction says "Перед созданием плана: если вы ещё не провели мозговой штурм, сначала вызовите навык мозгового штурма." (Before entering plan mode: if you haven't brainstormed, invoke brainstorming skill first.)

But the user hasn't asked me to enter plan mode. They've asked me to produce an architectural package.

Let me think about the actual workflow here. This is a substantial task that requires:
1. Reading the existing architecture (ARCHITECTURE-SPINE.md, docs/, openapi/, .arch-handoff/)
2. Understanding the change (recurring C2B debits / SBP subscriptions)
3. Producing the architectural package with 7 deliverables

The deliverable is essentially documentation/architecture changes. This is "creative work" in the sense of designing.

Given the strong emphasis on skills, I should:
1. First, read the repository to understand the existing architecture.
2. Use brainstorming skill to explore the design, OR given the detailed brief, proceed with writing a plan.

Actually, let me re-read the core mandates: "Confirm Ambiguity/Expansion: Do not take significant actions beyond the clear scope of the request without following the active interaction mode's question guidance."

And the GEMINI.md says skills take precedence.

Let me think about what's the right approach. The task is well-defined enough. But there's significant ambiguity in the domain (SBP recurring payments — how does the CBR's SBP actually support this? This is a real domain with specific mechanisms).

Actually, let me step back. The user is asking me to produce a concrete architectural package. This is a real, substantial deliverable. The right approach is:

1. Invoke relevant skills (brainstorming, possibly writing-plans).
2. Read the repository thoroughly.
3. Produce the package.

But I need to be careful not to over-engineer the process. Let me consider: the user said "используй их по назначению" (use them as intended). This is a directive to use the skills.

Let me first announce what I'm about to do, then invoke the brainstorming skill (since this is creative architectural work), then read the repository.

Actually, wait. Let me reconsider the brainstorming skill. Its description: "You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation."

This task is "modifying behavior" (adding recurring payments). So brainstorming applies. But the user has already given a very detailed spec of what they want. Brainstorming would explore further intent/requirements/design.

However, I think there's a real tension here. The brainstorming skill likely involves asking the user clarifying questions. The user has given a fairly complete brief. But there might be genuine architectural ambiguities to resolve.

Let me actually read the brainstorming skill first to understand what it asks me to do, and also read the repository.

Actually, the meta-rule from using-superpowers: invoke the skill BEFORE any response. So my first action should be to invoke the brainstorming skill (and possibly using-superpowers is already loaded).

Let me be careful about the order. The using-superpowers skill is already in my context (via GEMINI.md import). It says I must invoke relevant skills. The most relevant process skill here is brainstorming (creative work) and possibly writing-plans (multi-step task).

Let me invoke brainstorming first. Actually, let me think — should I read the repo first or invoke skill first? The rule says invoke skill BEFORE exploring the codebase: "Let me explore the codebase first" → "Skills tell you HOW to explore. Check first."

So: invoke brainstorming skill first.

Let me do that. I'll invoke the skill via the Skill tool.

Actually, I realize I should be thoughtful. Let me invoke the brainstorming skill to understand the process, then proceed accordingly. I'll also need to read the repository files.

Let me start by invoking the brainstorming skill.

Wait, but I also want to consider whether brainstorming is actually the right skill, or whether I should just proceed. The user's request is a well-scoped architecture task with clear deliverables. Brainstorming is for exploring intent before creative work. Here the intent is fairly clear, but the design space (how to implement SBP recurring payments) is genuinely open and needs exploration.

I'll invoke brainstorming. Let me announce and invoke.

Actually, let me reconsider once more the overall plan and not get too caught up. The key deliverables are clear. My workflow:

1. Invoke brainstorming skill (process skill for creative/design work).
2. Read the repository (architecture spine, docs, openapi, handoff).
3. Explore the design space (SBP recurring payments domain).
4. Produce the architectural package — likely as new files following the repo's conventions (ADR, changes to openapi, NFR updates, etc.).
5. Report.

Let me invoke the skill first.

I'll invoke `superpowers:brainstorming` via the Skill tool.

Let me do that now.
I'll start by loading the relevant methodology skill for this design task, then read the repository to understand the accepted architecture.

  `glob(pattern="**/*")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/README.md")`

Now I understand the brainstorming skill. This is clearly an **architectural** task — it changes how components fit together, alters interfaces others depend on (the openapi contract), and affects the accepted architecture.

Let me classify: This is architectural. The path is:
1. Explore project context
2. Ask clarifying questions
3. Propose 2-3 approaches
4. Present design
5. Write design doc
6. Spec self-review
7. User reviews written spec
8. Transition to implementation (writing-plans) — but actually, the user asked for an architectural package, not implementation.

Wait — but there's a nuance. The user's task has a specific deliverable shape that differs from the pure brainstorming flow. The user asked for:
1. Оценка значимости изменения и маршрута (change significance assessment and route)
2. Влияние на принятую архитектуру (impact on accepted architecture)
3. Архитектурное решение с альтернативами (AD with alternatives)
4. Изменения контрактов (contract changes)
5. Измеримые NFR
6. Критерии приёмки и план отката
7. Что остаётся на решение человека-архитектора

This maps onto the repo's existing structure (ADR, docs, .arch-handoff). So the deliverable is an architectural package in the repo's own format, not just a brainstorming spec.

So my process should be:
1. Explore project context (read all the files).
2. Since this is architectural and the user gave a detailed brief, I should still ask clarifying questions where genuinely needed, propose approaches, present design, etc. But the user also asked me to produce the full package in one go ("Когда закончишь, кратко перечисли созданные и изменённые файлы" — when you finish, briefly list created and modified files).

There's a tension: the brainstorming skill wants me to gate on approval at each stage (ask questions, propose approaches, present design sections, get approval, then write spec). But the user gave a comprehensive one-shot brief and expects a complete package.

However, the skill is emphatic about the HARD-GATE: "Before taking any implementation action... complete the selected path's prerequisites." And "Architectural: ... ask clarifying questions ... propose approaches ... present design ... get approval after each section ... write design doc ... user reviews spec ... then writing-plans."

But wait — the user's request is NOT to implement code. The user explicitly says "Код не пиши" (don't write code). The deliverable IS the architectural package (design docs, ADR, contract changes, NFR, acceptance criteria). So the "implementation" in this case is writing the architecture documents themselves.

Let me think carefully about how to reconcile this. The brainstorming skill is about turning ideas into designs. The user's request is essentially: "do the architectural design work and produce the package." 

The key question: should I do heavy interactive Q&A, or should I first explore the repo, understand it, and then either ask focused questions or produce the design?

Given:
- The user has provided a very detailed brief with exact deliverables.
- This is a domain (SBP recurring payments in a Russian bank context) that I have knowledge about.
- The repo has a specific structure I need to follow.

I think the right approach is:
1. First explore the repository thoroughly (read-only, allowed).
2. Then, since there are genuine design decisions (how to implement recurring consent in SBP — this has specific CBR mechanics like "подписка на списание" / recurring payments token), I should identify the key open questions and present approaches.
3. Produce the package.

But actually, let me reconsider whether I should do the full interactive brainstorming (one question at a time) or produce a draft and iterate. The skill says ask clarifying questions one at a time. But the user's brief is quite complete and they asked for a comprehensive deliverable. 

Given the interaction mode reminder: "Use 'ask_user_question' when you need clarification or want to validate assumptions." And the brainstorming skill wants clarifying questions.

I think a balanced approach: Explore the repo first (read all key files). Then present my understanding + the key architectural decisions/approaches to the user, ask focused clarifying questions on the genuinely ambiguous points, and then produce the full package.

But actually — this could go very long. Let me first read the repository to understand what's there. That's read-only and explicitly allowed.

Let me read the key files:
- ARCHITECTURE-SPINE.md
- README.md
- .arch-handoff/ (TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, adr/ADR-001-outbox.md)
- docs/ (nfr.md, solutioning.md, adr/, contracts/, rfp/, spec/)
- openapi/tsp-api.yaml

Let me do this exploration efficiently. I'll read multiple files in parallel.

Let me first list the directory structure more completely to know what files exist.

Let me use glob and read files in parallel.

Actually, I should first announce the classification (per the skill: "say the classification out loud"). Then explore.

Let me announce and explore. I'll do a batch of reads.

Let me first get the full file listing.
This is clearly an **architectural** change — it restructures how payment components interact and alters a contract (`tsp-api.yaml`) that external consumers depend on. I'll follow the architectural path: explore the repo thoroughly first, then surface the key design decisions.

Let me map the full repository and read the accepted-decision documents.

  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/spec/state-machine.md")`

Good. Now let me read the remaining key files. I need to understand:
- docs/solutioning.md — full design
- docs/nfr.md — measurable NFR
- docs/contracts/tsp-api.md — TSP API contract (merchant API)
- docs/contracts/opkc-adapter.md — OPKC adapter contract
- docs/spec/state-machine.md — state machine
- docs/rfp/vendor-rfp.md — RFP package
- openapi/tsp-api.yaml — the actual OpenAPI contract
- .arch-handoff/TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json — the rules for how to change things
- The ADRs (especially ADR-007 proposed A3, ADR-002 state machine, ADR-001 outbox)

This is a lot. Let me read them in parallel batches. Let me read the most important ones first: solutioning.md, nfr.md, tsp-api.md, tsp-api.yaml, state-machine.md, and the .arch-handoff files.

Let me batch these reads.
Now let me read the full design, NFRs, contracts, and the handoff rules that govern how changes must be made.

  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/openapi/tsp-api.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/.arch-handoff/ARCHITECTURE.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/.arch-handoff/MANIFEST.json")`

Now let me read the remaining files: the OpenAPI yaml, the .arch-handoff files (TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json), and the key ADRs (especially ADR-002, ADR-007, ADR-003, ADR-005, ADR-006). Also docs/contracts/opkc-adapter.md and rfp/vendor-rfp.md.

Let me batch these reads.
Now the OpenAPI contract, the handoff rules (how changes must be made), and the key ADRs.

  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/adr/ADR-002-model-konsistentnosti)`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/adr/ADR-005-integraciya-s-abs-zac)`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/contracts/opkc-adapter.md")`

Now I have a good understanding of the repository. Let me read the remaining important files: the ADRs (002, 003, 005, 006, 007), the opkc-adapter contract, and the rfp. I especially need ADR-007 (the A3 strategy decision, which is the one that says "hybrid" and deferred features like "автоплатежи"). Also ADR-002 (state machine) and ADR-005 (ABS credit from PAID + refunds saga).

Let me read those. I noticed in solutioning.md section 1: "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." So автоплатежи (autopayments) is explicitly listed as OUT of scope in the current accepted decision. And in ARCHITECTURE-SPINE.md "Deferred": "C2C-переводы и выплаты B2C/B2B" and "Диспуты/претензии" — but NOT explicitly "автоплатежи/подписки" in the deferred list. However solutioning lists "автоплатежи" as out of scope roadmap.

This is a key finding: the change (recurring C2B debits by payer consent = SBP subscriptions / autopayments) is currently explicitly OUT of scope. So this is a scope expansion that touches the parent initiative and the deferred list.

Also important: In the real СБП (NSPK), recurring payments are done via a mechanism called "платёжная ссылка" or more relevantly "подписка" — actually NSPK СБП has "Оплата по подписке" / recurring payments. The real mechanism: the payer gives consent in their bank's app, and there's a "payment link" that can be reused. Actually, the NSPK mechanism for recurring C2B is the "СБП подписка" — the payer signs an agreement (согласие) with the TSP, and the TSP can initiate debits without QR per transaction. There's a concept of "платёжное согласие" / "реккурентные платежи".

But I should be careful — the documentation says the exact NSPK protocol is external and marked [ТРЕБУЕТ ПРОВЕРКИ]. So I should design at the level of the gateway's internal contract + TSP API, and mark protocol details as [ТРЕБУЕТ ПРОВЕРКИ].

Let me read the remaining ADRs and contracts to understand the full picture, especially:
- ADR-007 (strategy A3 — this is the adopted one, and it lists what's in/out scope)
- ADR-002 full (state machine, idempotency)
- ADR-005 (ABS integration, refunds saga)
- ADR-006 (trust zones)
- opkc-adapter.md contract
- vendor-rfp.md

Let me read these.
Let me read the remaining ADRs (especially ADR-007 the adopted A3 strategy, ADR-002, ADR-005) and the OPKC adapter contract.

  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/rfp/vendor-rfp.md")`

I now have a very comprehensive understanding of the repository. Let me also quickly read ADR-003 (mTLS), ADR-004 (at-least-once DLQ), ADR-006 (trust), and the RFP vendor doc, plus docs/rfp/vendor-rfp.md, to be complete. But I think I have enough for the key decisions. Let me read ADR-004 and ADR-006 and ADR-003 briefly, and the rfp doc.

Actually, I have enough context to understand the architecture and the rules. Let me read a couple more to be thorough: ADR-003 (mTLS), ADR-004 (notifications/at-least-once), ADR-006 (trust). These matter for understanding what invariants are touched.

Let me read them quickly in parallel, plus the RFP doc.
Let me read the remaining ADRs and the RFP package to complete the picture.

  `ask_user_question(questions=[{"header": "Consent", "question": "Где авторитетно формируется и хранится согласие плательщика (подписка СБП)?", "options": [{"label": "Чер)`

I now have a complete and thorough understanding of the repository. Let me summarize my understanding and then follow the brainstorming skill's architectural path.

Key facts:
1. The repo is an accepted architecture for a SBP C2B-acceptance payment gateway.
2. There's a spine (ARCHITECTURE-SPINE.md) with invariants AD-001..AD-008.
3. Docs: solutioning.md, nfr.md, contracts (tsp-api, opkc-adapter), spec (state-machine), rfp (vendor-rfp), adr (001..007).
4. The change: recurring C2B debits by payer consent — SBP subscriptions (подписки СБП). This is currently explicitly OUT of scope (listed in solutioning.md §1 "Roadmap (вне scope): ... автоплатежи" and the deferred list doesn't explicitly mention it, but "автоплатежи" = autopayments).

Wait — let me note: solutioning.md says "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." So автоплатежи is explicitly out of scope. But the business now wants recurring C2B debits (subscriptions). This is essentially "автоплатежи" / "рекуррентные платежи СБП".

This is a significant scope expansion. The key architectural question is: how does the SBP actually support recurring payments?

Let me think about the real-world SBP recurring payment mechanism (from my domain knowledge, but marking protocol details as [ТРЕБУЕТ ПРОВЕРКИ]):

In СБП (NSPK), recurring payments / subscriptions are supported through a mechanism where:
- The payer gives consent (согласие) to the TSP for recurring debits.
- NSPK СБП has a "платёжное согласие" / "СБП подписка" feature.
- The actual mechanism: The payer, in their bank app, signs a consent (согласие на списание). This creates a "mandate" / "agreement" between payer, their bank, and the TSP (through NSPK).
- Then the TSP can initiate debits (pull payments) against this consent, without requiring a new QR for each payment.
- In NSPK terms, this is often called "подписка СБП" (SBP subscription) or "автоплатежи". There's a concept of "согласие на списание" (consent) and the recurring payment is initiated via a "payment link" that references the consent, or via a specific "recurring payment" request.

Actually, more precisely: NSPK's СБП C2B supports a "QR with payment by subscription" or there's a dedicated recurring payment flow. The key elements:
- Consent (согласие плательщика) — registered once, identifies the payer, the TSP, the bank, limits (max amount, period, frequency).
- The consent is given in the payer's bank app (via a payment link that opens the subscription setup).
- After consent, the TSP can initiate recurring payments (debits) referencing the consent token, without payer interaction.

But I should NOT invent precise NSPK protocol details. The repo's convention is to mark protocol-level details as `[ТРЕБУЕТ ПРОВЕРКИ]` and design the gateway's internal contract + TSP API, with the OPKC adapter hiding the protocol.

So the architectural design should be:
- A new domain object: **consent** (согласие) / **subscription** (подписка).
- New states: consent lifecycle (CREATED → AWAITING_CONFIRMATION → ACTIVE → SUSPENDED/REVOKED/EXPIRED).
- New recurring payment (автоплатёж) — initiated by TSP referencing a consent, without QR. The recurring payment goes through the payment state machine but skips QR_ISSUED (no payer action), going directly to a "awaiting debit result" state.
- TSP API changes: add endpoints for consent management and recurring payment initiation.
- OPKC adapter: add methods/events for consent and recurring debit.
- New NFRs: consent registration latency, recurring debit throughput, etc.
- Compliance: consent storage is ПДн, 152-ФЗ, 161-ФЗ (перевод без согласия клиента запрещён → need consent evidence), 115-ФЗ.

The invariant impact:
- AD-001 (изоляция платёжного контура) — unchanged, still applies.
- AD-002 (единый источник истины — статусная машина платежа) — needs extension: add consent state machine + recurring payment states. The rule (atomic transitions) still holds.
- AD-003 (идемпотентность) — extends to consent/recurring operations (new idempotency keys).
- AD-004 (единственный адаптер ОПКЦ) — unchanged in spirit, adapter gains consent/recurring methods.
- AD-005 (зачисление только из подтверждённого статуса) — for recurring, the "confirmed status" is the confirmed debit. The invariant "credit only from confirmed NSPK status" still holds, but the confirmed status for a recurring debit might be different (a "debited" confirmation). This needs careful mapping. Actually AD-005 says "только из PAID". For recurring payments, the equivalent is: credit to TSP only after NSPK confirms the debit succeeded. So the invariant holds conceptually, but PAID needs a semantic adjustment or a parallel state.
- AD-006 (trust zones) — unchanged, consent data is ПДн → same zones.
- AD-007 (соответствие НПС/КИИ/ПДн) — consent adds ПДн and a new regulatory angle (перевод без присутствия клиента — the consent is the legal basis). This is touched: consent evidence retention, 161-ФЗ.
- AD-008 (стратегия реализации — гибрид) — unchanged, but the OPKC adapter contract expands.

Now, the deliverables the user wants are 7 specific items. The brainstorming skill wants me to ask clarifying questions one at a time, propose 2-3 approaches, present design sections, get approval, then write a spec, then writing-plans.

But there's a subtlety: the user has given me a very specific deliverable list that is NOT the brainstorming spec format. The user wants an "архитектурный пакет" (architectural package) that follows the repo's own conventions (ADR, contracts, NFR, etc.), to be taken to "архитектурное решение" (architecture decision / A3 gate) and then handed to implementers.

So actually, the user's request is essentially: "produce the architecture decision package (like the existing ADR-001..007, spine changes, contract changes, NFR changes, acceptance criteria, rollback plan)". This IS the design work, and the output is the architectural documentation itself.

This is architectural. The brainstorming skill says I should follow the full process. But I need to reconcile with the user's clear one-shot request and the "Код не пиши" instruction.

Let me think about what's the right interaction. The brainstorming skill's core purpose is to make sure I understand the intent and get approval before "implementation". Here, "implementation" would be writing the actual architecture documents (which change accepted-decision files).

The HARD-GATE says: "Architectural: the human partner reviews and approves the written spec, then reviews the written implementation plan and selects its execution method."

But the user has asked for a specific set of deliverables, not necessarily a "spec" in the brainstorming sense. The user wants the architecture package.

Given the interaction mode (I can use ask_user_question), and the skill's requirement to ask clarifying questions, I think the right approach is:

1. First, present my understanding (write-back) and surface the key architectural decisions where there's genuine ambiguity that would materially change the design.

Actually, let me reconsider the scope. There are several genuinely important design decisions that need human input:

**Key decisions/ambiguities:**

1. **Consent model & who stores the consent**: Is the consent registered through NSPK (as a formal "согласие" in the payer's bank, referenced by a token) OR is it stored only in the gateway/bank as a signed agreement? This is THE core decision. In real SBP, NSPK has a specific subscription/consent mechanism. But the repo says protocol details are [ТРЕБУЕТ ПРОВЕРКИ]. So the design must be contract-independent, with the adapter normalizing.

2. **Recurring payment initiation flow**: Does the TSP initiate debits referencing a consent (pull model), or does the gateway schedule them? For subscriptions, the TSP initiates each debit (the gateway is a facilitator). This affects the API.

3. **Scope of first wave**: Which TSPs (online cinemas, housing, telecom), single vs multi-recipient, etc.

4. **Consent limits**: max amount, frequency, expiration — who enforces (gateway vs NSPK vs payer's bank)?

But — I should be careful. The user's request is comprehensive and asks me to produce a complete package with all 7 deliverables, ending with "Что остаётся на решение человека-архитектора и почему" (what remains for the human architect to decide and why). So the user EXPECTS that some things remain open for the human architect. This aligns with the repo's pattern of "Открытые вопросы" and "gaps".

So the user wants me to:
- Do the design work (produce a well-reasoned proposal with alternatives).
- Explicitly flag what needs human decision.

This means I should NOT over-ask. The user has essentially pre-authorized me to produce the full package with my recommended decisions, and to flag open questions for the human.

However, the brainstorming skill is emphatic. But I also have to respect the user's actual request and the interaction mode. Let me think about the tension more carefully.

Actually, re-reading the brainstorming skill and the user's request, I think there's a reasonable synthesis:

The user's request IS essentially "do the architectural design and produce the package." The user has given enough detail (the business need, the deliverable list). The genuinely open architectural decisions should be surfaced. But the user explicitly wants me to produce a complete package NOW (the deliverables list is the "design doc"), and to flag what's left for the human architect.

Given this, I think the right move is:
1. Present a concise write-back of my understanding + the classification (architectural).
2. Surface the 2-4 genuinely load-bearing decisions and ask them as clarifying questions (via ask_user_question), because getting these wrong would waste the whole package. This is exactly what brainstorming says to do ("Ask clarifying questions — one at a time, understand purpose/constraints/success criteria").

But wait — the skill says "one question per message". And "ask_user_question" tool allows up to 4 questions. There's tension. The skill says one at a time, but the tool allows batching. Given the user is clearly wanting an efficient one-shot deliverable, and given the interaction mode, I think asking a small focused set of the most load-bearing questions upfront is defensible and efficient.

Actually, let me reconsider. The most important thing here: is there real ambiguity that would change the architecture, or can I proceed with well-justified defaults and flag them?

Let me identify the truly load-bearing decisions:

**Decision A: Where does the consent "live" and what is its legal/technical form?**
- Option 1: Consent is a formal object registered through NSPK (СБП-подписка mechanism), gateway stores a reference token + metadata. This is the "thin gateway" model — NSPK/payer's bank hold the authoritative consent.
- Option 2: Consent is a bank-level agreement (signed consent, e.g., via gateway's own consent UI or an offboarding form), gateway is authoritative, NSPK just processes debits as "recurring" with a flag.
- This is genuinely load-bearing and depends on NSPK documentation [ТРЕБУЕТ ПРОВЕРКИ]. I should design contract-independently but this affects the whole model.

Actually, I realize the cleaner framing: The gateway should treat consent as a first-class domain entity regardless, with the adapter normalizing NSPK specifics. The core decision is about **who initiates the recurring debit and whether there's a payer-facing confirmation step**.

**Decision B: Does each recurring debit require the payer's bank to "confirm" (no payer action per transaction), or is there a periodic re-confirmation?** — This is NSPK-protocol-specific [ТРЕБУЕТ ПРОВЕРКИ].

**Decision C: Scope — which flows in first wave** (consent lifecycle only + manual-triggered debit, vs full scheduler).

**Decision D: The payment state machine integration** — whether recurring debits reuse the existing PAYMENT FSM (skipping QR) or get a separate FSM.

Hmm. Let me step back and think about what's genuinely needed vs. what I can decide with good justification and flag.

Given the nature of this task (produce an architecture decision package, with "what remains for human decision"), I believe the best approach is:

1. Write back understanding.
2. Ask 2-4 focused clarifying questions on the genuinely load-bearing business/scope decisions, using ask_user_question (which is allowed and encouraged by the interaction-mode reminder).

Actually, wait. Let me reconsider whether asking questions is even the right first step, versus reading more. I've read essentially everything. I understand the repo well.

The brainstorming skill's architectural path step 2 is "Ask clarifying questions — one at a time". 

But I also need to weigh: the user gave a detailed, self-contained brief and asked for a comprehensive deliverable. They said "используй навыки по назначению" (use skills as intended). This suggests they want me to follow the process but not be pedantic.

I think the most valuable and correct approach:
1. Brief write-back of understanding + classification (architectural).
2. Ask the few genuinely load-bearing clarifying questions (I'll use ask_user_question with 3-4 focused questions). These are real decisions that materially change the design.

Then, based on answers, produce the full package.

But actually — hold on. Let me reconsider. The user might find a long Q&A session annoying given they asked for a complete package. But the brainstorming skill and the "use skills as intended" instruction push me toward surfacing decisions. And the risk of producing a wrong architecture (e.g., wrong consent model) is high and costly.

I think there's a middle path that respects both: I'll present my understanding concisely and ask the 3-4 most load-bearing questions in ONE ask_user_question call (the tool supports up to 4). This is efficient and gets me the info I need to produce a correct package.

Let me identify the 4 best questions. Actually, I want to be careful not to ask things I can decide myself with good defaults.

Load-bearing questions that I genuinely cannot decide without business/regulatory input:

1. **Consent model / legal basis**: Is the consent a formally registered СБП-подписка in NSPK (payer confirms in their bank app via a link/QR, NSPK issues a consent reference), OR a bank-level consent captured outside NSPK (e.g., gateway's own form / TSP's form, gateway is authoritative)? — This determines whether the OPKC adapter needs consent methods, and the whole consent FSM. This is genuinely load-bearing and protocol-dependent.

Actually, given the repo's AD-008 (hybrid, contract-independent core), I can design the gateway's consent model independent of where NSPK stores it, treating "consent registration in NSPK" as an adapter concern. So maybe I can decide this: design a first-class consent entity in the gateway, with the adapter normalizing NSPK specifics, and flag the exact NSPK mechanism as [ТРЕБУЕТ ПРОВЕРКИ].

2. **Recurring debit trigger model**: 
   - (a) TSP-initiated pull: TSP calls the gateway "charge this consent X amount" for each subscription period (the gateway is a facilitator). 
   - (b) Gateway-scheduled: the gateway holds the schedule and auto-debits.
   - This is a real decision. For СБП subscriptions (online cinemas etc.), typically the TSP (merchant) initiates each charge (pull model), because the TSP owns the subscription logic/billing. The gateway just executes the debit. But there could be a hybrid.
   This is genuinely load-bearing for the API and components.

3. **Scope of first wave / MVP**: consent + single debit only? Or include partial refunds, consent management UI, etc.? And which TSP verticals first (cinemas vs housing vs telecom have different consent capture requirements)?

4. **Payer consent capture channel**: Who presents the consent UI to the payer — the payer's bank app (NSPK redirect), or the gateway/TSP? This affects whether we need a consent capture flow in the gateway.

Hmm, these are all somewhat interconnected. Let me consolidate into the most decision-relevant questions.

Actually, I realize I should think harder about the actual SBP recurring mechanism to ask GOOD questions. Let me recall what I know about НСПК СБП recurring payments:

The СБП (НСПК) supports recurring payments via a mechanism often described as:
- The TSP creates a "платёжная ссылка" (payment link) of type "подписка" (subscription).
- The payer follows the link, in their bank app confirms a "согласие на списание" (consent / mandate) with parameters (max amount, period, duration).
- After consent, NSPK registers the consent and issues a reference.
- The TSP then initiates recurring debits via the consent reference; each debit is authorized without payer action.
- There's also a "payments by subscription" where a single consent authorizes multiple future debits.

So the flow is essentially: consent capture (via a link that opens payer's bank app) → consent registered → TSP initiates debits.

This maps nicely to the gateway's architecture:
- New domain: **consent** (согласие) with lifecycle.
- Consent capture: TSP requests a "consent link" (like a QR/link) → gateway → adapter → NSPK → payer confirms in bank app → NSPK notifies consent activated.
- Recurring debit: TSP calls "initiate recurring payment" referencing consent → gateway validates consent (active, within limits) → adapter → NSPK debits → NSPK confirms → gateway credits TSP (per AD-005 equivalent) → notify TSP.

This is quite analogous to the existing QR payment flow, just with consent instead of per-payment QR.

OK. So the genuinely load-bearing questions for the HUMAN are mostly about **business scope and the exact regulatory/NSPK consent semantics**, plus a few architectural choices where I should present alternatives and let the human pick (which the user explicitly wants in deliverable #3 — "Архитектурное решение с рассмотренными альтернативами").

Actually, re-reading the deliverables:
- #3 asks me to PRODUCE "Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью" — this is an ADR. So I'm expected to make a recommendation with alternatives, not necessarily ask the user to pick each alternative.

So my job is: produce the design with my recommendations, present alternatives, flag open items for the human architect (deliverable #7).

Given this, I think the amount of upfront questioning should be minimal — only the truly blocking business questions. Let me identify the SINGLE most important set.

Actually, I think there are 2-3 questions worth asking before I write the full package, because they'd change the shape of the whole thing:

1. **Consent legal/technical model** — is it a СБП-подписка through НСПК (payer confirms in their bank app), or a gateway/TSP-captured consent? This determines the consent FSM and adapter surface.

Actually, I'm fairly confident the answer is "СБП-подписка через НСПК" (that's what СБП-подписки means — it's an NSPK feature). The user says "рекуррентные C2B-списания по согласию плательщика — подписки СБП". "Подписки СБП" strongly implies the NSPK subscription feature. So the consent IS registered through NSPK.

2. **Who initiates the recurring debit** — TSP (pull) vs gateway (schedule). For "подписки СБП", the TSP initiates. But some models have the gateway/payer's bank push. I lean TSP-initiated pull, but this is worth confirming because it affects the API.

3. **MVP scope** — which flows first.

4. **Consent limits enforcement point** — gateway vs NSPK vs payer's bank. (Probably NSPK enforces limits at the payer's bank, gateway enforces its own sanity checks + anti-fraud.)

Let me decide: I'll ask a focused set of clarifying questions (3-4) to nail down scope and the consent/debit model, then produce the full package. This is consistent with the brainstorming skill (architectural: ask clarifying questions) and the interaction mode.

Actually, let me reconsider once more whether I should ask questions at all, or just produce a complete draft package with clear "open questions for human" and let the user review/correct. The brainstorming skill says present design in sections and get approval after each section, then write the spec, then user reviews the spec.

Given the size and the user's "one-shot package" framing, I think the pragmatic and correct approach is:

1. Write back a concise understanding (classification + what I'll produce).
2. Ask a SMALL set of load-bearing clarifying questions (one ask_user_question call, 3-4 questions) — these are the decisions that materially shape the design and that I can't safely default.
3. Then produce the full package (the actual files: a new ADR, spine changes, tsp-api.yaml changes, tsp-api.md changes, opkc-adapter.md changes, state-machine.md changes, nfr.md changes, solutioning.md update, plus a summary/assessment doc with the 7 deliverables).

Actually — I realize I should also think about whether to write the "design doc" to `docs/superpowers/specs/` as the brainstorming skill says, OR whether the repo's own convention (ADR + docs/) is the right place. The user explicitly said: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." (Change accepted-decision files only in the way accepted in this repo.) This means: use ADR format, docs/ structure, spine invariants format. NOT the superpowers spec format. So I should follow the repo's conventions, not the brainstorming skill's default spec location. The user's instruction overrides the skill's default (and the skill itself says "User preferences for spec location override this default").

So the deliverable will be:
- A new ADR (ADR-008) for recurring payments/subscriptions, following the exact ADR template (Context, Decision, Alternatives Considered, Consequences, Reversibility, References).
- Possibly a spine update (ARCHITECTURE-SPINE.md) — but careful: the spine is the "accepted invariants". Adding a new invariant AD-009 for consent, and updating the "Deferred" list to remove автоплатежи. But the user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — so I need to follow how spine changes are done. The spine has statuses (Proposed/Adopted). Adding a new Proposed invariant + updating deferred list is the way.

Actually, let me reconsider the scope of file changes. The user wants a "архитектурный пакет этого изменения поверх принятого решения" — an architectural package of this change ON TOP of the accepted decision. So I should produce NEW/ADDITIVE artifacts (a new ADR, contract additions, NFR additions, a design/impact assessment doc), and modify existing files ONLY as the repo's process allows (e.g., add a new Proposed invariant to the spine, add endpoints to the OpenAPI as additive changes, extend contracts as v0.1-additions, extend the state machine spec with a consent FSM).

Let me now decide on the clarifying questions. I'll ask about:

Q1 (Consent model / legal basis): How is the payer consent captured & where is it authoritative?
- Options: (a) СБП-подписка НСПК — consent registered in NSPK, payer confirms in their bank app via a link (recommended); (b) bank-level consent captured by gateway/TSP outside NSPK; (c) hybrid — need to know.

Q2 (Debit initiation model): Who triggers each recurring debit?
- Options: (a) TSP initiates each charge (pull) — recommended; (b) gateway schedules automatically (push); (c) both.

Q3 (MVP scope): What's in the first wave?
- Options: (a) consent lifecycle + TSP-initiated debit, no scheduler — recommended; (b) include gateway scheduler + retry-on-failed-debit; (c) full incl. partial refunds + consent management UI.

Q4 (NSPK protocol assumption): Given NSPK documentation is [ТРЕБУЕТ ПРОВЕРКИ], should I design the gateway contract-independent (treat consent/debit as adapter-normalized, like the existing QR flow), flagging protocol details as [ТРЕБУЕТ ПРОВЕРКИ]? 
- Options: (a) Yes — contract-independent, [ТРЕБУЕТ ПРОВЕРКИ] (recommended); (b) assume a specific NSPK subscription mechanism and design against it.

Hmm, Q4 is almost certainly (a) given AD-008 is the adopted strategy. I might fold that into my design without asking, but it's worth a quick confirm because it affects how much I can "concretely" specify.

Actually, let me consolidate to 3 well-chosen questions to respect the user's time, since Q4's answer is basically forced by AD-008 (contract-independent is the adopted reality). I'll instead ask:

Q1: Consent authoritative source & capture channel.
Q2: Debit initiation model.
Q3: MVP scope / first wave.

And maybe Q4: enforcement of consent limits (max amount/frequency) — gateway vs NSPK vs payer's bank. Actually this can be a design decision I flag. Let me keep 3 questions, maybe 4 if there's room.

Let me reconsider Q1. The user said "рекуррентные C2B-списания по согласию плательщика — подписки СБП". "Подписки СБП" is literally NSPK's subscription product. So Q1's answer is almost certainly "СБП-подписка через НСПК". But there's still a meaningful sub-question: does the gateway need its OWN consent capture UI, or does the payer confirm entirely in their bank app (NSPK redirect)? For "подписки СБП", the payer confirms in their bank app. The gateway just orchestrates via the adapter. So maybe Q1 is less ambiguous than I thought.

Let me refine to the genuinely ambiguous, business-scope questions:

1. **Debit initiation (scheduler location)**: Does the bank's gateway own the subscription schedule and auto-debit, or does the TSP trigger each debit? — This is genuinely ambiguous and load-bearing (affects whether we build a scheduler component).

2. **Consent limits & enforcement**: What limits does the consent carry (max amount per debit, max total, frequency, validity), and who is authoritative for enforcement (payer's bank via NSPK, or gateway)? — affects data model and NFR.

3. **MVP scope / verticals**: Which verticals & flows first (consent + debit only, or also consent revocation by payer, dunning/retry, partial refunds)?

4. **Handling failed debits (insufficient funds)**: Is retry/dunning in scope? Who owns it (TSP vs gateway)?

Let me pick the 4 most load-bearing and frame them as multiple-choice. Actually, I think I'll ask 4 questions since the tool supports it and they're all genuinely load-bearing.

Wait, but I should be mindful: the brainstorming skill says "one question per message" and "prefer multiple choice". But it also says the ask_user_question tool supports batching. There's a real tension between the skill's "one at a time" and efficiency. 

Given the user's clear desire for a comprehensive one-shot deliverable and the interaction mode's encouragement of ask_user_question, I'll ask a focused batch of 3-4 questions. This is a reasonable adaptation; the skill's "one at a time" is about not overwhelming with a wall of questions, but a single structured ask_user_question with 3-4 clearly-scoped multiple-choice questions is manageable and respects the user's time.

Actually, let me reconsider — maybe I'm overcomplicating. Let me re-read the user's request one more time for signals about what they want me to decide vs. ask.

"Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям."

So the package is to be taken to the architecture decision (A3 gate / human decision). This means: the package should present the design + alternatives + what needs human decision. The human architect will then DECIDE. So my job is to prepare a complete, well-reasoned package with recommendations and explicitly flag the decision points.

Deliverable #7: "Что остаётся на решение человека-архитектора и почему" — what remains for the human architect to decide and why. This is where I list the open decisions.

So the flow is: I produce the package with my recommendations, and I clearly list what the human must decide. I don't necessarily need to BLOCK on asking questions first — I can produce the package with well-justified recommendations and clearly flag the decision points in deliverable #7 (and in the ADR's "open questions").

BUT — the brainstorming skill's HARD-GATE is about not implementing before approval. Here, "implementing" = writing the actual architecture files. The skill wants me to get approval on the design before writing the spec.

Hmm. But the user's request is literally "produce the architectural package" — the package IS the deliverable, not code. And the user has given a detailed brief.

Let me reconcile: I'll do a lightweight version of the brainstorming process:
1. Write back understanding (concise).
2. Ask the 3-4 genuinely load-bearing questions (because getting the consent/debit model wrong would invalidate the whole package).
3. Then produce the full package (the actual files), presenting my design recommendations within it.

Actually, you know what, I think the cleanest and most correct approach given all constraints is:

1. Write back a concise understanding + announce classification (architectural) + state the plan (what files I'll produce).
2. Ask a focused set of load-bearing clarifying questions via ask_user_question (the genuinely ambiguous decisions).

Then in the NEXT turn (after answers), produce the full package.

This respects: brainstorming skill (architectural path: explore → ask clarifying questions), interaction mode (ask_user_question), and the user's "use skills as intended".

But I'm also aware the user might just want me to go ahead. The ask_user_question tool lets the user pick "Other" and also I should make the recommended option first.

Let me finalize the questions. I'll ask 4:

**Q1 — Consent source / legal model** (header "Consent model"):
Question: "Где формируется и где авторитетно хранится согласие плательщика (подписка СБП)?"
Options:
- (a) "СБП-подписка через НСПК (Recommended)" — согласие регистрируется в ОПКЦ НСПК; плательщик подтверждает в приложении своего банка по ссылке; шлюз хранит ссылку/токен + метаданные. [protocol via adapter, [ТРЕБУЕТ ПРОВЕРКИ]]
- (b) "Согласие уровня банка/шлюза" — шлюз сам фиксирует согласие (форма/подпись), НСПК выполняет только сами списания.
- (c) "Гибрид / пока неясно" — проектировать нейтрально, решить после документации НСПК.

**Q2 — Debit initiation** (header "Debit trigger"):
Question: "Кто инициирует каждое рекуррентное списание?"
Options:
- (a) "ТСП инициирует (pull) (Recommended)" — ТСП вызывает шлюз «списать N по подписке»; шлюз оркестрирует через ОПКЦ.
- (b) "Шлюз по расписанию (push)" — шлюз хранит расписание и сам инициирует списания.
- (c) "Оба режима" — pull в MVP + push позже.

**Q3 — MVP scope** (header "MVP scope"):
Question: "Что входит в первую волну (для выноса на A3)?"
Options:
- (a) "Согласие + списание по запросу ТСП (Recommended)" — жизненный цикл согласия (создание/подтверждение/отзыв) + разовое списание по активному согласию, без планировщика и dunning.
- (b) "Плюс планировщик и dunning" — автоматические повторы при неуспехе списания (недостаточно средств).
- (c) "Полный объём" — плюс частичные возвраты, личный кабинет управления подписками.

**Q4 — Consent limits enforcement** (header "Limits"):
Question: "Кто авторитетно задаёт и контролирует лимиты согласия (макс. сумма, периодичность, срок действия)?"
Options:
- (a) "Плательщик/его банк через НСПК, шлюз проверяет дублирующе (Recommended)" — авторитет — НСПК; шлюз хранит копию и делает sanity-check + антифрод.
- (b) "Шлюз авторитетен" — шлюз задаёт/контролирует лимиты, НСПК — только транспорт.
- (c) "ТСП авторитетен" — ТСП контролирует лимиты, шлюз не дублирует.

These 4 are all genuinely load-bearing and I can't safely default all of them. Q1 and Q2 especially.

Actually, wait — I want to reconsider whether asking 4 questions is too much and whether I should just proceed. The user's tone ("Подготовь пакет... Когда закончишь, перечисли файлы") suggests they want the deliverable produced. But the brainstorming skill and "use skills as intended" push toward surfacing decisions.

I think a reasonable middle ground: I'll write back my understanding AND ask the 4 load-bearing questions in a single ask_user_question call. This is the right balance. The user can answer quickly (they're multiple choice), and then I produce the full package correctly.

Actually, let me reconsider even more carefully. Is there a risk the user just wanted me to "go and produce it" and will be annoyed by questions? The interaction mode reminder explicitly says "Use 'ask_user_question' when you need clarification or want to validate assumptions." And the brainstorming skill mandates clarifying questions for architectural work. So asking is correct.

Let me also make sure I follow the skill's instruction to "say the classification out loud" and "write back your understanding". I'll do that concisely in my text before/with the question.

Let me write a concise write-back + classification, then ask the questions.

Let me draft the write-back:

Understanding:
- Accepted decision = СБП C2B-acceptance gateway (dynamic/static QR, links, refunds), spine AD-001..008, docs + openapi v0.1.
- Currently автоплатежи/подписки explicitly out of scope (solutioning §1 roadmap; spine Deferred implicitly).
- New business need: recurring C2B debits by payer consent (СБП-подписки) for cinemas/housing/telecom. Each payment no longer needs a QR + client action.
- Deliverable: architectural package (impact assessment, invariant impact, ADR with alternatives, contract changes, NFR, acceptance criteria + rollback, open decisions for human architect).

Classification: architectural (new domain object, changes contract, restructures flows). Will follow repo conventions (ADR-008, spine AD-009 Proposed, additive contract changes, etc.).

Then ask 4 questions.

Actually, I want to be careful about one thing: the brainstorming skill says "Ask clarifying questions — one at a time". The ask_user_question tool batches. I'll batch 4 because they're all multiple-choice and it's efficient, but I'll acknowledge this is a batch. Actually the skill is quite explicit "one question per message". Hmm.

But the interaction-mode reminder and the tool (max 4 questions) suggest batching is acceptable. I'll batch but keep it tight (4 questions, all multiple choice, concise). This is a defensible adaptation given the user's clear one-shot intent. If the user wanted strictly one-at-a-time, they can answer in sequence.

Actually, let me reduce to the 3 most load-bearing to be less heavy: Q1 (consent model), Q2 (debit trigger), Q3 (MVP scope). Q4 (limits) I can decide with a sensible default (NSPK/payer's bank authoritative + gateway sanity-check + anti-fraud) and flag it. That's a defensible design decision.

Hmm, but Q4 (limits enforcement) actually matters for the data model and NFR. I think it's worth asking. But to keep it to 4 max, I'll include all 4. The tool allows 4.

Actually, I'll go with 4 questions. They're all genuinely load-bearing and multiple-choice, so low friction.

Let me also think: should I present approaches (skill step 4 "Propose 2-3 approaches") BEFORE asking these? No — the order in the skill is: explore (done) → ask clarifying questions → propose approaches → present design. So questions come first. Good.

One more consideration: the skill says "Discover intent... When that information is missing, ask one focused question about purpose or intended use before proposing features." The purpose is clear (subscriptions for cinemas/housing/telecom). So I don't need to ask "why". The questions I have are design-scope questions, which are appropriate.

Let me now write the response: concise write-back + classification + the 4 questions.

Let me make the write-back tight and in Russian (the user writes in Russian; output language auto → Russian).

I'll structure:
1. Classification announcement (architectural).
2. Short write-back of understanding (2-4 sentences + the key finding that автоплатежи currently out of scope).
3. Note that I'll follow repo conventions.
4. The ask_user_question with 4 questions.

Let me write it.

For the questions, I need to be careful with the tool schema: each question needs `question`, `header` (max 12 chars), `options` (2-4, each with `label` and `description`). Recommended option first with "(Recommended)".

Let me write concise labels and descriptions.

Let me finalize.

Q1 header: "Consent" (≤12 chars ok).
Q1 question: "Где авторитетно формируется и хранится согласие плательщика (подписка СБП)?"
Options:
1. "Через НСПК (Recommended)" — desc: "Согласие регистрируется в ОПКЦ НСПК; плательщик подтверждает в приложении своего банка по ссылке; шлюз хранит токен/ссылку + метаданные, протокол — за адаптером ОПКЦ [ТРЕБУЕТ ПРОВЕРКИ]."
2. "Согласие уровня шлюза" — desc: "Шлюз сам фиксирует согласие (форма/подпись/оферта), НСПК выполняет только сами списания; авторитетное хранилище — БД шлюза."
3. "Гибрид / неясно" — desc: "Проектировать контрактно-нейтрально, окончательно зафиксировать после документации НСПК."

Q2 header: "Debit trigger".
Q2 question: "Кто инициирует каждое рекуррентное списание?"
Options:
1. "ТСП инициирует (pull) (Recommended)" — "ТСП вызывает шлюз «списать N по согласию»; шлюз оркестрирует списание через ОПКЦ и зачисляет ТСП. Планировщик в шлюзе не нужен."
2. "Шлюз по расписанию (push)" — "Шлюз хранит расписание подписки и сам инициирует списания в нужные даты; ТСП только передаёт условия."
3. "Оба режима" — "В MVP — pull, расписание/push — отдельным расширением позже."

Q3 header: "MVP scope".
Q3 question: "Какой объём выносим в первую волну (на A3)?"
Options:
1. "Согласие + списание (Recommended)" — "Жизненный цикл согласия (создание→подтверждение→активно→отзыв/истекло) + разовое списание по активному согласию. Без планировщика и dunning."
2. "Плюс dunning/повторы" — "Дополнительно автоматические повторы при неуспехе (недостаточно средств) и уведомления плательщику."
3. "Полный объём" — "Плюс частичные возвраты и личный кабинет/управление подписками."

Q4 header: "Limits".
Q4 question: "Кто авторитетно задаёт и контролирует лимиты согласия (макс. сумма за списание, периодичность, срок)?"
Options:
1. "НСПК/банк плательщика (Recommended)" — "Лимиты задаёт плательщик при подтверждении, авторитет — НСПК; шлюз хранит копию и делает sanity-check + антифрод (115-ФЗ)."
2. "Шлюз авторитетен" — "Шлюз задаёт и контролирует лимиты, НСПК — только транспорт."
3. "ТСП авторитетен" — "ТСП контролирует лимиты и регулярность, шлюз не дублирует."

Good. These are solid. Let me write the response.

Actually, let me reconsider the header length constraint: "header" max 12 chars. "Consent" = 7, "Debit trigger" = 12 (ok, exactly 12), "MVP scope" = 9, "Limits" = 6. Good.

Let me also decide: should I write the write-back in the text before the tool call, or just do the tool call? The skill says write back understanding. I'll include a concise text write-back, then the question tool call.

Let me write it concisely.

Actually, I realize I should double check: is there a concern that asking 4 questions before producing anything is "too slow"? The user asked for a full package. But the skill and interaction mode support this. I'll proceed, keeping the write-back tight.

Let me write the final response now.
I've read the accepted decision in full. Here's my understanding before I design.

## Что я понял (write-back)

**Принятое решение**: СБП-шлюз C2B-приёма — маршрут Critical (11/15). Инварианты AD-001…AD-008 в `ARCHITECTURE-SPINE.md`, дизайн в `docs/solutioning.md`, статусная машина платежа (`CREATED→QR_ISSUED→PAID→CREDITED→COMPLETED`), контракт API ТСП v0.1 (`openapi/tsp-api.yaml` + `docs/contracts/tsp-api.md`), внутренний контракт адаптера ОПКЦ (`opkc-adapter.md`), стратегия «гибрид» ратифицирована (ADR-007 Accepted, AD-008 ADOPTED).

**Ключевая находка**: сейчас **автоплатежи/подписки явно вне scope** — `solutioning.md §1` перечисляет «автоплатежи» в roadmap-вне-scope, а каждая оплата требует QR + действия плательщика. Значит это **расширение scope**, а не локальная доработка: добавляется новый доменный объект (согласие/подписка), новый жизненный цикл, новые методы API ТСП и адаптера ОПКЦ.

**Классификация**: **architectural** — новый доменный объект, меняется контракт, от которого зависят внешние потребители (ТСП) и вендор транспорта. Поэтому пакет пойдёт в формате репозитория: новый ADR, добавка в spine (Proposed), аддитивные правки контрактов, NFR, критерии приёмки/откат, и явный список «что решает человек».

Есть 4 развилки, от которых меняется вся форма пакета. Они по-настоящему бизнес/регуляторные — их я не имею права «просто выбрать». Уточню их одним заходом, затем соберу пакет.

  `write_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/adr/ADR-008-rekurrentnye-c2b-spis, content="# ADR-008. Рекуррентные C2B-списания по согласию плательщика: подписки СБП\n\n- Date: 2026-09-28\n- Status: Proposed (выносится на архитект)`
  `write_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/spec/subscription-state-machine.m, content="# Статусная машина подписок СБП: согласие и рекуррентное списание\n\n- Status: Draft (для ревью на гейте A1)\n- Owner: solution-architect ()`
  `write_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/change-podpiski-sbp.md", content="# Изменение: рекуррентные C2B-списания по согласию плательщика (подписки СБП)\n\nПакет архитектурного изменения поверх принятого решения «П)`

The user confirmed all recommended options:
1. Consent through NSPK (subscription registered in OPKC, payer confirms in their bank app via link, gateway stores token/metadata, protocol behind adapter [ТРЕБУЕТ ПРОВЕРКИ]).
2. Debit trigger: TSP initiates (pull).
3. MVP scope: consent lifecycle + debit by request, no scheduler/dunning.
4. Limits: NSPK/payer's bank authoritative; gateway stores copy + sanity-check + anti-fraud (115-ФЗ).

Now I have everything I need to produce the architectural package. Let me plan the deliverables and the file changes.

The user wants 7 deliverables:
1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему).
2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет.
3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью.
4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей.
5. Измеримые NFR для нового функционала.
6. Критерии приёмки и план отката.
7. Что остаётся на решение человека-архитектора и почему.

And: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." (Change accepted-decision files only in the repo's accepted way.)

So I need to produce these as actual files in the repo, following its conventions. Let me plan the concrete artifacts:

**New files:**
1. `docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya.md` — the ADR (deliverable #3). Following the exact ADR template (Context, Decision, Alternatives Considered, Consequences, Reversibility, References).
2. A change/impact assessment doc. Where? The repo has `docs/solutioning.md` (full design) and `docs/nfr.md`. The impact assessment (deliverable #1 and #2) could be a new doc, e.g., `docs/change-podpiski-sbp.md` or a new `docs/adr/ADR-008` covers much of it. Actually, deliverables #1 (significance/route) and #2 (invariant impact) are assessment, which fits a "change assessment" doc. Let me think about where.

Actually, let me think about the repo's structure and how to fit this. The repo has:
- `ARCHITECTURE-SPINE.md` — invariants (AD-001..008) + Deferred list + contracts/versions.
- `docs/solutioning.md` — full design (components, flows, states, ADR mapping, NFR, gates, rollback, gaps, open questions).
- `docs/nfr.md` — measurable NFRs.
- `docs/contracts/tsp-api.md` — TSP API contract v0.1.
- `docs/contracts/opkc-adapter.md` — OPKC adapter contract v0.1.
- `docs/spec/state-machine.md` — payment state machine spec.
- `docs/rfp/vendor-rfp.md` — RFP.
- `docs/adr/ADR-001..007.md` — ADRs.
- `openapi/tsp-api.yaml` — OpenAPI 3.0.3 contract.
- `.arch-handoff/` — handoff package.

The user's deliverables map naturally to:
- #1 (significance/route) + #2 (invariant impact) → a change assessment doc. I'll create `docs/change-podpiski-sbp.md` (or `docs/spec/recurring-sbp.md`?). Hmm. Actually, let me think: the "significance & route" and "invariant impact" are the framing for the whole package. I could put them in a new doc `docs/recurring-sbp-assessment.md`. But maybe cleaner: a single new ADR + a new spec doc for the consent/subscription state machine + contract updates + NFR additions + a summary "decision package" doc that ties it together and lists open decisions.

Let me design the file set carefully to match the 7 deliverables and repo conventions:

1. **Deliverable #1 & #2 (significance/route + invariant impact)** → a new document. I'll create `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md`. The ADR's Context + a "Scope & significance" section covers #1, and the "invariant impact" can be a section in the ADR or a companion doc. Actually, the ADR should follow the exact template (Context / Decision / Alternatives / Consequences / Reversibility / References). The impact-on-invariants (#2) is a natural "Decision" or "Consequences" item, but it's substantial enough to warrant its own doc.

Let me reconsider. The cleanest mapping:

- **Deliverable #1 + #2** → `docs/change-assessment-rekurrentnye-c2b.md` (new): significance/route assessment + invariant-by-invariant impact analysis (what changes / what doesn't). This is the "оценка значимости и маршрута + влияние на архитектуру".

Actually, I realize the repo has a very specific "Solutioning" doc that IS the full design. And ADRs are the decisions. The user's deliverable list is essentially asking me to produce:
- An assessment (significance/route + invariant impact) — new doc.
- An ADR (decision with alternatives) — new ADR-008.
- Contract changes — edit openapi/tsp-api.yaml (additive) + edit docs/contracts/tsp-api.md + docs/contracts/opkc-adapter.md.
- NFR — edit docs/nfr.md (additive) or a new NFR section.
- Acceptance criteria + rollback — could be in the ADR + a new doc, or in solutioning.
- Open decisions for human — in the ADR + summary.

Let me also consider the state machine: consent/subscription needs its own state machine (lifecycle). The repo has `docs/spec/state-machine.md` for payments. I should add a `docs/spec/subscription-state-machine.md` (new) for the consent/subscription lifecycle. This is part of the design (deliverable #2/#3).

Let me finalize the file plan:

**New files:**
1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md` — the architectural decision (deliverable #3), with alternatives, consequences, reversibility, and open questions (deliverable #7 partly).
2. `docs/spec/subscription-state-machine.md` — consent/subscription + recurring debit state machine spec (part of #2/#3).
3. `docs/change-assessment-rekurrentnye-c2b.md` — significance/route assessment + invariant impact (deliverables #1 and #2). 

Hmm, actually — maybe I should combine #1 and #2 into one "assessment" doc and keep it separate from the ADR. Or fold the assessment into the ADR context. Let me think about what's cleanest and most "repo-like".

Looking at the existing repo, `docs/solutioning.md` is the big design doc, and ADRs are focused decisions. The user's deliverable #1 (significance/route) and #2 (invariant impact) are really "change assessment" — a preamble that frames WHY this is a big architectural change and WHAT it touches. This is best as a dedicated short doc that the architect presents alongside the ADR.

I'll create:
- `docs/change-podpiski-sbp.md` — change assessment: significance & route (#1) + invariant impact (#2). Actually let me name it consistently. The repo uses kebab-case filenames, some with Russian. E.g., `docs/adr/ADR-002-model-konsistentnosti-platezha-...`. And `docs/solutioning.md`, `docs/nfr.md` are English. Hmm, mixed. I'll use a clear name.

Let me use:
- `docs/change-assessment-rekurrentnye-c2b.md` — assessment (deliverables #1, #2).

Actually, I want to keep it simpler and more discoverable. Let me reconsider the whole deliverable-to-file mapping and minimize file count while covering all 7:

Proposal for file set (minimal, convention-following):

1. **`docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md`** (new) — the ADR. Contains:
   - Context (business need, current out-of-scope status, the 4 confirmed decisions).
   - Decision (consent through NSPK, pull model, MVP scope, limits via NSPK + gateway sanity/anti-fraud; consent + recurring-debit state machines; new TSP API; adapter methods).
   - Alternatives Considered (consent model: NSPK vs gateway-level vs hybrid; debit trigger: pull vs push vs both; MVP scope; limits enforcement).
   - Consequences (positive/negative).
   - Reversibility.
   - References.
   This covers deliverable #3 fully.

2. **`docs/change-assessment-rekurrentnye-c2b.md`** (new) — deliverable #1 (significance/route) + #2 (invariant-by-invariant impact: what changes / what doesn't / what's touched) + #6 (acceptance criteria + rollback plan) + #7 (open decisions for human). Actually, #6 and #7 fit naturally in the ADR + this assessment doc.

Hmm, but #6 (acceptance criteria + rollback) is usually part of the ADR or a gates doc. The repo has acceptance criteria in `solutioning.md §7` (gates) and rollback in `solutioning.md §8`. And NFR in `nfr.md`. 

Let me structure more cleanly. I think the cleanest is:

**Files to create (new):**
1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md` — ADR (deliverable #3 + open questions #7).
2. `docs/spec/subscription-state-machine.md` — consent/subscription + recurring debit state machines (part of #2 and the design).
3. `docs/change-assessment-rekurrentnye-c2b.md` — significance/route (#1) + invariant impact (#2) + acceptance criteria & rollback (#6) + open decisions (#7 consolidated).

Actually, that's a lot of overlap. Let me consolidate:

I think the cleanest, most reviewable set is:

1. **`docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md`** (new) — the decision + alternatives + consequences + reversibility. (deliverable #3)

2. **`docs/change-podpiski-sbp.md`** (new) — the change package summary doc that contains:
   - #1: significance & route assessment.
   - #2: invariant impact table (AD-001..008, what changes/what doesn't).
   - #5: new NFRs (measurable) — actually NFR should go in docs/nfr.md, but I can add a section there AND reference it. Hmm.
   - #6: acceptance criteria + rollback plan.
   - #7: open decisions for human.
   
   Actually this doc becomes a catch-all. Maybe better to distribute per repo convention:
   - NFR → append a new section to `docs/nfr.md` (edit, additive).
   - State machine → new `docs/spec/subscription-state-machine.md`.
   - Contract → edit `openapi/tsp-api.yaml`, `docs/contracts/tsp-api.md`, `docs/contracts/opkc-adapter.md`.
   - Assessment + acceptance + rollback + open decisions → new `docs/change-podpiski-sbp.md` (or fold assessment into ADR).

Let me settle on a clean, minimal, convention-following set:

**New files:**
1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md` — ADR (deliverable #3: decision + alternatives + consequences + reversibility; includes open questions for human → part of #7).
2. `docs/spec/subscription-state-machine.md` — consent/subscription & recurring-debit state machines (design detail for #2/#3).
3. `docs/change-podpiski-sbp.md` — the "architectural package" top-level summary: significance & route (#1), invariant impact table (#2), acceptance criteria & rollback (#6), and consolidated open decisions for human (#7). This is the doc to "вынести на архитектурное решение".

**Modified files (additive, following repo conventions):**
4. `ARCHITECTURE-SPINE.md` — add a new Proposed invariant `AD-009` for consent/subscriptions, and update the "Deferred" list (remove «автоплатежи/подписки» from deferred/out-of-scope since it's now in scope as a proposal). Also update the "Контракты и версии" note if needed. This is the "accepted way" to change the spine: new Proposed status invariant + move out of Deferred.

Wait — is adding to the spine the right move? The spine is "invariants AD-001..AD-008". A new domain object (consent) that binds the same components and adds rules deserves a new invariant AD-009 with status Proposed (pending ADR-008 ratification), following the existing pattern where AD-001..007 are "Proposed" until their ADR is accepted. AD-008 is [ADOPTED]. So adding AD-009 as Proposed (ADR-008) is consistent.

Also the "Deferred" list: currently lists "C2C-переводы и выплаты", "Диспуты/претензии", "Мультивалютность". It does NOT list автоплатежи explicitly (автоплатежи is in solutioning.md §1 roadmap "вне scope"). So I should update solutioning.md's roadmap line too. Let me check: solutioning.md §1 says "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." So автоплатежи IS explicitly out-of-scope there. I need to update that.

5. `docs/solutioning.md` — update §1 roadmap (remove автоплатежи from "вне scope", or note it's now covered by ADR-008), and add a pointer to the new ADR/subscription state machine. Possibly add the recurring flow. But I should be careful not to over-edit. Minimal: update roadmap line + add a reference. Actually, the user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — I should make minimal, additive, convention-following changes.

6. `openapi/tsp-api.yaml` — add consent + recurring-debit endpoints and schemas (additive, no breaking changes). This is deliverable #4.

7. `docs/contracts/tsp-api.md` — add consent/recurring methods (§3 new subsections) + new webhook events + new error codes. Additive.

8. `docs/contracts/opkc-adapter.md` — add consent/recurring methods (§3) + events (§4) to the adapter contract. Additive.

9. `docs/nfr.md` — add a new section with measurable NFRs for recurring (deliverable #5). Additive.

10. `docs/rfp/vendor-rfp.md` — maybe add consent/recurring to the adapter scope and POC scenarios. This is optional but consistent (the vendor adapter must support consent methods). I'll add a concise note. Actually, this might be scope creep. But it's genuinely needed: the vendor RFP scope now must include consent/debit methods. I'll add a concise addendum.

11. `README.md` — update the doc list to include the new files and note the change. Optional but good for discoverability. Also the "Статус" line mentions waiting for A3 on ADR-007; I could add a note about the new ADR-008 pending A3. I'll make a minimal update.

Hmm, that's a LOT of files. Let me be careful to be thorough but not over-reach. The user asked for a complete architectural package with 7 deliverables, so a multi-file package is appropriate. But I should keep edits minimal and additive, and clearly report all files.

Let me also reconsider: should I modify ARCHITECTURE-SPINE.md and solutioning.md at all, given they are "accepted decision files"? The user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — meaning: change them in the accepted way, not "don't change them". The accepted way is: new Proposed invariant + ADR reference + updating Deferred/roadmap. So yes, I should update them, but minimally and in the repo's format.

Actually, let me reconsider whether to touch the spine at all. The spine's Deferred list is the canonical "out of scope" record. Since автоплатежи is currently listed as "вне scope" in solutioning §1 (not in spine Deferred), and the spine Deferred has "C2C-переводы и выплаты B2C/B2B" and "Диспуты". So автоплатежи is NOT in the spine Deferred list — it's only in solutioning §1 roadmap. So I don't strictly need to touch the spine Deferred list for автоплатежи (it's not there). But I DO need to add the new invariant AD-009 (consent) to the spine, because the spine is the invariant source of truth and a new financial domain object (consent, recurring debits) needs its invariants there.

Wait, let me re-read the spine Deferred list:
```
## Deferred (с причиной и условием возврата)
- Мультивалютность ...
- C2C-переводы и выплаты B2C/B2B ...
- Диспуты/претензии ...
```
No автоплатежи here. So автоплатежи/подписки is a NEW deferred-topic that's now being pulled in. I'll add AD-009 as a new Proposed invariant for consent/recurring debits. And I should NOT need to remove anything from Deferred (автоплатежи wasn't listed there). But I should note in solutioning §1 that автоплатежи moved from "вне scope roadmap" to "in scope as ADR-008 proposal".

OK, let me also reconsider: is adding AD-009 to the spine too presumptuous? The spine invariants are "the accepted reality" (Proposed = действуют после ратификации ADR; Adopted = ратифицированная реальность). Adding a new "Proposed" invariant that binds the consent object is exactly the right way to PROPOSE the change — it becomes binding only after ADR-008 is ratified. This matches AD-001..007 which are "Proposed" pending their ADRs.

Good. So the spine change = add AD-009 (Proposed, ADR-008) capturing the consent/recurring invariants: (a) consent is a first-class object, (b) recurring debit crediting follows AD-005 (credit only from confirmed debit status), (c) consent limits authoritative at NSPK, gateway stores copy + anti-fraud, (d) idempotency extends to consent/debit operations, (e) consent data = ПДн (AD-007). This maps the invariant to the spine.

Now, let me think carefully about the actual DESIGN content, because that's the substance.

## DESIGN: Recurring C2B debits (СБП-подписки)

### Domain objects
1. **Consent (Согласие / подписка СБП)** — the payer's consent for the TSP to debit their account on a recurring basis. Authoritative in NSPK; gateway stores `consentId` (gateway id), `opkcConsentRef` (NSPK reference/token), `tspId`, payer reference (minimized), limits (max amount per debit, period/frequency, validity), status.

2. **Recurring payment (списание)** — a single debit under a consent, initiated by TSP. Reuses the payment state machine concept but with a different entry (no QR, no payer action).

### Consent lifecycle (state machine)
States:
- `CONSENT_CREATED` — TSP requested consent setup; consent link/QR issued to payer (via NSPK).
- `CONSENT_PENDING` — payer is confirming in their bank app (link opened, not yet confirmed). Actually "CREATED → PENDING_CONFIRMATION → ACTIVE".
- `CONSENT_ACTIVE` — payer confirmed; consent registered in NSPK; debits allowed.
- `CONSENT_REVOKED` — payer or TSP revoked; no new debits.
- `CONSENT_EXPIRED` — validity period ended.
- `CONSENT_REJECTED` — payer declined (optional).
- (technical sub-states: `CONSENT_REGISTERING` while registering in NSPK.)

Let me align with the existing payment FSM style. The existing payment FSM states are CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED, with technical ABS_PENDING/NOTIFY_PENDING.

For consent, I'll define:
- `CREATED` (consent request created by TSP)
- `LINK_ISSUED` (consent link/QR issued to payer — analogous to QR_ISSUED)
- `ACTIVE` (payer confirmed, NSPK registered the consent — the "confirmed" state)
- `REVOKED` (terminated by payer or TSP)
- `EXPIRED` (validity ended / max duration reached)
- `REJECTED` (payer declined / NSPK rejected)
Technical: `REGISTERING` (registration in NSPK in progress).

Transitions:
- C1: (—) → CREATED: TSP `POST /v1/consents` (create consent request).
- C2: CREATED → LINK_ISSUED: adapter returns consent link (NSPK).
- C3: CREATED → REJECTED: NSPK rejected consent request (invalid TSP/params).
- C4: LINK_ISSUED → ACTIVE: NSPK notifies consent confirmed by payer (`consent.activated`).
- C5: LINK_ISSUED → REJECTED: payer declined (`consent.rejected`).
- C6: ACTIVE → REVOKED: payer or TSP revokes (`consent.revoked`).
- C7: ACTIVE → EXPIRED: validity period / max duration reached (`consent.expired`), or max count reached.
- C8: LINK_ISSUED → EXPIRED: payer never confirmed, link TTL expired.

Guards:
- Only `ACTIVE` consent allows a debit.
- Revocation: payer (through NSPK → `consent.revoked` event) or TSP (`POST /v1/consents/{consentId}/revoke`).
- Idempotency: `Idempotency-Key` on create; `eventId` on NSPK events; `consentId` for revoke.

### Recurring debit lifecycle (state machine)
The recurring payment reuses the payment FSM but enters differently. Options:
- (a) Extend the existing payment FSM with a new entry state / skip QR.
- (b) Separate "recurring payment" FSM.

I think the cleanest is: a recurring debit IS a payment, but with `qrType`-like distinction and a different entry. However, the existing payment FSM has CREATED→QR_ISSUED→PAID→CREDITED→COMPLETED. For a recurring debit:
- No QR is issued (no payer action). 
- TSP initiates: `POST /v1/consents/{consentId}/payments` (or `POST /v1/recurring-payments`).
- Gateway → adapter → NSPK debits (pull). NSPK confirms debit → equivalent of PAID (confirmed debit status) → credit TSP → COMPLETED.

So the recurring payment FSM:
- `CREATED` (debit initiated, TSP request) → (no QR_ISSUED) → `PENDING` (awaiting NSPK debit result) → `PAID` (debit confirmed by NSPK) → `CREDITED` → `COMPLETED`. Plus `FAILED` (insufficient funds / declined), `EXPIRED` (N/A for debit, or timeout), `REFUNDED`.

Wait — but AD-005's invariant is "credit only from PAID (confirmed NSPK status)". For recurring debits, the "confirmed" status is the confirmed debit. I need to map this. The cleanest: recurring debits reuse the same payment FSM, where:
- `PAID` = "подтверждённое списание" (NSPK confirmed the debit succeeded).
- The entry skips QR_ISSUED (no QR). But the FSM currently has CREATED→QR_ISSUED→PAID as the canonical path. 

I think the design should be: recurring debit is a **separate payment kind** with its own (narrower) FSM, but sharing the same financial invariant: credit to TSP only after NSPK confirms the debit. I'll define a separate state machine `docs/spec/subscription-state-machine.md` with the recurring-debit FSM, explicitly noting it honors AD-005's rule (credit only from confirmed status) and reuses the idempotency/outbox/audit machinery.

Recurring debit states:
- `CREATED` — TSP initiated debit under active consent.
- `SUBMITTED` — debit sent to NSPK (via adapter), awaiting result.
- `PAID` — NSPK confirmed the debit (funds collected from payer). ← "confirmed" status, credit allowed (AD-005 analog).
- `CREDITED` — TSP credited in ABS.
- `COMPLETED` — notified TSP.
- `FAILED` — NSPK declined (insufficient funds, limits exceeded, consent revoked, etc.).
- `REFUNDED` — full refund completed (saga reuse).

Transitions:
- R1: (—) → CREATED: `POST /v1/consents/{consentId}/payments` (or `/v1/recurring-payments`), Idempotency-Key, amount, consentId.
- R2: CREATED → SUBMITTED: adapter accepted debit request (`reference` = paymentId).
- R3: CREATED → FAILED: adapter rejected immediately (invalid consent/params).
- R4: SUBMITTED → PAID: NSPK confirms debit (`payment.paid` event, or reconciliation).
- R5: SUBMITTED → FAILED: NSPK declines (`payment.rejected` — insufficient funds, etc.).
- R6: PAID → CREDITED: ABS confirms credit (absDocId), idempotent by paymentId.
- R7: CREDITED → COMPLETED: webhook delivered.
- R8: COMPLETED → REFUNDED: full refund saga.

Guards:
- Debit only if consent is `ACTIVE`.
- Amount ≤ consent max limit (sanity check against gateway's copy of NSPK limits; NSPK authoritative).
- Idempotency: `Idempotency-Key` (TSP), `eventId` (NSPK), `paymentId` (ABS).

This is clean and honors AD-005. 

### TSP API changes (deliverable #4)

New endpoints (additive to /v1, no breaking changes):
1. `POST /v1/consents` — TSP creates a consent request (payer subscribes). Request: `tspId`, payer identifier (minimized — e.g., phone mask or a TSP-side customer reference; per AD-007 ПДн minimization), `merchantOrderId`, limits (maxAmountPerDebit, maxTotalAmount?, period, expiresAt?), `returnUrl` (for the consent link), `redirectUrl`. Response: `consentId`, `consentUrl` (link to open payer's bank app), `status: LINK_ISSUED`.
   - Idempotency-Key required.
2. `GET /v1/consents/{consentId}` — consent status. Response: consentId, status, limits, tspId, createdAt, activatedAt, revokedAt, etc.
3. `POST /v1/consents/{consentId}/revoke` — TSP revokes consent. Idempotency-Key. Response: status REVOKED (or 202).
4. `POST /v1/consents/{consentId}/payments` — TSP initiates a recurring debit under active consent. Request: `amount` (kopecks), `merchantOrderId`, `paymentPurpose`, optional `Idempotency-Key`. Response: `paymentId`, `status: CREATED` (or SUBMITTED). 
   - Alternatively `POST /v1/recurring-payments` with `consentId` in body. But nested under consent is cleaner REST.
5. `GET /v1/payments/{paymentId}` — already exists; recurring debits are payments, so status query reuses this. The payment object gets an optional `consentId` field and `paymentType: QR | RECURRING`.

Webhook events (new):
- `consent.activated` — consent active.
- `consent.revoked` — consent revoked.
- `consent.expired` — consent expired.
- `payment.failed` — already exists, now also for insufficient-funds debit declines (reason code).
- `payment.completed` — already exists, used for recurring debit completion.

New error codes:
- `CONSENT_NOT_ACTIVE` (422) — debit attempted on non-active consent.
- `CONSENT_NOT_FOUND` (404).
- `AMOUNT_EXCEEDS_CONSENT_LIMIT` (422).
- `CONSENT_ALREADY_REVOKED` (409).

OpenAPI additions: new paths `/v1/consents`, `/v1/consents/{consentId}`, `/v1/consents/{consentId}/revoke`, `/v1/consents/{consentId}/payments`; new schemas ConsentRequest, Consent, RecurringPaymentRequest (or reuse PaymentRequest with consentId), and extend Payment schema with `consentId` + `paymentType` (optional, additive). Since the existing `PaymentRequest` has `required: [amount, merchantOrderId]`, adding optional fields is backward-compatible. Adding new paths is backward-compatible. Extending `Payment` with optional fields is backward-compatible.

Important: the existing OpenAPI is quite minimal (only /v1/payments POST and GET). I should extend it consistently with the richer `docs/contracts/tsp-api.md`. I'll add the new paths and schemas, and optionally add the missing fields to PaymentRequest (tspId, currency, qrType, etc.) — but wait, the user said "без поломки существующих потребителей". The existing OpenAPI only has a minimal PaymentRequest/Payment. The richer tsp-api.md has more fields. I should be careful: the OpenAPI yaml is the machine contract; tsp-api.md is the human doc. The yaml is v0.1.0 and minimal. I should ADD to the yaml the consent/recurring paths and schemas, in a backward-compatible way, and also add the `consentId`/`paymentType` optional fields to Payment, and `consentId` to PaymentRequest (optional) so a payment can be tagged as recurring.

Actually, for recurring debits, the request goes through a separate endpoint (`/v1/consents/{consentId}/payments`), so `PaymentRequest` doesn't strictly need a consentId — but the GET payment response should indicate it's a recurring payment and link the consent. I'll add optional `consentId` and `paymentType` to `Payment`, and a new `RecurringPaymentRequest` schema.

Let me also make sure I DON'T break the existing required fields. Existing `PaymentRequest` required `[amount, merchantOrderId]`. I'll keep that. New `RecurringPaymentRequest` can be `{amount, merchantOrderId, paymentPurpose?}`. Actually I can just reuse `PaymentRequest` for the recurring debit endpoint too (amount + merchantOrderId are both needed), and consentId is in the path. So no new request schema needed — reuse PaymentRequest. But I might add optional `paymentPurpose` to PaymentRequest (backward-compatible additive).

### OPKC adapter contract changes (deliverable #4, internal)

New sync methods (ядро → адаптер):
- `createConsent` — create consent request; `reference` (= consentId), `tspId`, payer ref, limits; → `consentOpcRef`, `consentUrl`, `ACCEPTED` (result by event).
- `getConsentStatus` — by `consentOpcRef`.
- `revokeConsent` — `consentOpcRef`, `reference`; → ACCEPTED.
- `createRecurringPayment` — `reference` (= paymentId), `consentOpcRef`, `amount`, `purpose?`; → ACCEPTED (result by event). (This is the debit.)

New events (адаптер → ядро):
- `consent.activated` — `consentOpcRef`, `reference` (= consentId), limits (as confirmed by payer).
- `consent.rejected` — reasonCode.
- `consent.revoked` — `consentOpcRef`, `reference`, `reason` (payer/TSP/expired).
- `consent.expired`.
- (reuse `payment.paid`, `payment.rejected` for debit results.)

Note: the adapter normalizes NSPK specifics; exact NSPK consent protocol = [ТРЕБУЕТ ПРОВЕРКИ].

### NFR (deliverable #5)

New measurable NFRs for recurring:
- Consent link issuance: p95 < 500 ms (same as QR).
- Consent status query: p95 < 300 ms.
- Recurring debit initiation (submit to NSPK): p95 < 500 ms.
- Recurring debit completion → TSP credit: p95 < 60 s (same ABS SLA).
- Throughput: recurring debits share the 200 TPS sustained / 500 peak envelope; consent creation lower (e.g., 50 TPS sustained).
- Availability: same ≥ 99.95%.
- Consent data: ПДн minimized; consent lifecycle events 100% in audit log; consent revocation propagation p95 < 5 s.
- No duplicate debits on retry (idempotency) — 0.
- Consent limit violation attempts: 100% blocked (sanity-check) — 0 unauthorized debits.
- Reconciliation: consent statuses reconciled with NSPK (daily or per reglament).

I'll add a new section "8. Рекуррентные списания (подписки СБП)" to docs/nfr.md.

### Acceptance criteria & rollback (deliverable #6)

Acceptance criteria (gates):
- Consent + debit state machines spec complete (transitions, guards, idempotency keys).
- Contract changes backward-compatible (existing /v1/payments POST/GET unchanged; new paths additive; old consumers unaffected).
- Fitness tests: (a) debit only from ACTIVE consent; (b) credit only from PAID (confirmed debit) — AD-005 analog; (c) idempotent duplicate NSPK events/debit requests → no double credit; (d) consent revocation blocks subsequent debits.
- Negative scenarios: insufficient funds (payment.rejected → FAILED, no credit), consent revoked mid-flight, duplicate debit request (Idempotency-Key), NSPK unavailable (transport.unavailable → debit queued/degraded), late consent.activated event after revoke.
- NFR pass (load tests).

Rollback plan:
- Feature flag for recurring endpoints (`recurring_enabled`); off by default; stop-new (block new consent/debit creation) without stopping existing operations.
- Consent is a new object — no data migration of existing payments; existing QR flow untouched.
- Rollback of the feature = disable endpoints; existing completed debits remain, refunds via existing saga.
- If NSPK consent mechanism not as assumed [ТРЕБУЕТ ПРОВЕРКИ] → adapter contract change isolated to adapter (AD-008), core unaffected.
- Emergency: DLQ + runbook for stuck debits; reconciliation with NSPK compensates.

### Open decisions for human (deliverable #7)

1. **Exact NSPK consent protocol** — [ТРЕБУЕТ ПРОВЕРКИ]. The whole consent model assumes NSPK has a subscription/consent mechanism with payer confirmation in their bank app. If NSPK's actual mechanism differs (e.g., consent captured outside NSPK), the adapter contract §consent changes; core unchanged (AD-008). Decision: confirm with НСПК documentation; this is a gate to implementing the transport.
2. **Payer identifier for consent** — what minimal payer identifier the TSP passes to initiate a consent (phone mask? bank app redirect?). ПДн minimization vs. usability. Needs ИБ/152-ФЗ sign-off.
3. **Consent limits schema** — which limit dimensions (max per debit, period, total, expiry) NSPK actually supports; which we must mirror in the gateway. Tied to #1.
4. **115-ФЗ / anti-fraud thresholds for recurring** — thresholds and screening rules (higher risk of "silent" debits). Needs AML/комплаенс.
5. **Refund policy for recurring debits** — whether the existing refund saga covers recurring (assumed yes), and any return windows.
6. **Business tariff/comission model** — not architectural but affects reporting (already an open question in solutioning).
7. **Scope expansion timing vs C2C/выплаты** — recurring debits pull the roadmap forward; confirm priority vs deferred items.

Now, I also need to decide: should I actually make all these file edits now, or present the design first for approval (per brainstorming HARD-GATE)?

Re-reading the brainstorming HARD-GATE: "Architectural: the human partner reviews and approves the written spec, then reviews the written implementation plan and selects its execution method."

But the user's request is explicitly to PRODUCE the architectural package (which IS the "written spec"/design artifact). The user said "Когда закончишь, кратко перечисли созданные и изменённые файлы" — they expect me to finish by creating files.

There's tension: the brainstorming skill wants approval BEFORE writing the spec. But the user has already approved the key decisions (via the 4 questions) and asked me to produce the package.

I think the right interpretation: the user's request IS the design task, and the "implementation" here = writing the architectural docs (the package). The user has pre-authorized producing the package (that's the explicit ask), and I've gotten approval on the load-bearing decisions. So I should now produce the full package (write the files), then present a summary and note that the human architect still needs to review/ratify (which is deliverable #7 — the human decision).

Actually, the brainstorming skill would have me present the design in sections and get approval before writing files. But that would be extremely heavyweight for a task where the user explicitly asked for a complete deliverable "to be taken to the architecture decision". The user is the one who will take it to the A3 gate. My job is to prepare the package.

I'll proceed to write the files. This is consistent with: the user's explicit request, the confirmed decisions, and the "proactiveness" mandate (fulfill the request thoroughly). I'll present the design content within the files themselves (which is what the repo expects — ADR format), and in my final summary I'll flag what needs human decision.

Let me also double check: the user said "Код не пиши" — don't write code. The OpenAPI yaml is a contract spec, not code (it's declarative). And I'm modifying it as a contract. This is fine — deliverable #4 explicitly asks for contract changes in `openapi/tsp-api.yaml`.

Now, let me plan the actual content and write the files. This is a large amount of writing. Let me be thorough but efficient.

Let me decide final file list and order:

1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md` (new) — ADR.
2. `docs/spec/subscription-state-machine.md` (new) — consent + recurring debit FSM.
3. `docs/change-podpiski-sbp.md` (new) — significance/route + invariant impact + acceptance criteria + rollback + open decisions. (This is the "package summary" / the doc to take to A3.)

Actually, let me reconsider the naming and reduce proliferation. Maybe combine #1 (significance/route) + #2 (invariant impact) + #6 (acceptance + rollback) + #7 (open decisions) into ONE "decision package" doc, and keep ADR-008 as the decision itself, plus the state-machine spec, plus NFR (in nfr.md), plus contract edits.

Final plan — files:

**NEW:**
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md` (deliverable #3 — decision + alternatives + consequences + reversibility; includes a compact "impact on invariants" subsection and "open questions" subsection).

Hmm, but I want the "significance/route" (#1) and "invariant impact" (#2) and "acceptance/rollback" (#6) and "open decisions" (#7) to be clearly addressed. I could put #1, #2, #6, #7 in the ADR as well (Context + Consequences + "Acceptance & Rollback" + "Open questions"). ADRs in this repo do have Consequences and References; acceptance/rollback aren't standard ADR sections though.

Let me look at how the repo handles acceptance criteria and rollback: it's in `solutioning.md §7` (gates) and §8 (rollback). So acceptance + rollback belong in a "solutioning"-style doc or the change-assessment doc.

Decision: I'll create a dedicated **change package doc** that serves as the single entry point for the human architect, containing all 7 deliverables in order, with the ADR and spec and NFR and contract edits as supporting artifacts. Actually no — that duplicates content.

Cleaner: 
- ADR-008 = decision (deliverable #3), with a compact "влияние на инварианты" table inside (part of #2), plus "открытые вопросы" (part of #7).
- New spec = consent/debit FSM (part of #3 design).
- New assessment doc `docs/change-podpiski-sbp.md` = significance/route (#1), full invariant impact (#2), acceptance criteria + rollback (#6), consolidated open decisions (#7).
- NFR → edit nfr.md (add section) (#5).
- Contracts → edit tsp-api.yaml, tsp-api.md, opkc-adapter.md (#4).
- Spine → add AD-009 (#2 — reflect invariant in spine).
- solutioning → update roadmap + reference (#2 minor).
- README → update file index (minor).

That's 3 new files + edits to 6 files. Reasonable for an architectural package.

Actually, let me reconsider combining the assessment into the ADR to reduce files. The ADR already needs a "Context" that explains significance and route. And the ADR can have a section "Влияние на инварианты (AD-001..008)". And "Приёмка и откат" + "Открытые вопросы". This would make ADR-008 a comprehensive decision doc. But the repo's ADRs are relatively focused. However, ADR-007 (the A3 one) is quite comprehensive with machine-readable decision package, constraints, rejected options, expiry. So a comprehensive ADR-008 is within repo norms.

Given the user's 7 deliverables, I think the cleanest presentation is:
- **One primary "decision package" document** that walks through all 7 deliverables in order — this is the artifact to "вынести на архитектурное решение". Let me call it `docs/change-podpiski-sbp.md` and make it the master document, with the ADR, spec, NFR, contract edits as the formal sub-artifacts.

Hmm, but that risks redundancy. Let me settle on a clean separation:

**Master package doc**: `docs/change-podpiski-sbp.md` — this contains:
- §1 Significance & route (deliverable #1)
- §2 Impact on invariants AD-001..008 (deliverable #2) — table
- §3 Decision summary → pointer to ADR-008 (deliverable #3)
- §4 Contract changes → pointer to openapi/contracts (deliverable #4) + summary of additive changes
- §5 NFR → pointer to nfr.md (deliverable #5) + summary
- §6 Acceptance criteria & rollback (deliverable #6)
- §7 Open decisions for human (deliverable #7)

Plus formal artifacts:
- ADR-008 (decision, alternatives, consequences, reversibility)
- subscription-state-machine.md (FSM spec)
- edits to nfr.md, tsp-api.yaml, tsp-api.md, opkc-adapter.md, spine, solutioning, README.

This is comprehensive and clear. The master doc ties everything together and directly answers all 7 deliverables, while the formal artifacts follow repo conventions.

Actually, I worry this is a bit much and risks overlap. But the user explicitly asked for 7 distinct deliverables and said "что должно получиться" (what should result). So producing a package that clearly maps to those 7 is exactly right.

Let me also make sure I'm not over-editing "accepted files". The key accepted files to edit minimally:
- `ARCHITECTURE-SPINE.md`: add AD-009 (Proposed). This is the correct way.
- `docs/solutioning.md`: §1 roadmap — change "автоплатежи" from out-of-scope to "in scope as ADR-008 (Proposed)". And maybe add a reference in §5 ADR mapping table + §3 status model note. Minimal.
- `docs/nfr.md`: add recurring section.
- `docs/contracts/tsp-api.md`: add consent/recurring methods + webhooks + errors.
- `docs/contracts/opkc-adapter.md`: add consent/recurring methods + events.
- `openapi/tsp-api.yaml`: add paths + schemas.
- `README.md`: update structure + status.
- `docs/rfp/vendor-rfp.md`: add consent/recurring to scope + POC (optional but consistent). I'll add a concise addendum.

That's a full, coherent package. Let me write it.

Let me start writing. I'll be efficient and produce high-quality content matching the repo's tone (Russian, tables, status headers, "Related", "[ТРЕБУЕТ ПРОВЕРКИ]" markers).

Let me first write the ADR-008.

Actually, let me think about ADR numbering: existing ADRs go 001..007. New one = ADR-008. Filename convention: `ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md`. There are TWO copies of ADRs: `docs/adr/` and `.arch-handoff/adr/`. The `.arch-handoff/` is the handoff package (epic-context) — generated/synced. I should create the ADR in `docs/adr/` (the source of truth). Should I also update `.arch-handoff/`? The `.arch-handoff/` is a "пакет передачи" generated from docs. The user's task is to prepare the architecture package for decision + handoff. I think I should focus on `docs/` (source of truth) and NOT manually duplicate into `.arch-handoff/` (that's a generated artifact). But I should note it. Actually, `.arch-handoff/ARCHITECTURE.md` is the "epic-context" that aggregates ADRs. Since I'm preparing a NEW change that will itself go through decision, I'll leave `.arch-handoff/` alone (it represents the current accepted handoff for the walking skeleton). I'll create everything in `docs/` + `openapi/` + `ARCHITECTURE-SPINE.md` + `README.md`. That's consistent: `.arch-handoff/` is regenerated by the harness.

Actually, let me reconsider — do I even need to touch `.arch-handoff/`? No. The handoff package is for the code harness for the CURRENT walking skeleton (C2B QR). The recurring feature is a NEW change pending A3. So I won't touch `.arch-handoff/`. Good.

Also, the CONSTRAINTS.yaml has a fitness rule `adr-no-placeholders` requiring `docs/adr/*.md` to NOT contain `<!--`. So my new ADR-008 must not contain HTML comments. Good to remember. Also `nfr-measurable` requires `99,95` in nfr.md (already there). And `abs-credit-only-from-paid` requires ADR-005 to contain 'только из состояния `PAID`' (unchanged). My additions shouldn't break these.

Also `spine-lints-clean`: ARCHITECTURE-SPINE.md must not contain 'TODO|TBD|XXX'. My AD-009 addition must avoid those. Fine.

Now let me write all files. I'll go file by file.

Let me draft the ADR-008 content carefully.

---

### ADR-008 content draft

```markdown
# ADR-008. Рекуррентные C2B-списания по согласию плательщика: подписки СБП

- Date: 2026-09-28
- Status: Proposed (выносится на архитектурное решение A3)
- Owner: solution-architect (платёжный контур) + бизнес/CIO
- Related: ADR-002, ADR-004, ADR-005, AD-002, AD-003, AD-005, AD-007

## Context

Бизнес-запрос: ТСП сегментов «онлайн-кинотеатры», «ЖКХ», «связь» просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сегодня каждый C2B-платёж требует генерации QR/ссылки и действия плательщика (сканирование, подтверждение в приложении банка плательщика); для подписочных моделей это неприемлемо — списание должно выполняться без участия плательщика в момент платежа.

В принятом решении «автоплатежи» были явно вне scope (`docs/solutioning.md §1`, roadmap). Настоящий ADR выводит их в scope.

**Подтверждённые на брифинге решения (бизнес-входы):**
1. Согласие — через ОПКЦ НСПК: авторитетно формируется и хранится в НСПК; плательщик подтверждает в приложении своего банка по ссылке; шлюз хранит ссылку/токен и метаданные. Протокольные детали — за адаптером ОПКЦ (AD-008), `[ТРЕБУЕТ ПРОВЕРКИ]` до получения документации НСПК.
2. Инициация списания — ТСП (pull): ТСП вызывает шлюз «списать N по согласию»; планировщик в шлюзе не нужен.
3. Первая волна (MVP): жизненный цикл согласия + разовое списание по активному согласию. Без планировщика и dunning.
4. Лимиты согласия — авторитет у НСПК/банка плательщика; шлюз хранит копию и делает sanity-check + антифрод (115-ФЗ).

## Decision

1. **Новый доменный объект `Consent` (согласие/подписка СБП)** — first-class сущность со своим жизненным циклом (`docs/spec/subscription-state-machine.md`). Авторитетное хранилище — НСПК; в БД шлюза — копия с метаданными и статусом (для сверки, аудита и проверки лимитов). Идентификаторы: `consentId` (ядро) ↔ `consentOpcRef` (сквозной ОПКЦ), по аналогии с `paymentId ↔ qrId`.

2. **Рекуррентное списание — платёж без QR.** Каждое списание — платёж в существующей статусной машине (ADR-002) с собственным узким путём: `CREATED → SUBMITTED → PAID → CREDITED → COMPLETED` (+ `FAILED`, `REFUNDED`). Шаг `QR_ISSUED` отсутствует (нет действия плательщика); `PAID` = подтверждённое НСПК списание. Инвариант AD-005 сохраняется дословно: **зачисление на счёт ТСП — только из подтверждённого НСПК статуса (`PAID`)**.

3. **Идемпотентность распространяется на новые операции** (AD-003): `Idempotency-Key` на создание согласия/списания/отзыв; дедупликация событий НСПК по `eventId`; идемпотентность АБС по `paymentId` (зачисление) и по `consentId` (без повторных действий). Внутренний контракт адаптера ОПКЦ дополняется методами/событиями согласия и списания (`docs/contracts/opkc-adapter.md`).

4. **Обратная совместимость API ТСП.** Новые ресурсы `POST/GET /v1/consents`, `POST /v1/consents/{consentId}/revoke`, `POST /v1/consents/{consentId}/payments` — аддитивно, существующие `/v1/payments` не меняются. Платёж обогащается опциональными полями `paymentType` (`QR` | `RECURRING`) и `consentId`. Детали — `docs/contracts/tsp-api.md`, `openapi/tsp-api.yaml`.

5. **Соответствие (AD-006, AD-007).** Согласие и реквизиты плательщика — ПДн (152-ФЗ): минимизация (плательщик идентифицируется минимально необходимым для НСПК), шифрование в покое, маскирование в логах. Списание без действия клиента — повышенный риск: передача в антифрод/AML (115-ФЗ) по порогам. Аудит-лог — каждый переход согласия и списания.

## Alternatives Considered

| Вариант | Плюсы | Минусы |
|---|---|---|
| **Согласие через НСПК (выбран)** | Авторитет у НСПК, плательщик подтверждает в привычном банковском приложении; шлюз не несёт бремя хранения волеизъявления; соответствует «подпискам СБП» как продукту НСПК | Зависимость от механизма НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`; до получения документации нельзя финализировать протокольные детали |
| Согласие уровня шлюза | Полный контроль, независимость от НСПК | Шлюз становится держателем волеизъявления (юридически нагружено, 152-ФЗ/161-ФЗ), дублирование функционала банка плательщика; риск рассинхронизации с НСПК |
| Гибрид / нейтрально | Гибкость | Размывает границы, откладывает решение — не даёт передать пакет исполнителям |

| Вариант | Плюсы | Минусы |
|---|---|---|
| **ТСП-инициация (pull) (выбран)** | Подписочная логика/биллинг остаются у ТСП; шлюз — фасилитатор; нет планировщика и его эксплуатации в MVP | Шлюз не контролирует регулярность; нужна проверка лимитов/антифрод на каждое списание |
| Шлюз по расписанию (push) | Централизованный контроль, dunning на шлюзе | Планировщик + хранение расписаний, рост ответственности шлюза; вне MVP |
| Оба режима | Полнота | Сложность MVP, откладывает первую волну |

| Вариант | Плюсы | Минусы |
|---|---|---|
| **MVP: согласие + списание (выбран)** | Быстрая ценность, доказуемый сквозной сценарий | Без dunning/повторов; при неуспехе списания — ручной/ТСП-инициированный повтор |
| Плюс dunning/повторы | Автоматизация неуспехов | Дополнительный планировщик, рост scope, откладывает решение |
| Полный объём (частичные возвраты + ЛК) | Полнота продукта | Размывает MVP, частичные возвраты/ЛК — отдельные решения |

## Consequences

### Positive
- Подписочные ТСП получают сквозной сценарий без QR/действия плательщика, на существующем ядре (переиспользование статусной машины, outbox, сверки, АБС-интеграции, нотификатора).
- Инвариант AD-005 (зачисление только из подтверждённого статуса) сохраняется без изменений — финансовая модель не пересматривается.
- Контрактная независимость ядра от транспорта (AD-008) сохраняется: механизм согласия НСПК скрыт за адаптером, ядро оперирует нормализованными событиями.
- Обратная совместимость: существующие ТСП и вендор-контракт не ломаются.

### Negative
- Новый доменный объект и жизненный цикл → расширение БД, статусной модели, сверки и отчётности.
- Повышенный комплаенс-вес: списание без действия клиента, ПДн согласия, 115-ФЗ/антифрод — дополнительный контроль (замедление релизов через ИБ).
- Зависимость от механизма НСПК `[ТРЕБУЕТ ПРОВЕРКИ]` — риск пересмотра адаптерного контракта после получения документации (изолирован AD-008).
- Два «вида» платежей (QR и рекуррентный) — усложнение статусной модели и отчётности.

## Reversibility

**reversible на уровне ядра и контрактов.** Согласие и рекуррентные списания — новый аддитивный ресурс: откат = отключение фиче-флага и запрет создания новых согласий/списаний; существующие QR-платежи и возвраты не затрагиваются; данные не мигрируются обратно (шлюз остаётся источником истины до полной сверки). Необратимость возникает только после боевой эксплуатации рекуррентных списаний (накопленные согласия и проводки) — тогда откат costly, как и у базового решения (ADR-001). Если механизм НСПК окажется иным (`[ТРЕБУЕТ ПРОВЕРКИ]`), пересматривается только адаптерный контракт (ADR-003 reversible), ядро не меняется.

## References
- AD-002 (spine): единый источник истины — статусная машина платежа
- AD-003 (spine): идемпотентность финансовых операций
- AD-005 (spine): зачисление только из подтверждённого статуса
- AD-007 (spine): соответствие НПС, КИИ, ПДн
- ADR-002 (статусная машина), ADR-004 (нотификации/сверка), ADR-005 (АБС)
- `docs/spec/subscription-state-machine.md` — спецификация переходов согласия и списания
- `docs/change-podpiski-sbp.md` — пакет изменения (значимость, влияние, приёмка, откат)
```

That's a solid ADR. Let me refine the reversibility wording and make sure "reversible" / "costly" matches the repo style (they use "costly", "reversible").

Now the state machine spec.

### subscription-state-machine.md draft

```markdown
# Статусная машина подписок СБП: согласие и рекуррентное списание

- Status: Draft (для ревью на гейте A1)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-008, ADR-002, ADR-005, AD-002, AD-003, AD-005

Два связанных конечных автомата: **согласие** (`Consent`) и **рекуррентное списание** (`RecurringPayment`). Оба следуют правилам ADR-002: переход — атомарная транзакция «смена статуса + outbox + аудит» (AD-002), повторные триггеры идемпотентны (AD-003).

## 1. Согласие (Consent)

### Состояния

| Состояние | Смысл | Виден ТСП |
|---|---|---|
| `CREATED` | ТСП инициировал создание согласия; запрос к ОПКЦ в процессе | да |
| `LINK_ISSUED` | Получена ссылка для подтверждения плательщиком; ожидается подтверждение | да |
| `ACTIVE` | **Подтверждено НСПК**: плательщик принял, согласие зарегистрировано; списания разрешены | да |
| `REVOKED` | Отозвано плательщиком или ТСП; новые списания запрещены | да |
| `EXPIRED` | Истёк срок действия / не подтверждено за TTL | да |
| `REJECTED` | НСПК отклонил (реквизиты/лимиты) или плательщик отказался | да |

Техническое: `REGISTERING` (регистрация в ОПКЦ в процессе) — наружу не выставляется.

### Переходы

| № | From | To | Триггер | Guard | Действие |
|---|---|---|---|---|---|
| C1 | — | `CREATED` | `POST /v1/consents` (новый `consentId`) | ТСП активен, валидный запрос | запись согласия + outbox «регистрация в ОПКЦ» |
| C2 | `CREATED` | `LINK_ISSUED` | ответ адаптера: `consentUrl` получен | `consentUrl` непустой | сохранить `consentOpcRef`/`consentUrl`, outbox |
| C3 | `CREATED` | `REJECTED` | ошибка регистрации (не транзиентная) | — | `errorCode`, вебхук `consent.rejected` |
| C4 | `LINK_ISSUED` | `ACTIVE` | событие `consent.activated` (или сверка) | плательщик подтвердил; лимиты зафиксированы | сохранить лимиты, outbox, вебхук `consent.activated` |
| C5 | `LINK_ISSUED` | `REJECTED` | событие `consent.rejected` | — | `errorCode`, вебхук `consent.rejected` |
| C6 | `LINK_ISSUED` | `EXPIRED` | таймер TTL | `ACTIVE` не наступил | outbox, вебхук `consent.expired` |
| C7 | `ACTIVE` | `REVOKED` | `POST /v1/consents/{consentId}/revoke` (ТСП) или событие `consent.revoked` (плательщик) | было `ACTIVE` | outbox, вебхук `consent.revoked` |
| C8 | `ACTIVE` | `EXPIRED` | истечение срока действия / лимит исчерпан | — | outbox, вебхук `consent.expired` |

### Инварианты
- Списание разрешено **только из `ACTIVE`** (guard на списание).
- `REVOKED`/`EXPIRED`/`REJECTED` — терминальные; переходов нет (повторные триггеры идемпотентны).
- Отзыв/истечение после `ACTIVE` необратимы; повторное согласие — новый `consentId`.

## 2. Рекуррентное списание (RecurringPayment)

Платёж, инициируемый ТСП по активному согласию. Шаг `QR_ISSUED` отсутствует — нет действия плательщика. `PAID` = подтверждённое НСПК списание.

### Состояния

| Состояние | Смысл | Виден ТСП |
|---|---|---|
| `CREATED` | Списание инициировано ТСП, запрос к ОПКЦ в процессе | да |
| `SUBMITTED` | Запрос списания передан адаптеру/НСПК | да (технич. — можно как `creditingStatus`-стиль, но виден) |
| `PAID` | **Подтверждённое НСПК списание** (средства собраны с плательщика) | да |
| `CREDITED` | Зачисление на счёт ТСП выполнено (`absDocId`) | да (как `creditingStatus`) |
| `COMPLETED` | Доведено до ТСП (вебхук) | да |
| `FAILED` | НСПК отклонил (недостаточно средств, лимит, согласие не активно) | да |
| `REFUNDED` | Полный возврат завершён (сага) | да |

Технические: `ABS_PENDING`, `NOTIFY_PENDING` — как в платеже (ADR-002).

### Переходы

| № | From | To | Триггер | Guard | Действие |
|---|---|---|---|---|---|
| R1 | — | `CREATED` | `POST /v1/consents/{consentId}/payments` | согласие `ACTIVE`; сумма ≤ лимита согласия (sanity-check) | запись списания + outbox «списание в ОПКЦ» |
| R2 | `CREATED` | `SUBMITTED` | ответ адаптера: списание принято | — | outbox |
| R3 | `CREATED` | `FAILED` | адаптер отклонил сразу (невалидное согласие/сумма) | — | `errorCode`, вебхук `payment.failed` |
| R4 | `SUBMITTED` | `PAID` | событие `payment.paid` (или сверка) | сумма совпадает | outbox «зачисление в АБС» |
| R5 | `SUBMITTED` | `FAILED` | событие `payment.rejected` (недостаточно средств и пр.) | — | `errorCode`, вебхук `payment.failed` |
| R6 | `PAID` | `CREDITED` | подтверждение АБС (`absDocId`) | идемпотентно по `paymentId` | сохранить `absDocId`, outbox |
| R7 | `CREDITED` | `COMPLETED` | вебхук доставлен/в очереди | — | outbox, вебхук `payment.completed` |
| R8 | `COMPLETED` | `REFUNDED` | сага возврата завершена (ADR-005) | полный возврат | outbox, вебхук `refund.completed` |

### Инварианты (сохранение AD-005)
- **Зачисление — только из `PAID`** (подтверждённое НСПК списание). Из `CREATED`/`SUBMITTED` недостижимо.
- Списание — только при `ACTIVE` согласии.
- `FAILED`/`REFUNDED` — терминальные.

## 3. Идемпотентность

| Триггер | Ключ | Поведение при повторе |
|---|---|---|
| `POST /v1/consents` | `Idempotency-Key` | тот же `consentId`, состояние не меняется |
| `POST /v1/consents/{consentId}/revoke` | `Idempotency-Key` | повторный отзыв — тот же результат (уже `REVOKED`) |
| `POST /v1/consents/{consentId}/payments` | `Idempotency-Key` | тот же `paymentId`, повторное списание не создаётся |
| событие `consent.activated` | `eventId` | обработанный `eventId` игнорируется |
| событие `payment.paid` | `eventId` | обработанный игнорируется; новый по завершённому — алерт |
| подтверждение АБС | `paymentId` | маппинг `paymentId → absDocId`, повторной проводки нет |

## 4. Сверка и восстановление
- Открытые состояния согласия (`LINK_ISSUED`, `ACTIVE`) и списания (`SUBMITTED`, `PAID`, `ABS_PENDING`) — кандидаты сверки с НСПК.
- «У НСПК `ACTIVE`, у нас нет» → дозапрос статуса согласия.
- «У нас `ACTIVE`, у НСПК нет» → стоп-сигнал, эскалация.
- Списание в `PAID` с недоступной АБС — остаётся `PAID`, зачисление гарантируется сверкой.

## 5. Маппинг на API ТСП
Согласие: `CREATED`, `LINK_ISSUED`, `ACTIVE`, `REVOKED`, `EXPIRED`, `REJECTED`. Списание — статусы платежа (§3.3 tsp-api) + опциональные `paymentType=RECURRING`, `consentId`.
```

Good. Now the change package doc (master doc). Let me draft.

### docs/change-podpiski-sbp.md draft

This should cover deliverables #1, #2, #6, #7, and summarize #3/#4/#5 with pointers.

```markdown
# Изменение: рекуррентные C2B-списания по согласию плательщика (подписки СБП)

Пакет архитектурного изменения поверх принятого решения «Платёжный шлюз СБП (C2B-приём)». Готовится к выносу на архитектурное решение (A3) и последующей передаче исполнителям.

- Status: Draft (выносится на A3)
- Owner: solution-architect (платёжный контур) + бизнес/CIO
- Связано: ADR-008, `docs/spec/subscription-state-machine.md`, `docs/nfr.md`, `docs/contracts/tsp-api.md`, `docs/contracts/opkc-adapter.md`

## 1. Оценка значимости и маршрута

**Значимость: Critical (соразмерно базовому решению, 11/15).** Новый финансовый доменный объект, списание без действия клиента (повышенный регуляторный/антифрод-профиль), изменение публичного контракта API ТСП и внутреннего контракта вендорского адаптера.

**Маршрут — архитектурный (full Solutioning), не bounded и не spike.** Обоснование: (1) добавляется новый доменный объект с собственным жизненным циклом; (2) меняется контракт, от которого зависят внешние потребители (ТСП) и вендор (адаптер ОПКЦ); (3) затрагивается инвариант финансового перехода (AD-005 — хотя сам инвариант сохраняется, его поверхность расширяется новым путём `SUBMITTED→PAID`); (4) комплаенс-развилки (152-ФЗ/115-ФЗ) требуют человеческого решения.

Требуемый объём проектирования: полный (ADR + спецификация автомата + правки контрактов + NFR + приёмка/откат). Код не пишется — пакет для решения и передачи.

## 2. Влияние на принятую архитектуру (инварианты AD-001..AD-008)

| Инвариант | Затронут? | Что меняется | Что не меняется |
|---|---|---|---|
| AD-001 Изоляция платёжного контура | Нет | — | СБП-шлюз остаётся единственной точкой; согласие/списание — внутри того же контура |
| AD-002 Единый источник истины — статусная машина | Да (расширение) | Добавляются автоматы согласия и списания; Rule «статус+outbox в одной транзакции» распространяется на них | Сам Rule не меняется; механизм атомарных переходов прежний |
| AD-003 Идемпотентность | Да (расширение) | Новые ключи: `Idempotency-Key` на согласие/отзыв/списание, `eventId` на события согласия | Принцип «повторная доставка не меняет завершённое состояние» не меняется |
| AD-004 Единственный адаптер ОПКЦ | Нет (расширение контракта) | Контракт адаптера дополняется методами/событиями согласия и списания | Протокол НСПК по-прежнему знает только адаптер |
| AD-005 Зачисление только из подтверждённого статуса | Да (та же суть, новый путь) | Для списания `PAID` = подтверждённое НСПК списание; зачисление только из него | Инвариант дословно сохранён; зачисление из `CREATED`/`SUBMITTED` недостижимо |
| AD-006 Trust-зоны и сегментация | Нет | — | Те же зоны; согласие — ПДн в платёжном контуре |
| AD-007 Соответствие НПС/КИИ/ПДн | Да (расширение) | Согласие + реквизиты плательщика — ПДн (152-ФЗ); списание без действия клиента — антифрод/115-ФЗ | Требования криптографии/аудита/СКЗИ не меняются |
| AD-008 Стратегия (гибрид) [ADOPTED] | Нет (уточнение) | Расширяется scope вендорского адаптера (согласие/списание) | Граница контракта и независимость ядра от транспорта не меняются |

**Новое:** предлагается добавить в spine инвариант `AD-009` (Proposed, ADR-008) — см. `ARCHITECTURE-SPINE.md`.

## 3. Архитектурное решение
См. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md` (решение, альтернативы, последствия, обратимость).

## 4. Изменения контрактов (без поломки потребителей)
См. `docs/contracts/tsp-api.md` (новые методы/события/ошибки) и `docs/contracts/opkc-adapter.md` (методы/события согласия и списания). Машиночитаемый контракт — `openapi/tsp-api.yaml`.

Принцип обратной совместимости: только аддитивные изменения — новые пути `/v1/consents`, опциональные поля `paymentType`/`consentId` в платеже, новые вебхуки и коды ошибок. Существующие `/v1/payments` (POST/GET) и их обязательные поля не меняются.

## 5. NFR
См. `docs/nfr.md` (раздел «Рекуррентные списания»). Ключевое: выдача ссылки согласия p95 < 500 мс; списание p95 < 500 мс до НСПК; зачисление от подтверждения p95 < 60 с; отсутствие дублей списания = 0; блокировка списания по неактивному согласию = 100 %.

## 6. Критерии приёмки и план отката

### Приёмка (гейты A4/A5)
- [ ] Спецификация автоматов согласия и списания полная (переходы, guards, ключи идемпотентности) — `docs/spec/subscription-state-machine.md`.
- [ ] Контракт обратно совместим: существующие потребители `/v1/payments` не затронуты (тест на неизменность обязательных полей и путей).
- [ ] Fitness-тесты: списание только из `ACTIVE`; зачисление только из `PAID` (подтверждённое списание); повторные события/запросы идемпотентны (0 двойных зачислений/списаний).
- [ ] Негативные сценарии: недостаточно средств (`payment.rejected` → `FAILED`, без зачисления); согласие отозвано в момент списания → `CONSENT_NOT_ACTIVE`; дубль `Idempotency-Key` → тот же `paymentId`; НСПК недоступен → `transport.unavailable`, списание в очереди/degraded, без потери.
- [ ] NFR выполнены на моках (нагрузка, лаги, идемпотентность).

### План отката
- **До боевой эксплуатации**: откат = не включать фиче-флаг; все артефакты обратимы (ADR-008 reversible).
- **После включения**: фиче-флаг `recurring_enabled` (по умолчанию off); мгновенный stop-new — запрет создания новых согласий/списаний без остановки обработки уже открытых; откат релиза — rolling; существующие QR-платежи и возвраты не затрагиваются; данные не мигрируются обратно (шлюз — источник истины до полной сверки).
- **Аварийный сценарий**: зависшее списание → DLQ + runbook; сверка с НСПК компенсирует потерянные нотификации; RTO ≤ 1 ч (как у базового решения).
- **Триггер отката**: > 0 несанкционированных списаний по неактивному согласию; дубль зачисления; расхождение сверки по согласиям, не разрешаемое runbook'ом.
- **Владелец решения об откате**: solution-architect + бизнес-владелец продукта (дежурная смена исполняет).

## 7. Что остаётся на решение человека-архитектора

1. **Точный механизм согласия НСПК** `[ТРЕБУЕТ ПРОВЕРКИ]` — подтвердить, что у НСПК есть механизм «подписка/согласие» с подтверждением плательщиком в приложении его банка. Если механика иная — пересматривается только адаптерный контракт (ADR-008), ядро не меняется. Это gate для реализации транспорта.
2. **Идентификатор плательщика в согласии** — какое минимальное ПДн ТСП передаёт для инициации (маска телефона/идентификатор ТСП); согласовать с ИБ/152-ФЗ.
3. **Схема лимитов согласия** — какие размерности (макс. за списание, период, итог, срок) реально поддерживает НСПК и какие шлюз обязан зеркалировать.
4. **Пороги антифрод/AML для рекуррентных списаний** (115-ФЗ) — повышенный риск «тихих» списаний.
5. **Политика возвратов для рекуррентных списаний** — распространяется ли существующая сага возврата (предполагается «да»), окна возврата.
6. **Приоритет против deferred** — рекуррентные списания тянут roadmap вперёд; подтвердить приоритет относительно C2C/выплат.
7. **Тарифы/комиссии** — не архитектурно, но влияет на отчётность (уже в открытых вопросах solutioning).
```

Good. Now let me think about the actual contract changes in detail.

### docs/contracts/tsp-api.md additions

Add to §3 methods:
- 3.6 Создание согласия (подписка) — `POST /v1/consents`
- 3.7 Запрос статуса согласия — `GET /v1/consents/{consentId}`
- 3.8 Отзыв согласия — `POST /v1/consents/{consentId}/revoke`
- 3.9 Списание по согласию — `POST /v1/consents/{consentId}/payments`

Add to §5 webhooks:
- consent.activated, consent.revoked, consent.expired, consent.rejected

Add error codes: CONSENT_NOT_FOUND, CONSENT_NOT_ACTIVE, AMOUNT_EXCEEDS_CONSENT_LIMIT, CONSENT_ALREADY_REVOKED.

Add note in §3.2/3.3 about paymentType/consentId optional fields.

Actually, I need to be careful with §3.3 payment status response — add optional `paymentType` and `consentId`.

Let me write the edits precisely. I'll use the edit tool to insert new content into the existing files at the right places.

For tsp-api.md, I'll:
1. Add new methods after §3.5.
2. Add new webhook events in §5.
3. Add new error codes in §4.

For opkc-adapter.md:
1. Add new sync methods to §3 table.
2. Add new events to §4 table.
3. Add note in §7/§8 about consent.

For nfr.md:
1. Add new section at the end.

For openapi/tsp-api.yaml:
1. Add new paths and schemas.

For ARCHITECTURE-SPINE.md:
1. Add AD-009 invariant.
2. Optionally note in "Контракты и версии".

For solutioning.md:
1. Update §1 roadmap line.
2. Add ADR-008 to §5 table (optional but good).
3. Maybe add a brief note in §3 about consent FSM.

For README.md:
1. Update structure and status.

For vendor-rfp.md:
1. Add consent methods to scope + POC scenarios (concise).

Let me now think about whether I should do ALL of these edits or keep it focused. The user asked for a complete package. I'll do the core ones and keep vendor-rfp minimal (a short addendum). Actually, vendor-rfp is important because the vendor must support consent methods — G4 "полный набор методов/событий контракта opkc-adapter" already covers it implicitly since opkc-adapter.md now includes consent. So I could add a one-line note. I'll add a brief note to vendor-rfp §1 scope and §5 POC.

Let me now actually write all files. I'll start with the new files (write_file), then edits.

Let me be efficient. I'll write the three new files first, then do edits.

Actually, given the volume, let me proceed methodically. I'll write:

1. `docs/adr/ADR-008-...md` (write_file)
2. `docs/spec/subscription-state-machine.md` (write_file)
3. `docs/change-podpiski-sbp.md` (write_file)
4. Edit `ARCHITECTURE-SPINE.md` (add AD-009)
5. Edit `docs/nfr.md` (add section)
6. Edit `docs/contracts/tsp-api.md` (add methods/webhooks/errors)
7. Edit `docs/contracts/opkc-adapter.md` (add methods/events)
8. Edit `openapi/tsp-api.yaml` (add paths/schemas)
9. Edit `docs/solutioning.md` (roadmap + ADR mapping)
10. Edit `docs/rfp/vendor-rfp.md` (scope + POC note)
11. Edit `README.md` (structure + status)

Let me write these now. I'll do write_file calls in parallel for the 3 new files first, then edits.

Actually, I need to read the exact current content of files before editing (I have most from earlier reads). I have full content of: ARCHITECTURE-SPINE.md, README.md, nfr.md, tsp-api.md, state-machine.md, opkc-adapter.md, tsp-api.yaml, solutioning.md, vendor-rfp.md, all ADRs. So I can edit precisely.

Let me write the 3 new files first.

For the ADR-008, let me finalize. Note: CONSTRAINTS rule `adr-no-placeholders` forbids `<!--` in docs/adr/*.md. My ADR won't have HTML comments. Good. Also I should avoid "TBD/TODO/XXX" (that's only checked in spine, but good practice).

Let me write.

Actually, let me reconsider the date. Today is 2026-09-28 per system. The existing ADRs use 2026-08-15. I'll use 2026-09-28 for new docs.

Let me write the files now.

For the spine AD-009 addition, let me draft:

```markdown
## AD-009. Рекуррентные C2B-списания по согласию плательщика (подписки СБП)

- Status: Proposed (ADR-008)
- **Binds**: БД шлюза (согласие), статусные машины согласия и списания, адаптер ОПКЦ (методы согласия/списания), антифрод/AML.
- **Prevents**: списание без активного согласия; зачисление по неподтверждённому списанию; хранение избыточных ПДн плательщика; двойное списание при ретрае.
- **Rule**: Рекуррентное списание выполняется только по согласию в состоянии `ACTIVE`; зачисление на счёт ТСП — только из `PAID` (подтверждённое НСПК списание, AD-005); идемпотентность распространяется на согласие/списание/отзыв (AD-003); авторитет лимитов согласия — НСПК/банк плательщика, шлюз хранит копию и выполняет sanity-check + антифрод (AD-007).
```

That fits the spine style. Good.

Now let me write everything. I'll do it in batches to be efficient but careful.

Let me write the 3 new files in one batch (3 parallel write_file calls).

Then the edits in subsequent batches (they're independent, so I can parallelize edits too, but edits to the same file must be sequential; different files can be parallel).

Let me start writing.

Actually, I need to carefully craft each file's full content. Let me write them out fully now.

I'll begin with the three new files in parallel.

For the tsp-api.md edits, I need to know exactly where to insert. From my earlier read:

§3 ends with §3.5 "Статус возврата". Then §4 "Ошибки". Then §5 "Вебхуки". Then §6 "Версионирование". Then §7 "Открытые вопросы".

I'll insert new methods §3.6–3.9 right before "## 4. Ошибки".

For §4 error codes, I'll add new codes to the canonical list sentence.

For §5 webhooks, I'll add new events to the "События:" list.

Let me write precise edits.

For opkc-adapter.md:
§3 table ends with `getReconciliationReport`. I'll add rows `createConsent`, `getConsentStatus`, `revokeConsent`, `createRecurringPayment` (or `submitRecurringPayment`). Let me name consistently with existing: `createPaymentLink` → for recurring: `createRecurringPayment`. And `getPaymentStatus` → reuse for recurring? The recurring payment status query can reuse `getPaymentStatus` by qrId... but recurring payments have no qrId. Hmm. Actually the recurring payment also gets a reference in OPKC. Let me use `consentOpcRef` and a `paymentOpcRef`/`debitRef`. For status query, I'll add `getRecurringPaymentStatus` or generalize `getPaymentStatus` to accept `reference`/`opcRef`. To keep additive and minimal, I'll add:
- `createConsent(reference=consentId, tspId, payerRef, limits) → consentOpcRef, consentUrl, ACCEPTED`
- `getConsentStatus(consentOpcRef) → status`
- `revokeConsent(reference=consentId, consentOpcRef, reason) → ACCEPTED`
- `createRecurringPayment(reference=paymentId, consentOpcRef, amount, purpose?) → ACCEPTED`

And for status of recurring payment, reuse `getPaymentStatus` — but it takes `qrId`. I'll note that the adapter normalizes: for recurring, the reference is `paymentOpcRef` (debit id in OPKC), and `getPaymentStatus` accepts either `qrId` or `paymentOpcRef`. Actually simpler: add a note that `getPaymentStatus`/`getReconciliationReport` cover both QR and recurring payments, with the adapter mapping `paymentId` to the OPKC operation id.

Events to add to §4:
- `consent.activated` — `reference` (= consentId), `consentOpcRef`, `limits`, `activatedAt`
- `consent.rejected` — `reference`, reasonCode, reasonText
- `consent.revoked` — `reference`, `consentOpcRef`, `reason` (payer/tsp), `revokedAt`
- `consent.expired` — `reference`, `consentOpcRef`, `expiredAt`

And `payment.paid`/`payment.rejected` now also apply to recurring payments (note).

I'll add a note that existing `payment.paid`/`payment.rejected` events carry a `paymentType` or the correlation distinguishes recurring via `consentOpcRef` presence.

Let me write the opkc-adapter edits.

OK, this is a lot. Let me just write it all carefully.

Let me begin with the three new files.

I'll write them now.

Actually, one more consideration on the OpenAPI. The current yaml is minimal. I'll add:
- paths:
  - `/v1/consents` (post)
  - `/v1/consents/{consentId}` (get)
  - `/v1/consents/{consentId}/revoke` (post)
  - `/v1/consents/{consentId}/payments` (post)
- components/schemas:
  - `ConsentRequest`
  - `Consent`
  - extend `Payment` with optional `consentId` and `paymentType`.

And add `Idempotency-Key` header to the new POST endpoints.

I need to keep it valid OpenAPI 3.0.3 and consistent with the existing style (which uses inline `{...}` and `$ref`).

Let me write the full new yaml carefully. Actually, I'll edit the existing yaml: add new paths after the existing `/v1/payments/{paymentId}` path, and add new schemas + extend Payment.

Let me draft the yaml additions.

For the `Consent` schema:
```yaml
    ConsentRequest:
      type: object
      required: [tspId, merchantOrderId]
      properties:
        tspId: {type: string}
        merchantOrderId: {type: string}
        payerRef: {type: string, description: Минимальный идентификатор плательщика (маска/токен); состав — по ИБ/152-ФЗ [ТРЕБУЕТ ПРОВЕРКИ]}
        maxAmountPerDebit: {type: integer, description: Макс. сумма одного списания, копейки (копия лимита НСПК)}
        validitySeconds: {type: integer, description: Срок действия согласия, сек}
        redirectUrl: {type: string}
    Consent:
      type: object
      required: [consentId, status]
      properties:
        consentId: {type: string}
        status: {type: string, enum: [CREATED, LINK_ISSUED, ACTIVE, REVOKED, EXPIRED, REJECTED]}
        consentUrl: {type: string, description: Ссылка для подтверждения плательщиком (при LINK_ISSUED)}
        maxAmountPerDebit: {type: integer}
        expiresAt: {type: string, format: date-time}
        merchantOrderId: {type: string}
```

And extend Payment:
```yaml
    Payment:
      type: object
      required: [paymentId, amount, status]
      properties:
        paymentId: {type: string}
        amount: {type: integer, description: Сумма в копейках}
        status:
          type: string
          enum: [CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED]
        paymentType: {type: string, enum: [QR, RECURRING], description: Вид платежа; по умолчанию QR}
        consentId: {type: string, description: Идентификатор согласия для рекуррентных списаний}
```

Wait — but the enum for Payment.status currently includes QR_ISSUED and EXPIRED. For recurring payments, QR_ISSUED and EXPIRED don't apply, but keeping them in the enum is fine (the status just won't be used for recurring). However, I added SUBMITTED as a state for recurring in the FSM. Should SUBMITTED appear in the API enum? In the payment FSM, SUBMITTED is a technical-ish state. In the tsp-api §3.3 status enum, there's no SUBMITTED currently. For consistency, I'll keep the API status enum as the financial states (no SUBMITTED), and treat SUBMITTED as a technical sub-state (like ABS_PENDING), reflected via creditingStatus-style. Actually, in my FSM I marked SUBMITTED as "виден ТСП (технич.)". To keep the API clean and backward-compatible, I'll make SUBMITTED internal (not in the TSP API enum), and map it: while SUBMITTED, the TSP sees status `CREATED` (awaiting result). Let me adjust: I'll note in the FSM that `SUBMITTED` is a technical sub-state not exposed; TSP sees `CREATED` until PAID/FAILED.

Actually, simpler and cleaner: make `SUBMITTED` a technical state (not exposed to TSP), like `ABS_PENDING`. So in the FSM doc I'll mark SUBMITTED as technical. Let me update the FSM doc: SUBMITTED → technical (не виден ТСП). TSP sees CREATED until PAID/FAILED.

Hmm, but then the payment status query during SUBMITTED would show CREATED. That's acceptable (mirrors how ABS_PENDING shows PAID + creditingStatus). I'll add a note.

Let me finalize: recurring debit financial states exposed to TSP: CREATED, PAID, CREDITED, COMPLETED, FAILED, REFUNDED. SUBMITTED is technical. So the API enum stays unchanged (already includes these). Good — no change to the enum needed, just add paymentType/consentId.

So the OpenAPI `Payment.status` enum stays the same (already has all needed values). I'll just add `paymentType` and `consentId` optional fields. And add consent paths + schemas.

Let me also add a `RecurringPaymentRequest`? The debit request = amount + merchantOrderId (+ optional paymentPurpose). I can reuse `PaymentRequest` (which has amount + merchantOrderId). But PaymentRequest currently is used for QR payment with fields amount+merchantOrderId. For recurring debit, amount is required, merchantOrderId required. So I can reuse PaymentRequest for the debit body. I'll just reference `PaymentRequest` in the debit path. Good — no new request schema needed. I might add optional `paymentPurpose` to PaymentRequest (additive) for parity with tsp-api.md. I'll add it as optional.

Let me finalize the OpenAPI edits.

Now let me write everything. I'll produce the three new files first.

Let me carefully write full content for each. Given length, I'll be thorough but avoid bloat.

I'll now write the files.
All four load-bearing decisions are confirmed (consent through НСПК, pull model, MVP = consent + debit, limits authoritative at НСПК). Now I'll build the architectural package following the repo's conventions: new ADR, new state-machine spec, a change-package doc, plus additive edits to contracts/NFR/spine.

Let me create the three new documents first.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now let me make the edits to existing files. Let me start with the spine (ARCHITECTURE-SPINE.md) — add AD-009 after AD-008, before the Deferred section.

The spine currently ends AD-008 with the Rule, then a blank line, then `---`, then `## Deferred`.

I'll insert AD-009 before the `---` separator. Let me find the exact text.

From my read, the AD-008 section ends:
```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll insert AD-009 between the AD-008 Rule and the `---`.

Let me craft the edit.
Now the additive edits. First, the spine — add the new invariant AD-009 (Proposed), following the existing invariant format.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/nfr.md", old_string="| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |\n\n## Зависимости (внешние входы для NFR)", new_string="| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |\n\n## 8. Рекуррентные списания (подписки СБП)\n\nЦелевые значения —)`

Good. Now let me edit nfr.md to add the recurring NFR section. I'll append a new section after section 7 and before the "Зависимости" section (or at the end). Let me look at nfr.md structure again: it ends with section "## 7. Наблюдаемость" table, then "## Зависимости (внешние входы для NFR)".

I'll insert a new "## 8. Рекуррентные списания (подписки СБП)" section before "## Зависимости".

Actually the existing sections are numbered 1-7, then "## Зависимости". I'll insert "## 8. Рекуррентные списания (подписки СБП)" after section 7's table and before "## Зависимости".

Let me find the exact text. Section 7 ends with:
```
| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |

## Зависимости (внешние входы для NFR)
```

I'll insert between them.
Now the measurable NFRs for the new functionality — append a section to `docs/nfr.md`.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/nfr.md", old_string="| Список по неактивному/отозванному согласию | блокируется в 100 % случаев (`CONSENT_NOT_ACTIVE`) | Fitness-тест guard'а |", new_string="| Списание по неактивному/отозванному согласию | блокируется в 100 % случаев (`CONSENT_NOT_ACTIVE`) | Fitness-тест guard'а |")`

I notice a typo I introduced: "Список по неактивному/отозванному согласию" should be "Списание по неактивному/отозванному согласию". Let me fix that.
I introduced a typo ("Список" → "Списание"). Fixing it.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/contracts/tsp-api.md", old_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n, new_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n)`

Now edit docs/contracts/tsp-api.md to add new methods, webhook events, and error codes.

I need to:
1. Add new methods §3.6–3.9 before "## 4. Ошибки".
2. Add new error codes to §4.
3. Add new webhook events to §5.
4. Add optional fields paymentType/consentId to §3.3 payment status response.

Let me do these edits. First, add methods before "## 4. Ошибки".

The current text before §4:
```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`

## 4. Ошибки (RFC 9457, Problem Details)
```

I'll insert §3.6–3.9 between §3.5 and §4.

Let me write the new methods content.

For §3.6 consent creation:
```
### 3.6 Создание согласия (подписка СБП)

`POST /v1/consents`

Запрос (Idempotency-Key обязателен):
{
  "tspId": "tsp_9f3c2a1b",
  "merchantOrderId": "sub-12345",       // сквозной для ТСП
  "payerRef": "7999****123",             // минимальный идентификатор плательщика; состав — по ИБ/152-ФЗ [ТРЕБУЕТ ПРОВЕРКИ]
  "maxAmountPerDebit": 1490,             // копейки; копия лимита НСПК (авторитет — НСПК/банк плательщика)
  "validitySeconds": 15552000,           // опц.; срок действия (180 сут)
  "redirectUrl": "https://merchant.example.com/sub/12345/return"
}

Ответ 201:
{
  "consentId": "cons_2f8a1c9d",
  "status": "LINK_ISSUED",
  "consentUrl": "https://qr.nspk.ru/…",   // ссылка для подтверждения плательщиком в приложении банка
  "expiresAt": "2026-09-28T18:00:00.000Z"
}
```

Правила: согласие авторитетно регистрируется в НСПК; плательщик подтверждает по `consentUrl`; статус меняется по вебхукам (`consent.activated` и пр.).

### 3.7 Запрос статуса согласия
`GET /v1/consents/{consentId}` → 200:
{
  "consentId": "cons_2f8a1c9d",
  "status": "ACTIVE",   // CREATED | LINK_ISSUED | ACTIVE | REVOKED | EXPIRED | REJECTED
  "maxAmountPerDebit": 1490,
  "activatedAt": "…",
  "revokedAt": null,
  "merchantOrderId": "sub-12345"
}

### 3.8 Отзыв согласия
`POST /v1/consents/{consentId}/revoke` (Idempotency-Key обязателен)
Запрос: { "reason": "…" }  // опц.
Ответ 200: { "consentId": "…", "status": "REVOKED" }
Правила: отзыв возможен из ACTIVE (или LINK_ISSUED); повторный отзыв идемпотентен. После отзыва списания запрещены (CONSENT_NOT_ACTIVE).

### 3.9 Списание по согласию (рекуррентный платёж)
`POST /v1/consents/{consentId}/payments` (Idempotency-Key обязателен)
Запрос:
{
  "amount": 1490,
  "merchantOrderId": "order-67890",
  "paymentPurpose": "Подписка, период 2026-10"
}
Ответ 201: { "paymentId": "pay_…", "status": "CREATED", "paymentType": "RECURRING", "consentId": "cons_2f8a1c9d" }
Правила: согласие должно быть ACTIVE; сумма ≤ maxAmountPerDebit (sanity-check; авторитет — НСПК). Списание без QR/действия плательщика. Статус далее — GET /v1/payments/{paymentId} (paymentType=RECURRING).
```

For §3.3, add paymentType/consentId to the response. The current response example:
```
{
  "paymentId": "pay_8d1e4f5a",
  "status": "COMPLETED",           // CREATED | QR_ISSUED | PAID | CREDITED | COMPLETED | FAILED | EXPIRED | REFUNDED
  "amount": 149990,
  "paidAt": "2026-08-15T17:31:02.000Z",
  "creditingStatus": "CREDITED",   // технический статус зачисления (для ТСП)
  "refunds": [
    { "refundId": "ref_1a2b3c", "amount": 149990, "status": "COMPLETED" }
  ],
  "errorCode": null,               // код отклонения НСПК, если статус FAILED
  "merchantOrderId": "order-12345"
}
```

I'll add two optional fields: `paymentType` and `consentId`. Insert after "amount" or after "merchantOrderId". Let me add after "status" line or at the end. I'll add:
```
  "paymentType": "QR",             // QR | RECURRING (опц.; по умолчанию QR)
  "consentId": null,               // для рекуррентных списаний (опц.)
```

Let me insert these right after "status" line.

For §4 error codes, current:
```
Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.
```

Add new codes: `CONSENT_NOT_FOUND` (404), `CONSENT_NOT_ACTIVE` (422), `AMOUNT_EXCEEDS_CONSENT_LIMIT` (422), `CONSENT_ALREADY_REVOKED` (409).

For §5 webhooks, current events:
```
События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
```

Add consent events:
```
- `consent.activated` — согласие подтверждено плательщиком и активно
- `consent.revoked` — согласие отозвано (плательщиком или ТСП)
- `consent.expired` — согласие истекло/не подтверждено за TTL
- `consent.rejected` — НСПК отклонил или плательщик отказался
```

And add a note that `payment.completed`/`payment.failed` also fire for recurring debits (with `paymentType=RECURRING`, `consentId` in body).

Let me do these edits. I'll do them as separate edit calls (different parts of the same file). Actually I can do multiple edits to the same file, but each edit needs unique old_string. I'll do them sequentially to be safe, or in parallel since they target different unique strings. Parallel edits to the same file might conflict if the tool re-reads. I'll do them sequentially to be safe, but actually the edit tool works on exact string replacement and each targets distinct text; parallel could be risky if the file is modified between. I'll do them one at a time in sequence within a single message? No — I should do them as separate sequential tool calls. Let me do them in sequence (multiple edit calls in separate turns is slow). Actually I can put multiple edit calls in ONE message only if they're independent — but they edit the same file, which the tool processes... The guidance says "run dependent calls sequentially". Edits to the same file should be sequential to avoid conflicts.

Let me do them sequentially: first the §3.6-3.9 insertion, then §3.3 fields, then §4 codes, then §5 events. I'll issue them one after another. Actually, I can issue multiple edits in parallel only across DIFFERENT files. For same file, sequential.

Let me just do them sequentially in separate tool calls. To be efficient, I'll do one edit per message but I can chain by doing multiple calls. Actually, I'll do them in a few messages. Let me start.

Actually, I realize I can do all tsp-api.md edits with careful unique old_strings. Since the edit tool replaces exact strings, and these are in different locations with unique context, I could issue them as separate tool calls in a single message — but the instruction says parallel edits to the same file risk conflicts. The safest is sequential. However, the tool likely applies them sequentially even in one message. To avoid risk, I'll do them one at a time.

Let me proceed with the first edit: insert §3.6-3.9.
Now the TSP API contract (`docs/contracts/tsp-api.md`). First, add the four new consent/recurring methods.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/contracts/tsp-api.md", new_string="{\n  \"paymentId\": \"pay_8d1e4f5a\",\n  \"status\": \"COMPLETED\",           // CREATED | QR_ISSUED | PAID | CREDITED | COMPLETED | FAILED, old_string="{\n  \"paymentId\": \"pay_8d1e4f5a\",\n  \"status\": \"COMPLETED\",           // CREATED | QR_ISSUED | PAID | CREDITED | COMPLETED | FAILED)`

Now add the new error codes and the paymentType/consentId fields to §3.3, and the webhook events to §5.

Let me edit §3.3 response to add paymentType and consentId.
Now add the optional `paymentType`/`consentId` fields to the payment status response (§3.3).

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/contracts/tsp-api.md", new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `CONSENT_NOT_FOUND` (404), `ID, old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`

Now add the new error codes to §4.

The current error codes line:
```
Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.
```

Add: `CONSENT_NOT_FOUND` (404), `CONSENT_NOT_ACTIVE` (422), `AMOUNT_EXCEEDS_CONSENT_LIMIT` (422), `CONSENT_ALREADY_REVOKED` (409).

I'll insert them logically.
Now add the new error codes to §4.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/contracts/tsp-api.md", new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`

Now add the consent webhook events to §5. The current events list:
```
События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
```

I'll add consent events after this list. And add a note that payment.completed/failed fire for recurring too.
Now add the consent webhook events to §5.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/contracts/opkc-adapter.md", new_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t, old_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t)`

Now edit the opkc-adapter.md contract to add consent/recurring methods and events.

I need to:
1. Add methods to §3 table (after `getReconciliationReport`).
2. Add events to §4 table (after `transport.unavailable`).
3. Maybe add a note about the recurring payment using payment.paid/rejected events.

Let me add the sync methods to §3. The current §3 table ends with:
```
| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |
```

I'll add rows after it:
```
| `createConsent` | создание согласия/подписки (ссылка для подтверждения) | `reference` (= `consentId` ядра), `tspId`, `payerRef` (мин. ПДн), `limits` (maxAmountPerDebit, validity) | `consentOpcRef`, `consentUrl`, `ACCEPTED` (результат — событием) | 5 c |
| `getConsentStatus` | статус согласия | `consentOpcRef` | `ACTIVE` / `PENDING` / `REJECTED` / `REVOKED` / `EXPIRED` / `UNKNOWN` | 3 c |
| `revokeConsent` | отзыв согласия | `consentOpcRef`, `reason`, `reference` | `ACCEPTED` (результат — событием) | 5 c |
| `createRecurringPayment` | списание по согласию | `reference` (= `paymentId` ядра), `consentOpcRef`, `amount`, `purpose?` | `ACCEPTED` (результат — событием) | 5 c |
```

For §4 events, after `transport.unavailable`:
```
| `consent.activated` | согласие подтверждено плательщиком | `reference` (= `consentId`), `consentOpcRef`, `limits`, `activatedAt` |
| `consent.rejected` | согласие отклонено/отказ | `reference`, `reasonCode`, `reasonText` |
| `consent.revoked` | согласие отозвано | `reference`, `consentOpcRef`, `reason` (`payer`/`tsp`), `revokedAt` |
| `consent.expired` | согласие истекло | `reference`, `consentOpcRef`, `expiredAt` |
```

And add a note that `payment.paid`/`payment.rejected` apply to both QR payments and recurring debits (correlation via `reference` = `paymentId`; recurring distinguished by presence of `consentOpcRef`/paymentType). I'll add a note in §4 after the events table or in the "Гарантии" paragraph.

Actually, let me add a short note after the events table about recurring. And update §3's `getPaymentStatus` to note it covers both QR and recurring payments.

Let me also update §3 note about `getPaymentStatus`/`getReconciliationReport` covering recurring. I'll add a line in §3.

Let me do the edits.

First, §3 table — add the four new methods after getReconciliationReport row.

The exact text of the last row:
```
| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |
```

And after it:
```
Статусные модели ОПКЦ (`PAID`, `REJECTED`, `EXPIRED`, `CONFIRMED`) — **нормализованные адаптером** из протокола НСПК; ядро не зависит от конкретных значений НСПК.
```

I'll insert the new rows between the last row and the "Статусные модели" paragraph.

Let me craft the edit.
Now the internal OPKC adapter contract (`docs/contracts/opkc-adapter.md`) — add the consent/recurring methods and events.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/contracts/opkc-adapter.md", new_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |\n| `consent.activated` | , old_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |")`

Now add the consent events to §4 table. The current §4 events table ends with:
```
| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |
```

I'll add consent events after it, before the "Гарантии" paragraph.
Now add the consent events to the adapter's async event table.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/openapi/tsp-api.yaml", new_string="  /v1/payments/{paymentId}:\n    get:\n      operationId: getPayment\n      parameters:\n        - {in: path, name: paymentId, required: tr, old_string="  /v1/payments/{paymentId}:\n    get:\n      operationId: getPayment\n      parameters:\n        - {in: path, name: paymentId, required: tr)`

Now edit the OpenAPI yaml. I need to add:
1. New paths: `/v1/consents` (post), `/v1/consents/{consentId}` (get), `/v1/consents/{consentId}/revoke` (post), `/v1/consents/{consentId}/payments` (post).
2. New schemas: `ConsentRequest`, `Consent`.
3. Extend `Payment` with optional `paymentType` and `consentId`.

Let me read the current yaml again to be precise. I have it from earlier:

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

I'll rewrite the whole file with the additions. Actually, rewriting the whole file via write_file is cleaner than multiple edits for yaml. But I must be careful to preserve the existing content exactly and add new content. Since I have the full current content, I'll use write_file to rewrite with additions. But wait — write_file requires "prior-read enforcement" — I already read it. And the user could have modified it? Unlikely. But to be safe, I'll use edit tool to make targeted additions instead, since the file is small and I know the exact content.

Actually, using edit with a large old_string covering the whole `paths` → end is cleaner. Let me do targeted edits:

Edit 1: Add new paths after `/v1/payments/{paymentId}` path, before `components:`.

Edit 2: Add `ConsentRequest` and `Consent` schemas, and extend `Payment` schema.

Let me do edit 1: insert new paths. The old_string is:
```
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
```

new_string adds the consent paths before `components:`.

Let me write the new paths in YAML. I'll use consistent style with the existing (2-space indentation, inline objects with `{...}`).

New paths:

```yaml
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
          description: Согласие создано, ссылка выдана
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
  /v1/consents/{consentId}/revoke:
    post:
      operationId: revokeConsent
      parameters:
        - {in: path, name: consentId, required: true, schema: {type: string}}
        - in: header
          name: Idempotency-Key
          required: true
          schema: {type: string}
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                reason: {type: string}
      responses:
        '200':
          description: Согласие отозвано
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Consent'}
  /v1/consents/{consentId}/payments:
    post:
      operationId: createRecurringPayment
      parameters:
        - {in: path, name: consentId, required: true, schema: {type: string}}
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
          description: Списание инициировано
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Payment'}
```

Note: The `PaymentRequest` for the recurring debit uses amount + merchantOrderId, which is fine. But I might want to add optional `paymentPurpose` to PaymentRequest. Actually, I'll add `paymentPurpose` as optional to PaymentRequest (additive, backward-compatible) for parity. Let me add it in the schema edit.

Now schemas. Add ConsentRequest and Consent, and extend Payment.

ConsentRequest:
```yaml
    ConsentRequest:
      type: object
      required: [tspId, merchantOrderId]
      properties:
        tspId: {type: string}
        merchantOrderId: {type: string}
        payerRef: {type: string, description: Минимальный идентификатор плательщика; состав — по ИБ/152-ФЗ}
        maxAmountPerDebit: {type: integer, description: Макс. сумма одного списания, копейки}
        validitySeconds: {type: integer, description: Срок действия согласия, сек}
        redirectUrl: {type: string}
    Consent:
      type: object
      required: [consentId, status]
      properties:
        consentId: {type: string}
        status:
          type: string
          enum: [CREATED, LINK_ISSUED, ACTIVE, REVOKED, EXPIRED, REJECTED]
        consentUrl: {type: string, description: Ссылка для подтверждения плательщиком}
        maxAmountPerDebit: {type: integer}
        expiresAt: {type: string, format: date-time}
        activatedAt: {type: string, format: date-time}
        revokedAt: {type: string, format: date-time}
        merchantOrderId: {type: string}
```

Extend Payment with paymentType and consentId, and add paymentPurpose to PaymentRequest.

Let me do the edits. I'll do two edits: one for paths, one for schemas.

Actually, I can do the paths edit and schemas edit as two separate edit calls (sequential, same file).

Let me write the paths edit first.
Now the machine-readable contract — extend `openapi/tsp-api.yaml` additively (new consent paths first).

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/openapi/tsp-api.yaml", new_string="components:\n  schemas:\n    PaymentRequest:\n      type: object\n      required: [amount, merchantOrderId]\n      properties:\n        amo, old_string="components:\n  schemas:\n    PaymentRequest:\n      type: object\n      required: [amount, merchantOrderId]\n      properties:\n        amo)`

Now add the ConsentRequest and Consent schemas, extend Payment with paymentType/consentId, and add paymentPurpose to PaymentRequest.

Current schemas section:
```yaml
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

I'll replace the whole schemas block with the extended version.

New schemas:
```yaml
components:
  schemas:
    PaymentRequest:
      type: object
      required: [amount, merchantOrderId]
      properties:
        amount: {type: integer, description: Сумма в копейках}
        merchantOrderId: {type: string}
        paymentPurpose: {type: string, description: Назначение платежа (опц.)}
    Payment:
      type: object
      required: [paymentId, amount, status]
      properties:
        paymentId: {type: string}
        amount: {type: integer, description: Сумма в копейках}
        status:
          type: string
          enum: [CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED]
        paymentType: {type: string, enum: [QR, RECURRING], description: Вид платежа (опц.; по умолчанию QR)}
        consentId: {type: string, description: Идентификатор согласия для рекуррентных списаний (опц.)}
    ConsentRequest:
      type: object
      required: [tspId, merchantOrderId]
      properties:
        tspId: {type: string}
        merchantOrderId: {type: string}
        payerRef: {type: string, description: Минимальный идентификатор плательщика; состав — по ИБ/152-ФЗ}
        maxAmountPerDebit: {type: integer, description: Макс. сумма одного списания, копейки}
        validitySeconds: {type: integer, description: Срок действия согласия, сек}
        redirectUrl: {type: string}
    Consent:
      type: object
      required: [consentId, status]
      properties:
        consentId: {type: string}
        status:
          type: string
          enum: [CREATED, LINK_ISSUED, ACTIVE, REVOKED, EXPIRED, REJECTED]
        consentUrl: {type: string, description: Ссылка для подтверждения плательщиком}
        maxAmountPerDebit: {type: integer}
        expiresAt: {type: string, format: date-time}
        activatedAt: {type: string, format: date-time}
        revokedAt: {type: string, format: date-time}
        merchantOrderId: {type: string}
```

Let me do the edit replacing the schemas block.
Now add the consent schemas and extend `Payment`/`PaymentRequest` additively.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/solutioning.md", new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop, old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop)`

Now update `docs/solutioning.md`:
1. §1 roadmap line — change "автоплатежи" from out-of-scope.
2. §5 ADR mapping table — add ADR-008 row.
3. §3 status model — maybe add a note about consent/recurring. Optional.

Let me update §1 first. The current text:
```
Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи.
```

Change to:
```
Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты. Рекуррентные C2B-списания по согласию плательщика (подписки СБП, бывш. «автоплатежи») выведены в scope — см. ADR-008.
```

Let me do this edit.

Then §5 ADR table — add row. Current table:
```
| Решение | ADR | Spine |
|---|---|---|
| Топология: выделенный компонент + outbox | ADR-001 | AD-001, AD-002 |
| Статусная машина + идемпотентность | ADR-002 | AD-002, AD-003 |
| Транспорт к ОПКЦ: изолированный адаптер, mTLS/ГОСТ, СКЗИ | ADR-003 | AD-004 |
| Нотификации: at-least-once, дедуп, DLQ, сверка | ADR-004 | AD-003 |
| АБС: зачисление из PAID, возвраты-сага | ADR-005 | AD-005 |
| НПС/КИИ/ПДн: trust-зоны, ГОСТ | ADR-006 | AD-006, AD-007 |
| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accepted) | AD-008 [ADOPTED] |
```

Add:
```
| Рекуррентные C2B-списания по согласию (подписки СБП) — Proposed | ADR-008 | AD-009 (Proposed) |
```

I'll add this row after ADR-007 row.

Also §3 status model — I could add a short note referencing the consent FSM. But to keep minimal, I'll add a one-line note in §3 after the existing status model. Actually, I'll add a brief note. Let me check §3:

```
## 3. Статусная модель платежа

```
CREATED ──► QR_ISSUED ──► PAID ──► CREDITED ──► COMPLETED
...
```

- `PAID` — подтверждённый НСПК статус; **только из него** разрешено зачисление (AD-005).
- Переходы — атомарные транзакции «статус + outbox + аудит» (AD-002).
- Повторные нотификации идемпотентны (AD-003).
```

I'll add a line: "Рекуррентные списания (подписки СБП) — отдельная статусная машина согласия и списания (ADR-008, `docs/spec/subscription-state-machine.md`): `CREATED → SUBMITTED → PAID → CREDITED → COMPLETED`, без `QR_ISSUED`."

Let me do these three edits sequentially (same file). Actually I'll do them one at a time.

Edit 1: §1 roadmap.
Edit 2: §3 note.
Edit 3: §5 table row.

Let me do edit 1.
Now update `docs/solutioning.md` — reflect the scope change (roadmap line), the state-model note, and the ADR mapping.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/solutioning.md", new_string="- `PAID` — подтверждённый НСПК статус; **только из него** разрешено зачисление (AD-005).\n- Переходы — атомарные транзакции «статус + outbo, old_string="- `PAID` — подтверждённый НСПК статус; **только из него** разрешено зачисление (AD-005).\n- Переходы — атомарные транзакции «статус + outbo)`

Now add the §3 note and §5 table row.

§3 note — I'll add after "Повторные нотификации идемпотентны (AD-003)." line.

The exact text:
```
- `PAID` — подтверждённый НСПК статус; **только из него** разрешено зачисление (AD-005).
- Переходы — атомарные транзакции «статус + outbox + аудит» (AD-002).
- Повторные нотификации идемпотентны (AD-003).
```

I'll add a new bullet after the last one.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/solutioning.md", new_string="| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accepted) | AD-008 [ADOPTED] |\n| Рекуррентные C2B-списания по согла, old_string="| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accepted) | AD-008 [ADOPTED] |")`

Now add the ADR-008 row to §5 table.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/rfp/vendor-rfp.md", new_string="6. Поддержку и SLA.\n\n**Не входит в scope вендора:** ядро шлюза (API ТСП, статусная машина, сверка, АБС-интеграция) — собственная разработ, old_string="6. Поддержку и SLA.\n\n**Не входит в scope вендора:** ядро шлюза (API ТСП, статусная машина, сверка, АБС-интеграция) — собственная разработ)`

Now update vendor-rfp.md to note the consent methods are part of the adapter scope, and add a POC scenario. This is a concise addendum. And update README.md.

Let me do vendor-rfp.md: add a note to §1 scope (что покупаем) and §5 POC scenarios.

Actually, the opkc-adapter.md already includes consent methods, and vendor-rfp §1 references "контракт `docs/contracts/opkc-adapter.md`" and §4 "Методы (§3)" lists them. Since I added consent methods to opkc-adapter.md §3, the vendor-rfp already implicitly covers them via the reference. But to be explicit and complete, I'll add a short line to §1 scope and a POC scenario P9 for consent.

Let me add to §1 scope list (after item 1 or in the list). The scope list is:
```
**Транспортный адаптер ОПКЦ СБП** — сертифицированный компонент, реализующий внутренний контракт `docs/contracts/opkc-adapter.md` поверх протокола участника НСПК, включая:

1. Транспорт к ОПКЦ СБП ...
...
6. Поддержку и SLA.
```

I'll add a note after item 6 or add item about consent. Actually item 2 "Нормализацию статусов/ошибок НСПК в канонический контракт." I can add a clarifying sentence. Simplest: add a sentence after the numbered list: "С релизом ADR-008 в scope вендора добавляются методы согласия и списания (`createConsent`, `getConsentStatus`, `revokeConsent`, `createRecurringPayment`) и события `consent.*` — см. opkc-adapter §3–4."

And in §5 POC scenarios, add P9:
```
| P9 | Создание/подтверждение согласия + списание по нему | consentUrl выдан; событие `consent.activated`; `createRecurringPayment` → `payment.paid` |
```

And in §4 technical requirements, the "Методы (§3)" line lists methods — I could add consent methods there too. But it's getting verbose. I'll add the §1 note + §5 P9, which is sufficient.

Let me do the vendor-rfp edits.

Actually, let me reconsider whether vendor-rfp edits are in scope. The user's deliverable #4 is "Изменения контрактов (openapi/tsp-api.yaml)". The vendor RFP is a supporting doc. Since the adapter contract (opkc-adapter.md) is the basis for the RFP, and I already updated opkc-adapter.md, the RFP is implicitly updated. But adding an explicit note makes the package complete and signals to the vendor that consent is in scope. It's low-risk and consistent. I'll add a concise note + POC row.

Let me do it.
Now a concise addendum to the vendor RFP (the adapter scope now includes consent/debit methods), then update the README index.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/rfp/vendor-rfp.md", new_string="| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |\n| P9 | Согл, old_string="| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |")`

Now add a POC scenario P9 to vendor-rfp §5. The current §5 table:
```
| P1 | Счастливый путь: createPaymentLink → payment.paid | qrId/qrUrl корректны; событие с `eventId` |
| P2 | **Повтор createPaymentLink с тем же `reference`** | тот же qrId, дубля QR нет (G3) |
| P3 | Нотификация rejected/expired | нормализованные события, reasonCode |
| P4 | Отказ канала к НСПК (остановка симулятора) | circuit breaker → `503 TRANSPORT_UNAVAILABLE` + `transport.unavailable`, восстановление |
| P5 | Потеря/задержка нотификации | сверка через `getPaymentStatus`/`getReconciliationReport` находит операцию |
| P6 | Нагрузка 200 TPS sustained, пик 500 TPS | latency в допусках, потерь 0 |
| P7 | Ротация ключей/сертификатов без остановки | документированная процедура, без сбоев |
| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |
```

Add P9:
```
| P9 | Согласие: createConsent → consent.activated → createRecurringPayment → payment.paid | consentUrl выдан; событие `consent.activated`; повтор `createRecurringPayment` с тем же `reference` — дубля списания нет |
```

Let me add after P8.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/README.md", new_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..008`, `ARCHITEC, old_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITEC)`

Now update README.md to reflect the new files and the change. Current README structure section:

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

I'll update:
- `инварианты AD-001..AD-008` → `инварианты AD-001..AD-009`
- add `spec/subscription-state-machine.md` line
- `adr/ADR-001..007.md` → `adr/ADR-001..008.md`
- add `change-podpiski-sbp.md` line

And update the top status line. Current:
```
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).
```

Add a note about the new ADR-008 (recurring). Actually the status line says "ожидает человеческого решения A3 по стратегии реализации (ADR-007)". ADR-007 is already Accepted (A3 принято). Wait, the README says "ожидает человеческого решения A3 по стратегии реализации (ADR-007)" but ADR-007 is already Accepted. There's a slight inconsistency in the repo (README is stale vs ADR-007 status). I won't fix that unrelated inconsistency, but I'll add a line about the new change.

Actually, let me keep README edits minimal and focused: update the "Ключевые документы" line and the structure block, and add a note about the recurring change.

Let me read the README top section again to be precise.

From earlier read:
```
# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).
```

I'll update the "Ключевые документы" to `ADR-001..008` and add `docs/change-podpiski-sbp.md`, and add a status bullet about the new change. And update the structure block.

Let me do these edits.

Edit 1: the "Ключевые документы" + status lines.

New:
```
- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..008`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).
- Изменение в работе: рекуррентные C2B-списания по согласию плательщика (подписки СБП) — `docs/change-podpiski-sbp.md`, ADR-008 (Proposed), выносится на A3.
```

Edit 2: structure block.

New structure:
```
ARCHITECTURE-SPINE.md        инварианты AD-001..AD-009
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps
  nfr.md                     измеримые NFR (вкл. рекуррентные списания)
  change-podpiski-sbp.md     пакет изменения: подписки СБП (оценка, влияние, приёмка, откат)
  contracts/tsp-api.md       контракт API ТСП v0.1 (мерчант-API; вкл. согласия)
  contracts/opkc-adapter.md  контракт адаптера ОПКЦ v0.1 (ядро ↔ транспорт; вкл. согласия)
  spec/state-machine.md      статусная машина платежа: переходы, инварианты
  spec/subscription-state-machine.md  автоматы согласия и рекуррентного списания
  rfp/vendor-rfp.md          RFP-пакет по вендору транспорта ОПКЦ (критерии, POC, SLA)
  adr/ADR-001..008.md        архитектурные решения
.arch-handoff/               handoff-пакет кодовому харнессу (этап: walking skeleton)
```

Let me do these two edits.

Actually, I also want to make sure I haven't missed the openapi reference in README. The README structure doesn't list openapi/. It's fine; the top has "openapi/tsp-api.yaml" in the folder structure. I'll leave openapi out of the structure block (it wasn't there), but the change is in openapi. Actually the README structure block doesn't mention openapi/ at all — it's a bit incomplete already. I won't add it (avoid scope creep), but I could add it. Hmm, minor. I'll leave the structure block as-is regarding openapi, but I'll note in my final summary that openapi was changed.

Let me do the README edits.
Finally, update the README index to reflect the new invariant, new ADR, and new documents.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/README.md", new_string="ARCHITECTURE-SPINE.md        инварианты AD-001..AD-009\ndocs/\n  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps\, old_string="ARCHITECTURE-SPINE.md        инварианты AD-001..AD-008\ndocs/\n  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps\)`

Now update the structure block in README.

  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r2/ws/openapi/tsp-api.yaml")`

Now let me verify the changes. Let me check:
1. The OpenAPI yaml is valid (I should validate it).
2. The CONSTRAINTS.yaml fitness rules still pass: `adr-no-placeholders` (no `<!--` in docs/adr/*.md), `spine-lints-clean` (no TODO/TBD/XXX in spine), `nfr-measurable` (99,95 in nfr.md), `abs-credit-only-from-paid` (ADR-005 unchanged).

Let me verify:
- ADR-008 has no `<!--` — correct, I didn't add any.
- Spine AD-009 has no TODO/TBD/XXX — correct.
- nfr.md still has "99,95" — yes, in section 1 availability. And my new section doesn't remove it.

Let me validate the OpenAPI YAML syntax. I can run a quick check. Is there a tool? I could run a Python yaml parse or a shell command. Let me check if there's a way. Actually, I should verify the yaml is well-formed. Let me use a quick Python check if python is available, or just re-read the file to eyeball it.

Actually, I should verify the full yaml file is correct. Let me re-read it fully.

Also, I should run the repo's fitness checks if there's a command. The CONSTRAINTS.yaml mentions `arch control check`. But that's a custom tool that may not be runnable here. The repo is docs-only (no code), so there's no build/test. The verification here is: (a) YAML validity, (b) fitness rule invariants.

Let me re-read the final openapi yaml to confirm it's well-formed, and maybe run a python yaml validation.

Let me read the full yaml file.
Let me verify the final OpenAPI file is well-formed and re-read it end-to-end.

  `run_shell_command(command="cd <HARNESS>/runs/cells/superpowers-r2/ws && python3 -c \"import yaml; yaml.s, description="Validate OpenAPI YAML syntax")`
  `grep_search(pattern="<!--|TODO|TBD|XXX", path="<HARNESS>/runs/cells/superpowers-r2/ws/docs/adr/ADR-008-rekurrentnye-c2b-spis)`
  `grep_search(pattern="TODO|TBD|XXX", path="<HARNESS>/runs/cells/superpowers-r2/ws/ARCHITECTURE-SPINE.md")`

The YAML looks well-formed. Let me validate it with a quick Python yaml parse to be sure (there's no code, but I can use python to validate the yaml syntax). Actually, let me check if python3 is available and validate. This is a reasonable verification step since the user asked for contract changes without breaking consumers.

Let me run a quick yaml validation. I'll use python3 with yaml, or if pyyaml isn't available, use a simpler check. Actually, let me just try python3 -c with yaml.safe_load.

Let me also verify the fitness rules:
1. `docs/adr/ADR-008-...md` must not contain `<!--` (rule adr-no-placeholders). My file doesn't.
2. Spine must not contain TODO/TBD/XXX. My AD-009 doesn't.
3. nfr.md must contain "99,95". Still there.

Let me run a quick validation: check the yaml parses, and grep for the fitness-rule patterns.

Actually, I'll run a combined shell command to validate YAML (if python/yaml available) and check for the forbidden patterns. But per the guidance, I should prefer dedicated tools. For YAML validation, there's no dedicated tool; I'll use run_shell_command with python. Let me check if there's a simple way.

Let me run:
`python3 -c "import yaml,sys; yaml.safe_load(open('.../openapi/tsp-api.yaml')); print('YAML OK')"`

But pyyaml might not be installed. Let me try. If it fails, I'll fall back to a manual note.

Actually, I could also check if `npx` / openapi validator is available, but that's overkill. A simple yaml parse is enough for "well-formed" (not full OpenAPI schema validation, but syntax).

Let me run the python check. Also grep for fitness patterns to confirm no `<!--` in the new ADR and no TODO in spine.

Let me do these verifications.
The YAML is well-formed by inspection. Let me run a lightweight verification: parse the YAML and confirm the repo's fitness-rule invariants still hold.

  `run_shell_command(command="cd <HARNESS>/runs/cells/superpowers-r2/ws && git status --short && echo '---', description="Show git status and diff stat")`

YAML parses OK, and the fitness rules (no HTML comments in ADR, no TODO/TBD/XXX in spine) are satisfied.

Now let me do a final review of the whole package. Let me verify:
1. The `docs/change-podpiski-sbp.md` and ADR-008 and subscription-state-machine are consistent.
2. Check git status to report what changed.

Let me run git status to enumerate the changes.

Actually, let me also double-check: is there a concern about the `.arch-handoff/` copies? The repo has duplicate ADRs in `.arch-handoff/adr/` and `docs/adr/`. I only created ADR-008 in `docs/adr/`. The `.arch-handoff/` is a generated handoff package (epic-context) with `ARCHITECTURE.md` that aggregates ADRs. I'm intentionally NOT modifying `.arch-handoff/` because it's a generated artifact for the walking-skeleton handoff, and my change is a new Proposed ADR pending A3. This is the right call. I'll note this in my summary.

Let me run git status to enumerate changes.

Also, I should reflect on whether the brainstorming skill's flow requires me to now present the design and get approval. The user asked me to produce the package and report files. I've done that. The design is now in the files. In my final summary, I should:
- Summarize what was produced (mapping to the 7 deliverables).
- List created and modified files (the user explicitly asked for this).
- Note the verification (YAML OK, fitness rules pass).
- Note the human-decision items (deliverable #7) — but I already put them in the doc; I can briefly point to them.

I should keep the final response concise but complete, per the user's request ("кратко перечисли созданные и изменённые файлы").

Let me run git status to get an accurate list.
YAML parses cleanly and the repo's fitness-rule invariants hold. Let me confirm the full set of changes via git.


Everything is in place. Let me now write the final summary, mapping to the 7 deliverables, listing created/modified files, and noting verification.

I should keep it concise per the user's request, but complete. I'll provide:
1. A one-line statement that the package is ready.
2. A brief mapping of the 7 deliverables to artifacts.
3. The list of created and modified files.
4. Verification note.
5. Brief pointer to what needs human decision (already in the docs).

Let me write the final response in Russian (matching user language).

I should be careful not to over-claim: I ran YAML parse (syntax OK) and checked fitness patterns; I did NOT run a full OpenAPI schema validator or a full "arch control check" (no such runnable tool). I'll state exactly what I verified.

Let me write the final summary concisely.

Actually, let me reconsider the deliverables mapping to be precise:

1. Оценка значимости + маршрут → `docs/change-podpiski-sbp.md` §1
2. Влияние на инварианты → `docs/change-podpiski-sbp.md` §2 + `ARCHITECTURE-SPINE.md` (AD-009)
3. Архитектурное решение (альтернативы/последствия/обратимость) → `docs/adr/ADR-008-...md`
4. Изменения контрактов → `openapi/tsp-api.yaml`, `docs/contracts/tsp-api.md`, `docs/contracts/opkc-adapter.md`
5. NFR → `docs/nfr.md` §8
6. Критерии приёмки + план отката → `docs/change-podpiski-sbp.md` §6
7. Что остаётся человеку → `docs/change-podpiski-sbp.md` §7

Plus supporting: `docs/spec/subscription-state-machine.md` (автоматы), `docs/solutioning.md` (scope + ADR mapping), `docs/rfp/vendor-rfp.md` (vendor scope), `README.md` (index).

Let me write the final response.
Готово. Архитектурный пакет изменения собран поверх принятого решения, в форматах самого репозитория (ADR + spine + спецификация автомата + контракты + NFR).

## Что покрывает каждый из 7 запрошенных пунктов

1. **Оценка значимости и маршрута** — `docs/change-podpiski-sbp.md §1` (Critical, архитектурный маршрут, почему именно).
2. **Влияние на инварианты** — `docs/change-podpiski-sbp.md §2` (таблица AD-001…AD-008: что меняется/что нет) + новый инвариант `AD-009` в `ARCHITECTURE-SPINE.md`.
3. **Архитектурное решение** — `docs/adr/ADR-008-…md` (решение, 3 таблицы альтернатив, последствия, обратимость).
4. **Изменения контрактов** — `openapi/tsp-api.yaml`, `docs/contracts/tsp-api.md`, `docs/contracts/opkc-adapter.md` (только аддитивно).
5. **Измеримые NFR** — `docs/nfr.md §8`.
6. **Критерии приёмки и план отката** — `docs/change-podpiski-sbp.md §6`.
7. **Что решает человек** — `docs/change-podpiski-sbp.md §7` (7 пунктов: механизм НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`, идентификатор плательщика, схема лимитов, пороги AML, политика возвратов, приоритет, тарифы).

## Созданные файлы

- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md`
- `docs/spec/subscription-state-machine.md` — автоматы согласия и рекуррентного списания
- `docs/change-podpiski-sbp.md` — сводный пакет изменения

## Изменённые файлы (аддитивно, в принятом формате)

- `ARCHITECTURE-SPINE.md` — добавлен `AD-009` (Proposed)
- `docs/solutioning.md` — вывод подписок из «вне scope» в scope, строка ADR-008, примечание к статусной модели
- `docs/nfr.md` — раздел §8 «Рекуррентные списания»
- `docs/contracts/tsp-api.md` — методы §3.6–3.9, новые вебхуки, коды ошибок, поля `paymentType`/`consentId`
- `docs/contracts/opkc-adapter.md` — методы `createConsent`/`getConsentStatus`/`revokeConsent`/`createRecurringPayment`, события `consent.*`
- `openapi/tsp-api.yaml` — пути `/v1/consents`, схемы `ConsentRequest`/`Consent`, расширение `Payment`/`PaymentRequest`
- `docs/rfp/vendor-rfp.md` — scope вендора + POC-сценарий P9
- `README.md` — индекс документов и статус

## Проверка

- `openapi/tsp-api.yaml` — синтаксически валиден (`yaml.safe_load` → OK).
- Fitness-правила репозитория соблюдены: в новом ADR нет `<!--`, в spine нет `TODO/TBD/XXX`, `nfr.md` сохраняет `99,95`.

Замечание: `.arch-handoff/` (сгенерированный handoff-пакет walking skeleton) намеренно не трогал — это производный артефакт текущего решения; новый ADR-008 в статусе Proposed пойдёт в handoff уже после ратификации A3. Код не писал — пакет готов к выносу на архитектурное решение.
