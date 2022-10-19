SELECT
    EXTRACT(YEAR FROM trip_date)::text AS date,
    COUNT(*) AS persons
FROM
    person_info
WHERE
    trip_date IS NOT NULL
GROUP BY
    date
ORDER BY
    date;
