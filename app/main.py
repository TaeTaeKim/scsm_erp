import starlette.status as status
import uvicorn
from fastapi import Cookie, Depends, FastAPI, Response
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from jinja2 import Environment, FileSystemLoader

from database.mysql import get_db
from router import account_router, auth_router , stock_router, order_router,item_router
from service.auth_service import AuthService, check_session
from sqlalchemy.orm import Session

auth_service = AuthService()
app = FastAPI()
app.mount('/static',StaticFiles(directory='static'),name='static')
templates = Environment(
    loader=FileSystemLoader("templates")
)

app.template_env = templates
app.include_router(account_router.account_router)
app.include_router(auth_router.auth_router)
app.include_router(stock_router.stock_router)
app.include_router(order_router.order_router)
app.include_router(item_router.item_router)

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
        print('check')
        response = RedirectResponse('/',status_code = status.HTTP_301_MOVED_PERMANENTLY)
        return response
    

@app.get('/')
def index():
    template = app.template_env.get_template('login.html')
    return Response(content=template.render(), media_type="text/html")

@app.get('/unauthorization')
def unauthorize():
    template = app.template_env.get_template('unauthorized.html')
    return Response(content=template.render(), media_type='text/html')


@app.get('/stock_list')
def stock_list(id:str=Cookie(), session_id:str=Cookie(),db:Session=Depends(get_db)):
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
def stock_list(id:str=Cookie(), session_id:str=Cookie(),db:Session=Depends(get_db)):
    session_checked = check_session(id, session_id, db)
    auth_order = auth_service.auth_order(id,db)
    return auth_process(auth_order,session_checked,'orderList.html',id)
        

@app.get('/stock_management')
def stock_management(id:str=Cookie(), session_id:str=Cookie(),db:Session=Depends(get_db)):
    session_checked = check_session(id, session_id, db)
    auth_item = auth_service.auth_item(id,db)
    print(auth_item)
    return auth_process(auth_item,session_checked,'stockManagement.html',id)


@app.get('/account')
def account(id:str=Cookie(), session_id:str=Cookie(),db:Session=Depends(get_db)):
    session_checked = check_session(id, session_id, db)
    print(session_checked)
    auth_management = auth_service.auth_account(id,db)
    return auth_process(auth_management,session_checked,'account.html',id)


if __name__ =="__main__":
    uvicorn.run(app,port=80)
