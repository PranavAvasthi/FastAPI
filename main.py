from fastapi import FastAPI # type: ignore
from typing import Optional

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