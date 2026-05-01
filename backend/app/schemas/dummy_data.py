from app.schemas.base_schemas import BaseSchema


class ImportDummyDataResponseSchema(BaseSchema):
    status: str
    users: int
    posts: int
    comments: int
