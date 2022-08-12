# 608. Tree Node
# Difficulty: Medium
# https://leetcode.com/problems/tree-node/
# 220812

SELECT id, IF(p_id IS NULL, 'Root',
    IF(id NOT IN (
    SELECT DISTINCT p_id
    FROM Tree
    WHERE p_id IS NOT NULL
), 'Leaf', 'Inner')) AS 'type'
FROM TREE