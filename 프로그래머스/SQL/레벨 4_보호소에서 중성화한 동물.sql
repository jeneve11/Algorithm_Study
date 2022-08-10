# 프로그래머스_레벨 4_보호소에서 중성화한 동물
# 220810

SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
FROM ANIMAL_OUTS O INNER JOIN ANIMAL_INS I
ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE SEX_UPON_INTAKE LIKE '%INTACT%' AND (SEX_UPON_OUTCOME LIKE '%SPAYED%' OR SEX_UPON_OUTCOME LIKE '%NEUTERED%')
ORDER BY ANIMAL_ID