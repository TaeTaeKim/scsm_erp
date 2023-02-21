from database.mysql import data_base
from sqlalchemy import Column, Float,Integer, DateTime
from datetime import datetime


class OrderModel(data_base):
    __tablename__ = "orders"

    __table_args__ = {'mysql_collate':'utf8_general_ci','extend_existing':True}

    order_index = Column(Integer, primary_key=True, autoincrement=True)
    order_item = Column(Integer, nullable=False)
    order_status = Column(Integer, nullable=False, default=0)
    order_num = Column(Float, nullable=False)
    order_requestdate = Column(DateTime, default=datetime.now())
    order_purchasedate = Column(DateTime)
    order_instockdate = Column(DateTime)
    order_canceldate =  Column(DateTime)