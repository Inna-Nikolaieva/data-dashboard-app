from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.db_connection import get_async_session
from app.repositories.user_repository import UserRepository
from app.services.users_service import UsersService
from app.repositories.post_repository import PostRepository
from app.services.comments_service import CommentsService
from app.services.posts_service import PostsService
from app.repositories.comment_repository import CommentRepository


async def get_users_service(
    session: AsyncSession = Depends(get_async_session),
) -> UsersService:
    user_repository = UserRepository(session=session)

    return UsersService(user_repository=user_repository)


async def get_posts_service(
    session: AsyncSession = Depends(get_async_session),
) -> PostsService:
    post_repository = PostRepository(session=session)

    return PostsService(post_repository=post_repository)


async def get_comments_service(
    session: AsyncSession = Depends(get_async_session),
) -> CommentsService:
    comment_repository = CommentRepository(session=session)

    return CommentsService(comment_repository=comment_repository)
