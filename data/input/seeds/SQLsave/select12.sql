SELECT EXTRACT(YEAR FROM employees.hire_date) AS year_hire, AVG(employees.salary)
FROM employees
GROUP BY year_hire;