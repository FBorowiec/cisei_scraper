SELECT
    age::text AS "Age",
    COUNT(*) AS "Age Count"
FROM
    person_info
WHERE
    age < 75
GROUP BY
    age;
