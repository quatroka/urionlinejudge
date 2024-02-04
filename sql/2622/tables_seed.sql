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
CREATE TABLE legal_person (
    id_customers SERIAL REFERENCES customers(id),
    cnpj CHAR(18),
    contact VARCHAR(255)
);
INSERT INTO customers (name, street, city, state, credit_limit)
VALUES (
        'Nicolas Diogo Cardoso',
        'Acesso Um',
        'Porto Alegre',
        'RS',
        475
    ),
    (
        'Cecília Olivia Rodrigues',
        'Rua Sizuka Usuy',
        'Cianorte',
        'PR',
        3170
    ),
    (
        'Augusto Fernando Carlos Eduardo Cardoso',
        'Rua Baldomiro Koerich',
        'Palhoça',
        'SC',
        1067
    ),
    (
        'Nicolas Diogo Cardoso',
        'Acesso Um',
        'Porto Alegre',
        'RS',
        475
    ),
    (
        'Sabrina Heloisa Gabriela Barros',
        'Rua Engenheiro Tito Marques Fernandes',
        'Porto Alegre',
        'RS',
        4312
    ),
    (
        'Joaquim Diego Lorenzo Araújo',
        'Rua Vitorino',
        'Novo Hamburgo',
        'RS',
        2314
    );
INSERT INTO legal_person (id_customers, cnpj, contact)
VALUES (4, '85883842000191', '99767-0562'),
    (5, '47773848000117', '99100-8965');