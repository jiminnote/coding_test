
-- 조건:2번 형질이 보유하지 않으면서 1번이나 3번 형질을 보유하고 있는 대장균 개체의 수(COUNT)를 출력
-- 테이블: ECOLI_DATA

SELECT
  COUNT(*) AS COUNT  
FROM ECOLI_DATA  
WHERE  
  (GENOTYPE & 2) = 0             -- 2번 형질이 없는 경우  
  AND (
    (GENOTYPE & 1) = 1           -- 1번 형질이 있는 경우
    OR (GENOTYPE & 4) = 4        -- 3번 형질이 있는 경우
  )