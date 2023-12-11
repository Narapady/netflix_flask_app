import pandas as pd
import psycopg2


class Credit:
    columns = pd.read_csv("./data/credits_cleans.csv").columns

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    @classmethod
    def actor_count(self, db: str, user: str, password: str):
        conn = psycopg2.connect(database=db, user=user, password=password)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM credit WHERE role = 'ACTOR'")
        return cursor.fetchall()
