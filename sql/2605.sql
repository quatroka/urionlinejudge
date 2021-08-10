SELECT p.name as name,
       pv.name as name
FROM products p
         INNER JOIN providers pv ON p.id_providers = pv.id
WHERE p.id_categories = 6;