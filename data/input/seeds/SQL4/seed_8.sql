SELECT dep_id, AVG(budget) FROM projects GROUP BY dep_id HAVING AVG(budget) > 300000;
