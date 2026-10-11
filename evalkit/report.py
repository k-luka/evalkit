"""Render results."""

from __future__ import annotations

from evalkit.runner import EvalResult


def markdown_table(results: list[EvalResult]) -> str:
    rows = [
        ["model", "task", "n", "accuracy", "95% CI"],
    ]
    for r in results:
        rows.append([r.model, r.task, str(r.n), f"{r.accuracy:.3f}", f"[{r.ci[0]:.3f}, {r.ci[1]:.3f}]"])
    widths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]

    def line(cells: list[str]) -> str:
        return "| " + " | ".join(c.ljust(w) for c, w in zip(cells, widths)) + " |"

    out = [line(rows[0]), "|" + "|".join("-" * (w + 2) for w in widths) + "|"]
    out += [line(row) for row in rows[1:]]
    return "\n".join(out)
