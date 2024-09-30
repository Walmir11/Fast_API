from datetime import datetime
from typing import Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID não precisa ser criado na requisição', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=1, lt=6)
    published_date: int = Field(description='Ano de publicação', gt=0, lt=datetime.now().year)

    model_config = {
        'json_schema_extra': {
            'example': {
                'title': 'Dom Casmurro',
                'author': 'Machado de Assis',
                'description': 'Dom Casmurro é um romance escrito por Machado de Assis em 1899.',
                'rating': 5,
                'published_date': 1899
            }
        }
    }

BOOKS = [
    Book(1, 'Dom Casmurro', 'Machado de Assis', 'Dom Casmurro é um romance escrito por Machado de Assis em 1899.', 5, 1899),
    Book(2, 'A Moreninha', 'Joaquim Manuel de Macedo', 'A Moreninha é um romance escrito por Joaquim Manuel de Macedo em 1844.', 4, 1844),
    Book(3, 'O Guarani', 'José de Alencar', 'O Guarani é um romance escrito por José de Alencar em 1857.', 4 , 1857),
    Book(4, 'Iracema', 'José de Alencar', 'Iracema é um romance escrito por José de Alencar em 1865.', 3, 1865),
    Book(5, 'Memórias Póstumas de Brás Cubas', 'Machado de Assis', 'Memórias Póstumas de Brás Cubas é um romance escrito por Machado de Assis em 1881.', 5, 1881),
    Book(6, 'O Cortiço', 'Aluísio Azevedo', 'O Cortiço é um romance naturalista escrito por Aluísio Azevedo em 1890.', 4, 1890),
]

@app.get('/books/')
async def read_books():
    return BOOKS

@app.get('/books/{book_id}')
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    return {'message': 'Book not found'}

@app.delete('/book/{book_id}/')
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break

@app.get('/books/{book_rating}/')
async def read_books_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_rating = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_rating.append(book)
    return books_rating

@app.post('/create_book')
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book

@app.put('/book/update_book')
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book

@app.get('/books/published_date/{published_date}')
async def read_books_by_date(published_date: int = Query(gt=0, lt=datetime.now().year)):
    books_published_date = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_published_date.append(book)
    return books_published_date
