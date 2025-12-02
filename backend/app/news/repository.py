from typing import Optional

from sqlmodel import Field, Session, SQLModel


class NewsPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: Optional[str] = Field(default=None, index=True)
    title: Optional[str] = None
    summary: str
    spiritual: str
    clean: str
    telegram_post: str


def create_news_post(
    session: Session,
    *,
    url: Optional[str],
    title: Optional[str],
    summary: str,
    spiritual: str,
    clean: str,
    telegram_post: str,
) -> NewsPost:
    """Persist a news post and return the saved model."""

    post = NewsPost(
        url=url,
        title=title,
        summary=summary,
        spiritual=spiritual,
        clean=clean,
        telegram_post=telegram_post,
    )
    session.add(post)
    session.commit()
    session.refresh(post)
    return post
