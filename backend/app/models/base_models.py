from datetime import datetime
from decimal import Decimal
from typing import Any

from sqlalchemy import Boolean, DateTime, Integer, String, func
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    type_annotation_map = {
        dict[str, Any]: postgresql.JSON,
        list[dict[str, Any]]: postgresql.ARRAY(postgresql.JSON),
        list[str]: postgresql.ARRAY(String),
        Decimal: postgresql.NUMERIC(10, 2),
        datetime: DateTime(timezone=True),
        int: Integer,
        bool: Boolean,
    }


class IDModel:
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class CreatedAtModel:
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(), server_default=func.now(), index=True
    )


class UpdatedAtModel:
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )


class TimestampModel(CreatedAtModel, UpdatedAtModel):
    """Model with created_at and updated_at fields"""
