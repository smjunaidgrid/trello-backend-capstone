import uuid

from sqlalchemy import (
    String,
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.db.database import Base


class Invitation(Base):
    __tablename__ = "invitations"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    board_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("boards.id"),
        nullable=False
    )

    token: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )