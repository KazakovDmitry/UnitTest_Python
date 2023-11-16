import pytest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# Тестирование методов класса Calculator
def test_calculator_add():
    calc = Calculator()
    result = calc.add(5, 3)
    assert result == 8

def test_calculator_subtract():
    calc = Calculator()
    result = calc.subtract(10, 4)
    assert result == 6
