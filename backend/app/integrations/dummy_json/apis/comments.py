from app.integrations.dummy_json.base_dummy_json_async_client import (
    BaseDummyJSONAsyncClient,
)
from app.integrations.dummy_json.dtos.comments import CommentsResponse


class DummyJSONCommentAPI:
    def __init__(self):
        self.uri = "comments"
        self.api_client = BaseDummyJSONAsyncClient()

    async def get_all_comments(self) -> CommentsResponse:
        endpoint = f"{self.uri}?limit=0"
        response = await self.api_client.get(endpoint)

        return CommentsResponse.model_validate(response)
