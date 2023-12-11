import pandas as pd
import psycopg2
import pytest

from src.helper import build_insert_data, bulid_insert_query
from src.models.credit import Credit
from src.settings import DB_TEST_NAME, PASSWORD, USER

MODEL = "credit"


def test_credit_instantiatation():
    values = pd.read_csv("./data/credits_cleans.csv")
    credit = Credit(values)
    assert type(credit) == Credit


@pytest.fixture()
def db_with_role():
    conn = psycopg2.connect(database=DB_TEST_NAME, user=USER, password=PASSWORD)
    cursor = conn.cursor()
    insert_sql = bulid_insert_query(MODEL)
    data_tuples = build_insert_data(MODEL)
    for data_tuple in data_tuples:
        cursor.execute(insert_sql, data_tuple)
    conn.commit()
    yield
    # cleanup
    cursor.execute("DELETE FROM credit;")
    conn.commit()


def test_actor_count(db_with_role):
    assert len(Credit.actor_count(DB_TEST_NAME, USER, PASSWORD)) == 5
