# Write your MySQL query statement below

SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins 
WHERE YEAR(time_stamp) = 2020 
GROUP BY user_id

# ----------------------------------------------------------

# SYNTAX ERROR
# GROUP BY --> HAVING
# ----------------------------------------------
# SELECT user_id, MAX(time_stamp) AS last_stamp
# FROM Logins GROUP BY user_id
# WHERE YEAR(time_stamp) = 2020

# ----------------------------------------------------------

# Wrong Answer
# WE NEED TO FILTER FIRST ON 2020 THEN REPORT THE LATEST LOGIN
# IF WE DID THE THE OPPOSITE WE ARE GOING TO MISS SOME USERS 
# WHO ACTUALLY LOGGED IN 2020
# -------------------------------------------------------------
# SELECT user_id, MAX(time_stamp) AS last_stamp
# FROM Logins GROUP BY user_id
# HAVING YEAR(last_stamp) = 2020