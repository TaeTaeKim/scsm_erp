from models.order_model import OrderModel
from models.stock_model import ItemModel
from datetime import datetime



class OrderService() :
    def __init__(self) -> None:
        return

    def get_orders(self ,db):
        result = db.query(OrderModel,ItemModel).outerjoin(ItemModel,OrderModel.order_item==ItemModel.item_code).all()
        orders = []

        for row in result:
            order = row[0].__dict__
            item = row[1].__dict__

            order['item_name'] = item['item_name']
            order['item_unit'] = item['item_unit']
            orders.append(order)

        return orders

    def check_purchase(self,order_id,ischeck,db):
        order = db.query(OrderModel).filter(OrderModel.order_index==order_id).one_or_none()
        if not order:
            return False
        if ischeck:
            order.order_status = 1
            order.order_purchasedate = datetime.now()
            db.commit()
            return True
        else:
            order.order_status = 0
            order.order_purchasedate = None
            db.commit()
            return True

    def check_instock(self,order_id,ischeck,db):
        order = db.query(OrderModel).filter(OrderModel.order_index==order_id).one_or_none()
        item = db.query(ItemModel).filter(ItemModel.item_code==order.order_item).one_or_none()
        if not order:
            return False
        
        if ischeck:
            order.order_status = 2
            order.order_instockdate = datetime.now()
            item.item_stock += order.order_num
            db.commit()
            return True
        else:
            order.order_status = 1
            order.order_instockdate = None
            item.item_stock -= order.order_num
            db.commit()
            return True
    
    def check_cancel(self,order_id,ischeck,db):
        order = db.query(OrderModel).filter(OrderModel.order_index==order_id).one_or_none()
        if not order:
            return False
        
        if ischeck:
            order.order_status = 3
            order.order_canceldate = datetime.now()
            db.commit()
            return True
        else:
            order.order_status = 1
            order.order_canceldate = None
            db.commit()
            return True
        