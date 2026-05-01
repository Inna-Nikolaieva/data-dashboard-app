from fastapi import APIRouter, Depends, HTTPException

from app.core.settings import settings
from app.services.comments_service import CommentsService
from app.utils.call_services import get_comments_service

from app.schemas.comments_schemas import PublicCommentSchema, UpdateCommentSchema

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.put("/{comment_id}", response_model=PublicCommentSchema)
async def update_comment(
    comment_id: int,
    data: UpdateCommentSchema,
    comment_service: CommentsService = Depends(get_comments_service),
):
    comment = await comment_service.update_comment(comment_id=comment_id, data=data)

    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    return comment


@router.delete("/{comment_id}")
async def delete_comment(
    comment_id: int,
    comment_service: CommentsService = Depends(get_comments_service),
):
    success = await comment_service.delete_comment(comment_id)

    if not success:
        raise HTTPException(status_code=404, detail="Comment not found")

    return {"message": "Deleted successfully"}
