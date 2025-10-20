SELECT department_id, COUNT(id) AS n_employees FROM employees GROUP BY department_id ORDER BY n_employees USING >, department_id USING <;
