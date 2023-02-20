import shutil
from typing import List
from fastapi import APIRouter, Depends,UploadFile,File ,Form

import os

from sqlalchemy.orm import Session

from service.item_service import ItemService
from schemas.item_schema import ItemIn
from database.mysql import get_db
item_router = APIRouter(
    prefix='/item',
    tags=['item']
)

item_service = ItemService()

@item_router.post('/add_image')
def create_upload_file(item_id:int,file: UploadFile = File(...),db:Session=Depends(get_db)):
    result = item_service.add_img(item_id,file,db)
    return result
@item_router.post('/add_item')
async def create_item(item_data : ItemIn, db:Session=Depends(get_db)):
    print(item_data)
    result = item_service.add_item(item_data,db)
    return result


@item_router.post('/update_item')
async def update_item(original_item:int,new_item_data:ItemIn, db:Session=Depends(get_db)):
    result = item_service.update_item(original_item,new_item_data,db)
    return result

@item_router.get('/delete_item')
async def delete_item(item_id:int,db:Session=Depends(get_db)):
    result = item_service.delete_item(item_id,db)
    return result


@item_router.get('/item_log')
async def get_log(item_id : int,db:Session=Depends(get_db)):
    result = item_service.get_logs(item_id,db)
    return result