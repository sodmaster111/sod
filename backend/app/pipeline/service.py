import hashlib
from typing import Dict

from app.news.services import interpret_news_from_summary, summarize_news
from app.publisher.service import format_for_telegram
from app.quality.service import clean_text


async def run_news_to_telegram_pipeline(text: str) -> Dict[str, object]:
    """Построить телеграм-пост по тексту новости."""

    summary = await summarize_news(text)
    interpretation = await interpret_news_from_summary(summary)
    cleaned_text = await clean_text(interpretation)
    telegram_text = await format_for_telegram(cleaned_text)

    digest = hashlib.sha256(telegram_text.encode("utf-8")).hexdigest()
    post_id = int(digest[:8], 16)

    return {"id": post_id, "text": telegram_text}
