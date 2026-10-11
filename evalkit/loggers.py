"""Send results somewhere other than stdout.

WIP: Weights & Biases logging. Table upload and failure samples still to do.
"""

from __future__ import annotations

from evalkit.runner import EvalResult


def log_wandb(result: EvalResult, project: str, run_name: str | None = None) -> None:
    try:
        import wandb
    except ImportError as e:
        raise RuntimeError("wandb logging needs `pip install wandb`") from e

    run = wandb.init(project=project, name=run_name or f"{result.model}-{result.task}", job_type="eval")
    run.log(
        {
            f"{result.task}/accuracy": result.accuracy,
            f"{result.task}/ci_low": result.ci[0],
            f"{result.task}/ci_high": result.ci[1],
            f"{result.task}/n": result.n,
        }
    )
    # TODO: log result.failures as a wandb.Table
    run.finish()
