SELECT department_name, id FROM departments JOIN employees ON departments.dep_number = employees.department_id GROUP BY department_name,id;
