# MCCP L1 Scenario-Based Hands-on Assessment

## Scenario: Orderly Sales Data Pipeline

You have joined the Orderly engineering team. Every day, the sales team provides a CSV file of orders. Your job is to validate and transform the data, store valid orders in SQLite, generate a sales report, package the app in Docker, and make sure the CI pipeline blocks broken code.

**This is a starter project, not a solution.** Some functions are TODOs and some files contain intentional bugs. Fix them yourself. Do not expect every test to pass at the beginning.

## Topics covered
1. Git/version control
2. Production-grade Python (functions, exceptions, logging, OOP, comprehensions, decorators/generators, pytest)
3. SQL (filtering, joins, aggregation, window functions, CTEs, indexes, query plans)
4. JSON/CSV/Parquet/Avro concepts and ETL/ELT
5. Linux CLI, permissions, environment variables, processes and logs
6. Docker and Docker Compose
7. Cloud infrastructure and least privilege (design exercise; no cloud account needed)
8. CI/CD and YAML
9. Debugging and troubleshooting
10. Documentation and communication

## Setup (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process Bypass` in that terminal, then activate again. You can also run tests using `py -m pytest -q`.

## Setup (Linux/macOS/Git Bash)
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

## Your mission
Work through `TASKS.md` in order. Use `data/orders.csv` as the source data. The test suite in `tests/` is your feedback. Add tests of your own. Do not put passwords, API keys, or real personal data into the repository.

## Useful commands
```bash
python -m pytest -q
python -m pytest tests/test_etl.py -q
python -m orderly.cli --input data/orders.csv --db data/orders.db --report output/report.json
```

The CLI command is expected to work after you complete the relevant tasks. It may fail before then.

## Submission checklist
- [ ] All tests pass
- [ ] Invalid rows are reported without crashing the whole import
- [ ] Running the import twice does not duplicate orders
- [ ] SQL report is correct
- [ ] Docker image builds and runs
- [ ] CI runs tests before packaging
- [ ] README and runbook are updated
- [ ] `git status` does not show generated databases, secrets, or virtual environments
