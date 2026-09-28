# Handoff к исполнителям: СБП-подписки (дельта к `.arch-handoff/`)

- Status: **Draft — заблокирован до гейта A3′** (ратификация ADR-008 и scope). После A3′ содержимое переносится в `.arch-handoff/` (обновляются `TASK.md`, `ARCHITECTURE.md`, `CONSTRAINTS.yaml`, `MANIFEST.json`, `RUBRIC.yaml`).
- Date: 2026-09-28
- Owner: solution-architect (платёжный контур)
- Основание: `docs/adr/ADR-008-...md`, `IMPACT.md`, `CONTRACT-DIFF.md`, `ARCHITECTURE-SPINE.md` (AD-009/AD-010), `docs/spec/state-machine.md` §7

Назначение: зафиксировать, что именно добавляется к принятому решению и что должно быть передано исполнителям — без изменения базового handoff-пакета до человеческого решения.

## 1. Дельта задачи для кодового харнесса

Дополнить walking skeleton (см. `.arch-handoff/TASK.md`) сквозным сценарием подписки:

1. **Ядро — агрегат «согласие» (mandate)** со статусной машиной `CREATED → PENDING_PAYER → ACTIVE` (+ `SUSPENDED`), терминальные `REVOKED`/`EXPIRED`/`FAILED`; состояние — в БД шлюза, единственный источник истины; переходы атомарны с outbox и аудит-логом (AD-002, `docs/spec/state-machine.md` §7).
2. **API ТСП v0.2** (аддитивно): `POST /v1/mandates`, `GET /v1/mandates/{mandateId}`, `POST /v1/mandates/{mandateId}/revoke`; в `POST /v1/payments` — опциональные `mandateId`, `initiation` (`ONE_OFF|RECURRENT`); вебхуки `mandate.activated`/`revoked`/`expired`/`failed` (ADR-008, `CONTRACT-DIFF.md`).
3. **Guard рекуррентного списания**: платёж с `initiation=RECURRENT` допускается только при согласии `ACTIVE` того же ТСП/валюты/плательщика и в пределах лимитов; проверка — в одной транзакции с переходом платежа (AD-009); иначе платёж уходит в `FAILED`, деньги не двигаются.
4. **Короткий путь списания**: `CREATED → PAID` без `QR_ISSUED`; зачисление — только из `PAID` (AD-005), как для обычного платежа.
5. **Отзыв**: событие НСПК или ТСП-запрос → `REVOKED`; после фиксации новые инициации запрещены; уже `PAID` — доводятся до `CREDITED` (AD-010).
6. **Мок-адаптер ОПКЦ**: добавить `registerMandate`, `getMandateStatus`, `cancelMandate`, `createSubscriptionCharge` и события `mandate.activated`/`revoked`/`expired`/`failed`; реальный протокол НСПК НЕ реализуется (внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`).
7. **Мок-адаптер АБС** переиспользуется без изменений (идемпотентное зачисление по `paymentId`).
8. **Нотификатор ТСП** переиспользуется; добавляются типы событий согласий.

## 2. Границы (что НЕ делать)

- Не менять принятые инварианты AD-001..AD-008 и ADR-001..007; конфликт с ними — остановка и эскалация (см. `.arch-handoff/TASK.md`, контракт результата).
- Не реализовывать протокол сервиса подписок НСПК; не встраивать протокольные детали в ядро (AD-004/AD-008).
- Не добавлять новые компоненты/сервисы и trust-зоны; согласие — агрегат внутри существующего ядра.
- Не ломать существующий TSP-API: только аддитивные изменения (`CONTRACT-DIFF.md` §1).
- Не разрешать зачисление из состояния, отличного от `PAID` (AD-005), и списание из состояния согласия, отличного от `ACTIVE` (AD-009).

## 3. Критерии приёмки

Полный список — `IMPACT.md` §6.1 (AC-1..AC-11), включая негативные сценарии (AC-4..AC-10) и проверку неизменности базового C2B (AC-11). Обязательные тесты: недостижимость списания вне `ACTIVE`; гонка «отзыв ↔ списание»; идемпотентность повторов (`Idempotency-Key`, `eventId`); лимиты согласия; сверка; отказ адаптера/АБС. NFR — `docs/nfr.md` §7.

## 4. План отката (исполнимая часть)

`IMPACT.md` §6.2: фиче-флаг «подписки»; выключение новых согласий/инициаций без остановки базового C2B; доведение `PAID` до зачисления; управляемое сворачивание действующих согласий; критерий успешного отката — 0 новых согласий/списаний, базовый C2B в норме, открытых операций без владельца нет. Владелец решения об откате — дежурный SRE/платёжный мониторинг + архитектор/владелец продукта.

## 5. Fitness-правила для `CONSTRAINTS.yaml` (добавить при передаче)

```yaml
  - name: mandate-charge-only-from-active
    type: must_contain
    glob: "docs/adr/ADR-008-*.md"
    pattern: 'только при согласии в состоянии `ACTIVE`'
    severity: error
  - name: revocation-blocks-future-charges
    type: must_contain
    glob: "ARCHITECTURE-SPINE.md"
    pattern: 'После фиксации `REVOKED` любая новая инициация списания по согласию отклоняется'
    severity: error
  - name: tsp-api-additive-only
    type: must_contain
    glob: "docs/changes/sbp-subscriptions/CONTRACT-DIFF.md"
    pattern: 'Ни одного нового обязательного поля'
    severity: error
  - name: subscriptions-nfr-measurable
    type: must_contain
    glob: "docs/nfr.md"
    pattern: 'Списания из состояния согласия, отличного от `ACTIVE`'
    severity: error
```

## 6. Что меняется в `.arch-handoff/` после A3′

| Файл | Изменение |
|---|---|
| `TASK.md` | добавить дельту §1; в контракт результата — тот же JSON-статус; включить тесты гонки/идемпотентности подписок |
| `ARCHITECTURE.md` | добавить источник `docs/adr/ADR-008-...md` (дистиллят в бюджет 800–1500 токенов) |
| `CONSTRAINTS.yaml` | добавить fitness из §5; пиннинг версий — после выбора стека |
| `MANIFEST.json` | добавить `docs/adr/ADR-008-...md` в `sources`; отразить изменение задачи |
| `RUBRIC.yaml` | критерии приёмки — из `IMPACT.md` §6 (негативные сценарии и откат обязательны) |
