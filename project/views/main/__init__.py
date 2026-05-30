from .genres import api as genres_ns
from .movie import movie_ns
from .director import api as director_ns

__all__ = [
    'genres_ns',
    'movie_ns',
    "director_ns"
]
