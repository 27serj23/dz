


#-----------------------ЗАДАНИЕ -------------------------------------
# Выберете минимум 1 любую БД
# и напиши функции(описаны требования у каждой бд) для работы с БД
# через CLI(командный интерфейс строки(через консоль)) в питоне при помощи sqlite3
#1. Создать  БД “онлайн-магазина,”с таблицами users, orders, products(таблицы можно создать и не через питон) и требования:
#a. Пользователи могут регистрироваться, входить в систему и изменять свои данные.
#b. Администратор может добавлять, удалять и изменять информацию о продуктах.
#c. Пользователи могут просматривать каталог товаров, добавлять их в корзину и оформлять заказы.
#d. После оформления заказа пользователь должен получить подтверждение по электронной почте.
#e. Статус заказа должен автоматически изменяться в зависимости от его выполнения (например, "в обработке", "отправлен", "доставлен").

import sqlite3

# Создание соединения с базой данных
conn = sqlite3.connect('online_store.db')
cursor = conn.cursor()

# Создание таблицы users
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL,
                    role TEXT NOT NULL
                    )''')

# Создание таблицы orders
cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER,
                    order_status TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                    )''')

# Создание таблицы products
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT NOT NULL,
                    price REAL NOT NULL,
                    description TEXT
                    )''')

conn.commit()

# Функции для работы с базой данных через CLI
#1. Регистрация пользователя. Добавляет нового пользователя в базу данных.
def register_user(username, password, email, role):
    cursor.execute('''INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)''',
                   (username, password, email, role))
    conn.commit()
# 2. Вход пользователя. Проверяет наличие пользователя в базе данных по имени пользователя и паролю.
def login_user(username, password):
    cursor.execute('''SELECT * FROM users WHERE username=? AND password=?''', (username, password))
    user = cursor.fetchone()
    if user:
        return user
    else:
        return None

# 3. Изменение данных пользователя. Обновляет адрес электронной почты пользователя по его ID.
def update_user_data(user_id, new_email):
    cursor.execute('''UPDATE users SET email=? WHERE user_id=?''', (new_email, user_id))
    conn.commit()

# 4. Добавление информации о продукте. Добавляет новый продукт в базу данных.
def add_product(product_name, price, description):
    cursor.execute('''INSERT INTO products (product_name, price, description) VALUES (?, ?, ?)''',
                   (product_name, price, description))
    conn.commit()

# 5. Удаление продукта. Удаляет продукт из базы данных по его ID.
def delete_product(product_id):
    cursor.execute('''DELETE FROM products WHERE product_id=?''', (product_id,))
    conn.commit()

# 6. Изменение цены на продукт. Обновляет цену на продукт по его ID.
def update_product(product_id, new_price):
    cursor.execute('''UPDATE products SET price=? WHERE product_id=?''', (new_price, product_id))
    conn.commit()

# 7.Просмотр всех продуктов. Выводит на экран информацию о всех продуктах в базе данных.
def view_products():
    cursor.execute('''SELECT * FROM products''')
    products = cursor.fetchall()
    for product in products:
        print(product)

# 8. Добавление продукта в корзину. Добавляет продукт в заказ пользователя с указанием количества.
def add_to_cart(user_id, product_id, quantity):
    cursor.execute('''INSERT INTO orders (user_id, product_id, quantity, order_status) VALUES (?, ?, ?, ?)''',
                   (user_id, product_id, quantity, "в обработке"))
    conn.commit()

# 9. Оформление заказа. Изменяет статус заказа на "отправлен" и отправляет подтверждение на электронную почту пользователя.
def place_order(user_id):
    cursor.execute('''SELECT * FROM orders WHERE user_id=? AND order_status="в обработке"''', (user_id,))
    orders = cursor.fetchall()
    for order in orders:
        print("Заказ оформлен: ", order)
        # Отправить подтверждение по электронной почте
        cursor.execute('''UPDATE orders SET order_status="отправлен" WHERE order_id=?''', (order[0],))
        conn.commit()

# Пример использования функций
register_user("user1", "password1", "user1@email.com", "user")
add_product("product1", 100.0, "description1")
add_to_cart(1, 1, 3)
place_order(1)
view_products()

conn.close()












