# Write your MySQL query statement below

# # WRONG ANSWERS (CORRECTED)
# ----------------------------
# https://www.quora.com/Why-is-SQL-left-join-not-returning-all-results-when-the-second-table-is-in-WHERE-statement-MySQL-SQL-select-left-join-where-clause-development

# A left join searches all rows that fulfil the join condition plus all rows of the first (left) table for which no matching rows of the second (right) table exist, and fills those columns whith NULL.

# The where condition is (logically) applied to this query result. That implies if you have anything in the “where” condition that checks columns of the second table, this condition will never be fulfilled by those NULL columns, so those rows are all eliminated.

# Solution: move those WHERE conditions into the LEFT JOIN condition.

# That’s a general rule. If you have more than one joins, if any of them references a table column a right table in a LEFT join before that join, this join must be a LEFT JOIN as well.

# CORRECT:
# ----------
SELECT S.name FROM 
Orders O JOIN Company C ON (O.com_id = C.com_id AND C.name = 'RED') 
RIGHT JOIN SalesPerson S USING(sales_id)
WHERE O.sales_id IS NULL

# WRONG ANSWER:
# BECAUSE WE DID A LEFT JOIN BEFORE FILTERING 'RED' 
# -------------
# SELECT S.name FROM 
# SalesPerson S LEFT JOIN  Orders O USING(sales_id) 
# LEFT JOIN Company C ON (O.com_id = C.com_id AND C.name = 'RED')  
# WHERE O.sales_id IS NULL

# --------------------------------------------------------------------------------

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

# --------------------------------------------------------------------------------

# SELECT name FROM salesperson
# WHERE sales_id NOT IN (SELECT sales_id FROM orders 
#                        LEFT JOIN company USING(com_id)  
#                        WHERE company.name='RED')
      
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