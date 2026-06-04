import uuid

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.board_repository import BoardRepository
from app.repositories.invitation_repository import InvitationRepository
from app.repositories.board_member_repository import BoardMemberRepository


class InvitationService:

    @staticmethod
    async def create_invitation(
        db: AsyncSession,
        board_id,
        current_user
    ):

        board = await BoardRepository.get_board_by_id(
            db,
            board_id
        )

        if board is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Board not found"
            )

        if board.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only board owner can create invitations"
            )

        existing_invitation = await InvitationRepository.get_board_invitation(
            db,
            board_id
        )

        if existing_invitation:
            return existing_invitation

        invitation_token = str(uuid.uuid4())

        return await InvitationRepository.create_invitation(
            db,
            {
                "board_id": board_id,
                "token": invitation_token
            }
        )

    @staticmethod
    async def accept_invitation(
        db: AsyncSession,
        token: str,
        current_user
    ):

        invitation = await InvitationRepository.get_invitation_by_token(
            db,
            token
        )

        if invitation is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invalid invitation token"
            )

        existing_member = await BoardMemberRepository.get_member(
            db,
            invitation.board_id,
            current_user.id
        )

        if existing_member:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User is already a board member"
            )

        await BoardMemberRepository.create_member(
            db,
            {
                "board_id": invitation.board_id,
                "user_id": current_user.id,
                "role": "MEMBER"
            }
        )

        return {
            "message": "Successfully joined board"
        }