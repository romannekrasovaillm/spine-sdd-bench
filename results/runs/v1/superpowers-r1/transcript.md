<!-- источник: <HARNESS>/runs/cells/superpowers-r1/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-cells-superpowers-r1-ws/chats/cd871185-7f5c-4a12-b641-8ebd85caee19.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `skill(skill="superpowers:brainstorming")`

The user is asking me to act as a solution architect for a bank, working on a repository that's an accepted solution "Платёжный шлюз СБП (C2B-приём)". The task is to prepare an architectural package for a new feature: recurring C2B charges by payer consent — СБП subscriptions.

Let me first check the skills. There's a `superpowers:brainstorming` skill and `superpowers:writing-plans` skill. But this is a documentation/architecture task, not code. Let me think about what skills apply.

The GEMINI.md context says I MUST invoke relevant skills before any response. Let me think:
- `superpowers:brainstorming` — "You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation."

This is a design task (architecture design). It's creative work in the sense of designing a new feature. But the user has given a very detailed, structured request with 7 specific deliverables. They've already done the "brainstorming" of requirements in a sense. But the skill says to use it before creative work.

Actually, let me re-read. The user's request is essentially to produce an architectural package. This is a well-specified task. But there may be a brainstorming skill that I should use.

Also there's `superpowers:writing-plans` — "Use when you have a spec or requirements for a multi-step task, before touching code." But this is not code — it's architecture docs.

Let me think carefully. The task is:
1. Read the repository (ARCHITECTURE-SPINE.md, docs/, openapi/tsp-api.yaml, .arch-handoff/)
2. Produce an architectural package

This is fundamentally a research + writing task. The "creative work" here is designing the architecture. The brainstorming skill might apply, but the user has already provided extensive requirements.

Let me consider the most important thing: the user says "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." (The project may have methodological skills and tools installed — use them as intended.)

So I should check what's in the project. Let me look at the repository structure more, and check for any project-level skills or methodological instructions (QWEN.md, AGENTS.md, etc.).

Let me first explore the repository to understand the context before deciding on skills. Actually, per the using-superpowers skill, I should invoke skills BEFORE exploring. But which skill?

Let me think about what's the right first move. The instruction from GEMINI.md says: "Invoke relevant or requested skills BEFORE any response or action — including clarifying questions, exploring the codebase, or checking files."

So I need to identify the relevant skill. The most relevant is likely `superpowers:brainstorming` for the creative design work. But actually, this is a well-defined architecture task where the user has already specified the exact deliverables.

Hmm, let me reconsider. The brainstorming skill is about "creating features, building components, adding functionality, or modifying behavior." This task is about designing an architectural change (adding recurring subscriptions). That's arguably "adding functionality" at the design level.

But there's tension: the user has given a very structured, detailed request. They want specific outputs. The brainstorming skill explores intent/requirements — but here requirements are quite clear.

Actually, I think the honest approach is: this is an architecture/documentation task. Let me check if there's a relevant skill. The available skills include brainstorming, writing-plans, systematic-debugging (not relevant), etc.

Let me think about what would actually help. The task is essentially:
1. Read and understand the current architecture
2. Design the new feature
3. Write an architectural package

The `superpowers:writing-plans` skill is about implementation plans. Not quite this.

`superpowers:brainstorming` is about exploring intent before implementation. The user has given clear requirements but there are ambiguities (e.g., how deep should the design go? What are the actual invariants?).

Actually, I think the right approach here is:

1. First, I should invoke `superpowers:brainstorming` since this is creative design work (designing a new feature). OR I should first explore the repo to understand it.

Wait, let me reconsider the whole thing. The GEMINI.md is a "skill" that's imported into my context. It says to use skills. But there's a subtlety: the note says "User instructions (CLAUDE.md, AGENTS.md, GEMINI.md, etc, direct requests) take precedence over skills."

The user has given a very direct, detailed request. And the user says "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." — meaning use the project's installed skills.

So I need to check the project for skills and instructions. Let me look at the repository.

Actually, let me step back and think about the practical flow:

1. I need to explore the repository thoroughly to understand:
   - ARCHITECTURE-SPINE.md (invariants AD-001..AD-008)
   - docs/ (solutioning.md, nfr.md, ADR-001..007, contracts, state machine)
   - openapi/tsp-api.yaml
   - .arch-handoff/ (rules, handoff package)

2. Then design the recurring subscription feature.

3. Then write the architectural package.

The question of which skill: I think `superpowers:brainstorming` is the most applicable process skill for "design a new feature." But given the user has given extremely detailed requirements (7 deliverables), maybe the brainstorming is mostly done.

Actually, let me reconsider. Let me re-read the brainstorming skill's trigger: "You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior."

This IS creating a feature (designing recurring subscriptions). So I should use brainstorming first.

But wait — there's also the consideration that this is a read-heavy, write-heavy task where I need to understand the existing architecture deeply first. The brainstorming skill would have me explore intent and requirements with the user.

Hmm, let me actually invoke the brainstorming skill to see what it says, then decide. Actually, I can't see the skill content without invoking it. Let me invoke it.

Actually, wait. Let me reconsider the priorities. The user's request is a substantial architecture task. Let me think about what skills genuinely apply:

1. `superpowers:brainstorming` — for creative/feature work. This applies.
2. `superpowers:writing-plans` — for multi-step tasks with spec. Possibly applies at the end.
3. `superpowers:verification-before-completion` — when claiming completion.

I think the right first step is to invoke `superpowers:brainstorming`. It's the "process skill" that comes first for "let's build X" type requests.

But actually, let me reconsider once more. Is this "building" something? The user explicitly says "Код не пиши" (don't write code). This is producing an architectural design document package. This is closer to a research + writing task than a coding task.

The brainstorming skill is about exploring requirements before implementation. The user has already done the requirements exploration themselves and given me a precise list of 7 deliverables. So brainstorming might be partially redundant.

However, the skill mandate is strong: "If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill."

So there's clearly a >1% chance brainstorming applies. Let me invoke it.

Actually, let me think about the sequence more holistically. I'll:
1. Invoke `superpowers:brainstorming` (process skill for creative design)
2. Follow its guidance
3. Explore the repo
4. Design
5. Write the package

Let me also consider: should I explore the repo first to understand it, then invoke skills? No — the using-superpowers skill says skill check comes BEFORE exploring.

But I also need to understand the repo. The brainstorming skill will likely guide me to explore requirements. Let me invoke it first and see.

Let me start by invoking the brainstorming skill.

Actually, I realize I should think about whether to invoke multiple skills or just one. The using-superpowers skill says "When multiple skills apply, process skills come first." Brainstorming is the process skill here.

Let me invoke brainstorming first. Then based on its content, proceed.

I'll announce what I'm doing first (per my own operational guidelines, I should briefly state what I'm about to do before first tool call).

Let me write a brief intro and invoke the skill.

Actually, wait — I should be careful. Let me re-read: "Invoke relevant or requested skills BEFORE any response or action". The using-superpowers skill itself says "announce 'Using [skill] to [purpose]' and follow the skill exactly."

So I should announce and invoke. Let me do that.

Let me start with brainstorming.
Я начну с методического навыка проектирования, затем изучу репозиторий и подготовлю архитектурный пакет.

Использую `superpowers:brainstorming` для исследования намерения и требований перед проектированием.

  `glob(pattern="**/*")`
  `glob(pattern="**/*.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/ARCHITECTURE-SPINE.md")`

Now I understand the brainstorming skill. Let me classify this request.

This is a design task — designing an architectural change (recurring C2B subscriptions). The user wants an "архитектурный пакет" (architectural package) to bring to architectural decision and then hand off to implementers.

Key classification question: is this "architectural" path, "bounded", or "spike"?

This is clearly architectural: "new subsystems, changes that restructure how components fit together or alter interfaces others depend on." Recurring subscriptions is a new subsystem (subscription management, recurring debits), alters interfaces (API contracts), affects invariants.

But there's a nuance. The user is asking me to PRODUCE an architectural package — not to implement code. The deliverables are:
1. Change significance assessment + route (how deep design needed)
2. Impact on accepted architecture (invariants)
3. Architectural decision with alternatives, consequences, reversibility
4. Contract changes without breaking consumers
5. Measurable NFRs
6. Acceptance criteria + rollback plan
7. What remains for human architect + why

This is essentially producing a written architectural design/spec document. The user has already done substantial requirements exploration (7 specific deliverables). They've given clear intent, constraints (don't write code, don't break invariants AD-001..AD-008, don't break existing consumers), and success criteria.

So this maps to the "architectural" path. The outcome is a written spec/design document (architectural package).

However, there's an important nuance in the brainstorming skill: it wants me to:
1. Explore project context
2. Ask clarifying questions (one at a time)
3. Propose 2-3 approaches
4. Present design sections
5. Write design doc
6. Get user review
7. Transition to writing-plans

But the user's request is a specific, well-defined deliverable. They want me to produce a package. The user has already essentially specified the design process outputs they want.

Let me think about whether I need to ask clarifying questions. The user's request is quite detailed, but there ARE genuine ambiguities that matter for the design:

1. What kind of consent/authorization mechanism is in scope? (СБП has specific regulations — recurring payments in СБП are governed by Банк России rules. There's a "subscription" mechanism in СБП using "списания без дополнительного подтверждения" via tokenized consent.)

2. What's the actual scope: full subscription lifecycle (creation, modification, cancellation by payer) vs just recurring debits?

3. Who manages the consent — the bank, the TSP, or the СБП operator (НСПК)?

4. Settlement/refund flows?

Actually, I should first EXPLORE the repo to understand the current architecture, then determine what questions are genuinely needed.

But wait — there's a tension here. The brainstorming skill says I should explore context first, then ask clarifying questions. But the user has given a very complete request and might expect me to just produce the package.

Let me re-read the user's exact ask: "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям."

So the user wants me to prepare the package. This IS the architectural design work. The 7 deliverables map to the sections of an architectural design/spec.

Given the detail in the request, and the fact that this is a documentation/architecture task (not code), I think the right approach is:

1. First, explore the repo thoroughly (this is allowed even before completing the brainstorming gate — "Read-only project exploration is allowed while those prerequisites remain incomplete").

2. Then, based on what I find, determine genuine ambiguities and ask focused clarifying questions if needed.

3. Then present the design / write the package.

But actually, let me reconsider the classification and how heavy the process needs to be. The brainstorming skill has a HARD GATE: for architectural path, the human partner must review and approve the written spec, then review the written implementation plan.

However, the user's request is itself the task: "prepare an architectural package." The deliverable IS the design document(s). So the "written spec" here would be... the architectural package itself, which includes the architectural decision (ADR), contract changes, NFRs, acceptance criteria.

Hmm, let me think about how to map this properly.

The user is asking me to be a solution architect. The output is an architectural decision package. In the repo, there's a `.arch-handoff/` with rules (CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, TASK.md) and there's `docs/adr/` with ADR-001..007, and `docs/solutioning.md`, `docs/nfr.md`.

The repo itself defines HOW to make architectural decisions — there's likely a process (ADR format, etc.). The user says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" (change accepted decision files only the way accepted in this repo).

So I need to:
1. Understand the repo's methodology (ADR format, how ADRs are added, how contracts change, how NFRs are expressed).
2. Produce the new architectural package following that methodology.

The brainstorming skill's "architectural path" says write spec to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`. But the user's repo has its OWN methodology and location conventions (docs/adr/, docs/spec/, docs/contracts/, docs/nfr.md, etc.).

There's a conflict between the brainstorming skill's default location and the repo's conventions. The skill says "User preferences for spec location override this default." And more importantly, the user's repo has established methodology that I must follow ("изменяй только тем способом, который принят в этом репозитории").

Also, the user said "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению" (the project may have methodological skills and tools installed — use them as intended). This suggests I should look for project-specific skills/tools.

So my plan:
1. Explore the repo thoroughly — especially .arch-handoff/ (the rules and handoff package), ARCHITECTURE-SPINE.md, docs/ structure, README.md.
2. Check for any project-specific skills, QWEN.md, AGENTS.md, or methodology files.
3. Understand the ADR process and contract change process.
4. Then decide what clarifying questions to ask (if any).
5. Then produce the package.

Let me start exploring. I should read the key files. Let me do a broad exploration first.

Actually, let me be strategic. I'll read:
- README.md (overview)
- ARCHITECTURE-SPINE.md (invariants)
- .arch-handoff/ files (TASK.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, ARCHITECTURE.md)
- docs/ structure and key files

Let me also glob for any skill/instruction files in the repo.

Let me announce the classification first. This is clearly architectural.

Let me do parallel exploration. First, let me get the full directory listing and read the key files.

Let me start with a broad set of parallel reads and searches.

Actually, I need to be careful about not overwhelming. Let me first glob the whole repo structure, read README, ARCHITECTURE-SPINE, and the .arch-handoff files in parallel.

Let me classify out loud first: "This is architectural."

Then explore.
Классифицирую задачу: это **architectural** — новый подсистемный функционал (рекуррентные списания, управление согласием), меняющий контракты и затрагивающий инварианты. Пройду путь: изучение контекста → уточняющие вопросы → подходы → дизайн → письменный пакет → ревью.

Сначала изучу репозиторий и его методику (`.arch-handoff/`, `docs/`, `ARCHITECTURE-SPINE.md`), а также поищу установленные в проекте навыки/инструкции.

  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/.arch-handoff/ARCHITECTURE.md")`

Now let me read the key documentation files. Let me read in parallel:
- .arch-handoff/TASK.md
- .arch-handoff/CONSTRAINTS.yaml
- .arch-handoff/RUBRIC.yaml
- .arch-handoff/MANIFEST.json
- .arch-handoff/ARCHITECTURE.md
- docs/solutioning.md
- docs/nfr.md
- docs/spec/state-machine.md
- docs/contracts/tsp-api.md
- openapi/tsp-api.yaml

Let me batch these reads. Some may be large. Let me read the most important ones first.
Изучаю методику передачи и ключевые документы.

  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/openapi/tsp-api.yaml")`

Now I understand the structure and methodology. Let me read the key source documents in full: docs/solutioning.md, docs/nfr.md, docs/spec/state-machine.md, docs/contracts/tsp-api.md, openapi/tsp-api.yaml. And the ADR files to understand the ADR format. Let me also read the ADR-007 (proposed A3) and ADR-005, ADR-006 since they're most relevant.

Let me read these in parallel. I need to understand:
1. The ADR format (for writing a new ADR)
2. The state machine (for the recurring payment state machine)
3. The TSP API contract (for contract changes)
4. NFR format (for new NFRs)
5. solutioning.md (the full design)

Let me read the main docs.

  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/adr/ADR-005-integraciya-s-abs-zac)`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/adr/ADR-002-model-konsistentnosti)`

Now I have a good understanding. Let me read the ADR files to understand the ADR format precisely (especially ADR-007 which is "Accepted" status and ADR-005, ADR-006 for their format). I need to understand:

1. The exact ADR format used (Date, Status, Owner, Related, Context, Decision, Alternatives Considered, Consequences, Reversibility, References)
2. The contracts/opkc-adapter.md (internal adapter contract — this may need changes for recurring)
3. The vendor-rfp.md

Let me also check if there are any project-level skills or instruction files (QWEN.md, AGENTS.md, etc.) that I might have missed. The glob showed only .md files in docs, .arch-handoff, README, ARCHITECTURE-SPINE. No QWEN.md or AGENTS.md. But there might be skills in a `.qwen` directory or similar. Actually, the glob `**/*` only returned 28 files — no skill directories. Wait, but the `**/*` glob may have excluded dotfiles. Let me check for `.qwen` and other hidden dirs. Actually the glob pattern `**/*` returned files including `.arch-handoff/...` and `.git/...` (implied). It didn't show `.qwen` directory. Let me not worry — the available skills are already listed in system reminder, and there are no project-specific skills listed (they'd appear in available_skills). The available skills are all bundled or extension (superpowers). So no project-specific methodological skill beyond superpowers.

Wait, actually, let me reconsider. The user said "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." This might just be a generic instruction meaning "use whatever methodological skills/tools are installed." The available skills are superpowers (extension) + bundled. I've already invoked brainstorming. Good.

Now, let me read the ADR files to understand the format. Let me read ADR-007 (accepted), ADR-005 (ABS), ADR-006 (trust), and one or two more to get the full format. Also read contracts/opkc-adapter.md and rfp/vendor-rfp.md briefly.

Actually, I already saw ADR-001's full format from the .arch-handoff/ARCHITECTURE.md (which contains the concatenated ADRs). Let me read the actual ADR files to get exact format, especially ADR-007 for the "Accepted" status format, and ADR-005 for ABS saga.

Let me read ADR-005, ADR-006, ADR-007, and contracts/opkc-adapter.md.
Читаю ADR (формат и содержание) и внутренний контракт адаптера ОПКЦ.

  `write_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/adr/ADR-008-rekurrentnye-spisaniy, content="# ADR-008. Рекуррентные C2B-списания по согласию плательщика (подписки СБП)\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: solution-ar)`
  `write_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/spec/consent-state-machine.md", content="# Статусная машина согласия и списания по согласию — спецификация переходов\n\n- Status: Draft (для ревью на гейте A1 подписок)\n- Owner: s)`

I now have a comprehensive understanding of the repository, its methodology, and content. Let me also check the vendor-rfp.md and ADR-003, ADR-004 briefly to be thorough, but I think I have enough. Let me also check the ADR-001, ADR-003, ADR-004 briefly to be complete on the format and to know what's in them for the "impact on invariants" analysis.

Actually, I already have the key content. Let me quickly read ADR-003 (mTLS) and ADR-004 (at-least-once/DLQ) and ADR-001 to complete the picture, plus vendor-rfp.md. Actually, the .arch-handoff/ARCHITECTURE.md already gave me ADR-001 fully. Let me read ADR-003 and ADR-004 briefly, and the vendor-rfp.md.

Actually, I think I have enough to proceed. But for completeness of the "impact on invariants" analysis and to understand the notification model (ADR-004), let me read ADR-003 and ADR-004 quickly. These matter for the recurring subscriptions design (e.g., consent storage, tokenization, notification flows).

Let me also understand: what is the key domain knowledge I need about СБП recurring/subscription payments?

СБП (Система быстрых платежей) has a mechanism for "платежи по подписке" / "автоплатежи" (recurring payments). This is a real feature of СБП. Key concepts:

1. **Согласие плательщика (consent)** — In СБП, recurring payments require the payer's consent, which is registered with the payer's bank (банк плательщика) through the СБП infrastructure. The consent (согласие) is a mandate that allows the TSP to initiate debits without the payer's active action each time.

2. The СБП subscription flow (as implemented by НСПК / Банк России): There's a "согласие на списание" (consent for debit) mechanism. The payer gives consent in their bank's app (банк плательщика), and the consent is registered in СБП. Then the TSP can initiate "C2B-платеж по согласию" (payment by consent) without a QR.

3. There are actually a few related mechanisms:
   - **С2В-платежи с подпиской** (recurring/subscription C2B payments) — introduced by НСПК around 2022-2023 as "СБП-подписки" / "автосписания".
   - The payer gives a one-time consent (согласие), which can be for a fixed amount or a range, with a validity period, maximum amount, frequency limits.
   - The TSP then initiates debits against this consent.

4. Key regulatory terms: 161-ФЗ, Положение ЦБ № 820-П (about information security), and specifically the consent mechanism for СБП is described in НСПК documentation and ЦБ regulation about "платежи без согласия" prevention (there was a requirement that recurring payments must have explicit consent, with max amount, period, and the ability to revoke).

Actually, let me be careful. The exact protocol details are marked `[ТРЕБУЕТ ПРОВЕРКИ]` in this repo because the НСПК documentation is an external input. So I should not over-specify protocol details. I should follow the same discipline: mark protocol details as `[ТРЕБУЕТ ПРОВЕРКИ]`.

Key domain facts I'm confident about (to use in the design, but flag protocol-level details):
- Recurring СБП payments require **consent (согласие)** of the payer.
- The consent has parameters: **maximum amount** (or fixed amount), **validity period**, **frequency limit** (e.g., max N debits per period), **scope** (specific TSP + specific payer).
- The payer can **revoke** the consent at any time (through their bank / СБП).
- The consent is registered with the **payer's bank** (банк плательщика), which verifies and holds it, and through СБП infrastructure the acquiring side (эквайер / ТСП side) gets a reference/token to initiate debits.
- This is fundamentally different from the QR flow: no QR, no active payer action at payment time.

Now, architecturally, what's the impact on this repo's architecture?

The current architecture is C2B-приём via QR. The recurring subscriptions add a new **flow type** (payment initiated by consent, not by QR) and a new **entity** (consent/mandate) with its own lifecycle and state machine.

Key architectural questions:

1. **Where does the consent live?** The consent is fundamentally held by the payer's bank and registered in СБП. The acquiring bank (our bank / ТСП side) needs to:
   - Receive/register consent references (from the ТСП, who obtains consent from the payer).
   - Initiate debits against the consent.
   - Handle consent revocation notifications.

   Actually, there are two consent models:
   - **Consent obtained by the ТСП** (the merchant gets the consent directly from the customer, e.g., in their app, and registers it via the bank).
   - **Consent obtained via СБП** (the payer authorizes in their bank app, consent flows through СБП infrastructure to the ТСП's bank).

   The exact model depends on НСПК protocol [ТРЕБУЕТ ПРОВЕРКИ]. But the key architectural point: consent is a new first-class entity with its own state machine (ACTIVE → REVOKED → EXPIRED, etc.), and debits against it are a new payment initiation path.

2. **Does this change the core payment state machine?** The payment state machine (CREATED→QR_ISSUED→PAID→CREDITED→COMPLETED) is QR-specific in the sense that `QR_ISSUED` is a QR-specific state. For consent-based debits, there's no QR. So we either:
   - **Generalize** the state machine (rename QR_ISSUED → something like `AUTHORIZED`/`INITIATED`), or
   - **Add a parallel flow** with a consent-specific state (e.g., `CONSENT_CHARGED`), or
   - **Reuse most of the machine** but skip the QR_ISSUED state for consent debits (CREATED → PAID → CREDITED → COMPLETED).

   This is a real design decision. The cleanest is probably to keep the same states but note that `QR_ISSUED` is "payment instrument issued / ready for debit" — for consent, the "instrument" is the consent reference rather than QR. Actually, the ADR-002 says states may need detail per НСПК documentation. But the spine invariant AD-005 (credit only from PAID) is unchanged.

   Hmm, but there's a subtlety: for consent-based debit, the "PAID" is confirmed by НСПК after the debit is executed. So the flow is: ТСП initiates debit → шлюз creates payment → adapter sends debit request to НСПК → НСПК processes against consent → confirms PAID (or REJECTED). The "QR_ISSUED" state doesn't apply. So the state machine needs a generalization.

3. **Which invariants (AD-001..AD-008) are affected?**
   - AD-001 (изоляция платёжного контура): unchanged — consent logic stays in the gateway.
   - AD-002 (единый источник истины — статусная машина): **extended** — a second state machine (consent) and possibly a generalized payment machine. The rule itself (atomic status+outbox) is unchanged, but the *set of entities* grows.
   - AD-003 (идемпотентность): unchanged, but new idempotency keys (consentId, debit reference).
   - AD-004 (единственный адаптер ОПКЦ): unchanged — consent protocol also goes through the adapter. The adapter contract extends with consent operations.
   - AD-005 (зачисление только из PAID): unchanged — debit-based payments still credit only from PAID.
   - AD-006 (trust-зоны): unchanged.
   - AD-007 (НПС/КИИ/ПДн): **extended** — consent involves storing more ПДн (payer identifier), consent params. More sensitive data.
   - AD-008 (гибрид стратегия): unchanged, but the adapter contract grows — vendor must support consent/debit operations.

   Also the **Deferred** section: the spine explicitly defers "автоплатежи" (autopayments)! Look at solutioning.md line: "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." And ARCHITECTURE-SPINE.md Deferred section lists "Диспуты/претензии" but NOT explicitly autopayments in the deferred list — wait, let me check. The spine's Deferred section lists:
   - Мультивалютность
   - C2C-переводы и выплаты B2C/B2B
   - Диспуты/претензии

   Autopayments (рекуррентные/подписки) are NOT in the spine's Deferred list explicitly, but they ARE in solutioning.md's roadmap (out of scope). This is important: the feature is currently out-of-scope, so bringing it in means **updating the scope** — and the spine's Deferred section should be updated (or a new initiative). Actually, wait — this is a "feature" level spine. Recurring subscriptions are a related feature. Is it a new initiative or an extension of this feature?

   This is actually one of the key "route/significance" questions: recurring C2B is a distinct initiative (подписки СБП) that builds on the C2B-приём foundation. It's arguably a **sibling feature** that reuses the C2B gateway, OR an **extension** of the same feature.

   The repo's own structure (README says "Подключение банка к СБП (эквайринг C2B)") and the spine says "Родительский spine: initiative «Подключение банка к СБП (эквайринг C2B)». Данный spine — уровень feature." So this spine is a feature under an initiative. Recurring subscriptions is a new feature that could be a **new feature-spine under the same initiative**, or a new initiative.

   This matters for the "route" assessment. I think the honest assessment is: this is a new feature (новый spine feature) that depends on the existing C2B-приём feature, reusing its gateway, status machine, adapter, АБС integration, and trust zones. It extends the adapter contract and the payment state machine.

4. **Contract changes (tsp-api.yaml)**: New endpoints for:
   - Consent registration: `POST /v1/consents` (register a consent obtained from payer)
   - Consent status: `GET /v1/consents/{consentId}`
   - Consent revocation: `POST /v1/consents/{consentId}/revoke` (or DELETE)
   - Debit initiation: `POST /v1/debits` or extend `POST /v1/payments` with a `paymentType` / `consentId` field.
   - New webhook events: `consent.created`, `consent.revoked`, `consent.expired`, `debit.completed`, `debit.failed`.

   Backward compatibility: add optional fields to `PaymentRequest` (e.g., `consentId`), add new paths, don't change existing semantics. Version stays `/v1` (additive), or introduce new resource `/v1/consents` and `/v1/debits` separately so existing `/v1/payments` unchanged.

   The cleanest backward-compatible approach: keep `/v1/payments` for QR; add `/v1/consents` and `/v1/debits` (or `/v1/consents/{id}/debits`) as new resources. This avoids touching the existing `PaymentRequest` schema. But there's a question of whether a debit IS a payment (shares the payment state machine and idempotency). I think debits should be modeled as payments with an additional `initiationType` field, but exposed via a new endpoint to avoid breaking the existing one. Or: extend `/v1/payments` with optional `consentId` — additive and backward-compatible.

   Actually, the repo's own versioning policy says: "Добавление опциональных полей — обратно совместимо, не требует новой версии." So adding optional fields to `PaymentRequest` is allowed. But adding a new resource path `/v1/consents` is cleaner for the consent lifecycle (which is genuinely a new entity, not a payment).

5. **NFRs**: New measurable NFRs for recurring:
   - Consent registration latency
   - Debit processing latency / success rate
   - Consent state consistency (revocation propagation)
   - Idempotency of debits (no double debit)
   - Limits enforcement (max amount, frequency)
   - No double debit (zero), no debit after revocation (zero)
   - Availability same as gateway

6. **Acceptance criteria + rollback**: 
   - Feature flags for enabling subscription capability per ТСП
   - Stop-new debits without stopping QR payments
   - Rollback: since debits are additive, rollback = disable consent endpoints + stop scheduler, no data migration back.

7. **What remains for human architect**:
   - Regulatory/legal: consent storage model, ПДн retention, 152-ФЗ basis
   - The НСПК protocol details [ТРЕБУЕТ ПРОВЕРКИ]
   - Business decisions: which consent model (ТСП-obtained vs СБП-obtained), limits, tariffs
   - Whether to treat as new initiative (change parent spine) or feature extension
   - Вендор RFP scope (does the transport adapter vendor support consent/debit operations)

Now, the key question per the brainstorming skill: what clarifying questions should I ask?

The brainstorming skill says "Ask clarifying questions — one at a time, understand purpose/constraints/success criteria." But the user's request is quite detailed and they've asked me to "prepare the package." The user is clearly an expert (a solution architect persona). 

However, there ARE genuine ambiguities that would materially change the design. The most important one is:

**Which consent model?** In СБП, there are (at least) two flows:
(a) **Согласие, получаемое через СБП** — плательщик даёт согласие в приложении своего банка, согласие регистрируется через инфраструктуру СБП (банк плательщика → НСПК → банк ТСП).
(b) **Согласие, получаемое ТСП напрямую** — ТСП сам получает согласие (оферта) от клиента и регистрирует его в банке-эквайере.

These have very different architecture implications. But actually, in the СБП subscription mechanism as standardized by НСПК, the consent is typically created in the payer's bank app and flows through СБП. But the ТСП-side integration might differ.

Actually, given the repo marks all protocol details as [ТРЕБУЕТ ПРОВЕРКИ], and given the user asked me to produce a *package* (not to fully resolve every detail), I think the right approach is:

1. Do the read-only exploration (done).
2. Ask ONE or TWO genuinely load-bearing clarifying questions before finalizing the design, OR present my understanding and a design with clearly-marked decision points for the human architect.

Given the brainstorming skill's guidance, and given this is an "architectural" path, I should ask clarifying questions. But I also need to be pragmatic: the user gave a very complete brief and wants a package. The user explicitly listed 7 deliverables including "What remains for human architect."

Let me identify the genuinely load-bearing ambiguities where a wrong assumption would invalidate the whole package:

1. **Scope of "рекуррентные C2B-списания по согласию"**: Is it full subscription lifecycle (create consent, initiate recurring debits on schedule, handle revocation/expiry, partial refunds) — or just the debit-by-consent primitive? The user says "подписки СБП" and "рекуррентные C2B-списания по согласию плательщика". This strongly implies the full recurring debit mechanism, but "подписки" might imply a scheduler/orchestrator (who triggers the recurring debit?).

   **Key question: who triggers the recurring debit?** 
   - (a) The ТСП triggers each debit via API (pull model) — the gateway is a passive debit executor.
   - (b) The gateway (or a scheduler) triggers debits on a schedule (push model) — the gateway manages subscription schedules.

   This is a HUGE architectural difference. "Подписки" (subscriptions) usually implies a schedule. But many payment gateways only provide the "debit by consent" primitive and let the merchant's billing engine handle schedules.

   This is probably THE most important clarifying question.

2. **Consent acquisition model** — who obtains and registers the consent (ТСП vs payer's bank via СБП). This affects the API surface.

3. **New initiative vs feature extension** — but this I can recommend and flag.

Actually, I realize I should think about whether to ask questions or just present the design with decision points. The brainstorming skill says for architectural path: "Ask clarifying questions — one at a time." But it also says "When the request already supplies the purpose and constraints, reflect that understanding instead of asking the same questions again."

The user's request supplies purpose and constraints clearly. But there are 1-2 genuinely load-bearing ambiguities. Per the skill, I should ask focused questions. The ask_user_question tool is available.

Let me think about what's truly load-bearing vs. what I can present as "decision point for human architect" (deliverable #7).

The user explicitly asked for deliverable #7 "Что остаётся на решение человека-архитектора и почему" — so they EXPECT some things to remain for the human. But there's a difference between "details to finalize" and "fundamental design forks that change the whole package."

I think the two genuinely load-bearing forks that would change the shape of the package are:
1. **Who triggers the recurring debit** (ТСП pull vs gateway schedule/push).
2. **Consent acquisition model** (via СБП payer bank vs ТСП direct).

Actually, let me reconsider. The СБП subscription reality: In the standardized СБП "подписка" flow, the consent is created by the payer in their bank's app, and it flows through СБП to the ТСП's bank. The ТСП's bank (us) then has a consent reference. The ТСП initiates debits against that consent. The schedule itself is managed by the ТСП (their billing system decides when to charge), OR the consent itself can specify a schedule.

Given uncertainty, I think the responsible thing is to ask 1-2 clarifying questions. But I should be efficient — the user wants a package, and asking too many questions would be annoying.

Let me use ask_user_question with a small number of focused questions. Actually, let me reconsider the interaction. The brainstorming skill wants ONE question at a time. But ask_user_question supports up to 4 questions. The skill says "Only one question per message." Hmm.

But actually, there's tension between the skill's "one question at a time" and pragmatics. The skill is quite explicit: "Only one question per message - if a topic needs more exploration, break it into multiple questions."

However, I also want to respect the user's time and the fact that they've given a detailed brief. Let me think about what's the SINGLE most load-bearing question.

I think the single most load-bearing question is: **What's the scope of "recurring" — does the gateway manage the subscription schedule (push), or does the ТСП trigger each debit (pull), with the gateway only providing the consent+debit-by-consent primitive?**

Actually, even more fundamental and combining: **What is the primary interaction model the business wants?** The user said "ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП." 

For онлайн-кинотеатры (online cinemas), связь (telecom): these are typically **subscription with fixed period** where the merchant bills monthly. The merchant's billing engine triggers the charge. So the gateway providing "debit by consent" (pull) is the standard. ЖКХ (utilities) can also be pull (utility bills variable amounts).

But "подписки СБП" as a product could also mean the gateway/SBП infra manages it.

I think the honest answer is: **both** — the consent primitive supports both, but the schedule management (who decides when to charge) is the key fork. The most likely business answer is "ТСП triggers each debit; gateway provides consent + debit primitive; scheduling stays with ТСП." But I shouldn't assume.

Given the guidance and the need to be rigorous, I'll ask a focused set of clarifying questions (using ask_user_question, which is the tool for this). But I need to balance with the skill's "one question at a time."

Let me reconcile: The brainstorming skill is a guideline; the user's actual request and the availability of ask_user_question (which supports multiple questions) suggests I can batch a few genuinely load-bearing questions. But the skill is explicit about one at a time.

Hmm. Actually, I think there's a reasonable middle path. The most load-bearing fork is the trigger model. But there are a few others. Given the user is clearly senior and wants a comprehensive package, and given they listed "what remains for human architect" as a deliverable (implying they want me to make reasonable decisions and flag the rest), I think the best approach is:

1. Ask the 2-3 genuinely load-bearing questions via ask_user_question (batched, since they're independent and each has clear options).

Actually, wait. Let me re-read the skill's guidance more carefully. It says "ask questions one at a time" but this is guidance for interactive dialogue. The ask_user_question tool explicitly supports up to 4 questions in one call. Given I have a tool designed for this, and the user is senior, I'll ask the load-bearing questions in one batch (2-3 questions), clearly separating them. This respects both the tool and the skill's intent (understand before designing).

But actually, let me reconsider whether I even need to ask, or whether I should present my understanding + design with explicit decision points and let the user correct.

The brainstorming skill's HARD GATE for architectural path: "the human partner reviews and approves the written spec, then reviews the written implementation plan." So the flow is: questions → approaches → design sections → written spec → user review → writing-plans.

Given the user's request is essentially "produce the architectural package" (which is the written spec/design), the natural flow is:
1. (Optional) clarifying questions on load-bearing forks
2. Propose approaches
3. Write the package (spec/design + ADR + contract changes + NFR + acceptance)
4. User reviews

I think asking a couple of genuinely load-bearing questions is the right move — it's cheap and prevents building the wrong thing. Let me identify the truly load-bearing questions:

**Q1 (most important): Trigger/scheduling model.** Who decides when a recurring debit happens?
- (a) ТСП pulls: gateway provides consent + "debit by consent" API; merchant billing engine triggers each charge. (Most common; gateway stays a passive payment executor.)
- (b) Gateway pushes: gateway manages subscription schedules (next charge date, frequency) and autonomously triggers debits.
- (c) Both.

**Q2: Consent acquisition/registration model.** Where does the consent originate and who registers it in our gateway?
- (a) Via СБП: payer consents in their bank app → СБП infra → consent reference lands in our gateway (acquiring side).
- (b) ТСП direct: ТСП obtains consent (oformление/offer) from payer and registers it with our gateway.
- (c) Both.

**Q3: Scope of the package.** Should the package cover the full subscription lifecycle (consent create/revoke/expiry, debit, refund of a debit, webhooks, NFR) — or just the minimum "debit by consent" primitive?

Actually Q3 is somewhat answerable by the user's brief (they listed 7 deliverables that clearly want the full package). So Q3 is less load-bearing.

Let me also consider: **Does the user want me to actually write files now, or just present the design in chat first?** The user says "Подготовь архитектурный пакет ... Код не пиши." and "Когда закончишь, кратко перечисли созданные и изменённые файлы." This implies they expect me to CREATE files (the package). So they want file output.

But the brainstorming skill says for architectural path: present design sections in chat, get approval, THEN write the spec doc. There's a gate.

Given the tension, and given the user's explicit "перечисли созданные и изменённые файлы" (list created and changed files), I believe the user wants me to actually produce the files. But the brainstorming skill wants approval before writing.

Let me reconcile: I'll follow a lightweight version — since the user has given a very detailed brief (essentially pre-approving the work) and asked for file deliverables, I will:
1. Ask the 2 genuinely load-bearing clarifying questions first (cheap, prevents wrong design).
2. Based on answers, present the design/approaches briefly and then write the package.

Actually, hold on. Let me reconsider the whole "should I ask questions" decision one more time.

The user is role-playing a senior solution architect giving me (also role-playing a solution architect) a task. The task is extremely well-specified with 7 concrete deliverables. The user said "Подготовь архитектурный пакет этого изменения." This is a "go do the work" instruction, not "let's brainstorm together."

The genuinely load-bearing forks (trigger model, consent model) are the kind of thing a solution architect would either (a) ask the business, or (b) present as options in the ADR with a recommendation and leave to the human decision (deliverable #7 "what remains for human architect").

Actually — deliverable #3 is explicitly "Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью" and deliverable #7 is "Что остаётся на решение человека-архитектора." This strongly suggests the user expects me to:
- Make a recommended decision (with alternatives) for the main architecture.
- Explicitly list what's left for the human.

So the trigger model and consent model are EXACTLY the kind of decision that should be in the ADR (with alternatives + recommendation) AND in "what remains for human" (if genuinely business-level).

Given this, I think the best approach is:
- Do NOT block on clarifying questions (the user wants a package, and the forks are precisely what should be presented as alternatives in the ADR + left as human decisions).
- BUT, per the brainstorming skill, I should still reflect my understanding and maybe confirm 1-2 truly critical forks.

Hmm, this is a genuine judgment call. Let me look at what's most valuable to the user.

Actually, I think the cleanest and most professional approach, honoring both the skill and the user's intent, is:

1. Reflect my understanding of the task in a concise note (what I understand the change to be, key assumptions, success criteria) — per brainstorming "write back your understanding."

2. Ask the 1-2 genuinely load-bearing questions where a wrong assumption would invalidate the package (trigger model and consent acquisition model), because these determine the entire shape of the ADR, contracts, and NFRs.

This is the "discover intent → write back understanding → ask what's missing" flow. It's cheap and it's exactly what a good solution architect does before writing a decision package.

But wait — I should be careful not to over-ask. Let me consolidate to the most essential.

Actually, let me reconsider the consent model question. In СБП, the "подписка/автоплатёж" is a specific, standardized flow. Let me recall the actual СБП subscription mechanism (as of my knowledge):

СБП introduced "СБП-подписки" (subscription payments). The flow:
1. The payer initiates a subscription in the ТСП's service (e.g., online cinema app/website).
2. The payer is redirected to their bank (банк плательщика) or the consent is created in the payer's bank app.
3. The payer's bank creates a "согласие" (consent/mandate) and registers it in СБП.
4. The consent is linked to the ТСП and its acquiring bank.
5. The ТСП can then initiate "списания" (debits) against this consent, subject to the consent's parameters (max amount, validity, frequency).
6. The payer can revoke the consent at any time.

So the consent is fundamentally created through the СБП infrastructure and the payer's bank. The acquiring bank (us) receives a consent reference via СБП (adapter ОПКЦ). The ТСП then initiates debits via the acquiring bank's API.

So the consent model is fairly standardized: consent originates with the payer's bank via СБП, and our gateway receives it via the adapter. The ТСП-side API is: (a) initiate a "consent request" (which triggers the payer redirect to their bank), (b) receive the consent status, (c) initiate debits against the active consent, (d) receive consent revocation events.

So actually the consent acquisition model is largely determined by СБП — the gateway needs to support the "consent request" initiation (ТСП → gateway → adapter → НСПК → payer's bank → payer approves → consent created → notification back). This is analogous to the QR flow but for consent.

The trigger model (who decides when to charge) is more of a product decision:
- For "подписки" (subscriptions with fixed period), the ТСП typically triggers each charge.
- The СБП consent mechanism itself supports "по запросу ТСП" (on-demand debit) rather than automatic scheduled debits.

So I think the trigger model is: **ТСП triggers each debit via the gateway's debit API** (pull model). The gateway provides the "debit by consent" primitive; scheduling is the ТСП's responsibility (their billing engine). This is the standard, lowest-risk, most-compatible approach and keeps the gateway a passive executor (consistent with existing architecture where the gateway doesn't have a scheduler beyond TTL expiry).

This is actually a good recommendation to make in the ADR, with the "gateway-managed scheduler" as a rejected/deferred alternative.

OK here's my refined plan. Given all this analysis, I believe the genuinely load-bearing questions to ask are actually quite few, and I can make strong, well-justified recommendations on most of them. The one thing I'm genuinely uncertain about and that would change the package is:

**The scope/ambition level**: Is this a full "subscription management" product (gateway schedules charges) or a "recurring debit by consent" capability (gateway is a passive executor, ТСП schedules)?

Actually, you know what, I've been going back and forth. Let me make a decision and commit:

I will ask a SMALL number (2-3) of genuinely load-bearing questions via ask_user_question, because:
1. The brainstorming skill mandates clarifying questions before design for architectural work.
2. These forks materially change the package shape.
3. The cost is low (one interaction).

The questions I'll ask:
1. **Trigger/scheduling model** — who triggers each recurring debit (ТСП pull vs gateway schedule). This determines whether there's a scheduler component (big architecture difference).
2. **Consent acquisition/registration** — confirm the СБП-native flow (consent created via payer's bank, reference delivered to us) vs ТСП-direct registration.
3. Maybe: **Delivery format** — but the user already said "созданные и изменённые файлы", so they want files.

Actually, let me also reconsider: should I ask about whether this is a NEW initiative (new spine) vs feature extension? This affects the spine/ADR structure. But I can make a recommendation (feature extension of the same initiative, new feature-spine) and flag it. It's more of a recommendation than a question.

Let me settle on asking 2 questions (trigger model, consent model), plus maybe a 3rd about the scope boundary (refund-of-debit in scope?).

Hmm, but actually the refund-of-debit: refunds already exist (ADR-005 saga), and a debit is just a payment, so refunds apply naturally. Not load-bearing.

Let me also consider: is there value in asking about **PДн/payer identifier storage**? This is a compliance issue (152-ФЗ). But it's really "what remains for human architect / ИБ" — I can flag it. Not a question for me to resolve.

Final decision: I'll ask 2 focused questions (trigger model + consent acquisition model), because these are the two forks that change the architecture most. I'll use ask_user_question with 2 questions.

Actually, wait — let me reconsider once more if I should ask at all vs. present understanding + recommendation. 

The user's tone is "go produce the package." They gave 7 deliverables. They're roleplaying a senior architect delegating to me. In such a context, the best move is often to demonstrate expertise by making well-justified decisions and flagging what's genuinely open — rather than bouncing questions back immediately.

But the brainstorming skill is quite insistent. And there IS genuine ambiguity. The skill says: "When that information is missing, ask one focused question about purpose or intended use before proposing features or an approach."

I think a hybrid is best and most professional:
1. Briefly write back my understanding (concise note of intent, constraints, success criteria + key assumptions).
2. Ask the 1-2 truly load-bearing questions (trigger model is the big one; consent model second).

This honors the skill (reflect understanding + ask what's missing) without over-asking.

Let me use ask_user_question for the trigger model and consent model. Actually, I'll ask about trigger model (Q1), consent acquisition model (Q2), and possibly the scope boundary of whether the package should assume the adapter/НСПК protocol is the "ТРЕБУЕТ ПРОВЕРКИ" external input (which is already established, so no need).

Let me write out the questions carefully.

Q1 — Trigger model (header "Trigger model"):
"Кто инициирует каждое рекуррентное списание?"
- Option A: "ТСП тянет (pull)" — ТСП вызывает debit-API по своему расписанию; шлюз — пассивный исполнитель списания по согласию. (Recommended — минимальное расширение, шлюз без планировщика)
- Option B: "Шлюз толкает (push)" — шлюз хранит расписание подписки (след. дата, частота) и сам инициирует списания.
- Option C: "Оба" — примитив списания по согласию + опциональный планировщик на стороне шлюза.

Q2 — Consent acquisition model (header "Consent model"):
"Как согласие плательщика попадает в шлюз?"
- Option A: "Через СБП (native)" — плательщик даёт согласие в приложении своего банка; согласие регистрируется через НСПК, ссылка на согласие приходит в шлюз через адаптер ОПКЦ. (Recommended — соответствует стандарту СБП-подписок)
- Option B: "ТСП напрямую" — ТСП сам получает согласие (оферта) и регистрирует его в шлюзе по API.
- Option C: "Оба"

Actually, I realize I should double check one thing: does the existing openapi/tsp-api.yaml only have createPayment and getPayment? Yes — it's a minimal draft with just those two paths. The docs/contracts/tsp-api.md is more complete (onboarding, refunds, webhooks). So the openapi is a subset/draft.

This matters for deliverable #4 "Изменения контрактов (openapi/tsp-api.yaml)". I need to propose additive changes to the OpenAPI.

OK, let me also reconsider: the user said the task is to prepare a package for architectural decision and handoff. The "route" (deliverable #1) is essentially asking me to classify significance and determine "how deep design needed." This is exactly the brainstorming classification (architectural) + a significance/market route assessment (like the repo's "Critical (11/15)" marking).

So my package should mirror the repo's existing structure. Where should I put it?

The repo has:
- `ARCHITECTURE-SPINE.md` — invariants (would need a new feature-spine or extension)
- `docs/solutioning.md` — full design
- `docs/nfr.md` — NFR
- `docs/adr/ADR-XXX.md` — ADRs
- `docs/contracts/` — contracts
- `docs/spec/state-machine.md` — state machine
- `openapi/tsp-api.yaml` — OpenAPI

For a new feature, the cleanest approach following the repo's conventions:
- A new ADR (ADR-008) for the recurring subscriptions architecture decision.
- Extension of `docs/spec/state-machine.md` (or a new `docs/spec/consent-state-machine.md`) — I'd add a consent state machine spec.
- Changes to `docs/contracts/tsp-api.md` (new endpoints) and `openapi/tsp-api.yaml`.
- New NFR entries in `docs/nfr.md` (or a new section).
- A solutioning doc for the feature (or a new `docs/solutioning-recurring.md`).
- Update `ARCHITECTURE-SPINE.md` (add new AD or update Deferred section).

But wait — the user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." (Change accepted decision files only the way accepted in this repo.) So:
- ADR files: follow the ADR format (Date, Status, Owner, Related, Context, Decision, Alternatives Considered, Consequences, Reversibility, References). New ADRs get "Status: Proposed" (since they're proposed until ratified by human).
- The spine: add new AD entries with "Status: Proposed" (like AD-001..AD-007 are "Proposed" until ADR ratified), and update the Deferred section.
- Contracts: versioning (additive, /v1, don't break).
- NFR: additive rows.

The CONSTRAINTS.yaml fitness rules: `adr-no-placeholders` requires no `<!--` comments in docs/adr/*.md. And `adr-set-complete` checks ADR-001 exists. There's also a fitness rule that `docs/nfr.md` must contain '99,95' and ADR-005 must contain 'только из состояния `PAID`'. So if I edit these files, I must preserve those patterns.

I should also be careful: the CONSTRAINTS.yaml says the stage is "решение (до кода)". The user wants me to prepare a package "чтобы его можно было вынести на архитектурное решение и затем передать исполнителям" — so this is a pre-decision package, and then it gets handed off.

Now, where does this package live? The brainstorming skill default is `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`. But the repo has its own structure. The user said use the repo's methodology. So I think the package should be integrated into the repo's existing docs structure (ADR, spec, contracts, nfr, solutioning), NOT in a separate superpowers/specs folder.

But there's a question of whether to create NEW files or modify existing. The cleanest, most repo-idiomatic approach:
1. **New ADR**: `docs/adr/ADR-008-rekurrentnye-spisaniya-podpiski-sbp.md` (+ mirror in `.arch-handoff/adr/`? — the .arch-handoff is a snapshot handoff package, I should NOT modify it, since it's a frozen handoff to the code harness. Actually, let me think. The .arch-handoff/ contains a COPY of the ADRs and ARCHITECTURE.md. The handoff is regenerated for the code harness. Since this task is "prepare package for architectural decision then handoff to implementers", I should create the package in docs/ (source of truth), and NOT modify .arch-handoff/ (which is a generated snapshot). The README says ".arch-handoff/ handoff-пакет кодовому харнессу". So .arch-handoff is generated output. I should leave it alone and only update docs/ + spine + openapi.)

Actually, let me verify: is .arch-handoff a generated artifact or hand-authored? The TASK.md, MANIFEST.json, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml are clearly the handoff package generated for the code harness (the "кодовый харнесс" receives this). The ARCHITECTURE.md says "Собран: 2026-08-15... Источники: docs/adr/...". So it's a generated distillation. I should NOT modify .arch-handoff/ — I should update docs/ (sources) and the spine and openapi.

So my planned file changes:
1. **Create** `docs/adr/ADR-008-rekurrentnye-spisaniya-po-soglasiyu-podpiski-sbp.md` — the main architectural decision.
2. **Create** `docs/spec/consent-state-machine.md` (or extend state-machine.md) — consent + debit state machine.
3. **Modify** `docs/contracts/tsp-api.md` — add consent/debit endpoints + webhooks.
4. **Modify** `openapi/tsp-api.yaml` — additive endpoints/schemas.
5. **Modify** `docs/nfr.md` — add NFR rows for recurring.
6. **Modify** `ARCHITECTURE-SPINE.md` — add AD-009 (recurring) as Proposed, or extend existing; update Deferred (remove "автоплатежи" from roadmap/out-of-scope note in solutioning).
7. **Create** a top-level solutioning/design doc for the feature (e.g., `docs/solutioning-recurring.md`) OR extend `docs/solutioning.md`. Given solutioning.md is already large, a separate `docs/solutioning-recurring.md` is cleaner. Actually, maybe I'll create a single "пакет" summary doc that ties everything together, or just rely on the ADR + spec + contracts + nfr changes.

Hmm, but actually — let me reconsider scope. The user wants a "архитектурный пакет" (architectural package). This is a cohesive deliverable. The 7 items they listed map to specific artifacts. Let me map:

1. Оценка значимости + маршрут → a section (maybe in the ADR or a separate "route" doc / top of the package).
2. Влияние на принятую архитектуру → section in ADR (impact analysis) + spine changes.
3. Архитектурное решение + альтернативы + последствия + обратимость → the ADR itself.
4. Изменения контрактов → contracts/tsp-api.md + openapi.
5. NFR → nfr.md.
6. Критерии приёмки + план отката → in ADR (acceptance criteria + rollback) + maybe a dedicated section.
7. Что остаётся на человека → in ADR (open questions / deferred decisions).

So the core deliverable is the ADR (which in this repo carries Decision + Alternatives + Consequences + Reversibility + References), plus supporting docs (spec, contracts, nfr), plus spine update.

I think the package = ADR-008 + consent state machine spec + contract changes + NFR + spine update. That's cohesive and follows repo conventions.

Now, should I also update `docs/solutioning.md`? The solutioning.md has a "Roadmap (вне scope): ... автоплатежи." I should update this to reflect that автоплатежи/подписки are now being brought in scope (as a new feature). But modifying solutioning.md is a bit heavy. I'll add a note/pointer. Actually, I think I'll leave solutioning.md mostly alone and add a pointer to the new feature package, OR create a `docs/solutioning-recurring.md` that's the "full design" for this feature (mirroring solutioning.md's role).

Hmm, this is getting complex. Let me simplify and decide the concrete artifact set:

Given the user's 7 deliverables and the repo's structure, I'll produce:

**A. `docs/adr/ADR-008-rekurrentnye-spisaniya-po-soglasiyu-podpiski-sbp.md`** — the core ADR containing:
- Route/significance assessment (deliverable 1)
- Impact on invariants (deliverable 2)
- Decision + alternatives + consequences + reversibility (deliverable 3)
- Acceptance criteria + rollback (deliverable 6)
- What remains for human (deliverable 7)

Actually, the ADR might get too big if I cram everything. But the repo's ADRs are already substantial. Alternatively, I split: ADR-008 (the decision) + a "solutioning-recurring" doc (route + impact + full design + acceptance + rollback).

Let me look at how the repo separates concerns:
- solutioning.md = full design (components, flows, gates, NFR summary, rollback, gaps)
- ADRs = individual decisions
- spec/ = formal specs (state machine, contracts)
- nfr.md = NFR
- contracts/ = API contracts

So the "package" for a new feature, following this structure, would be:
- `docs/adr/ADR-008-*.md` — the decision (with alternatives, consequences, reversibility)
- `docs/spec/consent-state-machine.md` — consent/debit state machine
- `docs/contracts/tsp-api.md` (extend) + `openapi/tsp-api.yaml` (extend) — contract changes
- `docs/nfr.md` (extend) — NFR
- `ARCHITECTURE-SPINE.md` (extend: new AD + Deferred update)
- A solutioning doc for the feature OR a top-level "пакет" summary.

I think I'll create ONE comprehensive "solutioning" doc for the feature: `docs/solutioning-recurring.md` (or `docs/spec/recurring-sbp.md`), which is the "пакет" that ties together: route/significance, impact on invariants, the decision summary (pointing to ADR-008), contract changes, NFR, acceptance criteria, rollback, human decisions. Plus the ADR-008 as the formal decision artifact.

Actually, to keep it clean and avoid over-engineering, let me do this:

1. `docs/adr/ADR-008-rekurrentnye-spisaniya-po-soglasiyu-podpiski-sbp.md` — formal ADR (decision + alternatives + consequences + reversibility + references). This is the heart of deliverable #3.
2. `docs/solutioning-recurring.md` — the "пакет" document: route/significance (#1), impact on invariants (#2), full design (components, flows, consent state machine), contract changes summary (#4), NFR (#5), acceptance criteria + rollback (#6), human decisions (#7). This ties everything together.
3. `docs/spec/consent-state-machine.md` — formal consent + debit state machine spec (referenced by ADR-008 and solutioning).
4. Modify `docs/contracts/tsp-api.md` — add §8 (consents) + §9 (debits) + webhooks.
5. Modify `openapi/tsp-api.yaml` — add /v1/consents, /v1/consents/{id}, /v1/debits (or /v1/consents/{id}/debits), schemas, webhook event enums.
6. Modify `docs/nfr.md` — add section 7 "Рекуррентные списания (подписки)".
7. Modify `ARCHITECTURE-SPINE.md` — add AD-009 (Proposed) + update Deferred (автоплатежи moved from roadmap-out-of-scope).

Wait, but I need to be careful about scope creep. That's 7 files. Is that too much? The user asked for a comprehensive package with 7 deliverables, so 6-7 files is reasonable. But let me consolidate where sensible.

Actually, let me reconsider whether to modify ARCHITECTURE-SPINE.md. The spine currently has AD-001..AD-008. The recurring feature's core invariant (consent-based debit only from active consent, no debit after revocation, credit only from PAID) could be a new AD-009. But adding to the spine is a significant action — the spine is "the invariants." The user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The spine has a clear pattern (AD-XXX with Status: Proposed/Adopted, Binds, Prevents, Rule). So adding AD-009 following that pattern is "the accepted way."

But I should be careful: AD-009 would be "Proposed (ADR-008)" — proposed until ratified. This is consistent with how AD-001..007 are "Proposed (ADR-XXX)".

Also, the spine's "Deferred" section doesn't currently list "автоплатежи" explicitly (it lists мультивалютность, C2C/выплаты, диспуты). But solutioning.md §1 lists "автоплатежи" in the roadmap (out of scope). So I should update solutioning.md to note that автоплатежи/подписки are now being brought into scope as a new feature. Actually, I'll note this in the new solutioning-recurring.md and maybe add a pointer in solutioning.md. Hmm, or just update solutioning.md's roadmap line.

Let me simplify my final plan and be decisive. I'll produce these artifacts:

**Created (new):**
1. `docs/adr/ADR-008-rekurrentnye-spisaniya-po-soglasiyu-podpiski-sbp.md`
2. `docs/solutioning-recurring.md` (the full package doc tying everything together — route, impact, design, acceptance, rollback, human decisions)
3. `docs/spec/consent-state-machine.md`

**Modified:**
4. `docs/contracts/tsp-api.md` (add consent + debit sections + webhooks)
5. `openapi/tsp-api.yaml` (add consent + debit paths/schemas)
6. `docs/nfr.md` (add recurring NFR section)
7. `ARCHITECTURE-SPINE.md` (add AD-009 Proposed + note in Deferred)

Maybe also:
8. `docs/solutioning.md` (update roadmap to reflect автоплатежи brought in scope) — small edit.

That's a solid, cohesive package. 7-8 files.

Actually, I realize I should reconsider whether to create `docs/solutioning-recurring.md` as a separate file vs. integrate. The user asked for "архитектурный пакет" — a package. A single entry-point document that summarizes the whole package (like a "solutioning" doc) plus the detailed artifacts (ADR, spec, contracts, NFR) is exactly right. The repo's solutioning.md is the entry point for the base solution. So a parallel `solutioning-recurring.md` is the entry point for this change. Good.

Now, before writing, I need to resolve the load-bearing questions. Let me make my final call on whether to ask.

Given:
1. The brainstorming skill mandates understanding before design.
2. There are 2 genuinely load-bearing forks.
3. But the user wants a package and listed "what remains for human architect" as a deliverable.

I'll ask the 2 load-bearing questions via ask_user_question. This is the professional move and aligns with the skill. If the user picks the recommended options (pull + СБП-native consent), I'll proceed confidently. If they pick something else, I'll adapt.

Let me also reflect my understanding first (briefly) in the same message before/after the questions. Actually, the ask_user_question tool is a single tool call; I can write a brief understanding note in my text before calling it.

Let me formulate my understanding note + questions.

Understanding note (concise):
- Change: add recurring C2B debits by payer consent (СБП-подписки) on top of the accepted C2B-приём gateway.
- Scope: consent lifecycle + debit-by-consent + refunds-of-debits + webhooks + NFR, reusing gateway/state-machine/adapter/ABS/trust-zones.
- Constraints: no code, don't break invariants AD-001..008, don't break existing TSP consumers, protocol details [ТРЕБУЕТ ПРОВЕРКИ], follow repo methodology (ADR format, spine, contracts, NFR).
- Success: package ready for architectural decision (A3-style human decision) and handoff to implementers.

Then ask:
Q1: Trigger model (pull vs push vs both).
Q2: Consent acquisition (СБП-native vs ТСП-direct vs both).

Actually, I want to also consider a Q3 about whether they want me to write files directly or present the design first. But the user already said "перечисли созданные и изменённые файлы", implying files. So no Q3.

Let me also think: is Q2 actually load-bearing enough, or is the СБП-native model essentially forced by the domain (as I recalled)? The СБП subscription standard does go through the payer's bank. But there might also be a "ТСП регистрирует согласие напрямую" model in some implementations. Given the repo's [ТРЕБУЕТ ПРОВЕРКИ] discipline, the exact consent flow is partly an open question. But the architectural question is: does our gateway need to support (a) initiating a consent request that redirects to the payer's bank (like QR), and (b) receiving consent status/revocation events from НСПК? This is almost certainly yes for СБП-native. And "ТСП-direct" would be a simpler registration.

I think Q2 is worth asking because it affects the API surface significantly (consent request initiation vs passive consent registration).

OK let me finalize and ask. I'll present a brief understanding + 2 questions.

Actually, let me reconsider the number of questions and their framing to be maximally useful. Let me make them multiple-choice with clear recommendations.

Let me write the understanding note and then call ask_user_question.

One more consideration: The brainstorming skill says "Classify first, announce the path" — I already announced architectural. Good. And "write back your understanding... separate what they said from assumptions... invite correction."

I'll do a concise write-back + 2 questions. Let me keep the write-back tight.

Let me now also double-check: am I confident about the СБП domain facts enough to present them? I'll present domain facts with appropriate hedging ([ТРЕБУЕТ ПРОВЕРКИ] for protocol-level), consistent with the repo. I'm confident that:
- Recurring СБП requires payer consent (согласие).
- Consent has params: max amount, validity, (frequency limit), scope.
- Payer can revoke at any time.
- No debit after revocation.
These are solid and I can state them.

Let me proceed to ask.

Actually, hold on. Let me reconsider whether asking questions is even the right call given the user's very clear directive and roleplay framing. The user is a "solution-архитектор банка" giving me a task with a specific output spec. They might expect me to just DO it, making expert decisions and flagging open items (deliverable #7 explicitly covers "what remains for human").

Re-reading the user's message: "Подготовь архитектурный пакет этого изменения... Что должно получиться: 1...2...7. Что остаётся на решение человека-архитектора и почему."

The user is literally telling me to include "what remains for the human architect" as a deliverable. This means they EXPECT me to make the architectural decisions (with alternatives) and flag what's genuinely open. They're NOT expecting me to ask them clarifying questions first — they want the package.

This tips me toward: DON'T block on questions. Instead, make well-justified recommendations for the forks (in the ADR as "Decision" with "Alternatives Considered"), and put genuinely business-level forks into "what remains for human."

But the brainstorming skill... ugh. Let me weigh: the skill is guidance; the user's explicit instruction takes precedence ("User instructions ... direct requests) take precedence over skills"). The user's direct request is to produce the package with 7 deliverables including "what remains for human." This is a strong signal that they want me to proceed and make decisions, flagging open items.

Also, the skill's HARD GATE says for architectural: "the human partner reviews and approves the written spec." So even if I don't ask questions upfront, I should present the package for review before it's "final." The user reviewing the written package IS the approval gate.

So my final approach:
1. Do NOT block on ask_user_question (the user wants the package; forks go into ADR alternatives + human-decision list).
2. Make expert, well-justified recommendations for each fork.
3. Produce the full package (files).
4. Present it for review (the brainstorming skill's "user reviews written spec" gate), explicitly noting the decision points that remain for the human architect (deliverable #7).

Wait, but is there any fork where I truly CANNOT make a reasonable recommendation and a wrong assumption would waste all my work? Let me check:
- Trigger model: I can recommend "pull (ТСП triggers), gateway passive executor" strongly — it's the lowest-risk, most-compatible, and consistent with the gateway being a passive executor (no scheduler today). The "push/scheduler" is a clear alternative I can describe and defer. This is a solid recommendation.
- Consent model: I can recommend "СБП-native (consent via payer's bank, reference via adapter)" strongly, with "ТСП-direct registration" as an alternative. This is solid.

Both have clear, defensible recommendations. No fatal ambiguity. So I can proceed without blocking.

This is the right call. The user gave a directive to produce a package; I'll produce it with expert decisions and clearly flag open items.

Actually, let me reconsider one more time, because I keep flip-flopping. The key deciding factor: the brainstorming skill's "discover intent → ask what's missing." But the user has given intent AND the deliverable structure. The forks (trigger, consent) are DESIGN decisions, not INTENT questions. The intent is clear: "рекуррентные C2B-списания по согласию." The design decisions are exactly what an ADR captures (decision + alternatives). So asking "who triggers" is really asking the user to make the ADR decision for me — but the user asked ME to prepare the ADR (with alternatives + recommendation). 

Therefore: proceed with expert recommendations, flag human decisions. This is consistent with both the user's intent and the skill (the written spec goes to user review at the end).

Decision made. I'll proceed to write the package.

Now let me also decide: should I present a design plan in chat first and get approval, or write files directly? The skill's architectural path says "present design sections, get approval after each section, then write spec doc." But that's for interactive co-design. The user's directive + "list created files" suggests they want files produced now.

I'll take a middle path: I'll write the package files (since the user explicitly asked for a package and to list created files), then in my final message present a concise summary + the key decision points for review. The user can then request changes (the "user reviews written spec" gate). This is efficient and honors the user's directive while still leaving room for review.

Actually, wait — let me reconsider the "present design, get approval before writing" gate more carefully, because the skill is emphatic ("Approval of an idea or feature scope does not approve artifacts that do not exist yet... Resume at the earliest incomplete stage").

But the user's instruction is to "prepare the package" and "list created files when done." This is a direct instruction to create files. The skill itself says user instructions take precedence over skills. So creating files is what the user wants.

However, I should still be careful to present the design clearly and invite correction. I'll write the files, then in my final summary clearly present the key decisions and ask for review, noting what's still open for the human architect.

Let me now also settle a few design specifics before writing:

### Design specifics

**Feature name**: "Рекуррентные C2B-списания по согласию (подписки СБП)".

**Route/significance**: 
- Similar to base C2B: Critical. Significance: high (new financial capability, new entity (consent) with ПДн, new НСПК integration surface, regulatory (161-ФЗ/152-ФЗ/115-ФЗ), affects existing gateway). I'd rate maybe 10-11/15 (slightly lower than base since it reuses foundation, but still Critical because: recurring debits without payer action = higher fraud/abuse risk, more ПДн (payer identifiers, consent params), new adapter contract surface, and it touches the payment state machine that's already accepted).
- Route: architectural (deep design needed) — because it (a) extends the accepted payment state machine, (b) adds a new entity with its own lifecycle, (c) changes the internal adapter contract (vendor must support it), (d) changes the TSP API contract (backward compat), (e) has regulatory/compliance implications.

**Impact on invariants (AD-001..008)**:
- AD-001 (изоляция контура): **не меняется** — consent/debit logic stays in gateway.
- AD-002 (единый источник истины — статусная машина): **расширяется** — новый автомат для consent + обобщение платёжного автомата (или отдельный debit-автомат). Rule (atomic status+outbox) unchanged; scope of "entities" grows.
- AD-003 (идемпотентность): **не меняется** (rule) but **расширяются ключи**: consentId, debit reference; повторное списание с тем же reference — идемпотентно.
- AD-004 (единственный адаптер ОПКЦ): **не меняется** (rule) but **контракт адаптера расширяется**: новые операции (registerConsent, revokeConsent, initiateDebit, события consent.*/debit.*).
- AD-005 (зачисление только из PAID): **не меняется** — debit-платёж тоже зачисляется только из PAID.
- AD-006 (trust-зоны): **не меняется**.
- AD-007 (НПС/КИИ/ПДн): **усиливается/расширяется** — consent хранит идентификатор плательщика и параметры согласия (ПДн), новые регуляторные требования к согласию (макс. сумма, срок, отзыв), 115-ФЗ мониторинг серии списаний.
- AD-008 (гибрид): **не меняется** (strategy) but **обязательства вендора расширяются**: адаптер должен поддерживать consent/debit-операции и их идемпотентность.

**New invariant AD-009** (proposed):
- **AD-009. Списание только по активному согласию.** Rule: Дебит по согласию возможен только при согласии в состоянии ACTIVE (не отозвано, не истекло, не превышен лимит/частота). Списание после отзыва/истечения — невозможно. Каждое списание проверяет параметры согласия (макс. сумма, период действия, частота). Prevents: несанкционированные списания, списание после отзыва (регуляторный риск). Binds: consent-автомат, статусная машина платежа, адаптер ОПКЦ, антифрод/AML.

This is a strong new invariant. I'll add it as AD-009 (Status: Proposed, ADR-008).

**Payment state machine impact**: 
- The existing machine: CREATED → QR_ISSUED → PAID → CREDITED → COMPLETED (+ FAILED/EXPIRED/REFUNDED).
- For consent debits, there's no QR. So the machine needs to either:
  (a) generalize QR_ISSUED → a more generic "instrument ready" state, or
  (b) allow a consent-debit to go CREATED → PAID (skipping QR_ISSUED), where "CREATED" = debit registered, and PAID = НСПК confirmed the debit.
  
  I'll propose: keep the same canonical states but add a new payment `initiationType` field (`QR` | `CONSENT`). For `CONSENT`, the machine goes CREATED → PAID (no QR_ISSUED), with an intermediate technical state `DEBIT_PENDING` (debit sent to НСПК, awaiting confirmation). The `QR_ISSUED` state is specific to `QR` initiation. The invariants (credit only from PAID, idempotency, atomic transitions) hold unchanged.

  Actually, cleaner: introduce the debit as its own resource type that shares the payment state machine's "financial core" but has a distinct initiation. But to minimize disruption, I'll model debits as payments with `initiationType: CONSENT` and `consentId`, reusing the same machine with a note that `QR_ISSUED` is skipped for CONSENT.

  Hmm, but the repo's state machine is explicitly QR-centric (QR_ISSUED is a canonical financial state visible to ТСП). Adding a second initiation path means the ТСП-facing status enum for debits would be: CREATED → PAID → CREDITED → COMPLETED (no QR_ISSUED), or a new enum.

  I think the cleanest architectural answer is:
  - **Consent** gets its own state machine (new spec file): ACTIVE → REVOKED / EXPIRED / SUSPENDED (with params).
  - **Debit** (списание) reuses the payment state machine, but with `initiationType=CONSENT` and no `QR_ISSUED` state; the debit's lifecycle is CREATED → PAID → CREDITED → COMPLETED (or FAILED). This is a *generalization* of the payment machine, flagged as such.

  I'll document this in the consent-state-machine.md spec and in the ADR (impact section).

**Contract changes (tsp-api + openapi)** — backward compatible, additive:
- New resource `/v1/consents`:
  - `POST /v1/consents` — initiate consent request (ТСП → gateway; gateway → adapter → НСПК → payer's bank). Idempotency-Key required. Body: tspId, payer reference (masked/minimal), maxAmount, currency, validity (validUntil), frequency limit, purpose. Response: consentId, status (PENDING_APPROVAL → ACTIVE), consentUrl (redirect for payer, if applicable).
  - `GET /v1/consents/{consentId}` — consent status.
  - `POST /v1/consents/{consentId}/revoke` — revoke consent (ТСП-initiated) OR just rely on НСПК events.
- New debit initiation:
  - Option A: `POST /v1/debits` (new endpoint) — body: consentId, amount, currency, merchantOrderId, Idempotency-Key. Response: debitId (= paymentId), status.
  - Option B: extend `POST /v1/payments` with optional `consentId` and `initiationType`. 
  
  I'll go with a new `POST /v1/consents/{consentId}/debits` endpoint (nested under consent) OR a top-level `POST /v1/debits`. To keep it clean and explicit, I'll propose `POST /v1/debits` as a sibling to `/v1/payments`, with the debit sharing the payment model (debitId is the paymentId). Actually, simplest and clearest for consumers: `POST /v1/debits` returning a `Debit` resource that reuses `Payment` schema fields + `consentId` + `initiationType`.

  Actually, re-examining: to minimize new top-level concepts and maximize reuse, I'll extend `POST /v1/payments` with optional `consentId` (additive, backward-compatible — the repo's own policy allows optional fields without version bump), and add the `consent` resource for the consent lifecycle. A debit IS a payment (same money-movement, same status machine minus QR). This is the cleanest.

  So:
  - Extend `PaymentRequest` with optional `initiationType: "QR" | "CONSENT"` (default "QR" for backward compat) and `consentId` (required when initiationType=CONSENT). Additive → no break.
  - Add `Payment` fields: `initiationType`, `consentId` (optional).
  - New `Consent` resource + endpoints.
  - New webhook events: `consent.activated`, `consent.revoked`, `consent.expired` (+ existing `payment.completed` etc. reused for debits).

  Wait, but there's a subtlety with backward compatibility: adding `initiationType` with default "QR" means existing consumers (who don't send it) still get QR behavior. Good. And `consentId` optional. Good. This is clean and additive.

  But should debits be a separate endpoint? The argument for separate endpoint: semantic clarity (a debit is conceptually different from a QR payment), avoids overloading /v1/payments. The argument for extending /v1/payments: reuse, less new surface, "a debit is a payment." 

  I'll recommend: **extend `/v1/payments`** with `initiationType`+`consentId` (additive), because it reuses the whole payment status/refund/idempotency machinery and the repo's own state machine treats "payment" as the core entity. I'll note the alternative (separate `/v1/debits`) in the ADR as considered-and-rejected. This is the cleaner, DRYer choice and matches the repo's "payment is the core entity" philosophy.

  Hmm, but actually there's a good argument that a "debit" is a distinct resource because it's bound to a consent (nested lifecycle) and has different validations. But the money-movement and settlement are identical to a payment. I'll go with extending /v1/payments and clearly document it. The consent resource is separate.

**NFR (new)**:
- Consent registration latency p95 < 1s (excluding НСПК).
- Consent status propagation (revocation) p95 < 5s from НСПК event.
- Debit-by-consent: latency p95 < 500ms (gateway, excluding НСПК/АБС), debit confirmation p95 < 60s.
- No debit after revocation: 0 (hard invariant, fitness test).
- No double debit: 0 (idempotency by consent debit reference).
- Limits enforcement: 100% (max amount, frequency, validity enforced before debit).
- Consent/ПДн: minimize storage, encryption, masking.
- Availability same as gateway (99.95%).
- Throughput: recurring debits add load; sustained +50 TPS headroom (or a separate target).
- Reconcile: debit vs consent state, hourly.

**Acceptance criteria + rollback**:
- Feature flag per ТСП (enable/disable subscription capability).
- Acceptance: consent create/activate/revoke flows, debit happy path, no-debit-after-revoke, idempotent repeat debit, limit enforcement, webhooks, reconcile, NFR thresholds.
- Rollback: disable consent endpoints (stop-new), stop any scheduler (none if pull), existing debits/consents remain queryable, no data migration back. Feature flag off = full revert of the capability without affecting QR payments. "Stop-new debits" without stopping QR.

**Human decisions (deliverable #7)**:
- Regulatory/legal: consent ПДн retention, 152-ФЗ basis, AML thresholds for recurring series.
- НСПК protocol details [ТРЕБУЕТ ПРОВЕРКИ]: exact consent flow, fields, whether consent is created via payer bank redirect vs ТСП registration, max amount/frequency semantics.
- Business: tariffs/commissions for subscriptions, whether "push/scheduler" is needed later.
- Whether to ratify as new initiative (parent spine change) vs feature extension — escalate to parent spine owner.
- Vendor RFP: does the chosen transport adapter support consent/debit operations (extends ADR-007 constraints).

OK. I have a complete design. Now let me write the files.

Let me be careful about a few constraints:
1. CONSTRAINTS.yaml fitness: `adr-no-placeholders` — no `<!--` in docs/adr/*.md. So in my new ADR, I must NOT use HTML comments. The existing ADRs don't use `<!--` (they use markdown). But note the existing ADRs DO use `[ТРЕБУЕТ ПРОВЕРКИ]` markers (not comments). I'll use the same.
   Also `nfr-measurable`: docs/nfr.md must contain '99,95' — I'll preserve that (and my additions won't remove it).
   `abs-credit-only-from-paid`: ADR-005 must contain 'только из состояния `PAID`' — I'm NOT editing ADR-005, so fine.
   `adr-set-complete`: docs/adr/ADR-001-outbox.md must exist — I'm not deleting it.

2. The `docs/nfr.md` currently has '99,95' in section 1. I'll preserve it.

3. OpenAPI 3.0.3 — I'll add paths/schemas additively.

4. The repo marks "Status: Proposed" for ADRs and spine ADs that await ratification. My new ADR-008 will be "Status: Proposed", and AD-009 "Status: Proposed (ADR-008)".

5. Today's date: 2026-09-28 (per system reminder). I'll use this date for the new ADR and spec.

Wait — the existing docs use "2026-08-15". Today is 2026-09-28. So new files dated 2026-09-28.

6. Versioning: the TSP API contract is "v0.1 draft". I'll bump to reflect additive changes, keeping /v1 path. I'll note version 0.2-draft or keep 0.1 with "additive changes" note. Actually, since these are additive and backward-compatible, I'll keep /v1 and note "v0.1 → v0.2 (additive)" in the doc header. For openapi info.version, bump 0.1.0 → 0.2.0 (additive). Actually, additive changes don't require a new MAJOR path version; a minor bump is fine. I'll set info.version to 0.2.0.

Let me now write the files. I'll write them one by one, being thorough but concise.

Let me start with the ADR-008 (the core decision).

Actually, let me reconsider the order and content to avoid duplication. I'll write:
1. ADR-008 (core decision) — includes: Context, Decision (consent entity + state machine + debit-by-consent via /v1/payments extension + adapter contract extension + AD-009), Alternatives, Consequences, Reversibility, References. Plus a brief "impact on invariants" section? The ADR format doesn't have an "impact" section, but I can add it in Context or as a subsection. Actually, the repo's ADRs don't have an explicit "impact on AD-XXX" section, but the "Related" field lists spine ADs. I'll add impact detail in the solutioning-recurring.md (deliverable #2) rather than bloating the ADR.

2. solutioning-recurring.md — the full package: route/significance (#1), impact on invariants (#2), summary of decision (pointer to ADR-008), design (components/flows), contract changes summary (#4), NFR summary (#5, pointer to nfr.md), acceptance criteria + rollback (#6), human decisions (#7).

3. consent-state-machine.md — formal spec of consent + debit states.

4. contracts/tsp-api.md — add sections.

5. openapi/tsp-api.yaml — add paths/schemas.

6. nfr.md — add section.

7. ARCHITECTURE-SPINE.md — add AD-009 + Deferred update.

8. (maybe) solutioning.md — update roadmap line to note автоплатежи in scope.

Let me write these now. I'll be efficient.

First, let me draft the ADR-008 content.

Actually, I want to reconsider whether the "debit" should reuse /v1/payments or be a separate /v1/debits. Let me think about backward compatibility more carefully.

The existing /v1/payments POST creates a QR payment. Its `PaymentRequest` currently (in openapi) has required [amount, merchantOrderId]. The docs/contracts version has more fields (tspId, currency, qrType, paymentPurpose, ttlSeconds, redirectUrl, merchantOrderId).

For consent debits, I add `initiationType` (default "QR") and `consentId`. This is purely additive. Existing consumers send no `initiationType` → default "QR" → identical behavior. 

But there's a semantic subtlety: for a consent debit, the response should NOT have `qrId`/`qrUrl` (no QR). So the `Payment` response schema would have those fields as optional/null for consent debits. That's fine (optional fields).

I think reusing /v1/payments is clean and I'll recommend it, but also add a dedicated consent resource. Let me also consider adding a convenience endpoint `POST /v1/consents/{consentId}/debits` that wraps the payment creation — actually, no, keep it simple: /v1/payments with consentId. One endpoint, one code path, full reuse of idempotency/status/refund.

Hmm, but actually, re-reading the repo, refunds are `POST /v1/payments/{paymentId}/refunds`. So a debit refund would naturally be `POST /v1/payments/{debitId}/refunds` — reusing the same. Clean.

OK, final: extend /v1/payments with `initiationType` + `consentId`; add /v1/consents resource. Document the alternative (separate /v1/debits) as rejected.

Let me write everything now.

Let me write the ADR first.

For the ADR filename, follow the repo's naming: kebab-case, descriptive. `ADR-008-rekurrentnye-spisaniya-po-soglasiyu-podpiski-sbp.md`.

Let me draft it fully.

I need to be careful about length — the repo ADRs are ~1.5-2.5 pages. I'll aim for similar.

Let me write.

Actually, I realize I should double-check: does the CONSTRAINTS.yaml `adr-no-placeholders` rule (must_not_contain '<!--') apply to my new ADR? Yes, glob "docs/adr/*.md". So no HTML comments. Good, I won't use any.

Also `spine-lints-clean`: ARCHITECTURE-SPINE.md must_not_contain 'TODO|TBD|XXX'. So when I edit the spine, no TODO/TBD/XXX. The existing spine uses `[ТРЕБУЕТ ПРОВЕРКИ]` which is fine. I'll avoid TODO/TBD/XXX.

Now let me write all files. I'll start.

Let me write ADR-008.

Content plan for ADR-008:

# ADR-008. Рекуррентные C2B-списания по согласию (подписки СБП)

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур) + бизнес/продукт «Подписки»
- Related: ADR-002, ADR-004, ADR-005, AD-002, AD-003, AD-005, AD-007 (и новый AD-009)

## Context
[Business need: ТСП — кинотеатры, ЖКХ, связь — хотят рекуррентные списания по согласию. Сейчас каждый платёж = QR + действие клиента. Подписки требуют: согласие плательщика, затем списания без активного действия клиента.]

[Domain: согласие — новый объект с параметрами (макс. сумма, срок действия, частота), отзыв в любой момент; списание по согласию — новый тип инициации платежа (без QR). Детали протокола НСПК — [ТРЕБУЕТ ПРОВЕРКИ].]

[Forces: нельзя сломать существующий C2B-приём и потребителей API; инварианты AD-001..008 остаются; риск несанкционированных списаний; регуляторика (161-ФЗ, 152-ФЗ, 115-ФЗ).]

## Decision
1. **Согласие — отдельный объект** с собственным конечным автоматом (ACTIVE/EXPIRED/REVOKED/SUSPENDED + PENDING_APPROVAL) и неизменяемыми параметрами.
2. **Списание по согласию — тот же платёж**, что и QR, с `initiationType=CONSENT` и ссылкой `consentId`; тот же статусный автомат (без `QR_ISSUED`), те же идемпотентность/зачисление-из-PAID/возвраты.
3. **Новый spine-инвариант AD-009**: списание только по активному согласию; проверка лимитов перед списанием; списание после отзыва невозможно.
4. **Адаптер ОПКЦ расширяется** операциями согласия (register/revoke + события consent.*) — контракт-независимость ядра сохраняется (AD-008).
5. **ТСП инициирует каждое списание (pull)**; планировщик подписок остаётся на стороне ТСП (шлюз — пассивный исполнитель). Gateway-планировщик — deferred.
6. **Контракт API ТСП расширяется аддитивно**: /v1/consents (новый ресурс) + опциональные поля в /v1/payments; без изменения существующих методов.

## Alternatives Considered
- Отдельный ресурс /v1/debits (плюс: семантическая ясность; минус: дублирование статус/рефанд/идемпотентность — отвергнут)
- Gateway-планировщик подписок (push) (плюс: сервис под ключ; минус: сложность, ответственность за расписания, новые NFR — deferred)
- Согласие как свойство платежа без отдельного автомата (плюс: просто; минус: нет lifecycle согласия, нельзя управлять отзывом/лимитами — отвергнут)
- Хранить полные ПДн плательщика (плюс: аналитика; минус: 152-ФЗ, поверхность атаки — отвергнут)

## Consequences
Positive / Negative.

## Reversibility
[feature-flag; consent entity additive; no data migration back; adapter contract additive but vendor-dependent]

## References

Good. Let me write it out in full now.

Now let me actually write all the files. I'll do it in a sequence of write_file/edit calls. Since write_file requires knowing existing content (for edits I use edit, for new files I use write_file — but I must read first if it might exist; for NEW files I know they don't exist based on glob). Actually write_file says "you MUST use read_file first; if file does not exist, then create it" — but for new files I've already established via glob that they don't exist (ADR-008, consent-state-machine, solutioning-recurring). So I can write_file directly.

For modifications to existing files (contracts/tsp-api.md, openapi/tsp-api.yaml, nfr.md, ARCHITECTURE-SPINE.md, solutioning.md), I'll use edit (I've already read all of them).

Let me write the new files first, then edit existing.

Let me write ADR-008.

Actually, let me reconsider the pull vs push one more time for the recommendation, because I want the recommendation to be defensible and clearly the "right" default. For "онлайн-кинотеатры, ЖКХ, связь":
- Онлайн-кинотеатры: monthly subscription → merchant billing triggers monthly charge.
- Связь (telecom): monthly billing cycle → merchant triggers.
- ЖКХ: monthly utility → merchant triggers (or via a "автоплатёж" where amount varies).

All three are "merchant triggers the charge on their schedule" = pull. The gateway providing "debit by consent" is exactly the primitive. Push/scheduler would require the gateway to hold billing schedules, which is the merchant's domain (pricing, plan changes, dunning). So pull is clearly correct for MVP; push is a roadmap item. Solid.

Now, one more subtlety: the СБП subscription mechanism — does the consent itself encode a schedule/frequency (e.g., "1 списание в месяц")? In СБП, the consent has parameters including **периодичность** (frequency) and **максимальная сумма**, and the debit must respect these. But the *trigger* (who fires at time T) is still the ТСП. The consent's frequency limit is a *guard* (enforced by payer's bank / НСПК), not a scheduler. So the gateway must also enforce/check frequency limits (defense in depth) before initiating, even though the ТСП triggers. This is consistent with AD-009 (limit enforcement). Good.

Let me write everything now. I'll be thorough.

Let me write the files in a batch where possible. write_file calls are independent (new files), but edits to existing files are also independent of the new files. However, I need to make sure edits have correct old_string. I've read all the target files, so I have their content.

Let me write new files first (3 write_file in parallel), then do edits (edit calls). Actually, I can do them somewhat in parallel, but edits depend on me having the exact current content (which I do). Let me do the 3 new files in parallel first, then the edits.

Actually, to be safe and since they're all independent, I'll batch the 3 write_file calls in one message, then batch the edits in subsequent messages.

Let me draft the content carefully.

---

**File 1: docs/adr/ADR-008-rekurrentnye-spisaniya-po-soglasiyu-podpiski-sbp.md**

Let me write full content.

---

**File 2: docs/solutioning-recurring.md**

This is the "пакет" entry doc. It should map to the 7 deliverables clearly.

---

**File 3: docs/spec/consent-state-machine.md**

Consent + debit state machine.

---

Then edits.

Let me write.

I'll write the ADR now with full detail.

Let me carefully compose. I need good Russian technical writing matching the repo's style.

For ADR-008:

```markdown
# ADR-008. Рекуррентные C2B-списания по согласию плательщика (подписки СБП)

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур) + бизнес/продукт «Подписки и автоплатежи»
- Related: ADR-002, ADR-004, ADR-005, AD-002, AD-003, AD-005, AD-007, AD-009 (новый)

## Context

ТСП в целевых сегментах (онлайн-кинотеатры, ЖКХ, связь) требуют **рекуррентные C2B-списания по согласию плательщика** — «подписки СБП». Сейчас C2B-приём (ADR-001..007) заточен под единичную оплату: каждый платёж требует динамический/статический QR и явное действие плательщика. Для подписки это неприемлемо: списание должно происходить по заранее данному **согласию**, без активного действия клиента в момент оплаты.

Ключевая бизнес-семантика:
- **Согласие (consent/mandate)** — самостоятельный объект с параметрами: максимальная сумма (или фикс.), срок действия, периодичность/лимит частоты, сторона-получатель (ТСП). Плательщик может **отозвать** согласие в любой момент; после отзыва списание невозможно.
- **Списание по согласию** — новый тип инициации платежа: вместо QR платёж инициируется ссылкой на активное согласие.

Точный протокол НСПК для согласий/списаний (формат, порядок регистрации, где хранится согласие — банк плательщика/ОПКЦ, лимиты) — внешний вход, `[ТРЕБУЕТ ПРОВЕРКИ]` до получения документации НСПК.

Силы:
- **Не сломать** существующий C2B-приём и его потребителей: контракт API ТСП v0.1 должен расширяться аддитивно.
- Инварианты AD-001..AD-008 остаются в силе; списание по согласию обязано проходить ту же дисциплину (идемпотентность, зачисление только из `PAID`, единый адаптер ОПКЦ, trust-зоны, аудит).
- Повышенный риск несанкционированных списаний: «платёж без действия клиента» ужесточает требования к согласию, лимитам и отзыву (161-ФЗ, 115-ФЗ) и добавляет ПДн плательщика (152-ФЗ).

## Decision

1. **Согласие — отдельный объект** с собственным конечным автоматом и неизменяемыми параметрами. Состояния: `PENDING_APPROVAL → ACTIVE`, терминальные `EXPIRED`, `REVOKED`, `SUSPENDED` (детализация — `docs/spec/consent-state-machine.md`). Согласие — источник истины для допустимости списания.

2. **Списание по согласию — это платёж.** Тот же статусный автомат, что у QR-платежа (ADR-002), с двумя отличиями: (а) `initiationType = CONSENT` вместо `QR`, (б) отсутствует состояние `QR_ISSUED` (нет QR) — путь `CREATED → PAID → CREDITED → COMPLETED` с техническим подсостоянием `DEBIT_PENDING` (списание отправлено в НСПК, ждём подтверждения). Зачисление в АБС — по-прежнему только из `PAID` (AD-005); идемпотентность — по `Idempotency-Key` и `reference` списания (AD-003); возвраты — та же сага (ADR-005).

3. **Новый spine-инвариант AD-009 (Proposed)**: списание возможно только по согласию в `ACTIVE`; параметры согласия (максимум, срок, периодичность) проверяются **до** инициации списания; списание после отзыва/истечения невозможно; повторная доставка запроса списания не создаёт дубль.

4. **Адаптер ОПКЦ расширяется** (контракт `docs/contracts/opkc-adapter.md`, AD-004): операции `registerConsent`/`revokeConsent`/`initiateDebit` (или их эквивалент), события `consent.activated`/`consent.revoked`/`consent.expired`, `debit.*`; ядро остаётся контрактно-независимым от протокола НСПК (AD-008). Идемпотентность мутирующих операций по `reference` обязательна для вендора (расширение требований RFP).

5. **ТСП инициирует каждое списание (pull-модель).** Шлюз — пассивный исполнитель списания по согласию; расписание и dunning — зона ТСП. Планировщик подписок на стороне шлюза — **deferred** (возврат при явном запросе бизнеса).

6. **Контракт API ТСП расширяется аддитивно** без смены мажорной версии: новый ресурс `/v1/consents` (создание запроса согласия, статус, отзыв) + опциональные поля `initiationType`/`consentId` в `POST /v1/payments` (обратно совместимо: отсутствие поля = `QR`). Вебхуки: добавляются `consent.activated`/`consent.revoked`/`consent.expired`; `payment.*` переиспользуется для списаний.

## Alternatives Considered

| Вариант | Плюсы | Минусы |
|---|---|---|
| Отдельный ресурс `/v1/debits` (не платёж) | Явная семантика «списание ≠ оплата по QR» | Дублирование статусной машины, возвратов, идемпотентности; рассинхрон с ADR-002; больше кода и тестов |
| Планировщик подписок на стороне шлюза (push) | «Подписка под ключ», монетизация сервиса | Ответственность за расписания/ретраи dunning; новые NFR и операционная нагрузка; дублирует billing-логику ТСП — YAGNI на старте |
| Согласие как атрибут платежа без отдельного автомата | Минимум сущностей | Нет жизненного цикла согласия: нельзя корректно обрабатывать отзыв/истечение/лимиты; списание «по умолчанию» без явного согласия — регуляторный риск |
| Хранить полный профиль плательщика (ФИО/телефон/привязка счёта) | Больше данных для аналитики и антифрода | Нарушение минимизации ПДн (152-ФЗ, AD-007); рост поверхности атаки; избыточно для сверки |

## Consequences

### Positive
- Повторное использование всего платёжного ядра (статусная машина, идемпотентность, АБС-интеграция, возвраты, сверка) — минимальное расширение, а не второй продукт.
- Явный жизненный цикл согласия даёт корректный отзыв и лимиты — регуляторная опора (161-ФЗ/115-ФЗ).
- Аддитивный контракт — существующие ТСП не замечают изменения.

### Negative
- Второй тип инициации усложняет статусную машину (ветка без `QR_ISSUED`) — нужны тесты на каждый переход и запрещённые переходы.
- Согласие — новый источник ПДн (идентификатор плательщика, параметры) → дополнительные требования ИБ/152-ФЗ (ADR-006/AD-007).
- Расширение контракта адаптера = новые обязательства вендора (и могут быть вне текущего RFP) → влияние на сроки (ADR-007).
- Риск «тихого» списания → обязательная интеграция с антифрод/AML на серии списаний.

## Reversibility

**reversible на уровне фичи.** Согласие и `initiationType=CONSENT` — аддитивные сущности: откат = выключение фиче-флага «подписки» (запрет новых согласий и списаний), существующие QR-платежи не затрагиваются. Миграции данных «назад» нет (согласия остаются в БД, но не используются). Обратимость дороже на стороне адаптера: если вендор не поддерживает согласия, это влияет на RFP (пересмотр ADR-007) — но не на уже принятое ядро.

## References

- AD-009 (spine, новый): списание только по активному согласию
- ADR-002 (статусная машина платежа), ADR-004 (нотификации/сверка), ADR-005 (АБС/возвраты)
- AD-003, AD-005, AD-007 (spine)
- `docs/spec/consent-state-machine.md` — спецификация согласия и списания
- `docs/solutioning-recurring.md` — полный пакет изменения (маршрут, влияние, приёмка, откат)
```

That's a solid ADR. Now the solutioning-recurring.md.

Actually, let me reconsider the "impact on invariants" — should it be a table in solutioning-recurring.md. Yes.

Let me write solutioning-recurring.md:

```markdown
# Solutioning — Рекуррентные C2B-списания по согласию (подписки СБП)

Надстройка поверх принятого решения «Платёжный шлюз СБП (C2B-приём)». Этот документ — пакет изменения для вынесения на архитектурное решение (A3) и последующей передачи исполнителям. Код не содержит.

- Дата: 2026-09-28
- Статус: Proposed (ожидает человеческого решения)
- Связано: ADR-008 (новый), ADR-002, ADR-004, ADR-005, AD-009 (новый)

## 1. Оценка значимости и маршрут (deliverable 1)

**Значимость: Critical** (оценка ~10/15). Ниже, чем у базового C2B-приёма (11/15), т.к. переиспользуется готовый фундамент (шлюз, статусная машина, адаптер, АБС, trust-зоны), но выше порога Architectural:
- финансовое влияние (новый способ списания средств клиента);
- новый объект с жизненным циклом (согласие) и новый тип инициации платежа;
- расширение контракта адаптера ОПКЦ (зависимость от вендора, ADR-007);
- регуляторный профиль: согласие и ПДн (161-ФЗ, 152-ФЗ, 115-ФЗ), риск несанкционированных списаний.

**Маршрут: глубокое проектирование (architectural).** Причины:
1. Затрагивает **принятую** статусную машину платежа (ADR-002) — нужно обобщение, а не новый изолированный код.
2. Добавляет сущность с собственным автоматом (согласие) — отдельная спецификация.
3. Меняет **контракт API ТСП** (аддитивно) и **внутренний контракт адаптера** — интерфейсы, на которые опираются потребители и вендор.
4. Вводит новый spine-инвариант (AD-009) — изменение архитектурного «позвоночника».

Без глубокого проектирования нельзя гарантировать инварианты «списание только по активному согласию» и «зачисление только из PAID» на новом типе инициации.

## 2. Влияние на принятую архитектуру (deliverable 2)

| Инвариант | Влияние |
|---|---|
| AD-001 Изоляция контура | **Без изменений** — логика согласий/списаний остаётся внутри шлюза |
| AD-002 Единый источник истины | **Расширяется** — Rule не меняется (атомарный переход + outbox + аудит), но появляется второй автомат (согласие) и второй тип инициации у платёжного автомата |
| AD-003 Идемпотентность | **Rule без изменений**; расширяются ключи: `consentId`, `reference` списания |
| AD-004 Единственный адаптер ОПКЦ | **Rule без изменений**; расширяется контракт адаптера (consent/debit-операции) |
| AD-005 Зачисление из PAID | **Без изменений** — списание тоже зачисляется только из `PAID` |
| AD-006 Trust-зоны | **Без изменений** |
| AD-007 НПС/КИИ/ПДн | **Усиливается** — новый ПДн-объект (согласие), новые требования к отзыву/лимитам, AML-мониторинг серий списаний |
| AD-008 Гибрид | **Rule без изменений**; расширяются обязательства вендора (consent/debit в RFP) |

**Новый инвариант AD-009** (Proposed, ADR-008): списание только по активному согласию; проверка лимитов до списания; списание после отзыва невозможно.

**Что НЕ меняется:** топология шлюза, trust-зоны, криптография, зачисление из PAID, возвраты-сага, модель «ядро контрактно-независимо от транспорта».

## 3. Архитектурное решение (deliverable 3)

Полное решение с альтернативами, последствиями и обратимостью — **`docs/adr/ADR-008-*.md`**. Кратко:
- согласие — отдельный объект с автоматом;
- списание = платёж с `initiationType=CONSENT` (путь без `QR_ISSUED`);
- pull-модель (ТСП инициирует списание), планировщик — deferred;
- контракты расширяются аддитивно.

(плюс конспект ключевых потоков)

## 4. Изменения контрактов (deliverable 4)
...

## 5. NFR (deliverable 5)
...

## 6. Критерии приёмки и план отката (deliverable 6)
...

## 7. На решение человека-архитектора (deliverable 7)
...
```

OK, this is getting very long. Let me be judicious. The solutioning-recurring.md can reference the ADR for full decision details and focus on the 7 deliverables concisely. I'll write it as the "пакет" doc with the 7 sections, each concise but complete.

Actually, I realize I should think about whether the user wants ONE comprehensive doc or multiple files. Re-reading: "Подготовь архитектурный пакет этого изменения" + "кратко перечисли созданные и изменённые файлы". So multiple files forming a package. My plan (ADR + solutioning-recurring + consent-state-machine + contract edits + nfr + spine) is a coherent package following repo conventions.

Let me also make sure I include the state machine spec (consent-state-machine.md) because it's the formal spec for the new entity, and the repo has docs/spec/state-machine.md as a precedent.

Let me now write everything. I'll write the 3 new files, then edit the 4-5 existing files.

Let me be mindful of total output length but be complete. This is a big task; I'll produce substantial content but keep each file focused.

Let me write the files now.

For consent-state-machine.md, content:

```markdown
# Статусная машина согласия и списания по согласию — спецификация переходов

- Status: Draft (для ревью на гейте A1 подписок)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-008, ADR-002, ADR-005, AD-009

## 1. Две сущности

1. **Согласие (Consent)** — самостоятельный объект, источник допустимости списания.
2. **Списание (Debit)** — платёж с `initiationType=CONSENT`, использует статусную машину платежа (ADR-002) с путём без `QR_ISSUED`.

## 2. Согласие: состояния

| Состояние | Смысл | Виден ТСП |
|---|---|---|
| PENDING_APPROVAL | запрос согласия создан, ожидается подтверждение плательщика/банка плательщика | да |
| ACTIVE | согласие действует, списания разрешены | да |
| EXPIRED | срок действия истёк | да |
| REVOKED | отозвано плательщиком (или ТСП) | да |
| SUSPENDED | приостановлено (технически/комплаенс) | да |

Параметры согласия (иммутабельны после ACTIVE): `maxAmount`, `currency`, `validUntil`, `maxDebitsPerPeriod`/`frequency` (по НСПК [ТРЕБУЕТ ПРОВЕРКИ]), `tspId`.

## 3. Согласие: переходы

| № | From | To | Триггер | Guard |
|---|---|---|---|---|
| C1 | — | PENDING_APPROVAL | POST /v1/consents (новый consentId) | валидный запрос, ТСП активен |
| C2 | PENDING_APPROVAL | ACTIVE | событие адаптера consent.activated | параметры согласия валидны |
| C3 | PENDING_APPROVAL | FAILED/REVOKED | отказ плательщика/НСПК или таймаут | — |
| C4 | ACTIVE | REVOKED | consent.revoked (плательщик/НСПК/ТСП) | — |
| C5 | ACTIVE | EXPIRED | validUntil достигнут (таймер/сверка) | — |
| C6 | ACTIVE | SUSPENDED | комплаенс/антифрод или транспорт.unavailable | — |
| C7 | SUSPENDED | ACTIVE | снятие приостановки | — |

## 4. Списание (Debit)

Платёж с `initiationType=CONSENT`. Состояния — те же финансовые, что у платежа, но без `QR_ISSUED`:

`CREATED → PAID → CREDITED → COMPLETED`, терминальные `FAILED`; техническое `DEBIT_PENDING` (списание отправлено в НСПК).

| № | From | To | Триггер | Guard |
|---|---|---|---|---|
| D1 | — | CREATED | POST /v1/payments (initiationType=CONSENT, consentId) | **consent в ACTIVE**, сумма ≤ maxAmount, срок/частота соблюдены (AD-009) |
| D2 | CREATED | PAID | нотификация НСПК «списание подтверждено» (debit.confirmed) | сумма/получатель совпадают |
| D3 | CREATED | FAILED | отклонение НСПК / исчерпаны ретраи | — |
| D4 | PAID | CREDITED | подтверждение АБС | идемпотентно по reference (AD-005) |
| D5 | CREDITED | COMPLETED | вебхук ТСП доставлен | — |
| D6 | COMPLETED | REFUNDED | сага возврата | полный возврат |

## 5. Запрещённые переходы и инварианты

- **Списание невозможно при согласии не в `ACTIVE`** (AD-009): guard D1 обязателен, проверяется fitness-тестом.
- Превышение `maxAmount`/`validUntil`/частоты → `FAILED` (или отклонение на входе) до обращения к НСПК.
- Повторный запрос списания с тем же `Idempotency-Key`/`reference` → тот же `paymentId`, нового списания нет (AD-003).
- Отзыв согласия (C4) не отменяет уже `PAID`/`CREDITED` списания — они доводятся до конца; отзыв блокирует только новые D1.
- `REVOKED`/`EXPIRED` согласия — терминальные (повторная активация не допускается; новое согласие — новый consentId).

## 6. Идемпотентность и сверка

- События согласия (`consent.*`) дедуплицируются по `eventId` (ADR-004).
- Сверка: активные согласия и открытые списания — кандидаты ежечасной сверки с НСПК; расхождение «у нас ACTIVE, у НСПК REVOKED» → стоп-сигнал, эскалация (списание блокируется).
```

Good. Now the contracts and openapi and nfr and spine edits.

For contracts/tsp-api.md, I'll append new sections §8 (Consent), §9 (Debit by consent / initiatonType), and update webhooks §5. Actually, I need to add content at specific places. Let me plan the edits:

1. Update header version note (v0.1 draft → v0.2 draft with additive consent/debit).
2. Add §3.6 (or a new §8) for consent endpoints. Since §3 has "Методы" 3.1-3.5, I'll add 3.6 (Consent) and 3.7 (Spisanie by consent — actually reuse 3.2 with initiationType).
3. Update §3.2 (createPayment) to mention initiationType/consentId optional.
4. Update §5 webhooks to add consent events.
5. Update §7 open questions.

This is getting complex. Let me do focused edits.

Actually, for the contracts/tsp-api.md, the cleanest is:
- Add `initiationType` and `consentId` to §3.2 request/response.
- Add new §3.6 consent endpoints.
- Add consent webhook events to §5.
- Bump version note.

For openapi/tsp-api.yaml, add:
- info.version 0.1.0 → 0.2.0
- PaymentRequest: add initiationType, consentId (optional)
- Payment: add initiationType, consentId (optional)
- New paths /v1/consents, /v1/consents/{consentId}, /v1/consents/{consentId}/revoke
- New schemas ConsentRequest, Consent

Let me do these edits carefully.

For nfr.md, add a new section 7 "Рекуррентные списания (подписки)" with a table.

For ARCHITECTURE-SPINE.md:
- Add AD-009 (Proposed) after AD-008.
- Update Deferred section to remove/annotate автоплатежи. Actually the Deferred section doesn't mention автоплатежи; solutioning.md §1 does. I'll add a note to the Deferred section or just leave it and update solutioning.md. Let me update the spine's Deferred to add a note that "автоплатежи/подписки" moved to scope (ADR-008). Actually simpler: the spine Deferred lists мультивалютность, C2C/выплаты, диспуты — none is автоплатежи. So I don't strictly need to edit Deferred for автоплатежи. But solutioning.md §1 roadmap lists "автоплатежи" as out of scope. I'll edit solutioning.md §1 to note автоплатежи now in scope (ADR-008).

Also the spine "Контракты и версии" section mentions tsp-api.md v0.1. I could update to v0.2 but it's minor; I'll leave or lightly note. Actually, I'll add a pointer in the spine to the new feature. Hmm, the spine is about invariants, not contracts. I'll just add AD-009 and leave the rest.

Let me finalize the plan and write.

Actually, I also want to update README.md to mention the new feature? The README lists structure and status. The user didn't ask to update README. I'll add a brief note to README status line pointing to the new package. Actually, minimal — I'll update the README status to note the new Proposed package. This helps discoverability. But it's optional. Let me include a small README update for completeness (it's the repo's index). Actually, I'll add one line to README structure/status. Let me keep it minimal.

Hmm, let me not over-expand scope. The essential deliverables are covered by: ADR-008, solutioning-recurring, consent-state-machine, contracts, openapi, nfr, spine. I'll also do a tiny solutioning.md roadmap edit and a tiny README note. That's 9 files touched. Reasonable for an "architectural package."

Actually, let me reconsider the README and solutioning.md edits — are they necessary? 
- solutioning.md roadmap says "автоплатежи" out of scope. Since we're bringing it in scope, leaving it stale would be inconsistent. A one-line edit is warranted.
- README status line: "решение подготовлено, ожидает человеческого решения A3..." — I can add a note about the new recurring package. Optional but nice. I'll do a small edit.

Let me keep total to ~9 files. Let me write.

Let me now actually produce all the content. I'll write the 3 new files in parallel first.

Let me carefully write the full text of each.

I'll start with the three write_file calls.

Let me write ADR-008 (full), consent-state-machine (full), solutioning-recurring (full).

I'll compose them now, carefully.

For solutioning-recurring, I need to cover all 7 deliverables. Let me write it comprehensively but not bloated.

Let me write.

Actually, one more design detail for the contracts: the consent endpoint request. What does the ТСП send to create a consent? In the СБП-native flow, the ТСП initiates a consent request, and the payer completes it in their bank. So the ТСП sends:
- tspId
- payerId (masked/minimal — e.g., phone or client reference) [ПДн — minimize]
- maxAmount (or fixed amount + schedule)
- currency
- validUntil / validity
- frequency limit (optional)
- purpose/subscription description

Response: consentId, status=PENDING_APPROVAL, consentUrl (redirect for payer, if applicable — [ТРЕБУЕТ ПРОВЕРКИ]).

Then НСПК notifies consent.activated (or the payer never completes → expired/failed).

This is analogous to the QR flow (create → external action → notification). Good, consistent with the architecture.

For the debit (POST /v1/payments with consentId):
Request adds: initiationType=CONSENT, consentId, amount (≤ maxAmount), merchantOrderId. No qrType/ttl (those are QR-specific; for consent, ttl doesn't apply). So the request fields are partially different. The openapi PaymentRequest currently has amount, merchantOrderId (required) and I'll add initiationType, consentId, plus the doc mentions tspId, currency, qrType, etc.

Actually the openapi PaymentRequest is minimal (amount, merchantOrderId). The docs/contracts version has more. For my openapi edit, I'll extend the openapi PaymentRequest with the additional optional fields (initiationType, consentId, and also the ones already in docs like currency, qrType — but to stay minimal, I'll just add initiationType and consentId, since the openapi is already a subset).

Let me keep openapi changes focused: add initiationType, consentId to PaymentRequest and Payment; add consent paths + schemas; bump version.

Let me write now. I'll produce the files.

For the openapi, I need to write the new YAML carefully, preserving existing structure. I'll use edit to modify specific parts, and also add new paths and schemas. Actually, it might be cleaner to rewrite the openapi file entirely via write_file (since it's small and I have its full content). But the instruction says for write_file I must read first (I have). Rewriting is cleaner than multiple edits for a small file. But there's a risk of losing exact existing content. I have the full content, so I'll rewrite it with additions. Actually, let me use edit for surgical changes to be safe, and add new blocks.

Hmm, the openapi file is small. Let me just rewrite it fully with write_file, preserving existing paths/schemas and adding new ones. I have the exact current content. This is cleaner.

Wait — write_file on an existing file: the guidance says "you MUST use read_file first; if file does not exist, then create it." I've read it, so I can write_file (overwrite). But "blind overwrites are rejected" if prior-read enforcement is on — but I HAVE read it, so it's fine. Actually, to be safe and precise, I'll use edit for the existing files (contracts, nfr, spine, solutioning, README) and rewrite openapi via write_file (it's small and I want to restructure it with additions). Actually, let me use edit for openapi too, to be safe and show minimal diff. Multiple edits on openapi.

Let me just do it step by step. I'll:
1. write_file × 3 (new files).
2. edit openapi (a few edits).
3. edit contracts/tsp-api.md (a few edits).
4. edit nfr.md (append section).
5. edit ARCHITECTURE-SPINE.md (add AD-009).
6. edit solutioning.md (roadmap line).
7. edit README.md (status line).

Let me begin. I'll write the 3 new files now.

Let me write out full content for each new file.

I'll be careful with the fitness constraint: no `<!--` in ADR. My ADR uses markdown only. Good. And no TODO/TBD/XXX in spine — my AD-009 text must avoid those.

Let me write.

For solutioning-recurring.md, I'll make it the comprehensive package with the 7 sections. Let me draft it fully and concisely.

Let me write all three now in one message (parallel write_file calls).

I need to be careful that the content is correct and idiomatic. Let me finalize the Russian text.

Let me write.
Изучение завершено. Я понял методику репозитория: ADR-формат (`Context/Decision/Alternatives/Consequences/Reversibility/References`), spine-инварианты (`AD-XXX` с `Binds/Prevents/Rule`), контракты с политикой аддитивного версионирования, измеримые NFR, гейты A0–A5, план отката, `.arch-handoff/` — генерируемый снапшот (его не трогаю, правлю только источники в `docs/`, spine и openapi).

Классифицирую задачу как **architectural** и перехожу к подготовке пакета: два развилочных решения (кто инициирует списание; откуда приходит согласие) я фиксирую как рекомендации в ADR с альтернативами и выношу бизнес-часть в «на решение человека». Пишу пакет файлов.

  `write_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/solutioning-recurring.md", content="# Solutioning — Рекуррентные C2B-списания по согласию (подписки СБП)\n\nПакет изменения поверх принятого решения «Платёжный шлюз СБП (C2B-п)`

Now write the solutioning-recurring.md (the comprehensive package doc).

  `write_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/openapi/tsp-api.yaml", content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\npaths:\n  /v1/payments:\n    post:\n      operationId: createPayment\)`

Now let me edit the existing files. Start with openapi/tsp-api.yaml — I'll rewrite it fully (small file) with additions. Actually, let me use edit to be surgical and preserve. The file is small enough. Let me do targeted edits.

Current openapi content:
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

I'll rewrite the whole file with additions. Since it's small and I want to add multiple paths and schemas, a full rewrite is cleanest. Let me use write_file to overwrite (I've read it, so no blind-overwrite issue).

Actually, wait — I need to be careful. The write_file tool with prior-read enforcement: I've read the file, so overwriting is allowed. But let me double check the guidance: "you MUST use the read_file tool first; if the file does not exist, then create it. With prior-read enforcement enabled, blind overwrites are rejected." I've read it, so fine.

Let me rewrite openapi/tsp-api.yaml with:
- version 0.2.0
- PaymentRequest: add initiationType, consentId (optional)
- Payment: add initiationType, consentId (optional)
- New paths /v1/consents (post), /v1/consents/{consentId} (get), /v1/consents/{consentId}/revoke (post)
- New schemas ConsentRequest, Consent

Let me write the full YAML.

Actually, I'll be careful with YAML to keep it valid. Let me write it in the same compact style as existing.

For PaymentRequest, add:
```yaml
        initiationType: {type: string, enum: [QR, CONSENT], default: QR, description: Тип инициации; CONSENT — списание по согласию}
        consentId: {type: string, description: Обязателен при initiationType=CONSENT}
```

For Payment add:
```yaml
        initiationType: {type: string, enum: [QR, CONSENT]}
        consentId: {type: string}
```

New consent endpoints. ConsentRequest:
```yaml
    ConsentRequest:
      type: object
      required: [maxAmount, validUntil]
      properties:
        maxAmount: {type: integer, description: Максимальная сумма списания в копейках}
        currency: {type: string, default: RUB}
        validUntil: {type: string, format: date-time, description: Срок действия согласия (ISO 8601 UTC)}
        maxDebitsPerPeriod: {type: integer, description: Лимит частоты списаний за период [ТРЕБУЕТ ПРОВЕРКИ]}
        purpose: {type: string, description: Назначение подписки}
    Consent:
      type: object
      required: [consentId, status, maxAmount, validUntil]
      properties:
        consentId: {type: string}
        status: {type: string, enum: [PENDING_APPROVAL, ACTIVE, EXPIRED, REVOKED, SUSPENDED]}
        maxAmount: {type: integer}
        currency: {type: string}
        validUntil: {type: string, format: date-time}
        maxDebitsPerPeriod: {type: integer}
        purpose: {type: string}
```

Paths:
```yaml
  /v1/consents:
    post:
      operationId: createConsent
      parameters:
        - {in: header, name: Idempotency-Key, required: true, schema: {type: string}}
      requestBody:
        required: true
        content:
          application/json:
            schema: {$ref: '#/components/schemas/ConsentRequest'}
      responses:
        '201':
          description: Запрос согласия создан
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
        - {in: header, name: Idempotency-Key, required: true, schema: {type: string}}
      responses:
        '200':
          description: Согласие отозвано
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Consent'}
```

Let me write the full file.

Now for docs/contracts/tsp-api.md, I'll do targeted edits:
1. Header version note: change "Версия контракта: 0.1" line to mention 0.2 draft with additive consent/debit. Let me find the exact text. The header:
```
- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
```
I'll change to 0.2 with note.

2. §3.2 createPayment — add initiationType/consentId to request and response, and a note.

3. Add §3.6 consent endpoints (after §3.5).

4. §5 webhooks — add consent events.

5. §7 open questions — add consent items.

Let me do these edits carefully with exact old_string.

Actually, for §3.2, I need to add fields. The request JSON in the doc:
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

I'll add `initiationType` and `consentId` fields. And update the "Правила" paragraph to mention consent.

Let me also add §3.6 for consents.

Let me structure the edits. I'll do them one at a time.

First, edit header version.

Let me do the openapi rewrite first (write_file), then the tsp-api.md edits, then nfr, spine, solutioning, README.

Let me write openapi now.
Расширяю OpenAPI-контракт аддитивно (новая минорная версия, без изменения существующих путей).

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/contracts/tsp-api.md", old_string="- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)", new_string="- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.2 (нестабильная; аддитивное расширение 0.1 согласиями и списаниями по соглас)`
  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/contracts/tsp-api.md", old_string="  \"redirectUrl\": \"https://merchant.example.com/order/12345/return\",\n  \"merchantOrderId\": \"order-12345\" // опц., сквозной для ТСП\n, new_string="  \"redirectUrl\": \"https://merchant.example.com/order/12345/return\",\n  \"merchantOrderId\": \"order-12345\", // опц., сквозной для ТСП\)`
  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/contracts/tsp-api.md", old_string="Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (AD, new_string="Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (AD)`
  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/contracts/tsp-api.md", old_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`", new_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n)`
  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/contracts/tsp-api.md", old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`
  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/contracts/tsp-api.md", old_string="4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.", new_string="4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.\n5. Семантика `maxDebitsPerPeriod`/частоты и место хранения согл)`

Now edit docs/contracts/tsp-api.md. Let me make several edits:

1. Header version note.
2. §3.2 createPayment — add initiationType/consentId.
3. Add §3.6 consent endpoints.
4. §5 webhooks — add consent events.
5. §7 open questions.

Let me do edit 1: header.

Current:
```
- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
```

New:
```
- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (нестабильная; аддитивное расширение 0.1 согласиями/списаниями; до A1 фиксируется v1.0-draft)
```

Edit 2: §3.2. I need to add fields to the request JSON and update the rules paragraph.

Let me find the exact request block and rules.

Request block (from earlier read):
```
`POST /v1/payments`

Запрос:
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
```

I'll add after "merchantOrderId" line:
```
  "initiationType": "CONSENT",     // опц.; QR (по умолчанию) | CONSENT — списание по согласию
  "consentId": "con_7a2b9c1d"      // обязателен при initiationType=CONSENT
```

And the rules paragraph:
```
Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (ADR-002). Максимальная сумма — по лимитам НСПК [ТРЕБУЕТ ПРОВЕРКИ].
```

I'll append a sentence about CONSENT:
```
При `initiationType=CONSENT`: `qrType`/`ttlSeconds`/`redirectUrl` не применяются (нет QR); `consentId` обязателен; согласие должно быть `ACTIVE`, `amount ≤ maxAmount` (ADR-008, AD-009). Путь статусов без `QR_ISSUED`.
```

Also update the response block? The response has qrId/qrUrl. For CONSENT, those are null. I'll add a note. Actually, I'll keep it simple and add a note after the response rules.

Let me also update §3.2 response to mention that qrId/qrUrl are null for CONSENT. I'll add a note line.

Let me do these edits.

Edit 3: Add §3.6 after §3.5.

§3.5 ends with:
```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`
```

I'll add §3.6 after it.

§3.6 content:
```
### 3.6 Согласие (consent) — подписки СБП

#### 3.6.1 Создание запроса согласия

`POST /v1/consents` (заголовок `Idempotency-Key` обязателен)

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "maxAmount": 49900,              // копейки; максимальная сумма одного списания
  "currency": "RUB",
  "validUntil": "2027-09-28T00:00:00.000Z",
  "maxDebitsPerPeriod": 1,         // опц.; лимит частоты [ТРЕБУЕТ ПРОВЕРКИ]
  "purpose": "Подписка на сервис"
}
```

Ответ `201`:
```json
{
  "consentId": "con_7a2b9c1d",
  "status": "PENDING_APPROVAL",    // PENDING_APPROVAL | ACTIVE | EXPIRED | REVOKED | SUSPENDED
  "maxAmount": 49900,
  "validUntil": "2027-09-28T00:00:00.000Z",
  "consentUrl": "https://…"        // опц.; ссылка для подтверждения плательщиком [ТРЕБУЕТ ПРОВЕРКИ]
}
```

Правила: `maxAmount` > 0; `validUntil` в будущем. После активации параметры согласия иммутабельны. Подтверждение плательщика/банка плательщика приходит событием НСПК (адаптер), статус меняется `PENDING_APPROVAL → ACTIVE`.

#### 3.6.2 Статус согласия

`GET /v1/consents/{consentId}` → `200 { consentId, status, maxAmount, validUntil, maxDebitsPerPeriod, purpose }`

#### 3.6.3 Отзыв согласия (инициатива ТСП)

`POST /v1/consents/{consentId}/revoke` → `200 { consentId, status: "REVOKED" }`

Правила: отзыв необратим; после отзыва новые списания отклоняются (`CONSENT_NOT_ACTIVE`). Уже `PAID`/`CREDITED` списания доводятся до конца (ADR-008). Отзыв плательщиком/банком плательщика приходит событием НСПК (`consent.revoked`).
```

Edit 4: §5 webhooks — add consent events.

Current §5 events list:
```
События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
```

Add:
```
- `consent.activated` — согласие активировано
- `consent.revoked` — согласие отозвано
- `consent.expired` — срок согласия истёк
```

And a note that `payment.*` is reused for debits.

Edit 5: §7 open questions — add consent items.

Current §7:
```
## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
```

Add:
```
5. Семантика `maxDebitsPerPeriod`/частоты и хранение согласия в НСПК — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
6. Отдельный `POST /v1/debits` vs расширение `/v1/payments` — зафиксировано в ADR-008 (расширение), пересмотр при росте семантического расхождения.
```

Let me do these edits now. I'll batch them but each edit is on the same file, so I should do them sequentially to avoid conflicts (edit requires exact old_string; multiple edits to same file in parallel could conflict). Actually, the edit tool operates on the file; doing multiple edits to the same file in parallel is risky. Let me do them sequentially, or combine where possible.

Actually, I can do multiple edit calls in sequence (separate messages) or in one message but they'd apply to the same file sequentially? The tool applies them in order within a message? To be safe, I'll do them one at a time (sequential messages). But that's slow. Alternatively, I can do them in a single message with multiple edit calls — the system should apply them sequentially. The guidance says "If you intend to call multiple tools and there are no dependencies between the calls, make all of the independent calls in the same block." Edits to the same file ARE dependent (they change the file). So I should do them sequentially.

Hmm, but actually multiple edits to the same file via separate edit calls in one message — the risk is that the old_string for later edits might not match if earlier edits changed surrounding text. But since my edits target distinct, non-overlapping regions, they should be fine even in sequence. However, the tool likely applies them in the order given. To be safe and correct, I'll do them in separate sequential messages. Actually, that's a lot of round-trips.

Let me be pragmatic: I'll do the tsp-api.md edits in a small number of edit calls, each targeting a distinct region with enough context. I'll put them in a single message (multiple edit tool calls) since they target non-overlapping regions and I have the exact current content. The tool should handle them.

Actually, the safer approach given "dependent calls run sequentially" is to chain them. But edit calls in one message are applied in order by the runtime. I'll risk doing them in one message since regions are non-overlapping.

Wait, actually, re-reading the tool guidance: "If you intend to call multiple tools and there are no dependencies between the calls, make all of the independent calls in the same block, otherwise you MUST wait for previous calls to finish first to determine the dependent values." Edits to the same file are technically independent in terms of values (I'm not using output of one as input to another), but they DO mutate the same file. The safe interpretation: they're independent enough since regions don't overlap and I know the exact content. I'll do them in one message.

Let me do all 5 tsp-api.md edits + nfr edit + spine edit + solutioning edit + README edit. Actually, let me group: do tsp-api.md edits (5 edits) in one message, then the other files' edits in the next message(s).

Let me write the exact old_strings and new_strings.

Edit A (header version):
old:
```
- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
```
new:
```
- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.2 (нестабильная; аддитивное расширение 0.1 согласиями и списаниями по согласию; до A1 фиксируется v1.0-draft)
```

Edit B (§3.2 request JSON — add fields):
old:
```
  "redirectUrl": "https://merchant.example.com/order/12345/return",
  "merchantOrderId": "order-12345" // опц., сквозной для ТСП
}
```
new:
```
  "redirectUrl": "https://merchant.example.com/order/12345/return",
  "merchantOrderId": "order-12345", // опц., сквозной для ТСП
  "initiationType": "CONSENT",      // опц.; QR (по умолчанию) | CONSENT — списание по согласию
  "consentId": "con_7a2b9c1d"       // обязателен при initiationType=CONSENT
}
```

Edit C (§3.2 rules paragraph):
old:
```
Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (ADR-002). Максимальная сумма — по лимитам НСПК [ТРЕБУЕТ ПРОВЕРКИ].
```
new:
```
Правила: `amount` > 0; для `qrType=static` сумма может отсутствовать (`amount` опц.); после создания **сумма и реквизиты иммутабельны** (ADR-002). Максимальная сумма — по лимитам НСПК [ТРЕБУЕТ ПРОВЕРКИ].

При `initiationType=CONSENT` (списание по согласию, ADR-008): `qrType`/`ttlSeconds`/`redirectUrl` не применяются (QR нет); `consentId` обязателен; согласие должно быть `ACTIVE`, `amount ≤ maxAmount`, срок/частота соблюдены (AD-009); статусный путь без `QR_ISSUED`; в ответе `qrId`/`qrUrl`/`expiresAt` отсутствуют (`null`).
```

Edit D (§3.5 → add §3.6 after):
old:
```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`
```
new: append §3.6 after.

Edit E (§5 webhooks events):
old:
```
События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
```
new: add consent events + note.

Edit F (§7 open questions):
old:
```
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
```
new: append items 5-6.

Let me do these edits. I'll put them in one message.

Actually, I realize Edit B and Edit C both touch §3.2 but non-overlapping. Fine.

Let me carefully write them.

For Edit D, the §3.6 content is long. Let me include it fully.

Let me proceed.
Вношу изменения в контракт API ТСП (аддитивно, без изменения существующих методов).

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/contracts/tsp-api.md", old_string="# Контракт API ТСП (мерчант-API) — v0.1 draft", new_string="# Контракт API ТСП (мерчант-API) — v0.2 draft")`
  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/contracts/tsp-api.md", old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`

All tsp-api.md edits applied. Now I notice the title still says "v0.1 draft" in the H1 header. Let me fix that too for consistency. Actually, the H1 is "# Контракт API ТСП (мерчант-API) — v0.1 draft". I should update to v0.2 draft. Let me do a small edit.

Also I need to update the §4 error codes to add CONSENT_NOT_ACTIVE code. Let me check §4 error codes: "Канонические коды: ... PAYMENT_NOT_REFUNDABLE (422), AMOUNT_EXCEEDS_PAID (422), RATE_LIMITED (429), INTERNAL (500)." I should add CONSENT_NOT_ACTIVE. Let me add it.

Let me do these two more edits to tsp-api.md (H1 title + error codes).

Then nfr.md, spine, solutioning.md, README.md.

Let me do the H1 + error codes edits.

Error codes current line:
```
Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.
```
Add `CONSENT_NOT_ACTIVE` (422) and maybe `CONSENT_LIMIT_EXCEEDED` (422). Let me add `CONSENT_NOT_ACTIVE` (409?) — hmm. Actually the consent not active is a business rejection. Let me use 422 with code CONSENT_NOT_ACTIVE. And CONSENT_LIMIT_EXCEEDED (422). I'll add both.

New:
```
Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `CONSENT_NOT_ACTIVE` (422), `CONSENT_LIMIT_EXCEEDED` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.
```

Let me do the H1 edit and error codes edit.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/nfr.md", old_string="| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |\n\n## Зависимости (внешние входы для NFR)", new_string="| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |\n\n## 7. Рекуррентные списания (подписки СБП)\n\nДополнительные изм)`

Now edit nfr.md to add section 7. Let me append after section 6 (Наблюдаемость) and before "Зависимости".

Current nfr.md ends with section 6 table then "## Зависимости (внешние входы для NFR)".

I'll insert a new section 7 before "## Зависимости".

Let me find the exact text around there.

From my earlier read:
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

I'll insert section 7 between the table end and "## Зависимости".

New section 7:
```
## 7. Рекуррентные списания (подписки СБП)

Дополнительные измеримые NFR для списаний по согласию (ADR-008). Базовые NFR разделов 1–6 наследуются (доступность, RPO, идемпотентность, безопасность).

| Метрика | Цель | Метод проверки |
|---|---|---|
| Latency «инициация списания по согласию» (шлюз, без НСПК/АБС) | p95 < 500 мс, p99 < 1 с | Нагрузочный тест |
| Подтверждение списания от события НСПК | p95 < 60 с (SLA с НСПК/АБС) | Метрика процесса |
| Latency «создание запроса согласия» | p95 < 1 с (без учёта НСПК) | Нагрузочный тест |
| Распространение отзыва согласия (от события НСПК до блокировки списаний) | p95 < 5 с | Метрика лага очереди |
| Списание после отзыва/истечения | 0 (guard D1, AD-009) | Fitness-тест |
| Двойное списание при повторной доставке | 0 (идемпотентность по `reference`/`Idempotency-Key`) | Тест на повтор |
| Принудительная проверка лимитов (maxAmount, срок, частота) до списания | 100 % списаний | Тест-кейсы |
| Сверка состояний согласий с НСПК | ежечасная; расхождений по активным согласиям — 0 | Reconciliation-отчёт |
| ПДн согласия | минимизация, шифрование в покое, маскирование в логах | ИБ-ревью |
| Throughput добавка от списаний | +50 TPS sustained без изменения архитектуры | Load-test |
```

Let me do this edit. I'll use the exact old_string of the section 6 table + "## Зависимости".

Actually, to be safe, I'll target the "## Зависимости" line and prepend the new section. old_string:
```
| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |

## Зависимости (внешние входы для NFR)
```
new_string: insert section 7 before ## Зависимости.

Let me do it.
Добавляю измеримые NFR для нового функционала.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`
  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/ARCHITECTURE-SPINE.md", old_string="- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.", new_string="- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.\n- **Планировщик под)`
  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/ARCHITECTURE-SPINE.md", old_string="- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec).", new_string="- Внутренний контракт шлюза (API ТСП): версия 0.2 draft (аддитивные согласия/списания, ADR-008) — `docs/contracts/tsp-api.md`.")`

Now edit ARCHITECTURE-SPINE.md to add AD-009 after AD-008, and update the Deferred section.

The AD-008 block ends with:
```
## AD-008. Стратегия реализации — гибрид [ADOPTED]

- Status: Adopted (A3 от 2026-08-15, ADR-007 Accepted)
...
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll insert AD-009 after AD-008's Rule and before the `---` separator.

Let me find the exact old_string. The end of AD-008:
```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll insert AD-009 before the `---`.

AD-009 content:
```
## AD-009. Списание только по активному согласию

- Status: Proposed (ADR-008)
- **Binds**: согласие (consent) и его статусная машина, статусная машина платежа (списание), адаптер ОПКЦ, антифрод/AML.
- **Prevents**: списание без согласия или после его отзыва/истечения; превышение параметров согласия (максимум, срок, частота); двойное списание при повторе.
- **Rule**: Списание по согласию (`initiationType=CONSENT`) возможно только при согласии в состоянии `ACTIVE`; параметры согласия (максимальная сумма, срок действия, лимит частоты) проверяются до инициации списания; повторная доставка запроса списания не создаёт дубль. Проверка: fitness-тест «списание из `REVOKED`/`EXPIRED`/`SUSPENDED` недостижимо».
```

I need to be careful not to use TODO/TBD/XXX (spine-lints-clean). My text doesn't. Good.

Also update Deferred section: currently:
```
## Deferred (с причиной и условием возврата)

- **Мультивалютность и иностранные платёжные системы**: не в scope C2B-приёма СБП; вернуть при расширении на валютные счета ТСП.
- **C2C-переводы и выплаты B2C/B2B**: roadmap после стабилизации C2B; вернуть как отдельный initiative (родительский spine изменится).
- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.
```

I should add a note about подписки being brought into scope (ADR-008). Actually, "автоплатежи" wasn't in the spine Deferred list. But solutioning.md §1 roadmap listed "автоплатежи" as out of scope. So I'll add a line to the Deferred section clarifying: подписки/автоплатежи ранее были вне scope, теперь внесены как feature (ADR-008, AD-009). Actually, better to add a line noting this transition, OR add to the "Deferred" a note. Hmm.

Actually, the cleanest is to add a short note in the Deferred section:
```
- **Планировщик подписок на стороне шлюза (push-списания)**: вне scope — списания инициирует ТСП (pull, ADR-008); вернуть по требованию бизнеса.
```

This is genuinely a deferred item (push scheduler). Good. I'll add it.

Also I might want to update the "Контракты и версии" section at the bottom to note tsp-api v0.2. Let me check: 
```
## Контракты и версии

- Контракт НСПК: `docs/contracts/nspk-contract.md` — создаётся после получения документации НСПК; ...
- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec).
- Пиннинг версий зависимостей — в CONSTRAINTS.yaml (.arch-handoff) при передаче кодовому харнессу.
```

I'll update "версия 0.1 draft" → "версия 0.2 draft (аддитивные согласия/списания)". Minor but good for consistency.

Let me do the spine edits: (1) insert AD-009, (2) add deferred item, (3) update contracts version line.

Let me do these three edits.

For edit 1, old_string:
```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```
new_string: insert AD-009 before `---`.

For edit 2 (Deferred), old_string:
```
- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.
```
new_string: append the push-scheduler deferred line.

For edit 3 (contracts version), old_string:
```
- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec).
```
new_string:
```
- Внутренний контракт шлюза (API ТСП): версия 0.2 draft (аддитивные согласия/списания, ADR-008) — `docs/contracts/tsp-api.md`.
```

Let me do all three edits in one message.
Добавляю новый spine-инвариант AD-009 и актуализирую deferred-секцию.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/solutioning.md", old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop, new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты, **рекуррентные сп)`
  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/solutioning.md", old_string="| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accepted) | AD-008 [ADOPTED] |", new_string="| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accepted) | AD-008 [ADOPTED] |\n| Рекуррентные списания по согласию )`
  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/README.md", old_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITEC, new_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..008`, `ARCHITEC)`
  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/README.md", old_string="ARCHITECTURE-SPINE.md        инварианты AD-001..AD-008\ndocs/\n  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps\, new_string="ARCHITECTURE-SPINE.md        инварианты AD-001..AD-009\ndocs/\n  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps\)`

Now update docs/solutioning.md roadmap line and README.md.

solutioning.md §1 roadmap:
```
Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи.
```

I'll change "автоплатежи" to reflect that подписки/автоплатежи now in scope (ADR-008). New:
```
Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты, **рекуррентные списания по согласию (подписки СБП, ADR-008)**. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, push-планировщик подписок.
```

Also there's a mention in solutioning.md §1: "Плательщик (физлицо)..." not relevant. And §10 open questions mentions scope. Not necessary to update.

Also solutioning.md §5 table lists ADR mapping. I could add ADR-008 row. Let me add a row to the §5 table. Actually, the §5 table is:
```
| Решение | ADR | Spine |
|---|---|---|
| Топология: выделенный компонент + outbox | ADR-001 | AD-001, AD-002 |
| ... | ... | ... |
| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accepted) | AD-008 [ADOPTED] |
```

I'll add a row for ADR-008. This is a nice touch for consistency. Let me add:
```
| Рекуррентные списания по согласию (подписки) | ADR-008 | AD-009 |
```

Let me do the solutioning.md edits (2 edits: roadmap line + §5 table row).

Actually, let me keep it minimal — just the roadmap line (the most important for consistency), and optionally the table row. I'll do both since they're small.

For README.md, update the status line. Current:
```
- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).
```

I'll update:
- Ключевые документы: add `docs/adr/ADR-008`, `docs/solutioning-recurring.md`.
- Add a status line about the new package.

Let me edit README. I'll add a line after the status.

New status addition:
```
- Надстройка: рекуррентные списания по согласию (подписки СБП) — пакет изменения `docs/solutioning-recurring.md` + `docs/adr/ADR-008` (Proposed, ожидает A3).
```

And update "Ключевые документы" to mention ADR-008 and solutioning-recurring.

Let me do these edits.

For README, old_string:
```
- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).
```

new:
```
- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..008`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).
- Надстройка: рекуррентные списания по согласию (подписки СБП) — пакет изменения `docs/solutioning-recurring.md` + `docs/adr/ADR-008` (Proposed, ожидает A3).
```

And also update the structure block? It lists:
```
docs/
  solutioning.md             полный дизайн: компоненты, потоки, гейты, gaps
  ...
```
I could add `solutioning-recurring.md` and `spec/consent-state-machine.md` to the structure. Minor. I'll add them for discoverability. Actually, let me keep README edits minimal but add the two lines to the structure listing too. Let me check the structure block:

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

I'll update:
- `ARCHITECTURE-SPINE.md инварианты AD-001..AD-009`
- add `solutioning-recurring.md` line after solutioning.md
- `contracts/tsp-api.md контракт API ТСП v0.2 (мерчант-API)`
- add `spec/consent-state-machine.md` after state-machine.md
- `adr/ADR-001..008.md`

Let me do the README edits. I'll do two edits: (1) the header status block, (2) the structure block.

Actually, I can do it as one or two edits. Let me do two edits.

Let me write these edits now.

For solutioning.md, two edits:
1. roadmap line.
2. §5 table row.

Let me do all of these in one message (solutioning.md × 2 + README × 2).

Let me write exact old_strings.

solutioning.md roadmap old:
```
Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи.
```
new:
```
Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты, **рекуррентные списания по согласию (подписки СБП, ADR-008)**. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, push-планировщик подписок.
```

solutioning.md §5 table old (last row):
```
| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accepted) | AD-008 [ADOPTED] |
```
new:
```
| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accepted) | AD-008 [ADOPTED] |
| Рекуррентные списания по согласию (подписки) | ADR-008 | AD-009 |
```

README edits as above.

Let me do all 4 edits.
Актуализирую roadmap в `solutioning.md` и индекс в `README.md`.

  `run_shell_command(command="python3 -c \"import yaml; d=yaml.safe_load(open('openapi/tsp-api.yaml')); print('openapi yaml OK; paths=', list(d['paths'].keys())); print(, description="Validate OpenAPI YAML and list paths/schemas")`
  `grep_search(pattern="<!--", path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/adr")`
  `grep_search(pattern="TODO|TBD|XXX", path="<HARNESS>/runs/cells/superpowers-r1/ws/ARCHITECTURE-SPINE.md")`
  `grep_search(pattern="99,95", path="<HARNESS>/runs/cells/superpowers-r1/ws/docs/nfr.md")`

All edits applied. Now let me verify:
1. The fitness constraints (CONSTRAINTS.yaml) still pass:
   - `adr-no-placeholders`: no `<!--` in docs/adr/*.md. My new ADR-008 has no HTML comments. Good.
   - `nfr-measurable`: docs/nfr.md contains '99,95'. I preserved section 1 (99,95). Good.
   - `abs-credit-only-from-paid`: ADR-005 unchanged. Good.
   - `spine-lints-clean`: ARCHITECTURE-SPINE.md must_not_contain 'TODO|TBD|XXX'. My AD-009 has none. But wait — let me double check I didn't introduce any of those strings. My AD-009 text: no TODO/TBD/XXX. Good.

2. Let me verify the openapi YAML is valid. Let me quickly run a YAML parse check? I could use python to validate. Actually, I should verify the OpenAPI is well-formed. Let me run a quick check with python yaml (if available) or at least visually. The system reminder says I should verify. Since this is a docs task, verification = consistency checks. Let me at least validate YAML syntax of openapi and check for the fitness patterns.

Let me run a quick shell command to validate YAML and check the fitness rules manually. Actually, I can use grep_search to verify no `<!--` in the new ADR, and check '99,95' in nfr.md, and check AD-009 has no TODO.

Actually, let me do a light verification:
- Validate openapi YAML with python3 -c yaml.safe_load.
- grep for '<!--' in docs/adr/*.md (should be none).
- grep for TODO|TBD|XXX in ARCHITECTURE-SPINE.md (should be none).

Let me run these checks. Also maybe check the whole docs/adr for placeholders. But the existing ADRs might have `[ТРЕБУЕТ ПРОВЕРКИ]` (which is fine, not a comment). The fitness rule only checks `<!--`.

Let me run a shell command to do a few checks. Actually, I should use the dedicated tools where possible, but YAML validation requires shell (python). Let me run:
`python3 -c "import yaml,sys; yaml.safe_load(open('openapi/tsp-api.yaml')); print('yaml ok')"`

And use grep_search for the pattern checks.

Let me do these in parallel: 
1. run_shell_command for YAML validation.
2. grep_search for `<!--` in docs/adr (pattern `<!--`).
3. grep_search for TODO|TBD|XXX in ARCHITECTURE-SPINE.md.

Actually grep_search pattern `<!--` — the `<` and `!` are regex chars? `<` is literal, `!` is literal, `-` literal. `<!--` is fine as literal. But ripgrep might interpret `<!--` as regex; `<!` is fine (literal). Actually `<!--` contains no special regex metachars except maybe none. `<`, `!`, `-` are all literal. Fine.

Let me run these checks.

Also, I should double check the openapi YAML is valid. Let me run python yaml.

Let me also verify the git status to see what changed (for the final summary). Actually, I'll do git status/diff at the end to report faithfully.

Let me run the verification checks now.
Проверяю целостность пакета: валидность OpenAPI, отсутствие плейсхолдеров в ADR и «грязных» маркеров в spine.

  `read_file(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/openapi/tsp-api.yaml", offset=108, limit=14)`

There's a YAML parse error in openapi/tsp-api.yaml at line 117, column 29: "expected ',' or '}', but got '['". This is because I used flow-style mapping with an enum that contains a comma inside? No wait. Let me look at line 117.

The error is "while parsing a flow mapping ... expected ',' or '}', but got '['". This is likely in my `ConsentRequest` schema where I wrote:

```yaml
        validUntil: {type: string, format: date-time, description: Срок действия согласия (ISO 8601 UTC)}
```

Wait, the description "Срок действия согласия (ISO 8601 UTC)" contains parentheses but that's fine in YAML flow mapping since it's a scalar. But wait — in flow mapping `{type: string, format: date-time, description: Срок действия согласия (ISO 8601 UTC)}`, the parentheses inside a plain scalar are fine. Actually the issue: `format: date-time` — `date-time` is fine. Hmm.

Actually the error says "got '['" at column 91. Line 117. Let me look at what's at line 117. Let me read the file around line 117.

Actually, the issue might be with a description containing a colon or special char, OR the `[ТРЕБУЕТ ПРОВЕРКИ]` bracket inside a flow scalar. Wait — I used:

```yaml
        maxDebitsPerPeriod: {type: integer, description: Лимит частоты списаний за период [ТРЕБУЕТ ПРОВЕРКИ]}
```

Here `[ТРЕБУЕТ ПРОВЕРКИ]` is inside a plain scalar in a flow mapping. In YAML flow context, `[` starts a flow sequence! So `description: Лимит частоты списаний за период [ТРЕБУЕТ ПРОВЕРКИ]` — the `[` is interpreted as start of a flow sequence, breaking the flow mapping. That's the bug.

So I need to quote any scalar containing `[`, `{`, `]`, `}`, `,`, `:`, etc. in flow context. The descriptions containing `[ТРЕБУЕТ ПРОВЕРКИ]` need quoting.

Let me find all such places in my openapi additions:
- `ConsentRequest.maxDebitsPerPeriod`: `description: Лимит частоты списаний за период [ТРЕБУЕТ ПРОВЕРКИ]` — needs quotes.
- `Consent` schema — `maxDebitsPerPeriod` has no description. Fine.
- `ConsentRequest.validUntil`: `description: Срок действия согласия (ISO 8601 UTC)` — parentheses are fine in flow? Actually parentheses are fine in plain scalars in flow context (they're not special). But to be safe, let me quote. Actually `(` and `)` are allowed in plain scalars. The issue is only `[`, `]`, `{`, `}`, `,`, `:` (in some positions), `#`, etc.

Let me look at the whole file and quote any description with special chars. The `[ТРЕБУЕТ ПРОВЕРКИ]` appears in:
1. PaymentRequest.consentId description — "Обязателен при initiationType=CONSENT" — no brackets. Fine.
2. ConsentRequest.maxDebitsPerPeriod — `[ТРЕБУЕТ ПРОВЕРКИ]` — BROKEN.

Also `default: QR` etc. are fine.

Also check the enum values: `enum: [QR, CONSENT]` — that's a flow sequence, intended. Fine.

So the fix: quote the description with `[ТРЕБУЕТ ПРОВЕРКИ]`. Let me change to:
```yaml
        maxDebitsPerPeriod: {type: integer, description: 'Лимит частоты списаний за период [ТРЕБУЕТ ПРОВЕРКИ]'}
```

Using single quotes around the scalar. But single quotes in YAML — the scalar contains no single quotes, so fine.

Actually, wait — there might be other places too. Let me re-read my openapi content. The descriptions I added:
- PaymentRequest.initiationType: "Тип инициации платежа. CONSENT — списание по согласию" — no brackets, fine. But contains `—` (em dash) — fine in YAML.
- PaymentRequest.consentId: "Обязателен при initiationType=CONSENT" — fine.
- ConsentRequest.validUntil: "Срок действия согласия (ISO 8601 UTC)" — parentheses fine? In flow mapping plain scalar, `(` is allowed. Yes.
- ConsentRequest.maxDebitsPerPeriod: "Лимит частоты списаний за период [ТРЕБУЕТ ПРОВЕРКИ]" — `[` breaks it. FIX.
- ConsentRequest.purpose: "Назначение подписки" — fine.

Also, let me double check the existing original descriptions I preserved: "Сумма в копейках" — fine.

So only one fix needed: the maxDebitsPerPeriod description.

But wait, the error was at line 117 column 29. Let me verify by reading the file to be sure which line. Actually the error trace says line 117. Let me just fix the `[ТРЕБУЕТ ПРОВЕРКИ]` description and re-validate.

Actually, let me also reconsider: are there other `[` in my descriptions? Let me grep the openapi for `[ТРЕБУЕТ`.

Let me fix the one place and also verify there are no other bracket issues by re-running validation.

Let me also consider: the `description` for validUntil has parentheses `(ISO 8601 UTC)`. In a flow mapping, plain scalars can contain `(` and `)` — these are NOT flow indicators. Only `,`, `[`, `]`, `{`, `}` are flow indicators. So `(ISO 8601 UTC)` is fine.

But wait, there's another subtlety: the description `Срок действия согласия (ISO 8601 UTC)` — actually the `(` immediately after a space is fine. OK.

Let me fix the maxDebitsPerPeriod description with quotes.

Let me read the exact current line to craft the edit.
OpenAPI содержит синтаксическую ошибку: в flow-mapping описания с `[ТРЕБУЕТ ПРОВЕРКИ]` `[` интерпретируется как начало flow-последовательности. Исправляю, закавычив скаляр.

  `edit(file_path="<HARNESS>/runs/cells/superpowers-r1/ws/openapi/tsp-api.yaml", old_string="        maxDebitsPerPeriod: {type: integer, description: Лимит частоты списаний за период [ТРЕБУЕТ ПРОВЕРКИ]}", new_string="        maxDebitsPerPeriod: {type: integer, description: 'Лимит частоты списаний за период [ТРЕБУЕТ ПРОВЕРКИ]'}")`

The line with `[ТРЕБУЕТ ПРОВЕРКИ]` is the maxDebitsPerPeriod. Also the validUntil description has `(ISO 8601 UTC)` which is fine, but let me also quote it to be safe? No, parentheses are fine. But actually, let me reconsider: in a flow mapping, a plain scalar with `(` is fine. But `date-time` — the `-` is fine. OK.

Actually, wait — let me also check the `format: date-time` — `date-time` plain scalar, `-` fine.

The only problematic scalar is `[ТРЕБУЕТ ПРОВЕРКИ]`. Let me quote it.

Let me also double-check there are no other `[` in the file that are NOT intended flow sequences. The enum lists `enum: [QR, CONSENT]`, `enum: [CREATED, QR_ISSUED, ...]`, `enum: [PENDING_APPROVAL, ...]`, `required: [...]` — all intended flow sequences. Only the description with `[ТРЕБУЕТ ПРОВЕРКИ]` is problematic.

Let me fix by quoting the description.

  `run_shell_command(command="python3 -c \"import yaml; d=yaml.safe_load(open('openapi/tsp-api.yaml')); print('openapi yaml OK; paths=', list(d['paths'].keys())); print(, description="Re-validate OpenAPI YAML after fix")`

Now re-validate the YAML.

  `run_shell_command(command="git status --short", description="Show working tree status")`

OpenAPI is now valid. All checks pass:
- OpenAPI YAML valid, paths and schemas correct.
- No `<!--` in docs/adr (adr-no-placeholders).
- No TODO/TBD/XXX in spine (spine-lints-clean).
- '99,95' still in nfr.md (nfr-measurable).
- 'только из состояния `PAID`' still in ADR-005 (unchanged, abs-credit-only-from-paid).

Now let me do a final git status/diff to confirm the changes and prepare the summary. Actually, I don't need to commit (user didn't ask to commit). But I should do a git status to confirm what changed and report faithfully.

Let me run git status and git diff --stat.

Actually, the user asked "Когда закончишь, кратко перечисли созданные и изменённые файлы." So I need to list created/changed files. Let me run git status to be precise.

Let me run git status --short.
Все проверки пройдены. Фиксирую итоговый состав изменений.


Everything is in place. Let me write the final summary. The user asked for a concise summary of created/changed files, and the task itself is the architectural package.

I should provide a final response that:
1. Briefly states what I produced (the package) and where the key decisions are.
2. Lists created and changed files.
3. Notes what remains for human architect (deliverable #7) — briefly, since it's already in the docs.
4. Notes that I followed the repo methodology and did not touch .arch-handoff (generated snapshot).

Per the brainstorming skill, the architectural path ends with the user reviewing the written spec. I should present the package and invite review, noting the decision points that remain for the human (which is deliverable #7).

I should keep it concise but cover the key points. The user is senior; a focused summary is best.

Let me also note verification results honestly: OpenAPI validated, fitness-constraint patterns checked (no placeholders, 99,95 present, spine clean). I did NOT run a full "arch control check" (that's a harness tool not available here), so I'll be precise about what I verified.

Let me write the final response in Russian (matching user's language).

Key content of final message:
- Package is ready for A3 decision and handoff.
- Core decision (ADR-008): consent = separate entity with state machine; debit = payment with initiationType=CONSENT (no QR_ISSUED); pull model; additive contracts; new AD-009 invariant.
- Impact: AD-001..006 unchanged (AD-002/AD-004/AD-007 extended, not broken); AD-008 extended (vendor obligations); AD-009 new.
- Files created/changed (list).
- What remains for human (short list).
- Verification done.

Let me write it concisely.

I'll list files as created vs changed, matching git status.

Let me produce the final answer.
Готово. Архитектурный пакет изменения «Рекуррентные C2B-списания по согласию (подписки СБП)» подготовлен поверх принятого решения, по методике репозитория (ADR-формат, spine-инварианты, аддитивное версионирование контрактов, измеримые NFR, гейты/приёмка/откат). `.arch-handoff/` (генерируемый снапшот) не трогал — правил только источники.

**Ключевое решение (ADR-008):**
- **Согласие** — отдельный объект с собственным автоматом (`PENDING_APPROVAL → ACTIVE`, терминальные `EXPIRED`/`REVOKED`/`SUSPENDED`) и неизменяемыми параметрами (максимум, срок, частота).
- **Списание = платёж** с `initiationType=CONSENT`, путь `CREATED → PAID → CREDITED → COMPLETED` (без `QR_ISSUED`); переиспользует идемпотентность, зачисление-из-`PAID`, возвраты-сагу.
- **Pull-модель**: списание инициирует ТСП; push-планировщик — deferred.
- Новый инвариант **AD-009** (Proposed): списание только по активному согласию, лимиты проверяются до списания, дубль невозможен.

**Влияние на принятую архитектуру:** AD-001, AD-005, AD-006 — без изменений; AD-002, AD-004, AD-007, AD-008 — Rule не меняется, расширяется состав (второй автомат, операции адаптера, обязательства вендора, ПДн/AML). Контракт ТСП расширен аддитивно (новые `/v1/consents` + опциональные `initiationType`/`consentId`), существующие потребители не ломаются.

**Созданные файлы:**
- `docs/adr/ADR-008-rekurrentnye-spisaniya-po-soglasiyu-podpiski-sbp.md`
- `docs/solutioning-recurring.md` (все 7 пунктов: маршрут, влияние, решение, контракты, NFR, приёмка/откат, «на решение человека»)
- `docs/spec/consent-state-machine.md`

**Изменённые файлы:**
- `openapi/tsp-api.yaml` (v0.2.0: `/v1/consents`, `ConsentRequest`/`Consent`, поля `initiationType`/`consentId`)
- `docs/contracts/tsp-api.md` (v0.2 draft: §3.6 согласия, поля списания, вебхуки `consent.*`, коды ошибок)
- `docs/nfr.md` (новый раздел 7 — измеримые NFR подписок)
- `ARCHITECTURE-SPINE.md` (AD-009, deferred «push-планировщик», версия контракта)
- `docs/solutioning.md` (scope/roadmap + строка ADR-008 в таблице)
- `README.md` (индекс и структура)

**Проверено:** OpenAPI валиден (пути и схемы разобраны), в `docs/adr` нет HTML-плейсхолдеров, в spine нет `TODO/TBD/XXX`, маркер `99,95` в `docs/nfr.md` сохранён — фитнес-констрейнты репозитория не нарушены.

**Остаётся на решение человека-архитектора** (полно — в `docs/solutioning-recurring.md` §7): ратификация ADR-008/AD-009 на A3; стратегическое размещение (feature-spine vs новый initiative); подтверждение pull vs push бизнесом; протокол НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`; включение consent/debit в RFP вендора; комплаенс по ПДн/AML. Пакет готов к вынесению на архитектурное решение — прошу ревью перед передачей исполнителям.
