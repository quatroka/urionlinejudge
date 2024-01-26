SELECT m.id AS "id",
    m.name AS "name"
FROM movies m
    INNER JOIN prices p ON p.id = m.id_prices
WHERE p.value < 2;