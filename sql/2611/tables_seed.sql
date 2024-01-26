DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS movies;
CREATE TABLE genres (
    id NUMERIC PRIMARY KEY,
    description VARCHAR
);
CREATE TABLE movies (
    id NUMERIC PRIMARY KEY,
    name VARCHAR,
    id_genres NUMERIC,
    FOREIGN KEY (id_genres) REFERENCES genres(id)
);
INSERT INTO genres (id, description)
VALUES (1, 'Animation'),
    (2, 'Horror'),
    (3, 'Action'),
    (4, 'Drama'),
    (5, 'Comedy');
INSERT INTO movies (id, name, id_genres)
VALUES (1, 'Batman', 3),
    (2, 'The Battle of the Dark River', 3),
    (3, 'White Duck', 1),
    (4, 'Breaking Barriers', 4),
    (5, 'The Two Hours', 2);