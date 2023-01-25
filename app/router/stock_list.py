"""
stock list 데이터를 가져오는 api들이 있는 router들

"""
from fastapi import APIRouter

router = APIRouter(
    prefix='/stocklist'
)