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
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    amount NUMERIC,
    price NUMERIC,
    id_categories INTEGER REFERENCES categories(id)
);
INSERT INTO categories (id, name)
VALUES (1, 'Superior'),
    (2, 'Super Luxury'),
    (3, 'Modern'),
    (4, 'Nerd'),
    (5, 'Infantile'),
    (6, 'Robust'),
    (9, 'Wood');
INSERT INTO products (id, name, amount, price, id_categories)
VALUES (1, 'Blue Chair', 30, 300.00, 9),
    (2, 'Red Chair', 200, 2150.00, 2),
    (3, 'Disney Wardrobe', 400, 829.50, 4),
    (4, 'Blue Toaster', 20, 9.90, 3),
    (5, 'Solar Panel', 30, 3000.25, 4);