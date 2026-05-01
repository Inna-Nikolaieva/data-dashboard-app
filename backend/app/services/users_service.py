from app.repositories.user_repository import UserRepository
from app.integrations.dummy_json.apis.users import DummyJSONUserAPI


class UsersService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.dummy_json_user_api = DummyJSONUserAPI()

    async def import_users(self) -> int:
        users = await self.dummy_json_user_api.get_all_users()

        await self.user_repository.base.create_many(
            [user.model_dump() for user in users.users]
        )

        return users.total
