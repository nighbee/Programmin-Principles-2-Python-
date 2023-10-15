import csv
import psycopg2

# connect to database
conn = psycopg2.connect(database="ict", user="postgres", password="72zv5u3xp")
cur = conn.cursor()

# cur.execute("CREATE TABLE student_perfomance (id SERIAL PRIMARY KEY, student_id VARCHAR(20) NOT NULL, semester VARCHAR(20) NOT NULL, paper_num VARCHAR(50), marks INT)")

# while True:
#     f_name = input("enter fname(or leave a blank to skip")
#     if not f_name:
#         break
#     id = input("enter id ")
#     l_name = input("enter lName")
#     course = input("enter no course")
#     school = input("enter school")
#     gpa = input ("enter gpa")
#     cur.execute("INSERT INTO shit1(student_id, fname, lname, course, school, gpa) VALUES (%s, %s,%s,%s,%s,%s)",  (id , f_name, l_name, course , school, gpa))
# conn.commit()
#1a  prob 1: selecting certain course number
# num= "2"
#
# query = "SELECT * FROM shit1 WHERE course = %s"
# cur.execute(query, (num, ))
# rows = cur.fetchall()
# for row in rows:
#     print(row)

#1b prob 2 most junior and most senior
# senior= "SELECT * FROM shit1 ORDER BY course DESC LIMIT 1"
# cur.execute(senior)
# seniorStu= cur.fetchone()
#
# junior= "SELECT * FROM shit1 ORDER BY course ASC LIMIT 1"
# cur.execute(junior)
# junorStu = cur.fetchone()
#
# print("most senior: ")
# print(seniorStu)
#
# print ("most june: ")
# print (junorStu)

#prob 2 update shit
# fnameUPD= "ooo"
# updLname= "chlen "
# upd ="UPDATE shit1 SET lname = %s WHERE fname=%s"
# cur.execute(upd, (updLname, fnameUPD))
# conn.commit()
# test= "SELECT * FROM shit1"
# cur.execute(test)
# rows = cur.fetchall()
# for row in rows:
#     print(row)

#2b  shit

#3a linkin tables and creating
'''
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

CREATE TABLE Teachers (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);
'''
'''
inserting data 
INSERT INTO Teachers (first_name, last_name)
VALUES ('Michael', 'Brown'),
       ('Emily', 'Davis');

INSERT INTO Courses (course_name, teacher_id)
VALUES ('Mathematics', 1),
       ('English', 2);

INSERT INTO Students (first_name, last_name, age, course_id)
VALUES ('John', 'Doe', 20, 1),
       ('Jane', 'Smith', 22, 2),
       ('David', 'Johnson', 19, 1);
'''

#prob 3 avg avg of gpa
cur.execute("SELECT AVG(gpa) FROM shit1 ")
avgGpa= cur.fetchone()[0]
cur.execute("SELECT student_id , fname, lname, AVG(gpa) AS average_gpa FROM shit1 GROUP BY student_id ,fname, lname HAVING AVG(gpa) > %s", (avgGpa, ))
selectedStu= cur.fetchall()
for student in selectedStu:
    student_id, first_name, last_name, avg_gpa = student
    print(f"Student ID: {student_id}, Name: {first_name} {last_name}, Average GPA: {avg_gpa}")
conn.commit()