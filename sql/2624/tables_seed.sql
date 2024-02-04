DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS prices;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS providers;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS legal_person;
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(255),
    state CHAR(2),
    credit_limit NUMERIC
);
INSERT INTO customers (id, name, street, city, state, credit_limit)
VALUES (
        1,
        'Nicolas Diogo Cardoso',
        'Acesso Um',
        'Porto Alegre',
        'RS',
        475
    ),
    (
        2,
        'Cecília Olivia Rodrigues',
        'Rua Sizuka Usuy',
        'Cianorte',
        'PR',
        3170
    ),
    (
        3,
        'Augusto Fernando Carlos Eduardo Cardoso',
        'Rua Baldomiro Koerich',
        'Palhoça',
        'SC',
        1067
    ),
    (
        4,
        'Nicolas Diogo Cardoso',
        'Acesso Um',
        'Porto Alegre',
        'RS',
        475
    ),
    (
        5,
        'Sabrina Heloisa Gabriela Barros',
        'Rua Engenheiro Tito Marques Fernandes',
        'Porto Alegre',
        'RS',
        4312
    ),
    (
        6,
        'Joaquim Diego Lorenzo Araújo',
        'Rua Vitorino',
        'Novo Hamburgo',
        'RS',
        2314
    );