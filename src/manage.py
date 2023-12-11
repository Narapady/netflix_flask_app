import psycopg2
from flask import Flask, jsonify

from src.helper import build_query_args
from src.models.credit import Credit
from src.models.title import Title
from src.settings import DB_NAME, PASSWORD, USER

app = Flask(__name__)


@app.route("/titles")
def titles():
    conn = psycopg2.connect(
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
    )
    cursor = conn.cursor()
    query_args = build_query_args(Title)

    if query_args:
        sql_str = "select * from title where "
        for k, v in query_args.items():
            sql_str += f"{k} = %s and "
        sql_str = sql_str[:-5] + ";"

        cursor.execute(
            sql_str,
            tuple(
                query_args.values(),
            ),
        )
    else:
        cursor.execute("select * from title;")

    title_records = cursor.fetchall()
    return jsonify([Title(title_record).__dict__ for title_record in title_records])


@app.route("/titles/<id>")
def show_title(id: int):
    conn = psycopg2.connect(
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
    )
    cursor = conn.cursor()
    cursor.execute("select * from title where id = %s;", (id,))
    title_records = cursor.fetchall()
    return jsonify([Title(title_record).__dict__ for title_record in title_records][0])


@app.route("/credits")
def credits():
    conn = psycopg2.connect(
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
    )
    cursor = conn.cursor()
    query_args = build_query_args(Credit)

    if query_args:
        sql_str = "select * from credit where "
        for k, v in query_args.items():
            sql_str += f"{k} = %s and "
        sql_str = sql_str[:-5] + ";"

        cursor.execute(
            sql_str,
            tuple(
                query_args.values(),
            ),
        )
    else:
        cursor.execute("select * from credit;")

    credits_records = cursor.fetchall()
    return jsonify(
        [Credit(credits_record).__dict__ for credits_record in credits_records]
    )


@app.route("/credits/<id>")
def show_credit(id: int):
    conn = psycopg2.connect(
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
    )
    cursor = conn.cursor()
    cursor.execute("select * from credit where id = %s;", (id,))
    credit_records = cursor.fetchall()
    return jsonify(
        [Credit(credit_record).__dict__ for credit_record in credit_records][0]
    )
