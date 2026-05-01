from .base_schemas import BaseORMSchema, BaseSchema
from .comments_schemas import PublicCommentSchema
from .users_schemas import PublicUserSchema


class PublicPostSchema(BaseORMSchema):
    title: str
    body: str

    user: PublicUserSchema
    comments: list[PublicCommentSchema] = []


class BasePostSchema(BaseSchema):
    title: str
    body: str
    user_id: int


class UpdatePostSchema(BaseSchema):
    title: str | None = None
    body: str | None = None
