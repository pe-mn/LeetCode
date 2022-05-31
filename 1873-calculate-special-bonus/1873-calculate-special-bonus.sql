# Write your MySQL query statement below

SELECT employee_id, 
# IF(condition, value_if_true, value_if_false)
IF(employee_id%2=1 and name not like 'M%',salary,0) 
AS bonus FROM employees
# ORDER BY employee_id; ALREADY ORDERED

# SELECT employee_id,
# CASE
#     WHEN employee_id%2=1 AND SUBSTRING(name, 1,1) <> 'M' 
#     THEN salary
#     ELSE 0
# END AS bonus
# FROM Employees
# ORDER BY employee_id;