SELECT
    EXTRACT(YEAR FROM trip_date)::text AS date,
    COUNT(*) AS persons
FROM
    person_info
WHERE
    trip_date IS NOT NULL
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
    date
ORDER BY
    date;
