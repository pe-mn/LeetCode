# Write your MySQL query statement below

# # Using UNION + Where_Not_In
# SELECT employee_id FROM Employees WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
# UNION
# SELECT employee_id FROM Salaries WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
# ORDER BY employee_id;

#------------------------------------------------------------------------------------

# Using Full Outer Join # T-->Temporary Table
SELECT T.EMPLOYEE_ID
FROM(
    SELECT * FROM EMPLOYEES LEFT JOIN SALARIES USING(EMPLOYEE_ID)
    UNION
    SELECT * FROM EMPLOYEES RIGHT JOIN SALARIES USING(EMPLOYEE_ID)
) T
WHERE T.SALARY IS NULL OR T.NAME IS NULL
ORDER BY T.EMPLOYEE_ID;

# The first subquery produces the list of names in the two tables. The LEFT JOINs will always match. So, this produces the same output as a FULL JOIN, including (unwanted) duplicates.