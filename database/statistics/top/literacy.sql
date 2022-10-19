-- Alfabeta / Leggere e scrivere
SELECT
    details ->> 'Alfabeta' AS literacy,
    COUNT(*) AS total_count
FROM
    person_info
WHERE
    details ->> 'Alfabeta' IS NOT NULL
GROUP BY
    details ->> 'Alfabeta'
ORDER BY
    total_count DESC
LIMIT 3;
