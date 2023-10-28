from fastapi import APIRouter

orders_router  = APIRouter( 
    prefix='/orders', 
    tags=['orders']
)

@orders_router.get('/')
async def sigin():
    return {'message':'List of Orders'}