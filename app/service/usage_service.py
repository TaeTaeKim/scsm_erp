from models.usage_model import UsageModel
from models.stock_model import ItemModel
from sqlalchemy import func
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

    def get_usage(self, db):
        usages = db.query(UsageModel.usage_item,func.count(UsageModel.usage_item)).filter(UsageModel.usage_check==False).group_by(UsageModel.usage_item).all()
        return [{'item_code':row[0], 'count':row[1]} for row in usages ]  

    def cancel_usage(self,usage_id,db):
        db.query(UsageModel).filter(UsageModel.usage_id==usage_id).delete()
        db.commit()
        return True      