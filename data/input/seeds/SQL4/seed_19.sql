SELECT project_id, COUNT(department_id) FROM employees GROUP BY project_id HAVING COUNT(department_id) > 2;
