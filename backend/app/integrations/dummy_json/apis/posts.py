from app.integrations.dummy_json.base_dummy_json_async_client import (
    BaseDummyJSONAsyncClient,
)
from app.integrations.dummy_json.dtos.posts import PostsResponse


class DummyJSONPostAPI:
    def __init__(self):
        self.uri = "posts"
        self.api_client = BaseDummyJSONAsyncClient()

    async def get_all_posts(self) -> PostsResponse:
        endpoint = f"{self.uri}?limit=0"
        response = await self.api_client.get(endpoint)

        return PostsResponse.model_validate(response)
