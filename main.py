from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {
        "Hello": "World"
    }

@app.get('/posts')
def get_posts():
    return {
        "data": { "id": "123", "name": "apple" }
    }

@app.post('/posts')
def create_posts():
    return {
        "data": { "id": "123", "name": "apple" }
    }