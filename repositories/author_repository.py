from db.run_sql import run_sql

from models.author import Author
from models.book import Book


def save(author):
    sql = "INSERT INTO authors(name) VALUES(%s) RETURNING * "
    values = ['author.name']

    author_id = run_sql(sql, values)[0]['id']

    author.id = author_id
    return author
