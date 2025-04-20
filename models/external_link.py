from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

# Внешние ссылки
class ExternalLink(Base):
    __tablename__ = 'external_links'

    id = Column(Integer, primary_key=True)  # Уникальный ID ссылки
    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'))  # ID фильма
    source = Column(String(100), default='official')  # Источник: IMDb, Wikipedia и т.д.
    url = Column(Text, default='')  # Ссылка