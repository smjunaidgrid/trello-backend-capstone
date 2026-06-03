from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.board import Board


class BoardRepository:

    @staticmethod
    async def create_board(
        db: AsyncSession,
        board_data: dict
    ):

        new_board = Board(**board_data)

        db.add(new_board)

        await db.commit()

        await db.refresh(new_board)

        return new_board

    @staticmethod
    async def get_boards_by_owner(
        db: AsyncSession,
        owner_id
    ):

        query = select(Board).where(
            Board.owner_id == owner_id
        )

        result = await db.execute(query)

        return result.scalars().all()

    @staticmethod
    async def get_board_by_id(
        db: AsyncSession,
        board_id
    ):

        query = select(Board).where(
            Board.id == board_id
        )

        result = await db.execute(query)

        return result.scalar_one_or_none()