SELECT employee_name FROM employees WHERE EXISTS (SELECT 1 FROM projects WHERE projects.proj_number = employees.project_id AND projects.budget > 100000);
