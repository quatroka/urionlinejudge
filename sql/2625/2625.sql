SELECT CONCAT(
        SUBSTRING(np.cpf, 0, 4),
        '.',
        SUBSTRING(np.cpf, 4, 3),
        '.',
        SUBSTRING(np.cpf, 7, 3),
        '-',
        SUBSTRING(np.cpf, 10, 2)
    )
FROM customers c
    INNER JOIN natural_person np ON np.id_customers = c.id;