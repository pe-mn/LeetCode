# Write your MySQL query statement below

# Interesting solution...to explain for others...
# The first inner join creates a view for just 'RED' orders
# The right join ensures all salespersons are included (even those who do not have RED orders)
# The WHERE IS NULL gives salespersons who did not have any RED orders due to the right join

# SELECT S.name
# FROM Orders O JOIN Company C ON (O.com_id = C.com_id AND C.name = 'RED')
# RIGHT JOIN SalesPerson S USING(sales_id)
# WHERE O.sales_id IS NULL

# --------------------------------------------------------------------------------

# SELECT name FROM salesperson
# WHERE sales_id NOT IN 
# (
#    SELECT sales_id FROM orders WHERE com_id IN 
# 	(SELECT com_id FROM company WHERE name='RED')
# )



SELECT name FROM salesperson
WHERE sales_id NOT IN (SELECT sales_id FROM orders 
                       LEFT JOIN company USING(com_id)  
                       WHERE company.name='RED')
      
# --------------------------------------------------------------------------------
      
# select s.name from
# salesperson s
# left join orders o USING(sales_id)
# left join company c USING(com_id)
# group by s.name
# having count(order_id)=0 or not sum(c.name='RED')>0

# --------------------------------------------------------------------------------

# SELECT s.name FROM salesperson s
# LEFT JOIN orders o USING (sales_id)
# LEFT JOIN company c USING (com_id)
# GROUP BY sales_id
# HAVING SUM(CASE c.name WHEN 'RED' THEN 1 ELSE 0 END)=0

