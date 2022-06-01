# Write your MySQL query statement below

SELECT sell_date, COUNT(DISTINCT(product)) AS num_sold,
GROUP_CONCAT(DISTINCT(product)) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date

# SELECT sell_date, COUNT(DISTINCT(product)) AS num_sold,
# GROUP_CONCAT(DISTINCT(product) ORDER by product SEPARATOR ',') AS products
# FROM Activities
# GROUP BY 1
# ORDER BY 1