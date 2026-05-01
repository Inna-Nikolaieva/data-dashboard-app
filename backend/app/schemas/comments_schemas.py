from .base_schemas import BaseORMSchema, BaseSchema
from .users_schemas import PublicUserSchema


class PublicCommentSchema(BaseORMSchema):
    body: str
    user: PublicUserSchema


class BaseCommentSchema(BaseSchema):
    body: str
    post_id: int
    user_id: int


class UpdateCommentSchema(BaseSchema):
    body: str | None = None
