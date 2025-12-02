from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class NewsPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: Optional[str] = Field(default=None, index=True)
    title: Optional[str] = Field(default=None)
    summary: str
    spiritual: str
    clean: str
    telegram_post: str
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
