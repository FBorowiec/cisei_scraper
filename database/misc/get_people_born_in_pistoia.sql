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
    details ->> 'Luogo di nascita' ILIKE '%PISTOIA%'
    OR details ->> 'Congiugimento (città)' ILIKE '%PISTOIA%'
    OR details ->> 'Provenienza' ILIKE '%PISTOIA%'
    OR details ->> 'Città di provenienza' ILIKE '%PISTOIA%'
    OR details ->> 'Provincia' ILIKE '%PISTOIA%'
    OR details ->> 'Provincia' ILIKE '%PT%'
    OR details ->> 'Luogo di nascita / patria / nazione' ILIKE '%PISTOIA%'
    OR details ->> 'Luogo di nascita normalizzato' ILIKE '%PISTOIA%';
