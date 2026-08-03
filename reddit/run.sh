#!/bin/bash
# Wrapper for scheduled runs: fixes the working directory, appends to a log,
# and trims the log so it cannot grow without bound.
set -uo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG="$DIR/sync.log"
PYTHON="${PYTHON:-python3}"

{
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') ==="
  "$PYTHON" "$DIR/sync.py" "$@"
  echo "exit: $?"
  echo
} >>"$LOG" 2>&1

# Keep the last ~2000 lines only.
if [ "$(wc -l <"$LOG")" -gt 2000 ]; then
  tail -n 2000 "$LOG" >"$LOG.tmp" && mv "$LOG.tmp" "$LOG"
fi
