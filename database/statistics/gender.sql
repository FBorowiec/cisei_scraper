SELECT
    LEFT(details ->> 'Sesso',
        1) AS gender,
    COUNT(*) AS total
FROM
    person_info
WHERE
    details ->> 'Sesso' = 'F'
    OR details ->> 'Sesso' = 'FEMMINILE'
    OR details ->> 'Sesso' = 'M'
    OR details ->> 'Sesso' = 'MASCHILE'
    OR details ->> 'Sesso' IS NULL
GROUP BY
    gender;
