SELECT project_id, COUNT(department_id) FROM employees JOIN projects ON employees.project_id = projects.proj_number GROUP BY project_id HAVING COUNT(department_id) > 1;
