# 프로그래머스_레벨 2_고양이와 개는 몇 마리 있을까
# 220809

SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE