# Write your MySQL query statement below

# # Wrong Answer !!! 
# # "rows": {"Weather": [[1, "2000-12-16", 3], [2, "2000-12-15", -1]]}}


# SELECT W1.id FROM Weather W1, Weather W2 
# WHERE (W1.id - W2.id) = 1 AND W1.temperature > W2.temperature


# SELECT W1.id FROM Weather W1 JOIN Weather W2 
# ON (W1.id - W2.id) = 1 AND W1.temperature > W2.temperature

# -------------------------------------------------------------

# # METHOD 1 (DATE_SUB)
# SELECT W1.id FROM Weather W1 JOIN Weather W2 
# ON W2.recordDate = DATE_SUB(W1.recordDate,interval 1 DAY)
# WHERE W1.temperature > W2.temperature

# SELECT W1.id FROM Weather W1, Weather W2 
# WHERE W2.recordDate = DATE_SUB(W1.recordDate,interval 1 DAY)
# AND W1.temperature > W2.temperature

# -------------------------------------------------------------

# # METHOD 2 (DATEDIFF)
# SELECT W1.id FROM weather W1, weather W2 
# WHERE DATEDIFF(W1.recordDate,W2.recordDate)=1 
# AND W1.temperature>W2.temperature;

# -------------------------------------------------------------

# # METHOD 3 (DATE_ADD)
# SELECT W1.id FROM Weather W2, Weather W1 
# WHERE W1.recordDate = DATE_ADD(W2.recordDate, INTERVAL 1 DAY) 
# AND W1.Temperature > W2.Temperature;

# -------------------------------------------------------------

# # METHOD 4 (TO_DAYS)
SELECT W1.id FROM Weather W2, Weather W1 
WHERE TO_DAYS(W1.recordDate) - TO_DAYS(W2.recordDate) = 1
AND W1.Temperature > W2.Temperature;

# -------------------------------------------------------------

# # Wrong Answer
# SELECT W1.id FROM Weather W2, Weather W1 
# WHERE W1.recordDate - W2.recordDate = 1
# AND W1.Temperature > W2.Temperature;








