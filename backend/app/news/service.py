from app.agents.llm_client import LocalLLMClient
from app.agents.prompts import NEWS_INTERPRETER_SYSTEM_PROMPT, NEWS_WATCHER_SYSTEM_PROMPT


async def summarize_news(text: str) -> str:
    """Return a concise neutral summary of the given news text."""
    client = LocalLLMClient()
    user_prompt = (
        "Сделай нейтральное краткое резюме этой новости (5–7 предложений, только факты):\n\n"
        f"{text}"
    )
    return await client.generate(
        system_prompt=NEWS_WATCHER_SYSTEM_PROMPT,
        user_prompt=user_prompt,
    )


async def interpret_news_from_summary(summary: str) -> str:
    """Return a spiritual interpretation of the provided news summary."""
    client = LocalLLMClient()
    user_prompt = (
        "Вот краткое резюме новости. Дай духовную трактовку по правилам system-промпта:\n\n"
        f"{summary}"
    )
    return await client.generate(
        system_prompt=NEWS_INTERPRETER_SYSTEM_PROMPT,
        user_prompt=user_prompt,
    )
