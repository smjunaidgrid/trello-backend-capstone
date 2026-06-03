import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SectionBase(BaseModel):
    name: str
    description: Optional[str] = None


class SectionCreate(SectionBase):
    board_id: uuid.UUID


class SectionUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class SectionResponse(SectionBase):
    id: uuid.UUID
    board_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True