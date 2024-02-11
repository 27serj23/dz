#------------------Задача 5: Управление почтовым ящиком-----------------#
# Реализуйте класс EmailClient, представляющий почтовый клиент.
# Класс должен содержать метод send_email, отправляющий электронное письмо.
# Создайте собственный класс исключения InvalidEmailError, который будет возбуждаться,
# если адрес электронной почты не соответствует формату.

import re


class InvalidEmailError(Exception):
    pass


class EmailClient:
    def send_email(self, recipient, subject, body):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", recipient):
            raise InvalidEmailError("Invalid email address")

        # Отправка электронного письма
        print(f"Письмо отправлено на адрес {recipient}, тема: {subject}, текст: {body}")


# Пример использования
client = EmailClient()
try:
    client.send_email("example.com", "Тема письма", "Текст письма")
except InvalidEmailError as e:
    print(f"Ошибка отправки письма: {e}")
















