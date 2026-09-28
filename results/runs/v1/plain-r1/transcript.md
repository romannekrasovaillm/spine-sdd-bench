<!-- источник: <HARNESS>/runs/cells/plain-r1/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-cells-plain-r1-ws/chats/b862c32f-a3c4-46ae-a9f4-cd2127dfdf90.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `glob(pattern="**/*")`

Let me start by understanding the repository. The user wants me to act as a solution architect and prepare an architectural package for adding recurring C2B debits (subscriptions) to an existing accepted solution for a "Платёжный шлюз СБП (C2B-приём)".

Key constraints:
- Don't write code.
- Use the repository's established methods for changing accepted solution files.
- Check if there are methodological skills/tools installed in the project.

Let me first explore the repository thoroughly. I need to read:
- `ARCHITECTURE-SPINE.md` (invariants AD-001…AD-008)
- `docs/` (solutioning, NFR, ADR-001…007, contracts, state machine)
- `openapi/tsp-api.yaml`
- `.arch-handoff/` (rules and handoff package)

Let me check the available skills. There's a "new-app" skill for new applications, but this is not a new application. There might be project-specific skills/tools. Let me check if there are methodological skills installed in the project.

The system reminder lists bundled skills. I should check if there are project-level skills. The `.arch-handoff/` directory might contain rules about how to change files.

Let me start by exploring. This is a significant architecture task, so I should be thorough. Let me use parallel tool calls to read key files.

First, let me get an overview of the whole structure.
Начну с изучения принятого решения и методических правил репозитория, прежде чем готовить пакет изменения.

  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/.arch-handoff/RUBRIC.yaml")`

Let me read the key files. I'll start with the spine, handoff rules, and README, then the docs.

  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/spec/state-machine.md")`

Now let me read the docs in detail: solutioning.md, nfr.md, contracts (tsp-api.md, opkc-adapter.md), state-machine.md, and all ADRs. Also the openapi/tsp-api.yaml.

  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/adr/ADR-001-outbox.md")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/adr/ADR-002-model-konsistentnosti-plate)`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/adr/ADR-005-integraciya-s-abs-zachislen)`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/adr/ADR-007-proposed-a3.md")`

Now let me read the ADRs and the openapi tsp-api.yaml.

  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/openapi/tsp-api.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/.arch-handoff/ARCHITECTURE.md")`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/rfp/vendor-rfp.md")`

Now let me read the openapi/tsp-api.yaml and the .arch-handoff/ARCHITECTURE.md, and check the vendor-rfp.md.

  `run_shell_command(command="cd <HARNESS>/runs/cells/plain-r1/ws && ls -la && echo \"--- .qwen ---\" && ls, description="Проверка проектных навыков и конфигураций")`

Now I have a comprehensive understanding of the repository. Let me also check if there's a project-level skill/methodological tool. The system reminder listed bundled skills. The task mentions "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению."

Let me check if there are any project-level skills in the .qwen directory or similar. Actually, let me check if there's a QWEN.md or AGENTS.md, or project skills. The structure only shows what I've read. There don't appear to be any project-specific skills beyond the bundled ones. Let me check for any skill files.

Actually, let me look more carefully. The available skills are all bundled. There's no project-specific skill listed. Let me check if there might be a `.qwen/` directory with project skills or commands.

Let me check the workspace for any hidden config files.

  `run_shell_command(command="cd <HARNESS>/runs/cells/plain-r1/ws && echo \"=== diff .arch-handoff/adr/ADR-, description="Проверка связи .arch-handoff и docs, статус git")`

No project-specific skills/commands, no QWEN.md/AGENTS.md. So the methodological tools are the bundled skills and the repository's own conventions (`.arch-handoff/`, `docs/adr/`, `docs/` structure, `ARCHITECTURE-SPINE.md`).

Let me review the `docs/contracts/nspk-contract.md` reference — it's referenced but doesn't exist (created after NSPK documentation). And there's no `docs/contracts/nspk-contract.md` in the file list. Correct.

Now I understand the repository's conventions for changing the accepted solution:
1. **ADRs** go in `docs/adr/ADR-XXX-slug.md` with a specific format: Date, Status, Owner, Related, Context, Decision, Alternatives Considered, Consequences (Positive/Negative), Reversibility, References.
2. **Spine invariants** go in `ARCHITECTURE-SPINE.md` as AD-XXX blocks, but changing spine is governed by rules — the spine says "Родительский spine ... Локальное переопределение родительских ограничений запрещено; конфликт эскалируется наверх." So the spine is for accepted invariants. New change needs to go through ADR first (Proposed status), and spine blocks marked "Proposed" act after ratification of the corresponding ADR.
3. **Contracts** — `docs/contracts/tsp-api.md` (human-readable) and `openapi/tsp-api.yaml` (machine-readable). Both need to stay in sync. The `docs/contracts/tsp-api.md` has versioning rules (§6): additive optional fields are backwards compatible, breaking changes → /v2 with ≥6 months support.
4. **NFR** — `docs/nfr.md` with measurable targets.
5. **State machine** — `docs/spec/state-machine.md`.
6. **solutioning.md** — full design doc.

Now, the task: The business wants **recurring C2B debits by payer consent (СБП subscriptions)**. Currently each payment requires QR and customer action. This is essentially "autopayments" / "подписки СБП" — which in the real СБП world is the "СБП: автоплатёж" / recurring payments with a pre-authorized mandate (согласие плательщика). Note the solutioning.md explicitly lists "автоплатежи" as out of scope / roadmap. And the spine's Deferred section mentions "Диспуты/претензии" etc. Actually it doesn't mention autopayments specifically; the solutioning.md says "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

So this is a significant feature-level change to the accepted architecture. It introduces a new concept: **платёжное согласие (mandate/consent)** that authorizes the ТСП to initiate debits without per-payment QR/customer action.

I need to produce a **package** (not code) that:
1. Assessment of significance and route (how deep design is needed and why).
2. Impact on accepted architecture: which invariants are touched, what changes, what doesn't.
3. Architectural decision with considered alternatives, consequences, reversibility.
4. Contract changes (`openapi/tsp-api.yaml`) without breaking existing consumers.
5. Measurable NFRs for the new functionality.
6. Acceptance criteria and rollback plan.
7. What remains for a human architect to decide and why.

And I must only change the accepted solution files in the way accepted in this repo (ADR format, spine, contracts, NFR, state machine, solutioning).

Now, the key question: how deep should I go? The task says "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям."

So I need to produce a set of documents (files) that:
- Assess significance and route (this is a doc, maybe in solutioning or a separate ADR / a "route" assessment).
- Impact on spine (which invariants touched).
- An ADR (or multiple ADRs) for the recurring debits feature.
- Contract changes (openapi + tsp-api.md).
- NFR additions.
- Acceptance criteria + rollback plan.
- Human-decide open questions.

Let me think carefully about the actual domain and design, because this is the core value of the deliverable.

## Understanding СБП recurring payments / subscriptions

In the СБП (System of fast payments) in Russia, there is a mechanism for "автоплатежи" / recurring payments. Actually, the official СБП has a service called "СБП: автоплатёж" (recurring payment / подписка). It works via a **согласие плательщика (consent/mandate)** — the payer gives consent in their bank's app to allow a specific merchant (ТСП) to debit their account for recurring payments (subscriptions), up to a certain limit / frequency. The merchant then initiates debits against this consent without needing the payer to scan a QR each time.

Key concepts:
- **Согласие (consent / mandate / подписка)**: an authorization by the payer, given in the payer's bank app (СБП consent flow), linking a payer's account to a merchant + subscription terms (max amount per debit, frequency, validity period, purpose).
- **Списание по согласию (recurring debit)**: merchant triggers a debit referencing the consent; СБП processes it without the payer's active confirmation (or with a push confirmation depending on rules).
- **Отмена/приостановка согласия**: payer or merchant can revoke.

This is a different flow from the existing one-shot QR payment. The existing architecture has:
- `CREATED → QR_ISSUED → PAID → CREDITED → COMPLETED` state machine for one-shot payments.
- The opkc-adapter contract has `createPaymentLink` (QR registration).

For subscriptions, we need a new set of concepts:
1. **Согласие (Consent/Mandate)** — new entity with its own lifecycle (ACTIVE → SUSPENDED → REVOKED → EXPIRED).
2. **Рекуррентное списание (Recurring debit)** — an operation that references the consent and produces a payment (or a debit) without QR.

Important architectural question: Is the recurring debit a *payment* in the existing state machine, or a new entity? The safest design: a recurring debit **reuses the payment state machine** but with a different entry transition (no QR_ISSUED — the consent replaces the QR authorization). So:

- Consent registration: `POST /v1/consents` (merchant creates a consent request) → payer confirms in their bank app → consent becomes ACTIVE → notify merchant via webhook.
- Recurring debit: `POST /v1/consents/{consentId}/debits` (or `POST /v1/payments` with `paymentMethod=recurring` + `consentId`) → creates a payment that skips QR_ISSUED, goes to a "consent-authorized" state, then PAID → CREDITED → COMPLETED.

Actually the key design decision is whether the consent is managed by the СБП (НСПК) itself (there's a "СБП автоплатёж" service where НСПК manages consents) or by the gateway. In the real world, НСПК manages consents via its "СБП: автоплатёж" — the consent is registered in НСПК (or in the payer's bank), and НСПК notifies about consent events. The bank-эквайер's gateway needs to:
1. Register a consent with ОПКЦ (via adapter).
2. Receive consent status notifications (ACTIVE, REVOKED, EXPIRED, SUSPENDED).
3. Initiate debits against the consent.

This is important because it means the consent lifecycle is driven by НСПК events, and the gateway's adapter (opkc-adapter) needs new methods and events:
- `createConsent` (register consent in ОПКЦ)
- `getConsentStatus`
- `cancelConsent` / `revokeConsent`
- `createRecurringDebit` (initiate debit against consent)
- events: `consent.activated`, `consent.revoked`, `consent.expired`, `consent.suspended`, `debit.paid`/`debit.rejected` etc.

Since the protocol details are external (`[ТРЕБУЕТ ПРОВЕРКИ]`), the design must keep the consent concept at the gateway level (contract-level) and normalize НСПК specifics in the adapter — consistent with AD-008 (ядро контрактно-независимо от транспорта).

This is a big change. It touches:
- **New entity**: Consent (согласие) with its own state machine.
- **New flow**: recurring debit.
- **Spine**: AD-001..AD-008 — do they need to change? Let me think:
  - AD-001 (изоляция платёжного контура) — unchanged, but "Binds" might need to include consent.
  - AD-002 (единый источник истины — статусная машина платежа) — the consent adds a second state machine; the invariant is about "платежа" — need to extend or add a new invariant AD-009 for consent. The rule about "Изменение финансового статуса платежа и запись исходящего события (outbox) в одной локальной транзакции" applies to consent too.
  - AD-003 (идемпотентность) — extends to consent and recurring debits (Idempotency-Key on consent/debit creation, eventId dedup, consentId/debitId for АБС).
  - AD-004 (единственный адаптер ОПКЦ) — unchanged; adapter gets new methods but the invariant "протокол НСПК знает только адаптер" holds.
  - AD-005 (зачисление только из подтверждённого статуса) — for recurring debits, the "confirmed status" is now the debit PAID status (confirmed by НСПК). The invariant still holds: зачисление only from PAID. But need to make sure a recurring debit that is authorized by consent still requires the НСПК confirmation (PAID) before АБС credit. So AD-005 holds, extended to debits.
  - AD-006 (trust-зоны) — unchanged.
  - AD-007 (НПС/КИИ/ПДн) — consent involves payer data (согласие = ПДн), need consent-specific ПДн handling (minimization, retention). Extends AD-007.
  - AD-008 (гибрид) — unchanged (adapter still vendor's).

So the change touches AD-001..AD-005 and AD-007 conceptually, but the core invariants largely hold. The cleanest approach: add a **new spine invariant AD-009 (согласие плательщика)** and possibly AD-010 (рекуррентное списание), and note in the impact analysis which existing invariants are extended vs unchanged. But the spine rules say "Локальное переопределение родительских ограничений запрещено" — adding new ADs is fine; changing existing ADs requires care. Since existing ADs are "Proposed" status (except AD-008), I should be careful. The impact analysis should distinguish "инварианты, которые надо расширить" vs "инварианты, которые не меняются".

Actually, let me re-read the task requirement 2: "Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет." So I need to produce this analysis. It doesn't necessarily mean I must edit the spine — but I should produce an impact analysis doc. The spine itself I should only change "тем способом, который принят в этом репозитории" — which means new ADs as new blocks in ARCHITECTURE-SPINE.md (marked Proposed, referencing the ADR), and possibly updating the Deferred section (remove "автоплатежи" from roadmap/out-of-scope since now it's in scope).

Let me plan the deliverables. The accepted convention for a "change package" here seems to be:
1. **ADR(s)** in `docs/adr/` — the architectural decision document. This is the primary artifact.
2. **Spine updates** in `ARCHITECTURE-SPINE.md` — new AD blocks + Deferred update.
3. **Contract updates** — `docs/contracts/tsp-api.md` + `openapi/tsp-api.yaml`.
4. **State machine** — `docs/spec/state-machine.md` (add consent state machine + recurring debit transitions) OR a new `docs/spec/consent-state-machine.md`.
5. **NFR** — `docs/nfr.md` additions.
6. **solutioning.md** — add a section, OR a new change-specific solutioning doc.

But wait — the task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." This means I should follow the repo's conventions. The repo has a clear pattern: ADRs are standalone files with the slug naming. Spine is the invariant register. Contracts in two places (md + yaml). NFR in nfr.md. State machine in spec/.

The most important consideration: **Don't over-engineer / don't make it too deep**. The task asks for an assessment of route (how deep). Let me think about what's the right granularity.

Given the existing repo is at "решение подготовлено, ожидает человеческого решения A3 по стратегии реализации (ADR-007) и получения документации НСПК", and now a NEW feature (recurring debits) arrives, this is a **feature-level change on top of a Critical-route initiative**. The right move is:

- This is a **significant change** (новый финансовый продукт, новые сущности, новый контур согласий, ПДн согласий, новые регуляторные аспекты). It warrants its own ADR (or a small set) + contract extension + NFR + acceptance/rollback. Not a full re-open of ADR-001..007.

The route assessment: The feature reuses the established architecture (isolation, outbox, state machine, adapter). It does NOT re-open ADR-001 (topology), ADR-003 (transport), ADR-006 (trust), ADR-007 (strategy). It EXTENDS ADR-002 (state machine — add consent), ADR-005 (АБС — recurring debit is still "credit from PAID"), and the adapter contract. So the route is: **Medium depth — a new ADR (ADR-008) for the consent/recurring-debit model + contract/NFR/state-machine extensions, reusing the existing Critical route gates A0-A5.** The human decision needed: (1) scope confirmation (is this "СБП автоплатёж" — consent held by НСПК/payer bank — or a gateway-side mandate?), (2) business rules for consent limits/frequency, (3) regulatory classification (is a recurring debit a "перевод" requiring the same 161-ФЗ protection, does it need explicit consent capture — 152-ФЗ legal basis).

Wait — I should double-check the actual СБП mechanism to be accurate. But I don't have internet necessarily. Actually I can rely on domain knowledge. The key architectural facts I need:
- СБП has a "СБП автоплатёж" (recurring payment) service. The consent is created in the payer's bank mobile app (like a standing order / subscription). НСПК acts as the central operator. The merchant (ТСП) initiates the debit, НСПК routes to the payer's bank, which debits the payer's account per the consent.
- There's also "платёж по согласию" — the payer gives consent for a specific merchant to debit within limits.

For the architecture, the exact protocol is `[ТРЕБУЕТ ПРОВЕРКИ]`, so I keep it abstract and mark it.

Now, a critical architectural nuance: **where does the consent live?** Options:
- (A) Consent managed by НСПК/ОПКЦ (the "автоплатёж" service): gateway registers consent request → НСПК → payer's bank captures consent → НСПК notifies ACTIVE. Debits reference the consent in НСПК. This aligns with AD-004/AD-008: the protocol lives in the adapter, gateway knows only the normalized consent contract.
- (B) Consent managed by the gateway itself (gateway stores consent, generates a QR/token for first payment, then repeats). This is a "card-on-file"-like approach and NOT how СБП автоплатёж works — СБП debits need payer's bank authorization each time unless НСПК has a consent.

The correct architecture for СБП автоплатёж is (A): **consent is a first-class object in the СБП (НСПК) ecosystem**, gateway registers consent with ОПКЦ, receives consent lifecycle events, and initiates debits against the consent. The gateway stores a **projection** of the consent (its own state machine) for idempotency/status, but the **authoritative consent** is in НСПК/payer's bank.

This is an important point for the ADR: the consent's source of truth is ОПКЦ (НСПК), while the gateway keeps a projection (like the payment state machine keeps payment state but НСПК is authoritative on PAID). Actually wait — for payments, the gateway's БД IS the "единый источник истины" per AD-002, with НСПК being an external actor. For consent, the consent lifecycle events come from НСПК, and the gateway projects them. There's a subtlety: is the gateway's consent state machine the "source of truth" or a projection of НСПК? I'll argue: the gateway's consent state machine is the **gateway's source of truth for its own operations** (idempotency, orchestration), but the **legal/financial authority of the consent** is in НСПК/payer's bank; a debit is only financially valid if НСПК confirms it. This mirrors the existing "PAID is confirmed by НСПК" model and keeps AD-002/AD-005 consistent.

OK, I have enough to design. Let me also think about the **contract changes** carefully, since the task explicitly requires (4) "Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей."

The existing openapi/tsp-api.yaml is minimal (just createPayment + getPayment). It's actually out of sync with docs/contracts/tsp-api.md (which has more endpoints: register TSP, refunds, etc.). Interesting — the yaml is a skeleton. But the task specifically says to change `openapi/tsp-api.yaml`. I should:
- Add new endpoints for consent and recurring debits as **additive** changes (new paths, new optional fields) — backwards compatible.
- Add new schemas: `Consent`, `ConsentRequest`, `RecurringDebit` (or extend `PaymentRequest` with optional `consentId`).
- Add new webhook event types (`consent.activated`, `consent.revoked`, `debit.completed`, etc.).

Since the yaml is minimal, I'll extend it in a backwards-compatible way: 
- New paths: `/v1/consents` (POST), `/v1/consents/{consentId}` (GET), `/v1/consents/{consentId}/debits` (POST), maybe `/v1/consents/{consentId}/revoke` (POST).
- Extend `PaymentRequest` with optional `consentId` and `paymentType` field (defaulting to existing behavior) OR add a distinct `RecurringDebitRequest`. To avoid breaking existing consumers, the cleanest is: keep `POST /v1/payments` unchanged, add a new `paymentType` enum field with default `ONE_SHOT` — but changing the enum with a new optional field is backwards compatible. Alternatively, add a dedicated `POST /v1/consents/{consentId}/debits` endpoint. I think the cleanest and most semantically clear is a dedicated endpoint for debits, but I should also consider whether the merchant wants "create a recurring debit" vs "create a payment with consent". 

Actually, for merchants, the recurring debit IS a payment (they get paid). The natural API is: the merchant creates a consent first (subscription signup), then each billing cycle creates a debit (which results in a payment credited to them). So:
- `POST /v1/consents` — create consent (subscription) → returns consentId + status PENDING (awaiting payer confirmation).
- `GET /v1/consents/{consentId}` — consent status.
- `POST /v1/consents/{consentId}/debits` — create recurring debit → returns a `paymentId`/`debitId` and its status (this reuse the payment state machine).
- `POST /v1/consents/{consentId}/revoke` — merchant revokes (or payer revokes → webhook).

And webhooks: `consent.activated`, `consent.revoked`, `consent.expired`, `consent.suspended`, plus existing `payment.completed`/`payment.failed` for the debits (since debits reuse payment state machine, the webhooks can be reused, or new `debit.*` events). I'll reuse `payment.*` events but add a `consentId`/`paymentType` field in the payload, and add `consent.*` events.

To be safe and minimal, I'll:
1. Extend `PaymentRequest` with optional `consentId` (string) and `paymentType` (enum, default `ONE_SHOT`). This keeps `POST /v1/payments` working for both one-shot and consent-based debits. But actually the consent-debit has different required params (no amount? amount must be ≤ consent limit). Hmm.

Let me settle on the cleanest backwards-compatible design:

**Design decision (to present as ADR):** introduce a distinct **Consent** resource and a **Recurring debit** that reuses the payment state machine with a consent-authorized entry. API:
- `POST /v1/consents` (Idempotency-Key) → create consent → 201 {consentId, status: PENDING}
- `GET /v1/consents/{consentId}` → consent status + terms
- `POST /v1/consents/{consentId}/debits` (Idempotency-Key) → create debit → 201 {debitId, paymentId, status: PAYMENT_PROCESSING...} — actually returns a Payment-like object
- `POST /v1/consents/{consentId}/cancel` (merchant-initiated revoke)
- webhooks: consent.activated / consent.revoked / consent.expired / consent.suspended; debit results reuse payment.completed/failed with consentId.

This is fully additive: existing `/v1/payments` and `/v1/payments/{id}` unchanged; existing consumers unaffected.

I'll present this in the ADR and in the contract changes.

Now for the **state machine**, I need to add:
- **Consent state machine**: `PENDING → ACTIVE → REVOKED | EXPIRED | SUSPENDED` (with SUSPENDED → ACTIVE possible).
- **Recurring debit** — reuses payment machine but entry differs: instead of `CREATED → QR_ISSUED → PAID`, a debit goes `DEBIT_CREATED → DEBIT_PROCESSING → PAID → CREDITED → COMPLETED` (or reuses `CREATED → PAID` without QR). Simplest: a recurring debit enters the payment state machine at `CREATED` with `paymentType=recurring` and transitions `CREATED → PAID` directly (skipping QR_ISSUED), guarded by `consent.status == ACTIVE` and amount ≤ consent limit. Then PAID → CREDITED → COMPLETED as before. On НСПК rejection (consent revoked / limit exceeded / insufficient funds) → FAILED.

This reuses AD-005 (credit only from PAID) cleanly.

Important invariants for the debit:
- A debit must only be created when consent is ACTIVE and amount ≤ consent.maxAmount and within validity period and frequency limits.
- The debit's PAID must be confirmed by НСПК (not assumed from consent alone) — this preserves AD-005.

Now, the **significance/route assessment**: This is a **Major/Critical feature** because:
- New financial product (recurring debits) = new money movement type.
- New entity (consent) with regulatory implications (152-ФЗ consent = ПДн/правовое основание; 161-ФЗ protection of transfers; НСПК "автоплатёж" rules).
- New integration surface (consent lifecycle events from НСПК, new adapter methods).
- BUT: reuses existing spine (isolation, outbox, state machine, adapter, АБС credit-from-PAID). No re-open of topology/transport/trust/strategy.

Route: **не требуется полный Solutioning с нуля** — требуется **инкрементальное проектирование на уровне feature**: новый ADR (или 2 ADR: consent model + recurring debit flow) + расширение spine (новый AD-009, возможно AD-010) + контракты + NFR + state machine + acceptance/rollback. Проходит через те же гейты A0–A5, но с фокусом на новые артефакты. Human decision needed on: scope/подтверждение что это именно «СБП автоплатёж» (consent у НСПК), бизнес-правила (лимиты, частота, отмена), регуляторная классификация, и согласование с НСПК протокола согласий.

Now let me decide the **concrete files to create/change**. Following repo conventions:

**Create:**
1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md` — the ADR (main decision). Number it ADR-008 (next after 007). Slug in Russian lowercase as per existing convention. Actually existing slugs are in Russian transliteration: "ADR-001-outbox.md", "ADR-002-model-konsistentnosti-platezha-konechnyy-avtomat-s-idempotentnostyu-na-urovne-shlyuza.md". So slug should be descriptive. Let me use `ADR-008-rekurrentnye-c2b-spisaniya-soglasie-platelshchika.md`.

Wait — should I split into 2 ADRs (consent model + recurring debit) or 1 ADR? The existing repo has granular ADRs (7 ADRs for one initiative). For a feature, a single ADR covering the consent + recurring debit is appropriate and keeps it manageable. But the consent lifecycle and the debit flow are separable concerns. I think **one ADR** is right for a feature-level decision, with clear sections. Actually, let me consider: the change has two tightly-coupled aspects (consent entity + debit flow) that are really one product decision. I'll do **one ADR (ADR-008)** with the full decision, alternatives, consequences, reversibility. That matches "3. Архитектурное решение с рассмотренными альтернативами".

Actually, re-reading the task: "3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью." — singular "решение". So one ADR is appropriate.

2. `docs/adr/` — also maybe an impact/route doc. Where does the "Оценка значимости и маршрута" (item 1) and "Влияние на инварианты" (item 2) go? These could be a separate document. The repo doesn't have a "route assessment" doc type explicitly. Options:
   - Put item 1 and 2 into the ADR's Context/Consequences (partially).
   - Create a dedicated `docs/change/` or add to solutioning.md a section "Изменение: рекуррентные C2B-списания".

Actually, the cleanest is to add a dedicated document for the change package that the human architect reviews, and reference the ADR. But to follow repo conventions tightly, I think:
   - The **ADR (ADR-008)** is the architectural decision (item 3).
   - A **route/impact assessment** can be a short section at the top of the ADR or a separate doc. Given the task asks for a "пакет", and the repo's `.arch-handoff/` shows that a "handoff package" has TASK/CONSTRAINTS/MANIFEST/RUBRIC/ARCHITECTURE, but that's for code handoff, not for this.

I think the most idiomatic approach is:
   - Add a **new section to `docs/solutioning.md`** OR create a **change-specific solutioning document** `docs/solutioning-recurrent.md`. Hmm. Actually solutioning.md is the "full design" for the base initiative. The recurrence feature is a feature-level increment. I'll create a dedicated document: `docs/adr/ADR-008-...` for the decision, and put the significance/route/impact/NFR/acceptance/rollback into... 

Let me reconsider. The 7 required deliverables map naturally to:
1. Оценка значимости и маршрута → a section, could go in the ADR Context + a dedicated "route" note. I'll put a concise "Маршрут и значимость" section in the ADR, and also reflect it in solutioning.md's section 1/5 (update roadmap: автоплатежи now in scope).
2. Влияние на инварианты → the ADR's "Влияние на spine/инварианты" section + the actual spine edit (new AD-009/AD-010, Deferred update).
3. Архитектурное решение → ADR-008.
4. Изменения контрактов → `docs/contracts/tsp-api.md` + `openapi/tsp-api.yaml`.
5. Измеримые NFR → `docs/nfr.md` (new section).
6. Критерии приёмки и план отката → could go in the ADR's Consequences/Reversibility + a dedicated acceptance section. The repo has acceptance criteria in nfr.md (as "метод проверки") and solutioning.md §7 gates + §8 rollback. I'll add acceptance/rollback to the ADR and/or a dedicated doc. I think a dedicated section in the ADR is cleanest, but the repo pattern puts rollback in solutioning.md §8. Since this is a feature increment, I'll add acceptance + rollback into the ADR (self-contained) AND note it references the base solutioning gates.
7. Остаётся на решение человека → the ADR's "Открытые вопросы" / "Human decision" section.

Actually, the repo convention is strong on **self-contained ADRs**. I'll make ADR-008 the centerpiece containing: significance/route, impact on invariants, decision, alternatives, consequences, reversibility, acceptance criteria, rollback, human-decide questions. Then I'll make the **actual file edits** to the other accepted-solution files (spine, contracts, NFR, state machine, solutioning) as the "изменение принятых файлов решения".

So the file changes:

**Create:**
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md` (the ADR — centerpiece)

**Edit:**
- `ARCHITECTURE-SPINE.md` — add AD-009 (согласие плательщика) and AD-010 (рекуррентное списание) blocks, update Deferred section (remove автоплатежи from roadmap).
- `docs/contracts/tsp-api.md` — add §3.6 consent endpoints + recurring debit, extend webhooks §5, versioning note, open questions.
- `openapi/tsp-api.yaml` — add consent/debit paths + schemas (backwards compatible).
- `docs/nfr.md` — add section 7 (рекуррентные списания/согласия) with measurable targets.
- `docs/spec/state-machine.md` — add consent state machine + recurring debit transitions.
- `docs/solutioning.md` — update roadmap (move автоплатежи from "вне scope" to "in scope via ADR-008"), update разбиение на ADR table, gaps/open questions.

That's a substantial but coherent package.

Now, should I be careful about the spine edits? The spine says "Родительский spine ... Локальное переопределение родительских ограничений запрещено; конфликт эскалируется наверх." This is about parent spine. Adding new ADs to the feature spine is fine. Marking them "Proposed" (like AD-001..007) is correct — they act after the ADR is ratified. The existing AD-001..007 are "Proposed"; AD-008 is "[ADOPTED]". So new AD-009, AD-010 should be "Proposed (ADR-008)".

Let me also verify: the CONSTRAINTS.yaml has fitness rules. One rule checks `docs/adr/ADR-005-...` contains 'только из состояния `PAID`'. And `adr-no-placeholders` checks `docs/adr/*.md` must not contain `<!--`. So my new ADR must not contain `<!--` (HTML comments). I'll avoid that. Also `spine-lints-clean` checks ARCHITECTURE-SPINE.md must not contain TODO/TBD/XXX. My spine additions must avoid those. Good.

Also the fitness rule `nfr-measurable` requires `docs/nfr.md` contains `'99,95'`. My edits must preserve that. Good.

Let me now also check: is there a `.arch-handoff/adr/` that mirrors `docs/adr/`? Yes! The glob shows `.arch-handoff/adr/ADR-001..007.md` AND `docs/adr/ADR-001..007.md`. These appear to be duplicates (the `.arch-handoff` is the "handoff package" copy). Let me check if `.arch-handoff/adr/ADR-001` is identical to `docs/adr/ADR-001`.

Actually, this matters: the `.arch-handoff/` is a snapshot package for the code harness. The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." The accepted-solution files are in `docs/` and `ARCHITECTURE-SPINE.md` and `openapi/`. The `.arch-handoff/` is a handoff package (generated snapshot). Should I update `.arch-handoff/adr/` too? 

Let me check whether .arch-handoff/adr files are identical to docs/adr. Let me diff quickly. Actually, the .arch-handoff/ARCHITECTURE.md is a concatenated epic-context (with truncation), and .arch-handoff/adr/*.md are likely copies. The task is about preparing the architecture package "поверх принятого решения" for human decision and then handoff to executors. The "принятые файлы решения" are the source files in `docs/`, `ARCHITECTURE-SPINE.md`, `openapi/`. The `.arch-handoff/` is the generated handoff for the previous (base) task — I should NOT need to touch it; it will be regenerated. But let me verify the relationship to be safe.

Let me diff the .arch-handoff/adr vs docs/adr.

Actually, I've spent enough exploration. Let me quickly check the diff to understand whether .arch-handoff/adr are copies that I need to keep in sync.

  `write_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-, content="# ADR-008. Рекуррентные C2B-списания по согласию плательщика (подписки СБП)\n\n- Date: 2026-09-28\n- Status: Proposed\n- Owner: solution-ar)`

The diff produced no output, meaning `.arch-handoff/adr/ADR-001-outbox.md` and `docs/adr/ADR-001-outbox.md` are identical. So `.arch-handoff/` is a snapshot copy. Git status is clean.

So the "принятые файлы решения" (accepted solution files) live in `docs/` and `ARCHITECTURE-SPINE.md` and `openapi/`. The `.arch-handoff/` is the generated handoff package (snapshot). I should update the source files (`docs/`, `ARCHITECTURE-SPINE.md`, `openapi/`), NOT the `.arch-handoff/` snapshot — it's a handoff artifact for the code harness (regenerated). Actually, but the task says "чтобы его можно было вынести на архитектурное решение и затем передать исполнителям" — the handoff to executors happens via `.arch-handoff/`. But I shouldn't regenerate that manually; the handoff tooling does. My job is the architecture package in the source-of-truth locations.

I'll focus on source-of-truth files. I'll note in my final summary that `.arch-handoff/` is regenerated by the handoff tooling and I did not touch it (or should I mirror?). Actually, to be safe and thorough, since `.arch-handoff/adr/*` are exact copies, and the CONSTRAINTS.yaml fitness rules reference `docs/adr/ADR-005-...` (source location), the source of truth is `docs/`. The `.arch-handoff` is a snapshot with MANIFEST.json listing sources. I'll leave `.arch-handoff` alone (it's a frozen handoff snapshot for the *base* task) — regenerating it is out of scope and would be speculative.

Now, I have everything I need. Let me think about whether I need to ask the user any clarifying questions before proceeding. The task is quite detailed and self-contained. However, there are genuine architectural ambiguities that the task explicitly says should be left to the human architect (item 7). So I should NOT ask; I should document them as "остаётся на решение человека". 

But there is one thing worth confirming: the exact СБП mechanism. However, since the repo already uses `[ТРЕБУЕТ ПРОВЕРКИ]` for НСПК protocol details, I'll follow that convention — mark protocol details as `[ТРЕБУЕТ ПРОВЕРКИ]` and keep the design protocol-agnostic (consistent with AD-008).

Given the task is well-specified and this is a "prepare the package" deliverable, I should proceed without asking questions (the ask_user_question tool is available, but the task says to leave specific decisions to the human architect and document them). I'll proceed.

Let me now write the deliverables. I'll be thorough but not over-engineer. Let me draft the ADR-008 first (the centerpiece), then make the edits.

Let me carefully design the content now.

### ADR-008 content

Title: Рекуррентные C2B-списания по согласию плательщика (подписки СБП)

Fields:
- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур)
- Related: ADR-002, ADR-005, AD-001..AD-008, AD-009, AD-010 (new)

Sections:
1. Оценка значимости и маршрут (route assessment)
2. Context
3. Влияние на принятую архитектуру (инварианты)
4. Decision (согласие + рекуррентное списание)
5. Alternatives Considered
6. Consequences (positive/negative)
7. Reversibility
8. Изменения контрактов (summary)
9. NFR (summary, details in nfr.md)
10. Критерии приёмки и план отката
11. Остаётся на решение человека
12. References

Actually, let me structure it to match the repo's ADR format (Context, Decision, Alternatives Considered, Consequences, Reversibility, References) and ADD the extra required sections (route assessment, impact, acceptance/rollback, human-decision). The repo ADRs already vary a bit (ADR-007 has a "A3 Decision" section). So I have freedom.

Let me write a comprehensive ADR that includes all 7 required deliverables, with the file edits carrying the details.

### Key design decisions to lock in ADR-008:

**D1. Согласие (Consent) — отдельная сущность первого класса**, источник финансовой авторизации — НСПК/банк плательщика (согласие хранится и верифицируется в контуре СБП), шлюз хранит **проекцию** согласия (свой конечный автомат) для идемпотентности и оркестрации. Это соответствует «СБП: автоплатёж» — протокол в адаптере ОПКЦ, ядро работает с нормализованным контрактом согласия (AD-008, AD-004).

**D2. Жизненный цикл согласия**: `PENDING → ACTIVE → (SUSPENDED → ACTIVE) | REVOKED | EXPIRED`. События: `consent.activated`, `consent.suspended`, `consent.revoked`, `consent.expired`. Ревок возможен со стороны плательщика (через его банк/НСПК), ТСП (cancel) и по истечении срока.

**D3. Рекуррентное списание повторно использует статусную машину платежа** (ADR-002): дебит входит в `CREATED` с `paymentType=recurring` и идёт `CREATED → PAID → CREDITED → COMPLETED` **минуя QR_ISSUED** (авторизация — согласие, не QR). `PAID` по-прежнему — подтверждённый НСПК статус дебита (AD-005: зачисление только из PAID сохраняется). Отказ НСПК (нет средств, лимит, согласие неактивно) → `FAILED`.

**D4. Guard'ы дебита**: дебит создаётся только если согласие `ACTIVE`, сумма ≤ `consent.maxAmount`, в пределах срока и частотных лимитов; идемпотентность — `Idempotency-Key` + `consentId`/`debitId`/`paymentId`.

**D5. Контракт адаптера ОПКЦ расширяется** (additive): методы `createConsent`, `getConsentStatus`, `cancelConsent`, `createRecurringDebit`, `getDebitStatus`; события `consent.*`, `debit.*`. Идемпотентность по `reference` обязательна (как в opkc-adapter §5). Протокольные детали — `[ТРЕБУЕТ ПРОВЕРКИ]`.

**D6. АБС**: дебит зачисляется на счёт ТСП только из `PAID` (AD-005), идемпотентно по `paymentId`/`debitId`. Возврат рекуррентного платежа — та же сага (ADR-005).

**D7. ПДн**: согласие содержит данные плательщика (ПДн) — минимизация, шифрование, маскирование, правовое основание (152-ФЗ); ревок согласия — необратимая юридическая операция, в аудит-лог (AD-007).

### Alternatives:
- **A. Шлюз сам хранит согласие и повторяет списания без НСПК** (card-on-file): не соответствует СБП «автоплатёж», списание без авторизации банка плательщика невозможно/нелегально; отвергнуто.
- **B. Отдельный новый компонент «сервис подписок»** вместо расширения шлюза: нарушает AD-001 (изоляция платёжного контура), дублирует outbox/АБС-интеграцию; отвергнуто.
- **C. Моделировать согласие как «платёж с нулевой суммой»/специальный QR**: хак, ломает статусную машину и идемпотентность, смешивает сущности; отвергнуто.
- **D. Полностью на вендоре (рекуррент как часть транспортного адаптера)**: vendor lock-in в финансовой логике, конфликт с ADR-007 (ядро — собственная разработка); отвергнуто.

Chosen: расширение ядра (согласие + рекуррентный дебит в статусной машине) + расширение контракта адаптера; авторизационная сущность — в контуре СБП (НСПК/банк плательщика).

### Reversibility:
- Добавление согласия и дебита — **reversible** на уровне ядра (новые сущности, новые переходы — можно отключить фиче-флагом; не мигрируем существующие платежи).
- Необратимая часть — юридическая: выданные согласия плательщиков и совершённые дебиты (факт финансовых операций). Откат кода не отменяет уже совершённые списания; их отмена — только возвратами (сага) и ревоком согласий.
- Классификация: **reversible (код) / irreversible (совершённые финансовые операции)**, аналогично ADR-002/ADR-005.

### Impact on invariants:
| Инвариант | Влияние |
|---|---|
| AD-001 изоляция | не меняется; Binds расширяется компонентами согласия (внутри шлюза) |
| AD-002 источник истины (статусная машина платежа) | расширяется: добавляется вторая статусная машина (согласие) с тем же правилом «статус + outbox + аудит в одной транзакции» |
| AD-003 идемпотентность | расширяется: Idempotency-Key на согласия/дебиты, eventId на consent-события, consentId/debitId на АБС |
| AD-004 единственный адаптер ОПКЦ | не меняется; контракт адаптера расширяется аддитивно (согласия/дебиты) |
| AD-005 зачисление только из PAID | сохраняется: дебит зачисляется только из PAID (подтверждён НСПК), не из CREATED/по факту согласия |
| AD-006 trust-зоны | не меняется |
| AD-007 НПС/КИИ/ПДн | расширяется: согласие = ПДн, ревок = юридическое действие, в аудит-лог |
| AD-008 гибрид | не меняется; ядро остаётся контрактно-независимым, адаптер (вендор) реализует новые методы |

### New spine ADs:
- **AD-009. Согласие плательщика (реккурентная авторизация)** — Rule: финансовое списание по согласию допустимо только при согласии в состоянии ACTIVE и подтверждении НСПК (PAID); проекция согласия в шлюзе атомарно обновляется с outbox/аудитом.
- **AD-010. Рекуррентное списание как платеж без QR** — Rule: рекуррентный дебит — это платёж статусной машины, входящий в CREATED с paymentType=recurring и минующий QR_ISSUED; зачисление только из PAID (AD-005).

Hmm, AD-010 might be merged into AD-009. Let me keep two ADs but make them crisp. Actually, let me reconsider — do I need two spine blocks? The existing spine has 8 blocks for 7 ADRs. For a feature, adding 2 spine blocks is reasonable. But maybe 1 block AD-009 is cleaner and AD-010 is over-splitting. Let me do:

- **AD-009. Согласие плательщика и рекуррентные C2B-списания** — one block covering both the consent entity and the debit-as-payment-without-QR rule. This keeps it tight. Actually the spine blocks each have a single "Rule". I could have AD-009 for consent and AD-010 for the debit flow. Two is fine and clearer. Let me do two.

Actually, I'll do TWO new spine blocks (AD-009 consent, AD-010 recurring debit) — mirrors the granularity of the existing spine and gives the human architect clean binding points.

### NFR additions (docs/nfr.md section 7):
- Доступность API согласий/дебитов — та же ≥99,95%.
- Latency «создать согласие» p95 < 500 мс; «создать дебит» p95 < 500 мс (без учёта НСПК).
- Доставка consent-вебхука от события НСПК p95 < 5 с.
- Зачисление дебита в АБС от PAID p95 < 60 с.
- Throughput: рекуррентные дебиты — sustained 200 TPS (пик 500) поверх разовых (общий пул) или отдельный бюджет; масштабирование ×2.
- RPO=0, RTO≤1ч (для согласий и дебитов).
- Идемпотентность: 0 дублей при повторах (создание согласия/дебита, consent-события).
- Сверка согласий с НСПК: ежечасная; расхождений 0.
- Соответствие: 100% согласий с правовым основанием (152-ФЗ), аудит-лог 100%, ревоки в аудит-логе 100%.
- ПДн: минимизация/маскирование/шифрование.
- Отказные сценарии: дебит при неактивном согласии → 100% отклонение (нет зачисления).

### Acceptance criteria (Критерии приёмки):
- Each is testable. Positive + negative scenarios (dup, neighbour failure, race).
- Positive: create consent → payer confirms → ACTIVE webhook → create debit → PAID → CREDITED → COMPLETED.
- Negative: debit on non-ACTIVE consent → 409/422, no credit; duplicate Idempotency-Key → same resource; duplicate consent event eventId → ignored; НСПК rejected debit → FAILED, no credit; consent revoked mid-flight → debit FAILED or blocked; АБС down during debit → retries, stays PAID, сверка; double notify → single credit.
- Race: debit created while consent transitioning ACTIVE→REVOKED → guard rejects or НСПК rejects.
- Rollback criterion: фиче-флаг stop-new-consents stops new consents/debits; existing debits in flight complete; no double credit; сверка confirms zero discrepancies.

### Rollback plan:
- Pre-production: don't enable feature flag; code changes reversible.
- Post-enable: feature flag "recurrent" — off stops new consent creation and new debits; in-flight debits complete normally (idempotent). Rolling rollback of release. Data not migrated back (consent projections remain, but revocable).
- Emergency: stop-new-consents + stop-new-debits; DLQ → runbook; сверка compensates lost notifications. Legal revocations remain.
- Owner of rollback decision: product owner / платёжный риск + архитектор.

### Human-decide (item 7):
1. Подтверждение scope: что это именно «СБП автоплатёж» (согласие ведётся в контуре НСПК/банка плательщика), а не gateway-side mandate — определяет, кто источник истины согласия. [ТРЕБУЕТ ПРОВЕРКИ с документацией НСПК].
2. Бизнес-правила согласия: лимиты (maxAmount, частота), срок действия по умолчанию, кто может ревокировать, поведение при нехватке средств (retry-политика для дебита).
3. Регуляторная классификация: правовое основание обработки ПДн согласия (152-ФЗ), требуется ли доп. согласие/информирование плательщика, классификация под 161-ФЗ защиту переводов; согласование с ИБ/комплаенс.
4. Точный протокол согласий/дебитов НСПК (поля, события, тайминги) — внешний вход, владелец проектный офис/НСПК.
5. Расширение контракта адаптера ОПКЦ и RFP-вендора (новые методы) — требуется ли доп. соглашение/поправка к контракту вендора (влияет на ADR-007 constraints).
6. Приоритизация: входит ли рекуррент в первую волну (A2 walking skeleton) или отдельная волна после базового C2B.

Why these remain human: они либо внешние входы (документация НСПК, регулятор), либо бизнес-решения с финансово-правовыми последствиями, которые архитектор не вправе принимать единолично.

OK. Now let me write everything. I need to be careful with the CONSTRAINTS fitness rules:
- `adr-no-placeholders`: `docs/adr/*.md` must not contain `<!--`. My ADR-008 must not contain `<!--`. I'll avoid HTML comments.
- `nfr-measurable`: nfr.md must contain '99,95'. I'll keep it.
- `abs-credit-only-from-paid`: ADR-005 must contain 'только из состояния `PAID`'. I'm not editing ADR-005, so fine.
- `spine-lints-clean`: ARCHITECTURE-SPINE.md must not contain TODO/TBD/XXX. My additions must avoid these. I'll avoid "TODO", "TBD", "XXX".

Wait, but the existing spine and docs contain `[ТРЕБУЕТ ПРОВЕРКИ]` — that's fine, not a lint violation. My additions can use `[ТРЕБУЕТ ПРОВЕРКИ]`.

Also note: my new ADR file must not contain `<!--` — I'll use regular markdown, no HTML comments.

Let me now also decide the exact openapi changes. The current openapi/tsp-api.yaml is minimal. I'll extend it additively:

Add paths:
- `/v1/consents` POST (Idempotency-Key) → 201 Consent
- `/v1/consents/{consentId}` GET → 200 Consent
- `/v1/consents/{consentId}/cancel` POST → 200/202 Consent (revoke)
- `/v1/consents/{consentId}/debits` POST (Idempotency-Key) → 201 Debit (or reuse Payment)

Add schemas:
- `ConsentRequest` (tspId, amount limit, currency, frequency, validity, purpose, payer reference)
- `Consent` (consentId, tspId, status, maxAmount, currency, frequency, validFrom, validTo, payerToken?, webhookUrl?)
- `DebitRequest` (amount, merchantOrderId, purpose)
- `Debit` (debitId, paymentId, consentId, amount, status, ...) — or reuse Payment + add `consentId` and `paymentType`.

Also extend `Payment` schema with optional `consentId` and `paymentType` (default one-shot) — additive, backwards compatible.

I need to be careful: the yaml is 3.0.3. I'll add components and paths cleanly.

Let me also extend `docs/contracts/tsp-api.md` §3 with consent endpoints and §5 webhooks with consent events, and §7 open questions.

And `docs/spec/state-machine.md`: add §7 (согласие) and §8 (рекуррентный дебит), and update §1/§2 to note the recurring entry. Actually, I'll add new sections rather than rewrite existing, to be minimally invasive. I'll add a section for consent state machine and note the recurring debit reuse in §2 (add a transition T0a or a note). Let me add a new top-level section "## 7. Согласие плательщика (реккурентная авторизация)" and "## 8. Рекуррентное списание (дебит) как платёж без QR" and renumber references. Actually the doc has sections 1-6. I'll append sections 7 and 8. And add a note in §2 table about recurring entry. To keep it clean, I'll add a note near T1 and a new subsection. Let me keep it simpler: append §7 (согласие) and §8 (дебит), and in §2 add a row note about the recurring entry point. Actually the cleanest: add the consent state machine and debit transitions as new sections, referencing the existing payment transitions (T1..T12) where reused.

Let me now write the files. I'll start with the ADR (the biggest), then edits.

Let me write ADR-008 first. I'll be comprehensive but tight.

Actually, I realize I should double check the exact naming convention for ADR slugs — they use transliterated Russian lowercase with hyphens. E.g. "ADR-005-integraciya-s-abs-zachislenie-po-podtverzhdyonnomu-statusu-vozvraty-kak-saga.md". So my ADR-008 slug: "ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md".

Let me write it now.

I'll write the ADR file content carefully.

Now let me also think about what "paymentType" enum values: `ONE_SHOT` and `RECURRING`. And the debit endpoint returns a Debit object referencing paymentId, so merchants can poll GET /v1/payments/{paymentId} for status. Good — reuse existing payment status endpoint.

For webhooks, add:
- `consent.activated`
- `consent.suspended`
- `consent.revoked`
- `consent.expired`
- `consent.failed` (payer declined / bank declined consent)
- debit results reuse `payment.completed` / `payment.failed` with added `consentId` + `paymentType: RECURRING` fields.

Let me write now. I'll produce the ADR, then do the edits in parallel where possible.

Let me draft the ADR content fully in my head then write.

Actually I'll write directly via write_file with the full content.

For the spine, I need to add AD-009 and AD-010 after AD-008, and update the Deferred section. Let me look at the exact text of the Deferred section and the end of the spine to craft precise edits.

The Deferred section currently:
```
## Deferred (с причиной и условием возврата)

- **Мультивалютность и иностранные платёжные системы**: не в scope C2B-приёма СБП; вернуть при расширении на валютные счета ТСП.
- **C2C-переводы и выплаты B2C/B2B**: roadmap после стабилизации C2B; вернуть как отдельный initiative (родительский spine изменится).
- **Диспуты/претензии (disputes)**: реализуются после базовых возвратов; вернуть по требованию бизнеса или регулятора.
```

Note: the spine's Deferred doesn't mention автоплатежи (the solutioning.md roadmap does). The solutioning.md §1 says "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." So автоплатежи is listed as "вне scope" in solutioning.md §1. I need to update that.

For the spine, I'll add AD-009 and AD-010 blocks after AD-008 (before the "---" and "## Deferred"). And I don't need to change the Deferred section in the spine (автоплатежи isn't there). But I could add a note. Actually, I'll leave Deferred as-is in the spine (it doesn't mention автоплатежи), and update solutioning.md §1 roadmap.

Wait, let me re-read the spine Deferred: it lists мультивалютность, C2C/выплаты, диспуты. No автоплатежи. So the spine never had автоплатежи in Deferred. The solutioning.md §1 lists "автоплатежи" in the "Roadmap (вне scope)". So the "accepted decision" that says автоплатежи is out of scope is in solutioning.md §1 and §5 (разбиение) — actually §5 table doesn't list автоплатежи. And README doesn't either. Let me check where "автоплатежи" appears.

From solutioning.md §1: "Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи."

So I need to update solutioning.md §1 to move автоплатежи/подписки from roadmap-out-of-scope into scope (referencing ADR-008), and update §5 разбиение table to add ADR-008 row, and §10 open questions maybe.

OK, I have a clear plan. Let me write.

I'll now write the ADR file. Then make edits to:
1. ARCHITECTURE-SPINE.md (add AD-009, AD-010)
2. docs/contracts/tsp-api.md (add consent/debit endpoints + webhooks)
3. openapi/tsp-api.yaml (add paths/schemas)
4. docs/nfr.md (add section 7)
5. docs/spec/state-machine.md (add §7 consent, §8 debit)
6. docs/solutioning.md (update §1 roadmap, §5 table, §10 open questions)

Let me write the ADR now.

For precision, I'll keep amounts in kopeks, dates in ISO 8601.

Let me write the full ADR-008.

I'll write in Russian (matching repo language).

Let me carefully compose. I'll aim for a thorough but not bloated document.

One more consideration: the ADR "Status: Proposed" — consistent with ADR-001..006 (ADR-007 is Accepted). Since this is being "вынесено на архитектурное решение", Proposed is correct.

Date: 2026-09-28 (today).

Let me write it.

For the "Оценка значимости и маршрута" I'll include a scoring consistent with the repo's "значимость 11/15" and "Critical" route. The base initiative is Critical 11/15. The recurrence feature is a significant feature-level change. I'll characterize it as: значимость feature — High (≈9-10/15), но не требует переоткрытия Critical-маршрута (ADR-001..007); маршрут — **Feature increment поверх Critical**, проектирование средней глубины: новый ADR + расширение контрактов/NFR/статусной машины, прохождение тех же гейтов A0–A5 с фокусом на новые артефакты.

Now writing.

Actually, let me reconsider the number of ADRs. The task says "3. Архитектурное решение" (singular). But I'm also required to update the spine with new invariants. One ADR (ADR-008) is right.

Let me write the files now. I'll do the ADR first (write_file), then the 6 edits. I can do several edits in parallel since they're independent files (different files). Actually edits to different files are independent — I can batch them. But write_file for ADR must come first logically (no dependency), but I can batch all in one message? The edits reference ADR-008 by name in cross-references, but that's just text, no actual dependency on tool result. I can do them all. However, to keep it manageable and ensure correctness, I'll write the ADR first, then batch the edits.

Let me write the ADR now.
Изучение завершено. Репозиторий использует чёткие конвенции: ADR в `docs/adr/` (формат Context→Decision→Alternatives→Consequences→Reversibility→References), spine-инварианты в `ARCHITECTURE-SPINE.md` (блоки AD-XXX со статусом Proposed/[ADOPTED]), контракты в двух местах (`docs/contracts/tsp-api.md` + `openapi/tsp-api.yaml`), NFR в `docs/nfr.md`, статусная машина в `docs/spec/state-machine.md`. Проектных навыков/команд нет — только bundled-навыки; `.arch-handoff/` — сгенерированный snapshot (не источник истины). Протокол НСПК — внешний вход, помечается `[ТРЕБУЕТ ПРОВЕРКИ]`.

Начну с центрального артефакта — ADR-008.

  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now let me update the ARCHITECTURE-SPINE.md — add AD-009 and AD-010 after AD-008. Let me re-read the exact text around AD-008 to make precise edits.

From the earlier read, AD-008 ends with:

```
## AD-008. Стратегия реализации — гибрид [ADOPTED]

- Status: Adopted (A3 от 2026-08-15, ADR-007 Accepted)
- **Binds**: ADR-007, ядро шлюза, вендорский транспортный адаптер ОПКЦ.
- **Prevents**: связывание ядра шлюза с конкретным транспортным адаптером; начало реализации транспорта до контракта с вендором и получения документации НСПК.
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

So I'll insert AD-009 and AD-010 between the "---" and "## Deferred". Actually I'll insert after AD-008's Rule line, before the "---" separator. Let me edit by replacing the "---\n\n## Deferred" marker, adding the two new ADs before it.

Let me craft the edit: replace:
```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```
with the same plus AD-009, AD-010 inserted before "---".

Let me write the AD-009 and AD-010 blocks matching the style of existing blocks.
Теперь обновлю spine — добавлю AD-009 и AD-010.

  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/contracts/tsp-api.md", old_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n, new_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n)`

Now update the Deferred section? The spine's Deferred doesn't mention автоплатежи, so no change needed there. But I should check the "Контракты и версии" section at the bottom of the spine — it references tsp-api.md v0.1 draft. That's fine.

Now update docs/contracts/tsp-api.md — add consent/debit endpoints, extend webhooks, add error codes, update open questions. Let me edit.

I'll add:
- §3.6 Согласие плательщика (consent) endpoints
- §3.7 Рекуррентное списание (debit) endpoint
- §5 webhooks: add consent events + note debit reuse payment events
- §4 errors: add new codes
- §6 versioning note (additive)
- §7 open questions

Let me do these edits carefully. First, read the relevant portions to make precise replacements. I already have the full tsp-api.md content from earlier. Let me craft edits.

I'll add §3.6 and §3.7 after §3.5 (Статус возврата) and before §4 (Ошибки).

The §3.5 ends with:
```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`

## 4. Ошибки (RFC 9457, Problem Details)
```

I'll insert §3.6 and §3.7 before "## 4. Ошибки".

Let me craft the consent/debit endpoint docs consistent with the existing style.

§3.6:
```
### 3.6 Согласие плательщика (подписка, рекуррентная авторизация)

Согласие — сущность первого класса (ADR-008). Авторизация плательщика выполняется в приложении банка плательщика через контур СБП; шлюз регистрирует согласие в ОПКЦ, получает события жизненного цикла и инициирует дебиты.

`POST /v1/consents` (заголовок `Idempotency-Key` обязателен)

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "currency": "RUB",
  "maxAmount": 100000,             // копейки, int; лимит одного списания
  "maxFrequency": "MONTHLY",       // DAILY | WEEKLY | MONTHLY | UNLIMITED
  "validFrom": "2026-09-28T00:00:00.000Z",
  "validTo": "2027-09-28T00:00:00.000Z",
  "purpose": "Подписка «Кино+»",
  "payerReference": "subscriber-12345", // сквозной идентификатор плательщика у ТСП
  "redirectUrl": "https://merchant.example.com/subscribe/return"
}
```

Ответ `201`:
```json
{
  "consentId": "con_1a2b3c4d",
  "tspId": "tsp_9f3c2a1b",
  "status": "PENDING",             // PENDING | ACTIVE | SUSPENDED | REVOKED | EXPIRED
  "maxAmount": 100000,
  "maxFrequency": "MONTHLY",
  "validTo": "2027-09-28T00:00:00.000Z"
}
```

Правила: согласие не даёт права на списание само по себе — `ACTIVE` наступает только после подтверждения плательщиком (событие `consent.activated`). Ревок возможен плательщиком (через его банк), ТСП (`POST /v1/consents/{consentId}/cancel`) и по истечении `validTo`. Ревок необратим.

`GET /v1/consents/{consentId}` → `200 { consentId, tspId, status, maxAmount, maxFrequency, validFrom, validTo, activatedAt?, revokedAt? }`

`POST /v1/consents/{consentId}/cancel` (заголовок `Idempotency-Key` обязателен) → `200 { consentId, status: "REVOKED" }`

§3.7:
```
### 3.7 Рекуррентное списание (дебит)

`POST /v1/consents/{consentId}/debits` (заголовок `Idempotency-Key` обязателен)

Запрос:
```json
{
  "amount": 79000,                 // копейки, int; ≤ consent.maxAmount
  "currency": "RUB",
  "purpose": "Списание за сентябрь",
  "merchantOrderId": "order-12345"
}
```

Ответ `201`:
```json
{
  "debitId": "dbt_7e8f9a0b",
  "paymentId": "pay_8d1e4f5a",    // дебит — платёж той же статусной машины (ADR-008)
  "consentId": "con_1a2b3c4d",
  "amount": 79000,
  "status": "CREATED"              // CREATED | PAID | CREDITED | COMPLETED | FAILED
}
```

Правила: дебит создаётся только при согласии `ACTIVE` и `amount ≤ maxAmount` (иначе `422 CONSENT_NOT_ACTIVE` / `422 CONSENT_LIMIT_EXCEEDED` без вызова НСПК). Зачисление в АБС — только из `PAID` (подтверждён НСПК), минуя `QR_ISSUED`. Статус дебита отслеживается через `GET /v1/payments/{paymentId}`. Возврат дебита — обычная сага (`POST /v1/payments/{paymentId}/refunds`).
```

Now §4 errors: add codes to the canonical list:
`CONSENT_NOT_FOUND` (404), `CONSENT_NOT_ACTIVE` (422), `CONSENT_LIMIT_EXCEEDED` (422), `CONSENT_CONFLICT` (409).

The canonical codes line:
```
Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.
```

I'll add the new codes into this list.

§5 webhooks: add consent events. The §5 lists:
```
События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
```

I'll add consent events and note debit reuse.

§6 versioning: note additive change (already says additive optional fields are backwards compatible). I'll add a sentence noting v0.1 → v0.2 additive for consents.

§7 open questions: add consent-specific questions.

Let me make the edits. I'll do them as multiple edit calls on the same file — but they must be sequential (same file). Actually I can do them in a single message as multiple edits? No — edits to the same file should be sequential to avoid conflicts. But the edit tool operates on exact strings, so I can do multiple edits to different parts of the same file. However, to be safe, I'll do them one at a time or in carefully-ordered batch. Since they target distinct, non-overlapping strings, I can batch them. But the tool might have issues with multiple edits to same file in parallel. I'll do them sequentially to be safe, but I can group into fewer edits.

Actually, let me do the tsp-api.md edits in a sequence of edit calls. I'll do them one by one but efficiently. Let me start with inserting §3.6/§3.7.

Let me be careful with the exact strings including backticks and quotes.
Теперь расширю контракт API ТСП (`docs/contracts/tsp-api.md`).

  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/contracts/tsp-api.md", old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `CONSENT_NOT_FOUND` (404), `ID)`

Now update §4 error codes, §5 webhooks, §6 versioning, §7 open questions. Let me edit the canonical codes line and webhook events.

First the error codes line.

  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/contracts/tsp-api.md", new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/contracts/tsp-api.md", offset=250, limit=30)`

Now update §6 versioning and §7 open questions. Let me read the current tail of the file to get exact strings.

  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/contracts/tsp-api.md", new_string="## 6. Версионирование и совместимость\n\n- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6, old_string="## 6. Версионирование и совместимость\n\n- Путь `/v1`; изменения, ломающие контракт, — только в `/v2` с периодом поддержки обеих версий ≥ 6)`
  `write_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/openapi/tsp-api.yaml", content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\n  description: >\n    Аддитивное расширение v0.1: согласия плательщик)`

Now update the openapi/tsp-api.yaml. I need to add consent/debit paths and schemas additively, and extend Payment schema with optional consentId and paymentType.

The current yaml:
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

I'll rewrite the whole file to add new paths and schemas cleanly. I'll bump version to 0.2.0 (additive). Actually the info.version is 0.1.0; since it's additive, I could keep 0.1.0 or bump to 0.2.0. The tsp-api.md says "v0.1 draft". The yaml is the machine-readable. I'll bump to 0.2.0 to reflect additive extension, and note it. Actually, to be careful: the task says "без поломки существующих потребителей" — additive changes. Version bump in the OpenAPI info is fine (it's the API spec version, not the URL version). I'll set 0.2.0.

Let me write the full new yaml. I'll use write_file to replace it (I've already read it, so I can overwrite). Actually I need to be careful — write_file requires prior read. I've read it. I'll write the full content.

Let me design the yaml additions:

New paths:
- `/v1/consents` POST (Idempotency-Key header) → 201 Consent
- `/v1/consents/{consentId}` GET → 200 Consent
- `/v1/consents/{consentId}/cancel` POST (Idempotency-Key) → 200 Consent (status REVOKED)
- `/v1/consents/{consentId}/debits` POST (Idempotency-Key) → 201 Debit

New schemas:
- `ConsentRequest` (tspId, currency, maxAmount, maxFrequency, validFrom, validTo, purpose, payerReference, redirectUrl)
- `Consent` (consentId, tspId, status, maxAmount, maxFrequency, validFrom, validTo, activatedAt?, revokedAt?)
- `DebitRequest` (amount, currency, purpose, merchantOrderId)
- `Debit` (debitId, paymentId, consentId, amount, status)
- Extend `Payment` with optional `consentId` and `paymentType`.

Let me write it out. I'll use inline YAML style consistent with the existing (compact). I'll keep it clean and valid YAML.

Let me write the full file.
Теперь расширю `openapi/tsp-api.yaml` аддитивно.

  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/contracts/opkc-adapter.md", new_string="| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |\n| `getReconciliationReport` | вып, old_string="| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |\n| `getReconciliationReport` | вып)`

Now update the opkc-adapter.md to add the new adapter methods/events (additive). The ADR-008 says the adapter contract is extended. I should update docs/contracts/opkc-adapter.md §3 (methods table) and §4 (events) to add consent/debit methods and events. Let me do that.

The §3 table currently has methods: registerTsp, createPaymentLink, getPaymentStatus, cancelPaymentLink, createRefund, getRefundStatus, getReconciliationReport.

I'll add: createConsent, getConsentStatus, cancelConsent, createRecurringDebit, getDebitStatus.

§4 events: add consent.* and debit.* events.

Let me edit opkc-adapter.md.

First the §3 table. I need the exact text. From earlier read:

```
| Метод | Направление смысла | Ключевые поля запроса | Ответ | Таймаут (p99.9) |
|---|---|---|---|---|
| `registerTsp` | регистрация/активация ТСП в ОПКЦ | `tspId` (ядро), реквизиты ТСП, `reference` | `jobId`, статус `ACCEPTED` (результат — событием) | 5 c |
| `createPaymentLink` | создание QR/ссылки | `reference` (= `paymentId` ядра), `amount` (копейки), `currency`, `qrType`, `ttlSeconds?`, `purpose?`, `redirectUrl?` | `qrId`, `qrUrl`, `expiresAt` | 3 c |
| `getPaymentStatus` | запрос статуса по `qrId` (сверка/опрос) | `qrId` | статус ОПКЦ: `PAID` / `PENDING` / `REJECTED` / `EXPIRED` / `UNKNOWN`, `paidAmount?`, `paidAt?` | 3 c |
| `cancelPaymentLink` | закрытие/отмена ссылки (TTL, отмена ТСП) | `qrId`, `reason` | `CANCELLED` | 3 c |
| `createRefund` | регистрация возврата в ОПКЦ | `reference` (= `refundId` ядра), `qrId`, `amount` | `ACCEPTED` (результат — событием) | 5 c |
| `getRefundStatus` | статус возврата | `refundId` (ОПКЦ) | `CONFIRMED` / `PENDING` / `REJECTED` | 3 c |
| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |
```

I'll add rows after `getReconciliationReport` (or after createPaymentLink group). I'll add a new subsection or just append rows. I'll add rows before the "Статусные модели ОПКЦ..." paragraph. Let me add the consent/debit methods after the existing table.

Actually, better to append new rows to the table, and add a note. Let me insert after the `getReconciliationReport` row.

New rows:
```
| `createConsent` | регистрация согласия в ОПКЦ | `reference` (= `consentId` ядра), `tspId`, `maxAmount`, `maxFrequency`, `validFrom?`, `validTo?`, `payerReference?`, `redirectUrl?` | `ACCEPTED` (результат — событием) | 5 c |
| `getConsentStatus` | статус согласия (сверка/опрос) | `consentId` | `ACTIVE` / `PENDING` / `SUSPENDED` / `REVOKED` / `EXPIRED` / `UNKNOWN` | 3 c |
| `cancelConsent` | ревок согласия (ТСП/плательщик) | `consentId`, `reason` | `REVOKED` | 3 c |
| `createRecurringDebit` | инициализация рекуррентного списания по согласию | `reference` (= `debitId` ядра), `consentId`, `amount`, `purpose?` | `ACCEPTED` (результат — событием) | 5 c |
| `getDebitStatus` | статус дебита (сверка/опрос) | `debitId` | `PAID` / `PENDING` / `REJECTED` / `UNKNOWN`, `paidAmount?`, `paidAt?` | 3 c |
```

And a note about consent/debit being additive + [ТРЕБУЕТ ПРОВЕРКИ].

§4 events: add consent.* and debit.* to the events table. Current table:

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

Add:
```
| `consent.activated` | согласие подтверждено плательщиком | `reference` (= `consentId` ядра) |
| `consent.suspended` | согласие приостановлено | `reference`, `reasonCode` |
| `consent.revoked` | согласие отозвано | `reference`, `reasonCode` |
| `consent.expired` | истёк срок согласия | `reference` |
| `consent.rejected` | согласие отклонено (банк плательщика) | `reference`, `reasonCode`, `reasonText` |
| `debit.paid` | дебит подтверждён ОПКЦ | `reference` (= `debitId` ядра), `consentId`, `amount`, `paidAt` |
| `debit.rejected` | дебит отклонён (нет средств/лимит/согласие неактивно) | `reference`, `consentId`, `reasonCode`, `reasonText` |
```

Also update the note about status models in §3 ("Статусные модели ОПКЦ ... — нормализованные адаптером"). That's fine.

Let me make these two edits.

Also update §5 идемпотентность note to mention consent/debit reference? It already covers "мутирующие операции по reference". The §5 text is generic. I'll add a small note. Actually §5 already says "Ядро передаёт reference (свой paymentId/refundId/tspId) в каждый мутирующий вызов." I should extend to consentId/debitId. Let me update that line.

Let me do the edits.
Расширю контракт адаптера ОПКЦ (`docs/contracts/opkc-adapter.md`) аддитивно.

  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/contracts/opkc-adapter.md", new_string="| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |\n| `refund.rejected` | возв, old_string="| `refund.confirmed` | возврат подтверждён | `refundRef` (= `refundId` ядра), `refundOpcId`, `qrId`, `amount` |\n| `refund.rejected` | возв)`
  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/contracts/opkc-adapter.md", new_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`/`consentId`/`debitId`) в каждый мутирующий вызов.\n- **Адаптер обязан обес, old_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.\n- **Адаптер обязан обеспечить идемпотентность)`

Now update §5 идемпотентность to mention consentId/debitId. Let me read the §5 text.

From earlier read:
```
## 5. Идемпотентность и ссылки

- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.
- **Адаптер обязан обеспечить идемпотентность**: повторный вызов с тем же `reference` возвращает тот же результат и **не создаёт дубль в ОПКЦ**. Если протокол НСПК не даёт идемпотентности «из коробки» — вендор реализует маппинг `reference → операция ОПКЦ` у себя. **Это обязательное требование RFP** (без него ретраи ядра дают двойные QR/возвраты).
- Повторная доставка события с тем же `eventId` — игнорируется ядром (ADR-003).
```

I'll update the first bullet to include consentId/debitId.

  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/spec/state-machine.md", offset=95)`

Now update docs/spec/state-machine.md — add consent state machine and recurring debit transitions. Let me append §7 and §8, and add a note in §2 about the recurring entry.

Let me read the end of state-machine.md to find the exact insertion point. From earlier read, the file ends with §6 "Согласованность с API ТСП". Let me append after §6.

I'll add:
## 7. Согласие плательщика (реккурентная авторизация) — отдельная статусная машина

States: PENDING, ACTIVE, SUSPENDED, REVOKED, EXPIRED.

Transitions table:
| № | From | To | Триггер | Guard | Действие |
| C1 | — | PENDING | POST /v1/consents | валидный запрос, ТСП активен | запись согласия + outbox «регистрация в ОПКЦ» |
| C2 | PENDING | ACTIVE | consent.activated (НСПК) | — | outbox, вебхук consent.activated |
| C3 | PENDING | REVOKED | consent.rejected (НСПК) / cancel ТСП | — | outbox, вебхук consent.failed/revoked |
| C4 | ACTIVE | SUSPENDED | consent.suspended (НСПК) | — | outbox, вебхук |
| C5 | SUSPENDED | ACTIVE | возобновление (НСПК/банк) | — | outbox, вебхук |
| C6 | ACTIVE/SUSPENDED | REVOKED | revoke (плательщик/ТСП) | — | аудит-лог, вебхук consent.revoked; ревок необратим |
| C7 | ACTIVE/SUSPENDED | EXPIRED | validTo истёк | — | вебхук consent.expired |

Invariants:
- Зачисление/списание по согласию возможно только из ACTIVE (и PAID дебита, AD-009/AD-010).
- REVOKED/EXPIRED — терминальные; повторные события идемпотентны.
- Переходы — атомарные «статус + outbox + аудит».

## 8. Рекуррентное списание (дебит) — платёж без QR

The debit reuses the payment state machine (T1..T12) but enters at CREATED with paymentType=recurring and skips QR_ISSUED.

New/modified transitions:
| № | From | To | Триггер | Guard | Действие |
| D1 | — | CREATED | POST /v1/consents/{id}/debits | consent ACTIVE, amount ≤ maxAmount, в сроке/частоте | запись дебита (paymentType=recurring) + outbox «дебит в ОПКЦ» |
| D2 | CREATED | PAID | debit.paid (НСПК) | сумма совпадает | outbox «зачисление в АБС» (переиспользует T4/T8) |
| D3 | CREATED | FAILED | debit.rejected (НСПК) / guard fail | — | errorCode, вебхук payment.failed |
| (T8-T10) | PAID | CREDITED | COMPLETED | — | переиспользуются без изменений |

Note: дебит не проходит QR_ISSUED; T2 (QR_ISSUED) для дебита недостижим.

Invariants:
- Зачисление дебита только из PAID (AD-005, AD-010).
- Дебит при неактивном согласии не создаётся (guard D1).
- Повторный дебит с тем же Idempotency-Key → тот же debitId/paymentId.

Also update §1 or §2 to note the recurring entry. I'll add a note in §2 near T1, or better in §8. I think appending §7/§8 is cleanest; I'll also add a short note in §1 states table? The §1 "Финансовые состояния" lists CREATED...REFUNDED. The debit reuses those. I'll leave §1 as-is and explain in §8.

Actually, to keep it coherent, I'll also add a brief cross-reference in §2 (the transition table) — but appending §8 with the debit transitions and a note that it reuses T8-T10 is sufficient.

Let me read the end of the file to get exact insertion anchor.

  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/spec/state-machine.md", offset=58)`

The file is 75 lines (the earlier read showed up to §6). The offset 95 is beyond. Let me read from line 60 to the end.

  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/spec/state-machine.md", new_string="## 6. Согласованность с API ТСП\n\nМаппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED, old_string="## 6. Согласованность с API ТСП\n\nМаппинг статусов наружу (TSP API §3.3): `CREATED`, `QR_ISSUED`, `PAID`, `CREDITED`, `COMPLETED`, `FAILED)`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/nfr.md", offset=70)`

Now update docs/nfr.md — add section 7 for recurring/consents. Also must preserve the '99,95' pattern for the fitness rule. Let me add a new section 7 after section 6 (Наблюдаемость), before the "Зависимости" section.

Let me read the tail of nfr.md to find the exact insertion point.

  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/nfr.md", offset=52)`
  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/nfr.md", new_string="| Trace id на операцию | 100 % операций | APM |\n| Алерт на DLQ | DLQ > 0 → алерт за ≤ 5 мин | Мониторинг |\n| Лаг очереди нотификаций | ≤ , old_string="| Trace id на операцию | 100 % операций | APM |\n| Алерт на DLQ | DLQ > 0 → алерт за ≤ 5 мин | Мониторинг |\n| Лаг очереди нотификаций | ≤ )`
  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/solutioning.md", old_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scop, new_string="Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Рекуррентные C2B-)`

Now update docs/solutioning.md:
1. §1 roadmap — move автоплатежи from "вне scope" to "in scope via ADR-008".
2. §5 разбиение на решения table — add ADR-008 row.
3. §10 open questions — maybe add a note, but §1 change is the main one. Also §9 gaps — add protocol автоплатежей gap.

Let me edit §1 first. The current text:
```
Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи.
```

Change to:
```
Сценарии C2B в scope: динамический QR, статический QR/наклейка, кассовые ссылки, оплата по ссылке в e-commerce, возвраты. Рекуррентные C2B-списания по согласию плательщика (подписки СБП) — в scope с ADR-008 (аддитивно). Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты.
```

Then §5 table add ADR-008 row. Current table ends with:
```
| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accepted) | AD-008 [ADOPTED] |
```

Add:
```
| Рекуррентные C2B-списания по согласию (подписки) | ADR-008 | AD-009, AD-010 |
```

Then §9 gaps — add a row for протокол автоплатежей НСПК. Current gaps table ends with:
```
| Выбор конкретного вендора транспорта ОПКЦ | RFP по критериям ADR-007 (сертификаты ФСТЭК, тестовый контур, SLA, референсы) | Проектный офис / закупки |
```

Add:
```
| Протокол согласий/дебитов НСПК (автоплатежи): поля, события, тайминги, отказные коды | Документация НСПК по сервису автоплатежей (Портал поддержки) | Проектный офис / НСПК |
```

Then §10 open questions — add:
```
5. Модель источника истины согласия (НСПК vs шлюз) и бизнес-правила лимитов/частоты/ревока — на решение человека (см. ADR-008 §12).
```

Let me do these edits. First §1.

Actually, let me do them as separate edits in sequence. Let me read the relevant lines to get exact strings. I already have solutioning.md content from earlier. Let me do the edits.

Edit 1: §1 roadmap line.
Edit 2: §5 table row.
Edit 3: §9 gaps row.
Edit 4: §10 open questions.

Let me do them.
Обновлю `docs/solutioning.md`: scope, разбиение на ADR, gaps, открытые вопросы.

  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/solutioning.md", new_string="| НПС/КИИ/ПДн: trust-зоны, ГОСТ | ADR-006 | AD-006, AD-007 |\n| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accept, old_string="| НПС/КИИ/ПДн: trust-зоны, ГОСТ | ADR-006 | AD-006, AD-007 |\n| Стратегия реализации (гибрид) — **A3 принято 2026-08-15** | ADR-007 (Accept)`
  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/solutioning.md", new_string="| Контракт АБС на зачисление/списание (идемпотентность, SLA) | Интервью с владельцем АБС | Архитектор + АБС |\n| Протокол согласий/дебитов , old_string="| Контракт АБС на зачисление/списание (идемпотентность, SLA) | Интервью с владельцем АБС | Архитектор + АБС |\n| Категория объекта КИИ, сос)`
  `read_file(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/solutioning.md", offset=172)`

Now add open questions in §10. Let me read §10 exact text.

  `edit(file_path="<HARNESS>/runs/cells/plain-r1/ws/docs/solutioning.md", new_string="1. Объём первой волны: только C2B-приём или сразу C2C/выплаты? (влияет на состав адаптеров, но не на ядро).\n2. Требования бизнеса к комисс, old_string="1. Объём первой волны: только C2B-приём или сразу C2C/выплаты? (влияет на состав адаптеров, но не на ядро).\n2. Требования бизнеса к комисс)`
  `run_shell_command(command="cd <HARNESS>/runs/cells/plain-r1/ws && python3 -c \"import yaml,sys; yaml.saf, description="Валидация YAML и фитнес-правил")`

Now let me verify the changes against the fitness rules in CONSTRAINTS.yaml:
1. `adr-set-complete`: docs/adr/ADR-001-outbox.md exists — yes.
2. `spine-present`: ARCHITECTURE-SPINE.md exists — yes.
3. `nfr-measurable`: docs/nfr.md must contain '99,95' — yes (still has ≥ 99,95 %).
4. `abs-credit-only-from-paid`: ADR-005 contains 'только из состояния `PAID`' — I didn't touch ADR-005, so still present.
5. `adr-no-placeholders`: docs/adr/*.md must NOT contain '<!--'. My ADR-008 has no HTML comments. But wait — the other ADRs (ADR-001..007) — do they contain '<!--'? They don't (I read them). Good. My ADR-008 doesn't either.
6. `readme-exists`: README.md — warn, fine.
7. `spine-lints-clean`: ARCHITECTURE-SPINE.md must NOT contain 'TODO|TBD|XXX'. My AD-009/AD-010 additions — let me verify no TODO/TBD/XXX. I wrote "реккурентная авторизация" (not "TODO"), no TBD, no XXX. Good.

Let me also verify the openapi yaml is valid. Let me run a quick check if there's a YAML linter available. Actually, I should verify the YAML parses. Let me check with python if available.

Let me also double-check the ADR-008 file doesn't contain '<!--' and the spine additions. And run git status/diff to review.

Let me run a quick validation:
1. Check the openapi yaml is valid YAML (python yaml).
2. grep for '<!--' in docs/adr/ADR-008 (should be none).
3. grep for TODO/TBD/XXX in ARCHITECTURE-SPINE.md.

Let me also verify the '99,95' is still in nfr.md.

Let me run these checks.
Проверю целостность изменений: валидность YAML, фитнес-правила (`adr-no-placeholders`, `spine-lints-clean`, `nfr-measurable`).

  `run_shell_command(command="cd <HARNESS>/runs/cells/plain-r1/ws && git status --short && echo \"=== diffs, description="Обзор изменённых файлов")`

All checks pass. Now let me do a final review with git diff to confirm all changes are correct and coherent, and to make sure I haven't broken anything.
Все проверки проходят. Финальный обзор изменений.


All changes are in place. Let me do a final summary. The task asked me to:
1. Оценка значимости и маршрута ✓ (ADR-008 §1)
2. Влияние на принятую архитектуру ✓ (ADR-008 §3 + spine AD-009/AD-010)
3. Архитектурное решение с альтернативами, последствиями, обратимостью ✓ (ADR-008 §4-§7)
4. Изменения контрактов ✓ (tsp-api.md + tsp-api.yaml + opkc-adapter.md)
5. Измеримые NFR ✓ (nfr.md §7)
6. Критерии приёмки и план отката ✓ (ADR-008 §10-§11)
7. Что остаётся на решение человека ✓ (ADR-008 §12)

Now I'll write the final concise summary listing created and changed files. I should not write code, and I should be concise but complete.

I won't commit (the user didn't ask to commit). I'll just summarize.

Let me write the final response in Russian (matching user's language).
Готово. Пакет архитектурного изменения подготовлен поверх принятого решения без написания кода, строго по конвенциям репозитория (ADR-формат, spine-блоки `AD-XXX`, контракты в `docs/contracts/` + `openapi/`, NFR, статусная машина, solutioning).

## Что сделано

**1. Оценка значимости и маршрута** — `docs/adr/ADR-008-…` §1: **High ≈ 9/15, Feature increment поверх Critical**. Полный Solutioning не нужен — инкрементальное проектирование (новый ADR + 2 spine-инварианта + аддитивное расширение контрактов/NFR/статусной машины), прохождение тех же гейтов A0–A5.

**2. Влияние на инварианты** — ADR-008 §3: таблица «что меняется / что нет» по AD-001…AD-008. Ключевое: AD-005 (зачисление только из `PAID`) **сохраняется**, дебит — тот же платёж без QR; расширяются AD-002/AD-003/AD-007; AD-001/AD-004/AD-006/AD-008 не меняются. В spine добавлены **AD-009 (согласие)** и **AD-010 (рекуррентное списание как платёж без QR)**.

**3. Архитектурное решение** — ADR-008: согласие — сущность первого класса (источник авторизации — контур СБП, шлюз хранит проекцию), дебит переиспользует статусную машину платежа, минуя `QR_ISSUED`; 4 отвергнутые альтернативы (card-on-file, отдельный сервис, «нулевой платёж», всё в вендоре); последствия и обратимость `reversible (код) / irreversible (фин. операции)`.

**4. Изменения контрактов (без поломки потребителей)** — новые пути `/v1/consents*` и `/v1/consents/{id}/debits`, опциональные поля `consentId`/`paymentType` в `Payment` (default `ONE_SHOT`), новые события вебхуков и коды ошибок; адаптер ОПКЦ расширен методами/событиями согласий и дебитов аддитивно.

**5. NFR** — `docs/nfr.md` §7: доступность ≥ 99,95 %, p95 < 500 мс, зачисление дебита p95 < 60 с, RPO=0/RTO≤1 ч, дублей 0, ежечасная сверка согласий, дебит при неактивном согласии — отклонение 100 %.

**6. Приёмка и откат** — ADR-008 §10–§11: 10 проверяемых критериев (позитивные + негативные: гонка ревока, дубли, отказ АБС) и план отката через фиче-флаг `recurrent` с сигналами-триггерами и владельцем решения.

**7. На решение человека** — ADR-008 §12: 6 пунктов (модель источника истины согласия, бизнес-правила лимитов/частоты/ревока, регуляторная классификация 152-ФЗ/161-ФЗ, протокол НСПК, влияние на контракт вендора, приоритизация волн) с обоснованием, почему это не архитектурное единоличное решение.

## Файлы

**Создан:**
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`

**Изменены:**
- `ARCHITECTURE-SPINE.md` — AD-009, AD-010
- `docs/contracts/tsp-api.md` — §3.6/3.7, ошибки, вебхуки, версии, открытые вопросы
- `docs/contracts/opkc-adapter.md` — методы/события согласий и дебитов, идемпотентность
- `openapi/tsp-api.yaml` — новые пути и схемы (v0.2.0, аддитивно)
- `docs/spec/state-machine.md` — §7 согласие, §8 дебит
- `docs/nfr.md` — §7 NFR рекуррентных списаний
- `docs/solutioning.md` — scope, разбиение ADR, gaps, открытые вопросы

Проверки: YAML валиден, фитнес-правила (`adr-no-placeholders`, `spine-lints-clean`, `nfr-measurable`) проходят. `.arch-handoff/` не трогал — это сгенерированный snapshot для кодового харнесса, он перегенерируется при handoff.
