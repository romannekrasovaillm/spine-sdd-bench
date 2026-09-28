# Spec Delta

## Purpose

Defines the required additions to the core↔transport contract (ОПКЦ СБП adapter) so the gateway
core can run recurring charges without knowing the НСПК protocol (AD-004, AD-008).

## ADDED Requirements

### Requirement: Рекуррентные операции адаптера

Контракт адаптера SHALL предоставлять операции регистрации и отмены согласия/подписки,
запроса статуса согласия, создания рекуррентного списания и его разворота (компенсации).
Все мутирующие вызовы SHALL быть идемпотентны по передаваемому `reference`.

#### Scenario: Регистрация согласия

- **WHEN** ядро вызывает `registerSubscription` с `reference` = `subscriptionId`
- **THEN** адаптер SHALL вернуть `consentId`/ссылку для плательщика, а повторный вызов с тем же `reference` MUST NOT создавать второе согласие

#### Scenario: Разворот подтверждённого, но не зачисленного списания

- **WHEN** ядро вызывает `reverseCharge` по `reference` = `chargeId` для подтверждённого, но не зачисленного списания
- **THEN** адаптер SHALL инициировать возврат средств плательщику и подтвердить операцию событием; повторный вызов MUST NOT дублировать возврат

### Requirement: События подписок и списаний адаптера

Адаптер SHALL публиковать события подписок и списаний с `eventId` (at-least-once) и
`correlationRef` ядра; ядро дедуплицирует по `eventId`.

#### Scenario: Событие отзыва согласия

- **WHEN** ОПКЦ фиксирует отзыв согласия
- **THEN** адаптер SHALL опубликовать `subscription.revoked` с `correlationRef` = `subscriptionId` и `eventId`

#### Scenario: Событие отклонённого списания

- **WHEN** ОПКЦ отклоняет списание
- **THEN** адаптер SHALL опубликовать `charge.rejected` с нормализованным `reasonCode`

### Requirement: Таймауты и деградация рекуррентных операций

Рекуррентные операции SHALL соблюдать те же требования по таймаутам, ретраям и circuit breaker,
что и платёжные (деградация — `503 TRANSPORT_UNAVAILABLE` + `transport.unavailable`, без потери операций).

#### Scenario: Недоступность канала

- **WHEN** канал к НСПК недоступен во время рекуррентной операции
- **THEN** адаптер SHALL вернуть `503 TRANSPORT_UNAVAILABLE` и опубликовать `transport.unavailable`; ядро SHALL сохранить операцию и повторить её идемпотентно
