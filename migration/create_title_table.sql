CREATE TABLE title (
    id serial primary key,
    title_id INTEGER,
    title VARCHAR(255),
    TYPE VARCHAR(255),
    description text,
    release_year INTEGER,
    age_certification VARCHAR(255),
    run_time INTEGER,
    genres VARCHAR(255),
    production_countries VARCHAR(255),
    seasons INTEGER,
    imdb_score DECIMAL(
        3,
        1
    ),
    imdb_votes DECIMAL(
        10,
        0
    )
);
