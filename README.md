# Bandit Policy Bench

Compare epsilon-greedy, UCB1 and Thompson sampling with repeated seeded trials and uncertainty summaries.

**Python** · Reusable core · CLI examples · Regression checks · Reproducible benchmark

> **Provenance:** created with AI assistance on **2026-11-01**.
> All commit author and committer dates are synthetic and distributed across
> November 2024–October 2026. They do not establish work on those dates.

## Quick start

```sh
python3 -m banditbench examples/bernoulli.json --trials 20 --steps 2000
```

## Repository map

- `banditbench/core.py` — algorithm primitives.
- `banditbench/features.py` — experiment and analysis APIs.
- `banditbench/cli.py` — argument parsing and JSON output.
- `examples/` — small reproducible inputs.
- `tests/` — API, numerical, and CLI checks.
- `benchmarks/run.py` — timed representative workload.

## How it works

Policy randomness and reward randomness use separate seeded generators. Thompson sampling uses independent Beta(1,1) priors and Bernoulli updates. Repeated trials summarize pseudo-regret, reward, standard error, and an approximate normal interval.

## Verification

```sh
sh scripts/check.sh
```

Seven test groups plus the original reference Python checks exercise reference cases, invalid inputs, and relevant invariants.
The complete local run is in [docs/verification.txt](docs/verification.txt).
The [checks workflow](.github/workflows/check.yml) executes the same source checks.

## Boundaries

Only stationary Bernoulli arms are modeled. Normal intervals are descriptive approximations, especially with few trials. Pseudo-regret uses known arm means, which are available to the evaluator but not the policies.

See [architecture](docs/architecture.md), [usage](docs/usage.md),
[release notes](CHANGELOG.md), and [provenance](PROVENANCE.json).

## License

MIT — [LICENSE](LICENSE).
