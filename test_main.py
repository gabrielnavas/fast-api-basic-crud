from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_posts():
    response = client.get('/posts')
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["data"][0]["name"] == "apple"
    assert type(json_data["data"][0]["id"]) == str
    assert len(json_data["data"][0]["id"]) == 36

def test_create_post():
    payload = { "id": "123", "name": "juice" }
    response = client.post('/posts', json=payload)
    json_data = response.json()
    assert response.status_code == 201
    assert len(json_data["data"]["id"]) == 36
    assert json_data["data"]["name"] == "juice"