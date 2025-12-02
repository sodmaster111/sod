from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NewsTextInterpretRequest(BaseModel):
    text: str


class NewsTextInterpretResponse(BaseModel):
    summary: str
    spiritual_interpretation: str


class NewsListItem(BaseModel):
    id: int
    title: Optional[str]
    summary: str
    created_at: datetime


class NewsDetail(BaseModel):
    id: int
    url: Optional[str]
    title: Optional[str]
    summary: str
    spiritual: str
    clean: str
    telegram_post: str
    created_at: datetime
