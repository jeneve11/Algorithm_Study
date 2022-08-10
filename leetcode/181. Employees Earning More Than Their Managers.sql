# 181. Employees Earning More Than Their Managers
# Difficulty: Easy
# https://leetcode.com/problems/employees-earning-more-than-their-managers/
# 220810

SELECT A.name AS Employee
FROM Employee A INNER JOIN Employee B
ON A.managerId = B.id
WHERE A.salary > B.salary