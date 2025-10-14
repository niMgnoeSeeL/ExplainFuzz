SELECT id, project_name, budget FROM projects WHERE budget > 400000 ORDER BY budget USING >, id USING <;
