# 176. Second Highest Salary
# Difficulty: Medium
# https://leetcode.com/problems/second-highest-salary/submissions/
# 220810

SELECT IF(COUNT(*) = 1, salary, NULL) AS 'SecondHighestSalary'
FROM (
    SELECT salary
    FROM Employee
    GROUP BY salary
    ORDER BY salary DESC
    LIMIT 1, 1
) A