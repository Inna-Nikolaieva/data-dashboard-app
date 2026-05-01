from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user_model import UserModel
from .base_repository import BaseRepository


class UserRepository:
    model = UserModel

    def __init__(self, session: AsyncSession):
        self.session = session
        self.base = BaseRepository(session, self.model)
