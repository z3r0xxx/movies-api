from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

# Связь фильм-язык
class MovieLanguage(Base):
    __tablename__ = 'movie_languages'

    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'), primary_key=True)  # ID фильма
    language_id = Column(Integer, ForeignKey('languages.id', ondelete='CASCADE'), primary_key=True)  # ID языка
    type = Column(String(50), default='original', primary_key=True)  # Тип языка: original / dubbed / subtitles

    