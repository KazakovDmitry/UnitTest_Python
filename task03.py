import pytest

# Тестирование строк
def test_string_concatenation():
    str1 = "Hello"
    str2 = "World"
    result = str1 + " " + str2
    assert result == "Hello World"

# Тестирование списков
def test_list_append():
    my_list = [1, 2, 3]
    my_list.append(4)
    assert my_list == [1, 2, 3, 4]

# Тестирование чисел
def test_numeric_operations():
    a = 10
    b = 5
    assert a + b == 15
    assert a - b == 5
    assert a * b == 50
    assert a / b == 2.0

# Тестирование исключений
def test_exception_raised():
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0
