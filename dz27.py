
#------------------------------------Задача ---------------------------------------------
# Создайте класс Book,
# представляющий книгу.
# Реализуйте магические методы сравнения (==, !=, <, >, <=, >=)
# на основе сравнения года издания книги.
# Книги сравниваются по году издания.

class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __lt__(self, other):
        return self.year < other.year

    def __gt__(self, other):
        return self.year > other.year

    def __le__(self, other):
        return self.year <= other.year

    def __ge__(self, other):
        return self.year >= other.year

# Пример использования:
book1 = Book('The Great Gatsby', 1925)
book2 = Book('To Kill a Mockingbird', 1960)

print(book1 == book2)  # False
print(book1 != book2)  # True
print(book1 < book2)   # True
print(book1 > book2)   # False
print(book1 <= book2)  # True
print(book1 >= book2)  # False





