# Изменения контрактов — `sbp-subscriptions`

- Контракт: `openapi/tsp-api.yaml` (v0.1.0 → **v0.2.0**), прозаическая версия — `docs/contracts/tsp-api.md`
- Связано: `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-soglasie-platelshchika.md`, `changes/sbp-subscriptions/DELTA.md`

## 1. Принцип совместимости

Изменение **чисто аддитивное**: только новые пути, новые схемы, новые опциональные поля и новые типы событий. Ни одно существующее поле, обязательное свойство, значение enum ответа или путь не изменено и не удалено. Существующий потребитель, вызывающий только `/v1/payments`, продолжает получать ответ по неизменной схеме.

## 2. Новые ресурсы (ТСП → шлюз)

| Метод | Путь | Назначение | Идемпотентность |
|---|---|---|---|
| POST | `/v1/consents` | Регистрация согласия плательщика | `Idempotency-Key` обязателен |
| GET | `/v1/consents/{consentId}` | Статус согласия | нативная (GET) |
| DELETE | `/v1/consents/{consentId}` | Отзыв согласия; блокирует будущие списания | `Idempotency-Key` + идемпотентность по ресурсу |
| POST | `/v1/subscriptions` | Создание подписки на базе согласия | `Idempotency-Key` обязателен |
| GET | `/v1/subscriptions/{subscriptionId}` | Статус подписки | нативная (GET) |
| DELETE | `/v1/subscriptions/{subscriptionId}` | Отмена подписки | `Idempotency-Key` + идемпотентность по ресурсу |
| POST | `/v1/subscriptions/{subscriptionId}/pause` | Пауза автодебетов | `Idempotency-Key` обязателен |
| POST | `/v1/subscriptions/{subscriptionId}/resume` | Возобновление | `Idempotency-Key` обязателен |
| GET | `/v1/subscriptions/{subscriptionId}/debits` | Список списаний (paymentId) | нативная (GET) |
| POST | `/v1/subscriptions/{subscriptionId}/debits` | Внеплановое списание в рамках согласия | `Idempotency-Key` обязателен |

## 3. Новые/расширенные схемы

- **`Consent`** (status: `PENDING` → `ACTIVE` → `REVOKED`/`EXPIRED`/`REJECTED`), **`ConsentRequest`** (лимиты, срок).
- **`Subscription`** (status: `ACTIVE`/`PAUSED`/`CANCELLED`/`EXPIRED`), **`SubscriptionRequest`** (период, сумма, первое списание).
- **`Debit`**, **`DebitInitiationRequest`**, **`Problem`** (RFC 9457 для новых ошибок).
- **`Payment`** — добавлены **опциональные** поля `subscriptionId` (nullable) и `initiationType` (`PAYER`/`SCHEDULED`/`MERCHANT`, nullable). Существующие поля `paymentId`, `amount`, `status` и enum статуса — без изменений.

## 4. Новые вебхук-события (проза — `docs/contracts/tsp-api.md` §5)

`consent.activated`, `consent.revoked`, `consent.expired`, `consent.rejected`, `subscription.debit.scheduled`, `subscription.debit.completed`, `subscription.debit.failed`, `subscription.paused`, `subscription.cancelled`.

Совместимость: новые типы событий доставляются на существующий `webhookUrl`. Контракт явно требует, чтобы ТСП игнорировал неизвестные типы событий и обрабатывал их идемпотентно по `X-SBP-Event-Id` (уже действующее требование ADR-004). Альтернатива «отдельный webhook URL для подписок» — решение A3 (см. `IMPACT.md` §5).

## 5. Новые коды ошибок (RFC 9457)

`CONSENT_NOT_FOUND` (404), `CONSENT_NOT_ACTIVE` (422), `CONSENT_LIMIT_EXCEEDED` (422), `CONSENT_REVOKED` (422), `SUBSCRIPTION_NOT_ACTIVE` (422), `SUBSCRIPTION_NOT_FOUND` (404).

## 6. Внутренний контракт адаптера ОПКЦ (`docs/contracts/opkc-adapter.md`)

Расширяется аддитивно новыми операциями/событиями (рекуррентные вызовы к ОПКЦ) — единственная зависимость ядра от транспорта (AD-008). Потребитель один (ядро шлюза), поэтому версия внутреннего контракта поднимается до v0.2-draft; детали протокола НСПК остаются `[ТРЕБУЕТ ПРОВЕРКИ]` до документации. Полный перечень операций приведён в `docs/spec/state-machine.md` §7 и `docs/contracts/tsp-api.md`.

## 7. Доказательство совместимости (машинная проверка)

```
# базовая версия контракта — из git
$ git show HEAD:openapi/tsp-api.yaml > <TMP>.1.0.yaml

openapi_lint(openapi/tsp-api.yaml)
  → openapi: 0 находок (error: 0, warn: 0)  Итог: PASS
contract_diff(old=<TMP>.1.0.yaml, new=openapi/tsp-api.yaml, format=openapi)
  → contract_diff: 7 изменений (breaking: 0, non-breaking: 7)  Итог: PASS
fitness_check(repo)     → Правил: 7, нарушений: 0 (error: 0, warn: 0)  passed=true
delta_guard(repo)       → защищённых изменённых файлов: 0, нарушений 0   passed=true
```

- `openapi_lint`: PASS (0 находок) — включая обязательный `Idempotency-Key` на всех mutating-операциях (OA-003).
- `contract_diff` (CD-001…CD-010): **breaking = 0**, 7 неразрушающих добавлений путей (CD-005). Существующий контракт совместим.
- Подтверждение, что дифф не «спрятал» изменение: `significance_from_diff` с заявленными триггерами → маршрут **Critical** (10/15), `undeclared` пуст; детектор диффа подтверждает `api_contract_change` (`sources.api_contract_change = declared+diff`). Дифф-детектор сам по себе видит только контракт (score 1 → Fast), поэтому заявленная оценка обязательна и записана в дельте.

## 8. Замечание вне scope изменения

`PaymentRequest` в `openapi` требует `amount`, тогда как `docs/contracts/tsp-api.md` допускает отсутствие суммы для `qrType=static`. Это расхождение существует в принятом контракте и **не связано** с рекуррентностью; предлагается вынести отдельной дельтой (не менять в рамках `sbp-subscriptions`, чтобы дифф был узким).
