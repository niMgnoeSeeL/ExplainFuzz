SELECT departments.department_name, AVG(employees.salary) FROM departments JOIN employees ON employees.department_id = departments.id GROUP BY departments.department_name;
