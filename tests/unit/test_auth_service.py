import pytest
from fastapi import HTTPException
from unittest.mock import AsyncMock, patch

from app.services.auth_service import AuthService
from app.schemas.user import UserCreate


@pytest.mark.asyncio
async def test_register_user_success():

    user_data = UserCreate(
        email="test@example.com",
        password="password123",
        first_name="John",
        last_name="Doe"
    )

    with patch(
        "app.repositories.user_repository.UserRepository.get_user_by_email",
        new_callable=AsyncMock
    ) as mock_get_user, patch(
        "app.repositories.user_repository.UserRepository.create_user",
        new_callable=AsyncMock
    ) as mock_create_user:

        mock_get_user.return_value = None

        mock_create_user.return_value = {
            "email": user_data.email
        }

        result = await AuthService.register_user(
            None,
            user_data
        )

        assert result["email"] == "test@example.com"


@pytest.mark.asyncio
async def test_register_user_duplicate_email():

    user_data = UserCreate(
        email="test@example.com",
        password="password123",
        first_name="John",
        last_name="Doe"
    )

    with patch(
        "app.repositories.user_repository.UserRepository.get_user_by_email",
        new_callable=AsyncMock
    ) as mock_get_user:

        mock_get_user.return_value = object()

        with pytest.raises(HTTPException) as exc:

            await AuthService.register_user(
                None,
                user_data
            )

        assert exc.value.status_code == 400


@pytest.mark.asyncio
async def test_login_user_invalid_email():

    with patch(
        "app.repositories.user_repository.UserRepository.get_user_by_email",
        new_callable=AsyncMock
    ) as mock_get_user:

        mock_get_user.return_value = None

        with pytest.raises(HTTPException) as exc:

            await AuthService.login_user(
                None,
                "test@example.com",
                "password123"
            )

        assert exc.value.status_code == 401