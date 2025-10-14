SELECT sample_table.id, AVG(employees.performance_score) AS avg_performance
FROM employees
JOIN sample_table ON employees.id = sample_table.id
GROUP BY sample_table.id
HAVING avg_performance > 80;