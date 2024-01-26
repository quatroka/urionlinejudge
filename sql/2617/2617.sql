SELECT prd.name AS "name",
    prv.name AS "name"
FROM products prd
    INNER JOIN providers prv ON prv.id = prd.id_providers
WHERE prv.name = 'Ajax SA';