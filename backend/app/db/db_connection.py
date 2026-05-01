from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from app.core.settings import settings

DATABASE_URL = f"postgresql+asyncpg://{settings.DB.POSTGRES_USER}:{settings.DB.POSTGRES_PASSWORD}@{settings.DB.POSTGRES_HOST}:{settings.DB.POSTGRES_PORT}/{settings.DB.POSTGRES_NAME}"

Base = declarative_base()

metadata = MetaData()

engine = create_async_engine(DATABASE_URL, echo=settings.DEBUG, poolclass=NullPool)
async_session_maker = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
