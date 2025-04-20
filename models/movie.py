from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)  # Уникальный ID фильма
    title = Column(String(255), nullable=False)  # Название фильма
    original_title = Column(String(255), default='')  # Оригинальное название
    release_date = Column(Date)  # Дата релиза
    duration_minutes = Column(Integer, default=0)  # Продолжительность в минутах
    description = Column(Text, default='')  # Описание фильма
    budget = Column(BigInteger, default=0)  # Бюджет фильма
    revenue = Column(BigInteger, default=0)  # Кассовые сборы
    age_rating = Column(String(10), default='NR')  # Возрастной рейтинг (NR = Not Rated)
    poster_url = Column(Text, default='')  # Ссылка на постер
    trailer_url = Column(Text, default='')  # Ссылка на трейлер
    imdb_id = Column(String(20), default='')  # ID на IMDb
    tmdb_id = Column(Integer, default=0)  # ID на TMDB
    created_at = Column(TIMESTAMP, server_default=func.now())  # Время создания
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # Время обновления
