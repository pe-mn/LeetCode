# Write your MySQL query statement below

# SELECT name as Customers FROM Customers  
# WHERE id NOT IN(SELECT customerId FROM Orders)

SELECT c.name AS Customers
FROM Customers c left join Orders o on c.id = o.customerId
WHERE o.customerId is null