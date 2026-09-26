# AGENTS.md

This repository contains a small ML application that serves a California housing price model through a Streamlit frontend and a BentoML API. The app is designed to run locally with Docker Compose and includes observability services for tracing and metrics.

## Key files and directories

- [README.md](README.md): project overview and run instructions.
- [api/README.md](api/README.md): BentoML service documentation.
- [streamlit/app.py](streamlit/app.py): frontend that uploads CSV data and calls the prediction endpoint.
- [api/src/service.py](api/src/service.py): main API service, Pydantic input schema, model load, and prediction logic.
- [api/tests/api_test.py](api/tests/api_test.py): integration-style API test for the predict endpoint.
- [docker-compose.yml](docker-compose.yml): local orchestration for API, web, Prometheus, Grafana, Loki, Jaeger, and Alloy.
- [justfile](justfile): lint and formatting commands.

## Working conventions

- Prefer the repo’s existing toolchain over ad hoc scripts: Docker Compose for local services, pytest for the API test, and the `just` commands for lint/formatting.
- Keep the frontend and backend contract aligned. If the API input schema changes in [api/src/service.py](api/src/service.py), update the frontend form and any test payloads that rely on it.
- Environment variables live in `.env` and are required by the services at runtime (for example `API_PORT`, `API_HOST`, `ALLOY_HOST`, and `ALLOY_PORT`).
- The model API is a BentoML service named `svr_regressor`; the app expects a prediction endpoint at `/predict`.
- Keep changes small and targeted, especially around data validation and model-serving code.

## Useful commands

- Start the API: `docker compose up --build api`
- Start the web app: `docker compose up --build web`
- Run the API test: `pytest api/tests/api_test.py`
- Lint: `just lint`
- Format: `just format`

## Notes for agents

- Do not duplicate setup instructions that already exist in [README.md](README.md) or [api/README.md](api/README.md); link to them instead.
- Favor minimal, repo-specific guidance here. This file should help an agent understand architecture and local workflow quickly without re-reading the whole project.
- When troubleshooting runtime issues, check the Compose wiring first; most service dependencies and ports are defined in [docker-compose.yml](docker-compose.yml).
