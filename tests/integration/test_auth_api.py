from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_user():

    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "pytest_user_123@example.com",
            "password": "password123",
            "first_name": "Py",
            "last_name": "Test"
        }
    )

    assert response.status_code == 201