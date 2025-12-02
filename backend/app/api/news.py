from typing import List

from fastapi import APIRouter, HTTPException

from app.news.schemas import NewsDetail, NewsListItem, NewsTextInterpretRequest, NewsTextInterpretResponse
from app.news.services import (
    get_news_post,
    get_session,
    interpret_news_from_summary,
    list_news_posts,
    summarize_news,
)

router = APIRouter()


@router.get("/news/list", response_model=List[NewsListItem])
async def news_list(limit: int = 20) -> List[NewsListItem]:
    with get_session() as session:
        return list_news_posts(session, limit)


@router.get("/news/{post_id}", response_model=NewsDetail)
async def news_detail(post_id: int) -> NewsDetail:
    with get_session() as session:
        news_post = get_news_post(session, post_id)

    if news_post is None:
        raise HTTPException(status_code=404, detail="News post not found")

    return news_post


@router.post("/news/interpret-from-text", response_model=NewsTextInterpretResponse)
async def interpret_from_text(payload: NewsTextInterpretRequest) -> NewsTextInterpretResponse:
    text = payload.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text must not be empty")

    try:
        summary = await summarize_news(text)
    except HTTPException:
        raise
    except Exception as exc:  # pragma: no cover - defensive logging placeholder
        raise HTTPException(status_code=500, detail=f"Failed to summarize news: {exc}") from exc

    try:
        interpretation = await interpret_news_from_summary(summary)
    except HTTPException:
        raise
    except Exception as exc:  # pragma: no cover - defensive logging placeholder
        raise HTTPException(status_code=500, detail=f"Failed to interpret news: {exc}") from exc

    return NewsTextInterpretResponse(summary=summary, spiritual_interpretation=interpretation)
