import uuid

from sqlalchemy import (
    ForeignKey,
    String
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.db.database import Base


class BoardMember(Base):
    __tablename__ = "board_members"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    board_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("boards.id"),
        nullable=False
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        String,
        default="MEMBER"
    )