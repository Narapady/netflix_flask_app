import pandas as pd


class Title:
    columns = pd.read_csv("./data/titles_cleans.csv").columns

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    @classmethod
    def highest_imdb_score(self, cursor):
        sql = """
        --sql
        SELECT * 
        FROM title
        WHERE imdb_score IS NOT NULL 
        ORDER BY imdb_score DESC LIMIT 1
        """
        cursor.execute(sql)
        return cursor.fetchone()
