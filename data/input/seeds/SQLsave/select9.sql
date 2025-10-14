SELECT employees.department,employees.salary
FROM employees
JOIN sample_table ON employees.id = sample_table.id
GROUP BY employees.department;