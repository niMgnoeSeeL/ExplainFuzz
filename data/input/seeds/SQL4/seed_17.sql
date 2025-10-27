SELECT department_name, COUNT(id) FROM departments JOIN employees ON departments.dep_number = employees.department_id GROUP BY department_name;
