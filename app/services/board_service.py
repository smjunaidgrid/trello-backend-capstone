from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException, status

from app.repositories.board_repository import BoardRepository
from app.repositories.board_member_repository import BoardMemberRepository


from app.schemas.board import (
    BoardCreate,
    BoardDetailResponse
)


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

        board = await BoardRepository.create_board(
            db,
            new_board_data
        )

        await BoardMemberRepository.create_member(
            db,
            {
                "board_id": board.id,
                "user_id": owner_id,
                "role": "OWNER"
            }
        )

        return board

    @staticmethod
    async def get_user_boards(
        db: AsyncSession,
        owner_id
    ):

        return await BoardRepository.get_boards_by_owner(
            db,
            owner_id
        )

    @staticmethod
    async def get_board_details(
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
                detail="Not authorized to access this board"
            )

        return board    
    
    @staticmethod
    async def get_board_members(
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
                detail="Not authorized"
            )

        return await BoardMemberRepository.get_board_members(
            db,
            board_id
        )