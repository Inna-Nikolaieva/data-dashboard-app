from http.client import HTTPException
from typing import Any, Optional, Dict

import httpx

from app.core.settings import settings


class BaseDummyJSONAsyncClient:
    def __init__(self):
        self.base_url = f"{settings.DUMMYJSON_BASE_API_URL}"
        self.timeout = 10

    async def _request(
        self,
        method: str,
        endpoint: str,
        params: dict[str, Any] | None = None,
        body: dict[str, Any] | None = None,
    ):
        """
        Private method to handle HTTP requests.
        """
        async with httpx.AsyncClient(
            base_url=self.base_url, timeout=self.timeout
        ) as client:
            try:
                response = await client.request(
                    method,
                    endpoint,
                    params=params,
                    json=body,
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise HTTPException(
                    status_code=e.response.status_code, detail=e.response.text
                )
            except httpx.RequestError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
    ):
        """
        Wrapper for making GET requests.
        """
        return await self._request("GET", endpoint, params=params)
