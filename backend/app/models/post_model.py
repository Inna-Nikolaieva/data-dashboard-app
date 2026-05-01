from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_models import Base, IDModel, TimestampModel


class PostModel(Base, IDModel, TimestampModel):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(String(256), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    user: Mapped["UserModel"] = relationship(back_populates="posts")
    comments: Mapped[list["CommentModel"]] = relationship(back_populates="post")
