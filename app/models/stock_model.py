from sqlalchemy import Column, String, Text,Integer,Float


from database.mysql import data_base


class ItemModel(data_base):
    __tablename__ = "items"
    
    __table_args__ = {'mysql_collate':'utf8_general_ci','extend_existing':True}

    item_code = Column(Integer,primary_key=True)
    item_name = Column(String(50), nullable=False)
    item_stock = Column(Float, nullable=False)
    item_unit = Column(String, nullable=False)
    item_email = Column(String)
    item_manufact = Column(String)
    item_phone  = Column(String)
    item_img = Column(String)
    item_price = Column(Integer)
    item_descript = Column(Text)