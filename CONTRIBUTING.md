# Contributing to MARBLE

## Set up

Follow the installation steps in the [README](README.md). MARBLE requires Python 3.9, 3.10 or 3.11.

## Make a change

1. Create a branch from `main`: `git checkout -b feature/feature-name`.
2. Make your change. Add or update tests in `tests/` for behavior you change.
3. If you add a third-party import, add the package to `pyproject.toml` and run `poetry lock`.

## Check your change

Run these before you open a pull request:

```bash
poetry run pytest
poetry run mypy --config-file pyproject.toml .
pre-commit run --all-files
```

Tests must not need API keys. Mock LLM and embedding calls, as `tests/test_long_term_memory.py` does. Tests that call a real provider must skip when its key is not set.

## Open a pull request

Open the pull request against `main`. Check that the GitHub Actions run passes. If it fails, fix the errors and push again.
