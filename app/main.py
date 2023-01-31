import uvicorn

import starlette.status as status
from fastapi import FastAPI,Response, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader

app = FastAPI()
app.mount('/static',StaticFiles(directory='static'),name='static')
templates = Environment(
    loader=FileSystemLoader("templates")
)

app.template_env = templates

@app.get('/')
async def index():
    template = app.template_env.get_template('login.html')
    return Response(content=template.render(), media_type="text/html")

@app.post('/login')
async def login(username:str=Form(...), password:str=Form(...)):
    if username=='admin' and password=="bj@n9c7f":
        response =  RedirectResponse(url='/stock_list', status_code=status.HTTP_301_MOVED_PERMANENTLY)
        return response


@app.get('/stock_list')
async def stock_list():
    template = app.template_env.get_template('stockList.html')
    return Response(content=template.render(user='admin'), media_type="text/html")

@app.get('/order_list')
async def stock_list():
    template = app.template_env.get_template('orderList.html')
    return Response(content=template.render(user='admin'), media_type="text/html")

@app.get('/stock_management')
async def stock_management():
    template = app.template_env.get_template('stockManagement.html')
    return Response(content=template.render(user='admin'),media_type="text/html")


if __name__ =="__main__":
    uvicorn.run(app,debug =True)