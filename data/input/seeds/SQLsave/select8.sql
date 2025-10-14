SELECT employees.name, sample_table.id
FROM employees
JOIN sample_table ON employees.id = sample_table.id;