from typing import Optional
from fastapi import APIRouter, Request
from domain.customer import  models
from domain.payment import home
from domain.utils import general
from db.base import engine
from domain.utils.general import get_user_info

## from api.models import StandardResponse



router = APIRouter(
    prefix="/manager/payment",
    tags=["manager/payment"],
)

@router.get("/", status_code=200)
def Home() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, welcome to bookstore"}

@router.post("/buy/{order_id}")
async def create_order_endpoint(request: Request, order_id: int):
    with engine.begin() as conn:
        return home.buy(conn, get_user_info(request), order_id)
    