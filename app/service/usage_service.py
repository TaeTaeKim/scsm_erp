from models.usage_model import UsageModel
from models.stock_model import ItemModel
class UsageService():
    def __init__(self) -> None:
        return

    def use_stock(self, id, num, db):
        
        db.add(UsageModel(usage_item=id,usage_num=num))
        db.commit()

        return {'result':True}

    def usage_log(self,id, db):
        usages = db.query(UsageModel).filter(UsageModel.usage_item ==id).all()

        return usages

    def usage_check(self,usage_id,item_id,ischeck,use_num,db):
        item = db.query(ItemModel).filter(ItemModel.item_code==item_id).one_or_none()
        usage = db.query(UsageModel).filter(UsageModel.usage_id==usage_id).one_or_none()
        if ischeck:
            item.item_stock -= use_num
            usage.usage_check = True
            db.commit()
        else:
            item.item_stock += use_num
            usage.usage_check = False
            db.commit()
        return
        