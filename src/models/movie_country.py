from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

# Связь фильм-страна
class MovieCountry(Base):
    __tablename__ = 'movie_countries'

    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'), primary_key=True)  # ID фильма
    country_id = Column(Integer, ForeignKey('countries.id', ondelete='CASCADE'), primary_key=True)  # ID страны

    