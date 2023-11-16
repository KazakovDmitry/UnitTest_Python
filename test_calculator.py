import pytest
from calculator import Calculator

# Создаем экземпляр калькулятора для тестов
@pytest.fixture
def calculator():
    return Calculator()

# Тестирование метода add
def test_add(calculator):
    result = calculator.add(5, 3)
    assert result == 8

# Тестирование метода subtract
def test_subtract(calculator):
    result = calculator.subtract(10, 4)
    assert result == 6

# Тестирование метода multiply
def test_multiply(calculator):
    result = calculator.multiply(3, 4)
    assert result == 12

# Тестирование метода divide
def test_divide(calculator):
    result = calculator.divide(10, 2)
    assert result == 5.0

# Тестирование деления на ноль
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError) as exc_info:
        calculator.divide(10, 0)
    assert str(exc_info.value) == "Деление на ноль недопустимо"