SELECT id, AVG(salary) FROM employees GROUP BY id HAVING AVG(salary) > 300000;
