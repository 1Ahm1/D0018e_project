from typing import Optional
from fastapi import APIRouter, Request
from domain.customer import  models
from domain.book import home
from domain.utils import general
from db.base import engine
from domain.utils.general import get_user_info

## from api.models import StandardResponse



router = APIRouter(
    prefix="/manager/book",
    tags=["manager/book"],
)

@router.get("/", status_code=200)
def Home() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, welcome to bookstore"}

@router.post("/create/")
async def create_book_endpoint(request: Request, data: models.CreateBookRequest):
    with engine.begin() as conn:
        return home.create_book(conn, get_user_info(request), data)
    
@router.post("/delete/{book_id}")
async def delete_book_endpoint(request: Request, book_id: int):
    with engine.begin() as conn:
        return home.delete_book(conn, get_user_info(request), book_id)

@router.post("/search/{book_id}")
async def search_book_endpoint(request: Request, book_id: int):
    with engine.begin() as conn:
        return home.book_details(conn, get_user_info(request), book_id)

@router.get("/get/")
async def get_book_endpoint(request: Request):
    with engine.begin() as conn:
        return home.book_list(conn, get_user_info(request))