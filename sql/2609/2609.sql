SELECT c.name AS "name",
    SUM(p.amount) AS "sum"
FROM products p
    INNER JOIN categories c ON p.id_categories = c.id
GROUP BY 1;