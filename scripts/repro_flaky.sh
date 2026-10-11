#!/usr/bin/env bash
# Same command, same seed, three runs. The scores should be identical.
set -euo pipefail
for i in 1 2 3; do
  python3 -m evalkit run --data data/arith.jsonl --n 100 --seed 0 | tail -1
done
