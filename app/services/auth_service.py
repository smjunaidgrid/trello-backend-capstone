from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreate
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password


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