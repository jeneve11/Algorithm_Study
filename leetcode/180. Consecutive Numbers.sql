# 180. Consecutive Numbers
# Difficulty: Medium
# https://leetcode.com/problems/consecutive-numbers/
# 220812
# LAG, LEAD 함수 이용

SELECT DISTINCT num AS 'ConsecutiveNums'
FROM (
    SELECT num, LAG(num, 1) OVER (ORDER BY id ASC) AS 'prev', LEAD(num, 1) OVER (ORDER BY id ASC) AS 'next'
    FROM Logs
) A
WHERE num = prev and num = next