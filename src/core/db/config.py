from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.core.settings import settings

HOST = settings.db_host
USER = settings.db_user
DATABASE = settings.db_name
PORT = settings.db_port
PASSWORD = settings.db_user_password

DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

metadata = MetaData()
Base = declarative_base(metadata)

# Нужно вложить сюда уже готовую строку подключения. Проблема в том что connect это корутина.
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
