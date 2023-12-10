import pandas as pd


class Title:
    columns = pd.read_csv("./data/titles_cleans.csv").columns

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    @classmethod
    def highest_imdb_score(self, cursor):
        sql = "select * from title order by imdb_score desc limit 1"
        cursor.execute(sql)
        return cursor.fetchone()
