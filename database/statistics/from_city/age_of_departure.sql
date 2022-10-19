SELECT
    age::text AS "Age",
    COUNT(*) AS "Age Count"
FROM
    person_info
WHERE
    age < 75
    AND (LENGTH('${city:raw}') = 0
        OR details ->> 'Luogo di nascita' ILIKE '%${city:raw}%'
        OR details ->> 'Congiugimento (città)' ILIKE '%${city:raw}%'
        OR details ->> 'Provenienza' ILIKE '%${city:raw}%'
        OR details ->> 'Città di provenienza' ILIKE '%${city:raw}%'
        OR details ->> 'Provincia' ILIKE '%${city:raw}%'
        --OR details ->> 'Provincia' ILIKE '%${city_code:raw}%'
        OR details ->> 'Luogo di nascita / patria / nazione' ILIKE '%${city:raw}%'
        OR details ->> 'Luogo di nascita normalizzato' ILIKE '%${city:raw}%')
GROUP BY
    age;
