from fastapi import APIRouter

from app.quality.schemas import QualityRequest, QualityResponse
from app.quality.service import clean_text

router = APIRouter()


@router.post("/quality/clean", response_model=QualityResponse)
async def clean_quality(payload: QualityRequest) -> QualityResponse:
    cleaned = await clean_text(payload.text)
    return QualityResponse(text=cleaned)
