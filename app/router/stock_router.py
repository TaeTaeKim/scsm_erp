"""
stock list 데이터를 가져오는 api들이 있는 router들

"""
from fastapi import APIRouter,Depends,Cookie
from sqlalchemy.orm import Session
from service.stock_service import StockService
from service.order_service import OrderService
from service.auth_service import AuthService
from service.usage_service import UsageService
from database.mysql import get_db
from schemas.order_schema import OrderIn


stock_router = APIRouter(
    prefix='/stocklist',
    tags=['stocklist']
)

stock_service = StockService()
order_service = OrderService()
auth_service = AuthService()
usage_service = UsageService()
@stock_router.get('/get_stock')
async def get_stock(db:Session=Depends(get_db)) -> list:
    items = stock_service.get_stockdata(db)
    return items

@stock_router.get('/find_by_id')
async def find_by_id(id:int, db:Session = Depends(get_db)):
    item  =stock_service.find_by_id(id,db)
    return item
@stock_router.post('/order_stock')
async def order_stock(order_data:OrderIn, db:Session=Depends(get_db)):
    result = order_service.make_order(order_data,db)
    return result

@stock_router.get('/get_stock_usage')
async def stock_usage(item_code : int,id:str=Cookie(), db:Session=Depends(get_db)):
    auth_order = auth_service.auth_order(id,db)
    if not auth_order:
        return {'result':False}
    else:
        # 사용기록을 반환하는 서비스 useage_service
        usages = usage_service.usage_log(item_code,db)
        return {'result':True, "usages":usages}

@stock_router.get('/use_stock')
async def use_stock(item_code : int, use_num:float,db:Session=Depends(get_db)):
    result = usage_service.use_stock(item_code,use_num,db)
    return result


@stock_router.get('/use_check')
async def use_check(usage_id:int,item_code : int,ischeck:bool,use_num:float, db:Session=Depends(get_db)):
    result = usage_service.usage_check(usage_id,item_code,ischeck,use_num,db)
    return result