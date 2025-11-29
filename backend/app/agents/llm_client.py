from __future__ import annotations

import subprocess
from typing import Any

from app.core.config import settings


class LocalLLMClient:
    """Minimal client wrapper for running prompts against a local LLM binary (e.g., Ollama)."""

    def __init__(self, model: str | None = None) -> None:
        self.model = model or settings.default_model

    def generate(self, system_prompt: str, user_prompt: str, context: dict[str, Any]) -> tuple[str, int]:
        prompt = f"[System]\n{system_prompt}\n[User]\n{user_prompt}"
        _ = context  # placeholder for future contextualization
        command = [settings.ollama_bin, "run", self.model, prompt]

        try:
            completed = subprocess.run(command, check=True, capture_output=True, text=True)
            output = completed.stdout.strip()
        except FileNotFoundError:
            output = "(ollama binary not found - ensure local LLM runtime is installed)"
        except subprocess.CalledProcessError as exc:  # noqa: PERF203
            output = exc.stderr or "(failed to run local LLM)"

        tokens_used = len(prompt.split()) + len(output.split())
        return output, tokens_used
