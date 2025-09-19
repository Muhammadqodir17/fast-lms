from fastapi import APIRouter

router = APIRouter(prefix='/about', tags=['compus'])

@router.get('/hello_world')
async def hello_world():
    return {'data': 'Hello world'}