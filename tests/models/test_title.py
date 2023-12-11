import pandas as pd
import psycopg2
import pytest

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


@pytest.fixture()
def db_with_genres_action():
    # setup db with premium customer and non-premium
    conn = psycopg2.connect(
        database="netflix_test", user="postgres", password="postgres"
    )
    cursor = conn.cursor()
    cols = pd.read_csv("./data/titles_cleans.csv").columns
    insert_into = f"INSERT INTO title ({[col for col in cols]})\
                            VALUES ({['%s' for _ in range(13)]} )"
    insert_into = (
        insert_into.replace("[", "")
        .replace("]", "")
        .replace("'", "")
        .replace("    ", "")
    )
    cursor.execute(
        insert_into,
        (
            0,
            2323,
            "Avenger",
            "Movie",
            "Marvel Film",
            2019,
            "PG-13",
            120,
            "action",
            "US",
            1,
            8.0,
            34234.234,
        ),
    )
    cursor.execute(
        insert_into,
        (
            1,
            23432,
            "Batman",
            "Movie",
            "DC Film",
            2023,
            "R",
            180,
            "action",
            "US",
            2,
            9.0,
            23423.34,
        ),
    )
    conn.commit()
    yield
    # cleanup
    cursor.execute("DELETE FROM title;")
    conn.commit()


def test_num_of_action_films(db_with_genres_action):
    assert len(Title.action_films("netflix_test", "postgres", "postgres")) == 2
