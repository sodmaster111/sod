from fastapi import APIRouter
from app.agents.llm_client import LocalLLMClient
from app.core.config import settings

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/health/llm")
async def health_llm():
    client = LocalLLMClient(
        base_url=settings.LLM_API_BASE,
        model=settings.LLM_MODEL_NAME,
    )
    try:
        text = await client.generate(
            system_prompt="You are a health-check probe.",
            user_prompt="Reply with OK.",
        )
        return {"llm": "ok", "sample": text[:200]}
    except Exception as e:
        return {"llm": "error", "detail": str(e)}
