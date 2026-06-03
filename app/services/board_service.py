from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.board_repository import BoardRepository
from app.schemas.board import BoardCreate


class BoardService:

    @staticmethod
    async def create_board(
        db: AsyncSession,
        board_data: BoardCreate,
        owner_id
    ):

        new_board_data = {
            "title": board_data.title,
            "description": board_data.description,
            "owner_id": owner_id
        }

        return await BoardRepository.create_board(
            db,
            new_board_data
        )

    @staticmethod
    async def get_user_boards(
        db: AsyncSession,
        owner_id
    ):

        return await BoardRepository.get_boards_by_owner(
            db,
            owner_id
        )