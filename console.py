import pandas as pd
import psycopg2

from src.models.title import Title
from src.settings import DB_NAME, PASSWORD, USER

if __name__ == "__main__":
    conn = psycopg2.connect(
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
    )
    cursor = conn.cursor()

    columns = pd.read_csv("./data/titles_cleans.csv").columns
    higest_imdb_score = Title.highest_imdb_score(cursor)
    # higest_imdb_score = pd.read_sql(
    #     "select * from title where imdb_score IS NOT NULL order by imdb_score desc limit 1;",
    #     conn,
    # )
    # print(higest_imdb_score)
    print(dict(zip(columns, higest_imdb_score)))
