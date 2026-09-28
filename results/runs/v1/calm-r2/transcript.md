<!-- источник: <HARNESS>/runs/cells/calm-r2/home/.qwen/projects/-home-roman----------Qwen-Code-Spine-OpenSpec-BMAD-Superpowers-live-tui-runs-cells-calm-r2-ws/chats/15fae2bd-635e-46c4-a9ef-b1b1970dca2d.jsonl -->


### ▶ Запрос оператора 1

Ты — solution-архитектор банка. Репозиторий — принятое решение «Платёжный шлюз СБП (C2B-приём)»: `ARCHITECTURE-SPINE.md` (инварианты AD-001…AD-008), `docs/` (solutioning, NFR, ADR-001…007, контракты, статусная машина), `openapi/tsp-api.yaml` (контракт API ТСП v0.1), `.arch-handoff/` (правила и пакет передачи). Задача бизнеса. ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Сейчас каждый платёж требует QR и действия клиента. Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям. Код не пиши. Что должно получиться: 1. Оценка значимости изменения и маршрута (насколько глубокое проектирование нужно и почему). 2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет. 3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью. 4. Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей. 5. Измеримые NFR для нового функционала. 6. Критерии приёмки и план отката. 7. Что остаётся на решение человека-архитектора и почему. Принятые файлы решения меняй только тем способом, который принят в этом репозитории. В проекте могут быть установлены методические навыки и инструменты — используй их по назначению. Когда закончишь, кратко перечисли созданные и изменённые файлы.

  `skill(skill="calm")`

The user wants me to act as a solution architect for a bank. The repository is an accepted solution "СБП Payment Gateway (C2B acceptance)". They want an architectural package for a change: recurring C2B debits by payer consent (СБП subscriptions). Currently every payment requires QR and client action.

They explicitly say: "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." (The project may have methodological skills and tools installed — use them for their intended purpose.)

I see there's a `calm` skill (project) — "An AI Assistant for FINOS CALM development." And there's `.arch-handoff/` directory, ARCHITECTURE-SPINE.md, docs/ with ADRs, etc. The user is asking me to prepare an architectural package.

First, I should invoke the `calm` skill since it's project-level and directly relevant. Let me also explore the repository structure to understand conventions.

The instruction says: "When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action." The `calm` skill is clearly relevant. Also possibly there are other skills in `.qwen/skills/` and `.claude/skills/`.

Let me start by invoking the `calm` skill, and simultaneously explore the repo. Actually, the skill invocation should be my first action. Let me invoke the skill first.

Actually, I should invoke the `calm` skill as my first action. Let me do that.

  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/architecture)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/calm-cli-ins)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/node-creatio)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/relationship)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/interface-cr)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/metadata-cre)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/control-crea)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/flow-creatio)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/pattern-crea)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/documentatio)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/standards-cr)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/moment-creat)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/timeline-cre)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.claude/skills/calm/calm-prompts/decorator-cr)`

Let me follow the skill instructions. First display "Loading FINOS CALM instructions..." and read the tool prompt files. Let me read the key ones. Actually, the skill says I MUST read those files. Let me read them. There are 14 files. Let me read the most relevant ones. But it says I MUST read all of them. Let me read them efficiently in parallel.

Actually, let me first understand the repo structure and the CALM skill. But the skill is about CALM modeling. The user's task is architectural work, and the repo uses `.arch-handoff/` (Architectural handoff), `docs/` with ADRs, `openapi/tsp-api.yaml`. The `calm` skill might not be the core thing — but the user said "methodological skills and tools installed — use them." Let me read the CALM prompt files as instructed, and also explore the repo.

Let me read the CALM prompt files in parallel, plus explore the repo structure.

Actually, the skill's "First Interaction Instructions" are explicit and mandatory. Let me read those files. Let me batch read them.

But wait — there might be other skills too. Let me check `.qwen/skills/` and `.claude/skills/` directories. Actually the available_skills listing only shows `calm` as a project skill. There might be other skills in the directories but not registered. Let me explore.

Let me do the CALM instructions first, then explore the repo thoroughly.

Let me read the CALM prompt files. I'll batch them.
Loading FINOS CALM instructions...

  `glob(pattern="**/*", path="<HARNESS>/runs/cells/calm-r2/ws")`
  `run_shell_command(command="which calm && calm --version 2>/dev/null; echo \"---\"; ls -la <HARNESS>/runs, description="Check calm-cli and list skills directories")`

Now I understand the CALM skill. But the key thing to understand is whether the repo actually uses CALM (`.architecture.json`, `.timeline.json`, etc.) or uses `.arch-handoff/` with a different convention (ARCHITECTURE-SPINE.md with AD-001...AD-008 invariants, docs/ with ADRs, etc.).

The user's request is specifically about preparing an architectural package for a change: recurring C2B debits (СБП subscriptions). The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" (Change the accepted decision files only in the way accepted in this repository).

I need to understand the repository's actual conventions first. The CALM skill is available, but I need to check whether the repo actually uses CALM as its modeling method. The `.arch-handoff/` directory and ARCHITECTURE-SPINE.md, docs/ with ADRs suggest a different, more document-centric convention (possibly BMAD/Superpowers/OpenSpec style).

Let me explore the repo thoroughly. Key files to read:
1. `ARCHITECTURE-SPINE.md` — the invariants AD-001...AD-008
2. `README.md`
3. `.arch-handoff/TASK.md`, `ARCHITECTURE.md`, `CONSTRAINTS.yaml`, `MANIFEST.json`, `RUBRIC.yaml`
4. `.arch-handoff/adr/`
5. `docs/nfr.md`, `docs/solutioning.md`, `docs/adr/`
6. `openapi/tsp-api.yaml`
7. `.qwen/skills/` — check what skills exist besides calm
8. `.claude/skills/`

Let me first get the full directory listing and read the key files. Let me also check if there's a calm-cli installed (`which calm`).

Let me do a broad exploration. I'll use glob to find files, and read the key ones in parallel.

Let me first list the full structure.

  `run_shell_command(command="cd <HARNESS>/runs/cells/calm-r2/ws && find . -type f -not -path './node_modul, description="List all project files excluding node_modules and .git")`

The `calm` CLI is not installed. There's only the `calm` skill in both `.qwen/skills/` and `.claude/skills/`. Let me explore the actual project files (not node_modules). Let me look at the directory structure excluding node_modules.

Let me read the key files.

  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/README.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/ARCHITECTURE-SPINE.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.arch-handoff/TASK.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.arch-handoff/ARCHITECTURE.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.arch-handoff/CONSTRAINTS.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.arch-handoff/MANIFEST.json")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.arch-handoff/RUBRIC.yaml")`

Now I have the full picture. The project files are:
- `ARCHITECTURE-SPINE.md` — invariants
- `.arch-handoff/` — ARCHITECTURE.md, CONSTRAINTS.yaml, MANIFEST.json, RUBRIC.yaml, TASK.md, adr/ADR-001..007
- `docs/` — nfr.md, solutioning.md, adr/ADR-001..007, contracts/opkc-adapter.md, contracts/tsp-api.md, rfp/vendor-rfp.md, spec/state-machine.md
- `openapi/tsp-api.yaml` — API contract
- `README.md`
- skills: calm (in both .qwen and .claude)

Note there's no `.architecture.json` or `.timeline.json` CALM files. The repo convention is document-centric (ARCHITECTURE-SPINE.md, ADRs in docs/adr/, .arch-handoff/). So the CALM skill is available but the repo doesn't use CALM JSON models. The task says "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" — meaning I should follow the repo's ADR/arch-handoff convention, not invent CALM JSON files.

Wait, but let me carefully check the README and the .arch-handoff files to understand the exact convention. Let me read all the key files.

Let me read them in parallel:
1. README.md
2. ARCHITECTURE-SPINE.md
3. .arch-handoff/TASK.md
4. .arch-handoff/ARCHITECTURE.md
5. .arch-handoff/CONSTRAINTS.yaml
6. .arch-handoff/MANIFEST.json
7. .arch-handoff/RUBRIC.yaml
8. docs/solutioning.md
9. docs/nfr.md
10. openapi/tsp-api.yaml
11. docs/contracts/tsp-api.md
12. docs/contracts/opkc-adapter.md
13. docs/spec/state-machine.md
14. docs/adr/ADR-001..007 (and .arch-handoff/adr copies)
15. docs/rfp/vendor-rfp.md
16. .qwen/skills/calm/SKILL.md and .claude/skills/calm/SKILL.md

Let me read the most important ones first in a batch.

  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/solutioning.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/nfr.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/contracts/tsp-api.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/contracts/opkc-adapter.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/spec/state-machine.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/openapi/tsp-api.yaml")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/.qwen/skills/calm/SKILL.md")`

Now I have a good understanding of the repo. This is a BMAD/OpenSpec-style architecture repository with:
- `ARCHITECTURE-SPINE.md` — invariants AD-001..AD-008
- `docs/solutioning.md`, `docs/nfr.md`, `docs/contracts/`, `docs/spec/`, `docs/rfp/`, `docs/adr/ADR-001..007`
- `.arch-handoff/` — handoff package (epic-context, constraints, rubric, manifest, task)
- `openapi/tsp-api.yaml` — API contract

The user's task is to prepare an architectural package for a NEW change: **recurring C2B debits by payer consent (СБП subscriptions)**. Currently every payment requires QR + client action.

The task requires me to produce:
1. Assessment of significance and route (how deep the design needs to be and why)
2. Impact on accepted architecture: which invariants are touched, what changes, what doesn't
3. Architectural decision with alternatives, consequences, reversibility
4. Contract changes (openapi/tsp-api.yaml) without breaking existing consumers
5. Measurable NFRs for new functionality
6. Acceptance criteria and rollback plan
7. What remains for the human architect to decide and why

The user says: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории" (change accepted decision files only in the way accepted in this repo). So I need to follow the ADR/ADR-XXX convention, docs/, etc. I should NOT modify existing ADR-001..007, ARCHITECTURE-SPINE.md invariants lightly — instead add new ADR(s) and possibly a new spine block? Let me think about the correct approach.

Actually, the way this repo works:
- New architectural decisions → new ADR files in `docs/adr/ADR-XXX-....md` (next number ADR-008)
- Invariants → new blocks in ARCHITECTURE-SPINE.md (AD-009...)
- Contract changes → openapi/tsp-api.yaml + docs/contracts/tsp-api.md
- NFRs → docs/nfr.md (append or new section)
- The solutioning.md is the full design

But I need to be careful. The user is asking me to "prepare an architectural package of this change" so it can be "вынести на архитектурное решение" (brought to an architectural decision) and then "передать исполнителям" (handed to implementers).

So the deliverable is a set of documents. Let me understand the exact structure and conventions of each document before writing.

Let me read the remaining key documents:
- docs/solutioning.md (full design)
- docs/nfr.md
- docs/contracts/tsp-api.md
- docs/contracts/opkc-adapter.md
- docs/spec/state-machine.md
- docs/rfp/vendor-rfp.md
- docs/adr/ADR-001..007 (full)
- openapi/tsp-api.yaml
- .qwen/skills/calm/SKILL.md (to understand the skill's SKILL.md)

Also I should check if there's a SOURCE_BRIEF.md or other methodology docs referenced. The RUBRIC mentions "docs/SOURCE_BRIEF.md §A.3" — but that's not in the file list. Let me check the git log and any other references.

Also important: I need to understand whether the recurring C2B debits (subscriptions) is actually a supported СБП feature. In reality, СБП (SBP - Russian Faster Payments System) does have a feature for "подписки" / recurring payments via consent (согласие на списание). Actually СБП has "С2В-подписки" / "платежи по подписке" — the feature is called "СБП C2B подписки" or "автоплатежи по СБП". There's a consent (согласие) mechanism where the payer gives consent to the TSP to debit their account. Actually, in СБП there is a mechanism of "согласие на списание" (standing order / consent) — НСПК introduced "С2В-подписки" (subscriptions) with consent-based debits. This is real: СБП added recurring payments feature.

I should be careful about the actual protocol details — I'll mark anything requiring НСПК documentation as [ТРЕБУЕТ ПРОВЕРКИ] consistent with the repo's convention.

Let me read the rest of the documents. Let me batch-read.

Let me read the solutioning.md, nfr.md, contracts, state-machine, rfp, and the ADR files in full, plus openapi/tsp-api.yaml, and the calm SKILL.md.

  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/adr/ADR-001-outbox.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/adr/ADR-002-model-konsistentnosti-platez)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/adr/ADR-003-mtls.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/adr/ADR-004-at-least-once-dlq.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/adr/ADR-005-integraciya-s-abs-zachisleni)`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/adr/ADR-006-trust.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/adr/ADR-007-proposed-a3.md")`
  `read_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/rfp/vendor-rfp.md")`

Now I have a comprehensive understanding. The repo convention is:
- BMAD/OpenSpec-style with `ARCHITECTURE-SPINE.md` (invariants AD-XXX), `docs/solutioning.md` (full design), `docs/nfr.md`, `docs/adr/ADR-XXX-....md` (decision records), `docs/contracts/`, `docs/spec/`, `docs/rfp/`, `openapi/tsp-api.yaml`, `.arch-handoff/` (handoff package).

Note: The `calm` skill is about FINOS CALM JSON modeling, but the repo does NOT use CALM `.architecture.json` files. The repo uses markdown ADRs and a "spine" of invariants. The CALM skill's "First Interaction Instructions" told me to read the prompts, which I did. But actually the CALM skill is not the primary methodology here — the repo is BMAD/OpenSpec-style. The `calm` skill was registered but the repo's actual convention is document-centric (spine + ADRs + solutioning + NFR).

Actually, wait — I need to think about whether I should produce CALM artifacts. The user said "В проекте могут быть установлены методические навыки и инструменты — используй их по назначению." (The project may have methodological skills and tools installed — use them for their intended purpose.) The only skill installed is `calm`. But the repo has no CALM files. The task is clearly about the BMAD/OpenSpec document convention.

The `calm` skill is about CALM JSON modeling, which doesn't match this repo. So I should note that CALM is available but not the repo's actual convention, and follow the repo's convention (spine + ADR + solutioning + NFR + openapi). Actually, I should be careful — the "calm" skill name coincides with "calm-r2" in the path, which is just the workspace name (cell name). This might be a red herring / the skill is a generic CALM skill installed by default.

Actually, let me reconsider. The key instruction is "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — "Change accepted decision files only in the way accepted in this repository." So the method is: add ADR-008 (new), possibly new spine blocks (AD-009+), extend docs/solutioning.md or create a new solutioning doc for the change, extend docs/nfr.md, extend docs/contracts/tsp-api.md + openapi/tsp-api.yaml, extend docs/spec/state-machine.md, and possibly update the .arch-handoff package.

Let me read the remaining ADR files fully (ADR-001 through ADR-007) to understand the exact ADR format and content. I've seen ADR-001 and part of ADR-002 in the ARCHITECTURE.md (epic-context, truncated). Let me read the full ADR files to match their exact structure and to know the content of ADR-002 through ADR-007.

Also I should read docs/rfp/vendor-rfp.md.

Let me read all the ADR files in full.

  `run_shell_command(command="cd <HARNESS>/runs/cells/calm-r2/ws && ls -la && echo \"--- package.json? ---\, description="Inspect root files, package.json, and git state")`

I now have a comprehensive understanding of the repository's conventions and content. Let me note the key facts:

1. The repo is BMAD/OpenSpec-style with:
   - `ARCHITECTURE-SPINE.md` — invariant spine AD-001..AD-008, with "Deferred" section listing roadmap items (including "автоплатежи" — autopayments!). This is key: "автоплатежи" is in the Deferred section of solutioning.md (roadmap, вне scope) and README mentions "автоплатежи" in the roadmap.
   
   Wait, let me re-check. In solutioning.md §1: "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." So "автоплатежи" (autopayments) is explicitly listed as outside scope / roadmap.

   In ARCHITECTURE-SPINE.md Deferred section: "C2C-переводы и выплаты B2C/B2B: roadmap после стабилизации C2B; вернуть как отдельный initiative." And "Диспуты/претензии (disputes)". Note "автоплатежи" is NOT explicitly in the spine Deferred section — only in solutioning.md §1 as roadmap.

   So the recurring C2B debits (подписки СБП / рекуррентные списания по согласию) is essentially what was called "автоплатежи" in the roadmap. This is a NEW feature that extends the C2B acceptance.

2. The task asks me to prepare an architectural package for this change, to be brought to architectural decision (A3-like human decision) and then handed to implementers.

Key deliverables required:
1. Оценка значимости изменения и маршрута (significance assessment and route — how deep design needed and why)
2. Влияние на принятую архитектуру: какие инварианты затронуты, что меняется, что нет (impact on accepted architecture)
3. Архитектурное решение с рассмотренными альтернативами, последствиями и обратимостью (architectural decision with alternatives, consequences, reversibility)
4. Изменения контрактов (openapi/tsp-api.yaml) без поломки существующих потребителей (contract changes without breaking existing consumers)
5. Измеримые NFR для нового функционала (measurable NFRs for new functionality)
6. Критерии приёмки и план отката (acceptance criteria and rollback plan)
7. Что остаётся на решение человека-архитектора и почему (what remains for human architect to decide and why)

The user also says: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." (Change accepted decision files only in the way accepted in this repo.)

So the correct approach is:
- Create a new ADR (ADR-008) for the recurring C2B debits / subscriptions feature. Actually, wait — ADR-007 is the last one. So the next is ADR-008.
- Add a new spine block AD-009 (or multiple) to ARCHITECTURE-SPINE.md for the new invariants, following the existing format. Actually, the spine blocks are "инварианты" — the new feature would add new invariants (e.g., "списание только по действующему согласию", "согласие как отдельная сущность с жизненным циклом").
- Extend docs/solutioning.md with a new section or create a separate solutioning doc? The user wants an "архитектурный пакет" (architectural package). Given the repo structure, I think the cleanest is:
  - New ADR(s) in docs/adr/ (ADR-008)
  - New spine block(s) in ARCHITECTURE-SPINE.md (AD-009+)
  - Extend openapi/tsp-api.yaml (add consent + subscription/debit endpoints, backwards compatible)
  - Extend docs/contracts/tsp-api.md (or create a new contract doc)
  - Extend docs/nfr.md (new NFR section for subscriptions)
  - Extend docs/spec/state-machine.md (new state machine for consent/subscription) or create docs/spec/consent-machine.md
  - Possibly a new solutioning doc: docs/solutioning-subscriptions.md or extend docs/solutioning.md

Actually, I should think about what's the minimal, correct set of changes that respects the repo convention.

The user's deliverable list is essentially a "solutioning" + "ADR" + "NFR" + "contracts" + "acceptance/rollback" package. The most natural mapping:

1. Оценка значимости и маршрут → a new solutioning document (or a section), e.g. `docs/solutioning-subscriptions.md` that opens with the significance/route assessment (маршрут Critical/High/Medium + why).

Actually, looking at the existing solutioning.md, it opens with "Маршрут: **Critical** (значимость 11/15)." So the significance assessment is a "маршрут" with a significance score /15. This is a BMAD convention (significance 11/15, route Critical).

Let me think about the BMAD methodology. "BMAD" = "Bank Method for Architecture Development"? Or "Superpowers" / "OpenSpec"? The repo references:
- "BMAD epic-context" (in RUBRIC.yaml)
- "OpenSpec" (in the path name)
- "Superpowers" (in path name)

The "значимость X/15" and "маршрут Critical/High/..." suggests a significance scoring model. Let me check if there's a methodology doc somewhere. The RUBRIC.yaml references "docs/SOURCE_BRIEF.md §A.3" but that file doesn't exist in the repo (it's an external reference to the methodology).

Actually, I shouldn't over-engineer. The repo gives me concrete examples of the format. I should:
1. Produce an ADR-008 (or ADR-008 + ADR-009) for the decision.
2. Add spine invariants.
3. Extend contracts.
4. Extend NFR.
5. Extend state machine spec.
6. Write a solutioning doc for the change (with significance/route assessment).
7. Possibly update the .arch-handoff package.

Let me think carefully about the content of the architectural decision. This is the core intellectual work.

**The business change: recurring C2B debits (subscriptions) by payer consent.**

Currently: every C2B payment requires QR + client action. The TSPs (online cinemas, ЖКХ/utilities, telecom) want subscriptions: payer gives a one-time consent, then TSP can debit their account on a schedule without the payer's action each time.

In СБП (Russian Faster Payments System), the real mechanism is:
- СБП introduced "платежи по подписке" (subscription payments) / "согласие на списание" (consent for debit) — this is the "С2В-подписки" feature. Actually, in real СБП, there's a "СБП-подписка" (recurring C2B) feature. The payer gives consent via their bank app (Банк плательщика), and the consent is stored, allowing the TSP to initiate recurring debits.

Actually, the exact mechanism in СБП: The payer, in their bank's app (Банк плательщика), subscribes to a service and gives consent for recurring debits. The consent is registered with the payer's bank. Then the TSP/merchant can initiate debits. There's a concept of "согласие плательщика на списание" (standing order) and "платёжные требования" / "списания по подписке".

Since I'm a solution architect and the exact protocol is [ТРЕБУЕТ ПРОВЕРКИ] (external input from НСПК documentation), I should design at the level of the internal contract and mark protocol details as [ТРЕБУЕТ ПРОВЕРКИ], consistent with the repo's convention.

Key architectural considerations for this change:

**Core concept: Consent (согласие) becomes a first-class entity.**

New domain entities:
1. **Consent (согласие на списание / подписка)** — a durable agreement between payer and TSP, with:
   - consentId
   - payer reference (as required for СБП — probably masked phone number / account reference)
   - TSP (merchant) reference
   - maximum amount per debit / total cap / frequency (limits)
   - validity period (start/end), schedule
   - status lifecycle: PENDING (awaiting payer confirmation in payer's bank app) → ACTIVE → PAUSED → CANCELLED → EXPIRED → REVOKED
   - The consent is confirmed by the payer via their bank (Банк плательщика), NOT by the acquiring bank's gateway directly. So consent confirmation flow goes through НСПК/Банк плательщика.

2. **Recurring debit (списание / subscription payment)** — a C2B payment triggered by the TSP under an active consent, WITHOUT QR and WITHOUT payer action. This reuses the existing payment state machine (CREATED → ... → COMPLETED) but the trigger is different (no QR, no payer action; it's a "списание по согласию").

**Impact on invariants (AD-001..AD-008):**

- AD-002 (single source of truth — payment state machine): The payment state machine still applies to each debit. But we need a NEW state machine for the **consent** entity (separate lifecycle). So AD-002's rule extends to consent (the consent is also a state machine with atomic transitions + outbox). Actually, AD-002 is about "платеж" specifically. We should extend the concept: "любой финансово-значимый объект (платёж, согласие, возврат) — конечный автомат с атомарными переходами". This is a refinement/extension of AD-002.

- AD-005 (зачисление только из PAID): still holds — each recurring debit must reach PAID (confirmed by НСПК) before АБС credit. Actually for subscription debits, the flow may be slightly different (the debit is confirmed/executed by НСПК/Банк плательщика), but the principle "зачисление только из подтверждённого статуса" holds. This invariant is NOT changed, just applied.

- AD-003 (идемпотентность): extends to consent operations (Idempotency-Key for consent creation, eventId for consent status changes, debitId for debits).

- AD-001 (изоляция): consent and debits go through the same gateway, same adapters. No change to the isolation principle; just more entities within the gateway.

- AD-004 (единственный адаптер ОПКЦ): the adapter must support consent operations + subscription debit operations. This is a CONTRACT extension to opkc-adapter.md, not an invariant change.

- AD-006 (trust zones): no change.

- AD-007 (НПС/КИИ/ПДн): consent introduces NEW sensitive data (payer's consent, maybe more payer PII than before — currently C2B QR doesn't store much payer data; consent requires payer identification/reference). This has ПДн implications. Actually — importantly, the consent references the payer, which is more ПДн than the current QR flow (where the gateway mostly doesn't know the payer). This is a notable compliance impact.

- AD-008 (гибрид strategy): unchanged, but the vendor adapter contract must be extended with consent/subscription methods.

So the impact summary:
- **New invariant(s)**: consent as first-class entity with its own state machine; debit only under ACTIVE consent within limits; consent revocation stops future debits immediately.
- **Extended**: AD-002 (state machine covers consent too), AD-003 (idempotency for consent), AD-004 (adapter contract extended).
- **Unchanged**: AD-001, AD-005, AD-006, AD-007, AD-008 (principles unchanged, scope widened).

**The decision: what are the alternatives?**

The key architectural decision (ADR-008) is about how to model the consent and recurring debit:

Alternative A: **Consent as first-class entity in the gateway, with its own state machine and limits; debits reuse the payment state machine.** (Recommended — consistent with AD-002 philosophy.)

Alternative B: **Consent lives entirely in НСПК/Банк плательщика; gateway is a thin passthrough for subscription debits.** (Less control, but less scope — the gateway just forwards TSP debit requests to НСПК which does the consent check.)

Alternative C: **Store consent in АБС (or another existing system) and only route debits through the gateway.** (Reuses existing consent infrastructure, but splits the source of truth.)

Actually, let me think about the real СБП subscription model more carefully, because it determines what's actually feasible.

In real СБП:
- СБП C2B подписки: The payer subscribes in the ТСП's app/site or in the payer's bank app. The consent ("согласие на списание") is registered. The acquiring bank's gateway receives a "списание по подписке" request from the ТСП, which references the consent. НСПК validates the consent with the payer's bank, and executes the debit. The payer does NOT scan QR or confirm each time.

Actually, the mechanism: In СБП subscriptions, the payer's consent is given once (usually via the payer's bank mobile app, where they approve the subscription). The consent is stored at the payer's bank (Банк плательщика) side, and НСПК coordinates. The acquiring bank's role is to receive the debit instruction from the ТСП and forward to НСПК, then credit the ТСП's account.

There are important nuances:
1. The **consent is confirmed by the payer's bank**, not the acquirer. The acquirer's gateway initiates a consent request that the payer must approve in their bank app.
2. The **payer can revoke** the consent at any time via their bank app.
3. The **ТСП can pause/cancel** the subscription.
4. Each debit is subject to limits defined in the consent (max amount, frequency).

So the gateway needs:
- Consent lifecycle management (initiate consent, receive consent status from НСПК, revoke).
- Debit initiation under consent.
- Idempotency and reconciliation for both consent and debits.

Given the repo's hybrid strategy (ADR-007), the vendor adapter must implement the consent + subscription-debit protocol, normalized into the internal contract.

OK. Let me now think about the significance/route assessment.

The BMAD "маршрут" (route) seems to have levels: Critical, High, Medium, Low — with a significance score /15. The existing C2B project is "Critical (значимость 11/15)".

For this change:
- New financial capability (recurring debits = money movement without per-transaction payer action) — financially significant, high fraud risk (a stolen/compromised consent = unauthorized debits).
- Regulatory impact: 161-ФЗ (НПС) has specific rules for recurring/standing orders and consent; ПДн (152-ФЗ) — more payer data; 115-ФЗ — fraud/AML on recurring.
- It extends a Critical initiative but is itself a well-scoped feature on top of existing infrastructure.

So significance: I'd estimate this as **High (значимость ~9/15)** — significant but it's an extension of an already-designed Critical platform, reusing the payment state machine, outbox, adapter pattern. Not as high as the initial Critical (11/15) because the platform exists, but it touches new financial semantics (consent, unauthorized debit risk) and compliance.

Actually, let me reconsider. The significance and route assessment should justify how deep the design needs to go. Since this is a NEW financial capability with:
- new domain entity (consent) with lifecycle,
- new compliance surface (consent revocation, dispute/chargeback for recurring, ПДн),
- new contract surface (TSP API + OPKC adapter),
- reuse of existing platform,

I'd argue the route is **High** with a focused but complete solutioning (one ADR + spine invariant + contract extensions + NFR + acceptance/rollback), NOT a full Critical re-solutioning. This is the "маршрут" part — how deep.

Now let me think about what "маршрут" means precisely in BMAD. Looking at the existing repo: solutioning.md says "Маршрут: Critical (значимость 11/15)". So "маршрут" = route = the level of design rigor required, and "значимость X/15" = significance score. The route likely determines the gates (A0-A5) and depth of solutioning.

I'll frame the significance/route assessment as: **High (значимость 8-9/15)**, route = "incremental architecture decision on top of accepted platform" — one ADR + spine invariant extension + contract version bump + NFR appendix + acceptance/rollback. Justify: (a) money movement without per-action consent → fraud risk; (b) new compliance surface; (c) but reuses Critical platform (state machine, outbox, adapter, trust zones) so no re-solutioning of ADR-001..007.

Let me now also think carefully about the **contract changes without breaking existing consumers**.

The openapi/tsp-api.yaml currently has:
- POST /v1/payments (createPayment)
- GET /v1/payments/{paymentId} (getPayment)

I need to add consent + subscription debit endpoints. To NOT break existing consumers:
- Add new endpoints (new paths), don't modify existing ones.
- Add new optional fields to existing schemas where needed (e.g., PaymentRequest could gain an optional "consentId" field to indicate a subscription debit — but that changes existing behavior slightly; actually a subscription debit should probably be a separate endpoint or a distinct "type" field).

Actually the cleanest backwards-compatible approach:
- New endpoints under /v1/consents (consent lifecycle): POST /v1/consents, GET /v1/consents/{consentId}, POST /v1/consents/{consentId}/revoke (or DELETE).
- New endpoint for subscription debit: POST /v1/consents/{consentId}/debits (or POST /v1/subscriptions/{...}/payments). This creates a debit under a consent, returning a paymentId that reuses the existing payment state machine and GET /v1/payments/{paymentId}.
- Add optional fields to PaymentRequest/Payment schema (e.g., "consentId", "paymentType": "qr" | "subscription") — but only ADD optional fields, never remove/rename/change existing required fields.
- Add new enum values to status if needed (consent status enum is separate).

The key: the existing `Payment` schema has `required: [paymentId, amount, status]` and `status enum: [CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED]`. For subscription debits, the state machine reuses these states (maybe skip QR_ISSUED since no QR). I should NOT change the existing enum (which would be a breaking change for clients that validate against it — though adding enum values is usually non-breaking for consumers but could break strict server-side). Actually adding a new enum value is generally non-breaking for consumers reading; but I should be careful: for subscription debits, the status flow might be CREATED → PAID → CREDITED → COMPLETED (no QR_ISSUED). I could reuse the existing statuses and just note that QR_ISSUED is skipped for subscription debits. That avoids changing the enum.

Actually, I should think about whether to bump the version. The existing contract is v0.1 (unstable draft). The tsp-api.md says "изменения, ломающие контракт, — только в /v2". Adding new endpoints + optional fields is NOT breaking, so stays in /v1. Good.

Let me plan the concrete file changes:

**New files:**
1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-podpiski-sbp.md` — the architectural decision.
2. `docs/solutioning-subscriptions.md` — the significance/route assessment + full solutioning of the change (or I could add it as a section to solutioning.md; but a separate doc keeps the accepted solutioning.md intact and the change clearly delimited). Actually, re-reading the task: "Подготовь архитектурный пакет этого изменения поверх принятого решения, чтобы его можно было вынести на архитектурное решение и затем передать исполнителям." — prepare an architectural package for THIS change, layered on top of the accepted decision, so it can be brought to architectural decision and then handed to implementers.

So the package should be self-contained and clearly delimited. A separate solutioning doc makes sense.

3. `docs/spec/consent-machine.md` — state machine spec for consent (and how debit reuses payment machine). OR extend state-machine.md. A separate spec doc is cleaner.
4. `docs/contracts/consent-api.md` — or extend tsp-api.md. Given tsp-api.md is the merchant API contract and it's getting new endpoints, I think extending tsp-api.md AND openapi/tsp-api.yaml is the right move. But a separate consent contract doc might be cleaner for handoff. Hmm.

Let me decide based on the "handoff" principle: the package must let implementers implement without access to original docs. So the changes must be in the canonical places:
- openapi/tsp-api.yaml (the machine-readable contract) — extend with consent + subscription endpoints.
- docs/contracts/tsp-api.md (human contract) — extend with new methods.
- docs/contracts/opkc-adapter.md — extend with consent + subscription-debit methods/events (because the vendor adapter must support them). This is important — the internal contract between core and transport needs new methods.
- docs/nfr.md — add NFR section for subscriptions.
- docs/spec/state-machine.md — add consent state machine (or new doc).
- ARCHITECTURE-SPINE.md — add AD-009 (consent invariant) and possibly AD-010.
- README.md — update structure/status.
- .arch-handoff — regenerate/update (TASK.md, ARCHITECTURE.md, MANIFEST.json, CONSTRAINTS.yaml, RUBRIC.yaml) to reflect the new scope. Actually, the .arch-handoff is the "handoff package" — but the user says "чтобы его можно было вынести на архитектурное решение и затем передать исполнителям" (to be brought to decision and THEN handed to implementers). So the handoff package update might be premature (it's for after the decision). But the .arch-handoff has TASK.md which describes the walking skeleton task. Hmm.

Actually, I should be careful not to over-produce. Let me focus on the 7 required deliverables and map them to the minimal correct set of files.

Let me re-map the 7 deliverables to files:

1. **Оценка значимости и маршрута** → new doc `docs/solutioning-subscriptions.md` (opening section) OR a dedicated `docs/adr/ADR-008...` + a significance note. I'll put it in a solutioning doc.

2. **Влияние на принятую архитектуру** → same solutioning doc (a section) + the spine changes + ADR.

3. **Архитектурное решение с альтернативами/последствиями/обратимостью** → `docs/adr/ADR-008-...md`.

4. **Изменения контрактов (openapi/tsp-api.yaml)** → edit `openapi/tsp-api.yaml` + `docs/contracts/tsp-api.md` + `docs/contracts/opkc-adapter.md`.

5. **Измеримые NFR** → edit `docs/nfr.md` (append new section).

6. **Критерии приёмки и план отката** → in the solutioning doc + ADR (reversibility) + NFR. I'll add a dedicated section in the solutioning doc.

7. **Что остаётся на решение человека-архитектора** → in the solutioning doc (open questions / human decisions section) + ADR status (Proposed, awaiting A3-like decision).

Plus:
- `ARCHITECTURE-SPINE.md` — add AD-009 (and possibly AD-010) invariants, and update the Deferred section (remove "автоплатежи" from roadmap/deferred, since now it's being brought in).
- `docs/spec/state-machine.md` — extend with consent state machine (or new doc `docs/spec/consent-machine.md`).
- `README.md` — update structure listing and status.

Let me think about whether to create a new spine block. The spine currently has AD-001..AD-008. The new invariant(s) would be AD-009 (and maybe AD-010).

What are the new invariants for subscriptions?

AD-009. **Согласие как отдельный источник истины / списание только по действующему согласию**:
- Rule: Списание (рекуррентный платёж) инициируется только при наличии действующего согласия плательщика (`ACTIVE`), в пределах лимитов согласия (макс. сумма, частота, срок). Отзыв/истечение согласия немедленно прекращает возможность новых списаний; уже инициированные списания завершаются по обычной статусной машине платежа.
- Binds: сущность «согласие», статусная машина платежа, адаптер ОПКЦ, антифрод.
- Prevents: списания без согласия или после отзыва; превышение лимитов; «подписки-призраки».

AD-010. **Идемпотентность и атомарность согласия** (maybe merge into AD-009 or AD-003 extension). Actually, consent operations must follow the same AD-002 (atomic transitions) and AD-003 (idempotency). I could add AD-010 for "согласие — конечный автомат с атомарными переходами и идемпотентностью" but that's basically AD-002 applied to consent. 

Hmm, let me think about whether AD-009 and AD-010 are both needed or just one.

Actually, I think the cleanest is:
- AD-009: **Рекуррентное списание только по действующему согласию в пределах лимитов** (the core new invariant).
- Possibly AD-010: **Согласие — полноправная сущность статусной машины шлюза с атомарными переходами и идемпотентностью** (extends AD-002/AD-003 to consent). But this could also be folded into AD-009 or noted as "extends AD-002".

I'll go with ONE new spine block AD-009 that captures the consent-as-source-of-truth + debit-only-under-active-consent + idempotency, and note it "extends AD-002, AD-003". Actually, to be clean and match the existing granularity (each AD is a distinct invariant), I'll create TWO: AD-009 (consent source of truth / lifecycle) and AD-010 (debit only under active consent within limits). Hmm, but that might be overkill.

Let me settle: I'll create **one new spine invariant AD-009** that captures the whole recurring-debit invariant, since the spine blocks are already fairly rich (each has Binds/Prevents/Rule). The single invariant: "Списание по согласию: согласие — первый класс, только ACTIVE, в пределах лимитов, отзыв немедленный, идемпотентность по consentId/debitId". This matches the existing AD-005 granularity (which is itself a rich invariant). Actually AD-005 is "зачисление только из PAID" — a single financial invariant. AD-009 "списание только по действующему согласию" is directly analogous. So ONE new block AD-009 is the right analogy.

Wait, but there might also be a distinct invariant about consent lifecycle state machine being atomic (AD-002 analog). But AD-002's Rule is generic enough ("Изменение финансового статуса платежа...") — I can extend AD-002's scope in the solutioning/ADR rather than the spine. The spine AD-002 says "финансового статуса платежа" — I could broaden to "финансового статуса платежа/согласия". But changing an existing invariant's Rule wording is risky ("конфликт эскалируется наверх"). I'll note in the ADR that AD-002's rule is **generalized** to consent, and propose the spine wording change as part of the change (to be ratified with the ADR). Actually the user says "какие инварианты затронуты, что меняется, что нет" — so I should explicitly say which invariants change and how.

Let me structure the impact precisely:
- **AD-002 (статусная машина платежа)** — принцип неизменен, **область расширяется** на сущность «согласие» (согласие тоже конечный автомат с атомарными переходами + outbox + аудит). Wording change: "платежа" → "платежа и согласия" (или добавить отдельную формулировку).
- **AD-003 (идемпотентность)** — принцип неизменен, **добавляются новые ключи**: `Idempotency-Key` для создания согласия, `consentId`/`debitId`/`eventId` для списаний. Binds-список расширяется.
- **AD-004 (единственный адаптер ОПКЦ)** — принцип неизменен, **контракт адаптера расширяется** новыми методами (согласие, списание по согласию). Binds-контракт: `docs/contracts/opkc-adapter.md` (уже существует) — не новый файл.
- **AD-005 (зачисление из PAID)** — НЕ меняется: списание по согласию всё равно проходит через подтверждённый статус НСПК перед зачислением.
- **AD-007 (НПС/КИИ/ПДн)** — принцип неизменен, **новый чувствительный контекст**: согласие несёт ПДн плательщика (идентификатор плательщика) — усиливает требования минимизации/шифрования. Не меняет Rule, расширяет scope.
- **AD-001, AD-006, AD-008** — НЕ меняются.

And NEW: **AD-009** — списание только по действующему согласию.

Good. This is a precise impact analysis.

Now, let me think about the **alternatives** for the core ADR-008 decision.

Core decision: **How to model the consent and where its source of truth lives.**

Option 1 (recommended): **Consent as a first-class entity in the gateway** (own table, own state machine, own idempotency), debits reuse the payment state machine. Rationale: consistent with AD-002 (single source of truth in gateway), local control of limits/revocation, auditability, and it keeps the "single gateway" model. The gateway is the source of truth for "is this consent active and within limits", while НСПК/Банк плательщика is the authority on whether the payer confirmed/revoked (the gateway receives consent status events from НСПК).

Option 2: **Gateway as thin passthrough** — consent lives only in НСПК/Банк плательщика; gateway forwards debit requests, НСПК enforces consent. Minus: gateway loses local source of truth → can't enforce limits/idempotency independently, hard to reconcile, hard to integrate with АБС/антифрод, and violates the spirit of AD-002 (gateway as source of truth). Plus: less scope.

Option 3: **Consent stored in АБС or a separate "consent service" outside the gateway** — reuse existing infra. Minus: splits source of truth across systems, adds a second component + reconciliation burden, and АБС has no "consent" concept (like it has no "СБП платёж" concept per ADR-005). Plus: reuse.

I'll recommend Option 1.

Second decision (sub-decision): **How the consent is confirmed** — the payer confirms in their bank app (Банк плательщика), so the acquirer gateway initiates a consent registration with НСПК, which routes to the payer's bank, and the payer approves. This is dictated by НСПК protocol [ТРЕБУЕТ ПРОВЕРКИ]. So consent confirmation is asynchronous: gateway creates consent (PENDING) → НСПК routes to payer bank → payer approves/declines → НСПК notifies gateway → consent becomes ACTIVE/REJECTED. This is a design constraint, not really an alternative.

Third sub-decision: **Debit initiation** — the ТСП calls the gateway with consentId + amount; gateway validates consent (ACTIVE, within limits), creates a debit (reuses payment state machine, no QR), forwards to НСПК for execution under the consent, receives confirmation, credits АБС. This reuses the existing flow minus QR.

Fourth sub-decision (worth flagging as human decision): **Chargeback/dispute handling for recurring debits** — currently disputes are "Deferred". Recurring debits have a higher dispute rate (payer claims unauthorized). This needs a decision on dispute handling — I'll flag it as a human decision / deferred with return condition.

Also worth flagging as human decision: **limits model** (max amount per debit, monthly cap, frequency) — business decides the default limits and who sets them (TSP or bank).

Also: **whether to support "pause" (приостановка) vs only cancel** — product decision.

Also: **Payer identification data** — what minimal payer data is needed (masked phone/account), ПДн impact — ИБ/legal decision.

OK, I have enough to write. Let me also think about the **NFRs** for subscriptions:

- Consent creation latency (p95), consent status propagation, debit success rate.
- Consent registry availability.
- Debit throughput (recurring debits are batchy — e.g., monthly billing spikes for telecom/ЖКХ).
- Idempotency: 0 double debits.
- Reconciliation: consent status sync with НСПК (e.g., hourly), debit reconciliation.
- Compliance: 100% of debits have an ACTIVE consent at initiation; revocation → new debit blocked within X seconds.
- Audit: consent lifecycle fully audited.
- Security: consent data (payer PII) encrypted at rest, masked in logs.

Let me think about concrete measurable targets consistent with existing NFR style:
- Регистрация согласия: p95 < 500 мс (аналогично регистрации QR).
- Синхронизация статуса согласия от НСПК: p95 < 5 с (аналогично нотификации).
- Инициация списания: p95 < 500 мс (без учёта НСПК).
- Отзыв согласия → блокировка новых списаний: ≤ 30 с (эффективная отзывность).
- Двойных списаний по одному согласию за один период: 0.
- Список незавершённых/отклонённых списаний: полный, актуальный (сверка ежечасная).
- 100% списаний — с действующим согласием на момент инициации (fitness-тест).
- Throughput пик: 500 TPS (учитывая батчевые списания в дни биллинга).

Now let me write the documents. This is a substantial amount of writing. Let me be thorough but precise, matching the repo's style (Russian, structured markdown, tables, mermaid where useful).

Let me plan the actual files and their content, then write them.

Files to create:
1. `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-podpiski-sbp.md`
2. `docs/solutioning-subscriptions.md` (significance/route + impact + acceptance criteria + rollback + human decisions)
3. `docs/spec/consent-machine.md` (consent state machine + debit flow)

Files to modify:
4. `ARCHITECTURE-SPINE.md` — add AD-009; update Deferred (remove "автоплатежи" note if present — actually "автоплатежи" is in solutioning.md §1 roadmap, not in spine Deferred. The spine Deferred has C2C/выплаты and диспуты. So I add AD-009 and maybe note the change in a changelog-like way. Actually, I should also update the parenthetical "roadmap" reference. Let me check: solutioning.md §1 says "Roadmap (вне scope): C2C, выплаты B2C/B2B, диспуты, автоплатежи." I should update solutioning.md to remove "автоплатежи" from out-of-scope, OR note it's now in scope. But the user said change accepted files only in the accepted way. solutioning.md is the accepted design. Should I modify it or create a new solutioning doc?

The cleanest: create `docs/solutioning-subscriptions.md` as a NEW doc (the "architectural package for the change"), and NOT modify solutioning.md's body, but I should update README.md to list the new doc. However, the "автоплатежи" is listed as "вне scope" in solutioning.md §1 — leaving it would be contradictory. I think a minimal, correct approach is to leave solutioning.md as the accepted baseline (historical), and in the new solutioning-subscriptions.md explicitly note "this brings 'автоплатежи' from the roadmap into scope" — this is cleaner than editing the accepted doc, and respects "change accepted files only in the accepted way" (new ADR + new spine block + new docs). 

Actually, the accepted way to change scope in this repo IS: new ADR + new spine invariant + new solutioning doc + README update. Editing the old solutioning.md's roadmap line is a minor consistency fix; I could do a small edit to that one line to avoid contradiction. But to be safe and minimal, I'll update README (structure + status) and add the new docs, and add a one-line note in solutioning.md's roadmap section? Let me think.

Actually the user said: "Принятые файлы решения меняй только тем способом, который принят в этом репозитории." — This means: when I DO change accepted files, use the accepted method (new ADR, new spine block, version bump, etc.), not that I can't touch them. The accepted method for evolving scope = new ADR (ADR-008) + new spine block (AD-009) + new/updated solutioning. So:

- I'll create ADR-008 (the decision).
- Add AD-009 to spine.
- Create solutioning-subscriptions.md (new, the package).
- Create consent-machine.md (spec).
- Extend nfr.md (append subscription NFR section).
- Extend tsp-api.md + openapi/tsp-api.yaml (contract).
- Extend opkc-adapter.md (internal contract for vendor).
- Update README.md (structure/status).

I'll avoid editing solutioning.md body to keep the accepted baseline intact; instead the new solutioning-subscriptions.md explicitly supersedes/extends the "автоплатежи" roadmap item. But I should update README which lists "Автоплатежи" implicitly? README says nothing about автоплатежи except "возвраты" and roadmap. Let me check README again: README says "приём C2B-платежей ... возвраты" and "ключевые документы". It doesn't mention автоплатежи explicitly. So README update is: add the new docs to structure, and update status to note the new proposed change.

Hmm wait, actually I realize I should double check: does the spine "Deferred" section need updating? The spine Deferred section lists:
- Мультивалютность
- C2C-переводы и выплаты B2C/B2B
- Диспуты/претензии

"Автоплатежи" is NOT there. It's in solutioning.md §1 roadmap. So no spine Deferred update needed for автоплатежи (it's not there). But I'm adding AD-009 which is a new invariant.

Actually, wait — let me reconsider. The task says "рекуррентные C2B-списания по согласию плательщика — подписки СБП". This IS "автоплатежи" from the roadmap. So I'm pulling it from roadmap into scope. The solutioning.md §1 roadmap line "автоплатежи" should be updated to reflect it's now a proposed change (ADR-008, Proposed). I'll do a minimal targeted edit to that line in solutioning.md, OR just leave it and note in the new doc. 

I think the cleanest and most defensible: leave solutioning.md untouched (it's the accepted baseline snapshot), and in the NEW solutioning-subscriptions.md, explicitly state "Принятая архитектура помечает рекуррентные списания как roadmap-пункт 'автоплатежи' (solutioning.md §1). Настоящий пакет переводит его из roadmap в scope." This avoids touching the accepted doc and is honest.

Actually, on reflection, I'll do BOTH: leave solutioning.md body untouched (to preserve accepted baseline), and clearly cross-reference. The new doc IS the change package. This is the most "accepted way" approach — additive.

Now, should I update `.arch-handoff/`? The handoff package (TASK.md, ARCHITECTURE.md, MANIFEST.json, CONSTRAINTS.yaml, RUBRIC.yaml) is for handing to the CODE harness (walking skeleton implementation). The user says "чтобы его можно было вынести на архитектурное решение и затем передать исполнителям" — the package is to be brought to decision FIRST, THEN handed to implementers. So the .arch-handoff update would happen AFTER the human decision. I think I should NOT update .arch-handoff now (it's for post-decision handoff), but I could note in the package that after A3 decision, the handoff should be regenerated. Actually, to keep scope tight and correct, I'll leave .arch-handoff untouched and note it in the "next steps" of the solutioning doc.

Hmm, but actually the deliverable list item 6 says "Критерии приёмки и план отката" — these are handoff-quality things (RUBRIC.yaml evaluates handoff quality including acceptance criteria and rollback). But those belong in the solutioning-subscriptions.md + ADR, not necessarily in .arch-handoff yet.

OK, let me also reconsider the CALM skill usage. The user said "используй их по назначению" (use them for their intended purpose). The CALM skill is for CALM JSON modeling, which this repo doesn't use. So the "intended purpose" of CALM doesn't apply here — I should NOT force CALM JSON into a BMAD repo. I already loaded the CALM instructions as required by the skill's first-interaction rule. I'll note in my final summary that CALM modeling was not applicable (repo uses BMAD spine/ADR convention, not CALM JSON), so I followed the repo's native convention. Actually, I don't need to belabor this. I'll just proceed with the repo's convention.

Wait — actually, is there any chance the repo DOES want CALM artifacts? Let me check: there are no `.architecture.json` or `.timeline.json` files. The `calm` skill is the only project skill, but it's registered as a generic FINOS CALM skill. The repo is clearly BMAD/OpenSpec. The path "calm-r2" is just the cell/run name (runs/cells/calm-r2), unrelated to CALM the modeling language — it's likely "calm" = the run's codename (calm-r2 = "calm round 2"?). 

I'll proceed with BMAD convention. I've already loaded CALM instructions per the skill, which is fine — I'll note CALM is not the repo's convention and move on. Actually I won't even belabor it in the final answer; I'll just deliver the package in the repo's native convention.

Let me also verify: is there a `calm` CLI available to validate anything? No (`which calm` returned empty). So no validation tooling to run. The repo's "fitness rules" in CONSTRAINTS.yaml use `arch control check` (a BMAD tool, not present here). So I can't run automated checks. I'll note that I can't run the `arch control check` (not installed) but I've followed the fitness rules manually (e.g., no `<!--` placeholders in ADRs, NFR contains '99,95', etc.).

Actually, let me check if there's any validation command I can run. There's node_modules with mermaid, playwright, typescript — suggesting some tooling exists. Let me check package.json.

Let me check if there's a package.json at root. The find earlier didn't show package.json at root (only node_modules). Wait, the find excluded node_modules but didn't show package.json. Let me verify there's no package.json. Actually the find output listed files but I don't see package.json. The node_modules has mermaid, playwright-core, typescript, ts-node, lodash, js-yaml, mkdirp, tree-dump — these are likely dependencies of some BMAD/OpenSpec CLI tool, but the tool itself isn't in the repo (it's probably globally installed or run externally). 

Let me not worry about running validation — there's no clear check command. I'll do a final YAML/JSON sanity check on the files I modify (openapi yaml, CONSTRAINTS if I touch it — I won't touch CONSTRAINTS).

Actually, I realize I should double-check the openapi file is valid YAML and my additions are consistent. And I should make sure the ADR files don't contain `<!--` placeholders (fitness rule "adr-no-placeholders"). And NFR should contain '99,95' (it already does; my additions keep that).

Let me now also verify there's a package.json or any tooling to validate openapi. Let me quickly check.

  `write_file(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-p, content="# ADR-008. Рекуррентные C2B-списания по согласию плательщика (подписки СБП): согласие как first-class сущность шлюза\n\n- Date: 2026-09-28\)`

No package.json at root, git status clean. So no validation tooling to run (no calm CLI, no arch control check, no openapi linter). I'll do manual correctness.

Now I have everything I need. Let me write the architectural package.

Let me carefully plan the content and write the files. I'll write in Russian to match the repo.

Let me now compose each file.

### File 1: `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-podpiski-sbp.md`

Format matching existing ADRs: header block (Date, Status, Owner, Related), then Context, Decision, Alternatives Considered (table), Consequences (Positive/Negative), Reversibility, References.

Content:

- Date: 2026-09-28
- Status: Proposed
- Owner: solution-architect (платёжный контур)
- Related: ADR-002, ADR-003, ADR-004, ADR-005, AD-009 (new), AD-002, AD-003, AD-005

Context:
- ТСП (онлайн-кинотеатры, ЖКХ, связь) требуют рекуррентные C2B-списания по согласию — подписки СБП. Сейчас каждый платёж требует QR и действия клиента.
- В принятой архитектуре это пункт roadmap («автоплатежи», solutioning.md §1).
- НСПК предоставляет механизм подписок/согласий [ТРЕБУЕТ ПРОВЕРКИ — протокол]. Плательщик даёт согласие однократно (в приложении банка плательщика), после чего ТСП инициирует списания без повторного действия клиента.
- Ключевые силы: финансовое влияние (списание без участия клиента = повышенный фрод-риск), регуляторика (161-ФЗ о рекуррентных/постоянных распоряжениях, 152-ФЗ ПДн плательщика, 115-ФЗ AML), необходимость не сломать существующий C2B QR-поток.

Decision:
1. Вводим сущность «Согласие» (consent) как первый класс в шлюзе: собственная таблица, собственная статусная машина, идемпотентность по consentId. Источник истины жизненного цикла согласия — шлюз; авторитет на подтверждение/отзыв плательщиком — НСПК/банк плательщика (шлюз получает статусы событиями, ADR-004-механика).
2. Согласие — конечный автомат: PENDING → ACTIVE → (PAUSED?) → CANCELLED / EXPIRED / REVOKED / DECLINED. Переходы атомарные + outbox + аудит (обобщение AD-002 на согласие).
3. Рекуррентное списание (debit) — платёж по действующему согласию: инициируется ТСП (consentId + сумма), валидируется шлюзом (ACTIVE + лимиты), проходит ту же статусную машину платежа (CREATED → PAID → CREDITED → COMPLETED, без QR_ISSUED), зачисление — только из PAID (AD-005 неизменен).
4. Лимиты согласия — макс. сумма/частота/срок — хранятся в шлюзе и проверяются до инициации; отзыв/истечение немедленно блокирует новые списания (AD-009).
5. Подтверждение согласия — асинхронно через НСПК/банк плательщика: шлюз регистрирует согласие в ОПКЦ (через адаптер), НСПК маршрутизирует плательщику, результат — событием. Точный протокол [ТРЕБУЕТ ПРОВЕРКИ].
6. Адаптер ОПКЦ расширяется методами/событиями согласия и списания (opkc-adapter.md v0.2); ядро остаётся контрактно-независимым (AD-008).

Alternatives table:
| Вариант | Плюсы | Минусы |
| Тонкий passthrough: согласие только в НСПК/банке плательщика, шлюз форвардит | Минимум scope | Нет локального источника истины → нельзя независимо проверять лимиты/идемпотентность, сложнее сверка/AML, противоречит AD-002 |
| Хранить согласие в АБС/отдельном сервисе вне шлюза | Переиспользование | Второй источник истины + сверка; АБС не имеет понятия «согласие» (как и «платёж СБП», ADR-005) |
| Согласие в шлюзе как первый класс (выбран) | Единый источник истины, локальные лимиты/отзыв, аудируемость, согласованность с AD-002 | Новый объект и таблица, расширение статусной модели |

Consequences:
Positive:
- Контроль фрод-риска: лимиты и отзыв проверяются локально, до обращения к НСПК.
- Переиспользование платформы: статусная машина платежа, outbox, сверка, адаптеры — без изменений ядра.
- Аудируемость: полный жизненный цикл согласия и каждого списания.
- Отделение от QR-потока: существующие потребители не затронуты.
Negative:
- Новый объект и статусная машина — рост сложности и тестов (fitness на каждый переход).
- ПДн плательщика (идентификатор) — расширение compliance-поверхности (152-ФЗ, шифрование, маскирование).
- Зависимость от протокола НСПК по согласиям [ТРЕБУЕТ ПРОВЕРКИ] — gap до получения документации.
- Диспуты/chargeback по рекуррентным списаниям (чаще, чем по QR) — остаются Deferred (риск).
Reversibility: **reversible** — сущность согласия добавляется аддитивно; отказ от фичи = отключение feature-флагом без влияния на QR-поток; данные согласий изолированы. Необратимой миграции нет.

References:
- AD-009 (spine) — списание только по действующему согласию
- AD-002, AD-003, AD-005 (spine) — расширение/неизменность
- ADR-002 (статусная машина), ADR-003/ADR-004 (адаптер/нотификации), ADR-005 (зачисление)
- docs/solutioning-subscriptions.md, docs/spec/consent-machine.md
- НСПК: механизм СБП-подписок [ТРЕБУЕТ ПРОВЕРКИ]

### File 2: `docs/solutioning-subscriptions.md`

Structure:
- Title
- 1. Оценка значимости и маршрут (significance/route)
- 2. Влияние на принятую архитектуру (impact: invariants table)
- 3. Доменная модель и потоки (consent + debit, mermaid)
- 4. Разбиение на решения (ADR-008, spine AD-009)
- 5. NFR (pointer to nfr.md)
- 6. Гейты/критерии приёмки
- 7. План отката
- 8. Gaps и внешние входы
- 9. Открытые вопросы / решения человека-архитектора

### File 3: `docs/spec/consent-machine.md`

Consent state machine spec + debit flow, analogous to state-machine.md.

### File 4: `ARCHITECTURE-SPINE.md` — add AD-009 block. I'll insert after AD-008, before "Deferred".

### File 5: `openapi/tsp-api.yaml` — add consent + debit endpoints (backwards compatible).

### File 6: `docs/contracts/tsp-api.md` — add new methods section.

### File 7: `docs/contracts/opkc-adapter.md` — add consent/subscription methods + events + idempotency.

### File 8: `docs/nfr.md` — add subscription NFR section.

### File 9: `README.md` — update structure + status.

This is a lot. Let me write them carefully. I'll be thorough but avoid bloat.

Let me start writing. I'll write the ADR first, then solutioning, then spec, then the edits.

Let me be careful with the spine edit — I need to read the exact text around where AD-008 ends and "Deferred" begins. From my earlier read, the spine ends AD-008 with:

```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll insert AD-009 between AD-008's Rule and the `---` before Deferred.

Now let me write the content. I'll aim for precision and match tone.

Let me write ADR-008 first.

Actually, let me reconsider the significance score. The existing is "Critical (значимость 11/15)". For this change, I'll say "High (значимость 8/15)". Let me justify in the text: it's a new financial capability with fraud/compliance surface, but it's an additive extension of an already-accepted Critical platform, reusing the state machine/outbox/adapter/trust-zones — so no re-solutioning of ADR-001..007, but a full feature-level solutioning (one ADR + one spine invariant + contract extensions + NFR + acceptance/rollback) is warranted.

Let me think about the route name. In BMAD, routes might be: Critical / High / Medium / Low, each mapping to a level of design ceremony (gates A0-A5). I'll present it as: route "High (feature-level)", meaning: no new initiative/spine-parent, but a full ADR + solutioning + NFR + acceptance/rollback, one human decision (A3-analog) before implementation, and the handoff regenerated after that decision.

I think that's defensible and clear.

Now let me also make sure I address deliverable #4 precisely: "Изменения контрактов (`openapi/tsp-api.yaml`) без поломки существующих потребителей."

I'll explicitly state the backward-compatibility strategy:
- Only additive changes: new paths, new optional fields, new enum values for consent status (separate enum), no changes to existing required fields/status enum of Payment.
- Existing /v1/payments and /v1/payments/{paymentId} unchanged.
- PaymentRequest gains optional `paymentType` and `consentId` (optional) — existing clients omit them.
- New paths: /v1/consents (POST), /v1/consents/{consentId} (GET), /v1/consents/{consentId}/revoke (POST), /v1/consents/{consentId}/debits (POST).
- Debits reuse the Payment schema; GET /v1/payments/{paymentId} works for debits too.
- Version stays /v1 (additive, non-breaking). If a future breaking change → /v2.

Good.

Now let me write everything. I'll write files with write_file for new files and edit for modifications.

Let me write the ADR-008 file.

I need to be careful about the debit status flow. In the existing payment state machine, states are CREATED → QR_ISSUED → PAID → CREDITED → COMPLETED + FAILED/EXPIRED/REFUNDED. For a subscription debit, there's no QR. So the debit starts at CREATED (registered in gateway, request to OPKC in process), then directly PAID (confirmed by НСПК) → CREDITED → COMPLETED. The QR_ISSUED state is simply skipped (not applicable). I should document this in the consent-machine spec: the debit reuses the payment FSM with QR_ISSUED unreachable/bypassed; a new "subtype" distinguishes debit from QR payment.

Alternatively, I could add a distinct state or a `paymentType` discriminator. Cleanest: keep the same FSM, add `paymentType` (`qr` | `subscription`) and note that for `subscription`, QR_ISSUED is skipped. This preserves AD-002/AD-005 and the existing status enum (no breaking change).

Now for consent states, I'll define:
- `PENDING` (registered in gateway, awaiting payer confirmation via НСПК/банк плательщика)
- `ACTIVE` (payer confirmed; debits allowed)
- `PAUSED` (optional, TSP/bank paused; debits suspended but resumable) — I'll include as optional product decision, mark as human decision.
- `CANCELLED` (TSP cancelled)
- `EXPIRED` (validity ended)
- `REVOKED` (payer revoked)
- `DECLINED` (payer declined initial consent) — terminal
- `FAILED` (registration failed) — terminal

Transitions table.

Limits: maxAmountPerDebit, maxAmountTotal (or per period), maxFrequency (min interval between debits), validFrom/validTo, schedule (optional). Stored on consent.

Idempotency:
- POST /v1/consents with Idempotency-Key → consentId
- debit by (consentId + merchantDebitId/Idempotency-Key) → paymentId
- consent status events by eventId
- debit confirmation by paymentId

Reconciliation: consent status sync with НСПК (hourly) — reconcile "active consent at НСПК vs gateway"; debit reconciliation reuses payment reconciliation.

Now let me write. I'll write concise but complete docs.

Let me draft the NFR additions (section 7 in nfr.md).

For acceptance criteria (deliverable #6), I'll put concrete checkable criteria in solutioning-subscriptions.md section 6, referencing NFR.

Let me write now. Given the volume, I'll write each file fully.

One more consideration: the fitness rule `adr-no-placeholders` forbids `<!--` in ADR files. I won't use HTML comments. The `nfr-measurable` requires '99,95' in nfr.md (already present). Good.

Also `spine-lints-clean` forbids TODO/TBD/XXX in spine. My AD-009 block must not contain those. I'll avoid.

Let me write the ADR now.

Actually, let me reconsider whether to create a separate `docs/solutioning-subscriptions.md` or fold into solutioning.md. The user asked for "архитектурный пакет этого изменения". A separate doc `docs/solutioning-subscriptions.md` is cleanest and additive. I'll do that, and it will contain items 1, 2, 6, 7, and reference 3 (ADR), 4 (contracts), 5 (NFR). This makes the package self-contained and navigable.

Let me write.

For the impact table (deliverable #2), I'll enumerate AD-001..AD-008 + new AD-009 with status: не затронут / расширен / новый, and what changes.

Let me write everything now.

Let me start with the spine edit (AD-009), then ADR-008, then solutioning, then consent-machine spec, then contracts (tsp-api.md, opkc-adapter.md, openapi yaml), then nfr.md, then README.

Actually, order doesn't matter much since they're independent files. I'll write new files first (write_file), then do edits.

Let me write ADR-008 first.

I want to make the ADR-008 filename follow the existing convention (kebab-case Russian, descriptive). Existing: `ADR-005-integraciya-s-abs-zachislenie-po-podtverzhdyonnomu-statusu-vozvraty-kak-saga.md`. So mine: `ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-podpiski-sbp.md`.

Let me write.

Now, about the "что остаётся на решение человека-архитектора" (deliverable #7). Key human decisions:
1. **A3-решение по ADR-008** (утвердить выбранную модель «согласие как первый класс») — как и ADR-007, это человеческое решение до реализации.
2. **Модель лимитов** (кто задаёт: банк/ТСП/плательщик, дефолты, верхние границы) — бизнес-продукт.
3. **Поддержка «паузы» (PAUSED)** vs только отмена/отзыв — продукт.
4. **Диспуты/chargeback по рекуррентным списаниям** — остаются Deferred; решение человека-архитектора о сроках возврата (риск фрода выше).
5. **Минимальный состав данных плательщика для согласия** (идентификатор — маскированный телефон/номер счёта) — совместно ИБ/юристы (152-ФЗ).
6. **Требования НСПК к согласиям** [ТРЕБУЕТ ПРОВЕРКИ] — внешний вход, до получения которого контракт не реализуется.

I'll list these clearly.

Why these remain for human: (1) — финансово-значимая стратегия требует A3-ранга; (2)-(3) — продуктовые решения вне компетенции архитектора; (4) — влияет на scope и сроки, стратегическое; (5)-(6) — правовые/внешние входы, требуют владельцев.

OK, writing now.

Let me carefully write the content. I'll produce full documents.

For the openapi yaml, I need to add schemas and paths. Let me design the additions:

New paths:
- POST /v1/consents (createConsent) — Idempotency-Key header, body ConsentRequest, 201 Consent
- GET /v1/consents/{consentId} (getConsent) — 200 Consent
- POST /v1/consents/{consentId}/revoke (revokeConsent) — 200 Consent (or 202)
- POST /v1/consents/{consentId}/debits (createDebit) — Idempotency-Key header, body DebitRequest, 201 Payment (reuses Payment schema)

New schemas:
- ConsentRequest: required [tspId, payerId, limits]. properties: tspId, payerId (masked), amountLimitPerDebit, amountLimitTotal?, maxFrequency?, validFrom?, validTo, purpose?, merchantSubscriptionId (сквозной для ТСП).
- Consent: consentId, tspId, status (enum CONSENT_PENDING|ACTIVE|PAUSED|CANCELLED|EXPIRED|REVOKED|DECLINED|FAILED), limits, validFrom/validTo, createdAt, ...
- DebitRequest: required [amount, merchantOrderId]. properties: amount, merchantOrderId, purpose?, subscriptionId? (опц, сквозной).
- PaymentRequest: add optional `paymentType` (enum qr|subscription, default qr) and `consentId` (optional).

Wait — but the existing `PaymentRequest` has `required: [amount, merchantOrderId]`. If I add `paymentType` and `consentId` as optional, existing consumers are unaffected. Good.

Also add `paymentType` to Payment response as optional, and possibly `consentId` optional.

For the status enum of Consent, I use a separate enum. Prefix consent states to avoid confusion: I'll use `PENDING`, `ACTIVE`, `PAUSED`, `CANCELLED`, `EXPIRED`, `REVOKED`, `DECLINED`, `FAILED`. But `FAILED` and `EXPIRED` overlap with payment status enum names — that's fine since they're separate schemas. But to be safe and clear in API, I might prefix. The existing payment enum uses plain CREATED/PAID/etc. I'll keep consent enum plain but document it's consent status. Actually to reduce ambiguity in the API I'll keep them plain but the schema name is `ConsentStatus`. Fine.

Now let me write the actual YAML. I'll append to the existing paths and components.

Let me write the files now. This is going to be long. Let me produce them.

I'll write the ADR, solutioning, and consent-machine as new files, then edit spine, openapi, tsp-api.md, opkc-adapter.md, nfr.md, README.md.

Let me write file by file.

I need to be mindful of total output length but this is a substantial architecture task; thoroughness is appropriate. I'll keep each doc focused.

Let me write ADR-008.
I have a full picture of the repository's conventions now. Let me summarize my approach before writing: the repo uses a BMAD/OpenSpec convention (spine invariants `AD-*`, `docs/adr/ADR-*`, `docs/solutioning.md`, `docs/nfr.md`, contracts, spec, handoff package) — **not** CALM JSON (no `.architecture.json`/`.timeline.json` present, and `calm` CLI is not installed), so I'll follow the repo's native convention and produce an additive change package.

I'll now create the architectural package: a new ADR, a feature-level solutioning doc (significance/route, impact, acceptance/rollback, human decisions), a consent state-machine spec, and backwards-compatible extensions to the spine, contracts, NFR, and README.

  `write_file(content="# Solutioning — Рекуррентные C2B-списания по согласию (подписки СБП)\n\nНастоящий документ — архитектурный пакет изменения поверх принятого, file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/solutioning-subscriptions.md")`

Now write the solutioning-subscriptions.md.

  `write_file(content="# Статусная машина согласия (consent) — спецификация переходов\n\n- Status: Draft (для ревью на гейте A1 фичи подписок)\n- Owner: solution-, file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/spec/consent-machine.md")`

Now write the consent-machine spec.

  `edit(file_path="<HARNESS>/runs/cells/calm-r2/ws/ARCHITECTURE-SPINE.md", old_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В, new_string="- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). В)`

Now edit ARCHITECTURE-SPINE.md to add AD-009. Let me do the edit, inserting AD-009 after AD-008's Rule and before the `---` / `## Deferred`.

The exact text to match (from the read):

```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll insert AD-009 between the Rule and the `---`.

Let me write the AD-009 block carefully, avoiding TODO/TBD/XXX.

AD-009. Рекуррентное списание только по действующему согласию

- Status: Proposed (ADR-008)
- Binds: сущность «согласие», статусная машина платежа, адаптер ОПКЦ, антифрод/AML.
- Prevents: списания без согласия, списания после отзыва/истечения согласия, превышение лимитов, «подписки-призраки».
- Rule: Рекуррентное списание инициируется только при действующем согласии (`ACTIVE`) в пределах его лимитов (макс. сумма, периодный потолок, мин. интервал, срок). Отзыв/истечение согласия немедленно блокирует новые списания; уже инициированные завершаются по статусной машине платежа. Согласие — first-class сущность шлюза с атомарными переходами и идемпотентностью (обобщение AD-002/AD-003).

Also update the "Контракты и версии" section? The spine has a "Контракты и версии" section at the end listing contract versions. It says:
- Контракт НСПК: docs/contracts/nspk-contract.md ...
- Внутренний контракт шлюза (API ТСП): версия 0.1 draft — docs/contracts/tsp-api.md ...
- Пиннинг версий зависимостей — в CONSTRAINTS.yaml ...

I could add a note about the new contract version v0.2, but it's not strictly necessary. I'll leave the spine's contract-version section as-is to avoid over-editing; the ADR and solutioning already reference v0.2. Actually, to keep consistency, I might update the tsp-api version note. But minimal is better. I'll leave it.

Actually, wait — I should double check the exact current text near the insertion point to make the edit precise. Let me use the edit tool with enough context. I have the full text from the read. Let me construct the old_string precisely.

The read showed the spine ends:

```
- **Rule**: Ядро шлюза проектируется контрактно-независимым от транспорта (внутренний контракт адаптера ОПКЦ — единственная зависимость). Вендор транспорта обязан предоставить сертификаты ФСТЭК/соответствие требованиям НСПК, тестовый контур, SLA. Реализация транспортного слоя начинается только после подписания контракта и получения документации НСПК.

---

## Deferred (с причиной и условием возврата)
```

I'll replace this with the same plus AD-009 inserted.

Let me do the edit.

  `write_file(content="openapi: 3.0.3\ninfo:\n  title: СБП-шлюз — API ТСП\n  version: 0.2.0\npaths:\n  /v1/payments:\n    post:\n      operationId: createPayment\, file_path="<HARNESS>/runs/cells/calm-r2/ws/openapi/tsp-api.yaml")`

Now edit openapi/tsp-api.yaml to add consent + debit endpoints and schemas. Let me rewrite the whole file to include the additions cleanly, since it's small. Actually, I'll use write_file to rewrite the full file with additions (it's small and I know its exact content).

Let me write the new openapi/tsp-api.yaml. I'll keep the existing content and add:
- New paths: /v1/consents (post), /v1/consents/{consentId} (get), /v1/consents/{consentId}/revoke (post), /v1/consents/{consentId}/pause, /v1/consents/{consentId}/resume, /v1/consents/{consentId}/cancel (optional), /v1/consents/{consentId}/debits (post).

Hmm, to keep it focused, I'll add: create consent, get consent, revoke consent, create debit. I'll include pause/resume/cancel as noted-but-optional? The consent-machine spec references pause/resume/cancel endpoints. For consistency I should include them. But to avoid over-expanding, I'll include the core ones (create, get, revoke, debits) and pause/resume/cancel as optional (marked). Actually, let me include pause/resume/cancel too since the spec references them, but keep them minimal. To keep the OpenAPI clean and consistent with the spec, I'll add: createConsent, getConsent, revokeConsent, pauseConsent, resumeConsent, cancelConsent, createDebit.

Actually, that's 7 new operations — a lot. The core minimal set for the feature is createConsent, getConsent, revokeConsent, createDebit. Pause/resume/cancel are flagged as product decisions (PAUSED optional). I'll add the 4 core ones, and note in the tsp-api.md contract that pause/resume/cancel are optional pending product decision. That's cleaner and consistent with "что остаётся на решение человека".

So OpenAPI additions:
- POST /v1/consents
- GET /v1/consents/{consentId}
- POST /v1/consents/{consentId}/revoke
- POST /v1/consents/{consentId}/debits

Schemas:
- ConsentRequest (required: tspId, payerId, limits)
- ConsentLimits (object: amountLimitPerDebit, amountLimitPeriod, amountLimitPeriodWindow, minIntervalSeconds, validFrom, validTo)
- Consent (consentId, tspId, payerId, status, limits, validFrom, validTo, createdAt)
- ConsentStatus enum
- DebitRequest (amount, merchantOrderId, purpose?, merchantDebitId?)
- PaymentRequest: add optional paymentType + consentId
- Payment: add optional paymentType + consentId

Let me write the full YAML.

Note: payerId — masked payer identifier. I'll describe as "маскированный идентификатор плательщика (телефон/номер счёта) — точный формат [ТРЕБУЕТ ПРОВЕРКИ]".

Let me write it.

  `edit(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/contracts/tsp-api.md", old_string="# Контракт API ТСП (мерчант-API) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.1 (нестабильная; до A1 фикс, new_string="# Контракт API ТСП (мерчант-API) — v0.2 draft\n\n- Status: Draft (для ревью на гейте A1)\n- Версия контракта: 0.2 (нестабильная; до A1 фикс)`

Now extend docs/contracts/tsp-api.md. I need to add a new section for consents and subscription debits, and update the version note (v0.1 → v0.2) and versioning/compatibility section.

Let me read the current tsp-api.md again to do precise edits. I already have it. The header says "v0.1 draft". I'll update the header and add new sections. Let me do targeted edits.

Actually, I'll update:
1. Header: "v0.1 draft" → "v0.2 draft", and add a note about additive changes.
2. Add new methods section §4 (after §3.5), renumbering? The existing sections: §1 Общие положения, §2 Идемпотентность, §3 Методы (3.1-3.5), §4 Ошибки, §5 Вебхуки, §6 Версионирование, §7 Открытые вопросы.

I'll insert new subsections 3.6, 3.7, 3.8 (consents + debits) into §3, and add consent webhook events to §5, and add consent error codes to §4, and update §6 versioning note and §7 open questions.

To minimize disruption, I'll do several targeted edits:

Edit 1: header — change "v0.1 draft" to "v0.2 draft", and add a "совместимость" note.

Actually the header block:
```
# Контракт API ТСП (мерчант-API) — v0.1 draft

- Status: Draft (для ревью на гейте A1)
- Версия контракта: 0.1 (нестабильная; до A1 фиксируется v1.0-draft)
```

Change to v0.2, and note additive.

Edit 2: Add §3.6 (Согласие), §3.7 (Списание по согласию) after §3.5.

Edit 3: Add consent webhook events in §5.

Edit 4: Add consent error codes in §4.

Edit 5: §7 open questions — add consent-related ones.

Let me be efficient and do a few edits. Actually, given the number of changes, maybe I should just carefully append/modify with edit tool on specific anchors.

Let me do the edits.

First, the header.

  `edit(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/contracts/tsp-api.md", old_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n, new_string="### 3.5 Статус возврата\n\n`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`\n)`

Now add §3.6 and §3.7 after §3.5. Let me find the anchor. §3.5 is:

```
### 3.5 Статус возврата

`GET /v1/payments/{paymentId}/refunds/{refundId}` → `200 { refundId, paymentId, amount, status, completedAt }`

## 4. Ошибки (RFC 9457, Problem Details)
```

I'll insert new subsections before "## 4. Ошибки".

  `edit(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/contracts/tsp-api.md", old_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), , new_string="Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), )`

Now add consent error codes to §4 and consent webhook events to §5. Let me find the error codes line and webhook events.

Error codes line:
```
Канонические коды: `INVALID_REQUEST` (400), `UNAUTHORIZED` (401), `TSP_NOT_ACTIVE` (403), `NOT_FOUND` (404), `IDEMPOTENCY_CONFLICT` (409), `PAYMENT_NOT_REFUNDABLE` (422), `AMOUNT_EXCEEDS_PAID` (422), `RATE_LIMITED` (429), `INTERNAL` (500). Идемпотентный повтор успешного запроса возвращает ресурс со статусом 200, а не ошибку.
```

I'll add `CONSENT_NOT_ACTIVE` (422), `CONSENT_LIMIT_EXCEEDED` (422) to the list.

Webhook events:
```
События:
- `payment.completed` — платёж зачислен (`status: COMPLETED`)
- `payment.failed` — платёж отклонён/ошибка
- `payment.expired` — истёк TTL
- `refund.completed` / `refund.failed`
```

Add consent events:
- `consent.activated`, `consent.declined`, `consent.revoked`, `consent.expired`, `consent.cancelled`, `consent.failed`

Let me do these edits.

  `edit(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/contracts/tsp-api.md", new_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —, old_string="События:\n- `payment.completed` — платёж зачислен (`status: COMPLETED`)\n- `payment.failed` — платёж отклонён/ошибка\n- `payment.expired` —)`
  `edit(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/contracts/tsp-api.md", new_string="## 7. Открытые вопросы (для A1)\n\n1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — road, old_string="## 7. Открытые вопросы (для A1)\n\n1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — road)`

Now update §7 open questions in tsp-api.md to add consent-related open questions. Let me find the §7 section.

From earlier read, §7 is:
```
## 7. Открытые вопросы (для A1)

1. Необходимость отдельного метода «отмена QR до оплаты» (`POST /v1/payments/{paymentId}/cancel`) — roadmap, ждёт подтверждения от бизнеса.
2. Лимиты сумм и TTL — по документации НСПК [ТРЕБУЕТ ПРОВЕРКИ].
3. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4.
4. Формат `qrImage` (PNG base64) и необходимость — на усмотрение продукта.
```

I'll add items 5-6 about consent.

Actually, let me also update the versioning §6 note? The §6 says "изменения, ломающие контракт, — только в /v2". My additions are non-breaking, staying in /v1. That's already covered. I'll leave §6 as-is but could add a sentence. It's fine.

Let me add consent open questions.

  `edit(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/contracts/opkc-adapter.md", new_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.2 draft\n\n- Status: Draft (для ревью на гейте A1; основа для RFP вендора)\n- Owner:, old_string="# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.1 draft\n\n- Status: Draft (для ревью на гейте A1; основа для RFP вендора)\n- Owner:)`

Now extend docs/contracts/opkc-adapter.md — add consent/subscription methods to §3 (sync ops), §4 (async events), §5 (idempotency), and update header version v0.1 → v0.2.

Let me do targeted edits.

First, header:
```
# Контракт адаптера ОПКЦ (ядро шлюза ↔ транспорт) — v0.1 draft

- Status: Draft (для ревью на гейте A1; основа для RFP вендора)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-003, ADR-004, AD-004, AD-008
```

Change to v0.2, add ADR-008, AD-009.

Then add sync ops to §3 table: registerConsent, getConsentStatus, revokeConsent, initiateDebit, getDebitStatus.

Then add async events to §4: consent.confirmed, consent.declined, consent.revoked, consent.expired (and debit events reuse payment.paid but with consent context — actually the debit reuses payment.paid event; I'll note that).

Then §5 idempotency: reference → consentId/debitId (paymentId).

Let me do these edits.

For §3 table, the current table has rows. I'll add rows after getReconciliationReport row. Let me find the anchor.

The §3 table ends with:
```
| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `timestamp` | 10 c |
```

I'll add consent rows after it.

For §4 events table, ends with:
```
| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |
```

I'll add consent events after it.

Let me do the header edit first.

  `edit(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/contracts/opkc-adapter.md", new_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t, old_string="| `getReconciliationReport` | выписка операций за период (сверка) | `from`, `to`, `type?` | список операций: `qrId`, `status`, `amount`, `t)`
  `edit(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/contracts/opkc-adapter.md", new_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |\n| `consent.confirmed` | , old_string="| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |")`

Now add consent events to §4. Find the anchor:

```
| `transport.unavailable` | техническое: канал к НСПК недоступен/восстановлен | `state` (`DOWN`/`UP`), `detail` |
```

Add consent events after it.

  `edit(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/contracts/opkc-adapter.md", new_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`/`consentId`) в каждый мутирующий вызов.\n- **Адаптер обязан обеспечить иде, old_string="- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.\n- **Адаптер обязан обеспечить идемпотентность)`

Now update §5 idempotency to mention consentId/debit. The §5 currently says:

```
- Ядро передаёт `reference` (свой `paymentId`/`refundId`/`tspId`) в каждый мутирующий вызов.
- **Адаптер обязан обеспечить идемпотентность**: повторный вызов с тем же `reference` возвращает тот же результат и **не создаёт дубль в ОПКЦ**. Если протокол НСПК не даёт идемпотентности «из коробки» — вендор реализует маппинг `reference → операция ОПКЦ` у себя. **Это обязательное требование RFP** (без него ретраи ядра дают двойные QR/возвраты).
- Повторная доставка события с тем же `eventId` — игнорируется ядром (ADR-003).
```

I'll update the first bullet to include `consentId`, and the second bullet's "двойные QR/возвраты" → "двойные QR/возвраты/списания".

Let me edit.

  `edit(file_path="<HARNESS>/runs/cells/calm-r2/ws/docs/nfr.md", new_string="## 7. Рекуррентные списания (подписки СБП)\n\n| Метрика | Цель | Метод проверки |\n|---|---|---|\n| Latency «создание согласия» | p95 < 500, old_string="## Зависимости (внешние входы для NFR)")`

Now extend docs/nfr.md with a §7 for subscriptions. Let me append a new section. The nfr.md ends with "## Зависимости (внешние входы для NFR)" section. I'll insert §7 before the "Зависимости" section, or append after. The existing sections are numbered 1-6, then "Зависимости". I'll add "## 7. Рекуррентные списания (подписки)" before the "Зависимости" section. Actually simpler: insert after §6 (Наблюдаемость) and before "## Зависимости".

Let me find the anchor:
```
## Зависимости (внешние входы для NFR)
```

I'll insert §7 before it.

Content for §7 — measurable NFRs for subscriptions, consistent with existing table style:

## 7. Рекуррентные списания (подписки)

| Метрика | Цель | Метод проверки |
- Регистрация согласия: p95 < 500 мс, p99 < 1 с (без учёта НСПК)
- Инициация списания: p95 < 500 мс (без учёта НСПК)
- Распространение отзыва согласия до блокировки новых списаний: ≤ 30 с
- Синхронизация статуса согласия от события НСПК: p95 < 5 с
- Throughput списаний пик (дни биллинга): 500 TPS, burst 1000 TPS на 1 мин
- Двойных списаний за один период по одному согласию: 0
- Доля списаний без ACTIVE-согласия на момент инициации: 0 (fitness-тест)
- Сверка статусов согласий с НСПК: ежечасная; расхождений по завершённым согласиям — 0
- Полнота аудита жизненного цикла согласия: 100% переходов в неизменяемом логе
- ПДн плательщика: хранение минимизировано, шифрование в покое, маскирование в логах — 100%

Also add a note about consent-specific idempotency and revocation.

Let me write the edit.

  `write_file(content="# Платёжный шлюз СБП (C2B-приём)\n\nПроектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через, file_path="<HARNESS>/runs/cells/calm-r2/ws/README.md")`

Now update README.md to reflect the new docs and status. Let me edit README.

Current README:
```
# Платёжный шлюз СБП (C2B-приём)

Проектирование платёжного шлюза банка к Системе быстрых платежей (СБП): приём C2B-платежей от ТСП через ОПКЦ СБП (АО «НСПК»), зачисление на счета ТСП в АБС, возвраты.

- Маршрут: **Critical** (значимость 11/15).
- Ключевые документы: `docs/solutioning.md`, `docs/nfr.md`, `docs/adr/ADR-001..007`, `ARCHITECTURE-SPINE.md`.
- Статус: решение подготовлено, **ожидает человеческого решения A3** по стратегии реализации (ADR-007) и получения документации НСПК (протокол участника — внешний вход, помечен `[ТРЕБУЕТ ПРОВЕРКИ]`).

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
- Add a line about the proposed change (подписки) status.
- Update structure listing to include the new files.
- Update spine "инварианты AD-001..AD-008" → "AD-001..AD-009".
- Update contracts version "v0.1" → "v0.2".
- Update ADR "ADR-001..007" → "ADR-001..008".

Let me do a full rewrite of README via write_file (it's small). Actually edit is cleaner. Let me do targeted edits.

I'll rewrite the README fully to be safe and clear.

  `run_shell_command(command="cd <HARNESS>/runs/cells/calm-r2/ws && python3 -c \"import yaml,sys; d=yaml.sa, description="Validate YAML and run fitness-style checks")`

Now let me do a sanity check: verify the openapi YAML is valid (parse with python yaml if available), and verify no `<!--` in ADR files, and verify NFR contains '99,95', and spine has no TODO/TBD/XXX.

Let me run a validation. Python may be available. Let me check the openapi yaml parses, and check the fitness rules manually.

Also, I should verify the `[ТРЕБУЕТ ПРОВЕРКИ]` and `[ADOPTED]` conventions are preserved, and that I didn't break anything.

Let me run checks:
1. Python yaml parse of openapi/tsp-api.yaml.
2. grep for `<!--` in docs/adr/*.md (should be none in my new ADR).
3. grep '99,95' in docs/nfr.md (present).
4. grep for 'TODO|TBD|XXX' in ARCHITECTURE-SPINE.md (should be none).

Let me run these.

  `run_shell_command(command="cd <HARNESS>/runs/cells/calm-r2/ws && git diff --stat && echo \"--- new files, description="Show diff stat and new files")`

All checks pass:
- YAML valid, paths and schemas correct.
- No `<!--` placeholders in ADR.
- NFR contains '99,95' (2 occurrences — the original and it's still there).
- Spine no TODO/TBD/XXX.
- Git status shows the expected modified and new files.

Now let me do a final review of the deliverables against the 7 required items, and make sure everything is coherent.

1. Оценка значимости и маршрута — in `docs/solutioning-subscriptions.md` §1. ✓
2. Влияние на принятую архитектуру — §2 (table). ✓
3. Архитектурное решение с альтернативами/последствиями/обратимостью — `docs/adr/ADR-008-...md`. ✓
4. Изменения контрактов без поломки — `openapi/tsp-api.yaml` + `docs/contracts/tsp-api.md` + `docs/contracts/opkc-adapter.md`. ✓
5. Измеримые NFR — `docs/nfr.md` §7. ✓
6. Критерии приёмки и план отката — `docs/solutioning-subscriptions.md` §6-7. ✓
7. Что остаётся на решение человека-архитектора — `docs/solutioning-subscriptions.md` §9. ✓

Plus supporting: `ARCHITECTURE-SPINE.md` (AD-009), `docs/spec/consent-machine.md`, `README.md`.

Let me verify the ADR file doesn't have issues — it has a "Related" line referencing "AD-009 (новый)" and "AD-002, AD-003, AD-005" which are spine invariants. That's consistent with existing ADRs which reference both ADRs and ADs. Good.

One thing to double check: in the ADR "Related" line I wrote "AD-009 (новый), AD-002, AD-003, AD-005" — mixing AD (spine) and ADR. Existing ADRs do mix (e.g., ADR-005 has "Related: ADR-002, ADR-004, AD-005" where AD-005 is spine). So it's fine, but "AD-009 (новый)" might be slightly odd. Actually it's fine and informative.

Let me also reconsider: should I verify the spine edit didn't leave a duplicate `---` or malformed structure. The edit output showed the AD-009 block inserted correctly between AD-008's Rule and the `---`/Deferred. Good.

Let me also double-check: the original spine had "## AD-008. Стратегия реализации — гибрид [ADOPTED]" with Status "Adopted". My AD-009 has "Status: Proposed (ADR-008)". Consistent with the spine's convention where Proposed blocks are "ратифицируются соответствующим ADR". Good.

Now, one more consideration: the solutioning-subscriptions.md references `docs/spec/consent-machine.md` and the openapi. All consistent.

I think the package is complete and coherent. Let me also verify I haven't left any inconsistency in the tsp-api.md — e.g., the `Consent` example uses `"limits": { "...": "..." }` which is a placeholder-ish. That's fine (it's an example, not an ADR placeholder). Actually the fitness rule "adr-no-placeholders" only applies to `docs/adr/*.md`, not contracts. So fine.

Let me also verify there are no issues with the openapi — the `DebitRequest` doesn't reference consentId (it's in the path). That's fine; the path is `/v1/consents/{consentId}/debits`.

I think everything is in order. Let me also consider whether I should mention the CALM skill in the final response — briefly note that CALM (FINOS) was reviewed but the repo uses BMAD spine/ADR convention, so I followed the repo's native method. And note that no automated validation tool (calm CLI / arch control check) is installed, so I ran manual checks (YAML parse, fitness-rule greps).

Let me write the final summary, concise, listing created and modified files.

Actually, let me quickly re-read the final spine to make sure the AD-009 block is clean and there's no leftover double separator issue. The earlier edit output showed lines 61-75 and it looked clean. Good.

Let me also verify the full git diff is coherent (quick check of the diff stat). Actually I have git status already. I'll do a final quick `git diff --stat` to report.


Готово. Архитектурный пакет изменения «подписки СБП (рекуррентные C2B-списания по согласию плательщика)» подготовлен поверх принятого решения, по нативной конвенции репозитория (spine + ADR + solutioning + NFR + контракты + spec). Код не писал.

## Что получилось по 7 пунктам

1. **Оценка значимости и маршрут** → `docs/solutioning-subscriptions.md` §1: **High (8/15)**, feature-уровень — переиспользует принятую платформу (не новый initiative), но новый финансово-значимый объект и повышенный фрод/комплаенс-риск; нужен полный ADR + инвариант + контракты + NFR, но не пере-солюшнинг ADR-001..007.
2. **Влияние на принятую архитектуру** → §2: таблица по AD-001..AD-009 — что расширяется (AD-002/AD-003/AD-004/AD-007), что не меняется (AD-001/AD-005/AD-006/AD-008), что добавляется (AD-009).
3. **Архитектурное решение** → `docs/adr/ADR-008-…md`: согласие как first-class сущность шлюза, debit переиспользует статусную машину платежа; 3 альтернативы, последствия, обратимость `reversible`.
4. **Контракты без поломки потребителей** → `openapi/tsp-api.yaml` (v0.2, только аддитивно: `/v1/consents`, `/v1/consents/{id}`, `…/revoke`, `…/debits`; `PaymentRequest`/`Payment` получили опциональные `paymentType`/`consentId` — существующие `required` и enum не тронуты) + `docs/contracts/tsp-api.md` v0.2 + `docs/contracts/opkc-adapter.md` v0.2 (методы/события согласия и списания).
5. **Измеримые NFR** → `docs/nfr.md` §7 (латентность, отзывность ≤ 30 с, 0 двойных списаний, 0 списаний без `ACTIVE`, сверка, аудит, ПДн).
6. **Критерии приёмки и план отката** → `docs/solutioning-subscriptions.md` §6–7 (позитивные + негативные сценарии, feature-флаг, `stop-new`, сигналы и владелец решения).
7. **Что остаётся человеку** → §9 (утверждение ADR-008 уровня A3; модель лимитов; `PAUSED`; диспуты по рекурренту; состав ПДн плательщика; документация НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`).

Поддерживающие: `ARCHITECTURE-SPINE.md` (новый инвариант **AD-009**), `docs/spec/consent-machine.md` (статусная машина согласия), `README.md` (структура/статус).

## Созданные файлы
- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-podpiski-sbp.md`
- `docs/solutioning-subscriptions.md`
- `docs/spec/consent-machine.md`

## Изменённые файлы
- `ARCHITECTURE-SPINE.md`
- `openapi/tsp-api.yaml`
- `docs/contracts/tsp-api.md`
- `docs/contracts/opkc-adapter.md`
- `docs/nfr.md`
- `README.md`

## Проверка
- `openapi/tsp-api.yaml` валиден (YAML-парсер прошёл, paths/schemas корректны).
- Fitness-правила из `CONSTRAINTS.yaml` проверены вручную: в `docs/adr/*.md` нет `<!--`-плейсхолдеров, `docs/nfr.md` содержит `99,95`, в spine нет `TODO/TBD/XXX`.

Замечание: установленный навык `calm` — это FINOS CALM (JSON-моделирование), а репозиторий использует BMAD/OpenSpec-конвенцию (spine/ADR/markdown), и `.architecture.json`/`.timeline.json` в проекте отсутствуют; `calm` CLI не установлен. Поэтому пакет оформлен в нативной конвенции репозитория, а не в CALM JSON.
