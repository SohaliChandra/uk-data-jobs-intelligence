SELECT 
    company,
    COUNT(*) AS job_postings
FROM jobs_clean
GROUP BY company
ORDER BY job_postings DESC
LIMIT 10;