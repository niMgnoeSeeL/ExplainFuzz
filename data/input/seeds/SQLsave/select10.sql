SELECT employees.department, COUNT(*) AS dept_count
FROM employees
GROUP BY employees.department
HAVING COUNT(*) > 2;