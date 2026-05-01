from app.repositories.comment_repository import CommentRepository
from app.integrations.dummy_json.apis.comments import DummyJSONCommentAPI
from app.schemas.comments_schemas import (
    BaseCommentSchema,
    UpdateCommentSchema,
    PublicCommentSchema,
)


class CommentsService:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository
        self.dummy_json_comment_api = DummyJSONCommentAPI()

    async def import_comments(self) -> int:
        comments = await self.dummy_json_comment_api.get_all_comments()

        await self.comment_repository.base.create_many(
            [
                BaseCommentSchema(
                    body=comment.body, post_id=comment.post_id, user_id=comment.user.id
                ).model_dump()
                for comment in comments.comments
            ]
        )

        return comments.total

    async def update_comment(
        self, comment_id: int, data: UpdateCommentSchema
    ) -> PublicCommentSchema:
        update_data = data.model_dump(exclude_unset=True)

        updated = await self.comment_repository.base.update_one(
            filters={"id": comment_id},
            data=update_data,
        )

        if not updated:
            return None

        return await self.comment_repository.get_comment_by_id_with_user(
            comment_id=comment_id
        )

    async def delete_comment(self, comment_id: int):
        return await self.comment_repository.base.delete_one(comment_id)
