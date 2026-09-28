# Контракт адаптера ОПКЦ — дополнение для подписок (ядро шлюза ↔ транспорт) — v0.2-draft

- Status: Draft (для ревью на гейте A1; дополняет `docs/contracts/opkc-adapter.md`, не заменяет его)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-008, ADR-010, ADR-011, AD-004, AD-008

Настоящее дополнение расширяет контракт `docs/contracts/opkc-adapter.md` операциями сервиса подписок/автоплатежей СБП. Общие положения, таймауты, модель доверия и идемпотентность по `reference` — из базового контракта. Реализация — вендорская, сертифицированная (ADR-007, ADR-010); точные поля протокола НСПК — `[ТРЕБУЕТ ПРОВЕРКИ]` до получения документации.

## 1. Назначение и границы

- Ядро **не знает** протокола НСПК по подпискам; адаптер нормализует статусы/ошибки и скрывает криптографию.
- Адаптер оперирует сквозными идентификаторами ядра: `consentId`, `periodNumber`, `reference`, `qrId`/`debitId`.
- Мутирующие вызовы идемпотентны по `reference`; для дебета `reference` детерминированно выводится из `consentId + periodNumber` (AD-011).

## 2. Синхронные операции (ядро → адаптер)

| Метод | Смысл | Ключевые поля запроса | Ответ | Таймаут (p99.9) |
|---|---|---|---|---|
| `registerConsent` | регистрация согласия плательщика | `reference` (= `consentId`), получатель, `amountType`, `maxAmount?`, периодичность, `validUntil?` | `jobId`, статус `ACCEPTED` (результат — событием) | 5 c |
| `getConsentStatus` | статус согласия (сверка/опрос) | `consentId` | `ACTIVE` / `PENDING` / `SUSPENDED` / `REVOKED` / `EXPIRED` / `REJECTED` / `UNKNOWN` | 3 c |
| `revokeConsent` | регистрация отзыва согласия | `consentId`, `reason` | `ACCEPTED` / `ALREADY_REVOKED` | 5 c |
| `createDebit` | инициация списания по согласию | `reference` (= `consentId + periodNumber`), `consentId`, `amount`, `currency`, `purpose?` | `debitId`, статус `ACCEPTED` (результат — событием) | 5 c |
| `getDebitStatus` | статус дебета | `consentId`, `periodNumber` | `PAID` / `PENDING` / `REJECTED` / `UNKNOWN`, `paidAt?` | 3 c |
| `getConsentReconciliationReport` | выписка по согласиям за период (сверка) | `from`, `to` | список: `consentId`, статус, `timestamp` | 10 c |

Статусы нормализуются адаптером; ядро не зависит от значений НСПК.

## 3. Асинхронные события (адаптер → ядро)

Обязательные поля — как в базовом контракте: `eventId`, `type`, `timestamp`, `correlationRef`.

| Тип события | Смысл | Ключевые поля |
|---|---|---|
| `consent.registered` | согласие подтверждено | `consentId`, получатель, `amountType`, `maxAmount?`, `validUntil?` |
| `consent.rejected` | согласие отклонено | `consentId`, `reasonCode`, `reasonText` |
| `consent.revoked` | согласие отозвано (со стороны НСПК/банка плательщика) | `consentId`, `revokedAt` |
| `debit.paid` | дебет подтверждён | `consentId`, `periodNumber`, `paymentId` (= reference), `amount`, `paidAt` |
| `debit.rejected` | дебет отклонён | `consentId`, `periodNumber`, `reasonCode`, `reasonText` |

Гарантии: at-least-once (ядро дедуплицирует по `eventId`); поздние/повторные события не меняют завершённое состояние; сверка страхует потери.

## 4. Идемпотентность (обязательное требование RFP)

- Повторный `registerConsent`/`revokeConsent` с тем же `reference` не создаёт дубль согласия/отзыва.
- Повторный `createDebit` с тем же `reference` (`consentId + periodNumber`) возвращает тот же `debitId` и **не создаёт второе списание** в ОПКЦ. Если протокол НСПК не даёт идемпотентности «из коробки» — вендор реализует маппинг `reference → операция НСПК` у себя.
- Проверка — сценарии POC (см. §6) и правило `debit_period_idempotency` в ядре.

## 5. Таймауты, ретраи, circuit breaker

- Таймауты — §2; при превышении ядро считает исход неопределённым (`UNKNOWN`) и перед повтором запрашивает статус по `reference` (ADR-011), а не повторяет слепо.
- Ретраи — в одном слое (внутри адаптера, транзиентные сбои, экспоненциальная задержка + джиттер); circuit breaker — внутри адаптера; при размыкании — `503 TRANSPORT_UNAVAILABLE` + событие `transport.unavailable` (как в базовом контракте).
- Нормализованные ошибки: `TRANSPORT_UNAVAILABLE`, `NSPK_REJECTED`, `CONSENT_NOT_ACTIVE`, `INVALID_REFERENCE`, `INTERNAL`.

## 6. Сценарии POC подписок (дополнение к RFP)

| # | Сценарий | Ожидаемый результат |
|---|---|---|
| S1 | `registerConsent` → подтверждение | `consent.registered` с `consentId`; согласие `ACTIVE` |
| S2 | `createDebit` по активному согласию → `debit.paid` | один дебет, `paymentId` = reference |
| S3 | **Повтор `createDebit` с тем же `reference`** | тот же `debitId`, второго списания нет |
| S4 | `revokeConsent` → попытка `createDebit` | отзыв подтверждён; дебет отклонён `CONSENT_NOT_ACTIVE` |
| S5 | Отзыв со стороны НСПК (`consent.revoked`) | ядро получает событие, останавливает списания |
| S6 | Отказ канала к НСПК | circuit breaker → `transport.unavailable`, восстановление |
| S7 | Нагрузка на границе периода (массовые дебеты) | потерь 0, latency в допусках NFR подписок |
| S8 | Потеря/задержка события | сверка через `getConsentStatus`/`getConsentReconciliationReport` находит расхождение |

## 7. NFR контракта (требования к вендору)

| Метрика | Цель | Метод проверки |
|---|---|---|
| Пропускная способность операций подписок | ≥ 300 TPS в окне границы периода; sustained 20 TPS | Нагрузочный тест на тестовом контуре |
| Latency `createDebit` | p95 < 1 c (без учёта НСПК) | Нагрузочный тест |
| Дубли при повторе `createDebit` | 0 (идемпотентность по `reference`) | Сценарий S3 |
| Потеря событий | 0 (at-least-once) | Тест на отказ |
| Доступность операций подписок | ≥ 99,95 % | SLO-отчёт |
| Обновления по протоколу НСПК | в срок SLA вендора | SLA-отчёт |

## 8. Открытые вопросы

1. Точный протокол НСПК по подпискам (поля, тайминги, ограничения типов списаний) — `[ТРЕБУЕТ ПРОВЕРКИ]`.
2. Обязательность уведомления плательщика перед дебетом и его форма (на стороне НСПК/банка плательщика).
3. Формат выписки согласий для сверки (по аналогии с базовым §9).
4. Поведение ядра при `transport.unavailable` в момент планового дебета (перенос окна vs фиксация пропуска) — политика утверждается на A3.
