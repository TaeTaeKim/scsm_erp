from fastapi import APIRouter, Depends, Form, Cookie
from fastapi.responses import RedirectResponse
from typing import Union
from sqlalchemy.orm import Session
import starlette.status as status


from service.auth_service import AuthService
from database.mysql import get_db


auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)



auth_service = AuthService()


# return cookie if account valid
@auth_router.post('/login')
async def login(username:str=Form(...), password:str=Form(...), db:Session=Depends(get_db)):
    user =  auth_service.authentication(username, password, db)
    session_id = user.account_session_id

    response = RedirectResponse('/stock_list',status_code=status.HTTP_301_MOVED_PERMANENTLY)
    response.set_cookie('session_id',session_id)
    response.set_cookie('id',user.account_id)
    

    return response


@auth_router.get('/logout')
async def logout(id:Union[str,None]=Cookie(default=None),db:Session=Depends(get_db)):
    result = auth_service.logout(id,db)
    if result:
        response = RedirectResponse('/',status_code=status.HTTP_301_MOVED_PERMANENTLY)
        response.delete_cookie('session_id')
        response.delete_cookie('id')
    return response
