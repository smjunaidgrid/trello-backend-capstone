from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin,
    Token
)
from app.db.database import get_db
from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
async def register_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    return await AuthService.register_user(
        db,
        user_data
    )
@router.post(
    "/login",
    response_model=Token
)
async def login_user(
    user_credentials: UserLogin,
    db: AsyncSession = Depends(get_db)
):

    return await AuthService.login_user(
        db,
        user_credentials.email,
        user_credentials.password
    )