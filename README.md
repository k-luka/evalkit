# evalkit

Small, boring model evals. Point it at a model and a benchmark, get a results table.

```bash
pip install -e ".[dev]"
evalkit run --data data/arith.jsonl --model baseline --n 100 --seed 0
```

```
| model    | task  | n   | accuracy | 95% CI         |
|----------|-------|-----|----------|----------------|
| baseline | arith | 100 | 0.610    | [0.510, 0.700] |
```

## Experiments

`data/arith_long.jsonl` asks the same arithmetic as word problems with extra distractor text, to see whether accuracy holds up as prompts get longer.

```bash
evalkit run --data data/arith_long.jsonl --n 100 --seed 0
```

## Layout

- `evalkit/datasets.py`: load JSONL benchmarks and subsample them
- `evalkit/models.py`: the `Model` interface and an offline baseline
- `evalkit/metrics.py`: exact match, accuracy, bootstrap confidence intervals
- `evalkit/runner.py`: runs a model over a dataset
- `evalkit/report.py`: renders results as a Markdown table
- `evalkit/cli.py`: the `evalkit` command

## Adding a model

Implement `Model.generate(prompt: str) -> str` and register it in `evalkit/models.py`.

## Tests

```bash
pytest
```
