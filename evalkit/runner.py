"""Run a model over a benchmark."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from evalkit.datasets import load_jsonl, subsample
from evalkit.metrics import accuracy, bootstrap_ci, exact_match
from evalkit.models import Model


@dataclass
class EvalResult:
    model: str
    task: str
    n: int
    accuracy: float
    ci: tuple[float, float]
    failures: list[dict] = field(default_factory=list)


def run_eval(model: Model, data: str | Path, n: int | None = None, seed: int = 0) -> EvalResult:
    examples = subsample(load_jsonl(data), n, seed=seed)
    correct = []
    failures = []
    for ex in examples:
        prediction = model.generate(ex.prompt)
        ok = exact_match(prediction, ex.answer)
        correct.append(ok)
        if not ok:
            failures.append({"id": ex.id, "prompt": ex.prompt, "expected": ex.answer, "got": prediction})
    return EvalResult(
        model=model.name,
        task=Path(data).stem,
        n=len(examples),
        accuracy=accuracy(correct),
        ci=bootstrap_ci(correct, seed=seed),
        failures=failures,
    )
