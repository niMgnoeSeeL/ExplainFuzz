SELECT projects.project_name, budget FROM projects WHERE budget > 350000 ORDER BY budget USING >, id USING <;
