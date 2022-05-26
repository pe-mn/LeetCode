# Write your MySQL query statement below

# SELECT customer_id, COUNT(customer_id) AS count_no_trans FROM Visits
# WHERE visit_id NOT IN (SELECT DISTINCT visit_id FROM Transactions)
# GROUP BY customer_id

# SELECT customer_id, COUNT(visit_id) AS count_no_trans FROM Visits 
# WHERE visit_id NOT IN (SELECT DISTINCT visit_id FROM Transactions)
# GROUP BY customer_id

SELECT customer_id, COUNT(visit_id) AS count_no_trans 
FROM Visits LEFT JOIN Transactions USING(visit_id)
WHERE transaction_id IS NULL
GROUP BY customer_id