SELECT c.name AS "name"
FROM customers c
    INNER JOIN legal_person lp ON lp.id_customers = c.id;