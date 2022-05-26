# Write your MySQL query statement below

# SELECT DISTINCT author_id AS id FROM Views
# WHERE author_id = viewer_id
# ORDER BY id

# -----------------------------------------------------

SELECT DISTINCT V1.author_id AS id 
FROM Views V1 JOIN Views V2
ON V1.author_id = V2.viewer_id AND V1.article_id = V2.article_id
ORDER BY id

# -----------------------------------------------------

# SELECT author_id AS id FROM Views
# WHERE author_id = viewer_id
# GROUP BY author_id
# ORDER BY id