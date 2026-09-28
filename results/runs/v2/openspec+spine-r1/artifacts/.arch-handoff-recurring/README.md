# Handoff-пакет дельты: рекуррентные C2B-списания СБП

Это пакет передачи **изменения** `add-sbp-recurring-payments` кодовому харнессу, а не переиздание принятого пакета разового C2B-приёма.

- Состав: `TASK.md`, `ARCHITECTURE.md` (epic-context), `CONSTRAINTS.yaml` (fitness), `RUBRIC.yaml` (рубрика приёмки), `MANIFEST.json`, `adr/` (ADR-008, ADR-009).
- Почему отдельный каталог: принятый `.arch-handoff/` относится к walking skeleton разового приёма и не должен перезаписываться. Гейт по умолчанию читает `.arch-handoff/CONSTRAINTS.yaml`.
- Как использовать при apply: слить правила из `CONSTRAINTS.yaml` в `.arch-handoff/CONSTRAINTS.yaml` либо перегенерировать пакет командой `arch-be handoff --repo . --task "<задача>" --route critical qwen-code` (флаг `--refresh-constraints` — только если правки архитектора не нужны).
- Предусловие старта: A3 (ратификация ADR-008/ADR-009 и AD-009..AD-011) и получение документации НСПК по подпискам.
