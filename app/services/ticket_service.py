from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.board_repository import BoardRepository
from app.repositories.section_repository import SectionRepository
from app.repositories.ticket_repository import TicketRepository
from app.repositories.board_member_repository import BoardMemberRepository

from app.schemas.ticket import (
    TicketCreate,
    TicketUpdate
)


class TicketService:

    @staticmethod
    async def create_ticket(
        db: AsyncSession,
        ticket_data: TicketCreate,
        current_user
    ):
        section = await SectionRepository.get_section_by_id(
            db,
            ticket_data.section_id
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

        member = await BoardMemberRepository.get_member(
            db,
            board.id,
            current_user.id
        )


        if member is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized"
            )

        new_ticket_data = {
            "title": ticket_data.title,
            "description": ticket_data.description,
            "section_id": ticket_data.section_id,
            "assignee_id": ticket_data.assignee_id,
            "creator_id": current_user.id
        }

        return await TicketRepository.create_ticket(
            db,
            new_ticket_data
        )

    @staticmethod
    async def get_section_tickets(
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

        member = await BoardMemberRepository.get_member(
            db,
            board.id,
            current_user.id
        )

        if member is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized"
            )

        return await TicketRepository.get_tickets_by_section(
            db,
            section_id
        )

    @staticmethod
    async def update_ticket(
        db: AsyncSession,
        ticket_id,
        ticket_data: TicketUpdate,
        current_user
    ):

        ticket = await TicketRepository.get_ticket_by_id(
            db,
            ticket_id
        )

        if ticket is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ticket not found"
            )

        current_section = await SectionRepository.get_section_by_id(
            db,
            ticket.section_id
        )

        current_board = await BoardRepository.get_board_by_id(
            db,
            current_section.board_id
        )

        if (
        current_board.owner_id != current_user.id
        and ticket.creator_id != current_user.id
        ):
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized"
        )

        update_data = ticket_data.model_dump(
            exclude_unset=True
        )

        # IMPORTANT VALIDATION
        if "section_id" in update_data:

            new_section = await SectionRepository.get_section_by_id(
                db,
                update_data["section_id"]
            )

            if new_section is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Target section not found"
                )

            if new_section.board_id != current_section.board_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Cannot move ticket across boards"
                )

        return await TicketRepository.update_ticket(
            db,
            ticket,
            update_data
        )

    @staticmethod
    async def delete_ticket(
        db: AsyncSession,
        ticket_id,
        current_user
    ):

        ticket = await TicketRepository.get_ticket_by_id(
            db,
            ticket_id
        )

        if ticket is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ticket not found"
            )

        section = await SectionRepository.get_section_by_id(
            db,
            ticket.section_id
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

        await TicketRepository.delete_ticket(
            db,
            ticket
        )

        return {
            "message": "Ticket deleted successfully"
        }
    
    @staticmethod
    async def get_user_tickets(
        db: AsyncSession,
        current_user
    ):

        return await TicketRepository.get_user_tickets(
            db,
            current_user.id
        )