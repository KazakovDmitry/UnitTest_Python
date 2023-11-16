import unittest
#from calculator import Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль недопустимо")
    return a / b


class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        result = add(3, 4)
        self.assertEqual(result, 7)  # Проверка равенства с помощью assertEqual

    def test_subtraction(self):
        result = subtract(10, 5)
        self.assertNotEqual(result, 0)  # Проверка неравенства с помощью assertNotEqual

