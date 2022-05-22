# Write your MySQL query statement below

SELECT *
FROM Patients
WHERE conditions LIKE('% DIAB1%') 
OR conditions LIKE 'DIAB1%'

#------------------------------------------------------------------------------------

# SELECT * FROM patients WHERE conditions REGEXP '\\bDIAB1'