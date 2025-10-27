SELECT departments.department_name, AVG(employees.salary) FROM departments JOIN employees ON employees.department_id = departments.dep_number GROUP BY departments.department_name;
