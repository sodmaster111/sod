from pydantic import BaseModel


class NewsPipelineRequest(BaseModel):
    text: str


class NewsPipelineResponse(BaseModel):
    id: int
    text: str
