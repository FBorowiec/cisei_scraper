SELECT
    (
        SELECT COUNT(*)
        FROM
            person_info
        WHERE
            details ->> 'Sesso' = 'F'
            OR details ->> 'Sesso' = 'FEMMINILE') AS women,
    (
        SELECT COUNT(*)
        FROM
            person_info
        WHERE
            details ->> 'Sesso' = 'M'
            OR details ->> 'Sesso' = 'MASCHILE') AS men,
    (
        SELECT COUNT(*)
        FROM
            person_info
        WHERE
            details ->> 'Sesso' IS NULL) AS unknown
FROM
    person_info
LIMIT 1;
