from fastapi import APIRouter,Depends
from schemas.account_schema import AccountOut

from schemas.account_schema import AccountSchema, AccountBasic, AccountAuth
from sqlalchemy.orm import Session

from service.account_service import AccountService
from database.mysql import get_db

account_router = APIRouter(
    prefix='/account',
    tags=['account']
)

account_service = AccountService()


@account_router.post('/save')
async def save_account(account : AccountSchema, db: Session=Depends(get_db)):
    save = account_service.add_account(account_schema=account, db=db)
    return save


@account_router.get('/delete')
async def delete_account(id : str, db:Session=Depends(get_db)):
    delete_id = id
    delete = account_service.delete_account(id=delete_id, db=db)
    return delete

@account_router.post('/update')
async def update_account(account : AccountBasic, db:Session=Depends(get_db)):
    update_id = account.account_id
    update = account_service.update_account(update_id,account.account_passwd,db)
    return update


@account_router.post('/user_auth')
async def reauth_account(account : AccountAuth, db:Session = Depends(get_db)):
    reauth_id = account.account_id
    user_order = account.account_order
    user_instock = account.account_instock
    user_item = account.account_item
    user_management = account.account_management
    reauth = account_service.reauth_account(reauth_id,user_order,user_instock,user_item,user_management,db)
    return reauth


@account_router.get('/get_user')
async def get_users(db:Session = Depends(get_db)):
    users = account_service.find_all(db)
    return [AccountOut(
        account_id=user.account_id,
        account_instock=user.account_instock,
        account_item=user.account_item,
        account_management=user.account_management,
        account_name=user.account_name,
        account_order=user.account_order) for user in users]

@account_router.get('/id_validation')
async def id_validate(id:str, db:Session = Depends(get_db)):
    return account_service.id_validation(id,db)

        


