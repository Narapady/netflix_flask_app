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
        ORDER BY imdb_score DESC LIMIT 1;
        """
        cursor.execute(sql)
        return cursor.fetchone()

    @classmethod
    def show_type(self, db: str, user: str, password: str):
        conn = psycopg2.connect(database=db, user=user, password=password)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM title WHERE type = 'SHOW';")
        return cursor.fetchall()

    @classmethod
    def movie_type(self, db: str, user: str, password: str):
        conn = psycopg2.connect(database=db, user=user, password=password)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM title WHERE type = 'MOVIE';")
        return cursor.fetchall()

    @classmethod
    def pg_age_certification(self, db: str, user: str, password: str):
        conn = psycopg2.connect(database=db, user=user, password=password)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM title WHERE age_certification = 'PG';")
        return cursor.fetchall()
