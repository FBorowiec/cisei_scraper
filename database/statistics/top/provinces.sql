SELECT
    details ->> 'Provincia' AS province,
    COUNT(*) AS total_count
FROM
    person_info
WHERE
    details ->> 'Provincia' IS NOT NULL
GROUP BY
    details ->> 'Provincia'
ORDER BY
    total_count DESC
LIMIT 10000;
