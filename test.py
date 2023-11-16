# Импортируем библиотеку pytest
import pytest

# Функция, которую мы хотим протестировать
def add(a, b):
    return a + b

# Напишем юнит-тест для функции add
def test_addition():
    result = add(2, 3)
    assert result == 5

def test_addition_not():
    result = add(2, 3)
    assert result != 7

# Запустим тест с помощью pytest
# Вы можете выполнить это в терминале PyCharm или через командную строку
# Просто выполните команду `pytest имя_вашего_файла.py`, где имя_вашего_файла.py - это имя вашего файла с тестами