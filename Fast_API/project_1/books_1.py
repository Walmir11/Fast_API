from fastapi import FastAPI, Body

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

# Criar um novo livro, com o método POST
@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

# Atualizar um livro, com o método PUT
@app.put('/books/update_book')
async def update_book(book_title=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.get('title').casefold():
            BOOKS[i] = book_title
            return BOOKS[i]

# Deletar um livro, com o método DELETE
@app.delete('/books/delete_book/{book_title}/')
async  def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

# Traz os livros pelo autor
@app.get('/books/byauthor/{author}')
async def read_books_author(author:str):
    books = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books.append(book)
    return books
