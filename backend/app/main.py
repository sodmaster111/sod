from fastapi import FastAPI

from app.api import agents, health
from app.core.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(health.router)
app.include_router(agents.router)


@app.get("/", tags=["root"], summary="Root description")
def read_root() -> dict[str, str]:
    """Provide a short welcome message."""
    return {"message": "SODMASTER backend is running"}
