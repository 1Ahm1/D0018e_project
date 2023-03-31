from jsql import sql

from fastapi import  status
from domain.utils.general import UserInfo,BookInfo
from domain.customer import models
from api import app

def create_book(conn, user_info: UserInfo, data: models.CreateBookRequest):

    is_here = sql(
        conn,
        """
            SELECT COUNT(*) FROM `book`
            WHERE `name` = :name
        """,
        name = data.name
    ).scalar()
    if is_here == 0:
        sql(
        conn,
        """
            Insert INTO book (name, author, description)
            VALUES (:name, :author, :description)
        """,
        author = data.author,
        name = data.name,
        description = data.description,
    ).lastrowid
    

def delete_book(conn, user_info: UserInfo, book_id: int):

    sql(
        conn,
        """
            DELETE FROM book
            WHERE `book_id` = :id
        """,
        id = book_id
    )
    
    
def book_details(conn, user_info: UserInfo, book_id: int):
    data = sql(
        conn,
        """
            SELECT book_id, name, author, description
            FROM book
            WHERE book_id =:book_id 
        """,
        book_id = book_id
    ).dict()    
    return data

def book_list(conn, user_info: UserInfo):
    data = sql(
        conn,
        """
            SELECT book_id, name, author, description
            FROM book
        """
    ).dicts()    
    return data