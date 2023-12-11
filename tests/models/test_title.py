import pandas as pd
import psycopg2
import pytest

from src.helper import build_insert_data, bulid_insert_query
from src.models.title import Title
from src.settings import DB_NAME, DB_TEST_NAME, PASSWORD, USER

MODEL = "title"


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
def db_with_titles():
    conn = psycopg2.connect(database=DB_TEST_NAME, user=USER, password=PASSWORD)
    cursor = conn.cursor()
    insert_sql = bulid_insert_query(MODEL)
    data_tuples = build_insert_data(MODEL)
    for data_tuple in data_tuples:
        cursor.execute(insert_sql, data_tuple)
    conn.commit()
    yield
    # cleanup
    cursor.execute("DELETE FROM title;")
    conn.commit()


def test_num_of_action_film(db_with_titles):
    assert len(Title.show_type(DB_TEST_NAME, USER, PASSWORD)) == 1


def test_movie_type(db_with_titles):
    assert len(Title.movie_type(DB_TEST_NAME, USER, PASSWORD)) == 4


def test_pg_age_certification(db_with_titles):
    assert len(Title.pg_age_certification(DB_TEST_NAME, USER, PASSWORD)) == 4
