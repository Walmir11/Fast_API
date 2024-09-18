from fastapi import FastAPI

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
