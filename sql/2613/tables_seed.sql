DROP TABLE IF EXISTS prices;
DROP TABLE IF EXISTS movies;
CREATE TABLE prices (
    id NUMERIC PRIMARY KEY,
    categorie VARCHAR,
    value NUMERIC
);
CREATE TABLE movies (
    id NUMERIC PRIMARY KEY,
    name VARCHAR,
    id_prices NUMERIC,
    FOREIGN KEY (id_prices) REFERENCES prices(id)
);
INSERT INTO prices (id, categorie, value)
VALUES (1, 'Releases', 3.50),
    (2, 'Bronze Seal', 2.00),
    (3, 'Silver Seal', 2.50),
    (4, 'Gold Seal', 3.00),
    (5, 'Promotion', 1.50);
INSERT INTO movies (id, name, id_prices)
VALUES (1, 'Batman', 3),
    (2, 'The Battle of the Dark River', 3),
    (3, 'White Duck', 5),
    (4, 'Breaking Barriers', 4),
    (5, 'The Two Hours', 2);