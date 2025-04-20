from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

# Страны
class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)  # Уникальный ID страны
    name = Column(String(100), unique=True, nullable=False)  # Название страны

    