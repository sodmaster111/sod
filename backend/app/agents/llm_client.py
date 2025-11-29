from typing import Any, Dict, List, Optional

import httpx

from app.core.config import settings


class LocalLLMClient:
    """
    Клиент для локального LLM-сервиса (например, Ollama).
    По умолчанию использует настройки из app.core.config.settings.
    """

    def __init__(
        self,
        base_url: Optional[str] = None,
        model: Optional[str] = None,
        timeout: float = 60.0,
    ) -> None:
        self.base_url = base_url or settings.LLM_API_BASE
        self.model = model or settings.LLM_MODEL_NAME
        self.timeout = timeout

    async def generate(self, system_prompt: str, user_prompt: str) -> str:
        """
        Отправляет запрос в локальный LLM и возвращает текст ответа.
        Ориентируемся на формат Ollama /api/chat, но делаем парсер максимально толерантным.
        """
        payload: Dict[str, Any] = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }

        async with httpx.AsyncClient(
            base_url=self.base_url,
            timeout=self.timeout,
        ) as client:
            # Попытка использовать endpoint Ollama /api/chat
            response = await client.post("/api/chat", json=payload)
            response.raise_for_status()
            data = response.json()

        # Попытка распарсить ответ Ollama (или OpenAI-подобный)
        # 1) Формат Ollama chat:
        #    {"message": {"role": "...", "content": "..."}, ...}
        if isinstance(data, dict):
            message = data.get("message")
            if isinstance(message, dict):
                content = message.get("content")
                if isinstance(content, str):
                    return content

            # 2) OpenAI-подобный формат:
            #    {"choices": [{"message": {"content": "..."}}, ...]}
            choices: Optional[List[Any]] = data.get("choices")  # type: ignore[arg-type]
            if isinstance(choices, list) and choices:
                first = choices[0]
                if isinstance(first, dict):
                    msg = first.get("message")
                    if isinstance(msg, dict):
                        content = msg.get("content")
                        if isinstance(content, str):
                            return content

            # 3) Если есть просто "content"
            content = data.get("content")
            if isinstance(content, str):
                return content

        # Если не смогли распарсить, вернём строковое представление JSON для отладки
        return str(data)
