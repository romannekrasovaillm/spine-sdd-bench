# Preflight v2 — преднастройка без модели (руководство `spine-sdd-bench-v2-guide.md`, §6 шаг 1)

Дата: 2026-09-28. Прогоны не запускались: ниже только проверка инструментов, установки и хука.

## 1. Версии и закрепление хоста

| Что | Проверка | Итог |
|---|---|---|
| Spine Core | `arch-be --version` | **0.3.11** |
| Qwen Code | `qwen --version` | **0.24.6** (пин, авто-обновление выключено) |
| Решатель | `GET https://api.deepseek.com/v1/models` | `deepseek-flash` = **DeepSeek-V4.1-Flash** |
| Судья | локальный OpenAI-совместимый шлюз | **glm-5.3** (`z-ai/glm-5.3`), другое семейство |

Автообновление выключено в каждой ячейке: `home/.qwen/settings.json` →
`general.disableAutoUpdate = true`, `general.disableUpdateNag = true`.

## 2. Установка 12 ячеек факторной сетки

`install()` + `verify_install()` для каждой ячейки; список проблем пуст у всех 12.

| Условие | скиллов проекта | скиллов расш. | команд | MCP | хуки | verify_install |
|---|---|---|---|---|---|---|
| plain | 0 | 0 | 0 | — | — | ок |
| plain+spine | 66 | 0 | 0 | spine | — | ок |
| plain+spine-hook | 66 | 0 | 0 | spine | Stop | ок |
| openspec | 6 | 0 | 6 | — | — | ок |
| openspec+spine | 72 | 0 | 6 | spine | — | ок |
| openspec+spine-hook | 72 | 0 | 6 | spine | Stop | ок |
| bmad | 29 | 0 | 0 | — | — | ок |
| bmad+spine | 95 | 0 | 0 | spine | — | ок |
| bmad+spine-hook | 95 | 0 | 0 | spine | Stop | ок |
| superpowers | 0 | 15 | 0 | — | — | ок |
| superpowers+spine | 66 | 15 | 0 | spine | — | ок |
| superpowers+spine-hook | 66 | 15 | 0 | spine | Stop | ок |

Коллизий имён скиллов нет ни в одной связке.

### Находка F9 (новая, потребовала отклонения)

При порядке установки из руководства («сначала стек, потом Spine») комбинированные
ячейки с `openspec` и `bmad` **теряли 66 скиллов Spine**: `arch-be connect qwen`
печатает

> «`.qwen/skills` уже существует — скиллы НЕ раскладываются (чужую библиотеку не перетираем)»

и молча не устанавливает свою библиотеку. `verify_install` это поймал
(`project_skills: 6 < 72`). Исправление — **порядок установки обратный: сначала Spine,
потом стек**; после установки стека `settings.json` досливается (MCP Spine сохраняется),
хук ставится последним. Это зафиксировано в DEVIATIONS пререгистрации. Проверено:
66+6=72 (openspec) и 66+29=95 (bmad), `mcpServers.spine` на месте в обоих случаях.

## 3. Тест Stop-хука на незакоммиченной работе (критичный)

Хук v2: `git add -A -N; arch-be gate --route auto --base bench-baseline || exit 2`.

| Тест | Действие | Ожидание | Итог |
|---|---|---|---|
| 1 | правка `AD-005` в `ARCHITECTURE-SPINE.md` без дельты | exit 2 | **exit 2** («spine: гейт FAIL») |
| 2а | откат + `arch-be delta new preflight-delta` (скелет) | PASS или находки дельты | **exit 0**, `Итог: PASS` |
| 2б | правка `AD-005` внутри дельты, дельта объявляет изменение | exit 0 | **exit 0** |
| 3 | новый неотслеживаемый файл | виден в диффе | **виден**: `changes/preflight-delta/{DELTA.md,NEW.md}` |

Вывод: хук **видит незакоммиченную работу** (это и была цель исправления F2). Ячейки
`spine-hook` в таком виде осмысленны. Ячейка после теста возвращена к тегу
`bench-baseline` (`git reset --hard bench-baseline && git clean -fd`, дерево чистое).

## 4. Вызов хука в TUI и наличие `HOOK_MARK`

Проверяется на пилоте в ячейке `plain+spine-hook` (см. `results-v2/pilot.md`):
факт вызова хука — счётчик `hook_blocks` по журналам HOME ячейки, маркер
`spine: гейт FAIL`. Детектор конца хода в хуковых ячейках ждёт тишины 200 с
(таймаут хука 150 с + запас), чтобы не остановиться между ходом и хуком.

## 5. Форматы вывода `arch-be 0.3.11` (сверены на реальном выводе)

- провалы: `[FAIL] <составляющая> — <текст>`;
- пропуски: `[SKIP] <составляющая> — <причина>` → `gate_skips` даёт `['model_validate','trace_check']`;
- маршрут: строка `Маршрут: <Fast|Standard|Critical> …`;
- итог: `Итог: PASS|FAIL — …`.

## 6. `contamination()` находит искусственное обращение

Самопроверка (журнал с чтением `<SPINE_BANK>/src/rubric/judge.rs`):
`contamination()` вернул ровно этот путь; собственные `ws/` и `home/` в выдачу не попали.

## 7. Проверка вспомогательных метрик v2

| Функция | Вход | Выход |
|---|---|---|
| `gate_class` | exit 1 | `FAIL` |
| `gate_class` | exit 0, дельта есть | `PASS_DELTA` |
| `gate_class` | exit 0, дельта пуста, защищённые не тронуты | `PASS_UNTOUCHED` |
| `gate_skips` | вывод гейта | `['model_validate','trace_check']` |
| `modified_invariants` | AD-005 изменён, AD-009 добавлен | `modified=['AD-005'], added=['AD-009']` |

Готово: все шесть пунктов шага 1 пройдены.
