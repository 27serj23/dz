

--задание 3
--Описание:

--В базе данных должна:
--содержать информацию о доступных курсах, включая их названия, описания и продолжительность.
--хранить данные о студентах, которые записаны на курсы. Это включает в себя их идентификаторы, имена и электронные адреса.
--содержать информацию о преподавателях, которые ведут эти курсы. Каждый преподаватель имеет свой уникальный идентификатор и имя.


--10 запросов:

--1. Получить список всех курсов.
--2. Получить список студентов, записанных на определённый курс.
--3. Получить список всех преподавателей.
--4. Получить информацию о курсе по его названию.
--5. Получить список всех студентов.
--6. Получить список курсов, на которых учит конкретный преподаватель.
--7. Получить список курсов, продолжительность которых больше 20 часов.
--8. Получить список студентов с указанием их электронной почты.
--9. Получить информацию о преподавателе по его имени.
--10. Получить список студентов, записанных на курс по его идентификатору.



CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    description VARCHAR(100),
    duration_hours INT,
    teacher_id INT
);

INSERT INTO courses (course_id, course_name, description, duration_hours, teacher_id) VALUES
(1, 'Mathematics', 'Intro to Algebra', 40, 30),
(2, 'History', 'World History', 40, 25),
(3, 'Science', 'Biology Basics', 40, 20);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    email VARCHAR(50),
    course_id INT
);

INSERT INTO students (student_id, student_name, email, course_id) VALUES
(1, 'Alice', 'alice@example.com', 1234),
(2, 'Bob', 'bob@example.com', 5678),
(3, 'Cindy', 'cindy@example.com', 9999);

CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY,
    teacher_name VARCHAR(50),
);

INSERT INTO teachers (teacher_id, teacher_name) VALUES
(1,'John'),
(2,'Mary'),
(3,'Sam');


--1. Получить список всех курсов
 SELECT * FROM courses;
-- 2. Получить список студентов, записанных на определённый курс
SELECT student_name, students.email FROM students JOIN courses ON students.course_id = courses.course_id WHERE courses.course_name = 'Introduction to Computer Science';
--3. Получить список всех преподавателей
SELECT * FROM teachers;
--4.  Получить информацию о курсе по его названию
SELECT * FROM courses WHERE course_name = 'Mathematics';
--5. Получить список всех студентов
SELECT * FROM students;
--6.  Получить список курсов, на которых учит конкретный преподаватель
SELECT course_name, description FROM courses JOIN teachers ON courses.teacher_id = teachers.teacher_id WHERE teachers.teacher_name = 'Professor Smith';
--7.  Получить список курсов, продолжительность которых больше 20 часов
SELECT * FROM courses WHERE duration_hours > 20;
--8. Получить список студентов с указанием их электронной почты
SELECT student_name, email FROM students;
--9. Получить информацию о преподавателе по его имени
SELECT * FROM teachers WHERE teacher_name = 'John';
--10. Получить список студентов, записанных на курс по его идентификатору
SELECT student_name, email FROM students JOIN courses ON students.course_id = courses.course_id WHERE courses.course_id = 1234;






