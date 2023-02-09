import uvicorn


from fastapi import FastAPI,Response,Cookie , Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
import starlette.status as status
from jinja2 import Environment, FileSystemLoader
from sqlalchemy.orm import Session

from router import account_router
from router import auth_router
from service.auth_service import check_session,AuthService
from database.mysql import get_db

auth_service = AuthService()
app = FastAPI()
app.mount('/static',StaticFiles(directory='static'),name='static')
templates = Environment(
    loader=FileSystemLoader("templates")
)

app.template_env = templates
app.include_router(account_router.account_router)
app.include_router(auth_router.auth_router)

def auth_process(api_auth,session_checked,render_template,id):
    if session_checked:
        if not api_auth:
            response = RedirectResponse('/unauthorization',status_code=status.HTTP_301_MOVED_PERMANENTLY)
            response.set_cookie('session_id',session_checked)
            return response
        else:

            template = app.template_env.get_template(render_template)
            response = Response(content=template.render(user=id), media_type="text/html")
            response.set_cookie('session_id',session_checked)
            return response
    elif not session_checked:
        response = RedirectResponse('/',status_code = status.HTTP_301_MOVED_PERMANENTLY)
        return response
    

@app.get('/')
async def index():
    template = app.template_env.get_template('login.html')
    return Response(content=template.render(), media_type="text/html")

@app.get('/unauthorization')
async def unauthorize():
    template = app.template_env.get_template('unauthorized.html')
    return Response(content=template.render(), media_type='text/html')


@app.get('/stock_list')
async def stock_list(id:str=Cookie(), session_id:str=Cookie(),db:Session=Depends(get_db)):
    session_checked = check_session(id, session_id, db)
    if session_checked:
        template = app.template_env.get_template('stockList.html')
        response = Response(content=template.render(user=id), media_type="text/html")
        response.set_cookie('session_id',session_checked)
        return response
    elif not session_checked:
        response = RedirectResponse('/',status_code = status.HTTP_301_MOVED_PERMANENTLY)
        return response

@app.get('/order_list')
async def stock_list(id:str=Cookie(), session_id:str=Cookie(),db:Session=Depends(get_db)):
    session_checked = check_session(id, session_id, db)
    auth_order = auth_service.auth_order(id,db)
    return auth_process(auth_order,session_checked,'orderList.html',id)
        

@app.get('/stock_management')
async def stock_management(id:str=Cookie(), session_id:str=Cookie(),db:Session=Depends(get_db)):
    session_checked = check_session(id, session_id, db)
    auth_item = auth_service.auth_item(id,db)
    return auth_process(auth_item,session_checked,'stockManagement.html',id)


@app.get('/account')
async def account(id:str=Cookie(), session_id:str=Cookie(),db:Session=Depends(get_db)):
    session_checked = check_session(id, session_id, db)
    auth_management = auth_service.auth_account(id,db)
    return auth_process(auth_management,session_checked,'account.html',id)


if __name__ =="__main__":
    uvicorn.run(app,debug =True)