import sqlite3

from flask import Flask, jsonify

from src.models.actor import Actor
from src.models.movie import Movie
from src.settings import DB_NAME

app = Flask(__name__)

app.config.from_mapping(DATABASE=DB_NAME)


@app.route("/movies")
def movies():
    conn = sqlite3.connect(app.config["DATABASE"])
    cursor = conn.cursor()
    cursor.execute("select * from movies;")
    movie_records = cursor.fetchall()
    return jsonify([Movie(movie_record).__dict__ for movie_record in movie_records])


@app.route("/movies/<id>")
def show_movie(id):
    conn = sqlite3.connect(app.config["DATABASE"])
    cursor = conn.cursor()
    cursor.execute("select * from movies where id = ?;", (id,))
    movie_records = cursor.fetchall()
    return jsonify([Movie(movie_record).__dict__ for movie_record in movie_records][0])


@app.route("/actors")
def actors():
    conn = sqlite3.connect(app.config["DATABASE"])
    cursor = conn.cursor()
    cursor.execute("select * from actors;")
    actor_records = cursor.fetchall()
    return jsonify([Actor(actor_record).__dict__ for actor_record in actor_records])


@app.route("/actors/<id>")
def show_actor(id):
    conn = sqlite3.connect(app.config["DATABASE"])
    cursor = conn.cursor()
    cursor.execute("select * from actors where id = ?;", (id,))
    actor_records = cursor.fetchall()
    return jsonify([Actor(actor_record).__dict__ for actor_record in actor_records])
