# Write your MySQL query statement below

# Need to left join the users and the rides table. Hence, even there is no travelling record for a particular user, that user is still listed in the output table.
# Use IFNULL since the non-travelling one will return null when joining.
 
SELECT name, IFNULL(SUM(distance), 0) AS travelled_distance
FROM Users LEFT JOIN Rides ON Users.id = Rides.user_id
GROUP BY user_id 
ORDER BY travelled_distance DESC, name

# ----------------------------------------------------------------------------

# # -- using left outer join
# select u.name, isnull(sum(r.distance),0) as travelled_distance
# from users u left outer join rides r
# on u.id = r.user_id
# group by u.name
# order by travelled_distance desc, name asc


# # --using coorelated sub-query
# select u.name, (select isnull(sum(r.distance),0)
#                 from rides r
#                 where u.id = r.user_id) as travelled_distance
# from users u
# order by travelled_distance desc, name asc

# --using cte
# -----------
# with cte
# as
# (
#     select r.user_id, sum(r.distance) as travelled_distance
#     from rides r
#     group by r.user_id
# )
#     select u.name, isnull(c.travelled_distance,0) as travelled_distance
#     from users u left outer join cte c
#     on u.id = c.user_id
#     order by travelled_distance desc, name asc