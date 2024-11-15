from fastapi import FastAPI # type: ignore
from . import schemas

app = FastAPI()

@app.post('/blog')
def create(request: schemas.Blog):
    return request