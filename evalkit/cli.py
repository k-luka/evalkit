"""The evalkit command."""

from __future__ import annotations

import argparse
import json

from evalkit.models import get_model
from evalkit.report import markdown_table
from evalkit.runner import run_eval


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="evalkit")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="evaluate a model on a benchmark")
    run.add_argument("--data", required=True, help="path to a JSONL benchmark")
    run.add_argument("--model", default="baseline")
    run.add_argument("--n", type=int, default=None, help="number of examples (default: all)")
    run.add_argument("--seed", type=int, default=0)
    run.add_argument("--failures", help="write failed examples to this JSON file")

    args = parser.parse_args(argv)
    result = run_eval(get_model(args.model), args.data, n=args.n, seed=args.seed)
    print(markdown_table([result]))
    if args.failures:
        with open(args.failures, "w") as f:
            json.dump(result.failures, f, indent=2)


if __name__ == "__main__":
    main()
