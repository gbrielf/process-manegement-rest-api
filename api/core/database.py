from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./processmanegement.db"

# conexão com o banco de dados, envio e recebimento de comandos SQL
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread"}
    # garante que a comunicação pode ser estabelecida entre diversas threads
)

# gerencia sessões no banco, INSERT, SELECT, UPDATE, DELETE
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# classe base do ORM, transforma classes em tabelas
Base = declarative_base()