SELECT t.tag_name, t.count
FROM `bigquery-public-data.stackoverflow.tags` t
ORDER BY t.count DESC
LIMIT 10
