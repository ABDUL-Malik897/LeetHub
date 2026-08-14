SELECT DISTINCT s1.*
FROM Stadium s1
JOIN Stadium s2
    ON ABS(s1.id - s2.id) <= 2
JOIN Stadium s3
    ON ABS(s1.id - s3.id) <= 2
WHERE s1.people >= 100
  AND s2.people >= 100
  AND s3.people >= 100
  AND (
      (s2.id = s1.id + 1 AND s3.id = s1.id + 2)
      OR
      (s2.id = s1.id - 1 AND s3.id = s1.id + 1)
      OR
      (s2.id = s1.id - 2 AND s3.id = s1.id - 1)
  )
ORDER BY s1.visit_date;