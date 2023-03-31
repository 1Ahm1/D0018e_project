from pydantic import BaseModel
from typing import List

class CustomerInitData(BaseModel):
    user_id: int
    email: str = None
    phone_number: str = None
    name: str = None
    image_id: str = None
class CreateAccountRequest(BaseModel):
    user_id: int
    email: str = None
    phone_number: str = None
    name: str = None
    image_id: str = None
    password: str

class CreateBookRequest(BaseModel):
    name: str = None
    author: str = None
    description: str = None
    

class CreateProductRequest(BaseModel):
    name: str
    price: int
    quantity: int
    book_id: int
class CreateOrderRequest(BaseModel):
    quantities: List[int]
    product_ids: List[int]
    

class CreateManagerRequest(BaseModel):
    user_id: int
    company_permissions: str=None
    