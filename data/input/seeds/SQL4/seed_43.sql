SELECT department_name, COUNT(proj_number) FROM departments JOIN projects ON projects.dep_id = departments.dep_number GROUP BY department_name HAVING COUNT(proj_number) > 2;
