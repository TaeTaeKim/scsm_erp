import shutil
from models.stock_model import ItemModel
import os

class ItemService():
    def __init__(self) -> None:
    
        return
    def add_item(self,item_schema,db):
        item = db.query(ItemModel).filter(ItemModel.item_code==item_schema.item_code).one_or_none()
        if item:
            return {"result":False, 'message':'이미 품목이 존재합니다.'}
        item = ItemModel(**item_schema.dict())
        db.add(item)
        db.commit()
        return {'result':True}

    def add_img(self,item_id,file,db):
        if not file:
            return {'result':False,'message':'파일을 찾을 수 없습니다.'}
        item = db.query(ItemModel).filter(ItemModel.item_code==item_id).one_or_none()
        if not item:
            return {'result':False,'message':'ItemNotFound'}
        # 파일을 저장할 떄 품목으로 저장하도록 수정필요 -> 나중에 업데이트에도 덮어써지게 된다.
        filename = str(item_id)
        path = os.path.join("/Users/tykim/stock_management/app/static/img/stockimg", filename)
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        item.item_img = path
        db.commit()
        return {'result':True}

    """
    
    """
    def update_item(self,original_item_id,item_schema,db):
        #### 품번을 바꾸는 지 검사
        #. 품번을 바꾸지 않고 바꾸는 경우
        if original_item_id == item_schema.item_code:
            item = db.query(ItemModel).filter(ItemModel.item_code== original_item_id).one_or_none()

            ######## ! 사진까지 없어진다. -> 물품수정과 사진수정이 따로 필요함.
            for key, value in item_schema:
                if key=="item_img":
                    continue
                setattr(item,key,value)
            db.commit()
            return {'result':True}
        # 품번을 바꾸는 경우
        else:
            check_item = db.query(ItemModel).filter(ItemModel.item_code == item_schema.item_code).one_or_none()
            # 이미 품번이 있을경우
            if check_item:
                return {'result':False,'message':f'바꾸려는 품번({item_schema.item_code})은 이미 존재하는 품목입니다.'}
            else:
                item = db.query(ItemModel).filter(ItemModel.item_code==original_item_id).one_or_none()
                for key, value in item_schema:
                    if key=="item_img":
                        continue
                    setattr(item,key,value)

                db.commit()
                return {'result':True}

    def delete_item(self,item_id, db):
        # 관련 사진을 지우는 코드
        remove_path ='/Users/tykim/stock_management/app/static/img/stockimg/'+str(item_id)
        os.remove(remove_path)
        
        # 실제 데이터를 db에서 삭제하는 함수.
        db.query(ItemModel).filter(ItemModel.item_code==item_id).delete()
        db.commit()
        return {'result':True}

    ## 아이템에 대한 모든 로그를 가져오는 서비스
    # def item_log(self,item_id,db):
        
        