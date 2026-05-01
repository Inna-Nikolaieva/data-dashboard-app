from fastapi import APIRouter, Depends, HTTPException

from app.services.posts_service import PostsService
from app.services.users_service import UsersService
from app.services.comments_service import CommentsService
from app.utils.call_services import (
    get_users_service,
    get_posts_service,
    get_comments_service,
)
from starlette import status

from app.schemas.dummy_data import ImportDummyDataResponseSchema

router = APIRouter(prefix="", tags=["Dummy data"])


@router.post("/import-dummy-data", response_model=ImportDummyDataResponseSchema)
async def import_dummy_data(
    users_service: UsersService = Depends(get_users_service),
    posts_service: PostsService = Depends(get_posts_service),
    comments_service: CommentsService = Depends(get_comments_service),
):
    try:
        users_count = await users_service.import_users()
        posts_count = await posts_service.import_posts()
        comments_count = await comments_service.import_comments()

        return ImportDummyDataResponseSchema(
            status="success",
            users=users_count,
            posts=posts_count,
            comments=comments_count,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to import dummy data.",
        )
