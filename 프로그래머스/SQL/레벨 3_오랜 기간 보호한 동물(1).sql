# 프로그래머스_레벨 3_오랜 기간 보호한 동물(1)
# 220810

SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I LEFT JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME
LIMIT 3