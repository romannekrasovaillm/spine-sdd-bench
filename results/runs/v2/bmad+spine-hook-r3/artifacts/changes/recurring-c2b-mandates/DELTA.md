# Дельта: recurring-c2b-mandates

- Route: Critical (полный Solutioning, `docs/solutioning-recurring-c2b.md`; дельта несёт правки спайна и реестра правил)
- Created: 2026-09-28

## Проблема

ТСП (онлайн-кинотеатры, ЖКХ, связь) просят рекуррентные C2B-списания по согласию плательщика — подписки СБП. Принятое решение требует QR и действия клиента на каждый платёж, что непригодно для подписок. Изменение вводит согласие плательщика (мандат) как отдельный источник истины, планировщик списаний и новый инвариант spine; принятая финансовая семантика (зачисление только из подтверждённого `PAID`, идемпотентность, outbox) переиспользуется.

## ADDED

- Инвариант **AD-009** «Списание только по действующему согласию плательщика (мандату)» в `ARCHITECTURE-SPINE.md`.
- Мандат (согласие) как сущность с собственной статусной машиной — `docs/spec/recurring-mandates.md`.
- Рекуррентное списание: `When мандат в состоянии ACTIVE, the шлюз shall инициировать списание по (mandateId, periodKey) и довести платёж до COMPLETED`.
- Новые эндпоинты API ТСП: `POST /v1/mandates`, `GET /v1/mandates/{mandateId}`, `POST /v1/mandates/{mandateId}/revoke`; поля `mandateId`/`periodKey`/`paymentType` (опц.) — `openapi/tsp-api.yaml` (0.1 → 0.2 аддитивно).
- Методы/события адаптера ОПКЦ: `registerMandate`, `getMandateStatus`, `revokeMandate`, `createDebit`; события `mandate.activated/rejected/revoked/expired` — `docs/contracts/opkc-adapter.md`.
- NFR рекуррентного контура — `docs/nfr.md` §7; критерии приёмки (EARS) и риски — `docs/spec/recurring-mandates.md`.
- Решение — `docs/adr/ADR-008-...md`; пакет изменения — `docs/solutioning-recurring-c2b.md`.

## MODIFIED

- `ARCHITECTURE-SPINE.md`, AD-002: правило атомарности «статус + outbox» распространено на мандат (перекрёстная ссылка на AD-009); раздел «Контракты и версии» — API ТСП `0.1 → 0.2`, контракт адаптера расширен.
- `.arch-handoff/CONSTRAINTS.yaml`: добавлены правила `mandate-fsm-present`, `adr-008-present`, `debit-only-active-mandate`, `mandate-period-idempotency`, `recurring-rollback-documented`, `nfr-recurring-measurable`, `ears-acceptance-criteria`.
- `openapi/tsp-api.yaml`, `docs/contracts/tsp-api.md`: версия 0.2 (аддитивно; contract_diff 0.1→0.2: breaking = 0).
- `docs/contracts/opkc-adapter.md`: расширены методы §3, события §4, требования RFP §8.
- `docs/nfr.md`: добавлен §7 (измеримые цели рекуррентного контура).
- `docs/spec/state-machine.md`: переход `T4a CREATED → PAID` для `mandate_debit`; добавлены секции «Проблема», «Критерии приёмки», «Риски».

## REMOVED

- Требования не удаляются. Уточнение: сценарий «рекуррентные C2B-списания» ранее числился в roadmap вне scope (`docs/solutioning.md` §1) — теперь вводится настоящим изменением; удаления действующих требований нет, потребители v0.1 не затронуты.

## Затронутые сущности

AD-001, AD-002, AD-003, AD-004, AD-005, AD-006, AD-007, AD-008, AD-009;
ADR-001, ADR-002, ADR-003, ADR-004, ADR-005, ADR-006, ADR-007, ADR-008.

## План отката

До боевого включения — выключить фиче-флаг `recurring_enabled` (данные не накоплены). После включения — режим «stop-new»: запрет новых мандатов и новых списаний, дренаж инициированных, сохранение обработки отзывов и возвратов; данные мандатов не удаляются. Сигналы и владелец — `docs/solutioning-recurring-c2b.md` §6.2.

## Критерии приёмки

- [ ] гейт репозитория зелёный (fitness, spine_lint, delta_guard — правка спайна покрыта этой дельтой)
- [ ] `openapi/tsp-api.yaml` линт без находок; diff 0.1→0.2 без breaking
- [ ] fitness AD-009: списание при недействующем мандате недостижимо; повтор за период → одно списание
- [ ] отзыв мандата блокирует новые списания (тест)
- [ ] гонка воркеров планировщика → ровно одно списание (тест)
- [ ] решения A3 (лимиты, канал согласия, повторы/уведомления, ПДн, поддержка вендором) приняты человеком до реализации транспортного слоя мандатов
