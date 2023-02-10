from fastapi import Body, FastAPI, HTTPException
from uuid import uuid4

app = FastAPI()

posts = [{ "id": uuid4(), "name": "apple" }]

@app.get('/posts')
def get_posts():
    return {
        "data": posts
    }

@app.post('/posts', status_code=201)
def create_post(payload: dict = Body()):
    new_post = {
        "id": uuid4(),
        "name": payload["name"]
    }
    posts.append(new_post)
    return {
        "data": new_post
    }