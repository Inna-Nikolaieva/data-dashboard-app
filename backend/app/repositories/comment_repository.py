from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.comment_model import CommentModel
from sqlalchemy.orm import selectinload

from .base_repository import BaseRepository


class CommentRepository:
    model = CommentModel

    def __init__(self, session: AsyncSession):
        self.session = session
        self.base = BaseRepository(session, self.model)

    async def get_comment_by_id_with_user(
        self, comment_id: int
    ) -> Optional[CommentModel]:
        query = (
            select(CommentModel)
            .where(CommentModel.id == comment_id)
            .options(
                selectinload(CommentModel.user),
            )
        )

        result = await self.session.execute(query)
        return result.scalar_one_or_none()
