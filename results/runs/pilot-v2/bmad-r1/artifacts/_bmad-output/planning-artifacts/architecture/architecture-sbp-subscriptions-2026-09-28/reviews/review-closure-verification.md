# Closure verification — SBP subscriptions change package (после применения правок)

- Verifier: independent verifier (read-only), не автор правок
- Date: 2026-09-28
- Repo root: `.../cells/wjk682n/ws`
- Method: для каждой находки прочитаны **текущие** файлы (не review-снапшот) и проверено, закрывает ли правка заявленный дефект. Источники review — `reviews/review-rubric.md`, `reviews/review-reality.md`, `reviews/review-adversarial.md`, `reviews/review-compliance.md` (обе версии — «до»), текущее состояние — рабочее дерево (все правки не закоммичены: `git status` показывает `M` по 9 файлам + новые ADR-008 / mandate-lifecycle / `_bmad-output`).
- Замечание: review-снапшоты писались против spine с AD-009…AD-011; текущий spine содержит AD-009…**AD-016**.

## Итог

| Вердикт | Кол-во |
|---|---|
| CLOSED | 16 |
| PARTIAL | 1 |
| OPEN | 2 |
| **Всего** | **19** |

---

## 1. `maxTotalAmount` не покрыт инвариантом и charge-guard (R-01, F4-1) — **CLOSED**

AD-011 Rule теперь включает «остаток `maxTotalAmount` достаточен» и инкремент суммарного счётчика под блокировкой/версией мандата; та же проверка продублирована в спецификации.

- Evidence: `ARCHITECTURE-SPINE.md` AD-011 (Rule) — «`amount ≤ maxAmountPerCharge` ∧ **остаток `maxTotalAmount` достаточен** ∧ … суммарный счётчик мандата инкрементируется **под блокировкой или версией мандата** в одной транзакции».
- Evidence: `docs/spec/mandate-lifecycle.md` §4 — та же пятичленная проверка + инкремент под блокировкой/версией.
- Остаток (не часть находки): семантика освобождения счётчика при `FAILED`/`EXPIRED`/возврате не описана; ADR-008 Decision 1 по-прежнему не перечисляет `maxTotalAmount` в списке параметров (но контракт и guard его содержат).

## 2. Нет сериализации charge-vs-revoke (R-02, adversarial 1) — **CLOSED**

AD-011 Rule прямо называет механизм (`под блокировкой или версией мандата`) и требование сериализации («списание не может быть создано после коммита отзыва»); то же в spec.

- Evidence: `ARCHITECTURE-SPINE.md` AD-011 (Rule) — «…под блокировкой или версией мандата в одной транзакции с созданием платежа; …Проверка и создание списания **сериализуются** с отзывом/приостановкой так, что списание **не может быть создано после коммита отзыва**».
- Evidence: `docs/spec/mandate-lifecycle.md` §4 — «Сериализация гарантирует, что списание не создаётся после коммита отзыва».

## 3. `CREATED → EXPIRED` для списаний не определён в FSM (R-03) — **OPEN**

Правка лишь переписала ссылку на переход, которого нет: `mandate-lifecycle.md` §4 теперь говорит «`CREATED → EXPIRED` — по TTL ожидания подтверждения (**T5**)», но T5 в таблице — это `QR_ISSUED → EXPIRED`, а `state-machine.md` §2а по-прежнему утверждает «Добавлен **только** переход T13».

- Evidence (`не закрыто`): `docs/spec/state-machine.md` §2 — T5 = `QR_ISSUED → EXPIRED`; строки `CREATED → EXPIRED` в T-таблице нет; §2а — «Добавлен только переход **T13**… все остальные … без изменений».
- Evidence (источник противоречия): `docs/spec/mandate-lifecycle.md` §4 — «`CREATED → EXPIRED` — по TTL ожидания подтверждения (T5)».
- Вывод: два документа по-прежнему расходятся; один исполнитель оставит списание в `CREATED` навсегда, другой изобретёт переход.

## 4. Вебхуки resume/expiry отсутствовали; timeout согласия помечен как rejected (R-04) — **CLOSED**

M4 теперь шлёт `mandate.expired` (не `rejected`), M6 шлёт `mandate.resumed`, M9 шлёт `mandate.expired`; полный набор из шести событий объявлен и в контракте, и в §7 спецификации.

- Evidence: `docs/spec/mandate-lifecycle.md` §2 (M4/M6/M9) и §7 — «События мандата наружу: `mandate.activated`, `mandate.suspended`, `mandate.resumed`, `mandate.revoked`, `mandate.expired`, `mandate.rejected`».
- Evidence: `docs/contracts/tsp-api.md` §5 — события `mandate.resumed`, `mandate.expired` и др. объявлены.

## 5. Операционный конверт не решён/не отложен на altitude spine (R-05) — **CLOSED**

В spine добавлен отдельный блок «Операционный конверт подписок (ADR-008)»: rollout/rollback (per-ТСП фиче-флаг, kill-switch, управляемый отзыв), эксплуатация мандатов (ежечасная сверка, алерты), политики на A2.

- Evidence: `ARCHITECTURE-SPINE.md`, раздел «Операционный конверт подписок (ADR-008)»; вторично — `docs/solutioning.md` §11 (план отката, владелец, RTO ≤ 1 ч).

## 6. Диаграмма: прямое ребро NSPK→gateway `mandate.activated` (F2-1) — **CLOSED**

Событие активации теперь идёт через адаптер: `N-->>V: mandate.activated` → `V-->>G: mandate.activated`.

- Evidence: `ARCHITECTURE-DECISION-SBP-SUBSCRIPTIONS.md` §2.3 (sequence diagram, шаги после «плательщик подтверждает согласие в своём банке»).

## 7. T13-guard без проверки суммы/получателя (F2-3) — **CLOSED**

Guard T13 теперь содержит «**сумма и получатель совпадают** (иначе — как T7: `FAILED`, зачисление запрещено, AD-005)».

- Evidence: `docs/spec/state-machine.md` §2, строка T13.

## 8. Suspend (обратимо) смешано с revoke (необратимо) в транспортном контракте (F2-2) — **CLOSED**

`revokeMandate` теперь явно «**необратимый** отзыв»; добавлен абзац, что `SUSPENDED` — локальный обратимый запрет, в ОПКЦ не передаётся и не подменяется `revokeMandate`; сверка трактует «ОПКЦ ACTIVE / у нас SUSPENDED» как ожидаемое расхождение.

- Evidence: `docs/contracts/opkc-adapter.md` §3 (`revokeMandate` + абзац про `SUSPENDED`); `docs/spec/mandate-lifecycle.md` §6 (ожидаемое расхождение, без алерта).

## 9. RFP: «G1–G7» при добавленном G8 (F3-1) — **CLOSED**

Диапазон исправлен на «G1–G8».

- Evidence: `docs/rfp/vendor-rfp.md` §9, шаг 1 — «RFI (2 нед): квалификация по **G1–G8**». Поиск по `docs/` не находит иных «G1–G7».

## 10. `Idempotency-Key` не объявлен на suspend/resume/revoke (F4-2) — **CLOSED**

Все три POST-эндпоинта теперь объявляют `Idempotency-Key` c `required: true`.

- Evidence: `openapi/tsp-api.yaml` — пути `/v1/mandates/{mandateId}/suspend`, `/resume`, `/revoke` (блок `parameters`).

## 11. Подтверждённые списания после отзыва некомпенсируемы (adversarial 2) — **CLOSED**

Добавлен AD-012: если списание уже подтверждено, оно исполняется, а компенсацию возвратом через сагу ADR-005 инициирует **шлюз** (не только ТСП); продублировано в ADR-008 Decision 9, spec и в критерии приёмки AC-11.

- Evidence: `ARCHITECTURE-SPINE.md` AD-012 (Rule) — «…**шлюз** (а не ТСП) инициирует компенсацию — возврат по этому списанию через сагу ADR-005».
- Evidence: `docs/spec/mandate-lifecycle.md` §3/§4; `ARCHITECTURE-DECISION-SBP-SUBSCRIPTIONS.md` §6.1 (AC-11).
- Остаток (вне формулировки находки): ADR-005 §4 и `docs/contracts/tsp-api.md` §3.4 не расширены явным «системным» origin возврата (`refundOrigin`) и событием; триггер возврата в ADR-005 по-прежнему описан как ТСП-инициируемый. Архитектурно владелец назначен на уровне spine (AD-012), поэтому дефект «архитектурно невосстановимо» закрыт.

## 12. Списания не видны сверке (ключ `qrId`) (adversarial 3) — **CLOSED**

Добавлен `getMandateChargeStatus` по ключу списания и расширен `getReconciliationReport` (`operationRef` = `qrId` **или** `reference` списания, `type` = `qr`/`mandate_charge`/`mandate`); закреплено AD-014 и spec §6.

- Evidence: `docs/contracts/opkc-adapter.md` §3 (`getMandateChargeStatus`, `getReconciliationReport`); `ARCHITECTURE-SPINE.md` AD-014; `docs/spec/mandate-lifecycle.md` §6.

## 13. Два AD-совместимых эмиттера зачисления → двойной кредит (adversarial 4) — **CLOSED**

Добавлен AD-013: переход `PAID → ABS_PENDING` фиксируется **атомарным claim** по `paymentId`; сверка не вызывает АБС напрямую, а дозапускает тот же claim; повторный claim при существующем `absDocId` не создаёт вторую проводку.

- Evidence: `ARCHITECTURE-SPINE.md` AD-013 (Rule); вторично — `docs/spec/mandate-lifecycle.md` §4, `ARCHITECTURE-DECISION…` AC-12.

## 14. Идемпотентность списания: скоупы/`период` неоднозначны (adversarial 5, R-06) — **CLOSED**

Финансовый ключ (`mandateId`, `merchantOrderId`) объявлен принадлежащим агрегату мандата и хранится **на весь срок жизни мандата** (а не 24 ч), `Idempotency-Key` низведён до 24-часового кэша ретрая; терминальный отказ (`FAILED`/`EXPIRED`) **освобождает** ключ, завершённое списание удерживает → `409`. Оба сценария из находки (двойное списание после 24 ч; «отравление» периода на транзиентном сбое) закрыты.

- Evidence: `docs/spec/mandate-lifecycle.md` §5; `docs/contracts/tsp-api.md` §3.9; `ARCHITECTURE-SPINE.md` AD-010.

## 15. Нет артефакта согласия (compliance C-1) — **CLOSED**

Добавлен AD-015: активация возможна только при получении **подтверждённых** условий и ссылки-доказательства; `getMandateStatus` обязан возвращать подтверждённые условия + ссылку-доказательство; в OpenAPI у `Mandate` появилось `consentEvidenceRef`.

- Evidence: `ARCHITECTURE-SPINE.md` AD-015; `docs/spec/mandate-lifecycle.md` M2/§3; `docs/contracts/opkc-adapter.md` §3 (`getMandateStatus`); `openapi/tsp-api.yaml` (`Mandate.consentEvidenceRef`).

## 16. Уведомление до списания без владельца и неисполнимо (compliance H-2) — **PARTIAL**

Точка контроля теперь обязательна и fail-closed (списание не исполняется без подтверждения требования уведомления — AD-016, spec §3), но **владелец проверки и форма подтверждения по-прежнему отложены на A2**, `noticeRef` в контракте остаётся **опциональным**, а NFR §7 сохраняет недостижимую цель «100 %».

- Evidence (закрыто частично): `ARCHITECTURE-SPINE.md` AD-016 (Rule) — «Списание не исполняется без подтверждения исполнения требования уведомления…»; `docs/spec/mandate-lifecycle.md` §3 — fail-closed.
- Evidence (не закрыто): там же AD-016 — «владелец проверки и форма подтверждения — по регламенту НСПК, **политика утверждается на A2** `[ТРЕБУЕТ ПРОВЕРКИ]`»; `docs/contracts/tsp-api.md` §3.9 (`noticeRef` — «опц.») и §7 п.6; `docs/nfr.md` §7 («100 % … `[ТРЕБУЕТ ПРОВЕРКИ]`»); `ARCHITECTURE-DECISION…` §7 п.8.

## 17. Нет обязательного антифрода/AML для безлюдных списаний (compliance H-4) — **CLOSED**

AD-016 делает контроль антифрода/AML **обязательным** при создании мандата (M1) и на каждое списание, fail-closed; закреплено в spec §3 и AC-14.

- Evidence: `ARCHITECTURE-SPINE.md` AD-016 (Rule) — «Контроль антифрода/AML обязателен при создании мандата и на каждое списание; при недоступности контроля списание отклоняется, а не пропускается (fail-closed)»; `docs/spec/mandate-lifecycle.md` §3; `ARCHITECTURE-DECISION…` AC-14.
- Остаток (вне формулировки находки): конкретные velocity/пороговые метрики в NFR §7 не добавлены и отложены на A2.

## 18. ПДн нового агрегата объявлены «не затронутыми» (compliance M-5) — **CLOSED**

Противоречие снято: AD-006 в таблице влияния помечен «Да, аддитивно» с явной новой поверхностью ПДн (минимизация/шифрование/срок хранения); AD-009 Rule требует минимизации, шифрования в покое и заданной политики хранения; срок хранения вынесен отдельным вопросом на человека.

- Evidence: `ARCHITECTURE-DECISION-SBP-SUBSCRIPTIONS.md` §2.1 (строка AD-006) — «Да, **аддитивно** … агрегат хранит реквизиты плательщика (ПДн) — новая поверхность минимизации/шифрования/срока хранения»; `ARCHITECTURE-SPINE.md` AD-009 (Rule) — «Реквизиты плательщика … минимизированы, шифруются в покое, срок хранения задан политикой ПДн»; `ARCHITECTURE-DECISION…` §7 п.5.
- Остаток (вне формулировки находки): отдельной строки ПДн в `docs/nfr.md` §7 так и нет.

## 19. Семантика протокола НСПК подана как нормативный факт (reality F1-1/F1-2/F1-3) — **OPEN**

Несущие Decision/Rule-утверждения остались без inline-метки: ADR-008 Decision 1 (`opkcMandateRef` = «сохранённый способ расчёта») и Decision 2 («подтверждение приходит от ОПКЦ нотификацией/сверкой»), AD-010 Rule («шаг выпуска QR пропускается (`CREATED → PAID`)»), `tsp-api.md` §3.8 («Отзыв плательщиком … приходит нотификацией ОПКЦ») — меток `[ТРЕБУЕТ ПРОВЕРКИ]`/`[ASSUMPTION]` рядом нет. Inline-метки есть только у AD-011 и AD-016; заявление spine «все ссылки на протокол … помечены `[ТРЕБУЕТ ПРОВЕРКИ]`» не подтверждается.

- Evidence (`не закрыто`): `docs/adr/ADR-008-…md` Decision 1/2 (grep: `[ТРЕБУЕТ ПРОВЕРКИ]` встречается только в Context:17, Consequences:57, References:71); `ARCHITECTURE-SPINE.md` AD-010 (Rule, стр. ~91) — метки нет; `docs/contracts/tsp-api.md` §3.8 (стр. ~180) — метки нет.
- Частично: из RFP убран тезис об обязанности уведомления до списания (§1 п.7, G8 текущей версии) — но это не помечает нормативный текст ADR/spine/contract.

---

## Сводка для родительского агента

- **CLOSED (16):** 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18.
- **PARTIAL (1):** 16 — fail-closed guard добавлен, но владелец/форма уведомления отложены на A2, `noticeRef` опционален, NFR «100 %» неизмерим.
- **OPEN (2):**
  - 3 — `CREATED → EXPIRED` так и не внесён в T-таблицу; ссылка на «T5» неверна (T5 = `QR_ISSUED → EXPIRED`), а §2а гласит «добавлен только T13».
  - 19 — Decision/Rule ADR-008 (1/2), AD-010 и tsp-api §3.8 остаются протокольными утверждениями без inline-метки.
- Новые residual-замечания (вне исходного списка): ADR-005 §4/tsp-api §3.4 без «системного» origin возврата; счётчик `maxTotalAmount` без семантики освобождения; ADR-008 References/спеки всё ещё ссылаются на «AD-009…AD-011»; отдельной строки ПДн/антифрода в NFR §7 нет.
