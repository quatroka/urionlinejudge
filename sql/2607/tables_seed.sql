DROP TABLE IF EXISTS providers;
CREATE TABLE providers (
    id NUMERIC PRIMARY KEY,
    name VARCHAR(100),
    street VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(2)
);
INSERT INTO providers (id, name, street, city, state)
VALUES (
        1,
        'Henrique',
        'Av Brasil',
        'Rio de Janeiro',
        'RJ'
    ),
    (
        2,
        'Marcelo Augusto',
        'Rua Imigrantes',
        'Belo Horizonte',
        'MG'
    ),
    (
        3,
        'Caroline Silva',
        'Av São Paulo',
        'Salvador',
        'BA'
    ),
    (
        4,
        'Guilherme Staff',
        'Rua Central',
        'Porto Alegre',
        'RS'
    ),
    (
        5,
        'Isabela Moraes',
        'Av Juiz Grande',
        'Curitiba',
        'PR'
    ),
    (
        6,
        'Francisco Accerr',
        'Av Paulista',
        'São Paulo',
        'SP'
    );