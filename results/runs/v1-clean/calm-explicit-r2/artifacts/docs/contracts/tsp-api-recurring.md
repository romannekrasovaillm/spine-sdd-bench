# Контракт API ТСП: рекуррентные списания по согласию (consent + debit) — аддитивное дополнение v0.2

- Status: Draft (для ревью на гейте A1 рекуррентного инкремента)
- Owner: solution-architect (платёжный контур)
- Связано: ADR-008, ADR-002, ADR-004, ADR-005; AD-003, AD-009
- Дополняет: `docs/contracts/tsp-api.md` (v0.1) и `openapi/tsp-api.yaml` (v0.2.0)

Назначение: **аддитивное** расширение мерчант-API контрактом согласий (consent) и списаний по согласию (debit). Существующие методы `/v1/payments*` и схема `Payment` **не меняются** — существующие потребители не затрагиваются (обратная совместимость).

## 1. Принципы совместимости

- Версия пути прежняя — `/v1`. Ломающих изменений нет: только новые ресурсы и новые опциональные поля.
- Контракт помечен v0.2.0; базовые положения `tsp-api.md` §1–2 (транспорт, копейки, ISO 8601, mTLS + `X-API-Key`, rate limiting, `Idempotency-Key`) действуют без изменений.
- Идемпотентность: `Idempotency-Key` обязателен для `POST` (создание согласия, создание списания); повтор с тем же ключом и телом возвращает тот же ресурс (200/201), с другим телом — `409 IDEMPOTENCY_CONFLICT`.

## 2. Ресурсы

### 2.1 Согласие (Consent)

#### Создание согласия

`POST /v1/consents` (заголовок `Idempotency-Key` обязателен)

Запрос:
```json
{
  "tspId": "tsp_9f3c2a1b",
  "payerRef": "+79991234567",          // идентификатор плательщика (телефон E.164) — ПДн, маскируется при хранении
  "consentType": "subscription",        // subscription | on_demand
  "amountLimitPerDebit": 50000,         // опц., копейки — максимум одного списания
  "amountLimitPerPeriod": 200000,       // опц., копейки — максимум за период
  "period": "month",                    // опц.: day | week | month (для amountLimitPerPeriod)
  "expiresAt": "2027-09-28T00:00:00.000Z", // опц., срок действия
  "merchantConsentRef": "sub-100500"    // опц., сквозной для ТСП
}
```

Ответ `201`:
```json
{
  "consentId": "con_5a1b2c3d",
  "tspId": "tsp_9f3c2a1b",
  "payerRefMasked": "+7999***4567",
  "consentType": "subscription",
  "status": "PENDING_CONFIRMATION",
  "amountLimitPerDebit": 50000,
  "amountLimitPerPeriod": 200000,
  "period": "month",
  "expiresAt": "2027-09-28T00:00:00.000Z",
  "merchantConsentRef": "sub-100500",
  "createdAt": "2026-09-28T12:00:00.000Z"
}
```

Правила: согласие проходит подтверждение плательщиком в его банковском приложении (асинхронно через ОПКЦ); до `ACTIVE` списания запрещены. `payerRef` — ПДн: наружу возвращается только `payerRefMasked`.

#### Статус согласия

`GET /v1/consents/{consentId}` → `200 { consentId, tspId, payerRefMasked, consentType, status, amountLimitPerDebit?, amountLimitPerPeriod?, period?, expiresAt?, activatedAt?, revokedAt? }`

#### Отзыв согласия

`POST /v1/consents/{consentId}/revoke` → `202` с телом согласия в статусе `REVOKED` (либо `200` при уже отозванном — идемпотентно).

Правила: отзыв возможен из `ACTIVE`/`SUSPENDED`; из `REVOKED`/`EXPIRED`/`REJECTED` повторный вызов возвращает текущее состояние без ошибки.

### 2.2 Списание по согласию (Debit)

#### Инициировать списание

`POST /v1/consents/{consentId}/debits` (заголовок `Idempotency-Key` обязателен)

Запрос:
```json
{
  "amount": 49900,               // копейки, int; обязателен
  "purpose": "Подписка, месяц 2026-10",
  "merchantDebitRef": "debit-100500-1" // опц.
}
```

Ответ `201`:
```json
{
  "debitId": "deb_6c7d8e9f",
  "consentId": "con_5a1b2c3d",
  "amount": 49900,
  "status": "SUBMITTED",
  "createdAt": "2026-10-01T00:05:00.000Z"
}
```

Правила (guard, выполняется атомарно с созданием — AD-009):
- согласие в статусе `ACTIVE`;
- `amount` ≤ `amountLimitPerDebit` (если задан);
- сумма успешных списаний текущего периода + `amount` ≤ `amountLimitPerPeriod` (если задан);
- нарушение → `422` `CONSENT_NOT_ACTIVE` / `CONSENT_LIMIT_EXCEEDED` / `CONSENT_EXPIRED` / `CONSENT_REVOKED`.

#### Статус списания

`GET /v1/consents/{consentId}/debits/{debitId}` → `200 { debitId, consentId, amount, status, errorCode?, paidAt?, creditedAt?, completedAt? }`

`Debit.status`: `CREATED, SUBMITTED, PAID, CREDITED, COMPLETED, FAILED, REFUNDED`.

## 3. Ошибки (RFC 9457 — дополнение к `tsp-api.md` §4)

Новые канонические коды: `CONSENT_NOT_FOUND` (404), `DEBIT_NOT_FOUND` (404), `CONSENT_NOT_ACTIVE` (422), `CONSENT_REVOKED` (422), `CONSENT_EXPIRED` (422), `CONSENT_LIMIT_EXCEEDED` (422), `PAYER_NOT_CONFIRMED` (422), `DEBIT_AMOUNT_EXCEEDS_LIMIT` (422). Остальные коды — без изменений.

## 4. Вебхуки (дополнение к `tsp-api.md` §5)

Механика доставки (at-least-once, `X-SBP-Event-Id`, HMAC-подпись `X-SBP-Signature`, ретраи + DLQ) — без изменений.

Новые события:
- `consent.activated` — согласие подтверждено плательщиком (`consentId`, `status: ACTIVE`)
- `consent.rejected` — плательщик отклонил (`consentId`, `reasonCode`)
- `consent.revoked` — отозвано плательщиком или ТСП (`consentId`)
- `consent.expired` — истёк срок (`consentId`)
- `consent.suspended` / `consent.resumed` — пауза/возобновление (опц.)
- `debit.completed` — списание зачислено (`debitId`, `consentId`, `amount`, `status: COMPLETED`)
- `debit.failed` — списание отклонено (`debitId`, `consentId`, `amount`, `errorCode`)
- `debit.refunded` — возврат по списанию завершён (`debitId`, `amount`)

ТСП обязан отвечать идемпотентно по `eventId` (как и для существующих событий).

## 5. Версионирование

- Всё аддитивно в `/v1`; ломающие изменения — только `/v2` с периодом поддержки ≥ 6 мес (как в `tsp-api.md` §6).
- Опциональные поля в запросе/ответе — обратно совместимы.
- Схемы `Payment`/`PaymentRequest` не затронуты.

## 6. Открытые вопросы (для A1 рекуррентного инкремента)

1. Формат и доступность `payerRef` (телефон vs маскированный счёт) — зависит от протокола НСПК `[ТРЕБУЕТ ПРОВЕРКИ]`.
2. Изменение лимитов активного согласия (`PATCH /v1/consents/{id}`) — в scope ли v0.2 или новым согласием.
3. `on_demand` (разовое списание без QR, «one-click») — включить ли в первую волну наряду с `subscription`.
4. Модель подписи запросов ТСП (mTLS + подпись тела) — финализирует ИБ на A4 (общий вопрос `tsp-api.md` §7.3).
5. Политика rate limiting для массового биллинга (пики 1-го числа) — согласовать пороги.
