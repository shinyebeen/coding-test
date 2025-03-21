SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d')
FROM REST_REVIEW R
     JOIN MEMBER_PROFILE M
     ON M.MEMBER_ID = R.MEMBER_ID
WHERE M.MEMBER_ID = (SELECT MEMBER_ID
                     FROM REST_REVIEW
                     GROUP BY MEMBER_ID
                     ORDER BY COUNT(MEMBER_ID) DESC
                     LIMIT 1)
ORDER BY REVIEW_DATE, REVIEW_TEXT;