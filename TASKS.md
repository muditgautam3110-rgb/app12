# Scenario Tasks — Do not skip straight to the end

## Stage 1 — Git and repository hygiene
1. Create a branch named `feature/etl-validation`.
2. Inspect `git status`, stage only source/test/documentation files, and make a meaningful commit.
3. Add suitable entries to `.gitignore` so `.venv/`, `*.db`, `__pycache__/`, `.env`, and test caches are not tracked.
4. Explain in your own notes why adding a secret to `.gitignore` does not erase it from Git history. State what you would do if a credential was committed.

## Stage 2 — Python ETL and validation
5. Complete `orderly/validators.py`: require a non-empty order ID, customer ID, valid ISO date (`YYYY-MM-DD`), and positive numeric amount.
6. Complete `orderly/etl.py`: read CSV safely, normalize fields, split valid and invalid rows, and record a useful reason for each rejected row.
7. Malformed rows must not crash the entire batch. Do not silently discard them.
8. Make the load idempotent: importing the same file twice must not duplicate an order.
9. Use logging instead of scattered `print()` calls. Never log secrets.
10. Complete the generator in `orderly/etl.py` so large CSV files can be processed one row at a time.
11. Add at least three pytest tests: malformed amount, missing ID, and duplicate order ID.

## Stage 3 — SQL reporting
12. Complete `sql/schema.sql` and `orderly/database.py` to create the required tables and constraints.
13. Complete `sql/reports.sql` to report total revenue and order count per customer.
14. Add a query for customers with no orders, and a query ranking each customer's orders by amount using a window function.
15. Add an index appropriate for date filtering. Explain when indexes help and why too many indexes can slow writes.
16. Use SQLite `EXPLAIN QUERY PLAN` to inspect one report query and write your observation in `docs/analysis.md`.

## Stage 4 — Data formats and quality
17. Implement JSON report output in `orderly/reporting.py`.
18. Explain in `docs/analysis.md` when CSV, JSON, Parquet, and Avro are appropriate. You do not need to install Parquet/Avro libraries for this task.
19. Ensure the CSV reader handles quoted fields correctly and reports invalid values.
20. Make the report deterministic so the same input yields the same report.

## Stage 5 — Linux and troubleshooting
21. Run the app from the command line and capture the error output when it fails.
22. Use `pwd`, `ls -la`, `grep`, `find`, `ps`, and `chmod` where relevant. Record the commands you used in `docs/analysis.md`.
23. Add a shell script `scripts/run_checks.sh` that exits non-zero if tests fail. Make it executable on Linux (`chmod +x scripts/run_checks.sh`).
24. Explain how you would inspect service logs and environment variables on a Linux host without printing secrets.

## Stage 6 — Docker
25. Fix `Dockerfile` so it installs dependencies and runs the CLI correctly.
26. Complete `compose.yaml` to mount input data read-only and persist output/database data in a volume or bind mount.
27. Build and run the container. Inspect logs and exit status if it stops.
28. Explain the difference between image and container, and why database/output data must persist outside the disposable container layer.

## Stage 7 — Cloud design (no cloud account required)
29. In `docs/cloud-design.md`, propose a safe deployment on Azure or AWS: compute, storage, monitoring, network exposure, backup, and budget alert.
30. Use least privilege: the app should only read its input location and write its output location. Explain why long-lived keys should not be hardcoded into code or images.
31. Include a rollback and recovery plan. Do not create real resources or include real credentials.

## Stage 8 — CI/CD
32. Fix `.github/workflows/ci.yml` so it is valid YAML and runs on pushes and pull requests.
33. CI must install dependencies, run tests, and only then build the Docker image. A failed test must fail the job.
34. Explain where repository secrets belong and why they should not be printed in logs.

## Stage 9 — Debugging and documentation
35. Diagnose the intentional bug in `orderly/etl.py` and the failing tests; identify the root cause before editing.
36. Improve error messages without exposing sensitive data.
37. Update `README.md` if setup or commands change.
38. Complete `docs/runbook.md` with symptoms, diagnosis, recovery, rollback, and verification.
39. In `docs/analysis.md`, record each bug, root cause, fix, and test used to verify it.

## Final challenge
40. Starting from a clean clone, follow your README exactly. Import the sample CSV twice, confirm no duplicates, inspect the JSON report, run tests, build/run Docker, and explain the deployment architecture in 3–5 minutes.
