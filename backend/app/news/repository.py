from typing import List, Optional

from sqlmodel import Session, select

from app.news.models import NewsPost


def create_news_post(
    session: Session,
    *,
    url: str | None,
    title: str | None,
    summary: str,
    spiritual: str,
    clean: str,
    telegram_post: str,
) -> NewsPost:
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


def list_news_posts(session: Session, limit: int = 20) -> List[NewsPost]:
    stmt = select(NewsPost).order_by(NewsPost.created_at.desc()).limit(limit)
    return list(session.exec(stmt))


def get_news_post(session: Session, post_id: int) -> Optional[NewsPost]:
    return session.get(NewsPost, post_id)
