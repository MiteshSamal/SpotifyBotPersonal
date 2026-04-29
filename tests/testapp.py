import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Your Playlists" in response.data

def test_volume_page_get(client):
    response = client.get("/volume")
    assert response.status_code == 200
    assert b"Volume Control" in response.data

def test_volume_post(client):
    response = client.post("/volume", data={"volume": "75"})
    assert response.status_code == 200
    assert b"Volume set to: 75" in response.data