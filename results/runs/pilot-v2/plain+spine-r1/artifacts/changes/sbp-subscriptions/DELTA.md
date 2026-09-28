# DELTA — Подписки СБП: рекуррентные C2B-списания по согласию плательщика

- Status: Proposed (ожидает A3 — человеческое решение по ADR-008)
- Дата: 2026-09-28
- Автор: solution-architect (платёжный контур)
- Маршрут: **Critical** (значимость **11** из 15; см. §1)
- Защищённые файлы в этой дельте: **`ARCHITECTURE-SPINE.md`**, **`.arch-handoff/CONSTRAINTS.yaml`**
- Связанные решения: `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`, `docs/adr/ADR-009-obratno-sovmestimoe-rasshirenie-kontraktov-podpisok.md`

Цель дельты: описать **изменение** поверх принятого решения «Платёжный шлюз СБП (C2B-приём)», не переписывая систему целиком. Точка истины обновляется вливанием дельты (propose → apply → archive), а не прямой правкой защищённых файлов.

---

## 1. Оценка значимости и маршрут

Машинный вердикт `significance_score` (11 триггеров → **Critical**):

`new_component` (сервис согласий), `new_datastore` (согласия/ключи дедупликации), `domain_ownership_change` (домен «подписки» внутри шлюза), `cross_domain_integration` (ТСП↔шлюз↔ОПКЦ), `api_contract_change`, `data_contract_change`, `security_boundary_change` (списание без активного действия плательщика), `consistency_model_change` (согласие + дедупликация обязательства), `significant_nfr` (пики биллинга), `financial_impact` (деньги без действия клиента), `criticality_or_exception` (КИИ/платёжный контур).

Не сработали: `new_vendor` (используем существующий транспортный адаптер), `trust_zone_change` (новых trust-зон нет), `rto_rpo_targets` (цели базового решения сохраняются), `irreversible_migration` (миграции нет).

**Почему Critical, а не дельта Fast/Standard:** платёжные операции + движение денег без активного действия клиента + новый security boundary. Дельты недостаточно (навык `delta-spec`, границы применимости). Требуется полный Solutioning, ADR с альтернативами, обязательная человеческая точка **A3** и evidence-гейты.

**План гейтов этой дельты:**
- **A0 (fit):** изменения аддитивны, ядро контрактно-независимо от транспорта — PASS по `architect_review` (fitness/spine_lint зелёные).
- **A1 (Spec):** `docs/spec/mandate-lifecycle.md`, `docs/nfr-sbp-subscriptions.md`, расширенные контракты.
- **A2 (Plan):** walking skeleton «согласие → активация → списание (мок ОПКЦ) → зачисление (мок АБС)» на фейках.
- **A3 (human):** `changes/sbp-subscriptions/A3-PACKAGE.md` — выбор модели инициации + go/no-go.
- **A4 (conformance):** fitness-правила ниже + property-тесты дедупликации/отзыва + `contract_diff` = 0 breaking.
- **A5 (drift):** сверка согласий с ОПКЦ, отчёт «списание после отзыва = 0» через 30 дней.

## 2. Что дельта НЕ трогает

- Существующий разовый приём (QR/ссылка): пути `/v1/payments`, `/v1/payments/{id}`, `/v1/payments/{id}/refunds`, статусы, вебхуки — **без изменений**.
- AD-005 (зачисление только из `PAID`), AD-001/AD-002/AD-003, AD-006, AD-007 — **действуют как есть**; AD-009 их не ослабляет, а продолжает.
- Стратегия реализации AD-008 (`[ADOPTED]`) сохраняется; добавляется лишь требование поддержки операций подписок к вендору.

---

## ADDED

### A1. Spine-инвариант AD-009 «Списание по согласию — только при действующем согласии»

Добавляется в `ARCHITECTURE-SPINE.md` блок:

```
## AD-009. Списание по согласию — только при действующем согласии

- Status: Proposed (ADR-008)
- Binds: сервис согласий (mandate store), статусная машина платежа, адаптер ОПКЦ, нотификатор ТСП, аудит-лог.
- Prevents: списание без действующего согласия плательщика; двойное списание за один период обязательства; списание сверх лимитов согласия; продолжение списаний после отзыва согласия; сокрытие отзыва согласия.
- Rule: Рекуррентное списание инициируется ТОЛЬКО при статусе согласия `ACTIVE`, в пределах лимитов согласия (сумма списания и сумма за период), при выполненном требовании предварительного уведомления плательщика; ключ дедупликации обязательства — (`mandateId`, `billingPeriod`), повтор не создаёт второе списание; после события отзыва согласия новые списания запрещены немедленно. Зачисление — по-прежнему только из `PAID` (AD-005). Fitness: «повтор за период → одно списание», «отзыв → ноль новых списаний», «списание вне лимита отклонено».
```

### A2. Артефакты решения (новые файлы)

- `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-po-soglasiyu-platelshchika.md`
- `docs/adr/ADR-009-obratno-sovmestimoe-rasshirenie-kontraktov-podpisok.md`
- `docs/spec/mandate-lifecycle.md`
- `docs/nfr-sbp-subscriptions.md`
- `changes/sbp-subscriptions/{IMPACT,ACCEPTANCE,A3-PACKAGE,HANDOFF}.md`

### A3. Fitness-правила (`.arch-handoff/CONSTRAINTS.yaml`)

Трассируемость новых инвариантов и артефактов (см. §3 записи ниже).

## MODIFIED

| Источник | Что меняется | Обоснование |
|---|---|---|
| `ARCHITECTURE-SPINE.md` → **AD-004** | В `Binds` добавляется «операции подписок (согласия, рекуррентные списания)»; `Rule` не меняется | Операции согласий идут через тот же единственный адаптер ОПКЦ; расползание протокола НСПК недопустимо |
| `ARCHITECTURE-SPINE.md` → **AD-008** | В `Binds` добавляется «вендорский адаптер обязан поддержать операции подписок»; в `Rule` — уточнение: реализация операций подписок начинается после подтверждения поддержки вендором и получения документации НСПК по подпискам | Сохраняет контрактно-независимость ядра (ADR-007) и не позволяет стартовать транспорт подписок без внешних входов |
| `docs/spec/state-machine.md` | Добавляется ссылка/секция: рекуррентное списание создаёт платёж в существующей машине состояний без стадии `QR_ISSUED`; отказ плательщика → `FAILED` + `errorCode=PAYER_REJECTED` | Единая статусная модель (AD-002), без второго автомата для платежа |
| `openapi/tsp-api.yaml` | v0.1.0 → **v0.2.0**, аддитивно: ресурсы `/v1/mandates...`, опциональные поля `Payment`, новые коды ошибок | Совместимость сохраняется (ADR-009); enum `Payment.status` не меняется |
| `docs/contracts/tsp-api.md` | Добавляется §7 «Согласия и рекуррентные списания» (открытые вопросы → §8) | Прозаическое зеркало контракта |
| `docs/contracts/opkc-adapter.md` | Добавляется §9 «Операции подписок» + требование RFP (открытые вопросы → §10) | Граница ядро↔вендор |
| `docs/rfp/vendor-rfp.md` | G4 и §4 расширяются ссылкой на `opkc-adapter.md` §9; scope вендора — операции подписок | Вендор обязан поддержать согласия/списания (constraint AD-008) |
| `docs/solutioning.md` §1 (Roadmap) | «автоплатежи» переносятся из Roadmap в scope (ссылкой на эту дельту) | Граница scope изменилась по запросу бизнеса |

## REMOVED

- Из **Roadmap (вне scope)** базового решения выводится пункт «автоплатежи/подписки» — он становится предметом этой дельты. Заменяющее решение — ADR-008. План миграции потребителей не требуется (потребителей «автоплатежей» не существовало: функция не была реализована).

---

## 3. Кандидаты fitness-правил (вносятся в `.arch-handoff/CONSTRAINTS.yaml`)

Дистилляция по шаблону «Trigger / Rule / Rationale / Check / Evidence / Reversibility / Owner / Expiry». Взятие правила и severity — решение архитектора; ниже — предлагаемые к внесению.

| name | type | проверка | severity | трассировка |
|---|---|---|---|---|
| `adr-008-present` | file_exists | `docs/adr/ADR-008-...md` | error | REQ→ADR |
| `adr-009-present` | file_exists | `docs/adr/ADR-009-...md` | error | REQ→ADR |
| `mandate-debit-only-active` | must_contain | `ARCHITECTURE-SPINE.md`: `только при статусе согласия` | error | AD-009 |
| `mandate-period-idempotency` | must_contain | `docs/adr/ADR-008*.md`: `billingPeriod` | error | AD-009 |
| `mandate-revocation-stops-debits` | must_contain | `ARCHITECTURE-SPINE.md`: `после события отзыва согласия новые списания запрещены` | error | AD-009 |
| `subscription-nfr-measurable` | must_contain | `docs/nfr-sbp-subscriptions.md`: `99,95` | error | NFR |
| `mandates-endpoint-present` | must_contain | `openapi/tsp-api.yaml`: `/v1/mandates` | error | ADR-009 |
| `delta-acceptance-ears` | must_contain | `changes/**/*.md`: EARS-форма (`When|While|If|Where`) | warn | приёмка |
| `delta-present` | file_exists | `changes/sbp-subscriptions/DELTA.md` | warn | процесс |

## 4. Evidence для гейта A4

- `fitness_check` — PASS по `CONSTRAINTS.yaml` (правила выше).
- `spine_lint` — без находок после добавления AD-009.
- `openapi_lint` — PASS на `openapi/tsp-api.yaml` v0.2.0.
- `contract_diff` (v0.1.0 → v0.2.0) — **0 breaking** (`CD-001..CD-010`).
- Property-тесты на фейках: «повтор за период → одно списание»; «отзыв → ноль новых списаний»; «списание вне лимита отклонено».
- `architect_review` / `gate` — PASS.

## 5. Открытые вопросы, блокирующие apply

1. Выбор модели инициации (ТСП-driven vs планировщик) — **A3** (`A3-PACKAGE.md`).
2. Документация НСПК по подпискам (согласие, lead time, лимиты) — внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`.
3. Поддержка операций согласий вендором транспорта — до старта транспортного слоя (constraint AD-008).
