from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

# Связь фильм-жанр (многие ко многим)
class MovieGenre(Base):
    __tablename__ = 'movie_genres'

    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'), primary_key=True)  # ID фильма
    genre_id = Column(Integer, ForeignKey('genres.id', ondelete='CASCADE'), primary_key=True)  # ID жанра

    