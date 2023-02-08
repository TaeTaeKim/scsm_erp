from typing import Union


from pydantic import BaseModel


# 권한 변경 controller에 쓰이는 request body schema
class AccountAuth(BaseModel):
    account_id : str
    account_order : bool = False
    account_instock : bool = False
    account_item  : bool = False
    account_management : bool = False


# 유저 등록 controller 에 쓰이는 request body schema
class AccountSchema(AccountAuth):
    account_name : str
    account_passwd : str
    account_session_id : Union[str,None] = None

    class Config:
        orm_mode = True
# 유저 업데이트 controller에 쓰이는 request body schema
class AccountBasic(BaseModel):
    account_id : str
    account_passwd : str

# 유저 listing controllelr에 쓰이는 request body schema
class AccountOut(BaseModel):
    account_name:str
    account_id : str
    account_order : bool
    account_instock : bool
    account_item  : bool
    account_management : bool




