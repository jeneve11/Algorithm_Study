# 184. Department Highest Salary
# Difficulty: Medium
# https://leetcode.com/problems/department-highest-salary/
# 220811

SELECT B.department_name AS 'Department', A.name AS 'Employee', A.salary AS 'Salary'
FROM Employee A INNER JOIN (
    SELECT D.id AS 'id', MAX(E.salary) AS 'max_salary', D.name AS 'department_name'
    FROM Employee E INNER JOIN Department D
    ON E.departmentId = D.id
    GROUP BY D.id
) B
ON A.departmentID = B.id
WHERE salary = max_salary