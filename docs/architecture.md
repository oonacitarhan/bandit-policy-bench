# Architecture

Policy randomness and reward randomness use separate seeded generators. Thompson sampling uses independent Beta(1,1) priors and Bernoulli updates. Repeated trials summarize pseudo-regret, reward, standard error, and an approximate normal interval.

## Data flow

- `banditbench/core.py` — algorithm primitives.
- `banditbench/features.py` — experiment and analysis APIs.
- `banditbench/cli.py` — argument parsing and JSON output.
- `examples/` — small reproducible inputs.
- `tests/` — API, numerical, and CLI checks.
- `benchmarks/run.py` — timed representative workload.

## Limits

Only stationary Bernoulli arms are modeled. Normal intervals are descriptive approximations, especially with few trials. Pseudo-regret uses known arm means, which are available to the evaluator but not the policies.
