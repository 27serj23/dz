
#-----------------Задача----------------------------------------#
# Создайте базовый класс "Сотрудник" с общими характеристиками
# (например, имя, зарплата).
# Затем создайте подклассы для различных типов сотрудников,
# таких как "Менеджер" и "Разработчик", добавляя уникальные свойства и
# методы для каждого типа.
# Реализуйте методы для подсчета общей зарплаты и вычисления премии.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus

class Developer(Employee):
    def __init__(self, name, salary, code_lang):
        super().__init__(name, salary)
        self.code_lang = code_lang

# экземпляры классов
employee1 = Employee("Сергей", 50000)
manager1 = Manager("Никита", 70000, 10000)
developer1 = Developer("Петр", 80000, "Python")

# подсчет зарплаты
total_salary = employee1.calculate_salary() + manager1.calculate_salary() + developer1.calculate_salary()
print("общая зарплата всех сотрудников", total_salary)

# вычисление премии для менеджера
manager_bonus = manager1.bonus
print("премия менеджера", manager_bonus)













