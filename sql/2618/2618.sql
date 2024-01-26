SELECT prd.name AS "product_name",
    pvr.name AS "provider_name",
    c.name AS "category_named"
FROM products prd
    INNER JOIN providers pvr ON pvr.id = prd.id_providers
    INNER JOIN categories c ON c.id = prd.id_categories
WHERE pvr.name = 'Sansul SA'
    AND c.name = 'Imported';