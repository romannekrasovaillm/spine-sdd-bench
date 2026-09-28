# Walking skeleton — Рекуррентные C2B-списания (подписки СБП)

- Дата: 2026-09-28 · Гейт: A2 (план) → A4 (conformance)
- Связано: `docs/SPEC.md`, `docs/solutioning-subscriptions.md`, `changes/sbp-recurrent-c2b/DELTA.md`

## Цель скелета

Доказать **сквозной путь рекуррентного списания** через реальные границы (API → модуль согласий → планировщик → статусная машина → мок АБС → вебхук) и **негативный путь** (нет/отозвано согласие → списание не создаётся). Не полнота продукта, а доказательство архитектуры.

## Сквозной срез (thin slice)

1. `POST /v1/consents` → `201 {consentId, PENDING_PAYER}` (мок ОПКЦ: `registerConsent`).
2. Мок ОПКЦ публикует `consent.activated` → согласие `ACTIVE` (дедуп по `eventId`).
3. `POST /v1/subscriptions` (consentId) → `ACTIVE`, `nextChargeAt`.
4. Планировщик наступает `scheduledAt` → проверки AD-009 (ACTIVE, лимиты, окно предуведомления) → `Charge=PLANNED`.
5. Мок ОПКЦ: предуведомление → нет возражения → `Charge=INITIATED` → создаётся `Payment` (reference=`chargeId`).
6. Мок ОПКЦ: нотификация `PAID` → мок АБС: идемпотентное зачисление по `paymentId` → `CREDITED` → `COMPLETED` → вебхук `charge.completed`.

## Негативные срезы (обязательны уже в скелете)

- Согласие `PENDING_PAYER` → попытка списания → `payment` не создаётся (`charge.skipped`).
- Согласие `REVOKED` до `scheduledAt` → `charge.skipped`, ожидающие остановлены.
- Повторный запуск планировщика по тому же `chargeId` → без второго `Payment`.
- Повторная инициация в тот же слот `(subscriptionId, scheduledAt)` с новым `Idempotency-Key` → возвращается существующий `Charge`, второго `Payment` нет.
- Сумма > `maxAmountPerCharge` → `422 CONSENT_LIMIT_EXCEEDED`, движения денег нет.
- Немедленное списание (`scheduledAt` в пределах окна предуведомления/в прошлом) → отказано.
- Обращение ТСП к чужому `consent`/`subscription`/`charge` → `403 FORBIDDEN`.

## Технологический стек

По выбору команды с обоснованием в ADR (наследует baseline). Приоритет — доказать архитектуру, а не выбрать стек. Мок ОПКЦ и мок АБС — с идемпотентностью по `reference`/`paymentId`.

## Критерий выхода из скелета

- Позитивный срез проходит сквозь все границы, виден в аудит-логе, вебхук доставлен.
- Все негативные срезы не создают движения денег.
- `arch-be gate --route critical --base bench-baseline` — PASS (авторитетный Critical-профиль; `--route auto` на документационном диффе даёт Fast).
- Только после этого — массовая генерация (expand по SP1–SP8 из `docs/SPEC.md`).

Итог: PASS — walking skeleton определён: сквозной позитивный срез, негативные срезы и критерий выхода заданы; массовая генерация начинается только после его прохождения.
