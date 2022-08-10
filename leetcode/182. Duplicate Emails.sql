# 182. Duplicate Emails
# Difficulty: Easy
# https://leetcode.com/problems/duplicate-emails/
# 220810

SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1