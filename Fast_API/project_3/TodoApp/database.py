from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define a URL de conexão com o banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# Cria o engine do SQLAlchemy com a URL do banco de dados
# O argumento connect_args é específico para SQLite
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Cria uma fábrica de sessões configurada para não fazer commit ou flush automaticamente
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe base declarativa para os modelos ORM
Base = declarative_base()
