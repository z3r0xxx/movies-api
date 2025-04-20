from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

# Языки
class Language(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)  # Уникальный ID языка
    name = Column(String(100), unique=True, nullable=False)  # Название языка
    