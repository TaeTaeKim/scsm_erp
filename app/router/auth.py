from fastapi import APIRouter

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.get('/login')
async def login():
    return

@router.get('/logout')
async def logout():
    return
