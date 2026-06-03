from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db.database import get_db
from app.schemas.board import (
    BoardCreate,
    BoardResponse
)
from app.services.board_service import BoardService


router = APIRouter(
    prefix="/boards",
    tags=["Boards"]
)


@router.post(
    "/",
    response_model=BoardResponse,
    status_code=201
)
async def create_board(
    board_data: BoardCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await BoardService.create_board(
        db,
        board_data,
        current_user.id
    )


@router.get(
    "/",
    response_model=list[BoardResponse]
)
async def get_user_boards(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return await BoardService.get_user_boards(
        db,
        current_user.id
    )