-- 조건: NULL인 데이터는 10으로 계산 / 평균값 / 반올림하여 소수점 둘째자리까지
-- 테이블: FISH_INFO

SELECT ROUND(AVG(COALESCE(LENGTH,10)),2) AS AVERAGE_LENGTH FROM FISH_INFO ;

