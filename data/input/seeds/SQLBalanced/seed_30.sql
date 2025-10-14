SELECT employee_name FROM employees WHERE EXISTS (SELECT 1 FROM departments WHERE departments.id = employees.department_id AND departments.budget > 400000);
