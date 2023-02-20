from sqlalchemy import Column,Integer,Float,DateTime,Boolean
from datetime import datetime


from database.mysql import data_base


class UsageModel(data_base):
    __tablename__ = "usages"
    
    __table_args__ = {'mysql_collate':'utf8_general_ci','extend_existing':True}

    usage_id = Column(Integer, primary_key=True, autoincrement=True)
    usage_item = Column(Integer,nullable=False)
    usage_num = Column(Float, nullable=False)
    usage_date = Column(DateTime, nullable=False, default=datetime.now())
    usage_check = Column(Boolean, default=False)