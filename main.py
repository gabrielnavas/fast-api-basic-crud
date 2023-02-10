from fastapi import Body, FastAPI, HTTPException
from uuid import uuid4, UUID

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

@app.delete('/posts/{post_id}', status_code=204)
def create_posts(post_id: str):
    print("POST ID: ", post_id)
    post_found = None
    for post in posts:
        print(post)
        if post["id"] == UUID(post_id):
            post_found = post
            break
    if not post_found:
        raise HTTPException(status_code=404, detail="Item not found")
    posts.remove(post_found)