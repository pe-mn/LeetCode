# Write your MySQL query statement below

# use WHERE before GROUP BY
# but HAVING after GROUP BY

# # COUNT(DISTINCT(session_id)) --> (WRONG ANSWER)
# # AS THE SAME USER MAY OPEN MORE THAN ONE SESSION PER DAY
# ----------------------------------------------------------
# SELECT activity_date AS day, 
# COUNT(DISTINCT(user_id)) AS active_users
# FROM Activity 
# WHERE DATEDIFF('2019-07-27', activity_date) <30
# AND activity_date <= '2019-07-27'
# GROUP BY activity_date

# # A user was active on someday if they made at least one activity on that day.
# HAVING Count(*) > 2

# # Explanation: Note that we do not care about days with zero active users.
# # 2019-06-25 IS NOT COUNTED AS IT'S NOT WITHIN THE 30 days PERIOD

# ----------------------------------------------------------------------

SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
GROUP BY activity_date
HAVING activity_date <= '2019-07-27' 
AND activity_date > '2019-06-27'
