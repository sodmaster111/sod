from pydantic import BaseModel


class NewsTextInterpretRequest(BaseModel):
    text: str


class NewsTextInterpretResponse(BaseModel):
    summary: str
    spiritual_interpretation: str
