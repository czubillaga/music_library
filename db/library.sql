DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE albums(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    year INT,
    genre VARCHAR(255),
    artist_id INT REFERENCES artists(id)
);

CREATE TABLE artists(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
);