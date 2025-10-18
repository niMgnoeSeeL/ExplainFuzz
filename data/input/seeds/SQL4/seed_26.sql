SELECT departments.department_name, COUNT(projects.proj_number) FROM departments JOIN projects ON projects.dep_id = departments.dep_number GROUP BY departments.department_name;
