from pydantic import BaseModel

class UseItem(BaseModel):
    usage_item : int
    usage_num : float