import uvicorn

from fastapi import FastAPI, Request,Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader

app = FastAPI()
app.mount('/static',StaticFiles(directory='static'),name='static')
templates = Environment(
    loader=FileSystemLoader("templates")
)

app.template_env = templates

@app.get('/')
def index():
    template = app.template_env.get_template('login.html')
    return Response(content=template.render(), media_type="text/html")


@app.get('/stock_list')
def stock_list():
    template = app.template_env.get_template('stockList.html')
    return Response(content=template.render(user='admin'), media_type="text/html")


if __name__ =="__main__":
    uvicorn.run(app,debug =True)