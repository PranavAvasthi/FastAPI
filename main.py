from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Pranav'}}

@app.get('/about')
def about():
    return {'data': 'about page'}