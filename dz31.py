

#-----------------------задача----------------------------------------------#
# напиши тестовые сценарии для данной функции и протестируйте ее

from typing import List


def calculate_average(numbers: List[float]) -> float:
    """
    Вычисляет среднее значение списка чисел.

    :param numbers: Список чисел
    :return: Среднее значение
    """
    if not numbers:
        raise ValueError("Список чисел не должен быть пустым")

    return sum(numbers) / len(numbers)

# Код для тестирования:


print(calculate_average([1, 2, 3, 4, 5]))  # результат: 3.0
print(calculate_average([-1, -2, -3, -4, -5]))  # результат: -3.0
print(calculate_average([1, -2, 3, -4, 5]))  # результат: 0.6
try:
    calculate_average([])
except ValueError as e:
    print(str(e))  # результат: Списoк чисел не должен быть пустым
print(calculate_average([3]))  # результат: 3.0




