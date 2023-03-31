from typing import Optional
from fastapi import APIRouter, Request
from domain.customer import  models
from domain.order import home
from domain.utils import general
from db.base import engine
from domain.utils.general import get_user_info

## from api.models import StandardResponse



router = APIRouter(
    prefix="/manager/order",
    tags=["manager/order"],
)

@router.get("/", status_code=200)
def Home() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, welcome to bookstore"}

@router.post("/create/")
async def create_order_endpoint(request: Request, data: models.CreateOrderRequest):
    with engine.begin() as conn:
        return home.create_order(conn, get_user_info(request), data)
    
@router.post("/delete/{order_id}")
async def delete_order_endpoint(request: Request, order_id: int):
    with engine.begin() as conn:
        return home.delete_order(conn, get_user_info(request), order_id)

@router.post("/search/{order_id}")
async def search_order_endpoint(request: Request, order_id: int):
    with engine.begin() as conn:
        return home.order_details(conn, get_user_info(request), order_id)

@router.get("/get/")
async def get_order_endpoint(request: Request):
    with engine.begin() as conn:
        return home.order_list(conn, get_user_info(request))