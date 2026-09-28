# CHG-001 — Изменения контрактов (без поломки потребителей)

- Дата: 2026-09-28
- Артефакт: `openapi/tsp-api.yaml` (v0.1.0 → **v0.2.0**), отложенно: `docs/contracts/tsp-api.md`, `docs/contracts/opkc-adapter.md`
- Инструменты: `openapi_lint` (обе версии), `contract_diff` (v0.1 → v0.2)

## 1. Принцип

Расширение **строго аддитивное**: существующие пути и схемы не изменяются, новые обязательные поля в существующие запросы не добавляются. Существующие потребители (ТСП, интегрированные на `/v1`) не затрагиваются — новая функциональность доступна только тем, кто вызывает новые пути.

## 2. Доказательство неразрывности

`contract_diff` baseline (`<TMP>.v0.1.yaml`) → новая версия:

```
contract_diff: 5 изменений (breaking: 0, non-breaking: 5)
Итог: PASS
```

- breaking = **0**; non_breaking = 5 (все — добавленные пути, правило CD-005).
- `openapi_lint`: error = 0, warn = 0 (ответы с ошибками — `application/problem+json`, RFC 9457).

## 3. Что добавлено в `openapi/tsp-api.yaml`

Пути:

| Метод | Путь | Смысл | Идемпотентность |
|---|---|---|---|
| POST | `/v1/subscriptions` | Регистрация подписки (мандата) ТСП | `Idempotency-Key` (обязателен) |
| GET | `/v1/subscriptions` | Список подписок ТСП | — |
| GET | `/v1/subscriptions/{subscriptionId}` | Карточка подписки | — |
| POST | `/v1/subscriptions/{subscriptionId}/cancel` | Отмена подписки со стороны ТСП | `Idempotency-Key` (обязателен) |
| GET | `/v1/subscriptions/{subscriptionId}/charges` | Списания по плановым периодам | — |
| GET | `/v1/charges/{chargeId}` | Карточка рекуррентного списания | — |

Схемы: `SubscriptionRequest`, `Subscription` (статусы `CREATED, PENDING_CONSENT, ACTIVE, SUSPENDED, REVOKED, EXPIRED`), `Charge` (статусы `SCHEDULED, INITIATED, PAID, CREDITED, COMPLETED, FAILED, SKIPPED`; поле `paymentId` связывает списание со статусной машиной, `billingPeriod` — ключ идемпотентности), `Problem` (RFC 9457).

Существующие `PaymentRequest`/`Payment` и пути `/v1/payments*` — **без изменений**.

## 4. Отложенные изменения (apply/archive)

В `docs/contracts/tsp-api.md` (нарратив) добавляются:
- раздел «Подписки и мандаты» (жизненный цикл, семантика отмены/отзыва, правила расписания);
- коды ошибок: `MANDATE_NOT_ACTIVE` (422), `SUBSCRIPTION_REVOKED` (422), `SUBSCRIPTION_NOT_CANCELLABLE` (422), `MANDATE_LIMIT_EXCEEDED` (422);
- события вебхуков: `subscription.activated`, `subscription.suspended`, `subscription.revoked`, `subscription.charge.succeeded` (ссылка на `payment.completed`), `subscription.charge.failed`, `subscription.charge.skipped`.

В `docs/contracts/opkc-adapter.md` (основа RFP) добавляются рекуррентные операции/события:
- синхронно: `registerSubscription`, `getSubscriptionStatus`, `cancelSubscription`, `initiateCharge`;
- события: `subscription.activated`, `subscription.revoked`, `charge.paid`, `charge.rejected`, `charge.skipped`;
- требование идемпотентности по `reference` (`subscriptionId`, `chargeId`) — обязательно для вендора;
- нормализация статусов/ошибок остаётся обязанностью адаптера (ядро протокола НСПК не знает).

## 5. Версионирование

- Выбрано **расширение `/v1`** с подъёмом версии контракта `0.1 → 0.2`; новые `/v2` не вводятся, так как изменений, ломающих контракт, нет.
- Deprecation-политика прежняя: ломающие изменения — только в `/v2` с окном поддержки ≥ 6 мес.
- Контракт с НСПК (рекуррентный протокол) — внешний вход `[ТРЕБУЕТ ПРОВЕРКИ]`; до получения документации соответствующие операции адаптера не реализуются.
