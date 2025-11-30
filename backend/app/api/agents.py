from fastapi import APIRouter, HTTPException

from app.agents.base import AgentRequest, AgentResponse
from app.agents.llm_client import LocalLLMClient
from app.agents.profiles import get_agent_profile
from app.core.config import settings

router = APIRouter()


@router.post("/agents/generate", response_model=AgentResponse)
async def generate_for_agent(payload: AgentRequest) -> AgentResponse:
    profile = get_agent_profile(payload.agent_name)
    if profile is None:
        raise HTTPException(status_code=404, detail=f"Unknown agent: {payload.agent_name}")

    system_prompt = (
        f"You are {profile.name}. "
        f"{profile.role_description}\n"
        f"Your goals:\n"
        + "\n".join(f"- {g}" for g in profile.goals)
    )

    client = LocalLLMClient()
    text = await client.generate(system_prompt=system_prompt, user_prompt=payload.user_prompt)

    return AgentResponse(
        agent=profile.name,
        response=text,
        model=settings.LLM_MODEL_NAME,
    )
