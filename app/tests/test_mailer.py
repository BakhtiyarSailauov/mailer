import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_send_email():
    response = client.post(
        "/send_email",
        json={
            "to": "test@example.com",
            "subject": "Test",
            "message": "This is a test email."
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Email sent successfully"}


def test_send_email_invalid():
    response = client.post(
        "/send_email",
        json={
            "to": "invalid_email",
            "subject": "Test",
            "message": "This is a test email."
        }
    )
    assert response.status_code == 422


