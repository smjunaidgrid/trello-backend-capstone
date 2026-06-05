import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db.database import get_db

from app.schemas.invitation import (
    InvitationResponse,
    InvitationAcceptRequest
)

from app.services.invitation_service import InvitationService


router = APIRouter(
    prefix="/invitations",
    tags=["Invitations"]
)


@router.post(
    "/boards/{board_id}",
    response_model=InvitationResponse
)
async def create_invitation(
    board_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await InvitationService.create_invitation(
        db,
        board_id,
        current_user
    )


@router.post("/accept")
async def accept_invitation(
    invitation_data: InvitationAcceptRequest,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await InvitationService.accept_invitation(
        db,
        invitation_data.token,
        current_user
    )   