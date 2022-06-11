-- Success case {"headers": {"Employee": ["id", "name", "salary", "departmentId"], "Department": ["id", "name"]}, "rows": {"Employee": [[1, "Joe", 70000, 1], [2, "Jim", 90000, 1], [3, "Henry", 80000, 2], [4, "Sam", 60000, 2], [5, "Max", 90000, 1]], "Department": [[1, "IT"], [2, "Sales"]]}}
-- Borked case {"headers": {"Employee": ["id", "name", "salary", "departmentId"], "Department": ["id", "name"]}, "rows": {"Employee": [[1, "Joe", 60000, 1], [2, "Sam", 50000, 1], [4, "Max", 50000, 2]], "Department": [[1, "IT"], [2, "HR"]]}}

SELECT Department.name AS "Department", 
Employee.name AS "Employee", salary AS "Salary"
FROM Employee 
INNER JOIN Department ON Employee.departmentId = Department.id
WHERE salary IN (
    SELECT MAX(salary) FROM Employee GROUP BY departmentId
)

