from __future__ import annotations

import re
from contextlib import contextmanager
from typing import Iterator, Optional

import requests
from sqlmodel import Session

from app.core.database import get_session
from app.news.repository import create_news_post


def _extract_plain_text(html: str) -> str:
    """Very lightweight HTML-to-text conversion for article bodies."""
    # Remove script and style content
    html = re.sub(r"<script.*?>.*?</script>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style.*?>.*?</style>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    # Strip remaining tags
    text = re.sub(r"<[^>]+>", " ", html)
    return " ".join(text.split())


def _prepare_news_payload(text: str) -> tuple[str, str, str, str]:
    """Prepare summary, spiritual interpretation, cleaned text, and telegram-ready post."""
    clean = " ".join(text.split())
    summary = clean[:500] if len(clean) > 500 else clean
    spiritual = f"Духовное толкование: {summary}"
    telegram_post = summary[:4000]
    return summary, spiritual, clean, telegram_post


@contextmanager
def _session_scope() -> Iterator[Session]:
    """Yield a database session using the shared get_session helper."""
    with get_session() as session:
        yield session


def process_news_text(text: str) -> dict:
    """Process raw news text, persist results, and return saved post details with id."""

    summary, spiritual, clean, telegram_post = _prepare_news_payload(text)
    with _session_scope() as session:
        post = create_news_post(
            session,
            url=None,
            title=None,
            summary=summary,
            spiritual=spiritual,
            clean=clean,
            telegram_post=telegram_post,
        )

    return {
        "id": post.id,
        "url": None,
        "title": None,
        "summary": summary,
        "spiritual": spiritual,
        "clean": clean,
        "telegram_post": telegram_post,
    }


def process_news_url(url: str) -> dict:
    """Fetch news by URL, persist processed results, and return saved post details with id."""

    response = requests.get(url, timeout=15)
    response.raise_for_status()
    html = response.text

    title_match = re.search(r"<title>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
    title: Optional[str] = title_match.group(1).strip() if title_match else None
    text = _extract_plain_text(html)

    summary, spiritual, clean, telegram_post = _prepare_news_payload(text)
    with _session_scope() as session:
        post = create_news_post(
            session,
            url=url,
            title=title,
            summary=summary,
            spiritual=spiritual,
            clean=clean,
            telegram_post=telegram_post,
        )

    return {
        "id": post.id,
        "url": url,
        "title": title,
        "summary": summary,
        "spiritual": spiritual,
        "clean": clean,
        "telegram_post": telegram_post,
    }
