SELECT dep_id, COUNT(id) FROM projects GROUP BY dep_id HAVING COUNT(id) > 2;
