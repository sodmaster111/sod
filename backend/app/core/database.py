"""Базовое подключение к базе данных SQLite для новостей."""

import os
from pathlib import Path

from sqlmodel import SQLModel, Session, create_engine

# Путь к файлу базы данных внутри контейнера
DB_PATH = Path("/app/data/news.db")

# Убеждаемся, что каталог для базы данных существует
os.makedirs(DB_PATH.parent, exist_ok=True)

# URL подключения к базе данных SQLite
DATABASE_URL = "sqlite:///data/news.db"

# Создаём движок SQLModel
engine = create_engine(DATABASE_URL)


def get_session():
    """Возвращает сессию базы данных через генератор."""

    with Session(engine) as session:
        yield session


def init_db():
    """Инициализирует базу данных и создаёт таблицы."""

    SQLModel.metadata.create_all(engine)
