from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define a URL de conexão com o banco de dados SQLite
# Esta linha define a URL de conexão para um banco de dados SQLite chamado "todos.db" localizado no diretório atual.
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# Cria o engine do SQLAlchemy com a URL do banco de dados
# O engine é a interface principal para o banco de dados. Ele é responsável por gerenciar as conexões com o banco de dados.
# O argumento `connect_args={"check_same_thread": False}` é específico para SQLite e permite que a conexão seja compartilhada entre diferentes threads.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Cria uma fábrica de sessões configurada para não fazer commit ou flush automaticamente
# `sessionmaker` é uma fábrica de sessões que cria novas instâncias de sessão.
# `autocommit=False` significa que as transações não serão automaticamente confirmadas.
# `autoflush=False` significa que as mudanças não serão automaticamente enviadas para o banco de dados.
# `bind=engine` associa a fábrica de sessões ao engine criado anteriormente.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe base declarativa para os modelos ORM
# `declarative_base` é uma fábrica que cria uma classe base para os modelos ORM (Object-Relational Mapping).
# Todos os modelos ORM irão herdar desta classe base.
Base = declarative_base()
