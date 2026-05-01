import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import settings
from app.routers.dummy_data import router as dummy_data_router
from app.routers.posts import router as posts_router
from app.routers.comments import router as comments_router


def get_application():
    _app = FastAPI(debug=settings.DEBUG)

    if settings.DEBUG:
        from debug_toolbar.middleware import DebugToolbarMiddleware

        _app.add_middleware(DebugToolbarMiddleware)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()

app.include_router(dummy_data_router)
app.include_router(posts_router)
app.include_router(comments_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
    )
