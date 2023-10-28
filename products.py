from fastapi import APIRouter

products_router  = APIRouter( 
    prefix='/products', 
    tags=['products']
)

@products_router.get('/')
async def sigin():
    return {'message':'List of Products'}