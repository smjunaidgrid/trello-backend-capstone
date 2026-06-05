from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.board import Board
from sqlalchemy.orm import selectinload


from app.models.board_member import BoardMember
from sqlalchemy import or_

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

        query = (
            select(Board)
            .options(
                selectinload(Board.sections)
            )
            .where(Board.id == board_id)
        )

        result = await db.execute(query)

        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_user_boards(
        db: AsyncSession,
        user_id
    ):

        query = (
            select(Board)
            .outerjoin(
                BoardMember,
                Board.id == BoardMember.board_id
            )
            .where(
                or_(
                    Board.owner_id == user_id,
                    BoardMember.user_id == user_id
                )
            )
        )

        result = await db.execute(query)

        return result.scalars().unique().all()