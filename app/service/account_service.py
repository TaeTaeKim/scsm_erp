import bcrypt
from models.account_model import AccountModel


def hash_password(password):
    hashed_passwd = bcrypt.hashpw(password.encode("UTF-8"),bcrypt.gensalt())
    return hashed_passwd

class AccountService():
    def __init__(self):
        return
    # add account to account table
    def add_account(self,account_schema,db):
        try:
            # hashing password for save account
            password = account_schema.account_passwd
            hashed_password = hash_password(password)
            account_schema.account_passwd = hashed_password

            user = AccountModel(**account_schema.dict())
            db.add(user)
            db.commit()
            return True
        except:
            return False
            
    # delete account to account table
    def delete_account(self, id, db):
        try:
            
            db.query(AccountModel).filter(AccountModel.account_id ==id).delete()
            db.commit()
            return True
        except:
            return False
    # update account to account table
    def update_account(self, id, password, db):
        try:

            user = db.query(AccountModel).filter(AccountModel.account_id  == id).one_or_none()
            if user is None:
                return False
            
            user.account_passwd = hash_password(password)
            db.commit()
            return True
        except:
            return False

    # manage auth of account
    def reauth_account(self, id, order, instock, item, management, db):
            user = db.query(AccountModel).filter(AccountModel.account_id == id).one_or_none()
            if user is None:
                return False
            
            user.account_order = order
            user.account_instock = instock
            user.account_item = item
            user.account_management = management

            db.commit()
            return True


    def find_all(self,db):
        users = db.query(AccountModel).all()
        return users

    def id_validation(self,id,db):

        # id가 중복되면 True / 아니면 False를 반환하는 함수.
        user = db.query(AccountModel).filter(AccountModel.account_id==id).one_or_none()
        if user:
            return True
        else:
            return False