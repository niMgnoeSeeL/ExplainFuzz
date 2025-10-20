SELECT proj_number, project_name, budget FROM projects WHERE budget > 400000 ORDER BY budget USING >, proj_number USING <;
