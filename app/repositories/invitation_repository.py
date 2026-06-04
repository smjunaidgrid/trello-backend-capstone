from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.invitation import Invitation


class InvitationRepository:

    @staticmethod
    async def create_invitation(
        db: AsyncSession,
        invitation_data: dict
    ):

        invitation = Invitation(**invitation_data)

        db.add(invitation)

        await db.commit()

        await db.refresh(invitation)

        return invitation

    @staticmethod
    async def get_invitation_by_token(
        db: AsyncSession,
        token: str
    ):

        query = select(Invitation).where(
            Invitation.token == token
        )

        result = await db.execute(query)

        return result.scalar_one_or_none()

    @staticmethod
    async def get_board_invitation(
        db: AsyncSession,
        board_id
    ):

        query = select(Invitation).where(
            Invitation.board_id == board_id
        )

        result = await db.execute(query)

        return result.scalar_one_or_none()