# 175. Combine Two Tables
# Difficulty: Easy
# https://leetcode.com/problems/combine-two-tables/
# 220810

SELECT P.firstName, P.lastNAme, A.city, A.state
FROM Person P LEFT OUTER JOIN Address A
ON P.personId = A.personId