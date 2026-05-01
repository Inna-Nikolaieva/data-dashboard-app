from typing import Any, List

from sqlalchemy import and_, delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base_models import Base


class BaseRepository:
    def __init__(self, session: AsyncSession, model: Base):
        self.session = session
        self.model = model

    async def create_many(self, data: List[dict]) -> List[Base]:
        rows = [self.model(**row) for row in data]
        self.session.add_all(rows)
        await self.session.commit()
        return rows

    async def get_one(self, **params) -> Base:
        query = select(self.model).filter_by(**params)
        result = await self.session.execute(query)
        db_row = result.scalar_one_or_none()
        return db_row

    async def get_all(self) -> List[Base]:
        query = select(self.model)
        result = await self.session.execute(query)
        db_rows = result.scalars().all()
        return db_rows

    async def _build_and_execute_update(
        self, filters: dict[str, Any], data: dict[str, Any]
    ):
        valid_fields = {key.name for key in self.model.__table__.columns}
        invalid_filters = set(filters.keys()) - valid_fields
        invalid_data = set(data.keys()) - valid_fields

        if invalid_filters:
            raise ValueError(f"Invalid filter fields: {invalid_filters}")
        if invalid_data:
            raise ValueError(f"Invalid update fields: {invalid_data}")

        query = (
            update(self.model)
            .where(
                and_(
                    getattr(self.model, field) == value
                    for field, value in filters.items()
                )
            )
            .values(**data)
            .returning(self.model)
        )

        result = await self.session.execute(query)
        await self.session.commit()

        return result

    async def update_one(
        self, filters: dict[str, Any], data: dict[str, Any]
    ) -> Base | None:
        result = await self._build_and_execute_update(filters, data)
        return result.scalar_one_or_none()

    async def delete_one(self, model_id: int) -> Base:
        query = (
            delete(self.model).where(self.model.id == model_id).returning(self.model)
        )
        res = await self.session.execute(query)
        await self.session.commit()
        return res.scalar_one_or_none()
