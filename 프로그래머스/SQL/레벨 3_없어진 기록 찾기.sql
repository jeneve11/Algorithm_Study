# 프로그래머스_레벨 3_없어진 기록 찾기
# 220810
# 서브쿼리 말고 그냥 JOIN으로도 풀 수 있을 거 같은데..

SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID NOT IN (
    SELECT ANIMAL_ID
    FROM ANIMAL_INS
)
ORDER BY ANIMAL_ID