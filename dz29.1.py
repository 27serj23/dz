# 

#-----------------------Творческая Задача---------------------------------------#
# Выберете тему
# опишите требования к задаче
# напишите код (Обязательно должны быть использованы хотя бы 2 класса и
# они должны быть интегрированы в ваш код)

import datetime

#----------------------------Задача----------------------------------------------#
# создать систему для управления библиотекой.
# Вам нужно реализовать следующие классы: Book (Книга):
# Свойства: название, автор, год издания, жанр, количество экземпляров.
# Методы: вывод информации о книге, уменьшение/увеличение количества экземпляров.
# Library (Библиотека):
# Свойства: список книг, список пользователей.
# Методы: добавление/удаление книг, регистрация/удаление пользователя, выдача/возврат книги пользователю,
# вывод списка доступных книг.
# User (Пользователь):
# Свойства: имя, ID, список взятых книг.
# Методы: вывод информации о пользователе, взятие/возврат книги.
# Transaction (Транзакция):
# Свойства: дата, тип (выдача/возврат), книга, пользователь.
# Методы: запись транзакции, вывод информации о транзакции.
# Требования:
# Каждый класс должен иметь конструктор для инициализации объектов.
# Методы классов должны быть реализованы так, чтобы обеспечивать безопасность данных и взаимодействие между объектами.
# Классы должны взаимодействовать друг с другом в рамках системы управления библиотекой.
class Book:
    def __init__(self, title, author, year, genre, quantity):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.quantity = quantity

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}, Quantity: {self.quantity}")

    def increase_quantity(self, amount):
        self.quantity += amount
        print(f"Quantity increased by{amount}. New quantity:{self.quantity}")

    def decrease_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            print(f"Quantity decreased by{amount}. New quantity:{self.quantity}")
        else:
            print("Error: insufficient quantity")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("The book is not available")

    def register_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
        else:
            print("user was not found")

    def lend_book(self, book, user):
        if book in self.books:
            user.borrowed_books.append(book)
            self.books.remove(book)
        else:
            print("Book not available")

    def return_book(self, book, user):
        if book in user.borrowed_books:
            book.quantity(1)
            user.borrowed_books.remove(book)
        else:
            print("Book not borrowed by the user")

    def display_available_books(self):
        available_books = [book for book in self.books if book.quantity > 0]
        if available_books:
            for book in available_books:
                book.display_info()
        else:
            print("No available books at the moment.")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def __str__(self):
        return f"Name: {self.name}, ID:{self.user_id}, borrowed books:{','.join(self.borrowed_books)}"

    def borrow_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            return f"{self.name} took the book:{book}"
        else:
            return f"{self.name}I've already taken the book:{book}"

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            return f"{self.name}I didn't take such a book{book}"


class Transaction:
    def __init__(self, date, transaction_type, book, user):
        self.date = date
        self.transaction_type = transaction_type
        self.book = book
        self.user = user

    def __str__(self):
        print(f"Date: {self.date}, Type: {self.transaction_type}, Book {self.book.title}, User: {self.user.name}")


# Example usage
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, "Fantasy", 5)
print(book1)
book2 = Book("1984", "George Orwell", 1949, "Dystopian", 3)
print(book2)

book1.increase_quantity(5)
book1.decrease_quantity(3)

book2.increase_quantity(7)
book2.decrease_quantity(4)

library = Library()
library.add_book(book1)
library.add_book(book2)

user1 = User("Alice", "001")
user2 = User("Bob", "002")

library.register_user(user1)
library.register_user(user2)

library.lend_book("Harry Potter and the Philosopher's Stone", user1)
library.display_available_books()

library.return_book("Harry Potter and the Philosopher's Stone", user1)
library.display_available_books()

transaction1 = Transaction("01.01.2023", " issuance", "Harry Potter and the Philosopher's Stone",user1)
transaction2 = Transaction("10.01.2023", "refund", "1984", user1)

print(user1)
print(user2)

# Интерфейс управления системой
while True:
    choice = input("Enter your choice (0-5): ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter book year: ")
        genre = input("Enter book genre: ")
        quantity = int(input("Enter book quantity: "))

        book = Book(title, author, year, genre, quantity)
        library.add_book(book)
        print("Book added to library.")

    elif choice == "2":
        name = input("Enter user name: ")
        user_id = int(input("Enter user ID: "))

        user = User(name, user_id)
        library.register_user(user)
        print("User registered.")

    elif choice == "3":
        user_id = int(input("Enter user ID: "))
        book_title = input("Enter book title: ")

        user = next((user for user in library.users if user.user_id == user_id), None)
        book = next((book for book in library.books if book.title == book_title), None)

        if user and book:
            library.lend_book(book, user)
        else:
            print("User or book not found.")

    elif choice == "4":
        user_id = int(input("Enter user ID: "))
        book_title = input("Enter book title: ")

        user = next((user for user in library.users if user.user_id == user_id), None)
        book = next((book for book in library.books if book.title == book_title), None)

        if user and book:
            library.return_book(book, user)
        else:
            print("User or book not found.")

    elif choice == "5":
        library.display_available_books()

    elif choice == "0":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")











