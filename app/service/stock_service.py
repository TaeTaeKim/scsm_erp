from models.stock_model import ItemModel

class StockService():
    

    def __init__(self) -> None:
        return

    def get_stockdata(self,db):
        items = db.query(ItemModel).all()

        return items

    def find_by_id(self,id,db):
        item = db.query(ItemModel).filter(ItemModel.item_code==id).one_or_none()
        if not item:
            return False
        else:
            return item