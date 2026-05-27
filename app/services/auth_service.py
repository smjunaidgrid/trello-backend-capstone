from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.schemas.user import UserCreate
from app.repositories.user_repository import UserRepository


class AuthService:

    @staticmethod
    async def register_user(
        db: AsyncSession,
        user_data: UserCreate
    ):

        existing_user = await UserRepository.get_user_by_email(
            db,
            user_data.email
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        hashed_pw = hash_password(user_data.password)

        new_user_data = {
            "email": user_data.email,
            "hashed_password": hashed_pw,
            "first_name": user_data.first_name,
            "last_name": user_data.last_name
        }

        return await UserRepository.create_user(
            db,
            new_user_data
        )

    @staticmethod
    async def login_user(
        db: AsyncSession,
        email: str,
        password: str
    ):

        user = await UserRepository.get_user_by_email(
            db,
            email
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not verify_password(
            password,
            user.hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        access_token = create_access_token(
            data={
                "sub": user.email
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }