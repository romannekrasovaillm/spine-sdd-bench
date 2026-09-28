# Дельта: add-sbp-subscriptions

- Route: **Critical** — дельта фиксирует ИЗМЕНЕНИЕ принятого решения как аудиторский след намерения; полный Solutioning — в `openspec/changes/add-sbp-subscriptions/design.md`. Дельта-спека не заменяет полное проектирование на Critical-маршруте.
- Created: 2026-09-28
- Owner: solution-architect (платёжный контур)
- Change (OpenSpec): `openspec/changes/add-sbp-subscriptions/`
- Связано: ADR-008, ADR-009; baseline — `docs/solutioning.md`, `ARCHITECTURE-SPINE.md` (AD-001…AD-008)

## Проблема

ТСП просят рекуррентные C2B-списания по согласию плательщика (подписки СБП). Нужно добавить домен согласия (мандат) и периодические списания, **не** заводя второй источник истины и не меняя пути зачисления/возвратов baseline. Прямые правки `ARCHITECTURE-SPINE.md` и `.arch-handoff/CONSTRAINTS.yaml` запрещены — изменения вносятся этой дельтой и вливаются при архивации.

## ADDED

Ниже — точные блоки для добавления в `ARCHITECTURE-SPINE.md` (при архивации дельты).

```
## AD-009. Списание подписки — это платёж СБП (единый путь зачисления)

- Status: Proposed (ADR-008)
- Binds: статусная машина платежа, планировщик списаний, АБС-адаптер, нотификатор ТСП.
- Prevents: появление второго источника истины о финансовом статусе списания; зачисление подписки в обход подтверждённого статуса; расхождение сверки между «платежами» и «списаниями».
- Rule: любое списание подписки оформляется как платёж СБП с полями `mandateId` и `billingPeriodKey` и проходит существующий автомат; зачисление — только из `PAID` (наследует AD-005). Fitness: отсутствие таблиц/потоков финансового состояния списания вне статусной машины платежа.

## AD-010. Мандат — единственный источник истины о разрешении списаний

- Status: Proposed (ADR-008, ADR-009)
- Binds: хранилище мандатов, планировщик списаний, API ТСП, адаптер ОПКЦ.
- Prevents: списание без действующего мандата; списание сверх лимита или вне разрешённого периода; хранение разрешения в обход хранилища мандатов.
- Rule: списание инициируется только при мандате в статусе `ACTIVE` и сумме не выше лимита; проверка статуса выполняется в той же транзакции, что и создание списания. Fitness: недостижимость создания списания при неактивном мандате.

## AD-011. Идемпотентность списания по периоду

- Status: Proposed (ADR-008)
- Binds: планировщик списаний, статусная машина платежа, БД шлюза.
- Prevents: двойное списание при повторном срабатывании планировщика и при ретраях; расхождение «одно расписание — N списаний».
- Rule: уникальность пары `(mandateId, billingPeriodKey)`; повторный запуск возвращает существующий платёж-списание. Fitness: тест «планировщик ×2 → эффект ×1».

## AD-012. Немедленный отзыв согласия

- Status: Proposed (ADR-009)
- Binds: хранилище мандатов, планировщик списаний, адаптер ОПКЦ, аудит-лог.
- Prevents: списание после отзыва согласия; необнаруженный отзыв; движение денег без действующего согласия.
- Rule: событие `mandate.revoked` переводит мандат в `REVOKED` и блокирует новые списания в пределах целевого окна (NFR); гонка «отзыв ↔ запуск» разрешается проверкой статуса в транзакции. Fitness: тест гонки + метрика окна отзыва.
```

## MODIFIED

Изменяются только перечисления `Binds` (область действия) существующих инвариантов; смысл `Prevents`/`Rule` не меняется, номера не переиспользуются.

- **AD-001**: в `Binds` добавить «хранилище мандатов», «планировщик списаний» (принцип изоляции контура — без изменений).
- **AD-002**: в `Binds` добавить «состояние мандата»; `Rule` без изменений, распространяется и на переходы мандата (статус + outbox + аудит в одной транзакции).
- **AD-003**: в `Binds` добавить «списание подписки (`mandateId` + `billingPeriodKey`)».
- **AD-007**: в `Binds` добавить «данные согласия плательщика (`payerRef`, `consentRef`)»; в `Rule` добавить: аудит покрывает переходы мандата, хранение данных согласия — минимальное.
- **AD-005, AD-006, AD-008**: без изменений (переиспользуются как есть).

## REMOVED

Нет.

## Предлагаемые fitness-правила (добавить в `.arch-handoff/CONSTRAINTS.yaml` при архивации)

Ссылочные правила (работают уже сейчас, на документах):

```yaml
  - name: spine-has-subscription-invariants
    type: must_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'AD-0(09|10|11|12)\.'
    severity: error
    rationale: 'в спайне зафиксированы инварианты подписок (AD-009..AD-012)'
    covers: [sbp-subscriptions]
  - name: subscriptions-pii-minimization
    type: must_contain
    glob: "docs/contracts/tsp-api.md"
    pattern: 'payerRef'
    severity: warn
    rationale: 'хранение согласия — по минимизации ПДн (AD-007)'
    covers: [sbp-subscriptions]
  - name: ears-acceptance-criteria
    type: must_contain
    glob: "docs/**/*.md"
    pattern: '(?m)^\s*[-*]?\s*\**\s*(When|While|If|Where)\b'
    severity: warn
    rationale: 'критерии приёмки в EARS-форме проверяемы формально (кандидат rules_suggest)'
    fix_hint: 'перенести EARS-критерии приёмки из design.md в docs при архивации'
    covers: [sbp-subscriptions]
```

Поведенческие правила (активировать на этапе кода — после walking skeleton; сейчас без `command_succeeds`, чтобы не исполнять отсутствующие тесты):

```yaml
  - name: subscription-charge-idempotent
    type: command_succeeds
    command: "тест: повторное срабатывание планировщика за период → одно списание"
    severity: error
    covers: [sbp-subscriptions]
    rationale: 'AD-011: не более одного успешного списания на (mandateId, billingPeriodKey)'
  - name: no-charge-without-active-mandate
    type: command_succeeds
    command: "тест: списание невозможно при мандате не в ACTIVE (включая гонку с отзывом)"
    severity: error
    covers: [sbp-subscriptions]
    rationale: 'AD-010, AD-012: запрет списания без действующего согласия'
  - name: subscription-credit-only-from-paid
    type: command_succeeds
    command: "тест: зачисление списания недостижимо из CREATED/QR_ISSUED"
    severity: error
    covers: [sbp-subscriptions]
    rationale: 'AD-005 + AD-009: единый путь зачисления по подтверждённому статусу'
```

## Файлы, изменяемые дельтой

- **Защищённые (через архивацию дельты, не вручную)**: `ARCHITECTURE-SPINE.md`, `.arch-handoff/CONSTRAINTS.yaml`.
- **Аддитивные (в этом изменении)**: `docs/adr/ADR-008-*.md`, `docs/adr/ADR-009-*.md` (новые), `openapi/tsp-api.yaml`, `docs/contracts/tsp-api.md`, `docs/contracts/opkc-adapter.md`, `docs/nfr.md`, `docs/spec/state-machine.md`.
- **Пакет изменения OpenSpec**: `openspec/changes/add-sbp-subscriptions/`.

## План отката

- **Уровень решения (эта дельта)**: откат = не архивировать дельту (спайн не меняется) либо внести обратную дельту, снимающую AD-009…AD-012 и уточнения `Binds`.
- **Уровень функционала**: снять фиче-флаг `sbp_subscriptions_enabled`; новые мандаты/списания не создаются; разовый приём платежей не затронут; незавершённые списания доводятся до терминального состояния. Обратной миграции данных нет (таблицы аддитивны).
- **Сигнал откатa**: двойное/несанкционированное списание, неотработанный отзыв согласия, превышение лага просроченных списаний, нарушение error budget.

## Критерии приёмки

- [ ] `spine_lint` по `ARCHITECTURE-SPINE.md` PASS после вливания (без пустых `Binds/Prevents/Rule`, без новых дублей ID).
- [ ] `delta_guard` PASS: защищённые файлы менялись только через эту дельту.
- [ ] `fitness_check` PASS: добавленные правила не нарушены, состав правил не ослаблен.
- [ ] `adr_registry` находит ADR-008/ADR-009 без новых находок формата (дата/статус/дубли).
- [ ] `contract_diff` (old → new `openapi/tsp-api.yaml`) — без ломающих изменений; `openapi_lint` PASS.
- [ ] `openspec validate add-sbp-subscriptions --strict` PASS.
