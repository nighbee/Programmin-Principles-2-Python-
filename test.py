import psycopg2
conn = psycopg2.connect(
    database= "snakeuser",
    user= "postgres",
    password= "72zv5u3xp"
)
# creating cursor
cur= conn.cursor()
cur.execute("Select*from scores")
rows = cur.fetchall()
for row in rows:
    print(f"{row[0]} - {row[1]} {row[2]} {row[3]}")