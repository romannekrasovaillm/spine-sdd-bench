# DELTA — Подписки СБП (рекуррентные C2B-списания по согласию плательщика)

- Change: `sbp-subscriptions`
- Status: proposed (аудит-след намерения ДО реализации)
- Date: 2026-09-28
- Route: **Critical** (значимость 10/15; см. `proposal.md` §1)
- Решение: `docs/adr/ADR-008-podpiski-sbp-soglasie-na-rekurrentnye-c2b-spisaniya.md`
- Пакет: `proposal.md` (значимость, влияние, NFR, приёмка, откат, решения человека), `HANDOFF.md` (передача исполнителям)
- Защищённые файлы, изменяемые этой дельтой: `ARCHITECTURE-SPINE.md`, `.arch-handoff/CONSTRAINTS.yaml`

Дельта описывает ИЗМЕНЕНИЕ относительно текущей истины (ARCHITECTURE-SPINE.md, docs/, openapi/
на baseline `bench-baseline`), а не систему целиком. Цикл: propose → apply → archive.

## ADDED

- Требование (spine) **AD-009**: списание только против мандата в состоянии `ACTIVE` в пределах лимитов.
  Критерий (EARS): When рекуррентное списание инициируется, the шлюз shall выполнить его только против мандата в состоянии `ACTIVE` и в пределах лимитов; иначе — отказать и не создавать платёж.
- Требование (spine) **AD-010**: изоляция и идемпотентность рекуррентного инициатора.
  Критерий (EARS): When инициатор запускается повторно за тот же `(mandateId, periodKey)`, the шлюз shall не создать второе списание.
- Требование API ТСП: методы `POST /v1/mandates`, `GET /v1/mandates/{mandateId}`, `POST /v1/mandates/{mandateId}/revoke`.
  Критерий (EARS): When ТСП создаёт согласие с валидным запросом, the шлюз shall вернуть `201` с `mandateId` и статусом `PENDING_CONFIRMATION`, идемпотентно по `Idempotency-Key`.
- Требование API ТСП: опциональные поля `Payment.originationType` (`QR` | `MANDATE`), `Payment.mandateId`.
- Требование API ТСП: типы вебхуков `mandate.activated`, `mandate.revoked`, `mandate.expired`, `debit.failed`.
- Требование (контракт ядро↔транспорт): методы `createMandate`, `getMandateStatus`, `revokeMandate`, `createDebitByMandate` и события `mandate.*`, `debit.*` (`docs/contracts/opkc-adapter.md` §10).
- Артефакт: `docs/spec/mandate-state-machine.md` — жизненный цикл мандата (состояния, переходы, лимиты, идемпотентность).
- Артефакт: `docs/adr/ADR-008-...md` — архитектурное решение.
- NFR: `docs/nfr.md` §7 — измеримые цели подписок.
- Fitness-правила (`CONSTRAINTS.yaml`): `subscriptions-adr-present`, `subscriptions-mandate-spec-present`, `mandate-consent-invariant`, `subscriptions-nfr-measurable`.

## MODIFIED

- `ARCHITECTURE-SPINE.md`:
  - добавлены инварианты AD-009, AD-010 (см. ADDED);
  - раздел **Deferred**: пункт про автоплатежи/подписки закрыт — capability переведена в scope (обосновано ADR-008);
  - раздел **Контракты и версии**: API ТСП 0.1 → **0.2.0** (аддитивно в рамках `/v1`); добавлен контракт адаптера §10.
- `docs/spec/state-machine.md`: добавлены переходы T13–T15 (платёж по мандату: `CREATED → PAID | FAILED` без `QR_ISSUED`); существующие переходы T1–T12 не изменены.
- `docs/contracts/tsp-api.md`: версия 0.2; добавлены §3.6–3.9, новые события в §5, §6 (совместимость). Существующие разделы не меняют смысла.
- `docs/contracts/opkc-adapter.md`: добавлен §10 (расширение подписок); §1–§9 без изменений.
- `openapi/tsp-api.yaml`: `info.version` 0.1.0 → 0.2.0; добавлены пути `/v1/mandates*`, схемы `Mandate`/`MandateRequest`/`Problem`, опциональные поля `Payment`. Существующие пути/схемы совместимы.
- `.arch-handoff/CONSTRAINTS.yaml`: добавлены 4 правила (см. ADDED); существующие 7 правил не изменены (анти-ослабление).

## REMOVED

- Нет. Изменение полностью **аддитивное**: ни одно требование, метод, обязательное поле или значение
  перечисления `Payment.status` не удаляется и не меняет смысла. Пункт roadmap «автоплатежи» не удаляется,
  а переводится в scope (см. MODIFIED / Deferred).

## Совместимость и обратимость

- Обратная совместимость API ТСП: потребители 0.1 работают без изменений (см. `docs/contracts/tsp-api.md` §6).
- Обратимость: reversible до боевой эксплуатации (фиче-флаг) → costly после появления действующих мандатов (см. ADR-008, `proposal.md` §6).
- Дрейф: при apply обязательна проверка `arch-be gate --route auto` и `fitness_check`; при archive — влитие дельты в живой спайн.
