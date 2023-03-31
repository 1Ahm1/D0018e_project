from jsql import sql

from fastapi import  status
from domain.utils.general import UserInfo,OrderInfo
from domain.customer import models
from api import app

def buy(conn, user_info: UserInfo, order_id: int):

    order = sql(
        conn,
        """
            SELECT product_ids , quantities
            FROM `order`
            WHERE order_id = :order_id AND customer_id = :customer_id
        """,
        order_id = order_id,
        customer_id = user_info.id
    ).dict()

    quantities = [int(x) for x in order["quantities"].split(",")]
    product_ids = [int(x) for x in order["product_ids"].split(",")]

    storage = sql(
        conn,
        """
            SELECT quantity FROM product
            WHERE product_id in :ids 
        """,
        ids = product_ids
    ).scalars()

    i = 0
    for quantity in storage:
        if quantity < quantities[i]:
            return "Not enough in stock"
        i = i + 1
    
    i = 0
    for product_id in product_ids:
        sql(
            conn,
            """
                UPDATE `product`
                SET `quantity` = :new_quantity
                WHERE `product_id` = :product_id
            """,
            product_id = product_id,
            new_quantity = storage[i] - quantities[i]
        )
        i = i + 1
    
