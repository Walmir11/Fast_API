from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):
    # Define o nome da tabela no banco de dados como 'todos'
    __tablename__ = 'todos'

    # Define a coluna 'id' como um inteiro, chave primária e indexada
    id = Column(Integer, primary_key=True, index=True)

    # Define a coluna 'title' como uma string
    title = Column(String)

    # Define a coluna 'description' como uma string
    description = Column(String)

    # Define a coluna 'priority' como um inteiro
    priority = Column(Integer)

    # Define a coluna 'complete' como um booleano, com valor padrão False
    complete = Column(Boolean, default=False)