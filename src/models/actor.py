# from models.movie import Movie
from src.models import movie


class Actor:
    columns = ["id", "name"]

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    def build_movie(self, values):
        return movie.Movie(values)
