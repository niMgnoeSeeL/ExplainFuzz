SELECT employee_name, ROUND(salary / 1000, 2) AS salary_k FROM employees ORDER BY salary_k USING >, id USING >;
