from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = Field(default="SODMASTER API")
    default_model: str = Field(default="llama3")
    ollama_bin: str = Field(default="ollama")
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8000)

    class Config:
        env_prefix = "SOD_"


settings = Settings()
