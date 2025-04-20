from sqlalchemy import Column, String, Integer, BigInteger, Text, Date, Boolean, ForeignKey, DECIMAL, Table, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

from . import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)  # Уникальный ID фильма
    title = Column(String(255), nullable=False)  # Название фильма
    original_title = Column(String(255), default='')  # Оригинальное название
    release_date = Column(Date)  # Дата релиза
    duration_minutes = Column(Integer, default=0)  # Продолжительность в минутах
    description = Column(Text, default='')  # Описание фильма
    budget = Column(BigInteger, default=0)  # Бюджет фильма
    revenue = Column(BigInteger, default=0)  # Кассовые сборы
    age_rating = Column(String(10), default='NR')  # Возрастной рейтинг (NR = Not Rated)
    poster_url = Column(Text, default='')  # Ссылка на постер
    trailer_url = Column(Text, default='')  # Ссылка на трейлер
    imdb_id = Column(String(20), default='')  # ID на IMDb
    tmdb_id = Column(Integer, default=0)  # ID на TMDB
    created_at = Column(TIMESTAMP, server_default=func.now())  # Время создания
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # Время обновления

# Связь фильм-язык
class MovieLanguage(Base):
    __tablename__ = 'movie_languages'

    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'), primary_key=True)  # ID фильма
    language_id = Column(Integer, ForeignKey('languages.id', ondelete='CASCADE'), primary_key=True)  # ID языка
    type = Column(String(50), default='original', primary_key=True)  # Тип языка: original / dubbed / subtitles

# Страны
class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)  # Уникальный ID страны
    name = Column(String(100), unique=True, nullable=False)  # Название страны

# Связь фильм-страна
class MovieCountry(Base):
    __tablename__ = 'movie_countries'

    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'), primary_key=True)  # ID фильма
    country_id = Column(Integer, ForeignKey('countries.id', ondelete='CASCADE'), primary_key=True)  # ID страны

# Люди (актёры, режиссёры и др.)
class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)  # Уникальный ID персоны
    full_name = Column(String(255), nullable=False)  # Полное имя
    birth_date = Column(Date)  # Дата рождения
    death_date = Column(Date)  # Дата смерти (если есть)
    biography = Column(Text, default='')  # Биография
    photo_url = Column(Text, default='')  # Фото

# Участие человека в фильме
class MoviePerson(Base):
    __tablename__ = 'movie_people'

    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'), primary_key=True)  # ID фильма
    person_id = Column(Integer, ForeignKey('people.id', ondelete='CASCADE'), primary_key=True)  # ID человека
    role = Column(String(100), default='actor', primary_key=True)  # Роль: actor / director / writer / etc.
    character_name = Column(String(255), default='')  # Имя персонажа (если актёр)
    billing_order = Column(Integer, default=0)  # Порядок в титрах

# Рейтинги
class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)  # Уникальный ID рейтинга
    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'))  # ID фильма
    user_id = Column(Integer)  # ID пользователя (если есть)
    source = Column(String(100), default='user')  # Источник: IMDb / Кинопоиск / user
    rating = Column(DECIMAL(3, 1), default=0.0)  # Оценка
    votes = Column(Integer, default=1)  # Кол-во голосов
    review = Column(Text, default='')  # Текстовый отзыв
    rated_at = Column(TIMESTAMP, server_default=func.now())  # Дата оценки

# Награды
class Award(Base):
    __tablename__ = 'awards'

    id = Column(Integer, primary_key=True)  # Уникальный ID награды
    name = Column(String(255), nullable=False)  # Название премии (Oscar, Cannes и т.д.)
    year = Column(Integer, nullable=False)  # Год награды
    category = Column(String(255), nullable=False)  # Категория награды
    won = Column(Boolean, default=False)  # Выиграна ли награда
    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'))  # ID фильма
    person_id = Column(Integer, ForeignKey('people.id'))  # ID человека (если награда персональная)

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

# Локации съёмок
class FilmingLocation(Base):
    __tablename__ = 'filming_locations'

    id = Column(Integer, primary_key=True)  # Уникальный ID локации
    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'))  # ID фильма
    location_name = Column(String(255), default='')  # Название места
    country_id = Column(Integer, ForeignKey('countries.id'))  # Страна
    city = Column(String(255), default='')  # Город
    address = Column(Text, default='')  # Адрес

# Внешние ссылки
class ExternalLink(Base):
    __tablename__ = 'external_links'

    id = Column(Integer, primary_key=True)  # Уникальный ID ссылки
    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='CASCADE'))  # ID фильма
    source = Column(String(100), default='official')  # Источник: IMDb, Wikipedia и т.д.
    url = Column(Text, default='')  # Ссылка