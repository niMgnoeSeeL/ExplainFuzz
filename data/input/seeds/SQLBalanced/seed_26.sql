SELECT departments.department_name, COUNT(projects.id) FROM departments JOIN projects ON projects.dep_id = departments.id GROUP BY departments.department_name;
