# 596. Classes More Than 5 Students
# Difficulty: Easy
# https://leetcode.com/problems/classes-more-than-5-students/
# 220811

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5