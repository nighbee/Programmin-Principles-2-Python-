import csv
import psycopg2

# connect to database
conn = psycopg2.connect(database="lab3", user="postgres", password="72zv5u3xp")
cursor = conn.cursor()

 # A prob 1a query certain course
course_name = "Mathematics"  # Replace with the desired course name
query = f"SELECT * FROM students WHERE course = '{course_name}'"
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)

# prob 1b most jun and senior
query_senior = "SELECT * FROM students ORDER BY admission_year ASC LIMIT 1"
cursor.execute(query_senior)
senior_student = cursor.fetchone()
print("Most Senior Student:")
print(senior_student)

# Most junior student
query_junior = "SELECT * FROM students ORDER BY admission_year DESC LIMIT 1"
cursor.execute(query_junior)
junior_student = cursor.fetchone()
print("Most Junior Student:")
print(junior_student)

# prob 2c  replacing shit
student_id = 1  # Replace with the ID of the student you want to update
new_last_name = "Smith"  # Replace with the new last name

query_update = f"UPDATE students SET last_name = '{new_last_name}' WHERE id = {student_id}"
cursor.execute(query_update)
conn.commit()

#prob 2d multiply changes idk


# B prob 1:
'''CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50)
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course_name VARCHAR(50),
    teacher_id INTEGER REFERENCES teachers(id)
);
'''

query = """
    SELECT
        teachers.first_name AS teacher_first_name,
        teachers.last_name AS teacher_last_name,
        courses.course_name,
        COUNT(students.id) AS student_count
    FROM
        teachers
        INNER JOIN courses ON teachers.id = courses.teacher_id
        LEFT JOIN students ON students.course = courses.course_name
    GROUP BY
        teachers.id,
        courses.id;
"""

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    teacher_first_name, teacher_last_name, course_name, student_count = row
    print(f"Teacher: {teacher_first_name} {teacher_last_name}")
    print(f"Course: {course_name}")
    print(f"Student Count: {student_count}")
    print()

# C prob 1a: num of stud in each course
# query_a = """
#     SELECT courses.course_name, COUNT(students.id) AS student_count
#     FROM courses
#     LEFT JOIN students ON courses.id = students.course
#     GROUP BY courses.course_name;
# """
#
# cursor.execute(query_a)
# result_a = cursor.fetchall()

#
# # prob 1b :average age
# query_b = """
#     SELECT courses.course_name, AVG(students.age) AS average_age
#     FROM courses
#     LEFT JOIN students ON courses.id = students.course_id
#     GROUP BY courses.course_name;
# """
#
# cursor.execute(query_b)
# result_b = cursor.fetchall()
#
# # Output the results
# for row in result_b:
#     course_name, average_age = row
#     print(f"Course: {course_name}")
#     print(f"Average Age: {average_age}")
#     print()

# prob 2c: average score aboove the average:
query_c = """
    SELECT *
    FROM students
    WHERE average_score > (
        SELECT AVG(average_score)
        FROM students
    );
"""

cursor.execute(query_c)
result_c = cursor.fetchall()

# Output the results
for row in result_c:
    print(row)

# prob 2d not below 3:
query_d = """
    SELECT *
    FROM students
    WHERE NOT EXISTS (
        SELECT *
        FROM grades
        WHERE students.id = grades.student_id
        AND grade < 3
    );
"""

cursor.execute(query_d)
result_d = cursor.fetchall()

# Output the results
for row in result_d:
    print(row)

# D prob 1: report view
"""CREATE VIEW student_course_grades_view AS
SELECT
    students.id AS student_id,
    students.first_name,
    students.last_name,
    courses.id AS course_id,
    courses.course_name,
    grades.grade
FROM
    students
    INNER JOIN courses ON students.course_id = courses.id
    INNER JOIN grades ON students.id = grades.student_id;
    """