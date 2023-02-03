from fastapi import APIRouter

from app.database.mysql import get_db

router = APIRouter(
    prefix='/account',
    tags=['account']
)
