"""Models evalkit can run. Anything with a generate(prompt) -> str works."""

from __future__ import annotations

import re
from typing import Protocol


class Model(Protocol):
    name: str

    def generate(self, prompt: str) -> str: ...


class BaselineModel:
    """Offline baseline: solves addition and subtraction, guesses on everything else.

    Useful for checking the pipeline end to end without an API key.
    """

    name = "baseline"
    _expr = re.compile(r"(-?\d+)\s*([+\-*])\s*(-?\d+)")

    def generate(self, prompt: str) -> str:
        m = self._expr.search(prompt)
        if not m:
            return ""
        a, op, b = int(m.group(1)), m.group(2), int(m.group(3))
        if op == "+":
            return str(a + b)
        if op == "-":
            return str(a - b)
        # Multiplication is where the baseline falls over: it adds instead.
        return str(a + b)


MODELS: dict[str, type] = {
    "baseline": BaselineModel,
}


def get_model(name: str) -> Model:
    try:
        return MODELS[name]()
    except KeyError:
        known = ", ".join(sorted(MODELS))
        raise ValueError(f"unknown model {name!r} (known: {known})") from None
