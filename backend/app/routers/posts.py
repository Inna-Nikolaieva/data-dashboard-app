from fastapi import APIRouter, Depends, HTTPException

from app.services.posts_service import PostsService
from app.utils.call_services import get_posts_service

from app.schemas.posts_schemas import PublicPostSchema, UpdatePostSchema

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/", response_model=list[PublicPostSchema])
async def get_posts(
    service: PostsService = Depends(get_posts_service),
):
    return await service.get_posts()


@router.get("/{post_id}", response_model=PublicPostSchema)
async def get_post(
    post_id: int,
    posts_service: PostsService = Depends(get_posts_service),
):
    post = await posts_service.get_post(post_id=post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


@router.put("/{post_id}", response_model=PublicPostSchema)
async def update_post(
    post_id: int,
    data: UpdatePostSchema,
    posts_service: PostsService = Depends(get_posts_service),
):
    post = await posts_service.update_post(post_id=post_id, data=data)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


@router.delete("/{post_id}")
async def delete_post(
    post_id: int,
    posts_service: PostsService = Depends(get_posts_service),
):
    success = await posts_service.delete_post(post_id)

    if not success:
        raise HTTPException(status_code=404, detail="Post not found")

    return {"message": "Deleted successfully"}
