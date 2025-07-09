-- 조건:
--  FISH_TYPE이 4, 5가 아닌 것
--  LENGTH는 내림차순,
--  동일 길이일 경우 ID는 오름차순
--  상위 10마리만 출력
-- 테이블: FISH_INFO

SELECT ID,LENGTH FROM FISH_INFO 
    WHERE ID NOT IN (4,5) 
    ORDER BY LENGTH DESC, ID ASC
    LIMIT 10;