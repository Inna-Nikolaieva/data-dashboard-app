from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.post_model import PostModel
from sqlalchemy.orm import selectinload

from .base_repository import BaseRepository
from ..models import CommentModel


class PostRepository:
    model = PostModel

    def __init__(self, session: AsyncSession):
        self.session = session
        self.base = BaseRepository(session, self.model)

    async def get_all_posts_with_users_and_comments(self) -> list[PostModel]:
        query = (
            select(PostModel)
            .options(
                selectinload(PostModel.user),
                selectinload(PostModel.comments).selectinload(CommentModel.user),
            )
            .order_by(PostModel.id.desc())
        )

        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_post_by_id_with_user_and_comments(
        self, post_id: int
    ) -> Optional[PostModel]:
        query = (
            select(PostModel)
            .where(PostModel.id == post_id)
            .options(
                selectinload(PostModel.user),
                selectinload(PostModel.comments).selectinload(CommentModel.user),
            )
        )

        result = await self.session.execute(query)
        return result.scalar_one_or_none()
