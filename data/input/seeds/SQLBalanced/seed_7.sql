SELECT department_name, SUBSTRING(location FROM 1 FOR 5) AS location_prefix FROM departments ORDER BY location_prefix USING >, id USING <;
