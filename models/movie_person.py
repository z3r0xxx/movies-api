from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

# Участие человека в фильме
class MoviePerson(Base):
    __tablename__ = 'movie_people'

    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'), primary_key=True)  # ID фильма
    person_id = Column(Integer, ForeignKey('people.id', ondelete='CASCADE'), primary_key=True)  # ID человека
    role = Column(String(100), default='actor', primary_key=True)  # Роль: actor / director / writer / etc.
    character_name = Column(String(255), default='')  # Имя персонажа (если актёр)
    billing_order = Column(Integer, default=0)  # Порядок в титрах

    