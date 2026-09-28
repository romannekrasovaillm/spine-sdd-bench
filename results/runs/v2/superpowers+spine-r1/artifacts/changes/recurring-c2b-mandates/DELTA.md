# Дельта: recurring-c2b-mandates

- Route: Critical (полный Solutioning: предложение спайна + ADR-008/009 + NFR + human A3 + walking skeleton; дельта — носитель правок защищённых файлов)
- Created: 2026-09-28
- Status: Proposed (ожидает A3; вливание в живую истину — на archive)
- Связано: `docs/adr/ADR-008-…`, `docs/adr/ADR-009-…`, `docs/contracts/tsp-api.md` v0.2, `openapi/tsp-api.yaml` v0.2, `SIGNIFICANCE.md`, `IMPACT.md`, `NFR.md`, `ACCEPTANCE.md`, `OPEN-QUESTIONS.md`

## Проблема

ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика. Сегодня каждый платёж требует динамического QR и действия клиента; автоплатежи вынесены в roadmap принятого решения. Изменение добавляет мандат (согласие) и инициацию списаний без участия клиента, **не создавая** второго денежного пути и второго источника истины (AD-001, AD-002).

## ADDED

- REQ-SUB-1 (EARS): When ТСП регистрирует мандат через `POST /v1/mandates`, the шлюз shall создать мандат в состоянии `PENDING_CONSENT` и инициировать регистрацию согласия в ОПКЦ через адаптер.
- REQ-SUB-2 (EARS): When ОПКЦ подтверждает согласие плательщика, the шлюз shall перевести мандат в `ACTIVE` и опубликовать событие `mandate.activated` (идемпотентно по `eventId`).
- REQ-SUB-3 (EARS): When наступает `billingPeriod` мандата в состоянии `ACTIVE`, the шлюз shall создать ровно одно списание `(mandateId, billingPeriod)` и инициировать его через адаптер ОПКЦ.
- REQ-SUB-4 (EARS): If мандат не в состоянии `ACTIVE`, then the шлюз shall не создавать списание (отказ `MANDATE_NOT_ACTIVE` либо `SKIPPED`).
- REQ-SUB-5 (EARS): When плательщик или ТСП отзывает мандат, the шлюз shall перевести мандат в `REVOKED` так, чтобы следующее списание не было создано, и опубликовать `mandate.revoked`.
- REQ-SUB-6 (EARS): While списание не подтверждено НСПК, the шлюз shall не зачислять средства в АБС (зачисление только из `PAID` — AD-005).
- REQ-SUB-7 (EARS): If исход инициации списания не определён (таймаут ответа), then the шлюз shall зафиксировать `UNKNOWN` и разрешить исход сверкой, не повторяя инициацию вслепую.
- REQ-SUB-8 (EARS): Where у мандата задан `amountLimit`, the шлюз shall не создавать списание на сумму выше лимита (отказ `MANDATE_LIMIT_EXCEEDED`).
- REQ-SUB-9 (EARS): When ТСП запрашивает состояние мандата или список списаний, the шлюз shall вернуть параметры и списания без раскрытия ПДн плательщика сверх согласованного состава.
- REQ-SUB-10 (EARS): When создаётся или меняется мандат/списание, the шлюз shall записать смену статуса, outbox-событие и аудит-запись в одной локальной транзакции (AD-002).

## MODIFIED

- `ARCHITECTURE-SPINE.md` (защищённый файл): добавляются блоки **AD-009**, **AD-010**, **AD-011** (см. ниже); блок AD-005 сохраняется и распространяется на рекуррентные списания.
- `ARCHITECTURE-SPINE.md`, секция Deferred: «автоплатежи/подписки» перестают быть вне scope → переведены в scope изменения (было: roadmap; стало: scope). C2C, выплаты B2C/B2B, диспуты остаются deferred.
- `docs/solutioning.md` §1: из roadmap-перечня исключаются автоплатежи; добавляются ссылки на ADR-008/ADR-009.
- `docs/solutioning.md` §2/§5: в C4-контур добавляются модуль подписок и планировщик; в таблицу решений — ADR-008/ADR-009.
- `docs/nfr.md`: добавляется раздел «Рекуррентные списания» с измеримыми целями (источник — `NFR.md`).
- `docs/spec/state-machine.md`: добавляется статусная машина мандата и связь `Charge` ↔ `Payment` (при archive). Требование сенсора `required_sections`: файл должен нести секции «Проблема», «Критерии приёмки», «Риски» — устраняется при archive.
- `docs/contracts/tsp-api.md`: версия 0.1 → 0.2; добавлен §7 «СБП-подписки» (аддитивно).
- `openapi/tsp-api.yaml`: `info.version` 0.1.0 → 0.2.0; пути `/v1/mandates*`; схемы `Mandate`, `Charge`, `Periodicity`, `MandateStatus`, `Problem`; опциональные поля `Payment` (`source`, `mandateId`, `billingPeriod`).
- `.arch-handoff/CONSTRAINTS.yaml` (защищённый файл): добавляются правила (фрагменты ниже).

## REMOVED

- Ничего не удаляется. Сценарии C2B и контракт v0.1 сохраняются; потребители v0.1 не мигрируют (аддитивность).

## Предлагаемые блоки спайна (вносятся при archive; Rule — дословно)

### AD-009. Согласие — предусловие автодействия
- Binds: модуль подписок, планировщик списаний, статусная машина, адаптер ОПКЦ.
- Prevents: списание без действующего согласия плательщика; создание операции после отзыва согласия.
- Rule: рекуррентное списание создаётся только при мандате в состоянии `ACTIVE` на момент инициации; отзыв согласия останавливает следующее списание. Проверка — property-тест «без `ACTIVE`-мандата списание не создаётся» (шаблон `consent-before-auto-action`).

### AD-010. Идемпотентность периода
- Binds: планировщик списаний, БД шлюза, адаптер ОПКЦ.
- Prevents: второе списание за период (двойное списание средств плательщика) при повторном проходе планировщика, переезде аренды или ретрае.
- Rule: ключ идемпотентности списания — `(mandateId, billingPeriod)`; уникальность обеспечивается БД; повторный триггер возвращает существующее списание. Для неопределённого исхода — `UNKNOWN` без повторной отправки. Проверка — property-тесты (шаблоны `idempotency-key`, `unknown-outcome-no-resend`).

### AD-011. Планировщик не источник истины расписания
- Binds: планировщик списаний, БД шлюза (мандаты).
- Prevents: потерю списаний при сбое/перезапуске планировщика; расхождение расписания и состояния.
- Rule: расписание (`nextChargeAt`, периодичность, `endAt`) хранится в БД шлюза; планировщик пересчитывает due-мандаты из БД и не хранит расписание в памяти или очереди. Проверка — тест «перезапуск планировщика не теряет due-списание и не создаёт дубль».

## Предлагаемые правила CONSTRAINTS.yaml (вносятся при archive после применения шаблонов)

```yaml
  - id: C-101
    name: consent_before_auto_action
    type: command_succeeds
    command: 'python3 -m pytest -q -p no:cacheprovider skeleton/rule_templates/consent-before-auto-action/test_consent_before_auto_action.py'
    timeout_secs: 120
    severity: error
    ad: AD-9
    rationale: 'AD-009: без ACTIVE-мандата списание не создаётся'
    skill: fitness-functions
  - id: C-102
    name: charge_idempotent_per_period
    type: command_succeeds
    command: 'python3 -m pytest -q -p no:cacheprovider skeleton/rule_templates/idempotency-key/test_idempotency_key.py'
    timeout_secs: 120
    severity: error
    ad: AD-10
    rationale: 'AD-010: повторная инициация за период не создаёт второе списание'
    skill: fitness-functions
  - id: C-103
    name: unknown_outcome_no_resend
    type: command_succeeds
    command: 'python3 -m pytest -q -p no:cacheprovider skeleton/rule_templates/unknown-outcome-no-resend/test_unknown_outcome_no_resend.py'
    timeout_secs: 120
    severity: error
    ad: AD-10
    rationale: 'AD-010/AD-003: неопределённый исход разрешается сверкой, а не повтором'
    skill: fitness-functions
```

- Фрагменты сняты штатной командой `arch-be rules template apply <id> --ad AD-N --dry-run` (поэтому ключи и `ad:`) и будут дополнены строкой `verified_by: [C-101]` и т. п. в сущности инварианта.
- Правила `command_succeeds` станут зелёными после применения шаблонов на реализации (этап «код»); на этапе решения они предлагаются и в реестр не вносятся, чтобы гейт отражал реальность.
- Дополнительно (текстовые звенья трассировки, не проверка поведения): `must_contain` `/v1/mandates` в `openapi/tsp-api.yaml`; `must_contain` `PERIOD_ALREADY_CHARGED`; `must_contain` числовых NFR подписок в `docs/nfr.md`.

## План отката

- До включения подписок (фиче-флаг): откат = не включать; механизм планировщика обратим (ADR-009 `reversible`).
- После включения: фиче-флаги `subscriptions.enroll=off` (нет новых мандатов) и `subscriptions.charge=off` (нет новых списаний); уже начатые операции доводятся штатно и видны в сверке; откат релиза — rolling; данные мандатов обратно не мигрируются.
- Сигналы и владелец решения — `ACCEPTANCE.md` §4 (владелец: solution-архитектор + дежурная смена).

## Критерии приёмки

- [ ] Все REQ-SUB-1..10 покрыты проверяемыми критериями (`ACCEPTANCE.md`, EARS) — включая негативные сценарии и критерий отката.
- [ ] Fitness-правила AD-009/AD-010/AD-011 зелёные и «зубатые» (падают на нарушающей реализации).
- [ ] `contract_diff` v0.1 → v0.2: breaking = 0; `openapi_lint` PASS.
- [ ] Негативные сценарии пройдены: повторная нотификация, перезапуск планировщика, отзыв перед списанием, гонка «отзыв ‖ инициация», недоступность АБС/ОПКЦ, неопределённый исход.
- [ ] Спайн пролинтован (`spine_lint`), предложенные AD-009..011 ратифицированы и внесены; дельта валидирована и влита (archive).
