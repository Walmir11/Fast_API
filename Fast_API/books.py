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


@app.get('/books/')
# async é usado para funções assíncronas, ele é opcional
async def read_all_books():
    return BOOKS

@app.get("/books/mybooks/")
async def read_mybooks():
    return {"books_title": 'My favorite books'}

# @app.get('/books/{dynamic_param}')
# async def read_book_category(dynamic_param:str ):
#     return {"dynamic_param": dynamic_param}

# Traz o livro pelo título
@app.get('/books/{book_title}/')
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

# Traz os livros pela categoria
@app.get('/books/{category}/')
async def book_category(books_category:str):
    books = []
    for book in BOOKS:
        if book.get('category').casefold() == books_category.casefold():
            books.append(book)
    return books

# Traz os livros pela categoria e autor
@app.get('/books/{category}/{author}/')
async def read_category_author_books(category:str, author:str):
    books = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold() and book .get('author').casefold() == author.casefold():
            books.append(book)
    return books
