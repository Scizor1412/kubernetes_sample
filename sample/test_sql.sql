-- employees (id int, name varchar(255), department_id int, salary bigint)
-- departments (id int, name varchar(255))
WITH CTE AS (
    SELECT e.name, d.name, e.salary, ROW_NUMBER() OVER (PARTITION BY d.id ORDER BY e.salary DESC) AS rownum
    FROM employees e
    JOIN departments d ON e.department_id = d.id
)
SELECT *
FROM CTE 
WHERE rownum = 2
ORDER BY salary