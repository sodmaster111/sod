#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

summary=${1:-"Automated codex memory update"}
timestamp="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
branch="$(git rev-parse --abbrev-ref HEAD)"
head_commit="$(git rev-parse --short HEAD)"

memory_dir="$repo_root/memory/codex_runs"
log_file="$memory_dir/run-${timestamp}.log"
chat_memory="$repo_root/docs/chat-memory.md"

mkdir -p "$memory_dir"

if [[ ! -f "$chat_memory" ]]; then
  mkdir -p "$(dirname "$chat_memory")"
  {
    echo "# Codex memory log"
    echo
    echo "This file records Codex assistant run metadata."
    echo
  } > "$chat_memory"
fi

{
  echo "timestamp: $timestamp"
  echo "branch: $branch"
  echo "head: $head_commit"
  echo "summary: $summary"
  echo
  git status -sb
} > "$log_file"

log_rel=${log_file#"$repo_root/"}

cat <<EOF_LOG >> "$chat_memory"
## $timestamp
- Branch: $branch
- Commit: $head_commit
- Summary: $summary
- Log: $log_rel

EOF_LOG

git add "$chat_memory" "$log_file"

if git diff --cached --quiet; then
  echo "No updates to commit." >&2
else
  git commit -m "chore: codex memory update $timestamp"
fi

if git remote | grep -q .; then
  git push
else
  echo "No git remote configured; skipping push." >&2
fi
