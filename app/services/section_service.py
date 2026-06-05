from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.board_repository import BoardRepository
from app.repositories.section_repository import SectionRepository
from app.schemas.section import (
    SectionCreate,
    SectionUpdate
)


class SectionService:

    @staticmethod
    async def create_section(
        db: AsyncSession,
        section_data: SectionCreate,
        current_user
    ):

        board = await BoardRepository.get_board_by_id(
            db,
            section_data.board_id
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

        new_section_data = {
            "name": section_data.name,
            "description": section_data.description,
            "board_id": section_data.board_id
        }

        return await SectionRepository.create_section(
            db,
            new_section_data
        )

    @staticmethod
    async def get_board_sections(
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

        return await SectionRepository.get_sections_by_board(
            db,
            board_id
        )

    @staticmethod
    async def update_section(
        db: AsyncSession,
        section_id,
        section_data: SectionUpdate,
        current_user
    ):

        section = await SectionRepository.get_section_by_id(
            db,
            section_id
        )

        if section is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Section not found"
            )

        board = await BoardRepository.get_board_by_id(
            db,
            section.board_id
        )

        if board.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized"
            )

        update_data = section_data.model_dump(
            exclude_unset=True
        )

        return await SectionRepository.update_section(
            db,
            section,
            update_data
        )

    @staticmethod
    async def delete_section(
        db: AsyncSession,
        section_id,
        current_user
    ):

        section = await SectionRepository.get_section_by_id(
            db,
            section_id
        )

        if section is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Section not found"
            )

        board = await BoardRepository.get_board_by_id(
            db,
            section.board_id
        )

        if board.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized"
            )

        await SectionRepository.delete_section(
            db,
            section
        )

        return {
            "message": "Section deleted successfully"
        }