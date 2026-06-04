import uuid

from sqlalchemy import (
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy.sql import func

from app.db.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String,
        nullable=True
    )

    section_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("sections.id"),
        nullable=False
    )

    assignee_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    section = relationship(
        "Section",
        back_populates="tickets"
    )

    assignee = relationship(
        "User"
    )