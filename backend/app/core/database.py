from contextlib import contextmanager
from functools import lru_cache
from typing import Iterator

from pydantic import Field
from pydantic_settings import BaseSettings
from sqlmodel import Session, SQLModel, create_engine


class Settings(BaseSettings):
    PROJECT_NAME: str = Field("SODMASTER AI Agency", env="PROJECT_NAME")
    API_V1_STR: str = Field("/api", env="API_V1_STR")
    LLM_API_BASE: str = Field("http://ollama:11434", env="LLM_API_BASE")
    LLM_MODEL_NAME: str = Field("llama3", env="LLM_MODEL_NAME")

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()

DATABASE_URL = "sqlite:///./sod.db"
engine = create_engine(DATABASE_URL, echo=False)


def init_db() -> None:
    """Create database tables if they do not yet exist."""
    SQLModel.metadata.create_all(engine)


@contextmanager
def get_session() -> Iterator[Session]:
    """Provide a SQLModel session, ensuring tables exist before use."""
    init_db()
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
