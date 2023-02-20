from pydantic import BaseModel

from typing import Union

class OrderIn(BaseModel):
    order_item :int
    order_num : Union[float,None]

    class Config:
        orm_mode=True