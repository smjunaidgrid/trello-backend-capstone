from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ticket import Ticket
from app.models.section import Section
from app.models.board import Board


class TicketRepository:

    @staticmethod
    async def create_ticket(
        db: AsyncSession,
        ticket_data: dict
    ):

        new_ticket = Ticket(**ticket_data)

        db.add(new_ticket)

        await db.commit()

        await db.refresh(new_ticket)

        return new_ticket

    @staticmethod
    async def get_ticket_by_id(
        db: AsyncSession,
        ticket_id
    ):

        query = select(Ticket).where(
            Ticket.id == ticket_id
        )

        result = await db.execute(query)

        return result.scalar_one_or_none()

    @staticmethod
    async def get_tickets_by_section(
        db: AsyncSession,
        section_id
    ):

        query = select(Ticket).where(
            Ticket.section_id == section_id
        )

        result = await db.execute(query)

        return result.scalars().all()

    @staticmethod
    async def update_ticket(
        db: AsyncSession,
        ticket,
        update_data: dict
    ):

        for key, value in update_data.items():
            setattr(ticket, key, value)

        await db.commit()

        await db.refresh(ticket)

        return ticket

    @staticmethod
    async def delete_ticket(
        db: AsyncSession,
        ticket
    ):

        await db.delete(ticket)

        await db.commit()

    @staticmethod
    async def get_user_tickets(
        db: AsyncSession,
        user_id
    ):

        query = select(Ticket).where(
            Ticket.creator_id == user_id
        )

        result = await db.execute(query)

        return result.scalars().all()
    