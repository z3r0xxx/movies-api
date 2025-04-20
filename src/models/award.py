from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

# Награды
class Award(Base):
    __tablename__ = 'awards'

    id = Column(Integer, primary_key=True)  # Уникальный ID награды
    name = Column(String(255), nullable=False)  # Название премии (Oscar, Cannes и т.д.)
    year = Column(Integer, nullable=False)  # Год награды
    category = Column(String(255), nullable=False)  # Категория награды
    won = Column(Boolean, default=False)  # Выиграна ли награда
    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'))  # ID фильма
    person_id = Column(Integer, ForeignKey('people.id'))  # ID человека (если награда персональная)

