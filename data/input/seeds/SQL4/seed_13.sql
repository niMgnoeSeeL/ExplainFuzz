SELECT employees.employee_name, departments.department_name FROM employees JOIN departments ON employees.department_id = departments.dep_number WHERE NOT employees.full_time;
