from fastapi import APIRouter, Depends

from app.agents.base import AgentRequest, AgentResponse, AgentService
from app.agents.profiles import get_default_profile

router = APIRouter(prefix="/agents", tags=["agents"])


def get_agent_service() -> AgentService:
    """Dependency that provides the agent service with the default profile."""
    profile = get_default_profile()
    return AgentService(profile=profile)


@router.post("/chat", response_model=AgentResponse, summary="Chat with the local agent")
def chat(request: AgentRequest, service: AgentService = Depends(get_agent_service)) -> AgentResponse:
    """Chat endpoint that relays prompts to the local LLM-backed agent."""
    return service.chat(request)
