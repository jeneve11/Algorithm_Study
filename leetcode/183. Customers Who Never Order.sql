# 183. Customers Who Never Order
# Difficulty: Easy
# https://leetcode.com/problems/customers-who-never-order/
# 220810

SELECT name AS Customers
FROM Customers C LEFT OUTER JOIN Orders O
ON C.id = O.customerId
WHERE O.id IS NULL