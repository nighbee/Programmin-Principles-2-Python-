import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database="movieGo",
    user="postgres",
    password="72zv5u3xp"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Create the database
# cur.execute("CREATE DATABASE Database_labka")
cur.execute("""
    CREATE TABLE users (
        StudentID SERIAL PRIMARY KEY,
        email VARCHAR(50),
        password VARCHAR(50)
    )
""")
conn.commit()

cur.close()
conn.close()