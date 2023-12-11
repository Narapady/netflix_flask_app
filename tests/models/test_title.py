import pandas as pd
import psycopg2

from src.models.title import Title
from src.settings import DB_NAME, PASSWORD, USER


def test_title_instantiatation():
    values = pd.read_csv("./data/titles_cleans.csv")
    title = Title(values)
    assert type(title) == Title


def test_highest_imdb_score():
    conn = psycopg2.connect(
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
    )
    cursor = conn.cursor()

    columns = pd.read_csv("./data/titles_cleans.csv").columns
    higest_imdb_score = Title.highest_imdb_score(cursor)
    data = dict(zip(columns, higest_imdb_score))
    assert data["title"] == "Crazy Delicious"