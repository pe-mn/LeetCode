# Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary, the query should report null.

# filter out the max
# USE < OR <> OR NOT IN

# SELECT MAX(salary) AS SecondHighestSalary FROM Employee
# WHERE salary < (SELECT MAX(salary) FROM Employee)

# SELECT MAX(salary) AS SecondHighestSalary 
# FROM (SELECT salary FROM Employee WHERE salary < 
#       (SELECT MAX(salary) FROM Employee)) T
      
#----------------------------------------------------------------------------------
      
# No need of sub queries,
# just skip one row and select second rows after order by descending
# ------------------------
# SELECT salary AS SecondHighestSalary
# FROM Employee
# ORDER BY salary DESC 
# LIMIT 1 
# OFFSET 1

# SELECT DISTINCT salary AS SecondHighestSalary
# FROM Employee
# ORDER BY salary DESC 
# LIMIT 1, 1

# However, this solution will be judged as 'Wrong Answer' if there is no such second highest salary since there might be only one record in this table. To overcome this issue, we can take this as a temp table.

#----------------------------------------------------------------------------------

SELECT
    (SELECT DISTINCT Salary FROM Employee
     ORDER BY Salary DESC
     LIMIT 1, 1) AS SecondHighestSalary

# SELECT
#     IFNULL(
#       (SELECT DISTINCT Salary
#        FROM Employee
#        ORDER BY Salary DESC
#         LIMIT 1 OFFSET 1),
#     NULL) AS SecondHighestSalary