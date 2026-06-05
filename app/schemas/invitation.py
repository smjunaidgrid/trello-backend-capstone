import uuid

from pydantic import BaseModel


class InvitationAcceptRequest(BaseModel):
    token: str


class InvitationResponse(BaseModel):
    id: uuid.UUID
    board_id: uuid.UUID
    token: str

    class Config:
        from_attributes = True