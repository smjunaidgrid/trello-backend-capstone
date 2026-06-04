import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db.database import get_db
from app.schemas.ticket import (
    TicketCreate,
    TicketUpdate,
    TicketResponse
)
from app.services.ticket_service import TicketService


router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post(
    "/",
    response_model=TicketResponse,
    status_code=201
)
async def create_ticket(
    ticket_data: TicketCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await TicketService.create_ticket(
        db,
        ticket_data,
        current_user
    )

@router.get(
    "/",
    response_model=list[TicketResponse]
)
async def get_user_tickets(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await TicketService.get_user_tickets(
        db,
        current_user
    )


@router.get(
    "/section/{section_id}",
    response_model=list[TicketResponse]
)
async def get_section_tickets(
    section_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await TicketService.get_section_tickets(
        db,
        section_id,
        current_user
    )


@router.put(
    "/{ticket_id}",
    response_model=TicketResponse
)
async def update_ticket(
    ticket_id: uuid.UUID,
    ticket_data: TicketUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await TicketService.update_ticket(
        db,
        ticket_id,
        ticket_data,
        current_user
    )


@router.delete(
    "/{ticket_id}"
)
async def delete_ticket(
    ticket_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await TicketService.delete_ticket(
        db,
        ticket_id,
        current_user
    )