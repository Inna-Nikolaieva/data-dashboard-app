from pydantic import EmailStr

from .base_schemas import BaseORMSchema


class PublicUserSchema(BaseORMSchema):
    username: str | None = None
    email: EmailStr
