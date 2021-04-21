from db.run_sql import run_sql

from models.author import Author
from models.book import Book





def save(book):
    sql = "INSERT INTO books(title, author_id) VALUES(%s, %s) RETURNING * "
    values = ['book.title', 'book.author.id']

    book = run_sql(sql, values) 
    return book


