from app.schemas.base_schemas import BaseSchema


class DummyUserDTO(BaseSchema):
    username: str
    email: str
    password: str


class UsersResponse(BaseSchema):
    users: list[DummyUserDTO]
    total: int
    skip: int
    limit: int
