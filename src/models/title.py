import pandas as pd
import psycopg2


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

    @classmethod
    def action_films(self, db: str, user: str, password: str):
        conn = psycopg2.connect(database=db, user=user, password=password)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM title WHERE genres LIKE '%action%';")
        return cursor.fetchall()
