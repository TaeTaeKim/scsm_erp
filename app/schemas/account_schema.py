from typing import Union


from pydantic import BaseModel

class AccountBasic(BaseModel):
    account_id : str
    account_passwd : str


class AccountAuth(AccountBasic):
    account_order : bool = False
    account_instock : bool = False
    account_item  : bool = False
    account_management : bool = False


class AccountSchema(AccountAuth):
    account_name : str
    account_session_id : Union[str,None] = None

    class Config:
        orm_mode = True



