SELECT dep_id, COUNT(proj_number) FROM projects GROUP BY dep_id HAVING COUNT(proj_number) > 2;
