> Отредактировано архитектором (не машинная компиляция). Контракты интерфейсов подписок для реализации.

# SPEC — контракты интерфейсов: СБП-подписки

Источники: `openapi/tsp-api.yaml` v0.2, `docs/contracts/tsp-api.md` §7, `docs/adr/ADR-008`, `docs/adr/ADR-009`.

## 1. API ТСП (внешний контракт)

| Метод | Вход | Выход | Ошибки |
|---|---|---|---|
| `POST /v1/mandates` | Заголовок `Idempotency-Key`; тело `MandateRequest` (`tspId`, `periodicity`, `purpose` обязательны; `amountLimit?`, `currency=RUB`, `startAt?`, `endAt?`, `payerReturnUrl?`) | `201` `Mandate` (`status=PENDING_CONSENT`) | `409 IDEMPOTENCY_CONFLICT`, `403 TSP_NOT_ACTIVE` |
| `GET /v1/mandates/{mandateId}` | path `mandateId` | `200` `Mandate` | `404 MANDATE_NOT_FOUND` |
| `GET /v1/mandates/{mandateId}/charges` | path `mandateId`; query `limit?` | `200` `ChargeList` | `404 MANDATE_NOT_FOUND` |
| `POST /v1/mandates/{mandateId}/revoke` | path `mandateId`; `Idempotency-Key`; тело `MandateRevokeRequest?` (`reason?`) | `200` `Mandate` (`status=REVOKED`) | `422 MANDATE_NOT_ACTIVE` (недопустимое состояние) |

Идемпотентность: все `POST` требуют `Idempotency-Key` (24 ч, ADR-002 / контракт §2). Ошибки — RFC 9457 (`application/problem+json`, поле `code` из `ErrorCode`).

## 2. Структуры данных

**Mandate**: `mandateId`, `tspId`, `status` (`MandateStatus`), `periodicity` (`Periodicity`), `amountLimit?`, `currency=RUB`, `startAt?`, `endAt?`, `consentRef?` (ссылка ОПКЦ), `consentAt?`, `lastChargeAt?`, `nextChargeAt?`.

**Charge**: `chargeId`, `mandateId`, `billingPeriod` (напр. `2026-10`), `paymentId?`, `amount`, `status` (`INITIATED|PAID|CREDITED|COMPLETED|FAILED|SKIPPED|UNKNOWN`), `scheduledAt`.

**Payment (расширение)**: добавляются `source` (`ONETIME|SUBSCRIPTION`), `mandateId?`, `billingPeriod?`. Существующие поля/перечисления не меняются.

**Periodicity**: `DAILY | WEEKLY | MONTHLY | ON_DEMAND`. **MandateStatus**: `PENDING_CONSENT | ACTIVE | SUSPENDED | REVOKED | EXPIRED | REJECTED`.

## 3. Статусная машина мандата (переходы)

| From | To | Триггер | Guard |
|---|---|---|---|
| — | `PENDING_CONSENT` | `POST /v1/mandates` (новый `mandateId`) | валидный запрос, ТСП активен |
| `PENDING_CONSENT` | `ACTIVE` | событие ОПКЦ о согласии | `eventId` не обработан ранее |
| `PENDING_CONSENT` | `REJECTED` | согласие не дано / ОПКЦ отказал | — |
| `ACTIVE` | `REVOKED` | отзыв плательщиком (ОПКЦ) или ТСП | — |
| `ACTIVE` | `EXPIRED` | `endAt` достигнут | — |
| `ACTIVE` | `SUSPENDED` | пауза (опц., вне первой волны) | — |
| `SUSPENDED` | `ACTIVE` | возобновление (опц.) | — |

Терминальные: `REVOKED`, `EXPIRED`, `REJECTED`. Каждый переход — атомарно с outbox и аудитом (AD-002); повторные события идемпотентны по `eventId` (AD-003).

## 4. Инициация списания (планировщик)

- Выборка: `status=ACTIVE AND nextChargeAt <= now`; `billingPeriod` выводится из `nextChargeAt`.
- Транзакция: `INSERT Charge (mandateId, billingPeriod, ...)` + outbox-событие «инициировать списание». Уникальность `(mandateId, billingPeriod)` — в БД (AD-010).
- Инициация у ОПКЦ через адаптер: `reference = paymentId`; при таймауте — `UNKNOWN`, без повторной отправки; исход разрешается сверкой.
- После успешной инициации `nextChargeAt` сдвигается на следующий период (в той же транзакции).
- Перезапуск планировщика: пересчёт due из БД; окно «догона» — по политике (см. `OPEN-QUESTIONS.md` A3-4).

## 5. Границы ошибок

- Домен подписок не знает протокола НСПК: ошибки адаптера нормализованы (`TRANSPORT_UNAVAILABLE`, `NSPK_REJECTED`, `INVALID_REFERENCE`, `INTERNAL`).
- Отказы бизнес-логики: `MANDATE_NOT_ACTIVE`, `MANDATE_LIMIT_EXCEEDED`, `PERIOD_ALREADY_CHARGED`, `CONSENT_PENDING`, `CONSENT_REVOKED`.
- Неопределённость (`UNKNOWN`) — не ошибка клиенту, а состояние, разрешаемое сверкой.

## 6. Критерии верификации (сводка)

- Property-тесты: «без `ACTIVE`-мандата списание не создаётся», «две инициации за период → одно списание», «`UNKNOWN` не повторяется».
- Контрактные тесты: коды/статусы API и события соответствуют `openapi/tsp-api.yaml`; `contract_diff` breaking = 0.
- Тесты гонок: «отзыв ‖ инициация»; «рестарт планировщика ‖ due-мандат».
- Негативные: повторная нотификация, недоступность АБС/ОПКЦ, превышение `amountLimit`.
- NFR: нагрузочный тест «пиковый день», мониторинг лага/backlog (см. `NFR.md`).
