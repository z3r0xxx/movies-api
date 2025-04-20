from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

# Локации съёмок
class FilmingLocation(Base):
    __tablename__ = 'filming_locations'

    id = Column(Integer, primary_key=True)  # Уникальный ID локации
    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'))  # ID фильма
    location_name = Column(String(255), default='')  # Название места
    country_id = Column(Integer, ForeignKey('countries.id'))  # Страна
    city = Column(String(255), default='')  # Город
    address = Column(Text, default='')  # Адрес