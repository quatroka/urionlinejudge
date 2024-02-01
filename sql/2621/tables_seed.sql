DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS prices;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS providers;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
CREATE TABLE providers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(255),
    state CHAR(2)
);
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    amount NUMERIC,
    price NUMERIC,
    id_providers INTEGER REFERENCES providers(id)
);
INSERT INTO providers (name, street, city, state)
VALUES (
        'Ajax SA',
        'Rua Presidente Castelo Branco',
        'Porto Alegre',
        'RS'
    ),
    ('Sansul SA', 'Av Brasil', 'Rio de Janeiro', 'RJ'),
    (
        'Pr Sheppard Chairs',
        'Rua do Moinho',
        'Santa Maria',
        'RS'
    ),
    ('Elon Electro', 'Rua Apolo', 'São Paulo', 'SP'),
    (
        'Mike Electro',
        'Rua Pedro da Cunha',
        'Curitiba',
        'PR'
    );
INSERT INTO products (name, amount, price, id_providers)
VALUES ('Blue Chair', 30, 300.00, 5),
    ('Red Chair', 50, 2150.00, 2),
    ('Disney Wardrobe', 400, 829.50, 4),
    ('Executive Chair', 17, 9.90, 3),
    ('Solar Panel', 30, 3000.25, 4);