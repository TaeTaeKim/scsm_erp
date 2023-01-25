import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/')
def index():
    return FileResponse('templates/index.html')


if __name__ =="__main__":
    uvicorn.run(app)