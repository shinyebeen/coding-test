SELECT INFO.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO INFO 
JOIN REST_REVIEW AS REVIEW
ON INFO.REST_ID = REVIEW.REST_ID
GROUP BY INFO.REST_ID
HAVING ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, INFO.FAVORITES DESC;
    