<!-- источник: <HARNESS>/runs-v2/cells/wh5tt2i/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-v2-cells-wh5tt2i-ws/chats/0c98be22-7464-48a6-85ff-35f33d98e1f9.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/ARCHITECTURE-SPINE.md")`

Let me start by understanding the repository. The task is an architecture task. Let me first check for skills — the superpowers skill says I must invoke relevant skills before responding. But the user instructions here: "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению."

Let me explore the repository first. Actually per using-superpowers, I should invoke a skill first. Which skill applies? This is architectural work — creating a change package on top of an accepted solution. There's no specific "architecture" skill in the list except superpowers:brainstorming (before creative work). Hmm. But brainstorming skill would engage in dialogue with the user. The task is quite well specified. Let me look at the repo first to understand `.arch-handoff/` rules — that's likely where the "methodical skills" live.

Actually let me be careful: the repo contains `.arch-handoff/TASK.md`, `RUBRIC.yaml`, `CONSTRAINTS.yaml`, `MANIFEST.json`. These likely define the process. Let me read them.

Let me start exploring.
Начну с изучения принятого решения и правил пакета передачи — `.arch-handoff` задаёт методологию работы в этом репозитории.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/.arch-handoff/ARCHITECTURE.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/README.md")`
  `run_shell_command(command="ls -la <HARNESS>/runs-v2/cells/wh5tt2i/ws/ && echo \"--- docs ---\" && ls -R , description="List project tree and docs")`

So the TASK.md is for a code harness (walking skeleton). But the user's request is a different task: architecture change package for recurring C2B payments (SBP subscriptions). The `.arch-handoff/` is a handoff package for the *previous* task. The user says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — accepted decision files should be changed only in the manner accepted in this repo.

Let me check RUBRIC.yaml, ARCHITECTURE.md, README.md, docs/, and ADR dir. Also check for any methodology skills/tools installed ("В проекте могут быть установлены методические навыки и инструменты"). Let me look for .qwen, opencode, .claude, etc.

Let me read more.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wh5tt2i && echo \"=== home/.qwen/skills ===\" && l, description="Inspect installed skills and extensions")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/spec/state-machine.md")`

Let me check the installed skills in home/.qwen/skills and extensions, and also the git log to understand the repo conventions. Also read docs/solutioning.md, docs/nfr.md, contracts, spec/state-machine.md, openapi/tsp-api.yaml.

Let me check the skills dir first.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/tsp-api.md")`
  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wh5tt2i/ws && git log --oneline -20 && echo \"=== , description="Read ADR-007 and git log")`

Now let me read solutioning.md, contracts/tsp-api.md, contracts/opkc-adapter.md, openapi/tsp-api.yaml, and the ADR-007. Also check the git log for conventions of how files are changed. And check if there's a methodology skill/tool — the superpowers extension is installed. There's likely a "brainstorming" skill and "writing-plans" skill. The task says "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." Superpowers extension with brainstorming/writing-plans skills seems to be the methodology.

Per the using-superpowers rule, I should invoke relevant skills before responding. This is creative/design work → superpowers:brainstorming. Hmm, but brainstorming skill typically requires dialogue with human partner. Let me consider. The task is substantial: an architecture change package. The superpowers brainstorming skill "You MUST use this before any creative work". Let me read it and decide. But it may want to ask questions. There's also a possibility the repo has its own methodology (the docs structure: solutioning, nfr, adr, spec, contracts, rfp, arch-handoff). The "принятый в этом репозитории способ" изменения принятых файлов: spine blocks have Status: Proposed (ADR-XXX) and get ratified; ADRs are added as new files ADR-008 etc.; README updated; docs/spec updated. So changing accepted decision files = add new ADR, ratify spine block, update docs.

Let me look at the rest of the files first, then decide about skills. Let me read solutioning.md, tsp-api.md, opkc-adapter.md, tsb openapi, ADR-007, ADR-005, and git log.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/openapi/tsp-api.yaml")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/opkc-adapter.md")`

Now let me read the openapi/tsp-api.yaml and the opkc-adapter contract, ADR-005, ADR-004, ADR-002 fully, and ADR-006. Also check whether there's a methodology tool/skill installed in the project (e.g., `.qwen`), and check the superpowers extension skills list for something relevant like "brainstorming", "writing-plans".

Let me read those files.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wh5tt2i/home/.qwen/extensions/superpowers/skills &, description="List superpowers skills")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/adr/ADR-005-integraciya-s-abs-zachisl)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/adr/ADR-004-at-least-once-dlq.md")`

Now let me read ADR-002 fully, ADR-004, ADR-005, ADR-006, and the vendor RFP. And ADR-001 remainder. Actually I have enough for most. Let me read ADR-002, ADR-004, ADR-005 fully since subscriptions touch them heavily.

Let me also decide on methodology. The task mentions "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." The superpowers extension is installed with skills: brainstorming, writing-plans, systematic-debugging, etc. This task is architecture design work (creating a change package). The most fitting: `superpowers:brainstorming` (before creative work) and `superpowers:writing-plans`. Also possibly there's a project-specific skill. The home/.qwen/skills is empty.

Hmm. But the repo's own methodology is: spine + ADRs + docs (solutioning, nfr, spec, contracts, rfp, arch-handoff). The "accepted files changed only the accepted way" = new ADR files, spine Status updates with ratification via ADR, README version list.

Let me be pragmatic: I'll invoke `superpowers:brainstorming` since it's mandated before creative work and would help structure. But brainstorming skill typically is a dialogue that ends with a design doc. Given the task is well-specified and asks for a deliverable package, maybe better to use it lightly. Let me read the brainstorming SKILL.md to see what it demands. Also check `writing-plans`.

Actually, the instruction says "use them as intended" — the project may have "методические навыки" (methodological skills). Let me check the superpowers skills directory for something architecture-specific.

Let me list skills.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wh5tt2i/ws && echo \"=== all md files ===\" && fin, description="Find significance scheme and read ADR-002")`

I now have a solid understanding. Let me read the brainstorming skill's remainder to classify paths. The skill says architectural path: for architectural work, write a spec, get approval, then writing-plans. But the user's explicit deliverable is an "архитектурный пакет" with 7 sections, and "Код не пиши". This is architectural work. The HARD-GATE requires human approval of written spec before... but here the deliverable IS the spec/package. The user explicitly asked for the package. Per "User instructions take precedence over skills". So I can produce the package.

However, the using-superpowers rule says announce "Using [skill] to [purpose]" and follow. I think the right move: invoke `superpowers:brainstorming` (process skill, architectural path) to structure, but I should be careful — the skill wants a design spec and approval. The user's request is essentially already a design-brief and they want the artifact. Given the ambiguity, and the CLI interaction mode, I could use ask_user_question to clarify a couple of load-bearing decisions (e.g., scope of the change package, whether to modify accepted spine files or produce a new change package). Actually the user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — this is guidance, not asking.

Hmm, but is there really a need for clarification? Let me think about the deliverable: an architecture change package. The repo has an established pattern for this exact situation: a new feature on top of adopted solution → new ADR(s), spine block(s) status change (Proposed → adopted via ADR ratification), updates to docs/contracts, docs/nfr, docs/spec, openapi. Plus an `.arch-handoff` style package? Actually the `.arch-handoff` is the handoff to code harness. The user says "подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям." So: a package for the architecture decision gate (A3-like) and then handoff.

Given "вынести на архитектурное решение" — the package should include the ADR (proposed, not accepted), impact assessment, contract changes, NFR, acceptance criteria + rollback, and open questions for the human architect.

Now, important: the change is significant. Subscriptions (рекуррентные C2B-списания по согласию плательщика) in SBP. This is a real thing: СБП "подписки" / "Автоплатёж" — there's a mechanism where a payer gives consent (согласие на периодические списания) and merchants can initiate payments without QR each time. In NSPK there's "СБП: Автоплатёж (закладка)". Let me think about the actual architecture implications.

Key aspects:
1. New entity: `mandate`/`subscription` (согласие плательщика на рекуррентные списания) — consent lifecycle: registration (with payer action, likely via QR/deep link in bank app), activation/confirmation, revocation by payer, expiry.
2. New flow: recurring debit (charge) — merchant initiates debit referencing mandate; payer's bank confirms (possibly without action if within consent limits); funds credited as C2B payment.
3. New states in state machine: mandate states; payment gains a new origin (`RECURRING`/`DEBIT`) and new pre-states (e.g., `DEBIT_REQUESTED`, `AUTHORIZED`).
4. Invariants: AD-005 (credit only from confirmed status) — the confirmed status for recurring is the bank-payer's confirmation of debit, not QR PAID. Need to map. AD-002 status machine extended. AD-003 idempotency keys extended: consent id, debit id. AD-004 single OPKC adapter — recurring protocol still goes through adapter; adapter contract must be extended with mandate operations. AD-001 isolation — mandate data is financial/PII → stays in gateway. AD-006 trust zones — payer consent may involve payer's bank app via NSPK, no new bank-side channel; but revocation flows. AD-007 audit — consent changes are administrative/financial events → audit log.
5. PII: payer's phone number / bank account are PII → AD-007 requirements; new data classes.
6. New contract methods on TSP API: consent registration, debit initiation, consent status, revocation (merchant or payer-initiated), list debits.
7. NFR: new latency for debit initiation, consent lifecycle SLO, idempotency of debits, no double debit (analogous to no double credit), notification of payer/merchant, retry semantics.
8. Acceptance criteria and rollback.
9. Open questions for human architect: whether NSPK supports this in the bank's contract; regulatory basis (согласие плательщика, 161-ФЗ, «периодические списания»), limits, TTL, whether full-vendor/hybrid transport covers mandate protocol (ADR-007 constraint), whether to modify AD-005 wording.

Also need to think about "что не меняется": core isolation, outbox, status machine as single source of truth, ABC integration semantics (credit only from confirmed), adapter-only NSPK.

Route/significance: This is a new capability with financial and regulatory risk, new external protocol (mandate), PII, irreversible-ish consent semantics. Likely route Critical or High. The original was Critical 11/15. Let me use the repo's significance scoring if defined. There's no explicit rubric in repo for significance, but solutioning says "Маршрут: Critical (значимость 11/15)". Let me check if there's a scoring doc. The docs mention `docs/SOURCE_BRIEF.md §A.3` in RUBRIC — not present. So significance scoring is probably a known BMAD-like scheme. I'll construct a significance assessment with rationale and route (e.g., "Critical, значимость N/15") — but I should be careful about inventing the exact scale. Maybe better: assess along dimensions and state route as "Critical (требуется архитектурное решение A3 + ревью ИБ/комплаенс)".

Let me check if there's a scoring file anywhere.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/adr/ADR-002-model-konsistentnosti-pla)`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/adr/ADR-003-mtls.md")`

I have enough context. Let me read the remainder of ADR-002 lines 1-25 and ADR-006, ADR-003, vendor-rfp quickly for completeness (they may matter: ADR-006 trust zones for PII consent; ADR-003 mTLS; vendor RFP adapter scope).

Let me read ADR-002 fully (it's 54 lines, I saw most) and ADR-006 / ADR-003 headers, plus vendor-rfp.

  `skill(skill="superpowers:brainstorming")`

I have a comprehensive picture. Now my plan:

The deliverable: an architecture change package. Per repo convention, accepted artifacts are: spine (AD-NNN blocks with Status: Proposed (ADR-XXX) → ratified), docs/adr/ADR-*.md (new ADRs to ratify), docs/solutioning.md, docs/nfr.md, docs/spec/*, docs/contracts/*, openapi/tsp-api.yaml, README.md.

The user says: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." This means: don't rewrite accepted ADRs to sneak in changes; instead follow the repo's way — add a new ADR, mark spine block as proposed for a new ADR, update docs by adding sections. Actually, hmm — accepted files: ADR-001..007 (mostly Proposed, ADR-007 Accepted), spine. The "принятый способ" = a new ADR + spine block, versioned. Since it's a change to a solution that has been "принято" (accepted) but this new change is being prepared for an architecture decision (not yet decided), the correct move is to produce a *change package* that includes a **Proposed** ADR (not Accepted), plus impact/contracts/NFR/acceptance/rollback sections — so it can be taken to the architecture decision (A3-like) and then handed off.

So I'll create files:
1. `docs/changes/recurring-c2b/CHANGE-PACKAGE.md` — the main package (sections 1-7). Hmm, but maybe better to fit repo layout. The repo has no `docs/changes/`. Let me think about the "принятый способ": spine is feature level; a new feature (subscriptions) is arguably a new feature-level spine or an extension. The task says "поверх принятого решения" (on top of). Options:
   - Add ADR-008 for the mandate/recurring model (new file `docs/adr/ADR-008-...md`, Status: Proposed).
   - Add a spine block AD-009 (recurring) — but changing ARCHITECTURE-SPINE.md needs the accepted way: blocks with Status: Proposed (ADR-XXX). Adding a new Proposed block bound to ADR-008 is consistent.
   - Create `docs/spec/mandate-state-machine.md` (new spec) — analogous to state-machine.md.
   - Update `docs/contracts/tsp-api.md` with new methods (additive, marked), `docs/contracts/opkc-adapter.md` with new adapter ops.
   - Update `openapi/tsp-api.yaml` additively (new paths/schemas, keep existing intact) — bump version 0.1.0 → 0.2.0.
   - Update `docs/nfr.md` with new measurable NFRs.
   - Update `docs/solutioning.md` (add change section) — or better create a change package document.
   - Update README to reference the change.
   - `.arch-handoff/` — the handoff package. The user says "затем передать исполнителям". So maybe add a handoff-style package for this change too. But the existing .arch-handoff is for the walking skeleton task. Overwriting it would break the accepted handoff. Better: create `.arch-handoff/` extension? Hmm. The RUBRIC/manifest describes the handoff package for the *current* task (walking skeleton). Since this is a *change on top*, and the change is not yet decided, the handoff to executors comes after decision. I think the deliverable should include an "epic-context / handoff brief" for the implementers in the change package, but not overwrite `.arch-handoff`.

Given the user explicitly asked for 7 things and "передать исполнителям", the cleanest deliverable is one primary document: `docs/changes/recurring-c2b/CHANGE-PACKAGE.md` containing all 7 sections, plus the concrete artifact updates (ADR-008, spine AD-009 block, spec, contracts, openapi, nfr, solutioning, README).

But wait — "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." Maybe it means: I should be careful and not break accepted artifacts, but the repo's way of evolving them IS to add ADRs and spine blocks. So modifying `ARCHITECTURE-SPINE.md` by adding a new block is fine. Modifying `openapi/tsp-api.yaml` additively is fine (versioning rules in tsp-api.md §6 say additive optional fields are backward compatible).

Hmm, but should I be more conservative and NOT edit the accepted openapi/spine, instead putting proposed changes into the change package? The user asked: "4. Изменения контрактов (openapi/tsp-api.yaml) без поломки существующих потребителей." — so they want the actual contract changes. I think producing the updated openapi yaml (additive, version bump) is right, plus documenting.

Let me reconsider scope and avoid over-engineering. The user wants a coherent architectural package. Let me plan files:

Primary deliverable (the package for architectural decision):
- `docs/changes/recurring-c2b/RECURRING-C2B.md` — main architecture change package: 1) significance & route; 2) impact on accepted architecture (invariants touched/unchanged); 3) architecture decision with alternatives, consequences, reversibility; 4) contract changes; 5) measurable NFR; 6) acceptance criteria & rollback; 7) what remains for human architect.

Supporting artifacts (the repo's accepted way of encoding decisions):
- `docs/adr/ADR-008-recurring-c2b-mandate.md` — Proposed ADR (the decision).
- `docs/spec/mandate-state-machine.md` — mandate/consent + recurring debit state model & transitions.
- `docs/contracts/tsp-api.md` — additive new section with new methods (consent & debits).
- `docs/contracts/opkc-adapter.md` — additive new adapter operations (mandate ops).
- `openapi/tsp-api.yaml` — additive paths/schemas; bump version to 0.2.0.
- `docs/nfr.md` — add section 7 with new measurable NFRs.
- `ARCHITECTURE-SPINE.md` — add AD-009 block (Status: Proposed (ADR-008)) + note in contract versions. Also note impact on AD-005 mapping.
- `docs/solutioning.md` — add a "Изменение" section? Maybe add to §9 gaps and §10 open questions, and roadmap. Hmm, editing solutioning is risky/heavy. I'll add a short section pointing to the change package. Actually better: keep solutioning as the baseline and add a brief pointer + new gaps.
- `README.md` — update structure and status.
- `.arch-handoff/` — produce an executor handoff brief for this change. Since the existing handoff package is task-specific and complete, I'll add a new one? The rubric-based handoff is for the code harness. Hmm. "затем передать исполнителям" — the package must be enough. I think including an "epic-context / handoff" section in the main package is enough, plus maybe a `.arch-handoff`-style file. But to avoid confusing the existing handoff, I'll create `docs/changes/recurring-c2b/handoff/` ... Hmm, over-engineering.

Let me re-read the user's ask: "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям." So the package serves two consumers: (a) the architecture decision body (human architect), (b) executors. And item 7 = what remains for the human architect.

I think a single well-structured main doc + the encoded artifacts is right. For executors, add an "Epic-context для исполнителей" section (distilled, 800–1500 tokens per rubric) and acceptance criteria. Perhaps also extend `.arch-handoff`? I'd rather create a new handoff folder that doesn't collide: `.arch-handoff/changes/recurring-c2b/`? Hmm, but `.arch-handoff/TASK.md` etc. are the walked skeleton's. Actually since the change ADR is Proposed, handoff to executors shouldn't be finalized until decision. So in the package, include a "handoff brief" section (ready-to-use epic-context) but don't overwrite `.arch-handoff/`.

Hmm, let me reconsider whether I should ask the user a clarifying question. The interaction mode: default. The task is fairly clear. But there's a genuine ambiguity: should I (a) only produce a proposal package without touching accepted files, or (b) also apply additive changes to accepted artifacts (spine, openapi, nfr, contracts, README)? The instruction "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" suggests (b) is allowed as long as done the repo's way. I'll go with (b) but keep changes strictly additive and versioned, and clearly mark Proposed/New. I think asking would be good practice but the user gave enough guidance. Let me use ask_user_question once to confirm the approach and depth? The mandate says use it when needed. Given the size, I'll ask one focused question about the desired output shape (single package doc + additive artifact edits, vs. only a proposal doc), and about whether to include the real NSPK protocol uncertainties.

Hmm — actually, the superpowers:brainstorming skill HARD-GATE says for architectural work, write a spec and get approval before implementation. Since "Код не пиши" and deliverable = documents, the "implementation" is writing docs. But the user explicitly asked for the package, so that's the approval. The skill says classify and announce. I'll invoke the skill and follow the architectural path: I can write the spec (the package) because the request supplies purpose and constraints. But the HARD-GATE wants approval of the spec before invoking writing-plans. I'm not going to write an implementation plan (that's for executors). Actually item "затем передать исполнителям" suggests I should include what's needed for handoff, but the actual handoff package generation could be a later step.

Given the complexity and the explicit deliverables, I'll:
1. Invoke superpowers:brainstorming to classify (announce), confirm understanding.
2. Possibly ask 1 clarifying question via ask_user_question about the output shape.
3. Produce the package + artifacts.
4. Verify (lint: the CONSTRAINTS fitness rules, e.g., no `<!--` in adr/*.md, nfr must contain '99,95', ADR-005 pattern, README exists).

Let me check the fitness rule: `adr-no-placeholders` = must_not_contain glob docs/adr/*.md pattern '<!--'. So my new ADR must NOT contain `<!--`. Good to know.

`nfr-measurable` = docs/nfr.md must contain '99,95'. Already there; if I rewrite, keep.

Let me now decide the significance route. The existing scheme is "значимость N/15". I need to derive for the change. Dimensions likely: (1) new external integration? (2) financial impact? (3) data/PII? (4) regulatory/compliance? (5) irreversibility? etc. I can construct a defensible scoring. Since original was 11/15 Critical, the change is comparable (adds new protocol, new PII, new regulatory basis) → maybe 10/15 or 12/15. I'll present a 5-dimensional assessment (each 0–3) summing to /15 with components and justify. Let me define 5 axes aligned with the repo's reasoning (new component/external integration, financial influence, data/PII, regulatory, reversibility/rework). Actually the original's rationale: "новый компонент, интеграция с внешним оператором, финансовое влияние, КИИ" — 4 axes plus maybe "изменение контрактов/влияние на существующее". Let me define:
- Новизна/внешняя интеграция (новый протокол подписок НСПК): 3
- Финансовое влияние (рекуррентные списания, риск двойных списаний): 3
- Данные/ПДн (согласие плательщика, реквизиты, лимиты): 2
- Регуляторный/КИИ (согласие, 161-ФЗ, ПОД/ФТ, аудит): 3
- Обратимость/влияние на принятое решение (расширение статусной машины и контрактов, но ядро сохраняется): 2 → hmm. Original 11. Sum=13 → Critical. Maybe 3+3+2+3+1=12. Let me set reversibility/scope = 2 → 13/15. Hmm, but graded "significance" typically higher = more significant. Let me say 12/15 Critical. Actually let me keep it consistent with a plausible 15-point scale: I'll present 5 criteria 0–3 and total. Let me settle: 3,3,2,3,1 = 12/15 → route Critical, requires full ADR + human A3 (mandate). Difference from baseline (11) explains "deeper than a bounded change".

Hmm, actually I want to be careful not to invent an authoritative scale that conflicts. The repo only says "Critical (значимость 11/15)". I'll present my own transparent 5-axis breakdown (state that the axis decomposition is my working model, to be confirmed), giving a route recommendation. That's defensible and item 7 can flag it.

Now the core architecture content. Let me design the recurring C2B (SBP subscriptions / автоплатёж) model properly.

**Business**: TSP (online cinemas, utilities, telecom) wants recurring C2B debits with payer consent — SBP subscriptions. Today each payment requires QR + client action.

**NSPK reality (as of knowledge)**: СБП "Автоплатёж" / "подписки" mechanism: payer sets up a mandate/consent in their bank app (via ТСП's site/app → СБП → bank), merchant gets a mandate ID; then merchant initiates "Списание по подписке" (debit request) which goes to payer's bank; payer bank confirms (possibly silently within consent parameters: max amount per period, period, max total, validity). This is the "СБП: Регулярные платежи / Автоплатёж". Protocol details [ТРЕБУЕТ ПРОВЕРКИ]. Also there's "Платежи по согласию" / "СБП Pay". I must mark protocol specifics as [ТРЕБУЕТ ПРОВЕРКИ] consistent with repo convention.

**Architecture design**:

New bounded capability "Подписки СБП (mandates + recurring debits)" within the existing gateway (not a new component — reuse isolation, outbox, status machine, adapter, notifier, reconciliation). Key new concepts:

1. **Mandate (согласие плательщика)** — new aggregate with its own lifecycle:
   - `DRAFT`/`CREATED` (шлюз зарегистрировал запрос на согласие) → `PENDING_PAYER` (передан в НСПК, плательщик в своём банке подтверждает) → `ACTIVE` (согласие действует) → `SUSPENDED` (приостановлено, напр. по решению ТСП или банка) → `REVOKED` (отозвано плательщиком/банком) / `EXPIRED` (истёк срок) / `REJECTED` (плательщик отказал или банк отклонил).
   - Mandate attributes: `mandateId`, `tspId`, `payerRef` (opaque/токенизированная ссылка, не открытые ПДн), лимиты (maxAmountPerPeriod, period, maxTotalAmount, validUntil), purpose, status, timestamps. ПДн минимизация (ADR-006).
   - Key: mandate is **финансово значимый** and **ПДн** → audit + isolation.

2. **Recurring debit (рекуррентное списание)** — a payment initiated by the TSP against an ACTIVE mandate, without the payer scanning a QR. It reuses the payment state machine but with a new entry path and an **authorization step at payer's bank**:
   - New states/transition: payment created in `CREATED` → (debit registered in NSPK) `DEBIT_PENDING`/`AUTHORIZING` → `PAID` (подтверждено банком плательщика) → `CREDITED` → `COMPLETED` (reuse downstream), terminal FAILED/EXPIRED/REFUNDED.
   - **Crucial invariant mapping**: AD-005 "зачисление только из PAID" still holds — `PAID` for a recurring debit means "подтверждено банком плательщика/НСПК по согласию". The definition of `PAID` must be extended (ADR-002 canonical states list) to cover both QR-payment confirmation and mandate-debit confirmation. This is the key invariant tension: AD-005 semantics preserved, but the *source of confirmation* broadens. And critically: **a debit request is NOT a payment** — no crediting from `DEBIT_PENDING`.
   - Also a new **pre-authorization** distinction: the debit may be declined (insufficient funds / limit exceeded / mandate revoked) → terminal FAILED, and **no ABC call**.
   - Amount must be validated against mandate limits *before* sending to NSPK (guard) and again against confirmation.

3. **Idempotency (AD-003)** extended:
   - mandate registration: `Idempotency-Key` (TSP) → same `mandateId`.
   - debit: `Idempotency-Key` + business key = (`mandateId`, `merchantOrderId`/period) → **не более одного успешного списания на период согласия** (это новый инвариант — защита от двойного списания подписчика). This is the analog of "no double credit" but for the payer side — arguably the most important new invariant. Need a new spine block AD-009.
   - NSPK debit notifications: dedupe by `eventId` (existing).
   - ABC credit idempotent by `paymentId` (existing).

4. **AD-004 (single OPKC adapter)** extended: mandate operations (`registerMandate`, `getMandateStatus`, `revokeMandate`, `createDebit`, `getDebitStatus`, mandate events `mandate.activated/rejected/revoked`, `debit.paid/rejected/expired`). All protocol specifics inside adapter. **This is an extension of the adapter contract → RFP/adapter scope change → depends on vendor & NSPK documentation.** Important: if the vendor's transport module doesn't support mandate protocol, ADR-007 hybrid constraint could break → open question for architect.

5. **AD-001 isolation** — mandate data stays in gateway payment contour; no direct calls; RPO=0 for mandates (a lost ACTIVE mandate = broken subscription / inability to debit). New: **RPO=0 for mandate and consent state**.

6. **AD-006/AD-007** — consent is ПДн-adjacent and regulated (согласие на периодические списания per 161-ФЗ / ГК ст. 1102? Actually 161-ФЗ ст. 4 + правила; and the "согласие плательщика" mechanism is defined by NSPK rules). Audit all mandate lifecycle and debit events; 4-eyes for manual revoke/suspend. Payer notification requirements (bank must notify payer of each debit per NSPK/legislation) — likely handled by payer's bank (NSPK), but the gateway/merchant must respect revocation. Need legal basis.

7. **Notifications to TSP** — new webhook events: `mandate.activated`, `mandate.rejected`, `mandate.revoked`, `mandate.expired`, `debit.completed` (or reuse `payment.completed` with new fields), `debit.failed`. Additive.

8. **Reconciliation** — extend hourly NSPK recon to mandates and debits; daily ABC recon unchanged. New metric: не более одного успешного списания на период.

**Alternatives** for the decision (item 3):
- A. Extend existing gateway core (reuse status machine/outbox/adapter/notifier) — recommended. Pros: reuse invariants, isolation, RPO, one source of truth; Cons: core complexity grows, status machine must generalize `PAID` source, mandates add PII/regulatory surface.
- B. Separate microservice "Subscriptions service" with own DB, calling gateway — Pros: independent evolution, blast-radius isolation; Cons: second source of truth / distributed consistency between mandate and payment, cross-service saga, violates "single source of truth" spirit, more operational cost.
- C. Store mandates in ABC / bank's subscription system (not gateway) — Pros: reuse existing ABC standing-order machinery; Cons: ABC has no SBP semantics, breaks AD-001/AD-004 isolation, no outbox/idempotency, regulatory audit gap.
- D. Vendor "full" subscriptions module — Pros: fast, certified; Cons: vendor lock-in of financial logic, audit difficulty for CB, breaks hybrid strategy ADR-007 boundary.

Reversibility: adding mandates as an additive capability → **reversible** (feature flag per TSP; extension of states is backward compatible; existing QR flow untouched). But once mandates are ACTIVE and debits run in prod, revoking the capability requires honoring existing consents → operational/regulatory commitment → "reversible technically, costly operationally once live". Rate it `reversible` technically / `costly` after live consents (like ADR-001 style).

**Item 4 — Contract changes without breaking consumers**:
- Additive only: new paths under `/v1/` with new resource names; new optional fields; no change to existing required fields/enums; existing `status` enum extended?? Careful: adding enum values to a response field CAN break strict consumers. Solution: introduce a **new status field or new resource** for debits, and keep `Payment.status` enum as-is where possible; if a new payment state (`DEBIT_PENDING`) must surface, use a *new optional field* `origin: QR|MANDATE` and add state only in v0.2 with deprecation notes... Actually strictly, adding a value to an existing enum is a compatibility risk. The repo's tsp-api.md §6 says "Добавление опциональных полей — обратно совместимо". Adding enum values is not covered → must be guarded. Recommendation: expose debit as a separate resource `/v1/mandates/{mandateId}/debits` and `Debit` schema; for payments created from a mandate, keep `Payment` schema but add optional `mandateId` + `origin` fields and **document that `status` may contain `DEBIT_PENDING` starting v0.2** (a known minor break → release-note + contract test + ≥6 мес support). Alternatively keep debit statuses inside the Debit resource and represent the resulting payment as existing states (PAID is the first visible state) → zero enum change. I'll recommend the latter as the conservative option and note the trade-off. This is exactly the "without breaking consumers" requirement — good content.

OpenAPI yaml: add new paths/schemas additively; bump `info.version` 0.1.0 → 0.2.0-draft; keep all existing paths/schemas byte-identical (except version). Note: existing `PaymentRequest` has `required: [amount, merchantOrderId]` and no `qrType` — I won't touch it.

**Item 5 — measurable NFRs** for the new functionality:
- Mandate registration: p95 latency of `POST /v1/mandates` < 500 ms (без учёта НСПК/действий плательщика), отдача ссылки/QR согласия.
- Mandate activation end-to-end: p95 < 30 с после подтверждения плательщиком в банке (нотификация НСПК → статус ACTIVE + вебхук ТСП) — target per existing notification p95 <5s actually; mandate activation = notification path → p95 < 5 с от события НСПК. Hmm, the payer action dominates. I'll set: от события НСПК о согласии до `ACTIVE`+вебхук — p95 < 5 с (consistent with §2 notification NFR).
- Recurring debit: `POST /v1/mandates/{id}/debits` p95 < 500 мс; время зачисления p95 < 60 с from confirmation (reuse).
- Idempotency/durability: **двойных списаний на один период согласия — 0**; двойных зачислений — 0; повторная доставка не меняет состояние — 100%.
- Availability: capability availability ≥ 99,95% same; но "отказ функции подписок не должен ронять приём разовых QR-платежей" → fault isolation test.
- RPO for mandate state = 0.
- Limit enforcement: 100% списаний проверены на лимиты согласия до отправки в НСПК; 0 списаний сверх лимита.
- Reconciliation: mandates and debits included in hourly NSPK recon; расхождений 0.
- DLQ alert ≤5 мин (reuse); lag ≤60s.
- Notification of payer: не в контуре банка-эквайера? Actually the acquirer is not the payer's bank; payer's bank notifies. So TSP-facing only.
- PII: payer identifier stored tokenized/masked — 100% masked in logs.
- Throughput: subscription debits add load; sustained target maybe +X TPS; state: ≥200 TPS total sustained, bundles.

**Item 6 — acceptance criteria & rollback**:
Acceptance (testable):
- AC1: `POST /v1/mandates` twice with same Idempotency-Key → same mandateId, no second mandate.
- AC2: debit only from ACTIVE mandate; from PENDING/REVOKED → 422, no NSPK call.
- AC3: debit amount > limit → 422 `AMOUNT_EXCEEDS_MANDATE_LIMIT` before NSPK; no debit registered.
- AC4: NSPK duplicate debit.paid eventId → state unchanged, no second credit.
- AC5: credit only from confirmed debit (`PAID`) — from DECREATED/PENDING unreachable (fitness).
- AC6: revocation by payer → subsequent debit fails; no credit; TSP webhook `mandate.revoked`.
- AC7: ABC unavailable → debit stays PAID, retries, no dup; recon catches.
- AC8: existing QR flow regression: all v0.1 contract tests pass unchanged; no enum/field removal.
- AC9: contract diff (oasdiff) v0.1→v0.2 reports only additive changes.
- AC10: no more than one successful debit per (mandate, period) enforced — concurrent double submit → one 201, one idempotent/409.

Rollback:
- Pre-decision: no code → nothing to roll back.
- Pre-production: feature off by default.
- Post-activation: **feature flag per TSP/segment** on TSP-API for mandate registration; disable `POST /v1/mandates` stops new consents; existing debits continue (must honor active consents) or a "stop-new-debits" switch; revoke-all runbook for emergency (payer protection) — coordinated with NSPK; data not migrated back (mandates remain in gateway until revoked/expired); QR flow unaffected.
- Signals/triggers: доля отказов списаний, двойные списания (any), расхождения сверки > порога, инцидент ПДн, inability to revoke. Owner: архитектор + владелец продукта + ИБ; decision body A3.
- Criterion of successful rollback: QR-приём работает, mandates недоступны для новых регистраций, активные согласия отозваны/истекли планово, 0 необработанных списаний.

**Item 7 — what remains for the human architect**:
- Решение по варианту (A/B/C/D) — ADR-008 ratification (A3-like gate).
- Внешний вход: подтверждение, что механизм рекуррентных списаний (Автоплатёж/подписки) доступен банку по договору с НСПК, и получение документации протокола (mandate ops, тайминги, лимиты, форматы) — currently [ТРЕБУЕТ ПРОВЕРКИ].
- Совместимость с ADR-007 hybrid: поддерживает ли вендорский транспортный модуль mandate-операции; иначе пересмотр границы контракта/выбор вендора.
- Юридическое основание/согласие плательщика, требования к уведомлению плательщика о каждом списании, лимиты (161-ФЗ, правила НСПК) — ИБ/комплаенс/юр.
- Изменение формулировки AD-005/AD-002 (расширение смысла `PAID`) vs добавление нового состояния — решение уровня spine (эскалация на родительский spine, т.к. это расширение semantics).
- Решение о версии контракта (v0.2 vs v2), политика по enum.
- Приоритет/roadmap, коммерческие условия.
- Категорирование ПДн/КИИ для mandate-данных.
- Точное определение "периода" согласия и защиты от двойного списания (бизнес+юр).

Also note: parent spine escalation — mandate introduces "согласие плательщика" which may belong to a parent-level initiative. The spine rules say conflict escalates.

Now "Изменение значимости и маршрута" — I'll give the 5-axis breakdown.

Now, about the "принятый способ" for changing accepted files: I'll:
- Add `docs/adr/ADR-008-recurring-c2b-mandate.md` (Status: Proposed) — new file, consistent with ADR-001..007 naming.
- Add a spine block `AD-009. Рекуррентные списания по согласию плательщика (подписки СБП)` with Status: `Proposed (ADR-008)`, in the same format.
- Note in spine "Контракты и версии" that TSP API goes to v0.2 draft (additive).
- Add `docs/spec/mandate-state-machine.md`.
- Extend `docs/contracts/tsp-api.md` additively (new §3.6+ methods, new §5 webhook events, bump version note).
- Extend `docs/contracts/opkc-adapter.md` additively (new ops §3 + events §4 + RFP requirements §8).
- Update `openapi/tsp-api.yaml` additively, version 0.2.0.
- Extend `docs/nfr.md` with §7.
- Update `docs/solutioning.md`: add a short §11 "Изменение: подписки СБП" pointer + update roadmap line (§1 says автоплатежи вне scope) and gaps/open questions.
- Update `README.md`.
- Main package: `docs/changes/recurring-c2b/ARCH-CHANGE-PACKAGE.md`.

Hmm, that's a lot of files. Let me consider whether editing solutioning.md is wise. The roadmap line in solutioning §1 says "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." Now autopayments move in scope → I should update that line and add a pointer. That's a legitimate accepted-way change. Also §10 open questions.

Also I should think: does the change need a new parent-level spine? The spine is feature-level. Adding AD-009 is right.

Also a **fitness constraint**? CONSTRAINTS.yaml rules are for the code harness stage; I might add a rule for the new invariant (e.g., new ADR file exists, mandate state machine contains the invariant). Hmm — CONSTRAINTS.yaml is "Fitness-правила для arch control check, этап решение". Adding a rule for the new change could be appropriate: e.g., `mandate-no-double-debit` must_contain in the new spec, and `adr-008-present`. But careful: adding rules that must pass. I could add:
  - name: adr-008-present (file_exists docs/adr/ADR-008-...)
  - name: mandate-single-source (must_contain docs/spec/mandate-state-machine.md pattern 'не более одного успешного списания')
  - name: spine-mandate-invariant (must_contain ARCHITECTURE-SPINE.md pattern 'AD-009')
These align with the repo's fitness approach and make the package enforceable. I'll add them (severity error/warn). Good — that's using the repo's method.

Now, do I need ask_user_question? The user gave a detailed spec. I think I can proceed. But the brainstorming skill says present a design and get approval for architectural path before writing the spec. However, the user explicitly requested the deliverable; that's approval to produce the package. I'll invoke brainstorming, classify, write the understanding note, and proceed to produce the package (the spec). I will not invoke writing-plans (that's for executors, later).

Hmm, but the HARD-GATE: "Architectural: the human partner reviews and approves the written spec, then reviews the written implementation plan". If I'm strict, I should write the spec, then stop for approval, then writing-plans. But the user asked for the package including handoff content. The deliverable itself contains acceptance criteria & handoff brief, which is arguably the "plan" content. I'll produce the package and explicitly note that handoff to executors starts after the human ratifies ADR-008, and list what's needed. That respects the gate: I produce the decision materials; the implementation plan/handoff is gated on approval. Good — item 7 covers "what remains for the human architect", naturally incorporating the gate.

Actually, to be safe and useful, I'll include an "Epic-context для исполнителей" (handoff brief) section but mark it as "draft, activates after ADR-008 ratification". That satisfies "затем передать исполнителям" without violating the gate.

Let me reconsider the amount of edits. Maybe I'm over-scoping. The user's 7 items map to a package document. The repo artifacts make it "передаваемым". I'll do it but keep each edit tight.

Let me also reconsider: should the main package be in `docs/changes/`? Repo has no such dir. Alternative: `docs/solutioning-recurring-c2b.md`? Or `docs/changes/recurring-c2b/`. I'll use `docs/changes/recurring-c2b/ARCH-CHANGE-PACKAGE.md`. Reasonable and discoverable. Hmm, but README structure lists docs/ subdirs; I'll update it.

Actually, maybe better naming aligned with repo: the repo used Russian-transliterated ADR filenames. I'll name ADR-008 as `ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md`. And spec `mandate-state-machine.md` (repo uses English kebab: `state-machine.md`, `tsp-api.md`, `opkc-adapter.md`, `vendor-rfp.md`). So `mandate-state-machine.md`. Good.

Let me think about what "architecture decision with alternatives, consequences, reversibility" should be — the ADR-008 file. And the package doc item 3 summarizes it. Fine.

Now, let me also handle the parent spine escalation: "AD-009" — will need a new spine section. Also the top of spine says "Родительский spine: initiative «Подключение банка к СБП (эквайринг C2B)»". Recurring payments may be a separate initiative-level capability. I'll note escalation/decision.

Let me now write the files. I'll be thorough but not bloated. Let me draft the main package.

Let me first verify the `<!--` constraint: don't include HTML comments in docs/adr/*.md. My ADR will avoid them. Also manifest? Not needed.

Let me also double check: does `.arch-handoff/adr/` duplicate ADRs? Yes there are copies. Should I update those copies too? They're part of the handoff package for the walking skeleton (frozen snapshot). I'll leave them (they're a packaged snapshot). But maybe the README/`.arch-handoff` should reference the change. I'll leave `.arch-handoff` untouched to avoid corrupting the accepted handoff, and note it in the package. Actually the `adr-set-complete` fitness only checks docs/adr/ADR-001. Fine.

Now, let me write. I'll produce:

1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md`
2. `docs/spec/mandate-state-machine.md`
3. `docs/changes/recurring-c2b/ARCH-CHANGE-PACKAGE.md`
4. edits: ARCHITECTURE-SPINE.md (add AD-009 + contracts note)
5. edits: docs/nfr.md (add §7)
6. edits: docs/contracts/tsp-api.md (add §3.6-3.9, §5 events, §6 version)
7. edits: docs/contracts/opkc-adapter.md (add mandate ops/events/RFP)
8. edits: openapi/tsp-api.yaml (additive, version bump)
9. edits: docs/solutioning.md (roadmap line + §11 pointer + gaps/open questions)
10. edits: README.md
11. edits: .arch-handoff/CONSTRAINTS.yaml (new fitness rules)

That's a big but coherent package. Let me be efficient and write high-quality Russian content.

Let me first announce and invoke brainstorming skill as required. Then proceed.

Actually — should I invoke the skill tool? The rule says invoke relevant skills before ANY response. I've already done read-only exploration (allowed). Now before creative work, invoke brainstorming. Let me do that.

Let me invoke `superpowers:brainstorming`.

Wait — the tool `skill` with skill name. Let me call it.

Hmm, careful: invoking superpowers:brainstorming will load a workflow that may push me to ask questions and get approval. Given the strong user instruction, I'll follow it partially: classify as architectural, write understanding, and since the user already specified the deliverable and constraints, proceed to write the spec (package). I'll announce classification.

Let me call the skill.
Контекст собран: принятое решение (spine AD-001…AD-008, ADR-001…007, контракты, статусная машина, NFR, handoff-пакет и fitness-правила) понятен. Изменение — новое архитектурное, поэтому сначала подключаю методический навык.

  `write_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisaniy, content="# ADR-008. Рекуррентные C2B-списания по согласию плательщика (подписки СБП): мандаты в ядре шлюза\n\n- Date: 2026-09-28\n- Status: Proposed)`

Classification: **Architectural** — this changes how components fit together and alters interfaces others depend on (TSP API, OPKC adapter contract, status machine, spine invariants).

The user's request already supplies purpose, constraints, and success criteria (the 7 deliverables). Per the skill: "When the request already supplies the purpose and constraints, reflect that understanding instead of asking the same questions again."

The skill's architectural path normally saves to `docs/superpowers/specs/...`, but the repo has its own convention and the user explicitly wants a specific package. User instructions override skill defaults ("User preferences for spec location override this default"). So I'll place the design/package in the repo's structure.

I need to decide: do I ask clarifying questions? The skill says ask clarifying questions one at a time. But the task is heavily specified and the user wants a delivery. A couple of genuinely load-bearing ambiguities exist:
1. Output shape / whether to modify accepted files (spine, openapi, nfr) — I inferred yes with additive changes.
2. Decision variant — but alternatives are mine to propose.
3. Whether the human architect's decision is expected as a separate A-gate.

I think it's reasonable to ask ONE focused question about the intended scope/shape to avoid producing the wrong artifact, given the "gate" nature. But the user's instruction is quite explicit ("Что должно получиться: 1..7"). They also said code-not-write. Asking might be seen as stalling. However the skill mandates a design gate. Given the CLI mode and that the user asked for a full package, I'll proceed but present the understanding note and, importantly, I'll produce the package as the "written spec" — the deliverable itself. I'll then stop for the human architect's review (which is exactly item 7 and the gate).

Actually, re-reading: The user said "Подготовь архитектурный пакет...". That IS the ask. Producing it = fulfilling. The gate is internal to the skill's process for implementation. Since this is document authoring (the spec), and the spec is precisely what's requested, I can write it. Then the "User review gate" applies: I present it and ask for review. And writing-plans is the next step which the user explicitly defers ("затем передать исполнителям"). 

I'll reflect the understanding briefly, then build. Given the size of edits, I'll create the artifacts. Let me also consider using ask_user_question to confirm one thing: whether to also encode changes additively into accepted files (spine/openapi/nfr/contracts/README) or keep the package self-contained. This is genuinely consequential and the user gave a hint ("меняй только тем способом, который принят"). I'm fairly confident additive encoding is the accepted way. I'll proceed without asking to avoid stalling, but I'll make it explicit in the package and reversible.

Hmm, the instructions say "Confirm Ambiguity/Expansion". I think one short confirmation is warranted given the scope of touching accepted files. But the user explicitly pre-authorized: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." That's a directive to change them the accepted way. So no confirmation needed.

OK. Let me now write everything. Let me set up a task list mentally and proceed.

Let me draft content carefully.

---

### ADR-008

Title: ADR-008. Рекуррентные C2B-списания по согласию плательщика (подписки СБП): расширение ядра шлюза мандатами
- Date: 2026-09-28
- Status: Proposed (на человеческое решение — ревизия ADR-007/A3-совместимость)
- Owner: solution-architect (платёжный контур) + владелец продукта
- Related: ADR-001, ADR-002, ADR-003, ADR-004, ADR-005, ADR-006, ADR-007, AD-001..AD-009

Context: business need (TSP: cinemas, utilities, telecom) wants recurring debits without QR each time. Current C2B requires QR + client action. SBP autopayment/subscription mechanism requires payer consent (mandate). New external protocol surface [ТРЕБУЕТ ПРОВЕРКИ]. Forces: financial (double debit risk on payer side), PII/consent, regulatory (161-ФЗ, 152-ФЗ, ПОД/ФТ), reuse of proven invariants; existing QR flow must not break.

Decision:
1. Recurring capability built INTO existing gateway core (option A), reusing isolation/outbox/status machine/adapter/notifier/recon.
2. New aggregate `Mandate` (согласие плательщика) with own lifecycle; single source of truth in gateway DB; RPO=0.
3. Recurring debit reuses payment state machine: new origin `MANDATE`, new pre-state `DEBIT_PENDING` (authorization at payer bank), then `PAID → CREDITED → COMPLETED`; no ABC call before confirmed debit.
4. AD-005 semantics preserved and generalized: credit only from confirmed status; for mandate debits confirmation = bank-payer/NSPK confirmation of the debit within mandate limits.
5. New idempotency invariant: not more than one successful debit per (mandate, period); business key `(mandateId, period)`; plus Idempotency-Key.
6. Adapter contract extended with mandate operations; NSPK protocol only inside adapter (AD-004).
7. Payer data minimized/tokenized; mandate lifecycle audited; revocation honored immediately.
8. Additive, versioned contract changes (v0.2 draft), no breaking change to v0.1 consumers.
9. Feature-flagged per TSP/segment; rollback = stop new mandates, honor existing.

Alternatives: A extend core (rec), B separate subscriptions microservice, C mandates in ABC/bank subscription system, D vendor subscriptions module. Table.

Consequences +/-.
Reversibility: reversible technically (additive, feature-flagged), costly operationally after live consents (must honor/revoke per regulation).
References.

### SPINE addition AD-009

AD-009. Рекуррентные списания только по действующему согласию плательщика
- Status: Proposed (ADR-008)
- Binds: статусная машина (mandate + debit), адаптер ОПКЦ (mandate-операции), нотификатор, сверка.
- Prevents: списание без действующего согласия; повторное списание за один период; зачисление по неинициированному/неподтверждённому списанию; необработанный отзыв согласия.
- Rule: Рекуррентное списание инициируется только при `Mandate.status = ACTIVE`, в пределах лимитов согласия, идемпотентно по `(mandateId, period)`; зачисление — только из подтверждённого статуса (расширение AD-005); отзыв/приостановка согласия прекращает новые списания немедленно и фиксируется в аудит-логе. Fitness: тесты «нет списания вне ACTIVE», «не более одного успешного списания на период», «отзыв → новое списание отклонено».

Also update the spine "Контракты и версии" to mention v0.2 draft. And maybe note AD-005 semantics extension — I'll add a line to AD-005? Careful: modifying accepted invariant wording is exactly the sensitive part. The repo's accepted way: AD-005 status is Proposed(ADR-005). Extending its semantics should be a new ADR and noted. I will NOT rewrite AD-005's Rule text; instead AD-009 explicitly states it extends AD-005's confirmation source, and ADR-008 explains. That preserves accepted text. Good: I'll add a cross-reference note under AD-009, not modify AD-005.

Hmm, but the user wants "какие инварианты затронуты, что меняется, что нет" — I'll cover in the package; the spine gets AD-009. I could optionally add to AD-005 block a "See also" line, but that edits accepted text. I'll leave AD-005 untouched and reference from AD-009. Actually adding a non-normative cross-ref could be fine, but safer to not touch. The package and ADR-008 handle it.

### mandate-state-machine.md

States for Mandate:
- `CREATED` (шлюз зарегистрировал намерение) → `PENDING_PAYER` (запрос согласия передан в НСПК; плательщик подтверждает в банке) → `ACTIVE` | `REJECTED` | `EXPIRED` (не подтверждено в срок)
- `ACTIVE` → `SUSPENDED` (приостановлено шлюзом/ТСП/банком) → `ACTIVE` (возобновление) | `REVOKED`
- `ACTIVE`/`SUSPENDED` → `REVOKED` (отзыв плательщиком/банком) — терминальное
- `ACTIVE` → `EXPIRED` (истёк `validUntil`) — терминальное
- `REJECTED` terminal.
Rules: no debit unless ACTIVE; revoke immediate & irreversible; amounts immutable? mandate limits immutable after ACTIVE (change = new mandate) — matches immutability principle.

Debit (recurring charge) — reuse Payment aggregate with `origin=MANDATE`:
- `CREATED` (запись списания, outbox «регистрация списания») → `DEBIT_PENDING` (отправлено в НСПК, ожидается подтверждение банка плательщика) → `PAID` (подтверждено) → `CREDITED` → `COMPLETED`; терминальные `FAILED` (отклонено плательщиком/банком/недостаток средств/лимиты), `EXPIRED` (таймаут авторизации), `REFUNDED` (через сагу).
- Guards: `mandate.status == ACTIVE`; `amount <= mandate.maxAmountPerPeriod` (и остаток общего лимита); `(mandateId, period)` not already successfully debited; `now < validUntil`.
- Invariants: no ABC before `PAID`; at most one successful debit per period; repeated NSPK events idempotent; revoke → subsequent debits fail.
- Reconciliation table.
- Mapping to TSP API.

### tsp-api.md additions

§3.6 Mandate registration: `POST /v1/mandates` (Idempotency-Key), body: tspId, payerRef/phone? (masked), limits {maxAmountPerPeriod, period, maxTotalAmount}, validUntil, purpose, redirectUrl, merchantOrderId; response 201 {mandateId, status PENDING_PAYER, consentUrl/qrUrl}. Payer confirmation is out of band (bank app). 
§3.7 Mandate status: `GET /v1/mandates/{mandateId}` → status enum, limits, validUntil, activatedAt, revokedAt.
§3.8 Initiate debit: `POST /v1/mandates/{mandateId}/debits` (Idempotency-Key) body {amount, merchantOrderId, period?} → 201 {paymentId, debitId?, status DEBIT_PENDING}. Note: returns a payment resource reference.
§3.9 Debit status: `GET /v1/debits/{debitId}` or via payment status. 
§3.10 Revocation by merchant: `POST /v1/mandates/{mandateId}/revoke` (merchant-initiated). Payer-initiated revocation arrives via NSPK → webhook.
Errors: new codes `MANDATE_NOT_ACTIVE` (422), `AMOUNT_EXCEEDS_MANDATE_LIMIT` (422), `MANDATE_LIMIT_EXCEEDED`/`PERIOD_ALREADY_DEBITED` (409), `MANDATE_EXPIRED` (422), `MANDATE_ALREADY_REVOKED` (409).
Webhooks: `mandate.activated`, `mandate.rejected`, `mandate.revoked`, `mandate.expired`, `debit.completed`, `debit.failed`.
Compatibility: all additive; new resources; `Payment` gains optional `mandateId`, `origin`; debit statuses delivered via `Debit` resource to avoid changing existing `status` enum; contract version → v0.2 draft, v0.1 support continues.

### opkc-adapter.md additions

New sync ops: `registerMandate(reference=mandateId, payerRef, limits, validUntil, purpose)` → `jobId/ACCEPTED` (result by event); `getMandateStatus(mandateId)`; `revokeMandate(mandateId, reason)`; `createDebit(reference=debitId/paymentId, mandateId, amount, period)` → ACCEPTED; `getDebitStatus`.
New events: `mandate.activated`, `mandate.rejected`, `mandate.revoked`, `mandate.expired`, `debit.paid`, `debit.rejected`, `debit.expired`.
Idempotency: by reference; RFP requirement #7: mandate protocol support.
Timeout table additions.

### nfr.md §7 additions

Table for mandate/recurring:
- Latency `POST /v1/mandates` p95 < 500 мс
- Latency `POST /v1/mandates/{id}/debits` p95 < 500 мс
- Mandate activation event→status/+webhook p95 < 5 с
- Credit from debit confirmation p95 < 60 с (reuse)
- Double debits per period = 0
- Double credits = 0
- Mandate RPO = 0
- Limit enforcement 100%
- Fault isolation: mandate/debit failure does not degrade QR intake (availability of QR ≥ 99,95% unaffected) — test.
- Recon: mandates+debits in hourly NSPK recon, 0 disrepancies.
- PII: payerRef tokenized, 100% masked in logs.
- Throughput: combined sustained ≥ 200 TPS.
- Availability capability ≥ 99,95%.
Keep '99,95' string present.

### solutioning.md changes
- §1 roadmap line: move «автоплатежи/рекуррентные списания» from out-of-scope to "в scope изменения, см. ...", keep C2C/выплаты/диспуты out.
- Add §11 «Изменение: подписки СБП (ADR-008)» pointer + status Proposed.
- §9 gaps add: документация НСПК по рекуррентным списаниям; поддержка mandate-протокола вендором (ADR-007); юридическое основание/уведомление плательщика.
- §10 open questions add items.

Actually editing §1 roadmap sentence: I'll adjust minimally.

### README
- Add change package to structure + status note.

### CONSTRAINTS.yaml
Add fitness rules:
- adr-008-present
- spine-mandate-invariant (AD-009)
- mandate-no-double-debit (spec pattern)
Perhaps also must_not_contain in ADR-008 for '<!--' (already covered by glob docs/adr/*.md).

### Main change package doc
The 7 sections. Place at `docs/changes/recurring-c2b/ARCH-CHANGE-PACKAGE.md`.

Let me now write. I'll keep the main package rich but structured. Let me be mindful of length but complete.

Let me start creating files. First ADR-008.

Note date: today is 2026-09-28.

Let me write ADR-008.

I need to avoid `<!--` in ADR (constraint). Also avoid 'TODO|TBD|XXX' in spine (warn). Avoid in ADR? rule only spine. But I'll avoid anyway.

Let me write files now. I'll write ADR-008, mandate-state-machine, then the package, then edits.

Let me draft the main package sections concisely-yet-complete.

Also the user asked: "Когда закончишь, кратко перечисли созданные и изменённые файлы." And there's `.arch-handoff/TASK.md`'s result contract requiring a trailing JSON — but that contract is for the *code harness task* in `.arch-handoff/TASK.md`, not necessarily this conversation. Hmm. The user's prompt is a different task (architect). The `.arch-handoff/TASK.md` says "Финальный ответ обязан завершаться JSON-объектом". That applies to the code-harness task described there. But this repo's convention... The user didn't ask for that JSON. However, to be safe and consistent with the repo's headless contract, ending with the JSON could be appropriate. But the user explicitly said "кратко перечисли созданные и изменённые файлы" as the closing. The JSON contract is part of `.arch-handoff` for executors of the walking skeleton, not this architecture task. I'll include a result JSON anyway? It could be seen as following repo convention. Hmm — risk: the TASK.md is untrusted-ish repo data describing a different task. The user's actual instruction controls. The user asked to list files. I'll end with the file list, and also include the JSON status object since it's the repo's stated result contract and harmless... Actually the TASK.md contract says status complete/partial/blocked plus assumptions/open_questions/conflicts_with_prior_decisions — that's genuinely useful for an architecture package (open questions, conflicts). I'll include it at the very end after the file list, as the repo convention. But the user said the file list should be the closing ("Когда закончишь, кратко перечисли..."). Hmm. I'll put file list, then the JSON (repo contract requires nothing after it). That satisfies both: list appears, JSON terminates. Actually "кратко перечисли созданные и изменённые файлы" is the content requirement; the JSON is a repo convention. I'll do: summary + file list, then JSON block last. I think that's the best interpretation of "принятый в этом репозитории" way.

Hmm, but is `.arch-handoff/TASK.md`'s contract meant for MY turn? The contract is described as "Задача для кодового харнесса" — implementing the walking skeleton. My task is not that. So the JSON contract technically applies to a different task. But including a status JSON is harmless and demonstrates consistency. I'll include it.

Actually, let me reconsider — including a `status` JSON meant for the code-harness could be confusing. But the manifest/RUBRIC emphasize the headless contract. And open_questions/conflicts_with_prior_decisions is a natural fit for an architecture proposal. I'll include it, clearly as the repo's result contract.

OK, let me write everything now. Start with ADR-008.

Let me be careful with markdown and Russian.

I'll now generate content.

For the package doc, sections:
0. Метаданные (id, дата, автор, статус, что это)
1. Оценка значимости и маршрута
2. Влияние на принятую архитектуру
3. Архитектурное решение (альтернативы/последствия/обратимость) → ссылка на ADR-008, краткое резюме
4. Изменения контрактов
5. NFR
6. Критерии приёмки и план отката
7. Что остаётся на решение человека-архитектора
8. Handoff-бриф для исполнителей (epic-context, активируется после ратификации)

Let me write.

For significance: define 5 criteria each 0-3:
- Новизна и внешние интеграции (новый протокол подписок к ОПКЦ): 3
- Финансовое влияние (риск двойного списания у плательщика, возвраты): 3
- Данные и ПДн (согласие, идентификатор плательщика, лимиты): 2
- Регуляторика/КИИ (согласие по 161-ФЗ, уведомление, аудит): 3
- Влияние на принятое решение/обратимость (расширение статусной машины и контрактов; ядро переиспользуется): 1... 

Hmm, I want total to justify "Critical". Baseline 11/15 was Critical. If my change is 12, Critical. Let me set: 3+3+2+3+1=12 → Critical. But is 12 more or less than 11? More. Fine: change is at least as significant. Actually maybe the 5th axis should be "изменение принятых решений/контрактов" = 2 → 13. Let me use 2 → 13/15 with explanation. Hmm. Let me not overthink; set 12/15 and clearly mark the decomposition as a working model requiring confirmation (item 7). I'll use:
1) Новизна (новый протокол/операции к ОПКЦ) — 3
2) Финансовое влияние — 3
3) Данные/ПДн — 2
4) Регуляторика/КИИ — 3
5) Влияние на принятые решения и обратимость — 1
Total 12/15 → Critical.

Hmm, axis 5=1 seems low given we're touching spine/contracts. But the change is additive and reversible → low irreversibility. Actually "влияние на принятое решение" is high (touches AD-002/AD-005 semantics). Let me rename axis 5 to "Обратимость (чем выше — тем хуже откат)". Additive+feature-flag → низкая необратимость → 1. And add the "влияние на принятые решения" into axis 1 or mention separately. I'll present 5 axes:
- Новизна/внешняя интеграция — 3
- Финансовое влияние — 3
- Данные и ПДн — 2
- Регуляторные требования/КИИ — 3
- Необратимость (стоимость отката) — 1
= 12/15 → Critical.

Consistent enough. And note baseline was 11/15.

Now writing. Let me create ADR-008 first.
Классификация: **архитектурная работа** (меняются интерфейсы, от которых зависят потребители: API ТСП, контракт адаптера ОПКЦ, статусная модель, инварианты spine). Поэтому иду полным маршрутом: контекст → решение с альтернативами → письменная спецификация/пакет → гейт человеческого решения → затем handoff исполнителям.

Фиксирую понимание задачи (отражение ваших вводных, не повторные вопросы):
- **Цель:** дать ТСП (кинотеатры, ЖКХ, связь) рекуррентные C2B-списания по согласию плательщика поверх принятого решения, без QR и действия клиента на каждый платёж.
- **Результат:** архитектурный пакет для вынесения на человеческое решение и последующей передачи исполнителям (7 требуемых разделов).
- **Ограничения:** код не пишу; принятые артефакты меняю принятым в репозитории способом (новый ADR + Proposed-блок в spine + аддитивные, версионируемые изменения контрактов/NFR/spec); протокольные детали НСПК — `[ТРЕБУЕТ ПРОВЕРКИ]`.
- **Критерий успеха:** пакет позволяет человеку-архитектору принять/отклонить решение, а исполнителям — реализовать без доступа к исходным материалам.

Приступаю к артефактам.

  `write_file(content="# Статусная модель подписок СБП — мандат и рекуррентное списание\n\n- Status: Draft (для ревью на гейте A1 изменения; вводится ADR-008)\n- , file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/spec/mandate-state-machine.md")`

Now the mandate-state-machine spec.

  `write_file(content="# Архитектурный пакет изменения — подписки СБП (рекуррентные C2B-списания по согласию плательщика)\n\n- ID изменения: CHG-SBP-RECURRING-001, file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/changes/recurring-c2b/ARCH-CHANGE-PAC)`

Now the main change package document.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now edit ARCHITECTURE-SPINE.md to add AD-009 and update contracts/versions. Let me read the end portion again to place edits precisely.

The spine currently has AD-001..AD-008, then "## Deferred", then "## Контракты и версии".

I'll insert AD-009 right after AD-008 block (before "---\n\n## Deferred"). And update "Контракты и версии" to mention v0.2.

Let me do the edits.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/ARCHITECTURE-SPINE.md", new_string="## Контракты и версии\n\n- Контракт НСПК: `docs/contracts/nspk-contract.md` — создаётся после получения документации НСПК; до этого все ссы, old_string="## Контракты и версии\n\n- Контракт НСПК: `docs/contracts/nspk-contract.md` — создаётся после получения документации НСПК; до этого все ссы)`

Now update the "Контракты и версии" section in the spine to mention v0.2 draft. Let me read the tail.

Original:
```
## Контракты и версии

- Контракт НСПК: `docs/contracts/nspk-contract.md` — создаётся после получения документации НСПК; до этого все ссылки на протокол помечены `[ТРЕБУЕТ ПРОВЕРКИ]`.
- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec).
- Пиннинг версий зависимостей — в CONSTRAINTS.yaml (.arch-handoff) при передаче кодовому харнессу.
```

Update: add v0.2 draft additive. Also note the TSP API openapi.

Also the Deferred section: add recurring note? The change moves subscriptions in scope — but as a separate change. I'll add a pointer line to the change package maybe. Let me add to "Контракты и версии" and perhaps a note under status line. Let me edit.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/tsp-api.md", new_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n, old_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`")`

Now extend docs/contracts/tsp-api.md. Add new sections. The existing structure: §3.5 status of refund, §4 errors, §5 webhooks, §6 versioning, §7 open questions. I'll insert new methods as §3.6–3.10 after §3.5, add to §4 canonical codes, §5 events, §6 versioning note, §7 open questions.

Let me do edits carefully.

First, insert after §3.5 block (before "## 4. Ошибки").

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/tsp-api.md", new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`

Now update §4 canonical error codes, §5 webhook events, §6 versioning, §7 open questions.

Let me edit §4 codes line.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/tsp-api.md", new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`

Now update §5 events list and §6 versioning, §7 open questions. Let me read lines around the events list and §6/§7.

  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/tsp-api.md", offset=255, limit=30)`

Now §6 versioning and §7 open questions. Let me read the tail of the file.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/tsp-api.md", new_string="## 6. Версионирование и совместимость\n\n- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6, old_string="## 6. Версионирование и совместимость\n\n- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/tsp-api.md", new_string="- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft); разделы подписок СБП (§3.6–3.10, §4, §5) — **0.2 draft** (ADR-008, ад, old_string="- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)\n- Owner: solution-architect (платёжный контур)\n- Связано: ADR-002 (и)`

Also bump the contract version header at the top of tsp-api.md. Currently: "Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)". I'll add a note about v0.2. Let me edit.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/opkc-adapter.md", new_string="| `createRefund` | регистрация возврата в ОПКЦ | `reference` (= `refundId` ядра), `qrId`, `amount` | `ACCEPTED` (результат — событием) | 5 , old_string="| `createRefund` | регистрация возврата в ОПКЦ | `reference` (= `refundId` ядра), `qrId`, `amount` | `ACCEPTED` (результат — событием) | 5 )`

Now extend docs/contracts/opkc-adapter.md. Add mandate ops to §3 table, events to §4, RFP requirement to §8, maybe timeout. Let me edit.

§3 table: add rows after `createRefund`/`getRefundStatus`/`getReconciliationReport`. I'll add mandate rows before `getReconciliationReport` or after. Let me add after `getRefundStatus` and before `getReconciliationReport`.

§4 events: add mandate/debit events.
§8 RFP: add item 7.

Let me do it.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/opkc-adapter.md", new_string="| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |\n| `refund.rejected` | возв, old_string="| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |\n| `refund.rejected` | возв)`

Now add events to §4 table and RFP item. Let me read the events table region.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/opkc-adapter.md", new_string="Гарантии: at-least-once (повторы возможны → ядро дедуплицирует по `eventId`); порядок по одному `qrId`/`mandateId` — консервативный (строги, old_string="Гарантии: at-least-once (повторы возможны → ядро дедуплицирует по `eventId`); порядок по одному `qrId` — консервативный (строгий порядок не)`

Update §4 guarantees line to mention mandateId/debitId ordering, and §8 RFP item, and the header "Связано". Also §7 open questions maybe. Let me edit the guarantees line and RFP.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/opkc-adapter.md", new_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`/`mandateId`/`debitId`) в каждый мутирующий вызов.", old_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.")`
  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/opkc-adapter.md", offset=80, limit=25)`

Now update §8 RFP requirements to add mandate support, and §9 open questions. Let me read the tail.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/opkc-adapter.md", new_string="1. Реализует настоящий контракт поверх протокола НСПК; нормализует статусы/ошибки.\n2. Сертификаты ФСТЭК/соответствие требованиям НСПК; СКЗ, old_string="1. Реализует настоящий контракт поверх протокола НСПК; нормализует статусы/ошибки.\n2. Сертификаты ФСТЭК/соответствие требованиям НСПК; СКЗ)`
  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/opkc-adapter.md", new_string="- Связано: ADR-003, ADR-004, ADR-008 (подписки СБП), AD-004, AD-008, AD-009", old_string="- Связано: ADR-003, ADR-004, AD-004, AD-008")`

Now update the header of opkc-adapter.md "Связано" to include ADR-008. And the NFR table §7 add mandate latency row maybe. Let me update header + add a row.

Header currently: "- Связано: ADR-003, ADR-004, AD-004, AD-008". Add ADR-008 and AD-009.

Wait — AD-008 is spine block (strategy). ADR-008 is the new ADR. Confusingly similar. The header lists spine "AD-004, AD-008". I'll add "ADR-008, AD-009".

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/contracts/opkc-adapter.md", new_string="| Latency `createPaymentLink` | p95 < 1 c (без учёта НСПК) | Нагрузочный тест |\n| Latency `registerMandate` / `createDebit` (ADR-008) | p9, old_string="| Latency `createPaymentLink` | p95 < 1 c (без учёта НСПК) | Нагрузочный тест |")`

Add mandate latency row to §7 NFR table of adapter. Let me add after `createPaymentLink` row.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/nfr.md", new_string="## 7. Подписки СБП (рекуррентные списания, ADR-008)\n\nЗначения — baseline; финализируются с бизнесом и НСПК. Дополняют разделы 1–6 (доступ, old_string="## Зависимости (внешние входы для NFR)")`

Now add §7 to nfr.md. Let me read the tail of nfr.md to append.

The file ends with "## Зависимости (внешние входы для NFR)". I'll insert §7 before "## Зависимости". Let me edit.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/solutioning.md", new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop, old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop)`

The '99,95' fitness pattern still present. Good.

Now update solutioning.md: roadmap line in §1, add §11 pointer, update §9 gaps and §10 open questions. Let me edit the roadmap line first.

Line: "Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

  `read_file(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/solutioning.md", limit=30, offset=146)`

Now add §11 and update §9/§10. Let me look at the end of solutioning.md (§9 Gaps, §10 open questions). I'll insert §11 after §10, and add rows/items.

Let me read the tail.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/solutioning.md", new_string="| Выбор конкретного вендора транспорта ОПКЦ | RFP по критериям ADR-007 (сертификаты ФСТЭК, тестовый контур, SLA, референсы) | Проектный офи, old_string="| Выбор конкретного вендора транспорта ОПКЦ | RFP по критериям ADR-007 (сертификаты ФСТЭК, тестовый контур, SLA, референсы) | Проектный офи)`
  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0-draft\n  description: >-\n    Аддитивное расширение v0.2 (ADR-008): по, file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/openapi/tsp-api.yaml")`

Now update openapi/tsp-api.yaml additively: version bump to 0.2.0-draft and add new paths + schemas. Also add optional `origin` and `mandateId` to Payment schema (additive properties). Keep existing intact.

Let me rewrite the file with additions. I need to be careful to keep existing content unchanged except version. Let me construct the new content.

Existing content:
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

I'll write the new file with:
- version: 0.2.0-draft
- add paths for mandates/debits
- add schemas MandateRequest, Mandate, DebitRequest, Debit
- add optional fields to Payment (origin, mandateId) — additive.

Let me write it. I must read the file first (I did read it fully earlier). write_file with full content is fine.

Let me produce clean YAML.

Note: existing Payment.status enum kept unchanged. Add `origin` and `mandateId` as optional properties.

New paths:
```
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
          description: Согласие зарегистрировано
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
  /v1/mandates/{mandateId}/debits:
    post:
      operationId: createDebit
      parameters:
        - in: path
          name: mandateId
          required: true
          schema: {type: string}
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
          description: Списание инициировано
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Debit'}
  /v1/debits/{debitId}:
    get:
      operationId: getDebit
      parameters:
        - {in: path, name: debitId, required: true, schema: {type: string}}
      responses:
        '200':
          description: Статус списания
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Debit'}
```

Schemas:
```
    MandateRequest:
      type: object
      required: [tspId, payerRef, maxAmountPerPeriod, period, validUntil]
      properties:
        tspId: {type: string}
        payerRef: {type: string, description: Токенизированная ссылка на плательщика (не открытые ПДн)}
        maxAmountPerPeriod: {type: integer, description: Лимит одного списания за период, копейки}
        period: {type: string, description: Период списаний (MONTHLY и т.п.) [ТРЕБУЕТ ПРОВЕРКИ]}
        maxTotalAmount: {type: integer, description: Общий лимит согласия, копейки}
        validUntil: {type: string, format: date-time}
        paymentPurpose: {type: string}
        redirectUrl: {type: string}
        merchantOrderId: {type: string}
    Mandate:
      type: object
      required: [mandateId, status]
      properties:
        mandateId: {type: string}
        status:
          type: string
          enum: [CREATED, PENDING_PAYER, ACTIVE, SUSPENDED, REVOKED, REJECTED, EXPIRED]
        consentUrl: {type: string}
        maxAmountPerPeriod: {type: integer}
        period: {type: string}
        maxTotalAmount: {type: integer}
        validUntil: {type: string, format: date-time}
        activatedAt: {type: string, format: date-time}
        revokedAt: {type: string, format: date-time}
        reasonCode: {type: string}
    DebitRequest:
      type: object
      required: [amount, period]
      properties:
        amount: {type: integer, description: Сумма списания, копейки}
        period: {type: string, description: Идентификатор периода [ТРЕБУЕТ ПРОВЕРКИ]}
        merchantOrderId: {type: string}
    Debit:
      type: object
      required: [debitId, paymentId, mandateId, amount, status]
      properties:
        debitId: {type: string}
        paymentId: {type: string}
        mandateId: {type: string}
        amount: {type: integer}
        status:
          type: string
          enum: [DEBIT_PENDING, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED]
        errorCode: {type: string}
        paidAt: {type: string, format: date-time}
```

And Payment add properties origin + mandateId.

Let me write.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wh5tt2i/ws && python3 -c \"import yaml,sys; d=yaml, description="Validate OpenAPI YAML parses")`

Let me validate the YAML parses. Also update CONSTRAINTS.yaml fitness rules and README.

Let me first validate YAML with python.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="  - name: readme-exists\n    type: file_exists\n    path: README.md\n    severity: warn\n  - name: spine-lints-clean\n    type: must_not_co, old_string="  - name: readme-exists\n    type: file_exists\n    path: README.md\n    severity: warn\n  - name: spine-lints-clean\n    type: must_not_co)`

Now update `.arch-handoff/CONSTRAINTS.yaml` with fitness rules for the new invariant. Add:
- adr-008-present: file_exists docs/adr/ADR-008-...
- spine-mandate-invariant: must_contain ARCHITECTURE-SPINE.md pattern 'AD-009'
- mandate-no-double-debit: must_contain docs/spec/mandate-state-machine.md pattern 'не более одного успешного списания на период'
- change-package-present: file_exists docs/changes/recurring-c2b/ARCH-CHANGE-PACKAGE.md

Let me read the file again (I have it). I'll edit to append rules under the existing list.

Careful: pattern 'AD-009' — must_contain uses regex presumably. Fine.

Let me edit the file. The rules list ends with spine-lints-clean. I'll add after.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/README.md", new_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..008`, `ARCHITEC, old_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITEC)`

Now update README.md. Let me add change package to structure and status.

Current README:
```
# Платёжный шлюз СБП (C2B-приём)
...
- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: ...
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК ...

## Структура
...
```
I'll add a line for the change and update structure. Let me edit both places.

Read README again to be precise — I have it from earlier. Let me edit.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/.arch-handoff/CONSTRAINTS.yaml", new_string="  - name: mandate-no-double-debit\n    type: must_contain\n    glob: \"docs/spec/mandate-state-machine.md\"\n    pattern: '[Нн]е более одно, old_string="  - name: mandate-no-double-debit\n    type: must_contain\n    glob: \"docs/spec/mandate-state-machine.md\"\n    pattern: 'не более одного )`

Now verify all constraints pass. Let me write a small verification: check the fitness rules manually.

1. adr-set-complete: docs/adr/ADR-001-outbox.md exists ✓
2. spine-present ✓
3. nfr-measurable: docs/nfr.md contains '99,95' ✓ (section 1 has 99,95 and section 7)
4. abs-credit-only-from-paid: ADR-005 contains 'только из состояния `PAID`' ✓ (must_contain pattern — check exact substring "только из состояния `PAID`"). The ADR-005 text: "**Зачисление — только из состояния `PAID`**". Yes contains "только из состояния `PAID`". ✓
5. adr-no-placeholders: docs/adr/*.md must not contain '<!--'. My ADR-008 — does it contain '<!--'? No. Let me verify all.
6. readme-exists ✓
7. spine-lints-clean: no TODO|TBD|XXX ✓ (need to check)
8. New rules: files exist; spine contains AD-009 ✓; mandate-state-machine contains 'не более одного успешного списания' and 'только при `Mandate.status = ACTIVE`' — let me check the exact strings. In my spec §2.3: "**Не более одного успешного списания на (`mandateId`, `period`)**" — contains "Не более одного успешного списания" — the pattern is 'не более одного успешного списания' (lowercase 'не'). Regex is case-sensitive likely. My text has capital "Не". Hmm! That would fail. Let me check: pattern 'не более одного успешного списания'. In the file: "**Не более одного успешного списания на (`mandateId`, `period`)**". Capital Н. So must_contain case-sensitive would fail.

But also in §2.2 D1 guard: "период не списан" — no. In §3 table: "новое списание не создаётся". Hmm. Also in §2.3 first bullet: "Не более одного...". Capital.

Also the main package has "не более одного успешного списания" (lowercase) in §2.1 and AD-009 in spine: "не более одного успешного списания за период" (lowercase). But the rule globs specifically docs/spec/mandate-state-machine.md. So I should ensure lowercase occurrence there, or change the rule to a case-insensitive-friendly substring. Simplest: adjust the regex to match both, e.g., '[Нн]е более одного успешного списания'. Let me update the rule pattern accordingly. Or add lowercase mention. Better fix the rule to be robust.

Similarly 'только при `Mandate.status = ACTIVE`' — in spec §1.3: "**Списание инициируется только при `Mandate.status = ACTIVE`.**" — lowercase "только при `Mandate.status = ACTIVE`" ✓. Good.

Let me change the mandate-no-double-debit pattern to '[Нн]е более одного успешного списания'.

Also check spine pattern 'AD-009' present ✓.

Let me also verify no '<!--' in ADRs and no TODO/TBD/XXX in spine. Let me run grep checks.

Also validate CONSTRAINTS.yaml parses.

Let me run a verification script.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wh5tt2i/ws && python3 - <<'PY'\nimport yaml, glob,, description="Run repo fitness rules verification")`

Now run a verification of all fitness rules via a python script to be thorough. I'll emulate the rules: file_exists, must_contain (regex search on glob), must_not_contain.

Let me write an inline python script (not a file) to check. Use glob pattern matching. I'll do a simple check.

Also verify CONSTRAINTS.yaml parses.

Let me run.

  `run_shell_command(command="cd <HARNESS>/runs-v2/cells/wh5tt2i/ws && python3 - <<'PY'\nimport re, json\nt, description="Validate result JSON and show git status")`

All fitness rules pass. Now also validate YAML of constraints parsed (it did). Let me also sanity-check that the ADR YAML/JSON result block at the end of the package is valid JSON. Let me extract and parse it. The package ends with a fenced json block. Let me check it parses.

Also I should verify git status to list created/modified files.

Let me run a JSON check and git status.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/changes/recurring-c2b/ARCH-CHANGE-PAC, new_string="Новые коды ошибок: `MANDATE_NOT_ACTIVE` (422), `MANDATE_EXPIRED` (422), `AMOUNT_EXCEEDS_MANDATE_LIMIT` (422), `PERIOD_ALREADY_DEBITED` (409, old_string="Новые коды ошибок: `MANDATE_NOT_ACTIVE` (422), `MANDATE_EXPIRED` (422), `AMOUNT_EXCEEDS_MANDATE_LIMIT` (422), `PERIOD_ALREADY_DEBITED` (409)`

Everything is in place. Now, per the brainstorming skill: after writing the spec, do a self-review (placeholder scan, internal consistency, scope, ambiguity), then ask the user to review. The user's request explicitly is to prepare the package. I've done it. I should NOT invoke writing-plans (that's the next step gated on approval, and the user said "затем передать исполнителям" — future). 

Let me do the self-review quickly:
- Placeholders: `[ТРЕБУЕТ ПРОВЕРКИ]` are intentional external inputs, not TODOs. No TODO/TBD. Good.
- Internal consistency: The package references ADR-008, spec, spine AD-009, contracts — all exist. The tsp-api says §3.6-3.10 and §4/§5 — consistent. openapi version 0.2.0-draft. NFR §7. Good.
- One check: In change package §2.3 table says `.arch-handoff/CONSTRAINTS.yaml` changed — done. 
- The package §4.2 mentions suspend/resume/revoke endpoints; spec M6/M7 reference them; tsp-api §3.10 documents them; openapi does not include them (I marked optional). Slight inconsistency: package §4.2 lists them as new methods, openapi omits. I noted they're optional/business-decided. Acceptable but let me make sure it's not contradictory. In §4.2 they're listed under "новые методы"; in tsp-api §3.10 "опциональны и включаются по решению бизнеса". In openapi I omitted them. This is a minor gap — to be safe I could add them to openapi or note omission. Given "without breaking consumers" and that they're optional, I'll leave openapi as-is but the package §4.2 could note openapi covers the core; optional endpoints are specified textually. Hmm, better to be consistent: either add to openapi or annotate. Let me annotate in §4.2 that openapi covers mandatory subset and optional suspend/resume/revoke are in the textual contract pending business decision. Actually simpler: add the three optional paths to openapi too — they are additive and harmless. But then "optional" semantics in yaml isn't expressible. I think annotating is cleaner. Let me add a sentence in §4.2.

Let me edit §4.2 to add a clarifier.

Also check: the package §4.2 table lists `GET /v1/debits/{debitId}` — openapi has it ✓. `POST /v1/mandates/{mandateId}/debits` ✓. `POST /v1/mandates` ✓, `GET /v1/mandates/{mandateId}` ✓. Good. Optional ones: suspend/resume/revoke. I'll clarify.

Let me make that small edit.

Also verify that ADR-008 doesn't contain '<!--' (pass, confirmed).

One more: the spine AD-009 "Status: Proposed (ADR-008)" format matches existing style "Status: Proposed (ADR-001)". Good.

Let me add the clarifier and then finish with the summary + JSON.

Actually, also reconsider: the user asked "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." I changed ARCHITECTURE-SPINE.md (added AD-009 block, updated Contracts section), which is the repo's way (blocks with Status: Proposed (ADR-XXX)). I changed ADR-001..007? No. I added ADR-008. Good. I didn't modify accepted ADRs. Good.

Let me do the small edit.

  `edit(file_path="<HARNESS>/runs-v2/cells/wh5tt2i/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisaniy, new_string="8. **Контракт API ТСП расширяется аддитивно** до v0.2 draft: новые ресурсы (`mandates`, `debits`) и опциональные поля; существующие пути, п, old_string="8. **Контракт API ТСП расширяется аддитивно** до v0.2 draft: новые ресурсы (`mandates`, `debits`) и опциональные поля; существующие пути, п)`

All good. Let me do a final self-review of the package for internal consistency, then present. Let me also double check the ADR-008 §Contract reference I used ("ADR-008 §Contract") — in ADR-008 I don't have a "## Contract" section; I wrote "см. ADR-008 §Contract / docs/contracts/tsp-api.md" in §Decision p.8. That's a dangling reference. Let me fix it to reference the contracts doc directly.

Let me check ADR-008 text: "Контракт API ТСП расширяется аддитивно до v0.2 draft: ... (см. ADR-008 §Contract / `docs/contracts/tsp-api.md`)." Hmm, there is no §Contract. I'll change to "(см. `docs/contracts/tsp-api.md` §6 и `openapi/tsp-api.yaml`)".

Let me edit.


Now final: present summary. Per brainstorming skill, I should invite the human to review the written spec before proceeding to writing-plans. That's item 7 and the gate. I'll present the outcome and ask for review, noting that handoff/planning is the next gated step.

The user asked to briefly list created and modified files. And repo convention wants a trailing JSON. I already put the JSON at the end of the package doc, but the "result contract" from `.arch-handoff/TASK.md` says the final *answer* must end with JSON. Should my chat answer end with JSON? The TASK.md is for the code harness task, but as a repo convention I'll end with the JSON. Hmm, the user said "кратко перечисли созданные и изменённые файлы" — I'll do that, then end with the JSON object (nothing after), satisfying the repo's headless contract. But wait, the JSON in TASK.md is about the walking-skeleton task. Including it here could be confusing ("conflicts_with_prior_decisions" is meaningful though). I'll include it — it's the repo's declared result contract and adds value. Actually, let me reconsider: the user's prompt is a role-play as solution-architect; the `.arch-handoff/TASK.md` result contract is stated as "Финальный ответ обязан завершаться JSON-объектом". Given ambiguity, including it is low-risk and follows repo convention. I'll end with it.

Now let me write the final response: concise summary of the package, key findings, verification results, and the file list, then review request, then JSON last.

Wait — the JSON must be last with nothing after. So order: content (summary, file list, review request), then JSON. But if I ask a question after the JSON, that violates. I'll put the review request before the JSON. But then the conversation ends with JSON and no question pending... The user can still respond. Fine.

Hmm, but "review request" implies I'm waiting. That's fine; the JSON is just a status trailer.

Let me compose the final message in Russian, concise but with key architecture points (per Core Mandates: include findings, references, verification, risks, next steps).

Let me structure:
- Что сделано (пакет + встроенные артефакты)
- Ключевые архитектурные выводы (кратко): маршрут Critical 12/15; затронутые инварианты AD-005/AD-003/AD-002/AD-004; новое AD-009; выбор варианта A; контракт аддитивно v0.2 (debit в отдельном ресурсе, enum Payment.status не трогаем); NFR; откат; открытые вопросы.
- Проверка: fitness-правила все PASS; YAML/JSON валидны.
- Файлы: созданные / изменённые.
- Следующий шаг (гейт): ревью спецификации человеком-архитектором → затем writing-plans/handoff. (Per skill.)
- JSON.

Keep it reasonably brief.

Let me write.
Готово. Пакет изменения «подписки СБП» (рекуррентные C2B-списания по согласию плательщика) собран поверх принятого решения; код не писал. Принятые артефакты менял принятым в репозитории способом: новый ADR (Proposed) + Proposed-блок spine + аддитивные/версионируемые дополнения контрактов и NFR, ни один принятый ADR не переписан.

Ключевые выводы пакета
- **Значимость:** 12/15 (рабочая 5-осевая модель, сопоставимо с базовым 11/15) → маршрут **Critical**, полный ADR и человеческое решение A3-типа.
- **Инварианты:** AD-005 сохранён и обобщён (подтверждение для `origin=MANDATE` приходит от банка плательщика, а не из нотификации QR) — обобщение вынесено в новый блок **AD-009**, текст AD-005 не тронут; расширены AD-003 (бизнес-ключ `(mandateId, period)` → «не более одного успешного списания на период»), AD-002 (агрегат `Mandate`, состояние `DEBIT_PENDING`), AD-004 (mandate-операции в адаптере). AD-001/AD-006/AD-007 наследуются.
- **Решение:** вариант A — расширение ядра (мандаты + списание), переиспользование outbox/статусной машины/адаптера/нотификатора/сверки/АБС; отклонены отдельный микросервис, хранение согласий в АБС, вендорский модуль целиком.
- **Контракты без поломок:** всё аддитивно в `/v1` (v0.1→0.2.0-draft); статусы списания отдаются в отдельном ресурсе `Debit`, чтобы **не расширять enum `Payment.status`**; в `Payment` — только опциональные `origin`/`mandateId`.
- **Откат:** технически reversible (флаг), организационно costly после появления действующих согласий; уровни: stop-new-mandates → stop-new-debits → аварийный revoke-all.
- **На человека-архитектора** (10 пунктов, §7): ратификация ADR-008/AD-009, доступность протокола по договору с НСПК, поддержка mandate-операций вендором (иначе пересмотр ADR-007), юр. основание согласия и уведомление плательщика, кодирование смысла `PAID`, версия контракта, определение «периода».

Проверка (выполнена)
- Fitness-правила `arch control check` из `.arch-handoff/CONSTRAINTS.yaml`: **13/13 PASS** (включая новые: `adr-008-present`, `spine-mandate-invariant`, `mandate-no-double-debit`, `mandate-debit-only-from-active`).
- `openapi/tsp-api.yaml` — валидный YAML, v0.2.0-draft, пути `/v1/payments*` сохранены.
- Результат-JSON пакета — валидный JSON.

Созданные файлы
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp.md`
- `docs/spec/mandate-state-machine.md`
- `docs/changes/recurring-c2b/ARCH-CHANGE-PACKAGE.md`

Изменённые файлы
- `ARCHITECTURE-SPINE.md` (+ блок AD-009, раздел «Контракты и версии»)
- `docs/contracts/tsp-api.md` (§3.6–3.10, коды ошибок, события, §6/§7)
- `docs/contracts/opkc-adapter.md` (mandate-операции/события, RFP, NFR)
- `docs/nfr.md` (раздел 7)
- `docs/solutioning.md` (roadmap, gaps, §11)
- `openapi/tsp-api.yaml` (0.2.0-draft, аддитивные пути/схемы)
- `README.md`, `.arch-handoff/CONSTRAINTS.yaml`

Следующий шаг — гейт (не реализация): прошу вас как человека-архитектора просмотреть пакет `docs/changes/recurring-c2b/ARCH-CHANGE-PACKAGE.md` и ADR-008 и подтвердить/отклонить ратификацию AD-008 + AD-009. Только после этого запускаю `writing-plans` для формирования handoff-плана исполнителям. Изменения не коммитил.

```json
{"status": "complete", "assumptions": ["Механизм рекуррентных списаний СБП реализуем по договору с НСПК через существующий адаптер ОПКЦ (AD-004) — протокол помечен [ТРЕБУЕТ ПРОВЕРКИ]", "Рекуррентное списание переиспользует агрегат платежа и статусную машину ADR-002", "Оценка значимости 12/15 дана по рабочей 5-осевой модели, сопоставимой с базовым решением (11/15)"], "open_questions": ["Поддерживает ли вендорский транспорт ADR-007 mandate-операции (иначе пересмотр границы)", "Обязанности по уведомлению плательщика о каждом списании и лимиты — юр./комплаенс", "Кодирование расширенного смысла PAID: новый блок AD-009 vs переформулировка AD-005 (эскалация на родительский spine)", "Определение 'периода' согласия и правил защиты от двойного списания — бизнес+юр.", "Версия контракта v0.2 draft vs /v2 и политика по enum"], "conflicts_with_prior_decisions": ["ADR-002/AD-005: канонический смысл PAID расширяется на подтверждение списания банком плательщика; правило AD-005 сохранено, обобщение вынесено в новый блок AD-009 (текст AD-005 не изменён)", "solutioning.md §1 относил 'автоплатежи' к roadmap вне scope — изменение переводит их в scope отдельной волны"]}
```
