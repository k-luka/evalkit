"""Load benchmarks and pick the examples a run is scored on."""

from __future__ import annotations

import json
import random
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Example:
    id: str
    prompt: str
    answer: str


def load_jsonl(path: str | Path) -> list[Example]:
    """Read a benchmark file with one {"id", "prompt", "answer"} object per line."""
    examples = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            examples.append(Example(id=str(row["id"]), prompt=row["prompt"], answer=str(row["answer"])))
    return examples


def subsample(examples: list[Example], n: int | None, seed: int = 0) -> list[Example]:
    """Pick n examples to evaluate on. Returns everything when n is None or too large."""
    if n is None or n >= len(examples):
        return list(examples)
    rng = random.Random()
    picked = list(examples)
    rng.shuffle(picked)
    return picked[:n]
