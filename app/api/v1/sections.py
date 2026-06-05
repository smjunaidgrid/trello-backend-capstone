import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db.database import get_db
from app.schemas.section import (
    SectionCreate,
    SectionUpdate,
    SectionResponse
)
from app.services.section_service import SectionService


router = APIRouter(
    prefix="/sections",
    tags=["Sections"]
)


@router.post(
    "/",
    response_model=SectionResponse,
    status_code=201
)
async def create_section(
    section_data: SectionCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await SectionService.create_section(
        db,
        section_data,
        current_user
    )


@router.get(
    "/board/{board_id}",
    response_model=list[SectionResponse]
)
async def get_board_sections(
    board_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await SectionService.get_board_sections(
        db,
        board_id,
        current_user
    )


@router.put(
    "/{section_id}",
    response_model=SectionResponse
)
async def update_section(
    section_id: uuid.UUID,
    section_data: SectionUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await SectionService.update_section(
        db,
        section_id,
        section_data,
        current_user
    )


@router.delete(
    "/{section_id}"
)
async def delete_section(
    section_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await SectionService.delete_section(
        db,
        section_id,
        current_user
    )