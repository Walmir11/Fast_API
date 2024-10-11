from typing import Annotated
# Importa o tipo `Annotated` do módulo `typing` para anotações de tipo avançadas.

from sqlalchemy.orm import Session
# Importa a classe `Session` do módulo `sqlalchemy.orm` para gerenciar sessões do banco de dados.

from fastapi import FastAPI, Depends
# Importa a classe `FastAPI` e a função `Depends` do módulo `fastapi` para criar a aplicação e gerenciar dependências.

import models
# Importa o módulo `models` que contém os modelos ORM.

from models import Todos
# Importa a classe `Todos` do módulo `models`, que representa a tabela `todos` no banco de dados.

from database import engine, SessionLocal
# Importa o `engine` e a fábrica de sessões `SessionLocal` do módulo `database`.

app = FastAPI()
# Cria uma instância da aplicação FastAPI.

models.Base.metadata.create_all(bind=engine)
# Cria todas as tabelas no banco de dados que ainda não existem, baseando-se nos modelos ORM definidos.

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Define uma função de dependência que cria uma nova sessão do banco de dados, a cede para a função chamadora e a fecha após o uso.

db_dependency = Annotated[Session, Depends(get_db)]
# Define uma anotação de tipo para a dependência do banco de dados, especificando que a função `get_db` deve ser usada para obter a sessão.

@app.get("/")
async def read_all(db: db_dependency):
    todos = db.query(models.Todos).all()
    return todos
# Define um endpoint GET na raiz ("/") que usa a dependência do banco de dados para consultar todos os registros da tabela `todos` e os retorna.
