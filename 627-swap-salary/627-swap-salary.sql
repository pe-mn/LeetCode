# Write your MySQL query statement below

# The ENUM data type in MySQL is a string object. It allows us to limit the value chosen from a list of permitted values in the column specification at the time of table creation. 
# It is short for enumeration, which means that each column may have one of the specified possible values. It uses numeric indexes (1, 2, 3…) to represent string values.

# It is mainly used to assign names to integral constants, the names make a program easy to read and maintain.

# IF(condition, value_if_true, value_if_false)
UPDATE Salary SET sex = IF(sex = 'f' , 'm','f');

# UPDATE salary SET sex =
# CASE
# WHEN sex = 'm' THEN 'f'
# WHEN sex = 'f' THEN 'm'
# # ELSE sex
# END