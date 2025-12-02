from fastapi import FastAPI

from app.api import agents, health, news, publisher, quality, texts
from app.core.database import init_db
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)


@app.on_event("startup")
async def on_startup():
    init_db()


@app.get("/")
async def read_root():
    return {"status": "SODMASTER AI Agency is online"}


# все API под /api
app.include_router(health.router, prefix="/api")
app.include_router(agents.router, prefix="/api")
app.include_router(news.router, prefix="/api")
app.include_router(quality.router, prefix="/api")
app.include_router(publisher.router, prefix="/api")
app.include_router(news.router, prefix="/api")
app.include_router(texts.router, prefix="/api")
