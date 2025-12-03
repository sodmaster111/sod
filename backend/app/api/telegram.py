from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.agents.base import AgentResponse
from app.agents.llm_client import LocalLLMClient
from app.agents.profiles import get_agent_profile
from app.integrations.telegram import TelegramClient
from app.core.config import settings
from app.utils.jewish_calendar import is_no_send_time

router = APIRouter()


class TelegramSendRequest(BaseModel):
    text: str
    parse_mode: str | None = "HTML"


class AgentBroadcastRequest(BaseModel):
    agent_name: str
    user_prompt: str
    parse_mode: str | None = "HTML"
    preview_only: bool = False


@router.post("/telegram/send")
async def send_telegram_message(payload: TelegramSendRequest):
    try:
        client = TelegramClient()
        result = await client.send_message(text=payload.text, parse_mode=payload.parse_mode)
        return {"ok": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/telegram/agent-broadcast", response_model=AgentResponse)
async def agent_broadcast(payload: AgentBroadcastRequest) -> AgentResponse:
    profile = get_agent_profile(payload.agent_name)
    if profile is None:
        raise HTTPException(status_code=404, detail=f"Неизвестный агент: {payload.agent_name}")

    system_prompt = (
        f"Ты — {profile.name}. "
        f"{profile.role_description}\n"
        f"Твои цели:\n" + "\n".join(f"- {g}" for g in profile.goals)
    )

    client = LocalLLMClient()
    text = await client.generate(system_prompt=system_prompt, user_prompt=payload.user_prompt)

    # если preview_only = False — отправляем в Telegram
    if not payload.preview_only:
        now = datetime.now(timezone.utc)
        if is_no_send_time(now):
            raise HTTPException(status_code=403, detail="Сейчас нельзя отправлять сообщения (Шаббат или Йом-Тов)")
        try:
            tg = TelegramClient()
            await tg.send_message(text=text, parse_mode=payload.parse_mode)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Ошибка отправки в Telegram: {e}")

    return AgentResponse(
        agent=profile.name,
        response=text,
        model=settings.LLM_MODEL_NAME,
    )
