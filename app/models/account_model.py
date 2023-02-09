
from sqlalchemy import Column, String, Boolean,Date

from database.mysql import data_base

class AccountModel(data_base):
    __tablename__ = "accounts"

    __table_args__ = {'mysql_collate':'utf8_general_ci','extend_existing':True}
    
    account_id = Column(String(10), primary_key=True)
    account_name = Column(String(10),unique=True, nullable=False)
    account_passwd = Column(String(255), nullable=False)
    account_order = Column(Boolean, default=False, nullable=False)
    account_instock = Column(Boolean, default= False, nullable=False)
    account_item = Column(Boolean, default=False, nullable=False)
    account_management = Column(Boolean, default=False, nullable=False)
    account_session_id = Column(String(255))
    session_expire = Column(Date)

