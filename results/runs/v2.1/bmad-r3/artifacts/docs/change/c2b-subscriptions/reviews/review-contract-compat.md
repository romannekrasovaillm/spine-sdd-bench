# Review — CONTRACT-COMPATIBILITY lens

- Линза: совместимость контракта и согласованность с моделью (FSM / ADR-008 / AD-009…AD-013)
- Предмет: `openapi/tsp-api.yaml` (v0.2.0), `docs/contracts/tsp-api.md` (v0.2 draft)
- Модель-эталон: `docs/spec/consent-state-machine.md`, `ARCHITECTURE-SPINE.md` (AD-009…AD-013), `docs/adr/ADR-008-*.md`, `docs/spec/state-machine.md` (платёж, v0.1)
- Дата: 2026-09-29. Read-only по артефактам; изменений в deliverables не вносилось.

## Вердикт

**Backward compatibility (§1): ПОДТВЕРЖДЕНА** для существующих потребителей — машинная проверка не нашла ни одного удаления/сужения (детали и точные команды ниже).

**Готовность контракта к фиксации (§2–§4): НЕ ГОТОВ** — есть два блокирующих дефекта согласованности (CONTRACT-1, CONTRACT-2) и один major по покрытию ошибок (CONTRACT-3). Оба блокирующих не ломают v0.1-потребителей, но делают новый (CONSENT) контур неоднозначным для реализации ядра и для клиента.

Тир-итог: **2 × Blocking, 1 × Major, 1 × Minor, 2 × Nit.**

---

## §1. Backward compatibility — evidence

Базa v0.1 извлечена из `git show HEAD:openapi/tsp-api.yaml` (`<TMP>.yaml`, 52 строки). Диф выполнен скриптом на `js-yaml` (v4) + `@apidevtools/swagger-parser` (в `/tmp`, вне репозитория).

**Результат (дословный вывод диффера):**

```
=== 1. PATHS ===
v0.1 paths: /v1/payments, /v1/payments/{paymentId}
v0.2 paths: /v1/payments, /v1/payments/{paymentId}, /v1/subscriptions, /v1/subscriptions/{subscriptionId},
            /v1/subscriptions/{subscriptionId}/charges, .../suspend, .../resume, .../close
REMOVED PATH: (none)
=== 2. OPERATIONS ===
REMOVED OP: (none)   ADDED OP: 6 подписочных операций
=== 3. SHARED OPERATIONS: param/response deltas ===
(нет строк => параметры, набор ответов и requestBody.required операций createPayment/getPayment не менялись)
=== 4. SHARED SCHEMA COMPAT (PaymentRequest, Payment) ===
(нет строк => required-множества не менялись, property не удалены, тип/enum не удалены и не сужены, nullable нигде не сужен)
=== 5. $REF INTEGRITY ===
total internal refs: 16, dangling: 0
=== 6. operationId UNIQUENESS ===
operationIds: createPayment, getPayment, createSubscription, getSubscription, createCharge,
              suspendSubscription, resumeSubscription, closeSubscription   (8 уникальных)
=== 7. nullable usage / 3.0.x validity ===
(нет строк => `nullable` используется корректно для 3.0.3)
=== 8. required fields with no schema ===
(нет строк)
```

**Независимая валидация:**

```
swagger-parser: SWAGGER-PARSER: VALID
spectral (spectral:oas): 0 errors, 18 warnings (servers/contact/operation-description/operation-tags)
```

**Покомпонентно:**

| Проверка | Вердикт | Свидетельство |
|---|---|---|
| Удалённые пути | Нет | скрипт §1: `REMOVED PATH: (none)` |
| Удалённые/изменённые операции | Нет | скрипт §2, §3 |
| Новые required-поля в существующих схемах | Нет | `Payment.required` = `[paymentId, amount, status]` в v0.1 (52 стр.) и v0.2 (`openapi/tsp-api.yaml:156`) идентичны |
| Сужение типа | Нет | скрипт §4 (типы `PaymentRequest`/`Payment` не менялись) |
| Удалённые/суженные значения enum | Нет | `Payment.status` = `[CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED]` в v0.1 и v0.2 (`:162`) — идентичны |
| Добавленные поля | Только опциональные | `operationType` (`:163`), `subscriptionId` (`:167`) — не в `required` |
| `Idempotency-Key` required на `createPayment` | Не менялось | v0.1 и v0.2 (`:16`) — `required: true` |
| Dangling `$ref` | 0 из 16 | скрипт §5 |
| operationId uniqueness | OK | скрипт §6 |

**Вывод:** `docs/contracts/tsp-api.md` §7 (`docs/contracts/tsp-api.md:320`) «Значения существующего перечисления `status` платежа **не расширяются**» — фактически верно; удалений, сужений и новых обязательных полей нет. Формальная BC v0.1→v0.2 выполнена.

> Оговорка: BC верна для потребителей, работающих только со старыми путями. Но новая проекция charge→payment через `Payment.status` не определена (CONTRACT-1) — это дефект **новой поверхности**, не регресс v0.1.

---

## §2. Internal consistency — charge vs payment status

### CONTRACT-1 · Blocking · Статус списания и статус платежа — несовместимые словари, отображение не определено

**Файл/строки и цитаты:**

- `openapi/tsp-api.yaml:222-224` — словарь списания:
  ```
  status:
    type: string
    enum: [INITIATED, PAID, CREDITED, COMPLETED, FAILED]
  ```
- `openapi/tsp-api.yaml:160-162` — словарь платежа (не изменён с v0.1):
  ```
  status:
    type: string
    enum: [CREATED, QR_ISSUED, PAID, CREDITED, COMPLETED, FAILED, EXPIRED, REFUNDED]
  ```
- `docs/contracts/tsp-api.md:271` — «…статус списания читается **существующим** `GET /v1/payments/{paymentId}`»
- `docs/contracts/tsp-api.md:267` — ответ 201 на `createCharge`: `"status": "INITIATED"`
- `ARCHITECTURE-SPINE.md:86` (AD-010) — «Рекуррентное списание моделируется платежом с `operationType = CONSENT`… Последовательность `INITIATED → PAID → CREDITED → COMPLETED`»
- `docs/spec/consent-state-machine.md:73` (D1) — `— → INITIATED` создаётся запросом charge.

**Дефект (evidence):** списание *является* платежом (AD-010, `consent-state-machine.md:18`: «платёж типа `CONSENT` — это и есть списание»), но у корректных состояний нет двустороннего отображения:

1. Свежесозданное списание отдаёт `status = INITIATED` (`createCharge` 201), однако `Payment.status` значения `INITIATED` **не содержит**. Значит `GET /v1/payments/{paymentId}` для того же `paymentId`, согласно §6.4 (`:271`), обязан вернуть одно из `{CREATED, QR_ISSUED, …}` — но какое именно, контракт и FSM не определяют. `QR_ISSUED` при `operationType=CONSENT` недостижим (`consent-state-machine.md:81`; AD-010). Никакого нормативного маппинга `INITIATED → CREATED` нет ни в §6, ни в FSM §7 (`consent-state-machine.md:118` перечисляет «те же значения платежа: `INITIATED`, `PAID`, …» — то есть FSM ошибочно называет `INITIATED` значением платежа).
2. `Charge.status` **не может представить** терминальные состояния, достижимые для того же платежа: возврат зачисленного списания — существующая сага (`docs/contracts/tsp-api.md:279`; `consent-state-machine.md:81`), после успешного полного возврата `Payment.status = REFUNDED`, а `EXPIRED` достижим таймером; в `Charge.status` нет ни `REFUNDED`, ни `EXPIRED`.

**Failure scenario:** клиент делает `POST …/charges` → получает `{paymentId: pay_X, status: "INITIATED"}`. Немедленный `GET /v1/payments/pay_X` возвращает `status: "CREATED"` (единственно возможное согласованное значение, но нигде не предписанное) — клиент видит **два разных статуса для одного `paymentId`** и не может построить автомат. Если списание возвращено, `GET payment` даёт `REFUNDED`, а `Charge.status` не способен выразить это состояние вообще.

**Минимальная правка (contract-side; §7 «enum платежа не расширять» не нарушается):**
1. В §6.1/§6.4 опубликовать обязательную таблицу проекции: внутреннее `INITIATED` ⇔ внешнее `Payment.status = CREATED`; далее 1:1 (`PAID/CREDITED/COMPLETED/FAILED`), а `REFUNDED`/`EXPIRED` — состояния, видимые только через `GET /v1/payments/{paymentId}`.
2. Привести `Charge.status` к тому же словарю, что `Payment.status` (раз «списание — это платёж»), либо явно расширить `Charge.status` до `[INITIATED, PAID, CREDITED, COMPLETED, FAILED, REFUNDED, EXPIRED]` и указать правило `INITIATED ≡ CREATED`. Рекомендуемый вариант — переиспользовать `Payment.status` целиком и убрать `INITIATED` из внешнего контракта (оставив его внутренним); тогда `openapi/tsp-api.yaml:224`, описание 201 (`:93`) и `consent-state-machine.md:118` синхронизируются.
3. Добавить в FSM §7 явную таблицу «внутренний статус списания → `Payment.status`».

---

## §3. Idempotency-semantics consistency

### CONTRACT-2 · Blocking · Прецедент `Idempotency-Key` vs `chargeId` не определён; правило повтора противоречит само себе

**Файл/строки и цитаты:**

- `ARCHITECTURE-SPINE.md:93` (AD-011): «У каждой попытки списания есть `chargeId` (**совместим с `Idempotency-Key`**) и ключ периода `billingPeriod`… **Повтор с тем же ключом возвращает существующий ресурс** и не создаёт второе списание или вторую проводку».
- `docs/spec/consent-state-machine.md:101`: «`POST /v1/subscriptions/{id}/charges` | **`Idempotency-Key` = `chargeId` + `billingPeriod`** | успешная попытка за период уже есть → возврат существующего `chargeId` (200)».
- `docs/contracts/tsp-api.md:24`: «Повторный `POST` с тем же ключом и **тем же телом** → возвращается **тот же ресурс**… **200/201**».
- `docs/contracts/tsp-api.md:25`: «Повторный `POST` с тем же ключом, но **другим телом** → **`409 IDEMPOTENCY_CONFLICT`**».
- `openapi/tsp-api.yaml:83-85` — `Idempotency-Key` (header, `required: true`); `openapi/tsp-api.yaml:209` — `chargeId` (body, «Идемпотентный идентификатор попытки»); `:210` — `billingPeriod` («уникален в паре с subscriptionId»).
- `openapi/tsp-api.yaml:102-103` — ответ `409` операции `createCharge`: `"CHARGE_ALREADY_EXISTS | CHARGE_CONFLICT"` — **`IDEMPOTENCY_CONFLICT` здесь отсутствует**.
- `docs/contracts/tsp-api.md:314` — `CHARGE_CONFLICT` (409) — «конфликт `chargeId`/`billingPeriod` с другим телом запроса».

**Дефект:** на одну операцию заведено **три** ключа идемпотентности (`Idempotency-Key`, `chargeId`, пара `(subscriptionId, billingPeriod)`), и ни один документ не задаёт приоритет. Хуже, источники противоречат друг другу в конкретном сценарии «тот же `Idempotency-Key`, `billingPeriod` повторяется, `chargeId` в теле другой»:

| Источник | Ожидаемый ответ |
|---|---|
| AD-011 (`ARCHITECTURE-SPINE.md:93`) и FSM (`:101`) | `200` + существующее списание (**ключ первичен, тело игнорируется**) |
| `docs/contracts/tsp-api.md:25` | `409 IDEMPOTENCY_CONFLICT` (**тело первично**) |
| `openapi/tsp-api.yaml:103` | `409 CHARGE_CONFLICT` |

Ни одно правило не покрывает случай `Idempotency-Key ≠ chargeId` на проводе. FSM `:101` вообще постулирует `Idempotency-Key = chargeId + billingPeriod`, но контракт этого равенства **не требует** — значит семантика FSM непроверяема у границы API.

**Failure scenario:** ТСП-планировщик ретраит списание, сгенерировав **новый** `chargeId` и **новый** `Idempotency-Key`, при том же `billingPeriod` и уже успешном списании. По §4 guard (`consent-state-machine.md:92`, п.6) → `409 CHARGE_ALREADY_EXISTS` (ок). Но при ретрае с **тем же** `Idempotency-Key` и изменённым телом три документа дают три разных ответа — реализация ядра и клиент не могут договориться о коде и о том, создаётся ли второе списание.

**Минимальная правка:**
1. В §2/§6.4 зафиксировать иерархию: **(a)** `Idempotency-Key` — единственный ключ повтора запроса; тот же ключ ⇒ тот же ресурс (`200`/`201`), тело обязано совпадать, иначе `409 IDEMPOTENCY_CONFLICT`; **(b)** `chargeId` — идентификатор ресурса: тот же `chargeId` под новым ключом ⇒ `200` + существующее списание; **(c)** тот же `(subscriptionId, billingPeriod)` при другом успешном `chargeId` ⇒ `409 CHARGE_ALREADY_EXISTS`.
2. Добавить `IDEMPOTENCY_CONFLICT` в описание `409` операции `createCharge` (`openapi/tsp-api.yaml:103`).
3. Привести FSM `:101` к контракту: либо явно требовать `Idempotency-Key == chargeId` для `/charges`, либо убрать равенство и сделать header авторитетным.

### CONTRACT-5 (Nit) · Несогласованная модель идемпотентного повтора на «старых» операциях

`docs/contracts/tsp-api.md:24` обещает «статус `200/201`» на идемпотентный повтор вообще, но:
- `createPayment` (`openapi/tsp-api.yaml:24`) объявляет **только** `201`;
- `createSubscription` (`:55`) объявляет **только** `201` (плюс `409`);
- `createCharge` (`:92`,`:97`) объявляет `201` **и** `200`.

Один и тот же инвариант смоделирован по-разному в одном контракте; кодогенерация и клиенты получают разные сигнатуры. Минимальная правка: добавить `200`-ответ (тот же ресурс) на `createPayment` и `createSubscription` либо убрать `200`-обещание из §2.

---

## §4. Error-code coverage vs FSM

### CONTRACT-3 · Major · Покрытие отказов FSM неполно; часть кодов не выведена в контракт

Полный перечень отказов FSM (`docs/spec/consent-state-machine.md` §2.2, §3, §4) и их отражение:

| Отказ FSM | Источник | Покрытие в контракте | Оценка |
|---|---|---|---|
| Guard списания: не `ACTIVE` | D2 (`:74`) | `422 SUBSCRIPTION_NOT_ACTIVE` (`openapi:108`) | ✅ |
| Guard: превышение лимита | D2, §4 п.3-4 | `422 SUBSCRIPTION_LIMIT_EXCEEDED` (`openapi:108`) | ✅ |
| Guard: срок истёк | D2, §4 п.5 | `422 SUBSCRIPTION_EXPIRED` (`openapi:108`) | ✅ |
| Успешное списание за период уже есть | §4 п.6, §5 (`:105`) | `409 CHARGE_ALREADY_EXISTS` (`openapi:103`) | ✅ (но см. CONTRACT-2) |
| Отказ банка/ОПКЦ по списанию (D4) | `:76` | асинхронно `charge.failed` + `Charge.failureCode` (`openapi:225`) | ⚠️ частично |
| Отказ плательщика / отклонение согласия (C3/C5) | `:42`,`:44` — FSM пишет **`errorCode`** | вебхук `subscription.declined` (тип), но поле `errorCode`/`reason` **отсутствует** и в `Subscription` (`openapi:187-205`), и в теле вебхука (`docs/contracts/tsp-api.md:306`) | ❌ причина не наблюдаема |
| Отзыв согласия (C6/C10) | `:45`, `:49` | `subscription.revoked` + guard → `422 SUBSCRIPTION_NOT_ACTIVE` | ✅ |
| Истечение срока (C9) | `:48` | `subscription.expired` + `422 SUBSCRIPTION_EXPIRED` | ✅ |
| `resume`/`close`/`suspend` по терминальному согласию (нарушение C8 guard «согласие не истекло и не отозвано» `:47`, §2.3 «отзыв необратим» `:57`) | `:47`, `:57` | операции объявляют **только `200`** (`openapi:118`, `:129`, `:141`) | ❌ нет `409`/`422` |
| Несуществующий/чужой `subscriptionId` (guard C1 «`tspId` совпадает» `:40`) | `:40` | Ни один подписочный путь не объявляет `404`; канонический `NOT_FOUND` (404) есть только в прозе (`docs/contracts/tsp-api.md:151`) | ❌ |
| Зачисление в АБС недоступно (D6, `ABS_PENDING`) | `:78` | FSM §7 (`:119`) обещает «`PAID` + `creditingStatus`», но `Payment` (`openapi:154-169`) **не имеет** `creditingStatus` | ❌ |
| Транзиентные сбои ОПКЦ/АБС, лимит частоты | `docs/contracts/tsp-api.md:151` (`INTERNAL` 500, `RATE_LIMITED` 429) | На подписочных операциях не объявлено ни `429`, ни `500`, ни `401/403`; `securitySchemes`/`security` отсутствуют вовсе | ❌ |

**Failure scenario (404):** ТСП делает `GET /v1/subscriptions/sub_0bad` или `POST …/close`. Контракт обещает `200`; фактический ответ ядра (по §4, `NOT_FOUND`) не описан — клиент по спецификации не может отличить «закрыто» от «не найдено», а кодогенерация не создаёт ветку ошибки.

**Failure scenario (decline reason):** плательщик отклонил оформление. FSM C5 (`consent-state-machine.md:44`) предписывает сохранить `errorCode`; `Subscription` его не выставляет, тело вебхука (`docs/contracts/tsp-api.md:306`) — тоже. ТСП не может передать клиенту причину.

**О размещении кодов на HTTP-статусах:** размещение *объявленных* кодов корректно — guard-нарушения на `422`, конфликты ресурса на `409`. Проблема не в статусах, а в **отсутствующих** кодах/статусах.

**Минимальная правка:**
1. Добавить `errorCode`/`reason` в схему `Subscription` (`openapi:187`) и в тело `subscription.declined` (`docs/contracts/tsp-api.md:306`).
2. Объявить `404` на `getSubscription`/`suspend`/`resume`/`close` (и на `getPayment`) со ссылкой на `Problem`/`NOT_FOUND`.
3. Ввести код для терминального состояния (например `SUBSCRIPTION_TERMINAL` / `SUBSCRIPTION_NOT_RESUMABLE`, `409`/`422`) на `resume`/`suspend`/`close`.
4. Добавить `errorCode` + `creditingStatus` в `Payment` (`openapi:154`), чтобы путь §6.4 (`docs/contracts/tsp-api.md:271`) не терял детали, показанные в примере §3.3 (`:109`).
5. Объявить общие `401`/`403`/`429`/`500` (или один `default`) на всех операциях; добавить `securitySchemes` (mTLS + `X-API-Key`, `docs/contracts/tsp-api.md:16`).

---

## §5. OpenAPI hygiene

**Пройдено (evidence):**
- Dangling `$ref` — **0** из 16 (скрипт §5).
- `operationId` уникальны — 8/8 (скрипт §6).
- `nullable` валиден для 3.0.3: `endDate` (`openapi:180`), `failureCode` (`:225`) — у обоих есть `type`, значение булево (скрипт §7); `swagger-parser: VALID`, `spectral: 0 errors`.
- Все `required`-поля имеют определения в `properties` (скрипт §8).

### CONTRACT-4 · Minor · Расхождения примеров и схемы; «статические» пробелы

1. **Отсутствует обязательное поле в примере.** `Charge.required = [chargeId, subscriptionId, billingPeriod, amount, status]` (`openapi:215`), но пример `charges[]` в `docs/contracts/tsp-api.md:240`:
   ```
   { "chargeId": "chg_1a2b3c", "billingPeriod": "2026-10", "amount": 49900, "status": "COMPLETED" }
   ```
   — отсутствует `subscriptionId`. Клиент, копирующий пример, получит невалидный по схеме объект. Правка: добавить `subscriptionId` в пример (или убрать поле из `required`).
2. **Схема `Payment` беднее прозы.** `Payment` (`openapi:154-169`) не содержит `errorCode`, `creditingStatus`, `refunds`, `paidAt`, `qrId`, хотя пример §3.2/§3.3 (`docs/contracts/tsp-api.md:82-109`) их показывает. Потребители, генерирующие клиентов по YAML, этих полей не увидят. (Частично наследие v0.1, но v0.2-документ их по-прежнему декларирует.)
3. **В YAML нет ни одного `example`.** Все примеры живут в `docs/contracts/tsp-api.md`; сам контракт машинно-читаемых примеров не несёт — генерённые моки/док-порталы будут пустыми, а `spectral` не сможет проверить примеры на соответствие схеме.
4. **Нет `servers`** (spectral `oas3-api-servers`) и **нет `security`/`securitySchemes`** при заявленных в `docs/contracts/tsp-api.md:16` «mTLS + `X-API-Key`».
5. **`integer` без `minimum`/`int64`.** `amount`, `maxAmountPerCharge`, `periodLimit` — «копейки»; при лимитах > 2³¹−1 копейки (≈ 21,47 млн ₽) кодогенерация с `int32` переполнится. Правка: `format: int64`, `minimum: 0` (для amounts — `minimum: 1`).
6. **`Subscription.charges` без пагинации** (`openapi:201-203`): для долгоживущего согласия массив растёт неограниченно; нет `limit`/`cursor`. Низкая срочность, но потребительский контракт.
7. **`Problem` (`openapi:227-236`) не помечает обязательными `type`/`title`/`status`**, хотя RFC 9457 их определяет. Низкая срочность.
8. **Условная обязательность не выражена.** `subscriptionId` «присутствует только при `operationType=CONSENT`» (`openapi:169`) — это инвариант, который в 3.0.x нельзя выразить схемой; зафиксировать в прозе §6.6 явно как MUST.

### CONTRACT-6 · Nit · Смешанные алфавиты и неоднозначность имён

- `openapi:203` — `consentUrl` описан как «Ссылка/**де**eplink…» (кириллическая «е» внутри латиницы «deeplink») — косметика, но ломает поиск/копипаст.
- `Charge.failureCode` (`openapi:225`) vs `Payment.errorCode` (`docs/contracts/tsp-api.md:109`) vs FSM `errorCode` (`consent-state-machine.md:76`) — три имени для одной сущности «нормализованный код отказа». Унифицировать (рекомендуется `errorCode`).

---

## Сводка

| ID | Тир | Суть | Файл |
|---|---|---|---|
| CONTRACT-1 | **Blocking** | `Charge.status` и `Payment.status` — несовместимые словари; маппинг `INITIATED↔?` не определён, `REFUNDED/EXPIRED` невыразимы в `Charge.status` | `openapi/tsp-api.yaml:162,224`; `docs/contracts/tsp-api.md:267,271` |
| CONTRACT-2 | **Blocking** | Приоритет `Idempotency-Key` vs `chargeId` vs `(subscriptionId,billingPeriod)` не задан; AD-011/FSM и §2 дают противоречивые ответы на «тот же ключ, другое тело» | `ARCHITECTURE-SPINE.md:93`; `consent-state-machine.md:101`; `docs/contracts/tsp-api.md:24-25,314`; `openapi/tsp-api.yaml:103,209` |
| CONTRACT-3 | Major | Не покрыты: `NOT_FOUND`/404 на подписочных путях, отказ `resume`/`close` терминального согласия, причина `DECLINED`, `creditingStatus`, общие 401/403/429/500 | `openapi/tsp-api.yaml:118,129,141,154,187` |
| CONTRACT-4 | Minor | Пример `charges[]` без обязательного `subscriptionId`; `Payment`-схема беднее прозы; нет `examples`/`servers`/`security`; `integer` без `int64` | `docs/contracts/tsp-api.md:240`; `openapi/tsp-api.yaml:154,227` |
| CONTRACT-5 | Nit | Идемпотентный повтор обещан `200/201`, но `200` есть только у `createCharge` | `openapi/tsp-api.yaml:24,55,97` |
| CONTRACT-6 | Nit | `деeplink` со смешанным алфавитом; `failureCode`/`errorCode` — три имени одной сущности | `openapi/tsp-api.yaml:203,225` |

**Backward compatibility (§1): PASS.** Блокирующие пункты относятся к согласованности новой (CONSENT) поверхности, а не к регрессу v0.1-потребителей; оба должны быть закрыты до фиксации `v1.0-draft` на A1.
