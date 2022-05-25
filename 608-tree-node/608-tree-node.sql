# Write your MySQL query statement below

# https://intellipaat.com/community/3903/difference-between-exists-and-in-in-sql#:~:text=LacieSmith%20(140%20points)-,EXISTS%20is%20used%20to%20determine%20if%20any%20values%20are%20returned,Engine%20will%20stop%20the%20process.

SELECT id, 'Root' AS type FROM Tree WHERE p_id IS NULL
UNION 
SELECT id, 'Inner' AS type FROM Tree T
    WHERE EXISTS(SELECT DISTINCT(p_id) FROM Tree WHERE p_id = T.id) 
    AND p_id IS NOT NULL
UNION 
SELECT id, 'Leaf' AS type FROM Tree T
    WHERE NOT EXISTS(SELECT DISTINCT(1) FROM Tree WHERE p_id = T.id) 
    AND p_id IS NOT NULL

# -----------------------------------------------------------------------------------

# select id,
# case
#     when p_id is null then 'Root'
#     when id in (select p_id from Tree) then 'Inner'
#     else 'Leaf'
# end as type
# from Tree
# order by id;

# -----------------------------------------------------------------------------------

# SELECT tree.id, 
# # TWO IFs ONE INSIDE ANOTHER
# IF(ISNULL(tree.p_id),'Root', 
# # IF(CONDITION, VALUE WHEN TRUE, VALUE WHEN FALSE)
# IF(tree.id IN (SELECT DISTINCT(p_id) FROM tree), 'Inner','Leaf')) Type 
# FROM tree ORDER BY tree.id



