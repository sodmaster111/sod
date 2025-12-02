from pydantic import BaseModel


class PublishFormatRequest(BaseModel):
    text: str


class PublishFormatResponse(BaseModel):
    text: str
