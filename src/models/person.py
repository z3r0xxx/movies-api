from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

# Люди (актёры, режиссёры и др.)
class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)  # Уникальный ID персоны
    full_name = Column(String(255), nullable=False)  # Полное имя
    birth_date = Column(Date)  # Дата рождения
    death_date = Column(Date)  # Дата смерти (если есть)
    biography = Column(Text, default='')  # Биография
    photo_url = Column(Text, default='')  # Фото
    