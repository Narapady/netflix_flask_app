class Title:
    columns = [
        "id",
        "title_id",
        "type",
        "description",
        "release_year",
        "age",
        "certificatin",
        "runtime",
        "genres",
        "production_country",
        "seasons",
        "imdb_score",
        "imdb_votes",
    ]

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
