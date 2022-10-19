SELECT
    details ->> 'Città di destinazione' AS destination,
    COUNT(*) AS total_count
FROM
    person_info
WHERE
    details ->> 'Città di destinazione' IS NOT NULL
GROUP BY
    details ->> 'Città di destinazione'
ORDER BY
    total_count DESC
LIMIT 10000;
