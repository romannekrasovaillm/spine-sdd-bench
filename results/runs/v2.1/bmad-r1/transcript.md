<!-- источник: <HARNESS>/runs-v2.1/cells/wqmwyyw/home/.qwen/projects/-home-architect-project/chats/d187dd23-54e1-4447-99d5-b3610fc30b79.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `read_file(file_path="/home/architect/project/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="/home/architect/project/README.md")`

I'll start by exploring the repository to understand the accepted solution, its conventions, and the handoff rules.

  `run_shell_command(command="find /home/architect/project -type f -not -path '*/.git/*' | sort", description="List all repository files")`
  `read_file(file_path="/home/architect/project/.arch-handoff/MANIFEST.json")`

Let me explore the rest of the repository. Let me look at the docs directory, handoff package, and the openapi file.

Let me delegate broad exploration? Actually let me read files directly since I need details.

Let me list the files.
Let me explore the full structure, handoff rules, and existing docs.

  `run_shell_command(command="find /home/architect/project -type f -not -path '*/.git/*' -not -path '*/.qwen/*' | sort && echo \"--- docs tree ---\" && ls -la /home/arch, description="List project files excluding skills")`
  `read_file(file_path="/home/architect/project/.arch-handoff/TASK.md")`

Let me see the rest of the file list (it was truncated) and read the handoff rules (TASK.md, RUBRIC.yaml, CONSTRAINTS.yaml), and the docs.

Let me get the full tree focusing on project files (excluding .qwen skills).

  `read_file(file_path="/home/architect/project/docs/solutioning.md")`
  `read_file(file_path="/home/architect/project/docs/nfr.md")`

Now let me read the key docs: solutioning.md, nfr.md, contracts/tsp-api.md, contracts/opkc-adapter.md, spec/state-machine.md, the openapi/tsp-api.yaml, and the ADRs. Also, the handoff package (CONSTRAINTS.yaml, RUBRIC.yaml, ARCHITECTURE.md) to understand the conventions.

Let me read in bulk.

  `read_file(file_path="/home/architect/project/docs/contracts/tsp-api.md")`
  `read_file(file_path="/home/architect/project/openapi/tsp-api.yaml")`
  `read_file(file_path="/home/architect/project/docs/spec/state-machine.md")`

Now let me read the contracts and state machine and openapi, and the ADRs. Let me do it in parallel.

  `read_file(file_path="/home/architect/project/docs/adr/ADR-002-model-konsistentnosti-platezha-konechnyy-avtomat-s-idempotentnostyu-na-urovne-shlyuza.md")`
  `read_file(file_path="/home/architect/project/docs/adr/ADR-005-integraciya-s-abs-zachislenie-po-podtverzhdyonnomu-statusu-vozvraty-kak-saga.md")`
  `read_file(file_path="/home/architect/project/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="/home/architect/project/docs/adr/ADR-001-outbox.md")`

Now let me read the ADRs. They're important for conventions (format of ADRs), and the handoff archive. Also the rubric and constraints. Let me read them in parallel. There are 7 ADRs. Let me read them all.

  `read_file(file_path="/home/architect/project/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="/home/architect/project/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="/home/architect/project/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="/home/architect/project/docs/contracts/opkc-adapter.md")`

Now let me read the remaining ADRs (003, 004, 006), the opkc-adapter contract, the vendor rfp, and the handoff files (ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml). Also I should check the bmad-architecture skill since it's the methodological skill installed — "bmad-architecture: Work out and record the architecture decisions... Creates, updates, or validates one". And the task says "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." So I should use the bmad-architecture skill.

Let me first read the skill and see what conventions it enforces (especially for spine updates, arch-handoff).

Let me read remaining core docs and the skill.

  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-architecture/SKILL.md")`
  `read_file(file_path="/home/architect/project/_bmad/config.toml")`
  `read_file(file_path="/home/architect/project/_bmad/config.user.toml")`

Now let me read the handoff ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, and the bmad-architecture skill (SKILL.md) plus reviewer-gate and lint_spine.py, spine-template. This matters because the task says to use methodological skills. The bmad-architecture skill covers "create technical architecture", "architecture spine", "solution design". Our task: prepare an architecture package for the change. So the skill is the right method.

Let me read them.

  `read_file(file_path="/home/architect/project/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="/home/architect/project/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="/home/architect/project/.arch-handoff/ARCHITECTURE.md")`
  `grep_search(pattern="значимост|Маршрут|маршрут|роутинг|Routing|critical|Critical", path="/home/architect/project", glob="!**/.git/**")`

The skill is a coaching skill. But we're operating as an architect asked to prepare a package. The interim: the task is a "prepare an architecture package of this change on top of the accepted solution" — this is an Update intent of the spine? Or a new architecture doc for the change ("архитектурный пакет этого изменения поверх принятого решения").

The task explicitly asks for 7 deliverables:
1. Significance assessment & route (how deep design needed, why)
2. Impact on accepted architecture: which invariants affected, what changes, what doesn't
3. Architectural decision with considered alternatives, consequences, reversibility
4. Contract changes (openapi/tsp-api.yaml) without breaking existing consumers
5. Measurable NFR for new functionality
6. Acceptance criteria and rollback plan
7. What remains for the human architect to decide and why.

And: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." (Change accepted solution files only in the way accepted in this repo.) And use methodological skills.

So the repo convention: the accepted solution is ARCHITECTURE-SPINE.md (invariants AD-001..AD-008 with statuses Proposed/Adopted; changes require a new ADR + ratification), docs/ (solutioning, nfr, ADRs, contracts, spec), openapi/tsp-api.yaml, .arch-handoff/ (rules and handoff package).

Since AD-008 is ADOPTED and others are Proposed, and the spine says "Статусы: блоки в статусе Proposed действуют после ратификации соответствующего ADR. Помеченные [ADOPTED] — ратифицированная реальность." So changes to the spine follow the ADR process: new ADR(s), new AD-n invariant, and status changes go through ADR ratification.

Now, the change: recurring C2B debits by payer consent — SBP subscriptions (подписки СБП). Real-world: СБП subscriptions/автоплатежи. In СБП, this is "СБП-подписка" / "Платежи по подписке" — mechanism where payer gives consent (in their bank app) to a TSP, and recurring debits occur without QR each time. In НСПК's terms this is likely "СБП Подписка"/"рекуррентные платежи". The exact protocol is [ТРЕБУЕТ ПРОВЕРКИ] since NSPK docs are external input.

Key architectural implications:
- New entity: Consent/Subscription (согласие плательщика) — with lifecycle, mandate, limits, revocation.
- New flow: create subscription (payer consent via bank app / QR for consent), then initiation of recurring debit (merchant-initiated, no payer action), notifications, revocation.
- New NSPK protocol surface: consent management, recurring debit initiation — adaptive adapter extension (AD-004: only ОПКЦ adapter knows protocol).
- Status machine: new entity state machine (consent) + new payment type/flow (subscription debit). Need to preserve AD-002 (single source of truth, atomic transitions), AD-003 (idempotency), AD-005 (credit only from confirmed status — a subscription debit still requires NSPK confirmed PAID before crediting).
- AD-001 (isolation) unchanged — subscription logic stays in the gateway.
- AD-006 (trust zones) unchanged.
- AD-007 (hybrid) — does the vendor adapter need to change? Yes: protocol surface for subscriptions; if the vendor doesn't support subscriptions, could require new vendor/version — this is a risk and possibly an A3-level (human decision) item. The hybrid decision AD-008 says core is contract-independent from transport; so the internal adapter contract must be extended, and vendor must support it. Big risk: vendor capability. That's a human-architect decision.
- Regulatory: recurring debits touch 161-ФЗ, and consent requirements — e.g., need for the payer's consent, right to revoke; possibly 152-ФЗ. Also "СБП Подписка" requirements from НСПК.
- Reference model: The mandate/consent must be verifiable, with revocation propagation. Blocking issues: chargebacks/disputes (deferred currently), refunds remain saga.

Also significance route: The repo has a routing convention "Маршрут: Critical (значимость 11/15)". There must be a scoring method somewhere — maybe in bmad-architecture or a routing reference. Let's check the .arch-handoff/RUBRIC.yaml and CONSTRAINTS.yaml and ARCHITECTURE.md. Also maybe there's a route/scoring methodology in docs? The solutioning says "Маршрут: Critical (значимость 11/15)". I need to produce an assessment of significance and route. I should find the scoring rubric. Let me search for "значимость" and "маршрут" and scoring.

Let me check the handoff files and search for a routing rubric.

  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-architecture/customize.toml")`
  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-architecture/references/reviewer-gate.md")`
  `run_shell_command(command="ls -la /home/architect/project/_bmad-output 2>/dev/null; find /home/architect/project -name '*.memlog.md' -o -name '*memlog*' -not -path '*, description="Check for existing memlog and output dirs")`

So the route/scoring methodology (11/15) isn't documented in the repo explicitly. It appears to be a convention. Let me check the bmad-architecture customize.toml and references, and the spine template, to understand conventions for the spine (statuses, Deferred, [ADOPTED], AD numbering, memlog, etc.). Also check if there's a `_bmad-output` folder or `.memlog.md`.

Let me look for a memlog and resolve_customization. Also check the customize.toml.

  `grep_search(pattern="значимост|criticality|significance|11/15|/15|routing|route", path="/home/architect/project/.qwen")`
  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-architecture/references/headless.md")`
  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-architecture/assets/spine-template.md")`

There's no existing memlog or _bmad-output. The existing ARCHITECTURE-SPINE.md was likely created by a previous process (not via this skill's memlog, or the memlog was discarded). The repo has a handoff package in `.arch-handoff/`.

Now: the task. It says "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям." (Prepare the architecture package for this change on top of the accepted solution, so it can be taken to an architecture decision [board] and then handed to implementers.)

Deliverables 1-7 listed. Plus "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." Change accepted solution files only in the way accepted in this repo → i.e., via ADR process (new ADR, spine update with new AD-n and Binds/Prevents/Rule blocks, statuses ratified via ADR). And note that AD-008 is ADOPTED, AD-001..007 Proposed. To change the spine, add a new AD and mark Proposed (ratification pending architecture decision). But the user said "чтобы его можно было вынести на архитектурное решение" — so the change is not yet ratified. So the new AD should be Proposed (pending A3/arch decision), and the ADR should be Proposed.

Now let me check: is there a routing/scoring methodology skill? The route "Critical (значимость 11/15)" suggests a scoring rubric with 15 points across criteria. Let me search the skills for such a rubric — maybe it's in `.qwen/skills` or bundled skills. Search for "15" scoring or "significance". Also check the `bmad-architecture` references/headless.md.

Actually, the user's deliverable #1 "Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему)" — I need to produce a significance/route assessment. The repo convention uses "значимость 11/15" and route names (Critical, and gates A0-A5, and "Fast path"/"Coaching path", and design rigor levels). Let me search for any doc with the scoring method. Maybe in the `.qwen/skills` there is a "solution design" or "arch" routing rubric. Let me grep for "route" in .qwen/skills.

Actually grep earlier across whole project only found 3 matches for "маршрут" — all in project docs. So the methodology isn't stored in the repo. It may be part of the human's framework. I'll reconstruct a defensible 15-point rubric based on the existing solution (dimensions implied: новый компонент, интеграция с внешним оператором, финансовое влияние, КИИ). Let me search skills for "criticality" or "significance".

Let me search for "A0" / "гейт" / scoring in the whole repo including skills.

  `run_shell_command(command="cd /home/architect/project && git log --stat -n 3 && echo \"=== branches ===\" && git branch -a && echo \"=== status ===\" && git status --, description="Inspect git history and branches")`
  `read_file(file_path="/home/architect/project/.qwen/skills/bmad-architecture/scripts/lint_spine.py")`

Now I have a good picture of the conventions. The task is essentially an "Update" of the ARCHITECTURE-SPINE.md at feature altitude (adding a new AD for subscriptions, and updating contracts/NFR/state machine via new ADR), plus producing an architecture package with 7 deliverables.

But careful: the skill says the memlog is the authority and the spine is distilled. The existing repo doesn't have a memlog. The repo's convention for changing accepted decision files seems to be: ADR-based. The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — the accepted way to change decision files is the ADR process: new ADR-008 (next number), new spine AD (AD-009), statuses updated via ratification. But wait — the change is not yet ratified; it must go to the architecture decision board. So the spine change should be Proposed and the ADR Proposed.

Hmm, but I need to think about whether to actually modify ARCHITECTURE-SPINE.md. Deliverable #2 says "Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет." Deliverable #3 "Архитектурное решение с рассмотренными альтернативами..." — that's an ADR. Deliverable #4 contract changes in openapi/tsp-api.yaml. So the package should include:

- A significance/route assessment doc
- An ADR (new, Proposed) for subscription/recurring C2B debits
- Spine update: new AD-009 (Proposed) + possibly note on changed statuses of affected invariants; and update Deferred (subscriptions were not listed as deferred actually; "автоплатежи" is listed as roadmap outside scope in solutioning §1: "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." So this change moves subscriptions from out-of-scope into scope. That's a scope change to the accepted decision → requires ADR + spine update.
- Contract changes: openapi/tsp-api.yaml (add subscription endpoints/schemas, backward compatible), plus docs/contracts/tsp-api.md, docs/spec/state-machine.md (new consent state machine), docs/contracts/opkc-adapter.md (new adapter methods/events — because the vendor must support it; AD-008/AD-004), docs/nfr.md (measurable NFR for new functionality).
- .arch-handoff package regeneration? The TASK.md is a handoff to coding harness. The task says "затем передать исполнителям" (then hand to implementers). The .arch-handoff package is the handoff. But it's for the walking skeleton of the base solution. Should I update it? The instructions say "принятые файлы решения меняй только тем способом, который принят в этом репозитории" — implies I may need to modify them. Maybe I should produce the architecture package and note handoff regeneration as a step (the handoff is regenerated at the implementation stage). Actually the user says "чтобы его можно было вынести на архитектурное решение и затем передать исполнителям" — the package is the input to the architecture decision, and afterward it's handed to implementers. So the package should include (or reference) what's needed for handoff.

Given the scope, I think the right deliverable set:

New/changed files (repo conventions):
1. `docs/solutioning-subscriptions.md` — or better a change package. Hmm. Let me think about what's idiomatic. The repo has `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-00X-*.md`, `docs/contracts/*`, `docs/spec/*`, `ARCHITECTURE-SPINE.md`, `README.md`.

The most idiomatic approach:
- New ADR: `docs/adr/ADR-008-sbp-subscriptions-recurring-c2b.md` (Proposed, A3/human decision pending).
- Update `ARCHITECTURE-SPINE.md`: add AD-009 (or maybe AD-009..AD-010) Proposed, and update the "Deferred" section / statuses. Wait — "подписки/автоплатежи" currently in roadmap out-of-scope. Adding a new AD that brings subscriptions into scope. Keep AD-001..AD-008 intact (don't renumber/reuse). New AD-009.
- Update `docs/spec/state-machine.md`: add consent state machine + new payment origin/flows. Or add a new file `docs/spec/subscription-state-machine.md` to avoid heavy edit? The change should be minimal and additive; but the payment state machine gains a new entry path (subscription debit without QR). Hmm, actually a subscription debit creates a payment in a new way. The existing machine CREATED→QR_ISSUED→PAID... For recurring debits there's no QR. So we need either a new state (e.g., `DEBIT_INITIATED` / `MANDATE_PENDING`) or the payment is created directly in a state meaning "debit initiated to NSPK" and then PAID. Need to be careful not to break AD-005 (credit only from PAID). This is the core architectural decision.
- Update `docs/contracts/tsp-api.md` + `openapi/tsp-api.yaml`: add consent/subscription endpoints (backward compatible: additive optional fields, new paths, new enum values? careful — adding enum values to `status` could break consumers; better to add new optional fields and new schemas/paths).
- Update `docs/contracts/opkc-adapter.md`: add consent/debit methods and events.
- Update `docs/nfr.md`: add NFR for subscriptions.
- Update `README.md` structure listing.
- Maybe update `docs/solutioning.md`? Since it's the "full design", it should reflect the change... but the change is a package on top. The skill's Update guidance: "An update that overrides something from a source input: offer to update that source too, so upstream and the spine don't silently diverge." So solutioning should be updated or a new solutioning doc added.

Given the volume, I think the cleanest and most idiomatic: create a **change package** directory `docs/changes/C2B-subscriptions/` containing the significance assessment, the ADR, impact analysis, NFR delta, acceptance/rollback. But the repo convention puts ADRs in docs/adr and NFR in docs/nfr.md.

Hmm. Let me reconsider what the user actually wants. They're a solution architect (roleplay) and want "архитектурный пакет этого изменения поверх принятого решения". The 7 items map to a specific artifact set. I think the most defensible interpretation and best value:

Create a dedicated change package that follows repo conventions and updates the accepted artifacts via the accepted mechanism (ADR + spine AD + contract version), specifically:

New:
- `docs/changes/CHANGE-001-sbp-subscriptions/README.md` — the package index + significance/route assessment + impact analysis + acceptance/rollback? That might duplicate.

Alternative: The repo is the "decision repo". The idiomatic thing: a new ADR + updated spine + updated contracts + updated NFR. And the "package" is these updates themselves. The 7 deliverables are the content of the ADR + a package overview doc.

Let me structure:

1. `docs/solutioning-subscriptions.md` — the full design addendum: significance/route (item 1), impact on architecture (item 2), the architecture decision reference (item 3 → ADR-008), contract changes summary (item 4), NFR (item 5 detailed in nfr.md but summarized), acceptance & rollback (item 6), human decisions (item 7). Actually that's a big overlap.

Better and cleaner:
- `ARCHITECTURE-SPINE.md` — update (new AD-009 Proposed + Deferred/scope note)
- `docs/adr/ADR-008-*.md` — the architecture decision (item 3), Proposed, with alternatives/consequences/reversibility; also references route (item 1)
- `docs/changes/CHANGE-001-c2b-subscriptions/ASSESSMENT.md` — items 1, 2, 6, 7 (significance/route, impact, acceptance/rollback, human decisions) — "change package README"
- `docs/nfr.md` — add section for subscriptions (item 5)
- `docs/contracts/tsp-api.md`, `openapi/tsp-api.yaml` — contract changes (item 4)
- `docs/spec/subscription-state-machine.md` (new) + maybe update state-machine.md
- `docs/contracts/opkc-adapter.md` — adapter contract extension
- `README.md` — update structure

Hmm, that's a lot of files. It's justified though — the task is substantial.

But wait: the user is roleplaying a solution architect and says "Код не пиши." and "Когда закончишь, кратко перечисли созданные и изменённые файлы." So they expect a set of files. Good.

Now the key substantive architecture. Let me think hard about СБП subscriptions (автоплатежи/подписки СБП) as of real-world knowledge, and mark protocol details [ТРЕБУЕТ ПРОВЕРКИ].

Real-world: NSPK launched "СБП" recurring payments? There is "Автоплатёж СБП" / "СБП Подписка". In the СБП ecosystem, there's "Платежи по QR", and there's the mechanism of "СБП: подписка на автоплатежи" — payer subscribes via their bank app, consent stored, merchant initiates debits. Also relevant: "Периодические платежи СБП" possibly implemented via ОПКЦ with a "mandate"/"подписка" identifier. The exact protocol: [ТРЕБУЕТ ПРОВЕРКИ].

There is also the concept from НСПК: "СБП Подписка" — позволяет ТСП проводить регулярные списания. And "Согласие на периодическое списание". Key entities:
- `Subscription` / `Consent` (mandate): id, payer (masked), tsp, amount/limit, periodicity, purpose, expiresAt, status, revocation.
- `Debit` (списание): a payment initiated by TSP under consent, without payer action; NSPK processes and notifies paid/rejected.
- Consent lifecycle: `DRAFT/CREATED → CONSENT_PENDING → ACTIVE → (SUSPENDED) → REVOKED/EXPIRED`. Payer's consent obtained via redirect to payer's bank (like SBP subscription flow) or via QR for consent.
- Debiting: TSP or bank initiates debit; NSPK returns paid/rejected (e.g., insufficient funds, consent revoked).

Key architecture questions/forks (alternatives):
A. Model consent as a separate aggregate with its own state machine (new component «Реестр согласий/мандатов») vs. as attributes of the payment (no stored consent).
   - Recommendation: separate consent aggregate, single source of truth in gateway DB, because revocation, limits, and reconciliation need it; enables idempotent debits and audit.
B. Payment state machine extension: add a new entry state `DEBIT_PENDING` (or reuse CREATED with a flag `origin=subscription`) vs. new entity.
   - To preserve AD-002/AD-005, a recurring debit is a payment created directly in a "debit initiated / awaiting NSPK" state (no QR_ISSUED), then PAID (confirmed) → CREDITED → COMPLETED. AD-005 still holds: credit only from PAID. Add states to the machine but don't alter existing transitions. Need to decide whether `QR_ISSUED` is reused (no — it's semantically wrong). Add `DEBIT_INITIATED` (or `MANDATE_DEBIT_PENDING`) between CREATED and PAID. Hmm, but is the initiation synchronous (returns paid/rejected) or async (notification)? Likely async with notification. So `CREATED` (or new `DEBIT_ISSUED`) → `PAID`/`FAILED`.
   - Actually maybe simplest: reuse the existing status machine but allow `CREATED → PAID` directly for subscription-origin payments (NSPK confirms). Or add intermediate `DEBIT_ISSUED` mirroring `QR_ISSUED`. Mirroring is cleaner: one new state `DEBIT_ISSUED`.
C. Who holds the mandate: gateway vs. NSPK (ОПКЦ holds consent) vs. payer's bank. In СБП likely the consent is registered with ОПКЦ (payer's bank confirms) and the gateway stores a local mirror for initiation/limits/revocation/audit. Alternative: rely solely on ОПКЦ (no local registry) — but then offline/at-least-once/idempotency and reconciliation suffer, and TSP API can't show consent status without NSPK. Recommend local authoritative-for-processing mirror + NSPK as source of truth for consent existence.
D. Vendor transport capability: does the certified vendor adapter support subscriptions? This is the big dependency/risk. Alternatives: (i) extend existing vendor's adapter (contract addendum, new version) — preferred; (ii) separate vendor/bank module for subscription protocol; (iii) defer the feature until NSPK docs/regulations confirm; (iv) implement in-house (conflicts with AD-008 adopted hybrid for the transport). This is a human/A3 decision if vendor can't support.
E. Money/limits: per-debit amount vs. per-period limit vs. total cap; does the payer set a max per period? Where enforced: gateway pre-check + NSPK authoritative. Also insufficient-funds handling (retry policy? dunning?) — business decision; likely out of scope or deferred.
F. Reversibility/rollback: feature flag per TSP; stop-new-consent; existing mandates revocable; no data migration back; disable debit initiation while keeping revocations/refunds working.

Also must handle: refunds for subscription debits — reuse the existing saga (ADR-005). Disputes still deferred, but subscriptions raise dispute/claim likelihood → note.

Impact on invariants:
- AD-001 isolation: unchanged; subscriptions live in the same gateway/payment contour. Consistent.
- AD-002 single source of truth: extended — a second aggregate (consent) with its own state machine, same discipline (atomic transitions + outbox + audit). Rule amended (extended, not weakened).
- AD-003 idempotency: extended keys (consent id, debit reference/idempotency key for merchant-initiated debit). Must guarantee no double debit.
- AD-004 single ОПКЦ adapter: unchanged; adapter contract extended with consent/debit operations. Vendor capability risk (AD-007/AD-008).
- AD-005 credit only from confirmed status: PRESERVED and reinforced — a subscription debit still credits only after NSPK-confirmed PAID; must explicitly encode that consent existence ≠ PAID. New fitness test.
- AD-006 trust zones: unchanged; possibly extended for consent data (payer PII minimization) — consent storage includes payer identifier → PII minimization (ADR-006 §4).
- AD-007/AD-008 hybrid & contract-independence: the core remains contract-independent; adapter contract extension is the mechanism; vendor must support subscriptions (constraint (2)/(3)); if not — A3 revision.
- AD-007 also caps: "реализация транспорта начинается только после подписания контракта с вендором и получения документации НСПК" — subscriptions require NSPK docs for the subscription protocol; same external input gate.

Contracts changes without breaking consumers:
- Add new optional fields to request/response (e.g., `paymentType`/`origin` optional with default `qr`, `consentId` optional, `subscription` object). Adding new optional fields is backward-compatible per contract §6.
- Add new enum values to `status`? Risky: existing consumers may use exhaustive enums. But new states only appear for subscription payments, which existing consumers don't create. Still, adding enum values is technically a compatible extension (consumers should tolerate unknown). To be safe: introduce a *separate* `subscriptionId`/`debitId` and keep `paymentId` semantics; status enum gets a new value only within subscription flows. Document it as a minor additive change; note consumer guidance. Better: keep `status` enum unchanged by mapping new internal states to existing visible statuses where possible. E.g., subscription debit created → visible `CREATED`, then `PAID` → `CREDITED` → `COMPLETED`; skip exposing a new state; use `origin: subscription` + `consentId` so consumer can distinguish. That avoids enum change entirely! Good — new visible states avoided; internal sub-state `DEBIT_ISSUED` not exposed (like ABS_PENDING). Hmm but is `CREATED`→`PAID` allowed without `QR_ISSUED`? Yes if we document that for subscription-origin payments the machine goes CREATED→PAID (the intermediate internal DEBIT_ISSUED is not exposed). Actually cleaner: expose existing statuses; internal state name `DEBIT_ISSUED` visible as `CREATED`? That's confusing for TSP polling (they'd see CREATED while debit is in-flight). Hmm. For TSP, they'd want to know the debit was submitted. Could use `PAID` only when confirmed. Before confirmation, it's "in flight". `CREATED` is acceptable as "registered, awaiting NSPK". But TSP may want to differentiate "awaiting payer scan" vs "debit submitted". Since subscriptions have no payer action, CREATED→PAID is fine and semantically "registered, awaiting confirmation". Keep enum unchanged = maximal compatibility. I'll propose this as the recommended path, with the alternative (new visible status `DEBIT_ISSUED`, requires /v2 or consumer sign-off) explicitly considered.

Wait — but subscription creation itself is a new flow needing endpoints:
- `POST /v1/subscriptions` (create consent → returns subscriptionId + consentUrl/redirect for payer authorization, or QR for consent)
- `GET /v1/subscriptions/{subscriptionId}`
- `POST /v1/subscriptions/{subscriptionId}/revoke` (merchant-initiated revocation) — but payer revocation happens in payer's bank, gateway learns via notification.
- `POST /v1/subscriptions/{subscriptionId}/debits` (initiate a debit under consent) — idempotent via Idempotency-Key; returns a `paymentId` (or `debitId`). Reuse payments endpoints for status/refund? A debit is a payment, so it should return the same `Payment` resource (paymentId) with `origin=subscription`. That means refunds/status/refunds endpoints work unchanged. 
- `GET /v1/subscriptions/{subscriptionId}/debits` maybe.
- Webhooks: `subscription.activated`, `subscription.revoked`, `subscription.expired`, `debit.failed`? Debit outcomes can reuse `payment.completed`/`payment.failed`.

Consent statuses: `PENDING_CONSENT`, `ACTIVE`, `REVOKED`, `EXPIRED`, `SUSPENDED`, `REJECTED`.

Adapter contract additions (core ↔ transport):
- `createConsent`/`registerSubscription` (reference = subscriptionId), `getConsentStatus`, `revokeConsent`/internal, `initiateDebit` (reference = paymentId, consentRef, amount), `getDebitStatus`; events `consent.activated`, `consent.revoked`, `consent.rejected`, `debit.paid` (or reuse `payment.paid` with reference=paymentId), `debit.rejected`.

Now NFR for new functionality (measurable):
- Consent creation latency p95 < 1s (gateway-side, excluding NSPK), activation webhook p95 < 5s.
- Debit initiation API latency p95 < 500ms (without NSPK), result notification p95 < 5s, crediting p95 < 60s (same).
- Idempotency: repeated debit with same Idempotency-Key → 0 duplicate debits (0 double charges); repeated NSPK events → state unchanged.
- Throughput: subscriptions add ≤ +20% to base 200 TPS sustained (or specify debit throughput target, e.g. 50 TPS sustained/150 burst) — must fit within existing 200/500.
- Consent ledger RPO=0, availability ≥99,95%.
- Peak annual/period billing spikes: recurring debits cluster at calendar boundaries (1st of month, 00:00-02:00) → burst profile; specify burst 500 TPS with 1000 for 1 min? The base already has that. Add: "periodic burst": ≥3× sustained for 15 min on billing windows.
- Revocation propagation latency: ≤ 60 s from payer revocation (NSPK) to gateway blocking new debits; 0 debits after revoke ack.
- Limit enforcement: 100% of debits exceeding consent limit are rejected before NSPK (pre-check) — 0 over-limit debits sent.
- Reconciliation: consent ledger reconciled daily; discrepancies 0.
- Audit: 100% consent lifecycle transitions logged.
- Availability of consent flow.
- Debit success handling: failed debits (insufficient funds) → notification p95 < 5s; no auto-retry without policy (business decision).

Acceptance criteria (testable) and rollback:
- Fitness tests: credit only from PAID (extend to subscription debits); no debit without active consent; no debit after revocation; idempotent repeat; atomic transitions; consent expiry enforcement.
- E2E: create consent → activate (mock NSPK) → debit → PAID → credit → webhook; refund a debit.
- Negative: revoked consent debit → rejected; over-limit → 422 pre-check; duplicate Idempotency-Key → same paymentId; duplicate NSPK paid event → single credit; NSPK unavailable → debit queued/deferred, no credit.
- Rollback: feature flag per TSP; stop-new-consent; stop-new-debit; keep revocation/refund processing; revert to QR-only; no data migration; signals/triggers (double debit, credit without PAID, consent misuse AML alert, NSPK test failure); decision owner (A3/business + architect); align with existing rollback plan §8.

Human-architect decisions (item 7):
- Vendor/transport capability for subscriptions: extend existing adapter vs. new module vs. postpone (A3-level, ADR-007/AD-008 constraint). Requires NSPK docs.
- Consent storage location & legal model: is the gateway the mandate holder or a mirror? Legal/regulatory sign-off (payer consent form, revocation rights, 161-ФЗ/152-ФЗ, NSPK rules).
- Who may initiate debits (TSP vs bank) and allowed periodicity/limits defaults; dunning/retry policy on insufficient funds (business).
- Whether new visible status/enum is needed → /v2 decision with TSPs.
- Refund/dispute policy for subscription debits; chargebacks (disputes currently deferred).
- AML/antifraud thresholds for recurring (velocity checks) — currently gap.
- PII minimization approach for payer identifiers in consent.
- Scope: which ТСП segments (cinema/ЖКХ/связь) and staged rollout.

Also significance/route: The change is significant: new external protocol surface (subscription), new financial flow and entity, new regulator touchpoints, vendor dependency, potential dual control with payer's bank. Score: I should present a rubric. The base was 11/15 Critical. I'll propose this change scores e.g. 12/15 → Critical (route: full design, A1–A4 gates, human A3 for vendor/legal). Or maybe significance is slightly lower because it reuses the core? Hmm.

I should be careful: the scoring rubric (what 15 points are) isn't in the repo. I'll define the dimensions explicitly in the assessment and give a transparent score, noting the rubric is reconstructed from the existing solutioning's rationale (новый компонент, интеграция с внешним оператором, финансовое влияние, КИИ + maybe регуляторика, обратимость, объём). Let me design a 5-dimension × 3-point rubric = 15:
D1. Влияние на деньги/финансовые риски (double debit, unauthorized debit) — 3
D2. Внешняя интеграция/протокол (новый участок протокола НСПК, вендор) — 3
D3. Регуляторика/КИИ/ПДн (согласие плательщика, 161-ФЗ, 152-ФЗ, НСПК) — 3
D4. Влияние на принятую архитектуру (инварианты, контракты, данные; миграция) — 2
D5. Обратимость/операционный риск (feature flag, откат) — 1
Total = 12/15 → Critical.

Hmm the base was 11/15. Let me make it defensible: I'll say the rubric is a 5×3 (0–3 per dimension). For the change: D1=3, D2=3, D3=3, D4=2, D5=1 → 12/15. Route: Critical; full design depth: new ADR + spine AD + contract versioning + new spec + NFR delta + acceptance/rollback + reviewer gate; A3 human decision required (vendor + legal + scope).

Actually, I worry about inventing a rubric not present. Better: present the significance assessment as a reasoned multi-dimension assessment AND map it to the existing route vocabulary, explicitly stating that the base's 11/15 rubric isn't documented in-repo and giving my scoring sub-dimensions transparently as a reconstruction, flagged as an assumption. That's honest.

Now, about modifying ARCHITECTURE-SPINE.md — should I? The user says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The accepted way: ADR + spine. And "чтобы его можно было вынести на архитектурное решение" — the change is Proposed. So yes, I'll add AD-009 (Proposed) to the spine with Binds/Prevents/Rule, consistent format, and update the scope note (sв scope/roadmap) minimally. Keep AD-001..008 untouched. Also add a line under "Контракты и версии" perhaps.

But hold on: the spine currently doesn't have a frontmatter. The template has frontmatter, but the existing spine starts with "# ARCHITECTURE-SPINE — ..." and has a custom structure with "Родительский spine", "Статусы", AD blocks with Binds/Prevents/Rule, Deferred, "Контракты и версии". So I'll follow the existing shape (not the template's frontmatter), since repo convention (ratify existing shape) wins over the skill template.

Also: the existing spine's AD blocks are in the shape:
```
## AD-00X. Title

- Status: Proposed (ADR-00X)
- **Binds**: ...
- **Prevents**: ...
- **Rule**: ...

## Rule text
```
Actually AD-001 has a "Rule" bullet plus a "## Rule" prose? Let me re-read: AD-001 block:
```
## AD-001. Изоляция платёжного контура

- Status: Proposed (ADR-001)
- **Binds**: ...
- **Prevents**: ...
- **Rule**: Любое взаимодействие ...

## Rule
```
Hmm no, looking again:
```
- **Rule**: Любое взаимодействие с АБС и ОПКЦ СБП — только через адаптеры СБП-шлюза (проверка: ...).

## AD-002. ...
```
So it's just the bullet. Good. I'll match.

Now, the deliverables require the ADR to include alternatives/consequences/reversibility, matching the existing ADR format exactly (Date, Status, Owner, Related, Context, Decision, Alternatives Considered table, Consequences Positive/Negative, Reversibility, References).

Also ADR numbering: next is ADR-008. And spine AD numbering: next is AD-009.

Wait — there's a subtlety: The spine says statuses: Proposed blocks act after ratification. The base solution's ADRs are all Proposed except ADR-007 Accepted. The package must "go to architecture decision" (A3). So ADR-008 should be Proposed and require A3/human ratification.

But there might be an issue: the user says "вынести на архитектурное решение" (to the architectural decision board) — meaning this is a proposal, not adopted. Good, Proposed.

Now, where to place the "change package" with items 1,2,6,7? Options:
(a) Put everything in the ADR. But ADR format is constrained.
(b) Create `docs/changes/CHANGE-001-c2b-subscriptions/` with:
   - `ASSESSMENT.md` (items 1, 2, 6, 7 + index)
   - Perhaps the ADR lives in docs/adr per convention.
(c) Extend `docs/solutioning.md` with a new section and `docs/solutioning-subscriptions.md`.

The `bmad-architecture` skill produces a spine as the build substrate plus optionally a fuller "solution design" companion. Given the repo's convention of `docs/solutioning.md`, an addendum `docs/solutioning-subscriptions.md` fits. But the 7-item "package" is more like a change proposal document.

I think the cleanest, most idiomatic, and most useful:

**Change package directory** `docs/changes/CHANGE-001-c2b-subscriptions/` — this keeps the accepted files clean and clearly separates the proposal:

```
docs/changes/CHANGE-001-c2b-subscriptions/
  README.md          — index + items 1 (значимость/маршрут), 2 (влияние), 6 (приёмка/откат), 7 (решения человека)
  ADR-008-...md      — hmm, ADRs live in docs/adr per repo convention
```

Hmm, ADR location convention: docs/adr/. I'll put the new ADR there. The change package README can host items 1,2,6,7 and summarize item 3 (pointing to ADR) and item 4 (pointing to contracts).

And update in place (accepted artifacts), via the accepted mechanism:
- `ARCHITECTURE-SPINE.md` — add AD-009 (Proposed), update Deferred/scope.
- `docs/nfr.md` — add section 7 for subscriptions.
- `docs/contracts/tsp-api.md` — v0.2 draft section for subscriptions (additive).
- `openapi/tsp-api.yaml` — version 0.2.0, additive paths/schemas.
- `docs/contracts/opkc-adapter.md` — v0.2 section for consent/debit.
- `docs/spec/state-machine.md` — add consent state machine + subscription entry path.
- `README.md` — update structure/status.

That's 7 modified + 2 new (ADR-008, change README). Maybe also regenerate `.arch-handoff`? The handoff package is generated for the coding harness at implementation stage; the task says "затем передать исполнителям" (after the architecture decision). I think I should NOT regenerate the handoff (that's an implementation-stage artifact, and the ADRs aren't ratified yet). But I should mention it as a next step and maybe note that the handoff must be regenerated after A3. Actually — the repo's `.arch-handoff/` is the handoff package. The user says "принятые файлы решения меняй только тем способом, который принят в этом репозитории" — the handoff package is a generated artifact (MANIFEST created_at, sources). Modifying it now would be premature and would violate "handoff after ratification". I'll leave it and note it.

Hmm, but the user explicitly listed deliverable 6 "Критерии приёмки и план отката" — these belong in the change package README and/or the handoff. I'll put them in the change README and NFR-adjacent.

Let me reconsider whether to create a separate change dir vs. put it all in the package. Given repo has no `docs/changes/`, introducing a new directory is a mild convention addition, but it's clean. Alternatively name it `docs/solutioning-subscriptions.md` (matching docs/solutioning.md) and put items 1,2,6,7 there, plus mention ADR/contracts. That's closer to repo conventions (docs/ has solutioning.md, nfr.md, adr/, contracts/, spec/, rfp/). Hmm, but the "package" framing suggests one entry point. I could do both minimal: add `docs/changes/README.md`? Over-engineering.

Let me pick: `docs/solutioning-subscriptions.md` — "Solutioning-аддендум: подписки СБП (рекуррентные C2B-списания)". It contains items 1,2,3 (summary + link to ADR-008),4 (summary + links),5 (summary + link to nfr),6,7. And it explicitly is a "пакет изменения поверх принятого решения". This matches the repo's `docs/solutioning.md` naming. Good — no new directory. Actually the file name is long but fine.

Hmm, but item 1 is "оценка значимости и маршрута" — a solutioning addendum can carry that.

Wait, maybe better to name it `docs/solutioning-recurring-c2b.md` or `docs/solutioning-subscriptions.md`. I'll use `docs/solutioning-subscriptions.md`.

Hmm, let me reconsider: the user says "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение". Maybe they'd like a single package entry. I'll make `docs/solutioning-subscriptions.md` the entry point ("архитектурный пакет"), which indexes the changes. And README links it.

Now let me also double check git conventions: recent commits: "Рабочее окружение", "Принятое решение: импорт". The user didn't ask to commit. "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — this is about how to change decision files (ADR process), not about committing. I won't commit unless asked. Actually the phrasing "меняй только тем способом, который принят" might also hint at ADR-based change vs. direct rewriting. I'll follow ADR process and also not silently rewrite; I'll keep changes additive and clearly marked Proposed.

Let me check the git history to see how the accepted decision was made — maybe there's a convention of a commit per decision. Let me check `git log -p --stat` for the decision commit? Might be large. Let me just check log stat.

Let me also verify there's no existing branch/PR convention. I'll run git log.

Also I should check the bmad-architecture lint script to make sure my spine edit passes lint (placeholders, duplicate AD IDs, missing Binds/Prevents/Rule, unpinned stack versions). The spine has no "Stack" section, and lint might require pinned versions — but the existing spine may already fail lint. Let me read lint_spine.py to know constraints, and run it via uv if available. Actually the markdown lint checks AD blocks for Binds/Prevents/Rule. Let me read it.

Let me now run git log and read lint_spine.py.

  `read_file(file_path="/home/architect/project/docs/rfp/vendor-rfp.md")`

Good. There's a git tag "accepted" on the current HEAD. So the "accepted solution" is tagged. Interesting: the accepted decision is the commit with tag `accepted`. That means modifying accepted files directly might be considered changing the accepted baseline. The user says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." Hmm — "the accepted solution files — change only in the way accepted in this repo". 

The repo convention for changing decisions: ADR + spine, and the ADRs are marked Proposed/Accepted. The tag "accepted" is at HEAD (working environment commit). Hmm, tag is on 7a8623f which is the "Рабочее окружение" commit (skills). The decision import commit 8f79410 is the parent. So tag "accepted" marks the state including environment.

I think the safest interpretation: don't rewrite the accepted solution; instead produce the change package that (a) adds a new ADR, (b) adds a new spine AD marked Proposed (extending, not weakening), (c) extends contracts additively with a version bump, (d) extends NFR/spec additively. That is the accepted mechanism.

Given the tag, maybe I should be conservative about editing ARCHITECTURE-SPINE.md. But the deliverable #2 explicitly asks "какие инварианты затронуты, что меняется, что нет" — that could be entirely in the package doc without editing the spine. And "принятые файлы решения меняй только тем способом, который принят в этом репозитории" strongly implies I *should* change them, but only via the accepted mechanism.

Hmm, "тем способом, который принят в этом репозитории" — the accepted way in this repo = ADR process + spine Proposed blocks. So editing the spine to add AD-009 (Proposed) is exactly the accepted way. Good.

Let me now decide the final artifact plan and get moving. This is a big writing task. Let me consider using subagents for parallel drafting? The files are interdependent (ADR is referenced by spine, contracts). Better to write them myself carefully and consistently. But it's a lot of content. I could delegate independent chunks, but consistency matters and the architectural reasoning is the core value. I'll write them myself.

Let me plan the files:

NEW:
1. `docs/adr/ADR-008-sbp-subscriptions-recurring-c2b.md` — architectural decision (Proposed), full ADR format, with alternatives/consequences/reversibility. This is deliverable 3.
2. `docs/solutioning-subscriptions.md` — the architecture change package: items 1 (significance/route), 2 (impact on invariants), 4 (contract change plan summary), 5 (NFR delta summary), 6 (acceptance + rollback), 7 (human decisions). Index pointing to ADR/contracts/spec. This is the "package" entry point.
3. `docs/spec/subscription-state-machine.md` — consent/mandate state machine + debit entry path; deliverable for the new domain.
   - Or add to `docs/spec/state-machine.md`. I think a separate spec file is cleaner and additive, and cross-link from state-machine.md.
4. `docs/contracts/subscription-api.md`? No — extend tsp-api.md and opkc-adapter.md in place (additive sections) per repo convention (the contract files are the contracts). Hmm, but "Принятые файлы решения меняй только тем способом..." — adding a section to a Draft contract is fine (contracts are Draft, versioned).

MODIFY:
5. `ARCHITECTURE-SPINE.md` — add AD-009 (Proposed, ADR-008), adjust Deferred/scope notes, add contract version line.
6. `docs/nfr.md` — add section 7 "NFR — подписки СБП (рекуррентные C2B-списания)" (item 5).
7. `docs/contracts/tsp-api.md` — v0.2: new section for subscriptions + version bump; add origin/consentId to payment; new webhooks.
8. `openapi/tsp-api.yaml` — version 0.2.0; additive paths/schemas (item 4).
9. `docs/contracts/opkc-adapter.md` — v0.2: consent/debit operations + events.
10. `docs/spec/state-machine.md` — cross-link + subscription entry path note (or leave and just link). I'll add a short section referencing the new spec.
11. `README.md` — update structure + status.
12. `docs/solutioning.md` — maybe add a short pointer? It says roadmap outside scope includes "автоплатежи". I should update that line to reference the change package. Minimal edit. Hmm, "Принятые файлы решения меняй только тем способом" — solutioning.md is the accepted design; changing it should be done via the package. A minimal cross-reference edit (not rewriting decisions) is fine. Actually, to avoid silently diverging, I'll add one line under §1 roadmap noting the change package. Or better, avoid editing solutioning.md and put everything in the package, and note in the package that solutioning.md §1 roadmap must be updated at ratification. Hmm. The skill says "offer to update that source too, so upstream and the spine don't silently diverge." Since I'm preparing for a decision (not ratified), I'll add a pointer line in solutioning.md §1 marked as proposed change. That's honest and prevents divergence.

Also `.arch-handoff/` — should NOT regenerate now (post-ratification). I'll note it in the package (next steps) and add open question. Actually the user asked "затем передать исполнителям" — I'll include a "handoff delta" section describing what must change in the handoff package after A3. Good.

That's ~12 files. Reasonable.

Wait — let me reconsider file #2 name. To make the "package" explicit, maybe put the package at `docs/changes/c2b-subscriptions/` with README. But repo convention doesn't have changes dir. I'll go with `docs/solutioning-subscriptions.md` as the package doc, clearly titled "Архитектурный пакет изменения: подписки СБП (рекуррентные C2B-списания)".

Now, let me nail the technical architecture content precisely.

### Domain model for СБП subscriptions

Entities:
- **Согласие (Consent / Мандат)** — authorizes a ТСП to debit a payer. Attributes: `consentId`, `tspId`, `payerId` (masked/opaque, minimization per ADR-006), `amountLimit` (per debit) / `periodLimit` / `totalLimit`? (protocol-dependent [ТРЕБУЕТ ПРОВЕРКИ]), `periodicity` (e.g., MONTHLY/WEEKLY/ON_DEMAND), `purpose`, `startAt`, `expiresAt`, `status`, `nspkConsentId`, audit.
- **Списание (Debit)** = a payment with `origin=subscription`, `consentId`.
- Payment machine reused: a debit is a **payment** created by TSP under consent; no QR (no payer action); NSPK processes → PAID/REJECTED; then CREDITED → COMPLETED as today. AD-005 preserved.

Consent state machine (new spec):
- `CREATED` — consent registered in gateway, not yet confirmed by payer/NSPK.
- `PENDING_PAYER` — payer authorization initiated (redirect/QR to payer's bank); awaiting payer consent.
- `ACTIVE` — payer consent confirmed via NSPK; debits allowed.
- `SUSPENDED` — temporarily blocked (e.g., NSPK transport unavailable? or payer freeze) — maybe not needed; keep minimal.
- `REVOKED` — revoked by payer (via bank) or ТСП/bank; debits blocked. Terminal-ish (can be re-created as new consent).
- `EXPIRED` — expiry reached. Terminal.
- `REJECTED` — payer declined / NSPK rejected. Terminal.
- Maybe `PAYER_ACTION_REQUIRED`?
Keep: `CREATED → PENDING_PAYER → ACTIVE → REVOKED | EXPIRED`; `PENDING_PAYER → REJECTED`; terminal: REJECTED, REVOKED, EXPIRED. Possibly `ACTIVE → EXPIRED`.

Invariants:
- Debit initiation only from `ACTIVE` consent (and not expired, within limits).
- Revocation is monotonic: `REVOKED` is terminal within the consent lifetime; no debit accepted after revocation is known; in-flight debits that NSPK confirms before revocation ack may still be processed but flagged.
  - Careful: revocation vs in-flight debit race. Define: once revocation ack is recorded, no new debit; debits already sent to NSPK may complete → must still be credited (NSPK confirmed = PAID → credit) and reported; ТСП/bank handles per rules. This is a legit architecture call.
- Consent id is the idempotency/correlation key for debits; debit referenced by paymentId.
- Payer's consent is authoritative at NSPK (and payer bank); gateway keeps a mirror; on divergence — reconcile, stop debits, escalate.

Payment machine extension (minimal, additive):
- New **origin**: `qr` (existing) | `subscription` (new).
- New internal state `DEBIT_ISSUED` (technical sub-state; visible to ТСП as `CREATED`), mirroring `QR_ISSUED`; transition `CREATED → DEBIT_ISSUED` on debit registration at NSPK; then `DEBIT_ISSUED → PAID` on NSPK confirmation. `DEBIT_ISSUED → FAILED` on rejection.
- Existing `QR_ISSUED` path untouched.
- All transitions still atomic (AD-002) and idempotent (AD-003); credit only from PAID (AD-005).
- Refund saga reused unchanged (ADR-005).

Hmm — do I even need DEBIT_ISSUED? Could reuse CREATED→PAID directly. But then CREATED means "awaiting NSPK confirmation" for subscription and "awaiting QR issuance" for QR — ambiguous internally. A distinct internal state is cleaner and testable, and not exposed (like ABS_PENDING). I'll define `DEBIT_ISSUED` as internal, exposed as `CREATED`. Actually wait: the existing spec exposes `CREATED` and `QR_ISSUED` to TSP. If subscription debits expose `CREATED` until PAID, existing TSP pollers see a plausible status. Good. But is it valuable to expose a distinct status so ТСП knows the debit was submitted? They got a 201 with paymentId; polling until PAID/FAILED is fine. Keep enum unchanged → maximum compatibility (item 4). I'll present the alternative (new visible `DEBIT_ISSUED`) as considered/rejected-for-now (would need /v2 or explicit consumer sign-off).

### API contract changes (additive)

Common:
- Add optional field `origin: qr | subscription` (default `qr`) to `Payment` response and `PaymentRequest`? Request for subscription debit goes to a different endpoint, so `origin` mainly in responses.
- Add optional `consentId` in `Payment` response for subscription-origin payments.
- New header: reuse `Idempotency-Key` on all new POSTs.

New endpoints (all under /v1, additive):
1. `POST /v1/subscriptions` — register consent (ТСП → gateway). Request: `tspId`, `payerPhone`/`payerId`(masked?), `amountLimit`/`periodLimit`, `periodicity`, `purpose`, `expiresAt`, `redirectUrl`, `merchantConsentId`. Response 201: `subscriptionId`, `consentUrl` (payer authorization deep link/QR), `status: PENDING_PAYER`.
   - Actually payer consent likely via QR/redirect to payer's bank app (like СБП подписка). So response includes `consentUrl` / `qrUrl`.
2. `GET /v1/subscriptions/{subscriptionId}` — status.
3. `POST /v1/subscriptions/{subscriptionId}/revoke` — ТСП-initiated revocation (idempotent). Response: status REVOKED.
4. `POST /v1/subscriptions/{subscriptionId}/debits` — initiate a recurring debit. Request: `amount`, `paymentPurpose`, `merchantOrderId`, `idempotency` via header. Response 201: `Payment` (paymentId, status CREATED, origin=subscription, consentId, amount, ...). Reuses payment status/refund endpoints.
5. `GET /v1/subscriptions/{subscriptionId}/debits` — list debits (paged) — optional, for ТСП reconciliation. Could be deferred. I'll include as optional.
6. `POST /v1/subscriptions/{subscriptionId}/debits` idempotency: same key+body → same paymentId; same key+different body → 409.

Wait, should debits be at `/v1/payments` with `consentId`? Alternative: `POST /v1/payments` with `origin=subscription`+`consentId`, reusing the existing path (very compatible). Hmm. Options:
- A: `POST /v1/payments` with optional `consentId` → reuses everything (payment resource), no new path; but semantically mixes QR and debit.
- B: `POST /v1/subscriptions/{id}/debits` → clearer resource model, nests debit under consent, returns a Payment.
I lean B (clear ownership, consent is the guard), returning the same `Payment` schema so status/refund endpoints are unchanged. I'll present A as an alternative (max reuse, less clear).

Webhooks (additive, new event types):
- `subscription.activated` — consent became ACTIVE (payer authorized).
- `subscription.rejected` — payer declined / NSPK rejected.
- `subscription.revoked` — consent revoked (payer/bank/ТСП), debits stop.
- `subscription.expired`.
- `debit.failed`? Debit outcome already covered by `payment.completed`/`payment.failed` (since debit is a payment). Keep payment.* for debits, add subscription.* for consent lifecycle. Good — minimal new events.
- Payload for subscription events: `eventId`, `type`, `subscriptionId`, `tspId`, `status`, `consentId?`, `timestamp`.

Backward compatibility analysis (item 4):
- All changes additive: new paths, new schemas, new optional fields, new webhook event types.
- No existing field removed/renamed; no type change; `status` enum unchanged (new internal states not exposed) → no consumer break.
- New error codes added: `SUBSCRIPTION_NOT_ACTIVE` (422), `CONSENT_LIMIT_EXCEEDED` (422), `SUBSCRIPTION_NOT_FOUND` (404), `SUBSCRIPTION_EXPIRED` (422). Additive to the code registry.
- Consumers that don't implement new webhooks: gateway must not send subscription events to ТСП who have no subscriptions → no change for existing ТСП. Also webhook `type` unknown to old consumer → they should ignore; note in contract §5.
- Versioning: minor bump 0.1→0.2 is additive; no /v2 needed. Keep `info.version: 0.2.0`. Contract doc says "Добавление опциональных полей — обратно совместимо". Good.
- TSP capability negotiation: maybe add `capabilities: ["subscriptions"]` on TSP registration; or feature flag per TSP. I'll add optional `features`/onboarding: subscription features enabled per TSP (feature flag) — supports rollback.

### Adapter contract changes (core ↔ transport vendor)

New synchronous ops:
- `createConsent` (reference = subscriptionId, tspId, limits, periodicity, purpose) → `consentId` (NSPK), `consentUrl`/QR, expiresAt.
- `getConsentStatus` (consentId) → PENDING/ACTIVE/REVOKED/REJECTED/EXPIRED.
- `revokeConsent` (consentId, reason) → REVOKED.
- `initiateDebit` (reference = paymentId, consentId, amount, purpose) → ACCEPTED (result via event).
- `getDebitStatus` (paymentId/qrId?) — reuse `getPaymentStatus`? For debits, status by reference. I'll add `getDebitStatus` or generalize `getPaymentStatus` with `reference`. Keep `getPaymentStatus` and note it covers debits by `reference`.
- `getConsentReconciliationReport` — or extend `getReconciliationReport` with type=consent.

New async events:
- `consent.activated` (reference=subscriptionId, consentId, payerMasked?)
- `consent.rejected`
- `consent.revoked`
- `consent.expired`
- `debit.paid` / `debit.rejected` — or reuse `payment.paid`/`payment.rejected` with reference=paymentId. Reuse is better (debit IS a payment). I'll reuse `payment.paid`/`payment.rejected` and note origin.

Vendor requirements delta (RFP): support subscriptions/consent protocol, idempotency by reference, test contour scenarios (activation, revocation, debit rejected/insufficient funds), reconciliation for consents, NSPK requirements. This is a key human decision / RFP delta.

### NFR (new, measurable)

Section 7 in nfr.md:
- Consent activation notification delivery p95 < 5 s from NSPK event (same as notifications).
- Consent creation API p95 < 500 ms gateway-side; consent activation end-to-end (payer authorizes → gateway ACTIVE) p95 < 10 s excluding payer bank time? Hmm payer-dependent, can't measure. Define gateway-side: from NSPK `consent.activated` event to ACTIVE state p95 < 2 s.
- Debit initiation API p95 < 300 ms gateway-side (no NSPK); debit confirmation→credit p95 < 60 s (existing SLA).
- Idempotency: 0 duplicate debits for repeated `Idempotency-Key`; 0 double credit on repeated NSPK events (fitness).
- Revocation: from NSPK revocation event to debits blocked ≤ 60 s (p95); 0 debits accepted after revocation state recorded.
- Limit enforcement: 100% pre-check of consent limits at gateway; 0 over-limit debits forwarded to NSPK.
- Throughput: subscription debits add ≤ +50% base; design target: sustained 100 TPS debit, burst 300 TPS, within existing 200/500 gateway envelope (or combined 200/500 unchanged). Billing-window burst: ×3 sustained for 15 min.
- Consent storage: RPO=0, availability ≥99,95%.
- Reconciliation: consents daily, discrepancies 0.
- Audit: 100% consent transitions in immutable log.
- PII: payer identifier masked/stored minimized (existing NFR §5 applies).

### Acceptance criteria (testable, incl. negative) & rollback

Acceptance (A4):
1. Fitness: credit only from PAID for `origin=subscription` too (no credit from CREATED/DEBIT_ISSUED).
2. Fitness: debit rejected if consent not ACTIVE / expired / revoked / over limit (pre-check, no NSPK call).
3. Idempotency: repeat `POST .../debits` same key → same paymentId, one NSPK debit; repeat NSPK `payment.paid` → single credit.
4. E2E mock: create consent → activate → 3 debits → refund one → webhooks.
5. Revocation race: revoke then debit → 422; debit in-flight then revoke → debit completes as PAID and is credited, reported.
6. NSPK unavailable → debit not credited, queued/retry, visible in unfinished ops.
7. Atomicity: crash between state change and outbox → no divergence (test).
8. Compatibility: existing QR scenario regression suite passes unchanged (no enum/field breakage).
9. Load: NFR targets.
10. Audit/ISO: consent transitions 100% in audit log.

Rollback plan:
- Feature flags: per-TSP subscriptions enablement (`tsp.features`), global kill-switch for new consents and new debits.
- Staged: (1) pilot ТСП; (2) wave.
- Rollback triggers (signals): any double debit; any credit without NSPK PAID; consent-revocation breach (debit after revocation ack); AML/fraud alert rate spike; NSPK test/conformance failure; error budget burn.
- Rollback steps: (a) disable new debits globally (existing consents stop charging; ТСП notified); (b) disable new consent creation; (c) keep revocation + refund + status processing online (must remain); (d) revert release (rolling) — DB schema additive, no destructive migration; (e) data: consents remain in DB (source of truth), no rollback migration; reconciliation continues; (f) communicate to ТСП/payers per NSPK/bank rules about suspended charges.
- Decision owner: business owner + solution architect (A3) with SRE/ИБ; ADR-008 reversibility = reversible pre-prod, costly post-prod (consents outstanding) but structurally reversible.
- Note: outstanding consents are the hard part — you can't "undo" payer consents; must revoke cleanly; hence keep revocation endpoints alive in any rollback. This is a key point.

### Human-architect decisions (item 7)

1. **Vendor/transport capability & procurement** (A3): extend existing vendor's adapter with the subscription protocol vs. second module vs. postpone until NSPK docs confirm protocol; ADR-007/AD-008 constraints. Why human: commercial/contractual, affects cost/timeline, and NSPK docs are external input.
2. **Legal/regulatory model of the consent**: is the gateway a mandate holder or a mirror; consent form and revocation rights; 161-ФЗ/152-ФЗ/НСПК rules; whether payer consent requires additional bank-side confirmation. Why human: legal sign-off, not an engineering call.
3. **Business policy: limits, periodicity, dunning/retry on insufficient funds, notifications to payer before debit, cooling-off** — product/legal; affects UX and fraud.
4. **Scope & staging**: which segments/ТСП, pilot, whether subscription debits are allowed for all MCCs; interaction with existing ТСП contracts.
5. **AML/antifraud thresholds for recurring** (velocity, per-payer caps) — currently a gap; requires business/ИБ decision.
6. **Whether to expose a new visible status/`origin`** and the deprecation/consumer-communication plan — depends on ТСП polls.
7. **Disputes/chargebacks policy for subscription debits** — disputes are currently deferred; subscriptions increase dispute likelihood → re-scope decision.
8. **PII minimization approach** for payer identifiers in consent (tokenization vs masked storage) — ИБ.
9. **Confirmation of NSPK protocol details** ([ТРЕБУЕТ ПРОВЕРКИ]) — external input; blocks implementation of transport.

### Alternative considered (ADR-008) — main options

A. **Расширить ядро шлюза новым агрегатом «согласие» + новыми операциями протокола в существующем адаптере** (recommended/hybrid-consistent).
B. Отдельный микросервис «рекуррентных платежей» со своей БД и своим адаптером (BFF) — conflicts with AD-001 (single point to АБС/ОПКЦ), splits source of truth, more reconciliation. Reject.
C. Хранить согласие только в НСПК, шлюз без локального реестра (stateless passthrough) — cannot enforce limits/audit/idempotency offline, no local source of truth (violates RPO=0 spirit, AD-002), breaks ТСП API status. Reject.
D. Реализовать транспорт подписок собственными силами (in-house) — conflicts with AD-008 adopted hybrid (transport must be vendor/certified). Reject unless A3 revises.
E. Отложить (defer) до получения протокола и требований НСПК — valid baseline; the package can be ratified conditionally but implementation gated on docs. Actually I should present "defer" as an explicit alternative and note it's the fallback if the vendor can't support or NSPK docs contradict.
F. Model debit as a normal QR payment with static QR re-use — no; defeats purpose (payer action each time).

Also within the decision: consent storage and the revocation race semantics; new state machine.

Reversibility of ADR-008: **reversible** pre-production; **costly/reversible with outstanding consents** post-production — feature flags + revocation path keep it safe; no data migration back (consents retained as source of truth for audit). Align with rollback plan.

Now — the significance/route assessment rubric. I'll define explicitly:
Dimensions (each 0–3):
1. Финансовый риск — 3 (несанкционированные/двойные списания, возвраты).
2. Внешняя интеграция — 3 (новый участок протокола НСПК, зависимость от вендора).
3. Регуляторный/КИИ/ПДн — 3 (согласие плательщика, 161/152/115-ФЗ, КИИ).
4. Влияние на принятую архитектуру — 2 (новый агрегат + состояния, но ядро/инварианты сохраняются; контракты расширяются аддитивно).
5. Обратимость/операционка — 1 (фиче-флаги, откат есть, но согласия плательщиков «не откатить» — нужно аккуратно отзывать).
Итог 12/15 → маршрут Critical.
Depth: full A1 (spec/contracts) → A2 (plan) → A3 (human) → A4 (conformance/fitness) → A5 (drift); minimal ADR, explicit new invariant, versioned additive contracts, NFR delta, acceptance + rollback, human decisions. Design depth > base because new external protocol + new financial flow + legal.

Wait, is 12/15 too high vs base 11/15? It's a change on top; some risk already mitigated by existing core (idempotency, outbox). Maybe 11/15 is more honest: D1=3, D2=3, D3=3, D4=1 (mostly additive, core invariants preserved), D5=1 → 11/15. Hmm. The change adds a new financial-initiation path (debiting without payer action) — that's a genuinely new financial risk class. I'll go with D4=2 because it adds a new aggregate and new protocol surface to the spine and contracts, and 12/15 total, and note "Critical". Either is defensible; I'll be explicit and transparent. Let me use 12/15.

Hmm, actually to avoid fabricating a precise score that could look arbitrary, I'll present it as an assessment with explicit dimension scores and mark the rubric as reconstructed/assumed. I'll state Route = Critical.

Let me also double-check: does the repo use "этап A3" for human decisions? Yes. Good.

Now, let me also think about whether to update `docs/rfp/vendor-rfp.md`. The vendor RFP would need a delta for subscription support. Since the RFP is part of the accepted solution and a human decision point, I'll add a short delta section to the RFP or note in the package. Let me read vendor-rfp.md quickly to decide.

Let me read it.

  `run_shell_command(command="cd /home/architect/project && which uv python3; echo \"--- gitignore ---\"; ls -a | head -30; cat .gitignore 2>/dev/null; echo \"--- _bmad-, description="Check tooling and gitignore state")`

The RFP is a substantial accepted artifact. For the change, I should add a delta to the RFP (subscription support criteria, POC scenarios) — or at least note it in the package. Given the vendor capability is a key human decision, adding a "RFP delta" section is valuable and idiomatic. But modifying the RFP heavily might be out of scope. I'll add a concise section 12 "Дельта подписок СБП (предложение)" or note in the package. Hmm. I think adding a short delta section to the RFP is right and useful — it's the natural place for "vendor must support subscriptions". But to keep the change package contained, maybe better to keep the RFP delta in the package doc, and only mark a TODO. Hmm.

Let me decide the final file set to keep it manageable but complete:

NEW (3):
1. `docs/adr/ADR-008-sbp-subscriptions-recurring-c2b.md` — decision (item 3)
2. `docs/solutioning-subscriptions.md` — change package: items 1,2,4(summary),5(summary),6,7 + index
3. `docs/spec/subscription-state-machine.md` — consent/ mandate state machine + debit entry path

MODIFY (8):
4. `ARCHITECTURE-SPINE.md` — AD-009 Proposed + scope/Deferred/contracts updates
5. `docs/nfr.md` — section 7
6. `docs/contracts/tsp-api.md` — v0.2 sections
7. `openapi/tsp-api.yaml` — v0.2.0 additive
8. `docs/contracts/opkc-adapter.md` — v0.2 sections
9. `docs/spec/state-machine.md` — subscription entry path + link
10. `docs/rfp/vendor-rfp.md` — delta section
11. `README.md` — structure/status

Optional: `docs/solutioning.md` — one-line pointer. I'll add a short pointer in §1 roadmap and §9 gaps? Minimal. Let me include a small edit to solutioning.md to prevent silent divergence: change the roadmap line "автоплатежи" to note the change package. Actually the roadmap says "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." I'll append: "(для автоплатежей/подписок готовится изменение — см. `docs/solutioning-subscriptions.md`)". Good, prevents divergence.

That's 12 files. Let me now write them.

I need to be careful and consistent. Let me start with the ADR-008 (the decision), then the spec/state machine, then contracts, then NFR, then spine, then package doc, then README/solutioning.

Let me think about naming conventions for slugs: existing ADR filenames are transliterated long names, e.g. `ADR-002-model-konsistentnosti-platezha-konechnyy-avtomat-s-idempotentnostyu-na-urovne-shlyuza.md`. So transliteration convention. So ADR-008 filename should be transliterated: `ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`. Let me do that to match convention.

Similarly spec file: existing `docs/spec/state-machine.md` is English. So `docs/spec/subscription-state-machine.md` — English, consistent with the spec dir convention. Good.

Package doc: `docs/solutioning-subscriptions.md` (English-ish, matches `docs/solutioning.md`). Good.

Now content. Let me write ADR-008.

I need to be precise about the decision and keep [ТРЕБУЕТ ПРОВЕРКИ] for protocol specifics.

Let me draft ADR-008.

---

# ADR-008. Подписки СБП: рекуррентные C2B-списания по согласию плательщика

- Date: 2026-09-29
- Status: Proposed (выносится на A3 — решение человека-архитектора/бизнеса)
- Owner: solution-architect (платёжный контур) + бизнес + ИБ/юрист
- Related: ADR-001, ADR-002, ADR-003, ADR-005, ADR-007, AD-001..AD-008

## Context

ТСП (онлайн-кинотеатры, ЖКХ, связь) просят подписки СБП — регулярные C2B-списания по согласию (мандату) плательщика без повторного сканирования QR и действий клиента. Сегодня каждый платёж требует QR/ссылки и действия клиента; автоплатежи вынесены за scope (`docs/solutioning.md` §1, roadmap).

Новый функционал вводит: (1) сущность «согласие плательщика» (мандат) с жизненным циклом (выдача, активация, отзыв, истечение); (2) инициацию списания *ТСП*, а не плательщиком; (3) новый участок протокола участника НСПК (согласия/рекуррентные списания) — точные поля/тайминги [ТРЕБУЕТ ПРОВЕРКИ] до получения документации НСПК; (4) регуляторный слой согласия (161-ФЗ, 152-ФЗ, правила НСПК).

Силы: финансовый риск несанкционированного/двойного списания (деньги списываются без участия клиента в момент операции); at-least-once внешнего канала; требование аудируемости согласия и его отзыва; AD-005 (зачисление только из подтверждённого статуса) и AD-002/AD-003 должны сохраниться; транспорт — вендорский (AD-008/ADR-007), значит поддержка подписок — требование к вендору и внешний вход (документация НСПК).

## Decision

1. **Согласие плательщика — отдельный агрегат шлюза со своей статусной машиной** (`docs/spec/subscription-state-machine.md`), единый источник истины — БД шлюза (расширение AD-002). Состояния: `CREATED → PENDING_PAYER → ACTIVE → REVOKED | EXPIRED`, ответвление `PENDING_PAYER → REJECTED`; терминальные `REJECTED`, `REVOKED`, `EXPIRED`. Каждый переход — атомарная транзакция «статус + outbox + аудит» (AD-002).
2. **Списание по согласию — это платёж** с новым признаком `origin = subscription` и ссылкой `consentId`. Платёж сохраняет существующую статусную машину и инварианты: внутреннее техническое состояние `DEBIT_ISSUED` (наружу не выставляется, отображается как `CREATED`) между `CREATED` и `PAID`; **зачисление — только из `PAID`** (AD-005 сохраняется без ослабления). Возвраты — существующая сага (ADR-005), без изменений.
3. **Инициация списания разрешена только при `ACTIVE` согласии и в пределах лимитов** (сумма/период/срок), проверяемых шлюзом до вызова ОПКЦ. Неактивное/отозванное/просроченное согласие или превышение лимита → отказ без обращения к НСПК (новые коды ошибок).
4. **Согласие хранится в шлюзе как процессный реестр-зеркало; источник истины согласия — НСПК/банк плательщика.** Шлюз обязан сверять согласия с НСПК (ежедневно) и останавливать списания при расхождении; отзыв, полученный от НСПК, немедленно блокирует новые списания.
5. **Транспорт подписок — через единственный адаптер ОПКЦ** (AD-004/AD-008): внутренний контракт адаптера расширяется операциями `createConsent`/`getConsentStatus`/`revokeConsent`/`initiateDebit` и событиями `consent.*`; протокол НСПК остаётся инкапсулирован. Реализация транспорта — по ADR-007 (вендор, сертифицированный), после получения документации НСПК.
6. **Идемпотентность**: `POST /v1/subscriptions` и `POST /v1/subscriptions/{id}/debits` — по `Idempotency-Key`; события НСПК — по `eventId`; повторная доставка не создаёт второе списание/второе зачисление (AD-003). Идемпотентность списания на уровне адаптера — по `reference` (= `paymentId`).
7. **Гонка «отзыв ↔ списание»**: после фиксации отзыва новые списания запрещены; списание, уже подтверждённое НСПК (`PAID`) к моменту фиксации отзыва, доводится до зачисления и отражается в отчётности (деньги плательщика уже списаны — откат только возвратом). Это осознанное правило, а не дефект.
8. **Совместимость контракта ТСП — аддитивная**: новые пути/схемы/опциональные поля/типы вебхуков; существующий enum `status` и поведение QR-потока не меняются (см. §4 пакета `docs/solutioning-subscriptions.md`).

## Alternatives Considered

| Вариант | Плюсы | Минусы |
|---|---|---|
| **A. Агрегат «согласие» + списание-как-платёж в ядре, расширение контракта вендорского адаптера (выбран)** | Переиспользует инварианты ядра (AD-002/003/005), один источник истины, аудит и сверка; минимальная дельта контракта; согласуется с AD-008 | Новый агрегат и участок протокола НСПК; зависимость от готовности вендора; юридическая модель согласия требует внешнего решения |
| B. Отдельный микросервис «рекуррентные платежи» со своей БД и адаптером | Изоляция новой логики | Нарушает AD-001 (единая точка выхода к ОПКЦ/АБС), дробит источник истины, второй контур сверки, дублирует статусную модель — отклонено |
| C. Хранить согласие только в НСПК, шлюз без локального реестра (passthrough) | Нет дублирования данных | Нельзя локально гарантировать лимиты, RPO=0 и идемпотентность; нет статуса для ТСП без вызова НСПК; нарушает дух AD-002 — отклонено |
| D. Реализовать транспорт подписок собственными силами | Нет зависимости от вендора | Противоречит принятому AD-008 (транспорт — сертифицированный вендорский); редкие компетенции СКЗИ/НСПК — отклонено |
| E. Отложить до получения документации и требований НСПК | Ноль регуляторного риска сейчас | Не отвечает запросу бизнеса; допустимо как условный сценарий (см. Reversibility/риски) |

## Consequences

### Positive
- Переиспользование проверенных инвариантов: зачисление только из PAID, атомарность, идемпотентность, outbox, сверка, сага возвратов.
- Новый источник дохода/удержания ТСП без пересборки ядра; контракт ТСП расширяется аддитивно.
- Аудируемость полного жизненного цикла согласия — соответствие требованиям НСПК/ЦБ.

### Negative
- Новый класс финансового риска: списание без действия плательщика в момент операции; требуется антифрод/лимиты и юридическая модель согласия.
- Зависимость от вендора транспорта (поддержка подписок) и от документации НСПК — внешние входы, влияют на сроки.
- Ещё один объект сверки (согласия) и расхождения — эксплуатационная нагрузка.
- Периодические пики списаний (биллинговые окна) — burst-профиль, отличный от QR-потока.

### Risks (кратко)
- Вендор не поддерживает подписки → A3-развилка (смена вендора/модуля/отсрочка).
- Протокол НСПК для подписок отличается от гипотезы → пересмотр сценариев (документация внешняя).
- Отзыв согласия не успевает за списанием → правила гонки (п.7) и SLA распространения отзыва.

## Reversibility

**reversible до боевой эксплуатации** (фиче-флаг, ничего не включено). **Costly/reversible после**: новые списания и выдача согласий отключаются флагом, но выданные согласия плательщиков нельзя «откатить» — их нужно корректно отозвать; поэтому откат обязан сохранять работоспособность отзыва/возврата/статусов и сверки согласий. Миграция данных обратно не требуется (согласия остаются в БД шлюза как источник аудита). См. план отката в `docs/solutioning-subscriptions.md` §6.

## References
- `docs/solutioning-subscriptions.md` — архитектурный пакет изменения (значимость, влияние, контракты, NFR, приёмка, откат, решения человека)
- `docs/spec/subscription-state-machine.md` — статусная машина согласия
- `docs/contracts/tsp-api.md` §8, `openapi/tsp-api.yaml` — дельта контракта ТСП
- `docs/contracts/opkc-adapter.md` — дельта контракта адаптера
- AD-001..AD-008 (spine); ADR-001, ADR-002, ADR-003, ADR-005, ADR-007
- НСПК: протокол подписок/рекуррентных списаний — [ТРЕБУЕТ ПРОВЕРКИ] (документация Портала поддержки НСПК по договору)

---

Good. Now the spine update: add AD-009.

```
## AD-009. Согласие плательщика как отдельный агрегат; списание — из подтверждённого статуса

- Status: Proposed (ADR-008; выносится на A3)
- **Binds**: реестр согласий (мандат), статусная машина платежа (`origin=subscription`), API ТСП (подписки/списания), контракт адаптера ОПКЦ (`createConsent`/`initiateDebit`), сверка, аудит-лог, AML/антифрод.
- **Prevents**: списание без действующего согласия или с превышением лимита; зачисление не подтверждённого НСПК списания; потеря/игнорирование отзыва согласия; расхождение «шлюз считает согласие активным, НСПК — отозванным».
- **Rule**: (1) Согласие плательщика — отдельный агрегат с собственной статусной машиной; его переходы — атомарные транзакции «статус + outbox + аудит» (расширение AD-002). (2) Инициация списания (`origin=subscription`) допустима только при согласии в состоянии `ACTIVE` и в пределах лимитов — проверка в шлюзе до вызова ОПКЦ; зачисление — только из `PAID` (AD-005 не ослабляется). (3) После фиксации отзыва новые списания запрещены; списание, подтверждённое НСПК до отзыва, доводится до зачисления и отражается в отчётности. (4) Согласие — процессный реестр-зеркало; источник истины — НСПК/банк плательщика, ежедневная сверка, расхождение останавливает списания. Fitness: тесты «списание без ACTIVE-согласия невозможно», «после отзыва новое списание невозможно», «повтор Idempotency-Key/eventId не создаёт второе списание/зачисление», «зачисление только из PAID для origin=subscription».
```

Then update Deferred: subscriptions were not explicitly listed in Deferred (they were "автоплатежи" in solutioning roadmap). The spine's Deferred lists "C2C-переводы и выплаты B2C/B2B" as roadmap. I'll add a Deferred note? Actually since we're adding subscriptions to scope (Proposed), I should not put it in Deferred. Instead maybe update the Deferred item about C2C to keep it. And add to "Контракты и версии": TSP API version 0.2 draft for subscriptions. Also update the top statuses note? No.

Also should I update parent spine compatibility: the change doesn't conflict with parent (initiative). Note "конфликт не выявлен".

Let me also add a line in "Контракты и версии": "- Внутренний контракт шлюза (API ТСП): версия 0.2 draft (+ подписки СБП, аддитивно; см. `docs/contracts/tsp-api.md` §8, `openapi/tsp-api.yaml`)." Keep original 0.1 line? Better amend: "версия 0.1 draft → 0.2 draft (дельта подписок — AD-009/ADR-008, аддитивно)".

Now, the spec `docs/spec/subscription-state-machine.md`:

Content: consent states, transitions table, invariants, debit entry path in payment machine, idempotency keys, reconciliation, mapping to ТСП API.

Let me write it thoroughly.

Then state-machine.md: add a section referencing subscription origin.

Then tsp-api.md: add §3.6-3.9 (subscriptions endpoints) and §5 webhook events, §4 error codes, §6 versioning note, version bump 0.2. And add `origin`/`consentId` to Payment. Careful to make it additive.

Then openapi/tsp-api.yaml: rewrite with version 0.2.0, additive paths and schemas. Keep existing paths/schemas unchanged in shape (only add optional fields). Let me write it carefully.

Then opkc-adapter.md: add §3 ops and §4 events (new rows) + §5 reference semantics + §7 NFR delta? and §9 open questions. Additive.

Then nfr.md: add section 7 + maybe update §2 table? Additive section 7.

Then vendor-rfp.md: add §12 delta (subscription support criteria + POC scenarios).

Then solutioning-subscriptions.md: the package doc with items 1,2,4,5,6,7 and index.

Then README.md and solutioning.md pointer.

Let me be efficient but thorough. Let me start writing files.

One more consideration: language. docs are in Russian. I'll write in Russian. Code/schemas in English. Protocol details marked [ТРЕБУЕТ ПРОВЕРКИ]. Good.

Also, I should use the memlog script? The skill says writes go through memlog.py. But the repo's accepted artifacts weren't produced via memlog (no memlog exists). Introducing a memlog for this change is arguably part of "the methodology". Hmm. The skill's run workspace is `_bmad-output/planning-artifacts/architecture/architecture-ws-{date}/`. That would create a new spine file there, not update the root ARCHITECTURE-SPINE.md. But the repo's convention is the root ARCHITECTURE-SPINE.md, and the user wants the change package in the repo. 

The skill's Update intent says resume from memlog; there is none. I think forcing the skill's file layout would conflict with repo convention, which the skill itself says to ratify (brownfield: ratify conventions). And the user's instruction "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" points to the repo's ADR mechanism, not the skill's workspace. So I'll use the skill as *methodology* (AD-n with Binds/Prevents/Rule, alternatives/consequences/reversibility, reviewer gate, deferred) but land artifacts in repo paths. I can optionally create a memlog to honor the method and record decisions — it's cheap and shows methodology. But it would add files in `_bmad-output/...` which may be noise. Hmm.

Given "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению", I should at least run the lint_spine.py and the reviewer gate (parallel subagents). The reviewer gate is explicitly part of the method. I'll run lint_spine.py against a workspace containing the spine (the repo root is the workspace containing ARCHITECTURE-SPINE.md). Then run the two configured finalize_reviewers as parallel subagents against ARCHITECTURE-SPINE.md, plus a rubric walker. That satisfies the methodology and gives real quality value.

Also I could create a memlog for the change run to honor the method. Let me create it in the repo under a sensible path? The skill default workspace is `_bmad-output/planning-artifacts/architecture/...`. Creating `_bmad-output` (gitignored? Let me check .gitignore) ... The `_bmad/config.toml` output_folder = "_bmad-output". _bmad/custom/.gitignore and _bmad/render/.gitignore exist. Is `_bmad-output` gitignored at root? There's no root .gitignore listed in files. Let me check. Actually find showed no .gitignore at root. Hmm.

I think creating a memlog is optional; the primary deliverables are the docs. But the skill says the memlog is the authority and decisions must be logged. To honor the methodology without polluting the repo, I could write the memlog into `_bmad-output/planning-artifacts/architecture/...`. But that might be considered noise by the user. 

Decision: I'll create the memlog for the change run at `_bmad-output/planning-artifacts/architecture/architecture-ws-subscriptions/` using memlog.py, since the methodology calls it "the run's working memory". Actually — hmm, `architecture-{project_name}-{date}` with project_name="ws". That's ugly. And it would produce an ARCHITECTURE-SPINE.md there if I follow the skill literally. I don't want a duplicate spine.

Alternative: keep it simple and repo-native. The user cares about the package. I'll skip the memlog and skill-workspace, but I WILL run the deterministic lint and the reviewer gate (subagents) and apply fixes — that's the substantive part of the methodology. I'll mention that I used the bmad-architecture method (AD-n invariants, alternatives, reviewer gate). If needed I can note the memlog omission. Hmm, but "используй их по назначению" — I'd better use the memlog too. 

Let me reconsider: creating `_bmad-output/planning-artifacts/architecture/...` is exactly where this skill puts its working memory; it's the configured output folder. It's not noise — it's the run's audit trail, and the reviewer gate writes to `reviews/`. I'll create the memlog there for this change run. That honors the method and leaves an auditable trail. I'll bind doc_workspace to a dedicated run folder. Let me use memlog.py init with scope/purpose/altitude. And append decisions. Then the reviewer gate reviews the root ARCHITECTURE-SPINE.md (I'll pass the repo root as workspace for lint, and point subagents at the root spine + the change package).

Wait, lint_spine.py requires APPROACH: it reads ARCHITECTURE-SPINE.md from --workspace. If I pass repo root, it lints the root spine. Good. Let me do that.

Hmm, but the skill's reviewer gate writes reviews to `{doc_workspace}/reviews/`. I'll put the run folder at `_bmad-output/planning-artifacts/architecture/architecture-change-subscriptions/` and write reviews there. Fine.

Let me check whether `uv` is available and memlog.py runs. Let me test. Also check root .gitignore.

Actually, let me not over-invest in tooling ceremony. Let me check uv availability quickly, and check .gitignore. If uv works, I'll init the memlog.

Let me proceed: first check uv + .gitignore, then start writing.

Actually — time/effort. Let me be decisive: I'll write the artifacts (the real value), run lint_spine.py (via uv or python), run the reviewer gate with 2-3 parallel subagents, apply fixes, then report. I'll create the memlog too if uv is available (cheap).

Let me check uv and gitignore.
I have the full picture. Let me verify the tooling (uv, gitignore) before starting to write.

  `run_shell_command(command="python3 --version 2>&1; python --version 2>&1; uv --version 2>&1; echo \"exit: $?\"", description="Check python and uv availability")`

No uv, no python3? `which uv python3` returned nothing. So lint_spine.py can't run via uv. Let me check python availability differently (maybe python3 exists but which output empty? It printed nothing before "--- gitignore ---"). Let me test `python3 --version`.

If no python, I can't run lint_spine.py. I can still do the reviewer gate with subagents. Let me check.

  `write_file(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", content="# ADR-008. Подписки СБП: рекуррентные C2B-списания по согласию плательщика\n\n- Date: 2026-09-29\n- Status: Proposed (выносится на A3 — реш)`

No Python, no uv. So the deterministic lint and memlog.py can't run. I'll note that. I can still do the reviewer gate via subagents (they can read files and reason). And I'll manually enforce the lint rules (no TODO/TBD, ascending AD ids, Binds/Prevents/Rule present, no template tokens).

Now let me write the artifacts. I'll start with the ADR-008, then the spec, then contracts, NFR, spine, package, README/solutioning.

Let me write ADR-008.
No Python/uv in this environment, so the deterministic linter and `memlog.py` can't run — I'll apply the method's checks manually and use the reviewer gate via subagents instead. Now writing the change package, starting with the decision record.

  `write_file(content="# Статусная машина согласия плательщика (подписки СБП) — спецификация переходов\n\n- Status: Draft (предложение к гейту A1 в рамках изменен, file_path="/home/architect/project/docs/spec/subscription-state-machine.md")`

Now the subscription state machine spec.

  `edit(file_path="/home/architect/project/docs/spec/subscription-state-machine.md", old_string="- **Отзыв монопропагандируется в одну сторону**: однажды зафиксированный отзыв не отменяется. Гонка со списанием — правило ADR-008 п.7 (см., new_string="- **Отзыв необратим**: однажды зафиксированный отзыв не отменяется, повторный отзыв идемпотентен. Гонка со списанием — правило ADR-008 п.7 )`

Oops, I wrote "Отзыв монопропагандируется в одну сторону" — that's a weird word, typo/nonsense. Let me fix that to "Отзыв необратим (движется в одну сторону)". I'll fix with edit.

Also, in T13 guard "Idempotency-Key уникален" - ok.

Let me fix the typo.

  `edit(file_path="/home/architect/project/docs/spec/state-machine.md", old_string="- Status: Draft (для ревью на гейте A1)\n- Owner: solution-architect (платёжный контур)\n- Связано: ADR-002, ADR-005, AD-002, AD-003, AD-00, new_string="- Status: Draft (для ревью на гейте A1)\n- Owner: solution-architect (платёжный контур)\n- Связано: ADR-002, ADR-005, AD-002, AD-003, AD-00)`

Now update `docs/spec/state-machine.md` to add subscription note (cross-reference) — minimal, additive. Add a section 7 (or append to §6). Let me add a new section after §6.

Also update the header "Связано" to include ADR-008.

Let me edit.
Now the payment state machine cross-reference:

  `edit(file_path="/home/architect/project/docs/spec/state-machine.md", old_string="Маппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `EXPIRED`, `REFUNDED` — без техн, new_string="Маппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `EXPIRED`, `REFUNDED` — без техн)`

Now add a section at the end of state-machine.md about subscriptions. Let me read the end to append correctly. The file ends with §6 "Согласованность с API ТСП". I'll append §7.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="# Контракт API ТСП (мерчант-API) — v0.2 draft\n\n- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.2 (нестабильная; до A1 фикс, old_string="# Контракт API ТСП (мерчант-API) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фикс)`

Now the TSP API contract. I need to add section 8 (subscriptions) and modify §3.2/3.3 for `origin`/`consentId`, §4 error codes, §5 webhooks, §6 versioning, and header version. Let me read the current file again around relevant parts to edit precisely. I have it in context. Let me make edits:

1. Header: version 0.1 → 0.2.
```
- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
```
Change to version 0.2 with note about additive subscription delta.

2. §3.3 Payment response add `origin` and `consentId`.
3. §3.2 note about `origin`.
4. §4 errors add codes.
5. §5 webhooks add subscription.* events and note.
6. §6 versioning add note.
7. Add §8 subscriptions (or insert as §3.6–3.9). Better as a new §8 to keep the numbered method sections; but the doc uses §3.1..3.5 methods. I'll add §3.6–3.9 under methods, and webhooks in §5. Hmm, §8 might be cleaner as "Подписки (v0.2)". Let me add §3.6–3.9 to methods for consistency (contract doc groups methods under §3), then error/webhook/versioning notes, then §8 "Открытые вопросы" shifts to §9. Actually current §7 is "Открытые вопросы (для A1)". I'll add §8 subscriptions? Let me instead insert methods as 3.6–3.9 and add a §5.1 subsection for subscription webhooks, then update §7 open questions, and add a new §8 "Совместимость v0.1 → v0.2 (дельта подписок)". Hmm.

Let me structure edits:
- Header version → 0.2, add "Изменение ADR-008: добавлены подписки (аддитивно, обратно совместимо)".
- §2 idempotency: add that it applies to subscription endpoints.
- §3.2: add note `origin` default qr.
- §3.3: add `origin`, `consentId` fields.
- Add §3.6–3.9 methods.
- §4: add error codes.
- §5: add subscription events.
- §6: add note about 0.2 additive.
- §7: update open questions.
- Add §8 "Дельта v0.1 → v0.2: совместимость".

That's a lot of edits; let me do them one by one. Actually maybe simpler to add a dedicated big §8 "Подписки СБП (v0.2, ADR-008)" containing endpoints, schemas deltas, webhooks, errors, compatibility — and make small edits elsewhere (version, §3.3 fields, error list, webhook list, open questions). That minimizes risk of breaking existing text while keeping discoverability. Hmm, but methods should be in §3 per convention. I'll add methods in §3 as 3.6–3.9 and put compatibility in §8. Let me do it.

Let me edit header first.
Now the TSP API contract — additive v0.2 with subscriptions:

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="- Повторный `POST` с тем же ключом, но **другим телом** → `409 IDEMPOTENCY_CONFLICT`.\n- GET-запросы идемпотентны по своей природе, ключ не, old_string="- Повторный `POST` с тем же ключом, но **другим телом** → `409 IDEMPOTENCY_CONFLICT`.\n- GET-запросы идемпотентны по своей природе, ключ не)`

Now edit §2 idempotency to include subscription endpoints. Current §2 text:

```
## 2. Идемпотентность

- Заголовок `Idempotency-Key` **обязателен** для всех `POST`.
...
```
Works for all POSTs already. I'll add a note that for debits the key identifies the debit. Minor — maybe skip. Let me add one line.

Then §3.2 request note about origin, §3.3 response fields.

Let me edit §3.3 response to add origin/consentId.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="```json\n{\n  \"paymentId\": \"pay_8d1e4f5a\",\n  \"origin\": \"qr\",                  // v0.2: qr | subscription (опц., по умолчанию qr — , old_string="```json\n{\n  \"paymentId\": \"pay_8d1e4f5a\",\n  \"status\": \"COMPLETED\",           // CREATED | QR_ISSUED | PAID | CREDITED | COMPLETED)`

Now §3.3 Payment response: add `origin` and `consentId`. Current:

```
Ответ `200`:
```json
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
```

Add `origin` and `consentId`.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n, old_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n)`

Now add methods §3.6–3.9 after §3.5. Let me find §3.5 text:

```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`

## 4. Ошибки (RFC 9457, Problem Details)
```

I'll insert subscription methods before "## 4. Ошибки". Also add a note in §3.4 that refunds apply to subscription debits too.

Let me insert.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="Правила: возврат возможен только если платёж в состоянии `CREDITED`/`COMPLETED` (ADR-005, сага). Полный возврат переводит платёж в `REFUNDE, old_string="Правила: возврат возможен только если платёж в состоянии `CREDITED`/`COMPLETED` (ADR-005, сага). Полный возврат переводит платёж в `REFUNDE)`

Now §3.4 refunds note: add that refunds apply to subscription debits. Let me edit the "Правила:" line in §3.4. Current text:

```
Правила: возврат возможен только если платёж в состоянии `CREDITED`/`COMPLETED` (ADR-005, сага). Полный возврат переводит платёж в `REFUNDED`; частичные — платёж остаётся `COMPLETED`, возврат виден в `refunds[]`. Статус возврата: `PENDING → COMPLETED | FAILED`.
```

Append: "Правила одинаковы для платежей `origin=qr` и `origin=subscription` — возврат по списанию идёт той же сагой."

Then §4 errors add codes.

Then §5 webhooks add subscription events.

Then §6 versioning.

Then §7 open questions update.

Then add §8 compatibility.

Let me do these edits.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`
  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`

Now §5 webhooks: add subscription events. Current:

```
События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`

Тело (`payment.completed`):
```json
{...}
```

Доставка: ...
```

Add subscription events after the existing list, and a note that debit outcomes use payment.* events. Also a note about unknown event types for old consumers.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="Тело (`subscription.activated`):\n```json\n{\n  \"eventId\": \"evt_…\",\n  \"type\": \"subscription.activated\",\n  \"subscriptionId\": \"s, old_string="Доставка: ответ ТСП `2xx` = успех; иначе ретрай (экспоненциальная задержка + джиттер), после исчерпания — DLQ. ТСП обязан отвечать идемпоте)`

Now add the subscription event body sample and a compatibility note after the delivery paragraph. Let me find the delivery paragraph:

```
Доставка: ответ ТСП `2xx` = успех; иначе ретрай (экспоненциальная задержка + джиттер), после исчерпания — DLQ. ТСП обязан отвечать идемпотентно по `eventId`.

## 6. Версионирование и совместимость
```

I'll insert before "## 6" a body example for subscription.activated + a note that unknown types must be ignored (compat).

Then §6 and §8.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.\n- Добавление опциональных полей — , old_string="- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.\n- Добавление опциональных полей — )`

Now §6 add a note about v0.1→v0.2 additive. And §7 open questions update (currently "Открытые вопросы (для A1)"). Let me edit §6 and §7.

Current §6:
```
- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.
- Добавление опциональных полей — обратно совместимо, не требует новой версии.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.

## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» ...
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
```

I'll add to §6 the 0.2 note; update §7 with subscription open questions; add §8 compatibility matrix.

Let me do §6 first.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\n  description: >\n    Дельта 0.2.0 аддитивна относительно 0.1.0 (подп, file_path="/home/architect/project/openapi/tsp-api.yaml")`

Now update the openapi/tsp-api.yaml to v0.2.0 with additive paths/schemas. Let me write the full file (I've read it; it's small). I'll preserve existing structure and add.

I need to include:
- info.version 0.2.0, description mentioning additive subscription delta.
- existing paths /v1/payments POST, /v1/payments/{paymentId} GET (unchanged; but Payment schema gains optional origin/consentId).
- new paths: /v1/subscriptions POST, /v1/subscriptions/{subscriptionId} GET, /v1/subscriptions/{subscriptionId}/revoke POST, /v1/subscriptions/{subscriptionId}/debits POST, /v1/subscriptions/{subscriptionId}/debits GET.
- new schemas: SubscriptionRequest, Subscription, SubscriptionRevokeRequest, DebitRequest, DebitList.
- Payment schema add origin enum, consentId nullable.
- PaymentRequest unchanged.
- Keep Idempotency-Key header params on new POSTs.

Let me write it. Note: keep the original minimal style (compact inline maps). I'll keep consistent formatting.

Also the CONFIRMS check: "adr-no-placeholders" and "spine-lints-clean" checks TODO/TBD/XXX — I must not put "TODO"/"TBD" anywhere. I use [ТРЕБУЕТ ПРОВЕРКИ] which is fine (not matching TODO|TBD|XXX). Good.

Let me write the yaml.
Now the OpenAPI spec — additive v0.2.0:

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.2 draft\n\n- Status: Draft (для ревью на гейте A1; основа для RFP вендора)\n- Версия, old_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1; основа для RFP вендора)\n- Owner:)`

Now the opkc-adapter.md — add subscription ops and events. Let me edit additively.

Edits:
1. Header: version 0.2, note delta.
2. §1: mention subscriptions.
3. §3 table: add rows createConsent, getConsentStatus, revokeConsent, initiateDebit, getConsentReconciliationReport (or extend getReconciliationReport).
4. §4 events table: add consent.activated, consent.rejected, consent.revoked, consent.expired; note debit.paid/rejected reuse payment.paid/rejected.
5. §5 idempotency: reference for debits = paymentId.
6. §7 NFR: maybe add adapter consent/debit NFR.
7. §8 vendor requirements: add subscriptions.
8. §9 open questions: add.

Let me make these edits.

Header current:
```
# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.1 draft

- Status: Draft (для ревью на гейте A1; основа для RFP вендора)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-003, ADR-004, AD-004, AD-008
```
Change to v0.2 with note.
Now the ОПКЦ adapter contract delta:

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t, old_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t)`

Now §3 sync ops table. Current:

```
| Метод | Направление смысла | Ключевые поля запроса | Ответ | Таймаут (p99.9) |
|---|---|---|---|---|
| `registerTsp` | ... | ... | ... | 5 c |
| `createPaymentLink` | ... | ... | ... | 3 c |
| `getPaymentStatus` | ... | `qrId` | ... | 3 c |
| `cancelPaymentLink` | ... | ... | ... | 3 c |
| `createRefund` | ... | ... | ... | 5 c |
| `getRefundStatus` | ... | ... | ... | 3 c |
| `getReconciliationReport` | ... | ... | ... | 10 c |

Статусные модели ОПКЦ ...
```

I'll add rows for createConsent, getConsentStatus, revokeConsent, initiateDebit. And add a paragraph after the table about statuses normalized.

Let me edit by replacing the last row + following paragraph.

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="| `consent.activated` | согласие плательщика активировано (подписка действует) | `reference` (= `subscriptionId` ядра), `consentId`, `activ, old_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |")`

Now §4 events table. Add consent events. Current table has rows ending with `transport.unavailable`. Add rows before/after. Let me edit the last row.

```
| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |

Гарантии: ...
```

I'll add consent rows after refund rows. Let me insert after `refund.rejected` row and before `transport.unavailable`. Actually simplest: replace `transport.unavailable` row with consent rows + that row. Let me do it.

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`/`subscriptionId`) в каждый мутирующий вызов.\n- **Адаптер обязан обеспечит, old_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.\n- **Адаптер обязан обеспечить идемпотентность)`

Now §5 add note about consent reference and revocation events. Current §5:

```
- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.
- **Адаптер обязан обеспечить идемпотентность**: ...
- Повторная доставка события с тем же `eventId` — игнорируется ядром (ADR-003).
```

Update first bullet to include subscriptionId; add note that `initiateDebit` idempotent by paymentId and `createConsent` by subscriptionId. Also note late/duplicate consent events.

Let me edit.

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="| Доступность адаптера | ≥ 99,95 % | SLO-отчёт |\n| Latency `createConsent` (подписки) | p95 < 1 c (без учёта НСПК) | Нагрузочный тест |\n|, old_string="| Доступность адаптера | ≥ 99,95 % | SLO-отчёт |\n| Метрики/наблюдаемость | Prometheus-метрики: latency, errors, circuit state; trace id | )`

Now §7 NFR table (adapter) and §8 requirements — add subscription NFR rows and vendor requirements. Current §7:

```
| Метрика | Цель | Метод проверки |
|---|---|---|
| Пропускная способность адаптера | ≥ 200 TPS sustained, пик 500 TPS ... |
| Latency `createPaymentLink` | p95 < 1 c ... |
| Потеря событий | 0 ... |
| Дубли при ретрае | 0 (идемпотентность по `reference`) | Тест на повторный вызов |
| Доступность адаптера | ≥ 99,95 % | SLO-отчёт |
| Метрики/наблюдаемость | Prometheus-метрики: latency, errors, circuit state; trace id | Аудит интеграции |
```

Add rows: latency createConsent p95 < 1c; latency initiateDebit p95 < 1c; дубли списаний/согласий 0. And amend "Дубли при ретрае" to mention debits. Let me add rows.

Then §8 requirements: add item for subscription protocol support + test scenarios. Item list currently 1-6. Add 7. And §9 open questions add.

Let me edit §7 table end.

  `read_file(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", offset=92)`
  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="5. SLA, поддержка, референсы в банках сопоставимого масштаба.\n6. Эксплуатация: метрики, алерты, документация runbook.\n7. **Поддержка подп, old_string="5. SLA, поддержка, референсы в банках сопоставимого масштаба.\n6. Эксплуатация: метрики, алерты, документация runbook.\n\n## 9. Открытые во)`
  `edit(file_path="/home/architect/project/docs/nfr.md", new_string="## 7. Подписки СБП (рекуррентные C2B-списания) — ADR-008\n\nНовые цели для функционала подписок; базовые профили §1–§6 сохраняются, подписк, old_string="## Зависимости (внешние входы для NFR)\n\n- Регламенты НСПК: таймауты, сроки уведомлений, требования к доступности [ТРЕБУЕТ ПРОВЕРКИ — из д)`

Now NFR — add section 7. Let me edit nfr.md. Current §6 ends with "## Зависимости (внешние входы для NFR)". I'll insert §7 before "## Зависимости". Actually the doc has sections 1-6 then "## Зависимости". I'll add §7 "Подписки СБП (рекуррентные C2B-списания) — ADR-008" before "## Зависимости", and add a dependency bullet.

Let me edit.
Now the NFR delta:

  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now the spine update: add AD-009 and update Deferred/Contracts section. Let me edit ARCHITECTURE-SPINE.md.

Add AD-009 after AD-008 block (before "---\n\n## Deferred"). Then update "Контракты и версии" version line.

Let me do the AD-009 insertion.
Now the spine — new Proposed invariant AD-009:

  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", new_string="## Изменения (Proposed, ожидают решения)\n\n- **Подписки СБП — рекуррентные C2B-списания по согласию плательщика** (ADR-008, AD-009). Вывед, old_string="## Deferred (с причиной и условием возврата)\n\n- **Мультивалютность и иностранные платёжные системы**: не в scope C2B-приёма СБП; вернуть )`

Now update the Deferred section to note subscriptions are no longer deferred (now covered by AD-009 Proposed) and update "Контракты и версии". Also note parent-spine conflict: none. Let me read the tail of spine.

Deferred currently:
```
- **Мультивалютность...**
- **C2C-переводы и выплаты B2C/B2B**: roadmap после стабилизации C2B; ...
- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; ...

## Контракты и версии

- Контракт НСПК: ...
- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — `docs/contracts/tsp-api.md` (создаётся на этапе Spec).
- Пиннинг версий зависимостей — в CONSTRAINTS.yaml (.arch-handoff) при передаче кодовому харнессу.
```

I'll:
- Add to Deferred: a note that disputes remain deferred but subscriptions increase dispute pressure (revisit condition). Actually disputes already listed; I'll amend its "вернуть" condition to mention subscriptions.
- Add a line: "Подписки СБП (рекуррентные списания): выведены из roadmap в scope изменением ADR-008/AD-009 (Proposed); до ратификации A3 функционал не реализуется." Hmm — better as a note under Deferred or a separate "Изменения (Proposed)" block. The spine's structure doesn't have an "in progress" section. I'll add a bullet at the top of Deferred? No, it's not deferred. Maybe add a short section "## Изменения (Proposed, ожидают A3)" before Deferred, listing ADR-008/AD-009 and scope change. That's honest and discoverable. Actually adding a whole section might diverge from the spine's convention; but the spine does have "Контракты и версии" and "Deferred" sections. A small "Изменения" section is fine and valuable. Let me add it right before "## Deferred".

Wait, I already inserted "---" after AD-009 and then "## Deferred". Let me insert a section between.

Let me edit the Deferred header area.

  `read_file(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", offset=86)`

Now update the "Контракты и версии" section: version 0.1 → 0.2 for TSP API, add adapter v0.2. Let me read the tail.

  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", new_string="- Контракт НСПК: `docs/contracts/nspk-contract.md` — создаётся после получения документации НСПК; до этого все ссылки на протокол помечены , old_string="- Контракт НСПК: `docs/contracts/nspk-contract.md` — создаётся после получения документации НСПК; до этого все ссылки на протокол помечены )`
  `edit(file_path="/home/architect/project/docs/rfp/vendor-rfp.md", new_string="## 11. Чек-лист готовности к запуску RFP\n\n- [ ] Контракт opkc-adapter.md зафиксирован как v1.0-draft (после ревью A1).\n- [ ] NDA с вендо, old_string="## 11. Чек-лист готовности к запуску RFP\n\n- [ ] Контракт opkc-adapter.md зафиксирован как v1.0-draft (после ревью A1).\n- [ ] NDA с вендо)`

Now the vendor RFP delta (§12) — add a section. Let me append before or after §11. Current file ends with §11 checklist. I'll add §12 after §11.

Let me edit the end of vendor-rfp.md.
Now the RFP delta:

  `write_file(content="# Архитектурный пакет изменения: подписки СБП (рекуррентные C2B-списания)\n\n- Status: **Proposed** — выносится на архитектурное решение (A, file_path="/home/architect/project/docs/solutioning-subscriptions.md")`

Now the main package document: `docs/solutioning-subscriptions.md`. This is the deliverable entry point with items 1-7. Let me write it thoroughly.

Contents:
- Header (Status Proposed/A3, Owner, Related, Назначение: архитектурный пакет изменения).
- §1 Значимость и маршрут (item 1): assessment, rubric (assumption-flagged), score 12/15, route Critical, depth of design, why.
- §2 Влияние на принятую архитектуру (item 2): table of invariants AD-001..AD-009, touched/not, what changes/doesn't; components; data; contracts; scope.
- §3 Архитектурное решение (item 3): summary + link to ADR-008; alternatives table (brief, refer to ADR); reversibility (refer).
- §4 Изменения контрактов (item 4): TSP API delta + adapter delta + compatibility; links.
- §5 NFR (item 5): summary + link to nfr §7.
- §6 Критерии приёмки и план отката (item 6): acceptance tests (incl. negative), rollback plan with triggers/owner.
- §7 Что остаётся на решение человека-архитектора (item 7): list with why.
- §8 Следующие шаги / handoff delta.
- Gaps/open questions.

Let me write. Be precise, measurable, testable. Use [ТРЕБУЕТ ПРОВЕРКИ] for protocol specifics. Avoid TODO/TBD/XXX.

Let me write the file.
Now the package entry point — significance, impact, acceptance/rollback, and human decisions:

  `edit(file_path="/home/architect/project/README.md", new_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..008`, `ARCHITEC, old_string="- Маршрут: **Critical** (значимость 11/15).\n- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITEC)`

Now update README.md to include the new docs and change status, and solutioning.md pointer.

README current:
```
# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): ...

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК ...

## Структура
...
```

Update to add change package. Let me edit the bullets and structure listing.

Let me read README again (I have it). I'll edit:
- Status bullet: add "Подготовлен architectural change package for subscriptions (ADR-008/AD-009), awaiting A3."
- Structure: add docs/changes lines. Actually add `docs/solutioning-subscriptions.md`, `docs/adr/ADR-008...`, `docs/spec/subscription-state-machine.md`.

Let me edit.
Now update README and the solutioning roadmap pointer:

  `edit(file_path="/home/architect/project/docs/solutioning.md", new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop, old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop)`

Now update solutioning.md §1 roadmap line to point to the change package. Current:

"Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

Change to append a pointer. Minimal.

  `agent(description="Adversarial seam review", subagent_type="general-purpose", run_in_background=false)`
  `agent(description="Verification and consistency review", subagent_type="general-purpose", run_in_background=false)`
  `agent(description="Security and data-integrity lens", subagent_type="general-purpose", run_in_background=false)`

Now I've written all files. Let me now run the reviewer gate per the bmad-architecture method: dispatch parallel subagents against ARCHITECTURE-SPINE.md and the change package. The configured finalize_reviewers (2) plus a rubric walker and a domain lens (security/compliance/data-integrity) for critical stakes.

The reviewers should read the spine and the change package and return compact summaries. They run in background by default; I need results before finalizing, so I should run them in foreground? Top-level regular subagents run in background by default and report via notification. I need the results to apply fixes. The instructions say: "Set run_in_background: false when you need a regular subagent's result inline before continuing." I do need them before finishing (well, before reporting). But I could also launch them in background and continue with... nothing else pending. Better: run them in foreground (run_in_background: false) so I get results inline. But multiple foreground subagents in one message — they run concurrently? The tool says "Run agents concurrently only when their tasks are independent... launch them in a single message with multiple Agent tool uses." Foreground multiple in one message should run concurrently and return inline. Let me do 3 review agents in one message with run_in_background: false.

Actually, the skill says the gate writes full review to a file and returns compact summary. I'll instruct each to write to a reviews folder and return a compact summary. But writing files in the repo adds artifacts. The skill's convention: `{doc_workspace}/reviews/review-{slug}.md`. Since I don't have a doc_workspace, I'll have them just return compact findings (no files) to avoid clutter — or write to `.qwen/tmp/`? Hmm. The method wants scratch out of the deliverable. I'll instruct them NOT to write files, just return a compact report. That's a reasonable adaptation given no doc_workspace and to avoid repo noise. Hmm, but the method says "Each writes its full review to a file ... and returns ONLY a compact summary". Without a workspace, returning compact summaries only is fine.

Let me define 3 reviewers:
1. Rubric walker + adversarial seam review (configured reviewer #2): find two units one level down that obey every AD yet build incompatibly. Focus on the new AD-009/subscription design and its interaction with existing ADs/contracts.
2. Verification/currentness reviewer (configured reviewer #1): verify named tech/claimed facts are reality-checked; flag anything asserted without confirmation; also check internal consistency of cross-references and that no accepted invariant is weakened.
3. Domain lens: security/compliance + data-integrity + edge cases (fits critical stakes): consent revocation races, PII, idempotency, reconciliation, and whether contracts are truly backward compatible.

Each should read the spine, ADR-008, solutioning-subscriptions.md, spec files, contracts, nfr, openapi, and report top findings with severity.

Let me launch them. I'll give precise file paths.

Actually, since they are subagents without parent context, I must give them enough pointers. Let me write good prompts.

Then I'll apply fixes for clear findings.

Let me launch 3 in one message, foreground.
Package drafted. Now I'll run the method's reviewer gate — independent reviewers against the spine and the change package.

  `write_file(content="# Статусная машина согласия плательщика (подписки СБП) — спецификация переходов\n\n- Status: Draft (предложение к гейту A1 в рамках изменен, file_path="/home/architect/project/docs/spec/subscription-state-machine.md")`

Excellent, very valuable findings. Let me triage and apply the clear, high-value fixes. Some findings are legitimate gaps; some are arguable. I should apply fixes to the docs (not code). Let me plan the edits.

Critical/High findings to fix:

F1 (critical, adversarial): Revoke-race predicate conflict. AD-009 rule (3) says "подтверждённое НСПК до фиксации отзыва" while spec §5 says "отправлено до отзыва, отзыв зафиксирован до ответа НСПК → если НСПК подтвердил — доводится". Also mid-debit EXPIRED undefined. Fix: define ONE predicate on initiation time: a debit accepted (registered at NSPK) while consent ACTIVE and before revoke/expiry fixation is honored to completion regardless of when NSPK confirms. Unify AD-009 (3), ADR-008 п.7, spec §5. Add EXPIRED mid-debit rule.

F2 (critical, adversarial): consent lifecycle ordering & revoke-from-PENDING; visibility contradictions; subscription.pending missing; create example status CREATED vs PENDING_PAYER.
Fixes:
- Add `PENDING_PAYER → REVOKED` and `CREATED → REVOKED` transitions (revoke absorbing in non-terminal states).
- Add monotonic consent version/sequence in consent.* events; drop stale events.
- Split "locally blocked" vs terminal REVOKED: introduce internal `REVOKE_PENDING`? Hmm. Simpler: keep `REVOKED` but define that revoke from TSP is recorded optimistically; if NSPK later rejects (rare), escalate via runbook (not auto-revert). Actually adversarial says optimistic unit permanently blocks if NSPK rejects. For safety, blocking is the safe default (fail-closed). I'll state: revoke is fail-closed — once requested/locally recorded, debits stop; NSPK rejection of the revoke is escalated (runbook), not auto-reverted. And align the API response: the revoke endpoint returns status REVOKED with note it's fail-closed/local and confirmed by NSPK asynchronously; or better, add a technical sub-state. Let me define `REVOKE_PENDING` as technical substate (visible as REVOKED to TSP, fail-closed), then `REVOKED` on NSPK confirmation. Hmm, that complicates. Simpler and honest: keep it fail-closed; document that `POST .../revoke` returns `REVOKED` (local, fail-closed) and `revokedAt` is set; NSPK confirmation is reconciled; if NSPK rejects revocation (protocol-dependent [ТРЕБУЕТ ПРОВЕРКИ]) → alert + runbook, no auto-revert. That resolves the contradiction enough.
- Fix §3.6 create example: response status should be `CREATED` at 201 (registration) OR `PENDING_PAYER` if the create synchronously returns a consentUrl. The NFR says create p95<500ms excluding NSPK, so the 201 can't include NSPK round-trip. So 201 should return `CREATED` with `consentUrl` possibly absent until C2. Hmm — but the design wants a consentUrl to give the payer. Realistically the createConsent call to NSPK returns consentUrl synchronously (adapter timeout 5s). The NFR "без учёта НСПК" contradicts. Options: (a) make create synchronous incl. NSPK (then NFR includes NSPK, contradicting "без учёта НСПК"); (b) create returns CREATED and consentUrl arrives via webhook/GET. I'll choose: `POST /v1/subscriptions` returns 201 with `status: CREATED`; `consentUrl` is included when the adapter returns it within the synchronous window (usually), otherwise polling/get returns PENDING_PAYER with consentUrl. Hmm, that's fuzzy.

Simplest consistent fix: make the create flow synchronous through the adapter (createConsent timeout 5s per adapter §3) and return `PENDING_PAYER` with `consentUrl` — and fix the NFR to say "p95 < 500 мс" for the gateway-side portion plus a separate end-to-end create incl. НСПК target. Actually the adapter contract says createConsent p99.9 = 5s. So the TSP API create cannot be p95<500ms if it waits for NSPK. 

Better: keep create async like QR flow. Recall the QR flow: `POST /payments` creates CREATED and returns 201 with paymentId; the QR is registered asynchronously? Actually in solutioning 4.1, gateway registers QR then returns 201 with qrId/qrUrl — synchronous. And NFR for "регистрация QR" is p95<500ms "без учёта времени НСПК" — meaning the gateway-side budget, while NSPK time is additive. OK so similarly for consent: create may include NSPK call but the NFR measures gateway overhead excluding NSPK. So returning `PENDING_PAYER` + consentUrl from create (after NSPK) is consistent with the QR pattern, and the NFR "без учёта НСПК" is the gateway budget. Good — then the §3.6 example returning `PENDING_PAYER` is fine, and the "created → PENDING_PAYER" is effectively synchronous; C1→C2. But the adversarial point is the state at response time. Since the QR pattern returns the post-NSPK state (QR_ISSUED), returning PENDING_PAYER is consistent. So I'll keep PENDING_PAYER but clarify: create is synchronous through the adapter (like QR registration); if the adapter call times out, returns `CREATED` (retry) and consentUrl via webhook when done. And add `subscription.pending` to the webhook list (it was emitted in C2) or remove the C2 outbox notification. Simplest: add `subscription.pending` to tsp-api §5 and note it's for async completion. Hmm, or remove the outbox notify in C2. I'll add the event to the list — cleaner.

Actually to reduce churn, I'll: 
- Clarify in §3.6 that on synchronous success 201 returns `PENDING_PAYER`; on adapter timeout returns `CREATED` (async completion), and add `subscription.pending` event.
- Add `subscription.pending` to §5 list.
- Add revoke transitions C10 `CREATED→REVOKED`, C11 `PENDING_PAYER→REVOKED`.
- Add consent version monotonicity note in §5 events.
- Align revoke semantics fail-closed.

F3 (high, adversarial): two sources of truth + reconciliation clock mismatch. Fix: declare NSPK authoritative; gateway = mirror+SOT for audit; on disagreement freeze debits and serve NSPK state; enumerate 4 cells; set consent reconciliation cadence ≤ revocation SLA (e.g., hourly, aligned with §4). Add a `SUSPENDED`/divergence handling — adversarial suggests a SUSPENDED state. I'll add `SUSPENDED` (technical, blocking) or a "debits frozen" flag. Adding a state is more work but valuable. Let me add a consent state `SUSPENDED` (technical/internal or visible?) — I'll make it internal/technical ("списания заморожены до выяснения"), visible to TSP as `ACTIVE`? Hmm. Simpler: define an internal flag `debits_blocked` set on divergence; document in §6. And change reconciliation to hourly with max staleness. Let me add `SUSPENDED` visible state? The NSPK protocol may not have it. I'll use an internal sub-state `DIVERGENCE_HOLD` (наружу — `ACTIVE`, но списания заблокированы) — but that's dangerous to show ACTIVE while blocking. Better show a distinct status. Given the API enum I set (CREATED|PENDING_PAYER|ACTIVE|REJECTED|REVOKED|EXPIRED), adding `SUSPENDED` to the visible enum is an additive change within v0.2 (still pre-release). I'll add `SUSPENDED` to the enum, spec states, OpenAPI, and contract. It's a real improvement. And it's fine since v0.2 isn't released yet.

Also fix reconciliation: nfr §7 says daily; change to hourly (align §4) with max staleness. And adapt "стоп-сигнал" to set `SUSPENDED`.

F4 (high, adversarial): T15 credits on qrId-keyed event; debit has no qrId. Fix: make `reference` (=paymentId) the mandatory correlation for subscription debits; forbid qrId matching; add `origin`/`consentId` to `payment.paid` key fields; state T15 crediting condition (reference matches paymentId AND amount matches). Add fitness case empty qrId.

F5 (high, adversarial + critical in security-1): limit guard vacuous + authority; limit reservation atomicity. Fix: make at least one limit mandatory (require `periodLimit` and/or `amountLimit`); define counted set and atomic reservation at T13 with release on T16; gateway is period-reservation authority reconciled to NSPK; serialize per consent. I'll make `amountLimit` and `periodLimit` mandatory in the request (at least one must be present — OpenAPI can use anyOf, but simpler: require both? Not all subscriptions have period limits). I'll say: `amountLimit` обязателен; `periodLimit` обязателен для периодических режимов; if absent → reject. And add reservation semantics.

Also security-1 F1 (critical): no ownership binding / IDOR. Fix: tspId derived from mTLS identity, not body; authorize consent.tspId == authenticated TSP; remove `consentUrl` from the generic Subscription response (return only at creation to initiator); add fitness test. Strong fix — apply.

Security F2 (high): pre-check at entry only, outbox dispatch re-check; revocation cancels queued debits. Fix: add dispatch-time re-validation in outbox consumer + C7 cancels queued debit outbox rows. Apply to spec + AD-009.

Security F4 (high): PII. Fix: store `payerPhoneHash` + last4 only; pass raw/token to NSPK via adapter; add measurable NFR (0 unmasked MSISDN, retention, deletion on revoke/reject/expire). Add `payerRef`/token to adapter createConsent? Security notes adapter createConsent has no payer identifier — a real gap. Fix: add `payerRef` (token/opaque) to `createConsent` in adapter contract, and say raw identifier flows only in a deeplink/tokenized form. Apply.

Security F5 (high): AML. Fix: add AML/antifraud pre-check step in T13/AD-009 + measurable NFR + thresholds owned by ИБ (H5). Apply at design level: add a guard "антифрод/AML-решение (sync call или async с блокировкой)". Keep thresholds as H5 decision but name the control and NFR.

Security F6 (medium): audit mechanics. Fix: specify append-only + hash chain, required fields, PII token not MSISDN, debit initiation in scope. Apply to ADR-006? ADR-006 is accepted; better add to AD-009/ADR-008 and spec + NFR. I'll add to ADR-008 consequences/decision and spec §8 + nfr §7.

Verification findings:
V1 (high): throughput arithmetic contradiction. Fix: state 200/500 is the total contour budget; subscriptions consume headroom; add admission control. Update nfr §7 and opkc-adapter §7 and RFP weights. Apply.
V2 (medium): spec §7 ref "TSP API §8" → §3.6–3.7. Fix.
V3 (medium): tsp-api §3.10 "§9" → "§7 п.6". Fix.
V4 (medium): rfp §4 "все 8 типов" → 12 (8+4). Fix.
V5 (medium): AC coverage: add ABS outage, transport.unavailable, concurrent limit race. Fix (AC-15..AC-17).
V6 (medium): NFR untestable: revocation anchor to receipt; billing peak degradation metric. Fix.
V7 (low): ADR-008 ABS_PENDING analogy. Fix.
V8 (low): ADR-008 add CREATED→REJECTED. Fix.
V9 (low): rfp v1.0 vs v0.2 conflict. Fix (align v1.0-draft).
V10 (low): tsp-api §8 "§3.1–3.5 без изменений" → note §3.4 text extended. Fix.
V11 (low): solutioning-subscriptions citation §1 → header. Fix.
V12 (low): ADR-008 add AD-009 to Related/References. Fix.
V13 (low pre-existing): openapi merchantOrderId required vs markdown optional. Fix openapi to make merchantOrderId optional (aligns with §3.2). Since v0.2 is additive and this is a pre-existing inconsistency, making it optional is a relaxation (backward compatible). Apply.
V14 (low pre-existing): ADR-002 REVERSED not in state machine. Out of scope-ish; but reviewer flagged. I could add a note in state-machine that REVERSED is legacy/unused. It's pre-existing and unrelated to the change; I'll leave it or add a tiny reconciliation note. I'll skip to avoid scope creep, but mention in report? Actually it's a real inconsistency in accepted docs. I'll add a brief note in state-machine.md §1 that `REVERSED` from ADR-002 is not used in the current machine (no transition), to close the gap. Minimal.

That's a lot of edits. Let me be efficient and apply the important ones. I'll prioritize critical+high (F1, F2, F3, F4, F5, security F1, F2, F4, F5) and the quick medium/low reference fixes.

Let me start editing. I'll do targeted edits.

### Edit 1: spec subscription-state-machine.md — major revision
Changes:
- §1 add `SUSPENDED` state (divergence hold) and note source-of-truth precedence.
- Intro: fix the dual-source-of-truth wording: NSPK authoritative; gateway DB is functional SOT/mirror; on disagreement freeze.
- §2 add transitions: C10 CREATED→REVOKED, C11 PENDING_PAYER→REVOKED, C12 divergence → SUSPENDED, C13 SUSPENDED→ACTIVE on resolution, C14 SUSPENDED→REVOKED.
- §3 invariants: add "revoke absorbing in non-terminal", "limits reservation", "NSPK authoritative".
- §4 T13 guard: add ownership (tspId from mTLS), mandatory limit + atomic reservation, AML/antifraud decision; T13 action with reservation; add re-validation at dispatch.
- Add T17 amount-mismatch → FAILED/alert (mirror T7). Actually T15 guard "сумма совпадает"; add T17 DEBIT_ISSUED→FAILED on mismatch + alert.
- Add T18: DEBIT_ISSUED at revoke/expire fixation → honored if initiation accepted before fixation (per unified predicate).
- §5 rewrite race table to unified predicate + expiry.
- §6 reconciliation: hourly, max staleness, all four cells, SUSPENDED on divergence.
- §7 fix ref §3.6–3.7.
- Add §8 audit fields.

### Edit 2: ADR-008 — fix rule 7 predicate, add CREATED→REJECTED, fix ABS_PENDING analogy, add AD-009 ref, add AML/audit/PII decisions.

### Edit 3: AD-009 in spine — unify predicate, add AML, ownership, limits reservation, dispatch re-check, NSPK authoritative.

### Edit 4: tsp-api.md — ownership (remove tspId from body / derive from mTLS), remove consentUrl from Subscription response (return at creation only), mandatory limits, add SUSPENDED status, add subscription.pending event, fix §3.10 ref, §8 note, AML note.

### Edit 5: openapi — owner binding (remove tspId required? keep but note; better remove tspId from SubscriptionRequest and PaymentRequest? PaymentRequest doesn't have tspId. Remove tspId from SubscriptionRequest), add SUSPENDED enum, limits required/anyOf, merchantOrderId optional, consentUrl only in create response (separate schema SubscriptionCreated).

### Edit 6: opkc-adapter.md — add payerRef to createConsent, make reference mandatory correlation, forbid qrId for debits, reconciliation for debits keyed by reference, fix throughput row note.

### Edit 7: nfr.md — revocation anchor, billing peak metric, throughput wording, PII/AML/audit metrics, reconciliation hourly.

### Edit 8: solutioning-subscriptions.md — AC additions, citation fix, throughput note, SUSPENDED mention.

### Edit 9: state-machine.md — REVERSED note + debit branch dispatch re-check mention.

### Edit 10: vendor-rfp.md — event count, version align.

This is large but let me do it with targeted edits. Given the volume, I could rewrite spec and relevant sections wholesale. Let me rewrite the subscription-state-machine.md fully (it's mine, new) to incorporate everything cleanly. That's most efficient.

Let me rewrite it.
The gate found real issues — most importantly a revoke-race predicate conflict, consent ordering/ownership gaps, and a missing correlation key for debits. I'll apply the fixes, starting by rewriting the consent state machine.

  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="1. **Согласие плательщика — отдельный агрегат шлюза со своей статусной машиной** (`docs/spec/subscription-state-machine.md`); единый источн, old_string="1. **Согласие плательщика — отдельный агрегат шлюза со своей статусной машиной** (`docs/spec/subscription-state-machine.md`); единый источн)`

Now update ADR-008 to align: rule 7 unified predicate, add CREATED→REJECTED, fix ABS_PENDING analogy, add AD-009 to Related/References, add AML/audit/PII decisions, SUSPENDED. Let me edit specific parts.

1. Related line: add AD-009? Related currently "ADR-001, ADR-002, ADR-003, ADR-005, ADR-007, AD-001…AD-008". Add AD-009 to References. Actually the finding says add AD-009 to Related/References. But AD-009 is created by this ADR — referencing it is fine ("creates AD-009"). I'll add to References.

2. Decision 1 state list: add SUSPENDED, CREATED→REJECTED.
3. Decision 2: fix ABS_PENDING analogy.
4. Decision 3: add ownership binding (tspId from mTLS), mandatory limits + reservation, AML/antifraud decision.
5. Decision 7: unified predicate.
6. Add a decision point on audit/PII.

Let me edit the Decision block. I'll replace decisions 1-3 and 7, and add 9.

Let me do targeted edits.
Now realign ADR-008 with the hardened design:

  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="4. **Сверка согласий с НСПК — ежечасная** (не реже каденса, требуемого SLA блокировки отзыва, `docs/nfr.md` §7). Расхождение переводит согл, old_string="4. **Согласие хранится в шлюзе как процессный реестр-зеркало; источник истины согласия — НСПК и банк плательщика.** Шлюз обязан сверять сог)`

Now decision 4 says "сверять согласия с НСПК (ежедневно)" — conflicts with the new hourly cadence. Fix. Decision 7 predicate. And add decisions 9 (audit/PII) and fix 6 (add business dedup key). Let me edit 4, 6, 7 and add 9.

Let me edit decision 4 (daily → hourly) — but decision 4 now duplicates decision 1's source-of-truth. I'll simplify decision 4 to be about reconciliation cadence & freeze.

Let me replace decisions 4, 6, 7 and append 8/9. Actually decision 8 (compatibility) exists after 7. Let me replace 4, then 6-7, then add 9-10 after 8.

Edit decision 4: "**Согласие хранится в шлюзе как процессный реестр-зеркало; источник истины согласия — НСПК и банк плательщика.** Шлюз обязан сверять согласия с НСПК (ежедневно)..." → "Шлюз сверяет согласия с НСПК ежечасно (не реже каденса блокировки отзыва по NFR §7); расхождение переводит согласие в SUSPENDED и останавливает списания; полученный от НСПК отзыв немедленно блокирует новые списания (fail-closed)."

Edit decision 6: add business dedup key.
Decision 7: unified predicate + expiry.
Add decision 9: audit & PII.

Let me do them.

  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="8. **Совместимость контракта ТСП — аддитивная**: новые пути, схемы, опциональные поля и типы вебхуков; существующий enum `status` и поведен, old_string="8. **Совместимость контракта ТСП — аддитивная**: новые пути, схемы, опциональные поля и типы вебхуков; существующий enum `status` и поведен)`

Now add decision 9 (audit/PII) after decision 8. And add AD-009 to References. Let me edit.

  `edit(file_path="/home/architect/project/docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md", new_string="- AD-001…AD-008 (spine); создаёт новый инвариант **AD-009** (Proposed); ADR-001, ADR-002, ADR-003, ADR-005, ADR-007", old_string="- AD-001…AD-008 (spine); ADR-001, ADR-002, ADR-003, ADR-005, ADR-007")`

Now update AD-008 References to add AD-009. Current References has "AD-001…AD-008 (spine); ADR-001, ADR-002, ADR-003, ADR-005, ADR-007". Add AD-009. Let me edit.

  `edit(file_path="/home/architect/project/ARCHITECTURE-SPINE.md", new_string="- **Rule**: (1) Согласие плательщика — отдельный агрегат с собственной статусной машиной (`docs/spec/subscription-state-machine.md`); перех, old_string="- **Rule**: (1) Согласие плательщика — отдельный агрегат с собственной статусной машиной (`docs/spec/subscription-state-machine.md`); его п)`

Now update AD-009 in spine to reflect the hardened design: unified predicate, NSPK authoritative, ownership, limits reservation, dispatch re-check, AML, SUSPENDED, audit/PII. Let me rewrite AD-009 Rule.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="### 3.6 Создание подписки (согласия плательщика) — v0.2\n\n`POST /v1/subscriptions`\n\nСоздаёт согласие плательщика на рекуррентные списани, old_string="### 3.6 Создание подписки (согласия плательщика) — v0.2\n\n`POST /v1/subscriptions`\n\nСоздаёт согласие плательщика на рекуррентные списани)`

Now update tsp-api.md for:
- §3.6: remove tspId from body (derive from mTLS), mandatory limits, add payerRef note, response: remove consentUrl from generic Subscription (return only at creation) — or keep consentUrl only in create response. I'll say consentUrl returned ONLY in the 201 create response (a `SubscriptionCreated` shape), not in GET. Also status CREATED/PENDING_PAYER.
- §3.7: Subscription status includes SUSPENDED; no consentUrl.
- §3.8: revoke fail-closed semantics; returns REVOKED (or REVOKE_PENDING visible as REVOKED).
- §3.9: add business dedup key; mandatory limits; ownership.
- §5: add subscription.pending and subscription.suspended events.
- §7: update ref (§3.10 → §7).
- §8: update "§3.4 text extended" note.
- §4: maybe add error code for ownership? 403 FORBIDDEN_CONSENT_OWNER? Add `CONSENT_FORBIDDEN` (403).
- §1: authorization note (tspId from mTLS).

Let me make these edits. First §3.6.

Current §3.6 body:
```
```json
{
  "tspId": "tsp_9f3c2a1b",
  "payerPhone": "+79990000000",     // плательщик, дающий согласие (маскируется в хранении/логах, ADR-006 §4)
  ...
```
```
and response 201 with status PENDING_PAYER, consentUrl.

Let me rewrite §3.6 request and response and rules.
Now hardening the TSP API contract — ownership, limits, correlation, events, references:

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="`GET /v1/subscriptions/{subscriptionId}/debits?from&to&cursor` → постраничный список платежей (`paymentId`, `amount`, `status`, `createdAt`, old_string="`GET /v1/subscriptions/{subscriptionId}/debits?from&to&cursor` → постраничный список платежей (`paymentId`, `amount`, `status`, `createdAt`)`
  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="События подписок (v0.2, аддитивно):\n- `subscription.pending` — согласие зарегистрировано в ОПКЦ, плательщику предъявлена форма (использует, old_string="События подписок (v0.2, аддитивно):\n- `subscription.activated` — согласие активировано плательщиком (списания разрешены)\n- `subscription.)`

Now fix §3.10 ref "§9" → "§7, п.6". Add SUSPENDED webhook `subscription.suspended`, `subscription.pending`. Add CONSENT_FORBIDDEN error code. Update §8 table. Update §1 authorization note.

Let me do these edits.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="Коды, добавленные в v0.2 (аддитивно, для подписок): `SUBSCRIPTION_NOT_FOUND` (404), `CONSENT_FORBIDDEN` (403) — согласие принадлежит другом, old_string="Коды, добавленные в v0.2 (аддитивно, для подписок): `SUBSCRIPTION_NOT_FOUND` (404), `SUBSCRIPTION_NOT_ACTIVE` (422) — согласие не в `ACTIVE)`

Now update §4 errors to add CONSENT_FORBIDDEN and SUSPENDED-related; §1 authorization; §8 table. Let me edit §4 error codes line.

Current:
```
Коды, добавленные в v0.2 (аддитивно, для подписок): `SUBSCRIPTION_NOT_FOUND` (404), `SUBSCRIPTION_NOT_ACTIVE` (422) — согласие не в `ACTIVE`, отозвано или истекло, `CONSENT_LIMIT_EXCEEDED` (422) — превышен лимит операции или периода. ...
```
Add `CONSENT_FORBIDDEN` (403) and note SUBSCRIPTION_NOT_ACTIVE covers SUSPENDED/EXPIRED/REVOKED.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="- Авторизация ТСП: **mTLS** (сертификат ТСП, выпущенный УЦ банка) + `X-API-Key`. Детали финализирует ИБ на A4; для v0.1 — mTLS обязателен.\, old_string="- Авторизация ТСП: **mTLS** (сертификат ТСП, выпущенный УЦ банка) + `X-API-Key`. Детали финализирует ИБ на A4; для v0.1 — mTLS обязателен.")`

Now §1 authorization note. Current §1:
```
- Авторизация ТСП: **mTLS** (сертификат ТСП, выпущенный УЦ банка) + `X-API-Key`. Детали финализирует ИБ на A4; для v0.1 — mTLS обязателен.
```
Add: identity binding — tspId derived from mTLS, never from body; ownership checks on all /v1/subscriptions*.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="| Новые коды ошибок подписок (`SUBSCRIPTION_*`, `CONSENT_*`) | аддитивно | нет (возможны только на новых путях) |\n| Существующие методы §3, old_string="| Новые коды ошибок подписок | аддитивно | нет (возможны только на новых путях) |\n| Существующие методы §3.1–3.5 | без изменений | нет |")`

Now §8 compatibility table: change "Существующие методы §3.1–3.5 | без изменений" row to note §3.4 text extended, and add rows for new fields. Also add subscription.pending/suspended already covered by "new webhook types". And add `CONSENT_FORBIDDEN`. Let me update the table row.

Current table rows:
```
| Новые коды ошибок подписок | аддитивно | нет (возможны только на новых путях) |
| Существующие методы §3.1–3.5 | без изменений | нет |
```
Change last row.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\n  description: >\n    Дельта 0.2.0 аддитивна относительно 0.1.0 (подп, file_path="/home/architect/project/openapi/tsp-api.yaml")`

Now update openapi/tsp-api.yaml:
- SubscriptionRequest: remove tspId, replace payerPhone with payerRef, require payerRef, amountLimit (and periodLimit for periodic — use anyOf? simpler: require payerRef, amountLimit, paymentPurpose; periodLimit optional but note), add period enum, keep others.
- Add SubscriptionCreated schema with consentUrl; Subscription schema without consentUrl but with SUSPENDED enum.
- createSubscription 201 → SubscriptionCreated.
- Add CONSENT_FORBIDDEN responses (403) to subscription paths.
- Add SUSPENDED to Subscription.status enum.
- DebitRequest: add merchantOrderId description as business dedup key.
- merchantOrderId in PaymentRequest: make optional (align with markdown) — this is a pre-existing inconsistency; relaxing required is backward-compatible.
- Add Operation header/tspId? no.
- Revoke response → Subscription.

Let me rewrite the components section carefully. I'll edit the file.

Let me just rewrite the whole yaml again with fixes.
Now update the OpenAPI to match (ownership, `SUSPENDED`, no `consentUrl` leak, optional `merchantOrderId`):

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` (`payment`/`refund`/`consent`/`debit`) | список о, old_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t)`

Now update opkc-adapter.md:
- createConsent: add payerRef; make `reference` mandatory correlation for debits; forbid qrId for debits; reconciliation for debits keyed by reference; add type=debit/consent.
- payment.paid event: add note that for subscription debits correlation is by `reference`, `qrId` absent.
- Throughput row note: 200/500 total budget.

Let me edit §3 table rows for createConsent and reconciliation, §4 payment.paid note, §7 throughput.

Current §3 createConsent row:
`| `createConsent` | регистрация согласия плательщика (подписка) | `reference` (= `subscriptionId` ядра), `tspId`, лимиты/период, `purpose?`, `expiresAt?` | `consentId` (ОПКЦ), `consentUrl`/QR, `expiresAt` | 5 c |`
Add `payerRef`.

getReconciliationReport row: add `type?` values and note debit keyed by reference. It's already `type?`; I'll change response description to mention `reference` for debits.

Let me edit.
Now the adapter contract — payer token, mandatory debit correlation, reconciliation:

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="| `payment.paid` | платёж подтверждён ОПКЦ (для списания по подписке — `reference` (= `paymentId`), без `qrId`) | `reference` (= `paymentId, old_string="| `payment.paid` | платёж подтверждён ОПКЦ | `qrId`, `reference` (= `paymentId`), `amount`, `paidAt` |")`

Now §4 payment.paid row note about correlation, and §5 idempotency note about qrId. Let me edit the events table's payment.paid row + add a correlation note.

Current events:
```
| `payment.paid` | платёж подтверждён ОПКЦ | `qrId`, `reference` (= `paymentId`), `amount`, `paidAt` |
```
Change to note qrId is absent for subscription debits.

Also the "Гарантии" paragraph and the result note. Let me edit the payment.paid row.

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="| `payment.rejected` | платёж отклонён (для списания — `reference` (= `paymentId`), без `qrId`) | `reference` (= `paymentId`, **обязателен*, old_string="| `payment.rejected` | платёж отклонён | `qrId`, `reference`, `reasonCode` (нормализованный), `reasonText` |")`

Also update `payment.rejected` row to note reference mandatory for debits. Let me edit it.

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="- Повторная доставка события с тем же `eventId` — игнорируется ядром (ADR-003). Поздние события согласий (например, `consent.revoked` после, old_string="- Повторная доставка события с тем же `eventId` — игнорируется ядром (ADR-003). Поздние события согласий (например, `consent.revoked` после)`

Now §5 note about qrId not used for debits + adapter idempotency must outlive core 24h window. Let me add a bullet in §5.

Current §5 ends with the late events bullet. Let me add after it.

  `edit(file_path="/home/architect/project/docs/nfr.md", new_string="| Метрика | Цель | Метод проверки |\n|---|---|---|\n| Latency «создание согласия» (API ТСП, без учёта НСПК) | p95 < 500 мс | Нагрузочный те, old_string="| Метрика | Цель | Метод проверки |\n|---|---|---|\n| Latency «создание согласия» (API ТСП, без учёта НСПК) | p95 < 500 мс | Нагрузочный те)`

Now update nfr.md §7: throughput wording (total budget), revocation anchor, billing peak metric, PII/AML/audit metrics, reconciliation hourly. Let me edit the §7 table rows and dependencies.

Rows to change:
- "Распространение отзыва: от события НСПК `consent.revoked`..." → "от приёма события ... до фиксации REVOKED в БД".
- "Пропускная способность списаний | sustained 100 TPS, burst 300 TPS; совместно с §2 не выходит за 200/500 TPS контура" → clarify 200/500 is total contour budget consumed jointly; add admission control.
- "Биллинговые пики ... без деградации" → concrete metrics.
- "Сверка согласий с НСПК | ежедневная" → ежечасная.
- Add AML row, PII row, audit debit-initiation row, ownership row.
- Add account-limit reservation row maybe.

Let me rewrite the §7 table rows. I'll do a targeted replacement of the whole table body.
Now tighten the NFR targets and add the missing security controls:

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="| Пропускная способность адаптера | ≥ 200 TPS sustained, пик 500 TPS — **суммарный бюджет** QR + подписок (см. `docs/nfr.md` §7) | Нагрузоч, old_string="| Пропускная способность адаптера | ≥ 200 TPS sustained, пик 500 TPS (соответствует NFR шлюза) | Нагрузочный тест на тестовом контуре НСПК )`

Now update opkc-adapter §7 throughput row to clarify shared budget. Current:
```
| Пропускная способность адаптера | ≥ 200 TPS sustained, пик 500 TPS (соответствует NFR шлюза) | Нагрузочный тест на тестовом контуре НСПК |
```
Change to clarify shared budget incl. subscriptions.

Also add consent/debit reconciliation NFR maybe. Let me edit.

  `edit(file_path="/home/architect/project/docs/solutioning-subscriptions.md", new_string="Рубрика значимости в репозитории отдельным документом не зафиксирована (база оценена как 11/15 в шапке `docs/solutioning.md`). Ниже — рекон, old_string="Рубрика значимости в репозитории отдельным документом не зафиксирована (база оценена как 11/15, `docs/solutioning.md` §1). Ниже — реконстру)`
  `edit(file_path="/home/architect/project/docs/solutioning-subscriptions.md", new_string="| AC-13 | 100 % переходов согласия и инициации списания в неизменяемом (append-only) аудит-логе | Аудит |\n| AC-14 | Сработали алерты: DLQ,, old_string="| AC-13 | 100 % переходов согласия в неизменяемом аудит-логе | Аудит |\n| AC-14 | Сработали алерты: DLQ, расхождение согласий, списание пос)`

Now update solutioning-subscriptions.md:
- citation fix §1 → header.
- Add AC-15..AC-18 for ABS outage, transport.unavailable, concurrent limits, ownership/IDOR, PII/AML? Let me add a few.
- Mention SUSPENDED and source-of-truth precedence in §2/§3.
- §5 throughput note.
- Update the H-list? Maybe add H10 (payer notification) — already H3. Fine.

Let me make targeted edits.

1. Citation: "база оценена как 11/15, `docs/solutioning.md` §1" → "база оценена как 11/15 в шапке `docs/solutioning.md`".

2. §4 compatibility: mention SUSPENDED added to subscription enum (not payment enum). Fine.

3. §6.1 add AC-15..AC-19.

4. §3 or §2: mention source-of-truth precedence + SUSPENDED.

Let me edit.
Now update the package doc: citation, hardened invariants, and additional acceptance criteria:

  `edit(file_path="/home/architect/project/docs/solutioning-subscriptions.md", new_string="- **Обратимость:** reversible до боевой эксплуатации; costly/reversible после (выданные согласия надо корректно отозвать). Детали и план от, old_string="- **Обратимость:** reversible до боевой эксплуатации; costly/reversible после (выданные согласия надо корректно отозвать). Детали и план от)`

Now add a note in §2/§3 about source-of-truth precedence and SUSPENDED, and update §4.2 to mention payerRef/reference. Also §5 already lists NFR (fine). Let me add a bullet to §2.2 "Что меняется" about SUSPENDED state / consent source-of-truth; and §4.2 adapter note. Let me edit §2.1 AD-002 row to mention SUSPENDED? It's fine.

Let me add to §2.2 list: "Согласие: состояние SUSPENDED (заморозка при расхождении с НСПК), источник истины — НСПК." And §3 add bullet about source of truth. Let me just add a sentence in §3.

Edit §3 list — add bullet: "Источник истины согласия — НСПК/банк плательщика; шлюз — реестр-зеркало, при расхождении согласие уходит в SUSPENDED."

Let me edit §3 bullets (after the reversibility bullet).

  `edit(file_path="/home/architect/project/docs/solutioning-subscriptions.md", new_string="- **Сущности:** новый агрегат «согласие плательщика» (`subscriptionId`) с состоянием `SUSPENDED` (заморозка списаний при расхождении с НСПК, old_string="- **Сущности:** новый агрегат «согласие плательщика» (`subscriptionId`), связь платежа с согласием (`consentId`, `origin=subscription`).")`
  `edit(file_path="/home/architect/project/docs/solutioning-subscriptions.md", new_string="- Новые синхронные операции: `createConsent`, `getConsentStatus`, `revokeConsent`, `initiateDebit`.\n- Новые события: `consent.activated`, , old_string="- Новые синхронные операции: `createConsent`, `getConsentStatus`, `revokeConsent`, `initiateDebit`.\n- Новые события: `consent.activated`, )`

Now update §2.2 "Что меняется" to mention SUSPENDED; and §4.2 adapter note about payerRef/correlation; §5 throughput. Let me edit §2.2 bullet list — add SUSPENDED and consent source of truth.

Current §2.2 first bullet: "**Сущности:** новый агрегат «согласие плательщика» (`subscriptionId`)..." — append "(состояние `SUSPENDED` для заморозки при расхождении)".

§4.2 last bullet: "Существующие методы/события не изменяются..." — add correlation note.

Let me do targeted edits.

  `edit(file_path="/home/architect/project/docs/solutioning-subscriptions.md", new_string="| H9 | **Подтверждение протокола НСПК** для подписок (поля, тайминги, статусы, лимиты) | Внешний вход: документация НСПК по договору [ТРЕБУ, old_string="| H9 | **Подтверждение протокола НСПК** для подписок (поля, тайминги, статусы, лимиты) | Внешний вход: документация НСПК по договору [ТРЕБУ)`

Now add H10 (payer notification before debit) to §7 table? It's already covered by H3 but security-1 emphasized it as a 161-ФЗ control. Let me add a row H10 explicitly for "уведомление плательщика перед списанием" and the AML. Actually H3 mentions "уведомление плательщика" partially ("политика повторов ... cooling-off") — no. Let me add H10.

Also update §8 to mention handoff includes new invariants.

Let me add H10 row to §7 table.

  `edit(file_path="/home/architect/project/docs/rfp/vendor-rfp.md", new_string="- **События** (§4): все 12 типов с `eventId` (8 базовых + 4 `consent.*` из v0.2); at-least-once; устойчивость к поздним/повторным событиям., old_string="- **События** (§4): все 8 типов с `eventId`; at-least-once; устойчивость к поздним/повторным событиям.")`
  `edit(file_path="/home/architect/project/docs/rfp/vendor-rfp.md", new_string="**Влияние на готовность к RFP (§11):** контракт opkc-adapter.md фиксируется как v1.0-draft, включая дельту подписок v0.2; к обязательным кр, old_string="**Влияние на готовность к RFP (§11):** контракт opkc-adapter.md фиксируется как v0.2-draft с дельтой подписок; к обязательным критериям и P)`

Now fix vendor-rfp.md: §4 "все 8 типов" → 12, version v1.0 alignment. Let me edit §4 and §12 note.

§4 current: "- **События** (§4): все 8 типов с `eventId`; at-least-once; устойчивость к поздним/повторным событиям."
Change to "все 12 типов (8 базовых + 4 `consent.*` из v0.2)".

§12 "контракт opkc-adapter.md фиксируется как v0.2-draft" → "v1.0-draft (включая дельту подписок v0.2)".

Also §11 checklist mentions v1.0-draft — fine.

Let me edit.

  `edit(file_path="/home/architect/project/docs/spec/state-machine.md", new_string="| `ABS_PENDING` | Зачисление в АБС инициировано, ждём подтверждения (ретраи) |\n| `NOTIFY_PENDING` | Вебхук ТСП поставлен в очередь (достав, old_string="| `ABS_PENDING` | Зачисление в АБС инициировано, ждём подтверждения (ретраи) |\n| `NOTIFY_PENDING` | Вебхук ТСП поставлен в очередь (достав)`

Now the state-machine.md §7 — add dispatch-time re-check note and REVERSED reconciliation. Let me edit §7 extension text to mention dispatch-time re-check and add a note about ADR-002 REVERSED.

Current §7 appended text ends: "Существующие переходы QR-потока (T1–T12) не изменяются."

Add: "Инициация списания защищена dispatch-time re-check (см. subscription-state-machine §4)." And add §1 note about REVERSED.

Let me edit §7 and §1.

§1 "Финансовые (видны ТСП в API)" table lists CREATED..REFUNDED; the doc says ADR-002 mentions REVERSED. I'll add a note after the table: "`REVERSED` из ADR-002 в текущей машине не используется (нет переходов и наружу не выставляется); при необходимости — отдельное решение." Let me find the exact text after the table.

The §1 ends with the технические table then "## 2. Таблица переходов". I'll add a note before "## 2.".

  `edit(file_path="/home/architect/project/docs/spec/state-machine.md", new_string="Инварианты не ослабляются: `DEBIT_ISSUED` — не подтверждение оплаты; **зачисление возможно только из `PAID`** (AD-005). Полное описание пер, old_string="Инварианты не ослабляются: `DEBIT_ISSUED` — не подтверждение оплаты; **зачисление возможно только из `PAID`** (AD-005). Полное описание пер)`
  `grep_search(pattern="payerPhone|ежедневн|§9|все 8 типов|v0\\.2-draft", path="/home/architect/project/docs", glob="*.md")`
  `grep_search(pattern="SUSPENDED|payerRef|CONSENT_FORBIDDEN|reference", path="/home/architect/project/docs/contracts/tsp-api.md")`

Now I have applied the fixes. Let me re-run a verification pass. The methodology says "Resolve before polish", and after applying fixes the gate should be re-run or at least a verification reviewer should confirm the critical/high findings are resolved and no new inconsistencies were introduced. Let me run one focused re-review subagent to verify the fixes and check for new inconsistencies (foreground). That's efficient.

Also I should manually check the spine lint rules: no TODO/TBD/XXX; AD ids ascending (AD-001..AD-009); each AD has Binds/Prevents/Rule. The spine uses "- **Binds**:" etc. — lint lowercases and searches "binds" in block; ok. AD-001..AD-009 present, ascending. No template tokens `{...}`? The spine has no `{...}`. Good. But `[ТРЕБУЕТ ПРОВЕРКИ]` — not TODO/TBD/XXX. Good.

Let me run a verification reviewer to confirm fixes. Actually, let me also grep for leftover contradictions: "ежедневная сверка" in subscription context, "dissens". Let me grep.

Let me do a few greps and then a verification agent.

Greps:
- "ежедневн" in subscription-state-machine / ADR-008 / solutioning-subscriptions / nfr (should not appear for consent).
- "payerPhone" remaining (should be gone from tsp-api/openapi).
- "§9" leftover in tsp-api.
- "tspId" in openapi SubscriptionRequest (should be gone).
- "consentUrl" in tsp-api §3.7 (should say without).
- "SUSPENDED" consistency.

Let me grep.
Let me verify the fixes and check for leftovers across the changed docs.

  `edit(file_path="/home/architect/project/docs/solutioning-subscriptions.md", new_string="- Сверка согласий с НСПК: ежечасно, расхождений 0 (при расхождении — `SUSPENDED`); аудит переходов согласия и инициации списания — 100 %; R, old_string="- Сверка согласий с НСПК: ежедневно, расхождений 0; аудит переходов согласия — 100 %; RPO = 0; доступность реестра согласий ≥ 99,95 %.")`

Fix `docs/solutioning-subscriptions.md:127` "ежедневно" → "ежечасно". Let me edit.

  `edit(file_path="/home/architect/project/docs/solutioning-subscriptions.md", new_string="- Пропускная способность: суммарный бюджет контура (QR + подписки) — 200 TPS sustained / 500 TPS пик, admission control; биллинговые пики ×, old_string="- Пропускная способность: sustained 100 TPS, burst 300 TPS, биллинговые пики ×3 за 15 мин; совместно с базой — в пределах 200/500 TPS конту)`

Also §5 in solutioning-subscriptions has the old throughput wording "sustained 100 TPS, burst 300 TPS; совместно с базой — в пределах 200/500 TPS контура" — update to shared budget. Let me edit that bullet.

  `edit(file_path="/home/architect/project/docs/solutioning-subscriptions.md", new_string="- Отзыв: от **приёма** события НСПК до фиксации `REVOKED` p95 < 60 с; после фиксации отзыва — 0 отправленных списаний.", old_string="- Отзыв: от события НСПК до блокировки списаний p95 < 60 с; после фиксации отзыва — 0 принятых списаний.")`

Also update the "Отзыв: от события НСПК" in §5 to "от приёма события". Let me edit.

  `agent(description="Verify applied fixes", prompt="You are a verification reviewer. A prior review of a bank architecture change (SBP subscriptions, ADR-008 / AD-009) raised findings; the do, run_in_background=false)`

Now re-run a focused verification reviewer to confirm the critical/high findings are resolved and no new contradictions. Let me launch one foreground verification agent.

Also, I should double check the spine lint manually: no `{template}` tokens. The spine "Изменения (Proposed...)": fine. Let me also verify AD numbering monotonic: AD-001...AD-009. Yes.

Let me run the verification agent.
Now a focused re-review to confirm the critical/high findings are resolved and nothing new broke.

  `edit(file_path="/home/architect/project/docs/contracts/tsp-api.md", new_string="- **Идентичность и владение (v0.2):** аутентифицированная личность ТСП (mTLS) — авторитетна; `tspId`, если передан в теле, должен ей соотве, old_string="- **Идентичность и владение (v0.2):** `tspId` выводится исключительно из аутентифицированной личности ТСП (mTLS); передача `tspId` в теле з)`
  `edit(file_path="/home/architect/project/docs/solutioning-subscriptions.md", new_string="- **Аддитивные коды ошибок:** `SUBSCRIPTION_NOT_FOUND` (404), `CONSENT_FORBIDDEN` (403), `SUBSCRIPTION_NOT_ACTIVE` (422), `CONSENT_LIMIT_EX, old_string="- **Аддитивные коды ошибок:** `SUBSCRIPTION_NOT_FOUND` (404), `SUBSCRIPTION_NOT_ACTIVE` (422), `CONSENT_LIMIT_EXCEEDED` (422).\n- **Аддитив)`

Good — findings all resolved, but new minor issues N1-N6. Let me fix the important ones:

N1 (correctness/contract): The §1 blanket "tspId в теле запрещено" contradicts QR example §3.2 which includes tspId. Fix: scope the rule to v0.2 subscription paths only, or clarify that tspId in body is deprecated/ignored for payments? The base contract §3.2 has tspId in the payment request. To keep additive, the ownership rule should apply to subscription paths (and generally the authenticated identity must match tspId). Best fix: reword §1 to say: "`tspId` должен совпадать с аутентифицированной личностью ТСП; в v0.2 для путей `/v1/subscriptions*` `tspId` в теле не передаётся. Расхождение → 403." That keeps QR behavior unchanged (tspId allowed but must match identity — actually base contract didn't enforce match; introducing enforcement on v0.1 paths would be a behavior change). To be strictly additive: enforce ownership on subscriptions; for existing paths, note "значение `tspId` в теле должно совпадать с аутентифицированным ТСП (проверка вводится; для v0.1-потребителей, передающих свой корректный tspId, поведение не меняется)". Hmm, that's still a behavior change for a TSP that sends someone else's tspId (which would be a bug/attack). It's fine to note it as security fix but flag. Simpler and safest: apply the "tspId derived from mTLS" rule to subscription paths; state that for existing paths the authenticated identity is authoritative and `tspId` in body, if present, must match (security tightening; existing correct consumers unaffected — still additive in practice since no legitimate consumer sends a mismatched tspId). I'll reword to avoid the blanket "запрещена" and reconcile with §3.2. And adjust §8 table note.

N2: update solutioning §4.1 to include subscription.pending, subscription.suspended, CONSENT_FORBIDDEN.

N3: add version/sequence to adapter events. Add to §4 mandatory fields: `seq`/`version` (monotonic per entity) optional/required. I'll add to the "Обязательные поля события" line: `seq` (монотонная версия по сущности согласия/платежа). Keep `correlationRef`.

N4: spec §3 release rule: include T17; and define terminal state for dispatch-time cancel (payment goes to FAILED with reason CONSENT_NOT_ACTIVE, reserve released). Fix.

N5: subscription.pending emission: spec C2 always enqueues; tsp-api says async only. Fix tsp-api wording: "используется при синхронной регистрации (уведомляет о PENDING_PAYER); не дублируется, если статус уже возвращён в 201" — hmm. Simplest: in C2, emit `subscription.pending` only if the create response already returned (async completion), else rely on 201. I'll adjust spec C2 to note the event is emitted only when C2 happens after the HTTP response (async), aligning with tsp-api. Add a clause.

N6: openapi add 404 responses to revoke/debits; add anyOf for periodLimit when period is periodic. Minor; I'll add 404s and a description note for periodLimit (instead of complex anyOf).

Let me apply these.

Edit 1: tsp-api §1 ownership wording.
All prior findings resolved; a few minor inconsistencies remain. Fixing them now.

  `edit(file_path="/home/architect/project/docs/contracts/opkc-adapter.md", new_string="Обязательные поля события: `eventId` (uuid, для дедупликации), `type`, `timestamp`, `seq` (монотонная версия по сущности: для согласия — ве, old_string="Обязательные поля события: `eventId` (uuid, для дедупликации), `type`, `timestamp`, `correlationRef` (reference ядра, если применимо).")`

Now N3: add seq/version to adapter events. Edit opkc-adapter §4 mandatory fields line.

Current: "Обязательные поля события: `eventId` (uuid, для дедупликации), `type`, `timestamp`, `correlationRef` (reference ядра, если применимо)."

Add `seq` (монотонная версия по сущности; для consent — версия согласия).

  `edit(file_path="/home/architect/project/docs/spec/subscription-state-machine.md", new_string="- **Лимиты обязательны и резервируются атомарно**: лимит должен быть задан при создании согласия (C1); T13 в одной транзакции проверяет и *, old_string="- **Лимиты обязательны и резервируются атомарно**: лимит должен быть задан при создании согласия (C1); T13 в одной транзакции проверяет и *)`

Now N4: spec §3 reserve release: include T17; define terminal state for dispatch-time cancel. Edit spec §3 bullet.

Current: "Резерв освобождается при `FAILED` (T16) и при финальном расхождении сверки; успешное списание (`PAID`) сохраняет резерв."

Change to: "Резерв освобождается при `FAILED` (T16/T17) и при отмене неотправленного списания (dispatch-time re-check переводит платеж в `FAILED` с `reasonCode=CONSENT_NOT_ACTIVE`), а также при финальном расхождении сверки; успешное (`PAID`) сохраняет резерв."

Let me edit.

  `edit(file_path="/home/architect/project/docs/spec/subscription-state-machine.md", new_string="| C2 | `CREATED` | `PENDING_PAYER` | ответ адаптера ОПКЦ: `consentId` получен | `consentUrl` непустой | сохранить `nspkConsentId`, `consent, old_string="| C2 | `CREATED` | `PENDING_PAYER` | ответ адаптера ОПКЦ: `consentId` получен | `consentUrl` непустой | сохранить `nspkConsentId`, `consent)`

N5: subscription.pending emission condition. In spec C2, note it's emitted only when C2 happens after the synchronous response (async). Let me edit C2 action.

Current C2 action cell: "сохранить `nspkConsentId`, `consentUrl`; outbox-нотификация `subscription.pending`".
Change: "...; outbox-нотификация `subscription.pending` — только если переход произошёл после отдачи ответа 201 (асинхронная регистрация)".

  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        '403':\n          description: Согласие принадлежит другому ТСП (CONSENT_FORBIDDEN)\n        '404':\n          description: Согласи, old_string="        '403':\n          description: Согласие принадлежит другому ТСП (CONSENT_FORBIDDEN)\n  /v1/subscriptions/{subscriptionId}/debits:")`
  `edit(file_path="/home/architect/project/openapi/tsp-api.yaml", new_string="        '403':\n          description: Согласие принадлежит другому ТСП (CONSENT_FORBIDDEN)\n        '404':\n          description: Согласи, old_string="        '403':\n          description: Согласие принадлежит другому ТСП (CONSENT_FORBIDDEN)\n        '422':\n          description: Согласи)`

N6: openapi add 404 to revoke/debits; add note on periodLimit conditional. Let me edit openapi: add '404' responses to revoke and debits post, and periodLimit description already says mandatory for periodic modes. I'll add the 404s. Also add 403 to listDebits? Minor. Let me add 404 to revoke and debits.

Let me edit the openapi file with targeted edits.

  `read_file(file_path="/home/architect/project/openapi/tsp-api.yaml", offset=64, limit=80)`

Wait — the first edit added a 404 to the revoke path (which already had 403). Good. The second edit added 404 to debits post. Both fine. But I need to verify the revoke path now has 403+404, and debits has 403+404+422. Let me check the openapi file around those paths.

Also the first edit's old_string matched the revoke path (403 then next path /debits). Good. The second matched debits path (403 then 422). Good.

But careful: the first edit could have matched the `GET /subscriptions/{id}` 403/404 block? No — that block has 403 then 404 (already) and next is `/v1/subscriptions/{subscriptionId}/revoke`. The old_string was "403 ... \n  /v1/subscriptions/{subscriptionId}/debits:" which uniquely matched revoke's 403 followed by the debits path. Good.

Let me verify with a read of the paths section to be safe, then run final checks. Actually let me just grep the openapi for response codes per path.

Let me read the openapi file head (paths) to confirm structure is valid YAML (indentation).

  `run_shell_command(command="cd /home/architect/project && echo \"=== AD ids in spine ===\" && grep -oE '^## AD-[0-9]+' ARCHITECTURE-SPINE.md && echo \"=== forbidden pl, description="Run repo fitness checks manually")`

YAML structure is valid. 

Now let me do a final consistency sweep: check that all cross-references resolve and that the spine lints clean manually. Also verify no "TODO|TBD|XXX" in spine or ADRs (CONSTRAINTS rules: adr-no-placeholders must_not_contain '<!--' in docs/adr/*.md; spine-lints-clean must_not_contain TODO|TBD|XXX).

Let me grep:
- `<!--` in docs/adr/*.md (must be none).
- TODO|TBD|XXX in ARCHITECTURE-SPINE.md.
- Also check the spine AD headings AD-001..AD-009 order.

Let me run greps.
Final mechanical checks — the repo's own fitness rules (no placeholders, ascending AD ids, no HTML comments in ADRs):

  `run_shell_command(command="cd /home/architect/project && git status --short", description="List created and modified files")`

All fitness checks pass. Now let me do a final YAML validity check without python. I can't parse YAML. But I can eyeball; it looks fine. Maybe use node? Check if node exists. Actually `node -e` could parse YAML only with a library. Skip.

Let me also verify the git status to list changed/created files, and double check nothing unexpected.

Also consider: should I create a memlog? Given no python/uv, the skill's memlog.py can't run. I'll note that in the report. The methodology's reviewer gate was run (2 rounds). Good.

Let me get git status.


Everything is in place. Let me write a final summary to the user (in Russian, matching their language), covering the 7 deliverables, the created/modified files, key decisions, and notes (no python/uv so memlog wasn't created; reviewer gate run; accepted files changed via ADR process; handoff regeneration deferred to after A3).

Should I save any memories? The auto-memory instructions: save durable cross-conversation knowledge. There's project context: the repo is a bank SBP gateway decision repo with an ADR-based change mechanism, tag "accepted", no python/uv in env. Is that worth remembering? "Memory types: project — ongoing work/goals not derivable from code/git." The ADR-based change convention is derivable from the repo. The absence of python/uv is environmental and could be useful ("no Python/uv available on this machine"), but that's environment-specific and might change. Hmm. The instruction says memory is currently empty and to save when worth remembering. I think a small project memory about the accepted decision + this change awaiting A3 could be useful, but it's derivable from the repo now (ADR-008 exists). I'll skip memory writes to avoid redundancy — the docs capture it. Actually, one non-obvious durable fact: the repo uses an ADR-ratification workflow (new ADR + Proposed spine AD) to change accepted decisions, and the accepted baseline is git-tagged `accepted`. That's derivable from git/docs. Skip.

Let me write the final response. Keep it structured but concise-ish given the scope. Use Russian. List created/modified files at the end as requested.

I must not claim things I didn't do. I did run the reviewer gate (subagents), applied fixes, ran manual fitness checks (no python). I did not run the deterministic lint_spine.py (no python). I did not create a memlog. Mention these honestly.

Let me draft.

Key content:
- What I did: used bmad-architecture method (AD-n invariants, alternatives/consequences/reversibility, reviewer gate).
- Change route: Critical, 12/15 (assumption flagged).
- Deliverables 1-7 mapping.
- Key decision ADR-008 + AD-009.
- Contracts additive, /v2 not needed.
- NFR, acceptance, rollback.
- Human decisions H1-H10.
- Reviewer gate: 3 reviewers, found & fixed critical/high issues.
- Notes: no python/uv → lint/memlog not run; accepted files changed via ADR/proposed-AD mechanism only; handoff (.arch-handoff) NOT regenerated — deliberately, after A3.
- Files list.

Let me write it.
Готово. Пакет собран по методике `bmad-architecture` (инварианты AD-n с Binds/Prevents/Rule, альтернативы/последствия/обратимость, reviewer gate) и по конвенции репозитория — принятые документы меняются только через ADR-процесс (новый ADR + новый Proposed-инвариант; `AD-001…AD-008` не переписаны, ничего не перенумеровано).

## Что получилось

**1. Значимость и маршрут** — маршрут **Critical**, оценка **12/15** (финансовый риск 3, внешний протокол 3, регуляторика/ПДн 3, влияние на архитектуру 2, обратимость 1). Рубрика 0–3×5 реконструирована из обоснования базы и помечена как допущение (в репозитории рубрики нет). Нужна полная глубина: A1→A5, обязательный A3 (вендор/юрист/бизнес).

**2. Влияние на архитектуру** — AD-002/003/004/007 **расширяются**, AD-005 **сохраняется без ослабления** (зачисление только из `PAID`, ветка `DEBIT_ISSUED` наружу не выставляется), AD-001/006 **не меняются**, AD-008 **напрягается** (развилка A3, если вендор не поддержит подписки). Введён **AD-009** (Proposed).

**3. Решение** — **ADR-008** (Proposed, на A3): согласие плательщика — отдельный агрегат со своей статусной машиной; списание — платёж `origin=subscription`; транспорт — через единственный адаптер ОПКЦ. Рассмотрены 5 альтернатив (микросервис, passthrough, in-house транспорт, отсрочка), последствия и обратимость (reversible до прода; costly после — выданные согласия надо корректно отозвать).

**4. Контракты** — API ТСП `v0.2` и адаптер ОПКЦ `v0.2`/OpenAPI `0.2.0`: **только аддитивно** (новые пути `/v1/subscriptions*`, опциональные `origin`/`consentId`, новые коды и вебхуки `subscription.*`; enum `status` платежа не тронут) → **`/v2` не требуется**.

**5. NFR** — §7 `docs/nfr.md`: измеримые цели, включая 0 дублей списаний, 0 списаний без `ACTIVE`-согласия, PII-показатели, ежечасную сверку согласий, суммарный бюджет 200/500 TPS.

**6. Приёмка и откат** — AC-1…AC-19 (включая негативные и конкурентные сценарии, IDOR, гонку «отзыв ↔ списание», отказ АБС/НСПК) и пошаговый откат с сигналами и владельцем решения; ключевой момент — сохранять онлайн отзыв/возврат/сверку при откате.

**7. На решение человека-архитектора** — H1…H10: поддержка подписок вендором, юридическая модель согласия, бизнес-политика лимитов/dunning, scope и этапность, AML/антифрод, disputes, ПДн, видимые статусы, подтверждение протокола НСПК, уведомление плательщика.

## Reviewer gate (важное)

Прогнал 3 независимых ревьюера. Они нашли и я исправил **критичные/высокие** дефекты: конфликт предиката гонки «отзыв ↔ списание» (сведён к единому предикату по времени приёма `initiateDebit`), отсутствие отзыва из `CREATED`/`PENDING_PAYER` и расхождение источников истины (НСПК авторитетен, шлюз-зеркало, состояние `SUSPENDED`, ежечасная сверка), корреляцию зачисления по `qrId` у списания без QR (теперь строго по `reference`), «пустой» лимит и его неатомарность (лимит обязателен + резерв), **IDOR** (владелец согласия из mTLS, `403 CONSENT_FORBIDDEN`, `consentUrl` только при создании), ПДн (`payerRef`/токен), AML-контроль, аудит (append-only), плюс правки битых ссылок и арифметики пропускной способности.

## Оговорки (честно)

- В окружении **нет Python/uv**, поэтому детерминированный `lint_spine.py` и `memlog.py` не запускались — их проверки (нет TODO/TBD/XXX, AD-id монотонны, Binds/Prevents/Rule на месте, нет `<!--` в ADR) я выполнил вручную, все прошли.
- **`.arch-handoff/` намеренно не перегенерирован**: передача исполнителям — после A3 и получения документации НСПК (в §8 пакета описана дельта для handoff).
- `docs/solutioning.md` тронут одной строкой-указателем (roadmap), чтобы принятый документ не разошёлся молча с изменением.

## Файлы

Созданы:
- `docs/adr/ADR-008-podpiski-sbp-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`
- `docs/solutioning-subscriptions.md`
- `docs/spec/subscription-state-machine.md`

Изменены:
- `ARCHITECTURE-SPINE.md` (AD-009 Proposed, раздел «Изменения», Deferred, «Контракты и версии»)
- `docs/contracts/tsp-api.md`, `openapi/tsp-api.yaml`
- `docs/contracts/opkc-adapter.md`
- `docs/spec/state-machine.md`
- `docs/nfr.md`, `docs/rfp/vendor-rfp.md`
- `README.md`, `docs/solutioning.md`
