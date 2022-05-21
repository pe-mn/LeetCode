# Write your MySQL query statement below

/* Not Equal Operator: !=
Evaluates both SQL expressions and returns 1 if they are not equal and 0 if they are equal, or NULL if either expression is NULL. If the expressions return different data types, (for instance, a number and a string), performs type conversion.*/

# SELECT name FROM Customer
# WHERE referee_id != 2
# OR referee_id is null

SELECT name FROM Customer
WHERE referee_id <> 2
OR referee_id is null

# SELECT name from Customer
# WHERE id not in (
#     SELECT id FROM Customer 
#     WHERE referee_id=2);