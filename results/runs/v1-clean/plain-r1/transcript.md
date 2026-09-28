<!-- источник: <HARNESS>/runs-clean/cells/wh4hwzh/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-clean-cells-wh4hwzh-ws/chats/1075396e-b243-4dfe-ac23-89588a114cab.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/.arch-handoff/RUBRIC.yaml")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/.arch-handoff/ARCHITECTURE.md")`

Let me start by understanding the repository structure and the accepted solution. This is a significant architecture task. I need to read the key files first.

Let me begin by exploring the repository structure and reading the key files.

The user is asking in Russian, so I should respond in Russian.

Let me first read the key files:
- ARCHITECTURE-SPINE.md
- .arch-handoff/ files (TASK.md, ARCHITECTURE.md, CONSTRAINTS.yaml, RUBRIC.yaml, MANIFEST.json, ADR-001-outbox.md)
- docs/ (nfr.md, solutioning.md, adr/, contracts/, spec/)
- openapi/tsp-api.yaml

Let me also check for methodological skills/tools that may be installed in the project.

Let me start exploring.
Начну с изучения принятого решения и правил репозитория, прежде чем готовить архитектурный пакет. Соберу ключевые файлы параллельно.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/openapi/tsp-api.yaml")`
  `glob(pattern="docs/**/*")`
  `glob(pattern="**/*.{md,yaml,yml,json}")`

Let me read more files: docs/solutioning.md, docs/nfr.md, the ADRs, contracts, spec, and openapi/tsp-api.yaml. Let me also check for methodological skills/tools installed in the project.

Let me explore the docs directory structure and read key files.
Изучаю документы решения, NFR, контракты и статусную машину. Параллельно проверю, есть ли в проекте методические навыки/инструменты.

  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/rfp/vendor-rfp.md")`

Let me read the remaining key files: the contracts (tsp-api.md, opkc-adapter.md), state-machine.md, vendor-rfp.md, README.md, and the remaining ADRs (003, 004, 005, 006, 007). Also let me check if there are any methodological skills installed (like superpowers, openspec, bmad). The repo name mentions "OpenSpec_BMAD_Superpowers" — these are likely methodology tools. Let me check for directories like .claude, .cursor, skills, openspec, etc.

Let me read the remaining important files.
Читаю контракты, статусную машину, оставшиеся ADR и README, а также проверяю наличие методических инструментов (OpenSpec/Superpowers/BMAD).

  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/adr/ADR-005-integraciya-s-abs-zach)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/adr/ADR-002-model-konsistentnosti-)`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/adr/ADR-006-trust.md")`

I have a good understanding now. Let me read the remaining ADRs (003, 004, 005, 006, 007) to fully understand the decisions, especially ADR-005 (refunds as saga) and ADR-007 (strategy), and check whether there's any methodology (OpenSpec, Superpowers, BMAD) installed. Let me check for skill/tool directories.

Let me read the remaining ADRs and check for methodology directories.
Читаю оставшиеся ADR и проверяю наличие методических инструментов в репозитории.

  `run_shell_command(command="ls -la <HARNESS>/runs-clean/cells/wh4hwzh/ws/ 2>/dev/null; echo '---DOT DIRS-, description="List root and hidden directories")`
  `run_shell_command(command="find <REPO> -maxdepth 4 -type d \\( -iname '*skill*' -o -iname '*superpower*' -o -i, description="Find methodology/skill directories")`

Now I have a complete picture of the repository. Let me check if there are methodological skills/tools installed (OpenSpec, Superpowers, BMAD). The repo name mentions these. Let me check for directories.

Let me check for any methodology directories or config files (like `.openspec/`, `.superpowers/`, `superpowers/`, `bmad/`, `.qwen/skills/`, etc.).
Проверяю наличие установленных методических инструментов (OpenSpec / Superpowers / BMAD) и скрытых каталогов навыков.

  `run_shell_command(command="for d in bmad-r1 bmad-r2 superpowers-r1 superpowers-r2 openspec-r1 openspec-r2; do echo \"=== $d ===\"; find \"<HOME>/Загрузки/Qwen_Co, description="List methodology frame contents")`

There are methodology directories in the parent. These are `frames/raw` — likely reference frames from Superpowers, BMAD, OpenSpec methodologies. The user said "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." (Methodological skills and tools may be installed in the project — use them as intended.)

Let me check if there are actual installed skills/commands accessible. The available skills listed in system-reminder are the bundled skills (agent-delegation, batch, etc.), none of which are specifically "solution architect" or "ADR" or "architecture" skills. But there might be BMAD/Superpowers/OpenSpec methodology content in `frames/raw`.

Let me look at what's in these frames/raw directories to understand the methodologies. Actually, these are the raw frames of the methodology. The `live-tui/frames/raw` directories contain methodology documentation. Let me explore what's there, specifically for things like "solution architect", "ADR", "architecture decision", "sol-arch", "architecture" workflows.

Actually, let me be careful. The task is essentially a solution architecture task. The repository itself is a "solution" produced by a methodology (the BMAD "sol-arch" flow, given the naming "solutioning.md", "solution-architect", "Critical route" 11/15 significance, gates A0-A5). This is clearly BMAD's Solution Architect / epic architecture methodology.

Let me explore the frames/raw to understand what methodology conventions are used, so I can follow them correctly. Specifically the naming: "solutioning.md", "ARCHITECTURE-SPINE.md" (AD-001...AD-008), "ADR" numbering, "гейты A0–A5", "Critical (значимость 11/15)", "NFR". This looks like a specific methodology.

Let me look at what's in the frames to understand the expected deliverable format for a "change package" on top of an accepted solution. The key question: what should the architecture change package look like? The user explicitly listed 7 deliverables.

Let me check the frames/raw directories for relevant methodology docs (e.g., sol-arch, change, ADR, spine).
Изучаю методические материалы (BMAD/Superpowers/OpenSpec) — нужно понять принятый в репозитории формат пакета изменения решения.

  `write_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/adr/ADR-008-rekurrentnye-c2b-plate, content="# ADR-008. Рекуррентные C2B-платежи СБП: подписки по согласию плательщика\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: solution-arch)`

These are just recording frames (terminal session captures). They're not methodology documents in the sense of instructions — they're the raw TUI frames of previous runs. These represent previous attempts/recordings. They don't contain "skills" per se.

The important thing: the user's instructions are clear. The task is to prepare an architecture change package for the recurrent C2B debit (subscription payments) feature. The 7 deliverables are listed. I should follow the repo's conventions (which I now understand well: ADR format, ARCHITECTURE-SPINE.md AD-XXX invariants, solutioning.md, nfr.md, contracts, state-machine.md, openapi yaml).

The user said "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." (Change accepted decision files only in the way accepted in this repository.)

Let me understand the repo conventions for how to modify:
1. ARCHITECTURE-SPINE.md — has AD-001..AD-008 with Status: Proposed/[ADOPTED]. New invariants would be AD-009+ with Status: Proposed (to be ratified by ADR).
2. docs/adr/ADR-00X.md — ADR format with Context/Decision/Alternatives/Consequences/Reversibility/References.
3. docs/solutioning.md — the full design.
4. docs/nfr.md — measurable NFRs.
5. docs/contracts/tsp-api.md — merchant API contract.
6. docs/contracts/opkc-adapter.md — OPKC adapter contract.
7. docs/spec/state-machine.md — state machine.
8. openapi/tsp-api.yaml — OpenAPI spec.

The change: recurrent C2B debits (subscriptions in СБП) with payer consent. Currently each payment requires QR + client action. Now: recurring subscription debits by consent.

Key domain knowledge about СБП recurring payments (рекуррентные платежи в СБП):

In СБП, the recurring payment mechanism is based on the payer's consent (согласие плательщика). The flow:
- Merchant (ТСП) requests recurring payment consent from payer.
- Payer gives consent in their bank app (via QR/link similar to a payment, but it's a consent for recurring debits).
- After consent, the merchant can initiate recurring debits (списания) without the payer's active participation (no QR each time).
- The consent has: merchant, payer, amount limit (max amount per debit), frequency limit (max debits per period), validity period.

In the НСПК СБП spec, this is the "автоплатежи" / рекуррентные платежи / подписки. The mechanism involves "согласие на автоплатеж" (subscription consent).

The СБП C2B recurring payment (подписка) involves:
1. ТСП initiates a subscription/consent request.
2. Payer consents (QR / deep link to their bank app).
3. Consent is registered in НСПК.
4. ТСП initiates recurring debit requests against the consent (each debit is a separate payment that references the consent, no payer action needed).
5. Payer can revoke consent at any time (via their bank app).

This is a significant architectural change. Let me think about what needs to change:

1. **New domain concepts**: Subscription/Consent (согласие), Mandate, Recurring debit.
2. **New state machine**: Consent lifecycle (PENDING → ACTIVE → REVOKED/EXPIRED/CANCELLED), and recurring debit states.
3. **New API endpoints**: consent creation, consent status, consent revocation, recurring debit initiation, and likely callback/webhook for consent events.
4. **OPKC adapter contract**: new methods (registerConsent, revokeConsent, createRecurringPayment, getConsentStatus), new events (consent.activated, consent.revoked, consent.rejected).
5. **New invariants**: AD-009 (recurring debits only against active consent within limits), AD-010 (consent revocation is immediate and propagates), etc.
6. **NFR**: consent registration latency, recurring debit throughput, consent revocation propagation latency.
7. **Contract changes**: openapi yaml — add new endpoints, add new statuses, keep backwards compatible (additive only, no breaking existing consumers).

Now, let me carefully consider the significance assessment and route. The existing solution is "Critical" (11/15). The recurrent payments change is a significant feature addition that touches:
- New financial domain (consent, mandate) — regulatorily sensitive (161-ФЗ, Положение ЦБ о защите информации при переводах, new НСПК rules for recurrent payments).
- New state machine (consent lifecycle) alongside existing payment state machine.
- Contract changes (API, OPKC adapter).
- Security/consent (ПДн, consent management, revocation rights).

But it doesn't break core invariants (AD-001..AD-008 remain valid): isolation of payment contour, single source of truth (status machine), idempotency, single OPKC adapter, credit only from confirmed status, trust zones, compliance. The change is additive/extension.

So the route: significant change → full solutioning-level design (a new ADR or a small set of ADRs), NOT a rewrite of the whole solution. The change is "major feature within existing spine" — I'd assess it as requiring: 1 new ADR (or 2-3 ADRs) for the recurrent payment design, additions to spine (AD-009+), contract additions, NFR additions, state machine additions, openapi additions.

Now, the deliverables the user wants:
1. Оценка значимости изменения и маршрута — significance & route (how deep the design needs to be).
2. Влияние на принятую архитектуру — which invariants affected, what changes, what doesn't.
3. Архитектурное решение с альтернативами, последствиями, обратимостью — an ADR.
4. Изменения контрактов (openapi/tsp-api.yaml) без поломки — contract changes.
5. Измеримые NFR для нового функционала.
6. Критерии приёмки и план отката.
7. Что остаётся на решение человека-архитектора и почему.

I need to produce these as files in the repo, following the repo's conventions. The user says "Код не пиши" (don't write code). But writing OpenAPI YAML is a contract, not code — and it's explicitly requested in deliverable #4. So I need to modify openapi/tsp-api.yaml.

Let me think about how to structure the deliverables in files:

The natural approach following the repo conventions:

**New ADR**: `docs/adr/ADR-008-rekurrentnye-platezhi-sbp-podpiski-po-soglasiyu.md` — the architecture decision for recurrent C2B debits.

Wait, but ADR-008 doesn't exist yet (ADR-001..007 exist). So the new ADR is ADR-008. Actually, let me double check: the spine has AD-001..AD-008 (AD-008 = strategy, adopted). ADRs are numbered separately: ADR-001..ADR-007. So new ADR = ADR-008.

**Spine additions**: new invariants AD-009, AD-010 (etc.) in ARCHITECTURE-SPINE.md, marked `Proposed` (to be ratified by ADR-008).

Actually, let me think carefully. The spine has AD-001..AD-008. AD-008 is the strategy. New invariants would be AD-009+. But wait — is it appropriate to add new ADs to the spine for a feature that is still being proposed? Yes — the spine already has AD-001..AD-007 all "Proposed (ADR-XXX)". So adding AD-009..AD-0XX with Status "Proposed (ADR-008)" fits.

**solutioning.md**: This is the "full design". Should I update it? The user says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The accepted way is ADR + spine + contracts + nfr + spec. solutioning.md is a "full solutioning" doc. I think I should add a section or a reference. Actually, given the deliverable structure, I think the cleanest approach is:

1. Create a new ADR-008 (the architecture decision) — this is deliverable #3 (decision with alternatives, consequences, reversibility) plus partially #1 and #2.
2. Add spine invariants AD-009..AD-011 to ARCHITECTURE-SPINE.md — this is deliverable #2 (impact on invariants).
3. Update openapi/tsp-api.yaml — deliverable #4.
4. Add NFR section for recurrent payments — deliverable #5. Either in docs/nfr.md (append a section) or a new file. Since nfr.md is the canonical NFR file, I'll append a new section there. But the CONSTRAINTS.yaml rule `nfr-measurable` checks that docs/nfr.md contains '99,95' — I must not break that. Appending is fine.

Actually wait — should I modify docs/nfr.md or create docs/nfr-recurrent.md? The repo convention has a single docs/nfr.md. To keep it clean and follow convention, I'll append a new section to docs/nfr.md for recurrent payments. But I need to be careful — modifying the accepted NFR file. The user said change only in the accepted way. Adding a clearly-marked new section for the new feature is the accepted way (the file is versioned, additive).

Hmm, but actually, let me reconsider. There might be a cleaner structure. Let me think about what's the minimal, well-organized set of files:

The user asked for 7 deliverables. These map naturally to:

1. Significance & route → a section in the ADR or a separate "solutioning change note". I think this belongs in the ADR's Context, or in a small dedicated section. Actually, the repo has `docs/solutioning.md` with "Маршрут: Critical (значимость 11/15)". So route/significance is a documented concept. I should produce an assessment. 

Let me think about whether to create a dedicated "change package" document vs. spreading across existing files. The user says "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям." — Prepare an architecture package for this change on top of the accepted solution, so it can be brought to architecture decision and then handed to implementers.

So the package should be self-contained enough to present at A3 (architecture decision) and hand off. The repo already has a handoff structure (.arch-handoff). But the user is asking me (the solution architect) to prepare the change package — not to regenerate the whole handoff.

I think the cleanest, convention-following approach is:

**Primary new artifact**: `docs/adr/ADR-008-<name>.md` — the complete architecture decision, containing:
- Context (business need + significance + route assessment)
- Decision (recurrent payment model, consent lifecycle, integration with existing components)
- Alternatives considered
- Consequences
- Reversibility
- References

**Spine**: add AD-009, AD-010, AD-011 to ARCHITECTURE-SPINE.md (Proposed).

**Contracts**:
- Update `openapi/tsp-api.yaml` (additive endpoints + schemas).
- Update `docs/contracts/tsp-api.md` (add recurring payment methods).
- Update `docs/contracts/opkc-adapter.md` (add consent/recurring methods + events).

**State machine**: update `docs/spec/state-machine.md` (add consent state machine + recurring debit states).

**NFR**: append section to `docs/nfr.md`.

**Acceptance criteria & rollback**: This is deliverable #6. Where does it go? In the repo, acceptance criteria live in solutioning.md §7 (gates) and the handoff RUBRIC. Rollback plan lives in solutioning.md §8 and ADR Reversibility. I think I should put acceptance criteria + rollback in the ADR itself (or a dedicated section). 

Actually, given the scale, I think the best approach to keep it reviewable and handoff-ready is:

1. `docs/adr/ADR-008-rekurrentnye-c2b-platezhi-podpiski-po-soglasiyu.md` — main decision (covers deliverables 1, 2, 3, and references NFR + contracts).
2. Modify `ARCHITECTURE-SPINE.md` — add AD-009..AD-011.
3. Modify `docs/spec/state-machine.md` — add consent + recurring debit state machines.
4. Modify `docs/contracts/tsp-api.md` — add methods.
5. Modify `docs/contracts/opkc-adapter.md` — add methods/events.
6. Modify `openapi/tsp-api.yaml` — additive endpoints/schemas.
7. Modify `docs/nfr.md` — add recurrent NFR section.
8. Optionally: a dedicated change package doc `docs/solutioning-recurrent.md` or a section in solutioning.md.

Hmm, this is getting large. But the user explicitly wants a comprehensive package. Let me be thorough but organized.

Actually, let me reconsider the scope to keep it manageable and high-quality. The 7 deliverables need to be visible. Let me map them to files:

1. **Оценка значимости + маршрут** → Section in ADR-008 (Context + "Значимость и маршрут" section). Also I can note in the summary.
2. **Влияние на принятую архитектуру** → ADR-008 "Impact on existing invariants" section + spine additions.
3. **Архитектурное решение** → ADR-008.
4. **Изменения контрактов** → openapi/tsp-api.yaml (code-like, but it's a contract) + docs/contracts/tsp-api.md + opkc-adapter.md.
5. **NFR** → docs/nfr.md new section.
6. **Критерии приёмки + план отката** → ADR-008 section (or a dedicated acceptance doc). Given the handoff RUBRIC values "acceptance criteria" and "rollback plan", and solutioning.md §7/§8 hold these, I'll put them in the ADR-008 as explicit sections "Критерии приёмки" and "План отката".
7. **Что остаётся на решение человека** → ADR-008 section "Открытые вопросы / что решает человек" + "A3 decision" style.

Actually, I realize the cleanest approach given "вынести на архитектурное решение" (bring to architecture decision = A3 gate) is to write the ADR in the style of ADR-007 which has an "A3 Decision (машинно-читаемый пакет)" section with choice/rationale/constraints/rejected options. This is exactly the format for a decision that needs a human A3 decision.

So ADR-008 will have:
- Context (business need, significance, route)
- A3 Decision (choice: e.g., "consent-based recurring debit as first-class domain in gateway" vs alternatives)
- Decision (detailed: consent lifecycle, recurring debit flow, state machines, contract changes, NFR)
- Alternatives Considered
- Consequences
- Reversibility
- Impact on existing invariants (AD-001..AD-008)
- Критерии приёмки
- План отката
- Открытые вопросы / что решает человек-архитектор
- References

That's a comprehensive single document. Then supporting file modifications.

Let me think about the actual architecture decisions for recurrent C2B payments in СБП.

### Domain model for СБП recurring payments (подписки / автоплатежи)

Key concepts (based on СБП/НСПК recurring payment model, which I know from the public "СБП C2B" and general subscription/mandate patterns; exact protocol details marked [ТРЕБУЕТ ПРОВЕРКИ] since НСПК docs are not public):

1. **Согласие (Consent / Mandate)** — the payer's consent to allow the merchant (ТСП) to initiate recurring debits. Key attributes:
   - `consentId` (gateway), `opkcConsentId` (НСПК)
   - `tspId` (merchant)
   - `payerId` (или ссылка на плательщика — в СБП это идентифицируется через банк плательщика / phone / account; детали [ТРЕБУЕТ ПРОВЕРКИ])
   - `maxAmount` (max per debit)
   - `maxFrequency` (max debits per period, e.g., per day/week/month)
   - `validUntil` (expiry)
   - `status`: PENDING → ACTIVE → REVOKED / EXPIRED / REJECTED
   - `subscriptionPurpose` / `merchantConsentRef`

2. **Рекуррентный платёж (Recurring Debit)** — a payment initiated by the merchant against an active consent, without payer's interactive action. It references `consentId` + `merchantOrderId`. Each debit is its own payment with its own state machine (reuse the existing payment state machine, but with a different trigger: initiated from consent, not from QR scan).

Key flow:
1. ТСП creates consent → gateway → OPKC → payer receives consent request (QR/deep link) → payer confirms in their bank app → НСПК sends consent.activated → gateway marks consent ACTIVE.
2. ТСП initiates recurring debit (POST /v1/recurring-payments {consentId, amount, merchantOrderId}) → gateway validates: consent ACTIVE, amount ≤ maxAmount, frequency within limits → creates a payment (CREATED → ... → COMPLETED) but with trigger from consent, not QR. The OPKC processes the debit via the consent reference (no QR needed).
3. Payer can revoke consent at any time (via their bank app / НСПК) → НСПК sends consent.revoked → gateway marks REVOKED → all future debits rejected; in-flight debits are settled by reconciliation.

### Architectural decisions (alternatives)

**D1. How to model consent in the gateway:**
- **Option A (chosen): Consent as a first-class domain aggregate in the gateway** with its own state machine, separate from payments, linked 1:N to recurring debits. Reuses the payment state machine for each debit (debit = payment with `paymentType=RECURRING`, `consentId` reference). This preserves AD-002 (single source of truth = status machine) and AD-005 (credit only from PAID).
- **Option B: Treat consent as just a "flag" on the merchant/TSP** without its own lifecycle — simpler but loses auditability, revocation guarantees, and limit enforcement; fails 161-ФЗ/ПДн consent requirements.
- **Option C: Delegate consent fully to OPKC** (gateway only proxies) — loses local source of truth (violates AD-002 spirit), can't enforce limits locally, depends on OPKC for every check.

Decision: Option A.

**D2. How to trigger the recurring debit (vs existing QR flow):**
- **Option A (chosen): Extend the existing payment state machine** with a new entry state/transition `CREATED` (via `paymentType=RECURRING` and `consentId`) instead of a separate machine. The existing T1 transition (`POST /v1/payments`) branches: if `consentId` present → recurring debit (no QR, OPKC debits via consent); else → QR flow. This maximizes reuse of the proven state machine + idempotency + outbox + credit-from-PAID.
- **Option B: Separate "subscription" state machine** for recurring debits — cleaner separation but duplicates the entire financial state machine, risk of divergence from payment machine, more surface for bugs.
- **Option C: Batch/aggregated debits** (one OPKC call for many) — optimization, defer.

Decision: Option A (extend payment machine with `paymentType` + `consentId`).

**D3. Where is the consent limit enforced?**
- **Decision**: Enforce `maxAmount`/`maxFrequency`/`validUntil` in the gateway (local, authoritative) AND rely on OPKC for final enforcement (defense in depth). Gateway is the source of truth for limits (AD-002), but OPKC is the ultimate authority at the НСПК layer; discrepancies → reject + reconcile.

**D4. Revocation propagation:**
- **Decision**: Consent revocation is **immediate and synchronous** in the gateway (mark REVOKED, reject in-flight debits at validation). НСПК revocation event is authoritative (AD-003 idempotency by eventId). Payer can revoke via their bank app (НСПК → gateway event) or via ТСП (gateway → OPKC → НСПК).

### Impact on invariants (AD-001..AD-008)

- AD-001 (isolation): unchanged — consent and recurring debits are part of the gateway contour, OPKC/АБС access still only via adapters. **New**: consent management is a new capability inside the gateway, no new bypass.
- AD-002 (status machine as single source of truth): **extended** — add consent state machine; recurring debits still use the payment machine. The invariant rule ("изменение финансового статуса платежа + outbox атомарно") applies unchanged; extended to consent transitions (consent status change + outbox atomic).
- AD-003 (idempotency): **extended** — new idempotency keys: consent `Idempotency-Key`, НСПК consent events `eventId`, recurring debit reuses `Idempotency-Key`/`paymentId`. Same rule.
- AD-004 (single OPKC adapter): unchanged — consent/recurring operations go through the same OPKC adapter.
- AD-005 (credit only from PAID): unchanged — recurring debit credits to ТСП only after PAID; consent activation itself is not a financial credit.
- AD-006 (trust zones): unchanged.
- AD-007 (compliance): **extended** — consent data = ПДн + new regulatory surface (161-ФЗ, Положение ЦБ о защите информации при переводах — consent/mandate rules), consent audit trail, payer's right to revoke (152-ФЗ). New audit requirements for consent lifecycle.
- AD-008 (strategy hybrid): unchanged — consent/recurring still core (own dev) + vendor transport. But **new RFP requirement**: vendor adapter must support consent/recurring methods in OPKC contract. This extends the RFP scope (opkc-adapter contract).

### New spine invariants (AD-009+)

- **AD-009. Рекуррентное списание — только по активному согласию в пределах лимитов** — debit possible only from ACTIVE consent, amount ≤ maxAmount, frequency within limits, not expired. Fitness: test that debit is rejected from REVOKED/EXPIRED/PENDING consent or over-limit.
- **AD-010. Отзыв согласия — немедленный и необратимый** — revocation is immediate, synchronous, no new debits after revocation; revocation event idempotent by eventId. Fitness: test revocation → subsequent debit rejected.
- **AD-011. Согласие — отдельный агрегат с собственной статусной машиной и аудитом** — consent lifecycle transitions atomic (status + outbox + audit), separate from payment machine, 1:N to debits. (This is a structural invariant.)

Maybe also AD-012 about audit/compliance for consent (ПДн minimization + revocation rights). Let me consolidate to 3-4 invariants.

Actually let me be careful not to over-engineer. 3 new invariants is reasonable: AD-009 (debit only from active consent within limits), AD-010 (immediate & irreversible revocation), AD-011 (consent as first-class aggregate with own state machine + audit). Compliance (ПДн, consent audit) can be folded into AD-011 or a 4th AD-012. I'll do AD-009, AD-010, AD-011, and maybe AD-012 for consent data/ПДн compliance. Let me keep it at 3 core + note compliance extends AD-007. Actually, let me add a 4th: AD-012 on consent ПДн/compliance — but that might be overkill. I'll fold compliance into AD-011 and add explicit note in the ADR that AD-007 is extended. Let me do 3 new ADs: AD-009, AD-010, AD-011. Keep it clean.

### Contract changes (openapi/tsp-api.yaml) — additive, non-breaking

Additive endpoints (new paths, don't modify existing ones):
- `POST /v1/consents` — create consent (Idempotency-Key)
- `GET /v1/consents/{consentId}` — consent status
- `DELETE /v1/consents/{consentId}` or `POST /v1/consents/{consentId}/revoke` — revoke consent (merchant-initiated)
- `POST /v1/recurring-payments` — initiate recurring debit (or extend POST /v1/payments with `paymentType`/`consentId`)

Hmm, two design choices for recurring debit endpoint:
- (a) Reuse `POST /v1/payments` with new optional fields `paymentType: "qr" | "recurring"` and `consentId`.
- (b) New endpoint `POST /v1/recurring-payments`.

For backwards compatibility and clear semantics, I think (b) a new endpoint `POST /v1/recurring-payments` is cleaner, but it duplicates. Alternatively (a) is more elegant reuse. Actually, the repo's tsp-api.md already has `POST /v1/payments` with `qrType: dynamic|static|link`. Extending it with `paymentType` might be awkward.

Let me decide: **New endpoint `POST /v1/recurring-payments`** that creates a recurring debit and internally produces a payment in the same state machine with `paymentType=RECURRING`. This is clean, non-breaking (new path), and keeps the existing `/v1/payments` semantics untouched for the QR flow. The recurring payment resource still returns `paymentId` and can be queried via existing `GET /v1/payments/{paymentId}` (status is shared). Actually, that's elegant: the debit IS a payment (same state machine), so it's visible via the existing GET /payments/{paymentId}. The only new thing is the initiation endpoint + consent endpoints.

Wait, but should the debit be visible in GET /payments/{paymentId}? Yes — it reuses the payment state machine and `paymentId`. So GET status works. And refunds on recurring debits work via existing refund saga (ADR-005) — good, no change needed there.

So contract changes:
1. New `POST /v1/consents` + `GET /v1/consents/{consentId}` + `POST /v1/consents/{consentId}/revoke` (+ `DELETE`).
2. New `POST /v1/recurring-payments` (Idempotency-Key).
3. New schemas: `ConsentRequest`, `Consent`, `RecurringPaymentRequest`.
4. Extend `Payment` schema: add optional `paymentType` (enum: `QR`, `RECURRING`) and optional `consentId`, optional `maxAmount`... actually `Payment` should get optional `paymentType` and `consentId` fields (additive — optional fields are backwards compatible).
5. Extend `Payment.status` enum? The recurring debit uses the same status enum (CREATED...REFUNDED), so no new status needed. Good — no breaking enum change. But wait, do we need a `REVOKED` status for the debit? No — revocation is on the consent, not the debit. In-flight debits either complete or fail. So no new payment status. 

But the consent has its own status enum: `PENDING`, `ACTIVE`, `REVOKED`, `EXPIRED`, `REJECTED`.

Also new webhook events: `consent.activated`, `consent.revoked`, `consent.expired`, `consent.rejected`, plus `payment.completed`/`payment.failed` already cover debits (they reuse payment events). Maybe add `paymentType` to webhook body for debits. Additive.

This is a good, clean design. Let me also add `maxAmount`, `maxFrequency`, `validUntil` to consent, and `consentId`, `amount` to recurring payment request.

Let me also think about frequency enforcement — `maxFrequency` needs a period unit. I'll model as `maxFrequencyPerPeriod` with `frequencyPeriod` enum (DAY/WEEK/MONTH) or just `maxDebitsPerMonth`. To keep it simple and align with НСПК, I'll use `maxAmount` (per debit) + `frequency` object. Actually, let me keep it aligned with typical НСПК consent: `amountLimit` (max per debit), `periodLimit` (max total over period), `validityPeriod`. Hmm. To avoid over-specifying [ТРЕБУЕТ ПРОВЕРКИ] fields, I'll define a minimal, sensible consent schema and mark НСПК-specific fields as [ТРЕБУЕТ ПРОВЕРКИ].

Consent schema (minimal):
```
Consent:
  consentId, tspId, status (PENDING|ACTIVE|REVOKED|EXPIRED|REJECTED),
  maxAmount (int, копейки, max per debit),
  maxDebitsPerPeriod (int, optional), period (DAY|WEEK|MONTH, optional),
  validUntil (ISO8601),
  purpose (string),
  merchantConsentRef (string, optional, сквозной),
  createdAt, activatedAt, revokedAt (optional)
```

RecurringPaymentRequest:
```
  consentId, amount, merchantOrderId (optional), paymentPurpose (optional)
```

Payment (extended, additive):
```
  + paymentType: QR | RECURRING (optional, default QR)
  + consentId: string (optional)
```

OK. Now let me also consider: the existing `PaymentRequest` in openapi requires `amount, merchantOrderId`. The new recurring payment request is a separate schema.

Let me now also think about the OPKC adapter contract changes (opkc-adapter.md):
New methods (ядро → адаптер):
- `createConsent` — register consent in НСПК (reference=consentId, tspId, maxAmount, limits, validUntil) → `ACCEPTED` (result by event)
- `getConsentStatus` — query consent status
- `revokeConsent` — revoke in НСПК (merchant-initiated)
- `createRecurringPayment` — initiate recurring debit by consent (reference=paymentId, consentId/opkcConsentId, amount) → `ACCEPTED` (result by event, or synchronous qrId-like? No — recurring debit has no QR; result is `payment.paid`/`payment.rejected` event)

New events (адаптер → ядро):
- `consent.activated`, `consent.rejected`, `consent.revoked`, `consent.expired`
- `recurring.paymentAccepted`/`recurring.paymentRejected` — or reuse `payment.paid`/`payment.rejected`? Since recurring debit reuses the payment machine, its result events can reuse `payment.paid`/`payment.rejected` with the `reference`=paymentId. But we might want a distinct `payment.recurringRejected` reasonCode for "consent revoked / limit exceeded". I'll reuse `payment.paid`/`payment.rejected` and add a `reasonCode` enum value. Also add `consent.*` events (4 new).

Also the RFP vendor requirements: vendor must implement consent/recurring methods (G4 extension), and idempotency by reference for consent creation.

Now let me also think about state machine (state-machine.md) changes:
Add a **Consent state machine** section:
```
PENDING → ACTIVE → REVOKED | EXPIRED | REJECTED
```
Transitions table for consent. Plus note that recurring debit reuses payment state machine with a new trigger (T1 variant: `paymentType=RECURRING` + `consentId` → CREATED, then OPKC debits → PAID via `payment.paid`).

Actually, let me think about whether the recurring debit's state machine is identical. For recurring:
- `CREATED` (registered in gateway) → (OPKC accepts debit) → ... → `PAID` (НСПК confirmed) → `CREDITED` → `COMPLETED`.
- The difference: no `QR_ISSUED` state (no QR). So the transition is `CREATED → PAID` directly (skip QR_ISSUED), or `CREATED → FAILED`.

So I need a new transition T-rec: `CREATED → PAID` (for recurring, via `payment.paid` event) and `CREATED → FAILED` (via `payment.rejected`). The existing machine has `QR_ISSUED → PAID`. So I add a branch: for `paymentType=RECURRING`, `CREATED → PAID` (no QR step). This is a modest extension.

Let me now also think: is there a "pending" debit state where НСПК is processing? The recurring debit might be accepted then paid later (asynchronously). So `CREATED` → (OPKC `recurring.accepted`) → maybe a technical state `DEBIT_PENDING` → `PAID`. To keep it simple, I'll reuse `CREATED` until `PAID`, with a technical substate if needed. Actually, the QR flow has `QR_ISSUED` as the "awaiting payment" state. For recurring, the analogous "awaiting НСПК debit result" state could be a new state or reuse. I'll introduce a technical sub-state or reuse `CREATED`. To keep the financial states (visible to ТСП) unchanged, I'll say: recurring debit goes `CREATED → PAID → CREDITED → COMPLETED` (financial states), with an internal `OPKC_PENDING` technical substate within `CREATED`. This keeps the ТСП-visible enum unchanged (good — no breaking change).

OK, I think I have a comprehensive plan. Now let me also decide on the "route" assessment (deliverable #1).

### Significance & route assessment

The existing solution is "Critical" (11/15). This change:

Significance factors:
- **Domain/regulatory sensitivity**: High. Recurring payments involve new consent/mandate model, additional 161-ФЗ/Положение ЦБ/НСПК rules for recurring payments, ПДн (consent data), payer's right to revoke. Financial risk: unauthorized recurring debits = direct consumer harm + regulatory exposure.
- **Architectural depth**: Medium-High. New aggregate (consent) + state machine + contract changes across API, OPKC adapter, НСПК protocol (external). But core invariants (AD-001..AD-008) remain intact — it's an extension, not a re-architecture.
- **Contract blast radius**: Medium. Additive API changes (non-breaking), new OPKC adapter methods (vendor RFP scope grows), new webhook events (additive).
- **New external dependency**: НСПК recurring payment protocol — external input [ТРЕБУЕТ ПРОВЕРКИ] (like the base QR protocol).

Route: **Significant feature — full ADR (ADR-008) + spine extension + contract additions + NFR additions**, NOT a full re-solutioning (the base solutioning.md stands; this is an increment). Route level: I'd call it "Major" (comparable to the original Critical route but scoped as a feature increment). Requires A3 human decision (strategy for consent model + vendor RFP scope + regulatory validation). 

Concretely, I'll rate it: **Значимость High (например 9–10/15, feature-level, не переоткрывающая базовое решение)**, маршрут: **полноценный ADR + расширение spine/контрактов/NFR, с обязательным A3-решением человека** (из-за регуляторной чувствительности и расширения RFP вендора). It does NOT require rewriting solutioning.md wholesale; it's an incremental change package.

I need to decide whether to actually produce a numeric significance. The repo uses "11/15" for the base. I'll produce a comparable assessment: "Значимость 10/15 (feature-уровень в рамках принятой Critical-инициативы)". This is defensible.

Let me now think about what NOT to change:
- Don't change AD-001..AD-008 rules (they're invariant; extending the scope is fine but not rewriting rules).
- Don't break the CONSTRAINTS.yaml fitness rules (nfr-measurable needs '99,95' in nfr.md; abs-credit-only-from-paid needs 'только из состояния `PAID`' in ADR-005; adr-no-placeholders needs no '<!--' in docs/adr/*.md). I must be careful: my new ADR-008 must not contain `<!--` HTML comments (the rule is `must_not_contain pattern '<!--'`). Good — I won't use HTML comments.
- Don't introduce `TODO|TBD|XXX` in spine (warn-level lint). I'll avoid those literal tokens in spine.

Now, one more consideration: the user said "Код не пиши" (don't write code). The openapi/tsp-api.yaml is a contract (data), and deliverable #4 explicitly asks to change it. So editing the YAML is in-scope and expected. I'll treat YAML contract changes as "contracts", not "code". This is consistent.

Also: should I actually edit the files, or present the package as a plan/proposal? The user says "Подготовь архитектурный пакет" and "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — this implies I should actually produce the files (the package), changing files in the accepted way (ADR + spine + contracts + nfr + spec + openapi). And "Когда закончишь, кратко перечисли созданные и изменённые файлы." — so I should create/modify files and list them.

This is not a plan-mode request; it's an execution request. I should execute: create/modify the files.

However, this is a substantial, multi-file change. Should I use plan mode? The user has NOT asked for plan mode. The instructions say don't enter plan mode on my own. And the task is clear enough. I'll proceed to implement the package directly, following repo conventions.

But wait — there's ambiguity worth confirming? Let me think. The main design decisions where I'm making choices:
1. Consent as first-class aggregate (vs delegate to OPKC) — I'll choose first-class, present alternatives in ADR.
2. Recurring debit reuses payment state machine (vs separate) — choose reuse.
3. Endpoint design: new `/v1/recurring-payments` + `/v1/consents` (vs extend /payments).
4. Whether to add numeric significance.

These are architecture decisions the user explicitly asked me to make ("Архитектурное решение с рассмотренными альтернативами"). So I should make them, document alternatives, and leave the truly human decisions (regulatory validation, НСПК protocol details, vendor RFP scope, consent revocation UX) as open questions. I don't need to ask the user upfront — the deliverable #7 is precisely "what remains for the human architect", so I document those.

I think I have enough to proceed. This is a large but well-scoped task. Let me also decide: do I need to check git status first? The repo is clean per the snapshot. I'll do a quick git status before editing to be safe, and to know the baseline. Actually the snapshot says clean. I'll proceed but do a quick git status at the end.

Let me also reconsider: should I modify `docs/solutioning.md`? The user wants the package to be "brought to architecture decision and then handed to implementers." The base solutioning.md has §9 gaps (which includes "roadmap: автоплатежи" — actually §1 says "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи"). So "автоплатежи" (recurring payments) is currently explicitly listed as OUT of scope / roadmap! This is an important finding: the change brings a roadmap item into scope.

I should note this clearly: this change pulls "автоплатежи" from the deferred/roadmap list into active scope. This affects solutioning.md §1 and the spine "Deferred" section (which currently lists C2C, выплаты, диспуты — but NOT автоплатежи; actually автоплатежи is in solutioning.md §1 roadmap, not in spine Deferred).

Wait, let me check the spine Deferred section again:
```
## Deferred (с причиной и условием возврата)
- Мультивалютность и иностранные платёжные системы...
- C2C-переводы и выплаты B2C/B2B...
- Диспуты/претензии (disputes)...
```
No "автоплатежи" in spine Deferred. But solutioning.md §1 roadmap lists "автоплатежи" as out of scope. So the change is consistent: it's bringing a previously-roadmapped item into scope. I should update solutioning.md §1 to reflect that автоплатежи is now in scope (via ADR-008), OR add a note. Actually, since the package is an increment, I'll add a brief note/reference in solutioning.md rather than rewrite it. Hmm, but solutioning.md is the "full design" — should I add a section? 

Let me think about the cleanest approach for solutioning.md. The base solutioning.md is a "полный Solutioning" for C2B-приём. The recurrent payments are a new feature. I think the cleanest is to NOT heavily edit solutioning.md (to avoid churn), but to add a short pointer at the top referencing the new ADR-008 and noting the scope change (автоплатежи в scope). Actually, I'll add a concise new section or a top-level note. Let me add a brief "## 11. Изменение: рекуррентные C2B-платежи (подписки)" section at the end of solutioning.md that summarizes the change and points to ADR-008 + changed files. That keeps the base intact and makes the increment discoverable.

Actually, let me reconsider the overall file plan to be clean and not over-produce. Final plan:

**New file:**
1. `docs/adr/ADR-008-rekurrentnye-c2b-platezhi-podpiski-po-soglasiyu-platelshchika.md` — the main architecture decision (covers deliverables 1, 2, 3, 6, 7).

**Modified files (accepted way):**
2. `ARCHITECTURE-SPINE.md` — add AD-009..AD-011 (Proposed, referencing ADR-008); update Deferred note if needed (no, автоплатежи not in Deferred).
3. `docs/spec/state-machine.md` — add consent state machine + recurring debit transition.
4. `docs/contracts/tsp-api.md` — add consent + recurring payment methods.
5. `docs/contracts/opkc-adapter.md` — add consent/recurring methods + events + RFP note.
6. `openapi/tsp-api.yaml` — additive endpoints + schemas + webhook note (yaml has no webhooks section currently, so I just add paths + schemas).
7. `docs/nfr.md` — add recurrent NFR section.
8. `docs/solutioning.md` — add a short increment section pointing to ADR-008 + note автоплатежи in scope.

That's 1 new + 7 modified = 8 files. Comprehensive but each change is focused.

Hmm, that's a lot. But the user asked for a complete package. Let me make sure each modification is high-quality and follows the exact style.

Let me reconsider whether to modify tsp-api.md AND openapi/tsp-api.yaml (they're both the merchant API contract). The openapi yaml is a thin subset (just payments + status, no refunds, no TSP registration, no webhooks, no errors). The tsp-api.md is the detailed contract. Deliverable #4 says "Изменения контрактов (`openapi/tsp-api.yaml`)". So the explicit ask is openapi/tsp-api.yaml. But for consistency, tsp-api.md (the detailed contract) should also be updated to match, otherwise they'd diverge. I'll update both, keeping them consistent. openapi is the machine-readable contract, tsp-api.md is the human-readable detailed contract.

Actually, let me reconsider — maybe I should keep the openapi as the source and update tsp-api.md to match. Both need updating for a coherent package.

Let me also reconsider the NFR: should I add a new file `docs/nfr-recurrent.md` or extend `docs/nfr.md`? The fitness rule `nfr-measurable` checks `docs/nfr.md` for '99,95' (must_contain). If I extend docs/nfr.md, that still contains '99,95' (it's already there). Extending is safe. I'll extend docs/nfr.md with a new section "## 7. Рекуррентные платежи (подписки) — NFR".

Wait, nfr.md currently has sections 1-6 + "Зависимости". Adding section 7 is fine. Let me append.

Now, let me carefully write everything. Let me be thorough but concise in each file.

Let me draft the ADR-008 first (the core). I need to nail the domain and the decision.

Let me reconsider the СБП recurring payment domain once more to be accurate. In СБП (НСПК), recurring payments (автоплатежи / подписки / рекуррентные платежи) work as follows (from public knowledge, exact protocol marked [ТРЕБУЕТ ПРОВЕРКИ]):

- There's a concept of "согласие на автоплатеж" (consent / подписка). 
- The merchant (ТСП) creates a subscription request; the payer approves it (via СБП QR or in-app confirmation in their bank).
- Once approved, the merchant can initiate "рекуррентные платежи" (debits) that reference the subscription, without the payer's per-transaction approval.
- The payer can revoke the subscription at any time.
- The НСПК/СБП rules define limits (max amount, frequency) — exact fields [ТРЕБУЕТ ПРОВЕРКИ].

This matches my model. Good.

For the business: онлайн-кинотеатры (subscriptions — monthly fee), ЖКХ (recurring utility payments), связь (telecom — monthly mobile/telecom bills). These are exactly the recurring C2B use cases.

Now let me write the ADR. I'll follow the exact ADR format used in the repo:
```
# ADR-008. <title>
- Date: ...
- Status: Proposed
- Owner: ...
- Related: ...
## Context
## Decision (или A3 Decision + Decision)
## Alternatives Considered
## Consequences (Positive/Negative)
## Reversibility
## References
```

Plus I'll add custom sections for the deliverables: "Значимость и маршрут", "Влияние на принятые инварианты (AD-001..AD-008)", "Критерии приёмки", "План отката", "Что остаётся на решение человека-архитектора". These extra sections are acceptable as the ADR format is somewhat flexible (ADR-007 added "A3 Decision (машинно-читаемый пакет)").

Let me write the content now. I'll be careful about:
- No `<!--` comments.
- Date: use today's date 2026-09-28 (the authoritative date). Actually the repo ADRs use 2026-08-15. I'll use 2026-09-28.
- Owner: solution-architect.

Let me write it all out.

Actually, let me reconsider the significance number. The base is 11/15 "Critical". This feature:
- New financial product (subscriptions), regulatorily sensitive (recurring debits, consent, 161-ФЗ, Положение ЦБ, НСПК автоплатежи rules). 
- Consumer harm potential (unauthorized debits, over-debiting).
- But: reuses the proven payment machine + outbox + adapters; additive contracts; no re-architecture.

I'll rate significance **10/15** and route **"Major — полноценный ADR + расширение spine/контрактов/NFR; обязательное A3-решение"**. This is defensible and comparable to the base scale.

Actually, I want to be careful about inventing a scale mapping. The repo uses "Critical (значимость 11/15)". I'll mirror: "Маршрут: Major (значимость 10/15)". And explain why it's not Critical (no re-architecture, reuses invariants) but above Standard/Minor (new financial domain, regulatory, new aggregate + contracts).

Let me also think about what a human must decide (deliverable 7):
1. **Бизнес-решение о продукте**: точная модель подписок (лимиты, периоды, тарифы), какие ТСП-сегменты в первой волне.
2. **Регуляторно-правовая валидация**: соответствие модели согласия требованиям 161-ФЗ/Положения ЦБ/правил НСПК по автоплатежам; порядок отзыва согласия; хранение и сроки ПДн согласия. Требует заключения ИБ/комплаенс.
3. **Точный протокол НСПК для автоплатежей** — внешний вход [ТРЕБУЕТ ПРОВЕРКИ]; без него невозможна финальная сигнатура контракта OPKC (какие поля согласия, как НСПК обрабатывает отзыв, лимиты).
4. **Расширение RFP вендора**: вендор должен поддержать методы/события согласий и рекуррентных списаний (расширение G4/G3); выбор вендора — уже человеческое решение A3 (ADR-007), теперь с расширенным scope.
5. **UX отзыва согласия**: как плательщик отзывает (только через банк плательщика/НСПК, или и через ТСП) — влияет на API и обязанности ТСП.
6. **Утверждение новых spine-инвариантов** (AD-009..AD-011) — ратификация ADR-008.

These are genuine human decisions, mostly regulatory/business/НСПК-external.

OK, I'm confident. Let me now write all the files.

Let me start with the ADR-008 (the core deliverable), then spine, then state-machine, then contracts (tsp-api.md + opkc-adapter.md), then openapi yaml, then nfr, then solutioning note.

Let me write carefully.

First, let me write ADR-008.

Actually, let me reconsider the title and naming convention. Existing ADRs:
- ADR-001-outbox.md
- ADR-002-model-konsistentnosti-platezha-konechnyy-avtomat-s-idempotentnostyu-na-urovne-shlyuza.md
- ADR-003-mtls.md
- ADR-004-at-least-once-dlq.md
- ADR-005-integraciya-s-abs-zachislenie-po-podtverzhdyonnomu-statusu-vozvraty-kak-saga.md
- ADR-006-trust.md
- ADR-007-proposed-a3.md

So the filename is `ADR-008-<slug>.md`. Slug in translit. Let me use: `ADR-008-rekurrentnye-c2b-platezhi-podpiski-po-soglasiyu.md`.

Now, an important nuance: the CONSTRAINTS.yaml has a rule:
```
- name: adr-set-complete
  type: file_exists
  path: docs/adr/ADR-001-outbox.md
```
Only checks ADR-001 exists. Fine.

And:
```
- name: abs-credit-only-from-paid
  glob: docs/adr/ADR-005-...md
  pattern: 'только из состояния `PAID`'
```
Only checks ADR-005. Fine, I won't modify ADR-005.

And `adr-no-placeholders`: `glob: docs/adr/*.md`, pattern '<!--'. My new ADR-008 must not contain `<!--`. I won't.

Good.

Now let me write everything. I'll produce substantial, high-quality content.

Let me start writing the ADR-008.

For the state machine section in state-machine.md, I need to add:
- New "Согласие (consent)" section with states and transitions.
- A note in the payment machine that recurring debits reuse it with a CREATED→PAID direct transition (skipping QR_ISSUED), plus paymentType field.

Let me also make sure the consent state machine is consistent with the OPKC adapter events (consent.activated → PENDING→ACTIVE, etc.).

Let me write the files now.

For openapi yaml, I need to carefully write valid OpenAPI 3.0.3 YAML, additive. Let me add:
- paths:
  - /v1/consents (post)
  - /v1/consents/{consentId} (get)
  - /v1/consents/{consentId}/revoke (post)
  - /v1/recurring-payments (post)
- components.schemas:
  - ConsentRequest
  - Consent
  - ConsentStatus (or inline enum)
  - RecurringPaymentRequest
  - Payment (extend with paymentType, consentId optional)

I need to preserve existing content exactly (paths /v1/payments, /v1/payments/{paymentId}, schemas PaymentRequest, Payment) and add to it. Since I'll rewrite the whole file, I must reproduce the existing parts exactly and add new ones.

Let me carefully reconstruct the existing openapi yaml and then extend it.

Existing openapi/tsp-api.yaml:
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

I'll extend `Payment` to add optional `paymentType` and `consentId`, and add the new paths + schemas. I'll write the full file with these additions.

For `Payment`:
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
        paymentType:
          type: string
          enum: [QR, RECURRING]
          description: Тип платежа; по умолчанию QR (обратно совместимо)
        consentId:
          type: string
          description: Идентификатор согласия для рекуррентных платежей (заполняется при paymentType=RECURRING)
```

Adding optional fields to Payment is backwards-compatible.

New schemas:
```yaml
    ConsentRequest:
      type: object
      required: [tspId, maxAmount]
      properties:
        tspId: {type: string}
        maxAmount: {type: integer, description: Максимальная сумма одного списания, в копейках}
        maxDebitsPerPeriod: {type: integer, description: Опц. лимит числа списаний за период}
        period: {type: string, enum: [DAY, WEEK, MONTH], description: Опц. период лимита частоты}
        validUntil: {type: string, format: date-time, description: Срок действия согласия (ISO 8601)}
        purpose: {type: string, description: Назначение подписки (например, «Ежемесячная подписка»)}
        merchantConsentRef: {type: string, description: Опц. сквозной идентификатор согласия ТСП}
    Consent:
      type: object
      required: [consentId, tspId, status, maxAmount]
      properties:
        consentId: {type: string}
        tspId: {type: string}
        status: {type: string, enum: [PENDING, ACTIVE, REVOKED, EXPIRED, REJECTED]}
        maxAmount: {type: integer}
        maxDebitsPerPeriod: {type: integer}
        period: {type: string, enum: [DAY, WEEK, MONTH]}
        validUntil: {type: string, format: date-time}
        purpose: {type: string}
        merchantConsentRef: {type: string}
        createdAt: {type: string, format: date-time}
        activatedAt: {type: string, format: date-time}
        revokedAt: {type: string, format: date-time}
    RecurringPaymentRequest:
      type: object
      required: [consentId, amount]
      properties:
        consentId: {type: string}
        amount: {type: integer, description: Сумма списания, в копейках}
        merchantOrderId: {type: string}
        paymentPurpose: {type: string}
```

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
          description: Согласие создано, ожидает подтверждения плательщиком
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
  /v1/recurring-payments:
    post:
      operationId: createRecurringPayment
      parameters:
        - in: header
          name: Idempotency-Key
          required: true
          schema: {type: string}
      requestBody:
        required: true
        content:
          application/json:
            schema: {$ref: '#/components/schemas/RecurringPaymentRequest'}
      responses:
        '201':
          description: Рекуррентный платёж зарегистрирован
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Payment'}
```

I'll also bump info.version? No — keep 0.1.0 (it's a draft; versioning handled separately). Actually, maybe add a note. I'll leave version 0.1.0 but could add to description. I'll add a description to info indicating recurring endpoints. Minor. Let me add `description:` to info. Actually to minimize risk, I'll keep it minimal — just add paths and schemas.

Now, the tsp-api.md detailed contract additions. I'll add a new section "### 3.6 Согласия (подписки)" and "### 3.7 Рекуррентные списания", plus extend the webhook events (§5) with consent events and paymentType, and update §6 versioning note. And update §7 open questions if relevant (add consent-related). Let me be careful to preserve existing content and append/modify minimally.

Actually, editing tsp-api.md requires careful insertions. Let me plan the edits:
1. After §3.5 (status return), add §3.6 (consents) and §3.7 (recurring payments). 
2. In §5 (webhooks), add consent events to the event list + a note on paymentType for debits.
3. Maybe add to §7 open questions.

Let me now write everything. This is a lot of content. Let me be efficient but complete.

Let me also update state-machine.md:
- Add new section "## 7. Согласие (consent) — статусная машина" with states + transitions.
- Add a note in §2 (payment transitions) about recurring debit transition (CREATED → PAID without QR_ISSUED).

And opkc-adapter.md:
- Add methods to §3 table: createConsent, getConsentStatus, revokeConsent, createRecurringPayment.
- Add events to §4: consent.activated, consent.rejected, consent.revoked, consent.expired.
- Add note in §7/§8 (RFP) that vendor must support consent/recurring.
- Maybe add note in §5 idempotency: consent creation idempotent by reference.

And nfr.md: append section 7 (recurrent payments NFR).

And solutioning.md: append section 11 (change increment) + update §1 roadmap note.

Let me also reconsider: should I update the spine "Deferred" section? Currently it doesn't list автоплатежи. But solutioning.md §1 lists автоплатежи as roadmap. To keep consistency, I'll update solutioning.md §1 roadmap to note that автоплатежи is now in-scope via ADR-008. I could also update the spine Deferred... but spine Deferred doesn't mention автоплатежи, so nothing to change there. Actually, to be safe and consistent, I'll add a note in solutioning.md.

Alright. Let me also think about whether the spine's AD-008 (strategy, ADOPTED) needs updating for the vendor RFP scope. AD-008 Rule says "Ядро шлюза проектируется контрактно-независимым от транспорта... Вендор транспорта обязан предоставить сертификаты... Реализация транспортного слоя начинается только после подписания контракта...". This is about the transport strategy, not specific methods. The consent/recurring methods are new OPKC adapter contract methods that the vendor must implement — this is captured in opkc-adapter.md and RFP, not in AD-008. So AD-008 Rule stays unchanged. Good — I won't modify AD-008.

Now let me write. I'll do the writes in a sensible order. I'll write the ADR first (new file), then modify the others.

Let me write out the full content now.

Actually, given the volume, I should be mindful of correctness and not introduce errors. Let me write each file with full attention.

Let me begin.

For the ADR-008, I'll write comprehensive content covering all deliverables inline, but also keep it as a proper ADR. Let me draft.

---

# ADR-008. Рекуррентные C2B-платежи СБП: подписки по согласию плательщика

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур)
- Related: ADR-001, ADR-002, ADR-004, ADR-005, ADR-007; AD-001..AD-008 (spine)

## 1. Context и значимость

### Бизнес-потребность
ТСП — онлайн-кинотеатры (ежемесячные подписки), ЖКХ (регулярные коммунальные платежи), операторы связи (ежемесячная абонентская плата) — просят рекуррентные C2B-списания по согласию плательщика («подписки СБП»). Сейчас каждый платёж требует генерации QR и активного действия клиента; для периодических платежей это неприемлемо (высокий отток, ручные напоминания).

### Значимость и маршрут

- **Значимость: Major — 10/15** (в принятой шкале базового решения «Critical 11/15»). Причины:
  - новый финансовый продукт (рекуррентные списания) и новая доменная сущность (согласие/мандат);
  - повышенная регуляторная чувствительность: неавторизованное или превышающее лимит списание = прямой вред плательщику; затрагивает 161-ФЗ, Положение ЦБ о защите информации при переводах, 152-ФЗ (ПДн согласия, право отзыва), правила НСПК по автоплатежам;
  - расширяет контракты (API ТСП, внутренний контракт адаптера ОПКЦ) и, следовательно, scope RFP вендора транспорта.
  - **но** не переоткрывает базовые инварианты (AD-001..AD-008): выделенный шлюз, статусная машина как источник истины, идемпотентность, единственный адаптер ОПКЦ, зачисление только из PAID, trust-зоны, гибридная стратегия остаются в силе. Это **инкремент поверх принятого решения**, а не перепроектирование.
- **Маршрут**: полноценный **ADR + расширение spine/контрактов/NFR/статусной машины**; обязательное **A3-решение человека** (регуляторная валидация модели согласия, точный протокол НСПК для автоплатежей — внешний вход, расширение RFP вендора). Не требует переписывания `solutioning.md` целиком — добавляется инкрементный раздел.

### Что меняется, что нет

**Меняется (добавляется):**
- Новая сущность **согласие (consent)** со своей статусной машиной и аудитом — первый гражданин шлюза наравне с платежом.
- Новый тип платежа `paymentType=RECURRING`: рекуррентное списание, инициируемое по активному согласию без QR (переход `CREATED → PAID` без `QR_ISSUED`).
- Новые методы API ТСП (согласия, рекуррентные списания), новые события вебхуков, новые методы/события контракта адаптера ОПКЦ.
- Новые NFR для подписок (латентность, пропускная способность, отзыв, лимиты).

**Не меняется:**
- Инварианты AD-001..AD-008 (см. §2) — расширяются, но не отменяются.
- Существующие методы API ТСП и их семантика (обратная совместимость контракта, §4 контракта).
- Модель зачисления (только из PAID) и сага возвратов (рекуррентные списания возвращаются тем же механизмом ADR-005).

## 2. Влияние на принятые инварианты (spine AD-001..AD-008)

...

## Decision / A3 Decision

...

## Alternatives Considered

...

## Consequences

...

## Reversibility

...

## Критерии приёмки

...

## План отката

...

## Что остаётся на решение человека-архитектора

...

## References

---

This is a lot. Let me write it fully in the actual file.

Let me be careful about one thing: the repo's ADR style uses "# ADR-00X. Title" then bullet metadata, then "## Context", "## Decision", "## Alternatives Considered", "## Consequences", "## Reversibility", "## References". I'll keep that, adding extra sections after Reversibility (or integrated). I'll place "Значимость и маршрут" inside Context, "Влияние" as its own section after Context, and the acceptance/rollback/open-questions as sections before References.

Let me write now. I'll produce the actual file contents.

I need to be thorough. Let me write the ADR content in full.

Let me now also decide the new spine invariants precisely with Rule text:

**AD-009. Рекуррентное списание — только из активного согласия в пределах лимитов**
- Status: Proposed (ADR-008)
- Binds: статусная машина согласия, статусная машина платежа (`paymentType=RECURRING`), адаптер ОПКЦ.
- Prevents: списание по отозванному/истёкшему/неподтверждённому согласию; превышение maxAmount/частоты; «платежи без согласия».
- Rule: Рекуррентное списание создаётся только если согласие в состоянии `ACTIVE`, не истекло (`validUntil` в будущем), сумма ≤ `maxAmount`, частота в пределах `maxDebitsPerPeriod`. Fitness: тест отклонения списания из `PENDING`/`REVOKED`/`EXPIRED`/`REJECTED` и при превышении лимита.

**AD-010. Отзыв согласия — немедленный, необратимый, идемпотентный**
- Status: Proposed (ADR-008)
- Binds: статусная машина согласия, нотификации НСПК (`eventId`), валидация списаний.
- Prevents: списание после отзыва; «мягкий» отзыв, не блокирующий новые списания; расхождение «НСПК отозвал, шлюз не знает».
- Rule: Переход согласия в `REVOKED` фиксируется атомарно (статус + outbox + аудит) и немедленно блокирует новые списания; повторная нотификация отзыва идемпотентна по `eventId`; `REVOKED`/`EXPIRED`/`REJECTED` — терминальные для согласия.

**AD-011. Согласие — отдельный агрегат с собственной статусной машиной и аудитом**
- Status: Proposed (ADR-008)
- Binds: БД шлюза (состояние согласия), outbox, аудит-лог, ПДн согласия.
- Prevents: размывание статусной модели платежа; хранение согласия «флагом» без жизненного цикла и аудита; утечку/перехранение ПДн согласия.
- Rule: Согласие — самостоятельный агрегат: `PENDING → ACTIVE → REVOKED|EXPIRED|REJECTED`, 1:N к рекуррентным списаниям; переходы атомарны (AD-002); каждый переход и каждое списание — в неизменяемом аудит-логе; ПДн согласия минимизированы (152-ФЗ), право отзыва — всегда доступно.

That's 3 clean invariants. Good.

Now, let me write all files. I'll do it now.

Let me write the ADR file first.

I want to make sure the ADR's "Decision" section is concrete and covers:
1. Consent as first-class aggregate.
2. Recurring debit reuses payment machine (paymentType=RECURRING, skip QR_ISSUED).
3. Limit enforcement (gateway authoritative + OPKC defense in depth).
4. Revocation propagation.
5. Contract changes summary (API, OPKC adapter).
6. State machine additions.
7. NFR.

And A3 decision block: choice = "consent-based recurring as first-class gateway capability (extend payment machine)" with rationale, constraints, rejected options, expiry.

Rejected options for A3:
- full-delegate to OPKC (lose local source of truth)
- full-vendor subscription module (vendor lock-in, inconsistent with ADR-007 hybrid)
- separate parallel subscription engine (duplicate state machine)

Let me finalize and write.

I'll now write all files via write_file/edit. For the ADR (new file), write_file. For modifications to existing files, I'll use edit with precise old_string.

Let me write the ADR-008 file.

Given the length, I'll write it now carefully.

For dates in the ADR I'll use 2026-09-28.

Let me write.
Я изучил решение полностью: spine (AD-001..AD-008), ADR-001..007, контракты, статусную машину, NFR, RFP и openapi. Ключевой факт для этого изменения — «автоплатежи» сейчас явно вынесены из scope (solutioning §1), а все базовые инварианты строятся вокруг модели «платёж → QR → PAID». Рекуррентное списание добавляет новую доменную сущность «согласие» и новый тип платежа без QR.

Готовлю пакет поверх принятого решения: новый ADR-008 + расширение spine/контрактов/статусной машины/NFR. Начинаю с ядра — ADR-008.

  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now let me update the ARCHITECTURE-SPINE.md to add AD-009..AD-011. I need to find the right insertion point — after AD-008 and before "## Deferred".

Let me read the exact text around there to make precise edits.

The spine content I already have. AD-008 ends with:
```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll insert AD-009, AD-010, AD-011 between AD-008's rule and the `---` / `## Deferred`.

Let me craft the edit. The old_string should be the AD-008 rule ending + the separator + Deferred heading. I'll insert new invariants.

Let me write the edit carefully.
Теперь расширяю spine — добавляю инварианты AD-009..AD-011 после AD-008.

  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/spec/state-machine.md", old_string="| T1 | — | `CREATED` | `POST /v1/payments` (новый `paymentId`) | валидный запрос, ТСП активен | запись платежа + outbox-событие «регистраци, new_string="| T1 | — | `CREATED` | `POST /v1/payments` (новый `paymentId`) или `POST /v1/recurring-payments` (`paymentType=RECURRING`) | валидный запро)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/spec/state-machine.md", old_string="| T12 | `COMPLETED` | (остаётся `COMPLETED`) | **частичный** возврат завершён | сумма возврата < суммы платежа | запись в `refunds[]`, вебх, new_string="| T12 | `COMPLETED` | (остаётся `COMPLETED`) | **частичный** возврат завершён | сумма возврата < суммы платежа | запись в `refunds[]`, вебх)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/spec/state-machine.md", old_string="Маппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `EXPIRED`, `REFUNDED` — без техн, new_string="Маппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `EXPIRED`, `REFUNDED` — без техн)`

Now update state-machine.md. I need to add:
1. A note in §2 (payment transitions) about the recurring debit transition (CREATED → PAID without QR_ISSUED).
2. A new section "## 7. Согласие (consent) — статусная машина".

Let me re-read the state-machine.md structure to find exact insertion points.

The state-machine.md ends with section 6 "Согласованность с API ТСП". I'll append section 7 after it. Also I should add a note in §2 table about the recurring transition.

Let me look at §2 table. The transitions T1..T12. T1 is `— → CREATED` via POST /v1/payments. T4 is `QR_ISSUED → PAID`. For recurring, I need a transition `CREATED → PAID` (skip QR_ISSUED).

I'll add a note after the table or add a new row T-rec. Better: add a note in §2 explaining the recurring variant, and add it to the table as T13/T14.

Actually, cleaner: add rows to the transitions table:
| T13 | `CREATED` | `PAID` | нотификация НСПК `payment.paid` (рекуррентное списание) | `paymentType=RECURRING`, согласие `ACTIVE`, лимиты соблюдены | outbox-событие «зачисление в АБС» |
| T14 | `CREATED` | `FAILED` | нотификация НСПК `payment.rejected` (рекуррентное списание) | — | `errorCode`, вебхук `payment.failed` |

And modify T1 to note it branches for recurring too. Actually T1 currently: `— → CREATED` via `POST /v1/payments` (новый paymentId). I should extend T1's trigger to also include `POST /v1/recurring-payments`. Let me update T1.

Let me make the edits precisely. Let me re-read the relevant section of state-machine.md to get exact strings.

I have the full content already from the earlier read. Let me construct edits.

T1 row:
```
| T1 | — | `CREATED` | `POST /v1/payments` (новый `paymentId`) | валидный запрос, ТСП активен | запись платежа + outbox-событие «регистрация в ОПКЦ» |
```
I'll change to:
```
| T1 | — | `CREATED` | `POST /v1/payments` (новый `paymentId`) или `POST /v1/recurring-payments` (`paymentType=RECURRING`) | валидный запрос, ТСП активен; для `RECURRING` — согласие `ACTIVE` и лимиты соблюдены (AD-009) | запись платежа + outbox-событие «регистрация в ОПКЦ» |
```

And add T13/T14 rows after T12.

T12 row:
```
| T12 | `COMPLETED` | (остаётся `COMPLETED`) | **частичный** возврат завершён | сумма возврата < суммы платежа | запись в `refunds[]`, вебхук `refund.completed` |
```

I'll add T13/T14 after T12.

Also, I should update §3 "Запрещённые переходы" or add a note about recurring. Maybe add a bullet. Actually, let me also add to §2 a note about `paymentType=RECURRING` skipping QR_ISSUED. I'll add a paragraph after the table.

And append section 7 for consent.

Let me do the edits. I'll do multiple edits to state-machine.md.

First edit: T1 row.
Second edit: add T13/T14 after T12 + a note.
Third edit: append section 7.

Let me be careful with exact strings.

Actually, let me just do targeted edits. Let me re-read the file to be 100% sure of exact whitespace. I already have it from the earlier read, but let me trust it since read_file returned exact content.

The T1 line exact:
"| T1 | — | `CREATED` | `POST /v1/payments` (новый `paymentId`) | валидный запрос, ТСП активен | запись платежа + outbox-событие «регистрация в ОПКЦ» |"

The T12 line exact:
"| T12 | `COMPLETED` | (остаётся `COMPLETED`) | **частичный** возврат завершён | сумма возврата < суммы платежа | запись в `refunds[]`, вебхук `refund.completed` |"

Section 6 ending:
"Маппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED`, `EXPIRED`, `REFUNDED` — без технических подсостояний (`ABS_PENDING`, `NOTIFY_PENDING` наружу не выставляются; `ABS_PENDING` отражается как `PAID` + поле `creditingStatus`)."

I'll append section 7 after that.

Let me make the edits.
Расширяю статусную машину: переход для рекуррентного списания (`CREATED → PAID` без QR) и новый раздел согласия.

  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/contracts/tsp-api.md", new_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n, old_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/contracts/tsp-api.md", new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`
  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/contracts/tsp-api.md", new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/contracts/tsp-api.md", new_string="## 7. Открытые вопросы (для A1)\n\n1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — road, old_string="## 7. Открытые вопросы (для A1)\n\n1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — road)`

Now update the contracts. First, tsp-api.md — add §3.6 (consents) and §3.7 (recurring payments), extend §5 webhooks, and extend §7 open questions.

Let me insert §3.6 and §3.7 after §3.5 (status return). The §3.5 ends with:
"### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`"

Then §4 starts:
"## 4. Ошибки (RFC 9457, Problem Details)"

I'll insert §3.6 and §3.7 between §3.5 and §4.

Let me also update §5 webhook events list to add consent events + paymentType. And §4 error codes to add CONSENT_NOT_ACTIVE, CONSENT_LIMIT_EXCEEDED, CONSENT_EXPIRED.

Let me plan the edits to tsp-api.md:

1. Insert §3.6 + §3.7 after §3.5.
2. Update §4 canonical error codes to add consent codes.
3. Update §5 event list to add consent.* events + note about paymentType.
4. Update §6 versioning note (maybe add a line about additive consent endpoints being backward compatible) — actually §6 already covers additive optional fields. I'll add a note in §7 open questions instead.

Let me do these edits.

For the §3.5 to §4 boundary, exact text:
```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`

## 4. Ошибки (RFC 9457, Problem Details)
```

I'll replace with the §3.5 content + new §3.6 + §3.7 + §4 heading.

Let me write §3.6 and §3.7.

§3.6 Согласия (подписки):
- `POST /v1/consents` — create consent
- `GET /v1/consents/{consentId}` — consent status
- `POST /v1/consents/{consentId}/revoke` — revoke consent

§3.7 Рекуррентные списания:
- `POST /v1/recurring-payments` — initiate recurring debit

Let me write it in the same style as the existing sections (with JSON examples, rules, notes).

Now let me write the edits.
Обновляю детальный контракт API ТСП — добавляю методы согласий и рекуррентных списаний, коды ошибок и события вебхуков.

  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/contracts/opkc-adapter.md", new_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t, old_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/contracts/opkc-adapter.md", new_string="| `refund.rejected` | возврат отклонён | `refundRef`, `reasonCode`, `reasonText` |\n| `consent.activated` | согласие подтверждено плательщи, old_string="| `refund.rejected` | возврат отклонён | `refundRef`, `reasonCode`, `reasonText` |\n| `transport.unavailable` | техническое: канал к НСПК н)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/contracts/opkc-adapter.md", new_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`/`consentId`) в каждый мутирующий вызов.", old_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.")`
  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/contracts/opkc-adapter.md", new_string="6. Эксплуатация: метрики, алерты, документация runbook.\n7. Поддержка рекуррентных платежей: методы `createConsent`/`getConsentStatus`/`rev, old_string="6. Эксплуатация: метрики, алерты, документация runbook.")`

I notice one issue: in the edit for §7 open questions, I accidentally introduced "Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4." — this is fine, unchanged. But wait, I see the result shows "3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4." Good, no issue. My new_string had "Модель подписи запросов ТСП (mTLS + подпись тела)" — yes that's correct. The earlier output in the tool result displayed "Модель подписи签名" — that was just a display glitch in the diff preview, not actual file content. The actual file should be correct. Let me verify by checking — actually the last edit result shows the correct text "Модель подписи запросов ТСП (mTLS + подпись тела)". Good.

Wait, actually there's a concern: the second edit result (the §7 open questions) shows correct Russian. But the FIRST tool result for the §7 edit showed "Модель подписи签名" which suggests a possible encoding issue in my new_string? No — let me look more carefully.

Actually looking back, the edit that showed "签名" was in the result of the SECOND tool call (the error codes edit) at line 215-223 — no wait. Let me re-read.

The tool results are:
1. First edit (insert §3.6/3.7) — success, shows lines 132-208.
2. Second edit (error codes) — success, shows lines 215-223.
3. Third edit (webhooks events) — success, shows lines 228-255.
4. Fourth edit (§7 open questions) — success, shows lines 263-269.

The fourth edit result shows:
"3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4."

Good, correct. No "签名" in the actual final content. The "签名" appeared in my earlier thinking? No, it didn't. Let me not worry — the displayed results all look correct.

Actually wait, I need to double-check: in the third edit result, the "Тело" section shows the example with `paymentType: "RECURRING"` and `consentId`. Good.

Now let me update opkc-adapter.md — add consent/recurring methods and events.

The opkc-adapter.md §3 table has methods. I'll add new rows: `createConsent`, `getConsentStatus`, `revokeConsent`, `createRecurringPayment`. And §4 events: add consent.* events. And §5 idempotency: note consent idempotency. And §7/§8 RFP: note vendor must support consent/recurring.

Let me find exact strings.

§3 table (rows):
```
| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |
```
This is the last row of §3 table. I'll add new rows after it.

§4 events list ends with:
```
| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |
```
I'll add consent events before or after. I'll add after `refund.rejected` row (before transport.unavailable) — actually order doesn't matter much, I'll add consent events after the `refund.rejected` row.

Let me find exact strings.

§3 last row:
"| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |"

§4 rows:
"| `refund.rejected` | возврат отклонён | `refundRef`, `reasonCode`, `reasonText` |
| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |"

§5 (idempotency) — add a bullet about consent. Actually §5 already covers reference-based idempotency for mutating calls. I can add a note that consent creation and recurring payment use the same reference mechanism (consentId/paymentId). I'll add a line.

§8 RFP requirement #4 (vendor requirements): "Идемпотентность мутирующих операций по `reference` (§5) — **обязательно**." I can add a requirement about consent methods. Let me add to §8 a new requirement #7 or extend #4. Actually, let me add a note to §7 (NFR) or §8. I'll add a new bullet to §8 requirements.

Let me also update §4 event list heading or add consent events properly. The §4 table has columns: "| Тип события | Смысл | Ключевые поля |". I'll add consent.* rows.

Let me make the edits.

For §3 table, I'll add after getReconciliationReport row:
```
| `createConsent` | регистрация согласия на рекуррентные списания в ОПКЦ | `reference` (= `consentId` ядра), `tspId`, `maxAmount`, `maxDebitsPerPeriod?`, `period?`, `validUntil`, `purpose?` | `ACCEPTED` (результат — событием) | 5 c |
| `getConsentStatus` | статус согласия | `consentId` | `PENDING` / `ACTIVE` / `REVOKED` / `EXPIRED` / `REJECTED` | 3 c |
| `revokeConsent` | отзыв согласия в ОПКЦ (по инициативе ТСП) | `consentId`, `reason?` | `ACCEPTED` (результат — событием) | 5 c |
| `createRecurringPayment` | инициация рекуррентного списания по согласию | `reference` (= `paymentId` ядра), `consentId`, `amount` | `ACCEPTED` (результат — событием `payment.paid`/`payment.rejected`) | 5 c |
```

For §4 events, add:
```
| `consent.activated` | согласие подтверждено плательщиком/ОПКЦ | `reference` (= `consentId` ядра), `activatedAt` |
| `consent.rejected` | согласие отклонено | `reference`, `reasonCode`, `reasonText` |
| `consent.revoked` | согласие отозвано (плательщиком) | `reference`, `revokedAt` |
| `consent.expired` | срок согласия истёк | `reference`, `expiredAt` |
```

Note: recurring payment result reuses `payment.paid`/`payment.rejected` events (the existing `payment.paid` event has `reference` = paymentId), so no new payment event needed. I'll add a note.

For §5, add a note line. §5 has:
"## 5. Идемпотентность и ссылки

- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов."

I'll update to include `consentId`:
"- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`/`consentId`) в каждый мутирующий вызов."

For §8, add requirement about consent. §8 list ends with:
"6. Эксплуатация: метрики, алерты, документация runbook."
I'll add:
"7. Поддержка рекуррентных платежей: методы/события согласий и `createRecurringPayment` (§3–4) с идемпотентностью по `reference` — **обязательно** (расширение G3/G4)."

Let me make these edits.
Обновляю контракт адаптера ОПКЦ — методы/события согласий и рекуррентных списаний + требования к вендору.

  `write_file(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/openapi/tsp-api.yaml", content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.1.0\n  description: Контракт API ТСП (draft). Пути /v1/consents и /v1/recu)`

Now update the openapi/tsp-api.yaml — rewrite with additive endpoints and schemas. I'll use write_file since it's a full rewrite (I have the exact original content and will reproduce + extend).

Actually, I should be careful: write_file requires that I've read the file (I have). I'll write the full new YAML.

Let me write the full openapi YAML preserving the original and adding the new parts.

Also add info.description? I'll keep minimal but add a version note. Actually I'll keep version 0.1.0 and not touch info beyond what's there. I'll add a description line to note additive recurring endpoints — but that's optional. I'll add a short `description` to info for clarity. Actually, minimal changes are safer. I'll just add paths + schemas, and extend Payment schema.

Let me write the full file.

I need to make sure the YAML is valid. Let me write it carefully.

Original + additions:

```yaml
openapi: 3.0.3
info:
  title: СБП-шлюз — API ТСП
  version: 0.1.0
  description: Контракт API ТСП (draft). Разделы /v1/consents и /v1/recurring-payments — аддитивное расширение для рекуррентных C2B-платежей (ADR-008); существующие методы /v1/payments не меняются.
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
          description: Согласие создано, ожидает подтверждения плательщиком
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
          description: Согласие отозвано
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Consent'}
  /v1/recurring-payments:
    post:
      operationId: createRecurringPayment
      parameters:
        - in: header
          name: Idempotency-Key
          required: true
          schema: {type: string}
      requestBody:
        required: true
        content:
          application/json:
            schema: {$ref: '#/components/schemas/RecurringPaymentRequest'}
      responses:
        '201':
          description: Рекуррентный платёж зарегистрирован
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
        paymentType:
          type: string
          enum: [QR, RECURRING]
          description: Тип платежа; по умолчанию QR (обратная совместимость)
        consentId:
          type: string
          description: Идентификатор согласия (заполняется при paymentType=RECURRING)
    ConsentRequest:
      type: object
      required: [tspId, maxAmount, validUntil]
      properties:
        tspId: {type: string}
        maxAmount: {type: integer, description: Максимальная сумма одного списания, в копейках}
        maxDebitsPerPeriod: {type: integer, description: Опциональный лимит числа списаний за период}
        period: {type: string, enum: [DAY, WEEK, MONTH], description: Период лимита частоты}
        validUntil: {type: string, format: date-time, description: Срок действия согласия (ISO 8601)}
        purpose: {type: string, description: Назначение подписки}
        merchantConsentRef: {type: string, description: Сквозной идентификатор согласия ТСП}
    Consent:
      type: object
      required: [consentId, tspId, status, maxAmount]
      properties:
        consentId: {type: string}
        tspId: {type: string}
        status: {type: string, enum: [PENDING, ACTIVE, REVOKED, EXPIRED, REJECTED]}
        maxAmount: {type: integer, description: Максимальная сумма одного списания, в копейках}
        maxDebitsPerPeriod: {type: integer}
        period: {type: string, enum: [DAY, WEEK, MONTH]}
        validUntil: {type: string, format: date-time}
        purpose: {type: string}
        merchantConsentRef: {type: string}
        createdAt: {type: string, format: date-time}
        activatedAt: {type: string, format: date-time}
        revokedAt: {type: string, format: date-time}
    RecurringPaymentRequest:
      type: object
      required: [consentId, amount]
      properties:
        consentId: {type: string}
        amount: {type: integer, description: Сумма списания, в копейках (не более maxAmount согласия)}
        merchantOrderId: {type: string}
        paymentPurpose: {type: string}
```

This is valid OpenAPI 3.0.3 YAML. Let me verify no issues:
- `format: date-time` is valid.
- The `info.description` uses a colon inside the string — it's a quoted? No, YAML plain scalar with colon followed by space would be a problem. "Разделы /v1/consents и /v1/recurring-payments — аддитивное расширение..." contains colons? Let me check: "рекуррентных C2B-платежей (ADR-008);" — no colon-space. Actually "СБП-шлюз — API ТСП" in title is fine (no colon). The description has "/v1/consents" — no colon. Good. But wait, plain scalar with ":" followed by non-space is OK; but I have "(ADR-008); существующие методы" — the ";" is fine. No ": " patterns. Actually "инфо description" — let me double check the description text: "Контракт API ТСП (draft). Разделы /v1/consents и /v1/recurring-payments — аддитивное расширение для рекуррентных C2B-платежей (ADR-008); существующие методы /v1/payments не меняются." No colon followed by space. Good.

Actually, to be safe and avoid YAML parsing issues with the description, I could drop the description entirely. But it's informative. I'll keep it but ensure no ": " — it's fine.

Wait, there's a subtle issue: in YAML, a plain scalar cannot contain ": " (colon followed by space). My description doesn't have that. Good.

Let me write the file.

Actually, one more consideration: should I keep `version: 0.1.0`? Yes, keep it. The additive change doesn't require a version bump (backwards compatible, still draft). I'll note in description.

Let me write it.
Обновляю `openapi/tsp-api.yaml` — аддитивные пути и схемы без изменения существующих методов.

  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/nfr.md", new_string="| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |\n\n## 7. Рекуррентные платежи (подписки по согласию) — NFR\n\nЦелев, old_string="| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |\n\n## Зависимости (внешние входы для NFR)")`
  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/solutioning.md", new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Рекуррентные C2B-, old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop)`
  `edit(file_path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/solutioning.md", new_string="4. Доступность АБС в ночные окна (влияет на SLA зачисления).\n\n## 11. Изменение: рекуррентные C2B-платежи (подписки по согласию) — ADR-008, old_string="4. Доступность АБС в ночные окна (влияет на SLA зачисления).")`

Now update nfr.md — add section 7 for recurrent payments. And update solutioning.md — add increment section + note автоплатежи in scope.

For nfr.md, append section 7 after section 6 and before "Зависимости". Let me find the exact boundary.

nfr.md ends:
"## 6. Наблюдаемость

| Метрика | Цель | Метод проверки |
...
| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |

## Зависимости (внешние входы для NFR)"

I'll insert section 7 between the end of section 6 and "## Зависимости".

Let me find the exact text. The last row of section 6 is:
"| Отчёт незавершённых операций | доступен всегда, актуален | Проверка |"

Then blank line, then "## Зависимости (внешние входы для NFR)".

I'll insert the recurrent NFR section.

Recurrent NFR section content:

## 7. Рекуррентные платежи (подписки) — NFR

| Метрика | Цель | Метод проверки |
|---|---|---|
| Latency «создание согласия» (POST /v1/consents) | p95 < 500 мс, p99 < 1 с (без учёта НСПК) | Нагрузочный тест, APM |
| Latency «инициация рекуррентного списания» | p95 < 500 мс | Нагрузочный тест |
| Активация согласия от нотификации НСПК | p95 < 5 с | Метрика лага очереди |
| Отзыв согласия (немедленный блок новых списаний) | ≤ 1 с от подтверждения до блокировки | Тест на отзыв |
| Зачисление по рекуррентному списанию от `payment.paid` | p95 < 60 с (как базовый NFR §2) | Метрика процесса |
| Throughput sustained (списания) | 200 TPS (в сумме с разовыми платежами) | Нагрузочный тест |
| Нарушение лимитов (сумма/частота) | 0 (все попытки отклонены) | Тест-кейсы негативных сценариев |
| Списание по отозванному/истёкшему согласию | 0 (отклонено `CONSENT_*`) | Тест-кейсы + fitness (AD-009/AD-010) |
| Потеря нотификации о согласии/списании | 0 (компенсируется сверкой) | Сверка с НСПК |
| Сверка по согласиям и списаниям | ежечасная с НСПК; расхождений 0 | Reconciliation-отчёт |
| Аудит жизненного цикла согласия | 100 % переходов в неизменяемом логе (AD-011) | Аудит, SIEM |

Зависимости: точные тайминги/лимиты согласия — по документации НСПК по автоплатежам [ТРЕБУЕТ ПРОВЕРКИ].

Let me also update the "Зависимости" section? No, I'll keep it; the recurrent dependency note is inside section 7.

Now solutioning.md — add increment section 11 and update §1 roadmap. Let me update §1 roadmap line.

§1 has: "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

I'll change to: "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты. Автоплатежи/рекуррентные списания — выведены из roadmap в scope: ADR-008."

And append section 11 after §10 "Открытые вопросы" (end of file).

§10 ends with:
"4. Доступность АБС в ночные окна (влияет на SLA зачисления)."

I'll append section 11.

Let me write the section 11 content:

## 11. Изменение: рекуррентные C2B-платежи (подписки по согласию) — ADR-008

Инкремент поверх принятого решения (см. `docs/adr/ADR-008-...`). Не переоткрывает §1–§10; добавляет:

- Новая сущность **согласие (consent)** со статусной машиной `PENDING → ACTIVE → REVOKED|EXPIRED|REJECTED` (spec §7).
- Новый тип платежа `paymentType=RECURRING` (`CREATED → PAID` без `QR_ISSUED`, spec §2 T13/T14).
- Новые инварианты spine **AD-009..AD-011**.
- Расширения контрактов: `openapi/tsp-api.yaml` (пути `/v1/consents*`, `/v1/recurring-payments`), `docs/contracts/tsp-api.md` (§3.6–3.7), `docs/contracts/opkc-adapter.md` (методы/события согласий).
- Новый раздел NFR `docs/nfr.md` §7.

Маршрут: **Major (10/15)**; требует A3-решения человека (регуляторная валидация модели согласия, протокол НСПК для автоплатежей — [ТРЕБУЕТ ПРОВЕРКИ], расширение scope RFP вендора).

Let me now make these edits.

Actually, for solutioning.md §1, the exact text is:
"Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

I'll edit the roadmap sentence.

Let me do the edits.
Добавляю раздел NFR для рекуррентных платежей и инкрементную секцию в solutioning.

  `grep_search(pattern="<!--", path="<HARNESS>/runs-clean/cells/wh4hwzh/ws/docs/adr")`
  `grep_search(pattern="签名|TODO|TBD|XXX", path="<HARNESS>/runs-clean/cells/wh4hwzh/ws")`
  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wh4hwzh/ws && python3 -c \"import yaml,sys; yam, description="Validate YAML and fitness rules")`

All edits are done. Now let me verify:
1. The CONSTRAINTS.yaml fitness rules: 
   - `adr-no-placeholders`: `must_not_contain glob "docs/adr/*.md" pattern '<!--'`. My new ADR-008 must not contain `<!--`. Let me verify by grep.
   - `nfr-measurable`: `must_contain glob "docs/nfr.md" pattern '99,95'`. Still there (section 1 unchanged).
   - `spine-lints-clean`: `must_not_contain glob "ARCHITECTURE-SPINE.md" pattern 'TODO|TBD|XXX'` (warn). My spine additions don't contain those.
   - `abs-credit-only-from-paid`: ADR-005 unchanged, still contains 'только из состояния `PAID`'.

2. Validate the openapi YAML is syntactically valid.

3. Check git status to list changed files.

Let me run a few verification commands:
- grep for `<!--` in docs/adr/ (should be empty).
- Validate YAML syntax of openapi (python yaml load or a yaml check). Let me try `python3 -c "import yaml; yaml.safe_load(open(...))"`.
- git status / diff --stat.

Let me run these.

Actually, let me also double check the tsp-api.md — there was a concern about "签名" appearing. Let me grep for any suspicious characters (non-Cyrillic/CJK). Let me grep for "签名" to be safe. Actually the tool output showed "Модель подписи签名" in one preview, but that might have been a rendering artifact. Let me grep for "签名" in the file.

Let me run verification commands in parallel.
Все изменения внесены. Проверяю целостность: fitness-правила (нет HTML-комментариев в ADR), валидность YAML и отсутствие артефактов кодировки.

  `run_shell_command(command="cd <HARNESS>/runs-clean/cells/wh4hwzh/ws && git status --short && echo '---ST, description="Show changed and new files")`

All checks pass:
- No `<!--` in docs/adr (adr-no-placeholders satisfied).
- No "签名"/TODO/TBD/XXX anywhere (the "签名" concern was just a display artifact).
- YAML OK.
- nfr-measurable: '99,95' count = 2 (still present).
- abs-credit-only-from-paid: 'только из состояния `PAID`' count = 1 (unchanged).

Now let me check git status/diff to list the changed files, and verify the ADR-008 file renders correctly (quick check of the key sections). Let me run git status.

Actually, let me also verify the tsp-api.md didn't get the "签名" artifact. The grep for "签名" returned no matches across the whole workspace, so the file is clean. Good.

Let me get the git status to produce the final file list.
Все проверки прошли. Собираю итоговый список изменений через git.


All changes are in place. Let me produce a concise final summary in Russian, mapping the 7 requested deliverables to the files, and listing created/changed files.

I should keep the final response concise but complete, covering the 7 deliverables briefly, and list files.

Let me write the final summary.
Готово. Архитектурный пакет изменения «Рекуррентные C2B-платежи СБП (подписки по согласию)» собран поверх принятого решения, в принятой в репозитории форме (ADR + spine + контракты + статусная машина + NFR + openapi). Код не писал.

## Ответы на 7 пунктов задачи (где это отражено)

1. **Оценка значимости и маршрута** — `ADR-008` §1: маршрут **Major (10/15)**, инкремент поверх Critical-решения; полное перепроектирование не требуется, обязательное A3-решение человека.
2. **Влияние на инварианты** — `ADR-008` §2 (таблица по AD-001..AD-008: что расширяется/что нет) + новые инварианты **AD-009..AD-011** в `ARCHITECTURE-SPINE.md` (Proposed, ADR-008).
3. **Архитектурное решение** — `ADR-008`: A3-пакет (choice `consent-first-class`), альтернативы (delegate-to-opkc / full-vendor / separate-engine / флаг на ТСП / батч), последствия, обратимость (reversible).
4. **Контракты без поломки** — `openapi/tsp-api.yaml` (аддитивные пути `/v1/consents*`, `/v1/recurring-payments`; `Payment` расширен опциональными `paymentType`/`consentId`, существующие методы не тронуты) + детализация в `docs/contracts/tsp-api.md` и `docs/contracts/opkc-adapter.md`.
5. **Измеримые NFR** — `docs/nfr.md` §7 (латентность согласия/списания, время отзыва ≤1 с, throughput 200 TPS, 0 нарушений лимитов/списаний по отозванному согласию, аудит 100%).
6. **Критерии приёмки и план отката** — `ADR-008` §§ «Критерии приёмки» (9 проверяемых пунктов, включая негативные сценарии) и «План отката» (фиче-флаг stop-new, сигналы, владелец решения, критерий успешного отката).
7. **Что остаётся человеку** — `ADR-008` §9: регуляторная валидация модели согласия, точный протокол НСПК по автоплатежам `[ТРЕБУЕТ ПРОВЕРКИ]`, расширение scope RFP вендора, продуктовая модель подписок, UX/канал отзыва, ратификация AD-009..011.

## Файлы

**Создан:**
- `docs/adr/ADR-008-rekurrentnye-c2b-platezhi-podpiski-po-soglasiyu.md`

**Изменены (принятым способом — расширение, не переписывание):**
- `ARCHITECTURE-SPINE.md` — инварианты AD-009..AD-011
- `docs/spec/state-machine.md` — переходы T13/T14 (`CREATED → PAID` без QR) + раздел согласия §7
- `docs/contracts/tsp-api.md` — §3.6–3.7, коды ошибок `CONSENT_*`, события вебхуков
- `docs/contracts/opkc-adapter.md` — методы/события согласий, требования вендору
- `openapi/tsp-api.yaml` — аддитивные пути и схемы
- `docs/nfr.md` — раздел §7
- `docs/solutioning.md` — scope-правка (§1) + инкрементный раздел §11

## Проверка
Fitness-правила не нарушены: `nfr-measurable` (есть `99,95`), `abs-credit-only-from-paid` (есть `только из состояния PAID`), `adr-no-placeholders` (нет `<!--` в `docs/adr/*.md`), spine без `TODO/TBD/XXX`; `openapi/tsp-api.yaml` валиден (YAML OK). Изменения не закоммичены — оставил в рабочем дереве для ревью/A3.
