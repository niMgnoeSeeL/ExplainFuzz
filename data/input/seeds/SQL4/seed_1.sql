SELECT dep_number, AVG(dep_budget) FROM departments GROUP BY dep_number HAVING AVG(dep_budget) > 400000;
