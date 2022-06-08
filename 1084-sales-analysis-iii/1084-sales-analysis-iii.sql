# only
# the products that were only sold in the first quarter of 2019

# Write your MySQL query statement below

SELECT s.product_id, product_name 
FROM Sales s LEFT JOIN Product p USING(product_id)
GROUP BY s.product_id
HAVING MIN(sale_date) >= CAST('2019-01-01' AS DATE) AND
       MAX(sale_date) <= CAST('2019-03-31' AS DATE)
       
       
# SELECT P.product_id, product_name 
# FROM Product P LEFT JOIN Sales S USING(product_id)
# GROUP BY P.product_id
# HAVING MIN(sale_date) >= CAST('2019-01-01' AS DATE) AND
#        MAX(sale_date) <= CAST('2019-03-31' AS DATE)


# Wrong AnswerS
# --------------
# SELECT P.product_id, P.product_name
# FROM Product P LEFT JOIN Sales S USING(product_id)
# WHERE sale_date BETWEEN 2019-01-01 and 2019-03-31


# SELECT P.product_id, P.product_name
# FROM Product P LEFT JOIN Sales S USING(product_id)
# WHERE sale_date >= '2019-01-01' AND sale_date <= '2019-03-31'


# SELECT P.product_id, P.product_name
# FROM Product P LEFT JOIN Sales S ON P.product_id = S.product_id AND sale_date >= '2019-01-01' AND sale_date <= '2019-03-31' 