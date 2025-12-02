from fastapi import APIRouter, HTTPException

from app.news.schemas import NewsTextInterpretRequest, NewsTextInterpretResponse
from app.news.services import interpret_news_from_summary, summarize_news

router = APIRouter()


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
