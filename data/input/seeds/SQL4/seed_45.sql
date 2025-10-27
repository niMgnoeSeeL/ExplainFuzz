SELECT location, COUNT(proj_number) FROM departments JOIN projects ON projects.dep_id = departments.dep_number GROUP BY location HAVING COUNT(proj_number) > 2;
