from jsql import sql

from fastapi import  status
from domain.utils.general import UserInfo,OrderInfo
from domain.customer import models
from api import app

def create_order(conn, user_info: UserInfo, data: models.CreateOrderRequest):

    storage = sql(
        conn,
        """
            SELECT quantity FROM product
            WHERE product_id in :ids 
        """,
        ids = data.product_ids
    ).scalars()

    i = 0
    for quantity in storage:
        if quantity < data.quantities[i]:
            return "Not enough in stock"
        i = i + 1
    sql(
        conn,
        """
            Insert INTO `order` (price, quantities, product_ids,customer_id)
            VALUES (:price, :quantities, :product_ids, :customer_id)
        """,
        price = 50,
        quantities = ",".join([str(x) for x in data.quantities]),
        product_ids = ",".join([str(x) for x in data.product_ids]),
        customer_id=user_info.id
    ).lastrowid
    

def delete_order(conn, user_info: UserInfo, order_id):

    sql(
        conn,
        """
            DELETE FROM `order`
            WHERE `order_id` = :id
        """,
        id = order_id
        
    ).lastrowid
    
    
def order_details(conn, user_info: UserInfo, order_id):
    data = sql(
        conn,
        """
            SELECT order_id, price, quantities, product_ids, customer_id, date
            FROM `order`
            WHERE order_id =:order_id 
        """,
        order_id = order_id
    ).dict()    
    data["quantities"] = [int(x) for x in data["quantities"].split(",")]
    data["product_ids"] = [int(x) for x in data["product_ids"].split(",")]
    return data

def order_list(conn, user_info: UserInfo):
    data = sql(
        conn,
        """
            SELECT order_id, price, quantities, product_ids, customer_id, date
            FROM `order`
        """
    ).dicts()    
    for obj in data:
        obj["quantities"] = [int(x) for x in obj["quantities"].split(",")]
        obj["product_ids"] = [int(x) for x in obj["product_ids"].split(",")]
    return data