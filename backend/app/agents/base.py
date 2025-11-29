from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel, Field

from app.agents.llm_client import LocalLLMClient


class AgentRequest(BaseModel):
    prompt: str = Field(..., description="User prompt for the agent")
    context: dict[str, Any] | None = Field(default=None, description="Optional structured context")


class AgentResponse(BaseModel):
    reply: str = Field(..., description="Agent response text")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Debug or tracing metadata")


@dataclass
class AgentProfile:
    name: str
    system_prompt: str


class AgentService:
    def __init__(self, profile: AgentProfile, client: LocalLLMClient | None = None) -> None:
        self.profile = profile
        self.client = client or LocalLLMClient()

    def chat(self, request: AgentRequest) -> AgentResponse:
        """Send a prompt to the local LLM client using the profile's system prompt."""
        response_text, tokens = self.client.generate(
            system_prompt=self.profile.system_prompt,
            user_prompt=request.prompt,
            context=request.context or {},
        )
        return AgentResponse(reply=response_text, metadata={"tokens_used": tokens, "profile": self.profile.name})
