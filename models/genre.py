from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)  # Уникальный ID жанра
    name = Column(String(100), unique=True, nullable=False)  # Название жанра
