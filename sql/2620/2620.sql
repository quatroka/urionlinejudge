SELECT c.name AS "name",
    o.id AS "id"
FROM customers c
    INNER JOIN orders o ON o.id_customers = c.id
WHERE o.orders_date BETWEEN '2016-01-01' AND '2016-06-30';