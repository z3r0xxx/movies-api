from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

# Рейтинги
class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)  # Уникальный ID рейтинга
    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'))  # ID фильма
    user_id = Column(Integer)  # ID пользователя (если есть)
    source = Column(String(100), default='user')  # Источник: IMDb / Кинопоиск / user
    rating = Column(DECIMAL(3, 1), default=0.0)  # Оценка
    votes = Column(Integer, default=1)  # Кол-во голосов
    review = Column(Text, default='')  # Текстовый отзыв
    rated_at = Column(TIMESTAMP, server_default=func.now())  # Дата оценки

    