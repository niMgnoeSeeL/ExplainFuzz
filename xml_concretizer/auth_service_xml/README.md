Small example project for ExplainFuzz evaluation.

- `app/` contains a small request processor that reads XML requests.
- `config/` contains service configuration.
- `data/` contains benign data and a safe `resources/` folder (with a fake secret).
- `fuzzing/` contains the `static_checker.py` and a `harness.py` that runs inputs safely.
- `tools/` contains `extract_pools.py`.

**SAFETY**: Attack files / payloads are included for testing. Always run the harness in an isolated environment (container/VM).
