# Review (verification lens): пакет изменения «СБП-подписки»

- Reviewer: independent verification subagent
- Date: 2026-09-28
- Scope: проверка фактических утверждений пакета изменения против реального содержимого репозитория
- Method: чтение файлов, `git show HEAD:openapi/tsp-api.yaml` (базовая версия до изменения), `grep -F`, разбор YAML через PyYAML

## Итоговый вердикт

Пакет в основном фактически корректен и аддитивность контракта подтверждена машинно, но содержит **три расхождения**, из которых два существенны: нерабочее fitness-правило (правило никогда не пройдёт) и заявленное, но отсутствующее изменение в текстовом контракте.

## По пунктам задания

### 1. Существование путей и точность цитат инвариантов — VERIFIED

- Все 13 проверенных путей существуют (ARCHITECTURE-SPINE.md, docs/adr/ADR-008-…, docs/changes/sbp-subscriptions/{IMPACT,CONTRACT-DIFF,HANDOFF}.md, openapi/tsp-api.yaml, docs/contracts/{tsp-api,opkc-adapter}.md, docs/spec/state-machine.md, docs/nfr.md, docs/solutioning.md, docs/rfp/vendor-rfp.md).
- AD-005 Rule цитируется точно: `ARCHITECTURE-SPINE.md:42` «Вызов АБС на зачисление возможен только из состояния `PAID`…»; совпадает с `docs/adr/ADR-005-…md:16`.
- AD-008 Rule цитируется точно: `ARCHITECTURE-SPINE.md:63` «Ядро шлюза проектируется контрактно-независимым от транспорта…».
- Идентификаторы в spine монотонны и без дублей: AD-001…AD-010 (`ARCHITECTURE-SPINE.md:9..74`).

### 2. Протокол-зависимые факты помечены `[ТРЕБУЕТ ПРОВЕРКИ]` — PARTIAL

- Помечены: `docs/adr/ADR-008-…md:13` (перечень протокольных деталей), `ADR-008:70` (внешний вход), `docs/contracts/tsp-api.md:140,256,259–262`, `docs/contracts/opkc-adapter.md` §9 (пп. 4–5), `docs/nfr.md` §7 (строки «Подтверждение списания НСПК», «Покрытие…», «Хранение…») и раздел «Зависимости».
- **Finding (low):** `docs/adr/ADR-008-…md:13` первую половину фразы подаёт как факт без inline-маркера: «плательщик один раз подтверждает согласие в приложении своего банка, после чего ТСП инициирует списания без участия клиента; согласие можно отозвать». Это протокол-зависимое утверждение (механизм списаний и отзыва); маркер стоит только в следующем предложении. Рекомендация: пометить механизм как `[ТРЕБУЕТ ПРОВЕРКИ — из документации НСПК]` либо явно отнести его к внешнему входу.

### 3. Аддитивность `openapi/tsp-api.yaml` 0.2.0 — VERIFIED

Машинный diff `git show HEAD:openapi/tsp-api.yaml` (0.1.0) против рабочего файла (0.2.0):

- paths added: `/v1/mandates`, `/v1/mandates/{mandateId}`, `/v1/mandates/{mandateId}/revoke`; paths removed: 0.
- schemas added: `Mandate`, `MandateRequest`, `MandateStatus`; schemas removed: 0.
- `PaymentRequest.required` и `Payment.required` не изменились; новых обязательных полей нет; удалённых/переименованных свойств нет; добавлены только `initiation`, `mandateId`.
- `Payment.status` enum не изменился (8 значений); статусы согласия — отдельный `MandateStatus` (`CREATED,PENDING_PAYER,ACTIVE,SUSPENDED,REVOKED,EXPIRED,FAILED`).
- YAML успешно парсится (PyYAML).

### 4. Соответствие CONTRACT-DIFF фактическим контрактам — FINDINGS

- **Finding (high):** `CONTRACT-DIFF.md` §3.3 заявляет: «Расширение ответа `GET /v1/payments/{paymentId}`: Добавлены опциональные `mandateId`, `initiation`». Фактически `docs/contracts/tsp-api.md:97–113` (§3.3) ответа с этими полями **не содержит** (JSON без `mandateId`/`initiation`). В `openapi/tsp-api.yaml` поля есть. Итог: текстовый контракт и дельта расходятся; потребитель, читающий markdown, не увидит расширения. Исправление: добавить `mandateId`/`initiation` в пример ответа §3.3 `tsp-api.md`.
- **Finding (medium):** `CONTRACT-DIFF.md` §4 (таблица дельты `opkc-adapter`) перечисляет только события `mandate.activated`/`revoked`/`expired`; `mandate.failed` не указан, хотя присутствует в `docs/contracts/opkc-adapter.md` §4 и в `docs/contracts/tsp-api.md` §5. Дельта неполна (недокументированное изменение).
- **Finding (low):** `CONTRACT-DIFF.md` §3.1 в ответе `POST /v1/mandates` указывает поле `expiresAt`; фактический `docs/contracts/tsp-api.md` §3.6.1 использует `validUntil` и `expiresAt` не содержит.
- Остальное совпадает: новые пути/схемы/enum (§2), новые коды ошибок `MANDATE_*` (§3.5 / `tsp-api.md` §4), события `mandate.*` (§3.4 / `tsp-api.md` §5), методы `registerMandate`/`getMandateStatus`/`cancelMandate`/`createSubscriptionCharge` (§4 / `opkc-adapter.md` §3).

### 5. Fitness-правила из HANDOFF §5 — FINDING

Проверка `grep -F` каждого паттерна в целевом файле:

| Правило | Паттерн | Совпадений |
|---|---|---|
| `mandate-charge-only-from-active` | `только при согласии в состоянии `ACTIVE`` | **0** |
| `revocation-blocks-future-charges` | `После фиксации `REVOKED` любая новая инициация списания по согласию отклоняется` | 1 |
| `tsp-api-additive-only` | `Ни одного нового обязательного поля` | 1 |
| `subscriptions-nfr-measurable` | `Списания из состояния согласия, отличного от `ACTIVE`` | 1 |

- **Finding (high):** правило №1 не сработает — в `docs/adr/ADR-008-…md:23` формулировка иная: «списание по согласию возможно только если согласие в состоянии `ACTIVE`». Паттерн `must_contain` требует дословного вхождения, поэтому fitness на A4′ будет вечно красным. Исправление: либо привести паттерн к фактическому тексту (`согласие в состоянии `ACTIVE``), либо поправить ADR-008 под паттерн.

### 6. Измеримость NFR §7 — VERIFIED

`docs/nfr.md` §7 — 16 строк, каждая содержит цель и метод проверки (нагрузочный тест/APM, тест гонки, fitness, сверка, SLO). Протокол-зависимые цели помечены `[ТРЕБУЕТ ПРОВЕРКИ]`. Базовое правило от `.arch-handoff/CONSTRAINTS.yaml` (`nfr-measurable`: подстрока `99,95`) сохранено.

## Дополнительно (вне шести пунктов, одна строка)

Проверен и `.arch-handoff/CONSTRAINTS.yaml` (`adr-no-placeholders`: `docs/adr/*.md` не должен содержать `<!--`) — ADR-008 комментариев не содержит, нарушений нет.

## Сводка

- Blocking (high): правило fitness №1; отсутствие `mandateId`/`initiation` в `tsp-api.md` §3.3 при заявленном расширении.
- Medium: пропуск `mandate.failed` в дельте opkc-adapter.
- Low: механизм подписок без inline-маркера в ADR-008; `expiresAt` vs `validUntil`.
