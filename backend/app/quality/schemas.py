from pydantic import BaseModel


class QualityRequest(BaseModel):
    text: str


class QualityResponse(BaseModel):
    text: str
