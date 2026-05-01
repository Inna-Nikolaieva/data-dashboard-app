from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_models import Base, IDModel, TimestampModel


class UserModel(Base, IDModel, TimestampModel):
    __tablename__ = "users"

    username: Mapped[str | None] = mapped_column(String(80), unique=True, nullable=True)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(256), nullable=False)

    posts: Mapped[list["PostModel"]] = relationship(back_populates="user")
    comments: Mapped[list["CommentModel"]] = relationship(back_populates="user")
