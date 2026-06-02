from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies import get_current_user
from app.models.user import User
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
@router.get(
    "/me",
    response_model=UserResponse
)
async def get_me(
    current_user: User = Depends(get_current_user)
):

    return current_user 