SELECT email FROM employees WHERE EXISTS (SELECT 1 FROM departments WHERE departments.dep_number = employees.department_id AND departments.dep_budget > 400000);
