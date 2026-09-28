<!-- источник: <HARNESS>/runs-clean/cells/wgmujp6/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-clean-cells-wgmujp6-ws/chats/8adabd83-16e1-4f6a-a62a-02e34faae783.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `skill(skill="calm")`

Let me start by understanding the task and the repository structure. This is a solution architecture task for a bank's C2B payment gateway (СБП = Система быстрых платежей, Russia's Faster Payments System). The task is to prepare an architectural package for adding recurring C2B debits (subscriptions) by payer consent.

The user explicitly says "Код не пиши" (don't write code), but I need to produce architectural artifacts. The user says "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению" (methodological skills and tools may be installed — use them as intended).

There's a `calm` skill available (project skill) - "An AI Assistant for FINOS CALM development." FINOS CALM = Common Architecture Language Model. This is likely relevant since we're doing architecture work with a CALM-based repo.

There's also `.claude/skills/` and `.qwen/skills/` in the repo. Let me explore.

Let me first understand the repository deeply before doing anything. I need to read:
1. `ARCHITECTURE-SPINE.md` - the invariants AD-001...AD-008
2. `docs/` - solutioning, NFR, ADR-001...007, contracts, status machine
3. `openapi/tsp-api.yaml` - TSP API contract v0.1
4. `.arch-handoff/` - rules and handoff package
5. `.qwen/skills/` - installed skills
6. `.claude/skills/` - installed skills

Let me start exploring. I should be thorough here. Let me read the key files in parallel first.

Actually, let me first invoke the `calm` skill since it's a project skill specifically for FINOS CALM development, and this is clearly CALM-based architecture work. But wait — I need to understand what the skill does first. Actually, the instructions say "When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action." The calm skill is relevant here since it's about FINOS CALM and this repo is CALM-based (the git log says "baseline: стек calm установлен").

But let me also think — should I invoke calm first, or explore first? The skill instruction says invoke immediately as first action when relevant. Let me invoke the calm skill to understand what methodological tools are available.

Actually, let me think carefully. The calm skill is "An AI Assistant for FINOS CALM development." Given the repo mentions CALM stack, this is highly relevant. Let me invoke it first.

Let me do that.
I'll start by loading the project's methodological skill, since this repo is explicitly CALM-based and the task is architecture work.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/.claude/skills/calm/calm-prompts/archit)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/.claude/skills/calm/calm-prompts/calm-c)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/.claude/skills/calm/calm-prompts/docume)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/.claude/skills/calm/calm-prompts/patter)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/.claude/skills/calm/calm-prompts/standa)`

The skill says I must read the tool prompt files. Let me read them. But note the base directory is `.qwen/skills/calm`, and the prompt files are in `.claude/skills/calm/calm-prompts/`. Let me read them.

Also I need to explore the repo thoroughly. Let me read the key files in parallel.

Let me first read the CALM prompt files (the important ones), and the core repo files.

Let me batch these reads.
Loading FINOS CALM instructions...

  `glob(pattern="**/*")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/README.md")`

I've read the CALM skill guidance. Now I need to deeply understand the repository. Let me explore the key files:

1. `ARCHITECTURE-SPINE.md` - the invariants AD-001...AD-008
2. `docs/` - solutioning, NFR, ADR-001...007, contracts, status machine
3. `openapi/tsp-api.yaml` - TSP API contract v0.1
4. `.arch-handoff/` - rules and handoff package

Let me also check the `.qwen/skills/` and `.claude/skills/` directory listing to see what other skills/tools exist.

Let me list the directory structures and read the core files in parallel.
Now let me explore the repository structure thoroughly. I'll list the key directories and read the core files in parallel.

  `glob(pattern="docs/**/*")`
  `glob(pattern=".arch-handoff/**/*")`
  `glob(pattern="openapi/**/*")`
  `glob(pattern=".qwen/**/*")`
  `glob(pattern=".claude/**/*")`

The `glob **/*` was too broad and got truncated by node_modules. Let me focus on the actual docs directory, .arch-handoff, openapi, and skills. Let me list those specific directories.
The glob was flooded by node_modules. Let me target the actual project directories.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/openapi/tsp-api.yaml")`

Now I have a clear picture of the repo structure. The key files to read:

1. `docs/solutioning.md` - full design
2. `docs/nfr.md` - NFRs
3. `docs/contracts/tsp-api.md` - TSP API contract v0.1
4. `docs/contracts/opkc-adapter.md` - OPKC adapter contract
5. `docs/spec/state-machine.md` - status machine
6. `docs/rfp/vendor-rfp.md` - RFP package
7. `docs/adr/ADR-001..007.md` - ADRs
8. `openapi/tsp-api.yaml` - OpenAPI contract
9. `.arch-handoff/TASK.md`, `.arch-handoff/ARCHITECTURE.md`, `.arch-handoff/CONSTRAINTS.yaml`, `.arch-handoff/RUBRIC.yaml`, `.arch-handoff/MANIFEST.json`

Let me read the most important ones. I'll batch these reads. Let me start with solutioning.md, nfr.md, state-machine.md, tsp-api.md, tsp-api.yaml, and the handoff TASK.md + RUBRIC.yaml (these will tell me the conventions for how to structure the handoff package).

Let me read them in parallel.
Now let me read the core design documents and the handoff conventions.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/.arch-handoff/ARCHITECTURE.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/.arch-handoff/MANIFEST.json")`

This is very rich. Now let me read the remaining docs: ADRs (at least the key ones), contracts/opkc-adapter.md, rfp/vendor-rfp.md, and the handoff package files (TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json). These will tell me how to properly extend the handoff package.

Let me read the ADRs and the handoff files. I'll batch.

Actually, given the volume, let me be strategic. The key thing I need to understand:
1. The handoff conventions (TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json) — this tells me HOW to change accepted solution files.
2. The ADRs — to understand the format and numbering, and the existing ADR-007 (A3 decision).
3. The opkc-adapter contract and vendor-rfp — to understand if recurring payments touches the OPKC adapter.

Let me read the handoff files and the ADRs.
Now the handoff package conventions and the existing ADRs.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/adr/ADR-005-integraciya-s-abs-zach)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/opkc-adapter.md")`
  `grep_search(pattern="architecture\\.json|pattern\\.json|\\.calm\\.json|\"\\\\$schema\"", path="<HARNESS>/runs-clean/cells/wgmujp6/ws", glob="!node_modules/**")`

Now I understand the structure well. Let me read the remaining ADRs (ADR-003 through ADR-007) to understand the full decision set, especially ADR-007 (strategy) and ADR-005 (ABS integration / returns saga), ADR-004 (notifications). And the opkc-adapter contract and vendor-rfp.

Actually, let me focus. The key files I still need:
- ADR-003 (mTLS)
- ADR-004 (at-least-once DLQ)
- ADR-005 (ABS integration)
- ADR-006 (trust)
- ADR-007 (strategy/A3)
- docs/contracts/opkc-adapter.md
- docs/rfp/vendor-rfp.md

Let me read these to fully understand. Also I should check whether there's a `calm` tool actually installed (`which calm`) and whether there are existing CALM architecture files (.architecture.json). The glob showed no `.architecture.json` files in docs. Let me check whether the repo uses CALM architecture files or just markdown. The spine is markdown, docs are markdown. There's no CALM JSON in the visible files. So the "CALM" here refers to the methodology/stack (FINOS CALM), but the actual artifacts in this repo are markdown ADRs + spine + contracts. The `calm` skill is the methodological assistant.

Actually wait — the git log says "baseline: стек calm установлен" (calm stack installed). But I don't see any `.architecture.json` files. Let me check if `calm` CLI is installed and if there are any pattern/architecture JSON files I might have missed. Let me search.

Actually the important thing for my task: I need to prepare an architecture package for the recurring C2B debits feature, layered on top of the accepted solution. The deliverable is a set of markdown artifacts (ADR, solutioning update, contract change to openapi/tsp-api.yaml, NFR, acceptance criteria, rollback plan), following the repo's conventions.

The task says: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." (Change accepted decision files only in the way accepted in this repo.) So I should follow the ADR convention: new ADR-008 (recurring payments), a new section in solutioning.md or a separate solutioning doc, update spine with a new AD-009 (or as a new spine block?), update contracts, update NFR.

Let me understand how the repo "changes" accepted decisions. Looking at the structure:
- `ARCHITECTURE-SPINE.md` — invariants AD-001..AD-008 (each has Status: Proposed/Adopted).
- `docs/adr/ADR-XXX.md` — ADR docs.
- `docs/solutioning.md` — full design.
- `docs/nfr.md` — NFRs.
- `docs/contracts/tsp-api.md` + `openapi/tsp-api.yaml` — TSP API contract.
- `docs/spec/state-machine.md` — status machine.
- `.arch-handoff/` — handoff package.

The convention for "changing" accepted decisions: Add a new ADR (ADR-008) rather than editing existing ADRs. The spine gets new invariant(s) with Status: Proposed referencing the new ADR. The solutioning gets a new section or new doc. The contract gets a versioned change (v0.1 → additive, since contract §6 says "Добавление опциональных полей — обратно совместимо, не требует новой версии").

Now, there's a question: should I create a CALM architecture JSON file? The `calm` skill was invoked, but the repo itself uses markdown artifacts, not CALM JSON. The skill's "first interaction instructions" say I should read the prompts and "confirm you're ready." I've read the key prompts. The repo doesn't seem to have `.architecture.json` files, so the CALM methodology is present as a skill but the actual deliverables are markdown. However, I should check whether `calm` CLI is installed and whether there's a CALM model somewhere I need to extend.

Actually, let me check for `.architecture.json` or `*.pattern.json` files and whether calm CLI is installed. This matters because if the repo uses CALM JSON as the source of truth, I need to extend it. Let me search.

Let me also read the remaining ADRs and the opkc-adapter + rfp docs.
Let me read the remaining ADRs, the OPKC adapter contract, and check whether CALM tooling/models are actually present in this repo.

  `run_shell_command(command="which calm 2>/dev/null || echo \"calm CLI not installed\"; ls -la <HARNESS>/r, description="Проверка наличия calm CLI и CALM-артефактов")`

Now I have a very complete picture. Key finding: **there are no CALM JSON files in this repo** — the repo uses markdown ADRs + spine + contracts. The CALM skill is a methodological assistant, but the actual artifacts are markdown. The `calm` stack "installed" refers to the skill being available, not necessarily CALM JSON models. The `.qwen/skills/calm` and `.claude/skills/calm` are identical (same prompt files). The `calm` CLI might not even be installed. Let me verify quickly whether `calm` CLI is installed, but honestly this doesn't matter much for my deliverable since there are no CALM JSON files to extend.

Actually, I should confirm there's no CALM CLI tooling needed. But given there are zero `.architecture.json` files, the deliverables are markdown. The `calm` skill's "first interaction" instruction asked me to read the prompts and confirm readiness. I've read the most relevant ones. I don't need to generate CALM JSON unless the repo used it. It doesn't. So I'll note that and proceed with markdown.

Now let me understand the task fully and plan.

The task: ТСП (online cinemas, housing, telecom) want **recurring C2B debits by payer consent** — СБП subscriptions. Currently every payment requires QR + client action. I need to prepare an architecture package for this change layered on the accepted solution, so it can be taken to architecture decision and then handed to implementers.

The 7 deliverables:
1. Significance assessment and route (how deep design needed and why)
2. Impact on accepted architecture: which invariants (AD-001..AD-008) affected, what changes, what doesn't
3. Architecture decision with alternatives, consequences, reversibility
4. Contract changes (`openapi/tsp-api.yaml`) without breaking existing consumers
5. Measurable NFRs for the new feature
6. Acceptance criteria and rollback plan
7. What remains for human architect to decide and why

And: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — change accepted decision files only in the way accepted in this repo. So I should follow the repo's conventions:
- New ADR (ADR-008) for the recurring payments feature.
- Spine: new invariant(s) AD-009 (with Status: Proposed referencing the new ADR).
- New/updated contract doc + OpenAPI yaml.
- NFR additions.
- Acceptance criteria + rollback plan (probably as part of the ADR + a dedicated section or new doc).

Let me think about the domain carefully. This is important — I'm acting as a bank's solution architect. I need to get the СБП recurring payments (recurrent/autopayments) domain right.

**СБП recurring payments domain (recurrent C2B by payer consent):**

In СБП, there are a few mechanisms relevant to recurring debits:
1. **Платёжные подписки (payment subscriptions / recurrent payments)** — НСПК introduced "СБП Платежи по подписке" / "автоплатежи" (recurring payments). This is a real СБП capability. The mechanism: payer gives consent (согласие) to the TSP/merchant to debit their account periodically. The consent is registered in НСПК (the СБП has a "подписка/согласие" concept — a token/ID that represents the payer's consent), and then the merchant initiates debits without the payer's active per-payment action.

2. There's also **С2В «подписка»** via НСПК's "СБП ЦФА/подписки" but more concretely, the "автоплатёж" flow in СБП.

Actually, the specific СБП capability is called "**Платежи по согласию (recurring payments) / СБП-подписка**". In the СБП ecosystem, the mechanism works roughly like:
- Payer registers consent (согласие) with the bank (ТСП's bank? or the payer's bank?). Actually in СБП, consent-based recurring payments involve the payer's bank (банк плательщика) holding the consent and the merchant initiating pull payments via ОПКЦ.

Let me recall the actual NSPK СБП features. СБП supports:
- C2B pull payments (QR-based)
- C2B "платёжная подписка" / recurring — actually НСПК launched "СБП Платежи по подписке" (СБП subscription payments) in ~2023-2024. This is the "автосписание" (autodebit) capability.

The key architectural concept in СБП recurring:
- **Согласие (consent/mandate)** — a standing instruction/authorization from the payer to the TSP to debit their account on a schedule. 
- The consent is established once (with the payer's active confirmation via their bank's app, similar to how they'd confirm a payment — but it's a consent for future debits).
- After consent is established, the TSP (via the acquirer bank = our bank's СБП gateway) initiates **recurrent debit requests** to НСПК, which routes them to the payer's bank, which executes them without per-payment confirmation (within the consent's limits/validity).
- The consent has: a unique consent ID (token), payer identifier, max amount per debit / max total, period/schedule, validity period, revocation capability.

This maps cleanly onto the existing architecture:
- New entity: **Согласие (consent/mandate)** with its own lifecycle/status machine (CREATED → ACTIVE → REVOKED/EXPIRED/SUSPENDED), distinct from the payment status machine.
- New TSP API methods: create consent (initiate consent flow), get consent status, initiate debit under consent, revoke consent.
- The consent flow requires the payer to confirm in their bank app (a consent URL / redirect to the payer's bank), which is similar to QR but a one-time setup.
- Debits are initiated by TSP on schedule → each debit creates a payment (reusing the existing payment status machine), but the trigger is different: no QR, instead a consent reference.
- Idempotency extends to consent creation and debit initiation.
- The OPKC adapter contract gets new operations: registerConsent, revokeConsent, initiateDebit (or createDebit under consent), plus new events (consent.registered, consent.revoked, consent.expired, debit.paid, debit.rejected).

This is a **significant** change because it introduces a new financial entity (consent/mandate), a new status machine, new TSP API surface, new OPKC adapter contract surface, and touches the invariants:
- AD-002 (single source of truth status machine) — extends to a second status machine (consent).
- AD-003 (idempotency) — extends to consent/debit operations.
- AD-005 (credit only from PAID) — recurring debit still lands on PAID → CREDITED, but the "payment" is now "debit", no QR.
- AD-001 (isolation) — unchanged in spirit.
- AD-004 (single OPKC adapter) — unchanged, but contract expands.
- AD-006 (trust zones) — unchanged.
- AD-007 (compliance) — consent is ПДн-heavy, needs explicit consent records, revocation rights (152-ФЗ, 161-ФЗ).
- AD-008 (hybrid) — unchanged; transport adapter vendor must support the new recurring operations → affects RFP/contract with vendor.

So the depth of design: **High / Significant** — new financial entity, new lifecycle, cross-cutting impact on contract (TSP + OPKC adapter), compliance (consent = ПДн, revocation), and it's a change to a Critical-route (11/15) initiative. This is not a trivial additive feature.

Now, there's a nuance about where the consent lives. In СБП, the consent is typically held in НСПК (the payer's bank registers the consent in НСПК, and the acquirer/merchant references it via a consent ID/token). The architecture decision here needs to consider: does the consent live in our gateway (as a mirror/copy), in НСПК (source of truth), or both? Given AD-002 (gateway DB is single source of truth for payment state), the natural extension is: **gateway holds the consent registry as the source of truth for the TSP-facing state, with НСПК as the authoritative source for the consent's technical validity** — but this is a decision to surface.

Actually let me be careful. There's an important architectural question: is the consent registered in НСПК (payer's bank) at all, or is this purely a gateway-level concept? In СБП's real "recurring/autopayment" model, there IS a consent/mandate registered in НСПК (or the banks) that enables pull payments. The precise protocol is `[ТРЕБУЕТ ПРОВЕРКИ]` (documentation from НСПК), consistent with the repo's convention.

So my package should:
1. Note the protocol details are `[ТРЕБУЕТ ПРОВЕРКИ]` (external input from НСПК documentation), exactly like the existing solutioning.
2. Design at the level of gateway/contract, with the НСПК protocol abstracted behind the OPKC adapter (consistent with AD-008).

Now let me plan the actual artifacts to create/modify. Following repo conventions:

**Files to create:**
1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md` — the architecture decision (ADR). Contains: context, significance/route, alternatives, decision, consequences, reversibility, acceptance criteria, rollback plan, open questions for human architect. Actually, let me split concerns per repo convention:
   - ADR contains: Date, Status, Owner, Related, Context, Decision, Alternatives Considered, Consequences, Reversibility, References.
   - Acceptance criteria and rollback go... In the existing repo, acceptance criteria are in `docs/nfr.md` (measurable) and gates in `docs/solutioning.md`. The rollback plan is in `docs/solutioning.md` §8. So maybe I should:
   
2. A solutioning doc for the feature: `docs/solutioning-recurrent.md` (or add a section to `docs/solutioning.md`). The repo convention has a single `docs/solutioning.md` with gates, rollback, gaps. But this is a NEW feature layered on top. The cleanest: a new focused document `docs/recurrent/solutioning.md` + `docs/recurrent/nfr.md`? Or follow the existing flat structure.

Let me think about what's the minimal, idiomatic set of files that:
- Follows repo conventions (ADR numbering, spine block format, contract format, NFR table format).
- Covers the 7 deliverables.
- Doesn't break existing files (additive changes only; contract change must be backward-compatible).

I'll propose:

**New files:**
1. `docs/adr/ADR-008-rekurrentnye-spisaniya-po-soglasiyu.md` — the ADR (significance/route + decision + alternatives + consequences + reversibility). This is the core "architectural decision" deliverable (item 1, 3, and 7 partially).
2. `docs/recurrent/solutioning.md` — feature-level solutioning: impact on AD invariants (item 2), flow, consent lifecycle, mapping to components, gates, acceptance criteria + rollback plan (item 6), gaps, open questions (item 7).
3. `docs/recurrent/nfr.md` — measurable NFRs for the feature (item 5). Or append to existing nfr.md with a new section. Hmm.

Actually, let me reconsider. The repo structure is flat and simple. Adding `docs/recurrent/` subdir is a new pattern. But the existing structure has `docs/spec/`, `docs/contracts/`, `docs/rfp/`, `docs/adr/` subdirs. So subdirs are established. A `docs/recurrent/` subdir would be reasonable but maybe overkill. 

Alternative cleaner approach that matches the existing repo's flat top-level docs:
- `docs/adr/ADR-008-rekurrentnye-spisaniya-po-soglasiyu-platelshchika.md` — ADR.
- `docs/spec/consent-state-machine.md` — consent/debit lifecycle spec (mirrors `docs/spec/state-machine.md`).
- Update `docs/contracts/tsp-api.md` — add consent/debit methods (v0.1 additive).
- Update `openapi/tsp-api.yaml` — add consent/debit paths (backward-compatible, version stays 0.1 or bump to 0.2? Since additive-only, keep version but the repo says v0.1 draft; additive optional fields are backward compatible. I'll keep version 0.1 and add new paths + optional fields — no breaking).
- Update `docs/contracts/opkc-adapter.md` — add consent/debit operations (adapter contract expansion).
- New `docs/recurrent/solutioning.md` — the feature-level solutioning that ties it together: significance/route, impact on invariants, acceptance criteria, rollback, open questions.
- Update `docs/nfr.md` — append a section for recurrent NFRs. OR create `docs/recurrent/nfr.md`. 

Hmm, but the task says "Код не пиши" and "кратко перечисли созданные и изменённые файлы". So the deliverable is files.

Let me decide on a clean, coherent file set. I'll aim for minimal but complete:

1. **`docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`** (CREATE) — the ADR. This is the central architectural decision. Covers: Context (business need), significance & route assessment, impact on invariants (summary), Decision, Alternatives, Consequences, Reversibility, References. Also I can put acceptance criteria and rollback here OR in a companion solutioning doc.

2. **`docs/recurrent/solutioning.md`** (CREATE) — feature solutioning: full impact on AD-001..AD-008 (item 2), consent & debit lifecycle, component/flow additions, gates, acceptance criteria (item 6), rollback plan (item 6), gaps & open questions (item 7).

3. **`docs/spec/consent-state-machine.md`** (CREATE) — consent lifecycle spec + debit reference to payment machine (mirrors state-machine.md).

4. **`docs/recurrent/nfr.md`** (CREATE) — measurable NFRs for recurring (item 5). 

Actually, maybe simpler to fold NFR into the solutioning or append to existing nfr.md. But NFR deserves its own measurable table. Let me append to `docs/nfr.md` a new section "§7 Рекуррентные списания" — this keeps all NFRs in one canonical place (the repo's single source for NFR), and the FITNESS constraint `nfr-measurable` pattern checks `docs/nfr.md` for `99,95` (still present). This is cleaner than a second NFR file. But appending to an existing "accepted" file... the repo allows it since NFR is a living doc. Hmm, but the instruction "Принятые файлы решения меняй только тем способом, который принят" — the accepted way to change NFR is additive sections (it already says "Целевые значения — измеримые критерии приёмки... финальные согласуются"). I'll append a new section to nfr.md.

Actually, let me reconsider whether to create a `docs/recurrent/` subdirectory at all. The cleaner approach, most consistent with the existing repo, might be:

- ADR-008 in `docs/adr/`.
- New spec in `docs/spec/consent-state-machine.md`.
- Contract updates: edit `docs/contracts/tsp-api.md`, edit `openapi/tsp-api.yaml`, edit `docs/contracts/opkc-adapter.md`.
- NFR: append section to `docs/nfr.md`.
- Feature solutioning: a single new doc `docs/recurrent/solutioning.md` OR `docs/solutioning-recurrent.md`.

Given the existing docs are all at `docs/` top level except adr/contracts/spec/rfp, I think `docs/recurrent/solutioning.md` (a subdir) is fine and clean, OR I could put it as `docs/recurrent-solutioning.md`. Hmm. Let me look at naming: existing are `docs/solutioning.md`, `docs/nfr.md`. For a feature solutioning, `docs/recurrent/solutioning.md` with its own nfr inside it would be self-contained.

Actually, I'll keep it simpler and more discoverable: create ONE comprehensive feature package doc at `docs/recurrent/solutioning.md` that contains the solutioning (impact, flows, lifecycle, gates, acceptance criteria, rollback, open questions), and put NFR as a dedicated section within it (plus optionally a short pointer append to `docs/nfr.md`). But the task explicitly lists "5. Измеримые NFR" as a separate deliverable — I can make it a clearly-marked section with measurable tables.

Let me settle on this final file set:

**Create:**
1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`
2. `docs/recurrent/solutioning.md` — the feature solutioning (impact on invariants, flows, lifecycle, acceptance criteria, rollback, gaps, open questions). Includes measurable NFR table (or references).

**Modify (additive, non-breaking):**
3. `docs/spec/consent-state-machine.md` (create — this is "modify spec" but really a new file)
4. `openapi/tsp-api.yaml` (add consent/debit paths + schemas; version bump to 0.2.0 to signal additive minor, or keep 0.1 and add. I'll bump `version: 0.2.0` but keep `/v1` paths — additive is backward compatible; but changing version in yaml is fine. Actually the repo's contract doc says "версия пути /v1" and "Добавление опциональных полей — обратно совместимо". The OpenAPI `info.version` 0.1.0 → 0.2.0 reflects a new draft with additive endpoints. I'll do 0.2.0 and note it's backward-compatible additive.)
5. `docs/contracts/tsp-api.md` (add new methods §3.6+ and webhook events; keep v0.1→ bump to v0.2 note? The doc header says "v0.1 draft". I'll update to note additive v0.2 changes but keep the file's core. Actually editing the tsp-api.md header and appending methods is "changing an accepted file" — but it's the accepted way: additive contract changes. I'll add new sections and mark version.)
6. `docs/contracts/opkc-adapter.md` (add consent/debit operations to §3/§4/§5 tables — additive).

**Possibly modify:**
7. `ARCHITECTURE-SPINE.md` — add AD-009 (recurring debits) as a new invariant block with Status: Proposed, and note in Deferred that "автоплатежи" moves out of deferred. Wait — the current spine's solutioning says "Roadmap (вне scope): ... автоплатежи". And ARCHITECTURE-SPINE.md "Deferred" section lists C2C, B2C/B2B, disputes — it does NOT list автоплатежи in the spine Deferred (the spine Deferred lists "Мультивалютность", "C2C", "Диспуты"). The solutioning.md "Roadmap (вне scope)" lists "автоплатежи" (recurring). So this feature pulls "автоплатежи" into scope. I should add an AD-009 block to the spine and update the solutioning roadmap note. But modifying the spine is a delicate operation — the spine is "инварианты". Adding a new proposed invariant AD-009 is the accepted way (like AD-001..AD-007 are all "Proposed" until ratified). I'll add AD-009 as a new block with Status: Proposed (ADR-008), and it will be "действует после ратификации соответствующего ADR" per the spine header convention.

Hmm wait, but should I actually edit ARCHITECTURE-SPINE.md? The task says "Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет." — this is about documenting the impact, not necessarily editing the spine. But "Принятые файлы решения меняй только тем способом, который принят" implies I CAN change accepted files, but only via the accepted way (new ADR + new proposed spine block, not rewriting existing ADs).

I think the right scope is:
- Document the impact (item 2) in the feature solutioning doc — detailed.
- Add AD-009 to the spine as a new Proposed block (the accepted way to extend invariants).
- Add ADR-008 (the accepted way to add a decision).

But I should be careful: editing ARCHITECTURE-SPINE.md is a change to the "accepted decision" file. The convention for changing the spine is: add a new AD block with `Status: Proposed (ADR-XXX)`. That's exactly how AD-001..007 are written. And AD-008 is `[ADOPTED]` referencing ADR-007 Accepted. So adding AD-009 `Status: Proposed (ADR-008)` is consistent.

Let me also consider: should I update `docs/solutioning.md` §1 (roadmap "автоплатежи" is out of scope)? That's a factual correction. I could update the roadmap line. But editing solutioning.md is editing an accepted file. The cleaner approach: don't rewrite solutioning.md; instead the new `docs/recurrent/solutioning.md` supersedes that roadmap note for the recurring scope. But leaving a stale "автоплатежи вне scope" in solutioning.md would be a contradiction. Hmm.

Actually, I think the most defensible approach, given "код не пиши" and "меняй только принятым способом", is:
- **Create** new files (ADR-008, recurrent solutioning, consent state machine).
- **Edit** the contract files (tsp-api.yaml, tsp-api.md, opkc-adapter.md) additively — these are the explicitly-required deliverable (item 4).
- **Edit** ARCHITECTURE-SPINE.md to add AD-009 (Proposed) — the accepted way to record a new invariant.
- **Edit** docs/nfr.md to append a recurrent NFR section.
- Leave `docs/solutioning.md` as-is (it's the parent-level solutioning; the new feature solutioning lives in its own doc). But to avoid the contradiction, I'll note in the recurrent solutioning that it supersedes the "автоплатежи вне scope" roadmap line, and reference it.

Actually, I realize I'm overcomplicating. Let me step back and think about what a solution architect would actually produce and hand over, keeping it tight and high-signal.

The task is essentially: "Produce an architecture package (documents) for the recurring C2B debit feature." The 7 numbered items map to sections of a solutioning/ADR package. The most natural single artifact is an ADR (for the decision) plus a solutioning doc (for impact, NFR, acceptance, rollback, open questions). The contract change is a required concrete edit (OpenAPI yaml + tsp-api.md + opkc-adapter.md).

Given "Код не пиши" and "кратко перечисли созданные и изменённые файлы" — I will:
1. Write ADR-008 (core decision doc).
2. Write `docs/recurrent/solutioning.md` (impact analysis, lifecycle, flows, NFR, acceptance criteria, rollback, open questions).
3. Write `docs/spec/consent-state-machine.md`.
4. Edit `openapi/tsp-api.yaml` (additive endpoints + schemas).
5. Edit `docs/contracts/tsp-api.md` (additive methods + webhooks).
6. Edit `docs/contracts/opkc-adapter.md` (additive operations/events).
7. Edit `ARCHITECTURE-SPINE.md` (add AD-009 Proposed block).
8. Edit `docs/nfr.md` (append recurrent NFR section).

That's a comprehensive, coherent package. But it's a lot of files. Is that over-engineering? The user explicitly asked for a package "чтобы его можно было вынести на архитектурное решение и затем передать исполнителям" and listed 7 distinct deliverables. So multiple files are warranted. But I want to be careful not to over-produce.

Let me reconsider consolidation to reduce file count while keeping completeness and repo-idiomatic structure:

Core decision: ADR-008 (one file).
Feature solutioning incl. impact + NFR + acceptance + rollback + open questions: one file `docs/recurrent/solutioning.md`.
Consent state machine spec: I could fold into the solutioning doc, but the repo has `docs/spec/state-machine.md` as a separate canonical artifact — a separate `docs/spec/consent-state-machine.md` is more consistent. I'll keep it separate.
Contract edits: 3 files (required by item 4).
Spine edit: 1 file (AD-009).
NFR: fold into `docs/recurrent/solutioning.md` OR append to `docs/nfr.md`. I'll append to `docs/nfr.md` (keeps single NFR source) AND also include the NFR summary in solutioning. Actually to avoid duplication, I'll put full measurable NFR in `docs/nfr.md` (appended §7) and reference it from solutioning. That's cleanest and matches "docs/nfr.md — измеримые NFR" as the canonical NFR home.

Wait, but appending to nfr.md means I edit an "accepted" file. That's fine — NFR is a living doc, additive append is the accepted way, and the FITNESS `nfr-measurable` check still passes (99,95 remains).

Final file set (8 files):

Create (4):
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`
- `docs/recurrent/solutioning.md`
- `docs/spec/consent-state-machine.md`

Modify (5):
- `openapi/tsp-api.yaml`
- `docs/contracts/tsp-api.md`
- `docs/contracts/opkc-adapter.md`
- `ARCHITECTURE-SPINE.md`
- `docs/nfr.md`

That's 8 files. Hmm. Let me reduce slightly. Actually, I think this is the right scope. Let me reconsider the `docs/recurrent/` subdir vs top-level. I'll use `docs/recurrent/` to group the feature package cleanly. Actually, wait — let me reconsider: the feature solutioning could just be named `docs/recurrent-solutioning.md` at top level to match `docs/solutioning.md`. But then NFR — the repo's single NFR file is `docs/nfr.md`. I'll append there.

Let me finalize with a slightly leaner structure. Actually, I'll keep it as I listed. Let me also decide: do I need to edit `README.md`? The README lists the structure. I could add a pointer to the new feature docs. That's a nice touch but optional. The README says "Статус: решение подготовлено, ожидает..." — I could add a line noting the recurring feature package. I'll add a brief pointer to README to keep discoverability. Actually, minor — I'll skip README to avoid scope creep, OR add one line. Let me add a one-line note in README's structure + status. Hmm, I'll do a minimal README addition since it documents structure and would otherwise be stale. Actually, I'll keep README edit minimal or skip. Let me skip README — not required, and the task says "кратко перечисли созданные и изменённые файлы", implying a focused set. I'll skip README.

Now, the critical intellectual work: I need to get the domain model right and produce high-quality content. Let me carefully design the recurring C2B debit solution.

## Domain analysis: СБП recurring C2B (subscriptions / autodebit by consent)

**Business need:** ТСП (online cinemas/subscriptions, ЖКХ recurring utility bills, telecom monthly charges) want to charge payers periodically without requiring the payer to scan a QR each time. Payer gives a one-time consent; thereafter the TSP (via the bank's gateway) debits on schedule.

**СБП mechanism (real-world):** НСПК supports "рекуррентные платежи / платежи по подписке" (recurring payments). The precise protocol is `[ТРЕБУЕТ ПРОВЕРКИ]` per the repo's convention (documentation from НСПК by contract). At a conceptual level:

1. **Consent (согласие/mandate):** A standing authorization by the payer to the TSP to initiate debits. Created once with the payer's explicit confirmation in the payer's bank app (the payer approves the consent terms: max amount, period, validity). The consent is registered and gets a token/id (in НСПК or referenced via it).
2. **Debit (списание):** After consent is active, the TSP initiates a debit (with amount within consent limits). НСПК routes to the payer's bank, which executes the pull payment without per-payment confirmation (within consent limits).
3. **Lifecycle:** consent can be revoked by the payer (via their bank app) or by the TSP; it can expire (validity period); it can be suspended (insufficient funds / limit exceeded → debit rejected but consent may stay active).
4. **Limits:** consent carries max amount per debit, max total amount, period (e.g., monthly), validity period (start/end date), frequency cap. These are consent-level controls.

**Mapping to the existing gateway architecture:**

New entity: **Consent (Mandate)** — new source-of-truth entity in the gateway DB, with its own status machine.

New entity/flow: **Recurrent debit** — reuses the existing payment status machine but with a different entry trigger. Instead of `CREATED → QR_ISSUED (wait for QR scan)`, a recurrent debit goes `CREATED (under consent) → PAID (debited by payer's bank via НСПК) → CREDITED → COMPLETED`, with no QR step. Or there's a distinct "DEBIT_REQUESTED" initial state. Actually, the payment machine has `QR_ISSUED` as the "awaiting payer action" state. For a debit, there's no QR, so the flow is `CREATED → PAID` directly (the debit request is submitted to НСПК, and НСПК responds with PAID/REJECTED). So I need to either:
- (a) Add a new state to the payment machine (e.g., `DEBIT_REQUESTED` / reuse `CREATED` with a `paymentType=RECURRENT` discriminator), or
- (b) Model recurrent debits as a separate subtype of payment with a modified flow.

The cleanest: **extend the payment entity with a `paymentType` (ONE_OFF | RECURRENT) and a `consentId` reference.** The recurrent debit shares the same status machine (CREATED → PAID → CREDITED → COMPLETED / FAILED), but the `QR_ISSUED` state is bypassed (not entered) for recurrent payments. This preserves AD-002 (single status machine) and AD-005 (credit only from PAID) unchanged. The "registration in ОПКЦ" step becomes "initiate debit under consent" instead of "create QR".

Actually, this is an important design point for the ADR: **reuse the payment status machine vs. create a separate debit status machine.** The decision: reuse the same machine, add `paymentType` discriminator, `consentId` optional reference; recurrent debits never enter `QR_ISSUED`. This minimizes invariant changes and preserves AD-005. Alternative (separate machine) would duplicate AD-002/AD-003/AD-005 logic — rejected.

Consent status machine (new): 
- `CONSENT_CREATED` (registration requested, awaiting payer confirmation)
- `CONSENT_ACTIVE` (payer confirmed, debits allowed)
- `CONSENT_REVOKED` (payer revoked — terminal)
- `CONSENT_EXPIRED` (validity elapsed — terminal)
- `CONSENT_SUSPENDED` (limit/decline policy — temporary, can return to ACTIVE) — optional
- `CONSENT_FAILED` (registration failed/rejected)

Consent transitions are also atomic (status + outbox + audit), idempotent, and reconciled with НСПК — mirroring AD-002/AD-003/AD-004 for a second entity.

**New TSP API surface (additive, backward compatible):**
- `POST /v1/consents` — create a consent (initiate consent flow). Returns `consentId` + `consentUrl` (link to payer's bank app for confirmation) + `status: CONSENT_CREATED`. Idempotency-Key required.
- `GET /v1/consents/{consentId}` — consent status.
- `POST /v1/consents/{consentId}/revoke` — TSP-initiated revocation.
- `POST /v1/consents/{consentId}/debits` — initiate a recurrent debit under consent. Idempotency-Key required. Returns `paymentId` (reuses payment resource).
- (Optional) `GET /v1/consents/{consentId}/debits` — list debits under consent.

Webhooks (new events):
- `consent.created`, `consent.activated`, `consent.revoked`, `consent.expired`, `consent.suspended`
- Reuse `payment.completed`/`payment.failed` for debit outcomes (the debit is a payment). Maybe add `paymentType` field to payment webhook body (additive optional field).

**OPKC adapter contract additions:**
Sync (core → adapter):
- `registerConsent(reference=consentId, payerToken?, amountLimits, validityPeriod, frequency)` → `ACCEPTED` + `consentOpcId`
- `revokeConsent(reference=consentId)` → `ACCEPTED`
- `initiateDebit(reference=paymentId, consentRef=consentId, amount, purpose?)` → `ACCEPTED` + `debitOpcId` (or `qrId`-like opc reference)
- `getConsentStatus(consentOpcId)` → status
- (reuse `getPaymentStatus` for debit status)

Async (adapter → core):
- `consent.activated`, `consent.revoked`, `consent.expired`, `consent.rejected`
- `debit.paid` (or reuse `payment.paid` with a flag), `debit.rejected`

Idempotency: `reference` for consent and debit operations; `eventId` for events.

**NFR for recurrent:** 
- Consent registration latency (p95 < 1s without НСПК), 
- Debit initiation throughput (adds to TPS; e.g., batch of debits at billing peaks — telecom/ЖКХ run batch billing windows, so burst profile differs: high burst at month-start), 
- Idempotency: 0 duplicate debits (critical — double-charging a subscriber is a top financial risk), 
- Consent revocation propagation latency (payer revokes → debits must stop; SLO p95 < X), 
- Consistency: no debit after consent revoked/expired (hard invariant), 
- Reconciliation: daily consent/debit reconciliation with НСПК, 
- Compliance: consent records = ПДн, explicit consent, revocation rights (152-ФЗ), audit trail.

**Key invariant / risk:** **No debit after consent revocation/expiry** — this is the single most important new invariant (the "зачисление только из PAID" analog for the consent side). A debit executed after the payer revoked consent is a compliance breach + chargeback/regulatory incident. So I need an invariant: a debit can only be initiated/executed if the consent is in `CONSENT_ACTIVE` at the moment of execution, and the amount is within the consent's limits. This becomes AD-009 (or part of it).

**Human architect decisions (item 7):** 
- Does the consent's source of truth live in НСПК (payer's bank) or the gateway? Regulatory scope of consent under 152-ФЗ/161-ФЗ and НСПК rules.
- Consent limit policy (max per-debit, max total, period) — who enforces (gateway vs НСПК vs both), and whether НСПК's consent model matches.
- Whether this feature requires a new НСПК participant role/contract amendment (the vendor's transport adapter must support the recurring operations — extends ADR-007 hybrid, affects RFP scope and vendor contract).
- Payer confirmation UX (bank app flow) — owned by payer's bank, not the acquirer gateway — so the consent flow has a dependency on payer-bank behavior that's outside our control (external dependency).
- Fee/commission model for subscriptions (business).
- Batch billing window handling (ЖКХ/telecom peak loads) — capacity planning decision.
- Regulatory: does 161-ФЗ allow consent-based debits without per-payment authorization? (This is a real question — I should flag it as a human/regulatory decision.)

These are the things I leave to the human architect with reasons.

Now, the significance/route assessment (item 1):
- Significance: High. This is a new financial entity (consent/mandate), a new lifecycle, new contract surface (TSP + OPKC adapter), cross-cutting compliance (consent = ПДн, 152-ФЗ), and a new failure mode (double debit / debit after revocation) with direct financial and regulatory impact. It touches the parent Critical (11/15) initiative.
- Route: This warrants a full ADR + solutioning (deep design), not a one-pager. Reasons: (a) new state machine; (b) new invariant (no debit after revocation) that must be fitness-testable like AD-005; (c) backward-compatible contract evolution; (d) vendor contract impact (ADR-007 hybrid, RFP); (e) external dependency on НСПК protocol (recurring) still `[ТРЕБУЕТ ПРОВЕРКИ]`. So: route = Critical-feature, full design, new ADR-008, extend spine (AD-009), extend contracts, extend NFR, gate at A3 (human decision) before transport implementation.

Let me now also make sure I understand the numbering. Existing ADRs: ADR-001..ADR-007. New = ADR-008. Existing spine ADs: AD-001..AD-008. New = AD-009.

Now let me also decide the consent/debit naming and states carefully, and write the content in Russian (matching the repo's language).

Let me draft the actual content now. I'll write high-quality, dense, repo-idiomatic documents.

Before writing, let me quickly check ADR-002, ADR-003, ADR-006 content for accuracy (I read 001 partially via ARCHITECTURE.md, 004, 005, 007 fully). I have enough. Let me also quickly verify there's no existing "consent"/"рекуррент"/"подпис"/"автоплат" mention that I'm contradicting — the solutioning §1 says "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." And ARCHITECTURE-SPINE.md Deferred lists C2C, B2C/B2B, disputes — NOT автоплатежи. So the spine's Deferred doesn't mention recurring, but solutioning's roadmap does ("автоплатежи"). Good — I'll note this.

Let me also confirm the OpenAPI file currently has no `servers`, `security`, etc. — it's minimal. I'll extend it carefully preserving existing content.

Now let me plan the OpenAPI edit precisely. Current:
- paths: `/v1/payments` (post), `/v1/payments/{paymentId}` (get).
- schemas: PaymentRequest, Payment.

I'll add:
- `POST /v1/consents`
- `GET /v1/consents/{consentId}`
- `POST /v1/consents/{consentId}/revoke`
- `POST /v1/consents/{consentId}/debits`
- (optionally GET debits list — I'll include for completeness? Keep minimal: the debit list is useful for reconciling a subscription. I'll include `GET /v1/consents/{consentId}/debits`.)

New schemas:
- `ConsentRequest`, `Consent`, `DebitRequest` (reuse `Payment` for response? Debit returns a payment). Add `paymentType` and `consentId` optional to PaymentRequest/Payment.

Also I need to add `paymentType` enum to PaymentRequest and Payment (optional, additive — no breaking). And add `consentId` optional.

Let me carefully design the schemas.

```yaml
openapi: 3.0.3
info:
  title: СБП-шлюз — API ТСП
  version: 0.2.0
  description: >
    v0.2 — аддитивное расширение для рекуррентных C2B-списаний по согласию
    плательщика (см. ADR-008). Существующие методы /v1/payments не изменены.
paths:
  /v1/payments:
    post: ...
  /v1/payments/{paymentId}:
    get: ...
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
          description: Согласие зарегистрировано, ожидает подтверждения плательщика
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
      responses:
        '200':
          description: Согласие отозвано (или уже было отозвано)
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Consent'}
  /v1/consents/{consentId}/debits:
    post:
      operationId: initiateDebit
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
            schema: {$ref: '#/components/schemas/DebitRequest'}
      responses:
        '201':
          description: Списание инициировано под согласием
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Payment'}
    get:
      operationId: listDebits
      parameters:
        - {in: path, name: consentId, required: true, schema: {type: string}}
      responses:
        '200':
          description: Список списаний по согласию
          content:
            application/json:
              schema:
                type: object
                properties:
                  items:
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
        paymentType:
          type: string
          enum: [ONE_OFF, RECURRENT]
          default: ONE_OFF
        consentId:
          type: string
          description: Согласие, под которым инициируется рекуррентное списание (только для paymentType=RECURRENT)
    Payment:
      type: object
      required: [paymentId, amount, status]
      properties:
        paymentId: {type: string}
        amount: {type: integer, description: Сумма в копейках}
        status: {...}
        paymentType:
          type: string
          enum: [ONE_OFF, RECURRENT]
        consentId: {type: string}
    ConsentRequest:
      type: object
      required: [tspId, amountLimit, period]
      properties:
        tspId: {type: string}
        payerRef: {type: string, description: Идентификатор плательщика на стороне ТСП (сквозной)}
        amountLimit:
          type: object
          required: [maxPerDebit, currency]
          properties:
            maxPerDebit: {type: integer, description: Максимум за одно списание, в копейках}
            maxTotal: {type: integer, description: Максимум суммарно за период действия, в копейках (опц.)}
            currency: {type: string, enum: [RUB]}
        period: {type: string, description: Периодичность (например P1M), ISO 8601 duration}
        validity:
          type: object
          properties:
            validFrom: {type: string, format: date-time}
            validUntil: {type: string, format: date-time}
        purpose: {type: string}
        webhookUrl: {type: string}
    Consent:
      type: object
      required: [consentId, status]
      properties:
        consentId: {type: string}
        status:
          type: string
          enum: [CONSENT_CREATED, CONSENT_ACTIVE, CONSENT_SUSPENDED, CONSENT_REVOKED, CONSENT_EXPIRED, CONSENT_FAILED]
        consentUrl: {type: string, description: Ссылка для подтверждения плательщиком (только пока CONSENT_CREATED)}
        amountLimit: {$ref: '#/components/schemas/AmountLimit'}
        period: {type: string}
        validFrom: {type: string, format: date-time}
        validUntil: {type: string, format: date-time}
        revokeReason: {type: string}
    DebitRequest:
      type: object
      required: [amount, merchantOrderId]
      properties:
        amount: {type: integer, description: Сумма в копейках}
        merchantOrderId: {type: string}
        purpose: {type: string}
    AmountLimit:
      type: object
      required: [maxPerDebit, currency]
      properties:
        maxPerDebit: {type: integer}
        maxTotal: {type: integer}
        currency: {type: string, enum: [RUB]}
```

That's a clean additive OpenAPI extension. I'll keep the existing `PaymentRequest`/`Payment` and add optional fields (backward compatible: `paymentType` default ONE_OFF, `consentId` optional).

Note: the existing PaymentRequest required is `[amount, merchantOrderId]` (the OpenAPI yaml is a simplified subset of the tsp-api.md). I should preserve that. I'll add `paymentType`/`consentId` as optional.

Now, let me write all the documents. I'll write in Russian, dense, repo-idiomatic. I'll aim for correctness and completeness.

Let me think about the invariant AD-009 text (spine block). Following the spine block format:

```
## AD-009. Рекуррентные списания только по действующему согласию

- Status: Proposed (ADR-008)
- **Binds**: реестр согласий, статусная машина согласия, инициация списания, нотификации НСПК.
- **Prevents**: списание после отзыва/истечения согласия; списание сверх лимита согласия; двойное списание при ретрае.
- **Rule**: Списание инициируется/исполняется только из состояния согласия `CONSENT_ACTIVE`, сумма — в пределах лимитов согласия; повторная доставка запроса/нотификации не создаёт второго списания (fitness-тест: недостижимость списания из `CONSENT_REVOKED`/`CONSENT_EXPIRED`, идемпотентность дебета).
```

That's a good new invariant. It mirrors AD-005 style.

Now let me also consider whether I should add a second invariant about consent being ПДн (compliance), but AD-007 already covers ПДн. I'll fold compliance into AD-009's prevents/rule or into the solutioning. Keep spine minimal: one new AD block.

Now let me write the content. I'll be thorough but not bloated.

Let me also think about the significance/route assessment more concretely, to give a defensible "значимость" score. The parent initiative is Critical (11/15). This feature adds a new financial entity and new failure modes. I'd rate the feature itself as **High (≈ 9–10/15) / маршрут Critical-feature**: requires full ADR + solutioning, new invariant, contract evolution, vendor (RFP) impact, and an external dependency (НСПК recurring protocol). But it does NOT require a new initiative/spine (it stays under the parent C2B-приём spine, AD-009 is a feature-level block). Route: same A0–A5 gates, with a new human decision (A3) for the consent model before transport.

Let me write the documents now. I'll produce them one by one using write_file / edit.

First, the ADR-008. Let me draft carefully.

Actually, I realize I should also double-check: is there a numbering concern with ADR filenames? Existing use `docs/adr/ADR-008-...` — wait, existing go ADR-001..007. New is ADR-008. Filename pattern uses kebab-case slugs. I'll name: `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`.

Let me write all files. I'll start with the ADR, then the spine edit, then solutioning, then consent state machine, then contracts, then NFR.

Let me write the ADR-008 content now.

I want to make sure the ADR covers items 1 (significance/route), 3 (decision + alternatives + consequences + reversibility), and references item 2 (impact) and 7 (open questions). But per repo convention, the ADR is the decision; the solutioning doc carries the detailed impact, NFR, acceptance, rollback, gaps. I'll put:
- ADR-008: Context (incl. significance/route), Decision, Alternatives, Consequences, Reversibility, References. Plus a short "Impact on invariants" summary pointing to solutioning. And "Open questions for human architect" — I'll put the open questions in the solutioning doc §Open questions, and also a brief note in ADR. Actually item 7 ("what remains for human architect") is best in the solutioning doc. But the ADR should note the A3 human decision needed.

Let me write everything now.

For the significance/route, I'll include a concise "Оценка значимости и маршрут" section at the top of the ADR (or in solutioning). I'll put it in the solutioning doc as §1 (since solutioning is where route/significance naturally lives — the existing solutioning.md starts with "Маршрут: Critical (значимость 11/15)"). I'll put a compact version in ADR Context too.

OK, let me write. I'll produce the files.

Let me write ADR-008 first.

For reversibility: The consent feature — adding the consent entity and new endpoints is additive and reversible (feature flag, can be disabled; existing one-off payments unaffected). But once consents are registered and debits executed, the data (consent records, debits) are real financial/ПДн records — reverting means stopping new debits (stop-new via feature flag) but not "un-creating" executed debits (which are normal payments, subject to returns). So: **reversible at the feature level (feature flag stop-new), costly to fully reverse after production debits exist** (consent records are ПДн with retention obligations; executed debits are financial facts). I'll state this precisely.

Let me now write.

Actually, I need to be efficient. Let me write all files in sequence with write_file (for new files) and edit (for existing files). I'll do the new files first, then edits.

Let me write the ADR-008.
I now have a complete picture of the repo: CALM is present only as a methodology skill (no `.architecture.json` models — artifacts are Markdown ADRs + spine + contracts). The accepted way to change a decision here is: **new ADR + new Proposed spine block + additive contract changes**, never rewriting ratified content. Let me verify the `calm` CLI isn't actually required and confirm there are no CALM JSON artifacts I'd be obliged to extend.

  `write_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisa, content="# ADR-008. Рекуррентные C2B-списания по согласию плательщика (СБП-подписки)\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: solution-ar)`

Confirmed: no CALM CLI, no CALM JSON artifacts. The deliverables are markdown ADRs + spine + contracts. The `calm` skill is the methodological guide; its real substance here is the architectural rigor (ADR, invariants, validation mindset), which aligns with what the repo already does.

Now let me write all the files. I'll produce the architecture package.

Let me write in this order:
1. ADR-008 (new)
2. docs/recurrent/solutioning.md (new)
3. docs/spec/consent-state-machine.md (new)
4. openapi/tsp-api.yaml (edit)
5. docs/contracts/tsp-api.md (edit)
6. docs/contracts/opkc-adapter.md (edit)
7. ARCHITECTURE-SPINE.md (edit - add AD-009)
8. docs/nfr.md (edit - append §7)

Let me write the ADR-008 first. I need to be precise and thorough.

Let me draft the full ADR-008 content.
Confirmed: no CALM CLI and no CALM JSON models in the repo — the methodology is applied through the existing Markdown ADR/spine/contract convention. I'll now produce the package. Starting with the core architectural decision (ADR-008).

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now the spine edit — add AD-009. Let me read the exact text around the end of the AD blocks to insert correctly.

The spine ends with AD-008 [ADOPTED], then a "## Deferred" section. I need to insert AD-009 before "## Deferred".

Let me do the edit. I'll insert the AD-009 block after the AD-008 Rule and before "## Deferred".
Now I'll add the new spine invariant AD-009 (Proposed), inserted before the Deferred section, following the exact block format.

  `write_file(content="# Статусная машина согласия (consent) — спецификация переходов\n\n- Status: Draft (для ревью на гейте A1)\n- Owner: solution-architect (пла, file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/spec/consent-state-machine.md")`

Now the consent state machine spec. Let me write it mirroring `docs/spec/state-machine.md`.

I'll write `docs/spec/consent-state-machine.md`.
Now the consent state-machine spec, mirroring the existing `docs/spec/state-machine.md` format.

  `write_file(content="# Solutioning — Рекуррентные C2B-списания по согласию плательщика (СБП-подписки)\n\n- Статус: Draft (пакет на архитектурное решение; гейт A, file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/recurrent/solutioning.md")`

Now the feature solutioning doc `docs/recurrent/solutioning.md` — the comprehensive doc covering items 2, 5, 6, 7. Let me write it.

This doc should cover:
1. Significance and route (summary, referencing ADR-008).
2. Impact on accepted architecture: which invariants (AD-001..AD-008) affected, what changes, what doesn't.
3. Flows (consent flow, debit flow).
4. Component additions.
5. NFR (measurable) — I'll put full NFR here OR reference docs/nfr.md §7. I decided to append to nfr.md and reference. Let me include the NFR table in the solutioning too but keep nfr.md as canonical. Actually to avoid duplication, I'll put the full measurable NFR table in the solutioning doc §NFR, AND append a compact §7 to nfr.md that points to the full table + includes the key measurable targets (since nfr.md is the canonical NFR home and there's a FITNESS rule checking nfr.md contains '99,95'). Hmm.

Actually, let me reconsider. The repo convention: `docs/nfr.md` is the single canonical NFR doc ("Полный набор с измеримыми целями — docs/nfr.md"). The feature NFR should live there. So I'll append §7 to nfr.md with the full measurable table for recurring. Then in the solutioning doc, I'll reference it and include a short summary of the distinctive new NFRs (double-debit=0, revocation propagation, batch burst) so the solutioning is self-contained for the reader.

Let me write the solutioning doc with sections and put the key NFR summary inline + reference nfr.md.

6. Acceptance criteria (gates + testable criteria) and rollback plan.
7. Gaps and open questions (human architect decisions).

Let me write it now. I'll keep it dense and high-signal.
Now the feature solutioning document that ties impact analysis, NFR, acceptance criteria, rollback, and open questions together.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\n  description: >\n    v0.2 — аддитивное расширение для рекуррентных C, file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/openapi/tsp-api.yaml")`

Now the contract edits. First, `openapi/tsp-api.yaml` — the required deliverable (item 4). I'll rewrite it additively. Since it's a small file, I'll rewrite the whole thing with write_file to add the new paths and schemas cleanly, preserving existing paths exactly.

Actually, I should use edit to be precise, but rewriting the whole file is cleaner given the extent. However, write_file with prior-read enforcement: I've already read it. Let me rewrite the whole file with the extended content.

Let me carefully construct the full YAML.
Now the required contract change. I'll extend `openapi/tsp-api.yaml` additively, preserving the existing `/v1/payments` paths exactly.

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/tsp-api.md", old_string="- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)", new_string="- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.2 (аддитивное расширение для рекуррентных списаний, ADR-008; существующие ме)`

Now edit `docs/contracts/tsp-api.md` additively — add new methods §3.6+, webhook events, and update the version note. I'll append new sections and update the header version line.

Let me be surgical. I need to:
1. Update the header version note to mention v0.2 additive.
2. Add §3.6 (consents), §3.7 (revoke), §3.8 (debits), §3.9 (list debits) — actually let me combine into clean subsections.
3. Add webhook events (§5) for consent.*.
4. Update §6 versioning note to mention additive change.

Let me read the exact current text around the places I'll edit. I already have the full content from earlier. Let me do targeted edits.

First, update the header. Current:
```
# Контракт API ТСП (мерчант-API) — v0.1 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
```

I'll change to note v0.2 additive. Actually, let me keep it simple: add a line about v0.2. Let me edit the version line.

Let me do the edits.

Edit 1: header version line.
Edit 2: add new methods after §3.5 (before §4 "Ошибки").
Edit 3: add webhook events in §5.
Edit 4: versioning §6 note.

Let me find exact anchors.

For §3.5, the text ends:
```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`

## 4. Ошибки (RFC 9457, Problem Details)
```

I'll insert new §3.6..§3.9 before "## 4. Ошибки".

For webhooks §5, current events list:
```
События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
```

I'll add consent events after these.

For §6, current:
```
- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.
- Добавление опциональных полей — обратно совместимо, не требует новой версии.
```

I'll add a note about v0.2 additive.

Let me do all edits now.
Now the additive edits to `docs/contracts/tsp-api.md`.

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/tsp-api.md", old_string="# Контракт API ТСП (мерчант-API) — v0.1 draft", new_string="# Контракт API ТСП (мерчант-API) — v0.2 draft (аддитивное расширение рекуррентных списаний)")`

The title still says "v0.1 draft" in the H1. Let me update that too for consistency. Actually, minor. Let me update the H1 title to reflect v0.2.

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/tsp-api.md", new_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n, old_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n)`

Now insert new methods §3.6-3.9 before "## 4. Ошибки".

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/tsp-api.md", new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`

Now add the new error codes for consent (CONSENT_NOT_ACTIVE, CONSENT_LIMIT_EXCEEDED) and the webhook events. Let me also add webhook events and update §6 versioning.

First, add error codes. Current §4 canonical codes line:
```
Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.
```

I'll add `CONSENT_NOT_ACTIVE` (409 or 422?) and `CONSENT_LIMIT_EXCEEDED` (422). Let me add them.

Then webhooks. Then versioning.

Let me do these edits.

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/tsp-api.md", new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/tsp-api.md", new_string="- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.\n- Добавление опциональных полей — , old_string="- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.\n- Добавление опциональных полей — )`

Now update §6 versioning note to mention the v0.2 additive change. Let me find the exact §6 text.

Current §6:
```
## 6. Версионирование и совместимость

- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6 мес.
- Добавление опциональных полей — обратно совместимо, не требует новой версии.
- Deprecation: заголовок `Deprecation` + `Sunset` в ответах старой версии.
```

I'll add a line noting v0.2 is additive.

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/opkc-adapter.md", new_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.2 draft (аддитивное расширение рекуррентных списаний)\n\n- Status: Draft (для ревью , old_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1; основа для RFP вендора)\n- Owner:)`

Now the opkc-adapter.md contract edit — add consent/debit operations to §3 and §4 tables, and add a note to §7/§8 about vendor requirements. Let me do targeted edits.

Current §3 table rows (I have the full content). I'll add new rows after `registerTsp`... actually the table is a markdown table with columns: Метод | Направление смысла | Ключевые поля запроса | Ответ | Таймаут (p99.9).

I'll add rows for `registerConsent`, `revokeConsent`, `initiateDebit`, `getConsentStatus`.

Let me find the exact table text to anchor. The table ends with `getReconciliationReport` row. I'll insert new rows before `getReconciliationReport` or after it. Actually cleaner to add them grouped. Let me add after the `createRefund`/`getRefundStatus` rows and before `getReconciliationReport`. 

Actually simpler: add after the `cancelPaymentLink` row (before `createRefund`), grouped with the payment-related ops. But consents are a distinct group. Let me add after `createPaymentLink` and `getPaymentStatus`... hmm.

Let me just add the 4 new rows right before the `getReconciliationReport` row, with a clear grouping. Actually markdown tables don't have grouping, so I'll just insert 4 rows before `getReconciliationReport`.

The exact text of the table:
```
| `registerTsp` | регистрация/активация ТСП в ОПКЦ | `tspId` (ядро), реквизиты ТСП, `reference` | `jobId`, статус `ACCEPTED` (результат — событием) | 5 c |
| `createPaymentLink` | создание QR/ссылки | `reference` (= `paymentId` ядра), `amount` (копейки), `currency`, `qrType`, `ttlSeconds?`, `purpose?`, `redirectUrl?` | `qrId`, `qrUrl`, `expiresAt` | 3 c |
| `getPaymentStatus` | запрос статуса по `qrId` (сверка/опрос) | `qrId` | статус ОПКЦ: `PAID` / `PENDING` / `REJECTED` / `EXPIRED` / `UNKNOWN`, `paidAmount?`, `paidAt?` | 3 c |
| `cancelPaymentLink` | закрытие/отмена ссылки (TTL, отмена ТСП) | `qrId`, `reason` | `CANCELLED` | 3 c |
| `createRefund` | регистрация возврата в ОПКЦ | `reference` (= `refundId` ядра), `qrId`, `amount` | `ACCEPTED` (результат — событием) | 5 c |
| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |
| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |
```

I'll insert after `getRefundStatus` row, before `getReconciliationReport`.

New rows:
```
| `registerConsent` | регистрация согласия в ОПКЦ | `reference` (= `consentId` ядра), `payerToken?`, `amountLimit`, `period`, `validity` | `consentOpcId`, `consentUrl`, статус `ACCEPTED` (результат — событием) | 5 c |
| `revokeConsent` | отзыв согласия | `reference` (= `consentId`), `reason` | `ACCEPTED` (результат — событием) | 5 c |
| `initiateDebit` | инициация списания под согласием | `reference` (= `paymentId` ядра), `consentRef` (= `consentId`), `amount`, `purpose?` | `debitOpcId`, статус `ACCEPTED` (результат — событием) | 3 c |
| `getConsentStatus` | статус согласия (сверка/опрос) | `consentOpcId` | `ACTIVE` / `PENDING_CONFIRM` / `REVOKED` / `EXPIRED` / `REJECTED` / `UNKNOWN` | 3 c |
```

And §4 events table — add consent/debit events. Current §4 table:
```
| `payment.paid` | ... |
| `payment.rejected` | ... |
| `payment.expired` | ... |
| `tsp.registered` | ... |
| `tsp.rejected` | ... |
| `refund.confirmed` | ... |
| `refund.rejected` | ... |
| `transport.unavailable` | ... |
```

I'll add after `payment.expired` (or group at end before transport.unavailable). Let me add:
```
| `consent.activated` | согласие подтверждено | `consentRef` (= `consentId`), `consentOpcId` |
| `consent.rejected` | согласие отклонено | `consentRef`, `reasonCode`, `reasonText` |
| `consent.revoked` | согласие отозвано (плательщик) | `consentRef`, `reason` |
| `consent.expired` | согласие истекло | `consentRef` |
| `debit.paid` | списание подтверждено | `debitOpcId`, `reference` (= `paymentId`), `amount`, `paidAt` |
| `debit.rejected` | списание отклонено | `reference`, `reasonCode`, `reasonText` |
```

And add a note in §5 idempotency about consent/debit references (already §5 says "Ядро передаёт reference... Адаптер обязан обеспечить идемпотентность... не создаёт дубль в ОПКЦ"). I can add a line mentioning consent/debit reference. Actually §5 already covers it generically. I'll add a note to §8 vendor requirements about recurring support.

Let me also update the header note of opkc-adapter.md to mention v0.2 (recurrent extension). The header currently says "v0.1 draft". I'll bump to v0.2 with additive note.

Let me do these edits.

First header.
Now the OPKC adapter contract — additive operations, events, and vendor requirements.

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/opkc-adapter.md", new_string="| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |\n| `registerConsent` | регистрация, old_string="| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |\n| `getReconciliationReport` | вып)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/opkc-adapter.md", new_string="| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |\n| `refund.rejected` | возв, old_string="| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |\n| `refund.rejected` | возв)`

Now add the events to §4. Current §4 table:
```
| `payment.paid` | платёж подтверждён ОПКЦ | `qrId`, `reference` (= `paymentId`), `amount`, `paidAt` |
| `payment.rejected` | платёж отклонён | `qrId`, `reference`, `reasonCode` (нормализованный), `reasonText` |
| `payment.expired` | ссылка истекла по TTL | `qrId`, `reference` |
| `tsp.registered` | ТСП активирован в ОПКЦ | `reference` (= `tspId` ядра) |
| `tsp.rejected` | ТСП отклонён ОПКЦ | `reference`, `reasonCode`, `reasonText` |
| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |
| `refund.rejected` | возврат отклонён | `refundRef`, `reasonCode`, `reasonText` |
| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |
```

I'll insert consent/debit events before `transport.unavailable`.

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/opkc-adapter.md", new_string="Статусные модели ОПКЦ (`PAID`, `REJECTED`, `EXPIRED`, `CONFIRMED`, `ACTIVE`, `PENDING_CONFIRM`, `REVOKED`) — **нормализованные адаптером** , old_string="Статусные модели ОПКЦ (`PAID`, `REJECTED`, `EXPIRED`, `CONFIRMED`) — **нормализованные адаптером** из протокола НСПК; ядро не зависит от ко)`

Now add a note to §8 vendor requirements about recurring support. Current §8 list:
```
## 8. Требования к вендору (для RFP)

1. Реализует настоящий контракт поверх протокола НСПК; нормализует статусы/ошибки.
2. Сертификаты ФСТЭК/соответствие требованиям НСПК; СКЗИ/HSM (ADR-003, ADR-006).
3. Тестовый контур НСПК: возможность гонять сценарии (paid/rejected/expired, повторы) — для тестов ядра.
4. Идемпотентность мутирующих операций по `reference` (§5) — **обязательно**.
5. SLA, поддержка, референсы в банках сопоставимого масштаба.
6. Эксплуатация: метрики, алерты, документация runbook.
```

I'll add a new item 7 (or extend item 3) about recurring. Let me add item 7.

Also the status model note after §3 table says "Статусные модели ОПКЦ (PAID, REJECTED, EXPIRED, CONFIRMED) — нормализованные...". I should add consent statuses there too. Let me update that line to include consent statuses.

Let me do two edits: (1) update the status-model note line; (2) add vendor requirement item.

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/contracts/opkc-adapter.md", new_string="4. Идемпотентность мутирующих операций по `reference` (§5) — **обязательно** (включая `registerConsent`, `revokeConsent`, `initiateDebit`)., old_string="4. Идемпотентность мутирующих операций по `reference` (§5) — **обязательно**.\n5. SLA, поддержка, референсы в банках сопоставимого масштаба)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/nfr.md", new_string="## 7. Рекуррентные C2B-списания (согласия и дебеты)\n\nЦелевые значения — измеримые критерии приёмки на A4/A5 для ADR-008 (AD-009). Baselin, old_string="## Зависимости (внешние входы для NFR)")`

Now append §7 to docs/nfr.md — the measurable NFRs for recurring. Let me read the current end of nfr.md to anchor. I already have the full content. The doc ends with:

```
## Зависимости (внешние входы для NFR)

- Регламенты НСПК: таймауты, сроки уведомлений, требования к доступности [ТРЕБУЕТ ПРОВЕРКИ — из документации НСПК].
- SLA АБС на зачисление и списание (согласуется с владельцем АБС).
- Требования ЦБ к защите информации при переводах (номер Положения — уточнить у ИБ) [ТРЕБУЕТ ПРОВЕРКИ].
```

I'll append §7 (recurrent) before the "## Зависимости" section, or after it? The "Зависимости" is a closing section. I'll insert §7 before "## Зависимости".

Actually cleaner: insert §7 as a new numbered section after §6 (Наблюдаемость) and before "## Зависимости".

Let me do the edit.
Now append the measurable NFRs for the recurring feature to `docs/nfr.md`.

  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wgmujp6/ws && python3 -c \"import yaml,sys; yam, description="Проверка валидности YAML и fitness-паттернов")`

Now let me verify the OpenAPI YAML is valid (syntactically). Let me run a quick YAML parse check. Since there's no node/yaml validator necessarily, I can use python to check YAML validity. Let me also verify the FITNESS constraints still pass conceptually (nfr.md contains '99,95' — yes, it's still there in §1).

Let me validate the YAML with python3 yaml, and also do a quick consistency check across files.

Actually, let me run a quick check:
1. YAML validity of openapi/tsp-api.yaml.
2. Confirm nfr.md still contains "99,95".
3. Confirm the spine has no TODO/TBD/XXX.

Let me also double check the ADR-008 filename referenced in solutioning: I wrote "docs/adr/ADR-008-..." with ellipsis in one reference — let me make it exact to avoid broken reference. Actually in solutioning.md §1 I wrote "Подробно — `docs/adr/ADR-008-...`." That's a bit sloppy. Let me fix it to the exact filename.

Let me run the YAML check and grep for the "99,95" and fix the ellipsis reference.
Let me validate the YAML and run the repo's own fitness-style checks (the `nfr-measurable` pattern and spine lint).

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/recurrent/solutioning.md", new_string="Гейт A3 (человеческое решение по модели согласия) обязателен **до** реализации транспорта (аналог ADR-007). Подробно — `docs/adr/ADR-008-re, old_string="Гейт A3 (человеческое решение по модели согласия) обязателен **до** реализации транспорта (аналог ADR-007). Подробно — `docs/adr/ADR-008-..)`

YAML is valid, nfr.md still contains '99,95' (2 occurrences, so the fitness `nfr-measurable` check still passes), spine has no TODO/TBD/XXX.

Now fix the ellipsis reference in solutioning.md. Let me read the exact line.

Actually the reference is "Подробно — `docs/adr/ADR-008-...`." Let me fix it to the full filename.

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/solutioning.md", new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты, **рекуррентные сп, old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop)`

Now let me also update the parent `docs/solutioning.md` roadmap line to reflect that "автоплатежи" is now being pulled into scope — but I said I'd leave the parent solutioning alone and just note the supersession in the child doc. Actually, the child doc says "Заменяет строку «автоплатежи — вне scope»". But the parent solutioning.md still literally says "Roadmap (вне scope): ... автоплатежи." Leaving it stale creates a contradiction that a reviewer would flag.

The instruction: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The parent solutioning.md's §1 roadmap line is a factual scope statement. The accepted way to change scope is to update the roadmap. But it's a minor one-line change. However, I'm cautious about editing the parent solutioning (it's the parent initiative's accepted solutioning). 

Actually, the cleanest and most honest approach: update the parent `docs/solutioning.md` §1 roadmap line to point to the new ADR-008 (i.e., "автоплатежи" moved from roadmap to scope via ADR-008). This is a factual, additive correction and prevents contradiction. It's the "accepted way" — I'm not rewriting the design, just updating the roadmap reference.

Let me find the exact line in docs/solutioning.md:
"Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

I'll change "автоплатежи" to be pulled into scope. Let me update to:
"Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты, рекуррентные списания по согласию (ADR-008, `docs/recurrent/solutioning.md`). Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты."

This is a minimal, honest correction. Let me do it.

Actually, wait — is editing the parent solutioning "changing an accepted decision file in an unaccepted way"? The task explicitly asks me to document "влияние на принятую архитектуру" and prepare a package "поверх принятого решения". Pulling a roadmap item into scope is exactly the kind of change this package represents. Updating the roadmap line is correct and expected. And it's a one-line factual update, not a rewrite. I'll do it.

Let me also consider: the README says "Статус: решение подготовлено, ожидает человеческого решения A3..." — I could add a line noting the recurring package. Optional. I'll add a brief note to README structure/status for discoverability, since it documents the repo structure and would otherwise be incomplete. Actually, let me keep scope tight but add a minimal, accurate README pointer since README lists key documents and would be stale. I'll add one line to README's "Ключевые документы" or structure.

Hmm, let me weigh. The task says "кратко перечисли созданные и изменённые файлы" — implying I should be clear about what I changed. Adding README is a reasonable small addition but not strictly required. I'll add a concise pointer in README to keep it accurate, since leaving README stale (it lists the structure and status) would be a minor inconsistency. Actually, I'll do a minimal README update: add the new files to the structure listing and a status note. Keep it short.

Let me first do the solutioning.md roadmap correction, then the README.

Let me do the solutioning.md edit.
I'll correct the parent solutioning's roadmap line so it no longer contradicts the new scope (this is a factual, additive scope update — the accepted way to record the change).

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/README.md", new_string="```\nARCHITECTURE-SPINE.md        инварианты AD-001..AD-009\ndocs/\n  solutioning.md             полный дизайн: компоненты, потоки, гейты, , old_string="```\nARCHITECTURE-SPINE.md        инварианты AD-001..AD-008\ndocs/\n  solutioning.md             полный дизайн: компоненты, потоки, гейты, )`

Now update README.md briefly to reflect the new package. Let me read the current README structure section and status, then add pointers.

Current README structure section:
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

I'll update: "инварианты AD-001..AD-009", add "recurrent/solutioning.md", "spec/consent-state-machine.md", "adr/ADR-001..008.md", update tsp-api/opkc-adapter to v0.2.

Let me do a targeted edit of the structure block and add a one-line note in the status section.

Actually, let me keep it minimal but accurate. I'll update the structure block and add a pointer line about the recurring package in the status/notes.

Let me edit the structure block.
Finally, a minimal README update so the repo map stays accurate.

  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wgmujp6/ws && git status --short && echo \"---\, description="Проверка созданных и изменённых файлов")`

Now let me do a final review. Let me verify the git status to see all changed/created files, and do a quick sanity check on the whole set.

Let me run git status and git diff --stat.
Let me review the final state of changes.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/rfp/vendor-rfp.md")`

Everything is in place. Let me do a final consistency review of the ADR-008 and the new files to make sure there are no errors. Let me quickly verify the ADR-008 content is complete and correct, and that all cross-references are valid.

Actually, I've reviewed all files as I wrote them. Let me do a final self-check on a couple of potential issues:

1. In ADR-008, I referenced "`docs/rfp/vendor-rfp.md`" for the RFP extension — but I did NOT actually edit vendor-rfp.md. I only noted in solutioning.md and opkc-adapter.md that RFP needs extension. That's fine — I'm flagging it as an impact, not claiming I edited it. But the ADR decision item 6 says "это расширяет RFP (см. docs/rfp/vendor-rfp.md)". Since I didn't edit vendor-rfp.md, this could be read as implying the RFP already has the content. Let me soften: it's fine as a pointer, but to be safe I should note it's a recommended follow-up edit, not done. Actually, the solutioning.md §4 says "RFP вендора (docs/rfp/vendor-rfp.md): добавить требование..." — "добавить" = "to be added", which is a recommendation, not a claim I did it. That's honest.

But in ADR-008 item 6, "Вендорский адаптер (ADR-007) обязан поддержать рекуррентные операции — это расширяет RFP (см. `docs/rfp/vendor-rfp.md`)." — "расширяет RFP" is a statement of impact, and "см." points to the RFP doc where it would be added. This is acceptable. I could optionally edit vendor-rfp.md to add the requirement. Should I?

The task item 4 is specifically about `openapi/tsp-api.yaml` contract changes. The opkc-adapter and rfp are secondary. I've already extended opkc-adapter. The vendor-rfp.md is a natural place to add the recurring requirement, but it's arguably beyond the core ask. However, since I've stated the RFP needs extension in multiple places, and the ADR-007 (hybrid) makes the vendor contract a real dependency, adding a concise requirement line to vendor-rfp.md would make the package complete and self-consistent.

Let me check vendor-rfp.md to see if a quick additive edit is warranted. I haven't read it yet. Let me read it and decide.

Actually, given time and scope, and that I've already clearly flagged the RFP extension as a required follow-up (in solutioning §4 and opkc-adapter §8 item 7 which is actually the concrete requirement), I think it's acceptable. The opkc-adapter §8 item 7 IS the vendor requirement, and solutioning §4 explicitly says "добавить требование... (расширение RFP)". 

But to be thorough and avoid a dangling reference ("см. docs/rfp/vendor-rfp.md" implies it's there), let me read vendor-rfp.md and add a concise recurring requirement. This makes the package coherent.

Let me read it.
Let me read the vendor RFP doc to decide whether a brief additive requirement is warranted, since I've referenced it as the place where the recurring requirement lands.

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/rfp/vendor-rfp.md", new_string="- **Методы** (§3): `registerTsp`, `createPaymentLink`, `getPaymentStatus`, `cancelPaymentLink`, `createRefund`, `getRefundStatus`, `registe, old_string="- **Методы** (§3): `registerTsp`, `createPaymentLink`, `getPaymentStatus`, `cancelPaymentLink`, `createRefund`, `getRefundStatus`, `getReco)`

The vendor-rfp.md is comprehensive. I should make a minimal additive edit to reflect the recurring requirement, so the package is coherent (I referenced "это расширяет RFP" in ADR-008 and solutioning). The cleanest minimal edits:

1. §1 scope item 3 → add recurring operations; or add a new scope item about consent/debit support.
2. §4 technical requirements — mention the new methods/events.
3. §5 POC scenarios — add a consent/debit scenario.

Actually, to keep it tight and avoid over-editing, I'll make two minimal additive edits:
- §1 scope: add item about "Рекуррентные операции (согласия и списания)" — extend item 3 or add item.
- §5 POC: add P9 scenario for recurring (registerConsent → consent.activated → initiateDebit → debit.paid; and consent.revoked stops debit).

Also update §4 methods/events lists to mention the new ops. Let me do a focused edit.

Actually, given the task's core deliverable (item 4) is the OpenAPI contract, and I've already extended opkc-adapter (which is the contract the vendor implements) and documented the RFP requirement in solutioning §4 + opkc-adapter §8 item 7, editing vendor-rfp.md is a nice-to-have for completeness. I'll do a concise additive edit: update §4 (methods/events lists) and §5 (add a POC scenario), plus a scope note. Keep it minimal.

Let me do:
Edit 1: §4 methods line — add `registerConsent`, `revokeConsent`, `initiateDebit`, `getConsentStatus` and events count update.
Edit 2: §5 add P9.

Let me do edit 1 first. The §4 lines:
```
- **Методы** (§3): `registerTsp`, `createPaymentLink`, `getPaymentStatus`, `cancelPaymentLink`, `createRefund`, `getRefundStatus`, `getReconciliationReport` — сигнатуры, таймауты, нормализованные ответы.
- **События** (§4): все 8 типов с `eventId`; at-least-once; устойчивость к поздним/повторным событиям.
```

Update to include new methods and "все типы (включая consent.*/debit.*)".

Edit 2: §5 POC add P9.

Let me do these.
The RFP references the adapter contract directly, so I'll make a minimal additive update there too so the recurring requirement is reflected end-to-end.

  `edit(file_path="<HARNESS>/runs-clean/cells/wgmujp6/ws/docs/rfp/vendor-rfp.md", new_string="| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |\n| P9 | **Ре, old_string="| P8 | Двойная доставка события (повтор `eventId`) | ядро дедуплицирует; вендор подтверждает, что дубль возможен и это норма |")`
  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wgmujp6/ws && echo \"== new files ==\" && git s, description="Финальная проверка согласованности пакета")`

All changes are complete. Let me do a final verification of the full git diff to ensure no mistakes, and confirm the whole set is coherent.

Let me run a final git status and check the new ADR file reads correctly (quick re-read of the ADR header and a couple key spots). Actually I've already verified content as I wrote. Let me just do a final git status to list everything, then write my summary.

Let me verify the final list and provide a concise summary to the user.

Actually, let me quickly double-check one thing: the FITNESS constraint in CONSTRAINTS.yaml `adr-no-placeholders` checks `docs/adr/*.md` must NOT contain `<!--`. My new ADR-008 does not contain `<!--` (I used markdown, no HTML comments). Good.

Also `abs-credit-only-from-paid` checks ADR-005 for 'только из состояния `PAID`' — I didn't touch ADR-005. Good.

Also the `adr-set-complete` checks ADR-001 exists — unchanged. Good.

Let me do a final verification with a quick grep that no `<!--` in new ADR and the new files are all consistent.


Everything is consistent. The package is complete. Let me write a concise summary in Russian, listing created and changed files and the key decisions.

I should provide the final answer summarizing:
- What I produced (the 7 deliverables mapped to files).
- Created files vs modified files.
- Key architecture decision highlights.
- What remains for the human architect.
- Verification done (YAML valid, fitness patterns pass).

Keep it concise but complete, in Russian (matching the user's language).

Let me structure the final response.
Готово. Пакет архитектурного решения по рекуррентным C2B-списаниям подготовлен поверх принятого решения, без ломки существующих потребителей и без правки ратифицированных инвариантов.

## Созданные файлы

| Файл | Что закрывает |
|---|---|
| `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md` | Оценка значимости/маршрута, решение, альтернативы, последствия, обратимость |
| `docs/recurrent/solutioning.md` | Влияние на AD-001…AD-008, потоки, NFR, критерии приёмки, план отката, gaps, «что остаётся человеку» |
| `docs/spec/consent-state-machine.md` | Статусная машина согласия + guard-инварианты |

## Изменённые файлы (все аддитивно, принятым в репозитории способом)

| Файл | Суть изменения |
|---|---|
| `ARCHITECTURE-SPINE.md` | Добавлен новый инвариант **AD-009** (Status: Proposed, ADR-008) |
| `openapi/tsp-api.yaml` | Новые пути `/v1/consents*` + опциональные `paymentType`/`consentId`; `version: 0.2.0`, существующие `/v1/payments` не тронуты |
| `docs/contracts/tsp-api.md` | Методы §3.6–3.10, события `consent.*`, новые коды ошибок, версионирование v0.2 |
| `docs/contracts/opkc-adapter.md` | Операции `registerConsent/revokeConsent/initiateDebit/getConsentStatus`, события `consent.*`/`debit.*`, требование к вендору |
| `docs/rfp/vendor-rfp.md` | Методы/события рекуррента + POC-сценарий P9 |
| `docs/nfr.md` | §7 — измеримые NFR для подписок |
| `docs/solutioning.md` | Roadmap: «автоплатежи» перенесено из вне-scope в scope (ADR-008) |
| `README.md` | Карта структуры приведена в соответствие |

## Ключевые архитектурные решения

- **Рекуррентное списание — это тот же платёж** (`paymentType=RECURRENT`), а не новая сущность: машина `CREATED → PAID → CREDITED → COMPLETED` переиспользуется, `QR_ISSUED` пропускается. Это сохраняет **AD-002** и **AD-005** без изменений.
- **Согласие (Consent)** — новый второй источник истины со своей статусной машиной (`CONSENT_CREATED → ACTIVE`, терминальные `REVOKED/EXPIRED/FAILED` + `SUSPENDED`).
- **Новый инвариант AD-009**: списание только из `CONSENT_ACTIVE`, в пределах лимитов, с идемпотентностью дебета — аналог AD-005 для подписок.
- Отклонены: отдельная машина «списания», согласия «только в НСПК», «очередь отложенных QR».

## Что остаётся на человека-архитектора (обязательно, гейт A3)

1. Где источник истины согласия (шлюз / НСПК / оба) — зависит от протокола НСПК (`[ТРЕБУЕТ ПРОВЕРКИ]`).
2. Точка enforcement лимитов и модель частичного отказа (`debit.rejected` ≠ отзыв).
3. Разграничение с банком плательщика (подтверждение/отзыв — внешняя зависимость, не контролируется нашим контуром).
4. Batch-окна нагрузки (ЖКХ/связь) — capacity и приоритеты очередей.
5. Правовой вердикт по 161-ФЗ/152-ФЗ и тарифной модели.
6. Формальная ратификация ADR-008/AD-009.

## Проверки

- `openapi/tsp-api.yaml` — валидный YAML (`yaml.safe_load` OK).
- Fitness-паттерны репо не нарушены: `99,95` в `docs/nfr.md` сохранён; spine без `TODO/TBD/XXX`; новые ADR без HTML-комментариев.
- Код не писал; изменения — только архитектурные артефакты Markdown/YAML.

До закрытия пунктов §9 пакет готов к гейту A1 (Spec), но **не** к реализации транспорта — как и задумано репозиторием.
