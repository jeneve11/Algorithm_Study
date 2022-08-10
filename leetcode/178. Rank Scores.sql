# 178. Rank Scores
# Difficulty: Medium
# https://leetcode.com/problems/rank-scores/
# 220810

SELECT score, DENSE_RANK() OVER (ORDER BY SCORE DESC) AS 'rank'
FROM Scores