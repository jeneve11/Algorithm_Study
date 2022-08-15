# 626. Exchange Seats
# Difficulty: Medium
# https://leetcode.com/problems/exchange-seats/
# 220812

SELECT IF(id%2=0, id-1, IF(LEAD(id, 1) OVER (ORDER BY id ASC) IS NULL, id, id+1)) AS 'id', student
FROM Seat
ORDER BY id ASC