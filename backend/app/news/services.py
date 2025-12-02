from contextlib import contextmanager
from typing import Iterator, List, Optional

from app.agents.llm_client import LocalLLMClient
from app.news.schemas import NewsDetail, NewsListItem


async def summarize_news(text: str) -> str:
    """Суммирует текст новости, возвращая краткий пересказ."""
    client = LocalLLMClient()
    system_prompt = (
        "Ты — помощник, который кратко пересказывает новости. "
        "Сделай сжатое резюме новости в 2-3 предложениях на русском языке."
    )
    return await client.generate(system_prompt=system_prompt, user_prompt=text)


async def interpret_news_from_summary(summary: str) -> str:
    """Делает духовное толкование новости на основе краткого резюме."""
    client = LocalLLMClient()
    system_prompt = (
        "Ты — мудрый учитель, который даёт духовное и еврейское толкование событий. "
        "На основе краткого резюме новости предложи вдохновляющий вывод и урок."
    )
    user_prompt = (
        "Краткое содержание новости:\n"
        f"{summary}\n\n"
        "Дай духовное толкование и практический вывод."
    )
    return await client.generate(system_prompt=system_prompt, user_prompt=user_prompt)


@contextmanager
def get_session() -> Iterator[None]:
    """Return a dummy session placeholder.

    This placeholder allows API handlers to depend on a session provider even if the
    backing persistence layer is not yet implemented.
    """

    yield None


def list_news_posts(_session: None, limit: int) -> List[NewsListItem]:
    """Return a list of recent news posts (placeholder)."""

    return []


def get_news_post(_session: None, _post_id: int) -> Optional[NewsDetail]:
    """Return a single news post (placeholder)."""

    return None
