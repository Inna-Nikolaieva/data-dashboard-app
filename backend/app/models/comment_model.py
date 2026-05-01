from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_models import Base, IDModel, TimestampModel


class CommentModel(Base, IDModel, TimestampModel):
    __tablename__ = "comments"

    body: Mapped[str] = mapped_column(Text, nullable=False)

    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id", ondelete="CASCADE"), nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    post: Mapped["PostModel"] = relationship(back_populates="comments")
    user: Mapped["UserModel"] = relationship(back_populates="comments")
