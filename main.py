from fastapi import FastAPI # type: ignore
from typing import Optional
# Using pydantic for data validation
from pydantic import BaseModel # type: ignore
import uvicorn # type: ignore

app = FastAPI()

# @app.get('/') # path operation decorator and the / is path
# def index(): #path operation function
#     return {'data': {'name': 'Pranav'}}

# @app.get('/about')
# def about():
#     return {'data': 'about page'}

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None): 
    #only get 10 published blogs
    if published:   
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    #fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id = id
    return {'data': {'1', '2'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

# Model
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None

# Post Method
@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created with title as {request.title}'}

# To run on a custom port
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=4000)