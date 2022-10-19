SELECT
    details ->> 'Stato civile' AS "Stato civile",
    COUNT(*) AS "Count"
FROM
    person_info
WHERE
    details ->> 'Stato civile' IS NOT NULL
    AND details ->> 'Stato civile' > 100
GROUP BY
    details ->> 'Stato civile'
ORDER BY
    "Count" DESC
LIMIT 10000;
