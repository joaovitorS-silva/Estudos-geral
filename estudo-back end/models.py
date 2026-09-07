import os
from argon2 import PasswordHasher
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,Session, sessionmaker, Mapped , mapped_column
from contextlib import contextmanager
from datetime import datetime
from sqlalchemy import DateTime , func

password_hash = PasswordHasher()
load_dotenv()

class Base(DeclarativeBase):
    pass


database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL nao foi definida no ambiente")

bd = create_engine(database_url)
Session = sessionmaker(bind=bd)
@contextmanager
def abrir_session():
    try:

        session = Session()
        yield session
    finally:
        session.close()


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int]= mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(nullable=False,)
    criado_em: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    admin: Mapped[bool] = mapped_column(nullable=False, default=False)
    
