SELECT
    (
        SELECT
            COUNT(*)
        FROM
            person_info
        WHERE (details ->> 'Sesso' = 'F'
            OR details ->> 'Sesso' = 'FEMMINILE')
        AND (LENGTH('${city:raw}') = 0
            OR details ->> 'Luogo di nascita' ILIKE '%${city:raw}%'
            OR details ->> 'Congiugimento (città)' ILIKE '%${city:raw}%'
            OR details ->> 'Provenienza' ILIKE '%${city:raw}%'
            OR details ->> 'Città di provenienza' ILIKE '%${city:raw}%'
            OR details ->> 'Provincia' ILIKE '%${city:raw}%'
            --OR details ->> 'Provincia' ILIKE '%${city_code:raw}%'
            OR details ->> 'Luogo di nascita / patria / nazione' ILIKE '%${city:raw}%'
            OR details ->> 'Luogo di nascita normalizzato' ILIKE '%${city:raw}%')) AS women,
(
    SELECT
        COUNT(*)
    FROM
        person_info
    WHERE (details ->> 'Sesso' = 'M'
        OR details ->> 'Sesso' = 'MASCHILE')
    AND (LENGTH('${city:raw}') = 0
        OR details ->> 'Luogo di nascita' ILIKE '%${city:raw}%'
        OR details ->> 'Congiugimento (città)' ILIKE '%${city:raw}%'
        OR details ->> 'Provenienza' ILIKE '%${city:raw}%'
        OR details ->> 'Città di provenienza' ILIKE '%${city:raw}%'
        OR details ->> 'Provincia' ILIKE '%${city:raw}%'
        --OR details ->> 'Provincia' ILIKE '%${city_code:raw}%'
        OR details ->> 'Luogo di nascita / patria / nazione' ILIKE '%${city:raw}%'
        OR details ->> 'Luogo di nascita normalizzato' ILIKE '%${city:raw}%')) AS men,
(
    SELECT
        COUNT(*)
    FROM
        person_info
    WHERE
        details ->> 'Sesso' IS NULL
        AND (LENGTH('${city:raw}') = 0
            OR details ->> 'Luogo di nascita' ILIKE '%${city:raw}%'
            OR details ->> 'Congiugimento (città)' ILIKE '%${city:raw}%'
            OR details ->> 'Provenienza' ILIKE '%${city:raw}%'
            OR details ->> 'Città di provenienza' ILIKE '%${city:raw}%'
            OR details ->> 'Provincia' ILIKE '%${city:raw}%'
            --OR details ->> 'Provincia' ILIKE '%${city_code:raw}%'
            OR details ->> 'Luogo di nascita / patria / nazione' ILIKE '%${city:raw}%'
            OR details ->> 'Luogo di nascita normalizzato' ILIKE '%${city:raw}%')) AS unknown
FROM
    person_info
LIMIT 1;

