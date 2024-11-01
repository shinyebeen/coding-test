SELECT O.PRODUCT_ID, PRODUCT_NAME, SUM(AMOUNT * PRICE) AS TOTAL_SALES
FROM FOOD_ORDER O
JOIN FOOD_PRODUCT P
ON O.PRODUCT_ID = P.PRODUCT_ID
WHERE PRODUCE_DATE LIKE '2022-05%'
GROUP BY PRODUCT_ID
ORDER BY TOTAL_SALES DESC, O.PRODUCT_ID;