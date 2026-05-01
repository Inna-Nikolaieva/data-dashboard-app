from app.integrations.dummy_json.base_dummy_json_async_client import (
    BaseDummyJSONAsyncClient,
)

from app.integrations.dummy_json.dtos.users import UsersResponse


class DummyJSONUserAPI:
    def __init__(self):
        self.uri = "users"
        self.api_client = BaseDummyJSONAsyncClient()

    async def get_all_users(self) -> UsersResponse:
        endpoint = f"{self.uri}?limit=0"
        response = await self.api_client.get(endpoint)

        return UsersResponse.model_validate(response)
