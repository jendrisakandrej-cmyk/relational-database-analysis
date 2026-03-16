import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="your_password",
    database="pixar_movies",
    port=3306
)

cursor = conn.cursor()

# 1. What is the average user score per Pixar movie?
query = """
SELECT m.movieTitle, AVG(r.score) AS avg_score
FROM movies m
JOIN reviews r ON m.movieId = r.movieId
GROUP BY m.movieTitle;
"""

cursor.execute(query)
rows = cursor.fetchall()

print("Average user score per Pixar movie:")
for row in rows:
    print(row)

# 2. What is the average user score for Toy Story?
query = """
SELECT AVG(r.score)
FROM reviews r
JOIN movies m ON r.movieId = m.movieId
WHERE m.movieTitle = 'Toy Story';
"""

cursor.execute(query)
result = cursor.fetchone()

print("\nAverage user score for Toy Story:")
print(result[0])

# 3. How many user reviews does each Pixar movie have?
query = """
SELECT m.movieTitle, COUNT(*) AS review_count
FROM reviews r
JOIN movies m ON r.movieId = m.movieId
GROUP BY m.movieTitle;
"""

cursor.execute(query)
rows = cursor.fetchall()

print("\nNumber of user reviews per Pixar movie:")
for row in rows:
    print(row)

# 4. What is the average number of reviews per Pixar movie?
query = """
SELECT AVG(review_count)
FROM (
    SELECT COUNT(*) AS review_count
    FROM reviews
    GROUP BY movieId
) t;
"""

cursor.execute(query)
result = cursor.fetchone()

print("\nAverage number of reviews per Pixar movie:")
print(result[0])

conn.close()



