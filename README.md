# SODMASTER Monorepo

SODMASTER is a local-first autonomous AI agency that runs entirely on self-hosted LLM runtimes
such as Ollama. This repository is organized as a monorepo with separate backend, web, and infra
folders to streamline development and deployment.

## Structure

- `backend/` — FastAPI service exposing health and agent chat endpoints backed by local models.
- `web/` — Next.js frontend shell prepared for integrating with the backend agents.
- `infra/` — Docker Compose stack for orchestrating the backend, web app, reverse proxy, and Ollama.

## Getting started

1. Build and start the stack:
   ```bash
   docker compose -f infra/docker-compose.yml up --build
   ```
2. Access the API at http://localhost:8000 and the web app at http://localhost:3000.
3. Pull a local model into Ollama (example):
   ```bash
   docker compose -f infra/docker-compose.yml exec ollama ollama pull llama3
   ```

## Philosophy

- **Local-only**: the agent stack is designed to run without cloud dependencies.
- **Composable**: backend, frontend, and infra remain decoupled but share conventions.
- **Extensible**: extend agent profiles, swap models, or customize the UI as needed.
