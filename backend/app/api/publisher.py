from fastapi import APIRouter

from app.publisher.schemas import PublishFormatRequest, PublishFormatResponse
from app.publisher.service import format_for_telegram

router = APIRouter()


@router.post("/publisher/format-telegram", response_model=PublishFormatResponse)
async def format_telegram(payload: PublishFormatRequest) -> PublishFormatResponse:
    formatted_text = await format_for_telegram(payload.text)
    return PublishFormatResponse(text=formatted_text)
