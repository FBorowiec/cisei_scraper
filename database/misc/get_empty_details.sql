SELECT
    id,
    idx,
    surname,
    full_name,
    age,
    trip_date,
    registration_place,
    url,
    details
FROM
    person_info
WHERE
    details = '{}';
