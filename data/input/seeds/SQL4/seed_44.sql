SELECT project_id FROM employees JOIN projects ON employees.project_id = projects.proj_number GROUP BY project_id;
