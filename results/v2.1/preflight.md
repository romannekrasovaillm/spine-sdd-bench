# Preflight v2.1 — преднастройка файловой песочницы

Дата: 2026-09-29. Проверка выполнена **до** первого вызова модели-решателя v2.1,
внутри той же среды, в которой будет работать агент (контейнер `bench-agent:1`).

## 1. Чем изолируем

Ревью (П2) предлагало bubblewrap. В этой среде он недоступен:

```
$ bwrap --dev /dev --proc /proc ... true
bwrap: setting up uid map: Permission denied
$ sysctl kernel.apparmor_restrict_unprivileged_userns
kernel.apparmor_restrict_unprivileged_userns = 1
```

Прав на изменение sysctl нет (`sudo` требует пароль), поэтому непривилегированные
пространства имён закрыты. Использован **Docker** — изоляция строже, чем у bwrap:
контейнер видит только смонтированные каталоги, реальный `$HOME` оператора в него
не попадает вообще (в bwrap его пришлось бы скрывать точечно).

Образ `bench-agent:1` = `debian:bookworm-slim` + `git`, `ca-certificates`, `ripgrep`, `procps`.
Node берётся из хостовой установки, смонтированной только для чтения.

Монтируется ровно три вещи:

| Хост | Контейнер | Режим |
|---|---|---|
| `runs-v2.1/cells/<токен>/ws` | `/home/architect/project` | rw |
| `runs-v2.1/cells/<токен>/home` | `/home/architect` | rw |
| `…/cells/<токен>/hooklog` | `/var/log/archgate` | rw (только хуковые ячейки) |
| `arch-be` | `/usr/local/bin/arch-be` | ro (только ячейки со Spine) |

## 2. Чек-лист ревью (§5, шаг 1) — результаты

| Проверка | Ожидание | Получено |
|---|---|---|
| `pwd` | `/home/architect/project` | **`/home/architect/project`** |
| `ls /home` | только `architect` | **только `architect`** |
| `ls ~` | только `project` | **только `project`** |
| `ls ~/.arch-harness` | нет такого файла | **No such file or directory** |
| `ls /home/roman` | нет такого файла | **No such file or directory** |
| `command -v arch-be` в контроле | пусто | **NO_ARCH_BE** |
| `qwen mcp list` в контроле | без `spine` | **No MCP servers configured** |
| `env` | без `LIVE_*`, `JUDGE_*`, `SPINE_BANK`, `BENCH_*` | **NO_BENCH_ENV** |
| `git log --oneline` | только нейтральные сообщения | **`Рабочее окружение`, `Принятое решение: импорт`** |
| `git tag` | только `accepted` | **`accepted`** |
| `qwen --version` в песочнице | 0.24.6 | **0.24.6** |

## 3. Что ещё исправлено в харнессе (П1–П7)

| № | Находка | Что сделано |
|---|---|---|
| П1 | Граница AD-блока | `harness_fixes.ad_blocks` + `modified_invariants` + `declared_modified`; данные v2 пересчитаны (`apply_corrections_v2.py`) |
| П2 | Агент видел реальный `$HOME`, харнесс, соседей, мета-файлы | Docker-песочница; мета-файлы ячейки в контейнер не монтируются вообще |
| П3 | Имя условия в `git log` и в теге | Нейтральные сообщения коммитов, метка `accepted` |
| П4 | Неинформативная проверка слепоты | `blindness_balanced`: сбалансированная выборка, вопрос ДА/НЕТ, сбалансированная точность |
| П5 | Детектор утечек шумит | `classify_access` с категориями вместо «любого абсолютного пути» |
| П6 | Отказ MCP в сессии не виден | `probe_argv`/`probe_verdict` до агента; `session_saw_spine_tools` после |
| П7 | `hook_blocks` засоряется текстом | Хук пишет срабатывания в `/var/log/archgate/hook.log`; счётчик читается оттуда |

## 4. Тест Stop-хука

Хук в v2.1 не менялся по механике (база — нейтральная метка `accepted`, `git add -A -N`),
кроме счётчика (П7). Проверка v2 остаётся в силе: правка AD-005 без дельты → `exit 2`,
внутри корректной дельты → `exit 0`, новый файл виден в диффе
([`03-preflight.md`](03-preflight.md), раздел 3). Прогонов со Spine в волне v2.1 нет,
поэтому хук в этой волне не исполняется; он проверяется при расширении волны.

## 5. Готовность

Песочница готова: все пункты чек-листа пройдены. Контрольные ячейки в ней видят
только свой проект и свой `HOME` — ни материалов Spine, ни харнесса, ни имени условия.
