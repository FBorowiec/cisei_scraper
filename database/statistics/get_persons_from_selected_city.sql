SELECT
    surname AS "Surname",
    full_name AS "Full_name",
    age AS "Age",
    trip_date AS "Trip date",
    registration_place AS "Registration place",
    details AS "Details"
FROM
    person_info
WHERE
    LENGTH('${city:raw}') = 0
    OR details ->> 'Luogo di nascita' ILIKE '%${city:raw}%'
    OR details ->> 'Congiugimento (città)' ILIKE '%${city:raw}%'
    OR details ->> 'Provenienza' ILIKE '%${city:raw}%'
    OR details ->> 'Città di provenienza' ILIKE '%${city:raw}%'
    OR details ->> 'Provincia' ILIKE '%${city:raw}%'
    --OR details ->> 'Provincia' ILIKE '%${city_code:raw}%'
    OR details ->> 'Luogo di nascita / patria / nazione' ILIKE '%${city:raw}%'
    OR details ->> 'Luogo di nascita normalizzato' ILIKE '%${city:raw}%'
LIMIT 10000;
