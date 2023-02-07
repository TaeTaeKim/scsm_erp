from typing import Union


from pydantic import BaseModel



class AccountAuth(BaseModel):
    account_id : str
    account_order : bool = False
    account_instock : bool = False
    account_item  : bool = False
    account_management : bool = False

class AccountBasic(AccountAuth):
    account_passwd : str

class AccountSchema(AccountBasic):
    account_name : str
    account_session_id : Union[str,None] = None

    class Config:
        orm_mode = True

class AccountOut(BaseModel):
    account_name:str
    account_id : str
    account_order : bool
    account_instock : bool
    account_item  : bool
    account_management : bool




