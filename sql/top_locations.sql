SELECT 
    location,
    COUNT(*) AS jobs
FROM jobs_clean
GROUP BY location
ORDER BY jobs DESC
LIMIT 10;