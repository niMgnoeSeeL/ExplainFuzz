SELECT employees.employee_name, departments.department_name FROM employees JOIN departments ON employees.department_id = departments.id WHERE NOT employees.full_time;
