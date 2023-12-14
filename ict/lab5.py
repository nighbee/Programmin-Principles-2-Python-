import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database="ictnew",
    user="postgres",
    password="72zv5u3xp"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Create the database
# cur.execute("CREATE DATABASE Database_labka")

# Switch to the newly created database
# cur.execute("USE Database_labka")

# Begin a transaction
# cur.execute("BEGIN TRANSACTION")

# Create the Students_labka table
cur.execute("""
    CREATE TABLE Students_labka (
        StudentID SERIAL PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50)
    )
""")

# Create the Courses_labka table
cur.execute("""
    CREATE TABLE Courses_labka (
        CourseID SERIAL PRIMARY KEY,
        CourseName VARCHAR(50)
    )
""")

# Create the Grades_labka table
cur.execute("""
    CREATE TABLE Grades_labka (
        GradeID SERIAL PRIMARY KEY,
        StudentID INT,
        CourseID INT,
        Grade INT,
        GradeCategoryO VARCHAR(50),
        FOREIGN KEY (StudentID) REFERENCES Students_labka(StudentID),
        FOREIGN KEY (CourseID) REFERENCES Courses_labka(CourseID)
    )
""")

# Insert data into the Students_labka table
students = [
    ('Ivan', 'Ivanov'),
    ('Elena', 'Petrova'),
    ('Alexey', 'Sidorov'),
    ('Olga', 'Novikova'),
    ('Sergey', 'Mikhailov'),
    ('Anna', 'Kuznetsova'),
    ('Dmitry', 'Kovalev'),
    ('Ekaterina', 'Belova'),
    ('Mikhail', 'Vasnetsov'),
    ('Alina', 'Solovyeva'),
    ('Nikolay', 'Zaytsev'),
    ('Tatiana', 'Popova'),
    ('Pavel', 'Lebedev'),
    ('Marina', 'Semenova'),
    ('Grigory', 'Morozov'),
    ('Evgenia', 'Volkova'),
    ('Artem', 'Orlov'),
    ('Irina', 'Koroleva'),
    ('Roman', 'Kozlov'),
    ('Natalia', 'Antonova'),
    ('Andrey', 'Krylov'),
    ('Yulia', 'Fedorova'),
    ('Sergey', 'Isaev'),
    ('Kristina', 'Polyakova'),
    ('Anton', 'Tarasov'),
    ('Larisa', 'Sergeeva'),
    ('Denis', 'Nikolaev'),
    ('Victoria', 'Grigorieva'),
    ('Ruslan', 'Vorobev')
    # Add more student records here
]

cur.executemany("INSERT INTO Students_labka (FirstName, LastName) VALUES (%s, %s)", students)

# Insert data into the Courses_labka table
courses = [
    ('Mathematics',),
    ('History',),
    ('English',),
    # Add more course records here
]

cur.executemany("INSERT INTO Courses_labka (CourseName) VALUES (%s)", courses)

# Insert data into the Grades_labka table
grades = [
    # Grades for Mathematics
    (1, 1, 85),
    (2, 1, 70),
    (3, 1, 92),
    (4, 1, 78),
    (5, 1, 88),
    (6, 1, 75),
    (7, 1, 90),
    (8, 1, 82),
    (9, 1, 95),
    (10, 1, 68),
    (11, 1, 89),
    (12, 1, 77),
    (13, 1, 93),
    (14, 1, 84),
    (15, 1, 72),
    (16, 1, 91),
    (17, 1, 79),
    (18, 1, 86),
    (19, 1, 76),
    (20, 1, 94),
    (21, 1, 87),
    (22, 1, 73),
    (23, 1, 81),
    (24, 1, 69),
    (25, 1, 83),
    (26, 1, 74),
    (27, 1, 97),
    (28, 1, 96),
    (29, 1, 98),

    # grades for hist
    (1, 2, 78),
    (2, 2, 65),
    (3, 2, 88),
    (4, 2, 72),
    (5, 2, 82),
    (6, 2, 79),
    (7, 2, 90),
    (8, 2, 85),
    (9, 2, 94),
    (10, 2, 68),
    (11, 2, 89),
    (12, 2, 77),
    (13, 2, 93),
    (14, 2, 84),
    (15, 2, 73),
    (16, 2, 91),
    (17, 2, 76),
    (18, 2, 86),
    (19, 2, 75),
    (20, 2, 92),
    (21, 2, 87),
    (22, 2, 74),
    (23, 2, 80),
    (24, 2, 69),
    (25, 2, 83),
    (26, 2, 71),
    (27, 2, 95),
    (28, 2, 96),
    (29, 2, 98),

    # grades for Engl
    (1, 3, 80),
    (2, 3, 75),
    (3, 3, 90),
    (4, 3, 85),
    (5, 3, 92),
    (6, 3, 78),
    (7, 3, 88),
    (8, 3, 75),
    (9, 3, 90),
    (10, 3, 82),
    (11, 3, 95),
    (12, 3, 68),
    (13, 3, 89),
    (14, 3, 77),
    (15, 3, 93),
    (16, 3, 84),
    (17, 3, 72),
    (18, 3, 91),
    (19, 3, 79),
    (20, 3, 86),
    (21, 3, 76),
    (22, 3, 94),
    (23, 3, 87),
    (24, 3, 73),
    (25, 3, 81),
    (26, 3, 69),
    (27, 3, 83),
    (28, 3, 74),
    (29, 3, 97)
]

cur.executemany("INSERT INTO Grades_labka (StudentID, CourseID, Grade) VALUES (%s, %s, %s)", grades)

# Add GradeCategoryO column to Grades_labka table
# cur.execute("ALTER TABLE Grades_labka ADD GradeCategoryO VARCHAR(50)")

# Update GradeCategoryO values based on the Grade values
cur.execute("""
    UPDATE Grades_labka
    SET GradeCategoryO = 
        CASE 
            WHEN Grade > 90 THEN '5'
            WHEN Grade BETWEEN 70 AND 90 THEN '4'
            WHEN Grade BETWEEN 50 AND 70 THEN '3'
            ELSE '2'
        END
""")

# Commit the transaction
conn.commit()

# Retrieve the data from the databases
cur.execute("""
    SELECT Students_labka.FirstName, Students_labka.LastName, Courses_labka.CourseName, Grades_labka.Grade, Grades_labka.GradeCategoryO
    FROM Students_labka
    INNER JOIN Grades_labka ON Students_labka.StudentID = Grades_labka.StudentID
    INNER JOIN Courses_labka ON Grades_labka.CourseID = Courses_labka.CourseID
""")

rows = cur.fetchall()

# Display the retrieved data
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()