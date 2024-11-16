from fastapi import FastAPI # type: ignore
from . import schemas, models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(request: schemas.Blog):
    return request