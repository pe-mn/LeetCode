# Write your MySQL query statement below

SELECT firstName, lastName, city, state
FROM Person LEFT JOIN Address USING(personId)

# -------------------------------------------------------------------------------------

# Error: Duplicate column name 'personId'
# Because both tables have a personId column. 
# And Because you say select *, you're getting two columns named personId, 
# and SQL doesn't know which one personId refers to.
# This can be solved by Using(personId) instead of ON p.personId = a.personId
# Or by removing the other select statement.

# SELECT firstName, lastName, city, state
# FROM (SELECT * FROM Person LEFT JOIN Address Using(personId)) T

# SELECT firstName, lastName, city, state
# FROM Person P LEFT JOIN Address A ON (P.personId = A.personId);

