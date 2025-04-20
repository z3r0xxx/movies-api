from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

# Прокат фильма
class Release(Base):
    __tablename__ = 'releases'

    id = Column(Integer, primary_key=True)  # Уникальный ID проката
    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'))  # ID фильма
    country_id = Column(Integer, ForeignKey('countries.id'))  # Страна проката
    release_date = Column(Date)  # Дата релиза
    box_office = Column(BigInteger, default=0)  # Сборы
    format = Column(String(50), default='theatrical')  # Формат: theatrical, streaming и т.д.
    distributor = Column(String(255), default='')  # Название дистрибьютора
