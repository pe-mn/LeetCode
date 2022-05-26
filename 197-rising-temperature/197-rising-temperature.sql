# Write your MySQL query statement below

# # Wrong Answer !!! 
# # "rows": {"Weather": [[1, "2000-12-16", 3], [2, "2000-12-15", -1]]}}


# SELECT W1.id FROM Weather W1, Weather W2 
# WHERE (W1.id - W2.id) = 1 AND W1.temperature > W2.temperature


# SELECT W1.id FROM Weather W1 JOIN Weather W2 
# ON (W1.id - W2.id) = 1 AND W1.temperature > W2.temperature

# -------------------------------------------------------------

# SELECT W1.id FROM Weather W1 JOIN Weather W2 
# ON W2.recordDate = DATE_SUB(W1.recordDate,interval 1 DAY)
# WHERE W1.temperature > W2.temperature

# -------------------------------------------------------------

SELECT W1.id FROM weather W1, weather W2 
WHERE datediff(W1.recordDate,W2.recordDate)=1 
AND W1.temperature>W2.temperature;

# -------------------------------------------------------------

# SELECT w2.id FROM Weather w1, Weather w2 
# WHERE w2.recordDate = DATE_ADD(w1.recordDate, INTERVAL 1 DAY) 
# AND w2.Temperature > w1.Temperature;








