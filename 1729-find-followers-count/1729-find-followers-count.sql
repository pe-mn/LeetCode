# Write your MySQL query statement below
SELECT user_id, COUNT(follower_id) AS followers_count
FROM Followers GROUP BY user_id ORDER BY user_id;


# Since (user_id, follower_id) is a primary key, I'm assuming follower_id is already distinct per user_id. So is distinct necessary here?