from fastapi import APIRouter

from app.pipeline.schemas import NewsPipelineRequest, NewsPipelineResponse
from app.pipeline.service import run_news_to_telegram_pipeline

router = APIRouter()


@router.post("/pipeline/news-to-telegram", response_model=NewsPipelineResponse)
async def news_to_telegram(payload: NewsPipelineRequest) -> NewsPipelineResponse:
    pipeline_result = await run_news_to_telegram_pipeline(payload.text)
    return NewsPipelineResponse(
        id=pipeline_result["id"],
        text=pipeline_result["text"],
    )
