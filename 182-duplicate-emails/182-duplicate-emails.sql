# Write your MySQL query statement below

# FASTEST
# ----------
select Email
from Person
group by Email
having count(*) > 1


# SELECT DISTINCT(P1.email) FROM Person P1, Person P2
# WHERE P1.email = P2.email
# AND P1.id <> P2.id


# SELECT distinct p1.Email FROM Person p1
# INNER JOIN Person p2
# ON p1.Email = p2.Email
# WHERE p1.Id <> p2.Id;