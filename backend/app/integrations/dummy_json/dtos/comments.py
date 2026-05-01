from app.schemas.base_schemas import BaseSchema
from pydantic import Field


class CommentUserDTO(BaseSchema):
    id: int


class DummyCommentDTO(BaseSchema):
    body: str
    post_id: int = Field(alias="postId")
    user: CommentUserDTO


class CommentsResponse(BaseSchema):
    comments: list[DummyCommentDTO]
    total: int
    skip: int
    limit: int
