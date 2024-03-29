
--Выберете минимум одно любое задание
--1.**Задание: Анализ продаж**

--У вас есть таблица `Sales`, содержащая информацию о продажах различных товаров в разных магазинах. Таблица имеет следующую структуру:

CREATE TABLE Sales (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    store_id INTEGER,
    sale_date DATE,
    quantity INTEGER,
    price REAL
);

INSERT INTO Sales (id, product_id, store_id, sale_date, quantity, price) VALUES
(1, 1, 1, '2022-01-01', 10, 15.99),
(2, 2, 1, '2022-01-02', 5, 20.50),
(3, 3, 2, '2022-01-03', 8, 12.75),
(4, 1, 2, '2022-01-04', 12, 15.99),
(5, 2, 3, '2022-01-05', 3, 20.50);

--Вам нужно выполнить любые 5 запросов:
--1. Найти общее количество проданных товаров за весь период.
--2. Рассчитать общую сумму выручки за весь период.
--3. Найти среднее количество проданных товаров в одной транзакции.
--4. Определить самый популярный товар (товар с наибольшим количеством продаж).
--5. Найти общее количество уникальных товаров, проданных в каждом магазине.
--6. Рассчитать общее количество продаж по месяцам.
--7. Найти месяц с наибольшим объемом продаж.
--8. Рассчитать общую сумму выручки и количество проданных товаров для каждого магазина.
--9. Определить магазин с наибольшим и наименьшим объемом продаж.
--10. Рассчитать средний чек (среднюю сумму покупки) в каждом магазине.
--11. Определить товары, проданные только в определенном магазине.

SELECT SUM(quantity) AS total_sold FROM Sales;

SELECT SUM(quantity * price) AS total_revenue FROM Sales;

SELECT AVG(quantity) AS avg_quantity_per_transaction FROM Sales;

SELECT product_id, SUM(quantity) AS total_quantity_sold
FROM Sales
GROUP BY product_id
ORDER BY total_quantity_sold DESC
LIMIT 1;

SELECT store_id, COUNT(DISTINCT product_id) AS unique_products_sold
FROM Sales
GROUP BY store_id;

SELECT strftime('%Y-%m', sale_date) AS month, SUM(quantity) AS total_sales
FROM Sales
GROUP BY month;

SELECT strftime('%Y-%m', sale_date) AS month, SUM(quantity) AS total_sales
FROM Sales
GROUP BY month
ORDER BY total_sales DESC
LIMIT 1;

SELECT store_id, SUM(quantity) AS total_quantity_sold, SUM(quantity * price) AS total_revenue
FROM Sales
GROUP BY store_id;

SELECT store_id, SUM(quantity) AS total_quantity_sold
FROM Sales
GROUP BY store_id
ORDER BY total_quantity_sold DESC
LIMIT 1;
SELECT store_id, SUM(quantity) AS total_quantity_sold
FROM Sales
GROUP BY store_id
ORDER BY total_quantity_sold ASC
LIMIT 1;

SELECT store_id, AVG(quantity * price) AS avg_transaction_amount
FROM Sales
GROUP BY store_id;

SELECT product_id
FROM Sales
WHERE store_id = 1
GROUP BY product_id
HAVING COUNT(DISTINCT store_id) = 1;

--2.**Задание: Анализ данных сотрудников**

--Создайте таблицу `Employees` со следующими столбцами:

-- `employee_id` - идентификатор сотрудника (уникальный ключ)
-- `department_id` - идентификатор отдела, к которому относится сотрудник
-- `employee_name` - имя сотрудника
-- `salary` - заработная плата сотрудника
-- `hire_date` - дата приема на работу

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    department_id INT,
    employee_name VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);

INSERT INTO Employees (employee_id, department_id, employee_name, salary, hire_date)
VALUES
(1, 101, 'John Smith', 50000, '2020-01-15'),
(2, 101, 'Jane Doe', 60000, '2019-03-20'),
(3, 102, 'Michael Johnson', 55000, '2020-05-10'),
(4, 103, 'Emily Davis', 52000, '2018-12-05');

--Вам нужно выполнить любые 5 запросов:

--1. Определить общее количество сотрудников в компании.
--2. Рассчитать среднюю заработную плату в компании.
--3. Определить количество сотрудников в каждом отделе.
--4. Найти самую высокооплачиваемую должность.
--5. Рассчитать общую сумму затрат на заработную плату для каждого отдела.
--6. Найти средний стаж работы сотрудников в компании.
--7. Определить месяц с наибольшим числом наймов сотрудников.
SELECT COUNT(employee_id) AS total_employees
FROM Employees;

SELECT AVG(salary) AS average_salary
FROM Employees;

SELECT department_id, COUNT(employee_id) AS employees_count
FROM Employees
GROUP BY department_id;

SELECT employee_name, MAX(salary) AS max_salary
FROM Employees;

SELECT department_id, SUM(salary) AS total_salary_expense
FROM Employees
GROUP BY department_id;



--2.**Задание: Анализ продуктов**

--Создайте таблицу `Products` со следующими столбцами:

-- `product_id` - идентификатор продукта (уникальный ключ)
-- `category_id` - идентификатор категории продукта
-- `product_name` - название продукта
-- `price` - цена продукта
-- `quantity` - количество продукта на складе
-- `date_added` - дата добавления продукта в ассортимент магазина

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    category_id INT,
    product_name VARCHAR(50),
    price DECIMAL(10,2),
    quantity INT,
    date_added DATE
);

INSERT INTO Products (product_id, category_id, product_name, price, quantity, date_added)
VALUES
(1, 1, 'Телевизор', 500, 10, '2022-01-01'),
(2, 1, 'Ноутбук', 800, 15, '2022-01-05'),
(3, 2, 'Холодильник', 700, 8, '2022-01-10'),
(4, 3, 'Фен', 50, 20, '2022-01-15'),
(5, 1, 'Смартфон', 300, 12, '2022-01-20');


--Вам нужно выполнить любые 5 запросов:

--1. Определить общее количество продуктов в магазине.
--2. Рассчитать среднюю цену продукта.
--3. Определить количество продуктов в каждой категории.
--4. Найти самый дорогой продукт.
--5. Рассчитать общее количество продуктов на складе.
--6. Найти среднее количество дней между добавлением продукта в ассортимент магазина и текущей датой.
--7. Определить месяц с наибольшим числом добавлений новых продуктов.

SELECT COUNT(*) FROM Products;

SELECT AVG(price) FROM Products;

SELECT category_id, COUNT(*) as category_count FROM Products GROUP BY category_id;

SELECT * FROM Products ORDER BY price DESC LIMIT 1;

SELECT SUM(quantity) FROM Products;

