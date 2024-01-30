SELECT prd.name AS "product_name",
    pvr.name AS "provider_name",
    prd.price AS "price"
FROM products prd
    INNER JOIN providers pvr ON pvr.id = prd.id_providers
    INNER JOIN categories c ON c.id = prd.id_categories
WHERE prd.price > 1000
    AND c.name = 'Super Luxury';