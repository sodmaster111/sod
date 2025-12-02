from fastapi import FastAPI

from app.api import agents, health, news, pipeline, publisher, quality
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)


@app.get("/")
async def read_root():
    return {"status": "SODMASTER AI Agency is online"}


# все API под /api
app.include_router(health.router, prefix="/api")
app.include_router(agents.router, prefix="/api")
app.include_router(news.router, prefix="/api")
app.include_router(quality.router, prefix="/api")
app.include_router(publisher.router, prefix="/api")
app.include_router(pipeline.router, prefix="/api")
