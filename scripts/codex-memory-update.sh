#!/bin/bash
set -e

# Переходим в корень репозитория относительно расположения скрипта
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

DATE_HUMAN="$(date '+%Y-%m-%d %H:%M')"
RUN_FILE="memory/codex_runs/$(date '+%Y-%m-%d_%H-%M').md"

# Убедиться, что директории существуют
mkdir -p docs
mkdir -p memory/codex_runs

# 1) Обновляем docs/chat-memory.md
if [ ! -f docs/chat-memory.md ] && [ -f docs/CHAT_MEMORY.md ]; then
  mv docs/CHAT_MEMORY.md docs/chat-memory.md
fi

if [ ! -f docs/chat-memory.md ]; then
  cat <<EOF > docs/chat-memory.md
# SODMASTER — CHAT MEMORY

## ✅ Текущий статус проекта

(описать текущий статус здесь)

## 🧠 Лента обновлений
EOF
fi

cat <<EOF >> docs/chat-memory.md

## [$DATE_HUMAN] Codex Update

- Что делали:
- Какие файлы изменены:
- Что получилось:
- Текущее состояние:
- Следующий шаг:

EOF

# 2) Лог отдельного запуска Codex
cat <<EOF > "$RUN_FILE"
# Codex Run [$DATE_HUMAN]

## Цель
-

## Выполненные действия
-

## Результат
-

## Вывод
-

## Следующий шаг
-
EOF

# 3) Фиксируем изменения в git (без падения, если нет изменений)
git add docs/chat-memory.md memory/codex_runs || true
git commit -m "codex: auto memory update" || true
git push || true
