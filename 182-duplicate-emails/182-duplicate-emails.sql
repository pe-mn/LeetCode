# Write your MySQL query statement below

# select Email
# from Person
# group by Email
# having count(*) > 1


SELECT DISTINCT(P1.email) FROM Person P1, Person P2
WHERE P1.email = P2.email
AND P1.id <> P2.id