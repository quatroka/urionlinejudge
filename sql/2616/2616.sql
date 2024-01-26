SELECT c.id AS "id",
    c.name AS "name"
FROM customers c
    LEFT JOIN locations l ON l.id_customers = c.id
WHERE l.locations_date IS NULL
ORDER BY c.id;