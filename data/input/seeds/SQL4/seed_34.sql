SELECT employees.employee_name, projects.project_name AS project FROM employees JOIN projects ON employees.project_id = projects.proj_number;
