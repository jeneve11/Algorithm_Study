# 프로그래머스_레벨 1_이름이 없는 동물의 아이디
# 220810

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID ASC