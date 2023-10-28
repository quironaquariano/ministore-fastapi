from fastapi import FastAPI
from orders import orders_router
from products import products_router
from auth import auth_router

app = FastAPI()

app.include_router(orders_router)
app.include_router(auth_router)
app.include_router(products_router)



