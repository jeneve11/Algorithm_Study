# 511. Game Play Analysis I
# Difficulty: Easy
# https://leetcode.com/problems/game-play-analysis-i/
# 220810

SELECT player_id, MIN(event_date) AS 'first_login'
FROM Activity
GROUP BY player_id