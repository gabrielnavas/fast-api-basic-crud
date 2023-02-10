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
    payload = { "name": "juice" }
    response = client.post('/posts', json=payload)
    json_data = response.json()
    assert response.status_code == 201
    assert len(json_data["data"]["id"]) == 36
    assert json_data["data"]["name"] == "juice"


def test_delete_post():
    # create the post
    payload = { "name": "juice" }
    response = client.post('/posts', json=payload)
    json_data = response.json()
    post = json_data["data"]

    # delete post
    post_id = post["id"]
    response = client.delete(f'/posts/{post_id}')
    assert response.status_code == 204

def test_update_post():
    # create the post
    payload = { "name": "juice" }
    response = client.post('/posts', json=payload)
    json_data = response.json()
    post = json_data["data"]

    # update post
    post_id = post["id"]
    new_post_data = { "name": "banana" }
    response = client.patch(f'/posts/{post_id}', json=new_post_data)
    assert response.status_code == 204
    