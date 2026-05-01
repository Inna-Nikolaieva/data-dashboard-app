from app.schemas.base_schemas import BaseSchema
from pydantic import Field


class DummyPostDTO(BaseSchema):
    title: str
    body: str
    user_id: int = Field(alias="userId")


class PostsResponse(BaseSchema):
    posts: list[DummyPostDTO]
    total: int
    skip: int
    limit: int
