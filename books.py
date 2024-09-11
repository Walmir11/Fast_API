from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Harry Potter','author': 'J.K. Rowling','category': 'fantasy'},
    {'title': 'Lord of the Rings','author': 'J.R.R. Tolkien','category': 'fantasy'},
    {'title': 'The Hobbit','author': 'J.R.R. Tolkien','category': 'fantasy'},
    {'title': 'A Game of Thrones','author': 'George R.R. Martin','category': 'fantasy'},
    {'title': 'The Catcher in the Rye','author': 'J.D. Salinger','category': 'fiction'},
    {'title': 'To Kill a Mockingbird','author': 'Harper Lee','category': 'fiction'},
    {'title': '1984','author': 'George Orwell','category': 'fiction'},
    {'title': 'Pride and Prejudice','author': 'Jane Austen','category': 'romance'},
    {'title': 'Gone with the Wind','author': 'Margaret Mitchell','category': 'romance'},
    {'title': 'Outlander','author': 'Diana Gabaldon','category': 'romance'},
]


@app.get('/books')
# async é usado para funções assíncronas, ele é opcional
async def read_all_books():
    return BOOKS


