
#----------------------ЗАДАНИЕ ----------------------
# Выберете минимум 1 любую таблицу и напиши запрос на создание и добавление новых записей в таблицу через CLI(командный интерфейс строки(через консоль)) в питоне при помощи sqlite3
# 1. Создать таблицу "Студенты" с полями: Имя, Фамилия, Возраст, Группа.


import sqlite3 as sq

with sq.connect("students.db") as con:
    cur = con.cursor()

    # для исполнения запроса - создаете один раз в одном соедение
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Surname TEXT,
    Age INTEGER,
    Group_number TEXT
    )""")

# Добавляем новую запись в таблицу "Студенты"
cur.execute("INSERT INTO Students (Name, Surname, Age, Group_number) VALUES ('Иван', 'Иванов', 20, 'Группа 1')")
con.commit()

# Закрываем соединение с базой данных
con.close()