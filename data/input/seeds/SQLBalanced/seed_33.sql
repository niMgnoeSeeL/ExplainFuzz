SELECT dep_id, COUNT(id) AS n_projects FROM projects GROUP BY dep_id ORDER BY n_projects USING >, dep_id USING <;
