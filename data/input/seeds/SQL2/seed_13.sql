SELECT employees.email, employees.department_id FROM employees JOIN departments ON employees.department_id = departments.dep_number WHERE NOT employees.full_time;
