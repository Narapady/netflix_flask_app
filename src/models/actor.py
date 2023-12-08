# from models.movie import Movie
import pandas as pd

from src.models import movie


class Title:
    columns = pd.read_csv("data/titles_cleansed.csv").columns

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    def build_movie(self, values):
        return movie.Movie(values)

    def build_movie(self, values):
        return movie.Movie(values)
