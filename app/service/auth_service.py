from models.account_model import AccountModel
import bcrypt
from fastapi import HTTPException
from fastapi.responses import RedirectResponse
import starlette.status as status
from service.account_service import hash_password
from datetime import datetime, timedelta

EXPIRE_MIN = 2


# 세션 데이터 베이스와 쿠키 세션을 비교한다. + 만기도 확인
def check_session(id, verify_session_id,db):
    user = db.query(AccountModel).filter(AccountModel.account_id==id).one_or_none()
    if not user:
        raise HTTPException(status_code=400, detail="유저를 찾을 수 없습니다.")
    session_id = user.account_session_id
    expire = user.session_expire
    
    print(session_id)
    print(verify_session_id)
    # 세션 만료 확인
    if datetime.now()>expire:
        return False
    # 세션 값 확인
    if verify_session_id != session_id:
        raise HTTPException(status_code=400, detail="잘못된 세션입니다.")
    else:
        now = datetime.now()
        if int((expire - now).total_seconds()) <= 60:
            user.session_expire = now+timedelta(minutes=EXPIRE_MIN)

        new_session_id = hash_password(user.account_id + now.strftime('%X'))
        user.account_session_id = str(new_session_id)
        db.commit()
        return new_session_id


class AuthService():
    
    def __init__(self):
        return    
    # 유저의 비밀번호를 인증 후 세션생성하는 함수
    def authentication(self,id,pw,db):
        user = db.query(AccountModel).filter(AccountModel.account_id == id).one_or_none()
        if not user:
            raise HTTPException(status_code=400, detail="잘못된 아이디 혹은 비밀번호입니다.")
        
        hashed_password = bytes( user.account_passwd,encoding='utf-8')
        verify_password = pw.encode('utf-8')

        auth = bcrypt.checkpw(verify_password,hashed_password)
        if auth:
            session_id = hash_password(user.account_id)
            expire = datetime.now()+timedelta(minutes=EXPIRE_MIN)
            self.session_maker(user,session_id,expire,db)
            return user
        else:
            raise HTTPException(status_code=400, detail="잘못된 아이디 혹은 비밀번호입니다.")


    def session_maker(self,user ,session_id, expire ,db):
        user.account_session_id = session_id
        user.session_expire = expire
        db.commit()
        return

    def logout(self,id,db):
        user = db.query(AccountModel).filter(AccountModel.account_id==id).one_or_none()
        user.account_session_id = None
        user.session_expire = None
        db.commit()
        
        
        return True

    def auth_order(self,id,db):
        user = db.query(AccountModel).filter(AccountModel.account_id==id).one_or_none()
        if not user:
            raise HTTPException(status_code=400,detail="유저를 찾을 수 없습니다.")

        return user.account_order

    def auth_item(self, id, db):
        user = db.query(AccountModel).filter(AccountModel.account_id==id).one_or_none()
        if not user:
            raise HTTPException(status_code=400,detail="유저를 찾을 수 없습니다.")

        return user.account_item

    def auth_instock(self, id, db):
        user = db.query(AccountModel).filter(AccountModel.account_id==id).one_or_none()
        if not user:
            raise HTTPException(status_code=400,detail="유저를 찾을 수 없습니다.")

        return user.account_instock
    
    def auth_account(self, id, db):
        user = db.query(AccountModel).filter(AccountModel.account_id==id).one_or_none()
        if not user:
            raise HTTPException(status_code=400,detail="유저를 찾을 수 없습니다.")

        return user.account_management
    