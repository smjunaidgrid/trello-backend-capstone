import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TicketBase(BaseModel):
    title: str
    description: Optional[str] = None


class TicketCreate(TicketBase):
    section_id: uuid.UUID
    assignee_id: Optional[uuid.UUID] = None


class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    section_id: Optional[uuid.UUID] = None
    assignee_id: Optional[uuid.UUID] = None


class TicketResponse(TicketBase):
    id: uuid.UUID
    section_id: uuid.UUID
    assignee_id: Optional[uuid.UUID]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  