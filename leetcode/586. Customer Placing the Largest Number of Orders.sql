# 586. Customer Placing the Largest Number of Orders
# Difficulty: Easy
# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
# 220811

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1