SELECT employees.employee_name, departments.department_name AS department FROM employees JOIN departments ON employees.department_id = departments.dep_number;
