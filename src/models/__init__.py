from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .award import Award
from .country import Country
from .external_link import ExternalLink
from .filming_location import FilmingLocation
from .genre import Genre
from .language import Language
from .movie_country import MovieCountry
from .movie_genre import MovieGenre
from .movie_language import MovieLanguage
from .movie_person import MoviePerson
from .movie import Movie
from .person import Person 
from .rating import Rating 
from .release import Release

__all__ = [
    'Award',
    'Country',
    'ExternalLink',
    'FilmingLocation',
    'Genre',
    'Language',
    'MovieCountry',
    'MovieGenre',
    'MovieLanguage',
    'MoviePerson',
    'Movie',
    'Person',
    'Rating',
    'Release',
]