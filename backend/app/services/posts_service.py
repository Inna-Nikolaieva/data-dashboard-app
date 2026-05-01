from app.repositories.post_repository import PostRepository
from app.integrations.dummy_json.apis.posts import DummyJSONPostAPI
from app.schemas.posts_schemas import PublicPostSchema, UpdatePostSchema


class PostsService:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository
        self.dummy_json_post_api = DummyJSONPostAPI()

    async def import_posts(self) -> int:
        posts = await self.dummy_json_post_api.get_all_posts()

        await self.post_repository.base.create_many(
            [post.model_dump() for post in posts.posts]
        )

        return posts.total

    async def get_posts(self) -> list[PublicPostSchema]:
        return await self.post_repository.get_all_posts_with_users_and_comments()

    async def get_post(self, post_id: int) -> PublicPostSchema:
        return await self.post_repository.get_post_by_id_with_user_and_comments(
            post_id=post_id
        )

    async def update_post(
        self, post_id: int, data: UpdatePostSchema
    ) -> PublicPostSchema:
        update_data = data.model_dump(exclude_unset=True)

        updated = await self.post_repository.base.update_one(
            filters={"id": post_id},
            data=update_data,
        )

        if not updated:
            return None

        return await self.post_repository.get_post_by_id_with_user_and_comments(
            post_id=post_id
        )

    async def delete_post(self, post_id: int):
        return await self.post_repository.base.delete_one(post_id)
