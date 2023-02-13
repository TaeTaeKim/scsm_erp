"""
stock list 데이터를 가져오는 api들이 있는 router들

"""
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from service.stock_service import StockService
from database.mysql import get_db


stock_router = APIRouter(
    prefix='/stocklist',
    tags=['stocklist']
)

stock_service = StockService()
@stock_router.get('/get_stock')
async def get_stock(db:Session=Depends(get_db)) -> list:
    items = stock_service.get_stockdata(db)
    return items

@stock_router.get('/find_by_id')
async def find_by_id(id:int, db:Session = Depends(get_db)):
    item  =stock_service.find_by_id(id,db)
    return item
    