from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


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
