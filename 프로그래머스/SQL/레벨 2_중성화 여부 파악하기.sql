# 프로그래머스_레벨 2_중성화 여부 파악하기
# 220810

SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE '%NEUTERED%' or SEX_UPON_INTAKE LIKE '%SPAYED%', 'O', 'X') AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID