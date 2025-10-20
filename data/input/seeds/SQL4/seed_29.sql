SELECT projects.project_name, departments.department_name AS department FROM projects JOIN departments ON projects.dep_id = departments.dep_number;
