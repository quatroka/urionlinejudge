SELECT p.id,
    p.name
FROM products p
    INNER JOIN categories c ON c.id = p.id_categories
WHERE c.name LIKE 'super%';