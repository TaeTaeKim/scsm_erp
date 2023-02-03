from typing import Union


from pydantic import BaseModel

class Account(BaseModel):
    id : str
    username : str
    userpasswd : str
    user_order : bool = False
    user_instock : bool = False
    user_item  : bool = False
    user_management : bool = False
    user_session_id : Union[str,None] = None


