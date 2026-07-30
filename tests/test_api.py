from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_chat_endpoint():

    response = client.post(
        "/chat",
        json={
            "message": "Describe the employees table",
            "session_id": "pytest",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "message" in body