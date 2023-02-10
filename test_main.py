from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == { "Hello": "World"}


def test_get_posts():
    response = client.get('/posts')
    assert response.status_code == 200
    assert response.json() == {
        "data": { "id": "123", "name": "apple" }
    }
