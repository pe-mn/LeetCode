# Write your MySQL query statement below

SELECT customer_id, COUNT(customer_id) AS count_no_trans FROM Visits
WHERE visit_id NOT IN (SELECT DISTINCT visit_id FROM Transactions)
GROUP BY customer_id

# SELECT 
#     V.customer_id, 
#     COUNT(DISTINCT V.visit_id) AS count_no_trans
# FROM Visits V
# WHERE V.visit_id NOT IN (SELECT visit_id FROM Transactions)
# GROUP BY V.customer_id