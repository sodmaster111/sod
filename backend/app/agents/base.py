from typing import List

from pydantic import BaseModel


class AgentProfile(BaseModel):
    name: str
    role_description: str
    goals: List[str]


class AgentRequest(BaseModel):
    agent_name: str
    user_prompt: str


class AgentResponse(BaseModel):
    agent: str
    response: str
    model: str
