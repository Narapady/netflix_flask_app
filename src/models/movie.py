# from models.actor import Actor
from src.models import actor


class Movie:
    columns = [
        "id",
        "title",
        "studio",
        "runtime",
        "description",
        "release_date",
        "year",
    ]

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    def add_actor(self, name):
        self.actor = actor.Actor([name])
