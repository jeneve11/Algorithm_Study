# 584. Find Customer Referee
# Difficulty: Easy
# https://leetcode.com/problems/find-customer-referee/
# 220811
# EVERYTHING compared with 'NULL' returns 'UNKNOWN', not 'TRUE' or 'FALSE'

SELECT name
FROM Customer
WHERE IFNULL(referee_id, 0) != 2