import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from app.schemas.section import SectionResponse

class BoardBase(BaseModel):
    title: str
    description: Optional[str] = None


class BoardCreate(BoardBase):
    pass


class BoardResponse(BoardBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        
class BoardDetailResponse(BoardResponse):
    sections: list[SectionResponse] = []