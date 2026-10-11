"""Scoring."""

from __future__ import annotations

import random


def normalize(text: str) -> str:
    return " ".join(text.strip().lower().split()).rstrip(".")


def exact_match(prediction: str, answer: str) -> bool:
    return normalize(prediction) == normalize(answer)


def accuracy(correct: list[bool]) -> float:
    if not correct:
        return 0.0
    return sum(correct) / len(correct)


def bootstrap_ci(
    correct: list[bool], iterations: int = 1000, level: float = 0.95, seed: int = 0
) -> tuple[float, float]:
    """Percentile bootstrap confidence interval for accuracy."""
    if not correct:
        return (0.0, 0.0)
    rng = random.Random(seed)
    n = len(correct)
    means = sorted(accuracy([correct[rng.randrange(n)] for _ in range(n)]) for _ in range(iterations))
    lo = means[int((1 - level) / 2 * iterations)]
    hi = means[min(iterations - 1, int((1 + level) / 2 * iterations))]
    return (lo, hi)
