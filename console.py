import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_01 = Author("Jane Austen")
author_repository.save(author_01)
author_02 =Author("JK Roling")
author_repository.save(author_02)



book_01 =Book("Pride and Prejudice", author_01)
book_repository.save(book_01)

book_02 = Book("Harry Potter", author_02)
book_repository.save(book_02)

pdb.set_trace()