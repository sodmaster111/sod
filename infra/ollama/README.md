# Ollama setup

This directory documents how to provision the local LLM runtime. The `docker-compose.yml` file
will start the official Ollama container and store its models in the shared `ollama-data` volume.

To add models, exec into the running container and pull them, for example:

```bash
docker compose -f infra/docker-compose.yml exec ollama ollama pull llama3
```
