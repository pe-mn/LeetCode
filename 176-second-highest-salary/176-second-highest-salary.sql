# Write your MySQL query statement below

SELECT MAX(salary) AS SecondHighestSalary 
FROM (SELECT salary FROM Employee WHERE salary < 
      (SELECT MAX(salary) FROM Employee)) T
 
# ------------------------------------------------------------------------------------

# SELECT MAX(SALARY) AS SecondHighestSalary
# FROM EMPLOYEE
# WHERE SALARY<(SELECT MAX(SALARY) FROM EMPLOYEE);
 
# ------------------------------------------------------------------------------------

# SELECT DISTINCT SALARY AS SecondHighestSalary
# FROM EMPLOYEE 
# ORDER BY SALARY DESC
# LIMIT 1
# OFFSET 1;