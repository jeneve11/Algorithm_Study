# 620. Not Boring Movies
# Difficulty: Easy
# https://leetcode.com/problems/not-boring-movies/
# 220811

SELECT *
FROM Cinema
WHERE id % 2 = 1 AND description != 'boring'
ORDER BY rating DESC