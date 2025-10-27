SELECT proj_number FROM projects WHERE project_name = 'proj' UNION SELECT dep_number FROM departments WHERE dep_budget > 400000;
