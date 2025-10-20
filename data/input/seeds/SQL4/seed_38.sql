SELECT employee_name, ROUND(salary / 1000, 2) AS salary_k, performance_score FROM employees ORDER BY salary_k USING >, performance_score USING >, id USING <;
