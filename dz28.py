# -----ЗАДАНИЕ---------------------------------------------------#
# Дописать метод удаления и/или частичного поиска
# контакта (см. текст задания из классной работы)
# Задание из классной работы:
# Написать программу для управления списком контактов.
# В качестве примера, добавьте в программу два объекта
# Contact в список контактов
# Так же необходимо выполнить операции по удалению
# контакта и поиску контакта в списке (удаление и поиск осуществляется пользователем)
# Результаты операций должны выводятся на экран.
# Результат работы: py-файл

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone_number = phone

    def display_info(self):
        print(f"имя: {self.name}, номер телефона: {self.phone_number}")


class BusinessContact(Contact):
    def __init__(self, name, phone, company):
        super().__init__(name, phone)
        self.company = company

    def display_info(self):
        # super().display_info()
        # print(f"компания: {self.company}")
        print(f"имя: {self.name}, номер телефона: {self.phone_number}, компания: {self.company}")


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    # def remove_contact(self, contact):

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact.display_info()
        return None

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact.display_info()
            return None

    def display_contacts(self):
        for contact in self.contacts:
            contact.display_info()


phone_book = PhoneBook()

contact1 = Contact("Иван Иванов", "8-999-777-66-55")
business_contact = BusinessContact("Петров Петр", "8-666-555-44-33", "Рога и копыта")

phone_book.add_contact(contact1)
phone_book.add_contact(business_contact)

print("список всех контактов")
phone_book.display_contacts()

search_contact = input("ведите имя контакта для поиска по телефонной книге")
found_contact = phone_book.find_contact(search_contact)

if found_contact:
    print("найди контакт")
    found_contact.display_info()
else:
    print(f"контакт с запрашиваемым именем '{search_contact}' не найден")

delete_name = input("введите имя контакта для удаления:")
delete_contact = phone_book.find_contact(search_contact)
if delete_contact:
    print("удалить контакт")
    delete_contact.display_info()
else:
    print(f"контакт с запрашиваемым именем '{search_contact}' контакт удален")