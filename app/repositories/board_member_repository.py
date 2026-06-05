from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.board_member import BoardMember


class BoardMemberRepository:

    @staticmethod
    async def create_member(
        db: AsyncSession,
        member_data: dict
    ):

        member = BoardMember(**member_data)

        db.add(member)

        await db.commit()

        await db.refresh(member)

        return member

    @staticmethod
    async def get_board_members(
        db: AsyncSession,
        board_id
    ):

        query = select(BoardMember).where(
            BoardMember.board_id == board_id
        )

        result = await db.execute(query)

        return result.scalars().all()

    @staticmethod
    async def get_member(
        db: AsyncSession,
        board_id,
        user_id
    ):

        query = select(BoardMember).where(
            BoardMember.board_id == board_id,
            BoardMember.user_id == user_id
        )

        result = await db.execute(query)

        return result.scalar_one_or_none()