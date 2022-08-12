# 607. Sales Person
# Difficulty: Easy
# https://leetcode.com/problems/sales-person/
# 220812

SELECT S.name
FROM SalesPerson S
WHERE S.sales_id NOT IN (
    SELECT O.sales_id
    FROM Orders O INNER JOIN company C
    ON O.com_id = C.com_id
    WHERE C.name = 'RED'
)