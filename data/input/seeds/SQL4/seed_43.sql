SELECT department_name FROM departments JOIN projects ON projects.dep_id = departments.dep_number GROUP BY department_name;
