from typing import Union


from pydantic import BaseModel


class ItemIn(BaseModel):
    item_code : int
    item_name : str
    item_stock : float =0
    item_unit : str
    item_manufact : Union[str,None] = None
    item_phone : Union[str,None] = None
    item_email : Union[str,None] = None
    item_img : Union[str,None] = None
    item_price : Union[int,None] =None
    item_descript : Union[str,None] =None
    item_purchase  : Union[str,None] = None


    class Config:
        orm_mode= True

class ImageIn(BaseModel):
    item_code : int
    class Config:
        orm_mode = True