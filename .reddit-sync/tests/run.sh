#!/bin/bash
# Run the whole suite. No credentials or network needed — test_http.py serves a
# fake Reddit on localhost.
set -uo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fail=0
for t in test_render test_api test_http; do
  echo "───── $t ─────"
  python3 "$DIR/$t.py" || fail=1
done
[ $fail -eq 0 ] && echo -e "\n✅ all suites passed" || echo -e "\n❌ failures above"
exit $fail
