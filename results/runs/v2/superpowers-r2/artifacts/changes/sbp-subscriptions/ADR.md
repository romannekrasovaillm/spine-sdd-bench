# Решения изменения: sbp-subscriptions (adr_or_pattern)

- Статус всех ADR: **Proposed** (до человеческого решения A3)
- Паттерн: **direct debit по предварительному согласию** — реестр мандатов как единый источник истины авторизации; инициатор периодического списания — ТСП; банк — валидатор авторизации и финансовый исполнитель (не биллинг-движок).

## Решения

| ADR | Решение | Spine | Альтернативы (отвергнуты) |
|---|---|---|---|
| `docs/adr/ADR-008-rekurrentnye-c2b-spisaniya-podpiski-sbp-model-avtorizacii-i-orkestraciya.md` | Мандат — первопородная сущность ядра; списание инициирует ТСП; шлюз проверяет мандат и лимиты | AD-009, AD-011 | `gateway-scheduler` (биллинг в ядре), `vendor-subscription-service` (lock-in), `tsp-held-consent` (нет банковского подтверждения), статус-кво |
| `docs/adr/ADR-009-soglasie-platelschika-na-rekurrentnye-spisaniya-zahvat-dokazatelstvo-otzyv-i-zaschita-pdn.md` | Согласие: подтверждение через банк плательщика, append-only доказательство, немедленный отзыв, минимизация ПДн | AD-009 | изменяемый флаг без доказательства; полные ПДн; асинхронный отзыв; журналы ТСП как доказательство |
| `docs/adr/ADR-010-idempotentnost-i-neopredelyonnyy-ishod-rekurrentnogo-spisaniya-zapret-povtornoy-otpravki-bez-proverki-statusa.md` | Идемпотентность списания по ключу + ключ периода; неопределённый исход — без повторной отправки | AD-010 | только `Idempotency-Key`; слепой ретрай; at-most-once; защита только в адаптере |

## Затронутые принятые решения

- Не меняются: ADR-001, ADR-003 (контракт адаптера расширяется аддитивно), ADR-005, ADR-006, ADR-007 [Accepted].
- Расширяются: ADR-002 (автомат мандата, подсостояние `OPKC_UNKNOWN`), ADR-004 (события подписок).
