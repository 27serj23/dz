# задача
# Определите класс IDGenerator, который генерирует уникальные идентификаторы. Добавьте статический метод generate_id(), который возвращает строку с уникальным идентификатором. Идентификатор может, например, состоять из текущей даты и случайного числа.

# пример
# Использование IDGenerator
# id1 = IDGenerator.generate_id()
# id2 = IDGenerator.generate_id()

# print(f"Generated ID 1: {id1}")
# print(f"Generated ID 2: {id2}")

import datetime
import random


class IDGenerator:
    @staticmethod
    def generate_id():
        current_date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        random_number = str(random.randint(1000, 9999))
        return f"{current_date}_{random_number}"

id1 = IDGenerator.generate_id()
id2 = IDGenerator.generate_id()

print(f"Generated ID 1:{id1}")
print(f"Generated ID 2:{id2}")

