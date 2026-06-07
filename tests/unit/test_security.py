from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token
)
from app.core.security import decode_access_token


def test_hash_password():

    password = "mypassword123"

    hashed = hash_password(password)

    assert hashed != password
    assert isinstance(hashed, str)


def test_verify_password_success():

    password = "mypassword123"

    hashed = hash_password(password)

    assert verify_password(
        password,
        hashed
    ) is True


def test_verify_password_failure():

    password = "mypassword123"

    hashed = hash_password(password)

    assert verify_password(
        "wrongpassword",
        hashed
    ) is False


def test_create_and_decode_token():

    token = create_access_token(
        {"sub": "junaid@test.com"}
    )

    payload = decode_access_token(token)

    assert payload["sub"] == "junaid@test.com"

def test_decode_invalid_token():

    payload = decode_access_token(
        "invalid.token.value"
    )

    assert payload is None
    