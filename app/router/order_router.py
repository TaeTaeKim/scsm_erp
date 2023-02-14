from service.order_service import OrderService
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.mysql import get_db


order_service = OrderService()

order_router = APIRouter(
    prefix='/order',
    tags=['order']
)

@order_router.get('/get_order')
async def get_order(db:Session = Depends(get_db)):
    orders = order_service.get_orders(db=db)
    return orders
@order_router.get('/check_purchase')
async def check_purchase(order_id:int,ischeck:bool, db:Session=Depends(get_db)):
    result = order_service.check_purchase(order_id,ischeck,db)
    return result

@order_router.get('/check_instock')
async def check_purchase(order_id:int,ischeck:bool, db:Session=Depends(get_db)):
    result = order_service.check_instock(order_id,ischeck,db)
    return result

@order_router.get('/check_cancel')
async def check_purchase(order_id:int,ischeck:bool, db:Session=Depends(get_db)):
    result = order_service.check_cancel(order_id,ischeck,db)
    return result
