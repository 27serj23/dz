#-----------------------задача----------------------#
# напиши тестовые сценарии для данной функции и протестируйте ее при помощи pytest
import pytest


def is_even(number: int) -> bool:
    """
    Проверяет, является ли число четным.

    :param number: Проверяемое число
    :return: True, если число четное, иначе False
    """
    return number % 2 == 0

# тест


def test_even_number():
    assert is_even(2) == True
    assert is_even(4) == True
    assert is_even(6) == True


def test_odd_number():
    assert is_even(3) == False
    assert is_even(5) == False
    assert is_even(7) == False


def test_negative_number():
    assert is_even(-2) == True
    assert is_even(-4) == True
    assert is_even(-6) == True


def test_zero():
    assert is_even(0) == True


def test_one():
    assert is_even(1) == False


# Run tests
pytest.main(['-sv'])