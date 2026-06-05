import uuid

from pydantic import BaseModel


class BoardMemberResponse(BaseModel):
    id: uuid.UUID
    board_id: uuid.UUID
    user_id: uuid.UUID
    role: str

    class Config:
        from_attributes = True