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
def delete_post(post_id: str):
    post_found = None
    for post in posts:
        print(post)
        if post["id"] == UUID(post_id):
            post_found = post
            break
    if not post_found:
        raise HTTPException(status_code=404, detail="Item not found")
    posts.remove(post_found)

@app.patch('/posts/{post_id}', status_code=204)
def update_post(post_id: str, post_data: dict = Body()):
    post_found = None
    post_index = -1
    for index, post in enumerate(posts):
        print(post)
        if post["id"] == UUID(post_id):
            post_found = post
            post_index = index
            break
    if not post_found:
        raise HTTPException(status_code=404, detail="Item not found")
    post_found["name"] = post_data
    posts[post_index] = post_found