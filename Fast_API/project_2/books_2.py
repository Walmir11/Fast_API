from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=1, lt=6)

BOOKS = [
    Book(1, 'Dom Casmurro', 'Machado de Assis', 'Dom Casmurro é um romance escrito por Machado de Assis em 1899.', 5),
    Book(2, 'A Moreninha', 'Joaquim Manuel de Macedo', 'A Moreninha é um romance escrito por Joaquim Manuel de Macedo em 1844.', 4),
    Book(3, 'O Guarani', 'José de Alencar', 'O Guarani é um romance escrito por José de Alencar em 1857.', 4),
    Book(4, 'Iracema', 'José de Alencar', 'Iracema é um romance escrito por José de Alencar em 1865.', 3),
    Book(5, 'Memórias Póstumas de Brás Cubas', 'Machado de Assis', 'Memórias Póstumas de Brás Cubas é um romance escrito por Machado de Assis em 1881.', 5),
    Book(6, 'O Cortiço', 'Aluísio Azevedo', 'O Cortiço é um romance naturalista escrito por Aluísio Azevedo em 1890.', 4),
]

@app.get('/books/')
async def read_books():
    return BOOKS

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