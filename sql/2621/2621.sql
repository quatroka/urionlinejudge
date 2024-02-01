SELECT prd.name AS "name"
FROM products prd
    INNER JOIN providers prv ON prd.id_providers = prv.id
WHERE prd.amount BETWEEN 10 AND 20
    AND prv.name LIKE 'P%';